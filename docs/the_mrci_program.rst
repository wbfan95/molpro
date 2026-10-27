.. raw:: html

   <span id="additional-reference-symmetries"></span>

.. raw:: html

   <span id="canonicalizing-external-orbitals"></span>

.. raw:: html

   <span id="closed-shell-orbitals"></span>

.. raw:: html

   <span id="cluster-corrections-for-multi-state-mrci"></span>

.. raw:: html

   <span id="coupled-electron-pair-approximation"></span>

.. raw:: html

   <span id="coupled-pair-functional-acpf-aqcc"></span>

.. raw:: html

   <span id="defining-reference-state-numbers"></span>

.. raw:: html

   <span id="defining-state-numbers"></span>

.. raw:: html

   <span id="defining-the-orbitals"></span>

.. raw:: html

   <span id="defining-the-state-symmetry"></span>

.. raw:: html

   <span id="explicitly-correlated-mrci-f12"></span>

.. raw:: html

   <span id="explicitly-specifying-reference-configurations"></span>

.. raw:: html

   <span id="frozen-core-orbitals"></span>

.. raw:: html

   <span id="level-shifts"></span>

.. raw:: html

   <span id="maximum-number-of-iterations"></span>

.. raw:: html

   <span id="miscellaneous-options"></span>

.. raw:: html

   <span id="miscellaneous-parameters"></span>

.. raw:: html

   <span id="miscellaneous-thresholds"></span>

.. raw:: html

   <span id="natural-orbitals"></span>

.. raw:: html

   <span id="occupation-restrictions"></span>

.. raw:: html

   <span id="occupied-orbitals"></span>

.. raw:: html

   <span id="one-electron-properties"></span>

.. raw:: html

   <span id="print-options"></span>

.. raw:: html

   <span id="projected-excited-state-calculations"></span>

.. raw:: html

   <span id="restricting-numbers-of-expansion-vectors"></span>

.. raw:: html

   <span id="restriction-of-classes-of-excitations"></span>

.. raw:: html

   <span id="saving-the-density-matrix"></span>

.. raw:: html

   <span id="saving-the-wavefunction"></span>

.. raw:: html

   <span id="selecting-configurations"></span>

.. raw:: html

   <span id="selecting-the-primary-configuration-set"></span>

.. raw:: html

   <span id="specifying-correlation-of-orbital-pairs"></span>

.. raw:: html

   <span id="starting-wavefunction"></span>

.. raw:: html

   <span id="transition-matrix-element-options"></span>

.. raw:: html

   <span id="transition-moment-calculations"></span>

.. _the_mrci_program--the-mrci-program:

The MRCI program
================

Multiconfiguration reference internally contracted configuration interaction

Bibliography:

H.-J. Werner and P.J. Knowles, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.455556>`__ **89**, 5803 (1988).
P.J. Knowles and H.-J. Werner, `Chem. Phys. Lett. <https://dx.doi.org/10.1016/0009-2614(88)87412-8>`__ **145**, 514 (1988).

For excited state calculations:

P. J. Knowles and H.-J. Werner, Theor. Chim. Acta **84**, 95 (1992).

For explicitly correlated MRCI (MRCI-F12):

T. Shiozaki, G. Knizia, and H.-J. Werner, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3528720>`__ **134**, 034113 (2011);
T. Shiozaki and H.-J. Werner, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3587632>`__ **134**, 184104 (2011);
T. Shiozaki and H.-J. Werner, `Mol. Phys. <https://dx.doi.org/10.1080/00268976.2013.779393>`__ **111**, 607 (2013).

All publications resulting from use of the corresponding methods must acknowledge the above.

The first internally correlated MRCI program was described in:

H.-J. Werner and E.A. Reinsch, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.443357>`__ **76**, 3144 (1982).
H.-J. Werner, Adv. Chem. Phys. 59, 1 (1987).

The command ``CI`` or ``CI-PRO`` or ``MRCI`` calls the MRCI program.
The command ``MRCI-F12`` calls the explicitly correlated MRCI-F12 program.
The command ``CISD`` calls fast closed-shell CISD program.
The command ``QCI`` calls closed-shell quadratic CI program.
The command ``CCSD`` calls closed-shell coupled-cluster program.

The following options may be specified on the command line:

* ``NOCHECK`` Do not stop if no convergence.
* ``DIRECT`` Do calculation integral direct.
* ``NOSING`` Do not include singly external configurations.
* ``NOPAIR`` Do not include doubly external configurations (not valid for single reference methods).
* **``MAXIT=``\ *value*** Maximum number of iterations.
* **``MAXITI=``\ *value*** Maximum number of microiterations (for internals).
* **``SHIFTI=``\ *value*** Denominator shift for update of internal configurations.
* **``SHIFTS=``\ *value*** Denominator shift for update of singles.
* **``SHIFTP=``\ *value*** Denominator shift for update of doubles.
* **``THRDEN=``\ *value*** Convergence threshold for the energy.
* **``THRVAR=``\ *value*** Convergence threshold for the CI-vector. This applies to the square sum of the changes of the CI-coefficients.
* ``SWAP|NOSWAP`` If ``SWAP`` is given, the MRCI wavefunctions are reordered according to maximum overlap with the reference functions (this only applies in multi-state calculations). The default is ``NOSWAP``, i.e. the states are ordered according to increasing MRCI energy.
* **``ROTREF=``\ *value*** If *value*\ =0 the cluster corrections are not printed for the rotated reference energies (cf. Section `cluster corrections for multi-state MRCI <the_mrci_program.html#cluster-corrections-for-multi-state-mrci>`__). If *value*\ =1 all corrections are printed. If *value*\ =2 (default) the reference are transformed to maximize the overlap with the final MRCI wavefunctions, and the cluster corrections are computed using these rotated reference states. If *value*\ =-1 the 2009.1 behaviour is recovered.
* **``CIREC=``\ *record*** If given, the program attempts reading the reference vectors from a previous CASSCF calculation. The vectors must have been saved in the CASSCF using ``SAVE,CIREC=``\ *record* This will only work if the active spaces in the CASSCF and MRCI are the same.

.. _the_mrci_program--introduction:

Introduction
============

The internally contracted MRCI program is called by the CI command. This includes as special cases single reference CI, CEPA, ACPF, MR-ACPF and MR-AQCC. For closed-shell reference functions, a special faster code exists, which can be called using the CISD, QCI, or CCSD commands. This also allows to calculate Brueckner orbitals for all three cases (QCI and CCSD are identical in this case).

The explicitly correlated variant is called by the command ``MRCI-F12``, see section `explicitly correlated MRCI-F12 <the_mrci_program.html#explicitly-correlated-mrci-f12>`__.

With no further input cards, the wavefunction definition (core, closed, and active orbital spaces, symmetry) corresponds to the one used in the most recently done SCF or MCSCF calculation. By default, a CASSCF reference space is generated. Other choices can be made using the ``OCC``, ``CORE``, ``CLOSED``, ``WF``, ``SELECT``, ``CON``, and ``RESTRICT`` cards. The orbitals are taken from the corresponding SCF or MCSCF calculation unless an ``ORBITAL`` directive is given. The wavefunction may be saved using the ``SAVE`` directive, and restarted using ``START``. The ``EXPEC`` directive allows to compute expectation values over one-electron operators, and the ``TRAN`` directive can be used to compute transition matrix elements for one-electron properties. Natural orbitals can be printed and saved using the ``NATORB`` directive.

For excited state calculations see ``STATE``, ``REFSTATE``, and ``PROJECT``.

.. _the_mrci_program--specifying-the-wavefunction:

Specifying the wavefunction
===========================

Note: All occupations must be given before ``WF``, ``PAIRSS``, ``DOMAIN``, ``REGION`` or other directives that need the occupations.

.. _the_mrci_program--occupied-orbitals:

Occupied orbitals
=================

``OCC,$n_1,n_2,\ldots,n_8$;``

:math:`n_i` specifies numbers of occupied orbitals (including ``CORE`` and ``CLOSED``) in irreducible representation number :math:`i`. If not given, the information defaults to that from the most recent SCF, MCSCF or CI calculation.

.. _the_mrci_program--frozen-core-orbitals:

Frozen-core orbitals
====================

``CORE,$n_1,n_2,\ldots,n_8$;``

:math:`n_i` is the number of frozen-core orbitals in irrep number :math:`i`. These orbitals are doubly occupied in all configurations, i.e., not correlated. If no ``CORE`` card is given, the program uses the same core orbitals as the last CI calculation; if there was none, then the atomic inner shells are taken as core. To avoid this behaviour and correlate all electrons, specify

``CORE``

.. _the_mrci_program--closed-shell-orbitals:

Closed-shell orbitals
=====================

``CLOSED,$n_1,n_2,\ldots,n_8$``

:math:`n_i` is the number of closed-shell orbitals in irrep number :math:`i`, inclusive of any core orbitals. These orbitals do not form part of the active space, i.e., they are doubly occupied in all reference CSFs; however, in contrast to the core orbitals (see ``CORE``), these orbitals are correlated through single and double excitations. If not given, the information defaults to that from the most recent SCF, MCSCF or CI calculation. For calculations with closed-shell reference function (closed=occ), see ``CISD``, ``QCI``, and ``CCSD``.

.. _the_mrci_program--defining-the-orbitals:

Defining the orbitals
=====================

``ORBIT,name.file,[specifications];``

*name.file* specifies the record from which orbitals are read. Optionally, various *specifications* can be given to select specific orbitals if *name.file* contains more than one orbital set. For details see section `selecting orbitals and density matrices (ORBITAL, DENSITY) <general_program_structure.html#selecting-orbitals-and-density-matrices-orbital-density>`__. Note that the ``IGNORE_ERROR`` option can be used to force MPn or triples calculations with non-canonical orbitals.

The default is the set of orbitals from the last SCF, MCSCF or CI calculation.

.. _the_mrci_program--defining-the-state-symmetry:

Defining the state symmetry
===========================

The number of electrons and the total symmetry of the wavefunction are specified on the ``WF`` card:

``WF,elec,sym,spin``

where

* ***elec*:** is the number of electrons
* ***sym*:** is the number of the irreducible representation
* ***spin*:** defines the spin symmetry, *spin*\ :math:`=2S` (singlet=0, doublet=1, triplet=2, etc.)

The WF card must be placed after any cards defining the orbital spaces ``OCC``, ``CORE``, ``CLOSED``.

The ``REF`` card can be used to define further reference symmetries used for generating the configuration space, see ``REF``.

.. _the_mrci_program--additional-reference-symmetries:

Additional reference symmetries
===============================

``REF,sym;``

This card, which must come after the ``WF`` directive, defines an additional reference symmetry used for generating the uncontracted internal and singly external configuration spaces. This is sometimes useful in order to obtain the same configuration spaces when different point group symmetries are used. For instance, if a calculation is done in :math:`C_s` symmetry, it may happen that the two components of a :math:`\Pi` state, one of which appears in :math:`A'` and the other in :math:`A''`, come out not exactly degenerate. This problem can be avoided as in the following example:

for a doublet :math:`A'` state:

.. code-block:: text

   WF,15,1,1;      !define wavefunction symmetry (1)
   REF,2;          !define additional reference symmetry (2)

and for the doublet A” state:

.. code-block:: text

   WF,15,2,1;      !define wavefunction symmetry (2)
   REF,1;          !define additional reference symmetry (1)

For linear geometries the same results can be obtained more cheaply using :math:`C_{2v}` symmetry,

.. code-block:: text

   WF,15,2,1;      !define wavefunction symmetry (2)
   REF,1;          !define additional reference symmetry (1)
   REF,3;          !define additional reference symmetry (3)

or

.. code-block:: text

   WF,15,3,1;      !define wavefunction symmetry (2)
   REF,1;          !define additional reference symmetry (1)
   REF,2;          !define additional reference symmetry (2)

Each ``REF`` card may be followed by ``RESTRICT``, ``SELECT``, and ``CON`` cards, in the given order.

.. _the_mrci_program--selecting-configurations:

Selecting configurations
========================

``SELECT,ref1,ref2,refthr,refstat,mxshrf;``

This card is used to specify a reference configuration set other than a CAS, which is the default. Configurations can be defined using ``CON`` cards, which must appear after the *SELECT* card. Alternatively, if *ref1* is an existing Molpro record name, the configurations are read in from that record and may be selected according to a given threshold.

The select card must be placed directly after the *WF* or *REF* card(s), or, if present, the ``RESTRICT`` cards. The general order of these cards is

``WF`` (or ``REF``)
``RESTRICT (optional)\\``
``SELECT  (optional)\\``
``CON  (optional)\\``

* ***ref1=rec1.file*:** (*rec1:math:`>`2000*) The configurations are read in from the specified record. See section `saving the CI vectors and information for a gradient calculation <the_mcscf_program_multi.html#saving-the-ci-vectors-and-information-for-a-gradient-calculation>`__ about how to save the configurations in the MCSCF calculation. If *ref1* is not specified, the program assumes that the configurations are read from subsequent ``CON`` cards (see ``CON``).
* ***ref2=rec2.file*:** (*rec2:math:`>`2000*) additional configurations are read from the specified record. If *rec2* is negative, all records between *rec1* and abs(*rec2*) are read. All configurations found in this way are merged.
* ***refthr*:** Selection threshold for configurations read from disc (records *rec1–rec2*). This applies to the norm of all CSFs for each orbital configuration.
* ***refstat*:** Specifies from which state vector the configurations are selected. This only applies to the case that the configurations were saved in a state-averaged calculation. If *refstat* is zero or not specified, the configurations are selected from all states. If *refstat* is greater than zero, then the specified reference state is used. If *refstat* is less than zero, then all appropriate reference states are used. Lastly, if *refstat* is of the form *istat1.istat2*, states *istat1* through *istat2* are used.
* ***mxshrf*:** maximum number of open shells in the selected or generated configurations.

.. _the_mrci_program--occupation-restrictions:

Occupation restrictions
=======================

``RESTRICT,nmin,nmax,orb$_1$,orb$_2$,$\ldots$orb$_n$;``

This card can be used to restrict the occupation patterns in the reference configurations. Only configurations containing between *nmin* and *nmax* electrons in the specified orbitals *orb*\ :math:`_1`, *orb*\ :math:`_2`, :math:`\ldots`, *orb*\ :math:`_n` are included in the reference function. If *nmin* and *nmax* are negative, configurations with exactly abs(*nmin*) and abs(*nmax*) electrons in the specified orbitals are deleted. This can be used, for instance, to omit singly excited configurations. The orbitals are specified in the form *number.sym*, where *number* is the number of the orbital in irrep *sym*. Several ``RESTRICT`` cards may follow each other.

The ``RESTRICT`` cards must follow the ``WF`` or ``REF`` cards to which they apply. The general order of these cards is

``WF`` (or ``REF``)
``RESTRICT (optional)\\``
``SELECT  (optional)\\``
``CON  (optional)``

If a ``RESTRICT`` cards precedes the ``WF`` card, it applies to all reference symmetries. Note that ``RESTRICT`` also affects the spaces generated by ``SELECT`` and/or ``CON`` cards.

.. _the_mrci_program--explicitly-specifying-reference-configurations:

Explicitly specifying reference configurations
==============================================

``CON,$n_1,n_2,n_3,n_4,\ldots$``

Specifies an orbital configuration to be included in the reference function. :math:`n_1`, :math:`n_2` etc. are the occupation numbers of the active orbitals (0,1,or 2). Any number of ``CON`` cards may follow each other, but they must all appear directly after a ``SELECT`` card.

.. _the_mrci_program--defining-state-numbers:

Defining state numbers
======================

``STATE,nstate,nroot(1),nroot(2),...,nroot(nstate);``

*nstate* is the number of states treated simultaneously; *nroot(i)* are the root numbers to be calculated. These apply to the order of the states in the initial internal CI. If not specified, *nroot(i)*\ =\ :math:`i`. Note that it is possible to leave out states, i.e.,

.. code-block:: text

   STATE,1,2;    ! calculates second state
   STATE,2,1,3;  ! calculates first and third state

All states specified must be reasonably described by the internal configuration space. It is possible to have different convergence thresholds for each state (see ``ACCU`` card). It is also possible not to converge some lower roots which are included in the list *nroot(i)* (see ``REFSTATE`` card). For examples, see ``REFSTATE`` card.

.. _the_mrci_program--defining-reference-state-numbers:

Defining reference state numbers
================================

``REFSTATE,nstatr,nrootr(1),nrootr(2),...,nrootr(nstatr);``

*nstatr* is the number of reference states for generating contracted pairs. This may be larger or smaller than *nstate*. If this card is not present, *nstatr*\ =\ *nstate* and *nrootr(i)*\ =\ *nroot(i)*. Roots for which no reference states are specified but which are specified on the ``STATE`` card (or included by default if the *nroot(i)* are not specified explicitly on the ``STATE`` card) will not be converged, since the result will be bad anyway. However, it is often useful to include these states in the list *nroot(i)*, since it helps to avoid root flipping problems. Examples:

.. code-block:: text

   state,2;

will calculate two states with two reference states.

.. code-block:: text

   state,2;refstate,1,2;

will optimize second state with one reference state. One external expansion vector will be generated for the ground state in order to avoid root flipping. The results printed for state 1 are bad and should not be used (unless the pair space is complete, which might happen in very small calculations).

.. code-block:: text

   state,1,2;refstate,1,2;

As the second example, but no external expansion vectors will be generated for the ground state. This should give exactly the same energy for state 2 as before if there is no root flipping (which, however, frequently occurs).

.. code-block:: text

   state,2;accu,1,1,1;

Will calculate second state with two reference states. The ground state will not be converged (only one iteration is done for state 1) This should give exactly the same energy for state 2 as the first example.

.. _the_mrci_program--specifying-correlation-of-orbital-pairs:

Specifying correlation of orbital pairs
=======================================

``PAIR,iorb1.isy1,iorb2.isy2,np;``

is a request to correlate a given orbital pair.

* ***np=1*:** singlet pair
* ***np=-1*:** triplet pair
* ***np=0*:** singlet and triplet pair (if possible)

Default is to correlate all electron pairs in active and closed orbitals. See also ``PAIRS`` card.

``PAIRS,iorb1.isy,iorb2.isy,np;``

Correlate all pairs which can be formed from orbitals *iorb1.isy1* through *iorb2.isy2*. Core orbitals are excluded. Either *iorb2* must be larger than *iorb1* or *isy2* larger than *isy1*. If *iorb1.isy1*\ =\ *iorb2.isy2* the ``PAIRS`` card has the same effect as a ``PAIR`` card. ``PAIR`` and ``PAIRS`` cards may be combined.

If no ``PAIR`` and no ``PAIRS`` card is specified, all valence orbitals are correlated. The created pair list restricts not only the doubly external configurations, but also the all internal and semi internals.

.. _the_mrci_program--restriction-of-classes-of-excitations:

Restriction of classes of excitations
=====================================

``NOPAIR;``

No doubly external configurations are included.

``NOSINGLE;``

No singly external configurations are included.

``NOEXC;``

Perform CI with the reference configurations only.

.. _the_mrci_program--coupled-electron-pair-approximation:

Coupled Electron Pair Approximation
-----------------------------------

``CEPA(ncepa);``

(:math:`0 \le ncepa \le 3`). Instead of diagonalizing the hamiltonian, perform CEPA calculation, CEPA type *ncepa*. This is currently available only for single configuration reference functions.

.. _the_mrci_program--coupled-pair-functional-acpf-aqcc:

Coupled Pair Functional (ACPF, AQCC)
------------------------------------

``ACPF,options\\``
``AQCC,options``

where options can be

* **``GACPFI=``\ *gacpfi***
* **``GACPFE=``\ *gacpfe***

Instead of diagonalizing the hamiltonian, perform ACPF calculation or AQCC calculation. Using the options ``GACPFI`` and ``GAPCPE`` The internal and external normalization factors *gacpfi*, *gacpfe* may be reset from their default values of 1, 2/*nelec* and 1, 1-(*nelec*-2)(*nelec*-3)/*nelec*\ (*nelec*-1), respectively.

The ACPF and related methods are currently not robustly working for excited states. Even though it sometimes works, we do not currently recommend and support these methods for excited state calculations.

.. _the_mrci_program--projected-excited-state-calculations:

Projected excited state calculations
------------------------------------

``PROJECT,record,nprojc;``

Initiate or continue a projected excited state calculation, with information stored on *record*. If *nprojc*\ :math:`>0`, the internal CI vectors of *nprojc* previous calculations are used to make a projection operator. If *nprojc*\ :math:`=-1`, this calculation is forced to be the first, i.e. ground state, with no projection. If *nprojc*\ :math:`=0`, then if *record* does not exist, the effect is the same as *nprojc*\ :math:`=-1`; otherwise *nprojc* is recovered from the dump in *record*. Thus for the start up calculation, it is best to use ``project``,\ *record*,-1; for the following excited calculations, use ``project``,\ *record*; At the end of the calculation, the wavefunction is saved, and the information in the dump *record* updated. The project card also sets the ``tranh`` option, so by default, transition hamiltonian matrices are calculated.

For example, to do successive calculations for three states, use

.. code-block:: text

   ci;...;project,3000.3,-1;
   ci;...;project,3000.3;
   ci;...;project,3000.3;

At the end of each calculation, Hamiltonian is diagonalized over the whole set of projected functions, and the diagonal and transition properties are transformed accordingly. The untransformed properties, if required, can be retrieved from the output.

.. _the_mrci_program--transition-matrix-element-options:

Transition matrix element options
---------------------------------

``TRANH,option;``

If *option*\ :math:`>-1`, this forces calculation of transition hamiltonian matrix elements in a ``TRANS`` or ``PROJECT`` calculation. If *option*\ :math:`<1`, this forces calculation of one electron transition properties.

.. _the_mrci_program--convergence-thresholds:

Convergence thresholds
----------------------

``ACCU,istate,energy,coeff;``

Convergence thresholds for state *istate*. The actual thresholds for the energy and the CI coefficients are 10\ **(-*energy*) and 10**-(*coeff*). If this card is not present, the thresholds for all states are the default values or those specified on the ``THRESH`` card.

.. _the_mrci_program--denominator-shifts:

Denominator shifts
------------------

``SHIFT,shiftp,shifts,shifti;``

Denominator shifts for pairs, singles, and internals, respectively.

**Note: these are not level shifts in CASPT2**, but simple denominator shifts which affect the convergence of the iterative Davidson procedure.

.. _the_mrci_program--maximum-number-of-iterations:

Maximum number of iterations
----------------------------

``MAXITER,maxit,maxiti;``

* ***maxit*:** maximum number of macroiterations;
* ***maxiti*:** maximum number of microiterations (internal CI).

.. _the_mrci_program--restricting-numbers-of-expansion-vectors:

Restricting numbers of expansion vectors
----------------------------------------

``MAXDAV,maxdav,maxvi;``

* ***maxdav*:** maximum number of external expansion vectors in macroiterations;
* ***maxvi*:** maximum number of internal expansion vectors in internal CI.

.. _the_mrci_program--selecting-the-primary-configuration-set:

Selecting the primary configuration set
---------------------------------------

``PSPACE,select,npspac;``

* ***select*:** energy criterion for selecting p-space configurations. If negative, a test for p-space H is performed.
* ***npspac*:** minimum number of p-space configurations. Further configurations are added if either required by select or if configurations are found which are degenerate to the last p-space configuration. A minimum number of npspace is automatically determined from the state specifications.

.. _the_mrci_program--canonicalizing-external-orbitals:

Canonicalizing external orbitals
--------------------------------

``FOCK,$n_1,n_2,\ldots$;``

External orbitals are obtained as eigenfunctions of a Fock operator with the specified occupation numbers :math:`n_i`. Occupation numbers must be provided for all valence orbitals.

.. _the_mrci_program--saving-the-wavefunction:

Saving the wavefunction
-----------------------

``SAVE,savecp,saveco,idelcg;``

or

``SAVE [,CIVEC=savecp] [,CONFIG=saveco] [,DENSITY=dumprec] [,NATORB=dumprec] [,FILES] [,SPINDEN]``

* ***savecp*:** record name for save of wavefunction. If negative the wavefunction is saved after each iteration, else at the end of the job. In case of coupled cluster methods (CCSD, QCISD, BCCD), the wavefunction is saved in each iteration in any case.
* ***saveco*:** record name for save of internal configurations and their maximum weight over all states for subsequent use as reference input (see ``SELECT`` card). If the record already exists, the record name is incremented by one until a new record is created.
* ***idelcg*:** if nonzero or ``FILES`` is specified, don’t erase icfil and igfil (holding CI and residual vectors) at the end of the calculation.
* ***dumprec*:** Dump record for saving density matrix and natural orbitals. Only one dump record must be given. In any case the density matrix and the natural orbitals are saved. See also ``DM`` or ``NATORB`` cards.
* ``SPINDEN`` In the second form, if specified, spin-density is evaluated and stored. It is not done by default, due to additional required memory and CPU time.

.. _the_mrci_program--starting-wavefunction:

Starting wavefunction
---------------------

``START,readc1,irest;``

* ***readc1*:** record name from which the wavefunction is restored for a restart. In the case of coupled cluster methods (CCSD, QCISD, BCCD), the amplitudes are read from record *readc1* and used for restart.
* ***irest*:** If nonzero, the CI coefficients are read and used for the restart; otherwise, only the wavefunction definition is read in.

.. _the_mrci_program--one-electron-properties:

One electron properties
-----------------------

``EXPEC,oper$_1$,oper$_2$,oper$_3$,…;``

After the wavefunction determination, calculate expectation values for one-electron operators *oper:math:`_i`*. See section `One-electron operators and expectation values (GEXPEC) <program_control.html#one-electron-operators-and-expectation-values-gexpec>`__ for the available operators and their keywords. In multi-state calculations or in projected calculations, also the transition matrix elements are calculated.

.. _the_mrci_program--transition-moment-calculations:

Transition moment calculations
------------------------------

``TRANS,readc1,readc2,[BIORTH],[oper$_1$,oper$_2$,oper$_3$,…];``

Instead of performing an energy calculation, only calculate transition matrix elements between wavefunctions saved on records *readc1* and *readc2*. See section `One-electron operators and expectation values (GEXPEC) <program_control.html#one-electron-operators-and-expectation-values-gexpec>`__ for a list of available operators and their corresponding keywords. If no operator names are specified, the dipole transition moments are calculated.

If option ``BIORTH`` is given, the two wavefunctions may use different orbitals. However, the number of active and inactive orbitals must be the same in each case. Note that ``BIORTH`` is not working for spin-orbit matrix elements. Under certain conditions it may happen that biorthogonalization is not possible, and then an error message will be printed. For transition properties which have nonzero nuclear contribution, the corresponding geometry is then that of the ket state (*readc2*). The same is valid when origin of operator is explicitly specified as a center number, i.e. its coordinates will be those for the ket state.

.. _the_mrci_program--saving-the-density-matrix:

Saving the density matrix
-------------------------

``DM,record.ifil,[idip];``

The first order density matrices for all computed states are stored in record *record* on file *ifil*. If *idip* is not zero, the dipole moments are printed starting at iteration *idip*. See also ``NATORB``. In case of transition moment calculation, the transition densities are also stored, provided both states involved have the same symmetry.

.. _the_mrci_program--natural-orbitals:

Natural orbitals
----------------

``NATORB,[RECORD=]record.ifil,[PRINT=nprint],[CORE[=natcor]];``

Calculate natural orbitals. The number of printed external orbitals in any given symmetry is *nprint*) (default 2). *nprint=-1* suppressed the printing. If *record* is nonzero, the natural orbitals and density matrices for all states are saved in a dump record *record* on file *ifil*. If *record.ifil* is specified on a ``DM`` card (see above), this record is used. If different records are specified on the ``DM`` and ``NATORB`` cards, an error will result. The record can also be given on the ``SAVE`` card. If ``CORE`` is specified, core orbitals are not printed.

Note: The dump record must not be the same as *savecp* or *saveco* on the ``SAVE`` card, or the record given on the ``PROJECT``.

.. _the_mrci_program--miscellaneous-options:

Miscellaneous options
---------------------

``OPTION,code1=value,code2=value,$\ldots$``

Can be used to specify program parameters and options. If no codes and values are specified, active values are displayed. The equal signs may be omitted. The following codes are allowed (max 7 per card):

* ``NSTATE:`` see ``state`` card
* ``NSTATI:`` number of states calculated in internal CI
* ``NSTATR:`` see ``refstat`` card
* ``NCEPA:`` see ``CEPA`` card
* ``NOKOP:`` if nonzero, skip integral transformation
* ``ITRDM:`` if .ge. 0 transition moments are calculated
* ``ITRANS:`` if nonzero, perform full integral transformation (not yet implemented)
* ``IDIP:`` Print dipole moments from iteration number *value*
* ``REFOPT:`` if nonzero, optimize reference coefficients; otherwise extract reference coefficients from internal CI
* ``IAVDEN:`` average HII and HSS denominators over spin couplings if nonzero
* ``IDELCG:`` if.ne.0 then destroy files icfil,igfil at end
* ``IREST:`` if nonzero, restart
* ``NATORB:`` if nonzero, natural orbitals are calculated and printed. The number of printed external orbitals per symmetry is min(*natorb*,2)
* ``WFNAT:`` if nonzero, natural orbitals are saved to this record
* ``IPUNRF:`` if nonzero, punch coefficients of reference configurations
* ``NPUPD:`` if nonzero, update pairs in nonorthogonal basis, otherwise in orthogonal basis.
* ``MAXIT:`` see ``maxiter`` card
* ``MAXITI:`` see ``maxiter`` card
* ``MAXDAV:`` see ``maxdav`` card
* ``MAXVI:`` see ``maxdav`` card
* ``NOSING:`` see ``nosing`` card
* ``NOPAIR:`` see ``nopair`` card
* ``MXSHRF:`` see ``select`` card
* ``IKCPS=0:`` In CIKEXT, only K(CP) is calculated; this option taken when and only when no singles.
* ``IKCPS=1:`` only K(CP’) is calculated. Implies that modified coupling coefficients are used.
* ``IKCPS=2:`` K(CP) and K(CP’) are calculated. Default is IKCPS=2 except when single reference configuration, when IKCPS=1.
* ``IOPTGM:`` Option for density matrix routines.
* ``IOPTGM=0:`` all quantities in density matrix routines are recalculated for each intermediate symmetry (max. CPU, min. core).
* ``IOPTGM=1:`` quantities precalculated and stored on disk (max. I/O, min. core).
* ``IOPTGM=2:`` quantities precalculated and kept in core (min. CPU, max. core).
* ``IOPTOR:`` If nonzero, calculate intermediate orbitals for each pair. Might improve convergence in some cases, in particular if localized orbitals are used.

.. _the_mrci_program--miscellaneous-parameters:

Miscellaneous parameters
------------------------

``PARAM,code1=value,code2=value$\ldots$``

Redefine system parameters. If no codes are specified, the default values are displayed. The following codes are allowed:

* ``LSEG:`` disc sector length
* ``INTREL:`` number of integers per REAL\*8 word
* ``IVECT=0:`` scalar machine
* ``IVECT=1:`` vector machine
* ``MINVEC:`` call MXMB in coupling coefficient routines if vector length larger than this value.
* ``IBANK:`` number of memory banks for vector machines. If IBANK\ :math:`>`\ 1, vector strides which are multiples of IBANK are avoided where appropriate.
* ``LTRACK:`` number of REAL\*8 words per track or block (for file allocation)
* ``LTR:`` determines how matrices are stored on disc. If LTR=LSEG, all matrices start at sector boundaries (which optimizes I/O), but unused space is between matrices (both on disc and in core). With LTR=1 all matrices are stored dense. This might increase I/O if much paging is necessary, but reduce I/O if everything fits in core.
* ``NCPUS:`` Maximum number of CPUs to be used in multitasking.

.. _the_mrci_program--miscellaneous-thresholds:

Miscellaneous thresholds
------------------------

``THRESH,code1=value,code2=value$\ldots$``

If *value*\ =0, the corresponding threshold is set to zero, otherwise 10\*\*(-*value*). The equal signs may be omitted. If no codes are specified, the default values are printed. The following codes are allowed (max 7 per card):

* ``ZERO:`` numerical zero
* ``THRDLP:`` delete pairs if eigenvalue of overlap matrix is smaller than this threshold.
* ``PNORM:`` delete pair if its norm is smaller than this threshold (all pairs are normalized to one for a closed shell case).
* ``PRINTCI:`` print CI coefficients which are larger than this value.
* ``INTEG:`` omit two-electron integrals which are smaller than this value.
* ``ENERGY:`` convergence threshold for energy; see also: ``ACCU`` card.
* ``COEFF:`` convergence threshold for coefficients; see also: ``ACCU`` card.
* ``SPARSE:`` omit coefficient changes which are smaller than this value.
* ``EQUAL:`` set values in the internal vector and the diagonal elements equal if they differ by less than this value. Useful for keeping track of symmetry.

.. _the_mrci_program--print-options:

Print options
-------------

``PRINT,code1=value,code2=value,$\ldots$``

Print options. Generally, the value determines how much intermediate information is printed. *value*\ =-1 means no print (default for all codes). In some of the cases listed below the specification of higher values will generate even more output than described. The equal signs and zeros may be omitted. All codes may be truncated to three characters. The following codes are allowed (max 7 per card):

* ``ORBITALS:`` print orbitals
* ``JOP=0:`` print operator list
* ``JOP=1:`` print coulomb operators in MO basis
* ``JOP=2:`` print coulomb operators in AO and MO basis
* ``KOP:`` as ``JOP`` for internal exchange operators
* ``KCP=0:`` print paging information for CIKEXT
* ``KCP=1:`` print external exchange operators in MO basis
* ``KCP=2:`` print operators in AO and MO basis
* ``DM=0:`` print paging information for CIDIMA
* ``DM=1:`` print density matrix in MO basis
* ``DM=2:`` print density matrix in AO and MO basis
* ``FPP=0:`` print energy denominators for pairs
* ``FPP=1:`` in addition, print diagonal coupling coefficients in orthogonal basis.
* ``FPP=2:`` print operators FPP
* ``CP=0:`` print update information for pairs in each iteration
* ``CP=1:`` print pair matrix updates (MO basis)
* ``CP=2:`` in addition print pair matrices (MO basis)
* ``CP=3:`` print CP in AO basis (in CIKEXT)
* ``CI=0:`` print convergence information for internal CI
* ``CI=1:`` print internal CI coefficients and external expansion coefficients
* ``CS:`` as CP for singles
* ``CPS=0:`` print paging information for CICPS
* ``CPS=1:`` print matrices CPS in MO basis
* ``GPP=0:`` print paging information for CIGPQ
* ``GPP=1:`` print matrices GP at exit of CIGPQ
* ``GPS=0:`` print paging information for CIGPS
* ``GPS=1:`` print vectors GS at exit CIGPS
* ``GSP=1:`` print matrices GP at exit CIGPS
* ``GPI=0:`` print paging information for CIGPI
* ``GPI=1:`` print total GP in orthogonal basis
* ``GPI=2:`` print matrices GP and TP
* ``GIP=0:`` print paging information for CIGIP
* ``GIP=1:`` print GI at exit CIGIP
* ``GSS=0:`` print paging information for CIGSS
* ``GSS=1:`` print vectors GS at exit CIGSS
* ``GSI=0:`` print paging information for CIGSI
* ``GSI=1:`` print GS at exit CIGSI
* ``GIS=0:`` print paging information for CIGIS
* ``GIS=1:`` print GI at exit CIGIS
* ``GII:`` print intermediate information in internal CI
* ``DPQ:`` print coupling coefficients :math:`\alpha(P,Q)`
* ``EPQ:`` print coupling coefficients :math:`\beta(P,Q)`
* ``HPQ:`` print coupling coefficients :math:`\gamma(P,Q)`
* ``DPI:`` print coupling coefficients for pair-internal interactions
* ``DSS:`` not yet used
* ``DSI:`` not yet used
* ``LOG:`` At end of each iteration, write summary to log file. Delete at end of job if ``LOG=0``
* ``CC=0:`` print address lists for coupling coefficients
* ``CC=1:`` print coupling coefficients
* ``DEN=1:`` print internal first order density
* ``DEN=2:`` print internal second order density
* ``DEN=3:`` print internal third order density
* ``DEN=4:`` print first, second and third order densities
* ``GAM=1:`` print first order transition densities
* ``GAM=2:`` print second order transition densities
* ``GAM=3:`` print first and second order transition densities
* ``PAIRS=0:`` print list of non redundant pairs
* ``PAIRS=1:`` print list of all pairs
* ``CORE=0:`` print summary of internal configurations (:math:`N, N-1` and :math:`N-2` electron)
* ``CORE=1:`` print internal configurations (:math:`N, N-1, N-2`)
* ``REF=0:`` print summary of reference configurations
* ``REF=1:`` print reference configurations and their coefficients
* ``PSPACE:`` print p-space configurations
* ``HII:`` print diagonal elements for internals
* ``HSS:`` print diagonal elements for singles
* ``SPQ:`` various levels of intermediate information in pair orthogonalization routine.
* ``TEST=0:`` print information at each subroutine call
* ``TEST=1:`` print in addition information about I/O in LESW, SREIBW
* ``TEST=2:`` print also information about I/O in FREAD, FWRITE
* ``CPU:`` print analysis of CPU and I/O times
* ``ALL:`` print everything at given level (be careful!)

.. _the_mrci_program--examples:

Examples
--------

.. code-block:: text
   :caption: examples/h2o_cepa1.inp

   ***,Single reference CISD and CEPA-1 for water
   r=0.957,angstrom
   theta=104.6,degree;
   geometry={O;              !z-matrix geometry input
             H1,O,r;
             H2,O,r,H1,theta}
   {hf;wf,10,1;}                         !TOTAL SCF ENERGY     -76.02680642
   {ci;occ,3,1,1;core,1;wf,10,1;}        !TOTAL CI(SD) ENERGY  -76.22994348
   {cepa(1);occ,3,1,1;core,1;wf,10,1;}   !TOTAL CEPA(1) ENERGY -76.23799334

.. code-block:: text
   :caption: examples/h2op_mrci_trans.inp

   ***,Valence multireference CI for X and A states of H2O
   gthresh,energy=1.d-8
   r=0.957,angstrom,theta=104.6,degree;
   geometry={O;              !z-matrix geometry input
             H1,O,r;
             H2,O,r,H1,theta}
   {hf;wf,10,1;}         !TOTAL SCF ENERGY               -76.02680642
   {multi;occ,4,1,2;closed,2;frozen,1;wf,9,2,1;wf,9,1,1;tran,ly}
                        !MCSCF ENERGY                   -75.66755631
                        !MCSCF ENERGY                   -75.56605896
   {ci;occ,4,1,2;closed,2;core,1;wf,9,2,1;save,7300.1}
                        !TOTAL MRCI ENERGY              -75.79831209
   {ci;occ,4,1,2;closed,2;core,1;wf,9,1,1;save,7100.1}
                        !TOTAL MRCI ENERGY              -75.71309879
   {ci;trans,7300.1,7100.1,ly}
                        !Transition moment <1.3|X|1.1> = -0.14659810  a.u.
                        !Transition moment <1.3|LY|1.1> = 0.96200488i a.u.

.. code-block:: text
   :caption: examples/bh_mrci_sigma_delta.inp

   ***,BH singlet Sigma and Delta states
   r=2.1
   geometry={b;h,b,r}
   {hf;occ,3;wf,6,1;}
   {multi;
   occ,3,1,1;frozen,1;wf,6,1;state,3;lquant,0,2,0;wf,6,4;lquant,2;
   tran,lz;
   expec2,lzlz;}
   ! Sigma states:- energies -25.20509620 -24.94085861
   {ci;occ,3,1,1;core,1;wf,6,1;state,2,1,3;}
   ! Delta states:- energies -24.98625171
   {ci;occ,3,1,1;core,1;wf,6,1;state,1,2;}
   ! Delta state:- xy component
   {ci;occ,3,1,1;core,1;wf,6,4;}

.. _the_mrci_program--cluster-corrections-for-multi-state-mrci:

Cluster corrections for multi-state MRCI
----------------------------------------

In the following, we assume that

.. math::

   \begin{align}
   \Psi_{\rm ref}^{(n)} &=& \sum_R C_{Rn}^{(0)} \Phi_R \\
   \Psi_{\rm mrci}^{(n)} &=& \sum_R C_{Rn} \Phi_R + \Psi_c\end{align}

are the normalized reference and MRCI wave functions for state :math:`n`, respectively. :math:`C_R^{(0)}` are the coefficients of the reference configurations in the initial reference functions and :math:`C_{Rn}` are the relaxed coefficients of these configurations in the final MRCI wave function. :math:`\Psi_c` is the remainder of the MRCI wave function, which is orthogonal to all reference configurations :math:`\Phi_R`.

The corresponding energies are defined as

.. math::

   \begin{align}
   E_{\rm ref}^{(n)} &=& \langle \Psi_{\rm ref}^{(n)} | \hat H | \Psi_{\rm ref}^{(n)}\rangle,\\
   E_{\rm mrci}^{(n)}&=& \langle \Psi_{\rm mrci}^{(n)} | \hat H | \Psi_{\rm mrci}^{(n)}\rangle.\end{align}

The standard Davidson corrected correlation energies are defined as
\begin{align}

.. code-block:: text

    E^{n}_{\rm D} &=& E_{\rm corr}^{(n)}\cdot \frac {1-c_n^2}{ c_n^2 } \label{eq:dav}\end{align}

where :math:`c_n` is the coefficient of the (fixed) reference function in the MRCI wave function:
\begin{align}

.. code-block:: text

     c_n = \langle \Psi_{\rm ref}^{(n)}|\Psi_{\rm mrci}^{(n)} \rangle = \sum_R C_{Rn}^{(0)} C_{Rn}, \label{eq:cfix}\end{align}

and the correlation energies are
\begin{align}
E_{\rm corr}^{(n)}=E_{\rm mrci}^{(n)}-E_{\rm ref}^{(n)} .\label{eq:ecorr}\end{align}
In the vicinity of avoided crossings this correction may give unreasonable results since the reference function may get a small overlap with the MRCI wave function. One way to avoid this problem is to replace the reference wave function :math:`\Psi_{\rm ref}^{(n)}` by the the relaxed reference functions

.. math::

   \begin{align}
   \Psi_{\rm rlx}^{(n)} &=& \frac{\sum_R C_{Rn} \Phi_R}{\sqrt{\sum_R C_{Rn}^2}},\end{align}

which simply leads to
\begin{align}

.. code-block:: text

     c_n^2 &=& \sum_R C_{Rn}^2.  \label{eq:crlx}

\end{align}
Alternatively, one can linearly combine the fixed reference functions to maximize the overlap with the MRCI wave functions. This yields projected functions

.. math::

   \begin{align}
        \Psi_{\rm prj}^{(n)} &=& \sum_m |\Psi_{\rm ref}^{(m)}\rangle\langle \Psi_{\rm ref}^{(m)} |\Psi_{\rm mrci}^{(n)} \rangle
         =  \sum_m |\Psi_{\rm ref}^{(m)}\rangle d_{mn}\end{align}

with

.. math::

   \begin{align}
         d_{mn} &=&  \langle \Psi_{\rm ref}^{(m)}|\Psi_{\rm mrci}^{(n)} \rangle = \sum_R C_{Rm}^{(0)} C_{Rn}.\end{align}

These projected functions are not orthonormal. The overlap is

.. math::

   \begin{align}
     \langle  \Psi_{\rm prj}^{(m)} |  \Psi_{\rm prj}^{(n)} \rangle &=& ({\bf d}^{\dagger} {\bf d})_{mn}.\end{align}

Symmetrical orthonormalization, which changes the functions as little as possible, yields

.. math::

   \begin{align}
        \Psi_{\rm rot}^{(n)} &=& \sum_m |\Psi_{\rm ref}^{(m)}\rangle u_{mn}, \\
         {\bf u} &=& {\bf d} ({\bf d}^{\dagger} {\bf d})^{-1/2}.\end{align}

The overlap of these functions with the MRCI wave functions is

.. math::

   \begin{align}
      \langle  \Psi_{\rm rot}^{(m)} | \Psi_{\rm mrci}^{(n)} \rangle &=&  [({\bf d}^{\dagger} {\bf d}) ({\bf d}^{\dagger} {\bf d})^{-1/2}]_{mn}
      = [({\bf d}^{\dagger} {\bf d})^{1/2}]_{mn}.\end{align}

Thus, in this case we use for the Davidson correction
\begin{align}

.. code-block:: text

         c_n &=& [({\bf d}^{\dagger} {\bf d})^{1/2}]_{nn}. \label{eq:crot}

\end{align}
The final question is which reference energy to use to compute the correlation energy used in eq. \eqref{eq:dav}. In older MOLPRO version (to 2009.1) the reference wave function which has the largest overlap with the MRCI wave function was used to compute the reference energy for the corresponding state. But this can lead to steps of the Davidson corrected energies if the order of the states swaps along potential energy functions. In this version there are two options: the default is to use for state :math:`n` the reference energy :math:`n`, cf. eq. \eqref{eq:ecorr} (assuming the states are ordered according to increasing energy). The second option is to recompute the correlation energies using the rotated reference functions
\begin{align}
E_{corr}^{(n)} &=& E_{\rm MRCI}^{(n)} - \langle \Psi_{\rm rot}^{(n)} \| \hat H \|  \Psi_{\rm rot}^{(n)} \rangle  \label{eq:erot}\end{align}
Both should give smooth potentials (unless at conical intersections or crossings of states with different symmetries), but there is no guarantee that the Davidson corrected energies of different states don’t cross. This problem is unavoidable for non-variational energies. The relaxed and rotated Davidson corrections give rather similar results; the rotated one yields somewhat larger cluster corrections and was found to give better results in the case of the F + H\ :math:`_2` potential [see `J. Chem. Phys. <https://dx.doi.org/10.1063/1.2822905>`__ **128**, 034305 (2008)].

By default, the different cluster corrections listed in the following table are computed in multi-state MRCI calculations. and stored in variables.

.. list-table::
   :header-rows: 2

   * - Cluster corrections computed in multi-state MRCI calculations
     - 
     - 
     - 
     - 
     - 
   * - Name
     - :math:`c_n` (Eq.)
     - $E_{corr}
     - {(n)}$ (Eq.)
     - Variable
     - 
   * - *Using standard reference energies:*
     - 
     - 
     - 
     - 
     - 
   * - Fixed
     - \eqref{eq:cfix}
     - \eqref{eq:ecorr}
     - ``ENERGD1(n)``
     - 
     - 
   * - Relaxed
     - \eqref{eq:crlx}
     - \eqref{eq:ecorr}
     - ``ENERGD0(n)``
     - 
     - 
   * - Rotated
     - \eqref{eq:crot}
     - \eqref{eq:ecorr}
     - ``ENERGD2(n)``
     - 
     - 
   * - *Using rotated reference energies:*
     - 
     - 
     - 
     - 
     - 
   * - Relaxed
     - \eqref{eq:crlx}
     - \eqref{eq:erot}
     - ``ENERGD3(n)``
     - 
     - 
   * - Rotated
     - \eqref{eq:crot}
     - \eqref{eq:erot}
     - ``ENERGD4(n)``
     - 
     - 

By default, the energies are in increasing order of the MRCI total energy. In single-state calculations only the fixed and relaxed values are available.

By default, ``ENERGD(n)=ENERGD0(n)``. This can be changed by setting ``OPTION,CLUSTER=``\ *x*; then ``ENERGD(n)=ENERGDx(n)`` (default :math:`x=0`). The behaviour of Molpro 2009.1 and older can be retrieved using

``MRCI,SWAP,ROTREF=-1.``

.. _the_mrci_program--explicitly-correlated-mrci-f12:

Explicitly correlated MRCI-F12
------------------------------

The only change needed for including explicitly correlated terms is to append ``-F12`` to the ``MRCI`` command. All other options work as described before. It is recommended to use correlation consistent basis sets (aug-cc-pVnZ or VnZ-F12) since for these the appropriate fitting and RI auxiliary basis sets are chosen automatically. Otherwise it max be necessary to specify these basis sets as described for single-reference methods in section :doc:`explicitly correlated methods <explicitly_correlated_methods>`.

The following options (to be given on the ``MRCI-F12`` command line) are specific to MRCI-F12:

* **``SCALF12``\ =\ *scalf12*** If ``scalf12=1`` (default) the explicitly correlated contributions are treated variationally (``SFIX`` ansatz, see `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3528720>`__ **134**, 034113 (2011). If ``scalf12=0`` intermediate normalization is used (``FIX`` ansatz).
* **``CABS_SINGLES``\ =\ *isingles*** ``isingles=1``: use singles-CI CABS singles correction (default); ``isingles=2``: use perturbational CABS singles correction; ``isingles=3``: include couplings of CABS singles with MRCI terms.

For a description of the various singles corrections see `Mol. Phys. <https://dx.doi.org/10.1080/00268976.2013.779393>`__ **111**, 607 (2013). [sec:rs23]
