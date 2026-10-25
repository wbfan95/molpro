.. raw:: html

   <span id="general-considerations"></span>

.. _the_nevpt2_program--the-nevpt2-program:

The NEVPT2 program
==================

**Reference literature:**

C. Angeli, R. Cimiraglia, S. Evangelisti, T. Leininger and J. P. Malrieu, *J. Chem. Phys.*, **114**,10252, (2001)

C. Angeli, R. Cimiraglia and J. P. Malrieu, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.1515317>`__ **117**, 9138, (2002)

C. Angeli, M. Pastore and R. Cimiraglia, *Theor. Chem. Acc.*, **117**, 743 (2007)

All publications resulting from use of this program must acknowledge the above.

.. _the_nevpt2_program--general-considerations:

General considerations
======================

NEVPT2 is a form of second-order multireference perturbation theory which can be applied to CAS–SCF wavefunctions or, more generally, to CAS–CI wavefunctions. The term NEVPT is an acronym for *“n–electron valence state perturbation theory”*. While we refer the reader to the pertinent literature (see above), we limit ourselves to recalling here that the most relevant feature of NEVPT2 consists in that the first order correction to the wave function is expanded over a set of properly chosen *multireference* functions which correctly take into consideration the two–electron interactions occurring among the active electrons. Among the properties ensured by NEVPT2 we quote:

* Strict separability (size consistence): the energy of a collection of non–interacting systems equals the sum of the energies of the isolated systems
* Absence of intruder states: the zero-order energies associated to the functions of the outer space are well separated from the zero-order energy of the state being studied, thus avoiding divergences in the perturbation summation
* The first order correction to the wavefunction is an eigenfunction of the spin operators :math:`S^2` and :math:`S_z`
* Electronically excited states are dealt with at the same level of accuracy as the ground state
* NEVPT2 energies are invariant under a unitary transformation of the active orbitals. Furthermore, the choice of canonical orbitals for the core and virtual orbitals (the default choice) ensure that the results coincide with those of an enlarged version of the theory fully invariant under rotations in the core and virtual orbital spaces, respectively
* NEVPT2 coincides with MP2 in the case of a HF wave function

NEVPT2 has been implemented in two variants both of which are present in ``MOLPRO``, these are the *strongly contracted* (SC) and the *partially contracted* (PC) variants. The two variants differ by the number of perturber functions employed in the perturbation summation. The PC–NEVPT2 uses a richer function space and is in general more accurate than the SC–NEVPT2. The results of SC–NEVPT2 and PC–NEVPT2 are anyway usually very close to one another.

Since Molpro2021.2, density fitting can be used to compute the integrals, and the program is then called with
``DF-NEVPT2.``

``If you encounter an error exit due to non-zero Fock-matrix elements, the following can help:``

* In state-averaged  CASSCF calculations, save state-specific canonical or natural orbitals in multi, e.g. for the second state in symmetry 1: ``NATORB,2141.2,state=2.1``. Do this for each state you want to treat by NEVPT2 with a different record. If you hit in multi the message "too many NATORB directives", you can use a subsequent CASCI calculation to add more NATORB directives.
* Use the ``NOEXTRA`` directive in multi.
* Add in nevpt2 the directives: ``PSPACE,1; OPTION, NSTATI=n; ORBIT,record``, where n is the number of states you have optimized in multi for the current symmetry, and record is the record on which you have saved the orbitals for the state under consideration (in fact, what matters is the state-specific Fock matrix, which is saved along with the orbitals).

.. _the_nevpt2_program--input-description:

Input description
=================

NEVPT2 must follow a CAS–SCF or CAS–CI calculation. The command

``NEVPT2,options\\``
has to be specified to carry out a second–order perturbation calculation. NEVPT2 is part of the MRCI program and uses the options of the latter. Of particular relevance are the options ``CORE``, ``CLOSED``, ``OCC``, ``WF`` and ``STATE`` of the MRCI program. There is, at the moment, only one option specific to NEVPT2 which can be provided by the user:

* ``THRNEVPT2`` The threshold to discard small coefficients in the CAS wavefunction (default = 0.0),

The present implementation of NEVPT2 is state–specific, *i.e.* the perturbation theory can only be applied to a single state.

An example is provided where the energies of the ground state and of the first :math:`^1A_2` (:math:`n \to \pi^*`) excited state of formaldehyde are calculated.

The first example shows a detailed input, where occupations, spatial and spin symmetries, and orbital orbital records are given explicitly in each step. This input can be much simplified by using defaults: the NEVPT2 program (as also other correlation programs) automatically use the same occupations, symmetries and orbitals as in the previous CASSCF orbital optimisation. The third example uses density fitting approximations for the integrals, which is strongly recommended for larger molecules.

.. code-block:: text
   :caption: examples/form_nevpt2.inp

   geometry
    O,,             0.000000000,     0.000000000,    0.0196594609
    C,,             0.000000000,     0.000000000,    2.3248507925
    H1,,            0.000000000,     1.7597110083,   3.3972521023
    H2,,            0.000000000,    -1.7597110083,   3.3972521023
   end
   
   basis=6-31G*
   
   {multi
   closed,4,0,1,0
   occ,6,2,4,0
   wf,16,1,0
   state,1
   natorb,2140.2,state=1.1
   }
   
   {nevpt2
   core,2,0,0,0
   closed,4,0,1,0
   occ,6,2,4,0
   orbit,2140.2,state=1.1
   wf,16,1,0
   }
   
   {multi
   closed,4,0,1,0
   occ,6,2,4,0
   wf,16,4,0
   start,2140.2
   natorb,2141.2,state=1.4
   }
   {nevpt2
   core,2,0,0,0
   closed,4,0,1,0
   occ,6,2,4,0
   orbit,2141.2,state=1.4
   wf,16,4,0
   }

Simplified input:

.. code-block:: text
   :caption: examples/form_nevpt2_simple.inp

   geometry
    O,,             0.000000000,     0.000000000,    0.0196594609
    C,,             0.000000000,     0.000000000,    2.3248507925
    H1,,            0.000000000,     1.7597110083,   3.3972521023
    H2,,            0.000000000,    -1.7597110083,   3.3972521023
   end
   
   basis=6-31G*
   
   {multi
   occ,6,2,4,0
   closed,4,0,1,0}
   
   nevpt2
   
   {multi
   occ,6,2,4,0
   closed,4,0,1,0
   wf,sym=4}
   
   nevpt2

Calculation with density fitting:

.. code-block:: text
   :caption: examples/form_dfnevpt2.inp

   geometry
    O,,             0.000000000,     0.000000000,    0.0196594609
    C,,             0.000000000,     0.000000000,    2.3248507925
    H1,,            0.000000000,     1.7597110083,   3.3972521023
    H2,,            0.000000000,    -1.7597110083,   3.3972521023
   end
   
   basis=6-31G*
   
   {df-multi
   occ,6,2,4,0
   closed,4,0,1,0}
   
   df-nevpt2
   
   {df-multi
   occ,6,2,4,0
   closed,4,0,1,0
   wf,sym=4}
   
   df-nevpt2
