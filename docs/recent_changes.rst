.. raw:: html

   <span id="features-that-were-new-in-molpro2000"></span>

.. raw:: html

   <span id="new-features-of-molpro2002-6"></span>

.. raw:: html

   <span id="new-features-of-molpro2006-1"></span>

.. raw:: html

   <span id="new-features-of-molpro2008-1"></span>

.. raw:: html

   <span id="new-features-of-molpro2009-1"></span>

.. raw:: html

   <span id="new-features-of-molpro2012-1"></span>

.. raw:: html

   <span id="new-features-of-molpro2015-1"></span>

.. raw:: html

   <span id="new-features-of-molpro2018-1"></span>

.. raw:: html

   <span id="new-features-of-molpro2019-2"></span>

.. _recent_changes--recent-changes:

Recent changes
==============

Several well parallelized new methods have been implemented in Molpro. A review of recent developments in Molpro can be found in `J. Chem. Phys. <https://doi.org/10.1063/5.0005081>`__ 152, 144107 (2020).

We recommend always to use the most recent version, since developments are ongoing and problems reported by users are always fixed as quickly as possible. In particular, before reporting bugs, please check if these still occur in the latest version.

.. _recent_changes--new-features-of-molpro2026-1:

New features of MOLPRO2026.1
============================

.. _recent_changes--fitting-basis-sets:

Fitting basis sets
==================

If density fitting (DF) basis sets or resolution of the identity (RI) basis sets for F12 calculations are defined in a basis set block, and the set names correspond to the contexts, these sets are now used automatically in the programs where needed. This concerns sets named JFIT, JKFIT, MP2FIT, CCSDFIT,  OPTRI, and CABS.

.. _recent_changes--basis-set-library:

Basis set library
=================

For the elements Ga-Kr, cc-pVDZ-JKFIT and aug-cc-pVDZ-JKFIT have been removed.
cc-pVTZ-JKFIT and aug-cc-pVTZ-JKFIT are now used instead, when cc-pVDZ and aug-cc-pVDZ orbital basis sets are chosen and JK fitting is done.

def2-SVP-JKFIT basis sets are now the same ones as in Turbomole. In earlier Molpro versions, the highest angular momentum had been omitted, but this could lead to large errors. def2-ASVP-JKFIT (def2-SVP-JKFIT as in Turbomole plus a diffuse exponent for each angular momentum) has been adjusted analogously.

Some basis sets for the atomic density guess in HF/KS have been improved.

.. _recent_changes--douglas-kroll-hess-calculations:

Douglas-Kroll-Hess calculations
===============================

DK is now activated automatically if a -DK, -DK3, or -X2C basis set is given. In this case the same basis type must be used for all atoms, otherwise an error occurs. By default, DKHO=2 is set for -DK basis sets, DKHO=3 for -DK3 basis sets, and DKHO=101 for -X2C basis sets. These settings can be overwritten by setting variable DKHO, which then has preference. The DK Hamiltonian can be disabled by setting variable DKOLL=0.

.. _recent_changes--intermolecular-interactions:

Intermolecular interactions
===========================

The input for the monomers in the INTERACT program has been generalised. It is now possible to define the monomers manually.

.. _recent_changes--new-features-of-molpro2025-4:

New features of MOLPRO2025.4
----------------------------

Bugfixes

.. _recent_changes--simplified-input:

Simplified Input
================

A simplified one-line input for standard calculations has been added, see :doc:`QuickStart <quickstart>`.

.. _recent_changes--new-option-ccf12-in-pno-lccsd-t-f12:

New Option CCF12 in PNO-LCCSD(T)-F12
====================================

A new option has been added to the PNO program, see `Options for F12 calculations in PNO-LCCSD(T)-F12 <local_correlation_methods_with_pair_natural_orbitals_pnos.html#options-for-f12-calculations>`__. With CCF12=0  F12 is not included in the PNO-LCCSD step and the MP2 F12 correction is added to the PNO-LCCSD and PNO-LCCSD(T) energies. This is similar to a ``focal point`` approximation, where the high-level calculation is PNO-LMP2-F12 and the low-level one PNO-LCCSD(T).

.. _recent_changes--gui-gmolpro-2-10-0:

GUI gmolpro 2.10.0
------------------

gmolpro version 2.10.0 should be used together with Molpro2025.4. On Mac, the package you download is already bundled with this Molpro version.

.. _recent_changes--new-features-of-molpro2025-3:

New features of MOLPRO2025.3
----------------------------

.. _recent_changes--cabs-single-correction-of-the-hf-energy:

CABS single correction of the HF energy
=======================================

The program for the CABS singles correction has been improved and now runs fine in parallel also on multiple nodes. Unless already available, the cabs correction will from now on be automatically computed in the PNO-F12 programs. It is stored in the orbital dump record and reused if available for the given orbital basis.

In large cases the non-parallel diagonalizations needed for basis orthonormalisation and block-diagonalization of the Fock matrix may take more time than the Fock matrix evaluation. To reduce the diagonalization time, the PNO program uses by default ORTHO_CABS=0. This saves one large diagonalization, but has only a negligible effect on relative energies. This default can be overwritten in the PNO program by setting option ortho_cabs=1 (which has been and still is the default if the cabs correction is computed with df-cabs or in non-PNO F12 calculations).

Please see section  section :doc:`Local correlation methods with pair natural orbitals (PNOs) <local_correlation_methods_with_pair_natural_orbitals_pnos>` for further details, e.g. how to disable this mechanism or how to force a recalculation of the CABS correction.

.. _recent_changes--improved-pno-domain-selection-in-pno-lccsd-t-f12:

Improved PNO domain selection in PNO-LCCSD(T)-F12
=================================================

A new option ``SORTPNO`` has been added to the PNO program (see `local_correlation_methods_with_pair_natural_orbitals_pnos#Options for PAO/OSV/PNO generation <local_correlation_methods_with_pair_natural_orbitals_pnos.html#options-for-pao-osv-pno-generation>`__ for details). If this is given, first all PNOs that satisfy the occupation number criterion are added. Then further PNOs are added until the energy completeness criterion is also satisfied. With ``SORTPAO`` these PNOs are added in the order of decreasing semi-canonical energy contributions (rather than in the order of decreasing occupation numbers). In some cases this leads to a drastic reduction of some domains. For backward compatibility, please set PNO option ``SORTPNO=0``. Additionally, there a a new option ``EPNO_MIN=//value//``. PNOs which have semi-canonical energy contributions smaller than the given value are omitted. The default value is zero.

.. _recent_changes--additional-options-in-the-pno-region-program:

Additional options in the PNO region program
============================================

Additional options to define region-specific domain options and to extend the center list for each region are available, see
`local_correlation_methods_with_pair_natural_orbitals_pnos#Correlation regions in the PNO program [REGION <local_correlation_methods_with_pair_natural_orbitals_pnos.html#correlation-regions-in-the-pno-program-region>`__].

.. _recent_changes--restarts-with-interact:

Restarts with INTERACT
======================

The restart possibilities in the INTERACT program have been improved. It is now possible to carry out calculations without counterpoise corrections or monomer relaxation calculations with a restart after a completed CP calculation. See `Interact <properties_and_expectation_values.html#intermolecular-interaction-energies>`__ for details.

.. _recent_changes--cc2-properties-and-transition-moments:

CC2 properties and transition moments
=====================================

CC2 Transition moments and ground state density matrices/properties can now be computed using the canonical CC2 program, see section :doc:`The closed-shell density fitting CC2 program for ground and excited states <the_closed-shell_density_fitting_cc2_program_for_ground_and_excited_states>`.

.. _recent_changes--finite-field-property-calculations:

Finite field property calculations
==================================

New automatic procedures to simplify the calculation of properties like multipole moments or polarizabilities using finite field approximations have been added.

.. _recent_changes--self-consistent-random-phase-approximation-method:

Self-consistent random phase approximation method
=================================================

The self-consistent random phase approximation method (`J. Chem. Phys. <https://doi.org/10.1063/1.4818984>`__ 139, 084113 (2013), `Phys. Rev. Lett. <https://doi.org/10.1103/PhysRevLett.134.016402>`__ 134, 016402 (2025)) is now available within the `SCRPA program <kohn-sham_random-phase_approximation.html#scrpa-program>`__. The program uses the optimized effective potential method to construct the exact exchange potential and the random phase approximation correlation potential. The `SCEXX program <kohn-sham_random-phase_approximation.html#scexx-program>`__ offers the self-consistent exact exchange optimized effective potential method (`J. Chem. Phys. <https://doi.org/10.1063/1.2751159>`__ 127, 054102 (2007), `J. Chem. Phys. <https://aip.scitation.org/doi/full/10.1063/5.0056431>`__ 155, 054109 (2021)) that neglects correlation.

.. _recent_changes--enhanced-interface-with-other-codes:

Enhanced interface with other codes
===================================

Molpro can now read and write geometries to/from `TREXIO <https://trex-coe.github.io/trexio/>`__ files.

New features have also been added to `pymolpro <https://github.com/molpro/pymolpro>`__:

* Export geometry, basis set and orbitals to a `TREXIO <https://trex-coe.github.io/trexio/>`__ file.
* `Prepare and launch Molpro runs <https://molpro.github.io/pymolpro/pymolpro.html#pymolpro.ASEMolpro>`__ within the `Atomic Simulation Environment (ASE) <https://wiki.fysik.dtu.dk/ase/>`__

.. _recent_changes--gui-gmolpro-2-9-0:

GUI gmolpro 2.9.0
-----------------

gmolpro version 2.9.0 should be used together with Molpro2025.3. On Mac, the package you download is already bundled with this Molpro version.

.. _recent_changes--gui-gmolpro-2-8-0:

GUI gmolpro 2.8.0
-----------------

gmolpro version 2.8.0 should be used together with Molpro2025.2. On Mac, the package you download is already bundled with this Molpro version.

The basis set library of Molpro had been extended, and gmolpro has been correspondingly adjusted.

.. _recent_changes--gui-gmolpro-2-7-0:

GUI gmolpro 2.7.0
-----------------

gmolpro version 2.7.0 should be used together with Molpro2025.1. On Mac, the package you download is already bundled with this Molpro version. On Linux, gmolpro does not come bundled with Molpro, and you need a separate installation of Molpro.

A trajectory can be visualised, i.e. a set of xyz files appended to each other.
In the builder window, do ``Geometry/Import to builder window...``

The box in which orbitals are plotted can be enlarged so that very diffuse orbitals can be plotted.

Molpro versions beyond 2025.1 will need gmolpro version at least 2.7.0 because the xml file will be split in xml and xml-sidecar

.. _recent_changes--bug-fixes:

Bug fixes
=========

A bug has been fixed where double hybrid DFT calculations gave different results in serial and parallel calculations. The scaling factor to the MP2 correlation energy is now applied both in serial and in parallel mode (before it was only applied in serial DH calculations). See section `Double-hybrid functionals (DH, DSDH) <the_density_functional_program.html#double-hybrid-functionals-dh-dsdh>`__ for more info.

.. _recent_changes--new-features-of-molpro2025-2:

New features of MOLPRO2025.2
----------------------------

.. _recent_changes--interact:

Interact
========

A minor bug concerning the PNO-LCCSD(T\*) triples scaling has been fixed. The effect of the bug is negligible.

.. _recent_changes--fitting-basis-sets-1:

Fitting basis sets
==================

The def2-QZVPP MP2FIT basis for Ba has been replaced by a newer version. The old version can be accessed as def2-QZVPPO.

.. _recent_changes--nuclear-electronic-orbital-dft:

Nuclear-Electronic Orbital DFT
==============================

Density-fitted NEO-DFT is now available. The program is currently limited to the use of standard numerical integration grids (SG1-3). The electron-proton correlation functionals currently available through the libxc library are the epc17.1, epc17.2, epc18.1 and epc18.2. Multicomponent basis sets (cc-pV\ *n*\ Z-mc, aug-cc-pV\ *n*\ Z-mc) from Brorsen and coworkers are now provided in the Molpro basis set library.

.. _recent_changes--new-features-of-molpro2025-1:

New features of MOLPRO2025.1
----------------------------

.. _recent_changes--bug-fixes-1:

Bug fixes
=========

Various bug fixes. Most notably, a bug that led to a wrong Hartree-Fock starting guess in the presence of ECPs has been fixed. In some cases an error occurred, in others no or very erratic HF convergence resulted. This only occurred if: (i) a segmented or core-valence (CV) basis set was used; (ii) two atoms of the same kind followed each other in the geometry before an atom with ECP; (iii) and/or symmetry was used which reflected atoms into each other. The error did not occur with [a]vnz[-f12] basis sets.

.. _recent_changes--basis-sets:

Basis sets
==========

New Pseudopotentials and associated basis sets have been added for several 3d transition metals.

.. _recent_changes--interact-1:

Interact
========

A new program to automatically compute CP-corrected interaction energies has been added, see `Interact <properties_and_expectation_values.html#intermolecular-interaction-energies>`__

.. _recent_changes--pno-regions:

PNO regions
===========

The PNO correlation region method [[Local correlation methods with pair natural orbitals (PNOs)#Correlation regions in the PNO program [REGION]\|(see REGION)]] has been further improved.

.. _recent_changes--binaries-and-parallelism:

Binaries and parallelism
========================

We recently took the decision not to distribute sockets binaries any more. MPI-PR is the configuration `recommended <https://globalarrays.readthedocs.io/en/latest/Section1-BuildInstructions.html#selecting-the-underlying-one-sided-runtime>`__ by the developers of Global Arrays, and, as far as we understand, is the only one that is asserted to be supported.  See :doc:`Running Molpro on parallel computers <running_molpro_on_parallel_computers>` for additional information on how configuring memory for Molpro can be slightly simpler when using MPI-PR.  We are aware of some failures on large memory-intensive jobs using runtimes other than MPI-PR, and feel that the correct thing to do is to make available only binaries that use MPI-PR.

.. _recent_changes--new-features-of-molpro2024-4:

New features of MOLPRO2024.4
----------------------------

Bug fixes.

.. _recent_changes--new-features-of-molpro2024-3:

New features of MOLPRO2024.3
----------------------------

Molpro now uses Libxc 7.0.0.

.. _recent_changes--new-features-of-molpro2024-2:

New features of MOLPRO2024.2
----------------------------

.. _recent_changes--cc2-excitation-energies:

CC2 excitation energies
=======================

An efficient new density-fitted CC2 Program for the calculation of excitation energies has been added.

.. _recent_changes--pno-lccsd-t-f12-region-approximations:

PNO-LCCSD(T)-F12 region approximations
======================================

Correlation regions have been implemented into the PNO-LCCSD(T)-F12 program. It allows to define uncorrelated (HF), low-level (LMP2-F12), and high-level (PNO-LCCSD(T)-F12) correlation regions in a molecule using lists of orbitals or atoms.

.. _recent_changes--generalised-basis-set-input:

Generalised basis set input
===========================

Atom-specific default basis sets can now be defined for ranges of atoms.

.. _recent_changes--some-old-programs-have-been-removed:

Some old programs have been removed
===================================

The following very old programs, which have redundant functionality with more recent ones, have been removed: CADPAC gradients, distributed multipole approximations (DMA), and an old spin-orbit integral code.

.. _recent_changes--input-syntax:

Input syntax
============

Change in input files using a z-matrix: Previously both Q and X could be used for dummy atoms in a z-matrix. Now, only X should be used.

.. _recent_changes--gui-gmolpro-2-5-0:

GUI gmolpro 2.5.0
-----------------

The colors of the labels (``Display/Labels``) in the builder window are now white, in the viewer window black.
In the viewer window, there is in addition the option ``Options/Graphics/Adaptive Label Colors``

Improved compatibility with iMolpro (xyz files from iMolpro are now shown in the builder when opening an iMolpro-project
with gmolpro).

.. _recent_changes--gui-gmolpro-2-4-0:

GUI gmolpro 2.4.0
-----------------

A window appears below the brown viewer window, to display the xyz file of the structure presently in the viewer;
continuously updated even during vibrations. It can be opened/closed with the menu item ``Window/Show xyz file``

Better placement of the windows on startup.

.. _recent_changes--new-features-of-molpro2024-1:

New features of MOLPRO2024.1
----------------------------

Various bug fixes and improvements of existing methods.

.. _recent_changes--imolpro:

iMolpro
=======

A new graphical user interface called ``iMolpro`` is now included without additional charge. This can be used for generating Molpro inputs for DFT and all single reference methods, and submit these for execution to a chosen machine. This functionality is very much like in gMolpro. In addition, structures, orbitals, and vibrations can be viewed using Jmol.

.. _recent_changes--d4-dispersion-correction:

D4 dispersion correction
========================

Unfortunately this has been wrong (usually too small) for pseudo-potential calculations. This bug has been fixed.

.. _recent_changes--dft-functional-alias-names:

DFT functional alias names
==========================

Many alias names for functionals computed with libxc have been added. These are compatible with those used in the D4 program.

.. _recent_changes--density-based-basis-set-correction:

Density-based basis set correction
==================================

This program has been very much speeded up, with and without density fitting. Various functionals can now be used in it.

.. _recent_changes--internally-contracted-multireference-coupled-cluster-theory:

Internally Contracted Multireference Coupled-Cluster Theory
===========================================================

A CAS(2,2) version of icMRCCSD is now available, as published in `J. Chem. Phys. 158, 134801 (2023) <https://doi.org/10.1063/5.0143214>`__.

.. _recent_changes--pno-lmp2-f12-pno-lccsd-t-f12:

PNO-LMP2-F12 / PNO-LCCSD(T)-F12
===============================

New variables EMP2F12_PNO and EMP2F12_OSV are set for MP2-F12 energies computed with PNO or PAO/OSV projector, respectively. This happens in calculations with option projector=PAO or projector=MIXED.

.. _recent_changes--nuclear-electronic-orbital-neo-methods:

Nuclear-electronic orbital (NEO) methods
========================================

A new automated procedure for the optimisation of quantum nuclei positions has been introduced (adaptive-NEO). The latter works by updating the nuclei position (meaning the nuclear basis centers, together with the respective electronic basis functions) to the nuclear orbital centroids during the SCF cycles. See `Adaptive NEO <nuclear-electronic_orbital_method.html#adaptive-neo>`__ for further information.

.. _recent_changes--basis-set-short-names:

Basis set short names
=====================

The short names [awc]vnz-dk (n=d,t,q,5) now refer to the [aug]-cc-p[wC]V(n+d)Z-DK sets for second-row elements Al-Cl. To avoid using the +d sets (not recommended!) use the full basis set name.

.. _recent_changes--gui-gmolpro-2-3-0:

GUI gmolpro 2.3.0
-----------------

Version 2.3.0 is bundled with Molpro 2024.1 .

There is now a switch "Display/Retina Screen"
in the builder and viewer window to deal with those Mac's which have retina screens.
It switches from a normal display (retina factor 1)
to a display with doubled number of pixels in both directions (retina factor 2).
When this factor is changed, then it gets auto-saved in a configuration file $HOME/.pqsmol/gmolpro.conf .
If necessary, this configuration file can be edited and retina factors different from 1 or 2 may be used.

LIBGL_ALWAYS_SOFTWARE is set to be true. This avoids a crash on some Linux distributions, which is due to a bug
in the Mesa library.

.. _recent_changes--new-features-of-molpro2023-1:

New features of MOLPRO2023.1
----------------------------

Molpro 2023.2 is a bug-fix release with the same features as Molpro 2023.1

.. _recent_changes--binaries-for-calculations-on-multiple-nodes:

Binaries for calculations on multiple nodes
===========================================

The Linux MPI-PR binary now supports parallel calculations on multiple computer nodes based on UCX (which must be installed on the cluster). Currently, multi-node calculations are restricted to closed-and open-shell DF-HF, DF-KS, and PNO-LCCSD(T). It is generally recommended to use the MPI-PR version for parallel calculations, since it is more stable than the sockets version and does not require GA preallocation (-G option). Note, however, that multi-node calculations can be very slow unless a fast network (e.g. Infiniband) is available.

.. _recent_changes--unrestricted-coupled-cluster:

Unrestricted coupled cluster
============================

Unrestricted UCCSD(T) and related methods based on UHF orbitals are now available, see section :doc:`Open-shell coupled cluster theories <open-shell_coupled_cluster_theories>`.

.. _recent_changes--improved-geometry-optimization:

Improved geometry optimization
==============================

An improved geometry optimizer using natural internal coordinates is now available and used by default, see section :doc:`Geometry optimization (OPTG) <geometry_optimization_optg>`. New special options for this optimizer are described in section `Options for the PQS optimizer <geometry_optimization_optg.html#options-for-the-pqs-optimizer>`__.

.. _recent_changes--dft-grids:

DFT Grids
=========

Rotationally invariant DFT grids have been implemented and is used by default. This is achieved by rotating the grid of each atom dependent of its local environment (see section `Atomic grid orientation (ORIENT) <the_density_functional_program.html#orientation-of-atomic-grids-orient>`__).

.. _recent_changes--treatment-of-core-correlation-in-pno-methods:

Treatment of core correlation in PNO methods
============================================

The algorithm for automatically sorting inner and outer core orbitals has been improved and new a new option ``LOC_OUTCORE=MIX`` has been added. See `Advanced options <local_correlation_methods_with_pair_natural_orbitals_pnos.html#advanced-options>`__ in section :doc:`Local correlation methods with pair natural orbitals (PNOs) <local_correlation_methods_with_pair_natural_orbitals_pnos>` for details.

.. _recent_changes--nuclear-electronic-orbital-neo-methods-1:

Nuclear-electronic orbital (NEO) methods
========================================

The multicomponent restricted NEO Hartree-Fock method has been implemented in Molpro. This allows for the quantum mechanical treatment of a selected number of protons concurrent with the electronic SCF. For more information, please consult the section :doc:`Nuclear-electron orbital (NEO) method <nuclear-electronic_orbital_method>`.

.. _recent_changes--basis-set-extrapolation-based-on-a-dft-model:

Basis set extrapolation based on a DFT model
============================================

The basis set incompleteness error correction based on a DFT model by E. Giner and J. Toulouse (`J. Phys. Chem. Lett. <https://dx.doi.org/10.1021/acs.jpclett.9b01176>`__ **10**, 2931 (2019)) has been implemented, see section `Basis set incompleteness error correction <basis_set_extrapolation.html#basis-set-incompleteness-error-correction-using-a-dft-model-of-short-ranged-electron-interactions>`__ for details.

.. _recent_changes--functionals-and-rpa-calculations-with-rirpa-code:

σ-functionals and RPA calculations with RIRPA code
==================================================

The σ-functionals developed by Görling and coworkers (`J. Chem. Phys. <https://aip.scitation.org/doi/full/10.1063/5.0026849>`__ 154, 014104 (2021), `J. Chem. Phys. <https://aip.scitation.org/doi/abs/10.1063/5.0059641>`__ 155, 134111 (2021)) are implemented in the RIRPA code. See the corresponding section in the manual for details: `RIRPA program <kohn-sham_random-phase_approximation.html#rirpa-program>`__. σ-functionals are as fast as RPA, but provide more accurate results for many chemical properties.

.. _recent_changes--the-cispt2-method:

The CISPT2 method
=================

A new variant of multi-reference perturbation theory, denoted cispt2, has been added. This adds a perturbative double correction to a MRCI-singles (MRCIS) calculation. The initial MRCIS relaxes the reference coefficients before generating the internally contracted doubles.  Valence excitation energies are more accurate than with CASPT2 or NEVPT2.

.. _recent_changes--bug-fixes-in-nevpt2:

Bug fixes in NEVPT2
===================

Some problems in NEVPT2 have been fixed, and tighter default integral screening thresholds for DF-NEVPT2 have been set.

.. _recent_changes--gui-gmolpro-version-2-2-0:

GUI gmolpro version 2.2.0
=========================

Version 2.2.0 of the graphical user interface gmolpro is bundled with Molpro2023.2.0 .
When installing gmolpro, then it is installed together with this Molpro version, and uses this version on the local machine.

Due to moving to gtk2.24, the menu bar on Mac is better synchronised.

Important: on some platforms such as openSUSE15.5, ``export LIBGL_ALWAYS_SOFTWARE=1`` or ``export MESA_LOADER_DRIVER_OVERRIDE=i965`` may be necessary before starting gmolpro , to avoid a crash (because of a bug in the Mesa library)

Frequently asked question:

Q: An optimisation (or frequency calculation) is performed, but the icon to open the optimisation (or frequency) window is greyed out, why?

A: The GUI searches for orbitals, and generates a pulldown menu with a set of orbitals found. If there is more than one set of orbitals, then it may be necessary to load a different set of orbitals. If a corresponding optimisation (or frequency) calculation is found, then the icon to open the window will become clickable (and is not greyed out any more).

.. _recent_changes--new-features-of-molpro2022-3:

New features of MOLPRO2022.3
----------------------------

.. _recent_changes--mppx-option:

MPPX option
===========

The ``--mppx`` option on the molpro command line has been disabled. mppx (i.e. independent calculations for different geometries on each processor) is used automatically in numerical gradient and hessian calculations, as well as in surface calculations for VCI. The mppx mode can be disabled setting option ``MPPX=0`` on the ``FREQENCIES``, ``HESSIAN``, ``OPTG``, or ``FORCE`` command lines, e.g. ``FREQ,MPPX=0``.

.. _recent_changes--coupled-cluster-calculations-using-ks-orbitals:

Coupled-cluster calculations using KS orbitals
==============================================

It is now possible to run CCSD or CCSD(T) calculations using orbitals from a previous Kohn-Sham (KS) calculation. New options ``H0=MP|KS`` and ``KSFOCK`` have been added. With ``H0=MP`` (default, Moeller-Plesset zeroth-order Hamiltonian) the Fock matrix is recomputed using the KS orbitals and block-diagonalised, while with ``H0=KS`` the KS Fock matrix is used as zeroth-order Hamiltonian, and thus the KS orbital energies in the denominators in the perturbative MP2 and triples steps. In both cases single excitations are included in the MP2 step (this is also possible with DF-MP2). Single excitations can be excluded using option ``NOSINGLES``.

Option ``KSFOCK`` forces the use of the KS Fock matrix in the subsequent calculation. This is required for double-hybrid DFT and RPA calculations.

Note that the (T) energies are still slightly different in closed-shell CCSD and UCCSD calculations. This is due to missing singles terms in the closed-shell triples program. Work is in progress to fix this problem.

.. _recent_changes--pno-methods:

PNO methods:
============

* The printed LMP2 energies in PNO-LMP2-F12 and PNO-LCCSD-F12 calculations now include the CABS singles correction (if available). The domain-corrected LMP2 energy is stored in a variable EMP2C (alias EMP2_DC), the MP2-F12 energy in variable EMP2F12 (alias EMP2_F12).

* (T) in PNO-LCCSD(T)-F12 calculations can be restarted from a dump file, see `Restarting (T) <local_correlation_methods_with_pair_natural_orbitals_pnos.html#restarting-t>`__ for details.

* A very tight domain option has been added (domopt=vtight), see `Default and tight settings <local_correlation_methods_with_pair_natural_orbitals_pnos.html#default-and-tight-settings>`__

* New options for computing intermolecular pairs with special domains have been added, see `Options for intermolecular interactions <local_correlation_methods_with_pair_natural_orbitals_pnos.html#options-for-intermolecular-interactions>`__ for details.

* If ``SAVE_LMO=//record//`` is given the localised orbitals are written to the given record as well as to the xml file for visualisation with gmolpro. If *record=1* the current orbital dump record is used.

.. _recent_changes--mrci-restart:

MRCI restart:
=============

A bug in the MRCI restart with stored reference vectors has been fixed.

.. _recent_changes--nevpt2:

NEVPT2:
=======

The maximum number of active orbitals in NEVPT2 has been increased from 14 to 32.

.. code-block:: text

.. _recent_changes--rs2-gradients:

RS2 Gradients
=============

An parallelisation problem occurring with large reference spaces has been fixed. The performance and parallelisation of some parts of the gradient program have been improved.

.. _recent_changes--rovibrational-spectra:

Rovibrational Spectra:
======================

The existing VCI program has been extended by a new directive (ROVIB), which allows for the automated calculation of high-resolution rotational and rovibrational spectra based on RVCI theory. Rotational and Coriolis coupling can be included up to high accuracy and several rotational bases are provided. As the final line lists can be very long, they are stored in an external file, which can be further processed by the DAT2GR program in order to simulate the corresponding spectra. To allow for maximal flexibility with respect to the vibrational bases, the VIBSTATE program has been significantly extended and controls now for all parts of the VSCF/VCI programs the list of states to be computed - including non-Abelian point groups (see the VSCF manual).

.. _recent_changes--nmr-shielding-tensors-with-dft:

NMR shielding tensors with DFT: =
=================================

NMR shielding tensors can be computed with LDA, GGA and hybrid GGA functionals using density fitting approximations of two-electron integrals using the new ``dftshield`` program. The program is restricted to closed-shell systems and currently does not support symmetry.

.. _recent_changes--documentation-of-default-basis-sets:

Documentation of default basis sets
===================================

The documentation of default basis sets in Molpro has been extended, see section
`Default basis sets <basis_input.html#default-basis-sets>`__

.. _recent_changes--cartesian-basis-functions:

Cartesian basis functions:
==========================

The input specifications for cartesian basis functions have been generalised. It is no possible to specify option ``CARTESIAN`` or ``ATTRIBUTES=CARTESIAN`` on basis set ``SET`` directives, e.g. ``SET,JK,CONTEXT=JKFIT,CARTESIAN``. It should be noted, however, that density fitting with cartesian basis functions is much slower than with spherical ones. F12 calculations with cartesian basis functions are not possible.

.. _recent_changes--python-project-management:

= Python project management
===========================

The pymolpro Python package has been released, and is available via conda-forge.  This supports the same Molpro project bundles as the gmolpro GUI, and allows the programmatic construction, running and analysis of Molpro jobs. For details, see https://molpro.github.io/pymolpro/ and https://github.com/molpro/pymolpro

.. _recent_changes--new-features-of-molpro2022-2:

New features of MOLPRO2022.2
----------------------------

Various problems concerning the use of cartesian basis functions have been fixed, including the starting guess and AVAS. Density fitting now works for cartesian basis sets up to h-functions.

The default of DFT grid option orient has been change to 1; this makes KS energies rotationally invariant, but may slightly change energies (mostly in the microhartree range. To recover the old behaviour add grid option orient=1.

A new `F12 projector option <local_correlation_methods_with_pair_natural_orbitals_pnos.html#options-for-f12-calculations>`__ is added to the PNO-LCCSD program.
Different F12 geminal exponents for valence, core-valence, and core-core pairs are now supported.
See `GEM_BETA <explicitly_correlated_methods.html#options>`__ for details.

The memory usage and performance of the RS2C expectation value calculations are significantly improved.
The :doc:`NOPROP <multireference_rayleigh_schroedinger_perturbation_theory>` option is added to skip the expectation value calculations.

DFT  options for controlling grid accuracy have been added to gmolpro.

OPTG options for choosing optimization methods and coordinates have been added to gmolpro.

.. _recent_changes--gui-gmolpro-version-2-1-0:

GUI gmolpro version 2.1.0
-------------------------

Version 2.1.0 of the graphical user interface gmolpro is bundled with Molpro2022.2.3 .
When installing gmolpro, then it is installed together with Molpro version 2022.2.3 , and uses this version on the local machine.

The token may be installed in
``$HOME/.molpro/token`` . Alternatively (useful for group licences), on Linux, it may be installed in ``/usr/share/gmolpro/molpro/lib/.token`` , and on Mac in ``/Applications/gmolpro.app/Contents/Resources/molpro/lib/.token``

A slider to change the vibrational amplitudes has been added. As before, the animation speed can be changed with Options/Graphics/Animation Speed

The xyz-geometry in the builder window is now displayed in a little extra window.

Various bug fixes: z-matrix containing dummy atoms now properly written by Molpro, so that gmolpro correctly displays it; small window (segment window) in builder: hydrogens + dummies properly displayed etc.

Force-field parameters autodetected when importing xyz.

.. _recent_changes--gui-gmolpro-version-2-0-0:

GUI gmolpro version 2.0.0
-------------------------

Version 2.0.0 of the graphical user interface gmolpro is bundled with Molpro2022.2.2 .
When installing gmolpro, then it is installed together with Molpro version 2022.2.2 , and uses this version on the local machine.

The token may be installed in
``$HOME/.molpro/token`` . Alternatively (useful for group licences), on Linux, it may be installed in ``/usr/share/gmolpro/molpro/lib/.token`` , and on Mac in ``/Applications/gmolpro.app/Contents/Resources/molpro/lib/.token``

.. _recent_changes--new-features-of-molpro2022-1:

New features of MOLPRO2022.1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _recent_changes--update-2022-1-2:

Update 2022.1.2
---------------

A bug affecting KS and TDDFT calculations with cartesian basis functions has been fixed.

.. _recent_changes--perturbation-adapted-perturbation-theory-papt:

Perturbation-Adapted Perturbation Theory (PAPT)
-----------------------------------------------

The perturbation-adapted zero-order hamiltonian described in J. Chem. Phys. 156, 011101 (2022); https://doi.org/10.1063/5.0079853 is available for closed-shell systems.

.. _recent_changes--core-directive:

CORE directive
--------------

With ``CORE,MIXED`` correlation of the 2s and 2p electrons for the third-row elements Al - Ar is now excluded.
Global ``CORE`` command is now supported.
See `defining orbital subspaces <general_program_structure.html#defining-orbital-subspaces-occ-closed-core-frozen>`__ for details.
The old behaviour, where these electrons were correlated, can be recovered using ``CORE,MIXED_OLD``.

.. _recent_changes--scf-program:

= SCF program
=============

* Quadratic optimization or mixed quadratic/first-order SO-SCI optimization is available for closed-shell and open-shell RHF by using ``{RHF,SO;...}`` or ``{RHF,SO-SCI;...}``.
* The CAHF optimization with the quadratic or the SO-SCI optimization is implemented into the CAHF program, and it can be called by ``{CAHF,SO;...}`` or ``{CAHF,SO-SCI;...}``.
* A new variant of the SO-SCI optimization is available for the RHF case. It optimizes all AVAS orbitals quadratically and is called by ``{RHF,SO-SCI-ACTIVE}``.

The ``SO-SCI`` option significantly improves convergence and is recommended in difficult cases. The cost may even be lower than for standard open-shell RHF or CAHF calculations, since the number of iterations is reduced. Furthermore, the probability of convergence to local minima or saddle points is much reduced.

.. code-block:: text

See section `options for the SO-SCI optimization <the_scf_program.html#options-for-the-so-sci-optimization>`__ for more details and options.

.. _recent_changes--mcscf-casscf:

MCSCF/CASSCF
------------

* The entire export of CI vectors to subsequent Molpro programs has been rewritten. CI vectors can be exported via ``SAVE,CIREC=record`` or ``NATORB,orbrecord,CIREC=record``; more details can be found `here <the_mcscf_program_multi.html#saving-the-ci-vectors>`__. All exported CI vectors are stored in the CSFs basis. Determinants are automatically transformed into the CSFs basis, which also allows an export with state-averaging over different spins.  **Warning**: MULTI based CI records from earlier Molpro versions are not compatible anymore, and the wfu file has to be recalculated with Molpro 2022!
* ``{MULTI,CASCI;...}`` can now be simply called by ``{CASCI;...}``, and the input orbitals are not transformed after the CASCI optimization (also for dont,orbital).
* Gradients of the state-averaged energy are now available.
* The program is now more robust against spin-contamination in determinant based calculations.

.. _recent_changes--mrci-caspt2:

MRCI, CASPT2
------------

The CI vectors stored in multi using the directive ``SAVE,CIREC=record`` can now be used in the MRCI and CASPT2 programs as reference vectors using option ``CIREC=record``.

.. _recent_changes--mcscf-casscf-spin-orbit-calculations-hlsmat:

MCSCF/CASSCF spin-orbit calculations (HLSMAT)
---------------------------------------------

A new much more efficient algorithm for computing the spin-orbit Hamiltonian using MCSCF wavefunctions and ECP spin-orbit operators. The program to compute and diagonalize spin-orbit matrices can generally be called using

``HLSMAT,type, record1, record2, record3, …``

where ``record1``, ``record2`` etc are records saved with MULTI or MRCI. The new program is used if ``type`` is ``ECPLS`` and if no external excitations are present (so either MCSCF/CASSCF wavefunctions or MRCI ones with NOEXC).

For more details see section `spin-orbit-coupling#calculation and diagonalization of the entire SO-matrix <spin-orbit-coupling.html#calculation-and-diagonalization-of-the-entire-so-matrix>`__.

.. _recent_changes--pno-lccsd:

PNO-LCCSD
---------

The IBO localization convergence threshold has been tightened from :math:`10^{-8}` to :math:`10^{-9}`.
The PAO redundancy threshold ``THRLOC`` has been tightened from :math:`10^{-6}` to :math:`10^{-7}`.

The localisation of core orbitals has been improved; it now uses an AO-based algorithm, which minimises
mixings of orbitals of different types (e.g. s, p\ :math:`_x`, p\ :math:`_y`, p\ :math:`_z`). It has been found that this stabilises the F12(PNO) energy contribution if core orbitals are correlated. The new default for core-orbital localization is loc_method_core=IBO(AO).

The previous behaviour of the PNO program can be recovered by putting before the first PNO command:

``local, thrpip=1.d-8, thrloc=1.d-6, loc_method_core=ibo``

The corresponding new options are

``local, thrpip=1.d-9, thrloc=1.d-7, loc_method_core=ibo(ao)``

The options can also be given on the PNO command, lines.

.. _recent_changes--gui-gmolpro:

GUI gmolpro
-----------

Version 1.4.0 of the graphical user interface gmolpro is compatible with Molpro2022.1 .

Main improvement over earlier versions is the ability to handle output files (xml files) with several optimisations, frequency calculations, or even different molecules within one xml file. Start from the brown window, open the orbital window, and then select and load an orbital set. A corresponding optimisation or vibrational modes may now be displayed.

When creating an input in guided mode, more properties may be selected by buttons.

.. _recent_changes--new-features-of-molpro2021-2:

New features of MOLPRO2021.2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _recent_changes--parallel-execution:

Parallel execution
------------------

An option has been added to use MPI files instead of large GlobalArrays to avoid potential GA allocation problems. From Molpro2020.2 the disk option (``--ga-impl disk``) is the default for single-node calculations. Thus, GA preallocation is not necessary unless ``--ga-impl ga`` is used. See `disk option <https://www.molpro.net/develop/manual/doku.php?id=running_molpro_on_parallel_computers#disk_option>`__ for details.

For molpro2020.2 and Linux systems, an additional binary compiled with the GA ``mpi-pr`` option is provided. It is recommended to use this binary if ``--ga-impl ga`` is chosen, since it avoids potential GA allocation problems as well (the ``-G`` option is not needed). Note, however, that this requires an extra helper process. For example, if ``-n 20`` is given, only 19 processes will be used for program execution. See `Running Molpro on parallel computers <https://www.molpro.net/develop/manual/doku.php?id=running_molpro_on_parallel_computers>`__ for details.

.. _recent_changes--rs2c-caspt2:

RS2C/CASPT2
-----------

Multi-state CASPT2 is now available in the rs2c program, see `Multi-State CASPT2 <multireference_rayleigh_schroedinger_perturbation_theory.html#multi-state-caspt2>`__.

.. _recent_changes--nevpt2-1:

NEVPT2
------

NEVPT2 can now be done with density fitting, the command is ``DF-NEVPT2``

.. _recent_changes--avas:

AVAS
----

Additional options allow a more flexible definition of the target space.

.. _recent_changes--new-features-of-molpro2021-1:

New features of MOLPRO2021.1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _recent_changes--hartree-fock:

Hartree-Fock
------------

A new implementation of the HF/KS program is now used by default. In difficult cases this shows more robust convergence.

* The old version can still be used by specifying option "old", e.g. hf,old.

* Optionally, the hybrid second-order/super-ci method (so-sci) can be used in difficult cases (hf,so-sci). In open-shell cases this converges more robustly than the standard open-shell RHF procedure.

.. _recent_changes--mcscf-casscf-1:

MCSCF/CASSCF
------------

* `Generalized dynamical weighting <the_mcscf_program_multi.html#dynamical-weighting>`__, in which the dynamical weighting can be restricted to certain states.

* `CAHF optimization <the_mcscf_program_multi.html#cahf-optimization-with-the-mcscf-program>`__ with the multi program for the state-averaged optimization including all irreducible representations and spin manifolds. Convergence is more robust than in the equivalent Hartree-Fock optimization, especially for multiple CAHF shells.

* `RHF export <the_mcscf_program_multi.html#rhf-optimization-with-the-mcscf-program>`__ for multi orbitals.

* `State restrictions for one-electron properties. <the_mcscf_program_multi.html#matrix-elements-over-one-electron-operators>`__

* Export of the `raw orbitals <the_mcscf_program_multi.html#raw-orbitals>`__ used in the MCSCF optimization. Input orbitals stay untouched in combination with the command dont,orbital.

.. _recent_changes--analytical-energy-gradients:

Analytical energy gradients
---------------------------

Analytical energy gradients are now available for RASPT2 (using rs2).

.. _recent_changes--td-dft:

TD-DFT
------

* Rotatory strengths for simulating CD spectra of optically active molecules can be computed for spin-restricted TDDFT excitations
* First-order nonadiabatic coupling matrix elements (NACME) are available for closed and open-shell TDHF and TDDFT (LDA or GGA-type functionals)

.. _recent_changes--miscellaneous:

Miscellaneous
-------------

* All fundamental constants used in the program have been updated to the most recent CODATA 2018 standard `https://physics.nist.gov/cuu/Constants <https://physics.nist.gov/cuu/Constants>`__
* The sparse orbital print has been modified. Now it shows for each printed coefficient the center number, the function type, and the sequence number for this type at the given atom (denoted MU).

.. _recent_changes--new-features-of-molpro2020-2:

New features of MOLPRO2020.2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _recent_changes--analytical-energy-gradients-1:

Analytical energy gradients
---------------------------

* DF-MCSCF (single state), DF-HF, DF-UHF, DF-KS, and DF-UKS gradients are now available with symmetry.
* TD-DFT gradients for closed-shell singlet excited states are available with and without density fitting.

.. _recent_changes--pno-lccsd-t-f12:

PNO-LCCSD(T)-F12
----------------

* The core orbitals are no longer excluded from the CCSD-F12 projector by default. The approximation, which is applied by default in previous versions, saves a few percent of the computation time, but can have a significant effect in calculations involving transition metals. The old default can be recovered by ``MODOMC=1``.
* Correlated core orbitals are now localized separately from the valence orbitals by default, which mostly improves the results and convergence in calculations with core orbital correlation. The old default can be recovered by ``LOC_OUTCORE=ON``.
* The ``ENERGY`` variable is now set to a scalar representing the final energy in F12 calculations. ``PNO-LCCSD-F12`` is now equivalent to ``PNO-LCCSD-F12b``, and F12a and F12b total energies can be accessed from the variables ``ENERGYA`` and ``ENERGYB``. Similar changes are made to the ``ENERGC`` variable.
* The scaling factor for F12-scaled triples now excludes the contribution from distant pairs, for which F12 energies are neglected.

.. _recent_changes--linux-binaries:

Linux binaries
--------------

The `minimum requirements <installation_guide.html#prerequisites>`__ for using the Linux binaries has increased to glibc 2.17 or newer.

.. _recent_changes--new-features-of-molpro2020-1:

New features of MOLPRO2020.1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _recent_changes--windows-support:

Windows support
~~~~~~~~~~~~~~~

A windows beta version of Molpro is now available.

.. _recent_changes--gmolpro-a-graphical-user-interface:

gMolpro: A graphical user interface
-----------------------------------

A powerful graphical user interface (based on PQSMol) for building and preoptimising molecular structures, preparing and running Molpro inputs, and visualisation of results (will soon be available). gMolpro also supports remote job submission and is available for Linux and Mac.

.. code-block:: text

.. _recent_changes--the-mcscf-casscf-program-multi:

The MCSCF/CASSCF program MULTI
------------------------------

The CASSCF program multi has been largely rewritten and well parallelized. Improved second-order algorithms as well as first-order methods applicable to large molecules have been implemented. The new program combines robust convergence with excellent efficiency. Details are described in `J. Chem. Phys. <https://doi.org/10.1063/1.5094644>`__ 150, 194106 (2019) and `J. Chem. Phys. <https://doi.org/10.1063/1.5142241>`__ 152, 074102 (2020).

.. _recent_changes--multi-state-pno-caspt2:

Multi-state PNO-CASPT2
----------------------

The PNO-CASPT2 program for large molecules has been extended to allow multi-state MS-CASPT2 calculations. For details see `J. Chem. Phys. <https://doi.org/10.1063/1.5097644>`__ 150, 214107 (2019).

.. _recent_changes--time-dependent-density-functional-tddft-program:

Time-dependent density-functional (TDDFT) program
-------------------------------------------------

The time-dependent DFT program has been completely rewritten to support molecular symmetry, open-shell systems (for spin-unrestricted wave functions), various integral modes (including a very fast parallelised density-fitting mode) and standard LDA, GGA, hybrid-GGA and range-separated hybrid GGA functionals and kernels. Calculations using the exact Kohn-Sham exchange (TDEXX) method can be done both by using the adiabatic and non-adiabatic EXX kernel. Linear response properties can be calculated for any one-electron operators available in Molpro. Isotropic and anisotropic :math:`C_6`, :math:`C_8`
and :math:`C_{10}` dispersion coefficients can be computed along with the calculation of frequency dependent (dipole,quadrupole,octopole) polarisabilities.

.. _recent_changes--libxc-density-functionals:

LibXC density functionals
-------------------------

An interface to the external LibXC library (see `https://www.tddft.org/programs/libxc <https://www.tddft.org/programs/libxc>`__) of density functionals has been added. Therefore virtually any density functional of the LDA, GGA, hybrid-GGA, meta-GGA and range-separated hybrid-GGA can be used in Molpro calculations in the DFT and Kohn-Sham programs. Range-separated DFT calculations with both long-range and/or short-range exact exchange admixtures can
be done now also using an efficient density-fitting implementation of the Fock matrix computation.

.. _recent_changes--van-der-waals-density-functionals:

Van-der-Waals density functionals
---------------------------------

An implementation of the nonlocal van-der-Waals DF VV10 by Vydrov & Van Voorhis is available for spin-restriced wave functions to improve the description of long-range correlation interactions of standard DFT methods.

.. _recent_changes--explicitly-correlated-local-coupled-cluster-program-for-high-spin-open-shell-molecules:

Explicitly correlated local coupled-cluster program for high-spin open-shell molecules
--------------------------------------------------------------------------------------

The local coupled-cluster program PNO-LCCSD(T)-F12 has been revised to support open-shell molecules.
The new revision also includes some minor changes in the local approximations and is also used for closed-shell molecules by default.
The closed-shell program in Molpro 2019.2 and earlier can be executed with the option ``version=2019.2``.
For more details see :doc:`Local correlation methods with pair natural orbitals (PNOs) <local_correlation_methods_with_pair_natural_orbitals_pnos>`.

.. _recent_changes--extended-potential-energy-surface-generator:

Extended potential energy surface generator
-------------------------------------------

A new program, XSURF, has been implemented for the efficient calculation of potential energy surfaces (PES) as needed for the calculation of anharmonic spectra. In contrast to the "old" SURF program, XSURF can handle any type of symmetry, is not restricted to the length of the expansion of the PES and is restartable at any point.

.. _recent_changes--acceleration-of-the-poly-and-the-pestrans-programs:

Acceleration of the POLY and the PESTRANS programs
--------------------------------------------------

Due to a complete redesign of the programs for the fitting (POLY) and the transformation of potential energy surfaces (PESTRANS), these programs could be accelerated by several orders of magnitude (only operative in combination of the new XSURF program).

.. _recent_changes--electronic-vibrational-spectra:

Electronic - vibrational spectra
--------------------------------

Similar to the Franck-Condon program, the new EVSPEC program allows for the calculation of anharmonic electronic-vibrational absorption spectra with the inclusion of Duschinsky effects. Two different implementations are provided, the contracted invariant Krylov subspace (CIKS) approach and a Raman wavefunction (RWF) formalism.

.. _recent_changes--new-features-of-molpro2019-2:

New features of MOLPRO2019.2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _recent_changes--improved-parallel-density-fitting-in-hartree-fock-and-dft:

Improved parallel density fitting in Hartree-Fock and DFT
---------------------------------------------------------

A new parallel density fitted Fock matrix generation has been implemented. For large molecules this scales well across computer nodes (with a fast network such as Infiniband) up to about half as many computing cores as occupied orbitals.

Symmetry can now be used in DF-HF and DF-KS (restricted and unrestricted), but not yet for gradients.

.. _recent_changes--new-features-of-molpro2018-1:

New features of MOLPRO2018.1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _recent_changes--quasi-variational-coupled-cluster-qvccd:

Quasi-variational coupled-cluster (QVCCD)
-----------------------------------------

Improved efficient implementation of quasi-variational coupled-cluster (QVCCD).

.. _recent_changes--analytical-energy-gradients-for-coupled-cluster-methods:

Analytical energy gradients for coupled cluster methods
-------------------------------------------------------

Analytical energy gradients for closed shell DF-MP2-F12, DF-CCSD(T)-F12, CCSD(T) and open-shell [DF-]RMP2 have been added. The gradients for explicitly correlated (F12) methods are restricted to certain Ansätze; please refer to the users manual for details and W. Györffy, G. Knizia and H.-J. Werner, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.5003065>`__ **147**, 214101 (2017); W. Györffy and H.-J. Werner, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.5020436>`__ **148**, 114104 (2018).

.. _recent_changes--analytical-energy-gradients-for-projection-based-wf-in-dft-embedding:

Analytical energy gradients for projection-based WF-in-DFT embedding
--------------------------------------------------------------------

Analytical nuclear gradients have been implemented for projection-based wavefunction-in-DFT (WF-in-DFT) embedding with and without atomic orbital (AO) truncation. The current available methods that can be used for the WF method on subsystem A are CCSD(T), CCSD, MP2, and HF. The current available methods that can be used for the low-level SCF method are LDA, LDAX (LDA with any amount of exact exchange) and HF. The support for using GGAs as the low-level method will be coming soon.

.. _recent_changes--analytical-energy-gradients-for-local-methods:

Analytical energy gradients for local methods
---------------------------------------------

Analytic energy gradients for local MP2, RMP2, CC2 and ADC(2) (with density fitting) are available. These methods can be used for geometry optimisations and property calculations of larger molecules.

.. _recent_changes--local-coupled-cluster-linear-response-method-for-ionization-potentials:

Local coupled cluster linear response method for ionization potentials
----------------------------------------------------------------------

A hierarchy of local coupled cluster models for ionization potentials employing LMP2 or LCC2 ground state amplitudes and the Jacobian formally reaching the IP-CCSD level: IP-CCSD\ :math:`_{\rm CC2}` is now available. For details see G. Wälz, D. Usvyat, T. Korona, M. Schütz, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.4942234>`__ **144**, 084117 (2016).

.. _recent_changes--local-mp2-nmr-shielding:

Local MP2 NMR shielding
-----------------------

Local MP2 NMR shielding, magnetisability, and rotational g tensors.

.. _recent_changes--mr-ccsd-t:

MR-CCSD(T)
----------

The internally contracted multi-reference program of A. Köhn et al. has been interfaced to Molpro. An embedded Multireference Coupled Cluster method as described in D. J. Coughtrie, R. Giereth, D. Kats, H.-J. Werner, and A. Köhn, `J. Chem. Theory Comput. <https://dx.doi.org/10.1021/acs.jctc.7b01144>`__ **14**, 693 (2018) is also available.

.. _recent_changes--local-density-fitting-hartree-fock-and-kohn-sham-ldf-hf-ldf-ks:

Local density fitting Hartree-Fock and Kohn-Sham (LDF-HF, LDF-KS)
-----------------------------------------------------------------

A new parallel implementation of Hartree Fock with local density fitting (closed and open-shell), as described in C. Köppl, H.-J. Werner, `J. Chem. Theory Comput. <https://dx.doi.org/10.1021/acs.jctc.6b00251>`__ **12**, 3122 (2016). This program can run in parallel across several nodes and is for large systems significantly faster than canonical DF-HF, DF-KS.

.. _recent_changes--local-complete-active-space-second-order-perturbation-theory-with-pair-natural-orbitals-pno-caspt2:

Local complete active space second-order perturbation theory with pair natural orbitals (PNO-CASPT2)
----------------------------------------------------------------------------------------------------

An accurate and efficient local PNO-CASPT2 for large molecules as described in F. Menezes, D. Kats, H.-J. Werner, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.4963019>`__ **145**, 124115 (2016). For extended systems the computational effort scales linearly with molecular size. A multi-state version will be made available soon.

.. _recent_changes--pno-lccsd-t-f12-1:

PNO-LCCSD(T)-F12
----------------

Explicitly correlated well parallelized PNO methods are now available up to the PNO-LCCSD(T)-F12 level. This program yields results that are very close to the corresponding canonical CCSD(T)-F12 ones. For medium size cases where canonical calculations are still feasible, the PNO-LCCSD(T)-F12 is up to an order of magnitude faster than the canonical CCSD(T)-F12 program, while relative energies typically differ by only 0.2 kcal/mol. The largest applications so far include molecules with up to about 300 atoms and 10000 basis functions. The methods are described in H.-J. Werner, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.4968595>`__ **145**, 201101 (2016). M. Schwilk, Q. Ma, C. Köppl, H.-J. Werner, `J. Chem. Theory Comput. <https://dx.doi.org/10.1021/acs.jctc.7b00554>`__ **13**, 3650 (2017); Q. Ma, M. Schwilk, C. Köppl, H.-J. Werner, `J. Chem. Theory Comput. <https://dx.doi.org/10.1021/acs.jctc.7b00799>`__ **13**, 4871 (2017); Q. Ma and H.-J. Werner, `J. Chem. Theory Comput. <https://dx.doi.org/10.1021/acs.jctc.7b01141>`__ **14**, 198 (2018). A review can be found in Q. Ma and H.-J. Werner, WIREs Comput. Mol. Sci. 2018;e1371. References for PNO-LMP2 and PNO-LMP2-F12 are given under "New features for Molpro2015.1".

.. _recent_changes--d4-dispersion-correction-for-dft:

D4 dispersion correction for DFT
--------------------------------

The new D4 dispersion model improves the description of atomic dispersion coefficients through charge-dependent local polarisabilities obtained by a self-consistent tight-binding method, see E. Caldeweyher, C. Bannwarth, and S. Grimme `J. Chem. Phys. <https://dx.doi.org/10.1063/1.4993215>`__ **147**, 034112 (2017)

.. _recent_changes--nonlocal-dft-method:

Nonlocal DFT method
-------------------

The nonlocal DFT method (NLDFT) improves the description of long-range correlation interactions of standard DFT functionals through a double-Hirshfeld partitioning of the correlation energy density, see A. Heßelmann, `J. Chem. Theory Comput. <https://dx.doi.org/10.1021/ct300735g>`__ **9**, 273 (2013).

.. _recent_changes--kohn-sham-rpa-methods:

Kohn-Sham RPA methods
---------------------

Random-phase approximation electron correlation methods based on Kohn-Sham reference determinants, see Refs. A. Heßelmann, `Phys. Rev. A <https://dx.doi.org/10.1103/PhysRevA.85.012517>`__ **85**, 012517 (2012); A. Heßelmann and A. Görling, `J. Chem. Theory Comput. <https://dx.doi.org/10.1021/ct4007212>`__ **9**, 4382 (2013).

.. _recent_changes--new-features-in-dft-sapt:

New features in DFT-SAPT
------------------------

Several new features have been implemented in the DFT-SAPT program, including:

* Exchange interaction energy contributions without the single-exchange approximation (R. Schäffer and G. Jansen,  *Theor. Chem. Acc.* **131** (2012) 1235; `Mol. Phys. <https://dx.doi.org/10.1080/00268976.2013.827253>`__ **111**, 2570 (2013))
* DFT-SAPT employing exact-exchange response kernels (A. Heßelmann, `J. Chem. Theory Comput. <https://dx.doi.org/10.1021/acs.jctc.7b01233>`__ **14**, 1943 (2018))
* Regularised SAPT for estimating short-range polarisation interactions (A. J. Misquitta, `J. Chem. Theory Comput. <https://dx.doi.org/10.1021/ct400704a>`__ **9**, 5313 (2013))

.. _recent_changes--automated-selection-of-molecular-active-space-avas:

Automated selection of molecular active space (AVAS)
----------------------------------------------------

This method helps to find good starting orbitals for CASSCF calculations. It is based on the work of Knizia et al., `J. Chem. Theory Comput. <https://dx.doi.org/10.1021/acs.jctc.7b00128>`__ **13**, 4063 (2017).

.. _recent_changes--further-enhancements:

Further enhancements
--------------------

* Improved parallelization of coupled-cluster codes

* Improved DFT quadrature

* New plugin interfaces for other programs, e.g. MR-CCSD(T), DMRG and FCIQMC codes, supporting directed parallel execution

* Implementation of the eXact-2-Component (X2C) scalar relativistic Hamilitonian

* Support for a Gaussian finite nucleus model

* New correlation consistent basis sets for heavy alkali and alkaline earth elements (both relativistic all-electron and with ECPs), as well as all-electron (DK3 and X2C) basis sets for the lanthanide and actinide elements.
* X2C-contracted versions for all the standard correlation consistent basis sets for H, He, B-Ne, and Al-Cl, e.g., cc-pVDZ-X2C

.. _recent_changes--new-features-of-molpro2015-1:

New features of MOLPRO2015.1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Molpro 2015 contains many improvements, bug-fixes and new features. Only the most important ones are listed in the following.

.. _recent_changes--projection-based-wavefunction-in-dft-embedding:

Projection-based wavefunction-in-DFT embedding
----------------------------------------------

The WF-in-DFT implementation in Molpro [F. R. Manby et al., `J. Chem. Theory Comput. <https://dx.doi.org/10.1021/ct300544e>`__ **8**, 2564 (2012)] permits embedding of almost any ground-state wavefunction method in Molpro in an environment described by DFT.

.. _recent_changes--intrinsic-bond-orbital-analysis-and-orbital-localization-ibo:

Intrinsic bond-orbital analysis and orbital localization (IBO).
---------------------------------------------------------------

IBOs provide a reliable and efficient way to generate localized orbitals and to analyze wavefunctions, see G. Knizia, `J. Chem. Theory Comput. <https://dx.doi.org/10.1021/ct400687b>`__ **9**, 4834 (2013)

.. _recent_changes--interface-to-nbo6:

Interface to NBO6
-----------------

Molpro 2015 supports NBO6 Natural Bond Orbital Analysis (NBO6) via an interface. NBO6 must be licensed separately.

.. _recent_changes--beyond-lmp2-treatment-of-intermolecular-pairs-in-local-coupled-cluster-methods:

Beyond LMP2 treatment of intermolecular pairs in local coupled cluster methods
------------------------------------------------------------------------------

Usually close (and weak) pairs are treated only at the LMP2 level in LCCSD(T) calculations. This not satisfying since LMP2 often treats van der Waals interactions poorly, hence compromising the high accuracy of the actual LCCSD(T) calculation. Fortunately, close pairs can now be treated in an inexpensive way at a level beyond LMP2, ranging from local direct RPA *via* ring CCD to LCCD[S]-R\ :math:`^{-6}`. This is described in

O. Masur, D. Usvyat and M. Schütz, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.4826534>`__ **139**, 164116 (2013);
M. Schütz, O. Masur and D. Usvyat, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.4884156>`__ **140**, 244107 (2014).

.. _recent_changes--distinguishable-cluster-approximation-dcsd-and-dcsd-f12:

Distinguishable cluster Approximation (DCSD and DCSD-F12)
---------------------------------------------------------

This approximation yields improved results at the cost of CCSD. In particular, DCSD equilibrium structures are as accurate as for CCSD(T), see

D. Kats and F. R. Manby, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.4813481>`__ **139**, 021102 (2013);
D. Kats, J. Chem. Phys. **141i**, 061101 (2014);
D. Kats, D. Kreplin, H.-J. Werner, F. R. Manby, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.4907591>`__ **142**, 064111 (2015).

.. _recent_changes--analytical-energy-gradients-2:

Analytical energy gradients
---------------------------

Analytical gradients are now available for DCSD. Analytical gradients for CCSD(T), as well as for MP2-F12, CCSD(T)-F12, and DCSD-F12 are under development and will be made available free of charge at a later stage.

.. _recent_changes--orbital-relaxed-properties-and-analytical-nuclear-gradients-for-excited-states:

Orbital relaxed properties and analytical nuclear gradients for excited states
------------------------------------------------------------------------------

Orbital relaxed properties, and analytical nuclear gradients for excited states are now available for local CC2 response and local ADC(2). This allows for geometry optimizations of excited states of large chromophores at these levels of theory. Furthermore, also local ADC(2) transition moments at the level of strict ADC(2) (which require second-order ground state singles and doubles) are available. For further reference see

K. Ledermüller, D.Kats and M. Schütz, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.4818586>`__ **139**, 084111 (2013);
K. Ledermüller and M. Schütz, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.4872169>`__ **140**, 164113 (2014);
M. Schütz, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.4921839>`__ **142**, 214103 (2015).

.. _recent_changes--pno-lmp2-and-pno-lmp2-f12:

PNO-LMP2 and PNO-LMP2-F12
-------------------------

New parallel linear scaling PNO-LMP2 and PNO-LMP2-F12 programs as described in

H.-J. Werner, G. Knizia, C. Krause, and M. Schwilk, `J. Chem. Theory Comput. <https://dx.doi.org/10.1021/ct500725e>`__ **11**, 484 (2015);
Q. Ma and H.-J. Werner, J. Chem. Theory Comput., DOI: 10.1021/acs.jctc.5b00843 (2015);
C. Köppl and H.-J. Werner, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.4918772>`__ **142**, 164108 (2015).

are available in version 2015. PNO-LCCSD(T) is currently under development and will be made freely available to licensees of Molpro 2015 at a later stage.

.. _recent_changes--magnetizability-and-rotational-g-tensor-at-df-lmp2-level-using-giaos:

Magnetizability and rotational g-tensor at DF-LMP2 level using GIAOs
--------------------------------------------------------------------

The program for NMR chemical shifts has been extended to include also magnetizability and rotational g-tensor. This is described in

S. Loibl and M. Schütz, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.4884959>`__ **141**, 024108 (2014).

.. _recent_changes--faster-density-fitting-integral-routines:

Faster density fitting integral routines
----------------------------------------

DFT and F12 methods with density fitting are significantly speeded up using improved integration routines written by G. Knizia.

.. _recent_changes--vibrational-perturbation-theory-vpt2:

Vibrational perturbation theory: VPT2
-------------------------------------

A VPT2 program based on a semi-quartic force field (QFF) has been implemented, which allows for low-cost evaluations of anharmonic vibrational frequencies and associated vibrational constants. The determination of the QFF does not require analytical gradients (see the ``SURF`` program) and can thus been used in combination with any electronic structure method.

.. _recent_changes--vibrational-multi-reference-methods-vmcscf-vmrci:

Vibrational multi-reference methods: VMCSCF, VMRCI
--------------------------------------------------

A suite of vibrational multi-reference methods is available now. Modals can be optimized at the VMCSCF level [S. Heislbetz and G. Rauhut, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3364861>`__ **132**, 124102 (2012)] and correlation effects can be accounted for either variationally (VMRCI [F. Pfeiffer and G. Rauhut, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.4865098>`__ **140**, 064110 (2014)].

.. _recent_changes--anharmonic-franck-condon-factors-fcon:

Anharmonic Franck-Condon factors: FCON
--------------------------------------

A Franck-Condon program based on anharmonic vibrational wavefunctions has been implemented. Franck-Condon factors can either be computed by rotating the vibrational wavefunction or by transforming the potential energy surface in order to account for Duschinsky effects. This program, which allows for the accurate calculation of photoelectron spectra (absorption and fluorescence) relies on the newly developed transformation program ``SURFTRANS`` [P. Meier and G. Rauhut, J. Chem. Phys. (2015)].

.. _recent_changes--transformation-of-multi-dimensional-potential-energy-surfaces-pestrans:

Transformation of multi-dimensional potential energy surfaces: PESTRANS
-----------------------------------------------------------------------

Multi-dimensional potential energy surfaces spanned in terms of normal coordinates - as computed with the ``SURF`` program - can now be rotated or transformed into an arbitrary set of normal coordinates. This allows for the efficient calculation of Franck-Condon factors or the calculation of vibrational spectra of isotopologues from just one potential energy surface [P. Meier, D. Oschetzki, R. Berger and G. Rauhut, J. Chem. Phys. **140**, 184111 (2014)].

.. _recent_changes--localized-normal-coordinates:

Localized normal coordinates
----------------------------

Within the ``SURF`` program, multi-dimensional potential energy surfaces can now alternatively be spanned in terms of localized normal coordinates. Three localization schemes are offered: (a) localization of the CH-stretching modes only and (b) localization of all normal coordinates to the subunits in molecular cluster calculations or (c) both. All localization schemes are symmetry sensitive.

.. _recent_changes--calculation-of-arbitrary-vibrational-states-vibstate:

Calculation of arbitrary vibrational states: VIBSTATE
-----------------------------------------------------

In the old Molpro release the calculation of vibrational states was limited to fundamentals, first vibrational overtones and simple combination bands. The new ``VIBSTATE`` program allows to specify arbitrary vibrational states, but the user must take care, that the parameters in the ``SURF`` program and the vibrational correlation programs are adjusted accordingly.

.. _recent_changes--raman-scattering-activities:

Raman scattering activities
---------------------------

Raman scattering activities can now be computed within all vibrational SCF and vibration correlation programs. As polarizabilities can only be determined at the Hartree-Fock level, the accuracy is currently still limited.

.. _recent_changes--reaction-databases:

Reaction databases
------------------

A facility is provided to store and interrogate sets of molecules, together with information about how they are to be combined in balanced chemical equations. This database can be generated manually, or partially by running appropriate Molpro calculations. Analysis of the database can give a summary of the energy changes associated with each described reaction, and two or more similar databases can be compared reaction by reaction, to give a statistical analysis of the differences between them. Several common databases are included.

.. _recent_changes--new-density-fitting-dft-sapt-program:

New density-fitting DFT-SAPT program
------------------------------------

A new DFT-SAPT program has been implemented in Molpro which can be used in conjunction with monomer-centered (MCBS), monomer-centered plus (MC+BS) or dimer-centered (DCBS) basis sets. Even in DCBS mode fairly large complexes with about 800 electrons can be studied with this program, see A. Heßelmann and T. Korona. `J. Chem. Phys. <https://dx.doi.org/10.1063/1.4893990>`__ **141**, 094107 (2014).

.. _recent_changes--new-features-of-molpro2012-1:

New features of MOLPRO2012.1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A summary of the features in Molpro can be found in a recent review: H.-J. Werner, P. J. Knowles, G. Knizia, F. R. Manby, and M. Schütz, *Molpro – a general purpose quantum chemistry program package*, WIRES Comput. Mol. Sci. **2**, 242 (2012), `10.1002/wcms.82 <https://dx.doi.org/10.1002/wcms.82>`__.

The new features of Molpro version 2012.1 include the following.

.. _recent_changes--quasi-variational-coupled-cluster-theory:

Quasi-variational coupled-cluster theory
----------------------------------------

This modification of standard CCSD is capable of robustly describing chemical bond breaking with a single Hartree-Fock reference determinant (see J. B. Robinson and P. J. Knowles, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3680560>`__ **136**, 054114 (2012), `10.1063/1.3680560 <https://dx.doi.org/10.1063/1.3680560>`__). It is implemented for closed-shell systems, with either the Brueckner condition or energy optimisation for the determination of orbitals. Triple excitations can be included perturbatively, ``BQVCCD(T)`` or ``OQVCCD(T)`` (J. B. Robinson and P. J. Knowles, `Phys. Chem. Chem. Phys. <https://dx.doi.org/10.1039/C2CP40698E>`__ **14**, 6729-6732 (2012), `10.1039/C2CP40698E <https://dx.doi.org/10.1039/C2CP40698E>`__; J. Chem. Theor. Comput. **8**, 2653-2660 (2012), `10.1021/ct300416b <https://dx.doi.org/10.1021/ct300416b>`__).

.. _recent_changes--a-new-internally-contracted-mrci-code-mrcic:

A new internally contracted MRCI code: MRCIC
--------------------------------------------

A new internally contracted MRCI code [see K. R. Shamasundar, G. Knizia, and H.-J. Werner, *A new internally contracted multi-reference configuration interaction (MRCI) method*, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3609809>`__ **135**, 054101 (2011)] is now available. As compared to the old MRCI code it has the following advantages: (i) inactive orbitals (correlated in MRCI but closed-shell in the reference function) are treated explicitly, i.e., no density matrices and coupling coefficients need to be computed that involve these orbitals. Thus, in principle any number of inactive orbitals can be correlated, without the previously existing limitation to 32 correlated orbitals. Furthermore, additional configuration spaces are internally contracted (as in the RS2C code), resulting in a much improved efficiency, particularly for cases with many inactive orbitals. Currently, the method is implemented only for single-state calculations, but an extension to multi-state cases is under development and will be provided in the near future.

.. _recent_changes--explicitly-correlated-multireference-theories-rs2-f12-mrci-f12:

Explicitly correlated multireference theories: RS2-F12, MRCI-F12
----------------------------------------------------------------

Explicitly correlated multireference theories (CASPT2-F12, MRCI-F12) as described in T. Shiozaki and H.-J. Werner, *Communication: Second-order multireference perturbation theory with explicit correlation: CASPT2-F12*, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3489000>`__ **133**, 141103 (2010); T. Shiozaki, G. Knizia, and H.-J. Werner, *Explicitly correlated multireference configuration interaction: MRCI-F12*, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3528720>`__ **134**, 034113 (2011); T. Shiozaki and H.-J. Werner, *Explicitly correlated multireference configuration interaction with multiple reference functions: Avoided crossings and conical intersections*, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3587632>`__ **134**, 184104 (2011) lead to much improved convergence of the correlation energies with the basis set size. Explicitly correlated version of the RS2C and MRCIC codes are not yet available but will be made available as soon as possible.

A review of the explicitly correlated multireference methods can be found in T. Shiozaki and H.-J. Werner, `Mol. Phys. <https://dx.doi.org/10.1080/00268976.2013.779393>`__ **111**, 607 (2013).

.. _recent_changes--extended-multi-state-caspt2:

Extended multi-state CASPT2
---------------------------

Extended multistate CASPT2 (XMS-CASPT2) [see T. Shiozaki, W. Győrffy, P. Celani, and H.-J. Werner, *Communication: The extended multi-state CASPT2 method: Energy and nuclear gradients*, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3633329>`__ **135**, 081106 (2011)] provides a better description of near degenerate situations and avoided crossings. Currently this option is available only with the ``RS2`` code, not for ``RS2C``.

.. _recent_changes--density-fitted-casscf-and-caspt2:

Density fitted CASSCF and CASPT2
--------------------------------

CASSCF and CASPT2 as well as the corresponding analytical gradient theories are now available with density fitting (``DF-CASSCF``, ``DF-RS2``). See details in W. Győrffy, T. Shiozaki, G. Knizia, and H.-J. Werner, *Analytical energy gradients for second-order multireference perturbation theory using density fitting*, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.4793737>`__ **138**, 104104 (2013).

.. _recent_changes--extensions-of-explicitly-correlated-coupled-cluster-methods:

Extensions of explicitly correlated coupled-cluster methods
-----------------------------------------------------------

The (F12\*) approximation proposed by Hättig et al. `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3442368>`__ **132**, 231102 (2010) has been implemented for closed-shell cases (in Molpro, this is denoted F12c). Other recent work (partly already included in Molpro2010.1) is described in H.-J. Werner, G. Knizia, and F. R. Manby, *Explicitly correlated coupled-cluster methods with pair-specific geminals*, `Mol. Phys. <https://dx.doi.org/10.1080/00268976.2010.526641>`__ **109**, 407 (2011); K. A. Peterson, C. Krause, H. Stoll, J. G. Hill, and H.-J. Werner, *Application of explicitly correlated coupled-cluster methods to molecules containing post-3:math:`d` main group elements*, `Mol. Phys. <https://dx.doi.org/10.1080/00268976.2011.624129>`__ **109**, 2607 (2011) for alternative approximations.

Further basis sets of K. A. Peterson and J.G. Hill for explicitly correlated methods have been included. In particular these include the aug-cc-pVnZ-PP/OptRI and aug-cc-pwCVnZ-PP/OptRI sets for the group 11 and 12 transition metals. A full set of F12 basis sets for the :math:`p`-block elements Ga-Rn will be added in the very near future. For recent work on molecules containing transition metals see D. H. Bross, J. G. Hill, H.-J. Werner, and Kirk A. Peterson, *Explicitly correlated composite thermochemistry of transition metal species*, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.4818725>`__ **139**, 094302 (2013).

.. _recent_changes--density-fitted-local-coupled-cluster-methods-df-lccsd-t-df-luccsd-t-df-lrpa:

Density fitted local coupled-cluster methods: DF-LCCSD(T), DF-LUCCSD(T), DF-LRPA
--------------------------------------------------------------------------------

The local coupled cluster methods have been further improved. See H.-J. Werner and M. Schütz, *An efficient local coupled-cluster method for accurate thermochemistry of large systems*, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3641642>`__ **135**, 144116 (2011) for a description of the current implementation. An open-shell implementation [DF-LUCCSD(T)] is now also available (Y. Liu and H.-J. Werner, to be published.) Furthermore, the direct random phase approximation (RPA) has been implemented as a local method and using density fitting. Direct RPA can be considered as a CCD method reduced to only ring diagrams. In contrast tp MP2 it also contains higher-order diagrams which e.g. cover Axilrod-Teller terms in intermolecular calculations. It is therefore especially attractive to replace in LCC calculations the LMP2 method for weak pairs by LRPA. This is now possible in our LCC code (O. Masur and M. Schütz, to be published.)

.. _recent_changes--local-coupled-cluster-methods-with-orbital-specific-virtual-orbitals-osv-lccsd-t:

Local coupled-cluster methods with orbital-specific virtual orbitals: OSV-LCCSD(T)
----------------------------------------------------------------------------------

Local coupled cluster methods can optionally use orbital specific virtual orbitals (OSVs), see J. Yang, G. K. L. Chan, F. R. Manby, M. Schütz, and H.-J. Werner, *The orbital-specific virtual local coupled-cluster singles and doubles method: OSV-LCCSD*, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3696963>`__ **136**, 144105 (2012). The main advantage of this method is that the accuracy of the domain approximation can be controlled by a single parameter. Further developments that also use pair-natural orbitals (PNOs) as described in C. Krause and H.-J. Werner, *Perspective: Comparison of explicitly correlated local coupled-cluster methods with various choices of virtual orbitals*, `Phys. Chem. Chem. Phys. <https://dx.doi.org/10.1039/C2CP40231A>`__ **14**, 7591-7604 (2012) are in progress. A preliminary parallel PNO-LMP2-F12 method is already available.

.. _recent_changes--explicitly-correlated-local-mp2-and-cc-methods-df-lmp2-f12-df-lccsd-t-f12:

Explicitly correlated local MP2 and CC methods: DF-LMP2-F12, DF-LCCSD(T)-F12
----------------------------------------------------------------------------

The explicitly correlated coupled cluster methods as described in H.-J. Werner, *Eliminating the domain error in local explicitly correlated second-order Møller-Plesset perturbation theory*, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.2982419>`__ **129**, 101103 (2008); T. B. Adler, F. R. Manby, and H.-J. Werner, *Local explicitly correlated second-order perturbation theory for the accurate treatment of large molecules*, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3040174>`__ **130**, 054106 (2009); T. B. Adler and H.-J. Werner, *Local explicitly correlated coupled-cluster methods: Efficient removal of the basis set incompleteness and domain errors*, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3160675>`__ **130**, 241101 (2009); T. B. Adler and H.-J. Werner, *An explicitly correlated local coupled-cluster method for calculations of large molecules close to the basis set limit*, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3647565>`__ **135**, 144117 (2011) are available for closed-shell cases (an open-shell implementation will follow soon). In these methods the errors of the local domain approximation are eliminated to a large extend, and the same accuracy as with the corresponding canonical methods can be achieved, even for molecules with 50-100 atoms.

.. _recent_changes--improved-dft-with-density-fitting:

Improved DFT with density fitting
---------------------------------

The efficiency of density functional theory has been much improved. In particular, the density fitting (DF-RKS, DF-UKS) codes for analytical energy gradients are now very much faster, due to a new integral code (adaptive integral core, AIC) written by G. Knizia. Some benchmarks can be found in H.-J. Werner, P. J. Knowles, G. Knizia, F. R. Manby, and M. Schütz, *Molpro – a general purpose quantum chemistry program package*, WIRES Comput. Mol. Sci. **2**, 242 (2012).

.. _recent_changes--additional-density-functionals:

Additional density functionals
------------------------------

A large number of additional density functionals has been added, including PBE0, PBEREV, M05, M05-2X, M06, M06-2X, M06-L, M06-HF, M08-HX, M08-SO, M11-L, SOGGA, SOGGA11, SOGGA11-X. (M11 is currently not available, but will likely be added in the near future).

.. _recent_changes--additional-gradient-theories-ccsd-df-mp2-df-casscf-df-rs2:

Additional gradient theories: CCSD, DF-MP2, DF-CASSCF, DF-RS2
-------------------------------------------------------------

New analytical gradient codes are now available for DF-MP2, DF-CASSCF, DF-RS2 (including MS and XMS options, also without density fitting), and for CCSD.

.. _recent_changes--local-methods-for-excited-states:

Local methods for excited states
--------------------------------

First-order properties of excited states via time-dependent Local CC2 linear response theory and ADC(2) are now also available for triplet states. This is described in K. Freundorfer, D. Kats, T. Korona, and M. Schütz, *Local CC2 response method for triplet states based on Laplace transform: Excitation energies and first-order properties*, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3506684>`__ **133**, 244110 (2010);

.. _recent_changes--nmr-shielding-tensors-at-df-lmp2-level-using-giaos:

NMR shielding tensors at DF-LMP2 level using GIAOs
--------------------------------------------------

An efficient method for calculating NMR shielding tensors at the local MP2 level has been implemented. Gauge including atomic orbitals (GIAOs) are used to eliminate the gauge origin dependence. Density fitting is employed to factorize the relevant electron repulsion integrals and their derivatives w.r. to the magnetic field. So far, the method has been already applied to systems with more than 2500 contracted basis functions and 300 correlated electrons. Relevant publications are S. Loibl, F. R. Manby, and M. Schütz, *Density fitted, local Hartree-Fock treatment of NMR chemical shifts using London atomic orbitals*, `Mol. Phys. <https://dx.doi.org/10.1080/00268970903580133>`__ **108**, 477 (2010), and S. Loibl and M. Schütz, *NMR shielding tensors for density fitted local second-order Møller-Plesset perturbation theory using gauge including atomic orbitals*, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.4744102>`__ **137**, 084107 (2012).

.. _recent_changes--sapt-ccsd:

SAPT(CCSD)
----------

Symmetry-adapted perturbation theory of intermolecular interactions with monomers described in the CCSD level.

.. _recent_changes--improved-scf-algorithms-for-high-spin-open-shell-systems:

Improved SCF algorithms for high-spin open-shell systems
--------------------------------------------------------

For open-shell systems, RHF and RKS now use a two-step diagonalization process by default: Here the beta orbitals are found by a second diagonalization in the subspace of occupied alpha orbitals. This process usually leads to more stable convergence in difficult cases, compared to the standard diagonalization of a single open-shell Fock matrix (the latter behavior is recovered by {rhf,algo=0}). An additional section with suggestions for dealing with difficult cases has been added to be manual under “The SCF program”. Additionally, various limitations of the SCF program have been lifted. In particular, {rhf; maxit,1} now always works, and just calculates a Fock matrix and energy from the input orbitals, without updating said orbitals.

.. _recent_changes--fciqmc-stochastic-full-ci:

FCIQMC: Stochastic Full CI
--------------------------

The FCIQMC program exists through an interface to the ``NECI`` codebase, which is actively developed in the group of A. Alavi, and has been integrated in to the Molpro code. The FCIQMC method is a recently introduced stochastic method which can calculate in principle FCI-quality energies for small to medium-sized molecules. See G. H. Booth, A. J. W. Thom, and A. Alavi, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3193710>`__ **131**, 054106 (2009); D. M. Cleland, G. H. Booth, and A. Alavi, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3525712>`__ **134**, 024112 (2011); G. H. Booth, D. M. Cleland, A. J. W. Thom, and A. Alavi, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3624383>`__ **135**, 084104 (2011).

.. _recent_changes--ab-initio-multiple-spawning-dynamics:

Ab Initio Multiple Spawning Dynamics
------------------------------------

The AIMS module implements the Ab Initio Multiple Spawning method to perform dynamics calculations on multiple electronic states. It can also be used quite generally for first principles molecular dynamics on a single electronic surface, provided that nuclear gradients are available. Currently, non-adiabatic dynamics is limited to CASSCF wavefunctions; however, MS-CASPT2 non-adiabatic dynamics (with an implementation of analytical MS-CASPT2 non-adiabatic couplings) will be provided in the very near future. See M. Ben-Nun and T. J. Martinez, `Chem. Phys. Lett. <https://dx.doi.org/10.1016/S0009-2614(98)01115-4>`__ **298**, 57 (1998); B. G. Levine, J. D. Coe, A. M. Virshup and T. J. Martinez, Chem. Phys. **347**, 3 (2008); T. Mori, W. J. Glover, M. S. Schuurman and T. J. Martinez, J. Phys. Chem. A **116**, 2808 (2012).

.. _recent_changes--updated-def2-basis-sets:

Updated def2 basis sets
-----------------------

The partially augmented Turbomole basis sets def2-SVPD, def2-TZVPD, and def2-QZVPPD (Rappoport, Furche: `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3484283>`__ **133**, 134105 (2010)) have been added to the library. Additionally, the recently developed dhf- variants of the def2- basis sets have been included (dhf-SVP, dhf-TZVPP, ..., Weigend, Baldes: `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3495681>`__ **133**, 174102 (2010)); these are reoptimized versions for the more modern MDF effective core potentials (most elements used MDF ECPs already in def2- and are unchanged). Short names like TZVPP (without prefix) now refer to dhf- basis sets.

.. _recent_changes--parallel-builds-merged:

Parallel builds merged
----------------------

The MPP and MPPX builds of Molpro have been merged and the decision to run in MPP or MPPX mode made a run-time option. To build parallel Molpro the ``-mpp`` flag to configure should be used; the ``-mppx`` flag is no longer required or valid. When running parallel Molpro, the ``--mpp`` option (default) can be used to specify MPP mode, and the ``--mppx`` option for MPPX mode.

.. _recent_changes--auto-build-options-for-parallel-configuration:

Auto-build options for parallel configuration
---------------------------------------------

New options for configuring parallel Molpro to run on a single node or workstation have been implemented. These options (see manual) are prefixed with ``-auto``, and in conjunction with ``-mpp`` configure will download, build and install a variety of different prerequisites for parallel Molpro.

.. _recent_changes--new-features-of-molpro2010-1:

New features of MOLPRO2010.1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The functionality is essentially the same as in 2009.1, but many bug fixes and small improvements have been added. Please note the following major changes, in particular of the default RI basis sets in explicitly correlated methods as described below.

.. _recent_changes--aic-density-fitting-integral-program:

AIC density fitting integral program
------------------------------------

A faster integral program for density fitting, written by Gerald Knizia, has been added. In particular this speeds up the integral evaluation in F12 calculations by up to a factor of about 10 (depending on the basis set). This program is now used by default, but can be disabled by setting

``dfit,aic=0``

in the beginning of the input.

.. _recent_changes--pair-specific-geminal-exponents-in-explicitly-correlated-methods:

Pair specific geminal exponents in explicitly correlated methods
----------------------------------------------------------------

Different exponents for the Slater-type geminals can be used for valence-valence, core-valence, and core-core pairs. See manual for details.

.. _recent_changes--change-of-defaults-in-explicitly-correlated-methods:

Change of defaults in explicitly correlated methods
---------------------------------------------------

For explicitly correlated F12 calculations that use the VnZ-F12 orbital basis sets (OBS), it is now the default to use the corresponding VnZ-F12/OPTRI basis sets to construct the complementary auxiliary orbital basis (CABS). In case that CABS is not used (e.g., in LMP2-F12), the OBS and OPTRI sets are merged automatically. This yields exactly the same results as would be obtained with the CABS approach. In order to use the default RI sets of 2009.1, please specify option RI_BASIS=JKFIT on the command line, or

``explicit,ri_basis=jkfit``

For compatibility reasons, it is still the default to use the JKFIT sets as RI basis for the AVnZ orbital basis sets. In order to use the corresponding OPTRI sets (where available) please specify option RI_BASIS=OPTRI.

.. _recent_changes--new-basis-sets-in-the-molpro-library:

New basis sets in the Molpro library
------------------------------------

A number of new basis sets have been added to the Molpro library since version 2009.1. The references for these sets can be found in the headers of the respective libmol files.

* **Li, Be, Na, Mg:** a) New official versions of the correlation consistent basis sets for these elements have been added, both non-relativistic and those contracted for Douglas-Kroll relativistic calculations. Specifically these are: cc-pVnZ (n=D-5) cc-pwCVnZ (n=D-5) aug-cc-pVnZ (n=D-5) aug-cc-pwCVnZ (n=D-5) and the above with a -DK extension. The older cc-pVnZ basis sets for these elements can still be accessed via the keywords vdz-old, etc. b) New basis sets, including RI and MP2 auxiliary sets, have been added for F12 explicit correlation calculations: cc-pVnZ-F12 (n=D-Q) cc-pCVnZ-F12 (n=D-Q) The optimized CABS auxiliary sets have the same name but with a /OptRI context For MP2 and CCSD auxiliary sets, the cc-pVnZ/MP2FIT sets of Hättig can be used, but a new cc-pV5Z/MP2FIT set has been added that is optimal for the new cc-pV5Z basis set; new aug-cc-pVnZ/MP2FIT (n=D-5) sets have been added as well. The original cc-pV5Z/MP2FIT sets of Hättig have been renamed v5z-old/mp2fit.
* **Cu-Zn, Y-Cd, Hf-Hg:** a) While the aug-cc-pVnZ-PP (n=D-5) and cc-pwCVnZ-PP (n=D-5) sets were already available, the combination aug-cc-pwCVnZ-PP was not yet defined. These have now been added for these elements. b) Triple-zeta DK sets have been included now for all of these elements. Unless otherwise noted, these were optimized for 2nd-order DKH. In the cases of Hf-Hg, sets contracted for 3rd-order DKH are also now included: cc-pVTZ-DK cc-pwCVTZ-DK aug-cc-pVTZ-DK aug-cc-pwCVTZ-DK and the above with -DK replaced by -DK3 for DKH3 calculations in the case of Hf-Hg.
* **H-He, B-Ne, Al-Ar, Ga-Kr:** a) A variety of DK contracted basis sets have been added for these elements: aug-cc-pVnZ-DK (n=D-5) cc-pCVnZ-DK (n=D-5) cc-pwCVnZ-DK (n=D-5) aug-cc-pCVnZ-DK (n=D-5) aug-cc-pwCVnZ-DK (n=D-5) b) Official cc-pCV6Z and aug-cc-pCV6Z are now also available for Al-Ar c) For explicitly correlated calculations, the core-valence sets have been added: cc-pCVnZ-F12 (n=D-Q) for B-Ne, Al-Ar cc-pCVnZ-F12/OptRI (n=D-Q) for B-Ne, Al-Ar d) cc-pVnZ-F12/OptRI (n=D-Q) as also been added for He
* **Turbomole def2 basis sets:** The complete Turbomole def2 basis set family has been added to the Molpro basis library (for all elements H to Rn, except Lanthanides). The def2-orbital basis sets can now be accessed as SV(P), SVP, TZVP, TZVPP, QZVP and QZVPP. In this nomenclature SVP, TZVPP, and QZVPP correspond to valence double-zeta (VDZ), valence triple-zeta (VTZ) and valence quadruple-zeta (VQZ) basis sets, respectively. Auxiliary density fitting basis sets for all elements are available as well (e.g., TZVPP/JFIT, TZVPP/JKFIT, TZVPP/MP2FIT) and are chosen automatically in density-fitted calculations. Supposedly, the JKFIT sets are universal and also applicable in combination with the AVnZ basis sets. Initial results indicate that they also work well with the cc-pVnZ-PP and aug-cc-pVnZ-PP series of basis sets. The orbital basis sets can also be accessed in singly and doubly augmented versions (carrying A or DA prefixes, respectively, e.g., ASVP, DASVP), and the auxiliary fitting sets in singly augmented versions (e.g., ATZVPP/MP2FIT). The old Turbomole basis sets have been renamed; if required, they can be accessed with a def1-prefix (e..g, def1-SVP, def1-TZVPP, etc.).

.. _recent_changes--improved-support-for-mpi-implementation-of-parallelism:

Improved support for MPI implementation of parallelism
------------------------------------------------------

The *ppidd* harness that manages interprocess communication has been improved. The performance of the implementation based on pure MPI, as an alternative to use of the Global Arrays toolkit, is considerably improved, through the use of dedicated helper processes that service one-sided remote memory accesses.

.. _recent_changes--change-of-the-order-of-states-and-the-defaults-for-computing-the-davidson-correction-in-multi-state-mrci:

Change of the order of states and the defaults for computing the Davidson correction in multi-state MRCI
--------------------------------------------------------------------------------------------------------

The previous way to compute the Davidson correction in multi-state MRCI could lead to non-continuous cluster corrected energies. This is now avoided by ordering the MRCI eigenstates according to increasing energy (previously they were ordered according to maximum overlap with the reference wavefunctions). Furthermore, additional options for computing the Davidson correction in multi-state calculations are added (for details see manual). The old behavior can be recovered using options SWAP,ROTREF=-1.

.. _recent_changes--ipea-shift-for-caspt2:

IPEA shift for CASPT2
---------------------

A variant of the IPEA shift of G. Ghigo, B. O. Roos, and P.A. Malmqvist, `Chem. Phys. Lett. <https://dx.doi.org/10.1016/j.cplett.2004.08.032>`__ **396**, 142 (2004) has been added. The implementation is not exactly identical to the one in MOLCAS, since in our program the singly external configurations are not (RS2) or only partially (RS2C) contracted. The shift is invoked by giving option ``IPEA=``\ *shift* on the ``RS2`` or ``RS2C`` commands; the recommended value for *shift* is 0.25. For details of the implementation see manual.

.. _recent_changes--karton-martin-extrapolation-of-hf-energies:

Karton-Martin extrapolation of HF energies
------------------------------------------

The two-point formula for extrapolating the HF reference energy, as proposed by A. Karton and J. M. L. Martin, Theor. Chem. Acc. **115**, 330 (2006) has been added: :math:`E_{\rm HF,n}=E_{\rm HF,CBS} +A (n+1)\cdot \exp(-9 \sqrt{n})`. Use ``METHOD_R=KM`` for this.

.. _recent_changes--new-features-of-molpro2009-1:

New features of MOLPRO2009.1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _recent_changes--basis-set-updates:

Basis set updates
-----------------

Correlation consistent basis sets for Li, Be, Na, and Mg have been updated to their official versions as reported in Prascher et al., Theor. Chem. Acc. (2010). These now also include core-valence, diffuse augmented, and Douglas-Kroll relativistically contracted versions. The previous sets are still available but have been renamed vdz-old, vtz-old, etc.

.. _recent_changes--explicitly-correlated-calculations:

Explicitly correlated calculations
----------------------------------

Due to new findings, the default behavior of the F12 programs was changed in the following points:

- For open-shell systems the default wave function ansatz for was modified. This affects RMP2-F12 and open-shell CCSD-F12 calculations. The new default generally improves open-shell treatments and leads to more consistent behavior. The previous behavior can be restored by ``explicit,extgen=0`` (for more details see manual).
- The procedure for the construction of complementary auxiliary basis sets (CABS) and the thresholds were changed. This affects all non-local F12 calculations. The previous behavior can be restored by ``explicit,ortho_cabs=0,thrcabs=1-7,thrcabs_rel=1e-8``
- In numeric frequency calculations, the freezing of auxiliary basis sets was improved. This can affect calculations where many redundant functions are deleted.
- Pair energies for the explicitly correlated methods can be printed using ``print,pairs`` If inner-shell orbitals are correlated, the cc, cv, and vv contributions to the correlation energies are also printed.

.. _recent_changes--improvements-to-the-hartree-fock-program:

Improvements to the Hartree-Fock program
----------------------------------------

The atomic density guess in Hartree-Fock has been improved and extended. Guess basis sets are now available for most atoms and for all pseudopotentials. Most pseudopotentials have been linked to the appropriate basis sets, so that it is sufficient to specify, e.g.

.. code-block:: text

   basis=vtz-pp

which will select the correlation consistent triple zeta basis sets and the associated (small core) pseudopotential. Similarly, it is mostly sufficient to specify the basis set for other pseudopotential/basis set combinations.

If the wavefunction symmetry is not given in the Hartree-Fock input and not known from a previous calculation, the HF program attempts to determine it automatically from the aufbau principle (previously, symmetry 1 was assumed in all cases). For example,

.. code-block:: text

   geometry={n};
   {hf;wf,spin=3}

automatically finds that the wavefunction symmetry is 8.

.. _recent_changes--changes-to-geometry-input:

Changes to geometry input
-------------------------

- Rationalisation of options for molecular geometry. It is now illegal to specify symmetry and orientation options (eg x;noorient;angstrom) inside a geometry block, which now contains just the geometry specification (Z-matrix or XYZ). Options have to be specified using the new ORIENT and SYMMETRY commands, and/or existing commands such ANGSTROM. This change will, unfortunately, render many inputs incompatible with 2008.1 and earlier versions of Molpro, but has been introduced to allow correct and clean parsing of geometries containing, for example, yttrium atoms, which previously conflicted with the Y symmetry option.
- Simplification of geometry input. The program now detects automatically whether the geometry is specified as a Z-matrix, or using cartesian coordinates, and so there is no need any more to set the geomtyp variable. The standard XYZ format is still accepted for cartesian coordinates, but the first two lines (number of atoms, and a comment) can be omitted if desired.

.. _recent_changes--mpi-2-parallel-implementation:

MPI-2 parallel implementation
-----------------------------

The program now can be built from the source files with the Global Arrays toolkit or the MPI-2 library for parallel execution.

.. _recent_changes--new-features-of-molpro2008-1:

New features of MOLPRO2008.1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The new features of Molpro version 2008.1 include the following.

- Efficient closed-shell and open-shell MP2-F12 and CCSD(T)-F12 methods which dramatically improve the basis set convergence, as described in `J. Chem. Phys. <https://dx.doi.org/10.1063/1.2712434>`__ **126**, 164102 (2007); ibid. 127, 221106 (2007); ibid. 128, 154103 (2008).
- Natural bond order (NBO) and natural population analysis (NPA) as described in `Mol. Phys. <https://dx.doi.org/10.1080/00268970701628209>`__ **105**, 2753 (2007) and references therein.
- Correlation regions within a localized molecular orbital approach as described in `J. Chem. Phys. <https://dx.doi.org/10.1063/1.2884725>`__ **128**, 144106 (2008).
- Automated calculation of anharmonic vibrational frequencies and zero-point energies using VCI methods as described in `J. Chem. Phys. <https://dx.doi.org/10.1063/1.2718951>`__ **126**, 134108 (2007) and references therein.
- Coupling of DFT and coupled cluster methods as described in `Phys. Chem. Chem. Phys. <https://dx.doi.org/10.1039/B804672G>`__ **10**, 3353 (2008) and references therein.
- Enhanced connections to other programs, including molproView of output and 3-dimensional structures.
- Support for latest operating systems and compilers, including Mac OS X.

.. _recent_changes--new-features-of-molpro2006-1:

New features of MOLPRO2006.1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Features and enhancements in Molpro version 2006.1 most notably included efficient density fitting methods, explicitly correlated methods, local coupled cluster methods, and several new gradient programs: following:

- More consistent input language and input pre-checking.
- More flexible basis input, allowing to handle multiple basis sets
- New more efficient density functional implementation, additional density functionals.
- Low-order scaling local coupled cluster methods with perturbative treatment of triples excitations (LCCSD(T) and variants like LQCISD(T))
- Efficient density fitting (DF) programs for Hartree-Fock (DF-HF), Density functional Kohn-Sham theory (DF-KS), Second-order Møller-Plesset perturbation theory (DF-MP2), as well as for all local methods (DF-LMP2, DF-LMP4, DF-LQCISD(T), DF-LCCSD(T))
- Analytical QCISD(T) gradients
- Analytical MRPT2 (CASPT2) and MS-CASPT2 gradients, using state averaged MCSCF reference functions
- Analytical DF-HF, DF-KS, DF-LMP2, and DF-SCS-LMP2 gradients
- Explicitly correlated methods with density fitting: DF-MP2-R12/2A’, DF-MP2-F12/2A’ as well as the local variants DF-LMP2-R12/2\*A(loc) and DF-LMP2-F12/2\*A(loc).
- Coupling of multi-reference perturbation theory and configuration interaction (CIPT2)
- DFT-SAPT
- Transition moments and transition Hamiltonian between CASSCF and MRCI wavefunctions with different orbitals.
- A new spin-orbit integral program for generally contracted basis sets.
- Douglas-Kroll-Hess Hamiltonian up to arbitrary order.
- Improved procedures for geometry optimization and numerical Hessian calculations, including constrained optimization.
- Improved facilities to treat large lattices of point charges for QM/MM calculations, including lattice gradients (see section :doc:`QM/MM interfaces <qm_mm_interfaces>`) .
- An interface to the MRCC program of M. Kallay, allowing coupled-cluster calculations with arbitrary excitation level.
- Automatic *embarrassingly parallel* computation of numerical gradients and Hessians (``mppx Version``).
- Additional parallel codes, e.g. DF-HF, DF-KS, DF-LCCSD(T) (partly, including triples).
- Additional output formats for tables ( `XHTML, <http://www.w3.org/TR/xhtml1>`__ LaTeX, `Maple, <http://www.maplesoft.com>`__ `Mathematica, <http://www.wolfram.com>`__ `Matlab <http://www.mathworks.com>`__ and comma-separated variables), orbitals and basis sets (XML), and an optional well-formed XML output stream with important results marked up.

.. _recent_changes--new-features-of-molpro2002-6:

New features of MOLPRO2002.6
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Relative to version 2002.1, there are the following changes and additions:

- Support for IA-64 Linux systems (HP and NEC) and HP-UX 11.22 for IA-64 (Itanium2).
- Support for NEC-SX systems.
- Support for IBM-power4 systems.
- Modified handling of Molpro system variables. The ``SET`` command has changed (see sections :doc:`variables <variables>` and `system variables <variables.html#system-variables>`__) .
- The total charge of the molecule can be specified in a variable ``CHARGE`` or on the ``WF`` card (see section `defining the wavefunction <general_program_structure.html#defining-the-wavefunction>`__) .
- Improved numerical geometry optimization using symmetrical displacement coordinates (see sections `numerical gradients <energy_gradients.html#numerical-gradients>`__ and :doc:`geometry optimization (OPTG) <geometry_optimization_optg>`) .
- Improved numerical frequency calculations using the symmetry (``AUTO`` option (see section :doc:`harmonic vibrational frequencies (FREQUENCIES) <harmonic_vibrational_frequencies_frequencies>`) .

.. _recent_changes--new-features-of-molpro2002:

New features of MOLPRO2002
~~~~~~~~~~~~~~~~~~~~~~~~~~

Relative to version 2000.1, there are the following principal changes and additions:

- Modules direct and local are now included in the base version. This means that integral-direct procedures as described in

M. Schütz, R. Lindh, and H.-J. Werner, `Mol. Phys. <https://dx.doi.org/10.1080/00268979909483008>`__ **96**, 719 (1999),
linear-scaling local MP2, as described in
G. Hetzer, P. Pulay, and H.-J. Werner, `Chem. Phys. Lett. <https://dx.doi.org/10.1016/S0009-2614(98)00491-6>`__ **290**, 143 (1998),
M. Schütz, G. Hetzer, and H.-J. Werner, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.479957>`__ **111**, 5691 (1999),
G. Hetzer, M. Schütz, H. Stoll, and H.-J. Werner, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.1321295>`__ **113**, 9443 (2000),
as well as LMP2 gradients as described in
A. El Azhary, G. Rauhut, P. Pulay, and H.-J. Werner, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.475955>`__ **108**, 5185 (1998)
are now available without special license. The linear scaling LCCSD(T) methods as described in
M. Schütz and H.-J. Werner, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.1330207>`__ **114**, 661 (2001),
M. Schütz and H.-J. Werner, `Chem. Phys. Lett. <https://dx.doi.org/10.1016/S0009-2614(00)00066-X>`__ **318**, 370 (2000),
M. Schütz, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.1323265>`__ **113**, 9986 (2000)
will be made available at a later stage.

- QCISD gradients as described in `Phys. Chem. Chem. Phys. <https://dx.doi.org/10.1039/B105126C>`__ **3**, 4853 (2001) are now available.
- Additional and more flexible options for computing numerical gradients and performing geometry optimizations.
- A large number of additional density functionals have been added, together with support for the automated functional implementer described in Comp. Phys. Commun. **136** 310–318 (2001).
- Multipole moments of arbitrary order can be computed.
- Further modules have been parallelized, in particular the CCSD(T) and direct LMP2 codes. The parallel running procedures have been improved. The parallel version is available as an optional module.
- The basis set library has been extended.
- Some subtle changes in the basis set input: it is not possible any more that several one-line basis input cards with definitions for individual atoms follow each other. Each new basis card supercedes previous ones. Either all specifications must be given on *one* ``BASIS`` card, or a basis input block must be used. ``BASIS,NAME`` is now entirely equivalent to ``BASIS=NAME``, i.e. a global default basis set is defined and the variable ``BASIS`` is set in both cases.
- Pseudopotential energy calculations can now be performed with up to :math:`i`-functions, gradients with up to :math:`h`-functions.
- Many internal changes have been made to make Molpro more modular and stable. Support has been added for recent operating systems on Compaq, HP, SGI, SUN, and Linux. The patching system has been improved.

.. _recent_changes--features-that-were-new-in-molpro2000:

Features that were new in MOLPRO2000
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Relative to version 98.1, there are the following principal changes and additions:

- There was a fundamental error in the derivation of the spin-restricted open-shell coupled-cluster equations in J. Chem. Phys. 99, 5129 (1993) that is also reflected in the RCCSD code in ``Molpro`` version 98.1 and earlier. This error has now been corrected, and an erratum has been published in `J. Chem. Phys. <https://dx.doi.org/10.1063/1.480886>`__ **112**, 3106 (2000). Fortunately, the numerical implications of the error were small, and it is not anticipated that any computed properties will have been significantly in error.
- There was a programming error in the transformation of gradients from Cartesian to internal coordinates, which in some cases resulted in slow convergence of geometry optimizations. The error is now fixed.
- Vibrational frequencies formerly by default used average atomic masses, rather than those of the most common isotopes, which is now the default behaviour.
- MCSCF second derivatives (author Riccardo Tarroni) added (preliminary version, only without symmetry). Frequency and geometry optimization programs are modified so that they can use the analytic Hessian.
- New internally contracted multi-reference second-order perturbation theory code (author Paolo Celani) through command ``RS2C``, as described in P. Celani and H.-J. Werner, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.481132>`__ **112**, 5546 (2000).
- EOM-CCSD for excited states (author Tatiana Korona).
- QCISD dipole moments as true analytical energy derivatives (author Guntram Rauhut).
- Linear scaling (CPU and memory) LMP2 as described by G. Hetzer, P. Pulay, and H.-J. Werner, `Chem. Phys. Lett. <https://dx.doi.org/10.1016/S0009-2614(98)00491-6>`__ **290**, 143 (1998).

M. Schütz, G. Hetzer, and H.-J. Werner, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.479957>`__ **111**, 5691 (1999).

- Improved handling of basis and geometry records. 98.1 and 99.1 dump files can be restarted, but in case of problems with restarting old files, add ``RESTART,NOGEOM`` immediately after the ``file`` card. Also, if there are unjustified messages coming up in very large cases about "ORBITALS CORRESPOND TO DIFFERENT GEOMETRY" try ``ORBITAL``,\ *record*,\ ``NOCHECK``. (This can happen for cases with more than 100 atoms, since the old version was limited to 100).
- Reorganization and generalization of basis input. Increased basis library.
- Counterpoise geometry optimizations.
- Improved running procedures for MPP machines. Parallel direct scf and scf gradients are working. These features are only available with the MPP module, which is not yet being distributed.
- Important bugfixes for DFT grids, CCSD with paging, finite field calculations without core orbitals, spin-orbit coupling.
- Many other internal changes.

As an additional service to the ``Molpro`` community, an electronic mailing list has been set up to provide a forum for open discussion on all aspects of installing and using ``Molpro``. The mailing list is intended as the primary means of disseminating hints and tips on how to use Molpro effectively. It is not a means of raising queries directly with the authors of the program. For clearly demonstrable program errors, reports should continue to be sent to <molpro@molpro.net>; however, ‘how-to’ questions sent there will merely be redirected to this mailing list.

In order to subscribe to the list, send mail to <molpro-user-request@molpro.net> containing the text ``subscribe``; for help, send mail containing the text ``help``.

Messages can be sent to the list (<molpro-user@molpro.net>), but this can be done only by subscribers. Previous postings can be viewed in the archive at https://www.molpro.net/molpro-user/archive irrespective of whether or not you subscribe to the list. Experienced Molpro users are encouraged to post responses to queries raised. Please do contribute to make this resource mutually useful.

.. _recent_changes--facilities-that-were-new-in-molpro98:

Facilities that were new in MOLPRO98
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``Molpro98`` has the full functionality of ``Molpro96``, but in order to make the code more modular and easier to use and maintain, a number of structural changes have been made. In particular, the number of different records has been significantly reduced. The information for a given wavefunction type, like orbitals, density matrices, fock matrices, occupation numbers and other information, is now stored in a single dump record. Even different orbital types, e.g., canonical, natural, or localized orbitals, are stored in the same record, and the user can subsequently access individual sets by keywords on the ``ORBITAL`` directive. New facilities allow the use of starting orbitals computed with different basis sets and/or different symmetries for SCF or MCSCF calculations. The default starting guess for SCF calculations has been much improved, which is most useful in calculations for large molecules. The use of special procedures for computing non-adiabatic couplings or diabatization of orbitals has been significantly simplified. We hope that these changes make the program easier to use and reduce the probability of input errors. However, in order to use the new facilities efficiently, even experienced Molpro users should read the sections *RECORDS* and *SELECTING ORBITALS AND DENSITY MATRICES* in the manual. It is likely that standard ``Molpro96`` inputs still work, but changes may be required in more special cases involving particular records for orbitals, density matrices, or operators.

All one-electron operators needed to compute expectation values and transition quantities are now stored in a single record. Operators for which expectation values are requested can be selected globally for all programs of a given run using the global ``GEXPEC`` directive, or for a specific program using the ``EXPEC`` directive. All operators are computed automatically when needed, and the user does not have to give input for this any more. See section *ONE-ELECTRON OPERATORS AND EXPECTATION VALUES* of the manual for details.

Due to the changed structure of dump and operator records, the utility program ``MATROP`` has a new input syntax. ``Molpro96`` inputs for ``MATROP`` do not work any more.

In addition to these organizational changes, a number of new programs have been added. Analytic energy gradients can now be evaluated for MP2 and DFT wavefunctions, and harmonic vibrational frequencies, intensities, and thermodynamic quantities can be computed automatically using finite differences of analytical gradients. Geometry optimization has been further improved, and new facilities for reaction path following have been added.

An interface to the graphics program MOLDEN has been added, which allows to visualize molecular structures, orbitals, electron densities, or vibrations.

Integral-direct calculations, in which the two-electron integrals in the AO basis are never stored on disk but always recomputed when needed, are now available for all kinds of wavefunctions, with the exception of perturbative triple excitations in MP4 and CCSD(T) calculations. This allows the use of significantly larger basis sets than was possible before. The direct option can be selected globally using the ``GDIRECT`` command, or for a specific program using the ``DIRECT`` directive. See section *INTEGRAL DIRECT METHODS* in the manual for details. Note that the ``DIRECT`` module is optional and not part of the basic ``Molpro`` distribution.

*Local* electron correlation methods have been further improved. In combination with the integral-direct modules, which implement efficient prescreening techniques, the scaling of the computational cost with molecular size is dramatically reduced, approaching now quadratic or even linear scaling for MP2 and higher correlation methods. This makes possible to perform correlated calculations for much larger molecules than were previously feasible. However, since these methods are subject of active current research and still under intense development, we decided not to include them in the current ``Molpro`` release. They will be optionally available in one of the next releases.
