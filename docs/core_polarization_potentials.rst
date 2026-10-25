.. _core_polarization_potentials--core-polarization-potentials:

Core polarization potentials
============================

.. _core_polarization_potentials--input-options:

Input options
=============

The calculation of core-polarization matrix elements is invoked by the CPP card, which can be called at an arbitrary position in the MOLPRO input, provided the usual AO integrals have been calculated before. The CPP card can have the following formats:

* CPP,INIT,\ *ncentres*;
* CPP,ADD[,\ *factor*];
* CPP,AE[,\ *record.file*];
* CPP,SET[,\ *fcpp*];

CPP,INIT,\ :math:`<ncentres>`;

abs(:math:`<ncentres>`) further cards will be read in the following format:

:math:`<atomtype>,<ntype>,<\alpha_d>,<\alpha_q>,<\beta_d>,<cutoff>,<q_{eff}`;

:math:`<atomtype>` specifies an atomic centre with polarizable core,
:math:`<ntype>` fixes the form of the cutoff-function (choose 1 for Fuentealba/Stoll and 2 for Mueller/Meyer);
:math:`<\alpha_d>` is the static dipole polarizability,
:math:`<\alpha_q>` is the static quadrupole polarizability,
:math:`<\beta_d>` is the first non-adiabatic correction to the dipole polarizability,
:math:`<cutoff>` is the exponential parameter of the cutoff-function, and
:math:`<q_{eff}` is the effective charge of the core with which it polarizes its surroundings (only needed if it contributes orbitals to the CPP core (see below)).
When :math:`<ncentres>` is lower than zero, only CPP integrals are calculated and saved in record 1490.1. Otherwise, the :math:`h_0` matrix (records 1200.1 and 1210.1) and the two-electron-integrals (record 1300.1) will be modified.

CPP,ADD,\ :math:`<factor>`;

With this variant, previously calculated matrix elements of the polarization matrix can be added with the variable factor :math:`<factor>` (default: :math:`<factor>` = 1) to the :math:`h_0`-matrix as well as to the two-electron integrals. In particular, CPP,ADD,-1.; can be used to retrieve the integrals without the polarization contribution.

CPP,AE,\ :math:`<record.file>`;

This is equivalent to the CPP,ADD command (with factor 1), but additionally sets a flag that CPP integrals projected with respect to core orbitals should be used. The projection is necessary whenever explicitly treated polarizable cores are present. The core orbitals are taken from *record.file*, and the CPP,AE command should be followed by a *core* card specifying the numbers of these orbitals in the various irreducible representations. Currently, the code assumes that the polarizable cores are spherically symmetric.

CPP,SET,\ :math:`<fcpp>`;

normally not necessary but may be used to tell MOLPRO after a restart, with what factor the polarization integrals are effective at the moment. Currently the CPP integrals are restricted to basis functions up to and including angular momentum 4, i.e. g functions.

.. _core_polarization_potentials--example-for-ecp-cpp:

Example for ECP/CPP
===================

.. code-block:: text
   :caption: examples/na2_ecp_cpp.inp

   ***,Na2
   ! Potential curve of the Na2 molecule
   ! using 1-ve ECP + CPP
   gprint,basis,orbitals;
   rvec=[2.9,3.0,3.1,3.2,3.3] ang
   do i=1,#rvec
   rNa2=rvec(i)
   geometry={na;na,na,rNa2}
   basis={
   ecp,na,ecp10sdf;        ! ecp input
   s,na,even,8,3,.5;       ! basis input
   p,na,even,6,3,.2;
   d,na,.12,.03;
   }
   cpp,init,1;             ! CPP input
   na,1,.9947,,,.62;
   hf;
   ehf(i)=energy
   {cisd;core;}
   eci(i)=energy
   enddo
   table,rvec,ehf,eci
   ---

.. _core_polarization_potentials--example-for-use-of-cpp-in-all-electron-calculations:

Example for use of CPP in all-electron calculations
===================================================

.. code-block:: text
   :caption: examples/p2_cpp.inp

   ***, P_2: All-electron calculation with polarizable P(+5) cores; calculation of the potential curve
   
   print,basis,orbital;
   
   basis=vtz
   
   dist = [2000.,1.84,1.86,1.88,1.90,1.92,1.94,1.96] ang
   do ii=1,#dist
   
   geometry={P1;P2,P1,dist(ii)}
   
   if (ii.eq.1) then
   !calculation of free atoms at large distance
   !the resulting cores are kept frozen in subsequent calculations
   {rhf;closed,4,1,1,,4,1,1;wf,spin=6;save,2101.2}
   e_scf(1)=energy
   e_scf_cpp(1)=0
   E_CCSDT_CPP(1)=0
   
   else
   
   
   !symmetric orthogonalization of the cores for current distance
   int
   {merge,2102.2;orbital,2101.2;move;orth,3,1,1,,3,1,1;}
   
   !calculation without CPP
   {multi;occ,5,2,2,,4,1,1;frozen,3,1,1,,3,1,1,2102.2;start,2102.2;wf,30,1,0;canorb,2140.2;}
   e_scf(ii)=energy
   
   !calculating CPP integrals
   cpp,init,-1;P,1,0.1057,,,1.6132,5;
   
   !projecting CPP integrals onto valence space
   {cpp,ae,2102.2;core,3,1,1,,3,1,1;}
   
   !following calculations are done with CPP; core must be frozen
   {multi;occ,5,2,2,,4,1,1;frozen,3,1,1,,3,1,1,2102.2;start,2140.2;wf,30,1,0;canorb,2141.2;}
   e_scf_cpp(ii)=energy
   
   {ccsd(t);occ,5,2,2,,4,1,1;core,3,1,1,,3,1,1;orbital,2141.2;}
   e_ccsdt_cpp(ii)=energy
   endif
   
   table,dist,e_scf,e_scf_cpp,e_ccsdt_cpp
   enddo
   ---
