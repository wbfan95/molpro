.. raw:: html

   <span id="disk-option"></span>

.. raw:: html

   <span id="ga-installation-notes"></span>

.. raw:: html

   <span id="memory-specifications"></span>

.. raw:: html

   <span id="notes-on-the-disk-option"></span>

.. raw:: html

   <span id="specifying-parallel-execution"></span>

.. _running_molpro_on_parallel_computers--running-molpro-on-parallel-computers:

Running Molpro on parallel computers
====================================

Molpro will run on distributed-memory multiprocessor systems, including workstation clusters, under the control of the `Global Arrays <http://www.emsl.pnl.gov/docs/global>`__ parallel toolkit or the MPI-2 library. There are also some parts of the code that can take advantage of shared memory parallelism through the `OpenMP <http://www.openmp.org>`__ protocol, although these are somewhat limited, and this facility is not at present recommended. It should be noted that there remain some parts of the code that are not, or only partly, parallelized, and therefore run with replicated work. Additionally, some of those parts which have been parallelized rely on fast inter-node communications, and can be very inefficient across ordinary networks. Therefore some caution and experimentation is needed to avoid waste of resources in a multiuser environment.

Molpro effects interprocess cooperation through MPI and the *ppidd* library, which, depending on how it was configured and built, draws on either the `GlobalArrays <http://www.emsl.pnl.gov/docs/global>`__ (GA) parallel toolkit or pure MPI. *ppidd* is described in `Comp. Phys. Commun. 180, 2673-2679 (2009) <http://dx.doi.org/10.1016/j.cpc.2009.05.002>`__.
The use of GlobalArrays (GAs) is recommended for performances considerations.
There are different GA implementation options (runtimes), and there are advantages and disadvantages for using one or the other implementation (see :doc:`GA Installation <ga_installation>`).

**Since Molpro 2021.2 the `#disk option <running_molpro_on_parallel_computers.html#disk-option>`__ is used by default** in single node calculation, in which case large data structures are simply kept in MPI files.
The behavior of previous versions can be recovered by the ``--ga-impl ga`` command line option.
However, ``--ga-impl ga`` requires pre-allocation of GA memory in many calculations if the ``socket`` GA runtime is used, and failing to preallocate sufficient amount of GA memory may lead to crashes or incorrect results.
Preallocating GA is not required with the ``mpi-pr`` runtime of GA or with the disk option.

Programs that use density fitting (e.g. df-hf, df-ks, df-multi, df-mp2) as well as pno Programs (pno-[lru]ccsd(t)[-F12\|) can run on multiple computer nodes. However, a fast interconnect (e.g. Infiniband) is necessary to get reasonable performance. For most other methods, in particular conventional methods that use integrals stored on disk, multi-node calculations are disabled, since no performance gain can be expected and memory requirements could be exceedingly large.

.. _running_molpro_on_parallel_computers--ga-installation-notes:

GA Installation notes
=====================

See :doc:`GA installation <ga_installation>`.

.. _running_molpro_on_parallel_computers--specifying-parallel-execution:

Specifying parallel execution
=============================

The following additional options for the ``molpro`` command may be used to specify and control parallel execution. In addition, appropriate memory specifications (``-m, -M, -G``) are important, see section `memory specifications <running_molpro_on_parallel_computers.html#memory-specifications>`__.

* **``-n`` :math:`|` ``--tasks`` *tasks*** specifies the number of parallel processes to be set up, and defaults to 1.
* **``-N`` :math:`|` ``--task-specification`` *node1:tasks1,node2:tasks2:math:`\dots`*** *node1, node2* etc. specify the host names of the nodes on which to run. *tasks1, tasks2* etc. specify the number of tasks on each node
* **``--ga-impl`` *method*** specifies the method by which large data structure are held in parallel. Available options are ``GA`` (GlobalArrays, default) or ``disk`` (MPI Files, see `#disk option <running_molpro_on_parallel_computers.html#disk-option>`__). This option is most relevant on the more recent programs such as Hartree-Fock, DFT, MCSCF/CASSCF, and the PNO programs.
* **``-D`` :math:`|` ``--global-scratch`` *directory*** specifies the scratch directory for the program which is accessible by all processors in multi-node calculations. This only affects parallel calculations with the `disk option <running_molpro_on_parallel_computers.html#disk-option>`__.
* ``--all-outputs`` produces an output file for each process when running in parallel.

.. _running_molpro_on_parallel_computers--memory-specifications:

Memory specifications
=====================

Large scale parallel Molpro calculations may involve significant amount of global data structure.
This concerns in particular :doc:`PNO-LCCSD <local_correlation_methods_with_pair_natural_orbitals_pnos>` calculations, and, to a lesser extent, also Hartree-Fock, DFT, and MCSCF/CASSCF calculations.
For these calculations, it may be necessary to share the available memory of the machine between molpro "stack" memory (determined by the ``-m`` command line option or the ``memory`` card in the input file) and the GA memory (determined by the ``-G`` command line option):

- If the `#disk option <running_molpro_on_parallel_computers.html#disk-option>`__ is disabled (the default) and one of the older GA runtimes (``sockets``, ``openib``, etc.) is used: Sufficient amount of GA memory must be specified by the ``-G`` or ``-M`` option (see below) and pre-allocated by Molpro in the beginning of a calculation, otherwise the calculation may crash or yields incorrect results.
- If the disk option is disabled and one of the comex-based GA runtimes (e.g. ``mpi-pr``) is used, or if the disk option is enabled but the scratch is in a tmpfs: the ``-G`` or ``-M`` option is not mandatory, but sufficient physical memory shall be left for the global data structure.
- If the `#disk option <running_molpro_on_parallel_computers.html#disk-option>`__ is enabled and the scratch directory is located on a physical disk: the GA usage should be negligible and the **``-G`` or ``-M`` options should not be given**. However, the performance of the calculation might be better if some memory is left for the system to buffer the I/O.

Note that we have made the disk option the default in single node calculations since Molpro 2021.2. If this causes performance problems, the previous behavior of storing large data structure in GlobalArrays can be enabled by setting the environment variable ``MOLPRO_GA_IMPL`` to ``GA``, or by passing the ``--ga-impl ga`` command-line option.

Both the ``-m`` and ``-G`` options are by default given in megawords (m) but unit gigaword (g) can also be used (e.g. ``-m1000`` is equivalent to ``-m1000m`` and to ``-m1g``).
The total memory :math:`M` per node allocated by molpro amounts to :math:`(n \cdot m+G)/N`, where :math:`n` is the total number of processes (``-n`` option), :math:`m` is the stack memory per process (``-m`` option), :math:`G` the GA memory (``-G`` option), and :math:`N` the number of nodes.
In addition, at least 200 MW per process should be added for the program itself.
In total, a calculation needs about :math:`8\cdot[n\cdot(m+0.3)+G]/N` GB (gigabytes) of memory (:math:`n,m,G` in gw), and this should not exceed the physical memory of the machine(s) used.
We do note that in many calculations leaving some memory for the system to buffer I/O operations may improve the performance significantly.

A proper ratio for the splitting between "stack" and GA memory depends on the calculation and the system.
Some experiments are usually required to obtain optimal performance.
As a rule of thumb, the following choice can be used as a starting point:

* **Density fitting and PNO calculations**: divide the memory into equal parts for GA and stack memory.
* **HF, DFT, and MCSCF calculations**: 75% for the stack and 25% for GA.
* **Canonical MRCI or CCSD(T) calculations** on one-node: no GA space is needed.

In order to facilitate the memory splitting, the ``-M`` option is provided (in the following, its value is denoted :math:`M`).
With this, the total memory allocatable by Molpro can be specified, and the memory is split 50-50 for stack and GA in DF/PNO calculations, and 75-25 in other calculations.
Thus, unless specified otherwise, in DF/PNO calculations the stack memory per process is :math:`m=M\cdot N/(2\cdot n)` and the total GA memory is :math:`G=N\cdot M/2`.
If the use of GA in storing large data structure is desired, it is recommended to provide a default ``-M`` value in .molprorc (**do not do so for disk-based calculation, see `#disk option <running_molpro_on_parallel_computers.html#disk-option>`__**), e.g. ``-M=25g`` for a dedicated machine with 256 GB of memory and 20 cores (.molprorc can be in the home directory and/or in the submission directory, the latter having preference). Then each Molpro run would be able to use the whole memory of the machine with reasonable splitting between stack and GA. The default can be overwritten or modified by molpro command line options ``-m`` and/or ``-G``, or by input options (cf. section `memory allocation <general_program_structure.html#memory-allocation>`__), the latter having preference over command line options.

Depending on the GA run time and the MPI library, the error messages from GA allocation failures (with ``--ga-impl ga``) can be very deceptive.
In our tests with OpenMPI and the ``mpi-pr`` GA runtime, such allocation failures usually show up as "Bus error", but sometimes no errors are shown at all.

If the ``-G`` or ``-M`` options are given, some programs check at early stages if the GA space is sufficient. If not, an error exit occurs and the estimated amount of required GA is printed. In this case the calculation should be repeated, specifying (at least) the printed amount of GA space with the ``-G`` option. If crashes without such message occur, the calculation should also be repeated with more GA space or with the disk option, but care should be taken that the total memory per node does not get too large.

The behavior of various option combinations is as follows:

* ``-M`` As described above.
* **``-M`` and ``-m``** The specified amount :math:`m` is allocated for each core, the remaining memory for GA.
* **``-M`` and ``-G``** The specified amount :math:`G` is allocated for GA, and the remaining amount is split equally for stack memory of each process.
* **``-M`` and ``-G`` and ``-m``** The specified amounts of :math:`m` and :math:`G` are allocated, and the :math:`M` value is ignored.
* **``-G`` and ``-m``** The specified amounts of :math:`m` and :math:`G` are allocated.
* ``-m`` The specified amount of :math:`m` is allocated. An infinite amount of GA space is assumed, but nothing is preallocated or checked.
* ``-G`` The specified amount of :math:`G` is allocated, and the same total amount for stack memory (i.e. :math:`M=2G`).
* ``nothing`` Same as -m32m.

If the ``-G`` or ``-M`` are present, the GA space is preallocated unless GA is using helper processes (i.e., a comix-based runtime is used and preallocation of GA is not necessary).
If neither ``-G`` nor ``-M`` are given, no preallocation and no checks of GA space are performed.

.. _running_molpro_on_parallel_computers--disk-option:

Disk option
===========

Since version 2021.1, Molpro can use MPI files instead of GlobalArrays to store large global data. This option can be enabled globally by setting the environment variable ``MOLPRO_GA_IMPL`` to ``DISK``, or by passing the ``--ga-impl disk`` command-line option.
Since version 2021.2 the disk option is made the default in single-node calculations.
Some programs in Molpro including DF-HF, DF-KS, (DF-)MULTI, DF-TDDFT, and PNO-LCCSD also support an input option ``implementation=disk`` to enable the disk option for the particular job step.
The file system for these MPI files must be accessible by all processors.
By default the default Molpro scratch directory is used, but another directory can be chosen for MPI Files using the ``-D`` command line option or the ``MOLPRO_GLOBAL_SCRATCH`` environment variable.
The directory can be tmpfs (e.g., ``-D /dev/shm``) in single-node calculations, and in this case the GAs / MPI Files are kept in shared memory.

With the disk option the problems associated with GA pre-allocation are avoided. In this case
use only ``-m`` or the ``memory`` card to specify Molpro scratch memory for each processor. To avoid GA preallocation **do not provide ``-M`` or ``-G``**.
Please also make sure that ``-M`` and ``-G`` are not present in ``.molprorc``, etc.

The performance of the disk option varies depending on the I/O capacity, available system memory, the MPI software, and the nature of the calculation.
Usually, the best practice is to reserve some system memory for the system to buffer I/O operations (i.e., not to allocate all available memory to Molpro with ``-m`` or the ``memory`` input card).
When this is done the performance of single-node disk-based calculations can be comparable to GA-based ones in many cases, in particular with SSDs.

.. _running_molpro_on_parallel_computers--embarrassing-parallel-computation-of-gradients-or-hessians-mppx-mode:

Embarrassing parallel computation of gradients or Hessians (mppx mode)
======================================================================

The numerical computation of gradients or Hessians, or the automatic generation of potential energy surfaces, requires many similar calculations at different (displaced) geometries. An automatic parallel computation of the energy and/or gradients at different geometries is implemented for the gradient, hessian, and surf programs. In this so-called mppx-mode, each processing core runs an independent calculation in serial mode. This happens automatically using the ``-n`` available cores. The automatic mppx processing can be switched off by setting option ``mppx=0`` on the ``OPTG``, ``FREQ``, or ``HESSIAN`` command lines. In this case, the program will process each displacement in the standard parallel mode.

.. _running_molpro_on_parallel_computers--options-for-developers:

Options for developers
======================

.. _running_molpro_on_parallel_computers--debugging-options:

Debugging options
=================

* ``--ga-debug`` activates GA debugging statements.
* ``--check-collective`` check collective operations when debugging.

.. _running_molpro_on_parallel_computers--options-for-pure-mpi-based-ppidd-build:

Options for pure MPI-based PPIDD build
======================================

This section is **not** applicable if the Molpro binary release is used, or when Molpro is built using the GlobalArrays toolkit (which we recommend).

In the case of the pure MPI implementation of PPIDD, there is a choice of using either MPI-2 one-sided memory access, or devoting some of the processes to act as data "helpers". It is generally found that performance is significantly better if at least one dedicated helper is used, and in some cases it is advisable to specify more. The scalable limit is to devote one core on each node in a typical multi-core cluster machine, but in most cases it is possible to manage with fewer, thereby making more cores available for computation. The options below

* **``--multiple-helper-server`` *nprocs_per_server*** enables the multiple helper servers, and *nprocs_per_server* sets how many processes own one helper server. For example, when total number of processes is specified as :math:`32` and :math:`nprocs\_per\_server=8`, then every :math:`8` processes(including helper server) will own one helper server, and there are :math:`4` helper servers in total. For any unreasonable value of :math:`nprocs\_per\_server` (i.e., any integer less than 2), it will be reset to a very large number automatically, and this will be equivalent to option ``--single-helper-server``.
* ``--node-helper-server`` specifies one helper server on every node if all the nodes are symmetric and have reasonable processes (i.e., every node has the same number of processes, and the number should be greater than 1), and this is the default behaviour. Otherwise, only one single helper server for all processes/nodes will be used, and this will be equivalent to option ``--single-helper-server``
* ``--single-helper-server`` specifies only one single helper server for all processes.
* ``--no-helper-server`` disables the helper server.

In the cases of one or more helper servers enabled, one or more processes act as data helper servers, and the rest processes are used for computation. Even so, it is quite competitive in performance when it is run with a large number of processes. In the case of helper server disabled, all processes are used for computation; however, the performance may not be good because of the poor performance of some existing implementations of the MPI-2 standard for one-sided operations.
