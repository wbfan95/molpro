.. raw:: html

   <span id="multi-layer-embedding"></span>

.. raw:: html

   <span id="selecting-the-embedded-orbitals"></span>

.. raw:: html

   <span id="truncating-the-virtual-space"></span>

.. _region--region:

Region
======

The ``REGION`` program allows a correlated method to be applied to a target region within a molecule, where it is restricted to a subset of spatially localised orbitals, and the rest of the valence electrons left uncorrelated and only treated at the mean-field level.

The correlated region can be embedded within an SCF environment (that of the reference wave function), or within a lower level correlated method using a simple subtractive approach (see section `Multi-layer embedding <region.html#multi-layer-embedding>`__). Multi-layer embedding can also be achieved using the same subtractive approach.

Firstly, molecular orbitals are localised using the intrinsic bonding orbital (IBO) method, described in chapter :doc:`intrinsic basis bonding analysis (IAO/IBO) <intrinsic_basis_bonding_analysis_iao_ibo>`. Occupied orbitals to be embedded are either chosen directly by the user, or the user chooses a set of atoms, and the orbitals sat on these atoms are embedded (see section `selecting the Embedded Orbitals <region.html#selecting-the-embedded-orbitals>`__). The occupied orbitals are reordered putting the embedded orbitals at the top, followed by the other valence orbitals which are placed into the core. The embedded and active/open orbital spaces are then made pseudo-canonical.

The virtual orbital space can also be reduced and localised to the embedding region (see section `truncating the virtual space <region.html#truncating-the-virtual-space>`__). This can only be utilised by the ``FCI`` program within Molpro (and some third-party programs interfaced to Molpro), because the number of molecular orbitals no longer equals the number of basis functions. However, regional local coupled cluster can be performed :doc:`PNO-LCCSD(T)-F12 program <local_correlation_methods_with_pair_natural_orbitals_pnos>` (recommended, see section `Correlation regions in the PNO program <local_correlation_methods_with_pair_natural_orbitals_pnos.html#correlation-regions-in-the-pno-program>`__) or by the old (obsolete) :doc:`DF-LCCSD program <pao-based_local_correlation_treatments>` (see section `correlating subsets of electrons (REGION) <pao-based_local_correlation_treatments.html#correlating-subsets-of-electrons-region>`__ for details).

.. _region--defining-the-orbital-spaces:

Defining the Orbital Spaces
===========================

The molecular orbitals are controlled using the directives:

``START,$<$record.file$>$``

``SAVE,$<$record.file$>$``

Molecular orbitals are read from the dump record given after ``START``, and saved to the dump record given after ``SAVE``

The initial occupancies of each orbital space are controlled using the usual directives:

``CORE,$<$integer$>$``

``CLOSED,$<$integer$>$``

``OCC,$<$integer$>$``

``WF,charge=$<$integer$>$,sym=$<$integer$>$,spin=$<$integer$>$``

The correct number of core orbitals must be known to the ``REGION`` program (either through inheriting it from the previous calculation, or through explicit declaration by the user). The core orbitals are kept separate from the inactive orbital space when performing the IBO localisation. If the definition of the core is changed, these two spaces will mix, leading to a slightly different set of embedded IBOs.

.. _region--selecting-the-embedded-orbitals:

Selecting the Embedded Orbitals
===============================

The IBOs to be embedded can be specified directly with the ``ORBITALS`` option, either using their index, or as a range of indices e.g.,

.. code-block:: text

   {REGION,ORBITALS=[10-15,17,21]}

Alternatively, the orbitals can be found automatically by choosing a set of target atoms with the ``ATOMS`` option. Orbitals exerting an IBO partial charge of at least ``THRESH_REGION`` (default=0.2 a.u.) on *any* of the target atoms, are included in the embedding region. Atoms may be specified using their names in the geometry specification, index, or using ranges of indices e.g.

.. code-block:: text

   {REGION,ATOMS=[H10-H15,C17,N21]}

or

.. code-block:: text

   {REGION,ATOMS=[H,17,N2]}

Further control of the ``ATOMS`` option is achieved using the ``ORB_SELECT`` option, which controls how strictly the target atoms inherit their orbitals. When ``ORB_SELECT=INCLUSIVE`` (the default), an orbital is embedded if *any* of the atoms it sits on are included in the target atoms. When ``ORB_SELECT=EXCLUSIVE``, an orbital is only embedded if *all* the atoms it sits on are included in the target atoms. For example, in the following molecule:

.. code-block:: text

   H      H
    \    /
     C1=C2
    /    \
   H      H

The command

.. code-block:: text

   {REGION,ATOMS=[C1,C2],ORB_SELECT=EXCLUSIVE}

selects only the carbon-carbon sigma and pi bonds, whereas the command

.. code-block:: text

   {REGION,ATOMS=[C1,C2],ORB_SELECT=INCLUSIVE}

selects all the bonds.

For both the ``ORBITALS`` and ``ATOMS`` options, the active orbital space (in a CASSCF wave function) or the open orbitals (in a single-reference wave function) are always included in the embedding region. Therefore using an empty ``ORBITALS`` or ``ATOMS`` option will embed only the active orbitals e.g.

.. code-block:: text

   {REGION,ORBTIALS=[]}
   {REGION,ATOMS=[]}

Core orbitals (as defined by the ``CORE`` variable) are exuded from the embedding region.

Finally the embedded orbital space is made pseudo-canonical by diagonalising the embedded-embedded block of the Fock matrix, and similarly the active/open orbitals. This can be disabled by setting the ``SEMI_CAN=false``.

.. _region--truncating-the-virtual-space:

Truncating the virtual space
============================

The ``FCI`` program, and some third-party programs interfaced to Molpro, can handle a reduction in the number of virtual orbitals. This procedure is called the *deleted virtual approximation*, and can significantly reduce the cost of correlated calculations. When the option ``FULL_VIRT=false``, a truncated virtual space localized to the embedding region is constructed from projected atomic orbitals (PAOs). By default ``FULL_VIRT=true`` and the full canonical virtual space from the previous SCF calculation is retained.

PAOs located on a set of ‘host atoms’ are transformed by means of a singular value decomposition of their overlap matrix. Virtual functions with an eigenvalue below ``THRESH_REDUN`` (default=\ :math:`1.0\times10^{-8}`) are considered redundant and deleted. PAOs on the other, environment, atoms are also discarded.

Host atoms are those sat ‘underneath’ the embedded occupied orbitals. When the embedded orbitals exert an IBO partial charge of at least ``THRESH_REGION`` (default 0.2 a.u.) on an atom, then it is classified as a host atom. Further host atoms may be manually included by using the ``HOST_ATOMS`` option. This allows the virtual domain to be extended.

The truncated virtual space is made pseudo-canonical by diagonalising the virtual-virtual block of the Fock matrix. This can be disabled by setting the ``SEMI_CAN=false``.

.. _region--multi-layer-embedding:

Multi-layer embedding
=====================

Treating the environment with a second correlated method (that is usually less expensive) is done with a simple subtractive embedding procedure, defined as

.. math::

   E = E_{low}(A+B) - E^{reg}_{low}(A) + E^{reg}_{high}(A).

The argument :math:`A` denotes the central target region, and :math:`B` the environment, and the subscripts denote the accuracy (and cost) of the correlated methods. :math:`E^{reg}_{low}(A)` is an energy calculation performed using the ``REGION`` program, with a lower level correlated method on the target region, for example MP2. Similarly :math:`E^{reg}_{high}(A)` is performed with a higher level correlated method on the *same* target region, for example CISD.

Multiple embedding layers can be achieved through repeatedly applying the above equation.

.. _region--summary-of-all-options:

Summary of all options
======================

* ``OBRITALS=``\ *:math:`<`string:math:`>`* Example: ‘[6,7,8,9-12]’. Indices of IBOs to be embedded.
* ``ATOMS=``\ *:math:`<`string:math:`>`* Example: ‘[C1,C2,H3,H4-H6]’. Orbitals exerting an IBO partial charge of at least ``THRESH_REGION`` on these atoms are embedded.
* ``ORB_SELECT=``\ *:math:`<`string:math:`>`* Either ‘INCLUSIVE’ or ‘EXCLUSIVE’. Controls how strictly embedded orbitals are selected, when using the ``ATOMS`` option. Default=INCLUSIVE.
* ``HOST_ATOMS=``\ *:math:`<`string:math:`>`* Example: ‘[C4,C5,H6-H10]’. List of extra host atoms, added to those chosen automatically. Only relevant when ``FULL_VIRT=false``.
* ``THRESH_REGION=``\ *:math:`<`double:math:`>`* IBO partial charge threshold. Determines which orbitals are sat on those atoms specified with the ``ATOMS`` option, as well as host atoms underneath embedded orbitals. Default=0.2 atomic units.
* ``THRESH_REDUN=``\ *:math:`<`double:math:`>`* Eigenvalue threshold. Determines redundant virtual functions when ``FULL_VIRT=false``. Default=\ :math:`1.0\times10^{-8}`.
* ``SEMI_CAN=``\ *:math:`<`logical:math:`>`* Control pseudo-canonicalisation of the embedded orbital spaces. Default=true.
* ``FULL_VIRT=``\ *:math:`<`logical:math:`>`* When true, the full canonical virtual space from the previous SCF calculation is retained. When false, a truncated virtual space is constructed. Default=true.
* ``IBO_AO_TYPE=``\ *:math:`<`string:math:`>`* Minimal basis set used by the IBO program. Default is that of the IBO program (MINAO-PP).
* ``PLOT_PAOS=``\ *:math:`<`logical:math:`>`* Writes the PAOs to the dump record, so they can be visualized by an orbital viewing program. Default=false.
* ``PRINT_MAP=``\ *:math:`<`logical:math:`>`* Prints a mapping of the rearranged IBO indices to the original IBO indices. Default=true.
* ``REGION_TYPE=``\ *:math:`<`integer:math:`>`* When set to 0, the atomic core and environment valence orbitals are totally deleted. This allows the user to plot the embedded orbitals only, though cannot be used for viable calculations. When set to 1, the atomic core and environment orbitals are placed into the core. These orbitals must be used for actual calculations. Default=1.

.. _region--examples:

Examples
========

This is an example of embedding MRCI inside CASPT2 for Butane.

.. code-block:: text

   memory,100,M
   gprint,orbitals,civector
   nosym;noextra
   ANGSTROM
   Geometry={
   C1 ,,   0.0000 ,0.7647+y ,0.0000
   C2 ,,   0.0000 ,-0.7647-y, 0.0000
   C3 ,,   -1.4029, 1.3695+y,0.0000
   C4 ,,   1.4029 ,-1.3695-y, 0.0000
   H5 ,,   0.5526 ,1.1231+y ,0.8740
   H6 ,,   0.5526 ,1.1231+y ,-0.8740
   H7 ,,   -0.5526, -1.1231-y,0.8740
   H8 ,,   -0.5526, -1.1231-y,-0.8740
   H9 ,,   -1.3684, 2.4598+y,0.0000
   H10,,   1.3684 ,-2.4598-y,0.0000
   H11,,   -1.9674, 1.0558+y,-0.8807
   H12,,   -1.9674, 1.0558+y,0.8807
   H13,,   1.9674 ,-1.0558-y,-0.8807
   H14,,   1.9674 ,-1.0558-y,0.8807}
   y=1.0
   basis=vdz
   
   {multi;closed,16;occ,18;wf,charge=0,sym=1,spin=0}
   
   {rs2c}
   e1=energy
   
   {region,orbitals='[7-10]';
   core,4;closed,16;occ,18;save,2200.2;wf,charge=0,sym=1,spin=0}
   
   {put,molden,p1.molden;nosort}
   
   {rs2c;orbital,2200.2}
   e2=energy
   
   {ci;orbital,2200.2}
   e3=energy
   
   e=e1-e2+e3

.. _region--references:

References
==========

Hans-Joachim Werner and Andreas Hansen, Local Wave Function Embedding: Correlation Regions in PNO-LCCSD(T)-F12 Calculations
`J. Phys. Chem. A <https://pubs.acs.org/doi/10.1021/acs.jpca.4c06852>`__ **128**, 10936–10947 (2024).
