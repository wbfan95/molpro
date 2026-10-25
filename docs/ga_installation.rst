.. _ga_installation--ga-installation:

GA Installation
===============

We recommend building Molpro with the `Global Arrays toolkit <https://github.com/GlobalArrays/ga>`__, using the latest stable version.

There are different ways (GA "runtimes") to configure the GA library which significantly affect the execution and options, and they are therefore important from a users point of view.
The current default of the GA installation is to use ``--with-mpi-ts``, which is **very slow** and should be avoided.
Our current recommendation is to use ``--with-mpi-pr``, preferably using the latest version of openmpi with UCX.

Note that openmpi may not work with ``--ga-impl disk`` when multiple parallel Molpro calculations are executed simultaneously on a node.

If a job scheduler is used, please also check the manual of the job scheduler for special instructions on how to run MPI programs.
For example, using openmpi under slurm requires the proper configuration of the `MpiDefault option <https://slurm.schedmd.com/mpi_guide.html#open_mpi>`__.
*Failure in doing so may result crashes or incorrect computation results.*

Older GA runtimes do not need any helper processes, but have a serious disadvantage that with ``--ga-impl ga`` (the default for multi-node calculations since Molpro 2021.2 and for all calculations in earlier versions), the GA software frequently crashes or gives wrong numbers if several GAs are allocated whose total size exceeds 16 GB (2 MW). This can be avoided by using ``--ga-impl disk`` (default for single-node calculations since Molpro 2021.2), or allocating in the beginning of the job a very large GA with at least the size of the total GA space needed in the calculation (which is not known in advance). The latter can be done with the ``-G`` or ``-M`` molpro options.
See :doc:`Running Molpro on parallel computers <running_molpro_on_parallel_computers>` for more details.

The ``mpi-pr`` runtime requires one helper process from each node. Thus, if for example ``-n40`` is specified as molpro options in a 2-node calculation, only 38 MPI processes run molpro, and 2 additional helper processes are started. The performance of ``mpi-pr`` runtime is usually comparable to the ``socket`` or ``openib`` runtims. GA preallocation is not needed and automatically disabled by Molpro with the ``mpi-pr`` runtime.

The ``socket`` and ``openib`` GA runtimes uses System V shared memory while the ``mpi-pr`` runtime uses POSIX shared memory. In the former case you may need to raise the value of ``SHMMAX`` and ``SHMALL`` kernel parameters, while in the latter case to raise the size-limit of ``/dev/shm``. Also note that even in successful calculations shared memory segments are sometimes left in ``/dev/shm``. These can accumulate to make a machine unusable, and should therefore be deleted from time to time.

Queries regarding Global Arrays installations should be sent directly to the Global Arrays team, any Molpro related queries will assume a fully functional Global Arrays suite with all internal tests run successfully.
