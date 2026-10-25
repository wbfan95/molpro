.. _intermolecular_interaction_energies--intermolecular-interaction-energies:

Intermolecular interaction energies
===================================

Counterpoise corrected (or uncorrected) intermolecular interaction energies can be computed automatically using the ``INTERACT`` procedure:

``INTERACT, options``

The INTERACT command can follow any input for a complete energy calculation and then computes the interaction energy for the last computed energy method. Alternatively, the energy calculation can be defined in a procedure. In this case, the procedure must contain input for a complete energy calculation, including the orbital optimization.

Dimer and monomer calculations must be carried out with the same symmetry. Note that the symmetry in the monomer CP calculations is sometimes lower than that of the dimer. The program checks the symmetry and stops with a message if a lower symmetry needs to be specified.

The following *options* are available:

``*  DO_CP[=value] If zero, do not compute CP-correction (default DO_CP=1).\\``
\* ``DO_NOCP``\ [=\ *value*] Calculate non-cp corrected interaction energy (**default  DO_NOCP=0**). Note: this does not work with region calculations.
\* ``PROC[NAME]``\ =\ *procname* Use the given procedure to carry out the energy calculations.
\* ``STARTCMD``\ =\ *command* The energy calculation is defined by all input starting at this command until the **INTERACT** command.
\* ``VARIABLE=``\ =\ *name* Use energies provided in variable *name* to compute interaction energies. This can be a vector of values. If not given, a selection of energy variables is determined automatically.
\* ``UNIT``\ =\ *unit* Specifies a unit for the printed interaction energies. Can be KCAL, KJ, AU, or CM (**default KCAL/MOL**).
\* ``FAC``\ =\ *[factors]* Factors for each monomer. For example, if the two monomers in a dimer calculation are symmetry equivalent, one can give ``FAC=[2,0]``, which means that the second monomer calculation is skipped. The sum of the factors must equal the number of monomers.
``* CHARGE=[charges] Charges for each monomer (default zero)\\``
\* ``SPIN``\ =\ *[spins]* Spins for each monomer. This means the number of singly occupied orbitals, i.e. 2 :math:`m_s`. The spin of the complex is assumed to be the sum of the monomer spins.
\* ``FILE|SAVE``\ =\ *filename* Save intermediate results in the given file. If the file is present, the program automatically restarts from it (unless ``NEW`` is given, see below). New results for later restarts are written to this file. From Molpro 2025.3 it is possible to add options ``DO_CP`` or ``RELAX`` in a restart after a completed CP calculation. 
\* ``START[FILE]``\ =\ *filename* File used for restart (**default FILE**). This can be used to avoid overwriting of the restart data, for example in connection with ``REPEAT`` (see below). When ``STARTFILE`` and ``FILE`` are present and ``FILE`` is empty (new), ``REPEAT`` is implied. If ``FILE`` is not empty, restart data are taken from it.
\* ``NEW`` A new restart file is created. If it exists, it is overwritten.
\* ``REPEAT`` The calculation is repeated even if restart data are found. For example, one could first do the DF-HF and DF-CABS calculations, and subsequently carry out PNO-LCCSD(T)-F12 calculations. The difference to ``NEW`` is that a restart is carried out, and for example orbital records, monomers, and symmetry are remembered.
\* ``USE_LOG[FILE]`` If this option is given, the outputs are written to the logfile. 
\* ``MAXCALC``\ =\ *value* Only the given number of molecules is computed. This requires ``FILE`` to be present to save and restart the data. For example, in a new calculation ``MAXCALC=1`` would only compute the dimer energy. The option can be used to split an otherwise exceedingly long calculation into several smaller ones. 
\* ``SCALE``\ =\ *factor* Two atoms are considered as bonded if the distance between them is smaller than sum of the atomic radii multiplied by this factor. This can affect the automatic detection of the monomers (**default 1.2**).
\* ``NOSYM`` Forces the calculation to be carried out without symmetry.
\* ``RECORD``\ =\ *record* Dump record number for the dimer calculation. The records for each subsequent monomer calculations are incremented by one. Normally, the program determines the record number automatically and this option should normally not be given.
\* ``MERGE``\ =\ *[list of molecules]* Merge the specified molecules to one monomer. The numbering of molecules is as they are given in the total complex. For example, if the complex consists of 3 monomers (as, e.g. GGG in the L7 test set), one can merge the second and third to one using ``MERGE=[2,3]``. Then the interaction energy of G+GG will be computed.

.. _intermolecular_interaction_energies--references:

References
==========

Andreas Hansen, Peter J. Knowles, and Hans-Joachim Werner, Accurate Calculation of Noncovalent Interactions Using PNO-LCCSD(T)-F12 in Molpro
`J. Phys. Chem. A <https://pubs.acs.org/doi/full/10.1021/acs.jpca.5c02316>`__ 129, 4812-4833 (2025).
