.. raw:: html

   <span id="cahf-optimization-with-the-mcscf-program"></span>

.. raw:: html

   <span id="calculating-expectation-values"></span>

.. raw:: html

   <span id="cas-ci"></span>

.. raw:: html

   <span id="closed-shell-orbitals"></span>

.. raw:: html

   <span id="combined-first-and-second-order-optimization-default"></span>

.. raw:: html

   <span id="convergence-thresholds"></span>

.. raw:: html

   <span id="coupled-optimization"></span>

.. raw:: html

   <span id="coupled-perturbed-mcscf"></span>

.. raw:: html

   <span id="defining-the-number-of-states-in-the-present-symmetry"></span>

.. raw:: html

   <span id="defining-the-optimized-states"></span>

.. raw:: html

   <span id="defining-the-orbital-subspaces"></span>

.. raw:: html

   <span id="defining-the-starting-ci-coefficients"></span>

.. raw:: html

   <span id="defining-the-starting-orbitals"></span>

.. raw:: html

   <span id="defining-the-state-symmetry"></span>

.. raw:: html

   <span id="diabatic-orbitals"></span>

.. raw:: html

   <span id="difference-gradients-for-sa-mcscf"></span>

.. raw:: html

   <span id="directives-of-the-mcscf-program"></span>

.. raw:: html

   <span id="disabling-the-extra-symmetry-mechanism"></span>

.. raw:: html

   <span id="disabling-the-optimization"></span>

.. raw:: html

   <span id="dynamical-weighting"></span>

.. raw:: html

   <span id="export-the-ci-vectors-in-determinant-form"></span>

.. raw:: html

   <span id="first-order-mcscf-for-large-molecules"></span>

.. raw:: html

   <span id="freezing-orbitals"></span>

.. raw:: html

   <span id="frozen-core-orbitals"></span>

.. raw:: html

   <span id="gradients-for-sa-mcscf"></span>

.. raw:: html

   <span id="localized-orbitals"></span>

.. raw:: html

   <span id="matrix-elements-over-one-electron-operators"></span>

.. raw:: html

   <span id="matrix-elements-over-two-electron-operators"></span>

.. raw:: html

   <span id="maximum-number-of-iterations"></span>

.. raw:: html

   <span id="mcscf-hessians"></span>

.. raw:: html

   <span id="natural-orbitals"></span>

.. raw:: html

   <span id="new-implementation-of-the-wmk-method-default"></span>

.. raw:: html

   <span id="non-adiabatic-coupling-matrix-elements-for-sa-mcscf"></span>

.. raw:: html

   <span id="occupation-restrictions"></span>

.. raw:: html

   <span id="occupied-orbitals"></span>

.. raw:: html

   <span id="old-implementation-of-the-wmk-method"></span>

.. raw:: html

   <span id="optimizing-valence-bond-wavefunctions"></span>

.. raw:: html

   <span id="options-of-the-mcscf-program"></span>

.. raw:: html

   <span id="orbital-hessian-eigenvalues"></span>

.. raw:: html

   <span id="print-options"></span>

.. raw:: html

   <span id="projection-to-specific-lambda-states-in-linear-molecules"></span>

.. raw:: html

   <span id="pseudo-canonical-orbitals"></span>

.. raw:: html

   <span id="raw-orbitals"></span>

.. raw:: html

   <span id="rhf-optimization-with-the-mcscf-program"></span>

.. raw:: html

   <span id="rotating-pairs-of-initial-orbitals"></span>

.. raw:: html

   <span id="saving-the-ci-vectors"></span>

.. raw:: html

   <span id="saving-the-ci-vectors-and-information-for-a-gradient-calculation"></span>

.. raw:: html

   <span id="saving-the-density-matrix"></span>

.. raw:: html

   <span id="saving-the-final-orbitals"></span>

.. raw:: html

   <span id="saving-transformed-integrals"></span>

.. raw:: html

   <span id="saving-wavefunction-information-for-casvb"></span>

.. raw:: html

   <span id="second-order-mcscf"></span>

.. raw:: html

   <span id="selecting-configurations"></span>

.. raw:: html

   <span id="selecting-the-ci-method"></span>

.. raw:: html

   <span id="selecting-the-primary-configuration-set"></span>

.. raw:: html

   <span id="special-optimization-parameters-old-implementation"></span>

.. raw:: html

   <span id="specifying-orbital-configurations"></span>

.. raw:: html

   <span id="specifying-weights-in-state-averaged-calculations"></span>

.. raw:: html

   <span id="structure-of-the-input"></span>

.. raw:: html

   <span id="super-ci"></span>

.. raw:: html

   <span id="uc-ah"></span>

.. _the_mcscf_program_multi--the-mcscf-program-multi:

The MCSCF program MULTI
=======================

*MULTI* is a general MCSCF/CASSCF program written by
P. J. Knowles and H.-J. Werner (1984)
D. Kreplin, P. J. Knowles, and H.-J. Werner (2019)

Bibliography:

Second-order MCSCF:

H.-J. Werner and P. J. Knowles, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.448627>`__ **82**, 5053 (1985).
P. J. Knowles and H.-J. Werner, `Chem. Phys. Lett. <https://dx.doi.org/10.1016/0009-2614(85)80025-7>`__ **115**, 259 (1985).
D. A. Kreplin, P. J. Knowles, and H.-J. Werner, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.5094644>`__ **150**, 194106 (2019).

First-order MCSCF:

D. A. Kreplin, P. J. Knowles, and H.-J. Werner, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.5142241>`__ **152**, 074102 (2020).

All publications resulting from use of this program must acknowledge the above. See also:

H.-J. Werner and W. Meyer, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.440384>`__ **73**, 2342 (1980).
H.-J. Werner and W. Meyer, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.440892>`__ **74**, 5794 (1981).
H.-J. Werner, Adv. Chem. Phys. LXIX, 1 (1987).

This program allows one to perform CASSCF as well as general MCSCF calculations. For CASSCF calculations, one can optionally use Slater determinants or CSFs as a :math:`N`-electron basis. In most cases, the use of Slater determinants is more efficient. General MCSCF calculations must use CSFs as a basis.

There are two different MCSCF methods implemented in MOLPRO: the first-order and the second-order method (see `First-order MCSCF (for large molecules) <the_mcscf_program_multi.html#first-order-mcscf-for-large-molecules>`__ and `Second-order MCSCF <the_mcscf_program_multi.html#second-order-mcscf>`__). The latter one is second-order in the orbital and CI coefficient changes and is therefore quadratically convergent. Since important higher order terms in the independent orbital parameters are included, almost cubic convergence is often observed. For simple cases, convergence is usually achieved in 3-4 iterations. However, the quadratic method requires the full orbital Hessian, and therefore, the computation time and memory requirements grow strongly with the molecular size. This problem is overcome by the first-order MCSCF method, where some second derivatives of the orbital parameters are approximated. The computation-time per iteration is considerably lower than in the second-order method, but more iterations are required. The overall convergence is improved by a convergence accelerator based on the L-BFGS method.

However, convergence problems can still occur in certain applications, and usually indicate that the active space is not adequately chosen. For instance, if two weakly occupied orbitals are of similar importance to the energy, but only one of them is included in the active set, the program might alternate between them. In such cases either reduction or enlargement of the active orbital space can solve the problem. In other cases difficulties can occur if two electronic states in the same symmetry are almost or exactly degenerate, since then the program can switch from one state to the other. This might happen near avoided crossings or near an asymptote. Problems of this sort can be avoided by optimizing the energy average of the particular states. It is also possible to force convergence to specific states by choosing a subset of configurations as primary space (``PSPACE``). The hamiltonian is constructed and diagonalized explicitly in this space; the coefficients of the remaining configurations are optimized iteratively using the P-space wavefunction as zeroth order approximation. For linear molecules, another possibility is to use the ``LQUANT`` option, which makes it possible to force convergence to states with definite :math:`\Lambda` quantum number, i.e., :math:`\Sigma`, :math:`\Pi`, :math:`\Delta`, etc. states.

.. _the_mcscf_program_multi--structure-of-the-input:

Structure of the input
======================

All sub-commands known to *MULTI* may be abbreviated by four letters. The input commands fall into several logical groups; within each group commands may appear in any order, but the groups must come in correct order.

* The program is invoked by the command ``MULTI``, ``MCSCF``, ``CASSCF``, or ``CASCI``. The commands can be prepended by 'DF-' to use density fitting, which is strongly recommended for larger molecules.
* cards defining partitioning of orbitals spaces – ``OCC,FROZEN,CLOSED``
* general options (most commands not otherwise specified here)
* a ``WF`` card defining a state symmetry
* options pertaining to that state symmetry – ``WEIGHT,STATE,LQUANT`` (must be given after ``WF``)
* configuration specification for that state symmetry – ``SELECT,CON,RESTRICT``
* definition of the primary configurations for that state symmetry - ``PSPACE``
* further general options

Stages d) through to h) may be repeated several times; this is the way in which you specify an average energy of several states of different symmetry.

If the command ``CASCI`` is given, only a CI calculation for each states is carried out. This is the same as giving option ``CAS-CI``. Optionally, natural or pseudo-canonical orbitals can be generated using the final CI vectors. See option `CAS-CI <the_mcscf_program_multi.html#cas-ci>`__ for more details.

Many options, directives, and thresholds, which can also be given on the command line, are described in section `options of the MCSCF program <the_mcscf_program_multi.html#options-of-the-mcscf-program>`__ and `directives of the MCSCF program <the_mcscf_program_multi.html#directives-of-the-mcscf-program>`__.

.. _the_mcscf_program_multi--defining-the-orbital-subspaces:

Defining the orbital subspaces
==============================

.. _the_mcscf_program_multi--occupied-orbitals:

Occupied orbitals
=================

``OCC,$n_1,n_2,...,n_8$;``

:math:`n_i` specifies numbers of occupied orbitals (including FROZEN and CLOSED) in irreducible representation number :math:`i`. In the absence of an ``OCC`` card, the information from the most recent MCSCF calculation is used, or, if there is none, those orbitals corresponding to a minimal valence set, i.e., full valence space, are used.

.. _the_mcscf_program_multi--frozen-core-orbitals:

Frozen-core orbitals
====================

``FROZEN,$n_1,n_2,\ldots,$record.file,type;``

:math:`n_i` is the number of frozen-core orbitals in irrep number :math:`i`. These orbitals are doubly occupied in all configurations and not optimized. Note that in earlier Molpro versions this directive was called ``CORE`` and has now been renamed to avoid confusion with ``CORE`` orbitals in the MRCI and CCSD programs.

*record.file* is the record name for frozen core orbitals; if not supplied, taken from *orb* on ``START`` card. *record.file* can be specified in any field after the last nonzero :math:`n_i`. It should always be given if the orbital guess is from a neighbouring geometry and should then specify the SCF orbitals calculated at the present geometry. If a subsequent gradient calculation is performed with this wavefunction, *record.file* is mandatory and must specify closed-shell SCF orbitals at the present geometry. Note that *record* must be larger than 2000.

*type* optionally specified the orbital type, e.g., ALPHA, BETA, or NATURAL if UHF/UKS orbitals are used.

If the ``FROZEN`` card is omitted, then the numbers of core orbitals are taken from the most recent MCSCF calculation, or otherwise no orbitals are frozen. If the ``FROZEN`` card is given as ``FROZEN``,record.file, then the orbitals corresponding to atomic inner shells are taken, i.e., :math:`1s` for Li–Ne, :math:`1s2s2p` for Na–Ar, etc. A ``FROZEN`` card without any specification resets the number of frozen core orbitals to zero.

.. _the_mcscf_program_multi--closed-shell-orbitals:

Closed-shell orbitals
=====================

``CLOSED,$n_1,n_2,\ldots,n_8$``

:math:`n_i` is the number of closed-shell orbitals in irrep number :math:`i`, inclusive of any ``FROZEN`` orbitals. These orbitals do not form part of the active space, i.e., they are doubly occupied in all CSFs. In contrast to the core orbitals (see ``FROZEN``), these orbitals are fully optimized.

If the ``CLOSED`` card is omitted, then the data defaults to that of the most recent MCSCF calculation, or else the atomic inner shells as described above for ``FROZEN``.

.. _the_mcscf_program_multi--freezing-orbitals:

Freezing orbitals
=================

``FREEZE,orb.sym;``

The specified orbital will not be optimized and will remain identical to the starting guess. *orb.sym* should be an active or closed-shell orbital. If *orb.sym* is a frozen core orbital, this card has no effect.

.. _the_mcscf_program_multi--defining-the-optimized-states:

Defining the optimized states
-----------------------------

Each state symmetry to be optimized is specified by one WF card, which may optionally be followed by ``STATE, WEIGHT, RESTRICT, SELECT, CON,`` and/or ``PSPACE`` cards. All cards belonging to a particular state symmetry as defined on the ``WF`` card must form a block which comes directly after the ``WF`` card. The cards can be in any order, however.

.. _the_mcscf_program_multi--defining-the-state-symmetry:

Defining the state symmetry
===========================

The number of electrons and the total symmetry of the wavefunction are specified on the WF card:

``WF,elec,sym,spin``

where

* ***elec*** is the number of electrons
* ***sym*** is the number of the irreducible representation
* ***spin*** defines the spin symmetry, *spin*\ :math:`=2S` (singlet=0, doublet=1, triplet=2, etc.)

Note that these values take sensible defaults if any or all are not specified (see section `symmetry <general_program_structure.html#symmetry>`__).

The input directives ``STATE``, ``WEIGHT``, ``LQUANT``, ``SELECT``, ``PUNCSF`` always refer to the state symmetry as defined on the previous ``WF`` card. If such a directive is found before a ``WF`` card has been given, an error occurs. If any of these cards and a ``WF`` card is given, the variables ``STATE``, ``WEIGHT``, ``LQUANT``, ``SELECT`` are *not* used, and the number of state symmetries defaults to one, regardless of how many symmetries are specified in variable ``[MC]SYMMETRY``.

.. _the_mcscf_program_multi--defining-the-number-of-states-in-the-present-symmetry:

Defining the number of states in the present symmetry
=====================================================

``STATE,nstate;``

*nstate* is the number of states in the present symmetry. By default, all states are optimized with weight 1 (see ``WEIGHT`` card). The ``STATE`` directive must follow a ``WF`` card.

.. _the_mcscf_program_multi--specifying-weights-in-state-averaged-calculations:

Specifying weights in state-averaged calculations
=================================================

``WEIGHT,$w(1),w(2),\ldots, w($nstate$)$;``

:math:`w(i)` is the weight for the state :math:`i` in the present symmetry. By default, all weights are 1.0. See also ``STATE`` card. If you want to optimize the second state of a particular state symmetry alone, specify

``STATE,2;WEIGHT,0,1;``

Note, however, that this might lead to root-flipping problems. ``WEIGHT`` should follow a ``STATE`` directive.

If very many states are included and weights are not 1, the following input simplifications are possible:

``STATE,50;WEIGHT,ALL,3``

This sets all weights in the current state symmetry to 3. One can also specify ranges of weights, e.g.,

``STATE,50;WEIGHT,20[3],30[1]``

which sets the weights for the first 20 states to 3 and the remaining ones to 1. The total number of states given in this way must equal the number of states.

.. _the_mcscf_program_multi--dynamical-weighting:

Dynamical weighting
===================

Dynamical weighting, as described in `J. Chem. Phys. <https://dx.doi.org/10.1063/1.1667468>`__ **120**, 7281 (2004), can be activated using

``DYNW,dynfac``

The weights for each state are then computed as

.. math::

   w=1/\cosh(dynfac*\Delta E)^2

where :math:`\Delta E` is the energy difference (in Hartree) between the state under consideration and the state with the lowest energy. This is dynamically adjusted during the optimization process.

Optionally, it is possible to restrict the number of states which are included in the dynamically weighting:

``DYNW,dynfac,STATES=[MS2=spin,SYM=sym,STATE=x-y]``

The states in the weighting are given by the criterion in the square bracket. It is also possible to select all symmetries, spins, and states by a star, e.g. SYM=\*.
Furthermore the brackets can be combined to set up multiple criteria, as shown in the example below.
During the dynamically weighting, only the weights of the selected states are adjusted while the weights of the other states are set to 1.0 before the normalization.
The energy minimum for :math:`\Delta E` is determined within the dynamically weighted states.
If no states are specified in the input, all states are included in the dynamically weighting.

Example

.. code-block:: text
   :caption: examples/h2o_dynw_states.inp

   geometry=h2o.xyz
   basis=vdz
   hf
   {multi;
   wf,spin=0,sym=1;
   state,5;
   wf,spin=2,sym=1;
   state,5;
   dynw,1,states=[[sym=1,ms2=0,state=3-5],[sym=1,ms2=2,state=5]]; ! only state 3.1, 4.1, 5.1, and 5.2 are included in the dynamically weighting
   }

.. _the_mcscf_program_multi--defining-the-configuration-space:

Defining the configuration space
--------------------------------

By default, the program generates a complete configuration set (CAS) in the active space. The full space may be restricted to a certain occupation pattern using the ``RESTRICT`` option. Alternatively, configurations may be selected from the wavefunction of a previous calculation using ``SELECT``, or explicitly specified on ``CON`` cards. Note that this program only allows to select or specify orbital configurations. For each orbital configuration, all spin couplings are always included. Possible ``RESTRICT, SELECT`` and ``CON`` cards must immediately follow the ``WF`` card which defines the corresponding state symmetry.

.. _the_mcscf_program_multi--occupation-restrictions:

Occupation restrictions
=======================

``RESTRICT,nmin,nmax,orb$_1$,orb$_2$,$\ldots$orb$_n$;``

This card can be used to restrict the occupation patterns. Only configurations containing between *nmin* and *nmax* electrons in the specified orbitals *orb*\ :math:`_1`,  *orb*\ :math:`_2`,\ :math:`\ldots`,\ *orb*\ :math:`_n` are included in the wavefunction. If *nmin* and  *nmax* are negative, configurations with exactly abs(*nmin*) and abs(*nmax*) electrons in the specified orbitals are deleted. This can be used, for instance, to omit singly excited configurations. The orbitals are specified in the form *number.sym*, where *number* is the number of the orbital in irrep *sym*. Several ``RESTRICT`` cards may follow each other. ``RESTRICT`` only works if a CONFIG card is specified before the first ``WF`` card.

``RESTRICT cards given before the first WF cards are global, i.e., are active for all state symmetries. If such a global restrict card is given, variable [MC]RESTRICT is not used.``

Additional state-specific ``RESTRICT`` cards may be given after a ``WF`` card. These are used in addition to the global orbital restrictions.

If neither state-specific nor global ``RESTRICT`` cards are found, the values from the variable ``[MC]RESTRICT`` are used.

.. _the_mcscf_program_multi--selecting-configurations:

Selecting configurations
========================

``SELECT,ref1,ref2,refthr,refstat,mxshrf;``

This card is used to specify a configuration set other than a CAS, which is the default. This option automatically triggers the ``CONFIG`` option, which selects CSFs rather than determinants. Configurations can be defined using ``CON`` cards, which must follow immediately the SELECT card. Alternatively, if *ref1* is an existing Molpro record name, the configurations are read in from that record and may be selected according to a given threshold.

* ***ref1=rec1.file*** (*rec1:math:`>2000`*) The configurations are read in from the specified record. If *ref1* is not specified, the program assumes that the configurations are read from subsequent CON cards (see CON).
* ***ref2=rec2.file*** (*rec2:math:`>2000`*) Additional configurations are read from the specified record. If *rec2* is negative, all records between  *rec1* and abs(*rec2*) are read. All configurations found in this way are merged.
* ***refthr*** Selection threshold for configurations read from disc (records  *rec1–rec2*). This applies to the norm of all CSFs for each orbital configuration.
* ***refstat*** Specifies from which state vector the configurations are selected. This only applies to the case that the configurations were saved in a state-averaged calculation. If *refstat* is not specified, the configurations are selected from all states.
* ***mxshrf*** max. number of open shells in the selected or generated configurations.

.. _the_mcscf_program_multi--specifying-orbital-configurations:

Specifying orbital configurations
=================================

``CON,$n_1,n_2,n_3,n_4,\ldots$``

Specifies an orbital configuration to be included in the present symmetry. The first ``CON`` card must be preceded by a ``SELECT`` card. :math:`n_1`, :math:`n_2` etc. are the occupation numbers of the active orbitals (0,1,or 2). For example, for
``OCC,5,2,2;CLOSED,2,1,1;\\``
:math:`n_1` is the occupation of orbital 3.1 (number.sym), :math:`n_2` is the occupation of orbital 4.1, :math:`n_3` of 5.1, :math:`n_4` of 2.2, and :math:`n_5` of 2.3 Any number of ``CON`` cards may follow each other.

Example for the BH molecule:

.. code-block:: text

   OCC,4,1,1;             ! four sigma, one pi orbitals are occupied
   FROZEN,1;              ! first sigma orbital is doubly occupied and frozen
   WF,6,1;                ! 6 electrons, singlet Sigma+ state
   SELECT                 ! triggers configuration input
   CON,2,2                ! 2sigma**2, 3sigma**2
   CON,2,1,1              ! 2sigma**2, 3sigma, 4sigma
   CON,2,0,2              ! 2sigma**2, 4sigma**2
   CON,2,0,0,2            ! 2sigma**2, 1pi_x**2
   CON,2,0,0,0,2          ! 2sigma**2, 1pi_y**2

.. _the_mcscf_program_multi--selecting-the-primary-configuration-set:

Selecting the primary configuration set
=======================================

``PSPACE,thresh``

The hamiltonian is constructed and diagonalized explicitly in the primary configuration space, which can be selected with the ``PSPACE`` card. The coefficients of the remaining configurations (Q-space) are optimized iteratively using the P-space wavefunction as zeroth order approximation.

If *thresh* is nonzero, it is a threshold for automatically selecting all configurations as P-space configurations which have energies less then :math:`emin+thresh`, where *emin* is the lowest energy of all configurations. Further P-space configurations can be specified using ``CON`` cards, which must follow immediately after the ``PSPACE`` card. These are merged with the ones selected according to the threshold. Automatic selection can be avoided by specifying a very small threshold. There is a sensible default value for thresh (0.4), so you usually don’t need a ``pspace`` card in your input. Furthermore, if the number of configurations in the MCSCF is less than 20, all configurations go into the P-space unless you give a PSPACE card in the input.

A P-space threshold defined on a ``PSPACE`` card before the first ``WF`` (or ``STATE``, ``WEIGHT``, ``SELECT``, ``PUNCSF`` if ``WF`` is not given) card is global, i.e., valid for all state symmetries. State-specific thresholds can be defined by placing a ``PSPACE`` card after the corresponding ``WF`` card. In the latter case the ``PSPACE`` card can be followed by ``CON`` cards, which define state-specific P-space configurations.

.. _the_mcscf_program_multi--projection-to-specific-lambda-states-in-linear-molecules:

Projection to specific Lambda states in linear molecules
========================================================

Since Molpro can only use Abelian point groups (e.g. :math:`C_{2v}` instead of :math:`C_{\infty v}` for linear molecules), :math:`\Delta_{x^2-y^2}` states as well as :math:`\Sigma^+` states occur in the irreducible representation number 1, for example. Sometimes it is not possible to predict in advance to which state(s) the program will converge. In such cases the ``LQUANT`` option can be used to specify which states are desired.

``LQUANT,lam(1),lam(2),$\ldots$,lam(nstate);``

*lam(i)* is the :math:`\Lambda` quantum number of state :math:`i`, i.e., 0 for :math:`\Sigma` states, 1 for :math:`\Pi` states, 2 for :math:`\Delta` states, etc. The matrix over :math:`\Lambda^2` will be constructed and diagonalized in the P-space configuration basis. The eigenvectors are used to transform the P-space hamiltonian into a symmetry adapted basis, and the program then selects the eigenvectors of the correct symmetry. The states will be ordered by symmetry as specified on the ``LQUANT`` card; within each symmetry, the states will be ordered according to increasing energy.

.. _the_mcscf_program_multi--restoring-and-saving-the-orbitals-and-ci-vectors:

Restoring and saving the orbitals and CI vectors
------------------------------------------------

MULTI normally requires a starting orbital guess. In this section we describe how to define these orbitals, and how to save the optimized orbitals. In a CASSCF calculation, one has the choice of transforming the final orbitals to natural orbitals (the first order density matrix is diagonalized), to pseudo-canonical orbitals (an effective Fock-operator is diagonalized), or of localizing the orbitals.

.. _the_mcscf_program_multi--defining-the-starting-orbitals:

Defining the starting orbitals
==============================

``START,record,[options];``

*record:* dump record containing starting orbitals. As usual, *record* has the form *irec.ifil*, where *irec* is the record number (e.g., 2140), and *ifil* the file number (usually 2). The *options* can be used to select orbitals of a specific type; for details, see section `selecting orbitals and density matrices (ORBITAL, DENSITY) <general_program_structure.html#selecting-orbitals-and-density-matrices-orbital-density>`__.

If this card is missing, the program tries to find suitable starting orbitals as follows:

* **First:** Try to read orbitals from the record specified on the ``ORBITAL`` card (or the corresponding default, see ``ORBITAL``). All files are searched.
* **Second:** Try to find orbitals from the most recent MCSCF calculation. All files are searched.
* **Third:** Try to find orbitals from the most recent SCF calculation. All files are searched.

If no orbitals are found, a starting orbital guess is generated.

It is often useful to employ MCSCF orbitals from a neighbouring geometry as starting guess (this will happen automatically if orbitals are found, see the above defaults). Note, however, that frozen-core orbitals should always be taken from an SCF or MCSCF calculation at the present geometry and must be specified separately on the ``FROZEN`` card. Otherwise the program is likely to stop with error “non-orthogonal core orbitals”. The program remembers where to take the core orbitals from if these have been specified on a ``FROZEN`` card in a previous MCSCF calculation.

.. _the_mcscf_program_multi--defining-the-starting-ci-coefficients:

Defining the starting CI coefficients
=====================================

MULTI normally obtains configuration mixing coefficients by a robust eigenvector solver that converges on the lowest eigenvalues, and applies a phase convention such that the largest coefficient is forced to be positive. For most purposes, this approach is satisfactory.

Sometimes one wants a guarantee that the CI vector is phase matched to that of a previous geometry. This can be achieved by using ``SAVE,CI=``\ *record.file* (see section `saving the CI vectors and information for a gradient calculation <the_mcscf_program_multi.html#saving-the-ci-vectors-and-information-for-a-gradient-calculation>`__) in the first job, and in the restart,

``CIGUESS,record.file``

The phase convention applied for the rest of the calculation is then that, for each optimised state, the largest coefficient in the original CI vector defines the sign of the corresponding coefficient in the optimised vector.

.. _the_mcscf_program_multi--rotating-pairs-of-initial-orbitals:

Rotating pairs of initial orbitals
==================================

``ROTATE,orb1.sym,orb2.sym,angle``

Performs a :math:`2\times 2` rotation of the initial orbitals *orb1* and *orb2* in symmetry *sym* by *angle* degrees. With *angle*\ =0 the orbitals are exchanged. ``ROTATE`` is meaningful only after the ``START`` card. See ``MERGE`` for other possibilities to manipulate orbitals.

.. _the_mcscf_program_multi--saving-the-final-orbitals:

Saving the final orbitals
=========================

``ORBITAL,record.file``

The orbitals are dumped to record *record.file*. Default for *record* is 2140 and *file=2*. This default record number is incremented by one for each subsequent MCSCF calculation in the same job (see section `selecting orbitals and density matrices (ORBITAL, DENSITY) <general_program_structure.html#selecting-orbitals-and-density-matrices-orbital-density>`__). Therefore, if several different MCSCF calculations at several geometries are performed in one job, each MCSCF will normally start with appropriate orbitals even if no ``ORBITAL`` or ``START`` card is present.

The ``ORBITAL`` card can be omitted if a ``NATORB, CANORB`` or ``LOCORB`` card is present, since *orb* can also be specified on these cards (the same defaults for  *orb* as above apply in these cases).

.. _the_mcscf_program_multi--natural-orbitals:

Natural orbitals
================

``NATORB,[record,] [options]``

Request to calculate final natural orbitals and write them to record *record*. The default for *record* is 2140.2, or what else has been specified on an ``ORBITAL`` card, if present. By default, the orbitals are not printed and the hamiltonian is not diagonalized for the new orbitals.

Options for printing the CI vectors and orbitals:

* **``PRINT``\ =\ *nvirt*** Request to print *nvirt* virtual orbitals in each symmetry. By default, the orbitals are not printed unless the ``ORBPRINT`` option (see section `print options <the_mcscf_program_multi.html#print-options>`__ is present or the global ``GPRINT,ORBITALS`` (see section `global Print Options (GPRINT/NOGPRINT) <program_control.html#global-print-options-gprint-nogprint>`__) directive has been given before. The ``PRINT`` option on this card applies only to the current orbitals.
* ``PRINTCI`` or ``CI`` Transforms the CI vector according to the natural orbitals and print the configurations and their associated coefficients. This has the same effect as the ``GPRINT,CIVECTOR`` directive (see section `global Print Options (GPRINT/NOGPRINT) <program_control.html#global-print-options-gprint-nogprint>`__. By default, only configurations with coefficients larger than 0.05 are printed. This threshold can be modified using the ``THRESH`` (see section `convergence thresholds <the_mcscf_program_multi.html#convergence-thresholds>`__) or ``GTHRESH`` (see section `global Thresholds (GTHRESH) <program_control.html#global-thresholds-gthresh>`__) options.

Options for storing the CI vectors and orbitals:

* **``CIREC``\ =\ *record*** or **``SAVE``\ =\ *record*** Save the civector(s) to the specified record. The CI vectors are automatically stored in CSF basis, for more details see `saving the CI vector <the_mcscf_program_multi.html#saving-the-ci-vectors>`__. Other aliases for ``CIREC``  are ``CIREF`` and ``CIVEC``.
* **``DETCIREC``\ =\ *record*** Export of the CI vector in determinant basis for multi restarts (more details `here <the_mcscf_program_multi.html#export-the-ci-vectors-in-determinant-form>`__).
* **``ORBITAL``\ =\ *record*** Request to save the orbitals to the specified record. This has the same effect as specifying *record* as the first argument (see above).

A simple export of the final orbitals and CI vectors reads "natorb,2140.2,cirec=5100.2;".

Options for selecting the states included in the density from which the natural orbitals are calculate (if not given, the state-averaged density is considered):

* **``STATE``\ =\ *state*** Compute natural orbitals for the specified state. *state* has the form *istate.isym*, e.g., 3.2 for the third state in symmetry 2. In contrast to earlier versions, *isym* refers to the number of the irreducible representation, and not the sequence number of the state symmetry. It is therefore independent of the order in which ``WF`` cards are given. The specified state must have been optimized. If ``STATE`` is not given and two or more states are averaged, the natural orbitals are calculated with the state-averaged density matrix (default).
* **``SPIN``\ =\ *ms2*** Compute natural orbitals for states with the specified spin. *ms2* equals :math:`2*S`, i.e., 0 for singlet, 1 for doublet etc. This can be used to together with ``STATE`` to select a specific state in case that states of different spin are averaged. If ``STATE`` is not specified, the state-averaged density for all states of the given spin is used.

Several ``NATORB, CANORB``, and ``LOCORB`` cards (for different states) may follow each other. In contrast to earlier versions of Molpro the different orbital sets can all be stored in one dump record (but different records still work). See section `selecting orbitals and density matrices (ORBITAL, DENSITY) <general_program_structure.html#selecting-orbitals-and-density-matrices-orbital-density>`__ for information about dump records and how specific orbital sets can be requested in a later calculation.

.. _the_mcscf_program_multi--pseudo-canonical-orbitals:

Pseudo-canonical orbitals
=========================

``CANORB,[record,] [options]``

or

``CANONICAL,[record,] [options]``

Request to canonicalize the final orbitals, and writing them to record *record*. All options have the same effect as described for ``NATORB``.

.. _the_mcscf_program_multi--localized-orbitals:

Localized orbitals
==================

``LOCORB,[record,] [options]``

or

``LOCAL,[record,] [options]``

Request to localize the final orbitals, and writing them to record *record*. All options have the same effect as described for ``NATORB``.

Note: ``LOCAL`` is interpreted by MULTI, but ``LOCALI`` is a separate command which calls the localization program and not recognized by MULTI. In order to avoid confusion, it is recommended to use ``LOCORB`` rather then ``LOCAL`` as subcommand within MULTI.

.. _the_mcscf_program_multi--raw-orbitals:

Raw orbitals
============

``RAWORB,[record,] [options]``

The command stores the raw orbitals used in the optimization in the given record *record*. All options have the same effect as described for ``NATORB``, except the options ``SPIN`` and ``STATE`` which have no effect.
The input orbitals stay unchanged if this is combined with ``dont,orbital``.
However, if absolutely no changes in the orbitals are desired, the extra symmetry treatment has to be manually switched off with the ``NOEXTRA`` directive.

All printed `expectation values <the_mcscf_program_multi.html#calculating-expectation-values>`__ are calculated from this orbital set.

.. _the_mcscf_program_multi--diabatic-orbitals:

Diabatic orbitals
=================

In order to construct diabatic states, it is necessary to determine the mixing of the diabatic states in the adiabatic wavefunctions. In principle, this mixing can be obtained by integration of the non-adiabatic coupling matrix elements. Often, it is much easier to use an approximate method, in which the mixing is determined by inspection of the CI coefficients of the MCSCF or CI wavefunctions. This method is applicable only if the orbital mixing is negligible. For CASSCF wavefunctions this can be achieved by maximizing the overlap of the active orbitals with those of a reference geometry, at which the wavefunctions are assumed to be diabatic (e.g. for symmetry reasons). The orbital overlap is maximized using using the new ``DIAB`` command in the ``MCSCF`` program. Only the active orbitals are transformed.

This procedure works as follows: first, the orbitals are determined at the reference geometry. Then, the calculations are performed at displaced geometries, and the "diabatic" active orbitals, which have maximum overlap with the active orbitals at the reference geometry, are obtained by adding a ``DIAB`` directive to the input:

``Old form (Molpro96, obsolete):``

``DIAB,orbref, orbsav, orb1,orb2,pri``

New form:

``DIAB,orbref [,TYPE=orbtype] [,STATE=state]  [,SPIN=spin] [,MS2=ms2] [,SAVE=orbsav]  [,PRINT=pri] [,METHOD=method]``

Here *orbref* is the record holding the orbitals of the reference geometry, and *orbsav* is the record on which the new orbitals are stored. If *orbsav* is not given (recommended!) the new orbitals are stored in the default dump record (2140.2) or the one given on the ``ORBITAL`` directive (see section `saving the final orbitals <the_mcscf_program_multi.html#saving-the-final-orbitals>`__). In contrast to earlier versions of Molpro  it is possible that *orbref* and *orbsav* are the same. The specifications ``TYPE``, ``STATE``, ``SPIN`` can be used to select specific sets of reference orbitals, as described in section `selecting orbitals and density matrices (ORBITAL, DENSITY) <general_program_structure.html#selecting-orbitals-and-density-matrices-orbital-density>`__. *orb1, orb2* is a pair of orbitals for which the overlap is to be maximized. These orbitals are specified in the form *number.sym*, e.g. 3.1 means the third orbital in symmetry 1. If *orb1, orb2* are not given, the overlap of all active orbitals is maximized. *pri* is a print parameter. If this is set to 1, the transformation angles for each orbital are printed for each Jacobi iteration. *method* determines the diabatization method. *method=1* (default): use Jacobi rotations; *method=2*: use block diagonalization. Both methods yield very similar results. *method=2* must only be used for CASSCF wavefunctions. *method=-1* and *method=-2*: as the positive values, but AO overlap matrix of the current geometry is used. This minimizes the change of the MO coefficients, rather than maximizing the overlap to the neighbouring orbitals.

Using the defaults described above, the following input is sufficient in most cases:

``DIAB,orbref``

Since ``Molpro98`` it has not been necessary any more to give any ``GEOM`` and ``DISPL`` cards. The displacements and overlap matrices are computed automatically (the geometries are stored in the dump records, along with the orbitals).

The diabatic orbitals have the property that the sum of orbital and overlap contributions in the non-adiabatic coupling matrix elements become approximately zero, such that the adiabatic mixing occurs only through changes of the CI coefficients. This allows to determine the mixing angle directly from the CI coefficients, either in a simple way as described for instance in `J. Chem. Phys. <https://dx.doi.org/10.1063/1.454971>`__ **89**, 3139 (1988), or in a more advanced manner as described by Pacher, Cederbaum, and Köppel in `J. Chem. Phys. <https://dx.doi.org/10.1063/1.455268>`__ **89**, 7367 (1988). Recently, an automatic procedure, as described in J. Chem. Phys. **102**, 0000, (1999) has been implemented into Molpro. This is available in Version 99.1 and later and is described in section :doc:`quasi-diabatization <quasi-diabatization>`.

Below we present an example for the first two excited states of H\ :math:`_2`\ S, which have :math:`B_1` and :math:`A_2` symmetry in :math:`C_{2v}`, and :math:`A''` symmetry in :math:`C_S`. We first perform a reference calculation in :math:`C_{2v}` symmetry, and then determine the diabatic orbitals for displaced geometries in :math:`C_S` symmetry. Each subsequent calculation uses the previous orbitals as reference. One could also use the orbitals of the :math:`C_{2v}` calculation as reference for all other calculations. In this case one would have to take out the second-last input card, which sets ``reforb=2141.2``.

.. code-block:: text
   :caption: examples/h2s_diab.inp

   ***,H2S diabatic A" states
   
   basis=VDZ                               !use cc-pVDZ basis set
   symmetry,x,planeyz                      !use Cs symmetry & fix orientation of the molecule
   orient,noorient                         !dont allow automatic reorientation
   geometry={s;h1,s,r1;h2,s,r2,h1,theta}   !Z-matrix geometry input
   
   gprint,orbitals,civector                !global print options
   
   text,reference calculation for C2V
   theta=92.12,r1=2.3,r2=2.3               !reference geometry
   
   {hf;occ,7,2;wf,18,1}                    !scf calculation for ground state
   
   {multi;occ,9,2;closed,4,1;              !define active and inactive spaces
   wf,18,2;state,2;                        !two A" states (1B1 and 1A2 in C2v)
   orbital,2140.2}                         !save orbitals to 2140.2
   reforb=2140.2
   
   text,calculations at displaced geometries
   
   rd=[2.4,2.5,2.6]                        !define a range of bond distances
   
   do i=1,#rd                              !loop over displaced geometries
   
   r2=rd(i)                                !set r2 to current distance
   
   {multi;occ,9,2;closed,4,1;              !same wavefunction definition as at reference geom.
   wf,18,2;state,2;
   orbital,2141.2                          !save new orbitals to record
   diab,reforb}                            !compute diabatic orbitals using reference orbitals
                                           !stored on record reforb
   reforb=2141.2                           !set variable reforb to the new orbitals.
   enddo

See section :doc:`quasi-diabatization <quasi-diabatization>` for the automatic generation of diabatic energies.

.. _the_mcscf_program_multi--saving-the-ci-vectors:

Saving the CI vectors
=====================

``SAVE,CIREC=record``

Exports the CI vector(s) at record *record* such that they can be read in as a reference vector in the RS2, the RS2C, the MRCI, and the PNO-CASPT2 programs as well as in the spin-orbit coupling program.
A minimal example for the MRCI program reads: {multi;save,cirec=5100.2}{mrci,cirec=5100.2;}.
The exported CI vectors are in the CSF basis which is used in nearly all subsequent post MCSCF program.
In case determinants are used in the (state-averaged) MCSCF optimization, the CI vectors are automatically transformed into the CSF basis during the export.
This is also possible for averaging over different spins!

**Important**: If more than a single ``WF`` card is specified, the CI record is automatically increased by 100 for each ``WF`` card!
This is implemented since the CSF export is only able to store a single wavefunction configuration.

In case of multiple ``NATORB``, ``CANORB``, ``LOCORB``, or ``RAWORB`` cards, the CI vector is only exported for the last card.
If the CI vectors should be exported for the different orbital cards, please use the ``CIREC`` option in each orbital card (see `natural orbitals <the_mcscf_program_multi.html#natural-orbitals>`__).

When exporting the CI vectors for the :doc:`spin-orbit-coupling program <spin-orbit-coupling>` please note that the orbitals have to be the same if multiple CI solutions are used in the spin-orbit program.
This can be achieved by using the `RAWORB <the_mcscf_program_multi.html#raw-orbitals>`__ directive. An example can be found in the `CAHF section <the_mcscf_program_multi.html#cahf-optimization-with-the-mcscf-program>`__.

Aliases for ``CIREC`` are: ``CIVEC`` and ``CIREF``

.. _the_mcscf_program_multi--export-the-ci-vectors-in-determinant-form:

Export the CI vectors in determinant form
=========================================

``SAVE,DETCIREC=record or SAVE,DET=record``

An export of the CI vector in determinant form can be necessary for restarting a determinant based ``MULTI`` with ``CIGUESS`` (see `defining the starting CI coefficients <the_mcscf_program_multi.html#defining-the-starting-ci-coefficients>`__) or if the CI vector is used in the `CASVB program <the_vb_program_casvb.html#the-vb-program-casvb>`__.

In contrast to the CSF export, all CI vectors of different WF cards are stored in the same specified record.
An export for different orbital cards is possible as well, e.g. ``natorb,2140.2,detcirec=5100.2``.
Also, the export in determinant and CSF basis can be combined, e.g. ``save,detcirec=4100.2,cirec=5100.2``.

.. _the_mcscf_program_multi--saving-information-for-single-state-or-state-averaged-gradient-calculations:

Saving information for single-state or state-averaged gradient calculations
---------------------------------------------------------------------------

``SAVE,GRD=grdsav``

*grdsav:* record name for saving the information which is needed in a subsequent gradient calculation. This save is done automatically to record 5000.1 if the input contains a ``FORCE`` or ``OPTG`` card, and therefore, the ``GRD`` option is mostly not required.

.. _the_mcscf_program_multi--first-order-mcscf-for-large-molecules:

First-order MCSCF (for large molecules)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First-order methods allow the treatment of larger molecules by avoiding the construction of the full orbital Hessian. Since Molpro Version 2020, the first-order MCSCF is the default for density fitting calculations. Nevertheless, the implementation can be also used without density fitting by setting the following option:

{``MULTI``,\ ``FIRST-ORDER``;...} or {``MULTI``,\ ``FO``;...}

There are several different first-order methods implemented in Molpro. They can be activated by the options given below. More details about the different first-order implementations can be found in `J. Chem. Phys. <https://dx.doi.org/10.1063/1.5142241>`__ **152**, 074102 (2020).

.. _the_mcscf_program_multi--combined-first-and-second-order-optimization-default:

Combined first- and second-order optimization (default)
-------------------------------------------------------

``{DF-MULTI,SO-SCI;...}``

This method combines the second-order optimization of the active orbitals with the first-order Super-CI method. The computation time per iteration is only slightly higher compared to the Super-CI method while convergence is more robust. This is the default first-order MCSCF method and is equivalent to the ``FIRST-ORDER`` command.
The following option is available for the SO-SCI method:

* ``SO_SCI_WMK_ACT`` Starts the optimization with a WMK optimization of the active-virtual rotations (default: 0). This can save iterations, if virtual orbitals are expected to swap into the active space, e.g. Rydberg orbitals.

.. _the_mcscf_program_multi--super-ci:

Super-CI
--------

``{DF-MULTI,SUPER-CI;...}``

Activates the Super-CI implementation.

.. _the_mcscf_program_multi--uc-ah:

UC-AH
-----

``{DF-MULTI,UC-AH;...}``

Activates the uncoupled augmented Hessian method (UC-AH). This method includes the exact orbital Hessian, and it is only recommended for small molecules.

.. _the_mcscf_program_multi--second-order-mcscf:

Second-order MCSCF
~~~~~~~~~~~~~~~~~~

An improved second-order MCSCF implementation is available since Molpro 2018. It is a reimplementation of the 1984 version and features several technical improvements as for example the L-BFGS convergence acceleration. More details about the implementation can be found in `J. Chem. Phys. <https://dx.doi.org/10.1063/1.5094644>`__ **150**, 194106 (2019). The second-order MCSCF method features a larger convergence radius and it sometimes finds lower minima. However, the cost per iterations are higher than in the first-order implementation due to the computation of the full orbital Hessian. Therefore, we recommend the second-order methods for calculations with smaller molecules. The second-order MCSCF is the default method for calculations without density fitting. For density fitting, the second-order MCSCF can be activated by:

{``DF-MULTI``,\ ``SECOND-ORDER``;...} or {``DF-MULTI``,\ ``SO``;...}

.. _the_mcscf_program_multi--new-implementation-of-the-wmk-method-default:

New implementation of the WMK method (default)
----------------------------------------------

``{MULTI,WMK;...}``

This is the new second-order MCSCF implementation and this command is equivalent to the ``SECOND-ORDER`` command. By default, the L-BFGS acceleration is activated. If the L-BFGS acceleration is switched off (``MULTI,QN=0``) the following options are available to change the optimization strategy i the micro-iterations.

* ``TWO_STEP_MODE=0`` Selects strategy automatically, default for ``QN=0``.
* ``TWO_STEP_MODE=1`` Uncoupled (CI), strategy with less CI optimization steps for large active spaces
* ``TWO_STEP_MODE=2`` Uncoupled (Orb), strategy with less orbital optimization steps for a large number of orbitals

More details about the different strategies can be found in `J. Chem. Phys. <https://dx.doi.org/10.1063/1.5094644>`__ **150**, 194106 (2019).

.. _the_mcscf_program_multi--old-implementation-of-the-wmk-method:

Old implementation of the WMK method
------------------------------------

``{MULTI,WMK_OLD;...}``

This activates the original second-order implementation of 1984, which was the default method in Molpro 2015 and earlier.

.. _the_mcscf_program_multi--coupled-optimization:

Coupled optimization
--------------------

``{MULTI,WMK,COUPLED;...}``

This second-order MCSCF optimization includes the explicit coupling between the reduced CI space obtained from the Davidson method and the orbitals. Additional CI expansion vectors obtained from the coupled residuum are included increasing the level of coupling. Through the explicit coupling, the convergence is more stable, but considerable more CI steps are required.

The level of coupling can be set by the following options:

* ``ADDTHR`` Threshold for adding additional expansion vectors to the reduced CI space (default: ``ADDTHR``\ =0.05). Expansion vectors are added until the relative energy change is lower than the threshold. Hence, a lower threshold increases the level of coupling by adding more additional expansion vectors. CI computation steps are required for each additional expansion vector.
* ``NADD`` Maximal number of additional expansion vectors obtained from the coupled residuum (default: ``NADD``\ =5). It is possible to add no additional expansion vectors by setting ``NADD``\ =0.
* ``EXCLUDECIROT`` Option for excluding CI rotations between the new expansion vectors and the CI state vectors if the associated gradients are tiny. (default: ``EXCLUDECIROT``\ =1)

.. _the_mcscf_program_multi--tools-for-the-mcscf-wavefunction:

Tools for the MCSCF wavefunction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _the_mcscf_program_multi--cas-ci:

CAS-CI
------

{``CAS-CI``;...} or {``MULTI``,\ ``CAS-CI``;...}

Performs a CI optimization (equivalent to ``dont,orbital``) without changing the orbitals.
The same directives as in multi are available, hence the CI optimization with orbital restrictions are also possible.
Following options are available for controlling the CAS-CI convergence:

* ``CAS_CI_EDIFF`` Threshold for the CAS-CI energy convergence (default: 1d-10). Convergence is reached, if the energy difference of two subsequent iterations is lower than the given threshold.
* ``CAS_CI_RES`` Threshold for the CAS-CI residuum convergence (default: 1d-7). Convergence is reached, if the residuum is lower than the given threshold.
* ``CAS_CI_MAXIT`` Maximal number of Davidson iterations in the CAS-CI optimization (default: 100).

In contrast to the MCSCF optimization, the input orbitals are not changed (equivalent to `RAWORB <the_mcscf_program_multi.html#raw-orbitals>`__).
If natural or canonical orbitals are desired, the additional directive has to be added to the input.
Note that the extra symmetry treatment has to be manually switched off with the ``NOEXTRA`` directive, if absolutely no changes in the orbitals are desired.

.. _the_mcscf_program_multi--orbital-hessian-eigenvalues:

Orbital Hessian eigenvalues
---------------------------

``{MULTI,HESS_EIG;...}``

Calculates and prints the eigenvalues of the orbital Hessian for a given set of orbitals. A CAS-CI optimization is done before building the orbital Hessian. The options in `CAS-CI <the_mcscf_program_multi.html#cas-ci>`__ can be used for controlling the CI optimization.

* ``HESS_EIG_NEIG`` Number of calculated and printed eigenvalues (default: 10).
* ``HESS_EIG_REDUNDANT`` If set one, includes redundant rotations (default: 0). One should remove all FREEZE and FROZEN directives and add the NOEXTRA directive for including all possible orbital rotations.
* ``HESS_EIG_EDIFF`` Threshold for the eigenvalue convergence in the diagonalization (default: 1d-10). Convergence is reached, if the eigenvalue difference of two subsequent iterations is lower than the given threshold.
* ``HESS_EIG_RES`` Threshold for the residuum convergence in the diagonalization (default: 1d-7). Convergence is reached, if the residuum is lower than the given threshold.
* ``HESS_EIG_MAXIT`` Maximal number of Davidson iterations in the Hessian diagonalization (default: 100).

.. _the_mcscf_program_multi--options-of-the-mcscf-program:

Options of the MCSCF program
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following options are given after the multi command, e.g. ``MULTI,QN=0;``

.. _the_mcscf_program_multi--exclusive-options-for-the-first-order-mcscf:

Exclusive options for the first-order MCSCF
-------------------------------------------

* ``FO_TRUST_RADIUS`` Size of the trust radius in the orbital optimization (default: 1.5).
* ``FO_CI_FAC`` Factor by which the CI residuum is lowered in each macro-iteration (default: 0.1).
* ``FO_CI_MAXIT`` Maximal number of CI Davidson iterations performed in each macro-iteration (default: 10). If poor convergence of the CI problem is expected, convergence might be improved by increasing this number.

.. _the_mcscf_program_multi--exclusive-options-for-the-second-order-mcscf:

Exclusive options for the second-order MCSCF
--------------------------------------------

* ``SO_TRUST_RADIUS`` Size of the trust radius in the orbital optimization (default: 0.4).
* ``SO_CI_MAXIT`` Maximal number of CI Davidson iterations performed in each micro-iteration (default: 10).
* ``SO_CI_FAC`` Factor by which the CI residuum is lowered in each micro-iteration (default: 0.3).
* ``SO_INTOPT_MAXIT`` Maximal number of micro-iterations in the internal optimization (default: 4).
* ``SO_MICRO_MAXIT`` Maximal number of micro-iterations (default: 20).
* ``SO_MICRO_FAC`` Factor by which the gradient has to be reduced for convergence of the micro-iterations (default: 0.01). In addition, the square of the starting  gradient (g) is also included, i.e. min(g\*so_micro_fac,g\*g).

.. _the_mcscf_program_multi--options-of-the-l-bfgs-convergence-acceleration:

Options of the L-BFGS convergence acceleration
----------------------------------------------

* ``QN`` Activates the L-BFGS convergence acceleration in first- and second-order MCSCF (default: 1).
* ``QN_CI`` Include the CI in the L-BFGS acceleration (default: 1).
* ``QN_START`` The L-BFGS acceleration is started after reaching the given macro-iteration (default: 4).
* ``QN_STEP`` The L-BFGS acceleration is started after reaching the given step size (default: 0.1).
* ``QN_DENS`` The L-BFGS acceleration is reseted if the change in the averaged density is larger than the given value (default: 0.5).
* ``QN_ENERGY`` The L-BFGS acceleration is reseted if the energy increases (default: 1).
* ``QN_STEP_LENGTH`` Maximal step length in the orbital optimization, if the QN acceleration is activated (default: 0.5).

.. _the_mcscf_program_multi--options-of-the-augmented-hessian-method:

Options of the augmented Hessian method
---------------------------------------

* ``AUGH_MAXIT`` Maximal number of Davidson iterations in the augmented Hessian solver (default: 10). If a large number of micro-iterations is observed, convergence might be improved by increasing this number.
* ``AUGH_FAC`` Orbital gradient times this factor gives the accuracy of the Davidson method in the augmented Hessian solver. (default: 0.1)
* ``AUGH_DAMPING`` Activates damping in the augmented Hessian solver (default: 1)
* ``AUGH_DAMPING_START`` Start value of the damping in the augmented Hessian solver (default: 1.0). Increased damping reduces the step-size.

.. _the_mcscf_program_multi--level-shifts:

Level shifts
------------

Level shifts for the closed-shell and active orbitals. These options are similar to the Hartree-Fock program (see `options <the_scf_program.html#options>`__), and they can be helpful for non-converging multi calculations. Often, a good starting point is ``SHIFTC``\ =-0.3 and ``SHIFTO``\ =-0.15. A large negative level shift might slow down the convergence considerably.

* ``SHIFTC`` Level shift for the closed-shell orbitals (default: 0.0).
* ``SHIFTO`` Level shift for the active orbitals (default: 0.0).
* ``SHIFT_AUTO`` Automatic adjustments of the level shifts (default: 1).

.. _the_mcscf_program_multi--various-more-options:

Various more options
--------------------

* ``MAXP_CI`` Max. number of P-space CI configurations (default: 400)
* ``MAXP_ROT`` Number of P-space rotations (default: 200)
* ``START_CI`` If set to one, the CI is fully convergence in the first macro-iteration (default: 0). This is done automatically, if the starting orbitals have been optimized with the MCSCF program.
* ``EXACT_DIAG`` If set one, the Hamiltonian is diagonalized exactly (default: 0)
* ``SPINCHECK`` Checks for spin contamination when using determinants (default: 1)
* ``VERBOSITY`` Level of print out information (default: 1). Showing all possible information at VERBOSITY=4.
* ``MANY_STATES`` Activates an alternative CI solver which is more specialized on many CI states.

.. _the_mcscf_program_multi--directives-of-the-mcscf-program:

Directives of the MCSCF program
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following directives are given as ``MULTI;CONFIG,CSF;``.

.. _the_mcscf_program_multi--selecting-the-ci-method:

Selecting the CI method
-----------------------

``CONFIG,key;``

*key* may be ``DET`` or ``CSF``, and defaults to ``CSF``. If no ``CONFIG`` or ``SELECT`` card is given, the default is determinants (CASSCF).

Note that state averaging of different spin-states is only possible with Slater determinants, i.e. no ``CONFIG`` or ``SELECT`` must be given in this case.

.. _the_mcscf_program_multi--disabling-the-optimization:

Disabling the optimization
--------------------------

Some procedures can be disabled more simply using the ``DONT`` directive. ``DONT``,\ *code* where *code* may be

* ``ORBITAL`` Do initial CI but don’t optimize orbitals.
* ``WAVEFUNC`` Do not optimize the orbitals and CI coefficients (i.e. do only wavefunction analysis, provided the orbitals and CI coefficients are supplied (see ``START card``)).
* ``WVFN`` Alias for WAVEFUNC.
* ``ANAL`` Do no wavefunction analysis.
* ``EXPEC`` Skip the calculation of the transition and expectation values.

.. _the_mcscf_program_multi--disabling-the-extra-symmetry-mechanism:

Disabling the extra symmetry mechanism
--------------------------------------

``NOEXTRA``

This card disables the search for extra symmetries. By default, if extra symmetries are present, each orbital is assigned to such an extra symmetry and rotations between orbitals of different extra symmetry are not performed.

.. _the_mcscf_program_multi--print-options:

Print options
-------------

``ORBPRINT[,nvirt]``

requests the occupied and *nvirt* virtual orbitals in each symmetry to be printed (default *nvirt*\ =0). By default, the program does not print the orbitals, unless the ``ORBPRINT`` directive or a global ``GPRINT,ORBITALS`` (see section `global Print Options (GPRINT/NOGPRINT) <program_control.html#global-print-options-gprint-nogprint>`__) command is present. Specific orbital sets can be printed using the ``PRINT`` option on a ``NATORB``, ``CANORB``, or ``LOCORB`` card (see section `natural orbitals <the_mcscf_program_multi.html#natural-orbitals>`__).

To print additional information at the end of the calculation, use

``PRINT,key1,key2,$\ldots$;``

Printing is switched on for *key1*, *key2*,\ :math:`\ldots` . To print information in each iteration, use

``IPRINT,key1,key2,$\ldots$;``

Possible print keys are:

* ``MICRO`` print details of “microiterations” — useful for finding out what’s going wrong if no convergence
* ``PSPACE`` print list of configurations making up the “primary” space
* ``ORBITALS`` print orbitals (see also ``ORBPRINT``)
* ``NATORB`` print natural orbitals (see also ``ORBPRINT``)
* ``CIVECTOR`` print CI vector (better use ``CANORB`` or ``NATORB``)
* ``STEP`` Prints information about the orbital rotations
* ``GRADIENT`` print gradient

.. _the_mcscf_program_multi--convergence-thresholds:

Convergence thresholds
----------------------

Convergence thresholds can be modified using

``ACCURACY,[GRADIENT=conv] [,STEP=sconv] [,ENERGY=econv]``

where

* ***conv*** Threshold for orbital gradient (default: :math:`10^{-5}`).
* ***econv*** Threshold for change of total energy (default: :math:`10^{-6}` for second-order and :math:`10^{-8}` for first-order).
* ***sconv*** Threshold for size of step, works only with ``MULTI``,\ ``WMK_OLD`` (default :math:`10^{-3}`).

The default values can be modified using the global ``GTHRESH`` command (see section `global Thresholds (GTHRESH) <program_control.html#global-thresholds-gthresh>`__). Normally, the above default values are appropriate.

.. _the_mcscf_program_multi--maximum-number-of-iterations:

Maximum number of iterations
----------------------------

``MAXITER,maxit;``

*maxit* is maximum number of iterations (default 20). If the calculation does not converge in the default number of iterations, you should first think about the reason before increasing the limit. In most cases the choice of active orbitals or of the optimized states is not appropriate (see introduction of MULTI). The maximum allowed value of *maxit* is 40. If the calculation has not converged in this number of iterations, it is likely that the active space is not reasonable. Note: slow convergence can occur in RASSCF calculations if single excitations into weakly occupied orbitals are present. These should be eliminated using

``RESTRICT,-1,-1,orbital list``

.. _the_mcscf_program_multi--special-optimization-parameters-old-implementation:

Special optimization parameters (old implementation)
----------------------------------------------------

This is only available for the WMK program activated by ``MULTI``,\ ``WMK_OLD``. The following parameters can also be given as options on the ``MULTI`` command line.

``FAILSAFE``

Use options for more robust convergence

``STEP,radius,trust1,tfac1,trust2,tfac2;``

Special parameters for augmented hessian method. For experts only!

``GOPER,igop;``

Use G-operator technique in microiterations (Default). If igop.lt.0 do not use G-operators.

``COPT,ciacc,copvar,maxci,cishft,icimax,icimx1,icimx2,icstrt,icstep;``

Special parameters for the direct CI method. For experts only!

* ***ciacc*** grad threshold for CI diagonalization
* ***copvar*** start threshold for CI-optimization
* ***maxci*** max. number of CI-optimizations per microiteration
* ***cishft*** denominator shift for q-space
* ***icimax*** max. number of CI-optimizations in first macroiteration
* ***icimx1*** max. number of CI-optimizations in second and subsequent iterations
* ***icimx2*** max. number of CI-optimizations in internal absorption step
* ***icstrt*** first microiteration with CI-optimization
* ***icstep*** microiteration increment between CI-optimizations

``INTOPT,maxito,maxitc,maxrep,nitrep,iuprod;``

Special parameters for internal optimization scheme. For experts only!

``NONLINEAR,itmaxr,ipri,drmax,drdamp,gfak1,gfak2,gfak3,irdamp,ntexp``

Special parameters for non-linear optimization scheme. For experts only!

Old form (obsolete):

``THRESH,thrpri,thrpun,varmin,varmax,thrdiv,thrdoub``

New form:

``THRESH [,THRPRI=thrpri] [,THRPUN=thrpun] [,VARMIN=varmin] [,THRDIV=thrdiv] [,THRDOUB=thrdoub]``

* ***thrpri*** threshold for printing CI coefficients (default 0.04)
* ***thrpun*** threshold for writing CI coefficients to the punch file. Default is no write to the punch file
* ***varmin,varmax*** thresholds for non-linear optimization scheme. For experts only!
* ***thrdoub*** threshold for detecting almost doubly occupied orbitals for inclusion into the pseudo canonical set (default 0, i.e. the feature is disabled).

``DIIS,disvar,augvar,maxdis,maxaug,idsci,igwgt,igvec,idstrt,idstep;``

Special parameters for DIIS convergence acceleration. For experts only!

.. _the_mcscf_program_multi--saving-wavefunction-information-for-casvb:

Saving wavefunction information for CASVB
-----------------------------------------

``VBDUMP[,vbdump];``

For users of the valence bond program *CASVB*, all wavefunction information that may subsequently be required is saved to the record *vbdump*. The default is not to write this information. If the keyword is specified without a value for *vbdump*, then record 4299.2 is used. This keyword is not needed prior to variational *CASVB* calculations.

.. _the_mcscf_program_multi--saving-transformed-integrals:

Saving transformed integrals
----------------------------

``TRNINT,trnint;``

*trnint* specifies the record name for integrals in the basis of active CASSCF MOs. These are used for example by *CASVB* (see section `recovering CASSCF CI vector and VB wavefunction <the_vb_program_casvb.html#recovering-casscf-ci-vector-and-vb-wavefunction>`__). The default value for *trnint* is 1900.1.

.. _the_mcscf_program_multi--cahf-optimization-with-the-mcscf-program:

CAHF optimization with the MCSCF program
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The configuration-averaged Hartree-Fock (CAHF) optimization is equivalent to a state-averaged optimization averaging over all possible irreducible representations and spin-manifolds.
In this case, the density can be evaluated analytically, and a CI optimization is not needed.
More details on the CAHF optimization can be found in the `Hartree-Fock program <the_scf_program.html#configuration-averaged-hartree-fock-cahf-or-df-cahf>`__.

The CAHF optimization with multi is activated by the following option:

``{MULTI,CAHF;...}``

This option works for all implemented first- and second-order optimization methods, except the Super-CI method.
Note that the final canonical orbitals vary from the HF ones, since a different Fock matrix is diagonalized.

Each CAHF shells is set by the following directive

.. code-block:: text

   CAHF,nel,orbital list

where nel is the number of electrons in the active shell and the orbital list is given in the form number1.sym1,number2.sym2,... . A range of orbitals in the same symmetry can be given as number1.sym,-number2.sym, which means from number1 to number2.
All CAHF orbitals have to be active orbitals, otherwise an error is thrown.
If no CAHF directive is given, all active orbitals and electrons are considered in a single CAHF shell.

The CI optimization is entirely skipped in the CAHF optimization, since it likely involves a massive number of states.
A subsequent CI optimization based on the WF cards in the input can be turned on by the option {``MULTI``,\ ``CAHF``,\ ``CAHF_DO_CI``;...} or by running a CAS-CI optimization with the resulting orbitals (see `CAS-CI optimization <the_mcscf_program_multi.html#cas-ci>`__).

Example:

.. code-block:: text
   :caption: examples/cahf_cu2_multi.inp

   memory,16,m;
   gprint,orbitals
   bohr
   nosym
   noextra
   set,charge = +4
   geometry={
   Cu1   10.000000000    0.000000000    0.000000000
   Cu2    0.000000000    0.000000000    0.000000000
   }
   basis=def2-tzvp
   
   {avas,thr=0.5,nela=18,locorb=1      ! Generate localized 3d orbitals on each Cu atom
   center,1,3d;                        ! as a starting guess
   center,2,3d;
   }
   
   {df-multi,so-sci,cahf;            
   start,local;                       
   cahf,9,19.1,-23.1;
   cahf,9,24.1,-28.1;
   }
   
   {df-casci,cisave=5000.2;
   wf,spin=0,sym=1;state,25;}
   
   {df-casci,cisave=5001.2;
   wf,spin=2,sym=1;state,25;}
   
   {hlsmat,ecp,5000.2,5001.2;}

.. _the_mcscf_program_multi--rhf-optimization-with-the-mcscf-program:

RHF optimization with the MCSCF program
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It can be helpful to use the multi program for a restricted-open shell Hartree-Fock (RHF) optimization, since it often provides a more robust optimization than the Hartree-Fock program. This is possible for all first- and second-order methods by the option:

``{MULTI,RHF;...}``

After the optimization, the final orbitals are always calculated as canonical orbitals reproducing the orbitals from the Hartree-Fock program.
(Note that the usual MCSCF pseudo canonical orbitals are not exactly the same as the HF ones).
Also, the final orbitals can be used in subsequent single-reference programs.
The closed, occ and wf cards have to be set accordingly such that the MCSCF wavefunction contains only the open-shell determinant, otherwise, a error is thrown.
However, this feature has not been heavily tested for all possible combinations of single-reference tools! Please submit a bug report if crashes or errors appear.

.. _the_mcscf_program_multi--calculating-expectation-values:

Calculating expectation values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, the program calculates the dipole expectation and transition moments. Further expectation values or transition properties can be computed using the ``TRAN, TRAN2`` and ``EXPEC, EXPEC2`` directives. The orbitals used for the calculation of the expectation values can be displayed using the `RAWORB <the_mcscf_program_multi.html#raw-orbitals>`__ directive.

.. _the_mcscf_program_multi--matrix-elements-over-one-electron-operators:

Matrix elements over one-electron operators
-------------------------------------------

``EXPEC,[print_zero],$oper_1,oper_2,\ldots,oper_n$\\``
``TRAN,[state],[print_zero],$oper_1,oper_2,\ldots,oper_n$``

Calculate expectation values and transition matrix elements for the given one-electron operators.
The [*state*] command is optional, and can be used to specify the states for which the matrix elements are calculated (see below).
With ``EXPEC`` only expectation values are calculated. :math:`oper_i` is a codeword for the operator. The available operators and their associated keywords are given in section `One-electron operators and expectation values (GEXPEC) <program_control.html#one-electron-operators-and-expectation-values-gexpec>`__. Only non-zero values are printed, unless the (optional) command *print_zero* is given!

Since Molpro 2021, only the transition matrix elements with the ground state are calculated as the default.
It is possible to specify the states used in the calculation by the following options for [*state*]:

* ``ground``: Only calculate the matrix elements including the ground state (default for ``TRAN``).
* ``all``: Calculate all matrix elements (default for ``EXPEC``).
* ``state=//state//,MS2=//spin//``: Only calculate the matrix elements including the specified state (e.g. state=2.1,ms2=0 for the first excited singlet state in symmetry 1).
* ``none``: Skip the matrix elements for the given operators.

Example:

.. code-block:: text

   {multi;
   TRAN,none,DM;              ! skips the dipole moment calculation
   TRAN,ground,print_zero,EF; ! all electric field elements with the ground state are printed including zero values
   TRAN,state=2.1,MS2=0,QM;   ! quadrupole moments for the second singlet state in symmetry 1
   }

.. _the_mcscf_program_multi--matrix-elements-over-two-electron-operators:

Matrix elements over two-electron operators
-------------------------------------------

``EXPEC2,$oper_1,oper_2,\ldots,oper_n$\\``
``TRAN2,[print_zero],$oper_1,oper_2,\ldots,oper_n$``

Calculate transition matrix elements for two-electron operators. This is presently only useful for angular momentum operators. With ``EXPEC2`` only diagonal matrix elements will be computed.

``Note that only matrix elements between states of the same symmetry can be computed.``

For instance

* ``TRAN2,LXX`` calculates matrix elements for :math:`L_x^2`
* ``TRAN2,LYY`` calculates matrix elements for :math:`L_y^2`
* ``TRAN2,LXZ`` calculates matrix elements for :math:`\frac{1}{2}(L_xL_z+L_zL_x)`
* ``TRAN2,LXX,LYY,LZZ`` calculates matrix elements for :math:`L_x^2`, :math:`L_y^2`, and :math:`L_z^2`. The matrix elements for the sum :math:`L^2` are also printed.

Only the non-zero values are printed for transition elements, while all values are printed for the expectation values. The zero values of the transition elements can be optionally printed by adding the command *print_zero* as for the one-electron operator matrix elements.

The special two-electron operator MPOL, i.e.

* ``EXPEC2,MPOL``
* ``TRAN2,MPOL``

will calculate expectation values and matrix elements of the mass polarization operator :math:`P_e^2=-VELO^2` which is one of the non-adiabatic correction terms. The corresponding variables are MPOL and TRMPOL.

.. _the_mcscf_program_multi--saving-the-density-matrix:

Saving the density matrix
-------------------------

``DM,[spindens]``

If the ``DM`` directive is given, the first order density matrix in AO basis is written to the dump record specified on the ``ORBITAL`` card (default 2140.2). If no ``ORBITAL`` card is present, but a record is specified on a ``NATORB``, ``CANORB``, or ``LOCORB`` card, the densities are saved to the first record occurring in the input. In a state-averaged calculation the SA-density, as well the individual state densities, are saved. See section `selecting orbitals and density matrices (ORBITAL, DENSITY) <general_program_structure.html#selecting-orbitals-and-density-matrices-orbital-density>`__ for information about how to recover any of these densities for use in later programs.

If *spindens* is a number greater than zero, the spin density matrices are also saved. Note that a maximum of 50 density matrices can be saved in one dump record.

If no ``DM`` directive is given), the first order density matrix is saved in single-state calculations, and only the stage-averaged density matrix in state-averaged calculations.

.. _the_mcscf_program_multi--coupled-perturbed-mcscf:

Coupled-perturbed MCSCF
~~~~~~~~~~~~~~~~~~~~~~~

The coupled-perturbed (CP) MCSCF is required for computing gradients with state-averaged orbitals, non-adiabatic couplings, difference gradients or polarizabilities.
The CP-MCSCF program has been reimplemented in Molpro 2020 to improve robustness and performance

The following options are available in the CP-MCSCF program:

* ``CP_MCSCF_OLD`` Activates the old implementation of Molpro 2019 and earlier (default: 0).
* ``CP_MCSCF_VERBOSITY`` Verbosity of the CP-MCSCF program. Subspace iterations can be printed with CP_MCSCF_VERBOSITY=2 (default: 1).
* ``CP_MCSCF_MAXIT`` Maximal number of iterations of the iterative subspace solver for the z-equation (default: 100).
* ``CP_MCSCF_ALL_RHS`` 0: z-equation is solved for each RHS separately, 1: the z-equation is solved for all RHS together, 2: automatic decision (default: 2).

.. _the_mcscf_program_multi--gradients-for-sa-mcscf:

Gradients for SA-MCSCF
----------------------

For computing state-averaged gradients, use

``CPMCSCF,GRAD,state,[SPIN=spin],[MS2=ms2],[ACCU=thresh],[RECORD=record]``

where *state* specifies the state (e.g., 2.1 for the second state in symmetry 1) for which the gradients will computed. *spin* specifies the spin of the state: this is half the value used in the corresponding WF card (e.g., 0=Singlet, 0.5=Doublet, 1=Triplet). Alternatively, ``MS2`` can be used, where *ms2* = 2\*spin, i.e., the same as specified on ``WF`` cards. The specification of ``SPIN`` or ``MS2`` is only necessary if states with different spin are state-averaged. *record* specifies a record on which the gradient information is stored (the default is 5101.1). *thresh* is a threshold for the accuracy of the CP-MCSCF solution. The default is 1.d-7.

The gradients are computed by a subsequent call to ``FORCES`` or ``OPTG`` (see Section `State-averaged MCSCF gradients with Cadpac <energy_gradients.html#state-averaged-mcscf-gradients-with-cadpac>`__)

Note: if for some reason the gradients are to be computed numerically from finite energy differences, it is in state-averaged calculations necessary to give, instead of the ``CPMCSCF`` input, the following:

``SAVE,GRAD=-1``

Otherwise the program will stop with an error message.

.. _the_mcscf_program_multi--difference-gradients-for-sa-mcscf:

Difference gradients for SA-MCSCF
---------------------------------

For computing difference gradients, use

``CPMCSCF,DGRAD,state1,state2,[ACCU=thresh],[RECORD=record]``

where *state1* and *state2* specify the two states considered. (e.g., 2.1,3.1 for the second and third states in symmetry 1) The gradient of the energy difference will be computed. Both states must have the same symmetry. *record* specifies a record on which the gradient information is stored (the default is 5101.1). *thresh* is a threshold for the accuracy of the CP-MCSCF solution. The default is 1.d-7.

The gradients are computed by a subsequent call to ``FORCES`` or ``OPTG``. (see Section `State-averaged MCSCF gradients with Cadpac <energy_gradients.html#state-averaged-mcscf-gradients-with-cadpac>`__)

.. _the_mcscf_program_multi--non-adiabatic-coupling-matrix-elements-for-sa-mcscf:

Non-adiabatic coupling matrix elements for SA-MCSCF
---------------------------------------------------

For computing non-adiabatic coupling matrix elements analytically, use

``CPMCSCF,NACM,state1,state2,[ACCU=thresh],[RECORD=record]``

where *state1* and *state2* specify the two states considered. (e.g., 2.1,3.1 for the second and third states in symmetry 1) Both states must have the same symmetry. *record* specifies a record on which the gradient information is stored (the default is 5101.1). This will be read in the subsequent gradient calculation. *thresh* is a threshold for the accuracy of the CP-MCSCF solution. The default is 1.d-7.

``NADC and NADK are an aliases for NADC, and SAVE is an alias for RECORD.``

The matrix elements for each atom are computed by a subsequent call to ``FORCES`` (see Section `State-averaged MCSCF gradients with Cadpac <energy_gradients.html#state-averaged-mcscf-gradients-with-cadpac>`__).

Note: this program is not yet extensively tested and should be used with care!

.. _the_mcscf_program_multi--mcscf-hessians:

MCSCF hessians
--------------

The MCSCF/CASSCF hessian can be computed analytically (only without symmetry) using

``CPMCSCF,HESS,[ACCU=value]``

where the ``ACCU`` option specifies the convergence threshold in the CPMCSCF calculation (default 1.d-4). The hessian is stored on record 5300.2 and can be used in a subsequent frequency calculation.

Example:

.. code-block:: text

   {multi;cpmcscf,hess,accu=1.d-5}
   frequencies

Note that the ``NOEXTRA`` option is used when computing a hessian.

.. _the_mcscf_program_multi--optimizing-valence-bond-wavefunctions:

Optimizing valence bond wavefunctions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``VB={…}``

Using this keyword, the optimization of the CI coefficients is carried out by *CASVB*. The ``VB`` keyword can be followed by any of the directives described in section :doc:`the VB program CASVB <the_vb_program_casvb>`. Energy-based optimization of the VB parameters is the default, and the output level for the main *CASVB* iterations is reduced to :math:`-1`.

.. _the_mcscf_program_multi--total-position-spread-tensor-tps:

Total Position-Spread tensor (TPS)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Bibliography:

M. El Khatib, T. Leininger, G.L. Bendazzoli, and S. Evangelisti, `Chem. Phys. Lett. <https://dx.doi.org/10.1016/j.cplett.2013.10.080>`__ **591**, 58 (2014).

O. Brea, M. El Khatib, C. Angeli, G.L. Bendazzoli, S. Evangelisti, and T. Leininger, `J. Chem. Theory Comput. <https://dx.doi.org/10.1021/ct400453b>`__ **9**, 5286 (2013).
All publications resulting from use of this program must acknowledge the above. See also:

W. Kohn, Phys. Rev. 133 (1964) A171.
R. Resta, S. Sorella, `Phys. Rev. Lett. <https://dx.doi.org/10.1103/PhysRevLett.82.370>`__ **82**, 370 (1999).
The total position-spread (TPS) tensor is a quantity originally introduced in the modern theory of electrical conductivity. In the case of molecular systems, this tensor measures the fluctuation of the electrons around their mean positions, which corresponds to the delocalization of the electronic charge within a molecular system. The TPS can discriminate between metals and insulators taking information from the ground state wave function. This quantity can be very useful as an indicator to characterize Intervalence charge transfer processes, the bond nature of molecules (covalent, ionic or weakly bonded), and Metal-insulator transition.

The program is invoked by ``TRAN2`` inside the ``MULTI`` input block:

``TRAN2,RXX,RYY,RZZ,RXY,RXZ,RYZ;``

The three different classes of contributions to the CASSCF wave function can be printed by using the keyword:

``IPRINT,TPS1;``

This will print the core-core, core-active, and active-active contributions of the TPS tensor are printed.

.. _the_mcscf_program_multi--hints-and-strategies:

Hints and strategies
~~~~~~~~~~~~~~~~~~~~

MCSCF is not a “black box” procedure like SCF! For simple cases, for example a simple CASSCF with no ``CLOSED`` orbitals, this program will converge in two or three iterations. For more complicated cases, you may have more trouble. In that case, consider the following:

* Always start from neighbouring geometry orbitals when available (this is the default).
* The convergence algorithm is more stable when there are no ``CLOSED`` orbitals, i.e., orbitals doubly occupied in all configurations, but fully optimized. Thus a reasonable approach is to make an initial calculation with ``CLOSED`` replaced by ``FROZEN`` (all doubly occ. frozen).

You can often get a clue about where the program starts to diverge if you include:

``IPRINT,MICRO;``

in the data. Also consider the general remarks at the beginning of this chapter. For the details of the algorithms used, see J. Chem. Phys 82, 5053 (1985); `Chem. Phys. Lett. <https://dx.doi.org/10.1016/0009-2614(85)80025-7>`__ **115**, 259 (1985); Advan. Chem. Phys. 59, 1 (1987);

.. _the_mcscf_program_multi--examples:

Examples
~~~~~~~~

The simplest input for a CASSCF calculation for H\ :math:`_2`\ O, :math:`C_{2v}` symmetry, is simply:

.. code-block:: text
   :caption: examples/h2o_casscf.inp

   geometry={o;h1,o,r;h2,o,r,h1,theta}   !Z-matrix geometry input
   r=1 ang                               !bond length
   theta=104                             !bond angle
   hf                                    !do scf calculation
   multi                                 !do full valence casscf

This could be extended, for instance, by the following input cards

.. code-block:: text

   OCC,4,1,2;       !  specify occupied space
   CLOSED,2         !  specify closed-shell (inactive) orbitals
   FROZEN,1;        !  specify frozen core orbitals
   WF,10,1;         !  define wavefunction symmetry
   START,2100.2;    !  read guess orbitals from record 2100, file 2
   ORBITAL,2140.2;  !  save final orbitals to record 2140, file 2
   NATORB,PRINT,CI  !  print natural orbitals and diagonalize the hamiltonian
                    !  for the natural orbitals. The largest CI coefficients
                    !  are printed.

Example for a state-averaged calculation for CN, :math:`X` and :math:`B` :math:`^2\Sigma^+` states, and :math:`A` :math:`^2\Pi_x`, :math:`^2\Pi_y` states averaged. A full valence CASSCF calculation is performed

.. code-block:: text
   :caption: examples/cn_sa_casscf.inp

   ***,cn
   r=2.2                             !define bond length
   geometry={c;n,c,r}
   {rhf;occ,5,1,1;wf,13,1,1;              !RHF calculation for sigma state
   orbital,2100.2}                       !save orbitals to record 2100.2 (default)
   
   {multi;occ,6,2,2;closed,2;             !Define active and inactive orbitals
   start,2100.2;                         !Start with RHF orbitals from above
   save,ref=4000.2                       !Save configuration weights for CI in record 4000.2
   wf,13,1,1;state,2;wf,13,2,1;wf,13,3,1;!Define the four states
   natorb,ci,print;                      !Print natural orbitals and associated ci-coefficients
   tran,lz                               !Compute matrix elements over LZ
   expec2,lzz}                           !compute expectation values for LZZ

Example for an RASSCF (restricted active space) calculation for N\ :math:`_2`, including SCF determinant plus all double excitations into valence orbitals. The single excitations are excluded. :math:`D_{2h}` symmetry, CSF method used:

.. code-block:: text
   :caption: examples/n2_rasscf.inp

   ***,N2
   geometry={N1;N2,N1,r}                 !geometry input
   r=2.2                                 !bond length
   {hf;occ,3,1,1,,2;wf,14,1;save,2100.2} !scf calculation
   
   {multi;occ,3,1,1,,3,1,1;              !Define occupied orbitals
   frozen,1,,,,1,2100.2;                   !Define frozen core scf orbitals
   config;                               !Use CSF method
   wf,14,1;                              !Define state symmetry
   restrict,0,2,3.5,1.6,1.7;             !Restriction to singles and doubles
   restrict,-1,-1,3.5,1.6,1.7;           !Take out singles
   print,ref1                            !Print configurations
   natorb,ci,print}                      !Print natural orbitals and CI coeffs
