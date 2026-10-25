.. raw:: html

   <span id="defining-groups-of-orbitals-group-offdiag"></span>

.. raw:: html

   <span id="defining-reference-orbitals-reforb"></span>

.. raw:: html

   <span id="defining-the-core-orbitals-core"></span>

.. raw:: html

   <span id="defining-the-occupied-space-occ"></span>

.. raw:: html

   <span id="delocalization-of-orbitals-delocal"></span>

.. raw:: html

   <span id="localization-between-groups-offdiag"></span>

.. raw:: html

   <span id="localization-thresholds-thresh"></span>

.. raw:: html

   <span id="localizing-aos-locao"></span>

.. raw:: html

   <span id="no-reordering-noorder"></span>

.. raw:: html

   <span id="ordering-of-localized-orbitals"></span>

.. raw:: html

   <span id="printing-options-print"></span>

.. raw:: html

   <span id="saving-the-localized-orbitals-save"></span>

.. raw:: html

   <span id="selecting-a-density-matrix-density"></span>

.. raw:: html

   <span id="selecting-the-fock-matrix-fock"></span>

.. raw:: html

   <span id="selecting-the-orbital-space"></span>

.. _orbital_localization--orbital-localization:

Orbital localization
====================

Localized orbitals are calculated according to the Boys, Pipek-Mezey or NLMO criteria. Localization takes place within each symmetry species separately. For intrinsic bond orbital (IBO) localization, see the IBBA program, section :doc:`intrinsic basis bonding analysis (IAO/IBO) <intrinsic_basis_bonding_analysis_iao_ibo>`. If complete localization is desired, no symmetry should be used. All subcommands can be abbreviated by three characters.

The localization program is invoked by the ``LOCALI`` command

``LOCALI [,method],[LOCMETHOD=locmethod],[REFORB=record],[THRPIP|THRBOYS=thresh]``

The keyword *method* can be either ``BOYS``, ``PIPEK``, ``NATURAL``, ``IBO`` By default, the canonical valence orbitals from the last energy calculation are localized using the Boys criterion. Only orbital subsets which leave the energy invariant are transformed. These defaults can be modified using the optional commands described in the following sections.

The option ``LOCMETHOD`` only applies to Pipek-Mezey localization. The value *locmethod* can take the following values:

* ***locmethod=1:*** Standard iterative localization method
* ***locmethod=2:*** Use second-order localization method. Redundant rotations will be eliminated.
* ***locmethod=3:*** First do a first iterations using the standard method, then invoke locmethod=2. This option is recommended in cases with redundant rotations, e.g., benzene.

The option ``REFORB`` has the same effect as the directive ``REFORB`` described further below.

The option ``THRPIP`` (``THRBOYS`` is an alias) is the threshold used for Pipek-Mezey or Boys localization (same as ``THRESH`` in section `localization thresholds (THRESH) <orbital_localization.html#localization-thresholds-thresh>`__).

.. _orbital_localization--defining-the-input-orbitals-orbital:

Defining the input orbitals (ORBITAL)
=====================================

``ORBITAL,record.file,specifications``

The orbitals to be localized are read from dump record *record.file*. A state specific orbital set can be selected using *specifications*, as explained in section `selecting orbitals and density matrices (ORBITAL, DENSITY) <general_program_structure.html#selecting-orbitals-and-density-matrices-orbital-density>`__. Default are the orbitals calculated last.

.. _orbital_localization--saving-the-localized-orbitals-save:

Saving the localized orbitals (SAVE)
====================================

``SAVE,record.file``

This specifies the dump record where the localized orbitals are stored. If the dump record already exists, the localized orbitals are added to it. Default is the input record (cf. ``ORBITAL``).

.. _orbital_localization--choosing-the-localization-method-method:

Choosing the localization method (METHOD)
=========================================

``METHOD,method``

The localization method *method* can be either ``BOYS``, ``PIPEK``, ``NATURAL``, or ``IBO``. This can also be specified as argument on the ``LOCALI`` card (see above).

.. _orbital_localization--delocalization-of-orbitals-delocal:

Delocalization of orbitals (DELOCAL)
====================================

``DELOCAL``

If this card is present, the orbitals are delocalized. This is not implemented for ``NATURAL`` and ``IBO``.

.. _orbital_localization--localizing-aos-locao:

Localizing AOs(LOCAO)
=====================

``LOCAO``

If this card is present, the number of AOs contributing to each MO is minimized. This can be useful to rotate degenerate orbitals (e.g., px, py, pz in an atom) so that pure orbitals (in this case px, py, pz) result.

This implies Pipek-Mezey localization.

.. _orbital_localization--selecting-the-orbital-space:

Selecting the orbital space
===========================

By default, only the valence orbitals are localized, in order to ensure invariance of subsequent electron correlation treatments. This behaviour can be modified using the ``OCC`` and ``CORE`` directives, or the ``LOCCORE`` option:

* ``LOCCORE=0``: Core orbitals are not localized (default)
* ``LOCCORE=1``: Core orbitals are localized together with all other orbitals
* ``LOCCORE=2``: Core orbitals are localized among themselves.

By default, all non-valence orbitals are treated as core.

.. _orbital_localization--defining-the-occupied-space-occ:

Defining the occupied space (OCC)
=================================

``OCC, $o_1$, $o_2 \ldots$``

defines the highest orbital :math:`o_i` in each symmetry :math:`i` to be localized.

.. _orbital_localization--defining-the-core-orbitals-core:

Defining the core orbitals (CORE)
=================================

``CORE, $c_1$, $c_2 \ldots$``

The first :math:`c_i` orbitals in each symmetry are treated as core orbitals and not localized. Thus, orbitals :math:`c_i+1` to :math:`o_i` are localized in symmetry :math:`i`.

.. _orbital_localization--defining-groups-of-orbitals-group-offdiag:

Defining groups of orbitals (GROUP, OFFDIAG)
============================================

``GROUP,orb1,orb2,orb3,...``

This card defines groups of orbitals to be localized as follows:

* ``GROUP,1.1,2.1,3.1`` a group of orbitals 1-3 in symmetry 1
* ``GROUP,1.1,-3.1`` equivalent to previous example
* ``GROUP,3.1,5.1,-8.1`` this group includes orbitals 3,5,6,7,8 in symmetry 1

Orbitals in different groups are localized independently. Orbitals not included in any group are unchanged.

.. _orbital_localization--localization-between-groups-offdiag:

Localization between groups (OFFDIAG)
=====================================

``OFFDIAG``

If this card is present, localize between groups instead of within groups.

.. _orbital_localization--ordering-of-localized-orbitals:

Ordering of localized orbitals
------------------------------

``ORDER,type``

If *type*\ =\ ``CHARGE``, the orbitals are ordered according to their charge centroids (default).

If *type*\ =\ ``FOCK``, the orbitals are ordered according to increasing diagonal elements of the fock operator (PIPEK) or increasing Coulson-additive orbital energies (BOYS). This requires a Fock operator from the preceding energy calculation. For localization of Hartree-Fock orbitals, this operator is stored in the dump record and automatically found. For localization of MCSCF orbitals, an effective fock operator is computed from the MCSCF density matrix (see ``DENSITY`` option). Alternatively, a dump record of a previous SCF calculation can be specified on the ``FOCK`` card, and then the fock operator is read from this record. For degenerate orbitals, further ordering according to the the coordinates of charge centres is attempted (first according to largest z-coordinates, then according to x, then y).

This card does not apply to NLMO localization.

.. _orbital_localization--no-reordering-noorder:

No reordering (NOORDER)
=======================

``NOORDER``

If this card is present, the localized orbitals are not reordered. This is useful if localized orbitals are used as starting guess, and it is intended that their order remains unchanged.

.. _orbital_localization--ordering-using-domains-sort:

Ordering using domains (SORT)
=============================

``SORT,[THRCHCHG=charge][THREIG=eps],GROUP=igrp],[REVERT],centrelist``

This directive only works for Pipek-Mezey localization. The orbitals are ordered according to domains and the given centrelist. The contributions of the centres to domains are determined by Löwdin charges. Only centres with charges greater than ``THRCHCHG`` (default 0.4) are included in these domains. The orbitals are reordered according to the following criteria:

* The primary centre in a domain is the one with largest charge, the secondary centre the one with the next largest charge. Orbitals are reordered separately within each localization group. First all orbitals are sorted so that the primary centres are in the order of the given *centrelist*. Orbitals with primary centres which are not in *centrelist* come last.
* Within each group of orbitals found for a given primary centre, those containing only one centre (lone pairs) are included first. The remaining ones are ordered so that the secondary atoms are in the order of *centrelist*. Orbitals with secondary centres which are not in *centrelist* come last.
* If ``REVERT`` is given, the order in each localization group is reverted.
* If ``GROUP`` is given, only the orbitals in the given group are reordered. *igrp* is 2 for closed shells and inactive orbitals, 1 for open-shells in single reference methods, and 3 for active orbitals in CASSCF calculations.
* If ``THREIG`` is given, only orbitals with energies larger than the given value are reordered. *eps* must be negative. The remaining orbitals come last (first if ``REVERT`` is given).

Note that core orbitals are neither localized nor reordered.

.. _orbital_localization--defining-reference-orbitals-reforb:

Defining reference orbitals (REFORB)
====================================

``REFORB,record.file,specifications``

The localized orbitals are reordered such that the overlap with the reference orbitals read from *record.file* is maximized. This is useful for local correlation treatments for keeping the order of the localized constant for different geometries. A state specific orbital set can be selected using *specifications*, as explained in section `selecting orbitals and density matrices (ORBITAL, DENSITY) <general_program_structure.html#selecting-orbitals-and-density-matrices-orbital-density>`__.

.. _orbital_localization--selecting-the-fock-matrix-fock:

Selecting the fock matrix (FOCK)
================================

``FOCK,record.file``

This specifies a record holding a Fock operator to be used for ordering the orbitals. Note that only SCF dump records hold fock operators. Default is the Fock operator from the energy calculation which produced the input orbitals.

.. _orbital_localization--selecting-a-density-matrix-density:

Selecting a density matrix (DENSITY)
====================================

``DENSITY,record.file,specifications``

This specifies a record holding a density matrix for construction of a fock operator used for ordering the orbitals. This can be used if no fock operator is available, and has only an effect for MCSCF localizations. By default, the (state averaged) MCSCF density is used. A state specific density matrix can be selected using *specifications* as described in section `selecting orbitals and density matrices (ORBITAL, DENSITY) <general_program_structure.html#selecting-orbitals-and-density-matrices-orbital-density>`__.

.. _orbital_localization--localization-thresholds-thresh:

Localization thresholds (THRESH)
--------------------------------

.. code-block:: text

    ''THRESH'',//thresh,eorder// [locsec:thrpip]

*thresh* is a threshold for localization (default 1.d-9). If *eorder* is nonzero (default 1.d-4), the orbitals whose energy difference is smaller then *eorder* are considered to be degenerate and reordered according to the position of their charge centres (see section `ordering of localized orbitals <orbital_localization.html#ordering-of-localized-orbitals>`__).

.. _orbital_localization--options-for-pm-localization-pipek:

Options for PM localization (PIPEK)
-----------------------------------

Some special options exist for Pipek-Mezey localization and can be given on the ``PIPEK`` directive (optional):

``PIPEK,METHOD=method,DELETE=ndel,MAXDL=maxdl,THRESH|ACC=thresh,ORDER=iorder,STEP=step``

* **``METHOD``:** *method=1*: use 2x2 rotation method (default);

*method=2*: use Newton-Raphson method;
*method=3*: Initial iterations using 2x2 rotation method , final convergence using NR method.

* **``DELETE``:** Delete the last *ndel* basis functions of each angular momentum type for each atom in PM localization. This can be useful to achieve proper localization with diffuse (augmented) basis sets.
* **``MAXDL``:** If *ndel*\ :math:`>`\ 0 delete functions only up to angular momentum *maxdl*.
* **``ORDER``:** If *iorder=1*, order final orbitals according to increasing diagonal fock matrix elements;

If *iorder=2*, order final orbitals according charge centres (default).

* **``THRESH``:** Localization threshold (same as on ``THRESH`` directive).
* **``STEP``:** Max step size in NR method (default 0.1d0).

.. _orbital_localization--printing-options-print:

Printing options (PRINT)
------------------------

``PRINT,[ORBITAL=]pri [,CHARGE] [,CENTRES] [,TEST] [,TRAN];``

If ``ORB[ITAL]`` is given, the localized orbitals are printed.
If ``CHA[RGE]`` or ``CEN[TRES]`` is given, the charge centres of the localized orbitals are printed.
If ``TRAN`` is given, the transformation matrix is printed (Boys only).
If ``TEST`` is given, intermediate information is printed.
