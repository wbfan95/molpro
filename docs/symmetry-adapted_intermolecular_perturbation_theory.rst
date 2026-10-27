.. raw:: html

   <span id="df-dft-sapt-calculation-of-the-near-dimer-using-the-delta-hf-correction"></span>

.. raw:: html

   <span id="dfsapt-a-density-fitting-dft-sapt-program-for-arbitrary-monomer-basis-sets"></span>

.. raw:: html

   <span id="dfsapt-calculation-of-the-water-dimer-using-a-dcbs-basis-set"></span>

.. raw:: html

   <span id="dfsapt-calculation-of-the-water-dimer-using-an-mc-bs-basis-set"></span>

.. raw:: html

   <span id="dfsapt-calculation-of-the-water-dimer-using-an-mcbs-basis-set"></span>

.. raw:: html

   <span id="dfsapt-calculation-of-the-water-dimer-with-additional-d-hf-correction"></span>

.. raw:: html

   <span id="dft-sapt-calculation-of-the-near-dimer-using-the-delta-hf-correction"></span>

.. raw:: html

   <span id="examples"></span>

.. raw:: html

   <span id="high-order-terms"></span>

.. raw:: html

   <span id="introduction"></span>

.. raw:: html

   <span id="mp2-coupled-mp2c"></span>

.. raw:: html

   <span id="using-exact-exchange-kohn-sham-response-kernels"></span>

.. _symmetry-adapted_intermolecular_perturbation_theory--symmetry-adapted-intermolecular-perturbation-theory:

Symmetry-adapted intermolecular perturbation theory
===================================================

.. _symmetry-adapted_intermolecular_perturbation_theory--introduction:

Introduction
============

The SAPT (symmetry-adapted intermolecular perturbation theory) program calculates the total interaction energy between closed-shell molecules as a sum of individual first and second order interaction terms, namely electrostatic :math:`E_{\text{pol}}^{(1)}`, induction :math:`E_{\text{ind}}^{(2)}` and dispersion :math:`E_{\text{disp}}^{(2)}` accompanied by their respective exchange counterparts (:math:`E_{\text{exch}}^{(1)}`, :math:`E_{\text{exch-ind}}^{(2)}` and :math:`E_{\text{exch-disp}}^{(2)}`). The latter ones arise due to electron exchange between the monomers when the molecules are close to each other and are sometimes denoted as Pauli repulsion. Since all above terms are accessible through density matrices and static and dynamic density-density response functions of the monomers, in principle (see section `high order terms <symmetry-adapted_intermolecular_perturbation_theory.html#high-order-terms>`__) no calculation of the dimer wave function is required. Therefore SAPT is free from the basis set superposition error which occurs in the supermolecular approach.

References:

**General Symmetry-adapted perturbation theory and many-body SAPT:**
:math:`[1]` B. Jeziorski, R. Moszynski and K. Szalewicz, Chem. Rev. **94**, 1887. (1994).
**DFT-SAPT:**
:math:`[2]` G. Jansen and A. Heßelmann, J. Phys. Chem. A **105**, 646 (2001).
:math:`[3]` A. Heßelmann and G. Jansen, `Chem. Phys. Lett. <https://dx.doi.org/10.1016/S0009-2614(02)00538-9>`__ **357**, 464 (2002).
:math:`[4]` A. Heßelmann and G. Jansen, `Chem. Phys. Lett. <https://dx.doi.org/10.1016/S0009-2614(02)01097-7>`__ **362**, 319 (2002).
:math:`[5]` A. Heßelmann and G. Jansen, `Chem. Phys. Lett. <https://dx.doi.org/10.1016/S0009-2614(02)01796-7>`__ **367**, 778 (2003).
:math:`[6]` A. Heßelmann and G. Jansen, `Phys. Chem. Chem. Phys. <https://dx.doi.org/10.1039/B310529F>`__ **5**, 5010 (2003).
**Density fitting DFT-SAPT (DF-DFT-SAPT):**
:math:`[7]` A. Heßelmann, G. Jansen and M. Schütz, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.1824898>`__ **122**, 014103 (2005).

**Density fitting DFT-SAPT for arbitrary monomer basis sets (DFSAPT):**
:math:`[8]` A. Heßelmann and T. Korona, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.4893990>`__ **141**, 094107 (2014).

**DFT-SAPT employing exact-exchange response kernels (EXX-SAPT):**
:math:`[9]` A. Heßelmann, `J. Chem. Theory Comput. <https://dx.doi.org/10.1021/acs.jctc.7b01233>`__ **14**, 1943 (2018)

**Single-determinant-based SAPT without single-exchange approximation:**
:math:`[10]` R. Schäffer and G. Jansen, *Theor. Chem. Acc.* **131** (2012) 1235
:math:`[11]` R. Schäffer and G. Jansen, `Mol. Phys. <https://dx.doi.org/10.1080/00268976.2013.827253>`__ **111**, 2570 (2013)

**SAPT with regularised nuclear attraction integrals:**
:math:`[12]` A. J. Misquitta, `J. Chem. Theory Comput. <https://dx.doi.org/10.1021/ct400704a>`__ **9**, 5313 (2013)

(See also:
K. Szalewicz, K. Patkowski and B. Jeziorski, Struct. Bond **116**, 43 (2005)
K. Szalewicz, WIREs Comput. Mol. Sci. **2**, 254 (2011)
and references therein for a related approach to DFT-SAPT termed SAPT(DFT))

.. _symmetry-adapted_intermolecular_perturbation_theory--first-example:

First example
=============

A typical input for SAPT has the following form:

.. code-block:: text

   r=5.6
   geometry={nosym; he1; he2,he1,r}
   basis=avqz
   
   !wf records
   ca=2101.2
   cb=2102.2
   
   !monomer A
   dummy,he2
   {hf; save,$ca}
   sapt;monomerA
   
   !monomer B
   dummy,he1
   {hf; start,atdens; save,$cb}
   sapt;monomerB
   
   !interaction contributions
   sapt;intermol,ca=$ca,cb=$cb

Here the ``sapt;monomerA/B`` store some informations about the two monomers which are needed in the subsequent SAPT calculation invoked by ``sapt;intermol``. The individual interaction energy terms are stored (in millihartree) in distinct variables and may be collected in arrays for producing potential energy surfaces. For example the input

.. code-block:: text

   geometry={nosym; he1; he2,he1,r}
   basis=avtz
   
   !wf records
   ca=2101.2
   cb=2102.2
   
   !distances
   dist=[4.5,5.0,5.5,5.6,6.0,6.5,7.0]
   
   do i=1,#dist
      r=dist(i)
   
      !monomer A
      dummy,he2
      {hf; save,$ca}
      sapt;monomerA
   
      !monomer B
      dummy,he1
      {hf; start,atdens; save,$cb}
      sapt;monomerB
   
      !interaction contributions
      sapt;intermol,ca=$ca,cb=$cb
   
      elst(i)=E1pol;  exch(i)=E1ex
      ind(i)=E2ind;   exind(i)=E2exind
      disp(i)=E2disp; exdisp(i)=E2exdisp
      etot(i)=E12tot
   
      data,truncate,$ca
   enddo
   
   {table,dist,elst,exch,ind,exind,disp,exdisp,etot
   ftyp,d,d,d,d,d,d,d,d,d
   plot}

yields the plot

.. image:: /media/he2.svg
   :alt: he2.svg
   :width: 500px

Currently SAPT only accepts single-determinant wave functions for the monomers, i.e. from Hartree-Fock or Kohn-Sham DFT (see next section) calculations. This means that if Hartree-Fock wave functions are used for monomer, the following quantity is obtained (zero in superscript denotes that no intramonomer correlation is accounted for) [1].

.. math::

   \begin{aligned}
   E_{\text{SAPT}}=E^{(10)}_{\text{pol}}+E^{(10)}_{\text{exch}}+
                  E^{(20)}_{\text{ind,resp.}}+
      E^{(20)}_{\text{exch-ind,resp.}}+E^{(20)}_{\text{disp}}+
      E^{(20)}_{\text{exch-disp}}\end{aligned}

No point group symmetry can be exploited in a SAPT calculation.

.. _symmetry-adapted_intermolecular_perturbation_theory--dft-sapt:

DFT-SAPT
========

It is of crucial importance to account for the *intra*\ molecular correlation effects of the individual SAPT terms since Hartree-Fock theory often yields poor first- and second-order electrostatic properties. While this can be done using many-body perturbation theory [1] (in a double perturbation theory ansatz) a more efficient way is to use static and time-dependent DFT theory. This variant of SAPT, termed as DFT-SAPT [2-6], has in contrast to Hartree-Fock-SAPT the appealing feature that the polarisation terms (:math:`E_{\text{pol}}^{(1)}`, :math:`E_{\text{ind}}^{(2)}`, :math:`E_{\text{disp}}^{(2)}`) are potentially exact, i.e. they come out exactly if the exact exchange-correlation (xc) potential and the exact (frequency-dependent) xc response kernel of the monomers were known. On the other hand, this does not hold for the exchange terms since Kohn-Sham theory can at best give a good approximation to the exact density matrix of a many-body system. It has been shown [6] that this is indeed the the case and therefore DFT-SAPT has the potential to produce highly accurate interaction energies comparable to high-level supermolecular many-body perturbation or coupled cluster theory. However, in order to achieve this accuracy, it is of crucial importance to correct the wrong asymptotic behaviour of the xc potential in current DFT functionals [3-5]. This can be done by using e.g.:

.. code-block:: text

   {ks,lda; asymp,<shift>}

which activates the gradient-regulated asymptotic correction approach of Grüning *et al.* (`J. Chem. Phys. <https://dx.doi.org/10.1063/1.1327260>`__ **114**, 652 (2001)) for the respective monomer calculation. The user has to supply a ``shift`` parameter (:math:`\Delta_{\text{xc}}`) for the bulk potential which should approximate the difference between the HOMO energy (:math:`\varepsilon_{\text{HOMO}}`) obtained from the respective standard Kohn-Sham calculation and the (negative) ionisation potential of the monomer (:math:`\mathrm{IP}`):

.. math::

   \Delta_{\text{xc}}=\varepsilon_{\text{HOMO}}-(-\mathrm{IP})

This method accounts for the derivative discontinuity of the exact xc-potential and that is missing in approximate ones. Note that this needs to be done only once for each system. (See also section `DFT-SAPT calculation of the NeAr dimer using the delta-HF correction <symmetry-adapted_intermolecular_perturbation_theory.html#dft-sapt-calculation-of-the-near-dimer-using-the-delta-hf-correction>`__ for an explicit example).

It is also possible to use an alternative asymptotic correction method described in Ref. [9] by using the ``EXX`` program (see section `optimised Effective Potential (OEP) method <the_density_functional_program.html#optimised-effective-potential-oep-method>`__). Here, the derivative discontinuity shift is determined through an interpolation between the HOMO energy of the EXX method and the HOMO energy of a corresponding hybrid functional. Currently, this technique should only be used in conjuction with hybrid methods employing 25% exact exchange.

Concerning the more technical parameters in the DFT monomer calculations it is recommended to use lower convergence thresholds and larger integration grids compared to standard Kohn-Sham calculations.

.. _symmetry-adapted_intermolecular_perturbation_theory--high-order-terms:

High order terms
================

It has been found that third and higher-order terms become quite important if one or both monomers are polar. As no higher than second-order terms are currently implemented in SAPT, one may use a non-correlated estimation of those terms by using supermolecular Hartree-Fock (see e.g. [7]). This can be done by adapting the following template:

.. code-block:: text

   !dimer
   hf
   edm=energy
   
   !monomer A
   dummy,<monomer2>
   {hf; save,$ca}
   ema=energy
   sapt;monomerA
   
   !monomer B
   dummy,<monomer1>
   {hf; start,atdens; save,$cb}
   emb=energy
   sapt;monomerB
   
   !interaction contributions
   sapt,sapt_level=2;intermol,ca=$ca,cb=$cb
   
   esup=(edm-ema-emb)*1000. mH
   dHF=esup-e1pol-e1ex-e2ind-e2exind

which stores the resulting :math:`\delta`\ (HF) term in ``dHF``.

.. _symmetry-adapted_intermolecular_perturbation_theory--exchange-interaction-energies-with-infinite-expansion-in-the-intermolecular-overlap:

Exchange interaction energies with infinite expansion in the intermolecular overlap
===================================================================================

The exchange interaction energies are commonly expanded in powers of the intermolecular overlap :math:`S`:

.. math::

   \begin{aligned}
   E_{\text{exch}}^{(1)}(S^\infty)&=&E_{\text{exch}}^{(1)}(S^2)+\Delta E_{\text{exch}}^{(1)}(S^4)
        +\Delta E_{\text{exch}}^{(1)}(S^6)\dots \\
   E_{\text{exch-ind}}^{(2)}(S^\infty)&=&E_{\text{exch-ind}}^{(2)}(S^2)+\Delta E_{\text{exch-ind}}^{(2)}(S^4)
         +\Delta E_{\text{exch-ind}}^{(2)}(S^6)+\dots \\
   E_{\text{exch-disp}}^{(2)}(S^\infty)&=&E_{\text{exch-disp}}^{(2)}(S^2)+\Delta E_{\text{exch-disp}}^{(2)}(S^4)
          +\Delta E_{\text{exch-disp}}^{(2)}(S^6)+\dots \\\end{aligned}

where :math:`E_{\text{exch}}^{(1)}(S^2)` corresponds to the exchange interaction energy in which the intermolecular overlap occurs only in single and quadratic powers and :math:`\Delta E_{\text{exch}}^{(1)}(S^4)` collects all terms up to the fourth power in :math:`S` excluding the terms in :math:`E_{\text{exch}}^{(1)}(S^2)`. The above expansions are commonly truncated after the first terms, leading to the so-called :math:`S^2` approximation. Accordingly, for very small distances of the monomers, the exchange interaction energies become inaccurate and eventually the :math:`S^2` approximation may even break down, see Refs. [10,11].

While this problem may be circumvented by adding the :math:`\delta`\ (HF) term to the SAPT interaction energy (see section `high order terms <symmetry-adapted_intermolecular_perturbation_theory.html#high-order-terms>`__), a derivation of the infinite expansions of the first-order exchange energy was given by Jeziorski, Bulski and Piela (*Int. J. Quantum Chem.* **10** (1976) 281). More recently, formulas for the second-order exchange induction and dispersion energies were derived by Schäffer and Jansen, see Refs. [10,11].

In Molpro, the calculation of the exchange interaction energies in the :math:`S^2` approximation or with an infinite expansion in :math:`S` (:math:`S^\infty`) can be controlled through the switch

.. code-block:: text

      sapt,sinf=<0,1,2>

where ``sinf=0`` will calculate the exchange interaction energies within the :math:`S^2` approximation and ``sinf=1`` calls the routines to calculate all exchange interaction terms with infinite overlap expansion (:math:`S^\infty`). Using ``sinf=2`` will calculate both the :math:`S^2` and the :math:`S^\infty` contributions. Note that the first-order exchange energy is always calculated in both variants.

.. _symmetry-adapted_intermolecular_perturbation_theory--using-exact-exchange-kohn-sham-response-kernels:

Using exact exchange Kohn-Sham response kernels
===============================================

The exact exchange Kohn-Sham response kernel can be used in the computations of the second order (exchange-)induction and (exchange-)dispersion contributions, see Ref. [9]. In order to do so, the :math:`\langle i|v_x^{\text{NL}}-v_x|j\rangle` matrix elements have to be precomputed for each monomer and supplied to the SAPT program. The following input template shows how to compute DFT-SAPT interaction energy contributions using the (A)TDEXX response kernels and the LPBE0AC xc potentials (cf section `optimised Effective Potential (OEP) method <the_density_functional_program.html#optimised-effective-potential-oep-method>`__):

.. code-block:: text

   dummy,<atoms on B> !monomer A
   {ks,lda; save,2100.2; start,atdens}
   {exxhyb,orb=2100.2,oep=7,homo=1,charge=1,maxit=30,scfthr=1d-9,add=1,xfac=0.25,shift=1
   func,pbex,pbec; dftfac,0.75,1.0}
   {oep,orb=2101.2,vxdiff=5100.2,gamma=3d-4,dfit=1,homo=1}
   {sapt;monomerA}
   
   dummy,<atoms on A> !monomer B
   {ks,lda; save,2200.2; start,atdens}
   {exxhyb,orb=2200.2,oep=7,homo=1,charge=1,maxit=30,scfthr=1d-9,add=1,xfac=0.25,shift=1
   func,pbex,pbec; dftfac,0.75,1.0}
   {oep,orb=2201.2,vxdiff=5200.2,gamma=3d-4,dfit=1,homo=1}
   {sapt;monomerB}
   
   sapt;intermol,ca=2101.2,cb=2201.2,icpks=0,vxdiffA=5100.2,vxdiffB=5200.2,\
        nlexfac=1.0,tdexx=<TDEXXMODE>

The input parameter ``TDEXXMODE`` takes the values 1 or 2. With ``TDEXXMODE=1`` the full nonadiabatic TDEXX response kernel and with ``TDEXXMODE=2`` only the adiabatic TDEXX response kernel is used in the calculation of the response matrices of the monomers. Notice also from the above template that it is important to set ``nlexfac=1.0`` which sets the scaling factor of exact exchange in the SAPT program. If ``nlexfac`` is set to a value lower than one, a hybrid ALDA-TDEXX kernel will be used in the calculation. All reported calculations using this program should cite Ref. [9].

Note that unlike in the conventional hybrid-DFT case, DFT-SAPT calculations can be performed also using density fitting techniques for (A)TDEXX kernels with Molpro. A corresponding efficient DF implementation which works in conjunction with (A)TDEXX kernels is the DFSAPT program, see section `DFSAPT: a density-fitting DFT-SAPT program for arbitrary monomer basis sets <symmetry-adapted_intermolecular_perturbation_theory.html#dfsapt-a-density-fitting-dft-sapt-program-for-arbitrary-monomer-basis-sets>`__.

.. _symmetry-adapted_intermolecular_perturbation_theory--sapt-with-regularised-nuclear-attraction-integrals:

SAPT with regularised nuclear attraction integrals
==================================================

The SAPT expansion of the intermolecular interaction energy does not yield the charge-transfer (CT) interaction energy as a separate term, rather it is included in the sum of the second-order induction and exchange-induction energies:

.. math::

   E_{\text{int}}^{\text{CT}} \subset E_{\text{ind}}^{(2)}+E_{\text{exch-ind}}^{(2)}

Due to Misquitta, see Ref. [12], the CT interaction energy can, however, be ’estimated’ by using a regularised nuclear attraction potential for the monomers in order to calculate (exchange-)induction energies excluding the (short-ranged) CT interaction contribution. The CT interaction energy can then be obtained by calculating the difference between the full (exchange-)induction interaction energy and the (exchange-)induction interaction energy as obtained by the regularised SAPT method:

.. math::

   E_{\text{int}}^{\text{CT}} \approx
         E_{\text{ind}}^{(2)}+E_{\text{exch-ind}}^{(2)}
         -E_{\text{ind}}^{(2)}[regul]-E_{\text{exch-ind}}^{(2)}[regul]

For obtaining regularised nuclear attraction integrals Misquitta proposes the form [12]:

.. math::

   V_{\text{regul}}=\frac{1}{r}\Big(1-e^{-\alpha r^2}\Big)

with :math:`\alpha=3.0`.

In Molpro, regularised SAPT calculations can be performed by calling the ``vreg`` module ’before’ saving the monomer geometries with ``{sapt; monomerA,B}``. An input template for the calculation of the CT interaction energy is given by:

.. code-block:: text

   dummy,<monomer B centres>
   {ks,<functional>; orbital,2100.2}
   {sapt;monomerA}
   
   dummy,<monomer A centres>
   {ks,<functional>; start,atdens; orbital,2200.2}
   {sapt;monomerB}
   
   sapt,sapt_level=2;intermol,ca=2100.2,cb=2200.2,icpks=0
   eIND1=e2ind+e2exind
   
   dummy,<monomer B centres>
   vreg,alpha=3d0,nq=1
   {sapt;monomerA}
   
   dummy,<monomer A centres>
   vreg,alpha=3d0,nq=1
   {sapt;monomerB}
   
   sapt,sapt_level=2;intermol,ca=2100.2,cb=2200.2,icpks=0
   eIND2=e2ind+e2exind
   
   eint_CT=eIND1-eIND2

The ``vreg`` module accepts the following options:

* ``ALPHA`` Exponent of the exponential function of the damping factor.
* ``NQ`` Global exponent of the damping factor (type: integer).
* ``SAVE`` Record (``record.file``) in which to save the integrals. If not used, the standard record that holds the nuclear attraction integrals is overwritten.

The regularised SAPT can also be used in order to resolve the breakdown of the conventional SAPT expansion for the interaction between heavy atoms, see, e.g., Liu *et al.*, `J. Chem. Theory Comput. <https://dx.doi.org/10.1021/ct200243s>`__ **7**, 2399 (2011). A regularised SAPT method was, e.g., used in T. Clark, A. Heßelmann, `Phys. Chem. Chem. Phys. <https://dx.doi.org/10.1039/C8CP03079K>`__ **20**, 22849 (2018) for calculating the bonding between carbon tetrahalides and halide anions. Note that in this case the addition of the :math:`\delta`\ (HF) term (see section `high order terms <symmetry-adapted_intermolecular_perturbation_theory.html#high-order-terms>`__) for taking into account short-ranged polarisation effects is crucial.

.. _symmetry-adapted_intermolecular_perturbation_theory--density-fitting:

Density fitting
===============

In order to be able to study interactions between extended monomers one can use density fitting to approximate the integrals in SAPT [7]. For this one may use the input:

.. code-block:: text

   {sapt;intermol,ca=$ca,cb=$cb,fitlevel=3
   dfit,basis_coul=jkfit,basis_exch=jkfit,basis_mp2=mp2fit,cfit_scf=3}

with in the basis section defined ``jkfit`` and ``mp2fit`` fitting basis sets (see section :doc:`density fitting <density_fitting>`).

Currently only ALDA or (A)TDEXX xc-kernels are implemented for the case ``SAPT_LEVEL``\ =3 and ``SAPT_FITLEVEL``\ =3. This means that a corresponding SAPT calculation would be incompatible with  (conventional) hybrid-DFT monomer orbitals/orbital energies. Therefore it is recommended to use nonhybrid functionals in the case the dispersion/exchange-dispersion energy terms are requested in a DF-DFT-SAPT run. Another possibility is to localise the xc-potential via, e.g., the OEP method (see section `exact exchange Kohn-Sham methods <the_density_functional_program.html#exact-exchange-kohn-sham-methods>`__ and the example in section `DF-DFT-SAPT calculation of the NeAr dimer using the delta-HF correction <symmetry-adapted_intermolecular_perturbation_theory.html#df-dft-sapt-calculation-of-the-near-dimer-using-the-delta-hf-correction>`__).

New density fitting routines for the calculation of :math:`E^{(2)}_{\text{IND}}(S^\infty)` and :math:`E^{(2)}_{\text{DISP}}(S^\infty)` can be activated with the switch

.. code-block:: text

    sapt,df2=.true.,...

For performing density-fitting DFT-SAPT calculations with arbitrary monomer basis sets see section `DFSAPT: a density-fitting DFT-SAPT program for arbitrary monomer basis sets <symmetry-adapted_intermolecular_perturbation_theory.html#dfsapt-a-density-fitting-dft-sapt-program-for-arbitrary-monomer-basis-sets>`__.

.. _symmetry-adapted_intermolecular_perturbation_theory--sapt-with-ecp-s:

SAPT with ECP’s
===============

If effective core potentials (ECP’s) are used in the monomer calculations, it is important to add the :math:`\delta`\ (HF) term to the SAPT interaction energy (see K. Patkowski, K. Szalewicz, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.2784391>`__ **127**, 164103 (2007)). For examples for the calculation of :math:`\delta`\ (HF) see sections `high order terms <symmetry-adapted_intermolecular_perturbation_theory.html#high-order-terms>`__ and `examples <symmetry-adapted_intermolecular_perturbation_theory.html#examples>`__.

.. _symmetry-adapted_intermolecular_perturbation_theory--examples:

Examples
========

.. _symmetry-adapted_intermolecular_perturbation_theory--hf-sapt-calculation-of-the-h2o-dimer-using-the-delta-hf-correction:

HF-SAPT calculation of the H2O dimer using the delta-HF correction
==================================================================

.. code-block:: text
   :caption: examples/h2odimer_sapt_hf.inp

   gthresh,energy=1.d-8,orbital=1.d-8,grid=1.d-8
   symmetry,nosym
   orient,noorient
   GEOMETRY={
   1,O1,,0.00000000,0.00000000,0.00000000
   2,H1,,0.00000000,0.00000000,1.83606000
   3,H2,,1.77604000,0.00000000,-0.4656040
   4,O2,,-0.6605540,0.00000000,5.54064000
   5,H3,,-1.6582100,-1.4536300,6.05324000
   6,H4,,-1.6582100,1.45363000,6.05324000
   }
   basis=avdz
   
   !sapt files
   ca=2101.2
   cb=2102.2
   
   !dimer
   hf
   edm=energy
   
   !monomer A
   dummy,o2,h3,h4
   {hf; save,$ca}
   ema=energy
   {sapt;monomerA}
   
   !monomer B
   dummy,o1,h1,h2
   {hf; start,atdens; save,$cb}
   emb=energy
   {sapt;monomerB}
   
   !interaction contributions
   {sapt,SAPT_LEVEL=3;intermol,ca=$ca,cb=$cb,icpks=1}
   
   !HF supermolecular interaction energy and delta(HF) contribution
   eint_hf=(edm-ema-emb)*1000 mH
   delta_hf=eint_hf-e1pol-e1ex-e2ind-e2exind
   
   !add E2disp + E2exch-disp to HF interaction energy
   eint_sapt=eint_hf+e2disp+e2exdisp

.. _symmetry-adapted_intermolecular_perturbation_theory--dft-sapt-calculation-of-the-near-dimer-using-the-delta-hf-correction:

DFT-SAPT calculation of the NeAr dimer using the delta-HF correction
====================================================================

.. code-block:: text
   :caption: examples/near_sapt_acdft.inp

   gthresh,energy=1.d-8,orbital=1.d-8,grid=1.d-8
   symmetry,nosym
   orient,noorient
   geometry={
   Ne,,0.0,0.0,0.0
   Ar,,0.0,0.0,6.5}
   basis=avtz
   
   !=========delta(HF) contribution for higher order interaction terms====
   !sapt files
   ca=2101.2
   cb=2102.2
   
   !dimer
   hf
   edm=energy
   
   !monomer A
   dummy,ar
   {hf; save,$ca}
   ema=energy
   {sapt;monomerA}
   
   !monomer B
   dummy,ne
   {hf; start,atdens; save,$cb}
   emb=energy
   {sapt;monomerB}
   
   !interaction contributions
   {sapt,SAPT_LEVEL=2;intermol,ca=$ca,cb=$cb,icpks=1}
   
   !calculate high-order terms by subtracting 1st+2nd order energies
   eint_hf=(edm-ema-emb)*1000 mH
   delta_hf=eint_hf-e1pol-e1ex-e2ind-e2exind
   
   
   !=========DFT-SAPT at second order intermol. perturbation theory====
   !sapt files
   ca=2103.2
   cb=2104.2
   
   !shifts for asymptotic correction to xc potential
   eps_homo_pbe0_ar=-0.440936      !HOMO(Ar)/PBE0 functional
   eps_homo_pbe0_ne=-0.589207      !HOMO(Ne)/PBE0
   ip_ar=0.5792                    !exp. ionisation potential
   ip_ne=0.7925                    !exp. ionisation potential
   shift_ar=ip_ar+eps_homo_pbe0_ar !shift for bulk xc potential (Ar)
   shift_ne=ip_ne+eps_homo_pbe0_ne !shift for bulk xc potential (Ne)
   
   !monomer A
   dummy,ar
   {ks,pbe0; asymp,shift_ne; save,$ca}
   {sapt;monomerA}
   
   !monomer B
   dummy,ne
   {ks,pbe0; start,atdens; asymp,shift_ar; save,$cb}
   {sapt;monomerB}
   
   !interaction contributions
   {sapt;intermol,ca=$ca,cb=$cb,icpks=0}
   
   !add high-order approximation to obtain the total interaction energy
   eint_dftsapt=e12tot+delta_hf

.. _symmetry-adapted_intermolecular_perturbation_theory--df-dft-sapt-calculation-of-the-near-dimer-using-the-delta-hf-correction:

DF-DFT-SAPT calculation of the NeAr dimer using the delta-HF correction
=======================================================================

.. code-block:: text
   :caption: examples/near_df_sapt_acdft.inp

   gdirect; gthresh,energy=1.d-8,orbital=1.d-8,grid=1.d-8
   symmetry,nosym
   orient,noorient
   geometry={
   Ne,,0.0,0.0,0.0
   Ar,,0.0,0.0,6.5}
   basis={
   set,orbital; default,avtz         !for orbitals
   set,jkfit;   default,avtz/jkfit   !for JK integrals
   set,mp2fit;  default,avtz/mp2fit  !for E2disp/E2exch-disp
   set,dflhf;   default,avtz/jkfit   !for LHF
   }
   
   !=========delta(HF) contribution for higher order interaction terms====
   ca=2101.2; cb=2102.2 !sapt files
   
   !dimer
   {df-hf,basis=jkfit,locorb=0}
   edm=energy
   
   !monomer A
   dummy,ar
   {df-hf,basis=jkfit,locorb=0; save,$ca}
   ema=energy
   {sapt;monomerA}
   
   !monomer B
   dummy,ne
   {df-hf,basis=jkfit,locorb=0; save,$cb}
   emb=energy
   {sapt;monomerB}
   
   !interaction contributions
   {sapt,Sinf=0,SAPT_LEVEL=2;intermol,ca=$ca,cb=$cb,icpks=1,fitlevel=3
   dfit,basis_coul=jkfit,basis_exch=jkfit,cfit_scf=3}
   
   !calculate high-order terms by subtracting 1st+2nd order energies
   eint_hf=(edm-ema-emb)*1000 mH
   delta_hf=eint_hf-e1pol-e1ex-e2ind-e2exind
   
   !=========DFT-SAPT at second order intermol. perturbation theory====
   ca=2103.2; cb=2104.2 !sapt files;
   
   !shifts for asymptotic correction to xc potential
   eps_homo_pbe0_ar=-0.440936      !HOMO(Ar)/PBE0 functional
   eps_homo_pbe0_ne=-0.589207      !HOMO(Ne)/PBE0
   ip_ar=0.5792                    !exp. ionisation potential
   ip_ne=0.7925                    !exp. ionisation potential
   shift_ar=ip_ar+eps_homo_pbe0_ar !shift for bulk xc potential (Ar)
   shift_ne=ip_ne+eps_homo_pbe0_ne !shift for bulk xc potential (Ne)
   
   !monomer A, perform LPBE0AC calculation
   dummy,ar
   {df-ks,pbex,pw91c,lhf; dftfac,0.75,1.0,0.25; asymp,shift_ne; save,$ca}
   {sapt;monomerA}
   
   !monomer B, perform LPBE0AC calculation
   dummy,ne
   {df-ks,pbex,pw91c,lhf; dftfac,0.75,1.0,0.25; start,atdens; asymp,shift_ar; save,$cb}
   {sapt;monomerB}
   
   !interaction contributions
   {sapt,Sinf=0,SAPT_LEVEL=3;intermol,ca=$ca,cb=$cb,icpks=0,fitlevel=3,nlexfac=0.0
   dfit,basis_coul=jkfit,basis_exch=jkfit,cfit_scf=3}
   
   !add high-order approximation to obtain the total interaction energy
   eint_dftsapt=e12tot+delta_hf

.. _symmetry-adapted_intermolecular_perturbation_theory--options:

Options
-------

* ``SAPT_LEVEL`` Set to 1 for first-order terms (:math:`E_{\text{pol}}^{(1)}` and :math:`E_{\text{exch}}^{(1)}`), to 2 for additional second order (exchange-)induction terms (:math:`E_{\text{ind}}^{(2)}` and :math:`E_{\text{exch-ind}}^{(2)}`) and 3 for all first- and second-order terms (including then also :math:`E_{\text{disp}}^{(2)}` and :math:`E_{\text{exch-disp}}^{(2)}`) (default 3)
* ``SINF`` Set to 0 to calculate exchange interaction energies within the :math:`S^2` approximation and to 1 for calculating all exchange terms with an infinite overlap expansion (default 1).
* ``SAPT_FITLEVEL`` Level of density fitting approximations in SAPT which can have values 0 to 3 (default 0)
* ``SAPT_ICPKS`` Switch between iterative (=1) and non-iterative (=0) solution of coupled-perturbed Kohn-Sham equations (default 0)
* ``SAPT_CPKSTHR`` Threshold for density matrix convergency in the coupled-perturbed Kohn-Sham program (default 1.d-6).
* ``SAPT_CPKMAXIT`` Maximum number of iterations in the coupled-perturbed Kohn-Sham program (default 50).
* ``SAPT_FROZENA`` Number of frozen electrons in the response calculations for monomer A (default 0)
* ``SAPT_FROZENB`` see above

The following parameters are of importance if ``SAPT_FITLEVEL``\ :math:`>`\ 0:

* ``SAPT_NFRQ_DISP`` Number of frequencies for the Casimir-Polder integration (default 10)
* ``SAPT_NORM_DISP`` Norm for the density fitting which can be either ``COULOMB`` or ``NATURAL`` (default ``COULOMB``)
* ``SAPT_DISP_N4`` Can speedup the calculation of the dispersion energy by :math:`N^4` scaling (default 1)
* ``THR_XCKERN`` Density threshold for the xc kernel matrix elements (default 1.d-8)
* ``FIT_XCKERN`` Fit both sides of the xc kernel (default 0)
* ``SAPT_DISK`` If 0 write all dimer amplitudes to file, if 1 write 3-index response propagators to file and if 2 write 3-index response propagators compressed to file. The latter two variants save disk space but need more CPU time to compute :math:`E^{(2)}_{\text{exch-disp}}` (default 0)
* ``COMPRESS_THR`` If ``SAPT_DISK``\ =2 this value determines the compression cutoff (default 1d-12)
* ``UNCOUPLED`` If ``SAPT_DISK``\ :math:`>`\ 0 calculate also uncoupled (exchange-)dispersion energies (default false)
* ``THRAO`` Threshold for AO 3-index integrals (default 1.d-12)
* ``THRMO`` Threshold for MO 3-index integrals (default 1.d-8)
* ``THROV`` Threshold for AO 2-index integrals (default 1.d-10)
* ``THRPROD`` Product threshold for first half transformation (default 1.d-8)
* ``THRSW`` Threshold for Schwarz screening (default 1.d-5)
* ``C6`` Calculate dispersion coefficients for the two monomers (Note that the full dimer basis set is used in each case and that a closer distance of the monomers can perturb the result).
* ``XCKERN_NBLOCK`` number of grid points treated together as a block for (aux\ :math:`|`\ f\ :math:`_{\text{xc}}|`\ occ\ :math:`\times`\ virt) integrals (default 128)
* ``CFAC`` factor for VWN correlation in ALDA xc-kernel (default 1.d0)
* ``SAPT_QUAD`` quadrature type in frequency integration (0: Chebyshev, 1: Gauss-Legendre (default))
* ``W0`` parameter in Gauss-Legendre quadrature (default 2.d0)
* ``GRIDTHR`` Threshold for grid accuracy in some routines which generate xc-kernel integrals.
* ``THRDUM`` Threshold for density calculated at dummy function gridpoints (which can serve as a singularity correction for the calculation of the XC kernel matrix) (default: ``1d-12``).
* ``LSING`` Singularity correction for XC kernel matrix (default: ``.false.``)
* ``DF2`` Logical switch for new DF routines. Note that with ``DF2=.true.`` the exchange interaction contributions are only calculated without the single-exchange approximation. (default: ``.false.``)
* ``DF2MOD`` Controls calculation mode of :math:`E^{(2)}_{\text{DISP}}`: with ``DF2MOD=0`` all 3idx integrals are calculated and stored on disk in advance. In case of ``DF2MOD=1`` this is done in two subsequent steps at the expense, however, of the fact that then the amplitudes have to be constructed twice. (default: ``0``)
* ``X0THR`` SVD threshold for inversion of :math:`\chi_0` if EXX kernel used (default: ``1d-8``)
* ``NAUX_MAX`` Maximal length of auxiliary function batches in EXX kernel routine (default: ``50``).
* ``PVVDISK`` Write :math:`(P|ab)` ints to disk in EXX kernel calculation. This can speed up the calculation on the expense of the disk space requirements (scaling as: :math:`N_{\text{aux}}^A` :math:`\times N_{\text{vir}}^A` :math:`\times (N_{\text{vir}}^A+1)/2` :math:`+N_{\text{aux}}^B` :math:`\times N_{\text{vir}}^B` :math:`\times (N_{\text{vir}}^B+1)/2` (default=\ ``.false.``).

The last threshold values for the 2- and 3-index integrals should not be set higher in density fitting calculations as this can cause lower accuracies in the interaction terms. In addition SAPT knows the following subcommands:

* ``MONOMERA`` Stores informations (like number of electrons, etc.) about previous monomer A calculation
* ``MONOMERB`` See above
* ``INTERMOL`` Starts the SAPT calculation

``INTERMOL`` may have the following subkeywords:

* ``CA`` Record number of wave function for monomer A (always needed)
* ``CB`` Record number of wave function for monomer B (always needed)
* ``SAPTLEVEL`` See above
* ``FITLEVEL`` See above
* ``ICPKS`` See above
* ``FROZA`` See above
* ``FROZB`` See above
* ``NLEXFAC`` Amount of nonlocal exact exchange in hybrid DFT-SAPT calculations
* ``CPKSTHR`` Threshold for density matrix convergency in the coupled-perturbed Kohn-Sham program.
* ``CPKSMAXIT`` Maximum number of iterations in the coupled-perturbed Kohn-Sham program.

.. _symmetry-adapted_intermolecular_perturbation_theory--dfsapt-a-density-fitting-dft-sapt-program-for-arbitrary-monomer-basis-sets:

DFSAPT: a density-fitting DFT-SAPT program for arbitrary monomer basis sets
---------------------------------------------------------------------------

DFSAPT is an alternative density-fitting DFT-SAPT program which works with arbitrary monomer basis sets and which can be used for extended dimer systems of about 800 electrons, see Ref.[8].

For a standard DFSAPT calculation using a dimer centered basis set the Molpro input file looks very similar to a corresponding DF-DFT-SAPT calculation, see `DFSAPT calculation of the water dimer using a DCBS basis set <symmetry-adapted_intermolecular_perturbation_theory.html#dfsapt-calculation-of-the-water-dimer-using-a-dcbs-basis-set>`__. There are, however, two important points to be taken care of:

* **\*\*important #1**\*\* Set ``oldnorm=1`` before any call to the DFSAPT program.
* **\*\*important #2**\*\* Add numbers to atom labels in the geometry blocks. These have to have a subsequent ordering, see examples in `DFSAPT calculation of the water dimer using a DCBS basis set <symmetry-adapted_intermolecular_perturbation_theory.html#dfsapt-calculation-of-the-water-dimer-using-a-dcbs-basis-set>`__ to `DFSAPT calculation of the water dimer with additional d(HF) correction <symmetry-adapted_intermolecular_perturbation_theory.html#dfsapt-calculation-of-the-water-dimer-with-additional-d-hf-correction>`__.

A corresponding calculation, in which the water monomers are calculated in their own local basis set (monomer centered basis set calculation) is presented in `DFSAPT calculation of the water dimer using an MCBS basis set <symmetry-adapted_intermolecular_perturbation_theory.html#dfsapt-calculation-of-the-water-dimer-using-an-mcbs-basis-set>`__. Note, however, that very large basis sets are required to converge the individual interaction energy contributions. In order to improve the basis set convergence, additional midbond functions can be added as is exemplified in `DFSAPT calculation of the water dimer using an MC+BS basis set <symmetry-adapted_intermolecular_perturbation_theory.html#dfsapt-calculation-of-the-water-dimer-using-an-mc-bs-basis-set>`__. Here the def2-TZVP basis functions for the Neon atom were positioned in between the O\ :math:`\cdots`\ H hydrogen bridge.

A complete (DCBS) DFSAPT calculation with additional :math:`\delta`\ (HF) correction and using the PBE0AC(BRJ) xc potential (with automatic asymptotic correction) is shown in section `DFSAPT calculation of the water dimer with additional d(HF) correction <symmetry-adapted_intermolecular_perturbation_theory.html#dfsapt-calculation-of-the-water-dimer-with-additional-d-hf-correction>`__.

Note that in contrast to the DFT-SAPT/DF-DFT-SAPT programs the exchange-dispersion energy is not calculated on the coupled level. Instead, the coupled :math:`E^{(2)}_{exch-disp}` energies are estimated by scaling the uncoupled ones with a factor which has been obtained from a linear fit to exact results, see Ref.[8].

The following list shows all options which can be used with the DFSAPT program:

* ``E1P`` Calculate :math:`E^{(1)}_{pol}` (default: ``1``).
* ``E1X`` Calculate :math:`E^{(1)}_{exch}` (default: ``1``).
* ``E2I`` Calculate :math:`E^{(2)}_{ind}` (default: ``0``).
* ``E2XI`` Calculate :math:`E^{(2)}_{exch-ind}` (default: ``0``).
* ``E2D`` Calculate :math:`E^{(2)}_{disp}` (default: ``0``).
* ``E2XD`` Calculate :math:`E^{(2)}_{exch-disp}` (default: ``0``).
* ``ALL`` Calculate all SAPT contributions (up to 2nd order) (default: ``0``).
* ``AUXBAS`` Auxiliary basis set (default: ``MP2FIT``).
* ``NFREQ`` Number of frequencies for computing the monomer response matrices (default: ``10``).
* ``GRIDTHR`` Threshold for grid accuracy (default: ``1d-10``).
* ``THRKERN`` Threshold for density in xc kernel calculation (default: ``1d-12``).
* ``PRINT`` Print flag (default: ``0``).
* ``W0`` Value effects Gauss-Legendre quadrature for computing the response function (see Amos,Handy,Knowles,Rice,Stone,\ *J. Phys.Chem.* **89** (1985) 2186) (default: ``2d0``)
* ``FEXX`` Exact exchange factor in response calculations (default: ``0d0``).
* ``FXC`` Exchange-correlation factor in response calculations (default: ``0d0``).
* ``FCOUL`` Coulomb contribution factor in response calculations (default: ``1d0``).
* ``XFAC`` Exchange factor in XC kernel (default: ``1d0``).
* ``CFAC`` Correlation factor in XC kernel (default: ``1d0``).
* ``AUXMAX`` Maximum block size of auxiliary function space for three-index integrals of the type (aux\ :math:`|`\ orb.orb) (default: ``50``).
* ``MOMAX`` Maximum block size of orbital function space for three-index integrals of the type (orb\ :math:`|`\ orb.aux) (default: ``50``).
* ``FXCSING`` Singularity correction for XC kernel matrix (default: ``0``)
* ``THRDUM`` Threshold for density calculated at dummy function gridpoints (which can serve as a singularity correction for the calculation of the XC kernel matrix) (default: ``1d-4``).
* ``COMP`` Write 3-index integrals compressed to disk (to save disk space) (default: ``0``).
* ``THRC`` Threshold for 3-index integral calculations (integrals which are smaller than the given threshold are not written to disk) (default: ``1d-10``).
* ``MINB`` Minimal bytelength for integral compression (default: ``1``).
* ``MODE`` Switch for alternative DFSAPT driver which can use integral compression (to be evoked by ``MODE=2``) (default: ``1``).
* ``FXCFIT`` Use density fitting for computation of XC contributions in CPKS calculation (default: ``0``).
* ``CPKS`` Switch for different CPKS solvers (default: ``1``).
* ``CDIRECT`` Use integral direct algorithm for computing the (exact) exchange contributions in CPKS calculations, otherwise integrals of the type (aux\ :math:`|`\ vir.vir) are written to disk (default: ``0``).
* ``MAXIT`` Maximum number of interactions in CPKS (default: ``60``).
* ``THRCG`` Threshold for CG/GMRES solver in CPKS calculations (default: ``1d-8``).
* ``NSYSOLVE`` Switch for BiCG (``NSYSOLVE=1``) or GMRES (``NSYSOLVE=2``) solver in CPKS calculations (default: ``2``).
* ``NSUB`` Subspace size in GMRES solver (default: ``50``).
* ``T678`` Switch for 3 different computation modes for :math:`E^{(2)}_{exch-disp}`. ``T678=3`` is recommended for the calculation of large systems but requires more disk space to store intermediate quantities (default: ``1``).
* ``TDEXX`` set to 1 for using the adiabatic TDEXX kernel and to 2 for using the nonadiabatic TDEXX kernel
* ``TDEXXFAC`` prefactor for TDEXX response kernel
* ``X0THR`` threshold for SVD inversion of the KS response matrix
* ``KERNMOD`` if set to 1, DFSAPT computes (aux\ :math:`|`\ virt\ :math:`\times`\ virt) integrals for use in the TDEXX kernel calculation and stores them on disk. If set to 2, these integrals are directly contracted to reduce I/O operations.
* ``RESTART`` when set to 1, integral records are not deleted and can be used for subsequent calculations. This is possible by using ``RESTART=2``.
* ``PLUSOV`` take terms that contain :math:`\langle occ|v_x^{\text{NL}}-v_x|virt\rangle` matrix elements into account in the calculation of the kernel (normally very small)

The DFSAPT program can also be used to compute the monomer response functions within the exact-exchange Kohn-Sham response (TDEXX) approach, see section `using exact exchange Kohn-Sham response kernels <symmetry-adapted_intermolecular_perturbation_theory.html#using-exact-exchange-kohn-sham-response-kernels>`__. As in the standard DFT-SAPT program, the :math:`\langle i|v_x^{\text{NL}}-v_x|j\rangle` have to be computed for each monomer using the OEP program (section `optimised Effective Potential (OEP) method <the_density_functional_program.html#optimised-effective-potential-oep-method>`__). An input template for this would be given by:

.. code-block:: text

   dummy,<atoms on B> !monomer A
   {df-ks,lda; save,2100.2; start,atdens}
   {exxhyb,orb=2100.2,oep=7,homo=1,charge=1,maxit=30,scfthr=1d-9,add=1,\
           xfac=0.25,shift=1,dfit=1
   func,pbex,pbec; dftfac,0.75,1.0}
   {oep,orb=2101.2,vxdiff=5100.2,gamma=3d-4,dfit=1,homo=1}
   {sapt;monomerA}
   
   dummy,<atoms on A> !monomer B
   {ks,lda; save,2200.2; start,atdens}
   {exxhyb,orb=2200.2,oep=7,homo=1,charge=1,maxit=30,scfthr=1d-9,add=1,\
           xfac=0.25,shift=1,dfit=1
   func,pbex,pbec; dftfac,0.75,1.0}
   {oep,orb=2201.2,vxdiff=5200.2,gamma=3d-4,dfit=1,homo=1}
   {sapt;monomerB}
   
   dfsapt,all=1,fcoul=1.0,fxc=1.0,cpks=2,x0thr=1d-8,tdexx=2,nfreq=10, \
          tdexxfac=1d0,kernmod=1,auxmax=100

which again presents an example where the orbitals of the monomers are calculated with the LPBE0AC xc potential. All publications resulting from DFSAPT calculations employing the (A)TDEXX response kernel should cite Ref. [9].

.. _symmetry-adapted_intermolecular_perturbation_theory--dfsapt-calculation-of-the-water-dimer-using-a-dcbs-basis-set:

DFSAPT calculation of the water dimer using a DCBS basis set
============================================================

.. code-block:: text
   :caption: examples/h2o_2-dfsapt.inp

   ***,h2o-dimer DCBS
   gthresh,energy=1.d-8,orbital=1.d-8,grid=1.d-8
   oldnorm=1
   ca=2101.2
   cb=2102.2
   
   basis={
   set,orbital
   default,def2-tzvpp
   set,mp2fit
   default,def2-tzvpp/mp2fit}
   
   symmetry,nosym
   angstrom
   geometry={
    1,O1,,  -1.551007,  -0.114520,   0.000000
    2,H2,,  -1.934259,   0.762503,   0.000000
    3,H3,,  -0.599677,   0.040712,   0.000000
    4,O4,,   1.350625,   0.111469,   0.000000
    5,H5,,   1.680398,  -0.373741,  -0.758561
    6,H6,,   1.680398,  -0.373741,   0.758561}
   
   dummy,4,5,6
   {ks,pbe; save,$ca}
   monomerA,orb=$ca,core=1
   
   dummy,1,2,3
   {ks,pbe; start,atdens; save,$cb}
   monomerB,orb=$cb,core=1
   
   {grid,gridthr=1d-8}
   dfsapt,all=1,fcoul=1.0,fxc=1.0

.. _symmetry-adapted_intermolecular_perturbation_theory--dfsapt-calculation-of-the-water-dimer-using-an-mcbs-basis-set:

DFSAPT calculation of the water dimer using an MCBS basis set
=============================================================

.. code-block:: text
   :caption: examples/h2o_2-mc-dfsapt.inp

   ***,h2o-dimer MCBS
   gthresh,energy=1.d-8,orbital=1.d-8,grid=1.d-8
   oldnorm=1
   ca=2101.2
   cb=2102.2
   
   symmetry,nosym
   angstrom
   noorient
   geometry={
    1,O1,,  -1.551007,  -0.114520,   0.000000
    2,H2,,  -1.934259,   0.762503,   0.000000
    3,H3,,  -0.599677,   0.040712,   0.000000}
   basis={set,orbital; default,def2-tzvpp}
   
   {ks,pbe; save,$ca}
   monomerA,orb=$ca,core=1
   
   symmetry,nosym
   angstrom
   noorient
   geometry={
    4,O4,,   1.350625,   0.111469,   0.000000
    5,H5,,   1.680398,  -0.373741,  -0.758561
    6,H6,,   1.680398,  -0.373741,   0.758561}
   
   {ks,pbe; start,atdens; save,$cb}
   monomerB,orb=$cb,core=1
   
   symmetry,nosym
   angstrom
   noorient
   geometry={
    1,O1,,  -1.551007,  -0.114520,   0.000000
    2,H2,,  -1.934259,   0.762503,   0.000000
    3,H3,,  -0.599677,   0.040712,   0.000000
    4,O4,,   1.350625,   0.111469,   0.000000
    5,H5,,   1.680398,  -0.373741,  -0.758561
    6,H6,,   1.680398,  -0.373741,   0.758561}
   
   basis={
   set,orbital; default,def2-tzvpp
   set,jkfit;   default,def2-tzvpp/jkfit
   set,mp2fit;  default,def2-tzvpp/mp2fit}
   
   {grid,gridthr=1d-8}
   dfsapt,all=1,fcoul=1.0,fxc=1.0

.. _symmetry-adapted_intermolecular_perturbation_theory--dfsapt-calculation-of-the-water-dimer-using-an-mc-bs-basis-set:

DFSAPT calculation of the water dimer using an MC+BS basis set
==============================================================

.. code-block:: text
   :caption: examples/h2o_2-mcplus-dfsapt.inp

   ***,h2o-dimer MC+BS
   gthresh,energy=1.d-8,orbital=1.d-8,grid=1.d-8
   oldnorm=1
   ca=2101.2
   cb=2102.2
   basis={set,orbital; default,def2-tzvpp}
   
   symmetry,nosym
   angstrom
   noorient
   geometry={
    1,O1,,  -1.551007,  -0.114520,   0.000000
    2,H2,,  -1.934259,   0.762503,   0.000000
    3,H3,,  -0.599677,   0.040712,   0.000000
    4,Ne7,,  0.375474,   0.076091,   0.000000}
   dummy,ne7
   {ks,pbe; save,$ca}
   monomerA,orb=$ca,core=1
   
   symmetry,nosym
   angstrom
   noorient
   geometry={
    4,O4,,   1.350625,   0.111469,   0.000000
    5,H5,,   1.680398,  -0.373741,  -0.758561
    6,H6,,   1.680398,  -0.373741,   0.758561
    7,Ne7,,  0.375474,   0.076091,   0.000000}
   dummy,ne7
   {ks,pbe; start,atdens; save,$cb}
   monomerB,orb=$cb,core=1
   
   symmetry,nosym
   angstrom
   noorient
   geometry={
    1,O1,,  -1.551007,  -0.114520,   0.000000
    2,H2,,  -1.934259,   0.762503,   0.000000
    3,H3,,  -0.599677,   0.040712,   0.000000
    4,O4,,   1.350625,   0.111469,   0.000000
    5,H5,,   1.680398,  -0.373741,  -0.758561
    6,H6,,   1.680398,  -0.373741,   0.758561
    7,Ne7,,  0.375474,   0.076091,   0.000000}
   basis={
   set,orbital; default,def2-tzvpp
   set,jkfit;   default,def2-tzvpp/jkfit
   set,mp2fit;  default,def2-tzvpp/mp2fit}
   
   dummy,ne7
   {grid,gridthr=1d-8}
   dfsapt,all=1,fcoul=1.0,fxc=1.0

.. _symmetry-adapted_intermolecular_perturbation_theory--dfsapt-calculation-of-the-water-dimer-with-additional-d-hf-correction:

DFSAPT calculation of the water dimer with additional d(HF) correction
======================================================================

.. code-block:: text
   :caption: examples/h2o_2-dfsapt2.inp

   gdirect
   gthresh,energy=1d-8,orbital=1d-7,grid=1d-8
   symmetry,nosym
   angstrom
   geometry={
    1,O1,,  -1.551007,  -0.114520,   0.000000
    2,H2,,  -1.934259,   0.762503,   0.000000
    3,H3,,  -0.599677,   0.040712,   0.000000
    4,O4,,   1.350625,   0.111469,   0.000000
    5,H5,,   1.680398,  -0.373741,  -0.758561
    6,H6,,   1.680398,  -0.373741,   0.758561}
   basis={
   set,orbital; default,avdz
   set,jkfit;   default,avdz/jkfit
   set,mp2fit;  default,avdz/mp2fit}
   oldnorm=1
   ca=2110.2; cb=2120.2
   nkerna=1;  nkernb=1
   
   {df-hf,basis=jkfit; save,2100.2}
   edm_hf=energy
   
   dummy,4,5,6
   {df-hf,basis=jkfit; save,$ca; start,atdens}
   ema_hf=energy
   monomerA,orb=$ca,core=$nkerna
   
   dummy,1,2,3
   {df-hf,basis=jkfit; save,$cb; start,atdens}
   emb_hf=energy
   monomerB,orb=$cb,core=$nkernb
   
   {grid,gridthr=1d-6}
   {dfsapt,e1p=1,e1x=1,e2i=1,e2xi=1,auxbas='jkfit',fexx=1.0,fcoul=1.0,mode=1,cdirect=1,thrcg=1d-6}
   {grid,gridthr=1d-8}
   
   eint_hf=(edm_hf-ema_hf-emb_hf)*1000e0 mH
   delta_hf=eint_hf-e12tot
   
   dummy,4,5,6
   lxgamma=1.15
   {df-ks,lxbecke,pbex,pbec,basis=jkfit; dftfac,0.25,0.75,1.0; asymp,0d0; save,$ca; start,atdens}
   monomerA,orb=$ca,core=$nkerna
   
   dummy,1,2,3
   lxgamma=1.15
   {df-ks,lxbecke,pbex,pbec,basis=jkfit; dftfac,0.25,0.75,1.0; asymp,0d0; save,$cb; start,atdens}
   monomerB,orb=$cb,core=$nkernb
   
   {grid,gridthr=1d-6}
   {dfsapt,all=1,auxbas='mp2fit',fxc=1.0,fcoul=1.0,mode=1,cpks=2,fxcfit=1,fxcsing=1,t678=3}
   eint_sapt=e12tot+delta_hf

.. _symmetry-adapted_intermolecular_perturbation_theory--sapt-ccsd:

SAPT(CCSD)
----------

SAPT with monomers described on the CCSD level is available for small complexes. In SAPT(CCSD) monomer density matrices and density-density matrix response functions from expectation-value CCSD theory are utilized. A high cost of SAPT(CCSD) results from the necessity of calculation of the CCSD response functions. Cumulant contributions from two-electron density matrices for :math:`E_{\text{exch}}^{(1)}` and :math:`E_{\text{exch-ind}}^{(2)}` are also available. The calculations can be performed for dimer-centered or monomer-centered-plus basis sets (the latter for all components but :math:`E^{(2)}_{\text{exch-disp}}`). :math:`E^{(2)}_{\text{disp}}` and :math:`E^{(2)}_{\text{exch-disp}}` are usually calculated from density-fitted response functions in order to reduce the CPU time (from :math:`{\cal O}({\cal N}^8)` to :math:`{\cal O}({\cal N}^7)`, where :math:`{\cal N}` is the molecular size). Note that :math:`E^{(2)}_{\text{disp}}` and :math:`E^{(2)}_{\text{exch-disp}}` are calculated separately from other SAPT components. It is important to note that SAPT(CCSD) and DFT-SAPT from Chapter `introduction <symmetry-adapted_intermolecular_perturbation_theory.html#introduction>`__ are completely different codes.

References:

**Review of SAPT(CCSD):**
:math:`[1]` T. Korona, in *Recent Progress in Coupled Cluster Methods*, Eds. P. Čársky, J. Paldus, J. Pittner, Springer-Verlag (2010), *Coupled cluster treatment of intramonomer correlation effects in intermolecular interactions*, p. 267
:math:`[2]` T. Korona, M. Przybytek, B. Jeziorski, `Mol. Phys. <https://dx.doi.org/10.1080/00268970600673975>`__ **104**, 2303 (2006)
:math:`[3]` T. Korona, B. Jeziorski, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.2364489>`__ **125**, 184109 (2006)
:math:`[4]` T. Korona, B. Jeziorski, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.2889006>`__ **128**, 144107 (2008)
:math:`[5]` T. Korona, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.2933312>`__ **128**, 224104 (2008)
:math:`[6]` T. Korona, `Phys. Chem. Chem. Phys. <https://dx.doi.org/10.1039/B804513E>`__ **10**, 5698 (2008)
:math:`[7]` T. Korona, `Phys. Chem. Chem. Phys. <https://dx.doi.org/10.1039/B807329E>`__ **10**, 6509 (2008)
:math:`[8]` T. Korona, `J. Chem. Theory Comput. <https://dx.doi.org/10.1021/ct900232j>`__ **5**, 2663 (2009)

.. _symmetry-adapted_intermolecular_perturbation_theory--mp2-coupled-mp2c:

MP2-coupled (MP2C)
------------------

The standard second-order Møller-Plesset perturbation theory (MP2) method fails to describe long-range correlation energies accurately. The reason for this stems from the fact that the MP2 method does not take into account intramolecular correlation effects of two interacting monomers, i.e., describes dispersion interactions on an uncoupled Hartree-Fock level [1]. To remedy this, the supermolecular MP2 interaction energy can be corrected in a hybrid supermolecular-perturbation theory approach by subtracting the uncoupled HF (UCHF) dispersion energy and adding the dispersion energy from a more accurate response theory method instead. In the MP2C (MP2 coupled) method, the latter is computed using the time-dependent density-functional theory (TDDFT) approach employing static response functions from the EXX method and coupled response functions computed by using the ALDA exchange kernel:

.. math::

   \Delta E_{\text{int}}^{\text{MP2C}}=\Delta E_{\text{int}}^{\text{MP2}}
                          -E_{\text{disp}}^{(20)}[\mbox{UCHF}]
                          +E_{\text{disp}}^{(2)}[\mbox{TDDFT}]

In Molpro, MP2C calculations can be performed with the aid of the TDDFT module that computes frequency-dependent coupled or uncoupled response functions. Using the LHF (Local Hartree-Fock) method (section `local Hartree-Fock (LHF) method <the_density_functional_program.html#local-hartree-fock-lhf-method>`__) an input for computing the MP2C interaction energy could read (using density-fitting within the HF/MP2 calculations and using 10 frequency integration points)

.. code-block:: text

   basis={
   set,orbital; default,<basis>
   set,jkfit;   default,<basis>/jkfit
   set,mp2fit;  default,<basis>/mp2fit
   set,dflhf;   default,<basis>/jkfit
   set,tddft;   default,<basis>/mp2fit}
   
   {df-hf,basis=jkfit}  !Dimer
   {df-mp2}
   edm_mp2=energy
   
   dummy,<dummy atoms>  !Monomer A
   {df-hf,basis=jkfit; save,<recordA>}
   {df-mp2}
   ema_mp2=energy
   {dftresp; respmat,orb=<recordA>,save=<xarec>,order=0,nfreq=10,ncore=<coreA>,init=1}
   
   dummy,<dummy atoms>  !Monomer B
   {df-hf,basis=jkfit; save,<recordB>}
   {df-mp2}
   ema_mp2=energy
   {dftresp; respmat,orb=<recordB>,save=<xbrec>,order=0,nfreq=10,ncore=<coreB>}
   
   {dftresp; disp}
   edisp_uhf=e2disp  !uncoupled dispersion energy
   
   
   dummy,<dummy atoms>  !Monomer A
   {cfit,basis=jkfit,locorb=0}
   dflhf,orb=<recordA>,lhffit=1
   {dftresp; respmat,orb=<recordA+1>,save=<xarec+1>,nfreq=10,ncore=<coreA>,cfac=0.0,init=1}
   
   dummy,<dummy atoms>  !Monomer B
   {cfit,basis=jkfit,locorb=0}
   dflhf,orb=<recordB>,lhffit=1
   {dftresp; respmat,orb=<recordB+1>,save=<xbrec+1>,nfreq=10,ncore=<coreB>,cfac=0.0}
   
   {dftresp; disp}
   edisp_lhf=e2disp  !coupled dispersion energy
   
   esup_mp2disp=esup_mp2+(-edisp_uhf+edisp_lhf)*1000.0 mH
   show,esup_mp2        !MP2 interaction energy
   show,edisp_uhf       !uncoupled dispersion energy
   show,edisp_lhf       !coupled dispersion energy
   show,esup_mp2disp    !MP2C interaction energy

Notice that in the basis input section a number of basis sets have to be specified for the different parts in the calculation.

Alternatively, the MP2C method can also be used in combination with the OEP method described in section `optimised Effective Potential (OEP) method <the_density_functional_program.html#optimised-effective-potential-oep-method>`__. In this case, the latter part where the coupled dispersion energy is calculated would have to be replaced by something like:

.. code-block:: text

   dummy,<dummy atoms>  !Monomer A
   {cfit,basis=jkfit,locorb=0}
   oep,orb=<recordA>,gamma=3d-4,dfit=1
   {dftresp; respmat,orb=<recordA+1>,save=<xarec+1>,nfreq=10,core=<coreA>,cfac=0.0,init=1}
   
   dummy,<dummy atoms>  !Monomer B
   {cfit,basis=jkfit,locorb=0}
   oep,orb=<recordB>,gamma=3d-4,dfit=1
   {dftresp; respmat,orb=<recordB+1>,save=<xbrec+1>,nfreq=10,core=<coreB>,cfac=0.0}

The ``TDDFT`` program used to compute the response functions can have the following further options:

* **ORB** record containing orbital coefficients (mandatory)
* **SAVE** record number used to save the response matrix (in the auxiliary basis) for each frequency
* **ORDER** can be used to denote the order of the electron-electron interaction that is taken into account in the calculation of the response matrix, so ``ORDER=0`` corresponds to the uncoupled case. If set to a negative value (default) the electron-electron interactions are taken into account through infinite order (fully coupled case, the default setting)
* **NORM** may be used to change the fitting norm (default ’J’, should better not be changed)
* **3IDX** a logical flag (choices: 0/1) to specify if the xc-kernel matrix should be computed by using 3-indexed (aux\ :math:`|f_{\text{xc}}|`\ occ\ :math:`\times`\ virt) integrals
* **GRIDTHR** threshold for quadrature integration
* **GRIDFREE** set to :math:`\ne` 0 if the xc kernel matrix shall be computed with a gridfree approach (see Ref. [2]). This is more efficient but can be less accurate and is only recommended if used in conjunction with large auxiliary basis sets.
* **THRKERN** a threshold that is used to remove the singularities of the :math:`(P|f_{\text{xc}}|Q)` matrix, see Ref. [3]
* **XFAC** scaling factor of ALDA exchange
* **CFAC** scaling factor of ALDA correlation
* **INIT** set to :math:`\ne` 0 in order to initialise an MP2C calculation. In subsequent calculations (where ``INIT``\ =0) the response matrices are stored for each individual call to ``TDDFT``
* **NCORE** number of core orbitals
* **NBLOCK** number of batch points in the numerical integration
* **THRED** can be used to compress the size of the xc kernel values on the grid in order to increase the efficiency (experimental)
* **FCX3MOD** switch between different computation modes for the calculation of the (aux\ :math:`|f_{\text{xc}}|`\ occ\ :math:`\times`\ virt) integrals
* **FXC2MOD** switch between different computation modes for the calculation of the (aux\ :math:`|f_{\text{xc}}|`\ aux) integrals
* **THRDUM** when integrating over a dummy centre and when the electron density is lower than this value, skip the integration point (used to eliminate the singularities of the xc kernel
* **SING** set to :math:`\ne` 0 in order to employ a singularity correction to the xc kernel matrix (is used by default)
* **POL** print polarisabilities
* **ESHIFT** parameter :math:`\alpha` in Eq. (5) in Ref. [3]
* **FSCAL** parameter :math:`\beta` in Eq. (5) in Ref. [3]
* **MATINV** flag for choosing matrix inversion routine to take inverse of the metric matrix (1: LU decomposition and 2: SVD decomposition).
* **THRINV** threshold for SVD matrix inversion

All publications resulting from use of this program to compute MP2C interaction energies should acknowledge Refs. [1] and [2]. If the singularity correction to the xc kernel matrix is used, additionally also Ref. [3] can be cited.

Bibliography:
:math:`[1]` A. Heßelmann, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.2905808>`__ **128**, 144112 (2008)
:math:`[2]` M. Pitonak, A. Heßelmann, `J. Chem. Theory Comput. <https://dx.doi.org/10.1021/ct9005882>`__ **6**, 168 (2010)
:math:`[3]` A. Heßelmann and T. Korona, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.4893990>`__ **141**, 094107 (2014).
