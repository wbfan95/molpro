.. _internally_contracted_multireference_coupled-cluster_theory--multireference-cc-computations:

Multireference CC computations
==============================

Internally contracted multireference internally contracted coupled-cluster theory

Bibliography:

M. Hanauer, A. Köhn, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3592786>`__ **134**, 204111 (2011).
A. Köhn, J. A. Black, Y. A. Aoto, M. Hanauer, `Mol. Phys. <https://dx.doi.org/10.1080/00268976.2020.1743889>`__ **118**, e1743889 (2020).
A. Waigum, J. A. Black, A. Köhn, `J. Chem. Phys. <https://dx.doi.org/10.1063/5.0067511>`__ **155**, 204106 (2021).

New ITF-based code in Molpro:

J. A. Black, A. Waigum, R.G. Adam, K.R. Shamasundar, A. Köhn, `J. Chem. Phys. <https://dx.doi.org/10.1063/5.0143214>`__ 158, 134801 (2023)

All publications resulting from use of the corresponding methods must acknowledge the above.

The command ``CMRCC`` calls the new Molpro implementation, currently restricted to CAS(2,2).
The command ``CMRCC,GECCO`` calls the external program GeCCo.
The command ``DF-CMRCC,GECCO`` calls the external program GeCCo and uses density fitting for the integral transformation.

The following options may be specified on the command line (all implementations):

* **``MAXIT=``\ *value*** Maximum number of iterations.
* **``SV_THRESH=``\ *value*** Singular value decomposition threshold (default 1E-7)

Command line options for new implementation:

* **``MAX_EN=``\ *value*** Highest order commutator included in the energy equations (default: 4)
* **``MAX_RES=``\ *value*** Highest order commutator included in the amplitude equations (default: 2)
* **``SELECT=``\ *value*** Confine cubic and quartic commutator terms in amplitude equations to those from single reference CC (default: True)
* **``RELAX=``\ *value*** Switch on reference relaxation (default: True)
* **``MAXDIIS=``\ *value*** Maximum number of vectors for DIIS extrapolation (default: 6)
* **``SHIFTI=``\ *value*** Denominator shift for update of internal configurations.
* **``SHIFTS=``\ *value*** Denominator shift for update of singles.
* **``SHIFTP=``\ *value*** Denominator shift for update of doubles.

Command line options for old implementation:

* ``GECCO`` Required: switch for calling the external GeCCo program (see below for setup)
* ``DUMP`` Do not execute the GeCCo program but dump interface files
* ``FCIDUMP`` Dump interface files in FCIDUMP format
* **``FILE=``\ *filename(s)*** Filename or colon-separated list of filenames with inputs for the external GeCCo program

Orbital spaces: The usual directives of Molpro for defining the orbital spaces (``CORE``, ``CLOSED``, ``OCC``)  and the symmetry and spin of the reference wavefunction (``WF``) can be used. By default the definition from any previous command applies.
Only CAS references are supported.

.. _internally_contracted_multireference_coupled-cluster_theory--introduction:

Introduction
============

Internally contracted multireference coupled-cluster (icMRCC) theory is designed as a straight-forward generalisation of coupled-cluster theory to multiconfigurational references. It also provides access to strictly spin-adapted coupled-cluster energies for any open-shell case. As a downside, the approach comes with significant computational overhead as compared to standard coupled-cluster theory and potentially more problems concerning convergence of the equations. The full approach is currently only available as a pilot implementation using the GeCCo program (see below), a more efficient version is currently restricted to doublet and CAS(2,2) singlet and triplet wavefunctions.

.. _internally_contracted_multireference_coupled-cluster_theory--the-external-gecco-program:

The external GeCCo program
==========================

The option ``GECCO`` calls the external GeCCo program:

.. code-block:: text

   {cmrcc,gecco}

The GeCCo binary must be referenced by the environment variable ``$GECCO_BIN``; the environment variable ``$GECCO_DIR`` must also be set and point to a path consistent with ``$GECCO_BIN``. The GeCCo program can be downloaded from `GitHub <https://github.com/ak-ustutt/GeCCo-public>`__, see there for further documentation.

The ``FILE`` option allows to start arbitrary GeCCo input from Molpro (input file should be located in starting directory of the Molpro computation.
Apart from multireference coupled-cluster theory, GeCCo also provides a reasonably fast arbitrary-order single-reference coupled-cluster code (closed-shell systems only). Explicitly correlated calculations can currently not be directly started from Molpro.

The :doc:`Region <region>` command can be used to enable icMRCC computations for large molecules, when only a fraction of it (for instance the transition metal center and the coordinating orbitals) shall be correlated at this level (virtual space truncation can be used in this case). The approach should be combined with density fitting to cope with the integral transformation (see :doc:`Region <region>` for details).

.. _internally_contracted_multireference_coupled-cluster_theory--the-new-implementation:

The new implementation
======================

The new implementation is based on the ITF framework. It is simply envoked by

.. code-block:: text

   {cmrcc}

which runs the code with the default settings. The singular value threshold is normally not decisive for CAS(2,2) runs. We recommend to keep the ``relax`` option switched on (but it makes only a difference for CAS(2,2) singlets at present, for triplets there is only one reference CSF).

In addition, two simplified versions based on CEPA(0) or a hybrid of MRCC/CEPA(0) are available:

.. code-block:: text

   {cmrcc,method=MRCEPA0}
   {cmrcc,method=MRCCSD-CEPA}

.. _internally_contracted_multireference_coupled-cluster_theory--examples:

Examples
========

Singlet and triplet state of methylene (new code)

.. code-block:: text

   memory,250,m
   gprint,orbitals,civector
   
   basis=cc-pVDZ
   
   r=1.1 angs,theta=115
   geometry={c;h1,c,r;h2,c,r,h1,theta}
   
   {multi;occ,3,1,1,0;closed,2,0,1,0;wf,sym=2,spin=2}  !MCSCF STATE 1.2 Energy  -38.917652
   {cmrcc,max_en=4,max_res=2}                          !Total energy:           -39.035139
   
   {multi;occ,3,1,1,0;closed,2,0,1,0;wf,sym=1,spin=0}  !MCSCF STATE 1.1 Energy  -38.898293
   {cmrcc,relax=F,max_en=4,max_res=2}                  !Total energy:           -39.016538
   {cmrcc,max_en=4,max_res=2}                          !Total energy:           -39.016562

Ground state energy of carbon dimer, compare MRCI and MRCC

.. code-block:: text

   memory,500,m
   gprint,orbital
   
   rr = 1.1 ang
   geometry={c;c,1,rr}
   
   basis=cc-pVDZ
   
   {multi;
    occ,   3,1,1,0,3,1,1,0;
    closed,1,0,0,0,1,0,0,0;
    wf,,1,0;state,3;lquant,0,0,2  ! make sure to get the true lowest state
   }
   
   {ci}              !MRCI STATE 1.1 Energy               -75.667843
                     !Cluster corrected energies          -75.672973 (Davidson, relaxed reference)
                     !Cluster corrected energies          -75.671780 (Pople, relaxed reference)
   {cmrcc,gecco}     !icMRCCSD STATE 1.1 Energy           -75.671237
