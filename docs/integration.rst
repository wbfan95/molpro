.. raw:: html

   <span id="imported-hamiltonian"></span>

.. raw:: html

   <span id="integral-direct-calculations-gdirect"></span>

.. raw:: html

   <span id="sorted-integrals"></span>

.. _integration--integration:

Integration
===========

Before starting any energy calculations, the geometry and basis set must be defined in ``GEOMETRY`` and ``BASIS`` blocks, respectively. By default, two electron integrals are evaluated once and stored on disk. This behaviour may be overridden by using the input command ``gdirect`` (see section `INTEGRAL-DIRECT CALCULATIONS (GDIRECT) <integration.html#integral-direct-calculations-gdirect>`__) to force evaluation of integrals on the fly. Molpro checks if the one-and two-electron integrals are available for the current basis set and geometry, automatically computing them if necessary. The program also recognizes automatically if only the nuclear charges have been changed, as is the case in counterpoise calculations. In this case, the two-electron integrals are not recomputed.

By default a point charge nuclear model is used for all atoms. Alternatively, a Gaussian nuclear model can be used by setting

``SET,FNUC=1\\``
before the first energy evaluation (a value of 0 corresponds to a point charge nucleus). Alternatively, this also can be given as an option to the ``INT`` command:

``INT,FNUC=1``

.. _integration--sorted-integrals:

Sorted integrals
================

If the integrals are stored on disk, immediately after evaluation they are sorted into complete symmetry-packed matrices, so that later program modules that use them can do so as efficiently as possible. As discussed above, it is normally not necessary to call the integral and sorting programs explicitly, but sometimes additional options are desired, and can be specified using the ``INT`` command, which should appear after geometry and basis specifications, and before any commands to evaluate an energy.

``INT, [[NO]SORT,] [SPRI=value]``

``SORT, [SPRI=value]``

``INT,NOSORT;SORT`` can be used to explicitly separate the integral evaluation and sorting steps, for example to collect separate timing data. With *value* set to more than 1 in the ``SPRI`` option, all the two-electron integrals are printed.

The detailed options for the integral sort can be specified using the ``AOINT`` parameter set, using the input form

``AOINT, key1=value1, key2=value2, $\dots$``

``AOINT`` can be used with or without an explicit ``INT`` command.

The following summarizes the possible keys, together with their meaning, and default values.

* **c_final** Integer specifying the compression algorithm to be used for the final sorted integrals. Possible values are 0 (no compression), 1 (compression using 1, 2, 4 or 8-byte values), 2 (2, 4 or 8 bytes), 4 (4, 8 bytes) and 8. Default: 0
* **c_sort1** Integer specifying the compression algorithm for the intermediate file during the sort. Default: 0
* **c_seward** Integer specifying the format of label tagging and compression written by the integral program and read by the sort program. Default: 0
* **compress** Overall compression; c_final, c_seward and c_sort1 are forced internally to be not less than this parameter. Default: 1
* **thresh** Real giving the truncation threshold for compression. Default: :math:`0.0`, which means use the integral evaluation threshold (``GTHRESH,TWOINT``)
* **io** String specifying how the sorted integrals are written. Possible values are ``molpro`` (standard ``Molpro`` record on file 1) and ``eaf`` (Exclusive-access file). ``eaf`` is permissible only if the program has been configured for MPP usage, and at present ``molpro`` is implemented only for serial execution. ``molpro`` is required if the integrals are to be used in a restart job. For maximum efficiency on a parallel machine, ``eaf`` should be used, since in that case the integrals are distributed on separate processor-local files.

For backward-compatibility purposes, two convenience commands are also defined: ``COMPRESS`` is equivalent to ``AOINT,COMPRESS=1``, and ``NOCOMPRESS`` is equivalent to ``AOINT,COMPRESS=0``.

.. _integration--imported-hamiltonian:

Imported hamiltonian
====================

It is possible to import the second-quantised hamiltonian completely from outside ``Molpro``. In order to do so, it is necessary to set up a job that simulates the desired calculation by having a basis set of exactly the same dimensions as the one to be imported. One can then import the hamiltonian using the command

``HAMILTONIAN,filename``

*filename* is the name of a file that contains the hamiltonian in `FCIDUMP <https://github.com/molpro/fcidump>`__ format, which can be produced using Molpro’s ``{FCI,DUMP=}`` facility, or by another method.

Note that this facility is fragile, and is limited to energy-only calculations. Attempts to calculate gradients or other properties will inevitably fail. At present, the implementation does not support the use of point-group symmetry.

.. _integration--integral-direct-calculations-gdirect:

INTEGRAL-DIRECT CALCULATIONS (GDIRECT)
======================================

References:

Direct methods, general: M. Schütz, R. Lindh, and H.-J. Werner, `Mol. Phys. <https://dx.doi.org/10.1080/00268979909483008>`__ **96**, 719 (1999).
Linear scaling LMP2: M. Schütz, G. Hetzer, and H.-J. Werner `J. Chem. Phys. <https://dx.doi.org/10.1063/1.479957>`__ **111**, 5691 (1999).

Most methods implemented in ``MOLPRO`` can be performed integral-direct, i.e., the methods are integral driven with the two-electron integrals in the AO basis being recomputed whenever needed, avoiding the bottleneck of storing these quantities on disk. Exceptions are currently full CI (FCI), perturbative triple excitations (T), ``UMP2``, ``RMP2``, ``CPP``, ``MRCI-F12``, and ``RS2-F12``. For small molecules, this requires significantly more CPU time, but reduces the disk space requirements when using large basis sets. However, due to efficient prescreening techniques, the scaling of the computational cost with molecular size is lower in integral-direct mode than in conventional mode, and therefore integral-direct calculations for extended molecules may even be less expensive than conventional ones. The break-even point depends strongly on the size of the molecule, the hardware, and the basis set. Depending on the available disk space, calculations with more than 150–200 basis functions in one symmetry should normally be done in integral-direct mode.

Integral-direct calculations are requested by the ``DIRECT`` or ``GDIRECT`` directives. If one of these cards is given outside the input of specific programs it acts globally, i.e. all subsequent calculations are performed in integral-direct mode. On the other hand, if the ``DIRECT`` card is part of the input of specific programs (e.g. ``HF``, ``CCSD``), it affects only this program. The ``GDIRECT`` directive is not recognized by individual programs and always acts globally. Normally, all calculations in one job will be done integral-direct, and then a ``DIRECT`` ``or GDIRECT`` card is required before the first energy calculation. However, further ``DIRECT`` or ``GDIRECT`` directives can be given in order to modify specific options or thresholds for particular programs.

The integral-direct implementation in ``MOLPRO`` involves three different procedures: (i) Fock matrix evaluation (``DFOCK``), (ii) integral transformation (``DTRAF``), and (iii) external exchange operators (``DKEXT``). Specific options and thresholds exist for all three programs, but it is also possible to specify the most important thresholds by general parameters, which are used as defaults for all programs.

Normally, appropriate default values are automatically used by the program, and in most cases no parameters need to be specified on the ``DIRECT`` directive. However, in order to guarantee sufficient accuracy, the default thresholds are quite strict, and in calculations for extended systems larger values might be useful to reduce the CPU time.

The format of the ``DIRECT`` directive is

``DIRECT, key1=value1, key2=value2…``

The following table summarizes the possible keys and their meaning. The default values are given in the subsequent table. In various cases there is a hierarchy of default values. For instance, if ``THREST_D2EXT`` is not given, one of the following is used: [``THR_D2EXT``, ``THREST_DTRAF``, ``THR_DTRAF``, ``THREST``, *default*]. The list in brackets is checked from left to right, and the first one found in the input is used. *default* is a default value which depends on the energy threshold and the basis set (the threshold is reduced if the overlap matrix contains very small eigenvalues).

* **\*\*General Options (apply to all programs):**

\*\*

* ``THREST`` Integral prescreening threshold. The calculation of an integral shell block is skipped if the product of the largest estimated integral value (based on the Cauchy-Schwarz inequality) and the largest density matrix element contributing to the shell block is smaller than this value. In ``DTRAF`` and ``DKEXT`` effective density matrices are constructed from the MO coefficients and amplitudes, respectively.
* ``THRINT`` Integral prescreening threshold. This applies to the product of the exact (i.e. computed) integral value and a density matrix. This threshold is only used in ``DTRAF`` and ``DKEXT``. A shell block of integrals is skipped if the product of the largest integral and the largest element of the effective density matrix contributing to the shell block is smaller than this threshold. If it is set negative, no computed integrals will be neglected.
* ``THRPROD`` Prescreening threshold for products of integrals and MO-coefficients (``DTRAF``) or amplitudes (``DKEXT``). Shell blocks of MO coefficients or amplitudes are neglected if the product of the largest integral in the shell block and the largest coefficient is smaller than this value. If this is set negative, no product screening is performed.
* ``THRMAX`` Initial value of the prescreening threshold ``THREST`` for ``DFOCK`` and ``DKEXT`` in iterative methods (``SCF``, ``CI``, ``CCSD``). If nonzero, it will also be used for ``DKEXT`` in ``MP3`` and ``MP4(SDQ)`` calculations. The threshold will be reduced to ``THREST`` once a certain accuracy has been reached (see ``VARRED``), or latest after ``MAXRED`` iterations. In ``CI`` and ``CCSD`` calculations, also the initial thresholds ``THRINT_DKEXT`` and ``THRPROD_DKEXT`` are influenced by this value. For a description, see ``THRMAX_DKEXT``. If ``THRMAX``\ =0, the final thresholds will be used from the beginning in all methods.
* ``SCREEN`` Enables or disables prescreening.

``SCREEN$\ge 0$: full screening enabled.\\``
``SCREEN``\ :math:`\lt 0`: ``THRPROD`` is unused. No density screening in direct SCF.
``SCREEN``\ :math:`\lt -1`: ``THRINT`` is unused.
``SCREEN``\ :math:`\lt -2`: ``THREST`` is unused.

* ``MAXRED`` Maximum number of iterations after which thresholds are reduced to their final values in ``CI`` and ``CCSD`` calculations. If ``MAXRED``\ =0, the final thresholds will be used in ``CI`` and ``CCSD`` from the beginning (same as ``THRMAX``\ =0, but ``MAXRED`` has no effect on ``DSCF``. In the latter case a fixed value of 10 is used.
* ``VARRED`` Thresholds are reduced to their final values if the sum of squared amplitude changes is smaller than this value.
* ``SWAP`` Enables or disables label swapping in ``SEWARD``. Test purpose only.

* **\*\*Specific options for direct SCF (``DFOCK``):**

\*\*

* ``THREST_DSCF`` Final prescreening threshold in direct SCF. If given, it replaces the value of ``THREST``.
* ``THRMAX_DSCF`` Initial prescreening threshold in direct SCF. This is used for the first 7-10 iterations. Once a certain accuracy is reached, the threshold is reduced to ``THREST_DSCF``
* ``SWAP_DFOCK`` Enables or disables label swapping in fock matrix calculation (test purpose only).

* **\*\*General options for direct integral transformation (``DTRAF``)**:

\*\*

* ``PAGE_DTRAF`` Selects the transformation method.

``PAGE_DTRAF=0: use minimum memory algorithm, requiring four integral evaluations.\\``
``PAGE_DTRAF=1``: use paging algorithm,leading to the minimum CPU time (one integral evaluation for DMP2/LMP2 and two otherwise).

* ``SCREEN_DTRAF`` If given, replaces value of :math:`{\tt SCREEN}` for ``DTRAF``.
* ``MAXSHLQ1_DTRAF`` Maximum size of merged shells in the first quarter transformation step (0: not used).
* ``MINSHLQ1_DTRAF`` Shells are only merged if their size is smaller than this value (0: not used).
* ``MAXSHLQ2_DTRAF`` Maximum size of merged shells in the second quarter transformation step (0: not used).
* ``MINSHLQ2_DTRAF`` Shells are only merged if their size is smaller than this value (0: not used).
* ``MAXCEN_DTRAF`` Maximum number of centres in merged shells (0: no limit).
* ``PRINT_DTRAF`` Print parameter for ``DTRAF``.

* **\*\*General thresholds for all direct integral transformations:**\*\*
* ``THR_DTRAF`` General threshold for ``DTRAF``. If given, this is taken as default value for all thresholds described below.
* ``THREST_DTRAF`` AO prescreening threshold for ``DTRAF``.

``Defaults: [THR_DTRAF, THREST, default].``

* ``THRINT_DTRAF`` Integral threshold for ``DTRAF``.

``Defaults: [THR_DTRAF, THRINT, default].``

* ``THRPROD_DTRAF`` Product threshold for ``DTRAF``.

``Defaults: [THR_DTRAF, THRPROD, default].\\``

* **\*\*Thresholds specific to direct integral transformations:**\*\*
* ``THR_D2EXT`` General threshold for generation of 2-external integrals. If given, this is used as a default for all ``D2EXT`` thresholds described below.
* ``THREST_D2EXT`` Prescreening threshold for generation of 2-external integrals.

``Defaults: [THR_D2EXT, THREST_DTRAF, THR_DTRAF, THREST, default].``

* ``THRINT_D2EXT`` Integral threshold for generation of 2-external integrals.

``Defaults: [THR_D2EXT, THRINT_DTRAF, THR_DTRAF, THRINT, default].``

* ``THRPROD_D2EXT`` Product threshold for generation of 2-external integrals.

``Defaults: [THR_D2EXT, THRPROD_DTRAF, THR_DTRAF, THRPROD, default].\\``

* ``THR_D3EXT`` General threshold for generation of 3-external integrals. If given, this is used as a default for all ``D3EXT`` thresholds described below.
* ``THREST_D3EXT`` Prescreening threshold for generation of 3-external integrals.

``Defaults: [THR_D3EXT, THREST_DTRAF, THR_DTRAF, THREST, default].``

* ``THRINT_D3EXT`` Integral threshold for generation of 3-external integrals.

``Defaults: [THR_D3EXT, THRINT_DTRAF, THR_DTRAF, THRINT, default].``

* ``THRPROD_D3EXT`` Product threshold for generation of 3-external integrals.

``Defaults: [THR_D3EXT, THRPROD_DTRAF, THR_DTRAF, THRPROD, default].\\``

* ``THR_D4EXT`` General threshold for generation of 4-external integrals. If given, this is used as a default for all ``D4EXT`` thresholds described below.
* ``THREST_D4EXT`` Prescreening threshold for generation of 4-external integrals.

``Defaults: [THR_D4EXT, THREST_DTRAF, THR_DTRAF, THREST, default].``

* ``THRINT_D4EXT`` Integral threshold for generation of 4-external integrals.

``Defaults: [THR_D4EXT, THRINT_DTRAF, THR_DTRAF, THRINT, default].``

* ``THRPROD_D4EXT`` Product threshold for generation of 4-external integrals.

``Defaults: [THR_D4EXT, THRPROD_DTRAF, THR_DTRAF, THRPROD, default].\\``

* ``THR_DCCSD`` General threshold for generalized transformation needed in each CCSD iteration. If given, this is used as a default for ``THREST_DCCSD``, ``THRINT_DCCSD``, and ``THRPROD_DCCSD`` described below.
* ``THREST_DCCSD`` Prescreening threshold for DCCSD transformation.

``Defaults: [THR_DCCSD, THREST_DTRAF, THR_DTRAF, THREST, default].``

* ``THRINT_DCCSD`` Integral threshold for DCCSD transformation.

``Defaults: [THR_DCCSD, THRINT_DTRAF, THR_DTRAF, THRINT, default].``

* ``THRPROD_DCCSD`` Product threshold for DCCSD transformation.

``Defaults: [THR_DCCSD, THRPROD_DTRAF, THR_DTRAF, THRPROD, default].``

* ``THRMAX_DCCSD`` Initial value for ``THREST_DCCSD`` in ``CCSD`` calculations. The threshold will be reduced to ``THREST_DCCSD`` once a certain accuracy has been reached (see ``VARRED``), or latest after ``MAXRED`` iterations. The initial thresholds ``THRINT_DCCSD`` and ``THRPROD_DCCSD`` are obtained by multiplying their input (or default) values by ``THRMAX_DCCSD``/``THREST_DCCSD``, with the restriction that the initial values cannot be smaller than the final ones.

* **\*\*Specific options for direct MP2 (``DMP2``)**:\*\*
* ``DMP2`` Selects the transformation method for direct ``MP2``:

``DMP2``\ =\ :math:`-1`: automatic selection, depending on the available memory.
``DMP2=0: use fully direct method for DMP2 (min. two integral evaluations, possibly multipassing, no disk space).\\``
``DMP2``\ =1: use semi-direct method for ``DMP2`` (one to four integral evaluations, depending on ``PAGE_DTRAF``).
``DMP2``\ =2: use ``DKEXT`` to compute exchange operators in ``DMP2`` (one integral evaluation). This is only useful in local ``DMP2`` calculations with many distant pairs.

* ``THR_DMP2`` General threshold for generation of 2-external integrals in DMP2. If given, this is used as a default for all ``DMP2`` thresholds described below.
* ``THREST_DMP2`` Prescreening threshold for generation of 2-external integrals.

``Defaults: [THR_DMP2, THREST_DTRAF, THR_DTRAF, THREST, default].``

* ``THRINT_DMP2`` Integral threshold for generation of 2-external integrals.

``Defaults: [THR_DMP2, THRINT_DTRAF, THR_DTRAF, THRINT, default].``

* ``THRPROD_DMP2`` Product threshold for generation of 2-external integrals

``Defaults: [THR_DMP2, THRPROD_DTRAF, THR_DTRAF, THRPROD, default].\\``

* **\*\*Specific options for direct local MP2 (``LMP2``)**:\*\*
* ``DTRAF`` Selects the transformation method for direct ``LMP2``:

``DTRAF`` :math:`\geq 0`: generates the 2-external integrals (exchange operators) first in AO basis and transforms these thereafter in a second step to the projected, local basis. The disk storage requirements hence scale cubically with molecular size.
``DTRAF`` :math:`= -1`: generates the 2-external integrals (exchange operators) directly in projected basis. The disk storage requirements hence scale linearly with molecular size. This (together with ``PAGE_DTRAF`` = 0) is the recommended algorithm for very large molecules (cf. linear scaling LMP2, chapter :doc:`PAO-based local correlation treatments <pao-based_local_correlation_treatments>`).
``DTRAF`` :math:`= -2`: alternative algorithm to generate the exchange operators directly in projected basis. Usually, this algorithm turns out to be computationally more expensive than the one selected with ``DTRAF`` :math:`= -1`. Note, that neither ``DTRAF`` :math:`= -1` nor ``DTRAF`` :math:`= -2` work in the context of LMP2 gradients.

* ``THR_LMP2`` General threshold for generation of 2-external integrals in linear scaling LMP2. If given, this is used as a default for all ``LMP2`` thresholds described below.
* ``THREST_LMP2`` Prescreening threshold for generation of 2-external integrals.

``Defaults: [THR_LMP2, THREST_DTRAF, THR_DTRAF, THREST, default].``

* ``THRQ1_LMP2`` Threshold used in the first quarter transformation.

``Defaults: [THR_LMP2, THRPROD_DTRAF, THR_DTRAF, THRPROD, default].``

* ``THRQ2_LMP2`` Threshold used in the second and subsequent quarter transformations.

``Defaults: [THR_LMP2, THRINT_DTRAF, THR_DTRAF, THRINT, default].``

* ``THRAO_ATTEN`` Special threshold for prescreening of attenuated integrals :math:`(\mu \mu | \nu \nu)`

``Default: THREST_LMP2\\``

* **\*\*Options for integral-direct computation of external exchange operators (``DKEXT``):**\*\*
* ``DKEXT`` Selects driver for ``DKEXT``.

``DKEXT=-1``: use paging algorithm (minimum memory). This is automatically used if in-core algorithm would need more than one integral pass.
``DKEXT``\ =0: use in-core algorithm, no integral triples.
``DKEXT``\ =1: use in-core algorithm and integral triples.
``DKEXT``\ =2: use in-core algorithm and integral triples if at least two integrals of a triple differ.
``DKEXT``\ =3: use in-core algorithm and integral triples if all integrals of a triple differ.

* ``SCREEN_DKEXT`` if given, replaces value of :math:`{\tt SCREEN}` for ``DKEXT``.
* ``MAXSIZE_DKEXT`` Largest size of merged shells in ``DKEXT`` (0: not used).
* ``MINSIZE_DKEXT`` Shells are only merged if their size is smaller than this value. (0: not used).
* ``MAXCEN_DKEXT`` Maximum number of centres in merged shells (0: no limit).
* ``SCREEN_DKEXT`` Enables of disables screening in ``DKEXT``.
* ``PRINT_DKEXT`` Print parameter for ``DKEXT``.
* ``SWAP_DKEXT`` Enables of disables label swapping in ``DKEXT`` (test purpose only)
* ``MXMBLK_DKEXT`` Largest matrix block size in ``DKEXT`` (only used with ``DKEXT``\ :math:`\ge 1`).

* **\*\*Thresholds for integral-direct computation of external exchange operators (``DKEXT``):**\*\*
* ``THR_DKEXT`` General threshold for ``DKEXT``. If given, this is used as a default for all ``DKEXT`` thresholds described below.
* ``THREST_DKEXT`` Prescreening threshold for ``DKEXT``.

``Defaults: [THR_DKEXT, THREST, default].``

* ``THRINT_DKEXT`` Integral threshold for ``DKEXT``.

``Defaults: [THR_DKEXT, THRINT, default].``

* ``THRPROD_DKEXT`` Product threshold for ``DKEXT``.

``Defaults: [THR_DKEXT, THRPROD, default].``

* ``THRMAX_DKEXT`` Initial value for ``THREST_DKEXT`` in ``CI``, and ``CCSD`` calculations. If nonzero. it will also be used for ``DKEXT`` in ``MP3`` and ``MP4(SDQ)`` calculations. The threshold will be reduced to ``THREST_DKEXT`` once a certain accuracy has been reached (see ``VARRED``), or latest after ``MAXRED`` iterations. The initial thresholds ``THRINT_DKEXT`` and ``THRPROD_DKEXT`` are obtained by multiplying their input (or default) values by ``THRMAX_DKEXT``/``THREST_DKEXT``, with the restriction that the initial values cannot be smaller than the final ones.

For historical reasons, many options have alias names. The following tables summarize the default values for all options and thresholds and also gives possible alias names.

.. list-table::
   :header-rows: 2

   * - Default values and alias names for ``direct`` options.
     - 
     - 
   * - Parameter
     - Alias
     - Default value
   * - ``SCREEN``
     - 
     - :math:`1`
   * - ``MAXRED``
     - 
     - :math:`7`
   * - ``VARRED``
     - 
     - 1.d-7
   * - ``SWAP``
     - 
     - :math:`1`
   * - ``SWAP_DFOCK``
     - 
     - ``SWAP``
   * - ``DMP2``
     - ``DTRAF``
     - :math:`-1`
   * - ``PAGE_DTRAF``
     - ``PAGE``
     - :math:`1`
   * - ``SCREEN_DTRAF``
     - 
     - ``SCREEN``
   * - ``MAXSHLQ1_DTRAF``
     - ``NSHLQ1``
     - :math:`32`
   * - ``MINSHLQ1_DTRAF``
     - 
     - :math:`0`
   * - ``MAXSHLQ2_DTRAF``
     - ``NSHLQ2``
     - :math:`16`
   * - ``MINSHLQ2_DTRAF``
     - 
     - 0
   * - ``MAXCEN_DTRAF``
     - 
     - 0
   * - ``PRINT_DTRAF``
     - 
     - :math:`-1`
   * - ``SWAP_DTRAF``
     - 
     - ``SWAP``
   * - ``DKEXT``
     - ``DRVKEXT``
     - :math:`3`
   * - ``SCREEN_DKEXT``
     - 
     - ``SCREEN``
   * - ``MAXSIZE_DKEXT``
     - 
     - :math:`0`
   * - ``MINSIZE_DKEXT``
     - 
     - :math:`5`
   * - ``MAXCEN_DKEXT``
     - 
     - :math:`1`
   * - ``PRINT_DKEXT``
     - 
     - :math:`-1`
   * - ``SWAP_DKEXT``
     - 
     - ``SWAP``
   * - ``MXMBLK_DKEXT``
     - 
     - depends on hardware (-B parameter on ``molpro`` command)

.. list-table::
   :header-rows: 2

   * - Default thresholds and alias names for ``direct`` calculations
     - 
     - 
   * - Parameter
     - Alias
     - Default value
   * - ``THREST``
     - ``THRAO``
     - :math:`\min(\Delta E \cdot 1.d-2,1.d-9)^{a,b}`
   * - ``THRINT``
     - ``THRSO``
     - :math:`\min(\Delta E \cdot 1.d-2,1.d-9)^{a,b}`
   * - ``THRPROD``
     - ``THRP``
     - :math:`\min(\Delta E \cdot 1.d-3,1.d-10)^{a,b}`
   * - ``THRMAX``
     - 
     - 1.d-8\ :math:`^b`
   * - ``THREST_DSCF``
     - ``THRDSCF``
     - :math:`\le` 1.d-10 (depending on accuracy and basis set)
   * - ``THRMAX_DSCF``
     - ``THRDSCF_MAX``
     - ``THRMAX``
   * - ``THR_DTRAF``
     - ``THRDTRAF``
     - 
   * - ``THREST_DTRAF``
     - ``THRAO_DTRAF``
     - [``THR_DTRAF``, ``THREST``]
   * - ``THRINT_DTRAF``
     - ``THRAO_DTRAF``
     - [``THR_DTRAF``, ``THRINT``]
   * - ``THRPROD_DTRAF``
     - ``THRP_DTRAF``
     - [``THR_DTRAF``, ``THRPROD``]
   * - ``THR_D2EXT``
     - ``THR2EXT``
     - ``THR_DTRAF``
   * - ``THREST_D2EXT``
     - ``THRAO_D2EXT``
     - [``THR_D2EXT``, ``THREST_DTRAF``]
   * - ``THRINT_D2EXT``
     - ``THRSO_D2EXT``
     - [``THR_D2EXT``, ``THRINT_DTRAF``]
   * - ``THRPROD_D2EXT``
     - ``THRP_D2EXT``
     - [``THR_D2EXT``, ``THRPROD_DTRAF``]
   * - ``THR_D3EXT``
     - ``THR3EXT``
     - ``THR_DTRAF``
   * - ``THREST_D3EXT``
     - ``THRAO_D3EXT``
     - [``THR_D3EXT``, ``THREST_DTRAF``]
   * - ``THRINT_D3EXT``
     - ``THRSO_D3EXT``
     - [``THR_D3EXT``, ``THRINT_DTRAF``]
   * - ``THRPROD_D3EXT``
     - ``THRP_D3EXT``
     - [``THR_D3EXT``, ``THRPROD_DTRAF``]
   * - ``THR_D4EXT``
     - ``THR4EXT``
     - ``THR_DTRAF``
   * - ``THREST_D4EXT``
     - ``THRAO_D4EXT``
     - [``THR_D4EXT``, ``THREST_DTRAF``]
   * - ``THRINT_D4EXT``
     - ``THRSO_D4EXT``
     - [``THR_D4EXT``, ``THRINT_DTRAF``]
   * - ``THRPROD_D4EXT``
     - ``THRP_D4EXT``
     - [``THR_D4EXT``, ``THRPROD_DTRAF``]
   * - ``THR_DCCSD``
     - ``THRCCSD``
     - ``THR_DTRAF``
   * - ``THREST_DCCSD``
     - ``THRAO_DCCSD``
     - [``THR_DCCSD``, ``THREST_DTRAF``]
   * - ``THRINT_DCCSD``
     - ``THRSO_DCCSD``
     - [``THR_DCCSD``, ``THRINT_DTRAF``]
   * - ``THRPROD_DCCSD``
     - ``THRP_DCCSD``
     - [``THR_DCCSD``, ``THRPROD_DTRAF``]
   * - ``THRMAX_DCCSD``
     - ``THRMAX_DTRAF``
     - ``THRMAX``
   * - ``THR_DMP2``
     - ``THRDMP2``
     - ``THR_DTRAF``
   * - ``THREST_DMP2``
     - ``THRAO_DMP2``
     - [``THR_DMP2``, ``THREST_DTRAF``, *default*\ :math:`^c`]
   * - ``THRINT_DMP2``
     - ``THRSO_DMP2``
     - [``THR_DMP2``, ``THRINT_DTRAF``, *default*\ :math:`^c`]
   * - ``THRPROD_DMP2``
     - ``THRP_DMP2``
     - [``THR_DMP2``, ``THRPROD_DTRAF``, *default*\ :math:`^c`]
   * - ``THR_LMP2``
     - ``THRLMP2``
     - ``THR_DTRAF``
   * - ``THREST_LMP2``
     - ``THRAO_LMP2``
     - [``THR_LMP2``, ``THREST_DTRAF``, *default*\ :math:`^c`]
   * - ``THRQ1_LMP2``
     - ``THRQ1``
     - [``THR_LMP2``, ``THRPROD_DTRAF``, *default*\ :math:`^c`]
   * - ``THRQ2_LMP2``
     - ``THRQ2``
     - [``THR_LMP2``, ``THRINT_DTRAF``, *default*\ :math:`^c`]
   * - ``THRAO_ATTEN``
     - ``THRATTEN``
     - ``THREST_LMP2``
   * - ``THR_DKEXT``
     - ``THRKEXT``
     - 
   * - ``THREST_DKEXT``
     - ``THRAO_DKEXT``
     - [``THR_DKEXT``, ``THREST``]
   * - ``THRINT_DKEXT``
     - ``THRSO_DKEXT``
     - [``THR_DKEXT``, ``THRINT``]
   * - ``THRPROD_DKEXT``
     - ``THRP_DKEXT``
     - [``THR_DKEXT``, ``THRPROD``]
   * - ``THRMAX_DKEXT``
     - 
     - ``THRMAX``

a) :math:`\Delta E` is the requested accuracy in the energy (default 1.d-6).
b) The thresholds are reduced if the overlap matrix has small eigenvalues.
c) The default thresholds for DMP2 and LMP2 are :math:`0.1 \cdot {\Delta E}`.

.. _integration--example-for-integral-direct-calculations:

Example for integral-direct calculations
========================================

.. code-block:: text
   :caption: examples/h2o_direct.inp

   $method=[hf,mp2,ccsd,qci,bccd,multi,mrci,acpf,rs3]              !some methods
   basis=vdz                                                      !basis
   geometry={o;h1,o,r;h2,o,r,h1,theta}                            !geometry
   gdirect                                                        !direct option
   r=1 ang,theta=104                                              !bond length and angle
   do i=1,#method                                                 !loop over methods
   $method(i)                                                     !run method(i)
   e(i)=energy                                                    !save results in variables
   dip(i)=dmz
   enddo
   table,method,e,dip                                             !print table of results

This job produces the following table:

.. code-block:: text

    METHOD       E            DIP
    HF       -76.02145798   0.82747348
    MP2      -76.22620591   0.00000000
    CCSD     -76.23580191   0.00000000
    QCI      -76.23596211   0.00000000
    BCCD     -76.23565813   0.00000000
    MULTI    -76.07843443   0.76283026
    MRCI     -76.23369819   0.76875001
    ACPF     -76.23820180   0.76872802
    RS3      -76.23549448   0.75869972
