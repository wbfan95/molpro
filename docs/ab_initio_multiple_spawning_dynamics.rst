.. raw:: html

   <span id="control-dat"></span>

.. raw:: html

   <span id="examples"></span>

.. raw:: html

   <span id="frequencies-dat"></span>

.. raw:: html

   <span id="frequenciesmp-dat"></span>

.. raw:: html

   <span id="geometry-dat"></span>

.. raw:: html

   <span id="hessian-dat"></span>

.. _ab_initio_multiple_spawning_dynamics--ab-initio-multiple-spawning-dynamics-aims:

Ab initio multiple spawning dynamics (AIMS)
===========================================

*AIMS* is a multi-state first-principles dynamics program written by
Benjamin G. Levine, Joshua D. Coe, Aaron M. Virshup, Hongli Tao, Christian R. Evenhuis, William J. Glover, Toshifumi Mori, Michal Ben-Nun and Todd J. Martinez.

Bibliography:

B. G. Levine, J. D. Coe, A. M. Virshup and T. J. Martinez, Chem. Phys. 347, 3 (2008).
M. Ben-Nun and T. J. Martinez, `Chem. Phys. Lett. <https://dx.doi.org/10.1016/S0009-2614(98)01115-4>`__ **298**, 57 (1998).

All publications resulting from use of this program must acknowledge the above. See also:

B. G. Levine and T. J. Martinez, J. Phys. Chem. A 113, 12815 (2009).
T. J. Martinez, Acc. Chem. Res. 39, 119 (2006).

The AIMS module implements the Ab Initio Multiple Spawning method to perform dynamics calculations on multiple electronic states. Although the program was designed for non-adiabatic dynamics with CASSCF wavefunctions, it can be used quite generally for first principles molecular dynamics, provided that nuclear gradients are available.

AIMS provides a description of a time-evolving molecular wavepacket with a multi-configurational, product gaussian function basis. To allow the size of the basis set to remain small while describing the wavepacket dynamics, the centers of the full-dimensional gaussian functions follow classical trajectories while their widths are kept fixed (the frozen Gaussian approximation). When these classical trajectories encounter regions of large non-adiabatic coupling to another electronic state, new basis functions are *spawned* on the coupled state and the Time Dependent Schrödinger Equation is solved in order to describe population transfer between the electronic states. In this way, the description of the wavepacket can be systematically improved by increasing the number of initial trajectory basis functions, while reducing the coupling threshold at which trajectories spawned. Alternatively, spawning can be disabled, and the method will reduce to traditional first-principles classical molecular dynamics when a single trajectory basis function is used.

.. _ab_initio_multiple_spawning_dynamics--compilation:

Compilation
===========

AIMS is compiled as a component of Molpro; however, it requires a fortran 2003 compiler and is disabled unless the preprocessor variable MOLPRO_f2003 is defined, which depends on the version of your compiler.

.. _ab_initio_multiple_spawning_dynamics--structure-of-the-input:

Structure of the input
======================

The AIMS program is controlled by the Molpro input deck and a number of external text files:

.. _ab_initio_multiple_spawning_dynamics--molpro-input-deck:

Molpro input deck
=================

The AIMS program is invoked by the command AIMS. The details of the electronic structure are defined in specifically named procedures. At a minimum, for first principles dynamics, AIMS requires the following structure to the input deck:

``SYMMETRY, nosym\\``
``ORIENT, noorient\\``
``GEOMTYP=xyz\\``
``GEOMETRY={ Initial atom specifications. Must match ordering of Geometry.dat, but need not be the same geometry }``

``BASIS={Basis specifications.}``

``MPINIT={ Electronic structure routines for initial wavefunction }``

``MPCALC={ Electronic structure routines for dynamics calculations. At a minimum, must include: ener(1)=energy(1) ener(2)=energy(2)etc force }``

``AIMS,dir``

where

* ``dir`` (string) Relative directory to AIMS input files. (Default is working directory).

Note: the above is appropriate only for first-principles dynamics (without spawning). CASSCF spawning calculations require additional procedures and a specific structure to the MPINIT and MPCALC procedures. See the examples in section `examples <ab_initio_multiple_spawning_dynamics.html#examples>`__.

.. _ab_initio_multiple_spawning_dynamics--control-dat:

Control.dat
===========

Control.dat is a fortran NAMELIST file storing the main parameters (in au) of an AIMS simulation. At the end of the file, one can optionally specify user-defined atom types (see below). Also time steps are in au, 1 au = 0.0241888 femtoseconds.

.. list-table::
   :header-rows: 2

   * - Initialization
     - 
     - 
   * - Parameter
     - Options (Default)
     - Description
   * - Required parameters:
     - 
     - 
   * - ``NumStates``
     - ``Integer``
     - Number of electronic states.
   * - ``InitState``
     - ``Integer``
     - Initial electronic state.
   * - ``NumParticles``
     - ``Integer``
     - Number of atoms.
   * - Common parameters:
     - 
     - 
   * - ``IMethod``
     - ``0``
     - First principles dynamics (No NACV).
   * - 
     - ``(1)``
     - CASSCF dynamics, with NACV.
   * - ``IRestart``
     - ``(0)/1``
     - Restart the calculation when set to 1.
   * - ``RestartTime``
     - ``Real (-100.0)``
     - Time from which to restart in Checkpoint.txt. If disabled, use Last_Bundle.txt.
   * - ``IRndSeed``
     - ``Integer (0)``
     - Initial condition random number seed.
   * - ``InitialCond``
     - ``('NoSample')``
     - Read initial conditions from Geometry.dat.
   * - 
     - ``'Wigner'``
     - Sample from the Wigner distribution of harmonic normal modes in Frequencies.dat.
   * - 
     - ``'Quasiclassical'``
     - As above, for the Quasiclassical distribution.
   * - 
     - ``'Boltzmann'``
     - As above, for the Boltzmann distribution.
   * - ``Temperature``
     - ``Real (0.0)``
     - Temperature (Kelvin) of the initial conditions.
   * - Expert parameters:
     - 
     - 
   * - ``InitBright``
     - ``Logical (.false.)``
     - Select optically brightest of ``InitState`` and ``IDark`` as initial state.
   * - ``InitDark``
     - ``Logical (.false.)``
     - As above, but for darkest state.
   * - ``IDark``
     - ``Integer (-1)``
     - See above.
   * - ``InitGap``
     - ``Real (0.0)``
     - Select initial ground-excited energy gap to within :math:`\pm 0.5\times`\ ``InitGapWidth``.
   * - ``InitGapWidth``
     - ``Real (0.0)``
     - See above.
   * - ``IRestartTraj``
     - ``Integer array (0)``
     - Subset of trajectories to restart from. Can restart a single dead trajectory.
   * - ``NumInitBasis``
     - ``Integer (1)``
     - Number of initial coupled basis functions.
   * - ``FirstGauss``
     - ``Logical (.false.)``
     - Place the first basis function at the molecular origin (that of Geometry.dat), with zero momentum.
   * - ``MirrorBasis``
     - ``Logical (.false.)``
     - Mirror the initial basis on another electronic state, ``MirrorState``.
   * - ``MirrorState``
     - ``Integer (1)``
     - See above.
   * - ``EnergyAdjust``
     - ``Logical (.false.)``
     - Adjust momenta of mirrored basis (along NACV) to match original basis energy.
   * - ``SharpEnergy``
     - ``Logical (.false.)``
     - Adjust momenta of all initial basis functions to match first basis function energy.

.. list-table::
   :header-rows: 2

   * - Integration and numerics
     - 
     - 
   * - Parameter
     - Options (Default)
     - Description
   * - Required parameters:
     - 
     - 
   * - ``TimeStep``
     - ``Real``
     - Simulation timestep.
   * - ``SimulationTime``
     - ``Real``
     - Simulation length.
   * - Common parameters:
     - 
     - 
   * - ``ExShift``
     - ``Real (0.0)``
     - Apply a shift of ``+ExShift`` to diagonals of Hamiltonian to improve amplitude/phase propagation. Good choice is average potential energy of ground and excited states.
   * - ``CoupTimeStep``
     - ``Real (TimeStep/4)``
     - Timestep to use in regions of large nonadiabatic coupling.
   * - Expert parameters:
     - 
     - 
   * - ``TimeStepRejection``
     - ``Logical (.true.)``
     - Enables adaptive time-stepping when encountering integration problems.
   * - ``MinTimeStep``
     - ``Real (CoupTimeStep/4)``
     - Minimum timestep to use when adaptive time-stepping.
   * - ``DieOnMinStep``
     - ``Logical (.true.)``
     - Stop calculation if minimum timestep is reached.
   * - ``EnergyStepCons``
     - ``Real (0.005)``
     - Allowed violation of classical energy conservation before timestep is rejected.
   * - ``NormCons``
     - ``Real (0.25)``
     - Permitted deviation in Norm from beginning of simulation.
   * - ``RejectAllStateFlip``
     - ``Logical (.true.)``
     - Reject a timestep if any two electronic states flip. If ``.false.`` then only reject if state is coupled to occupied state.
   * - ``OlapThresh``
     - ``Real (0.001)``
     - Threshold overlap between two trajectories below which matrix elements not calculated.
   * - ``RegThresh``
     - ``Real (0.0001)``
     - Threshold to regularize the overlap matrix before inversion.
   * - ``Constrain``
     - ``Logical (.false.)``
     - Apply geometric constraints? If yes, supply Constraints.dat

.. list-table::
   :header-rows: 2

   * - Spawning
     - 
     - 
   * - Parameter
     - Options (Default)
     - Description
   * - Common parameters:
     - 
     - 
   * - ``CSThresh``
     - ``Real (0.1)``
     - Threshold Coupling, above which to spawn.
   * - ``PopToSpawn``
     - ``Real (0.1)``
     - Minimum population a trajectory must have before it can spawn.
   * - ``OMax``
     - ``Real (0.8)``
     - Prevent spawning if overlap of spawned trajectory with existing basis greater than ``Omax``.
   * - ``MaxTraj``
     - ``Real (100)``
     - Maximum number of allowed trajectories. Above which, spawning is disabled.
   * - ``IgnoreState``
     - ``Integer (0)``
     - Stop dynamics of trajectories on ``IgnoreState``. if not coupled for at least ``DecoherenceTime``. Choose 1 if only interested in excited states.
   * - ``MaxEDiff``
     - ``Real (0.03)``
     - Energy gap threshold for calculating nonadiabatic couplings, above which, coupling taken to be zero.
   * - Expert parameters:
     - 
     - 
   * - ``DecoherenceTime``
     - ``Real (200.0)``
     - See above.
   * - ``SpawnCoupV``
     - ``Logical (.false.)``
     - Use Coup.velocity as criterion for spawning rather than Coupling magnitude alone.
   * - ``EShellOnly``
     - ``Logical (.true.)``
     - Require spawned trajectories to have same classical energy as parent by adjusting momentum along NACV.

.. list-table::
   :header-rows: 2

   * - Output
     - 
     - 
   * - Parameter
     - Options (Default)
     - Description
   * - Common parameters:
     - 
     - 
   * - ``zAllText``
     - ``Logical (.false.)``
     - Write all output files?
   * - ``zEDatFile``
     - ``Logical (.true.)``
     - Write Energy file?
   * - ``zNDatFile``
     - ``Logical (.true.)``
     - Write Population file?
   * - ``zTrajFile``
     - ``Logical (.false.)``
     - Write Trajectory files?
   * - ``zAmpFile``
     - ``Logical (.false.)``
     - Write Amplitude files?
   * - ``zPotEnFile``
     - ``Logical (.false.)``
     - Write Potential Energy files?
   * - ``zXYZ``
     - ``Logical (.false.)``
     - Write XYZ Geometry files?
   * - ``zCoupFile``
     - ``Logical (.false.)``
     - Write Coupling files?
   * - ``zChargeFile``
     - ``Logical (.false.)``
     - Write Charge files?
   * - ``zDipoleFile``
     - ``Logical (.false.)``
     - Write Dipole files?
   * - ``zTDipoleFile``
     - ``Logical (.false.)``
     - Write Transition Dipole files?
   * - ``zQMRRFile``
     - ``Logical (.false.)``
     - Write :math:`\langle r^2 \rangle` quadrupole moment files?
   * - ``zCIVecFile``
     - ``Logical (.false.)``
     - Write CI Vector files? (Not recommended for large CI)
   * - ``zCorrfile``
     - ``Logical (.false.)``
     - Write Correlation function file?
   * - ``zBundMatFile``
     - ``Logical (.false.)``
     - Write Matrices (H, S, etc)?
   * - ``WriteMolden``
     - ``Logical (.false.)``
     - Write Molden files?
   * - ``MoldenStep``
     - ``Integer (200)``
     - How often (every number of timesteps) Molden files are written.
   * - ``RestartStep``
     - ``Integer (4)``
     - How often (every number of timesteps) Restart files are written.
   * - Expert parameters:
     - 
     - 
   * - ``NStepToPrint``
     - ``Integer (1)``
     - How often (every number of timesteps) output files are written.
   * - ``WriteEveryStep``
     - ``Logical (.true.)``
     - Write output every timestep, including subtimesteps of adaptive propagation. Overrides ``NStepToPrint``.
   * - ``NBonds``
     - ``Integer (0)``
     - Number of bond lengths to print. Define IBond below.
   * - ``IBond(2,NBonds)``
     - ``Integer (0)``
     - List of atom indices that are bonded. See NBonds above.
   * - ``NAngles``
     - ``Integer (0)``
     - Number of bond angles to print. Define IAngle below.
   * - ``IAngle(3,NAngles)``
     - ``Integer (0)``
     - List of atom indices that define bond angles.
   * - ``NDihedrals``
     - ``Integer (0)``
     - Number of dihedral angles to print. Define IDihedral below.
   * - ``IDihedral(4,NDihedrals)``
     - ``Integer (0)``
     - List of atom indices that define dihedral angles.
   * - ``NPyrams``
     - ``Integer (0)``
     - Number of pyramidalization angles to print. Define IPyram below.
   * - ``IPyram(4,NPyrams)``
     - ``Integer (0)``
     - List of atom indices that define pyramidalization angles.

**User-defined atom types**

AIMS recognizes the atoms H, C, N, O, S, F, Cl and assigns appropriate masses and gaussian width parameters for these atoms. If you wish to modify these defaults, or if your system contains other atoms, you can define custom atom types at the end of Control.dat. The format is (in atomic units):

``n\\``
``AtomName(1) AtomicNumber(1) AtomicMass(1) GaussianWidth(1)\\``
:math:`\vdots`
``AtomName(n) AtomicNumber(n) AtomicMass(n) GaussianWidth(n)``

.. _ab_initio_multiple_spawning_dynamics--geometry-dat:

Geometry.dat
============

Geometry.dat contains the molecular geometry that will be used in the generation of initial conditions. Optionally, the momenta can also be specified, which is useful if
``InitialCond='NoSample':``

``UNITS=ANG or UNITS=BOHR \\``
``natom\\``
``AtomName(1)     x(1)      y(1)      z(1)\\``
:math:`\vdots`
``AtomName(natom) x(natom)  y(natom)  z(natom)\\``
``Momenta:\\``
``AtomName(1)     px(1)     py(1)     pz(1)\\``
:math:`\vdots`
``AtomName(natom) px(natom) py(natom) pz(natom)``

.. _ab_initio_multiple_spawning_dynamics--frequenciesmp-dat:

FrequenciesMP.dat
=================

FrequenciesMP.dat contains the normal-mode frequencies and displacements of the molecule in its initial geometry and electronic state (usually the ground state). This information is used in the generation of initial conditions. If ``InitialCond``\ :math:`\neq`\ ``'NoSample'`` then either this file, Hessian.dat or Frequencies.dat (Sections `Hessian.dat <ab_initio_multiple_spawning_dynamics.html#hessian-dat>`__ and `Frequencies.dat <ab_initio_multiple_spawning_dynamics.html#frequencies-dat>`__ respectively) must be present. The format of FrequenciesMP.dat follows the Molpro output of a Frequencies calculation (note: in the first line, the number of normal modes has to be given; the rest is as in the Molpro output):

.. code-block:: text
   :caption: FrequenciesMP.dat

   6
                                 1 A         2 A         3 A         4 A         5 A
    Wavenumbers [cm-1]         1116.71     1725.49     1728.47     3435.76     3566.01
    Intensities [km/mol]        157.34       17.93       16.24        1.67        0.53
    Intensities [relative]      100.00       11.40       10.32        1.06        0.33
              GX1             -0.10597    -0.00088    -0.00021    -0.03801    -0.00009
              GY1              0.00067    -0.05838    -0.02628    -0.00017    -0.07554
              GZ1              0.00004     0.02639    -0.05807     0.00078     0.00226
              GX2              0.49134    -0.14946     0.19728     0.17300    -0.07729
              GY2              0.03972     0.54519     0.46553    -0.12339     0.02439
              GZ2             -0.19161     0.21763    -0.00782     0.51879    -0.19043
              GX3              0.49290    -0.09010    -0.22955     0.17771    -0.20720
              GY3              0.13665     0.43154    -0.28739    -0.39612     0.35792
              GZ3              0.13722    -0.52910     0.11024    -0.37702     0.36169
              GX4              0.48838     0.25184     0.03520     0.17755     0.28570
              GY4             -0.18573    -0.16545     0.18702     0.52182     0.66736
              GZ4              0.05376    -0.05521     0.70450    -0.15258    -0.20268
   
                                 6 A
    Wavenumbers [cm-1]         3570.66
    Intensities [km/mol]          0.61
    Intensities [relative]        0.39
              GX1             -0.00060
              GY1             -0.00245
              GZ1             -0.07574
              GX2              0.28798
              GY2             -0.16745
              GZ2              0.68133
              GX3             -0.20790
              GY3              0.37733
              GZ3              0.33817
              GX4             -0.07175
              GY4             -0.17584
              GZ4              0.03308

Note: Only the real, non-zero frequencies should be included in this file (i.e. those corresponding to vibrations). The first line of the file must be the number of frequencies. See section :doc:`harmonic vibrational frequencies (FREQUENCIES) <harmonic_vibrational_frequencies_frequencies>` for details on how to perform a normal-mode frequencies calculation in Molpro.

.. _ab_initio_multiple_spawning_dynamics--hessian-dat:

Hessian.dat
===========

As an alternative to FrequenciesMP.dat, AIMS can generate the normal mode frequencies after reading in the Hessian from Hessian.dat. The format of this file is:

``natom\\``
``Hess(1,1) Hess(2,1) ... Hess(3*natom,3*natom)``

Note: the Hessian should not be mass weighted. It is permissible to have carriage returns in the list of Hessian components.

.. _ab_initio_multiple_spawning_dynamics--frequencies-dat:

Frequencies.dat
===============

As an alternative to FrequenciesMP.dat and Hessian.dat, AIMS can read in normal-mode frequencies and vectors in AIMS format in Frequencies.dat. The format of this file is:

``natom   nmodes\\``
``freq(1) freq(2) ... freq(nmodes)\\``
``modevec(1,1) modevec(2,1) ... modevec(3*natom,nmodes)``

Note: Frequencies must be in cm\ :math:`^{-1}`, but normal mode vectors can be mass scaled or not- AIMS will detect. Also, it is permissible to have carriage returns in the list of frequencies and mode vectors. This file is generated by AIMS if either FrequenciesMP.dat or Hessian.dat is used initially.

.. _ab_initio_multiple_spawning_dynamics--constraints-dat:

Constraints.dat
===============

If ``Constraint=.true.`` then Constraints.dat must be supplied. This is a fortran NAMELIST file that defines the geometric constraints in the system. These constraints are enforced with the RATTLE algorithm. The parameters contained in this file are:

.. list-table::
   :header-rows: 2

   * - Constraint parameters
     - 
     - 
   * - Parameter
     - Options (Default)
     - Description
   * - ``NumBonds``
     - ``Integer (0)``
     - Number of bond lengths to constrain. Define IBondPtcles below.
   * - ``IBondPtcles(2,NumBonds)``
     - ``Integer (0)``
     - List of atom indices that are bonded. See NumBonds above.
   * - ``NumAngles``
     - ``Integer (0)``
     - Number of bond angles to constrain. Define IAnglePtcles below.
   * - ``IAnglePtcles(3,NumAngles)``
     - ``Integer (0)``
     - List of atom indices that define bond angles.
   * - ``NComAtoms``
     - ``Integer (0)``
     - Number of atoms that define the center-of-mass constraint. Define ICOMPtcles below.
   * - ``ICOMPtcles(NComAtoms)``
     - ``Integer (0)``
     - List of atom indices that define the center of mass.
   * - ``Toler``
     - ``Real (1E-4)``
     - Rattle tolerance
   * - ``MaxIts``
     - ``Integer (10000)``
     - Maximum number of Rattle iterations

Note, a maximum of 1000 constraints is allowed.

.. _ab_initio_multiple_spawning_dynamics--running-a-casscf-spawning-calculation:

Running a CASSCF spawning calculation
-------------------------------------

This section gives an overview of how to set up and run a CASSCF ab initio multiple spawning calculation.

1) The first step is to create a molpro input deck that controls how the CASSCF electronic structure calculations are performed. AIMS requires a fairly complicated structure to the molpro deck and it is highly recommended that you use the ethylene CASSCF example as a starting point (section `examples <ab_initio_multiple_spawning_dynamics.html#examples>`__). Control.dat should then be modified for your system and desired simulation parameters (section `Control.dat <ab_initio_multiple_spawning_dynamics.html#control-dat>`__).

2) Next, the initial conditions should be defined. This involves providing an initial geometry in Geometry.dat (section `Geometry.dat <ab_initio_multiple_spawning_dynamics.html#geometry-dat>`__) and normal-mode frequencies and displacements in FrequenciesMP.dat (section `FrequenciesMP.dat <ab_initio_multiple_spawning_dynamics.html#frequenciesmp-dat>`__), which will be used to generate a phase-space distribution that the initial conditions sample. Alternatively, one can also provide momenta in Geometry.dat and set ``InitialCond='NoSample'`` in Control.dat, and directly specify the initial conditions.

3) The AIMS calculation is then initiated by running molpro on the input deck, in the usual fashion. In order to sample different initial conditions, multiple AIMS simulations should be run with different values of the random number seed ``IRndSeed`` (or different Geometry.dat files) - each of these should be run in a unique directory.

.. _ab_initio_multiple_spawning_dynamics--output:

Output
------

Beyond the regular molpro output, which contains the electronic structure output, AIMS writes to a number of text files, depending on the output parameters in Control.dat (section `Control.dat <ab_initio_multiple_spawning_dynamics.html#control-dat>`__). All values are given in atomic units unless otherwise specified. Electronic properties of a trajectory are evaluated at the center geometry of the trajectory basis function.

* **FMS.out** Current progress of simulation and any warning/error messages.
* **E.dat** Wavepacket energies. QM energies are expectation values of the quantum operators, including coherences between the trajectory basis functions. CL energies are averages of the trajectories’ classical energies, weighted by the amplitude norm of each trajectory.
* **N.dat** Electronic populations, the sum of which should be conserved.
* **TrajDump.i** Dynamic variables for trajectory i.
* **Amp.i** Amplitudes of trajectory i. Note: since the product Gaussian basis is non-orthogonal, the amplitude norms do not necessarily sum to 1.
* **PotEn.i** Electronic energies for trajectory i. The last column displays the total classical energy of the trajectory, which should be conserved.
* **positions.i.xyz** Snapshots of trajectory i’s center geometry in XYZ format (Angstrom).
* **Coup.i** Nonadiabatic couplings of each state to the occupied state for trajectory i. The first nstate columns contain the magnitude of coupling vectors and the last nstate columns contain the projection of the coupling onto the velocity vector.
* **Charge.i** Partial atomic charges corresponding to the occupied electronic state of trajectory i. The molpro input deck must contain a Mulliken population analysis directive in the ``MPCALC`` procedure.
* **Dipole.i** Dipole moments of each electronic state for trajectory i.
* **TDip.i** Transition dipoles from ground to excited states for trajectory i.
* **QMRR.i** Isotropic quadrupole moment :math:`\langle r^2 \rangle` of each electronic state for trajectory i. The molpro input deck must contain ``EXPEC,QMRR``.
* **CIVec.i** CI Vectors for each state of trajectory i.
* **CFxn.dat** The overlap correlation function :math:`\langle \Psi(t) | \Psi(0) \rangle`.
* **H.dat** Hamiltonian matrix.
* **S.dat** Overlap matrix. Note: the overlap between trajectories on different states is zero, but is displayed here as if they were on the same state.
* **SDot.dat** The time derivative of the Overlap matrix.
* **i.j.molf** Molden file for trajectory i at time j.
* **Checkpoint.txt** Restart file with history.
* **Last_Bundle.txt** Restart file for the last written timestep.
* **Spawn.log** Details of successful spawns.
* **FailSpawn.log** Details of unsuccessful spawns.
* **Spawn.i** XYZ file of geometry where trajectory i was spawned.

.. _ab_initio_multiple_spawning_dynamics--examples:

Examples
--------

The following two examples show how AIMS can be run in either single-state first-principle molecular dynamics mode, or multi-state spawning mode. The parameters found in these input files were chosen for illustrative purposes and are not necessarily appropriate for your system of interest. It is recommended the literature be consulted before performing AIMS simulations.

Ethylene Hartree-Fock First-Principles Molecular Dynamics

See examples/aims_ethyl_HF

.. code-block:: text
   :caption: examples/aims_ethyl_HF.inp

   ! FMS-Molpro does not support parallel execution.
   if(NPROC_MPP.gt.1) then
   skipped
   endif
   if(.not.modul_aims) then
   skipped
   endif
   
   SYMMETRY,nosym
   ORIENT,noorient
   GEOMTYP=xyz
   GEOMETRY={
   6
   ethylene ground-state geom
    C    0.0000000031    0.0000000000    0.6768496105
    C   -0.0000000013    0.0000000000   -0.6768496105
    H   -0.0000000017    0.9131426983   -1.2402810929
    H   -0.0000000095    0.9131426983    1.2402810929
    H   -0.0000000159   -0.9131426983    1.2402810929
    H    0.0000000047   -0.9131426983   -1.2402810929
   }
   BASIS=6-31g**
   
   MPINIT={
   hf
   }
   
   MPCALC={
    ! Calculate Energy and Forces
    show,itimestep,itrj;
    hf
    ener( 1 )=energy( 1 )
    if(status.lt.0) then
       text,ERROR: could not converge SCF.
       STOP
    endif
    pop;density
    force
   }
   
   aims,dir='./aims_ethyl_HF'

.. code-block:: text
   :caption: examples/aims_ethyl_HF/Control.dat

    &control
   
   !------ Initialization -------!
    InitState=1
    iRndSeed=1
   
   !------ Simulation Properties -------!
    IMethod=0              !Single- state dynamics - no couplings.
    NumParticles=6         !Number of atoms
    NumStates=1            !number of electronic states
   
   !-------- Integration and numerics --------!
    TimeStep=20.0          !timestep for integration
    SimulationTime=2000.0  !integration time
    MinTimeStep=1.0        !minimum adaptive timestep
   !------- Ouput options ---------!
   zAllText=.false.
   zEDatFile=.true.       !Energy file
   zNDatFile=.false.       !Population file
   zTrajFile=.true.      !Trajectory data file
   zAmpFile=.false.        !Amplitude files
   zPotEnFile=.true.      !Potential energy files
   zXYZ=.true.            !XYZ files
   zCoupFile=.false.       !Coupling files
   zChargeFile=.false.     !Charge files
   zDipoleFile=.false.     !Dipole files
   zTDipoleFile=.false.    !Transition dipole files
   
   
   / !using default atom types, so user-defined types are not necessary
    

.. code-block:: text
   :caption: examples/aims_ethyl_HF/Geometry.dat

      UNITS=BOHR
           6
   C  0.000000  0.000000  1.279060
   C  0.000000  0.000000 -1.279060
   H  0.000000  1.725590 -2.343792
   H  0.000000  1.725590  2.343792
   H  0.000000 -1.725590  2.343792
   H  0.000000 -1.725590 -2.343792
   #Momenta
      0.000     0.000     0.000
      0.000     0.000     0.000
      0.000     0.000     0.000
      0.000     0.000     0.000
      0.000     0.000     0.000
      0.000     0.000     0.000

Ethylene CASSCF Spawning Dynamics

See examples/aims_ethyl_CASSCF

.. code-block:: text
   :caption: examples/aims_ethyl_CASSCF.inp

   !Ethylene (2/2)-CASSCF AIMS deck.
   !This can be used as a template for other simulations by changing
   !User options below. The deck calculates couplings for up to three
   !states simultaneously coupled to the occupied state (NUMCOUP=3.0),
   !which should suffice for most applications. If this needs to be increased,
   !modify MPCALC accordingly.
   
   !User options
   symmetry,nosym  !Do not change!
   occ,9,context=MCSCF
   closed,7,context=MCSCF
   wf,16,1,0
   nstate=3
   orient,noorient !Do not change!
   geomtyp=xyz     !Do not change!
   geometry={
   6
   ethylene ground-state geom
    C    0.0000000031    0.0000000000    0.6768496105
    C   -0.0000000013    0.0000000000   -0.6768496105
    H   -0.0000000017    0.9131426983   -1.2402810929
    H   -0.0000000095    0.9131426983    1.2402810929
    H   -0.0000000159   -0.9131426983    1.2402810929
    H    0.0000000047   -0.9131426983   -1.2402810929
   }
   basis=6-31g*
   
   
   !Aims variables - do not change!
   ! FMS-Molpro does not support parallel execution.
   if(NPROC_MPP.gt.1) then
   skipped
   endif
   if(.not.modul_aims) then
   skipped
   endif
   
   ! tighten thresholds:
   gthresh,twoint=1.0d-13
   gthresh,energy=1.0d-7,gradient=1.0d-2
   ! records used by AIMS
   orbrec=2101.2
   cirec=2501.2
   diabrec=3000.2
   gradrec0=5101.1
   do icoup=1,nstate-1
     gradrec(icoup)=gradrec0+icoup
   enddo
   
   MPINIT={ !Find the initial CASSCF wavefunction
   if(orbital.eq.0) then
     hf
     multi
     pspace,10.0
     wf;state,nstate
     maxiter,20
     orbital,orbrec
     ciguess,cirec
     save,det=cirec
     if (status.lt.0) then
       text, MCSCF failed in MPINIT.
       text, Attempting uncoupled iterations.
       {multi,so
       pspace,10.0
       wf;state,nstate
       orbital,orbrec
       ciguess,cirec
       save,det=cirec
       maxiter,50}
     endif
     if(status.lt.0) then
       text,ERROR: could not converge MCSCF.
       text,FMS should now stop
       STOP
     endif
   endif
   }
   
   MPCALC={ !Calculate Energy and Forces
   if (jtrj.eq.0) then
     show,itimestep,itrj;
   else
     show,itimestep,itrj,jtraj
   endif
   data,truncate,diabrec
   data,truncate,gradrec0
   do icoup=1,nstate-1
     data,truncate,gradrec(icoup)
   enddo
   data,copy, orbrec, diabrec
   {multi
   pspace,10.0
   wf;state,nstate
   maxiter,20
   orbital,orbrec
   ciguess,cirec
   dm,orbrec
   save,det=cirec
   diab,diabrec,save=orbrec
   }
   if (status.lt.0) then
     text, MCSCF failed in MPCALC.
     text, Attempting uncoupled iterations.
     {multi
     pspace,10.0
     state,nstate
     orbital,orbrec
     ciguess,cirec
     dm,orbrec
     save,det=cirec
     {iterations
       do,uncouple,1,to,10}
     maxiter,30
     diab,diabrec,save=orbrec
     }
   endif
   if(status.lt.0) then
     text,ERROR: could not converge MCSCF.
     text,FMS should now stop
     STOP
   endif
   do istate=1,nstate
     ener( istate )=energy( istate )
   enddo
   pop;density,orbrec,state=stateind
   if (numcoup.eq.0.0) then
     {multi
     pspace,10.0
     wf;state,nstate
     maxiter,20
     orbital,orbrec
     ciguess,cirec
     save,det=cirec
     diab,diabrec,save=orbrec
     cpmcscf,grad,stateind,save=gradrec0;
     }
   elseif (numcoup.eq.1.0) then
     {multi
     pspace,10.0
     wf;state,nstate
     maxiter,20
     orbital,orbrec
     ciguess,cirec
     save,det=cirec
     diab,diabrec,save=orbrec
     cpmcscf,grad,stateind,save=gradrec0;
     cpmcscf,nacm,stateind,stateind2(1),save=gradrec(1);
     }
   elseif (numcoup.eq.2.0) then
     {multi
     pspace,10.0
     wf;state,nstate
     maxiter,20
     orbital,orbrec
     ciguess,cirec
     save,det=cirec
     diab,diabrec,save=orbrec
     cpmcscf,grad,stateind,save=gradrec0;
     cpmcscf,nacm,stateind,stateind2(1),save=gradrec(1);
     cpmcscf,nacm,stateind,stateind2(2),save=gradrec(2);
     }
   elseif (numcoup.eq.3.0) then
     {multi
     pspace,10.0
     wf;state,nstate
     maxiter,20
     orbital,orbrec
     ciguess,cirec
     save,det=cirec
     diab,diabrec,save=orbrec
     cpmcscf,grad,stateind,save=gradrec0;
     cpmcscf,nacm,stateind,stateind2(1),save=gradrec(1);
     cpmcscf,nacm,stateind,stateind2(2),save=gradrec(2);
     cpmcscf,nacm,stateind,stateind2(3),save=gradrec(3);
     }
   elseif (numcoup.ge.4.0) then
     text, Number of couplings requested: $numcoup beyond limits of input deck.
     text, Please modify input deck accordingly.
     STOP
   endif
   forces;samc,gradrec0
   }
   
   MGCOUP={
   forces;nacm,gradrec(ncoup)
   }
   
   ! writes a molden file
   WRITEMOLDEN={
   moldenfile='$itrj.$itimestep.molf'
   put,molden,$moldenfile;
   }
   
   AIMS,dir='./aims_ethyl_CASSCF'

.. code-block:: text
   :caption: examples/aims_ethyl_CASSCF/Control.dat

    &control
   
   !------ Initialization -------!
    NumStates=3            !Number of electronic states
    InitState=2            !Initial trajectory's state
    NumParticles=6         !Number of atoms
    IMethod=1              !CASSCF dynamics with couplings
    IRestart=0             !Do not restart
    IRndSeed=1             !Random number seed
    InitialCond='WIGNER'   !Sample from Wigner Distribution
   
   !-------- Integration and numerics --------!
    TimeStep=20.0          !Simulation timestep
    SimulationTime=800.0   !Simulation length - note this is short for illustrative purposes
    ExShift=77.8381            !Diagonal shift of Hamiltonian
    CoupTimeStep=5.0       !Timestep in coupling regions
    MinTimeStep=1.0        !Minimum adaptive timestep
   
   !-------- Spawning -------!
    CSThresh=3.0           !Coupling threshold to enter spawning mode
    PopToSpawn=0.01        !Minimum population before spawning
    OMax=0.6               !Prevent spawning if spawned trajectory has at least
                           !this much overlap with existing basis
    MaxTraj=50             !Max number of trajectories
    IgnoreState=1          !Remove uncoupled trajectories on S0
    MaxEDiff=0.04          !Energy gap threshold for calculating couplings
   
   !------ Output Options -----!
    zEDatFile=.true.       !Energy file
    zNDatFile=.true.       !Population file
    zTrajFile=.false.      !Trajectory data file
    zAmpFile=.true.        !Amplitude files
    zPotEnFile=.true.      !Potential energy files
    zXYZ=.true.            !XYZ files
    zCoupFile=.true.       !Coupling files
    zChargeFile=.true.     !Charge files
    zDipoleFile=.true.     !Dipole files
    zTDipoleFile=.true.    !Transition dipole files
    WriteMolden=.true.     !Write molden files?
    MoldenStep=100         !time between molden files
   /
    

.. code-block:: text
   :caption: examples/aims_ethyl_CASSCF/Geometry.dat

          UNITS=BOHR
           6
          C        .0000000059         .0000000000        1.2790603970
          C       -.0000000025         .0000000000       -1.2790603970
          H       -.0000000032        1.7255896200       -2.3437915934
          H       -.0000000180        1.7255896200        2.3437915934
          H       -.0000000300       -1.7255896200        2.3437915934
          H        .0000000089       -1.7255896200       -2.3437915934

.. code-block:: text
   :caption: examples/aims_ethyl_CASSCF/Frequencies.dat

            6        12
         903.7528062134      956.3515160547      973.2169016266     1081.4111041520
        1347.2742737477     1428.7725115327     1619.2543810461     1733.9363838709
        3311.5802800265     3331.2669071062     3396.3102184138     3424.0982861930
            .0000000013        -.0390884910         .0000000000        -.0000000013
           -.0390884910         .0000000000        -.0000000011         .2328927096
            .4297450592        -.0000000022         .2328927096        -.4297450592
           -.0000000083         .2328927096         .4297450592         .0000000116
            .2328927096        -.4297450592
           -.1224921629        -.0000000003        -.0000000019         .1224921629
           -.0000000003         .0000000009        -.3982789485         .0000000028
            .0000000065         .3982789485         .0000000046        -.0000000004
            .3982789485        -.0000000010         .0000000115        -.3982789485
            .0000000009        -.0000000053
            .0773477556        -.0000000004         .0000000014         .0773477556
            .0000000004         .0000000002        -.4608448140        -.0000000009
           -.0000000015        -.4608448140        -.0000000010        -.0000000078
           -.4608448140         .0000000036        -.0000000077        -.4608448140
           -.0000000017        -.0000000014
            .0000000000        -.0000000011         .0000000006         .0000000000
            .0000000008        -.0000000006        -.4980193316        -.0000000032
           -.0000000070         .4980193316         .0000000021         .0000000059
           -.4980193316         .0000000047        -.0000000049         .4980193316
           -.0000000005         .0000000059
           -.0000000001        -.1223605066         .0000000000        -.0000000001
            .1223605066         .0000000000         .0000000006        -.1174845526
           -.3808090966        -.0000000042         .1174845526        -.3808090966
            .0000000059         .1174845526         .3808090966         .0000000012
           -.1174845526         .3808090966
           -.0000000002         .0000000000         .1383677568         .0000000005
            .0000000000        -.1383677568         .0000000002        -.1068007050
           -.3500649362        -.0000000021        -.1068007050         .3500649362
            .0000000013         .1068007050         .3500649362        -.0000000032
            .1068007050        -.3500649362
            .0000000007         .0000000000        -.0652027245         .0000000004
            .0000000000        -.0652027245        -.0000000016         .2679058162
            .3884836376        -.0000000067        -.2679058162         .3884836376
           -.0000000048         .2679058162         .3884836376         .0000000003
           -.2679058162         .3884836376
           -.0000000004         .0000000000         .1409332482        -.0000000003
            .0000000000        -.1409332482        -.0000000011         .2552526222
            .2540250265         .0000000050         .2552526222        -.2540250265
            .0000000053        -.2552526222        -.2540250265        -.0000000014
           -.2552526222         .2540250265
           -.0000000010         .0000000000         .0416086531        -.0000000002
            .0000000000         .0416086531        -.0000000005         .4198210670
           -.2479080594         .0000000046        -.4198210670        -.2479080594
            .0000000075         .4198210670        -.2479080594         .0000000025
           -.4198210670        -.2479080594
            .0000000009         .0000000000        -.0511876036        -.0000000001
            .0000000000         .0511876036        -.0000000002         .4140808652
           -.2468786768        -.0000000049         .4140808652         .2468786768
           -.0000000074        -.4140808652         .2468786768         .0000000023
           -.4140808652        -.2468786768
            .0000000002         .0662092557         .0000000000         .0000000002
           -.0662092557         .0000000000         .0000000002         .3992928311
           -.2499404332         .0000000054        -.3992928311        -.2499404332
           -.0000000079        -.3992928311         .2499404332        -.0000000027
            .3992928311         .2499404332
            .0000000002         .0667440272         .0000000000        -.0000000002
            .0667440272         .0000000000         .0000000004        -.3976668561
            .2516792378         .0000000053        -.3976668561        -.2516792378
           -.0000000078        -.3976668561         .2516792378         .0000000021
           -.3976668561        -.2516792378
