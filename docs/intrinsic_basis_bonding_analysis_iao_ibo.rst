.. _intrinsic_basis_bonding_analysis_iao_ibo--intrinsic-basis-bonding-analysis-iao-ibo:

Intrinsic basis bonding analysis (IAO/IBO)
==========================================

The IBBA program is used to perform a chemical bonding analysis of a previously computed Hartree-Fock or Kohn-Sham wave function. Options include the computation of partial charges, bond orders, and localized bond orbitals (i.e., orbitals which correspond to “chemical intuition” bonds). The localized orbitals can be visualized by exporting to ``xml`` files or ``molden`` files:

.. code-block:: text

     ! the 'save' and 'orbital' directives are for illustration only here.
     ! This snipped would do the same without them.
     {df-rhf; save, 2101.2}
     {ibba; orbital,2101.2; save,2103.2}
     {put,xml,'orbs.xml'; orbital,2103.2; keepspherical; skipvirt}

Recommended programs for visualization include IboView (http://www.iboview.org) and the current and upcoming versions of jmol and  `jsmol <http://chemapps.stolaf.edu/jmol/jsmol/jsmol.htm>`__.

Additionally, IBOs can also be used as a general choice for localized molecular orbitals (LMOs), since they are an exact representation of the input determinant wave function (i.e., IBOs are related to canonical occupied orbitals by a unitary transformation). IBOs are a particularly good choice for local correlation methods, since they are both very stable (also in the presence of diffuse basis sets, unlike Pipek-Mezey orbitals) and very fast to compute (faster even than Pipek-Mezey or Boys orbitals). If used as input to subsequent correlation calculations, the *FREEZECORE* directive should be used (see below).

Intrinsic bond orbitals (IBOs) and intrinsic atomic orbital charges (IAO charges) can be computed via ``{ibba,option1=value1,option2=value2,…; directive1; directive2, ...}``

The techniques have been described and validated in

* Knizia, *Intrinsic atomic orbitals: An unbiased bridge between quantum theory and chemical concepts* `J. Chem. Theory Comput. <https://dx.doi.org/10.1021/ct400687b>`__ **9**, 4834 (2013)
* Knizia, Klein, *Electron Flow in Reaction Mechanisms-Revealed from First Principles* `Angew. Chem. Int. Ed. <https://dx.doi.org/10.1002/anie.201410637>`__, **54**, 5518 (2015)

The first article should be cited if the IBBA program is used for bonding analysis. The second one should be cited if the program is used for deriving chemical transformations (curly arrows) in reaction mechanisms.

Regular options are:

* ``AO`` Define the minimal AO basis set from which the intrinsic atomic orbitals are built. Defaults to ’MINAO-AUTO-PP’, which is a minimal basis set of spherically averaged Hartree-Fock orbitals (for most elements). This option can be used to change the orbitals which are considered as valence space for individual centers. For example, using this, 4p orbitals of 3d transition metals can be included into the valence space.
* ``BONDS`` Via ``{ibba,bonds=1}`` bond orders between the atoms and valencies of atoms are computed. The bond orders includes both the IAO-generalization of Wiberg bond orders and the (unpublished) renormalized bond orders.
* ``IBORTH`` Defines the orthogonalization method to use. Can be ’SYM’ for Loewdin’s symmetric orthogonalization or ’ZBD’ for Laikov’s zero-bond dipole orthogonalization (if using ZBD, please cite Laikov: http:''dx.doi.org/10.1002/qua.22767). Defaults to ’SYM’. ’ZBD’ orthogonalization may give charges in closer correspondence with electrostatic potentials and chemical intuition, but extensive tests have not yet been performed.
* ``IBOEXP`` Exponent to use in the localization functional. Defaults to 4. Allowed values are 2 and 4.
* ``ANTIBONDS`` If set to 1, IBBA will compute not only localized occupied orbitals, but also localized unoccupied orbitals in the valence space. The localized unoccupied orbitals will typically correspond to the unoccupied anti-bonding orbitals.

Further specialist options:

* ``THRLOC_IB`` Threshold for convergence of localization. Defaults to 1e-8
* ``MAXIT_IB`` Maximum number of iterations in localization.
* ``THRPRINT`` When printing the orbital composition summary, do not list centers with less than this many electrons explicitly. Defaults to 0.02.
* ``IBOLOC_FACQ`` Factor for charge matrix elements in localization functional (IBO :math:`\rightarrow` localize charge). Defaults to 1.0
* ``IBOLOC_FACF`` Factor for Fock matrix elements in localization functional (IBO :math:`\rightarrow` localize band energy). Defaults to 0.0. Adding a small value here might help in situations with very high symmetry (e.g., in diatomics) and in the presence of multiple orbitals with exact 2.0 partial charges on the same center, which the regular charge criterion cannot distinguish.
* ``IBTYPE`` Method to use for making pre-orthogonal IAOs:

1: :math:`\vert\mathrm{IAO}\rangle=(1+o-\tilde o)P_{12}\vert\mathrm{minao}\rangle`
2: :math:`\vert\mathrm{IAO}\rangle=(o {\tilde o}+(1-o)(1-\tilde o))P_{12}\vert\mathrm{minao}\rangle`
Both are described in the IAO article. In practice both produce indistinguishable results.

Additionally to the options, the following directives are supported:

* ``SAVE`` Defines the record on which the output orbitals are saved
* ``FREEZECORE`` If used, core orbitals are excluded from the localization. (e.g., ``{ibba; freezecore}``). Freezing core orbitals is recommended if subsequent correlation calculations are intended to be performed. It is the default behavior of the other orbital localization programs called via ``locali``, but not of ``ibba``, since ``ibba`` is not primarily a orbital localization program.
* ``ROTATE`` Defines rotation operations to perform on the input orbitals before localization. See SCF program for reference
* ``CORE`` Defines the number of core orbitals
* ``CLOSED`` Defines the number of closed-shell orbitals (including core orbitals)
* ``OCC`` Defines the number of active orbitals. Active orbitals which are not closed are assumed to be singly occupied with alpha spin.
* ``LOCCORE`` See `selecting orbital space <orbital_localization.html#selecting-the-orbital-space>`__.
