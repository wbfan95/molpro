.. raw:: html

   <span id="approximations-used-in-calculating-spin-orbit-integrals-and-matrix-elements"></span>

.. raw:: html

   <span id="calculation-and-diagonalization-of-the-entire-so-matrix"></span>

.. raw:: html

   <span id="so-calculation-for-the-s-atom-using-the-bp-operator"></span>

.. _spin-orbit-coupling--spin-orbit-coupling:

Spin-orbit-coupling
===================

.. _spin-orbit-coupling--introduction:

Introduction
============

Spin-orbit matrix elements and eigenstates can be computed using either the Breit-Pauli (BP) operator or spin-orbit pseudopotentials (ECPs). The *state-interacting* method is employed, which means that the spin-orbit eigenstates are obtained by diagonalizing :math:`\hat H_{el} + \hat H_{SO}` in a basis of eigenfunctions of :math:`\hat H_{el}`. The full Breit-Pauli SO-operator can be used only for MCSCF wavefunctions. For MRCI wavefunctions, the full BP operator is used for computing the matrix elements between *internal configurations* (no electrons in external orbitals), while for contributions of external configurations a mean-field one-electron fock operator is employed. The error caused by this approximation is usually smaller than 1 cm\ :math:`^{-1}`.

The program allows either the computation of individual spin-orbit matrix elements for a given pair of states, or the automatic setting-up and diagonalization of the whole matrix for a given set of electronic states. In the latter case, matrix elements over one-electron operators are also computed and transformed to the spin-orbit eigenstates (by default, the dipole matrix elements are computed; other operators can be specified on the ``GEXPEC`` or ``EXPEC`` cards, see section `One-electron operators and expectation values (GEXPEC) <program_control.html#one-electron-operators-and-expectation-values-gexpec>`__). Since it may be often sufficient to compute the spin-orbit matrix elements in a smaller basis than the energies, it is possible to replace the energy eigenvalues by precomputed values, which are passed to the spin-orbit program by the ``MOLPRO`` variable ``HLSDIAG``.

.. _spin-orbit-coupling--calculation-of-so-integrals:

Calculation of SO integrals
===========================

The one-and two-electron spin-orbit integrals over the BP Hamiltonian can be precomputed and stored on disk using the command

``LSINT [,X] [,Y] [,Z] [,ONECENTER] [;TWOINT,twoint;] [;PREFAC,prefac;]\\``
``X``, ``Y``, and ``Z`` specify the components to be computed. If none of these is given, all three are evaluated. The advantage of precomputing the integrals is that they can then be used in any number of subsequent SO calculations, but this may require a large amount of disk space (note that there are 6 times as many integrals as in an energy calculation). If the ``LSINT`` card is not given, the integrals are computed whenever needed. The keyword ``ONECENTER`` activates the one-center approximation for one- and two- electron spin-orbit integrals. This can reduce drastically the computing time for large molecules. ``TWOINT`` and ``PREFAC`` can be used to control the accuracy of spin-orbit integrals. These thresholds are similar to ``TWOINT`` and ``PREFAC`` for standard integrals. The default value for ``PREFAC`` is ``TWOINT/100``, and the default value for ``TWOINT`` is :math:`10^{-7}`. In the case when no integrals are precomputed, these thresholds can be specified as options for ``HLSMAT`` or ``TRANLS`` cards, see below.

The input for spin-orbit ECPs is described in section :doc:`effective core potentials <effective_core_potentials>`. Of course, in ECP-LS calculations the ``LSINT`` card is not needed.

.. _spin-orbit-coupling--calculation-of-individual-so-matrix-elements:

Calculation of individual SO matrix elements
============================================

Individual spin-orbit matrix elements can be computed within the MRCI program using

``TRANLS,record1.file, record2.file, bra2ms, ket2ms, lsop;``

where

* ***record1.file*** Record holding the bra-wavefunction.
* ***record2.file*** Record holding the ket-wavefunction. Both records must have been generated using the ``SAVE`` directive of the MRCI program.
* ***bra2ms*** :math:`2 \times M_S` value of the bra-wavefunction.
* ***ket2ms*** :math:`2 \times M_S` value of the ket-wavefunction.
* ***lsop*** Cartesian component of the Spin-orbit Hamiltonian.

This can be one of :math:`{\tt LSX}`, :math:`{\tt LSY}`, or :math:`{\tt LSZ}` in all electron calculations, and :math:`{\tt ECPLSX}`, :math:`{\tt ECPLSY}`, or :math:`{\tt ECPLSZ}` in ECP calculations. Starting from the ``MOLPRO`` version 2008.1, more types are available which control the approximation level. These are described in section `approximations used in calculating spin-orbit integrals and matrix elements <spin-orbit-coupling.html#approximations-used-in-calculating-spin-orbit-integrals-and-matrix-elements>`__.

Since the spin-orbit program is part of the MRCI program, the ``TRANLS`` card must be preceded by a ``[MR]CI`` card.  If in the MRCI step several states of the same symmetry are computed simultaneously using the ``STATE`` directive, the matrix elements are computed for all these states. Note that the ``OCC`` and ``CLOSED`` cards must be the same for all states used in a ``TRANLS`` calculation. ``TRANLS`` can also be used with records saved by the ``MULTI`` program (e.g. ``multi,cisave=record1.file``).

The selection rules for the :math:`M_S` values are :math:`\Delta M_S = \pm 1` for the ``LSX`` and ``LSY`` operators, and :math:`\Delta M_S=0` for the ``LSZ`` operator. Note that :math:`2M_S` has to be specified, and so the selection rules applying to the difference of the input values are 0 or 2.

In all-electron SO calculations the value of the calculated spin-orbit matrix element is saved (in atomic units) in the ``MOLPRO`` variables ``TRLSX``, ``TRLSY`` and ``TRLSZ`` for the :math:`x`, :math:`y`, and :math:`z` components respectively. For ECP-LS calculations the variables ``TRECPLSX``, ``TRECPLSY``, and ``TRECPLSZ`` are used. Note that for imaginary matrix elements (i.e., for the :math:`x` and :math:`z` components of the SO Hamiltonian) the matrix elements are imaginary and the stored real values have to be multiplied by :math:`i`. If matrix elements for several states are computed, all values are stored in the respective variable-arrays with the bra-states running fastest.

.. _spin-orbit-coupling--approximations-used-in-calculating-spin-orbit-integrals-and-matrix-elements:

Approximations used in calculating spin-orbit integrals and matrix elements
===========================================================================

Recently, more sophisticated approximations were introduced to simplify spin-orbit calculations for larger molecules. These are controlled by specifying the spin-orbit operator type *lsop* as follows (we omit suffixes ``X, Y, Z`` which specify the component):

* ``LS`` Standard spin-orbit calculations.
* ``ALS`` The one-center approximation is used for one- and two-electron spin-orbit integrals.
* ``FLS`` The effective Fock-matrix approximation is used for the internal part too.
* ``AFLS|AMFI`` The one-center approximation is used for one- and two-electron spin-orbit integrals, and the effective Fock-matrix approximation for the internal part.
* ``ECPLS`` Effective core potentials are used for all atoms at which they are defined; contributions of all other atoms are neglected (see below).

In case that the effective Fock matrix is used for all contributions, and no spin-orbit integrals are pre-calculated and stored on disk (i.e., the ``LSINT`` command is not given), the Fock matrices are evaluated in direct mode and no integrals are stored on disk. When this is combined with the one-center approximation (AMFI), the computing and I/O times are drastically reduced, and this makes spin-orbit calculations quite fast even for larger molecules.

Also, the treatment of ECP-type of spin-orbit interaction has been changed and now allows for treating both ECP and non-ECP atoms in one calculation. Thus, in molecules containing both heavy and light atoms, the heavy atoms can be described using ECPs and the light atoms using all-electron basis sets. If the operator type is ``LS``, ``ALS``, ``FLS``, or ``AFLS``, then for the atoms having an ECP spin-orbit operator defined in the basis input the ECP operator is used, while the full BP-operator is used for all other atoms (couplings are neglected). Both one-center and AMFI approximations can be used in this case. If, on the other hand, one specifies the operator type as ``ECPLS``, then the behavior is the same as in the previous versions, i.e., only the ECP contributions are considered and the contributions from all other atoms are neglected.

.. _spin-orbit-coupling--calculation-and-diagonalization-of-the-entire-so-matrix:

Calculation and diagonalization of the entire SO-matrix
=======================================================

``HLSMAT,type, record1, record2, record3, …``

Computes the entire SO matrix and diagonalizes it using all states which are contained in the records *record1, record2, record3, …*. All records must have been generated using the ``SAVE`` directive of the of the MULTI or MRCI programs. *type* may be either ``LS`` for Breit-Pauli calculations, or ``ECP`` for ECP-LS calculations. By default, the eigenvalues and dipole transition matrix elements between the ground and excited states are printed.

As with the ``TRANLS`` card, the ``HLSMAT`` is recognized only by the MRCI program and must be preceded by a ``CI`` card (this is no longer necessary with molpro2021.3 or later). Also, the ``OCC`` and ``CLOSED`` cards must be the same for all states used in a ``HLSMAT`` calculation.

.. _spin-orbit-coupling--modifying-the-unperturbed-energies:

Modifying the unperturbed energies
==================================

Often it may be sufficient to compute the spin-orbit matrix elements in a smaller basis or at a lower computational level than the energies. It is therefore possible to replace the energy eigenvalues by precomputed values, which are passed to the spin-orbit program by the ``MOLPRO`` variable ``HLSDIAG``. The energy values in ``HLSDIAG`` must be in exactly the same order as the states in the records given on the ``HLSMAT`` card. Before any spin-orbit calculation, the variable ``HLSDIAG`` must either be undefined or cleared (then the original energies are used), or must contain exactly the number of energies as the number of states treated in the subsequent spin-orbit calculation (use ``CLEAR,HLSDIAG`` to clear any previous values in the variable). It is the user’s responsibility that the order of the energies in ``HLSDIAG`` is correct!

See example in section `SO calculation for the S-atom using the BP operator <spin-orbit-coupling.html#so-calculation-for-the-s-atom-using-the-bp-operator>`__

.. _spin-orbit-coupling--print-options-for-spin-orbit-calculations:

Print Options for spin-orbit calculations
=========================================

``PRINT,option$_1$=value$_1$, option$_2$=value$_2, \ldots$``

where option can be

* ``HLS`` ``HLS=-1`` only the SO energies and transition matrix elements between ground and excited states are printed (default).

``HLS``\ :math:`\ge 0`: The SO matrix is printed.
``HLS``\ :math:`\ge 1`: The property matrices are printed.
``HLS``\ :math:`\ge 2`: The individual matrix elements are printed (same as ``OPTION,MATEL``).
``HLS``\ :math:`\ge 3`: Debugging information is printed.

* ``VLS`` ``VLS=-1``: No print of eigenvectors (default).

``VLS``\ :math:`\ge 0`: The eigenvectors are printed.

.. _spin-orbit-coupling--options-for-spin-orbit-calculations:

Options for spin-orbit calculations
===================================

Some options can be set using the ``OPTION`` directive (in any order)

``OPTIONS  [,WIGNER=value] [,HLSTRANS=value] [,MATEL=value] \\``
where

* ``WIGNER`` This option determines whether the Wigner-Eckart theorem should be used when the SO matrix is determined. ``WIGNER=1`` (default) uses the theorem, ``WIGNER=0`` calculates each SO matrix element individually. This option is needed for test purposes only.
* ``HLSTRANS`` This option determines whether a SO matrix calculation should be performed in the not spin-symmetry adapted basis set (``HLSTRANS=0``), in the spin-symmetry adapted basis set (``HLSTRANS=1``, default) or with both basis sets (``HLSTRANS=2``). At present, symmetry adaption can only be performed for triplet states, where the following notation is used to indicate the symmetry adapted spin functions: :math:`|S,M_S\rangle_+ = \frac{1}{\sqrt{2}} (|S,M_S\rangle + |S,-M_S\rangle)`, :math:`|S,M_S\rangle_- = \frac{1}{\sqrt{2}} (|S,M_S\rangle - |S,-M_S\rangle)`. If only singlet and triplet states are considered, the spin-orbit matrix is blocked according to double-group symmetry and the eigenvalues for each each block are printed separately. In all other cases the ``HLSTRANS`` option is ignored.
* ``MATEL`` If the entire SO matrix is calculated using ``HLSMAT``, the individual matrix elements are normally not shown. When the option ``MATEL=1`` is given, the individual matrix elements and the contributions of the internal and external configuration classes are printed.

.. _spin-orbit-coupling--data-dump:

Data dump
=========

The data from the SO-CI calculation (SO-CI matrix, property matrices, energies, etc.) can be exported (dumped) to a file (for external post-processing).

``DUMP,format,file``

where format is one of

* ``HDF5`` - Exports the data into a HDF5 file. Note: This is **only supported if Molpro has been compiled with enabled HDF5 support** (by default support is disabled!)

and file is the name of the file the data will be written to.

.. _spin-orbit-coupling--examples:

Examples
========

.. _spin-orbit-coupling--so-calculation-for-the-s-atom-using-the-bp-operator:

SO calculation for the S-atom using the BP operator
===================================================

.. code-block:: text
   :caption: examples/s_so.inp

   ***,SO calculation for the S-atom
   geometry={s}
   basis={spd,s,vtz}                                 !use uncontracted basis
   
   {rhf;occ,3,2,2,,2;wf,16,4,2}                      !rhf for 3P state
   
   {multi                                            !casscf
   wf,16,4,2;wf,16,6,2;wf,16,7,2;                    !3P states
   wf,16,1,0;state,3;wf,16,4,0;wf,16,6,0;wf,16,7,0}  !1D and 1S states
   
   {ci;wf,16,1,0;save,3010.2;state,3;noexc}          !save casscf wavefunctions using mrci
   {ci;wf,16,4,0;save,3040.2;noexc}
   {ci;wf,16,6,0;save,3060.2;noexc}
   {ci;wf,16,7,0;save,3070.2;noexc}
   {ci;wf,16,4,2;save,3042.2;noexc}
   {ci;wf,16,6,2;save,3062.2;noexc}
   {ci;wf,16,7,2;save,3072.2;noexc}
   
   {ci;wf,16,1,0;save,4010.2;state,3}                !mrci calculations for 1D, 1S states
   ed=energy(1)                                      !save energy for 1D state in variable ed
   es=energy(3)                                      !save energy for 1S state in variable es
   {ci;wf,16,4,2;save,4042.2}                        !mrci calculations for 3P states
   ep=energy                                         !save energy for 3P state in variable ep
   {ci;wf,16,6,2;save,4062.2}                        !mrci calculations for 3P states
   {ci;wf,16,7,2;save,4072.2}                        !mrci calculations for 3P states
   text,only triplet states, casscf
   
   lsint                                             !compute so integrals
   
   text,3P states, casscf
   {ci;hlsmat,ls,3042.2,3062.2,3072.2}               !Only triplet states, casscf
   
   text,3P states, mrci
   {ci;hlsmat,ls,4042.2,4062.2,4072.2}               !Only triplet states, mrci
   
   text,3P, 1D, 1S states, casscf
   {ci;hlsmat,ls,3010.2,3040.2,3060.2,3070.2,3042.2,3062.2,3072.2}       !All states, casscf
   
   text,only triplet states, use mrci energies and casscf SO-matrix elements
   hlsdiag=[ed,ed,es,ed,ed,ed,ep,ep,ep]             !set variable hlsdiag to mrci energies
   {ci;hlsmat,ls,3010.2,3040.2,3060.2,3070.2,3042.2,3062.2,3072.2}

.. _spin-orbit-coupling--so-calculation-for-the-i-atom-using-ecps:

SO calculation for the I-atom using ECPs
========================================

.. code-block:: text
   :caption: examples/i_ecp.inp

   ***,I
   gprint,orbitals,civector,basis;
   gthresh,energy=1.d-8,coeff=1.d-8;
   geometry={I};
   
   basis={
   !
   ! Iodine-ECP (Dirac-Fock) with SO-coupling
   !
   ecp,I,46,4,3;
   1; 2,   1.00000000,       0.00000000;                                       ! local term = 0
   2; 2,   3.50642001,      83.09814545; 2,   1.74736492,       5.06370919;    ! s-terms
   4; 2,   2.99860773, 1/3* 81.88444526; 2,   3.01690894, 2/3* 83.41280402;    ! p-terms with weights
      2,   1.59415934, 1/3*  2.32392477; 2,   1.19802939, 2/3*  2.72079843;
   4; 2,   1.03813792, 2/5*  6.40131754; 2,   1.01158599, 3/5*  6.21328827;    ! d-terms with weights
      2,   2.04193864, 2/5* 19.11604172; 2,   1.99631017, 3/5* 19.08465909;
   4; 2,   2.64971585,-3/7* 24.79106489; 2,   2.75335574,-4/7* 24.98147319;    ! f-terms with weights
      2,   0.49970082,-3/7*  0.27936581; 2,   0.79638982,-4/7*  0.70184261;
   4; 2,   2.99860773,-2/3* 81.88444526; 2,   3.01690894, 2/3* 83.41280402;    ! ECP-SO for p-terms
      2,   1.59415934,-2/3*  2.32392477; 2,   1.19802939, 2/3*  2.72079843;
   4; 2,   1.03813792,-2/5*  6.40131754; 2,   1.01158599, 2/5*  6.21328827;    ! ECP-SO for d-terms
      2,   2.04193864,-2/5* 19.11604172; 2,   1.99631017, 2/5* 19.08465909;
   4; 2,   2.64971585, 2/7* 24.79106489; 2,   2.75335574,-2/7* 24.98147319;    ! ECP-SO for f-terms
      2,   0.49970082, 2/7*  0.27936581; 2,   0.79638982,-2/7*  0.70184261;
   !
   ! Iodine-basis
   !
   s,I,0.2027624,0.4080619,0.8212297,1.6527350,3.3261500;
   c,1.5,-0.4782372,-0.5811680,0.2617769,0.4444120,-0.1596560;
   s,I,0.05,0.1007509;
   p,I,0.2027624,0.4080619,0.8212297,1.6527350,3.3261500;
   c,1.5,0.4251859,0.2995618,0.0303167,-0.2064228,0.0450858;
   p,I,0.05,0.1007509,0.01;  ! diffuse p-function because of possible negative partial charge
   d,I,0.2,0.4;
   f,I,0.3;
   }
   
   
   {hf;occ,1,1,1,,1;wf,7,5,1}       !scf for 2Pz
   {multi;occ,1,1,1,,1;             !casscf with minimal active space
   wf,7,2,1;wf,7,3,1;wf,7,5,1}      !average 2P states
   {ci;wf,7,2,1;noexc;save,5000.2}  !save casscf vector for 2Px state
   {ci;wf,7,3,1;noexc;save,5100.2}  !save casscf vector for 2Py state
   {ci;wf,7,5,1;noexc;save,5200.2}  !save casscf vector for 2Pz state
   {ci;wf,7,2,1;save,6000.2}        !mrci for 2Px state
   {ci;wf,7,3,1;save,6100.2}        !mrci for 2Py state
   {ci;wf,7,5,1;save,6200.2}        !mrci for 2Pz state
   
   {multi;occ,1,2,2,,2              !casscf with larger active space
   wf,7,2,1;wf,7,3,1;wf,7,5,1}      !average 2P states
   {ci;wf,7,2,1;noexc;save,5010.2}
   {ci;wf,7,3,1;noexc;save,5110.2}
   {ci;wf,7,5,1;noexc;save,5210.2}
   {ci;wf,7,2,1;save,6010.2}
   {ci;wf,7,3,1;save,6110.2}
   {ci;wf,7,5,1;save,6210.2}
   
   text,casscf,  occ,1,1,1,,1
   {ci;hlsmat,ecp,5000.2,5100.2,5200.2}   !do spin-orbit calculations
   text,casscf,  occ,1,2,2,,2
   {ci;hlsmat,ecp,5010.2,5110.2,5210.2}
   
   text,mrci, occ,1,1,1,,1
   {ci;hlsmat,ecp,6000.2,6100.2,6200.2}
   text,mrci, occ,1,2,2,,2
   {ci;hlsmat,ecp,6010.2,6110.2,6210.2}

.. code-block:: text
   :caption: examples/i_ecp_cpp.inp

   ***,I
   
   gprint,orbitals,civector,basis;
   gthresh,energy=1.d-8,coeff=1.d-8;
   geometry={I};
   
   basis={
   !
   ! Iodine-ECP (Dirac-Fock) with SO-coupling and cpp
   !
   ecp,I,46,4,3;
   1; 2,   1.00000000,       0.00000000;                                       ! local term = 0
   2; 2,   3.50642001,      83.09814545; 2,   1.74736492,       5.06370919;    ! s-terms
   4; 2,   2.99860773, 1/3* 81.88444526; 2,   3.01690894, 2/3* 83.41280402;    ! p-terms with weights
      2,   1.59415934, 1/3*  2.32392477; 2,   1.19802939, 2/3*  2.72079843;
   4; 2,   1.03813792, 2/5*  6.40131754; 2,   1.01158599, 3/5*  6.21328827;    ! d-terms with weights
      2,   2.04193864, 2/5* 19.11604172; 2,   1.99631017, 3/5* 19.08465909;
   4; 2,   2.64971585,-3/7* 24.79106489; 2,   2.75335574,-4/7* 24.98147319;    ! f-terms with weights
      2,   0.49970082,-3/7*  0.27936581; 2,   0.79638982,-4/7*  0.70184261;
   4; 2,   2.99860773,-2/3* 81.88444526; 2,   3.01690894, 2/3* 83.41280402;    ! ECP-SO for p-terms
      2,   1.59415934,-2/3*  2.32392477; 2,   1.19802939, 2/3*  2.72079843;
   4; 2,   1.03813792,-2/5*  6.40131754; 2,   1.01158599, 2/5*  6.21328827;    ! ECP-SO for d-terms
      2,   2.04193864,-2/5* 19.11604172; 2,   1.99631017, 2/5* 19.08465909;
   4; 2,   2.64971585, 2/7* 24.79106489; 2,   2.75335574,-2/7* 24.98147319;    ! ECP-SO for f-terms
      2,   0.49970082, 2/7*  0.27936581; 2,   0.79638982,-2/7*  0.70184261;
   !
   ! Iodine-basis
   !
   s,I,0.2027624,0.4080619,0.8212297,1.6527350,3.3261500;
   c,1.5,-0.4782372,-0.5811680,0.2617769,0.4444120,-0.1596560;
   s,I,0.05,0.1007509;
   p,I,0.2027624,0.4080619,0.8212297,1.6527350,3.3261500;
   c,1.5,0.4251859,0.2995618,0.0303167,-0.2064228,0.0450858;
   p,I,0.05,0.1007509,0.01;  ! diffuse p-function because of possible negative partial charge
   d,I,0.2,0.4;
   f,I,0.3;
   }
   
   {cpp,init,1;       ! core polarization potential
   I,2,1.028,,,1.23}  ! Iodine-atom,form of cut-off function, static polarizability
                      ! 1.23 =  exponential-factor of cut-off function
   
   {hf;occ,1,1,1,,1;wf,7,5,1}      !scf for 2Pz
   {multi;occ,1,1,1,,1;            !casscf with minimal active space
   wf,7,2,1;wf,7,3,1;wf,7,5,1}     !average 2P states
   {ci;wf,7,2,1;noexc;save,5000.2} !save casscf vector for 2Px state
   {ci;wf,7,3,1;noexc;save,5100.2} !save casscf vector for 2Py state
   {ci;wf,7,5,1;noexc;save,5200.2} !save casscf vector for 2Pz state
   {ci;wf,7,2,1;save,6000.2}       !mrci for 2Px state
   {ci;wf,7,3,1;save,6100.2}       !mrci for 2Py state
   {ci;wf,7,5,1;save,6200.2}       !mrci for 2Pz state
   
   {multi;occ,1,2,2,,2              !casscf with larger active space
   wf,7,2,1;wf,7,3,1;wf,7,5,1}     !average 2P states
   {ci;wf,7,2,1;noexc;save,5010.2}
   {ci;wf,7,3,1;noexc;save,5110.2}
   {ci;wf,7,5,1;noexc;save,5210.2}
   {ci;wf,7,2,1;save,6010.2}
   {ci;wf,7,3,1;save,6110.2}
   {ci;wf,7,5,1;save,6210.2}
   
   text,casscf,  occ,1,1,1,,1
   {ci;hlsmat,ecp,5000.2,5100.2,5200.2}   !do spin-orbit calculations
   text,casscf,  occ,1,2,2,,2
   {ci;hlsmat,ecp,5010.2,5110.2,5210.2}
   
   text,mrci, occ,1,1,1,,1
   {ci;hlsmat,ecp,6000.2,6100.2,6200.2}
   text,mrci, occ,1,2,2,,2
   {ci;hlsmat,ecp,6010.2,6110.2,6210.2}
