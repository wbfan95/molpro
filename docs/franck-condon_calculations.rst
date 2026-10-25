.. raw:: html

   <span id="electronic-vibrational-spectra-evspec"></span>

.. raw:: html

   <span id="franck-condon-factors-fcon"></span>

.. _franck-condon_calculations--franck-condon-calculations:

Franck-Condon calculations
==========================

.. _franck-condon_calculations--franck-condon-factors-fcon:

FRANCK-CONDON FACTORS (FCON)
============================

``FCON,options [fcon]``

The ``FCON`` program allows for the calculation of Franck-Condon factors based on potential energy surfaces obtained from the ``XSURF`` program and vibrational wavefunctions as provided by the ``VSCF`` or ``VCI`` programs. Duschinsky effects may or may not be included. These can either be applied to the vibrational wavefunction (of the vibrational ground state) or the potential by using the ``PESTRANS`` program. The latter possibility is the recommended one as it is significantly faster. The ``FCON`` program including Duschinsky rotations can only be used with analytical representations of the potential energy surfaces. A prescreening of the Franck-Condon factors without Duschinsky effects at the ``VSCF`` level is used to reduce the computational effort for correlated levels, e.g. ``VCI``. Note that, Franck-Condon factors at the uncorrelated ``VSCF`` level including Duschinsky effects are usually of fairly poor quality. As the calculation of Franck-Condon factors often involves very high quantum numbers for the vibrational states of the final electronic state, very high excitation levels must be enabled in the ``VCI`` calculations, i.e. see keyword ``LEVEX``. For details see:
P. Meier, G. Rauhut, *Comparison of methods for calculating Franck-Condon factors beyond the harmonic approximation: how important are Duschinsky rotations?*, `Mol. Phys. <https://dx.doi.org/10.1080/00268976.2015.1074740>`__ **113**, 3859 (2015).
G. Rauhut, *Anharmonic Franck-Condon factors for the :math:`\tilde{\mbox{X}}\,{}^2`B:math:`{}_1 \longleftarrow \tilde{\mbox{X}}\,{}^1`A:math:`{}_1` photoionization of ketene*, J. Phys. Chem. A **119**, (2015) 10264.

.. _franck-condon_calculations--options:

Options
=======

The following *options* are available:

* **``DUSCH``\ =\ *n*** This keyword controls the Duschinsky transformation. ``DUSCH=0`` entirely neglects the Duschinsky transformation - including the shift-vector. ``DUSCH=3`` neglects the Duschinsky rotation, but includes the shift-vector. This is the default option as the Duschinsky rotation can be passed to the ``PESTRANS`` program, which is much more efficient.
* **``ECKART``\ =\ *n*** ``ECKART=1`` (default) determines the Eckart transformation matrix as described in the literature. ``ECKART=0`` approximates the Eckart transformation matrix by a unit matrix, which is meaningless unless for debugging purposes or for some very special tests.
* **``MAXSEL``\ =\ *n*** ``MAXSEL=n`` determines the maximum number of Franck-Condon factors to be selected. By default *n* is set to 100.
* **``SEL``\ =\ *n*** This option switches the selection of Franck-Condon factors based on VSCF calculation on (``SEL=1``) or off (``SEL=0``, default).
* **``THRDELTA``\ =\ *value*** The :math:`\delta`-criterion is a threshold, which allows for the prescreening of overlap integrals within the evaluation of the Franck-Condon factors prior to their evaluation. The default is set to 1.0d-8.
* **``THRFCF``\ =\ *value*** The sum of all Franck-Condon factors is 1.0d0 by definition. However, this value is hard to reach by sum over states approaches. Therefore, it can be lowered by this keyword.
* **``THRFCFSPEC``\ =\ *value*** This threshold controls, if a Franck-Condon factor will be considered within the plotting of the spectrum. See the ``PUT`` command and the ``IRSPEC`` style. The default is 1.0d-6.
* **``THRPRINT``\ =\ *value*** This keyword defines the smallest value of a Franck-Condon factor to be printed in the output. The default is set to 1.0d-99, i.e. this threshold usually is inactive.
* **``THRSEL``\ =\ *value*** This threshold controls, if a Franck-Condon factor shall be selected and thus be considered in all subsequent calculations or not. The default is 1.0d-5.
* **``THRSKIPBAS``\ =\ *value*** Basis functions in the outer regions of the potentials may be skipped within the calculation of Franck-Condon factors. In particular within the approach of Doktorov, the CPU time depends strongly on the number of basis functions. This keyword allows to skip such basis functions and is given as the overlap integral of the modal. The default is 0.999999d0.
* **``THRSUMSEL``\ =\ *value*** This threshold controls the sum of the selected Franck-Condon factors, which must formally be 1.0d0. The default is set to 0.999999d0.
* **``THRVCIMIN``\ =\ *value*** Within the calculation of Franck-Condon factors based on VCI wavefunctions, the leading VCI coefficient should be largest in order to correspond to the state of interest. The default is set to 0.01d0, which of course means that this keyword essentially is inactive.
* **``WF``\ =\ *type*** Defines the type of the wavefunction. ``WF=VSCF`` specifies state-specific ``VSCF`` wavefunctions for both levels, while ``WF=VCI`` denotes state-specific ``VCI`` wavefunctions. Alternatively, one may use ``WF=VSCFG`` for ground-state based VSCF wavefunctions and ``WF=VCIG`` for ground-state based VCI wavefunctions. The default is ``WF=VCI``.

Some of the keywords as described for the ``VCI`` program are also valid for the ``FCON`` program, i.e. ``CITYPE, LEVEX, CIMAX, NDIM, NBAS, BASIS`` and ``INFO``.

.. _franck-condon_calculations--information-handling:

Information Handling
====================

``DISK,options\\``
As the Franck-Condon program requests the information of two sets of potentials and wave functions, the information handling is controlled by an extra directive. All the records provided here must refer to the defaults or the explicitly given records in the preceding ``POLY``, ``VSCF`` and ``VCI`` calculations.

* **``FINAL``\ =\ *n*** Rather than specifying the records explicitly, the number of the final state as defined in ``DISK`` directive of the ``POLY`` program may be used.
* **``INITIAL``\ =\ *n*** Rather than specifying the records explicitly, the number of the initial state as defined in ``DISK`` directive of the ``POLY`` program may be used.
* **``SURF1``\ =\ *record*** Specifies the record from where to read the potential information for the final PES.
* **``SURF2``\ =\ *record*** Specifies the record from where to read the potential information for the initial PES.
* **``VSCF1``\ =\ *record*** Specifies the record from where to read the VSCF information for the final wave function.
* **``VSCF2``\ =\ *record*** Specifies the record from where to read the VSCF information for the initial wave function.
* **``VCI1``\ =\ *record*** Specifies the record from where to read the VCI information for the final wave function.
* **``VCI2``\ =\ *record*** Specifies the record from where to read the VCI information for the initial wave function.

.. _franck-condon_calculations--example-1:

Example 1
=========

The following example shows the input for a calculation of Franck-Condon factors at the VCI level. The selection of important Franck-Condon factors will be done at the VSCF level without Duschinsky rotation.

.. code-block:: text

   memory,20,m
   basis=vdz
   orient,mass
   geometry={
      3
   Water
   O          0.0675762564        0.0000000000       -1.3259214590
   H         -0.4362118830       -0.7612267436       -1.7014971211
   H         -0.4362118830        0.7612267436       -1.7014971211
   }
   
   label1
   hf
   
   {xsurf,sym=auto                    ! read in the PES of the initial electronic state and assign it to surface label 1
    disk,where=home,auto=1,extern='final.pot'}
       
   {poly
    disk,auto=1}                      ! read surface 1 from disk and transform it to polynomials
   {vscf,pot=poly                     
    disk,auto=1}                      ! read polynomials for surface 1 from disk and perform a VSCF calculation 
       
   {xsurf,sym=auto                    ! read in the PES of the final electronic state and assign it to surface label 2
     disk,where=home,auto=2,extern='initial.pot'}       
       
   {poly
    disk,auto=2}                      ! read surface 2 from disk and transform it to polynomials
   {vscf,pot=poly
    disk,auto=2}                      ! read polynomials for surface 2 from disk and perform a VSCF calculation
    
   {fcon,wf=vscfg,sel=1               ! perform a Franck-Condon calculation at the VSCF level in order to
    disk,initial=2,final=1}           ! identify important transitions, which shall be considered later in the VCI part
    
   {poly,vam=0                        ! transform PES 2 to polynomials without adding the Watson correction term
    disk,auto=2}                      ! as a pseudopotential to (this is needed for the subsequent transformation)
    
   {pestrans,transtype=fcf,umat=1     ! transform PES 2 (initial) to the axes (normal coordinates) of PES 1 (final state)
    disk,where=home,auto=2            ! (Duschinsky transformation)
    disk,extern='initial.pot'}                  
                                            
   {poly                              ! transform the transformed PES to polynomials       
    disk,auto=2}
   {vscf,pot=poly                     ! do a VSCF calculation for surface 2
    disk,auto=2}                           
   {vci,pot=poly,export=fcon          ! perform a VCI calculation for surface 2 and export the VCI vectors for     
    disk,auto=2}                      ! the Franck-Condon program     
                                            
   {poly                              ! transform surface 1 to polynomials   
    disk,auto=1}                           
   {vscf,pot=poly                     ! perform a VSCF calculation for surface 1              
    disk,auto=1}                             
   {vci,pot=poly,export=fcon          ! perform a VCI calculation for surface 1 and export the VCI vectors for 
    disk,auto=1}                      ! the Franck-Condon program
    
   {fcon                              ! perform a Franck-Condon calculation on the basis of the selected VCI states
    disk,initial=2,final=1}
   
   put,irspec,h2o_pe.gnu              ! generate a GNU file with the PE spectrum

<!--

.. _franck-condon_calculations--example-2:

Example 2
=========

This alternative example shows the use of the ``AUTO`` cards, which may be used to control the correct order of the records. It avoids the explicit use of record numbers.

.. code-block:: text

   !options: --logfile-scratch
   memory,100,m
   orient,mass;
   geometry={
       5
    UCCSD(T)-F12A/VTZ-F12  ENERGY=-152.07488677
   C          0.0000000000        0.0000000000       -0.0682760315
   C          0.0000000000        0.0000000000        1.3222851825
   O          0.0000000000        0.0000000000       -1.1931542345
   H          0.0000000000        0.9578360683        1.8313436280
   H          0.0000000000       -0.9578360683        1.8313436280
   }
   
   mass,iso
   
   basis=vdz
   {rhf;accu,14;start,atden}
   ccsd(t)-f12a
   optg
   freq,symm=auto
   
   basis=vtz-f12
   {rhf;accu,14;start,atden}
   ccsd(t)-f12a,freeze_save=1891.2
   
   basis=vdz-f12
   {rhf;accu,14;start,atden}
   ccsd(t)-f12a,freeze_save=1892.2
   
   label1
   basis=vtz-f12
   {rhf;start,atden}
   {ccsd(t)-f12a,freeze_start=1891.2}
   goto,label4
   
   label2
   basis=vdz-f12
   {rhf;start,atden}
   {ccsd(t)-f12a,freeze_start=1892.2}
   
   label4
   {surf,start1D=label1,info=1,ndim=3
    scalnm,auto=on,show=1
    vmult,start2D=label1,start3D=label2,multi=4
    disk,where=home,extern='keten_final.pot'}
   
   {poly,dipole=0,info=1
    disk,auto=1}
   {vscf,type=poly,dipole=0,info=1
    disk,auto=1}
   
   {surf,start1D=label1,info=1,ndim=3
    scalnm,auto=on,show=1
    vmult,start2D=label1,start3D=label2,multi=4
    disk,where=home,extern='keten_initial.pot'}
   
   {poly,dipole=0,info=1
    disk,auto=2}
   {vscf,type=poly,dipole=0,info=1,usermode=2
    disk,auto=2}
   
   {fcon,wf=vscfg,sel=1,thrsel=1.0d-6,maxsel=1000,dipole=0
    disk,initial=2,final=1}
   
   {poly,dipole=0,info=1,vam=0
    disk,auto=2}
   {pestrans,scale=0.7,info=1
     scalnm,auto=on,show=1
     disk,where=home,extern='keten_final.pot'}
   
   {poly,dipole=0,info=1
    disk,auto=2}
   {vscf,type=poly,dipole=0,info=1,usermode=2
    disk,auto=2}
   {vci,type=poly,version=3,export=fcon,dipole=0,info=1,usermode=2
    disk,auto=2}
   
   {surf,start1D=label1,info=1,ndim=3
    scalnm,auto=on,show=1
    vmult,start2D=label1,start3D=label2,multi=4
    disk,where=home,extern='keten_final.pot'}
   
   {poly,dipole=0,info=1
    disk,auto=1}
   {vscf,type=poly,usermode=1,dipole=0,info=1
    disk,auto=1}
   {vci,type=poly,version=3,export=fcon,usermode=1,dipole=0,info=1
    disk,auto=1}
   
   {fcon,dipole=0
    disk,initial=2,final=1}
   
   put,irspec,keten-fcon.gnu

-->

.. _franck-condon_calculations--electronic-vibrational-spectra-evspec:

ELECTRONIC-VIBRATIONAL SPECTRA (EVSPEC)
---------------------------------------

``EVSPEC,options [evspec]``

Similar to the ``FCON``, the ``EVSPEC`` program allows for the calculation of anharmonic electronic-vibrational absorption spectra with the inclusion of Duschinsky effects. In addition, it can take finite-temperature effects into account as arising from the thermal population of the excited vibrational levels of the electronic ground PES. The program requires a precalculated set of initial VCI wavefuncions, a polynomial representation of the final PES, and the corresponding VSCF ground-state modals. In addition, the initial VCI states should be provided in the same set of normal coordinates as the final PES, which is achieved by the coordinate transformation of the potential energy function via the ``PESTRANS`` program. All these aspect will be illustrated in the examples below.

There are basically two approaches employed in this module. The first one consists in the determination of the eigenstates with the largest Franck-Condon factors within the formalism of contracted invariant Krylov subspaces (CIKS) by means of the Lanczos or RACE methods. Alternatively, the spectra can be evaluated using the time-independent eigenstate-free ansatz based on the inhomogeneous Schrödinger equation. The solution of this equation, the so-called Raman wavefunction (RWF), is directly related to the spectral intensities. For details see:
T. Petrenko, G. Rauhut, *Time-independent eigenstate-free calculation of vibronic spectra beyond the harmonic approximation* , `J. Chem. Phys. <https://dx.doi.org/10.1063/1.4937380>`__ **143**, 234106 (2015).
T. Petrenko, G. Rauhut, *A new efficient method for the calculation of interior eigenpairs and its application to vibrational structure problems* , `J. Chem. Phys. <https://dx.doi.org/10.1063/1.4978581>`__ **146**, 124101 (2017).
T. Petrenko, G. Rauhut, *A general approach for calculating strongly anharmonic vibronic spectra with a high density of states: the :math:`\tilde{\mbox{X}}\,{}^2`B:math:`{}_1 \longleftarrow \tilde{\mbox{X}}\,{}^1`A:math:`{}_1` photoelectron spectrum of difluoromethane*, `J. Chem. Theory Comput. <https://dx.doi.org/10.1021/acs.jctc.7b00468>`__ **13**, 5515 (2017).
T. Petrenko, G. Rauhut, *Refined analysis of the :math:`\tilde{\mbox{X}}\,{}^2`A:math:`{}_2 \longleftarrow \tilde{\mbox{X}}\,{}^1`A:math:`{}_1` photoelectron spectrum of furan* , `J. Chem. Phys. <https://dx.doi.org/10.1063/1.5018928>`__ **148**, 054306 (2018).

.. _franck-condon_calculations--options-1:

Options
=======

The following *options* are available:

* ``METHOD=CIKS|RWF`` Defines the method of calculation. ``METHOD=CIKS`` specifies the CIKS approach which enables the determination of the eigenstates with the most significant Franck-Condon factors. ``METHOD=RWF`` denotes the eigenstate-free method based on the Raman wavefunction formalism.

``Default: METHOD=RWF.``

* **``INITIAL``\ =\ *n1*, ``FINAL``\ =\ *n2***   

These keywords provide the reference values for the initial and final PESs, respectively. In this case, the option ``AUTO``\ =\ *n1* within the ``DISK`` directive of the ``POLY``, ``VSCF``, or ``VCI`` blocks would attribute the respective computational results to the *initial* PES, while ``AUTO``\ =\ *n2* would attribute them to the *final* PES.
``Default: INITIAL=1, FINAL=2.``

The keyword ``INFO`` has the same meaning as in the other programs.

.. _franck-condon_calculations--handling-of-initial-states:

Handling of Initial States
==========================

``ISTATES,options\\``
For a given temperature, the program can calculate the spectrum with the contributions from all initial states which are found in the VCI record. This directive provides the opportunity to control the prescreening of the initial states based on their relative thermal populations. The following options are possible:

* **``TEMPK``\ =\ *value*** Provides the temperature in Kelvin.

``Default: TEMPK=300.0.``

* **``THRPOP``\ =\ *value*** The initial states with the relative thermal populations (with respect to the ground vibrational level) which are below this parameter will be neglected.

``Default: THRPOP=1.0d-3.``

.. _franck-condon_calculations--rwf-calculations:

RWF calculations
================

``RWF,options\\``
This directive provides various computational settings which are specific to the RWF calculations. Currently, only the iterative subspace algorithm of Lanczos type is implemented. The following options are possible:

* **``ERANGE``\ =\ *value1,value2*** Defines the spectral range in 1/cm unit for the RWF calculation relative to the 0-0 transition energy. In the case that the eV unit is implied, see the explanation for the keyword ``EUNIT``.

Default: automatic determination of the spectral range with significant intensity.

* ``EUNIT=CM|EV`` Defines the energy unit for the values specified via the keywords ``ERANGE`` and ``GAMMA``. ``CM`` and ``EV`` stand for 1/cm and eV, respectively.

``Default: EUNIT=CM.``

* **``GAMMA``\ =\ *value*** Defines the damping factor in 1/cm unit. In the case that the eV unit is implied, see the explanation for the keyword ``EUNIT``.

``Default: GAMMA=100.0.``

* **``NLMAX``\ =\ *n*** Defines the maximum number of Lanczos iterations.

``Default: NLMAX=2000.``

* **``NSMAX``\ =\ *n*** Defines the maximum number of printed approximate eigenstates representing the RWF.

``Default: NSMAX=2000.``

* **``THRCONV``\ =\ *value*** Defines the convergence threshold for the RWF in terms of the dimensionless squared residual norm for the inhomogeneous Schrödinger equation.

``Default: THRCONV=1.0d-3.``

* **``THRFCF``\ =\ *value*** This is the threshold for the sum of the FCFs which controls the number of printed approximate eigenstates representing the RWF.

``Default: THRFCF=0.999.``

.. _franck-condon_calculations--ciks-calculations:

CIKS calculations
=================

``CIKS,options\\``
This directive provides the computational settings that are specific to the CIKS calculations. The following options are possible:

* ``METHOD=LCS|RACE`` Defines the method of calculation. Currently, two choices are possible: Lanczos (``LCS``) and RACE (``RACE``) algorithms.

``Default: METHOD=RACE.``

* **``NDMAX``\ =\ *n*** Defines the maximum number of the state-specific expansion vectors. It is valid only for ``METHOD=RACE``.

``Default: NDMAX=1000.``

* **``NEVMAX``\ =\ *n*** Defines the maximum number of the eigenvectors to be calculated in one batch (``NEVMAX``\ :math:`\leq`\ ``NSMAX``).

Default: ``NEVMAX=20`` for the RACE method, and ``NEVMAX=NLMAX`` for the Lanczos one.

* **``NLMAX``\ =\ *n*** Defines the maximum number of Lanczos iterations.

Default: ``NLMAX=2000`` for the Lanczos method, and ``NLMAX=300`` for the RACE one.

* **``NSMAX``\ =\ *n*** Defines the maximum number of the eigenstates to be calculated. The same number of states will be printed out.

Default: ``NSMAX=100`` for the RACE method, and ``NSMAX=NLMAX`` for the Lanczos one.

* **``THREN``\ =\ *value*** Defines the convergence threshold for the calculated eigenstates in terms of the residual norm in Hartree unit.

``Default: THREN=1.0d-7.``

* **``THRFCF``\ =\ *value*** This is the threshold for the sum of the FCFs which additionally controls the total number of the calculated and printed eigenstates.

``Default: THRFCF=0.999.``

.. _franck-condon_calculations--vibrational-configuration-basis:

Vibrational configuration basis
===============================

``VCIBASIS,options\\``
This directive controls the choice of the vibrational configuration basis. The following options are possible:

* **``REFTYPE``\ =\ *n*** Controls the selection of the reference configuration involved in the generation of the VCI basis. ``REFTYPE=1`` refers to the ground vibrational configuration. The other choices are based on the calculated modal-contracted Franck-Condon factors (MCFCFs). For ``REFTYPE=2``, the modals with the largest MCFCF is selected for the respective components of the reference vector, while for ``REFTYPE=3``, one takes the modal which approximately corresponds to the average of the MCFCF distribution over the modals.

``Default: REFTYPE=3.``

The keywords ``CITYPE``, ``LEVEX``, and ``CIMAX`` restrict the VCI basis to certain excitation patterns, and have the same meaning as in the other modules:

* **``CIMAX``\ =\ *n*** Defines the maximum total excitation level over all modes.

``Default: CIMAX=6.``

* **``CITYPE``\ =\ *n*** Defines the maximum number of simultaneously excited modes relative to the reference configuration.

``Default: CITYPE=4.``

* **``LEVEX``\ =\ *n*** Defines the maximum excitation level within a single mode.

``Default: LEVEX=4.``

.. _franck-condon_calculations--vibrational-interaction-matrix:

Vibrational interaction matrix
==============================

``HMAT,options\\``
This directive controls the construction of the VCI Hamiltonian matrix. The following options are possible:

* **``THRSPARSE``\ =\ *value*** Defines the threshold for neglecting the off-diagonal elements in the Hamiltonian matrix stored in a packed sparse form. The smaller is this value the higher are the memory demands, and the computational cost of the matrix-vector multiplications. In particular, setting ``THRSPARSE=0.0`` would not lead to any meaningful changes in the calculated transition energies and intensities, but can easily increase the memory demands by :math:`\sim 10-10000` times as compared to the default value.

``Default: THRSPARSE=1.0d-6.``

.. _franck-condon_calculations--interface-to-gnuplot:

Interface to Gnuplot
====================

``GRAPH,options\\``
This directive controls the output of the calculated spectra for plotting with the ``GNUPLOT`` program. Thus far, a single option is available:

* **``EVSDUMP``\ =\ *file name*** Provides the name of the gnuplot input file.

``Default: EVSDUMP=’InputFileName.evs.gnu’.``

.. _franck-condon_calculations--example:

Example
-------

The following example shows a general program flow involving the ``EVSPEC`` calculations.

.. code-block:: text

   memory,40,m
   
   basis=vdz
   geometry={
   H   ,,     2.3971901752  ,    -2.3962403391   ,    0.0000000000
   S   ,,    -0.0873406755  ,    -1.8178592700   ,    0.0000000000
   S   ,,     0.0117763411  ,     1.8933936636   ,    0.0000000000
   }
   
   basis=vdz
   hf
   
   {xsurf                                            ! reads the PES of the initial electronic
    disk,where=home,extern='initial.pot'}            ! state from 'initial.pot'
   
   poly                                              ! Transform  the initial PES to the
   vscf,pot=poly                                     ! representation in terms of the normal
   vci,pot=poly                                      ! coordinates of the final PES
                                                     ! (stored in 'final.pot'), and fit it
   {pestrans,info=1                                  ! with polynomial functions.
    disk,where=home,auto=1,extern='final.pot'}       ! All results for the initial surface
                                                     ! are stored with the reference number
   {poly                                             ! given by the keyword auto=1.
    disk,auto=1}
   {vscf,pot=poly                                    ! Run VSCF calculations for initial states.
    disk,auto=1}                                     
   {vci,pot=poly,export='EVSPEC'                     ! Run VCI calculations for initial states.
    disk,auto=1}
   
   {xsurf                                            ! Reads the PES of the final electronic
    disk,where=home,auto=2,extern='final.pot'}       ! state from 'final.pot'.
   
   {poly                                             ! Provides the polynomial representation
    disk,auto=2}                                     ! of the final PES.
   {vscf,pot=poly                                    ! Run VSCF calculations for generating
    disk,auto=2}                                     ! vibrational modals for the final PES.
   
   {evspec,method=rwf,start=1,final=2,info=1         ! Simple input for the RWF calculation
   graph, evsdump='hs2_rwf.gnu'}

<!--

.. code-block:: text

   memory,20,m
   basis=vdz
   orient,mass
   geometry={
      3
   Water
   O          0.0675762564        0.0000000000       -1.3259214590
   H         -0.4362118830       -0.7612267436       -1.7014971211
   H         -0.4362118830        0.7612267436       -1.7014971211
   }
   
   label1
   int
   {hf
    start,atden}
   
   {surf,start1D=label1,sym=auto           ! reads the PES of the initial electronic
    disk,where=home,extern='initial.pot'   ! state from 'initial.pot'
    disk,save=5600.2
   }
   
   {poly                                   ! Transform  the initial PES to the
    disk, auto=1}                          ! representationin terms of the normal
   {pestrans                               ! coordinates of the final PES
    disk,where=home,save=5600.2            ! (stored in 'final.pot'), and fit it
    disk,extern='final.pot'}               ! with polynomial functions.
   {poly                                   ! All results for the initial surface
    disk, auto=1}                          ! are stored with the reference number
                                           ! given by the keyword auto=1.
   
   !  NOTE THAT AUTO=1 CAN ONLY REFER TO THE PES STORED IN THE RECORD 5600.2
   !  (KEYWORD SAVE=5600.2 FOR THE SURF AND PESTRANS PROGRAMS), WHILE  AUTO=2
   !  IMPLIES THAT THE PES STORED IN THE RECORD 5601.2 (SAVE=5601.2).
   !  ACCORDINGLY, ONE SHOULD ALSO ADJUST THE VALUE OF THE KEYWORD SAVE
   !  IN THE RESPECTIVE .POT FILE.
   
   
   {vscf,type=poly,ibx=0,bsf=4.0           ! Run VSCF calculations
    disk,auto=1}                           ! for initial states.
   
   ! For avoiding  artifacts in the EVSPEC calculations,
   ! it is advisable to control the quality of
   ! the modal basis functions by the keywords IBX and BSF.
   ! The keyword IBX=0 disables the shift of the gaussian basis functions
   ! related to the shift of the respective grid points.
   ! The keyword BSF=4.0 provides  the minimum extension of the basis
   ! functions over the PES.
   
   {vci,type=poly,gsmodals=1               ! Run VCI calculations
    disk,auto=1}                           ! for initial states.
                                           ! It is important to use the
                                           ! ground-states modals (gsmodals=1).
   
   ! It is advisable to combine the VSCF and VCI calculations with the
   ! VIBSTATE program  for explicit specification of all relevant initial states
   
   
   {surf,start1D=label1,sym=auto           ! Reads the PES of the final electronic
    disk,where=home,extern='final.pot'     ! state from 'final.pot'.
    disk,save=5601.2
   }
   {poly                                   ! Provides the polynomial representation
    disk, auto=2}                          ! of the final PES.
   {vscf,ibx=0,bsf=4.0                     ! Run VSCF calculations for generating
    disk, auto=2}                          ! vibrational modals for the final PES.
   
   
   evspec,method=rwf,start=1,final=2       ! Simple input for the RWF calculation
   
   {evspec,method=rwf,start=1,final=2      ! A more detailed specification of
   hmat,thrsparse= 1.0d-8                  ! the RWF calculation
   rwf,thrconv=2.0d-4
   rwf,gamma=2,erange=-500,6000
   vcibasis,levex=8,maxci=8,citype=3
   vcibasis,reftype=3
   istates,tempk=255,thrpop=1.0d-3
   graph, evsdump='graph.gnu'}
   
   evspec,method=ciks,start=1,final=2       ! Simple input for the CIKS calculation
   
   {evspec,method=ciks,start=1,final=2      ! A more detailed specification of
   hmat,thrsparse= 1.0d-8                   ! the CIKS calculation
   ciks,method=race,thrfcf=0.99,nsmax=10
   vcibasis,levex=8,maxci=8,citype=3
   vcibasis,reftype=3
   istates,tempk=255,thrpop=1.0d-3
   graph, evsdump='graph.gnu'}
   
   

-->
