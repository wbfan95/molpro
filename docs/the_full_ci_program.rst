.. raw:: html

   <span id="convergence-threshold"></span>

.. raw:: html

   <span id="defining-the-orbitals"></span>

.. raw:: html

   <span id="defining-the-state-symmetry"></span>

.. raw:: html

   <span id="example"></span>

.. raw:: html

   <span id="excited-states"></span>

.. raw:: html

   <span id="frozen-core-orbitals"></span>

.. raw:: html

   <span id="interface-to-other-programs"></span>

.. raw:: html

   <span id="occupied-orbitals"></span>

.. raw:: html

   <span id="printing-options"></span>

.. _the_full_ci_program--the-full-ci-program:

The full CI program
===================

This module is the determinant full CI program, as described in

P.J. Knowles and N.C. Handy, `Chem. Phys. Lett. <https://dx.doi.org/10.1016/0009-2614(84)85513-X>`__ **111**, 315 (1984),
P.J. Knowles and N.C. Handy, Comp. Phys. Commun. 54 (1989) 75.

Published work resulting from the use of this program should cite these references.

The program in normal use finds the lowest eigenvector of the complete CI hamiltonian matrix; more sophisticated use is possible, but not documented here. The program is interfaced to free standing versions such as supplied in the CPC program library by use of the ``DUMP`` option.

The program is called with the command ``FCI``.

.. _the_full_ci_program--defining-the-orbitals:

Defining the orbitals
=====================

``ORBIT,name.file;``

*name.file* specifies the record from which orbitals are read. The default is the set of orbitals from the last SCF, MCSCF or CI calculation.

.. _the_full_ci_program--occupied-orbitals:

Occupied orbitals
=================

``OCC,$n_1,n_2,\ldots,n_8$;``

:math:`n_i` specifies numbers of occupied orbitals (including ``CORE``) in irreducible representation number :math:`i`. If not given, the default is the complete basis set.

.. _the_full_ci_program--frozen-core-orbitals:

Frozen-core orbitals
====================

``CORE,$n_1,n_2,\ldots,n_8$;``

:math:`n_i` is the number of frozen-core orbitals in irrep number :math:`i`. These orbitals are doubly occupied in all configurations, i.e., not correlated. If no ``CORE`` card is given, the program uses the same core orbitals as the last CI calculation; if there was none, then the atomic inner shells are taken as core. To avoid this behaviour and correlate all electrons, specify

``CORE``

.. _the_full_ci_program--defining-the-state-symmetry:

Defining the state symmetry
===========================

The number of electrons and the total symmetry of the wavefunction are specified on the ``WF`` card:

``WF,elec,sym,spin``

where

* ***elec*:** is the number of electrons
* ***sym*:** is the number of the irreducible representation
* ***spin*:** defines the spin symmetry, *spin*\ :math:`=2S` (singlet=0, doublet=1, triplet=2, etc.)

.. _the_full_ci_program--density-matrix:

Density matrix
==============

The 1-electron density matrix can be computed with

``DM,record.file``

and then subsequently used to calculate one-electron properties using the ``PROP`` program.

.. _the_full_ci_program--excited-states:

Excited states
==============

``STATE,value;``

Specifies the number of states to be sought (default 1).

.. _the_full_ci_program--convergence-threshold:

Convergence threshold
=====================

``THR,value;``

Convergence threshold (default :math:`10^{-5}`). If changes in the normalised wavefunction become less than this value, then the iterative eigenvector solver terminates.

.. _the_full_ci_program--printing-options:

Printing options
================

``PRINT,code,value;``

Print options. Generally, the value determines how much intermediate information is printed. *value*\ =-1 means no print (default for all codes). if *value* is omitted, it is taken as zero, which is usually appropriate. Specification of higher values will generate more output. The following codes are allowed:

* ``ORBITAL`` Print molecular orbitals
* ``INTEGRAL`` Print integrals
* ``TIMING`` Print extra timing information
* ``DIAGONAL`` Print diagonal elements of Hamiltonian
* ``HAMILTONIAN`` Print much intermediate information

.. _the_full_ci_program--interface-to-other-programs:

Interface to other programs
===========================

``FCI,DUMP=filename;``

causes the FCI diagonalization to be bypassed, with input information and transformed integrals being written to a formatted file *filename*. The format is as described in Comp. Phys. Commun. 54 (1989) 75, and in an external program should be accessed using the FCIdump class or module available from `https://github.com/molpro/fcidump. <https://github.com/molpro/fcidump>`__

.. _the_full_ci_program--example:

Example
=======

.. code-block:: text
   :caption: examples/h2o_fci.inp

   ***,FCI calculation for water in dz basis set
   basis=dz
   geometry={
   o
   h,,0.0, 1.1,1.4
   h,,0.0,-1.1,1.4}
   hf
   {fci
   wf,10,1;core,1}      ! these options could be omitted
                        ! FCI energy = -76.08088039
   ---;
