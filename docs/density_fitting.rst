.. raw:: html

   <span id="options-for-density-fitting"></span>

.. _density_fitting--density-fitting:

Density fitting
===============

Density fitting can be used to approximate the integrals in spin restricted Hartree-Fock (``HF``), density functional theory (``KS``), second-order Møller-Plesset perturbation theory (``MP2`` and ``RMP2``), explicitly correlated MP2 (MP2-F12), all levels of closed-shell local correlation methods (``LCC2``, ``LMP2``-``LMP4``, ``LQCISD(T)``, ``LCCSD(T)``), as well as for ``CASSCF`` and ``CASPT2`` methods. Density fitting is invoked by adding the prefix ``DF-`` to the command name, e.g. ``DF-HF``, ``DF-KS``, ``DF-MP2`` and so on. Gradients are available for ``DF-HF``, ``DF-KS``, ``DF-MP2``, ``DF-LMP2``, ``DF-CASSCF``, and ``DF-CASPT2``. Symmetry is implemented for energy calculations (without gradients) for ``DF-RHF``, ``DF-RKS``,\ ``DF-UHF``, ``DF-UKS`` ``DF-RMP2``,\ ``DF-RMP2-F12``, ``DF-CASSCF|DF-MULTI``, ``DF-NEVPT2``, ``DF-CASPT2|DF-RS2``, and ``DF-RS2C``, but for ``DF-MP2``, ``DF-CCSD`` (and variants) as well as for local methods symmetry is not implemented and automatically turned off.

By default, a fitting basis set will be chosen automatically that corresponds to the current orbital basis set and is appropriate for the method. For instance, if the orbital basis set is ``VTZ``, the default fitting basis is ``VTZ/JKFIT`` for ``DF-HF`` or ``DF-KS``, and ``VTZ/MP2FIT`` for ``DF-MP2``. Other fitting basis sets from the library can be chosen using the ``DF_BASIS`` option, e.g.

.. code-block:: text

   BASIS=VTZ             !use VTZ orbital basis
   DF-HF,DF_BASIS=VQZ    !use VQZ/JKFIT fitting basis
   DF-MP2,DF_BASIS=VQZ   !use VQZ/MP2FIT fitting basis

The program then chooses automatically the set which is appropriate for the method. Optionally, the basis type can be appended to the basis name and then this supercedes the default, e.g.

.. code-block:: text

   DF-HF,DF_BASIS=VQZ/JKFIT    !use VQZ/JKFIT fitting basis

Orbital basis sets can be chosen using type ``ORBITAL`` (but this is not recommended normally!). Contraction/uncontraction can be forced appending (CONTRACT) or (UNCONTRACT) to the basis name, e.g.
``DF_BASIS=AVQZ(UNCONTRACT)/ORBITAL.\\``
If other options are given in parenthesis, these can be separated by commas, e.g.
``DF_BASIS=AVQZ(f/d,UNCONTRACT)/ORBITAL.\\``
Alternative forms, which should work as well, are
``DF_BASIS=AVQZ(f/d)(UNCONTRACT)/ORBITAL\\``
or
``DF_BASIS=AVQZ(f/d)/ORBITAL(UNCONTRACT).\\``
Note that the CONTRACT/UNCONTRACT option cannot be used with basis set names previously defined in a basis block (see below).

Alternatively, fitting basis sets can be defined in a preceding basis block (see :doc:`basis input <basis_input>`), and then be referred to with their set names, e.g.,

``DF-HF, DF_BASIS=MYJKBASIS\\``
``DF-MP2, DF_BASIS=MYMP2BASIS``

where ``MYJKBASIS`` and ``MYMP2BASIS`` are sets defined in a basis block. In this case it is the responsibility of the user to ensure that the basis set is appropriate for the method.

Further options, as fully described in section `options for density fitting <density_fitting.html#options-for-density-fitting>`__, can be added on the command line. In this case they are valid only for the current command. Alternatively, the options can be specified on a separate ``DFIT`` directive. If this is given within a command block, the options are used only for the current program; this is entirely equivalent to the case that the options are specified on the command line. However, if a ``DFIT`` (or ``GDFIT``) directive is given outside of a command block, the specified options are used globally in all subsequent density fitting calculations in the same run.

The options specified on a global ``DFIT`` directive are also passed down to procedures. However, if a ``DFIT`` is given within a procedure, the corresponding options are used only in the same procedure and procedures called from it. When the procedure terminates, the options from the previous level are recovered.

.. _density_fitting--options-for-density-fitting:

Options for density fitting
===========================

The options described in this section have sensible default values and usually do not have to be given. Many options described below have alias names. These can be obtained using

``HELP,CFIT,ALIASES.``

.. _density_fitting--options-to-select-the-fitting-basis-sets:

Options to select the fitting basis sets
========================================

* ``BASIS`` Basis set for fitting (Default: set corresponding to the orbital basis)
* ``BASIS_COUL`` Basis set for Coulomb fitting (default ``BASIS``)
* ``BASIS_EXCH`` Basis set for exchange fitting (default ``BASIS``)
* ``BASIS_MP2`` Fitting basis set for DF-MP2 (default ``BASIS``)
* ``BASIS_CCSD`` Fitting basis set for DF-LCCSD (default ``BASIS``)

.. _density_fitting--screening-thresholds:

Screening thresholds
====================

* ``THRAO`` Threshold for neglecting contracted 3-index integrals in the AO basis (default 1.d-8).
* ``THRMO`` Threshold for neglecting half-transformed 3-index integrals (default 1.d-8).
* ``THRSW`` Threshold for Schwarz screening (default 1.d-5).
* ``THROV`` Threshold for neglecting 2-index integrals in the AO (default 1.d-10.
* ``THRPROD`` Product screening threshold for first half transformation (default 1.d-8).

Analogous thresholds for specific programs can be set by appending the above keywords by the following specifications

* ``_SCF`` Coulomb and exchange fitting in DF-HF/DF-KS
* ``_COUL`` Coulomb fitting in DF-HF/DF-KS
* ``_EXCH`` Exchange fitting in DF-HF/DF-KS
* ``_CPHF`` Coulomb and exchange fitting in CPHF
* ``_SCFGRD`` Coulomb and exchange fitting in DF-HF/DF-KS gradients

The default values are the same as for the general thresholds.

Further thresholds:

* ``THR2HLF`` Threshold for second-half transformation in exchange fitting (default ``THRAO_SCF``)
* ``THRASM_SCF`` Threshold for local assembly of exchange matrix (default ``THRAO_SCF``)
* ``THRAO_FOCK`` Threshold for Coulomb fitting in DF-KS

``(default MIN(THRAO_SCF*1.d-2,1.d-12))``

.. _density_fitting--parameters-to-enable-local-fitting:

Parameters to enable local fitting
==================================

Local fitting as described in H.-J. Werner, F. R. Manby, and P. J. Knowles, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.1564816>`__ **118**, 8149 (2003), Polly, H.-J. Werner, F. R. Manby, and Peter J. Knowles, `Mol. Phys. <https://dx.doi.org/10.1080/0026897042000274801>`__ **102**, 2311 (2004), and M. Schütz, H.-J. Werner, R. Lindh and F. R. Manby, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.1760747>`__ **121**, 737 (2004) can be activated by setting ``LOCFIT=1``. By default, local fitting is disabled, because under certain circumstances it can lead to unacceptable errors. For instance, local fitting must not be used in counter-poise calculations, since the lack of fitting functions at the dummy atoms can lead to wrong results.

Local fitting can be restricted to certain programs, using the following options:

* ``LOCFIT`` If positive, use local fitting in all programs in which it is available (default 0).
* ``LOCFIT_SCF`` If positive, use local fitting in SCF (default ``LOCFIT``)
* ``LOCFIT_MP2`` If positive, use local fitting in DF-LMP2; 1: use orbital domains; 2: use pair domains (default ``LOCFIT``)
* ``LOCFIT_F12`` If positive, use local fitting in DF-LMP2-F12 (default ``LOCFIT``)
* ``LOCFIT_CCSD`` If positive, use local fitting in DF-LCCSD (default ``LOCFIT``)
* ``LOCFIT_2EXT`` If positive, use local fitting in LCCSD 2ext transformation (default ``LOCFIT_CCSD``)
* ``LOCFIT_3EXT`` If positive, use local fitting in LCCSD 3ext transformation (default ``LOCFIT_CCSD``)
* ``LOCFIT_4EXT`` If positive, use local fitting in LCCSD 4ext transformation (default ``LOCFIT_CCSD``)
* ``LOCFIT_CPHF`` If positive, use local fitting in CPHF (default ``LOCFIT``)
* ``LOCFIT_SCFGRD`` If positive, use local fitting in gradient calculations (default ``LOCFIT``)
* ``LOCORB`` If positive, use localized orbitals in DF-HF (default 1)
* ``LOCTRA`` If positive, use local screening in first half transformation (default ``LOCFIT``).
* ``DSCREEN`` If positive, enable density screening in LMP2 (default 0)
* ``KSCREEN`` If positive, enable fit-basis Schwarz screening in LMP2 (default depends on ``LOCTRA``).

.. _density_fitting--parameters-for-fitting-domains:

Parameters for fitting domains
==============================

The following options can be used to modify the domains used in local fitting. These parameters only have an effect if ``LOCFIT``\ =1. The local fitting domains are determined in two steps: first *primary* orbital domains are determined. In the LMP2 and LCCSD programs, the primary orbital domains are the same as used for excitation domains and determined by the Boughton-Pulay procedure, as described in Sect. :doc:`PAO-based local correlation treatments <pao-based_local_correlation_treatments>`. Depending on the value of ``FITDOM_MP2`` or ``FITDOM_CCSD`` for LMP2 and LCCSD, respectively, either the orbital domains are used directly or united pair domains are generated. In DF-HF the primary orbital domains include all basis functions at atoms which have Löwdin charges greater or equal to ``THRCHG_SCF``. In the second step the primary fitting domains are extended using either distance criteria (``RDOMAUX``, in bohr) or bond connectivity criteria (``IDOMAUX``). ``IDOMAUX``\ =1 means to include all functions at atoms which are at most one bond distant from the primary domains. By default, distance criteria are used. However, if ``IDOMAUX``.ge.0, the distance criteria are ignored and connectivity is used.

* ``THRCHG_SCF`` Parameter to select the primary orbital domains in local exchange fitting (default 0.1). All atoms are included which have Löwdin charges greater than this value. The primary domains are extended according to ``RDOMAUX_SCF`` or ``IDOMAUX_SCF``.
* ``FITDOM_MP2`` Parameter to select primary fitting domains in LMP2 transformation (default 3). 1: use orbital domains; 2: use united orbital domains of strong pairs; 3: use united orbital domains of strong and weak pairs (default 3). The primary domains are extended according to ``RDOMAUX_MP2`` or ``IDOMAUX_MP2``
* ``FITDOM_CCSD`` Similar to ``FITDOM_MP2`` but used for LCCSD 2-ext transformation.
* ``RDOMAUX_SCF`` Distance criterion for fitting domain extension in SCF (default 5.0)
* ``IDOMAUX_SCF`` Connectivity criterion for fitting domain extension in SCF (default 0)
* ``RDOMAUX_CORE`` Distance criterion for core orbital fitting domain extension in SCF (default ``RDOMAUX_SCF``).
* ``IDOMAUX_CORE`` Connectivity criterion for core orbital fitting domain extension in SCF (default ``IDOMAUX_SCF``).
* ``RDOMSCF_START`` Distance criterion for fitting domain extension in the initial SCF iterations (default 3.0).
* ``IDOMSCF_START`` Connectivity criterion for fitting domain extension in the initial SCF iterations (default 1).
* ``RDOMSCF_FINAL`` Distance criterion for fitting domain extension in the final SCF iterations (default ``RDOMAUX_SCF``).
* ``IDOMSCF_FINAL`` Connectivity criterion for fitting domain extension in the final SCF iterations (default ``IDOMAUX_SCF``).
* ``RDOMAUX_MP2`` Distance criterion for fitting domain extension in LMP2. The default value depends on ``FITDOM_MP2``
* ``IDOMAUX_MP2`` Connectivity criterion for fitting domain extension in LMP2. The default value depends on ``FITDOM_MP2``
* ``RDOMAUX_CCSD`` Distance criterion for fitting domain extension in LCCSD. The default value depends on ``FITDOM_CCSD``).
* ``IDOMAUX_CCSD`` Connectivity criterion for fitting domain extension in LCCSD. The default value depends on ``FITDOM_CCSD``.
* ``RDOMAUX_CPHF`` Distance criterion for fitting domain extension in CPHF (default 3.0).
* ``RDOMAUX_SCFGRD`` Distance criterion for fitting domain extension in gradients (default 5.0).
* ``SCSGRD`` Switches the DF-LMP2 analytic gradient to Grimme's SCS scaled MP2 energy functional (default 0).

.. _density_fitting--miscellaneous-control-options:

Miscellaneous control options
=============================

There is a rather large number of parameters. Many of these should normally not be changed, and therefore only a subset is described here. A full list can be obtained using

``HELP,CFIT``
