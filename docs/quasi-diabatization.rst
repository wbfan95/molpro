.. _quasi-diabatization--quasi-diabatization:

Quasi-diabatization
===================

The DDR procedure can also be used to generate quasi-diabatic states and energies for MRCI wavefunctions (CASSCF case can be treated as special case using the ``NOEXC`` directive in the MRCI). The quasi-diabatic states have the property that they change as little as possible relative to a reference geometry; with other words, the overlap between the states at the current geometry with those at a reference geometry is maximized by performing a unitary transformation among the given states. Preferably, the adiabatic and diabatic states should be identical at the reference geometry, e.g., due to symmetry. For instance, in the examples given below for the :math:`^1B_1` and :math:`^1A_2` states of H\ :math:`_2`\ S, C\ :math:`_{2v}` geometries are used as reference, and at these geometries the states are unmixed due to their different symmetry. At the displaced geometries the molecular symmetry is reduced to :math:`C_S`. Both states now belong to the :math:`^1A''` irreducible representation and are strongly mixed. For a description and application of the procedure described below, see D. Simah, B. Hartke, and H.-J. Werner, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.479214>`__ **111**, 4523 (1999).

This diabatization can be done automatically and requires two steps: first, the active orbitals of a CASSCF calculation are rotated to maximize the overlap with the orbitals at the reference geometry. This is achieved using the ``DIAB`` procedure described in section `diabatic orbitals <the_mcscf_program_multi.html#diabatic-orbitals>`__. Secondly, the ``DDR`` procedure can be used to find the transformation among the CI vectors.

The following input is required:

* ``DDR`` calls the DDR procedure.
* **``ORBITAL``,\ *orb1, orb2*** *orb1* and *orb2* are the (diabatic) orbitals at the current and reference geometry, respectively.
* **``DENSITY``,\ *trdm1,trdm2*** *trdm1* are the transition densities computed at the current geometry, *trdm2* are transition densities computed using the wavefunctions of the current (bra) and reference (ket) geometries.
* **``MIXING``,\ *state1, state2, …*** The given states are included in the diabatization.
* **``ENERGY``,\ *e1, e2, …*** Adiabatic energies of the states. If this input card is present, the Hamiltonian in the basis of the diabatic states is computed and printed. Alternatively, the energies can be passed to ``DDR`` using the Molpro variable ``EADIA``.

The results are printed and stored in the following Molpro variables, provided the ``ENERGY`` directive or the ``EADIA`` variable is found:

Results including the first-order orbital correction:

* ``SMAT`` The first :math:`nstate \times nstate` elements contain the state overlap matrix (bra index runs fastest).
* ``UMAT`` The first :math:`nstate \times nstate` elements contain the transformation matrix.
* ``HDIA`` The first :math:`nstate \cdot (nstate+1)/2` elements contain the lower triangle of the diabatic hamiltonian.
* ``MIXANG`` Non-adiabatic mixing angle in degree. This is available only in the two-state case.

The corresponding results obtained from the CI-vectors only (without orbital correction) are stored in the variables [``SMATCI``], ``UMATCI``, ``HDIACI``, and ``MIXANGCI``.

The way it works is most easily demonstrated for some examples. In the following input, the wavefunction is first computed at the :math:`C_{2v}` reference geometry, and then at displaced geometries.

.. code-block:: text
   :caption: examples/h2s_diab1.inp

   ***,h2s Diabatization
   
   gprint,orbitals,civector
   
   symmetry,x
   orient,noorient             !noorient should always be used for diabatization
   geometry={
            s;
            h1,s,r1;
            h2,s,r2,h1,theta}
   
   basis=avdz                  !This basis is too small for real application
   
   r1=2.5                      !Reference geometry
   theta=[92]
   
   r=[2.50,2.55,2.60]          !Displaced geometries
   
   reforb=2140.2               !Orbital dumprecord at reference geometry
   refci=6000.2                !MRCI record at reference geometry
   savci=6100.2                !MRCI record at displaced geometries
   
   text,compute wavefunction at reference geometry (C2v)
   r2=r1
   
   {hf;occ,9,2;wf,18,2,4;
   orbital,2100.2}
   
   {multi;occ,9,2;closed,4,1;
   wf,18,2;state,2;            !1B1 and 1A2 states
   natorb,reforb               !Save reference orbitals on reforb
   noextra}                    !Dont use extra symmetries
   
   {ci;occ,9,2;closed,4,1;      !MRCI at reference geometry
   wf,18,2,0;state,2;          !1B1 and 1A2 states
   orbital,reforb              !Use orbitals from previous CASSCF
   save,refci}                 !Save MRCI wavefunction
   
   Text,Displaced geometries
   
   do i=1,#r                   !Loop over different r values
   data,truncate,savci+1       !truncate dumpfile after reference
   r2=r(i)                     !Set current r2
   
   {multi;occ,9,2;closed,4,1;
   wf,18,2,0;state,2;          !Wavefunction definition
   start,reforb                !Starting orbitals
   orbital,3140.2;             !Dump record for orbitals
   diab,reforb                 !Generate diabatic orbitals relative to reference geometry
   noextra}                    !Dont use extra symmetries
   
   {ci;occ,9,2;closed,4,1;
   wf,18,2,0;state,2;          !1B1 and 1A2 states
   orbital,diabatic            !Use diabatic orbitals
   save,savci}                 !Save MRCI for displaced geometries
   
   e1(i)=energy(1)             !Save adiabatic energies
   e2(i)=energy(2)
   
   {ci;trans,savci,savci        !Compute transition densities at R2
   dm,7000.2}                  !Save transition densities on this record
   {ci;trans,savci,refci;       !Compute transition densities between R2 and R1
   dm,7100.2}                  !Save transition densities on this record
   
   {ddr
   density,7000.2,7100.2       !Densities for <R2||R2> and <R2||R1>
   orbital,3140.2,2140.2       !Orbitals for <R2||R2> and <R2||R1>
   energy,e1(i),e2(i)          !Adiabatic energies
   mixing,1.2,2.2}             !Compute mixing angle and diabatic energies
   
   mixci(i)=mixangci(1)          !Mixing angle obtained from ci vectors only
   h11ci(i)=hdiaci(1)            !Diabatic energies obtained from ci vectors only
   h21ci(i)=hdiaci(2)
   h22ci(i)=hdiaci(3)
   
   mixtot(i)=mixang(1)         !Mixing angle from total overlap (including first-order correction)
   h11(i)=hdia(1)              !Diabatic energies obtained from total overlap
   h21(i)=hdia(2)
   h22(i)=hdia(3)
   
   
   {table,r,e1,e2,h11ci,h22ci,h21ci,mixci
   title,Diabatic energies for H2S, obtained from CI-vectors
   format,'(f10.2,5f14.8,f12.2)'
   sort,1}
   
   {table,r,e1,e2,h11,h22,h21,mixtot
   title,Diabatic energies for H2S, obtained from CI-vectors and orbital correction
   format,'(f10.2,5f14.8,f12.2)'
   sort,1}
   
   enddo                       !end loop over i

This calculation produces the following results:

.. code-block:: text

    Diabatic energies for H2S, obtained from CI-vectors
   
           R       E1            E2            H11CI         H22CI         H21CI          MIXCI
         2.50 -398.64296319 -398.63384782 -398.64296319 -398.63384782    0.00000000        0.00
         2.55 -398.64572746 -398.63666636 -398.64509901 -398.63729481   -0.00230207       15.27
         2.60 -398.64911752 -398.63771802 -398.64662578 -398.64020976   -0.00471125       27.87
   
    Diabatic energies for H2S, obtained from CI-vectors and orbital correction
   
           R       E1            E2            H11           H22           H21           MIXTOT
         2.50 -398.64296319 -398.63384782 -398.64296319 -398.63384782    0.00000000        0.00
         2.55 -398.64572746 -398.63666636 -398.64509941 -398.63729441   -0.00230139       15.26
         2.60 -398.64911752 -398.63771802 -398.64662526 -398.64021027   -0.00471160       27.88

The results in the first table are obtained from the CI-contribution to the state-overlap matrix only, while the ones in the second table include a first-order correction for the orbitals. In this case, both results are almost identical, since the ``DIAB`` procedure has been used to minimize the change of the active orbitals. This is the recommended procedure. If simply natural orbitals are used without orbital diabatization, the following results are obtained from the otherwise unchanged calculation:

.. code-block:: text

    Diabatic energies for H2S, obtained from CI-vectors
   
           R       E1            E2            H11CI         H22CI         H21CI          MIXCI
         2.50 -398.64296319 -398.63384782 -398.64296319 -398.63384782    0.00000000        0.00
         2.55 -398.64572742 -398.63666630 -398.64475612 -398.63763760   -0.00280315       19.11
         2.60 -398.64911746 -398.63771803 -398.64521031 -398.64162518   -0.00541050       35.83
   
    Diabatic energies for H2S, obtained from CI-vectors and orbital correction
   
           R       E1            E2            H11           H22           H21           MIXTOT
         2.50 -398.64296319 -398.63384782 -398.64296319 -398.63384782    0.00000000        0.00
         2.55 -398.64572742 -398.63666630 -398.64509146 -398.63730226   -0.00231474       15.36
         2.60 -398.64911746 -398.63771803 -398.64648358 -398.64035190   -0.00480493       28.73

It is seen that the mixing obtained from the CI vectors only is now very different and meaningless, since the orbitals change significantly as function of geometry. However, the second calculations, which accounts for this change approximately, still gives results in quite good agreement with the calculation involving diabatic orbitals.

The final examples shows a more complicated input, which also computes the non-adiabatic coupling matrix elements. In a two-state model, the NACME should equal the first derivative of the mixing angle. In the example, the NACME is computed using the 3-point ``DDR`` method (NACMECI), and also by finite difference of the mixing angle (DCHI).

.. code-block:: text
   :caption: examples/h2s_diab2.inp

   ***,h2s Diabatization and NACME calculation
   
   gprint,orbitals,civector
   
   symmetry,x
   orient,noorient             !noorient should always be used for diabatization
   geometry={
            s;
            h1,s,r1;
            h2,s,r2,h1,theta}
   
   basis=avdz                  !This basis is too small for real application
   
   r1=2.5                      !Reference geometry
   theta=[92]
   
   r=[2.55,2.60]               !Displaced geometries
   dr=[0,0.01,-0.01]           !Samll displacements for finite difference NACME calculation
   
   reforb1=2140.2              !Orbital dumprecord at reference geometry
   refci=6000.2                !MRCI record at reference geometry
   savci=6100.2                !MRCI record at displaced geometries
   
   text,compute wavefunction at reference geometry (C2v)
   r2=r1
   
   {hf;occ,9,2;wf,18,2,4;orbital,2100.2}
   
   {multi;occ,9,2;closed,4,1;
   wf,18,2;state,2;            !1B1 and 1A2 states
   natorb,reforb1              !Save reference orbitals on reforb1
   noextra}                    !Dont use extra symmetries
   
   {ci;occ,9,2;closed,4,1;      !MRCI at reference geometry
   wf,18,2,0;state,2;          !1B1 and 1A2 states
   orbital,reforb1             !Use orbitals from previous CASSCF
   save,refci}                 !Save MRCI wavefunction
   
   Text,Displaced geometries
   
   do i=1,#r                   !Loop over different r values
   data,truncate,savci+1       !truncate dumpfile after reference
   reforb=reforb1
   
   do j=1,3                    !Loop over small displacements for NACME
   r2=r(i)+dr(j)               !Set current r2
   
   {multi;occ,9,2;closed,4,1;
   wf,18,2,0;state,2;          !Wavefunction definition
   start,reforb                !Starting orbitals
   orbital,3140.2+j;           !Dumprecord for orbitals
   diab,reforb                 !Generate diabatic orbitals relative to reference geometry
   noextra}                    !Dont use extra symmetries
   
   reforb=3141.2               !Use orbitals for j=1 as reference for j=2,3
   
   {ci;occ,9,2;closed,4,1;
   wf,18,2,0;state,2;
   orbital,diabatic            !Use diabatic orbitals
   save,savci+j}               !Save MRCI for displaced geometries
   
   eadia=energy                !Save adiabatic energies for use in ddr
   if(j.eq.1) then
   e1(i)=energy(1)             !Save adiabatic energies for table printing
   e2(i)=energy(2)
   end if
   
   {ci;trans,savci+j,savci+j;  !Compute transition densities at R2+DR(j)
   dm,7000.2+j}                !Save transition densities on this record
   {ci;trans,savci+j,refci;    !Compute transition densities between R2+DR(j) and R1
   dm,7100.2+j}                !Save transition densities on this record
   {ci;trans,savci+j,savci+1;  !Compute transition densities between R and R2+DR(j)
   dm,7200.2+j}                !Save transition densities on this record
   
   {ddr
   density,7000.2+j,7100.2+j   !Densities for <R2+DR||R2+DR> and <R2+DR||R1>
   orbital,3140.2+j,2140.2     !Orbitals for <R2+DR||R2+DR> and <R2+DR||R1>
   energy,eadia(1),eadia(2)    !Adiabatic energies
   mixing,1.2,2.2}             !Compute mixing angle and diabatic energies
   
   if(j.eq.1) then             !Store diabatic energies for R2  (DR(1)=0)
     mixci(i)=mixangci(1)      !Mixing angle obtained from ci vectors only
     h11ci(i)=hdiaci(1)        !Diabatic energies obtained from ci vectors only
     h21ci(i)=hdiaci(2)        !HDIA contains the lower triangle of the diabatic hamiltonian
     h22ci(i)=hdiaci(3)
     mixtot(i)=mixang(1)       !Mixing angle from total overlap (including first-order correction)
     h11(i)=hdia(1)            !Diabatic energies obtained from total overlap
     h21(i)=hdia(2)
     h22(i)=hdia(3)
   end if
   
   mix(j)=mixang(1)            !Store mixing angles for R2+DR(j)
   
   enddo                       !End loop over j
   
   dchi(i)=(mix(3)-mix(2))/(dr(2)-dr(3))*pi/180  !Finite difference derivative of mixing angle
   
   {ddr
   density,7201.2,7202.2,7203.2   !Compute NACME using 3-point formula
   orbital,3141.2,3142.2,3143.2
   states,2.2,1.2}
   nacmeci(i)=nacme
   
   {table,r,mixci,mixtot,dchi,nacmeci
   Title,Mixing angles and non-adiabatic coupling matrix elements for H2S
   format,'(f10.2,4f14.4)'
   sort,1
   }
   
   {table,r,e1,e2,h11ci,h22ci,h21ci
   Title,Diabatic energies for H2S, obtained from CI-vectors
   format,'(f10.2,5f16.8)'
   sort,1}
   
   {table,r,e1,e2,h11,h22,h21
   title,Diabatic energies for H2S, obtained from CI-vectors and orbital correction
   format,'(f10.2,5f16.8)'
   sort,1}
   
   enddo

The calculation produces the following table

.. code-block:: text

    Mixing angles and non-adiabatic coupling matrix elements for H2S
   
           R          MIXCI        MIXTOT          DCHI       NACMECI
         2.55       15.2694       15.2644       -5.2226       -5.2365
         2.60       27.8740       27.8772       -3.4702       -3.4794
   
    Diabatic energies for H2S, obtained from CI-vectors
   
           R       E1            E2            H11CI         H22CI         H21CI
         2.55 -398.64572746 -398.63666636 -398.64509901 -398.63729481   -0.00230207
         2.60 -398.64911752 -398.63771802 -398.64662578 -398.64020976   -0.00471125
   
    Diabatic energies for H2S, obtained from CI-vectors and orbital correction
   
           R       E1            E2            H11           H22           H21
         2.55 -398.64572746 -398.63666636 -398.64509941 -398.63729441   -0.00230139
         2.60 -398.64911752 -398.63771802 -398.64662526 -398.64021027   -0.00471160

As expected the coupling matrix elements obtained from the 3-point ``DDR`` calculation (NACMECI) and by differentiating the mixing angle (DCHI) are in close agreement.
