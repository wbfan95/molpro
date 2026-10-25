.. raw:: html

   <span id="input-from-ecp-library"></span>

.. _effective_core_potentials--effective-core-potentials:

Effective core potentials
=========================

Pseudopotentials (effective core potentials, ECPs) may be defined at the beginning of ``BASIS`` blocks.

The general form of the input cards is

``ECP,atom,[ECP specification]``

which defines a pseudopotential for an atom specified either by a chemical symbol or a group number. The *ECP specification* may consist either of a single keyword, which references a pseudopotential stored in the library, or else of an explicit definition (extending over several input cards), cf. below.

.. _effective_core_potentials--input-from-ecp-library:

Input from ECP library
======================

The basis set library presently contains the pseudopotentials and associated valence basis sets by a) the Los Alamos group (P. J. Hay and W. R. Wadt, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.448799>`__ **82**, 270 (1985) and following two papers), and b) the Stuttgart/Köln group (e.g., A. Nicklass, M. Dolg, H. Stoll and H. Preuß, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.468948>`__ **102**, 8942 (1995); for more details and proper references, `click here <http://www.tc.uni-koeln.de/PP/index.en.html>`__). Pseudopotentials a) are adjusted to orbital energies and densities of a suitable atomic reference state, while pseudopotentials b) are generated using total valence energies of a multitude of atomic states.

Library keywords in case a) are ``ECP1`` and ``ECP2``; ``ECP2`` is used when more than one pseudopotential is available for a given atom and then denotes the ECP with the smaller core definition. (For Cu, e.g., ``ECP1`` refers to an Ar-like 18\ :math:`e^-`-core, while ``ECP2`` simulates a Ne-like 10\ :math:`e^-` one with the :math:`3s` and :math:`3p` electrons promoted to the valence shell). For accurate calculations including electron correlation, promotion of all core orbitals with main quantum number equal to any of the valence orbitals is recommended.

Library keywords in case b) are of the form ``ECP``\ :math:`nXY`; :math:`n` is the number of core electrons which are replaced by the pseudopotential, :math:`X` denotes the reference system used for generating the pseudopotential (:math:`X=S`: states of the single-valence-electron ion; :math:`X=M`: states of the neutral atom and of ions with low charge), and :math:`Y` stands for the theoretical level of the reference data (:math:`Y=HF`: Hartree-Fock, :math:`Y=WB`: quasi-relativistic; :math:`Y=DF`: relativistic). For one- or two-valence electron atoms :math:`X=S`, :math:`Y=DF` is a good choice, while otherwise :math:`X=M`, :math:`Y=WB` (or :math:`Y=DF`) is recommended. (For light atoms, or for the discussion of relativistic effects, the corresponding :math:`Y=HF` pseudopotentials may be useful.) Additionally, spin-orbit (SO) potentials and core-polarization potentials (CPP) are available, to be used in connection with case b) ECPs, but these are not currently contained in the library, so explicit input is necessary here (cf. below).

In both cases, a) and b), the same keywords refer to the pseudopotential and the corresponding basis set, with a prefix ``MBS``-…in case a).

.. _effective_core_potentials--explicit-input-for-ecps:

Explicit input for ECPs
=======================

For each of the pseudopotentials the following information has to be provided:

* a card of the form

``ECP,atom,$n_{core},l_{max},l'_{max}$;\\``
where :math:`n_{core}` is the number of core electrons replaced by the pseudopotential :math:`V_{ps}`, :math:`l_{max}` is the number of semi-local terms in the scalar-relativistic part of :math:`V_{ps}`, while :math:`l'_{max}` is the corresponding number of terms in the SO part:

.. math::

   V_{ps}= -\frac{Z-n_{core}}{r} + V_{l_{max}}
             +\sum_{l=0}^{l_{max}-1} (V_l-V_{l_{max}}){\cal P}_{l}
             +\sum_{l=1}^{l'{max}} \Delta V_l {\cal P}_{l} \vec{l}\cdot\vec{s} {\cal P}_{l} ;

the semi-local terms (with angular-momentum projectors :math:`{\cal P}_{l}`) are supplemented by a local term for :math:`l=l_{max}`.
\* a number of cards specifying :math:`V_{l_{max}}`, the first giving the expansion length :math:`n_{l_{max}}` in

.. math::

   V_{l_{max}} = \sum_{j=1}^{n_{l_{max}}} c_j r^{m_j-2} e^{-\gamma _j r^2}

and the following :math:`n_{l_{max}}` ones giving the parameters in the form

.. math::

   m_1, \gamma _1, c_1; m_2, \gamma _2, c_2; \ldots

\* a number of cards specifying the scalar-relativistic semi-local terms in the order :math:`l=0,1,\ldots , l_{max}-1.` For each of these terms a card with the expansion length :math:`n_l` in

.. math::

   V_l -V_{l_{max}}=\sum_{j=1}^{n_l} c_j^l r^{m_j^l-2} e^{-\gamma _j^l r^2}

has to be given, and immediately following :math:`n_l` cards with the corresponding parameters in the form :math:`m_1^l, \gamma_1^l, c_1^l; m_2^l, \gamma_2^l, c_2^l;\ldots`

* analogously, a number of cards specifying the coefficients of the radial potentials :math:`\Delta V_l` of the SO part of :math:`V_{ps}`.

.. _effective_core_potentials--example-for-explicit-ecp-input:

Example for explicit ECP input
==============================

.. code-block:: text
   :caption: examples/cu_ecp_explicit.inp

   ***,CU
   ! SCF d10s1 -> d9s2 excitation energy of the Cu atom
   !  using the relativistic Ne-core pseudopotential
   ! and basis of the Stuttgart/Koeln group.
   gprint,basis,orbitals
   geometry={cu}
   basis
   ECP,1,10,3;   ! ECP input
    1; ! NO LOCAL POTENTIAL
    2,1.,0.;
    2; ! S POTENTIAL
    2,30.22,355.770158;2,13.19,70.865357;
    2; ! P POTENTIAL
    2,33.13,233.891976;2,13.22,53.947299;
    2; ! D POTENTIAL
    2,38.42,-31.272165;2,13.26,-2.741104;
   ! (8s7p6d)/[6s5p3d] BASIS SET
   s,1,27.69632,13.50535,8.815355,2.380805,.952616,.112662,.040486,.01;
   c,1.3,.231132,-.656811,-.545875;
   p,1,93.504327,16.285464,5.994236,2.536875,.897934,.131729,.030878;
   c,1.2,.022829,-1.009513;C,3.4,.24645,.792024;
   d,1,41.225006,12.34325,4.20192,1.379825,.383453,.1;
   c,1.4,.044694,.212106,.453423,.533465;
   end
   rhf;
   e1=energy
   {rhf;occ,4,1,1,1,1,1,1;closed,4,1,1,1,1,1;wf,19,7,1;}
   e2=energy
   de=(e2-e1)*toev  ! Delta E = -0.075 eV

.. _effective_core_potentials--example-for-ecp-input-from-library:

Example for ECP input from library
==================================

.. code-block:: text
   :caption: examples/auh_ecp_lib.inp

   ***,AuH
   ! CCSD(T) binding energy of the AuH molecule at r(exp)
   ! using the scalar-relativistic 19-valence-electron
   ! pseudopotential of the Stuttgart/Koeln group
   gprint,basis,orbitals;
   geometry={au}
   basis={
   ecp,au,ECP60MWB;              ! ECP input
   spd,au,ECP60MWB;c,1.2;        ! basis set
   f,au,1.41,0.47,0.15;
   g,au,1.2,0.4;
   spd,h,avtz;c;
   }
   rhf;
   {rccsd(t);core,1,1,1,,1;}
   e1=energy
   geometry={h}
   rhf
   e2=energy;
   rAuH=1.524 ang                ! molecular calculation
   geometry={au;h,au,rAuH}
   hf;
   {ccsd(t);core,2,1,1;}
   e3=energy
   de=(e3-e2-e1)*toev            ! binding energy = 3.11 eV
