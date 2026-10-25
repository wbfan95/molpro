.. _non_adiabatic_coupling_matrix_elements--non-adiabatic-coupling-matrix-elements:

Non adiabatic coupling matrix elements
======================================

Non-adiabatic coupling matrix elements can be computed by finite differences for ``MCSCF`` or ``CI`` wavefunctions using the ``DDR`` program. For state-averaged ``MCSCF`` wavefunctions, they can also be computed analytically (cf. section `difference gradients for SA-MCSCF <the_mcscf_program_multi.html#difference-gradients-for-sa-mcscf>`__).

Note that present numerical procedure has been much simplified relative to ``Molpro96``. No ``GEOM`` and ``DISPL`` input cards are needed any more, and the three necessary calculations can be done in any order.

.. _non_adiabatic_coupling_matrix_elements--the-ddr-procedure:

The DDR procedure
=================

In order to compute the coupling matrix elements by finite differences, one has to compute and store the wavefunctions at two (first-order algorithm) or three (second-order algorithm) slightly displaced geometries. The order of these calculations is arbitrary.

The typical strategy is as follows:

1.) Compute the wavefunction at the reference geometry. The wavefunctions for both states have to be stored using the ``SAVE`` command of the ``CI`` program. If the matrix elements are computed for ``MCSCF`` wavefunctions, it is necessary to recompute the wavefunction with the ``CI`` program, using the ``NOEXC`` option. The transition density matrix is stored using the ``DM`` directive of the CI program.

2.) Compute the wavefunctions at the (positively) displaced geometry and store the CI wavefunction in a second record.

3.) If the second-order (three-point) method is used, step (2) is repeated at a (negatively) displaced geometry.

4.) Compute the transition density matrices between the states at the reference geometry and the displaced geometr(ies). This is done with the ``TRANS`` directive of the CI program.

5.) Finally, the ``DDR`` program is used to assemble the matrix element. Using the first-order two-point method, only a single input line is needed:

``DDR, dr, orb1, orb2, trdm2``

where *dr* is the geometry increment used as denominator in the finite difference method, *orb1* is the record holding the orbitals of the reference geometry, *orb2* is the record holding the orbitals of the displaced geometry, and *trdm2* is the record holding the transition density matrix computed from the CI-vectors at *R* and *R+DR*.

If central differences (three points) are used, the input is as follows:

``DDR,2*dr\\``
``ORBITAL,orb1,orb2,orb3\\``
``DENSITY,trdm1,trdm2,trdm3\\``
where *dr, orb1, orb2* are as above, and *orb3* is the record holding the orbitals at the negatively displaced geometry.

*trdm1, trdm2, trdm3* are the records holding the transition densities :math:`\gamma(R|R)`, :math:`\gamma(R|R+DR)`, and :math:`\gamma(R|R-DR)`, respectively.

If more than two states are computed simultaneously, the transition density matrices for all pairs of states will be stored in the same record. In that case, and also when there are just two states whose spatial symmetry is not 1, it is necessary to specify for which states the coupling is to be computed using the ``STATE`` directive:

``STATE,state$_1$, state$_2$``

where *state:math:`_i`* is of the form *istate.isym* (the symmetries of both states must be the same, and it is therefore sufficient to specify the symmetry of the first state).

As an example the input for first-order and second-order calculations is given below. The calculation is repeated for a range of geometries, and at the end of the calculation the results are printed using the ``TABLE`` command.

In the calculation shown, the "diabatic" CASSCF orbitals are generated in the two CASSCF calculations at the displaced geometries by maximizing the overlap with the orbitals at the reference geometry. This is optional, and (within the numerical accuracy) does not influence the final results. However, the relative contributions of the orbital, overlap and CI contributions to the NACME are modified. If diabatic orbitals are used, which change as little as possible as function of geometry, the sum of overlap and orbital contribution is minimized, and to a very good approximation the NACME could be obtained from the CI-vectors alone.

.. code-block:: text
   :caption: examples/lif_nacme.inp

   ***,lif non-adiabatic coupling
   
   basis,f=avdz,li=vdz             !define basis
   r=[10.0,10.5,11.0,11.5,12.0]    !define bond distances
   dr=0.01                         !define increment
   geometry={li;f,li,rlif}         !define geometry
   
   rlif=3                          !first calculation at R=3
   {hf;occ,4,1,1}                  !SCF
   {multi;closed,3;                !CASSCF, 3 inactive orbitals
   wf,12,1;state,2;                !Two 1A1 states
   orbital,2140.2}                 !dump orbitals to record 2140.2
   
   do i=1,#r                       !loop over geometries
   rlif=r(i)                       !set bond distance
   {multi;closed,3;                !CASSCF, 3 inactive orbitals
   wf,12,1;state,2;                !Two 1A1 states
   orbital,2140.2}                 !Overwrite previous orbitals by present ones
   
   {ci;state,2;noexc;              !CI for 2 states, no excitations
   save,6000.2;                    !save wavefunction to record 6000.2
   dm,8000.2}                      !save (transition) densities to record 8000.2
   
   rlif=r(i)+dr                    !increment bond distance by dr
   
   {multi;closed,3;                !same CASSCF as above
   wf,12,1;state,2;                !Two 1A1 states
   start,2140.2;                   !start with orbitals from reference geometry
   orbital,2141.2;                 !save orbitals to record 2141.2
   diab,2140.2}                    !generate diabatic orbitals by maximizing the
                                   !overlap with the orbitals at the reference geometry
   
   {ci;state,2;noexc;save,6001.2}   !CI for 2 states, wavefunction saved to record 6001.2
   
   {ci;trans,6000.2,6001.2;        !Compute overlap and transition density <R|R+DR>
   dm,8100.2}                      !Save transition density to record 8100.2
   
   rlif=r(i)-dr                    !repeat at r-dr
   
   {multi;closed,3;                !same CASSCF as above
   wf,12,1;state,2;                !Two 1A1 states
   start,2140.2;                   !start with orbitals from reference geometry
   orbital,2142.2;                 !save orbitals to record 2142.2
   diab,2140.2}                    !generate diabatic orbitals by maximizing the
                                   !overlap with the orbitals at the reference geometry
   
   {ci;state,2;noexc;save,6002.2}  !CI for 2 states, wavefunction saved to record 6002.2
   
   {ci;trans,6000.2,6002.2;        !Compute overlap and transition density <R|R-DR>
   dm,8200.2}                      !Save transition density to record 8200.2
   
   {ddr,dr,2140.2,2141.2,8100.2}   !compute NACME using 2-point formula (forward difference)
   nacme1p(i)=nacme                !store result in variable nacme1p
   {ddr,-dr,2140.2,2142.2,8200.2}  !compute NACME using 2-point formula (backward difference)
   nacme1m(i)=nacme                !store result in variable nacme1m
   
   {ddr,2*dr                       !compute NACME using 3-point formula
   orbital,2140.2,2141.2,2142.2;   !orbital records for R, R+DR, R-DR
   density,8000.2,8100.2,8200.2}   !transition density records for R, R+DR, R-DR
   nacme2(i)=nacme                 !store result in variable nacme2
   
   end do                          !end of loop over different bond distances
   
   nacmeav=(nacme1p+nacme1m)*0.5   !average the two results forward and backward differences
   table,r,nacme1p,nacme1m,nacmeav,nacme2   !print a table with results
   title,Non-adiabatic couplings for LiF    !title for table

This calculation produces the following table:

.. code-block:: text

    Non-adiabatic couplings for LiF
   
          R      NACME1P       NACME1M       NACMEAV       NACME2
       10.0   -0.22828936   -0.22328949   -0.22578942   -0.22578942
       10.5   -0.51777034   -0.50728914   -0.51252974   -0.51252974
       11.0    0.76672943    0.76125391    0.76399167    0.76399167
       11.5    0.42565202    0.42750263    0.42657733    0.42657733
       12.0    0.19199878    0.19246799    0.19223338    0.19223338

Note that the sign changes because of a phase change of one of the wavefunctions. In order to keep track of the sign, one has to inspect both the orbitals and the ci-vectors.

Please also see `the_mcscf_program_multi#diabatic_orbitals <the_mcscf_program_multi.html#diabatic-orbitals>`__.
