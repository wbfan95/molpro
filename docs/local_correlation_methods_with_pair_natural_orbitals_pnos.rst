.. raw:: html

   <span id="advanced-options"></span>

.. raw:: html

   <span id="bibliography"></span>

.. raw:: html

   <span id="correlation-regions-in-the-pno-program"></span>

.. raw:: html

   <span id="correlation-regions-in-the-pno-program-region"></span>

.. raw:: html

   <span id="default-and-tight-settings"></span>

.. raw:: html

   <span id="getting-started"></span>

.. raw:: html

   <span id="options"></span>

.. raw:: html

   <span id="options-for-f12-calculations"></span>

.. raw:: html

   <span id="options-for-intermolecular-interactions"></span>

.. raw:: html

   <span id="options-for-job-execution"></span>

.. raw:: html

   <span id="options-for-pao-osv-pno-generation"></span>

.. raw:: html

   <span id="restarting-t"></span>

.. raw:: html

   <span id="versions"></span>

.. _local_correlation_methods_with_pair_natural_orbitals_pnos--local-correlation-methods-with-pair-natural-orbitals-pnos:

Local correlation methods with pair natural orbitals (PNOs)
===========================================================

In this page single-reference local correlation methods using pair natural orbitals (PNOs) are described.
This program is entirely distinct from the older :doc:`PAO-based methods <pao-based_local_correlation_treatments>`.
It is designed for parallel execution both on one node and across multiple nodes. By default, the program store some data in distributed memory, which means more memory is required than in other programs. The memory required per CPU core for these distributed data is approximately inversely linear in the number of cores used. Therefore, it is normally not recommended using these programs on a single core. Depending on the molecular size, parallelization works well with up to 100-300 cores using multiple nodes, provided that a fast network (Infiniband or similar) is available. Calculations can also be performed with reasonable efficiency on one node using disk storage instead of distributed memory when fast SSDs are used for scratch.

The methods can be executed with or without explicitly correlated (F12) terms. It is strongly recommended always to include F12, since this does not only reduce the basis set errors, but also the domain errors.

Appropriate default values are set which normally yield results that are close to the canonical ones. In particular, sub-kJ/mol accuracy of relative energies is usually achieved with PNO-LMP2-F12 (relative to MP2-F12), and sub-kcal/mol accuracy for PNO-LCCSD(T)-F12 relative to CCSD(T)-F12.

We strongly recommend that the user reads the review `WIREs Comput. Mol. Sci. <https://doi.org/10.1002/wcms.1371>`__ **8**, e1371 (2018) for the concepts and local approximations used in the PNO program.
More details on the PNO methods can be found in `#bibliography <local_correlation_methods_with_pair_natural_orbitals_pnos.html#bibliography>`__.
We kindly ask you to cite our original publications on the corresponding methods in publications resulting from this program.
**Please read the important notes in `#getting started <local_correlation_methods_with_pair_natural_orbitals_pnos.html#getting-started>`__ before attempting a PNO calculation!**

.. _local_correlation_methods_with_pair_natural_orbitals_pnos--getting-started:

Getting started
===============

The program can be invoked using one of the following commands:

* **``PNO-LMP2-F12``, *options*** runs a second order Møller Plesset perturbation theory calculation.
* **``PNO-LCCSD-F12``, *options*** runs a local coupled cluster calculation with single and double excitations.
* **``PNO-LCCSD(T)-F12``, *options*** runs a local coupled cluster calculation with single, double, and perturbative triple excitations. ``(T)`` can be replaced by ``(T0)`` or ``(T1)`` for reduced cost.
* **``PNO-LDCSD-F12``, *options*** runs a distinguishable cluster calculation with single and double excitations.

Available options are described `below <local_correlation_methods_with_pair_natural_orbitals_pnos.html#options>`__.
``F12 in the above commands can be omitted for calculations without explicit correlation.``
For coupled-cluster calculations the F12 variants are strongly recommended due to the significantly improved accuracy and very little added cost.
The PNO program uses a different *Ansatz* from the default one in the `canonical program <explicitly_correlated_methods.html#ccsd-t-f12>`__, and we recommend using the more rigorous F12b approximation instead of F12a for all basis sets.

For Open-shell molecules (supported since Molpro 2020.1), LMP2 calculations use the spin adapted theory described in `J. Chem. Theory Comput. <https://doi.org/10.1021/acs.jctc.8b01012>`__ **15**, 987 (2019), and coupled cluster and distinguishable cluster calculations use the partially spin-restricted theory (similar to the canonical ``RCCSD`` in Molpro) by default.
The command ``PNO-RCCSD`` is equivalent to to ``PNO-LCCSD``.
Spin-unrestricted CC or DC calculations can be performed using, for example, ``PNO-UCCSD``.
Calculations on close-shell molecules will use the compatible spin-free theories when the ``PNO-RCCSD`` or ``PNO-UCCSD`` command is given.

**It is important to check the following before attempting a PNO calculation:**

* Depending on the GA runtime, Larger PNO calculations may **require pre-allocating GA memory** (shared or distributed memory). Please read `memory specifications <running_molpro_on_parallel_computers.html#memory-specifications>`__ for details. In single node calculations the `disk option <local_correlation_methods_with_pair_natural_orbitals_pnos.html#options-for-job-execution>`__ can be considered.
* Multi-node calculation over InfiniBand requires compiling Molpro from the source code. Please refer to :doc:`GA Installation <ga_installation>` when doing so.
* New releases may include some improvements that break backward compatibility. Please check :doc:`recent changes <recent_changes>` when upgrading. In particular, a new PNO-LCCSD program has been developed for Molpro 2020.1 and the results are **not compatible with Molpro 2019.2 or earlier** by default (see `#versions <local_correlation_methods_with_pair_natural_orbitals_pnos.html#versions>`__ for more details).

The PNO program requires a preceding Hartree–Fock calculation, and for the F12 varieties the CABS singles correction should be included. The Hartree–Fock calculation can be performed with the density-fitted HF program (``DF-HF``) or a well-parallelized local variety of it (``LDF-HF``). If a canonical F12 calculation is done before the PNO calculation, the CABS singles correction is computed by default and is stored in Molpro variable EF12_RHFRELAX and (from Molpro 2025.1) in the orbital dump record. If the correction is available it will be added automatically added to the PNO energies. The correction is remembered across restarts. However, it is cleared whenever a new Hartree-Fock calculation is done. If variable EF12_RHFRELAX is zero or not set, the CABS singles correction can be computed in the PNO program by setting the option ``CABS_SINGLES=1`` (this is possible only in closed-shell cases). Also in this case EF12_RHFRELAX is set and remembered across restarts, so that in a restarted calculation the CABS correction needs not to be computed again.

A typical input including CABS singles correction is

.. code-block:: text

   geometry=...
   basis=...
   df-hf
   pno-lccsd(t)-f12,cabs_singles=1     !energies will automatically include the cabs correction

**\*\* Note:** Computations of the cabs correction are not well suited for multi-node calculations (``but see below for Molpro version 2025.3 and later``). They may become slow and require too much GA space. It may therefore be advantageous to carry out these calculations separately on a single node. This can be done with

.. code-block:: text

   file,2,name.wfu
   geometry=...
   basis=...
   df-hf
   df-cabs

In this case the CABS correction is computed and available after a restart. Note that the calculation of the cabs correction on a single node may require a lot of memory (in particular for open-shell) but less GA than a PNO calculation. It is therefore generally recommended to compute the cabs correction in a separate calculation. See also below regarding OPTRI basis sets.

``However, from Molpro 2025.3 and later, the CABS program has been improved and also runs efficiently in parallel on multiple nodes. It is therefore computed automatically in the PNO program (only with F12)  unless already available. In order to save computation time, a slightly simplified method for computing the CABS basis is used (ORTHO_CABS=0). Extensive tests have shown that this has only a negligible effect on relative energies. However, it is possible to set PNO option ORTHO_CABS=1 in order to generate the CABS correction exactly as with DF-CABS (which uses  ORTHO_CABS=1 by default). Furthermore, one can use PNO option CABS_SINGLES=0 to disable the automatic computation of the CABS correction or CABS_SINGLES=2 to force recalculating it even if it is already available.``

By default, the program uses as RI basis the JKFIT basis corresponding to the orbital basis set. It is strongly recommended to use orbital basis sets that include diffuse functions, e.g. aug-cc-pVTZ or cc-pVTZ-F12 (diffuse functions can be omitted on hydrogen atoms). The cc-pVnZ-F12 basis sets (short names: vnz-f12) [see `J. Chem. Phys. <https://dx.doi.org/10.1063/1.2831537>`__ **128**, 084102 (2008), `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3308483>`__ **132**, 054108 (2010), `Phys. Chem. Chem. Phys. <https://dx.doi.org/10.1039/C0CP00020E>`__ **12**, 10460 (2010)] are particularly well suited. Furthermore, the RI basis should at least have triple-zeta quality, if JKFIT sets are used for this purpose. Errors of several kcal/mol in relative energies can occur if e.g. ``ri_basis=vdz`` is used. Thus, with a double-zeta orbital basis, the RI-basis should be specified using the ``ri_basis`` option, e.g.:

.. code-block:: text

   geometry=...
   basis={
   default=vdz-f12
   set,jkfit,context=jkfit
   default,avtz
   set,mp2fit,context=mp2fit
   default,avdz
   set,ri,context=jkfit
   default,avtz
   }
   explicit,ri_basis=ri,df_basis=mp2fit,df_basis_exch=jkfit
   
   df-hf,basis=jkfit            !Hartree-Fock using the JKFIT density fitting basis
   df-cabs                      !compute cabs correction (Molpro2020.3 or newer; not needed with Molpro 2025.3 or newer, see above)
   pno-lccsd(t)-f12             !the cabs correction is included automatically.

Both F12 calculations use the basis sets specified on the explicit directive, which must be given before the first F12 calculation in the input. Note that specifications on an ``explicit`` directive are not remembered in restarts and must therefore be given again after a restart.

An alternative, usually somewhat more expensive choice is to use the optimized RI basis sets of Peterson et al. (see `J. Chem. Phys. <https://dx.doi.org/10.1063/1.4893989>`__ **141**, 094106 (2014) and references therein). In this case the RI basis is generated as then union of the orbital basis and the optri basis. In Molpro, this is done automatically by specifying, e.g. ``vdz-f12/cabs``.

.. code-block:: text

   basis={
   ...
   set,ri
   default,vdz-f12/cabs
   }

**Warning: Do not define the RI basis for PNO calculation with the `context <basis_input.html#auxiliary-basis-sets-for-density-fitting-or-resolution-of-the-identity>`__ ``optri``.**
This will lead to very large errors.
The ``cabs`` context should be used instead. If such cabs RI basis sets are used, the cabs-singles correction should not be computed within the PNO program, but beforehand using df-mp2-f12,cabs_singles=-1 (see above). The latter method can use the proper CABS approach, with is numerically more stable.

Local coupled cluster calculations on large molecules require a significant amount of memory. The memory requirements of the PNO program consist of two parts:

* *Local memory*: the memory for each CPU core allocated using the ``memory`` card in the input file or the -m option on the molpro command line. This is primarily used for scratch storage of data, and the usage per core is roughly invariant with the number of cores.
* *Distributed memory*: the memory used to store large data structure that are shared by all processors. The usage per core is roughly inversely linear in the number of cores. By default it is implemented with the ``globalarrays`` (GA) toolkit, but it is also possible to use disk storage (with the ``implementation=disk`` option) when the program is executed on one node.

Some typical memory usage can be found in `WIREs Comput. Mol. Sci. <https://doi.org/10.1002/wcms.1371>`__ **8**, e1371. Unless the disk storage option is given, one should not allocate all available physical memory using the ``memory`` command in an input file, so that the GA toolkit could allocate sufficient memory when needed. In large cases it may be necessary to pass the ``-G [ga_mem]`` option in the molpro command line. This allows the allocation of ``ga_mem`` megawords of memory (all cores in total) for GA at the beginning of execution. Without doing this, GA may crash when the distributed data structures get large, most likely due to an upstream bug. More information about memory and GA allocation is given in sections `GA Installation notes <running_molpro_on_parallel_computers.html#ga-installation-notes>`__ and `memory specifications <running_molpro_on_parallel_computers.html#memory-specifications>`__. Please read these sections carefully before starting large-scale calculations.

When using the ``implementation=disk`` option, allocating memory for GA is not necessary. However it only supports calculations on a single node. Also be aware that the program is not specifically optimized for disk operations, and it requires fast SSDs for optimal performance.

.. _local_correlation_methods_with_pair_natural_orbitals_pnos--versions:

Versions
========

In Molpro 2020.1 we have made a major revision to the PNO-LCCSD program to support open-shell molecules.
Some changes in the local approximations and default program settings have been applied.
**The computed energies will not be identical to those obtained with earlier versions of Molpro.**

**The option version=2019.2 is no longer available.**

.. _local_correlation_methods_with_pair_natural_orbitals_pnos--default-and-tight-settings:

Default and tight settings
==========================

In most cases the recommended default values should be sufficient and provide chemical accuracy for relative energies. In cases of doubt or to benchmark the accuracy of the local approximations, ``TIGHT`` presets can be chosen using one of the following options:

* ``DOMOPT=TIGHT`` Use tight domain approximations.
* ``PAIROPT=TIGHT`` Use tight pair approximations.

In most cases, the domain approximations causes the largest errors, in particular in PNO-LCCSD(T)-F12 calculations, and if very high accuracy is required or in cases of doubt ``DOMOPT=TIGHT`` should be tried first. This also reduces the errors of the projection approximations, which depend on the domain sizes. Note, however, the calculations with ``TIGHT`` settings are much more demanding than with ``DEFAULT`` options regarding CPU time and memory. For intermolecular interactions, we recommend ``DOMOPT=TIGHT, THRPNO_EN_CC=0.997``. Alternatively, ``DOMOPT=VTIGHT`` can be used, but this leads to a significant further increase of the computational cost.

* ``Note:`` To closely reproduce the results in `J. Chem. Theory Comput. <https://doi.org/10.1021/acs.jctc.8b01098>`__ **15**, 1044 (2019), use ``DOMOPT=TIGHT, THRPNO_EN_CC=0.997, THRVAL=1d-4``. Remaining very small differences stem from changes of some projection approximations since molpro2020, which cannot be affected by options.

* ``Note:`` Additional options ``DOMOPT=DEFAULT+`` and ``DOMOPT=TIGHT+`` have been added in Molpro 2025.3 (see below). These are particularly useful for accurate calculations of intermolecular interactions.

For a detailed description of all options see the `original publications <local_correlation_methods_with_pair_natural_orbitals_pnos.html#bibliography>`__.

.. list-table::
   :header-rows: 2

   * - Default and tight settings for PNO calculations (in atomic units)
     - 
     - 
     - 
     - 
     - 
   * - Description
     - threshold
     - default
     - tight
     - vtight      \|
     - 
   * - **Domain approximations** (affected by ``DOMOPT``)
     - 
     - 
     - 
     - 
     - .
   * - Primary PAO domains (partial charge)
     - ``THRLMO``
     - 0.2
     - 0.2
     - 0.2
     - 
   * - Domain extension (connectivity)
     - ``IEXT``
     - 2
     - 3
     - 3
     - 
   * - Domain extension (radius)
     - ``REXT``
     - 5
     - 7
     - 7
     - 
   * - OSV domain occupation number threshold
     - ``THROSV``
     - :math:`10^{-9}`
     - :math:`10^{-10}`
     - :math:`10^{-10}`
     - 
   * - LMP2 PNO domains (occ. number threshold)
     - ``THRPNO_OCC_LMP2``
     - :math:`10^{-8}`
     - :math:`10^{-8}`
     - :math:`10^{-9}`
     - 
   * - LMP2 PNO domains (energy threshold)
     - ``THRPNO_EN_LMP2``
     - 0.997
     - 0.997
     - 0.997
     - 
   * - LCCSD PNO domains (occ. number threshold)
     - ``THRPNO_OCC_CC``
     - :math:`10^{-7}`
     - :math:`10^{-8}`
     - :math:`2.5 \times 10^{-9}`
     - 
   * - LCCSD PNO domains (energy threshold)
     - ``THRPNO_EN_CC``
     - 0.990
     - 0.990
     - 0.997
     - 
   * - Large domains for (T0) calculation occ. number threshold
     - ``THRTNO_T0``
     - :math:`10^{-9}`
     - :math:`10^{-10}`
     - :math:`10^{-10}`
     - 
   * - Small domains for (T) calculation occ. number threshold
     - ``THRTNO_T``
     - :math:`10^{-7}`
     - :math:`10^{-7}`
     - :math:`5 \times 10^{-8}`
     - 
   * - **Pair approximations** (affected by ``PAIROPT``)
     - 
     - 
     - 
     - 
     - 
   * - Close pair energy threshold
     - ``THRCLOSE``
     - :math:`10^{-4}`
     - :math:`10^{-5}`
     - 
     - 
   * - Weak pair energy threshold
     - ``THRWEAK``
     - :math:`10^{-5}`
     - :math:`10^{-6}`
     - 
     - 
   * - Distant pair energy threshold
     - ``THRDIST``
     - :math:`10^{-6}`
     - :math:`10^{-6}`
     - 
     - 
   * - Very distant pair energy threshold
     - ``THRVDIST``
     - :math:`10^{-7}`
     - :math:`10^{-7}`
     - 
     - 
   * - Triples preselection type
     - ``TRIPTYP``
     - 2
     - 2
     - 
     - 
   * - Preselection of triples list
     - ``THRCLOSE_T``
     - :math:`10^{-4}`
     - :math:`10^{-5}`
     - 
     - 
   * - Selection of triples for iterations
     - ``THRTRIP_IT``
     - :math:`10^{-7}`
     - :math:`10^{-8}`
     - 
     - 
   * - **Local density fitting and RI approximations** (affected by ``DOMOPT``)
     - 
     - 
     - 
     - 
     - 
   * - Connectivity criterion for DF domains
     - ``IDFDOM``
     - 2
     - 3
     - 
     - 
   * - Distance criterion for DF domains
     - ``RDFDOM``
     - 5
     - 7
     - 
     - 
   * - Connectivity criterion for RI domains
     - ``IRIDOM``
     - 3
     - 4
     - 
     - 
   * - Distance criterion for RI domains
     - ``RRIDOM``
     - 7
     - 9
     - 
     - 

Additional domain selection options ``DEFAULT+`` and ``TIGHT+`` are provided since Molpro 2025.3. ``DEFAULT+`` differs from DEFAULT by increasing **REXT=5** to **REXT=7**. ``TIGHT+`` differs from TIGHT by increasing **THREN_CC** from **0.990 to 0.997**. For highly accurate calculations of interaction energies we recommend the options ``DOMOPT=TIGHT, DOMOPT_INTMOL=TIGHT+``. Nearly as accurate but less expensive are options ``DOMOPT=DEFAULT+, DOMOPT_INTMOL=TIGHT+``. See  `J. Phys. Chem. A 129, 4812 (2025) <https://doi.org/10.1021/acs.jpca.5c02316>`__ for benchmarks.

.. _local_correlation_methods_with_pair_natural_orbitals_pnos--directives:

Directives
==========

The usual ``OCC``, ``CORE``, ``CLOSED``, and ``WF`` directives can be given. Normally, this is not needed since the information can be recovered from the orbital dump file. Local options can be given on the command line or on a ``LOCAL`` directive. Options form explicit can also be given either on the command line or on an ``EXPLICIT`` directive. For ``REGION`` input see section [[#Correlation_regions_in_the_PNO_program_[region]\|Correlation regions]].

\* ``INTERACT``, ``MERGE=[list of molecules]``

.. code-block:: text

    Giving this directive implies option ''INTERACT'' to be true. ''MERGE'' works exactly as merge described for the [[properties_and_expectation_values#intermolecular_interaction_energies|INTERACT]] program, and the inputs should be consistent.

.. _local_correlation_methods_with_pair_natural_orbitals_pnos--options:

Options
=======

In this section we describe the parameters most relevant to the accuracy and performance of the PNO program. We note that our team has carefully selected the default options through benchmark calculations, and the options only need to be modified for special cases.

.. _local_correlation_methods_with_pair_natural_orbitals_pnos--options-for-job-execution:

Options for job execution
=========================

* **``IMPLEMENTATION``\ =\ ``GA|DISK``** Choose whether large data structures are stored in distributed memory (default) or disk. **Do not use the ``-G`` or ``-M`` options to preallocate GA in calculations using the disk implementation!** Please check the `notes on the disk option <running_molpro_on_parallel_computers.html#notes-on-the-disk-option>`__.

The program is generally optimized for using GA, but the disk option can be used in single-node calculations that would otherwise require too much memory.

Also, in single-node calculations ``implementation=disk`` with the global scratch set to a tmpfs (e.g., with ``-D /dev/shm``) can be efficient. Do note that when ``-D /dev/shm`` and ``implementation=disk`` is used on nodes with a physical disk, the options ``PNO_3EXTK_IMPL=4, PNO_4EXTK_IMPL=4`` can be given to save some less frequently accessed data to the physical disk (with path defined by the ``-d`` command line option) to reduce the memory usage.

.. _local_correlation_methods_with_pair_natural_orbitals_pnos--options-for-pao-osv-pno-generation:

Options for PAO/OSV/PNO generation
==================================

* **``THRLMO``\ =\ *value*** Charge threshold for selection of primary PAO domains when using IBOs or NBOs (default 0.2). For open-shell orbitals the threshold is divided by 2. If the threshold is larger than the largest partial charge cmax of an orbital, it is reduced to cmax\*0.9 for this orbital.
* **``THRLMO_ACT``\ =\ *value*** Charge threshold for selection of primary PAO domains when using IBOs or NBOs for active (open-shell) orbitals (default THRLMO).
* **``IEXT``\ =\ *value*** Domain extension using connectivity. *value* corresponds to the number of bonds by which the primary domains are extended.
* **``REXT``\ =\ *value*** Domain extension using distance. *value* is the radius in :math:`a_0` from any atom in the primary domain. ``IEXT`` and ``REXT`` can be combined. If both are given all atoms are included that are selected by one or the other criterion.
* **``THROSV``\ =\ *threshold*** OSV selection threshold based on natural occupation numbers.
* **``THRPNO_OCC_LMP2``\ =\ *threshold*** PNO selection threshold for LMP2 based on natural occupation numbers. It is also possible to specify 3 values for strong+close, weak, and distant pairs as ``THRPNO_OCC_LMP2``\ =[*thrstrong, thrweak, thrdist*]. ``THRPNO_LMP2`` is an alias for ``THRPNO_OCC_LMP2``.
* **``THRPNO_EN_LMP2``\ =\ *threshold*** PNO selection threshold for LMP2 based on the energy criterion. ``THREN_LMP2`` is an alias for ``THRPNO_EN_LMP2``.
* **``THRPNO_OCC_CC``\ =\ *threshold*** PNO selection threshold for LCCSD based on occupation numbers. ``THRPNO_CC`` is an alias for ``THRPNO_OCC_CC``.
* **``THRPNO_EN_CC``\ =\ *threshold*** PNO selection threshold for LCCSD based on the energy criterion. ``THREN_CC`` is an alias for ``THRPNO_EN_CC``.
* ``SORTPNO`` If this option is given, PNOs are first selected using the occupation number criterion. Then PNOs are added in the order of decreasing semi-canonical energy contributions until the energy completeness criterion is satisfied. Without this option, PNOs are added in the order of decreasing occupation numbers. In some cases, SORTPNO significantly reduces the PNO domain sizes. The default since Molpro version 2025.3 is  ``SORTPNO=1``. For compatibility with older program versions, set ``SORTPNO=0``.
* **``EPNO_MIN``\ =\ *value*** PNOs which have semi-canonical energy contributions smaller than the given value are omitted. The default is EPNO_MIN=0.

Note that in LCCSD calculations the thresholds ``THRPNO_OCC_LMP2`` and ``THRPNO_EN_LMP2`` only affect the LMP2 domain corrections. The thresholds ``THRPNO_OCC_CC`` must not be smaller and ``THRPNO_EN_CC`` not be larger than the corresponding LMP2 thresholds. Thus, the LCCSD domains are always smaller or equal to the LMP2 ones. PNOs are added to the domains until both the occupation number and energy criteria are fulfilled.

.. _local_correlation_methods_with_pair_natural_orbitals_pnos--options-for-pair-approximations:

Options for pair approximations
===============================

In the PNO-LCCSD program the pairs are classified according to the LMP2 pair energies into strong, close, weak, distant and very distant pairs. Close pairs are treated by approximate CCSD, in which terms that cancel at long-range are neglected. Weak pairs are treated with the same approximations as close pairs, but in addition terms that are non-linear in the amplitudes are neglected (CEPA). Distant pairs are approximated by the iterative SCS-LMP2 multipole approximation. Very distant pairs are treated by the semi-canonical SCS-LMP2 (non-iterative) multipole approximation.

* **``THRCLOSE``\ =\ *thrclose*** Pairs with PNO-LMP2 energies :math:`thrclose \ge E_{ij} \gt thrweak` are treated as close pairs.
* **``THRWEAK``\ =\ *thrweak*** Pairs with PNO-LMP2 energies :math:`thrweak \ge E_{ij} \gt thrdist` are treated as weak pairs.
* **``THRDIST``\ =\ *thrdist*** Pairs with PNO-LMP2 energies :math:`thrdist \ge E_{ij} \gt thrvdist` are treated as distant pairs.
* **``THRVDIST``\ =\ *thrvdist*** Pairs with PNO-LMP2 energies :math:`thrvdist \ge E_{ij}` are treated as very distant pairs.

.. _local_correlation_methods_with_pair_natural_orbitals_pnos--options-for-triples-calculation:

Options for triples calculation
===============================

The **domain approximations in (T)** calculations are controlled by the following options:

* **``THRTNO_T0``\ =\ *value*** Occupation number threshold for selecting triples domains for the non-iterative (T0) approximation.
* **``THRTNO_T``\ =\ *value*** Occupation number threshold for selecting triples domains for the iterative (T) approximation. Note that decreasing ``THRTNO_T`` will lead to significantly increased GA usage.
* **``IEXT_T``\ =\ *value*, ``REXT_T``\ =\ *value*** PAO domain selection criteria similar to ``IEXT`` and ``REXT`` but affect only (T) calculations. Defaults to ``IEXT`` and ``REXT``, respectively.

The selection of the **triple list** is controlled by the following options:

* **``TRIPTYP``\ =\ *value*** Determines triples list via pair classes (default 2).
* **``THRCLOSE_T``\ =\ *value*** Energy threshold for close pairs in selecting triples (in :math:`E_h`, default 1.d-4).
* **``THRWEAK_T``\ =\ *value*** Energy threshold for weak pairs in selecting triples (in :math:`E_h`, default 0, i.e., considering all nondistant pairs “close” in the triple selection).
* **``THRTRIP``\ =\ *value*** Threshold for additional triple screening using (T0) triple corrections from a small-domain calculation (in :math:`E_h`, default 0, i.e., perform (T0) calculation for all triples selected by ``TRIPTYP``).
* **``THRTRIP_IT``\ =\ *value*** (T0) energy threshold for screening triples before the iterations (in :math:`E_h`, default 1.d-7).

.. _local_correlation_methods_with_pair_natural_orbitals_pnos--options-for-f12-calculations:

Options for F12 calculations
============================

* **``PROJECTOR``\ =**\ ``PNO|PAO|MIXED`` (*since 2022.1*, default PNO) The type of virtual orbitals to be used in the F12 strong orthogonality projector. ``MIXED`` means using PAOs in the LMP2-F12 projector and the PNOs in the LCCSD-F12 projector. In typical calculations this does not affect the relative energy significantly. In some difficult cases (e.g., there is correlated core orbitals) the PAO projector may lead to more accurate results. The ``PAO`` option is somewhat more expensive than the other choices.
* **``THRF12``\ =\ *threshold*** LMP2 pair energy threshold for selecting pairs for which F12 corrections are computed (default 0, i.e., all nondistant pairs are included).
* **``THRVAL``\ =\ *value*** The MP2 pair energy threshold in determining the LMO domains :math:`[ij]_{\rm LMO}` used in the F12 strong orthogonality projector (default :math:`10^{-5}`). This option only applies to the selection of the valence occupied orbitals in the LMO domains.
* **``ICOREDOM_F12``\ =\ *value*, ``RCOREDOM_F12``\ =\ *value*** The connectivity and distance (in :math:`a_0`) criteria in determining the LMO domains :math:`[ij]_{\rm LMO}` used in the F12 strong orthogonality projector (defaults are 2 and 5.0, respectively). This option only applies to the selection of the core orbitals in the LMO domains.
* **``MODOMC``\ =\ *value*** (*since Molpro 2020.2*) By default core contributions are included (``MODOMC=0``) in the CCSD-F12 projector. With ``MODOMC=1`` these contributions are neglected, which slightly reduces the cost and usually introduces only small errors. However, the approximation can have a significant effect in calculations of transition metal complexes. *The approximation is always applied before Molpro 2020.2.*
* **``IRIDOM``\ =\ *value*** RI domain extension using connectivity. The default is 3.
* **``RRIDOM``\ =\ *value*** RI domain extension using distances in :math:`a_0`. The default is 7. If both ``IRIDOM`` and ``RRIDOM`` are given, the RI basis functions at a center will be included when either criterion is fulfilled.
* **``CCF12``\ =\ *[0|1]***. If ccf12=0, the MP2 F12 correction is added to the PNO-LCCSD(T) energy, i.e. no F12 is included in the PNO-LCCSD step (default CCF12=1, i.e. PNO-LCCSD-F12 is done).

.. _local_correlation_methods_with_pair_natural_orbitals_pnos--options-for-fitting-basis-and-orbital-screening:

Options for fitting basis and orbital screening
===============================================

* **``IDFDOM``\ =\ *value*** Fitting domain extension using connectivity criterion (default 3).
* **``RDFDOM``\ =\ *value*** Fitting domain extension using distances criterion (in :math:`a_0`, default 7). If both ``IDFDOM`` and ``RDFDOM`` are given, the DF functions at a center will be included when either criterion is fulfilled.
* **``IDFDOM_T``\ =\ *value*, ``RDFDOM_T``\ =\ *value*** Fitting domain extension criteria similar to ``IDFDOM`` and ``RDFDOM`` but apply only to (T) calculations. The default values are 0 for both, in which case the primary fitting domains are used.
* **``FITLMO``\ =\ *threshold*** In the PNO program LMOs are truncated if the square sum of the coefficients at one center is smaller than *threshold* (default 1.d-6). The remaining LMO coefficients are fitted to the original LMO.
* **``FITPAO``\ =\ *threshold*** In the PNO program PAOs at one center are truncated when none of the PAOs at the center has a square sum of coefficients greater than *threshold* (default 1.d-6). The remaining PAO coefficients are fitted to the original PAOs.

.. _local_correlation_methods_with_pair_natural_orbitals_pnos--options-for-intermolecular-interactions:

Options for intermolecular interactions
=======================================

The following special options for computing intermolecular interactions are available since Molpro2022.3. The purpose is to save computation time by using small (e.g. default) domains for intramolecular pairs, but larger (tight) domains for intermolecular pairs. This is still experimental.

* ``INTERACT`` (logical) Activates options for intermolecular interactions. The individual molecules are determined automatically.
* **``IEXT_INTMOL``\ =\ *value*** PAO connectivity criterion for intermolecular pairs.
* **``REXT_INTMOL``\ =\ *value*** PAO distance criterion for intermolecular pairs.
* **``THRPNO_CC_INTMOL``\ =\ *value*** PNO occupation number threshold for intermolecular pairs (only for CC domains).
* **``THREN_CC_INTMOL``\ =\ *value*** Energy completeness criterion for intermolecular pairs (only for CC domains).
* **``THRTNO_T0_INTMOL``\ =\ *value*** Threshold for selecting T0 domains for intermolecular triples.
* **``THRTNO_T_INTMOL``\ =\ *value*** Threshold for selecting T domains for intermolecular triples.
* **``TYPE_INTMOL``\ =\ *value*** Type for intermolecular pairs (STRONG\|CLOSE\|WEAK)
* **``TYPE_INTMOL_T``\ =\ *value*** Type for intermolecular triples (STRONG\|CLOSE\|WEAK). With WEAK, intermolecular triples are excluded.

Additional domain selection options ``DEFAULT+`` and ``TIGHT+`` are provided. ``DEFAULT+`` differs from DEFAULT by increasing **REXT=5** to **REXT=7**. ``TIGHT+`` differs from TIGHT by increasing **THREN_CC** from **0.990 to 0.997**. For highly accurate calculations of interaction energies we recommend the options ``DOMOPT=TIGHT, DOMOPT_INTMOL=TIGHT+``. Nearly as accurate but less expensive are options ``DOMOPT=DEFAULT+, DOMOPT_INTMOL=TIGHT+``. See `Phys. Chem. A 129, 4812 (2025) <https://doi.org/10.1021/acs.jpca.5c02316>`__ for benchmarks.

.. _local_correlation_methods_with_pair_natural_orbitals_pnos--miscellaneous-options:

Miscellaneous options
=====================

* **``MAXIT``\ =\ *value*** The maximum number of PNO-LCCSD iterations.
* **``MAXIT_LMP2``\ =\ *value*** The maximum number of PNO-LMP2 iterations.
* **``MAXITT``\ =\ *value*** The maximum number of (T) iterations.
* **``THRCONV_TRIP``\ =\ *value*** Convergence threshold (energy) for (T) iterations.

Note that the local MP2 and (T) equations are linear and usually converge in several iterations.
Difficulties in convergence is usually caused by poor orbital localization.

.. _local_correlation_methods_with_pair_natural_orbitals_pnos--restarting-t:

Restarting (T)
==============

The (T) calculations in PNO-LCCSD(T)-F12 can be restarted from a dump file since Molpro 2022.3.
The options to create a dump file and restart from it are:

* **``CCSDDUMP``\ =\ *path*** The dump file to be created. It can be a absolute path or a relative path to the input file. Quote the path with single quotation marks to avoid case conversion. The dump file is created at the beginning of the (T) calculation.
* **``RESTART_T``\ =\ *path*** The dump file from which (T) is restarted. If given, the program will start from the (T) calculation directly from the dump file.

In trail calculations where the memory requirement is unknown, when (T) calculation crashes due to insufficient memory, the calculation can be restarted from the dump file if it is requested. These options can also be used in testing different local options that only affects the (T) calculation.

The dump file is an HDF5 file. If Molpro is compiled from the source code, ``--with-hdf5`` must be given to ``configure`` to use this feature.

.. _local_correlation_methods_with_pair_natural_orbitals_pnos--correlation-regions-in-the-pno-program-region:

Correlation regions in the PNO program [REGION]
-----------------------------------------------

Correlation regions can be defined using ``REGION`` directives within the PNO program. This is a 2-step process: first, LMOs are assigned to a region (HF, LOW, or HIGH]. Then, orbital pairs :math:`i,j` are selected for that region depending if :math:`i` or :math:`j` or both are in the corresponding orbital region. Similarly, in PNO-LCCSD(T) or PNO-LCCSD(T)-F12 calculations only those triples :math:`i,j,k` are include for which either 1, 2, or 3 of the three orbitals are in the region (this applies only to the high-level region).

.. code-block:: text

   REGION,METHOD[,[[TYPE=][INCLUSIVE|EXCLUSIVE][,RESTRICT_P=1|2][,RESTRICT_T=1|2|3],CENTERS=[list]

where

\* ``LOC_METHOD = LOW|MP2`` for the low-level method (LMP2 or LMP2-F12)

\* ``LOC_METHOD = HIGH|CCSD`` for the current high-level method [e.g. LCCSD(T) or LCCSD(T)-F12]

LMOs that are not included in the HIGH- or LOW-level regions are assigned to the HF region. These orbitals are not correlated at all.

\* ``INCLUSIVE`` (default) means that orbitals are selected which contain in their primary domain at least one of the chosen atoms.

\* ``EXCLUSIVE``  means that orbitals are selected which contain in the primary domain only atoms only chosen atoms.

\* ``RESTRICT_P=1|2``  RESTRICT_P=1 (default) means that an orbital pair :math:`i,j` is included in this correlation region if either :math:`i` or :math:`j` is in the orbital region. RESTRICT_P=2 means that an orbital pair :math:`i,j` is included if both orbitals are in the orbital region. Other pairs are assigned to the next lower region (in the order HIGH, LOW, HF).

\* ``RESTRICT_T=1|2|3``  (default 2 means that a triple :math:`i,j,k`  is included in the region of one, two or three orbitals of the triple are in the region. This only applies to the high-level region.

\* ``CENTERS=[//list//]`` A list of atoms that are assigned to the current region. Positive numbers refer to the respective row in the input z-matrix. Negative numbers mean "up to" this atom, starting with the previous number. Example: CENTERS=[5,-10, 12] means centers five to ten and 12. In order to keep this input short and simple, it is advisable to order the centers in the xyz input according to regions.

\* ``REXT_REG=//value//`` The given list of centers is augmented by all centers within REXT_REG bohr from any atom in the initial list.

\* ``IEXT_REG=//value//`` The given list of centers is augmented by all centers within IEXT_REG bonds from any atom in the initial list.

Example for C\ :math:`_4`\ H\ :math:`_9`\ COOH, where the order is CH3 - CH2 - CH2 - CH2 - COOH:

.. code-block:: text

    <code>

{pno-lccsd(t)-f12

.. code-block:: text

    region,low,inclusive,centers=[7,-13]
    region,high,inclusive,centers=[14,-17]}

In this case atoms 14-17 are the COOH group. The orbitals of COOH group and in addition the connected C-C bond orbital are assigned to the high level region. The C-H orbitals or the CH3  group are in the HF region and not correlated.

It is also possible to specify region-specific domain options. The following options can be given on a region directive:

``DOMOPT, THRPNO_LMP2, THRPNO_CC, THREN_LMP2, THREN_CC, IEXTDOM, IEXTDOM_S, REXTDOM, REXTDOM_S``

Their meaning is the same as described for the PNO program.

.. code-block:: text

.. _local_correlation_methods_with_pair_natural_orbitals_pnos--advanced-options:

Advanced options
----------------

In this section we list some advanced options to the PNO program. These options exist for technical or historical reasons and we do not recommend modifying the default values in general.

The following options are available for the **orbital localization**:

* **``LOC_METHOD``\ =\ *method*** Localization method. *method* can be ``IBO`` (intrinsic bond orbitals, default), ``PM`` (Pipek-Mezey), ``BOYS`` (Forster-Boys localization). ``IBO`` is recommended, as it is most efficient and stable.
* **``LOC_METHOD_CORE``\ =\ *method*** Localization method for core orbitals. *method* can be ``IBO``, ``PM``, ``IBO(AO)``, or ``PM(AO)``. The latter two minimize mixings of core orbitals of different types (e.g. s, p\ :math:`_y`, p\ :math:`_x`, p\ :math:`_z` etc.). The default is ``IBO(AO)``.
* **``IBTYPE``\ =\ *value*** Projector type for generation of intrinsic atomic orbitals. *value* can be 1 or 2 (default).
* **``IBOEXP``\ =\ *value*** Exponent used in the PM-like localization functional. *value* can be 2 or 4 (default).
* ``LOC_OUTCORE=ON|OFF|SEP|MIX`` If (outer) core orbitals are correlated, this option determines how these are localised. ``ON`` or ``MIX``: localization together with the valence orbitals; ``OFF``: no localization; ``SEP``: localisation separately from the valence orbitals, i.e. in a different localization group. With ``OFF`` and ``SEP``, the orbitals are sorted before localization, so that the correlated core orbital come before the valence orbitals. WITH ``ON`` and ``MIX`` all correlated orbitals are first localized and then sorted. WITH ``MIX`` the outer core orbitals are subsequently re-localized using IBO(AO). This sometimes reduces the mixing of (nearly) degenerate atomic core orbitals. The default is ``SEP``.
* **``SAVE_LMO``\ =\ *value*** If this option is given, the localised orbitals are written to a record. If ***value=1*** the current orbital dump record is used. If ***value>1000*** the given record is used (e.g. ***value=2110.2***). Furthermore, the orbitals are written to the xml file (if present) for visualisation with gmolpro.

Options for **PAO domain selection**:

* **``THRBP``\ =\ *value*** Boughton-Pulay (BP) completeness criterion for selection of primary PAO domains (default 0, i.e., do not use the BP procedure). The BP criterion takes precedence over the LMO partial charge criterion if a positive ``THRBP`` is given.
* **``THRLOC``\ =\ *value*** Redundancy threshold in the PAO pair domain generation. Default :math:`10^{-7}`.

Options for **OSV generation**:

* ``OSV_AMPL=PAO|CAN|OPT`` Amplitudes to used to generate OSVs. ``PAO`` (default) means to use semi-canonical amplitudes in the PAO domains; ``CAN`` means semi-canonical in the full virtual space; ``OPT`` means fully optimized LMP2 amplitudes in the full virtual space.
* **``THRLOC``\ =\ *value*** Redundancy threshold in the OSV  pair domain generation. Default :math:`10^{-6}`.

Options for **multipole approximations**:

* **``MLTP_METHOD``\ =\ *value*** If 1 use non-iterative multipole approximation for distant pairs, if 2 iterative multipole approximation (default 2).
* **``MLTP_ORDER``\ =\ *value*** Expansion level for multipole approximation (default 3).
* **``MLTP_SELECT``\ =\ *value*** Expansion level of multipole approximation used to select distant pairs (default MLTP_ORDER).

Options for **PNO generation**:

* ``PNO_AMPL=PAO|PAO(OPT)|OSV|OSV(OPT)`` Amplitudes to used to generate PNOs. ``PAO`` (default) means semi-canonical (non-iterative) PAO amplitudes, and ``OSV`` means to use semi-canonical (non-iterative) OSV amplitudes. ``OSV`` is not supported in open-shell calculations. If ``(OPT)`` is appended the amplitudes are iteratively optimized (can be expensive with ``OSV(OPT)`` and very expensive with ``PAO(OPT)``!
* ``THRDEG`` (*Since Molpro 2020.1*) PNOs with occupation number difference less than ``THRDEG`` (default :math:`10^{-12}`) are considered degenerate. Degenerate PNOs are either all included or all excluded from the domains.
* ``PNO_DIAG`` (logical). If true, use PNO domain selection criterion also for diagonal pairs. Otherwise OSV domains are used for diagonal pairs. If ``PNO_DIAG=true`` the threshold ``THROSV`` only affects the distant pair multipole treatment.

The PNO program divides basis functions to blocks for integral screening. The following options are available for defining the **block sizes**. A smaller block size encourages more efficient integral screening, reduces scratch memory usage, and improves the parallel efficiency. However, a larger block size improves the performance of matrix operations, and reduces the communication and bookkeeping cost.

* **``BB_BLOCKS_AO``\ =\ *value*** Target blocking size in the AO basis (default 32).
* **``BB_BLOCKS_DF_F12``\ =\ *value*** Target blocking size in the DF basis for the F12 calculations (default 32). The option does not affect PNO-LMP2 calculations.
* **``BB_BLOCKS_RI``\ =\ *value*** Target blocking size in the RI basis for the F12 calculations (default 128).

In addition, the following options control the **integral screening thresholds**:

* **``BB_THRESH``\ =\ *value*** Block screening threshold (default 1.d-5).
* **``BB_RADIUS``\ =\ *value*** Block screening radius (default 4).

Other miscellaneous options:

* **``BB_F12_PNO``\ =\ *value*** (deprecated since Molpro 2022.2, use ``PROJECTOR`` instead) If ``BB_F12_PNO``\ =0, PNO-LMP2-F12 energies with both OSV and PNO projectors will be computed; If ``BB_F12_PNO``\ =1, only energies using the PNO projector will be computed; If ``BB_F12_PNO``\ =2, only energies with the OSV projector will be computed (default 1). PNO projectors are always used in the F12 terms in coupled-cluster equations regardless of this option.
* ``BB_F12_LOCCORE`` (logical) If true (default), localize the core orbitals. This may affect the pair approximations in the LMP2-F12 projector.

.. _local_correlation_methods_with_pair_natural_orbitals_pnos--obsolete-options:

Obsolete options
----------------

The following options that have been deprecated in Molpro 2020.1.
They can still be used in calculations with ``version=2019.2``.

* ``PROJOPT=TIGHT`` Use tight projection approximations.
* ``ALLTIGHT`` (logical). Use tight domain, pair, and projection approximations.

.. list-table::

   * - **Projection approximations** (affected by ``PROJOPT``)((Our benchmark calculations show that the projection approximations are unlikely to be a major contributor to the local errors. These options will be deprecated in a future release.))
     - 
     - 
     - 
   * - Project K-integrals
     - ``PROJECT_K``
     - true
     - true
   * - Project J-integrals
     - ``PROJECT_J``
     - all
     - weak
   * - Projection of singles amplitudes to doubles domains
     - ``PROJECT_S``
     - all
     - all
   * - Projection of 3-external :math:`{\bf J}({\bf E}^{kj})` terms
     - ``PROJECT_JE``
     - on
     - on
   * - Level of projection in the 3-external :math:`{\bf K}({\bf E}^{kj})` terms
     - ``PROJECT_KE``
     - 2
     - 1

* ``LOCFIT=0`` Disables local fitting (default is ``LOCFIT=1``). Note that this is extremely expensive and memory demanding for large molecules, and local fitting is seldom a noticeable source of error. *Please use a large ``RDFDOM`` instead.*
* ``LOCRI=0`` Disables local RI (default is ``LOCRI=1``). *Please use a large ``RRIDOM`` instead.*

.. _local_correlation_methods_with_pair_natural_orbitals_pnos--variables-set-by-the-pno-program:

Variables set by the PNO program
--------------------------------

* ``ENERGR`` Reference energy (including CABS correction if present).
* ``ENERGY`` Last computed total energy including the Hartree–Fock energy and CABS correction (if present). In F12 calculations the F12b energy is stored unless the input specifies F12a (*note the different behavior in canonical F12 programs*).
* ``ENERGYA`` Total energy using the F12a approximation. Not available in non-F12 calculations.
* ``ENERGYB`` Total energy using the F12b approximation. Not available in F12a calculations.
* ``ENERGT0`` (T0) energy contribution.
* ``ENERGT1`` (T1) energy contribution. Available only in (T1) calculations, or in iterative (T) calculations with ``skip_t1=0``.
* ``ENERGT1`` (T) energy contribution. Contains the scaled triples if ``scale_trip=1`` is given.
* ``ENERGC`` Total PNO-LCCSD or PNO-LCCSD(T) energy without (T) correction.
* ``EMP2`` PNO-LMP2 energy without domain correction.
* ``EMP2_DC`` PNO-LMP2 energy including domain correction.
* ``EF12`` F12 contribution in PNO-LMP2-F12 (only set in F12 calculations).
* ``EMP2_F12`` PNO-LMP2-F12 energy (only set in F12 calculations).
* ``EMP2_PNO`` Same as ``EMP2``.
* ``EF12_PNO`` Same as ``EF12``.
* ``EMP2_SCS`` PNO-SCS-LMP2 energy without domain correction.
* ``EF12_SCS`` SCS-F12 contribution (only set in F12 calculations).
* ``EMP2_F12_SCS`` PNO-SCS-LMP2-F12 energy (only set in F12 calculations)
* ``DOMCORR`` Domain contribution for PNO-LMP2 (should not be added to F12 energies)
* ``DOMCORR_CC`` PNO-LMP2 domain correction for PNO-LCCSD.
* ``DOMCORR_F12`` PNO-LMP2-F12 domain correction for PNO-LCCSD-F12
* ``DOMCORR_PNO`` Same as ``DOMCORR``.
* ``ENERGT`` (T) energy contribution in PNO-LCCSD(T) and PNO-LCCSD(T)-F12 calculations

Note: The CABS correction has to be computed beforehand and is stored in variable ``EF12_RHFRELAX``. If this is present, it is in F12 calculations added to all total energies, including the PNO-LMP2 one. It is not added in non-F12 calculations, even if ``EF12_RHFRELAX`` is set.

.. _local_correlation_methods_with_pair_natural_orbitals_pnos--troubleshooting:

Troubleshooting
---------------

.. _local_correlation_methods_with_pair_natural_orbitals_pnos--problems-running-df-hf-or-df-mp2-f12-on-multiple-nodes:

Problems running DF-HF or DF-MP2-F12 on multiple nodes
======================================================

The ``DF-HF`` and ``DF-MP2-F12`` programs are not designed for execution over multiple computer nodes, and all disk I/O are replaced by GA operations in this case. It is sometimes helpful running these calculations separately on one node. For example, one can run a single-node calculation for DF-HF and CABS singles correction with

.. code-block:: text

    FILE, 2, some_orbitals.wfu
    [specifications of basis, geometries, options, etc]
    {DF-HF}
    {DF-MP2-F12, CABS_SINGLES=-1}

and then a PNO-LCCSD(T)-F12 calculation can be performed on multiple nodes with

.. code-block:: text

    FILE, 2, some_orbitals.wfu
    [specifications of basis, options, etc]
    {PNO-LCCSD(T)-F12}

The CABS singles corrections must be manually added to the final PNO-LCCSD(T)-F12 results when this procedure is used. Also note that the wave function repository of Molpro needs to be on a network file system accessible to all nodes.

.. _local_correlation_methods_with_pair_natural_orbitals_pnos--problems-with-allocation-of-ga-memory:

Problems with allocation of GA memory
=====================================

If the program crashes with a message ”ARMCI DASSERT fail” most likely more GA memory must be specified using the -G command line option, see section `getting started <local_correlation_methods_with_pair_natural_orbitals_pnos.html#getting-started>`__. This is necessary due to a bug in the GA software, which is out of our control. The GA developers recommend to install the GA software with configure option ``–with-mpi-pr``. This avoids the problem and does not require the -G option. Unfortunately also this GA version, which is MPI based, is not stable on all systems, in particular for large cases. It is also somewhat slower since an extra process is needed. Since molpro 2025.2 ``–with-mpi-pr`` is used by default in the Molpro binary.

.. _local_correlation_methods_with_pair_natural_orbitals_pnos--bibliography:

Bibliography
------------

General reviews of the PNO program:

* Q. Ma, and H.-J. Werner, *Explicitly correlated local coupled-cluster methods using pair natural orbitals*, `WIREs Comput. Mol. Sci. <https://doi.org/10.1002/wcms.1371>`__ **8**, e1371 (2018)
* H.-J. Werner, C. Köppl, Q. Ma, and M. Schwilk, *Explicitly correlated local electron correlation methods*, in `Fragmentation: Towards Accurate Calculations on Complex Molecular Systems <https://www.wiley.com/en-us/Fragmentation%3A+Toward+Accurate+Calculations+on+Complex+Molecular+Systems-p-9781119129240>`__, ed. Mark S. Gordon, Wiley (2017), p. 1–79. The chapter is accessible at no cost as an excerpt.
* H.-J. Werner and A. Hansen, //Accurate Calculation of Isomerization and Conformational Energies

of Larger Molecules Using Explicitly Correlated Local Coupled
Cluster Methods in Molpro and ORCA//,\ `J. Chem. Theory Comput. <https://doi.org/10.1021/acs.jctc.3c00270>`__ **19**, 7007−7030 (2023).

* A. Hansen, P. J. Knowles, and H.-J. Werner, *Accurate Calculation of Noncovalent Interactions Using PNO-LCCSD(T)-F12 in Molpro*,\ `J. Phys. Chem. <https://doi.org/10.1021/acs.jpca.5c02316>`__ **A 129**, 4812 (2025)

Closed-shell PNO-LCCSD(T)-F12:

* H.-J. Werner, G. Knizia, C. Krause, M. Schwilk, and M. Dornbach, *Scalable electron correlation methods I.: PNO-LMP2 with linear scaling in the molecular size and near inverse-linear scaling in the number of processors*, `J. Chem. Theory Comput. <https://doi.org/10.1021/ct500725e>`__ **11**, 484 (2015)
* Q. Ma, and H.-J. Werner, *Scalable electron correlation methods. 2. Parallel PNO-LMP2-F12 with near linear scaling in the molecular size*, `J. Chem. Theory Comput. <https://doi.org/10.1021/acs.jctc.5b00843>`__ **11**, 5291 (2015)
* M. Schwilk, Q. Ma, C. Köppl, and H.-J. Werner, *Scalable electron correlation methods. 3. Efficient and accurate parallel local coupled cluster with pair natural orbitals (PNO-LCCSD)*, `J. Chem. Theory Comput. <https://doi.org/10.1021/acs.jctc.7b00554>`__ **13**, 3650 (2017)
* Q. Ma, M. Schwilk, C. Köppl, and H.-J. Werner, *Scalable electron correlation methods. 4. Parallel explicitly correlated local coupled cluster with pair natural orbitals (PNO-LCCSD-F12)*, `J. Chem. Theory Comput. <https://doi.org/10.1021/acs.jctc.7b00799>`__ **13**, 4871 (2017)
* Q. Ma, and H.-J. Werner, *Scalable electron correlation methods. 5. Parallel perturbative triples correction for explicitly correlated local coupled cluster with pair natural orbitals*, `J. Chem. Theory Comput. <https://doi.org/10.1021/acs.jctc.7b01141>`__ **14**, 198 (2018)

Open-shell PNO-LCCSD(T)-F12:

* C. Krause, and H.-J. Werner, *Scalable electron correlation methods. 6. Local spin-restricted open-shell second-order Møller–Plesset perturbation theory using pair natural orbitals: PNO-RMP2*, `J. Chem. Theory Comput. <https://doi.org/10.1021/acs.jctc.8b01012>`__ **15**, 987 (2019)
* Q. Ma, and H.-J. Werner, *Scalable electron correlation methods. 7. Local open-shell coupled-cluster methods using pair natural orbitals: PNO-RCCSD and PNO-UCCSD*, `J. Chem. Theory Comput. <https://doi.org/10.1021/acs.jctc.0c00192>`__ **16**, 3135 (2020)

Other topics on local approximations used in the PNO program:

* M. Schwilk, D. Usvyat, and H.-J. Werner, *Communication: Improved pair approximations in local coupled-cluster methods*, `J. Chem. Phys. <https://doi.org/10.1063/1.4916316>`__ **142**, 121102 (2015)
* C. Köppl, and H.-J. Werner, *On the use of Abelian point group symmetry in density-fitted local MP2 using various types of virtual orbitals*, `J. Chem. Phys. <https://doi.org/10.1063/1.4918772>`__ **142**, 164108 (2015)
* H.-J. Werner, *Communication: Multipole approximations of distant pair energies in local correlation methods with pair natural orbitals*, `J. Chem. Phys. <https://doi.org/10.1063/1.4968595>`__ **145**, 201101 (2016)

Application on intermolecular interactions:

* Q. Ma, and H.-J. Werner, *Accurate intermolecular interaction energies using explicitly correlated local coupled cluster methods [PNO-LCCSD(T)-F12]*, `J. Chem. Theory Comput. <https://doi.org/10.1021/acs.jctc.8b01098>`__ **15**, 1044 (2019)

* A. Hansen, P. J. Knowles, and H.-J. Werner, *Accurate Calculation of Noncovalent Interactions Using PNO-LCCSD(T)-F12 in Molpro*,\ `J. Phys. Chem. <https://doi.org/10.1021/acs.jpca.5c02316>`__ **A 129**, 4812 (2025)
