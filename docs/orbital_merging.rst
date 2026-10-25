.. raw:: html

   <span id="adding-or-replacing-orbitals-in-the-output-set-add-replace"></span>

.. raw:: html

   <span id="defining-extra-symmetries-extra"></span>

.. raw:: html

   <span id="defining-offsets-in-the-output-set-offset"></span>

.. raw:: html

   <span id="defining-the-input-orbitals-orbital"></span>

.. raw:: html

   <span id="initialization-of-a-new-output-set-init"></span>

.. raw:: html

   <span id="moving-orbitals-to-the-output-set-move"></span>

.. raw:: html

   <span id="printing-options-print"></span>

.. raw:: html

   <span id="projecting-orbitals-project"></span>

.. raw:: html

   <span id="rotating-orbitals-rotate"></span>

.. raw:: html

   <span id="saving-the-merged-orbitals"></span>

.. raw:: html

   <span id="schmidt-orthonormalization-schmidt"></span>

.. raw:: html

   <span id="symmetric-orthonormalization-orth"></span>

.. _orbital_merging--orbital-merging:

Orbital merging
===============

Orbitals can be manipulated using the ``MERGE`` facility. For instance, this allows the construction of molecular orbitals from atomic orbitals, to merge and orthogonalize different orbital sets, or to perform :math:`2 \times 2` rotations between individual orbitals. Other orbital manipulations can be performed using the ``LOCALI`` program (see section :doc:`orbital localization <orbital_localization>`) or the ``MATROP`` program (section :doc:`matrix operations <matrix_operations>`).

The merge program is called using

``MERGE [,namout.file]``

All subcommands described in the following sections may be abbreviated by three characters. *namout.file* specifies the output data set (see also ``SAVE`` command). If *namout.file* is omitted and no ``SAVE`` card is present, the new orbitals are not saved. All output orbitals must be supplied via ``ORBITAL`` and ``ADD``, ``MOVE``, ``REPLACE``, ``EXTRA``, or ``PROJECT`` directives before they can be saved.

.. _orbital_merging--defining-the-input-orbitals-orbital:

Defining the input orbitals (ORBITAL)
=====================================

``ORBITAL,namin.file,specifications``

Reads an input orbital set from a dump record. *specifications* can be used to select specific orbital sets, as described in section `selecting orbitals and density matrices (ORBITAL, DENSITY) <general_program_structure.html#selecting-orbitals-and-density-matrices-orbital-density>`__. Subsets of these orbitals can be added to the output set by the ``ADD``, ``MOVE``, or ``EXTRA`` commands.

.. _orbital_merging--moving-orbitals-to-the-output-set-move:

Moving orbitals to the output set (MOVE)
========================================

``MOVE,orb1.sym1,orb2.sym2,orb3.sym3,ioff,fac,istart,iend``

Moves orbitals *orb1.sym1* to *orb2.sym2* from the input set to the first vector of symmetry *sym3* in the output set which is undefined so far. The first *orb3-1* vectors in the output set are skipped regardless of whether they have been defined before or not. If *sym2 :math:`>` sym1*, *sym3* will run from *sym1* to *sym2* and the input for *sym3* has no effect. If *orb1.sym1* is negative, abs(*orb1*) is the maximum number of orbitals to be moved, starting with orbital *1.sym1*, up to *orb2.sym2*. If *orb2.sym2* is negative, abs(*orb2*) is the maximum number of vectors to be moved, starting at *orb1.isym1* up to the last orbital in symmetry *sym2*.

Orbitals from the input set which have already been moved or added to the output set are generally skipped. If *orb1* and *orb2* are zero, the whole input set is moved to the output set. In this case the input and output dimensions must be identical. If *orb1* is nonzero but *orb2* is zero, *orb2* is set to the last orbital in symmetry *sym2*. If *sym2=0*, *sym2* is set to *sym1*. *ioff* is an offset in the output vector, relative to the global offset set by ``OFFSET`` directive. *fac* has no effect for move. The elements  *istart* to *iend* of the input vector are moved. If *istart=0* and *iend=0*, the whole input vector is moved.

The usage of the ``MOVE`` directive is most easily understood by looking at the examples given below. See also ``ADD`` and ``EXTRA`` commands.

.. _orbital_merging--adding-or-replacing-orbitals-in-the-output-set-add-replace:

Adding or replacing orbitals in the output set (ADD,REPLACE)
============================================================

``ADD,orb1.sym1,orb2.sym2,orb3.sym3,ioff,fac,istart,iend``

This adds orbitals *orb1.sym1* to *orb2.sym2* to the output vectors, starting at *orb3.sym3*. The input vectors are scaled by the factor *fac*. If *fac=0*, *fac* is set to 1.0. For other details see ``MOVE`` command. Note, however, that the output vectors which have already been defined are not skipped as for ``MOVE``.

``REPLACE,orb1.sym1,orb2.sym2,orb3.sym3,ioff,,iustart,iend Replaces orbitals in the outputs set. If the output orbitals already exists, they are set to zero and then replaced by the given input orbitals. Otherwise as ADD.``

See also ``MOVE`` and ``EXTRA`` commands.

.. _orbital_merging--defining-extra-symmetries-extra:

Defining extra symmetries (EXTRA)
=================================

``EXTRA,exsym,orb1.sym1,orb2.sym2,orb3.sym3,ioff,fac,istart,iend``

Works exactly as ``MOVE``, but only input vectors with extra symmetry *exsym* are considered. If *orb1.sym1* and *orb2.sym2* are zero, all input vectors are moved to the output set ordered according to increasing extra symmetries.

Examples:

* ``EXTRA,1,-4.1`` will move the next 4 orbitals in symmetry 1 which have extra symmetry 1. Orbitals which have been moved before are skipped.
* ``EXTRA,2,1.1`` will move all orbitals of symmetry 1 which have extra symmetry 2. Orbitals which have been moved before are skipped.
* ``EXTRA`` will move all orbitals (all symmetries) and order them according to extra symmetries.
* ``EXTRA,3,1.1,0.8`` Will move all orbitals which have extra symmetry 3 in all symmetries. Orbitals which have been moved before are skipped.

See also ``ADD`` and ``MOVE`` commands.

.. _orbital_merging--defining-offsets-in-the-output-set-offset:

Defining offsets in the output set (OFFSET)
===========================================

``OFFSET,iof$_1$,iof$_2$,$\ldots$,iof$_8$;``

Sets offsets in the output vector for symmetries 1 to 8. In subsequent ``MOVE`` or ``ADD`` commands, the input vectors are moved to the locations *iof:math:`_i`+1* in the output vectors. The offset for individual ``ADD`` or ``MOVE`` commands can be modified by the parameter *ioff* on these cards. This card should immediately follow the orbital directive to which it applies. Generally, this card is only needed if the dimensions of input and output vectors are not identical.

If the dimensions of the input orbital sets are smaller than the current basis dimension, the offsets are determined automatically in the following way: each time an orbital set is read in, the previous input orbital dimensions are added to the offsets. Hence, this works correctly if the orbital sets are given in the correct order and if the individual dimensions add up to the current total dimension. If this is not the case, the offsets should be specified on an ``OFFSET`` card which must follow the orbital directive.

.. _orbital_merging--projecting-orbitals-project:

Projecting orbitals (PROJECT)
=============================

``PROJECT,namin.file``

This command will read vectors from record *namin.file*. These vectors must have the same dimension as those of the current calculation. All orbitals defined so far by the ``ORBITAL``, ``MOVE``, and ``ADD`` directives are projected out of the input set. The projected orbitals are then orthonormalized and moved to the undefined output vectors. This should always yield a complete set of vectors.

.. _orbital_merging--symmetric-orthonormalization-orth:

Symmetric orthonormalization (ORTH)
===================================

``ORTH,$n_1,n_2,\ldots,n_8$``

Symmetrically orthonormalizes the first :math:`n_i` vectors in each symmetry :math:`i`. These vectors must be supplied before by ``ORBITAL`` and ``MOVE`` or ``ADD`` directives.

.. _orbital_merging--schmidt-orthonormalization-schmidt:

Schmidt orthonormalization (SCHMIDT)
====================================

``SCHMIDT,$n_1,n_2,\ldots,n_8$``

Schmidt orthonormalizes the first :math:`n_i` vectors in each symmetry :math:`i`. These vectors must be supplied before by ``ORBITAL`` and ``MOVE`` or ``ADD`` directives.

.. _orbital_merging--rotating-orbitals-rotate:

Rotating orbitals (ROTATE)
==========================

``ROTATE,iorb1.sym,iorb2,angle``

Will perform :math:`2 \times 2` rotation of orbitals *iorb1* and *iorb2* in symmetry *sym* by the specified *angle* (in degree). *angle=0* means to swap the orbitals (equivalent to *angle=90*) These vectors must be supplied before by ``ORBITAL`` and ``MOVE`` or ``ADD`` directives.

.. _orbital_merging--initialization-of-a-new-output-set-init:

Initialization of a new output set (INIT)
=========================================

``INIT,namout.file``

Will initialize a new output set. All previous vectors in the output set are lost unless they have been saved by a ``SAVE`` directive!

.. _orbital_merging--saving-the-merged-orbitals:

Saving the merged orbitals
==========================

``SAVE,namout.file``

Saves the current output set to record *namout.file*. The current output set must be complete and will be Schmidt orthonormalized before it is saved. If the ``SAVE`` directive is not supplied, the output vectors will be saved after all valid commands have been processed to the record specified on the ``MERGE`` card.

.. _orbital_merging--printing-options-print:

Printing options (PRINT)
========================

``PRINT,iprint,ideb``

Specifies print options.

* :math:`iprint = 0` no print
* **:math:`iprint \ge 1`:** orthonormalized orbitals specified on ``ORTH`` card are printed.
* **:math:`iprint \ge 2`:** orbitals are also printed before this orthonormalization.
* **:math:`iprint \ge 3`:** all final vectors are printed.
* **:math:`ideb \ne 0`:** the overlap matrices are printed at various stages.

.. _orbital_merging--examples:

Examples
========

.. _orbital_merging--h2f:

H2F
===

This example merges the orbitals of H\ :math:`_2` and F

.. code-block:: text
   :caption: examples/h2f_merge.inp

   ***,example for merge
   print,orbitals,basis
   rh2=1.4
   rhf=300.
   basis=vdz
   symmetry,x,y                            !use C2v symmetry
   geometry={F}
   
   text,F
   {rhf;wf,9,1,1;occ,3,1,1;orbital,2130.2} !rhf for f-atom
   
   text,H2
   symmetry,x,y                            !use C2v symmetry
   geometry={
            H1,
            H2,H1,rh2}
   
   {hf;orbital,2100.2}                     !scf for h2
   {multi;occ,2;orbital,2101.2}            !mcscf for h2
   
   text,FH2
   geometry={F;                            !linear geometry for F+H2
            H1,F,rhf
            H2,H1,rh2,F,180}
   
   int
   {merge
   orbital,2130.2                          !rhf orbitals for F-atom
   move,1.1,2.1,1.1                        !move orbitals 1.1, 2.1
   move,3.1,0.4,4.1;                       !move all remaining, starting at 4.1
   orbital,2100.2                          !hf orbitals for H2
   move,1.1,0.4                            !move these to free positions
   save,2131.2}                            !save merged orbitals
   
   {rhf;occ,4,1,1;start,2131.2             !rhf for F+H2
   orbital,2132.2}
   
   {merge
   orbital,2130.2                          !rhf orbitals for F-atom
   move,1.1,2.1,1.1                        !move orbitals 1.1, 2.1
   move,3.1,3.1,4.1;                       !move orbital 3.1 to 4.1
   move,4.1,0.4,6.1                        !move all remaining, starting at 6.1
   orbital,2101.2                          !mcscf orbitals for H2
   move,1.1,0.4                            !move these to free positions
   save,2141.2}                            !save merged orbitals
   
   {multi;occ,5,1,1;start,2141.2}          !casscf for F+H2 using valence space

.. _orbital_merging--no:

NO
===

This example merges the SCF orbitals of N and O to get a full valence space for NO. In the simplest case the atomic calculations are performed in the individual separate basis sets, but using the same symmetry (C\ :math:`_{2v}`) as the molecular calculation.

.. code-block:: text
   :caption: examples/no_merge1.inp

   ***,NO merge
   r=2.1
   
   symmetry,x,y
   geometry={n}         !N-atom, c2v symmetry
   
   {rhf;occ,3,1,1;      !rhf nitrogen
   wf,7,4,3;            !4S state
   orbital,2110.2}      !save orbitals to record 2110 on file 2
   
   symmetry,x,y
   geometry={o}
   
   {rhf;occ,3,1,1;      !rhf for oxygen
   wf,8,4,2             !3P state
   orbital,2120.2}      !save orbitals to record 2120 on file 2
   
   geometry={n;o,n,r}   ! NO molecule, c2v symmetry
   
   int
   {MERGE
   ORBITAL,2110.2       ! read orbitals of N atom
   MOVE,1.1,1.1         ! move 1s orbital to output vector 1.1
   MOVE,2.1,2.1,3.1     ! move 2s orbital to output vector 3.1
   MOVE,3.1,3.1,5.1     ! move 2pz orbital to output vector 5.1
   MOVE,1.2,1.2         ! move 2px orbital to output vector 1.2
   MOVE,1.3,1.3         ! move 2py orbital to output vector 1.3
   MOVE,4.1,,7.1        ! move virtual orbitals of symmetry 1
   MOVE,2.2,,3.2        ! move virtual orbitals of symmetry 2
   MOVE,2.3,,3.3        ! move virtual orbitals of symmetry 2
   MOVE,1.4             ! move virtual orbitals of symmetry 2
   ORBITAL,2120.2       ! read orbitals of O atom
   MOVE,1.1,0.4         ! move all oxygen orbitals into place
   ROT,3.1,4.1,45;      ! rotate 2s orbitals to make bonding and antibonding
                        ! linear combinations
   ROT,5.1,6.1,-45;     ! rotate 2pz orbitals to make bonding and antibonding
                        ! linear combinations
   PRINT,1              ! set print option
   ORTH,6,2,2           ! symmetrically orthonormalize the valence orbitals
                        ! the resulting orbitals are printed
   save,2150.2}         ! save merged orbitals to record 2150.2
   
   {multi;occ,6,2,2     ! perform full valence casscf for NO
   wf,15,2,1            ! 2Pix state
   wf,15,3,1            ! 2Piy state
   start,2150.2}        ! start with merged orbitals

One can also do the atomic calculations in the total basis set, using dummy cards. In this case the procedure is more complicated, since the union of the two orbital spaces is over-complete. The calculation can be done as follows:

a) SCF for the total molecule, orbitals saved to 2100.2

b) SCF for the N atom with dummy basis on the O atom, orbitals saved on 2110.2

c) SCF for the O atom with dummy basis on the N atom, orbitals saved on 2120.2

d) Merge the atomic SCF orbitals. Finally, obtain the virtual orbitals by projecting the merge orbitals out of the SCF orbitals for NO.

.. code-block:: text
   :caption: examples/no_merge2.inp

   ***,NO merge
   geometry={n;o,n,r}
   r=2.1
   
   {rhf;occ,5,2,1     !rhf for NO
   wf,15,2,1          !2Pi state
   orbital,2100.2}    !save orbitals to record 2100 on file 2
   
   dummy,o            !oxygen is dummy
   {rhf;occ,3,1,1;     !rhf nitrogen
   wf,7,4,3;          !4S state
   orbital,2110.2}    !save orbitals to record 2110 on file 2
   
   dummy,n            !nitrogen is dummy
   {rhf;occ,3,1,1;    !rhf for oxygen
   wf,8,4,2           !3P state
   orbital,2120.2}    !save orbitals to record 2120 on file 2
   
   dummy              ! remove dummies
   {MERGE              !call merge program
   
   ORBITAL,2110.2     ! read orbitals of N atom
   MOVE,1.1,1.1       ! move input vector 1.1 to output vector 1.1
   MOVE,2.1,3.1,3.1   ! move input vectors 2.1,3.1 to output vectors
                      ! 3.1 and 4.1
   MOVE,1.2,1.2       ! move input vector 1.2  to output vector 1.2
   MOVE,1.3,1.3       ! move input vector 1.3  to output vector 1.3
   ORBITAL,2120.2     ! read orbitals of O atom
   MOVE,1.1,3.1       ! move input vectors 1.1 to 3.1 to output vectors
                      ! 2.1, 5.1, 6.1
   MOVE,1.2,1.2       ! move input vector 1.2 to output vector 2.2
   MOVE,1.3,1.3       ! move input vector 1.3 to output vector 2.3
   ROT,3.1,5.1,45;    ! rotate 2s orbitals to make bonding and antibonding
                      ! linear combinations
   ROT,4.1,6.1,-45;   ! rotate 2pz orbitals to make bonding and antibonding
                      ! linear combinations
   PRINT,1            ! set print option
   ORTH,6,2,2         ! symmetrically orthonormalize the valence orbitals
                      ! the resulting orbitals are printed
   PROJ,2100.2        ! Project valence orbitals out of scf orbitals of the
                      ! molecule and add virtual orbital set.
   SAVE,2150.2        ! save merged orbitals to record 2150 on file 2
   }
   
   {multi;occ,6,2,2   ! perform full valence casscf for NO
   wf,15,2,1          ! 2Pi state
   wf,15,3,1          ! 2Pi state
   start,2150.2}      ! start with merged orbitals
