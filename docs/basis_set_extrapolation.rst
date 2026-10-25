.. raw:: html

   <span id="basis-set-incompleteness-error-correction-using-a-dft-model-of-short-ranged-electron-interactions"></span>

.. raw:: html

   <span id="extrapolation-functionals"></span>

.. _basis_set_extrapolation--basis-set-extrapolation:

Basis set extrapolation
=======================

Basis set extrapolation can be carried out for correlation consistent basis sets using

``EXTRAPOLATE,BASIS=basislist,options``

where basislist is a list of at least two basis sets separated by colons, e.g. AVTZ:AVQZ:AV5Z. Some extrapolation types need three or more basis sets, others only two. The default is to use :math:`n^{-3}` extrapolation of the correlation energies, and in this case two subsequent basis sets and the corresponding energies are needed. The default is not to extrapolate the reference (HF) energies; the value obtained with the largest basis set is taken as reference energy for the CBS estimate. However, extrapolation of the reference is also possible by specifying the ``METHOD_R`` option.

The simplest way to perform extrapolations for standard methods like MP2 or CCSD(T) is to use, e.g.

.. code-block:: text

   ***,H2O
   memory,32,m
   gthresh,energy=1.d-8
   
   r =   0.9572 ang, theta =  104.52
   geometry={O;
             H1,O,r;
             H2,O,r,H1,theta}
   
   basis=avtz
   hf
   ccsd(t)
   extrapolate,basis=avqz:av5z
   
   table,basissets,energr,energy-energr,energy
   head,basis,ehf,ecorr,etot

This will perform the first calculation with AVTZ basis, and then compute the estimated basis set limit using the AVQZ and AV5Z basis sets. The correlation energy obtained in the calculation that is performed immediately before the extrapolate command will be extrapolated (in this case the CCSD(T) energy), and the necessary sequence of calculations [here HF;CCSD(T)] will be automatically carried out.

The resulting energies are returned in variables ENERGR (reference energies), ENERGY (total energies), and ENERGD (Davidson corrected energy if available); the corresponding basis sets are returned in variable BASISSETS. The results can be printed, e.g., in a table as shown above, or used otherwise. The above input produces the table

.. code-block:: text

    BASIS       EHF           ECORR          ETOT
    AVQZ    -76.06600082   -0.29758099   -76.36358181
    AV5Z    -76.06732050   -0.30297495   -76.37029545
    CBS     -76.06732050   -0.30863418   -76.37595468

The extrapolated total energy is also returned in variable ECBS (ECBSD for Davidson corrected energy if available).

In order to extrapolate the HF energy as well (using exponential extrapolation), three energies are needed. One can modify the input as follows:

``extrapolate,basis=avtz:avqz:av5z,method_r=ex1,npc=2``

``method_r determines the method for extrapolating the reference energy (in this case a single exponential); npc=2 means that only the last two energies should be used to extrapolate the correlation energy (by default, a least square fit to all given energies is used). This yields``

.. code-block:: text

    BASIS           EREF            ECORR           ETOT
    AVTZ        -76.06061330     -0.28167606    -76.34228936
    AVQZ        -76.06600082     -0.29758099    -76.36358180
    AV5Z        -76.06732050     -0.30297495    -76.37029545
    CBS         -76.06774863     -0.30863419    -76.37638283

Rather than using the default procedure as above, one can also specify a procedure used to carry out the energy calculation, e.g.

.. code-block:: text

   extrapolate,basis=avtz:avqz:av5z,proc=runccsd, method_r=ex1,npc=2}
   
   procedure runccsd
   hf
   ccsd(t)
   endproc

Alternatively, the energies can be provided via variables ``EREF``, ``ECORR``, ``ETOT`` etc. These must be vectors, holding as many values as basis sets are given.

.. _basis_set_extrapolation--options:

Options
=======

The possible options and extrapolation methods are:

* **``BASIS``\ =\ *basissets*** Specify as set of correlation consistent basis sets, separated by colons.
* **``PROC``\ =\ *procname*** Specify a procedure to run the energy calculations
* **``STARTCMD``\ =\ *command*** Start command for the energy calculations: the sequence of commands from ``STARTCMD`` and the current ``EXTRAPOLATE`` is run. ``STARTCMD`` must come before the extrapolate command in the input.
* **``METHOD``\ =\ *key*** Specifies a keyword to define the extrapolation function, see section `extrapolation functionals <basis_set_extrapolation.html#extrapolation-functionals>`__.
* **``METHOD_C``\ =\ *key*** Specifies a keyword to define the extrapolation function for the correlation energy, see section `extrapolation functionals <basis_set_extrapolation.html#extrapolation-functionals>`__.
* **``METHOD_R``\ =\ *key*** Specifies a keyword to define the extrapolation function for the reference energy, see section `extrapolation functionals <basis_set_extrapolation.html#extrapolation-functionals>`__.
* **``VARIABLE``\ =\ *name*** Specifies a variable name; this variable should contain the energies to be extrapolated.
* **``ETOT``\ =\ *variable*** Provide the total energies in *variable* (a vector with the same number of energies as basis sets are given) If only ETOT but not EREF is given, the total energy is extrapolated.
* **``EREF``\ =\ *variable*** Provide the reference energies to be extrapolated in *variable* (a vector with the same number of energies as basis sets are given)
* **``ECORR``\ =\ *variable*** Provide the correlation energies to be extrapolated in *variable* (a vector with the same number of energies as basis sets are given)
* **``ECORRD``\ =\ *variable*** Provide the Davidson corrected correlation energies to be extrapolated in *variable* (a vector with the same number of energies as basis sets are given). If both ``ECORR`` and ``ECORRD`` are given, both will be extrapolated.
* **``MINB``\ =\ *number*** First basis set to be used for extrapolation (default 1)
* **``MAXB``\ =\ *number*** Last basis set to be used for extrapolation (default number of basis sets)
* **``NPR``\ =\ *number*** If given, the last NPR values are used for extrapolating the reference energy. NPR must be smaller or equal to the number of basis sets.
* **``NPC``\ =\ *number*** If given, the last NPC values are used for extrapolating the reference energy. NPC must be smaller or equal to the number of basis sets.
* **``XR``\ =\ *array*** Provide a vector of exponents to be used for defining the extrapolation functional for the reference energy when using the ``LX`` functional.
* **``XC``\ =\ *array*** Provide a vector of exponents to be used for defining the extrapolation functional for the correlation energy when using the ``LX`` functional.
* **``PR``\ =\ *array*** Provide the constant :math:`p` to be used for defining the extrapolation functional for the reference energy.
* **``PC``\ =\ *array*** Provide the constant :math:`p` to be used for defining the extrapolation functional for the correlation energy.

.. _basis_set_extrapolation--extrapolation-functionals:

Extrapolation functionals
=========================

The extrapolation functional is chosen by a keyword with the ``METHOD``, ``METHOD_R``, and/or ``METHOD_C`` options. The default functional is ``L3``. In the following, :math:`n` is the cardinal number of the basis set (e.g., 2 for VDZ, 3 for VTZ etc), and :math:`x` is an arbitrary number. :math:`p` is a constant given either by the ``PR`` or ``PC`` options (default :math:`p=0`). ``X`` is a number or a vector given either by the ``XR`` or ``XC`` options (only for ``LX``; :math:`nx` is the number of elements provided in ``X``). :math:`A`, :math:`B`, :math:`A_i` are the fitting coefficients that are optimized by least-squares fits.

* **``L``\ :math:`x`** :math:`E_{n} = E_{\tt CBS} + A \cdot (n+p)^{-x}`
* **``LH``\ :math:`x`** :math:`E_{n} = E_{\tt CBS} + A \cdot (n+\frac{1}{2})^{-x}`
* ``LX`` :math:`E_{n} = E_{\tt CBS} + \sum_{i=1}^{nx} A_i \cdot (n+p)^{-x(i)}`
* ``EX1`` :math:`E_{n} =E_{\tt CBS}+A\cdot \exp(-C\cdot n)`
* ``EX2`` :math:`E_{n} =E_{\tt CBS}+A\cdot \exp(-(n-1))+B\cdot\exp(-(n-1)^2)`
* ``KM`` Two-point formula for extrapolating the HF reference energy, as proposed by A. Karton and J. M. L. Martin, Theor. Chem. Acc. **115**, 330 (2006): :math:`E_{\rm HF,n}=E_{\rm HF,CBS} +A (n+1)\cdot \exp(-9 \sqrt{n})`. Use ``METHOD_R=KM`` for this.

The following example shows various possibilities for extrapolation:

.. code-block:: text
   :caption: examples/h2o_extrapolate_ccsd.inp

   ***,h2o
   
   gthresh,energy=1.d-9
   basis=avtz
   
   r =   0.9572 ang, theta =  104.52
   geometry={!nosym
             O;
             H1,O,r;
             H2,O,r,H1,theta}
   
   hf
   {ccsd(t)}
   text,compute energies, extrapolate reference energy using EX1 and correlation energy using L3
   extrapolate,basis=avtz:avqz:av5z,method_c=l3,method_r=ex1,npc=2
   
   ehf=energr(1:3)
   etot=energy(1:3)
   
   text,extrapolate total energy using EX2
   extrapolate,basis=avtz:avqz:av5z,etot=etot,method=ex2
   
   text,extrapolate reference energy by EX1 and correlation energy by EX2
   extrapolate,basis=avtz:avqz:av5z,etot=etot,method_c=ex2,eref=ehf,method_r=ex1
   
   text,extrapolate reference energy by EX1 and correlation energy by LH3
   extrapolate,basis=avtz:avqz:av5z,etot=etot,method_c=LH3,eref=ehf,method_r=ex1,npc=2
   
   text,extrapolate reference energy by EX1 and correlation energy by LX
   extrapolate,basis=avtz:avqz:av5z,etot=etot,method_c=LX,eref=ehf,method_r=ex1,xc=[3,4],pc=0.5

The second example shows extrapolations of MRCI energies. In this case both the MRCI and the MRCI+Q energies are extrapolated.

.. code-block:: text
   :caption: examples/h2o_extrapolate_mrci.inp

   ***,h2o
   
   gthresh,energy=1.d-9
   basis=avtz
   
   r =   0.9572 ang, theta =  104.52
   geometry={
             O;
             H1,O,r;
             H2,O,r,H1,theta}
   
   hf
   multi
   mrci
   text,Compute energies, extrapolate reference energy using EX1 and correlation energy using L3;
   text,The Davidson corrected energy is also extrapolated
   extrapolate,basis=avtz:avqz:av5z,method_c=l3,method_r=ex1,npc=2
   
   emc=energr
   ecorr_mrci=energy-emc
   ecorr_mrciq=energd-emc
   
   text,Extrapolate reference energy by EX1 and correlation energy by LH3
   text,The Davidson corrected energy is also extrapolated
   extrapolate,basis=avtz:avqz:av5z,ecorr=ecorr_mrci,ecorrd=ecorr_mrciq,method_c=LH3,eref=emc,method_r=ex1,npc=2

.. _basis_set_extrapolation--geometry-optimization-using-extrapolated-energies:

Geometry optimization using extrapolated energies
=================================================

Geometry optimizations are possible by using numerical gradients obtained from extrapolated energies. Analytical energy gradients cannot be used.

The following possibilities exist:

1.) If ``OPTG`` directly follows the ``EXTRAPOLATE`` command, the extrapolated energy is optimized automatically (only variable settings may occur between ``EXTRAPOLATE`` and ``OPTG``).

Examples:

Extrapolating the energy for the last command:

.. code-block:: text
   :caption: examples/h2o_extrapol_opt1.inp

   geometry={o;h1,o,r;h2,o,r,h1,theta}
   theta=102
   r=0.96 ang
   basis=vtz
   
   hf
   ccsd(t)
   extrapolate,basis=vtz:vqz
   
   optg

Extrapolating the energy computed in a procedure:

.. code-block:: text
   :caption: examples/h2o_extrapol_opt2.inp

   geometry={o;h1,o,r;h2,o,r,h1,theta}
   theta=102
   r=0.96 ang
   
   proc ccsdt
   hf
   ccsd(t)
   endproc
   
   extrapolate,basis=vtz:vqz,proc=ccsdt
   
   optg

Note that this is not possible if ``EXTRAPOLATE`` gets the input energies from variables.

2.) Using a procedure for the extrapolation:

By default, variable ``ECBS`` is optimized, but other variables (e.g. ``ECBSD``) can be specified using the ``VARIABLE`` option on the ``OPTG`` command.

.. code-block:: text
   :caption: examples/h2o_extrapol_opt3.inp

   geometry={o;h1,o,r;h2,o,r,h1,theta}
   theta=102
   r=0.96 ang
   basis=vtz
   
   proc cbs34
   hf
   ccsd(t)
   extrapolate,basis=vtz:vqz
   endproc
   
   optg,variable=ecbs,proc=cbs34

.. code-block:: text
   :caption: examples/h2o_extrapol_opt4.inp

   geometry={o;h1,o,r;h2,o,r,h1,theta}
   theta=102
   r=0.96 ang
   
   proc cbs34
   basis=vtz
   hf
   ccsd(t)
   eref(1)=energr
   ecc(1)=energy
   
   basis=vqz
   hf
   ccsd(t)
   eref(2)=energr
   ecc(2)=energy
   extrapolate,basis=vtz:vqz,eref=eref,etot=ecc
   endproc
   
   optg,variable=ecbs,proc=cbs34

.. _basis_set_extrapolation--harmonic-vibrational-frequencies-using-extrapolated-energies:

Harmonic vibrational frequencies using extrapolated energies
============================================================

This is possible by defining the extrapolation in a procedure:

.. code-block:: text
   :caption: examples/h2o_extrapol_freq.inp

   geometry={o;h1,o,r;h2,o,r,h1,theta}
   theta=102
   r=0.96 ang
   basis=vtz
   
   proc cbs34
   hf
   ccsd(t)
   extrapolate,basis=vtz:vqz
   endproc
   
   optg,variable=ecbs,proc=cbs34
   freq,variable=ecbs,proc=cbs34

.. _basis_set_extrapolation--basis-set-incompleteness-error-correction-using-a-dft-model-of-short-ranged-electron-interactions:

Basis set incompleteness error correction using a DFT model of short-ranged electron interactions
=================================================================================================

As an alternative to basis set extrapolations or using F12 correlation methods, the BSIE (basis set incompleteness error) to electron correlation energies can also be corrected by using a density based model by Giner *et al.*, see:

:math:`[1]` E. Giner, B. Pradines, A. Ferté, R. Assaraf, A. Savin, and J. Toulouse, *Curing basis-set convergence of wave-function theory using density-functional theory: A systematically improvable approach*, `J. Chem. Phys. <https://doi.org/10.1063/1.5052714>`__ **149**, 194301 (2018).
:math:`[2]` P.-F. Loos, B. Pradines, A. Scemama, J. Toulouse, and E. Giner, *A density-based basis-set correction for wave function theory*, `J. Phys. Chem. Lett. <https://dx.doi.org/10.1021/acs.jpclett.9b01176>`__ **10**, 2931 (2019).
:math:`[3]` E. Giner, A. Scemama, P.-F. Loos, and J. Toulouse, *A basis-set error correction based on density-functional theory for strongly correlated molecular systems*, `J. Chem. Phys. <https://dx.doi.org/10.1063/5.0002892>`__ **152**, 174104 (2020).

This basis-set correction relies on a mapping between wave-function calculations in a finite basis set and range-separated DFT (RSDFT) through the definition of an effective non-divergent interaction corresponding to the electron–electron Coulomb interaction projected in the finite basis set. This enables the use of RSDFT-type complementary correlation density functionals to recover the dominant part of the short-range correlation effects missing in this finite basis set.

For example, to compute the extrapolated MP2 energy with the DFT correction the following input can be used for Molpro

.. code-block:: text

   !water molecule 
   r=0.9575 ANG
   theta=104.51
   geometry={O; H1,O,R; H2,O,R,H1,theta}
   
   !small basis set with diffuse functions
   basis=avdz
   
   !hf calculation
   hf
   eref=energy !save reference energy
   
   !mp2 calculation for this small basis set
   mp2
   ecorr=energy-eref !save mp2 correlation energy 
   
   !compute DFT correction
   bascorr,core=1   !use option for frozen-core here
   
   !add correction to total energy (DFT correction stored in ecmd variable
   etot=eref+ecorr+ecmd

Note that the DFT correction may be used in conjunction with any wave function correlation method which suffers from the wrong description of the interelectronic cusp with finite basis sets, so in the above example the MP2 method could be replaced with any other electron correlation method available in Molpro.

The reference energy term is not corrected for the BSIE in the example above. One may do so by using either the basis set extrapolation
approach described in this section:

.. code-block:: text

   hf
   extrapolate,basis=avdz:avtz:avqz
   eref=energr(4) !the last element in the array (first 3 elements are the avdz/avtz/avqz energies)

or by adding the CABS singles correction to the HF energy computed in the small basis set

.. code-block:: text

   hf
   eref0=energy
   df-mp2-f12,cabs_singles=-1
   eref=eref0+ef12_singles

see also the corresponding subsection in `Explicitly correlated methods <explicitly_correlated_methods.html#cabs-singles-correction>`__

In general the density based BSIE correction can be called as

.. code-block:: text

   bascorr,<core=...>,<orb=...>,<tolorb=...>

with the following options

.. code-block:: text

* ``CORE`` number of core orbitals (normally required, since by default all orbitals are included). When symmetry is used an array of the form [nc1,nc2,...] must be given to the option for specifying the core orbitals in each symmetry
* ``ORB`` the record storing the orbital coefficients. If omitted, the orbitals from the last SCF calculation are being used.
* ``TOLORB`` screening threshold for the calculation of the basis functions on the grid.
* ``CFUN`` set correlation functional (default: ``CFUN=PBEC``).

Since the calculation of the BSIE correction requires a numerical integration on a quadrature grid, the grid setting described
`here <the_density_functional_program.html#numerical-integration-grid-control-grid>`__ also can affect the results of the correction. In practice,
however, the default settings for DFT integrations should be adequate.

The density-based BSIE correction involves the calculation of a 4-indexed quantity on the quadrature grid. For larger molecules this step can therefore become very expensive and it is strongly advised to use the corresponding density fitting implementation of the method which can drastically reduce the computation time. The DF implementation currently can not generate the fitting basis sets automatically, so an input of the following kind needs to be used then:

.. code-block:: text

   basis={
   set,orbital; default,avdz
   set,jkfit; default,avdz/jkfit   !only for scf calculation
   set,mp2fit; default,avdz/mp2fit
   }
   
   df-hf,basis=jkfit
   {cfit,basis=mp2fit}  !change to mp2fit basis set
   df-bascorr

where the MP2Fit fitting basis set is used for the ``BASCORR`` program which has been found to yield better results than the corresponding JKFit basis set that we use for the SCF calculation in the example above.

By default the PBE correlation functional ``cfun=PBEC`` is used to describe the short ranged correlation contribution of the BASCORR model. It is possible to choose a different correlation functional by using the ``cfun`` option. This, however, should normally not be changed, because the basis set correction has so far only been tested for the PBEC functional. Furthermore, note that Molpro does not distinguish between correlation and exchange functionals and will not exit with an error if the BASCORR program is used with improper exchange functional.
