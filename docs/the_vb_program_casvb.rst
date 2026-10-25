.. raw:: html

   <span id="casscf-projected-structure-coefficients"></span>

.. raw:: html

   <span id="controlling-the-amount-of-output"></span>

.. raw:: html

   <span id="defining-several-optimizations"></span>

.. raw:: html

   <span id="deleting-structures-from-the-optimization"></span>

.. raw:: html

   <span id="freezing-orbitals-in-the-optimization"></span>

.. raw:: html

   <span id="freezing-structure-coefficients-in-the-optimization"></span>

.. raw:: html

   <span id="guess-for-structure-coefficients"></span>

.. raw:: html

   <span id="multi-step-optimization"></span>

.. raw:: html

   <span id="number-of-iterations"></span>

.. raw:: html

   <span id="optimization-criterion"></span>

.. raw:: html

   <span id="orbital-guess"></span>

.. raw:: html

   <span id="orthogonality-constraints"></span>

.. raw:: html

   <span id="permuting-orbitals"></span>

.. raw:: html

   <span id="point-group-symmetry-and-constraints"></span>

.. raw:: html

   <span id="printing-weights-of-the-casscf-wavefunction-in-the-vb-basis"></span>

.. raw:: html

   <span id="printing-weights-of-the-valence-bond-structures"></span>

.. raw:: html

   <span id="read-orbitals-or-structure-coefficients"></span>

.. raw:: html

   <span id="recovering-casscf-ci-vector-and-vb-wavefunction"></span>

.. raw:: html

   <span id="saddle-point-optimization"></span>

.. raw:: html

   <span id="saving-the-vb-wavefunction"></span>

.. raw:: html

   <span id="selecting-the-spin-basis"></span>

.. raw:: html

   <span id="service-mode"></span>

.. raw:: html

   <span id="specifying-a-guess"></span>

.. raw:: html

   <span id="specifying-orbital-configurations"></span>

.. raw:: html

   <span id="spin-correlation-analysis"></span>

.. raw:: html

   <span id="symmetry-operations"></span>

.. raw:: html

   <span id="symmetry-relations-between-orbitals"></span>

.. raw:: html

   <span id="the-coeffs-keyword"></span>

.. raw:: html

   <span id="the-irreps-keyword"></span>

.. raw:: html

   <span id="the-symproj-keyword"></span>

.. raw:: html

   <span id="the-trans-keyword"></span>

.. raw:: html

   <span id="the-vb-program-casvb"></span>

.. raw:: html

   <span id="the-vbdump-directive"></span>

.. _the_vb_program_casvb--the-vb-program-casvb:

The VB program CASVB
====================

*CASVB* is a general program for valence bond calculations
written by T. Thorsteinsson and D. L. Cooper (1996–2005).

This program can be used in two basic modes:

* variational optimization of quite general types of nonorthogonal MCSCF or so-called modern valence bond wavefunctions;
* to generate representations of CASSCF wavefunctions in modern valence bond form, using overlap- (*relatively inexpensive*) or energy-based criteria.

In general, as in the spin-coupled generalized valence bond (SCGVB) approach, active orbitals are expanded in the full molecular basis set without locality constraints.

Key references:

T. Thorsteinsson, D. L. Cooper, J. Gerratt, P. B. Karadakov and M. Raimondi, `Theor. Chim. Acta <https://dx.doi.org/10.1007/s002140050158>`__ **93**, 343–366 (1996).
D. L. Cooper, T. Thorsteinsson and J. Gerratt,\ `Int. J. Quantum Chem. <https://dx.doi.org/10.1002/(SICI)1097-461X(1997)65:5%3C439::AID-QUA8%3E3.0.CO;2-X>`__ **65**, 439−451 (1997).
D.L. Cooper, T. Thorsteinsson and J. Gerratt, `Adv. Quantum Chem. <https://dx.doi.org/10.1016/S0065-3276(08)60406-2>`__ **32**, 51-67 (1998).

All publications resulting from use of this program should acknowledge relevant publications. There is a somewhat more complete *CASVB* bibliography at `https://pcwww.liv.ac.uk/~dlc/CASVB/ <https://pcwww.liv.ac.uk/~dlc/CASVB/>`__.

For a review of applications of SCGVB and SCGVB(*N*,\ *M*) calculations, see: T. H. Dunning, Jr., L. T. Xu, D. L. Cooper and P. B. Karadakov, `J. Phys. Chem. A <https://dx.doi.org/10.1021/acs.jpca.0c10472>`__ **125**, 2021-2050 (2021).

.. _the_vb_program_casvb--structure-of-the-input:

Structure of the input
======================

Most *CASVB* sub-commands may be abbreviated by four letters. The general input structure can be summarized as follows:

* For generating representations of CASSCF wavefunctions, the program is invoked by the command ``CASVB``. For variational optimization of wavefunctions it is normally invoked inside *MULTI* by the sub-command ``VB`` (see `optimizing valence bond wavefunctions <the_mcscf_program_multi.html#optimizing-valence-bond-wavefunctions>`__).
* Definition of the CASSCF wavefunction (not generally required).
* Definition of the valence bond wavefunction.
* Recovery and/or storage of orbitals and vectors.
* Manual input of starting guess (optional).
* Optimization control.
* Definition of molecular symmetry and possible constraints on the VB wavefunction.
* Wavefunction analysis.
* Further general options.

Items a) and b) should precede everything else in the input; apart from this, commands may come in any order.

.. _the_vb_program_casvb--defining-the-casscf-wavefunction:

Defining the CASSCF wavefunction
================================

When *MULTI* is run prior to *CASVB*, the CI vector must dumped using one of the directives ``SAVE, NATORB, CANONICAL,`` or ``LOCALI`` (see section `saving the CI vectors and information for a gradient calculation <the_mcscf_program_multi.html#saving-the-ci-vectors-and-information-for-a-gradient-calculation>`__). The three latter are recommended. Note that *CASVB* relies on the determinant part of *MULTI*. This means that when *MULTI* is run prior to *CASVB*, ``CONFIG,DET;`` should be used, whereas ``CONFIG,CSF;`` must *not* be.

.. _the_vb_program_casvb--the-vbdump-directive:

The VBDUMP directive
====================

``VBDUMP[,vbdump]``

If present, the ``VBDUMP`` card must occur first in the *CASVB* input. It is *not* required for variational calculations.

Note that in the majority of cases (*e.g.*, if a *CASVB* run occurs immediately after *MULTI*, or for variational calculations), explicit specification of dump records with *vbdump* is not required.

Wavefunction definitions may be restored here using ``VBDUMP`` cards (see also Section `saving wavefunction information for CASVB <the_mcscf_program_multi.html#saving-wavefunction-information-for-casvb>`__). The default record name (*vbdump*) is 4299.2. If a ``VBDUMP`` card is not present and record 4299.2 does not exist, then *CASVB* will attempt to generate the wavefunction information automatically based on the latest MCSCF calculation (however, ``STATE`` and ``WEIGHT`` information will not be restored in such a case).

.. _the_vb_program_casvb--other-wavefunction-directives:

Other wavefunction directives
-----------------------------

The definitions of the CASSCF wavefunction may also be specified manually using some or all of the directives:

* ``OCC`` Occupied orbitals.
* ``CLOSED`` Closed-shell orbitals.
* ``FROZEN`` Frozen-core orbitals.
* ``WF`` Wavefunction card.
* ``STATE`` Number of states for this wavefunction symmetry.
* ``WEIGHT`` Weights of states.

For the exact definition of these cards see sections `defining the orbital subspaces <the_mcscf_program_multi.html#defining-the-orbital-subspaces>`__ and `defining the optimized states <the_mcscf_program_multi.html#defining-the-optimized-states>`__. These commands may also be used to modify the values defined in ``VBDUMP``. The information given on these cards should correspond to the CI vector saved in the CASSCF calculation. The cards, and their ordering, should therefore coincide with those used in *MULTI*, except for the ``WEIGHT`` cards which may differ. At present, the VB wavefunction must correspond to a well-defined number of electrons and total spin. Other states may be present, but an error condition will occur if non-zero weights are specified for wavefunction symmetries with varying values of *elec* or *spin*.

.. _the_vb_program_casvb--defining-the-valence-bond-wavefunction:

Defining the valence bond wavefunction
--------------------------------------

.. _the_vb_program_casvb--specifying-orbital-configurations:

Specifying orbital configurations
=================================

The number of core and active orbitals (:math:`mcore`, :math:`mact`), active electrons (:math:`Nact`), and the value of the total spin will be identical to that defined for the CASSCF wavefunction. The spatial VB configurations are defined in terms of the active orbitals only, and may be specified using one or more ``CON`` cards (note that the ``RESTRICT`` and ``SELECT`` keywords are not used in *CASVB*):

``CON,$n_1,n_2,n_3,n_4,\ldots$;``

The configurations can be specified by occupation numbers, exactly as in *MULTI* (see section `specifying orbital configurations <the_mcscf_program_multi.html#specifying-orbital-configurations>`__), so that :math:`n_i` is the occupation of the :math:`i`\ th valence bond orbital. Alternatively a list of :math:`Nact` orbital numbers (in any order) may be provided – the program determines which definition applies. The two cards ``CON,1,0,1,2;`` and ``CON,1,3,4,4;`` are thus equivalent.

If no configurations are specified the single covalent configuration :math:`\phi_1\phi_2\cdots\phi_{Nact}` is assumed (SCGVB wavefunction).

Multiple configurations are most likely to be used for SCGVB(*N*,\ *M*) calculations -- see for example: P. B. Karadakov, D. L. Cooper, B. J. Duke and J. Li, `J. Phys. Chem. A <https://dx.doi.org/10.1021/jp303998h>`__ **116**, 7238-7244 (2012); P. B. Karadakov and D. L. Cooper. `Theor. Chem. Acc. <https://dx.doi.org/10.1007/s00214-013-1421-1>`__ **133**, 1421-1426 (2014).

.. _the_vb_program_casvb--selecting-the-spin-basis:

Selecting the spin basis
========================

``SPINBASIS,key;``

*key* may be chosen from ``KOTANI`` (default), ``RUMER``, ``PROJECT`` or ``LTRUMER``, specifying the basis of spin eigenfunctions used in the definition of valence bond structures. ``PROJECT`` refers to spin functions generated using a particular spin projection operator (see: B. Friis-Jensen, D.L. Cooper and S. Rettrup, `Theor. Chem. Acc. <https://dx.doi.org/10.1007/s002140050304>`__ **99**, 64-67 (1998)), ``LTRUMER`` to Rumer functions with the so-called “leading term" phase convention.

.. _the_vb_program_casvb--recovering-casscf-ci-vector-and-vb-wavefunction:

Recovering CASSCF CI vector and VB wavefunction
-----------------------------------------------

The appropriate Molpro records may be specified explicitly using the ``START`` directive (an alternative is the *vbdump* mechanism described in section `the VBDUMP directive <the_vb_program_casvb.html#the-vbdump-directive>`__):

``START,ci,vb,orb,trnint;[casvb:trnint]``

*ci:* record name for the CASSCF CI vector. The CI vector must have been dumped previously using either of the ``SAVE, NATORB, CANONICAL,`` or ``LOCALI`` directives (see section `saving the CI vectors and information for a gradient calculation <the_mcscf_program_multi.html#saving-the-ci-vectors-and-information-for-a-gradient-calculation>`__). A default value for *ci* is determined from the most recent *vbdump* record(s).

Note that if the *ci* record is not found, only an energy-based optimization of the VB wavefunction can be carried out.

*vb:* record name for the valence bond orbitals and structure coefficients, as saved by a previous CASVB calculation. If the VB wavefunction was previously saved in the AO basis the orbitals will be projected onto the present active space (note that it is necessary to specify a record name for the molecular orbitals (*orb* below) for this to be possible).

*orb:* record name for the molecular orbitals defining the CASSCF wavefunction. This information is necessary if one wants to output the valence bond orbitals in the atomic orbital basis.

*trnint:* record name for the transformed CASSCF integrals. These are required for the energy-based criteria (i.e., if ``CRIT,ENERGY`` is specified), and can be saved inside *MULTI* by the ``TRNINT`` sub-command (see `saving transformed integrals <the_mcscf_program_multi.html#saving-transformed-integrals>`__). The default record name, both here and in *MULTI*, is 1900.1.

.. _the_vb_program_casvb--saving-the-vb-wavefunction:

Saving the VB wavefunction
--------------------------

``SAVE,vb,civb;``

*vb:* record name for VB wavefunction (default is first available record after 3200.2), i.e., orbitals and structure coefficients.

*civb:* record name for valence bond full CI vector defined in terms of the CASSCF MOs (default is 3300.2). Saving this vector is necessary for the calculation of further properties, geometry optimization, etc.

It is normally advisable to use records on file 2 for *vb* and *civb*.

.. _the_vb_program_casvb--specifying-a-guess:

Specifying a guess
------------------

``GUESS;key-1,…;key-2,…;…``

The ``GUESS`` keyword initiates the input of a guess for the valence bond orbitals and structure coefficients. *key-i* can be either ``ORB``, ``STRUC`` or ``READ``. These keywords modify the guess provided by the program, or specified by the ``START`` directive. It is thus possible to modify individual orbitals in a previous solution to construct the starting guess.

.. _the_vb_program_casvb--orbital-guess:

Orbital guess
=============

``ORB,i, c$_1$, c$_2$,…c$_{mact}$;``

Specifies a starting guess for valence bond orbital number :math:`i`. The guess is specified in terms of the :math:`mact` active MOs defining the CASSCF wavefunction. (Note that the definition of these MOs will depend on how the CI vector was dumped – i.e. which of the ``SAVE, NATORB, CANONICAL,`` or ``LOCALI`` directives was used (see section `saving the CI vectors and information for a gradient calculation <the_mcscf_program_multi.html#saving-the-ci-vectors-and-information-for-a-gradient-calculation>`__). Use of one of the three latter keywords is recommended.)

.. _the_vb_program_casvb--guess-for-structure-coefficients:

Guess for structure coefficients
================================

``STRUC,c$_1$, c$_2$,…c$_{NVB}$;``

Specifies a starting guess for the :math:`NVB` structure coefficients. If this card is not provided, and no guess specified by ``START``, the perfect-pairing mode of spin coupling is assumed for the spatial configuration having the least number of doubly occupied orbitals. Note that the definition of structures depends on the value of ``SPINBASIS``. Doubly occupied orbitals occur first in all configurations, and the spin eigenfunctions are based on the singly occupied orbitals being in ascending order.

.. _the_vb_program_casvb--read-orbitals-or-structure-coefficients:

Read orbitals or structure coefficients
=======================================

The ``READ`` keyword can take one of the following forms:

``READ,ORB,iorb1[,TO,iorb2] [,AS,jorb1[,TO,jorb2]] [,FROM,record];``

``READ,STRUC,istruc1[,TO,istruc2] [,AS,jstruc1[,TO,jstruc2]] [,FROM,record];``

``READ,ALL [,FROM,record];``

In this way a subset of orbitals and/or structure coefficients may be picked out from a previous calculation. Renumbering of orbitals or structures can be done using the “\ ``AS``" construct as outlined above. If the VB wavefunction was previously saved in the AO basis, the orbitals will be projected onto the present active space (note that it is necessary to specify a record name for the molecular orbitals (*orb* in the ``START`` command) for this to be possible).

Default for *record* is the *vb* record name specified in keyword ``START`` (if applicable).

.. _the_vb_program_casvb--permuting-orbitals:

Permuting orbitals
------------------

``ORBPERM,$i_1$,…,$i_{mact}$;``

Permutes the orbitals in the valence bond wavefunction and changes their phases according to :math:`\phi_j'={\rm sign}(i_j)\phi_{{\rm abs}(i_j)}`. The guess may be further modified using the ``GUESS`` keyword. Also the structure coefficients will be transformed according to the given permutation (note that the configuration list must be closed under the orbital permutation for this to be possible).

.. _the_vb_program_casvb--optimization-control:

Optimization control
--------------------

.. _the_vb_program_casvb--optimization-criterion:

Optimization criterion
======================

``CRIT,method;``

Specifies the criterion for the optimization. *method* can be ``OVERLAP`` or ``ENERGY`` (``OVERLAP`` is default). The former maximizes the normalized overlap with the CASSCF wavefunction:

.. math::

   {\rm max}\left(\frac{\langle\Psi_{CAS}|\Psi_{VB}\rangle}{(\langle\Psi_{VB}|\Psi_{VB}\rangle)^{1/2}}\right)

and the latter simply minimizes the energy:

.. math::

   {\rm min}\left(\frac{\langle\Psi_{VB}|\hat{H}|\Psi_{VB}\rangle}{\langle\Psi_{VB}|\Psi_{VB}\rangle}\right).

.. _the_vb_program_casvb--number-of-iterations:

Number of iterations
====================

``MAXITER,$N_{iter}$;``

Specifies the maximum number of iterations in the second order optimizations. Default is :math:`N_{iter}`\ =50.

.. _the_vb_program_casvb--casscf-projected-structure-coefficients:

CASSCF-projected structure coefficients
=======================================

``(NO)CASPROJ;``

With this keyword the structure coefficients are picked from the transformed CASSCF CI vector, leaving only the orbital variational parameters. For further details see the bibliography. This option may be useful to aid convergence.

.. _the_vb_program_casvb--saddle-point-optimization:

Saddle-point optimization
=========================

``SADDLE,n;``

Defines optimization onto an *n*\ :math:`^{\rm th}`-order saddle point. See also T. Thorsteinsson and D. L. Cooper, `Int. J. Quant. Chem. <http://onlinelibrary.wiley.com/doi/abs/10.1002/%28SICI%291097-461X%281998%2970%3A4/5%3C637%3A%3AAID-QUA10%3E3.0.CO%3B2-%23>`__ **70**, 637–650 (1998).

.. _the_vb_program_casvb--defining-several-optimizations:

Defining several optimizations
==============================

More than one optimization may be performed in the same *CASVB* deck, by the use of ``OPTIM`` keywords:

``OPTIM[;…;FINOPTIM];``

The subcommands may be any optimization declarations defined in this section, as well as any symmetry or constraints specifications described in section `point group symmetry and constraints <the_vb_program_casvb.html#point-group-symmetry-and-constraints>`__. Commands given as arguments to ``OPTIM`` will be particular to this optimization step, whereas commands specified outside will act as default definitions for all subsequent ``OPTIM`` keywords.

If only one optimization step is required, the ``OPTIM`` keyword need not be specified.

When only a machine-generated guess is available, *CASVB* will attempt to define a sequence of optimization steps chosen such as to maximize the likelihood of successful convergence and to minimize CPU usage. This default behaviour corresponds to specifying the keyword ``INIT`` and it can be overridden by specifying the keyword ``NOINIT``. Alternatively, specify one or more ``OPTIM`` cards.

.. _the_vb_program_casvb--multi-step-optimization:

Multi-step optimization
=======================

A loop over two or more optimization steps may be specified using:

``ALTERN,Niter;…;FINALTERN``

With this specification the program will repeat the enclosed optimization steps until either all optimizations have converged, or the maximum iteration count, *Niter*, has been reached.

.. _the_vb_program_casvb--point-group-symmetry-and-constraints:

Point group symmetry and constraints
------------------------------------

The problems associated with symmetry-adapting valence bond wavefunctions are considered, for example, in: T. Thorsteinsson, D. L. Cooper, J. Gerratt and M. Raimondi, `Theor. Chim. Acta <https://dx.doi.org/10.1007/BF02341697>`__ **95**, 131-150 (1997).

.. _the_vb_program_casvb--symmetry-operations:

Symmetry operations
===================

``SYMELM,label,sign;``

Initiates the definition of a symmetry operation referred to by *label* (any three characters). *sign* can be + or :math:`-`; it specifies whether the total wavefunction is symmetric or antisymmetric under this operation, respectively. A value for *sign* is not always necessary but, if provided, constraints will be put on the structure coefficients to ensure that the wavefunction has the correct overall symmetry (note that the configuration list must be closed under the orbital permutation induced by *label* for this to be possible).

The operator is defined in terms of its action on the active MOs as specified by one or more of the keywords ``IRREPS``, ``COEFFS``, or ``TRANS`` (any other keyword will terminate the definition of this symmetry operator). If no further keyword is supplied, the identity is assumed for *label*. The alternative format ``SYMELM``,\ *label*,\ *sign*;\ *key-1,…*; *key-2,…*;…may also be used.

.. _the_vb_program_casvb--the-irreps-keyword:

The IRREPS keyword
==================

``IRREPS,i$_1$, i$_2$,…;``

The list *i:math:`_1`, i:math:`_2`,…* specifies which irreducible representations (as defined in the CASSCF wavefunction) are antisymmetric with respect to the *label* operation. If an irreducible representation is not otherwise specified it is assumed to be symmetric under the symmetry operation.

.. _the_vb_program_casvb--the-coeffs-keyword:

The COEFFS keyword
==================

``COEFFS,i$_1$, i$_2$,…;``

The list *i:math:`_1`, i:math:`_2`,…* specifies which individual CASSCF MOs are antisymmetric with respect to the *label* operation. If an MO is not otherwise specified, it is assumed to be symmetric under the symmetry operation. This specification may be useful if, for example, the molecule possesses symmetry higher than that exploited in the CASSCF calculation.

.. _the_vb_program_casvb--the-trans-keyword:

The TRANS keyword
=================

``TRANS,n$_{dim}$, i$_1$, …i$_{n_{dim}}$, c$_{11}$, c$_{12}$, …c$_{n_{dim}n_{dim}}$;``

Specifies a general n\ :math:`_{dim}\times n_{dim}` transformation involving the MOs *i:math:`_1`, …i:math:`_{n_{dim}}`*, specified by the :math:`c` coefficients. This may be useful for systems with a two- or three-dimensional irreducible representation, or if localized orbitals define the CASSCF wavefunction. Note that the specified transformation must always be orthogonal.

.. _the_vb_program_casvb--symmetry-relations-between-orbitals:

Symmetry relations between orbitals
===================================

In general, for a VB wavefunction to be symmetry-pure, the orbitals must form a representation (not necessarily irreducible) of the symmetry group. Relations between orbitals under the symmetry operations defined by ``SYMELM`` may be specified according to:

``ORBREL,i$_1$, i$_2$, label1, label2,…;``

Orbital :math:`i_1` is related to orbital :math:`i_2` by the sequence of operations defined by the *label* specifications (defined previously using ``SYMELM``). The operators operate right to left. Note that :math:`i_1` and :math:`i_2` may coincide. Only the minimum number of relations required to define all the orbitals should be provided; an error exit will occur if redundant ``ORBREL`` specifications are found.

.. _the_vb_program_casvb--the-symproj-keyword:

The SYMPROJ keyword
===================

As an alternative to incorporating constraints, one may also ensure correct symmetry of the wavefunction by use of a projection operator:

``(NO)SYMPROJ[,irrep$_1$,irrep$_2$,…];``

The effect of this keyword is to set to zero coefficients in unwanted irreducible representations. For this purpose the symmetry group defined for the CASSCF wavefunction is used (always a subgroup of D\ :math:`_{2h}`). The list of irreps in the command specifies which components of the wavefunction should be kept. If no irreducible representations are given, the current wavefunction symmetry is assumed. In a state-averaged calculation, all irreps are retained for which a non-zero weight has been specified in the wavefunction definition. The ``SYMPROJ`` keyword may also be used in combination with constraints.

.. _the_vb_program_casvb--freezing-orbitals-in-the-optimization:

Freezing orbitals in the optimization
=====================================

``FIXORB,i$_1$,i$_2$,[TO,i$_3$,]i$_4$,…;``

Freezes the specified orbitals to be those in the starting guess. Alternatively the special keywords ``ALL`` or ``NONE`` may be used. These orbitals are eliminated from the optimization procedure, but will still be normalized and symmetry-adapted according to any ``ORBREL`` keywords given.

.. _the_vb_program_casvb--freezing-structure-coefficients-in-the-optimization:

Freezing structure coefficients in the optimization
===================================================

``FIXSTRUC,i$_1$,i$_2$,[TO,i$_3$,]i$_4$,…;``

Freezes the coefficients for the specified structures to be those in the starting guess. Alternatively the special keywords ``ALL`` or ``NONE`` may be used. The structures are eliminated from the optimization procedure, but may still be affected by normalization or any symmetry keywords present.

.. _the_vb_program_casvb--deleting-structures-from-the-optimization:

Deleting structures from the optimization
=========================================

``DELSTRUC,i$_1$,i$_2$,[TO,i$_3$,]i$_4$,…;``

Deletes the specified structures from the wavefunction. The special keywords ``ALL`` or ``NONE`` may be used. A structure coefficient may already be zero by symmetry (as defined by ``SYMELM`` and ``ORBREL``), in which case deleting it has no effect.

.. _the_vb_program_casvb--orthogonality-constraints:

Orthogonality constraints
=========================

``ORTHCON;key-1,…;key-2,…;…``

The ``ORTHCON`` keyword initiates the input of orthogonality constraints between pairs of valence bond orbitals. The sub-keywords *key-i* can be one of ``ORTH``, ``PAIRS``, ``GROUP``, ``STRONG`` or ``FULL`` as described below. Orthogonality constraints should be used with discretion. Note that orthogonality constraints for an orbital generated from another by symmetry operations (using the ``ORBREL`` keyword) cannot in general be satisfied.

``ORTH,i$_1$, i$_2$, …;``

Specifies a list of orbitals to be orthogonalized. All overlaps between pairs of orbitals in the list are set to zero.

``PAIRS,i$_1$, i$_2$, …;``

Specifies a simple list of orthogonalization pairs. Orbital :math:`i_1` is made orthogonal to :math:`i_2`, :math:`i_3` to :math:`i_4`, etc.

``GROUP,label,i$_1$, i$_2$, …;``

Defines an orbital group to be used with the ``ORTH`` or ``PAIRS`` keyword. The group is referred to by *label* which can be any three characters beginning with a letter a–z. Labels defining different groups can be used together or in combination with orbital numbers in ``ORTH`` or ``PAIRS``. *i:math:`_1`, i:math:`_2`, …* specifies the list of orbitals in the group. Thus the combination ``GROUP``,AZZ,1,2; ``GROUP``,BZZ,3,4; ``ORTH``,AZZ,BZZ; will orthogonalize the pairs of orbitals 1-3, 1-4, 2-3 and 2-4.

``STRONG;``

This keyword is short-hand for strong orthogonality. The only allowed non-zero overlaps are between pairs of orbitals ($2n

.. math::

   -

1\ :math:`,`\ 2n$).

``FULL;``

This keyword is short-hand for full orthogonality. This is mainly likely to be useful for testing purposes.

.. _the_vb_program_casvb--wavefunction-analysis:

Wavefunction analysis
---------------------

.. _the_vb_program_casvb--spin-correlation-analysis:

Spin correlation analysis
=========================

``(NO)SCORR;``

With this option, expectation values of the spin operators :math:`(\hat{s}_\mu+\hat{s}_\nu)^2` are evaluated for all pairs of :math:`\mu` and :math:`\nu`. Default is ``NOSCORR``. The procedure is described by: G. Raos, J. Gerratt, D. L. Cooper and M. Raimondi, `Chem. Phys. <https://dx.doi.org/10.1016/0301-0104(94)00177-4>`__ **186**, 233–250 (1994); `ibid <https://dx.doi.org/10.1016/0301-0104(94)00178-2>`__, 251–273 (1994); D. L. Cooper, R. Ponec, T. Thorsteinsson and G. Raos, `Int. J. Quant. Chem. <https://dx.doi.org/10.1002/(SICI)1097-461X(1996)57:3%3C501::AID-QUA24%3E3.0.CO;2-4>`__ **57**, 501–518 (1996).

This analysis has been implemented only for single configurations of singly-occupied active orbitals (as in SCGVB wavefunctions).

.. _the_vb_program_casvb--printing-weights-of-the-valence-bond-structures:

Printing weights of the valence bond structures
===============================================

For further details regarding the calculation of weights in *CASVB*, see T. Thorsteinsson and D. L. Cooper, `J. Math. Chem. <https://dx.doi.org/10.1023/A:1019100703879>`__ **23**, 105-126 (1998).

``VBWEIGHTS,key1,key2,…``

Calculates and outputs weights of the structures in the valence bond wavefunction :math:`\Psi_{VB}`. *key* specifies the definition of nonorthogonal weights to be used, and can be one of:

* ``CHIRGWIN`` Evaluates Chirgwin-Coulson weights (see: B. H. Chirgwin and C. A. Coulson, `Proc. Roy. Soc. Lond. <https://dx.doi.org/10.1098/rspa.1950.0053>`__ **A201**, 196 (1950)).
* ``LOWDIN`` Performs a symmetric orthogonalization of the structures and outputs the corresponding weights.
* ``INVERSE`` Outputs “inverse overlap populations" as in G. A. Gallup and J. M. Norbeck, `Chem. Phys. Lett. <https://dx.doi.org/10.1016/0009-2614(73)80292-1>`__ **21**, 495–500 (1973).
* ``ALL`` All of the above.
* ``NONE`` Suspends calculation of structure weights.

The commands ``LOWDIN`` and ``INVERSE`` require the overlap matrix between valence bond structures, and thus some additional computational overhead is involved.

.. _the_vb_program_casvb--printing-weights-of-the-casscf-wavefunction-in-the-vb-basis:

Printing weights of the CASSCF wavefunction in the VB basis
===========================================================

For further details regarding the calculation of weights in *CASVB*, see T. Thorsteinsson and D. L. Cooper, `J. Math. Chem. <https://dx.doi.org/10.1023/A:1019100703879>`__ **23**, 105-126 (1998).

``CIWEIGHTS,key1,key2,…[,$N_{\rm conf}$];``

Prints weights of the CASSCF wavefunction transformed to the basis of nonorthogonal VB structures. For the *key* options see ``VBWEIGHTS`` above. Note that the evaluation of inverse overlap weights involves an extensive computational overhead for large active spaces. Weights are given for the total CASSCF wavefunction, as well as the orthogonal complement to :math:`\Psi_{VB}`. The default for the number of configurations requested, :math:`N_{\rm conf}`, is 10. If :math:`N_{\rm conf}`\ =\ :math:`-1` all configurations are included.

.. _the_vb_program_casvb--controlling-the-amount-of-output:

Controlling the amount of output
--------------------------------

``PRINT,i$_1$, i$_2$,…;``

Each number specifies the level of output required at various stages of the execution, according to the following convention:

* **-1** No output except serious, or fatal, error messages.
* **0** Minimal output.
* **1** Standard level of output.
* **2** Extra output.

The areas for which output can be controlled are:

* :math:`i_1` Print of input parameters, wavefunction definitions, etc.
* :math:`i_2` Print of information associated with symmetry constraints.
* :math:`i_3` General convergence progress.
* :math:`i_4` Progress of the 2nd order optimization procedure.
* :math:`i_5` Print of converged solution and analysis.
* :math:`i_6` Progress of variational optimization.
* :math:`i_7` Usage of record numbers on file 2.

For all, the default output level is +1. If :math:`i_5\geq`\ 2 VB orbitals will be printed in the AO basis (provided that the definition of MOs is available); such output may be especially useful for plotting of orbitals.

.. _the_vb_program_casvb--further-facilities:

Further facilities
------------------

Calculations can also be performed for various types of direct product wavefunctions and/or with strictly localized orbitals. Details are available from the authors. These facilities will be documented in a later release.

.. _the_vb_program_casvb--service-mode:

Service mode
------------

``SERVICE;\\``
This keyword takes precedence over any others previously defined to *CASVB*. It provides simple facilities for retrieving orbital coefficients and VB structure coefficients. It should not be used during a run of *CASVB* that has been invoked from inside *MULTI*.

``START,record.file;\\``
Coefficients are taken from *record.file*. The default value is *2100.2*.

``WRITE,iwrite;\\``
Vectors in the symmetry orbital basis are written to channel *iabs(iwrite)*. The default action is to write these vectors to the standard output. If *iwrite* is negative, then the vectors are instead written to a binary file as a single record.

``SPECIAL,idim1,idim2,idim3,idim4;\\``
If present, this keyword must come last. The program attempts to retrieve from *record.file* a vector of length *idim1\*idim2+idim3*, after first skipping *idim4* elements. The vector is written according to the setting of *iwrite*. (Default *idim* values are zero.)

.. _the_vb_program_casvb--examples:

Examples
--------

.. code-block:: text

   ***, ch2                      ! A1 singlet state
   geometry={angstrom
   c
   h1,c,1.117
   h2,c,1.117,h1,102.4}
   hf
   {multi;occ,4,1,2;closed,1;config,det      ! 6 in 6 CASSCF
   natorb,,detcirec=3500.2;vbdump}
   {casvb                         ! Overlap-based calculation of SCGVB wavefunction
   save,3200.2}
   {casvb                         ! Corresponding energy-based calculation
   start,,3200.2;save,3220.2
   crit,energy}
   {multi;occ,4,1,2;closed,1      ! Fully-variational SCGVB calculation
   {vb;start,,3220.2;save,3240.2;print,,,,,2}}

.. code-block:: text

   ***,n2s2 (model a)            ! Variational calculation for N2S2.
   v=2.210137753 bohr
   geometry={ n, -v, 0, 0;       ! NOTE: other choices of active space
              n, +v, 0, 0;       ! give alternative (competing) models.
              s, 0, -v, 0;
              s, 0, +v, 0}
   basis=VTZ
   {rhf; occ,7,4,5,2,3,1,1,0}
   {multi; occ,7,4,5,2,4,2,2,0; closed,7,4,5,2,1,0,1,0; config,det; natorb,,detcirec=3500.2}
   {multi; occ,7,4,5,2,4,2,2,0; closed,7,4,5,2,1,0,1,0;
   {vb; start,3500.2; scorr}}

.. code-block:: text

   ***, lih                      ! Fully-variational SCGVB calculation
   r=2.8 bohr                    ! and geometry optimization.
   geometry={li;h,li,r}
   basis={
   s,1,921.300000,138.700000,31.940000,9.353000,3.158000,1.157000;
   c,1.6,0.001367,0.010425,0.049859,0.160701,0.344604,0.425197;
   s,1,0.444600,0.076660,0.028640;
   p,1,1.488000,0.266700,0.072010,0.023700;
   c,1.2,0.038770,0.236257;
   s,2,13.36,2.013,0.4538,.1233;
   c,1.2,0.032828,0.231204}
   hf
   {multi; occ,4,0,0,0; closed,0,0,0,0; config,det; natorb,,detcirec=3500.2}
   {multi; occ,4,0,0,0; closed,0,0,0,0;
   {vb; start,3500.2}}
   optg
