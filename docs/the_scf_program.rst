.. raw:: html

   <span id="configuration-averaged-hartree-fock-cahf-or-df-cahf"></span>

.. raw:: html

   <span id="convergence-threshold"></span>

.. raw:: html

   <span id="defining-the-number-of-occupied-orbitals-in-each-symmetry"></span>

.. raw:: html

   <span id="defining-the-wavefunction"></span>

.. raw:: html

   <span id="direct-scf"></span>

.. raw:: html

   <span id="expectation-values"></span>

.. raw:: html

   <span id="handling-difficult-cases-when-scf-does-not-converge"></span>

.. raw:: html

   <span id="handling-difficult-cases-when-the-scf-cycle-does-not-converge"></span>

.. raw:: html

   <span id="initial-orbital-guess"></span>

.. raw:: html

   <span id="interpolation"></span>

.. raw:: html

   <span id="level-shifts"></span>

.. raw:: html

   <span id="local-density-fitting-configuration-averaged-hartree-fock-ldf-cahf"></span>

.. raw:: html

   <span id="local-density-fitting-hartree-fock"></span>

.. raw:: html

   <span id="maximum-number-of-iterations"></span>

.. raw:: html

   <span id="options"></span>

.. raw:: html

   <span id="options-for-the-so-sci-optimization"></span>

.. raw:: html

   <span id="polarizabilities"></span>

.. raw:: html

   <span id="print-options"></span>

.. raw:: html

   <span id="reorthonormalization-of-the-orbitals"></span>

.. raw:: html

   <span id="rotating-pairs-of-orbitals"></span>

.. raw:: html

   <span id="sanity-check-on-the-energy"></span>

.. raw:: html

   <span id="saving-the-final-orbitals"></span>

.. raw:: html

   <span id="specifying-closed-shell-orbitals"></span>

.. raw:: html

   <span id="specifying-open-shell-orbitals"></span>

.. raw:: html

   <span id="starting-with-previous-orbitals"></span>

.. raw:: html

   <span id="using-additional-point-group-symmetry"></span>

.. _the_scf_program--the-scf-program:

The SCF program
===============

The Hartree-Fock self-consistent field program is invoked by one of the following commands:

* **``HF`` or ``RHF``** calls the spin-restricted Hartree-Fock program
* **``UHF`` or ``UHF-SCF``,\ *options*** calls the spin-unrestricted Hartree-Fock program

In contrast to older versions of ``molpro``, the ``HF`` and ``RHF`` directives have identical functionality and can both be used for closed-shell or open-shell calculations. Other aliases are ``HF-SCF`` or ``RHF-SCF``.

Often, no further input is necessary. By default, the number of electrons is equal to the nuclear charge.
The wavefunction is assumed to be totally symmetric (symmetry 1) for singlet calculations.
The program attempts to determine the occupation numbers and the ground state configuration from the Aufbau principle. Normally, this works well in closed-shell and many open-shell cases, but sometimes wrong occupations are obtained.
Then the wave function symmetry and spin need to be specified using a WF (wave function) directive.
Also, the ``OCC`` and/or ``CLOSED`` directives can be used to force convergence to the desired state. The default behaviour can be modified either by options on the command line, or by directives.

In open-shell cases, we recommend to use the ``WF``, ``OCC``, ``CLOSED``, or ``OPEN`` cards to define the wavefunction uniquely. Other commands frequently used are ``START`` and ``ORBITAL`` (or ``SAVE``) to modify the default records for starting and optimized orbitals, respectively. The ``SHIFT`` option or directive allows to modify the level shift in the RHF program, and ``EXPEC`` to calculate expectation values of one-electron operators (see section `One-electron operators and expectation values (GEXPEC) <program_control.html#one-electron-operators-and-expectation-values-gexpec>`__). Section `handling difficult cases: When SCF does not converge <the_scf_program.html#handling-difficult-cases-when-scf-does-not-converge>`__ discusses strategies for dealing difficult molecules and convergence problems. Since Molpro 2020, it is recommended to use the new first-order mcscf program ``MULTI,SO-SCI`` in such cases.
With Molpro 2021 or later, it is also possible to use ``HF,SO-SCI``, which is equivalent to ``MULTI,SO-SCI``, except that the Hartree-Fock default occupations and options are used.
Also, a quadratic optimization of the RHF energy can be activated by ``HF,SO``.
These options are not available for UHF or local density fitting.

.. _the_scf_program--density-fitting-hartree-fock:

Density fitting Hartree-Fock
============================

Density fitting can be used for closed and open-shell (RHF and UHF) HF and is invoked by a prefix ``DF-`` (``DF-HF``, ``DF-RHF``, or ``DF-UHF``), see section :doc:`density fitting <density_fitting>`). Density fitting very much speeds up calculations for large molecules and is strongly recommended. The greatest savings are seen for large basis sets with high angular momentum functions. The DF-HF program is well parallelized. Density fitting also works well for Kohn-Sham (``DF-KS`` or ``DF-UKS``) calculations.

.. _the_scf_program--local-density-fitting-hartree-fock:

Local density fitting Hartree-Fock
==================================

Using

.. code-block:: text

   LDF-HF, options
   LDF-RHF, options
   LDF-UHF, options

enables the new local density fitting Hartree-Fock program described in C. Köppl and H.-J. Werner, `J. Chem. Theory Comput. <https://dx.doi.org/10.1021/acs.jctc.6b00251>`__ **12**, 3122 (2016) (``LDF-HF`` and ``LDF-RHF`` are the same). For large and dense 3-dimensional systems this can speed up DF-HF calculations typically by a factor of 4-5, and even more if run in parallel or for extended 1- or 2-dimensional systems. Since the total HF energy is rather sensitive to the local fitting approximation, the final energy is either recomputed without local fitting (default), or with larger domains. Typically, with default options, :math:`\mu`\ H accuracy of the absolute HF energy is achieved, and the effect of the approximations on relative energies is negligible. This is also true for subsequent local coupled-cluster calculations (see section :doc:`local correlation methods with pair natural orbitals (PNOs) <local_correlation_methods_with_pair_natural_orbitals_pnos>`). The program is well parallelized and can also be run across several computer nodes.

The following options can be used to affect the local approximations:

* **``IDFDOM_LSCF=``\ *value*** Connectivity criterion for fitting domains (default 3).
* **``RDFDOM_LSCF=``\ *value*** Distance criterion for fitting domains (default 7 bohr).
* **``FITMOS_LSCF=``\ *thresh*** Threshold for LMO domains (default :math:`10^{-6})`.
* **``FITENERGY=``\ *value*** If nonzero, recompute the final energy without local fitting (default). If set to zero, the domain parameters below are used for computing the final energy.
* **``DYNFIT=``\ *value*** If non-zero and ``FITENERGY=0``, increase ``IDFDOM_LSCF`` by ``DYNFIT`` and ``RDFDOM_LSCF`` by 2\*\ ``DYNFIT`` for computing the final energy (default 0).
* **``RDFDOM_LFINAL``\ =\ *value*** Connectivity criterion for fitting domains in the last iteration (default 6, only used if ``DYNFIT=0`` and ``FITENERGY=0``).
* **``IDFDOM_LFINAL``\ =\ *value*** Distance criterion for fitting domains in the last iteration

(default 13 bohr, only used if ``DYNFIT=0`` and ``FITENERGY=0``).

* **``FITMOS_LFINAL``\ =\ *thresh*** Threshold for LMO domains in the last iteration (default :math:`10^{-8}`, only used if ``DYNFIT=0`` and ``FITENERGY=0``).
* **``ROTDIAG=``\ *iter*** Use fast rotational update of the orbitals, starting in iteration *iter* (default 3). Setting ``ROTDIAG=0`` disables the method and uses full diagonalization of the Fock matrix.

Other options are as in the standard HF and DF-HF programs. Please refer section :doc:`density fitting <density_fitting>` for more options regarding density fitting.

For more information about local fitting see R. Polly, H.-J. Werner, F. R. Manby, and Peter J. Knowles, *Fast Hartree-Fock theory using local density fitting approximations*, `Mol. Phys. <https://dx.doi.org/10.1080/0026897042000274801>`__ **102**, 2311 (2004) and C. Köppl and H.-J. Werner, `J. Chem. Theory Comput. <https://dx.doi.org/10.1021/acs.jctc.6b00251>`__ **12**, 3122-3134 (2016).

**All publications resulting from LDF-HF or LDF-KS calculations should cite this work.**

.. _the_scf_program--configuration-averaged-hartree-fock-cahf-or-df-cahf:

Configuration-averaged Hartree-Fock (CAHF or DF-CAHF)
=====================================================

This program (available since Molpro2020.3) is called using

.. code-block:: text

   cahf,options

or, with density fitting,

.. code-block:: text

   df-cahf,options

It yields orbitals which are equivalent to the orbitals of a state-averaged CASSCF calculation averaging over all states of all possible spin-manifolds given by a chosen active space, where the states of different spin-manifolds are given weighting factors corresponding to their MS-degeneracy. It is also possible to define two or more shells of active orbitals, and the calculation is then equivalent to a state-averaged RASSCF (restricted active space) calculation in which the configuration space is the direct product of the given CASSCF subspaces.

The active orbitals always follow the closed-shell ones, and it is essential to start with a qualitatively correct set of active orbitals in order to converge to the desired solution. The AVAS procedure is often very helpful to define the active space, see below.

The active space must be defined in one of the following ways (or consistent combinations of these):

* Using OCC and CLOSED directives following the command line.
* By specifying the active orbitals explicitly using SHELL directives.

SHELL directives are mandatory if more than one active shell is used. For each shell the active orbitals are specified as

.. code-block:: text

   SHELL,nel,orbital list

where ``nel`` is the number of electrons in the active shell and
``orbital list is given in the form number1.sym1,number2.sym2,.... Orbital numbers in the same symmetry must be consecutive. A range of orbitals in the same symmetry can be given as number1.sym,-number2.sym, which means from number1 to number2. The lowest orbital in a symmetry isym on any SHELL directive must equal iclos(isym)+1, where iclos(isym) is the number of closed-shell orbitals in the symmetry as given on a CLOSED directive. The highest orbital in symmetry isym on any SHELL directive equals iocc(isym), where iocc(isym) is the total number of occupied orbitals, as defined on an OCC directive, and any orbitals in-between must be defined on the SHELL directives. IF OCC and/or CLOSED directives are not given, the number of occupied and closed-shell orbitals is derived from the SHELL directive(s). But this only works if all symmetries occur on them.``

``OPTIONS can be the same as described for HF or DF-HF. The most useful ones in the context of CAHF are``

* **``SHIFTC=``\ *value***: shift for closed shell orbitals (negative means shifting down), default -0.6 Hartree.
* **``SHIFTO=``\ *value***: shift for open-shell (active) orbitals, default -0.3  Hartree.
* **``MINGAP=``\ *value***: minimal energy gaps between closed-active and active-virtual orbitals (default 0.5 Hartree). If more than one shell is defined, an energy gap is ensured also between the shells. This parameter is essential for convergence of CAHF.

If a subsequent CASCI calculation using  MULTI is performed using the CAHF orbitals, the corresponding state-averaged CASSCF wave functions for the individual states are obtained. The orbitals can also be employed in subsequent multi-reference correlation methods, such as CASPT2 and MRCI. The program is for example useful for the efficient calculation of
transition-metal/lanthanide/actinide compounds, where many nearly degenerate spin-eigenstates are of interest.

Different optimization methods are available for the CAHF case. The default is the classic SCF optimization, but the SO-SCI and quadratic optimization of the RHF program are available as well.
They can be activated by ``CAHF,SO-SCI`` for the SO-SCI method, or ``CAHF,SO`` for the quadratic optimization.
It is recommended to use the ``CAHF,SO-SCI`` optimization, since it is often less expensive and more robust.
Note that it is also possible to carry out CAHF calculations using the `MULTI program <the_mcscf_program_multi.html#cahf-optimization-with-the-mcscf-program>`__.

Example:

.. code-block:: text

    geometry={O}
    basis=vdz
    {cahf
    occ,2,1,1,,1
    closed,2}

Alternative:

.. code-block:: text
   :caption: examples/o_cahf.inp

    geometry={O}
    basis=vdz
    {cahf
    closed,2
    shell,4,1.2,1.3,1.5}

This yields the same orbitals as

.. code-block:: text

   {multi
   occ,2,1,1,,1
   closed,2
   wf,spin=2,sym=4;weight,3
   wf,spin=2,sym=6;weight,3
   wf,spin=2,sym=7;weight,3 !3P states
   wf,spin=0,sym=1;state,3  !1D and 1s states
   wf,spin=0,sym=4          !1D
   wf,spin=0,sym=6          !1D
   wf,spin=0,sym=7          !1D
   }

In order to converge to the correct solution, appropriate starting orbitals are essential. This is not always given by the default density guess. The AVAS procedure may be used to obtain proper starting orbitals. An example with two Ytterbium atoms is given below. Previous cahf calculations (with a smaller basis set and local density fitting approximations) can be found in
`Phys. Chem. Chem. Phys. <https://dx.doi.org/10.1039/C9CP00785G>`__ **21**, 9769 (2019),
and the structure is from [[https://doi.org/10.1021/jacs.7b10714\|
J. Am. Chem. Soc.]] **140**, 2504–2513 (2018) (`yb_hq_no3.xyz <media/examples/yb_hq_no3.xyz>`__ geometry file)
The f-orbitals on each Yb atom form the two active shells. The AVAS orbitals are localised and ordered according to center numbers:

.. code-block:: text
   :caption: examples/Yb2.inp

   memory,200m 
   geometry=yb_hq_no3.xyz
   
   charge=-1
   basis=def2-tzvpp
   
   {avas,locorb=1,nela=26  ! 26 active electrons, localized orbitals
   center,1,4f             ! This assumes that the first 2 atoms are Yb
   center,2,4f}
   
   {df-cahf,so-sci;
   cahf,13,227.1,-233.1
   cahf,13,234.1,-240.1}
   

.. _the_scf_program--local-density-fitting-configuration-averaged-hartree-fock-ldf-cahf:

Local density fitting configuration-averaged Hartree-Fock (LDF-CAHF)
====================================================================

Using

.. code-block:: text

   LDF-CAHF

calls the local density fitting configuration-averaged Hartree-Fock (LDF-CAHF) described in P. P. Hallmen et. al, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.4998815>`__ **147**, 164101 (2017), and for multi-shell problems to `Phys. Chem. Chem. Phys. <https://dx.doi.org/10.1039/C9CP00785G>`__ **21**, 9769 (2019). The further input is the same as for the non-local variant.

Considering accuracy, the same holds as for LDF-RHF. Local approximations cause an overhead in the density fitting calculation of the Fock matrices, and speedups can only be expected for rather large systems. For a molecule as shown in the last example for df-cahf, the computation times of local and non-local calculations are very similar, and it is not worthwhile to use the local version.

.. _the_scf_program--options-for-the-scf-program:

Options for the SCF program
===========================

In this section the options for ``HF|RHF|UHF|CAHF`` are described. For further options affecting Kohn-Sham calculations see section :doc:`the density functional program <the_density_functional_program>`. For compatibility with previous *MOLPRO* versions, options can also be given on subsequent directives, as described in later sections.

.. _the_scf_program--options-to-control-hf-convergence:

Options to control HF convergence
=================================

* **``ACCU[RACY]``\ =\ *accu*** Convergence threshold for the density matrix (square sum of the density matrix element changes). If *accu*\ :math:`> 1`, a threshold of :math:`10^{-accu}`) is used. The default depends on the global ``ENERGY`` threshold, and the threshold is automatically tightened in geometry optimizations or frequency calculations (unless a tight threshold is given).
* **``ENERGY``\ =\ *thrden*** The convergence threshold for the energy. The default depends on the global ``ENERGY`` threshold.
* **``START``\ =\ *record*** Record holding start orbitals.
* **``SAVE|ORBITAL``\ =\ *record*** Dump record for orbitals.
* **``MAXIT``\ =\ *maxit*** Maximum number of iterations (default 60)
* **``SHIFTA|SHIFTC``\ =\ *shifta*** Level shift for closed-shell orbitals in RHF (default :math:`-0.3`) and :math:`\alpha`-spin orbitals in UHF (default 0).
* **``SHIFTB|SHIFTO``\ =\ *shiftb*** Level shift for open-shell orbitals in RHF and :math:`\beta`-spin orbitals in UHF (default 0)
* **``NITORD|NITORDER``\ =\ *nitord*** Starting with iteration *nitocc*, the orbital occupation pattern is kept fixed: The orbitals are reordered after each iteration to obtain maximum overlap with the closed-shell/open-shell/virtual spaces from the previous iteration. This takes only effect after *nitord* iterations. The default depends on the quality of the starting guess.
* **``NITSH|NITSHIFT``\ =\ *nitsh*** If the iteration count is smaller than *nitsh*, the shifts are set to zero. The default depends on the quality of the starting guess.
* **``NITCL|NITCLOSED``\ =\ *nitcl*** If the iteration count is smaller than *nitcl*, only the closed-shell part of the Fock matrix is used (default *nitcl*\ :math:`=0`). This option is left for compatibility purposes, it almost never helps.
* **``NITOCC``\ =\ *nitocc*** Starting with iteration *nitocc* the occupation pattern is kept fixed. The default depends on the quality of the starting guess.
* **``NITORT|NITORTH``\ =\ *nitort*** The orbitals are reorthonormalized after every *nitort* iterations. The default is *nitort*\ :math:`=10`.

Note that in case of a restart the iteration count starts with 3.

.. _the_scf_program--options-for-orbital-localization:

Options for orbital localization
================================

The following options can be used to localize the RHF orbitals (not implemented for UHF):

* **``LOCORB``\ =\ *value*** if set to 1, the valence orbitals are localized at the end (default 0).
* **``LOC_METHOD``\ =\ ``IBO|PM|BOYS|NPA``** determines localization method if ``LOCORB=1``. Default is IBO.

Only the valence orbitals are localized, and the options only work without symmetry. Alternatively the ``LOCALI`` program can be used for localization, which offers more flexible options.

.. _the_scf_program--options-for-the-diagonalization-method:

Options for the diagonalization method
======================================

In calculations with very large basis sets, the diagonalization time becomes a significant fraction of the total CPU time. This can be reduced using the orbital rotation method as described in R. Polly, H.-J. Werner, F. R. Manby, and Peter J. Knowles, `Mol. Phys. <https://dx.doi.org/10.1080/0026897042000274801>`__ **102**, 2311 (2004))

* **``MINROT``\ =\ *minrot*** If *minrot*\ :math:`\ge 0`, the orbital rotation method is employed. Explicit diagonalization of the full Fock matrix is performed in the first *minrot* iterations and in the last iteration. If *minrot*\ =0, a default is used which depends on the starting guess.
* **``NEXPR``\ =\ *nexpr*** Number of terms used in the exponential expansion of the unitary orbital transformation matrix (default 4).
* **``DEROT``\ =\ *nexpr*** Energy gap used in the orbital rotation method. For orbitals within :math:`\pm`\ *derot* hartree of the HOMO orbital energy the Fock matrix is constructed and diagonalized (default 1.0)
* **``JACOBI``\ =\ *jacobi*** If nonzero, use Jacobi diagonalization.

.. _the_scf_program--options-for-convergence-acceleration-methods-diis:

Options for convergence acceleration methods (DIIS)
===================================================

``For more details, see IPOL directive.``

* **``IPTYP``\ =\ *iptyp*** Interpolation type (default ``DIIS``, see ``IPOL`` directive).
* **``IPNIT|DIIS_START``\ =\ *ipnit*** First iteration for DIIS interpolation.
* **``IPSTEP|DIIS_STEP``\ =\ *ipstep*** Iteration increment for DIIS interpolation.
* **``MAXDIS|MAXDIIS``\ =\ *maxdis*** Max number of Fock matrices used in DIIS interpolation (default 10).

.. _the_scf_program--options-for-integral-direct-calculations:

Options for integral direct calculations
========================================

* ``DIRECT`` (logical). If given, do integral-direct HF.
* **``THRMIN|THRDSCF_MIN``\ =\ *value*** Final integral screening threshold for DSCF.
* **``THRMAX|THRDSCF_MAX``\ =\ *value*** Initial integral screening threshold for DSCF.
* **``THRINT|THRDSCF``\ =\ *value*** Same as ``THRDSCF_MIN``.
* **``PRESCREEN``\ =\ *value*** If nonzero, use density screening (default).
* **``DISKSIZE]``\ =\ *value*** Max disk size in Byte for semi-direct calculations (currently disabled).
* **``BUFSIZE``\ =\ *value*** Max memory buffer size for semi-direct calculations (currently disabled).
* **``THRDISK``\ =\ *value*** Threshold for writing integrals to disk (currently disabled).
* **``PRINT_DFOCK``\ =\ *value*** Print option for direct Fock matrix calculation.

.. _the_scf_program--special-options-for-uhf-calculations:

Special options for UHF calculations
====================================

* **``NATORB``\ =\ *record*** Save natural charge orbitals in given record.
* **``UNOMIN``\ =\ *unomin*** Minimum occupation number for UNO-CAS (default 0.02)
* **``UNOMAX``\ =\ *unomax*** Maximum occupation number for UNO-CAS (default 1.98)

.. _the_scf_program--options-for-polarizabilities:

Options for polarizabilities
============================

* **``POLARI``\ =\ *value*** If nonzero, compute analytical dipole polarizabilities. See also the ``POLARI`` directive (section `polarizabilities <the_scf_program.html#polarizabilities>`__), which allows to specify various one-electron operators (by default, the dipole operator is used).
* **``THRCPHF``\ =\ *thresh*** Threshold for CPHF if polarizabilities are computed (default 1.d-6).

.. _the_scf_program--printing-options:

Printing options
================

* **``PRINT|ORBPRINT``\ =\ *value*** Number of virtual orbitals to be printed. If *value*\ =0, the occupied orbitals are printed.
* **``DEBUG``\ =\ *value*** Option for debug print.
* **``THRPRINT``\ =\ *value*** Threshold for printing orbitals

thrprint=-1 : column-wise;
thrprint=0 : row-wise, as in Molpro2015 and earlier versions ;
thrprint :math:`>0`: print only coefficients that are larger than the threshold together with labels (default: thrprint=0.25)

.. _the_scf_program--options-for-the-so-sci-optimization:

Options for the SO-SCI optimization
===================================

Since Molpro 2021, it is possible to use the SO-SCI optimization of multi (see `so-sci <the_mcscf_program_multi.html#combined-first-and-second-order-optimization-default>`__) within the RHF program, which is activated by ``HF,SO-SCI``.
All open-shell orbitals are added to the active space and optimized at second-order level.
The remaining closed-virtual optimization is approximated at first-order level.
This often solves convergence problems for difficult open-shell systems.

In case of closed-shell systems, the HOMO and the LUMO orbital are put automatically into the active space and optimized quadratically.
The selection of the HOMO and LUMO orbitals is based on the orbital energies of the starting/input orbitals.
The following options are available for the selection:

* ``SO_SCI_THRESH`` Energy difference threshold for selecting similar orbitals (default: 0.0001) 
* ``SO_SCI_MAX_2`` Maximum number of closed-shell orbitals taken by the threshold criterion (default: 5)
* ``SO_SCI_MAX_0`` Maximum number of virtual orbitals taken by the threshold criterion (default: 5)

The selection can be also activated for open-shell systems by setting ``SO_SCI_THRESH`` manually.

As an alternative, the fully quadratic optimization is available by ``HF,SO``.

.. _the_scf_program--quadratic-optimization-of-the-avas-orbitals:

Quadratic optimization of the AVAS orbitals
===========================================

It is possible to optimize all active orbitals from the given starting record quadratically by setting ``HF,SO-SCI-ACTIVE``.
This enables for example the quadratic optimization of all active orbitals selected by the AVAS program, which often improves the convergence of transition metal complexes considerably for which the correct ordering of the 3d orbitals might be challenging.

.. _the_scf_program--defining-the-wavefunction:

Defining the wavefunction
-------------------------

The number of electrons and the total symmetry of the wavefunction are specified on the ``WF`` card:

``WF,elec,sym,spin``

where

* ***elec*** is the number of electrons
* ***sym*** is the number of the irreducible representation
* ***spin*** defines the spin symmetry, :math:`spin=2*S` (singlet=0, doublet=1, triplet=2 etc.)

Note that these values take sensible defaults if any or all are not specified (see section `symmetry <general_program_structure.html#symmetry>`__). For example, ``{rhf; wf,sym=N,spin=M}`` gives the explicit values N for the symmetry and M for the spin of the wave function, but uses the default number of electrons.

In HF/RHF, the spin has to be equal to the number of singly occupied orbitals, i.e. the electrons couple to a high-spin state. For example, an open-shell singlet state cannot be described on this level. Instead, for states which are not high-spin, MCSCF has to be used.

.. _the_scf_program--defining-the-number-of-occupied-orbitals-in-each-symmetry:

Defining the number of occupied orbitals in each symmetry
---------------------------------------------------------

``OCC,$n_1,n_2,\ldots,n_8$``

To avoid convergence problems in cases with high symmetry, this card should be included whenever the occupation pattern is known in advance. :math:`n_i` is the number of occupied orbitals in the irreducible representation :math:`i`. The total number of orbitals must be equal to (*elec+spin*)/2 (see ``WF`` card).

.. _the_scf_program--specifying-closed-shell-orbitals:

Specifying closed-shell orbitals
--------------------------------

``CLOSED,$n_1,n_2,\ldots,n_8$``

This optional card can be used in open-shell calculations to specify the number of closed-shell orbitals in each symmetry. This makes possible to force specific states in the absence of an ``OPEN`` card.

.. _the_scf_program--specifying-open-shell-orbitals:

Specifying open-shell orbitals
------------------------------

``OPEN,$orb_1.sym_1,orb_2.sym_2,\ldots,orb_n.sym_n$``

This optional card can be used to specify the singly occupied orbitals. The number of singly occupied orbitals must be equal to *spin*, and their symmetry product must be equal to *sym* (see ``WF`` card). If the ``OPEN`` card is not present, the open shell orbitals are selected automatically. The algorithm tries to find the ground state, but it might happen that a wrong state is obtained if there are several possibilities for distributing the open shell electrons among the available orbitals. This can also be avoided using the ``CLOSED`` card. If :math:`orb_i.sym` is negative, this orbital will be occupied with negative spin (only allowed in UHF).

.. _the_scf_program--saving-the-final-orbitals:

Saving the final orbitals
~~~~~~~~~~~~~~~~~~~~~~~~~

``ORBITAL,record.file\\``
``SAVE,record.file``

The optimized orbitals, and the corresponding density matrix, fock matrix, and orbital energies are saved on *record.file*. ``SAVE`` is an alias for ``ORBITAL``. If this card is not present, the defaults for  *record* are:

* ``RHF`` 2100
* ``UHF`` 2200 (holds both :math:`\alpha` and :math:`\beta`-spin orbitals and related quantities)

These numbers are incremented by one for each subsequent calculation of the same type in the same input. Note that this holds for the sequence number in the input, independently in which order they are executed (see section `records <general_program_structure.html#records>`__).

The default for *file* is 2.

.. _the_scf_program--starting-orbitals:

Starting orbitals
~~~~~~~~~~~~~~~~~

The ``START`` directive can be used to specify the initial orbitals used in the SCF iteration. It is either possible to generate an initial orbital guess, or to start with previously optimized orbitals. Alternatively, one can also use a previous density matrix to construct the first fock operator.

If the ``START`` card is absent, the program tries to find suitable starting orbitals as follows:

* **First:** Try to read orbitals from *record* specified on the ``ORBITAL`` or ``SAVE`` card or the corresponding default (see ``ORBITAL``). All files are searched.
* **Second:** Try to find orbitals from a previous SCF or MCSCF calculation. All files are searched.
* **Third:** If no orbitals are found, the starting orbitals are generated using approximate atomic densities or eigenvectors of :math:`h` (see below).

Since these defaults are usually appropriate, the ``START`` card is not required in most cases.

.. _the_scf_program--initial-orbital-guess:

Initial orbital guess
---------------------

An initial orbital guess can be requested as follows:

``START,[TYPE=]option``

The *option* keyword can be:

* ``H0`` Use eigenvectors of :math:`h` (core Hamiltonian) as starting guess.
* ``ATDEN`` Use natural orbitals of a diagonal density matrix constructed using atomic orbitals and atomic occupation numbers (default).

Note that it is also possible to use orbitals from previous (e.g., smaller basis set) calculations as starting orbitals (see section `starting with previous orbitals <the_scf_program.html#starting-with-previous-orbitals>`__ below).

Example:

.. code-block:: text
   :caption: examples/h2o_sto3gstart1.inp

   r=1.85,theta=104          !set geometry parameters
   geometry={O;              !z-matrix geometry input
             H1,O,r;
             H2,O,r,H1,theta}
   basis=STO-3G              !first basis set
   hf                        !scf using STO-3G basis
   basis=6-311G              !second basis set
   hf                        !scf using 6-311G basis set

The second calculation uses the optimized orbitals of the STO-3G calculation as starting guess. This is done by default and no ``START`` card is necessary. The explicit use of ``START`` and ``SAVE`` cards is demonstrated in the example in the next section.

The following input is entirely equivalent to the one in the previous section:

.. code-block:: text
   :caption: examples/h2o_sto3gstart2.inp

   r=1.85,theta=104          !set geometry parameters
   geometry={O;              !z-matrix geometry input
             H1,O,r;
             H2,O,r,H1,theta}
   basis=STO-3G              !first basis set
   hf                        !scf using STO-3G basis
   start,atdens              !use atomic density guess
   save,2100.2               !save orbitals to record 2100.2
   basis=6-311G              !second basis set
   hf                        !scf using 6-311G basis set
   start,2100.2              !start with orbitals from the previous STO-3G calculation.
   save,2101.2               !save optimized orbitals to record 2101.2

Beware, however, that STO-3G is a very poor basis set and usually gives very bad starting vectors. This technique is best used in combination with reasonable small basis sets (e.g., cc-pVDZ or def2-SVP) or minimal basis sets with a proper representation of the occupied atomic orbitals (e.g, 6-31G or MINAO/MINAO-PP):

.. code-block:: text
   :caption: examples/minao_startorb.inp

   memory,50,m
   
   ! CuO2(NH3)4
   geometry={
    N    -2.244097     0.000000    -0.017684
    N     1.111652    -1.671116    -0.178974
    N     1.111652     1.671116    -0.178974
    N    -0.306059     0.000000    -2.311080
   Cu    -0.179579     0.000000    -0.290548
    O    -0.184327     0.000000     1.594789
    O     1.053213     0.000000     2.103145
    H    -2.331519     0.000000     1.002818
    H     0.614110     0.000000    -2.753879
    H    -0.793743     0.815054    -2.687415
    H    -0.793743    -0.815054    -2.687415
    H    -2.764729     0.814552    -0.345484
    H    -2.764729    -0.814552    -0.345484
    H     0.635193     2.543632     0.052739
    H     0.635193    -2.543632     0.052739
    H     1.616225     1.397092     0.672915
    H     1.616225    -1.397092     0.672915
    H     1.809254     1.910324    -0.883324
    H     1.809254    -1.910324    -0.883324
   }
   wf,charge=1,spin=2
   
   ! select all-electron minimal basis sets for H,N,O and ECP10 based basis
   ! set for Cu; using MINAO-PP here instead of MINAO allows us to project
   ! the obtained wave function on the cc-pVTZ-PP basis later on.
   basis=MINAO,Cu=MINAO-PP
   
   ! Run HF to get an initial guess for the valence electronic
   ! structure. The level shifts damp and stabilize the convergence.
   {rhf; shift,-1.0,-0.5; save,2100.2}
   
   ! select the actual basis set and start RHF with projected wave function
   ! from MINAO basis. nitord=1 asks RHF to reorder orbitals in each
   ! iteration to maximize overlap with the closed and active space
   ! from the last iteration.
   basis=AVTZ,Cu=VTZ-PP,H=VDZ(p)
   {df-rhf,nitord=1; start,2100.2}

.. _the_scf_program--starting-with-previous-orbitals:

Starting with previous orbitals
-------------------------------

``START,[RECORD=]record.file,[specifications]``

reads previously optimized orbitals from record *record* on file *file*. Optionally, a specific orbital set can be specified as described in section `selecting orbitals and density matrices (ORBITAL, DENSITY) <general_program_structure.html#selecting-orbitals-and-density-matrices-orbital-density>`__.

The specified dump record may correspond to a different geometry, basis set, and/or symmetry than used in the present calculation. Using starting orbitals from a different basis set can be useful if no previous orbitals are available and the ``ATDENS`` option cannot be used (see above).

The following example shows how to change the symmetry between scf calculations. Of course, this example is quite useless, but sometimes it might be easier first to obtain a solution in higher symmetry and then convert this to lower symmetry for further calculations.

.. code-block:: text
   :caption: examples/h2o_c2v_cs_start.inp

   r1=1.85,r2=1.85,theta=104          !set geometry parameters
   geometry={O;                       !z-matrix geometry input
             H1,O,r1;
             H2,O,r2,H1,theta}
   basis=vdz
   {hf                                !scf using c2v symmetry
   orbital,2100.2}                    !save on record 2100.2
   
   symmetry,x
   
   {hf
   start,2100.2                       !start with previous orbitals from c2v symmetry
   orbital,2101.2}                    !save new orbitals
   
   geometry={O;                       ! geometry has to be respecified so that
             H1,O,r1;                 ! H1 and H2 can be retagged as symmetry related
             H2,O,r2,H1,theta}
   symmetry,x,y
   {hf
   start,2101.2                       !start with orbitals from cs symmetry
   orbital,2102.2}                    !save new orbitals

Note, however, that this only works well if the orientation of the molecule does not change. Sometimes it might be helpful to use the ``noorient`` option.

Note also that a single dump record cannot hold orbitals for different basis dimensions. Using ``save=2100.2`` in the second calculation would therefore produce an error.

If orbitals from a corresponding SCF calculation at a neighbouring geometry are available, these should be used as starting guess.

.. _the_scf_program--starting-with-a-previous-density-matrix:

Starting with a previous density matrix
---------------------------------------

``START,DENSITY=record.file,[specifications]``

A density matrix is read from the given dump record and used for constructing the first fock matrix. A specific density matrix can be specified as described in section `selecting orbitals and density matrices (ORBITAL, DENSITY) <general_program_structure.html#selecting-orbitals-and-density-matrices-orbital-density>`__. It is normally not recommended to use the ``DENSITY`` option.

.. _the_scf_program--starting-with-avas-orbitals:

Starting with AVAS orbitals
---------------------------

Using the automated valence active space procedure (AVAS) procedure is often useful to generate a suitable starting guess for open-shell Hartree-Fock calculations. If no previous orbitals are available, AVAS first uses an atomic density guess to create initial orbitals, and these are the reordered according to input specifications. For example, d-orbitals in transition metal complexes can be rotated to the top of the occupied space. For more details see section :doc:`Automated construction of atomic valence active spaces <automated_construction_of_atomic_valence_active_spaces>`.

.. _the_scf_program--rotating-pairs-of-orbitals:

Rotating pairs of orbitals
~~~~~~~~~~~~~~~~~~~~~~~~~~

``ROTATE,$orb_1.sym,orb_2.sym,angle$``

Performs a :math:`2\times 2` rotation of the initial orbitals :math:`orb_1` and :math:`orb_2` in symmetry *sym* by *angle* degrees. With *angle*\ :math:`=0` the orbitals are exchanged. See ``MERGE`` for other possibilities to manipulate orbitals. In ``UHF``, by default only the :math:`\beta`-spin orbitals are rotated. The initial :math:`\alpha`-spin orbitals can be rotated using

``ROTATEA,$orb_1.sym,orb_2.sym,angle$``

In this case ``ROTATEB`` is an alias for ``ROTATE``.

.. _the_scf_program--using-additional-point-group-symmetry:

Using additional point-group symmetry
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Since *MOLPRO* can handle only Abelian point-groups, there may be more symmetry than explicitly used. For instance, if linear molecules are treated in :math:`C_{2v}` instead of :math:`C_{\infty v}`, the :math:`\delta_{(x^2-y^2)}`-orbitals appear in symmetry 1 (:math:`A_1`). In other cases, a linear geometry may occur as a special case of calculations in :math:`C_S` symmetry, and then one component of the :math:`\pi`-orbitals occurs in symmetry 1 (:math:`A'`). The program is able to detect such hidden “extra” symmetries by blockings in the one-electron hamiltonian :math:`h` and the overlap matrix :math:`S`. Within each irreducible representation, an “extra” symmetry number is then assigned to each basis function. These numbers are printed at the end of the integral output. Usually, the extra symmetries are ordered with increasing :math:`l`-quantum number of the basis functions. This information can be used to determine and fix the extra symmetries of the molecular orbitals by means of the ``SYM`` command.

``SYM,$irrep,sym(1),sym(2),,,sym(n)$``

:math:`sym(i)` are the extra symmetries for the first :math:`n` orbitals in the irreducible representation *irrep*. For instance, if you want that in a linear molecule the orbitals 1.1 to 3.1 are :math:`\sigma` and 4.1, 5.1 :math:`\delta`, the ``SYM`` card would read (calculation done with X,Y as symmetry generators):

``SYM,1,1,1,1,2,2``

If necessary, the program will reorder the orbitals in each iteration to force this occupation. The symmetries of occupied and virtual orbitals may be specified. By default, symmetry contaminations are not removed. If *irrep* is set negative, however, symmetry contaminations are removed. Note that this may prevent convergence if degenerate orbitals are present.

.. _the_scf_program--expectation-values:

Expectation values
~~~~~~~~~~~~~~~~~~

``EXPEC,$oper_1,oper_2,\ldots,oper_n$``

Calculates expectation values for one-electron operators :math:`oper_1`, :math:`oper_2`, :math:`\ldots`, :math:`oper_n`. See section `One-electron operators and expectation values (GEXPEC) <program_control.html#one-electron-operators-and-expectation-values-gexpec>`__ for the available operators. By default, the dipole moments are computed. Normally, it is recommended to use the ``GEXPEC`` directive if expectation values for other operators are of interest. See section `One-electron operators and expectation values (GEXPEC) <program_control.html#one-electron-operators-and-expectation-values-gexpec>`__ for details.

.. _the_scf_program--polarizabilities:

Polarizabilities
~~~~~~~~~~~~~~~~

``POLARIZABILITY[,$oper_1,oper_2,\ldots,oper_n$]``

Calculates polarizabilities for the given operators :math:`oper_1`, :math:`oper_2`, :math:`\ldots`, :math:`oper_n`.. See section `One-electron operators and expectation values (GEXPEC) <program_control.html#one-electron-operators-and-expectation-values-gexpec>`__ for the available operators. If no operators are specified, the dipole polarizabilities are computed.

Presently, this is working only for closed-shell without direct option.

The polarizabilities are stored in the variables ``POLXX, POLXY, POLXZ, POLYY, POLYZ, POLZZ``.

.. _the_scf_program--miscellaneous-directives:

Miscellaneous directives
~~~~~~~~~~~~~~~~~~~~~~~~

All commands described in this section are optional. Appropriate default values are normally used.

.. _the_scf_program--level-shifts:

Level shifts
------------

``SHIFT,shifta,shiftb``

A level shift of *shifta* and *shiftb* hartree for :math:`\alpha`- and :math:`\beta`-spin orbitals, respectively, is applied. This can improve convergence, but has no effect on the solution. *shifta*\ :math:`=-0.2` to :math:`-0.3` are typical values. The defaults are *shifta*\ :math:`=0` and *shifta*\ :math:`=-0.3` in closed and open-shell calculations, respectively, and *shiftb*\ :math:`=0`.

Applying large negative level shifts like ``{rhf; shift,-1.0,-0.5}`` will often stabilize convergence at the expense of making it somewhat slower. See section `handling difficult cases: When SCF does not converge <the_scf_program.html#handling-difficult-cases-when-scf-does-not-converge>`__.

.. _the_scf_program--maximum-number-of-iterations:

Maximum number of iterations
----------------------------

``MAXIT,maxit``

sets the maximum number of iterations to *maxit*. The default is *maxit*\ :math:`=60`.

.. _the_scf_program--convergence-threshold:

Convergence threshold
---------------------

``ACCU,accu This threshold applies to the square sum of the density matrix element changes (same as option ACCU). If accu$> 1$, a threshold of $10^{-accu}$) is used. The default depends on the global ENERGY threshold, and the threshold is automatically tightened in geometry optimizations or frequency calculations (unless a tight threshold is given).``

.. _the_scf_program--sanity-check-on-the-energy:

Sanity check on the energy
--------------------------

``NOENEST``

This disables the sanity check on the energy even if the energy value is unreasonable. Otherwise, the energy will be automatically checked by default.

.. _the_scf_program--print-options:

Print options
-------------

``ORBPRINT,print,test``

This determines the number of virtual orbitals printed at the end of the calculation. By default, *print*\ :math:`=0`, i.e., only the occupied orbitals are printed. *print*\ :math:`=-1` suppresses printing of orbitals entirely. *test*\ :math:`=1` has the additional effect of printing the orbitals after each iteration.

.. _the_scf_program--interpolation:

Interpolation
-------------

``IPOL,iptyp,ipnit,ipstep,maxdis``

This command controls iterative subspace interpolation. *iptyp* can be:

* ``DIIS`` direct inversion of the iterative subspace. This is the default and usually yields fast and stable convergence.
* ``KAIN`` Krylov-subspace accelerated inexact newton. A method similar to DIIS.
* ``NONE`` No interpolation.

:math:`ipnit` is the number of the iteration in which the interpolation starts (default: as soon as possible).  *ipstep* is the iteration increment between interpolations (default: 1, i.e., every iteration). *maxdis* is the maximum dimension of the DIIS matrix (default 10). *iptyp* and *maxdis* can also be set as options. E.g.,

``{rhf,maxdis=20,iptyp=’DIIS’; shift,-1.0,-0.5}``

.. _the_scf_program--reorthonormalization-of-the-orbitals:

Reorthonormalization of the orbitals
------------------------------------

``ORTH,nitort``

The orbitals are reorthonormalized after every *nitort* iterations. The default is *nitort*\ :math:`=10`.

.. _the_scf_program--direct-scf:

Direct SCF
----------

``DIRECT,options``

If this card is present, the calculation is done in direct mode. See section `INTEGRAL-DIRECT CALCULATIONS (GDIRECT) <integration.html#integral-direct-calculations-gdirect>`__ for options. Normally, it is recommended to use the global ``GDIRECT`` command to request the direct mode. See section `INTEGRAL-DIRECT CALCULATIONS (GDIRECT) <integration.html#integral-direct-calculations-gdirect>`__ for details.

.. _the_scf_program--handling-difficult-cases-when-scf-does-not-converge:

Handling difficult cases: When SCF does not converge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

General suggestions:

* Carry out convergence experiments with a small but reasonable basis set (e.g., cc-pVDZ, def2-SVP, aug-cc-pVDZ, ASVP). STO-3G is *not* a reasonable basis set.

Before you start you should check:

* Whether your geometry is sensible (e.g., look for Angstrom/Bohr conversion issues). Note that Molpro prints bond distances in both Angstroms and atomic units at the top of an output.
* Whether you have selected the correct electronic state (spin and symmetry). Molpro tries to guess spatial symmetries of open-shell compounds automatically if none are provided. However, the guess is not always right. In such a case you need to give the symmetry manually (in the simplest case as ``wf,sym=N,spin=M``. See section `defining the wavefunction <the_scf_program.html#defining-the-wavefunction>`__). Molpro does attempts to find the ground state configuration from the Aufbau principle, but this may fail and then the wave function symmetry and spin need to be specified using a WF (wave function) directive

If convergence problems persist, it is recommended to use the new mixed first-order/second-order MCSCF program (``MULTI,SO-SCI``, or (recommended for larger systems) ``DF-MULTI`` (SO-SCI is default for DF-MULTI) as described in D.A. Kreplin, P.J. Knowles and H.-J. Werner, J. Chem. Phys. 152, 074102 (2020); https://doi.org/10.1063/1.5142241. This provides very robust convergence, even in cases where RHF does not converge or converges to a wrong solution. Due to faster convergence and only small additional cost per iteration the overall computation time is often even smaller than for conventional RHF or DF-RHF. For MULTI it is necessary to specify the configuration uniquely using OCC, CLOSED, and WF directives.
See section :doc:`The MCSCF program MULTI <the_mcscf_program_multi>` for details.

With older Molpro versions, which do not contain the new MCSCF program, the following techniques can be attempted:

Hartree-Fock options & Small-basis initial guess:

* **Level shifts:** Adding a level shift like ``{rhf; shift,-1.0,-0.5}`` stabilizes the current RHF solution against changes and leads to smoother (but slower) convergence. That should be your first try; it is often sufficient.
* **Occupation freezing:** The option ``{rhf,nitord=N}`` can be used to freeze orbital occupations at iteration N. When the programs emits warnings about reassigned orbital occupations, you could try to freeze the occupations only later (give a higher N) or earlier (give a smaller N). By freezing the occupation pattern you tell the RHF program to try to lock on whatever solution it currently is pursuing. This often helps if multiple RHF solutions with similar energies are present and otherwise the program would oscillate between some of them. Note that ``{rhf,nitord=1}``\ will tell RHF to lock onto the initial occupation; if combined with orbital rotation or advanced initial guesses this can often be used to converge to specific solutions (e.g., some excited states).
* **Minimal-basis SCF guess:** Try to obtain a Hartree-Fock solution with a minimal-basis AO set first and to use this as initial guess for the actual Hartree-Fock calculation. For this purpose we provided the basis set definition "MINAO" (to complement cc-pVnZ basis sets) and "MINAO-PP" (to complement cc-pVnZ-PP sets with ECPs). See section `initial orbital guess <the_scf_program.html#initial-orbital-guess>`__ for an example. These sets simply consist of the AO part of the cc-pVTZ or cc-pVTZ-PP basis sets, stripped of all their polarization functions. Since a minimal basis has fewer degrees of freedom than a real basis set, convergence is often easier, and it can still provide reasonable guess for the valence electronic structure. Note: The MINAO basis sets are very small, so conventional Hartree-Fock (in integral-direct mode if necessary) is typically much faster than density-fitting Hartree-Fock.
* **Increasing the DIIS dimension:** In rare cases ``{rhf,maxdis=30,iptyp=’DIIS’,nitord=20; shift,-1.0,-0.5}`` can find solutions which are not found in the standard settings. Usually increasing the DIIS dimension beyond 10 (the default) just slows down convergence. It is also worthwhile to try a variation of DIIS known as KAIN (Krylov-subspace accelerated inexact Newton): ``{rhf,maxdis=10,iptyp=’KAIN’,nitord=10; shift,-1.0,-0.5}`` which sometimes shows different convergence behavior than straight DIIS.
* **AVAS** may be used to have a good initial guess for the orbitals.
* **sym** may be used to exploit extra symmetries.

Cationic or Anionic initial guess:

* If molecule :math:`X` does not converge, it might still be possible to converge :math:`X^+` (:math:`X^{2+}`, ..) and use this as initial guess for the actual computation. Particularly if :math:`X^+` is a closed-shell compound this will often work. If using this technique, you need to be careful about the final state you arrive in. Because your initial guess is biased, the :math:`X` calculation might converge to an excited state.

Density-functional initial guess:

* For transition metals and transition states sometimes DFT methods show better convergence behavior than RHF. You might perform a DFT calculation (possibly with a smaller basis set) and use it as initial guess for the SCF. E.g., ``{df-rks,b-lyp; coarsegrid; save,2100.2}`` ``{df-rhf,nitord=1; orbital,2100.2}``

If all else fails: Use the MCSCF program. The MCSCF program uses an advanced orbital optimization algorithm which is much more robust than the SCF method, and which can converge almost everything you give to it (but it is often slower and sometimes locks on an excited state if started from an atomic density guess). MCSCF can also calculate Hartree-Fock solutions if used with suitable input cards.

.. _the_scf_program--stability-check-eigenvalues-of-the-orbital-hessian:

Stability check: Eigenvalues of the orbital Hessian
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is possible to calculate the eigenvalues of the orbital Hessian with the MCSCF program (see `orbital Hessian eigenvalues <the_mcscf_program_multi.html#orbital-hessian-eigenvalues>`__ ) for a RHF wavefunction. This requires a manually given orbital occupation in the MCSCF program (see ``CLOSED`` and ``OCC``) similar to the RHF solution. The computation of the orbital Hessian is considerably more expansive than the RHF optimization. Negative eigenvalues show that the solution is a saddle point, and a lower energy could be found.

.. _the_scf_program--advanced-use-core-excited-states:

Advanced use: Core-excited states
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Some kinds of excited or higher ionized states can be calculated using a so-called delta-SCF procedure. Here the excitation/ionization energy is obtained as difference of the SCF solutions for the ground state and the excited/ionized state. If the excited state is reasonably well described by a single determinant, this procedure is normally quite accurate.

The example (requires `pyridine.xyz <media/examples/pyridine.xyz>`__ geometry file)

.. code-block:: text
   :caption: examples/pyridine-N1s-core-hole.inp

   ! This example calculates the N 1s core-hole binding energy of pyridine
   ! using a delta-SCF procedure. It calculates a SCF solution in the
   ! ground state, then in the core-excited state, and reports the
   ! difference. The example shows how to obtain the core-excited state
   ! of a core of your choice.
   geometry=pyridine.xyz
   
   ! we use default basis sets for all atoms except the one we wish
   ! to calculate the core hole of, in this case N 1s. For this atom,
   ! we uncontract the s and p functions of the basis to give the core
   ! hole more opportunities for relaxation.
   !
   ! Notes:
   !   - Uncontracting the complete basis would of course also work,
   !     but might be more expensive
   !   - For correlated calculations, you would need additional tight
   !     correlation functions for the hole (e.g., use a cc-pwCVnZ basis
   !     on the affected atom and cc-pVTZ on the rest)
   basis={
      default,def2-TZVPP
      sp,N,def2-TZVPP     ! no "c;" following -- uncontracted.
      df,N,def2-TZVPP;c;  ! use d and f functions with contractions.
   }
   
   ! reference calculation, normal DFT. We also uncontract the fitting
   ! basis to fit the core region more accurately.
   {df-rks,pbe,df_basis=def2-tzvpp(u)}
   ENORMAL = ENERGY       ! remember energy of ground state calculation.
   
   ! localize orbitals. This isolates the cores of the individual atoms
   ! also in the case of degeneracy. And, in particular, it shows us which
   ! orbital is the N 1s we are looking for. It comes out as orbital 1.1.
   {ibba; save,2101.2}
   
   ! do the core-hole calculation. Additionally to the previous command, we
   ! specify nitord=1, which asks SCF to fix orbital order & occupations
   ! starting at iteration 1. This should prevent SCF from dropping down to
   ! the ground state SCF solution.
   !
   ! With this, SCF will emit warnings about strongly deviating orbital
   ! occupations in the first iterations. This is to be expected when
   ! treating instable states and no reason for concern.
   {df-rks,pbe,df_basis=def2-tzvpp(u),nitord=1;
      ! in the program, closed-shell orbitals always have lower numbers
      ! than open-shell orbitals. In order to get the core hole state, we
      ! thus need to exchange the localized N1s orbital (1.1) with whatever
      ! came out at the highest orbital number (21.1) before. [Because the
      ! latter one will be considered as singly-occupied. If we would not use
      ! localized orbitals, 21.1 would be the HOMO].
      rotate,1.1,21.1;    ! exchange orbitals 1.1 and 21.1
      orbital,2101.2;     ! use the localized orbitals as input
      wf,spin=1,charge=1  ! one open-shell orbital (implicitly 21.1)
   }
   EWITH_HOLE = ENERGY
   ! run population analysis again to see if we arrived at the right
   ! state. This should be indicated by an active orbital occupation
   ! of about 1.0 on the N 1s orbital.
   {ibba}
   ! show the result, converted to electron volts.
   {table,(EWITH_HOLE-ENORMAL)*toev
    title,N 1s core hole binding energy [Exp. value: (404.94 +/- 0.03) eV. [Can J. Chem 58 694 (1980)]]
   }

shows how to use the delta-SCF procedure to calculate the N 1s core binding energy in pyridine, by employing localized orbitals and moving them to the HOMO position using a ROTATE card (Sec. `rotating pairs of orbitals <the_scf_program.html#rotating-pairs-of-orbitals>`__). In the core-excited state calculation, SCF is prevented from collapsing to the ground state by using the option NITORD=1 (Sec. `options <the_scf_program.html#options>`__), which asks SCF to lock onto the input solution.
