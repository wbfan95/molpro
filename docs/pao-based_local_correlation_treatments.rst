.. raw:: html

   <span id="correlating-subsets-of-electrons-region"></span>

.. raw:: html

   <span id="density-fitted-lmp2-df-lmp2-ldcsd-df-ldcsd-and-coupled-cluster-df-lccsd-t0"></span>

.. raw:: html

   <span id="doing-it-right"></span>

.. raw:: html

   <span id="domain-merging-mergedom"></span>

.. raw:: html

   <span id="extended-domains"></span>

.. raw:: html

   <span id="general-options"></span>

.. raw:: html

   <span id="gradients-and-frequency-calculations"></span>

.. raw:: html

   <span id="intermolecular-interactions"></span>

.. raw:: html

   <span id="localization"></span>

.. raw:: html

   <span id="options-for-selection-of-domains"></span>

.. raw:: html

   <span id="options-for-selection-of-pair-classes"></span>

.. raw:: html

   <span id="orbital-domains"></span>

.. raw:: html

   <span id="restarting-a-calculation-start"></span>

.. raw:: html

   <span id="saving-the-wavefunction-save"></span>

.. raw:: html

   <span id="summary-of-options"></span>

.. _pao-based_local_correlation_treatments--pao-based-local-correlation-treatments:

PAO-based local correlation treatments
======================================

.. _pao-based_local_correlation_treatments--introduction:

Introduction
============

In this section the original PAO-based local correlation methods are described. Since Molpro version 2018, a completely new PNO-LCCSD(T)-F12 program is available, which is much more accurate and well parallelized. It is recommended to use this new program, which is described in section :doc:`local correlation methods with pair natural orbitals (PNOs) <local_correlation_methods_with_pair_natural_orbitals_pnos>`.

The PAO based local correlation program of Molpro can currently perform closed-shell LMP2, LMP3, LMP4(SDTQ), LCISD, LDCSD, LQCISD(T), and LCCSD(T) calculations. For large molecules, all methods scale linearly with molecular size, provided very distant pairs are neglected, and the integral-direct algorithms are used.

Much higher efficiency is achieved by using density fitting (DF) approximations to compute the integrals. Density fitting is available for all local methods up to LCCSD(T), as well as for analytical LMP2 gradients. Only iterative triples methods like LCCSDT-1b can currently not be done with density fitting.

The errors introduced by DF are negligible, and the use of the DF methods is highly recommended. Linear scaling can be obtained in DF-LMP2 using the ``LOCFIT`` option (see Ref. 11); in DF-LCCSD(T), the most important parts also scale linearly, but some transformation steps scale quadratically.

Energy gradients are available for LMP2, DF-LMP2, DF-SCS-LMP2, and LQCISD (in the latter case only for ``LOCAL=1``, i.e. the local calculation is simulated using the canonical program, and savings only result from the reduced number of pairs).

Local explicitly correlated methods (DF-LMP2-R12 and DF-LMP2-F12, DF-LCCSD(T)-F12 are described in section :doc:`explicitly correlated methods <explicitly_correlated_methods>`.

Before using these methods, it is strongly recommended to read the literature in order to understand the basic concepts and approximations. A recent review [1] and Ref. [2] may be suitable for an introduction.

References:

**Review**:
:math:`[1]` H.-J. Werner and K. Pflüger, *On the selection of domains and orbital pairs in local correlation treatments*, `Ann. Rep. Comp. Chem. <https://doi.org/10.1016/S1574-1400(06)02004-4>`__ **2**, 53 (2006).

**General local Coupled Cluster:**
:math:`[2]` C. Hampel and H.-J. Werner, *Local Treatment of electron correlation in coupled cluster (CCSD) theory*, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.471289>`__ **104**, 6286 (1996).
:math:`[3]` M. Schütz and H.-J. Werner, *Local perturbative triples correction (T) with linear cost scaling*, `Chem. Phys. Lett. <https://dx.doi.org/10.1016/S0009-2614(00)00066-X>`__ **318**, 370 (2000).
:math:`[4]` M. Schütz, *Low-order scaling local electron correlation methods. III. Linear scaling local perturbative triples correction (T)*, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.1323265>`__ **113**, 9986 (2000).
:math:`[5]` M. Schütz and H.-J. Werner, *Low-order scaling local electron correlation methods. IV. Linear scaling local coupled-cluster (LCCSD)*, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.1330207>`__ **114**, 661 (2001).
:math:`[6]` M. Schütz, *Low-order scaling local electron correlation methods. V. Connected Triples beyond (T): Linear scaling local CCSDT-1b*, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.1470497>`__ **116**, 8772 (2002).
:math:`[7]` M. Schütz, *A new, fast, semi-direct implementation of Linear Scaling Local Coupled Cluster Theory*, `Phys. Chem. Chem. Phys. <https://dx.doi.org/10.1039/B203994J>`__ **4**, 3941 (2002).

**Multipole treatment of distant pairs:**
:math:`[8]` G. Hetzer, P. Pulay, H.-J. Werner, *Multipole approximation of distant pair energies in local MP2 calculations*, `Chem. Phys. Lett. <https://dx.doi.org/10.1016/S0009-2614(98)00491-6>`__ **290**, 143 (1998).

**Linear scaling local MP2:**
:math:`[9]` M. Schütz, G. Hetzer and H.-J. Werner, *Low-order scaling local electron correlation methods. I. Linear scaling local MP2*, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.479957>`__ **111**, 5691 (1999).
:math:`[10]` G. Hetzer, M. Schütz, H. Stoll, and H.-J. Werner, *Low-order scaling local electron correlation methods II: Splitting the Coulomb operator in linear scaling local MP2*, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.1321295>`__ **113**, 9443 (2000).

**Density fitted local methods:**
:math:`[11]` H.-J. Werner, F. R. Manby, and P. J. Knowles, *Fast linear scaling second-order Møller-Plesset perturbation theory (MP2) using local and density fitting approximations*, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.1564816>`__ **118**, 8149 (2003). :math:`[12]` M. Schütz and F.R. Manby, *Linear scaling local coupled cluster theory with density fitting. Part I: 4- external integrals*, `Phys. Chem. Chem. Phys. <https://dx.doi.org/10.1039/B304550A>`__ **5**, 3349 (2003).
:math:`[13]` Polly, H.-J. Werner, F. R. Manby, and Peter J. Knowles, *Fast Hartree-Fock theory using local density fitting approximations*, `Mol. Phys. <https://dx.doi.org/10.1080/0026897042000274801>`__ **102**, 2311 (2004).
:math:`[14]` H.-J. Werner and M. Schütz, *Low-order scaling coupled cluster methods (LCCSD(T)) with local density fitting approximations*, in preparation.

**LMP2 Gradients and geometry optimization:**
:math:`[15]` A. El Azhary, G. Rauhut, P. Pulay and H.-J. Werner, *Analytical energy gradients for local second-order Møller-Plesset perturbation theory*, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.475955>`__ **108**, 5185 (1998).
:math:`[16]` G. Rauhut and H.-J. Werner, *Analytical Energy Gradients for Local Coupled-Cluster Methods*, `Phys. Chem. Chem. Phys. <https://dx.doi.org/10.1039/B105126C>`__ **3**, 4853 (2001).
:math:`[17]` M. Schütz, H.-J. Werner, R. Lindh and F.R. Manby, *Analytical energy gradients for local second-order Møller-Plesset perturbation theory using density fitting approximations*, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.1760747>`__ **121**, 737 (2004).

**LMP2 vibrational frequencies:**
:math:`[18]` G. Rauhut, A. El Azhary, F. Eckert, U. Schumann and H.-J. Werner,  *Impact of Local Approximations on MP2 Vibrational Frequencies*, Spectrochimica Acta **55**, 651 (1999).
:math:`[19]` G. Rauhut and H.-J. Werner *The vibrational spectra of furoxan and dichlorofuroxan: a comparative theoretical study using density functional theory and Local Electron Correlation Methods*, `Phys. Chem. Chem. Phys. <https://dx.doi.org/10.1039/B212590K>`__ **5**, 2001 (2003).
:math:`[20]` T. Hrenar, G. Rauhut and H.-J. Werner, *Impact of local and density fitting approximations on harmonic vibrational frequencies*, J. Phys. Chem. A., **110**, 2060 (2006).

**Intermolecular interactions and the BSSE problem:**
:math:`[21]` M. Schütz, G. Rauhut and H.-J. Werner, *Local Treatment of Electron Correlation in Molecular Clusters: Structures and Stabilities of (H:math:`_2`O):math:`_n`, :math:`n=2-4`*, J. Phys. Chem. **102**, 5997 (1998). See also [2] and references therein.
:math:`[22]` N. Runeberg, M. Schütz and H.-J. Werner, *The aurophilic attraction as interpreted by local correlation methods*, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.478665>`__ **110**, 7210 (1999).
:math:`[23]` L. Magnko, M. Schweizer, G. Rauhut, M. Schütz, H. Stoll, and H.-J. Werner, *A Comparison of the metallophilic attraction in (X-M-PH:math:`_3`):math:`_2` (M=Cu, Ag, Au; X=H, Cl)*, `Phys. Chem. Chem. Phys. <https://dx.doi.org/10.1039/B110624D>`__ **4**, 1006 (2002).

**Improved treatment of intermolecular pairs in local coupled cluster methods (beyond LMP2):**
:math:`[24]` O. Masur, D. Usvyat and M. Schütz *Efficient and accurate treatment of weak pairs in local CCSD(T) calculations*, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.4826534>`__ **139**, 164116 (2013).
:math:`[25]` M. Schütz, O. Masur and D. Usvyat *Efficient and accurate treatment of weak pairs in local CCSD(T) calculations. II. Beyond the ring approximation*, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.4884156>`__ **140**, 244107 (2014).

.. _pao-based_local_correlation_treatments--getting-started:

Getting started
===============

The local correlation treatment is switched on by preceding the command name by an ``L``, i.e., by using the ``LMP2``, ``LMP3``, ``LMP4``, ``LQCISD``, ``LCCSD``, ``LDCSD``, or ``LCISD`` commands.

The ``LQCISD`` and ``LCCSD`` commands can be appended by a specification for the perturbative treatment of triple excitations (e.g., ``LCCSD(T0)``):

* ``(T)`` Use the default triples method. Currently this is T0.
* ``(T0)`` Non-iterative local triples. This is the fastest triples option. It is usually sufficiently accurate and recommended to be used in most cases.
* ``(T1)`` T0 plus one perturbative update of the triples amplitudes. If the accuracy of T0 is insufficient (very rarely the case!), this can be used to improve the accuracy. The computational cost is at least twice as large as for T0. In contrast to T0, the triples amplitudes must be stored on disk, which can be a bottleneck in calculations for large molecules. Also the memory requirements are substantially larger than for T0.
* ``(T1C)`` As T1, but a caching algorithm is used which avoids the simultaneous storage of all triples amplitudes on disk (as is the case for ``(T1)`` or ``(TF)``). Hence, T1C requires less disk space but more CPU-time than T1. The more disk space is made available for the caching algorithm (using the T1DISK option on the local card, see below), the less CPU time is used.
* ``(TF)`` Full iterative triples calculation. With full domains and without weak pair approximations this gives the same result as a canonical (T) calculation. Typically, 3-5 iterations are needed, and therefore the computational effort is 2-3 times larger than for (T1). The disk and memory requirements are the same as for T1. The T0 energy is also computed and printed. ``TFULL`` and ``FULL`` are aliases for ``TF``.
* ``(TA)`` As TF, but the T1 energy is also computed. Since the first iteration is different for T1, the convergence of the triples iterations is slightly different with TF and TA (TF being somewhat faster in most cases). ``TALL`` and ``ALL`` are aliases for ``TA``.

Density fitting can be invoked by prepending the command name by ``DF-``, e.g. ``DF-LMP2``, ``DF-LCCSD(T0)`` etc. In density fitting calculations an additional auxiliary basis set is needed. Details about choosing such basis sets and other options for density fitting are described in sections `Density-fitted LMP2 (DF-LMP2), LDCSD (DF-LDCSD), and coupled cluster (DF-LCCSD(T0)) <pao-based_local_correlation_treatments.html#density-fitted-lmp2-df-lmp2-ldcsd-df-ldcsd-and-coupled-cluster-df-lccsd-t0>`__ and :doc:`density fitting <density_fitting>`.

The general input for local coupled LMP2 or coupled cluster calculations is:

* **``LMP2``,\ *options*** Local MP2 calculation
* **``LCCSD``,\ *options*** Local CCSD calculation
* **``LDCSD``,\ *options*** Local DCSD calculation
* **``LCCSD(T0)``,\ *options*** Local CCSD(T0) calculation

The same options as on the command line can also be given on subsequent ``LOCAL`` and ``MULTP`` directives. Instead of using the ``MULTP`` directive, the ``MULTP`` option on the command line can also be used.

In the following, we will first give a summary of all options and directives. These will be described in more detail in the subsequent sections. For new users it is recommended to read section `doing it right <pao-based_local_correlation_treatments.html#doing-it-right>`__ at the end of this chapter before starting calculations.

.. _pao-based_local_correlation_treatments--summary-of-options:

Summary of options
==================

Many options can be specified on the command line. For all options appropriate default values are set, and so these options must usually be modified only for special purposes. For convenience and historical reasons, alias names are available for various options, which often correspond to the variable name used in the program. The following table summarizes the options, aliases and default values. In the following, the parameters will be described in more detail.

.. list-table::
   :header-rows: 2

   * - Summary of ``local`` (``multp``) options and their default values
     - 
     - 
     - 
   * - Parameter
     - Alias
     - Default value
     - Meaning
   * - *General Parameters*
     - 
     - 
     - 
   * - ``LOCAL``
     - 
     - 4
     - determines which program to use.
   * - ``MULTP``
     - 
     - 0
     - turns on multipole approximations for distant pairs.
   * - ``SAVEDOM``
     - ``SAVE``
     - 0
     - specifies record for saving domain info.
   * - ``RESTDOM``
     - ``START``
     - 0
     - specifies record for reading domain info.
   * - ``LOCORB``
     - 
     - 0
     - activates or deactivates orbital localization.
   * - ``LOC_METHOD``
     - 
     - 
     - specifies which localization method to use.
   * - ``CANONICAL``
     - 
     - 0
     - allows to use canonical virtual orbitals (for testing).
   * - ``PMDEL``
     - ``CPLDEL``
     - 0
     - discards contributions of diffuse functions in PM localization.
   * - ``SAVORB``
     - ``SAVLOC``
     - 0
     - specifies record for saving local orbitals.
   * - ``DOMONLY``
     - 
     - 0
     - if 1, only domains are made. if 2, only orbital domains are made.
   * - *Parameters to define domains*
     - 
     - 
     - 
   * - ``THRBP``
     - ``DOMSEL``
     - 0.98
     - Boughton-Pulay selection criterion for orbital domains.
   * - ``NPASEL``
     - 
     - 0
     - charge used in the NPA selection criterion for orbital domains.
   * - ``CHGMIN``
     - 
     - 0.01
     - determines the minimum allowed atomic charge in domains.
   * - ``CHGMINH``
     - 
     - 0.03
     - as ``CHGMIN``, but used for H-atoms (default 0.03).
   * - ``CHGMAX``
     - 
     - 0.40
     - If the atomic charge is larger than this value, the atom is always included in the domain.
   * - ``MAXANG``
     - ``MAXL``
     - 99
     - angular momentum restriction for BP domain selection
   * - ``MAXBP``
     - 
     - 0
     - determines how atoms are ranked in BP procedure.
   * - ``MULLIKEN``
     - ``LOCMUL``
     - 0
     - determines the method to determine atomic charges.
   * - ``MERGEDOM``
     - 
     - 0
     - merges overlapping domains.
   * - ``DELCOR``
     - ``IDLCOR``
     - 2
     - delete projected core AOs up to certain shell.
   * - ``DELBAS``
     - ``IBASO``
     - 0
     - determines how to remove redundancies.
   * - *Distance criteria for domain extensions*
     - 
     - 
     - 
   * - ``REXT``
     - 
     - 0
     - criterion for all pair domains.
   * - ``REXTS``
     - 
     - 0
     - criterion for strong pair domains.
   * - ``REXTC``
     - 
     - 0
     - criterion for strong and close pair domains.
   * - ``REXTW``
     - 
     - 0
     - criterion for strong, close, and weak pair domains.
   * - *Connectivity criteria for domain extensions*
     - 
     - 
     - 
   * - ``IEXT``
     - 
     - 0
     - criterion for all pair domains.
   * - ``IEXTS``
     - 
     - 0
     - criterion for strong pair domains.
   * - ``IEXTC``
     - 
     - 0
     - criterion for strong and close pair domains.
   * - ``IEXTW``
     - 
     - 0
     - criterion for strong, close, and weak pair domains.
   * - *Parameters to select pair classes*
     - 
     - 
     - 
   * - ``USE_DIST``
     - 
     - 1
     - determines if distance of connectivity criteria are used.
   * - ``RCLOSE``
     - ``CLOSEP``
     - 1
     - distance criterion for selection of weak pairs.
   * - ``RWEAK``
     - ``WEAKP``
     - 3
     - distance criterion for selection of weak pairs.
   * - ``RDIST``
     - ``DISTP``
     - 8
     - distance criterion for selection of distant pairs.
   * - ``RVDIST``
     - ``VERYD``
     - 15
     - distance criterion for selection of very distant pairs.
   * - ``ICLOSE``
     - 
     - 1
     - connectivity criterion for selection of weak pairs.
   * - ``IWEAK``
     - 
     - 2
     - connectivity criterion for selection of weak pairs.
   * - ``IDIST``
     - 
     - 5
     - connectivity criterion for selection of distant pairs.
   * - ``IVDIST``
     - 
     - 8
     - connectivity criterion for selection of very distant pairs.
   * - ``CHGMIN_PAIRS``
     - ``CHGMINP``
     - 0.20
     - determines minimum charge of atoms used for pair classification.
   * - ``KEEPCL``
     - 
     - 0
     - determines if close pairs are included in LCCSD.
   * - *Parameter for multipole treatment of exchange operators*
     - 
     - 
     - 
   * - ``DSTMLT``
     - 
     - 3
     - multipole expansion level for distant pairs
   * - *Parameters for energy partitioning*
     - 
     - 
     - 
   * - ``IEPART``
     - 
     - 0
     - If nonzero: do energy partitioning.
   * - ``EPART``
     - 
     - 3.0
     - cutoff parameter for determining individual monomers.
   * - *Parameters for redundancy check using ``DELBAS=1`` (not recommended)*
     - 
     - 
     - 
   * - ``TYPECHECK``
     - ``TYPECHK``
     - 1
     - activates basis function type restrictions.
   * - ``DELSHL``
     - ``IDLSHL``
     - 1
     - determines if whole shells are to be deleted.
   * - ``DELEIG``
     - ``IDLEIG``
     - 1
     - determines how to select redundant functions.
   * - ``DELCMIN``
     - ``CDELMIN``
     - 0.1
     - parameter for use with ``DELEIG=1``
   * - *Parameters for choosing operator domains in LCCSD*
     - 
     - 
     - 
   * - ``OPDOM``
     - ``IOPDOM``
     - 5
     - determines how operator domains are determined for LCCSD
   * - ``RMAXJ``
     - 
     - 8
     - distance criterion for J-operator list.
   * - ``RMAXK``
     - 
     - 8
     - distance criterion for K-operator list.
   * - ``RMAXL``
     - 
     - 15
     - distance criterion for L-operator list.
   * - ``RMAX3X``
     - 
     - 5
     - distance criterion for 3-ext integral list.
   * - ``RDOMJ``
     - 
     - 0
     - distance criterion for K-operator domains.
   * - ``RDOMK``
     - 
     - 8
     - distance criterion for J-operator domains.
   * - ``IMAXJ``
     - 
     - 5
     - connectivity criterion for J-operator list.
   * - ``IMAXK``
     - 
     - 5
     - connectivity criterion for K-operator list.
   * - ``IMAXL``
     - 
     - 8
     - connectivity criterion for L-operator list.
   * - ``IMAX3X``
     - 
     - 3
     - connectivity criterion for 3-ext integral list.
   * - ``IDOMJ``
     - 
     - 0
     - connectivity criterion for K-operator domains.
   * - ``IDOMK``
     - 
     - 5
     - connectivity criterion for J-operator domains.
   * - *Miscellaneous options*
     - 
     - 
     - 
   * - ``SKIPDIST``
     - ``SKIPD``
     - 3
     - determines at which stage weak and distant pairs are eliminated
   * - ``ASYDOM``
     - ``JITERM``
     - 0
     - parameter for use of asymmetric domains
   * - ``LOCSING``
     - ``LOCSNG``
     - 0
     - determines virtual space used for singles
   * - ``PIPEKAO``
     - ``LOCAO``
     - 0
     - activates AO localization criterion
   * - ``NONORM``
     - 
     - 2
     - determines whether projected functions are normalized
   * - ``LMP2ALGO``
     - ``MP2ALGO``
     - 3
     - if nonzero, use low-order scaling method in LMP22 iterations
   * - ``OLDDEF``
     - 
     - 0
     - allows to revert to older defaults
   * - ``T1DISK``
     - 
     - 10
     - maximum disk space (in GByte) for T1 caching algorithm
   * - *Thresholds*
     - 
     - 
     - 
   * - ``THRBP``
     - 
     - 0.98
     - Threshold Boughton-Pulay method.
   * - ``THRPIP``
     - 
     - 1.d-9
     - Threshold for Pipek-Mezey or Boys localization.
   * - ``THRCPL``
     - 
     - 1.d-9
     - Threshold for coupled-perturbed localization
   * - ``THRORB``
     - 
     - 1.d-6
     - Threshold for eliminating projected orbitals with small norm.
   * - ``THRLOC``
     - 
     - 1.d-6
     - Threshold for eliminating redundant projected orbitals.
   * - ``THRCOR``
     - 
     - 1.d-1
     - Threshold for eliminating projected core orbitals.
   * - ``THRMP2``
     - 
     - 1.d-8
     - Threshold for neglecting small fock matrix elements in the LMP2 iteration.

.. _pao-based_local_correlation_treatments--summary-of-directives:

Summary of directives
=====================

The same standard directives as in the canonical programs, e.g., ``OCC``, ``CLOSED``, ``CORE``, ``WF``, ``ORBITAL`` are also valid in the local methods. In addition, there are some directives which only apply to local calculations:

* ``LOCAL`` Invokes local methods and allows to specify the same options as on the command line.
* ``MULTP`` As ``LOCAL``, but multipole approximations are used for distant pairs.
* ``DOMAIN`` Define domains manually (not recommended).
* ``MERGEDOM`` Allows to merge domains
* ``REGION`` Allows to select regions of a molecule to be treated at a certain level of theory.
* ``ENEPART`` Analysis of pair energies.
* ``SAVE`` Save domains and LCCSD amplitudes.
* ``START`` Restart with domains and LCCSD amplitudes from a previous calculation.

.. _pao-based_local_correlation_treatments--general-options:

General Options
===============

* **``LOCAL``\ =\ *local*** Determines which method is used:

``LOCAL=0: Conventional (non-local) calculation.\\``
``LOCAL=1``: Local method is simulated using canonical MOs. The local basis is used only at an intermediate stage to update the amplitudes in each iteration (only for testing).
``LOCAL=2``: Calculation is done in local basis, but without using local blocking (i.e. full matrices are used). This is the most expensive method and only for testing.
``LOCAL=3: Fully local calculation (obsolete).\\``
``LOCAL=4``: Fully local calculation (default). This is the fastest method for large molecules with many weak pairs and requires minimum memory.

* **``LOCORB``\ =\ *option*** If this option is given and *option*\ :math:`\gt 0`, the orbitals are localized using the Pipek-Mezey technique. If this option is not given or *option*\ =0 (default), the orbitals are localized unless localized orbitals are found in the orbital record (cf. ``ORBITAL`` directive and ``LOCALI`` command). In the latter case, the most recent localized orbitals are used. Setting *option*\ =-1 switches the localization off. If *option*\ :math:`\gt 1` the localized orbitals are printed. Note: Boys localization can only be performed using the ``LOCALI`` command. The program will use the Boys orbitals if they are found in the orbital record and the ``LOCORB`` option is absent or *option*\ :math:`\le 0`.
* **``LOC_METHOD``\ =\ *method*** This option allows to select between Pipek-Mezey (*method*\ =\ ``PM``) or Natural Orbitals (*method*\ =\ ``NBO``) localization. If Pipek-Mezey orbitals are requested, the default Boughton-Pulay domain selection will be used. When *method*\ =\ ``NBO``, the domain selection will be based on the NPA charges, with ``NPASEL``\ =0.03 (by default). In both cases, the domain selection parameter can be explicitly given (cf. ``DOMSEL`` and ``NPASEL`` options) in order to use another domain criterion. If localized orbitals are found in the orbital record, but the type does not coincide, the orbitals are again localized according to *method* and used in the calculation.
* **``SAVORB``\ =\ *record*** Allows the localized and projected orbitals to be saved in *record=name.ifil* for later use (e.g. plotting). The two orbital sets are stored in the same dump record and can be restored at later stages using

``ORBITAL``,\ *record*,[``TYPE``\ =]\ ``LOCAL`` or
``ORBITAL,record,[TYPE=]PROJECTED, respectively.``

* **``DOMONLY``\ =\ *value*** If *value*\ :math:`\gt 0` only domains are made, but no energy is computed. This can be used to check and save the domains for later use.
* **``DSTMLT``\ =\ *level*** Determines the expansion level of the multipole expansion of distant pairs (e.g. 1 means dipole approximation, 2 quadrupole approximation and so on). The default for ``MULTP`` is 3.
* ``INTERACT`` Automatically determine individual molecules in a calculation and set appropriate pair lists for computing interaction energies. See section `intermolecular interactions <pao-based_local_correlation_treatments.html#intermolecular-interactions>`__ for more details.
* **\*\*Parameters for energy partitioning:**\*\*
* **``IEPART``\ =\ *value*** enables/disables energy partitioning.

*iepart=0*: Energy partitioning is disabled.
*iepart=1*: Energy partitioning is enabled.
*iepart=2*: Energy partitioning is enabled. Additionally, a list of all pair energies and their components is printed.

* **``EPART``\ =\ *cutoff*** Cutoff parameter to determine individual monomers in a cluster (i.e. centre groups). Should be somewhat larger than the largest intramolecular bond length (given in a.u.).

* **\*\*Miscellaneous options:**\*\*
* **``SKIPDIST``\ =\ *skipdist*** Test-parameter. Its value should only affect the efficiency but not influence the results.

*skipdist=-1*: Weak and distant pairs are set to zero after MP2 but are not eliminated from the pair list and not skipped in any loop.
*skipdist=0*: No pairs are deleted from pair list, but weak and distant pairs are skipped in the loops were appropriate.
*skipdist=1*: Very distant pairs are neglected from the beginning. Distant pairs are eliminated after MP2.
*skipdist=2*: As skipdist=1, but also weak pairs are eliminated after MP2.
*skipdist=3*: As skipdist=2, but distant pairs are eliminated from the operator list in case of LMP2 with multipole approximations for distant pairs. This is the default.

* **``ASYDOM``\ =\ *jiterm*** Experimental test parameter. Enables the use of asymmetric domains for distant pairs. The asymmetric domain approximation supplements the multipole approximation for distant pairs, as it suppresses the treatment of configurations for which no integrals can be computed by multipole expansion. This leads to computational savings and improved numerical stability.

*jiterm=0*: Disable asymmetric domains.
*jiterm=-1*: Enable asymmetric domains (default).
*jiterm=-2*: Enable a variation of the asymmetric domain formalism: Exchange operators will initially be projected to the asymmetric domain instead of simply packed.

* **``LOCSING``\ =\ *locsing*** If *locsing.ne.0*, the single excitations use the full space, i.e., they are not treated locally. This is only works for ``LOCAL=1``.
* **``MAXANG``\ =\ *lmax*** The purpose of this experimental option is to reduce the basis set sensitivity of the Boughton-Pulay (BP) method for domain selection. Only basis functions with angular momentum up to *lmax-1* are included when computing the overlap of the approximate and exact orbitals. For example, ``MAXANG=2`` means to omit all contributions of :math:`d`, :math:`f` and higher angular momentum functions. To obtain reasonable domains, the value of ``THRBP`` must often be reduced (to 0.97 or so). This option should only be used with care!
* **``PIPEKAO``\ =\ *option*** If *option*\ :math:`\ge 0`, the orbitals are localized my maximizing the coefficients of basis functions of a given type at a given atom. Normally, this is only useful to uniquely define degenerate orbitals in atoms. For instance, when this option is used to localize the orbitals for a dimer like (Ar)\ :math:`_2` at a very long distance, clean :math:`s`, :math:`p_x`, :math:`p_y`, and :math:`p_z` atomic orbitals will be obtained. It is not recommended to use this option for molecular calculations!
* **``NONORM``\ =\ *value*** Determines if projected functions are normalized (not recommended). *value*\ =-1: projected orbitals are normalized before redundancy check.

*value*\ =0: projected orbitals are normalized after redundancy check (default).
*value*\ =1: projected orbitals are normalized in redundancy check, afterwards unnormalized.
*value*\ =2: projected orbitals are never normalized (default in gradient calculations).

* **``LMP2ALGO``\ =\ *value*** If nonzero, use low-order scaling method in LMP2 iterations. Values can be 1, 2, or 3, and 3 is usually fastest if large basis sets are used.
* **``OLDDEF``\ =\ *value*** For compatibility with older versions: if nonzero, revert to old defaults. Options set before this may be overwritten.
* **\*\*Thresholds:**\*\*
* **``THRPIP``\ =\ *thresh*** Threshold for Pipek-Mezey or Boys localization. The localization is assumed to be converged if all :math:`2 \times 2` rotation angles are smaller than *thresh*. The default is :math:`1.d-9`. It can also be modified globally using ``GTHRESH, LOCALI=``\ *thresh*.
* **``THRCPL``\ =\ *thresh*** Threshold for coupled perturbed localization (default 1.d-9). This is only needed in local gradient calculations.
* **``THRORB``\ =\ *thresh*** Threshold for eliminating functions from pair domains whose norm is smaller than *thresh* after projecting out the occupied space. The default is *throrb=1.d-6*.
* **``THRLOC``\ =\ *thresh*** Threshold for eliminating redundant basis functions from pair domains. For each eigenvalue of :math:`{\bf \tilde S}^{ij} \lt thresh` one function is deleted. The default is 1.d-6. The method used for deleting functions depends on the parameters ``IDLEIG`` and ``IBASO``.
* **``THRMP2``\ =\ *thresh*** Threshold for neglecting small fock matrix couplings in the LMP2 iterations (default 1.d-8). Specifying a larger threshold speeds up the iterations but may lead to small errors in the energy. In the initial iterations, a larger threshold is chosen automatically. It is gradually reduced to the specified final value during the iterations.
* **``THRCOR``\ =\ *thresh*** Threshold for deleting projected core orbitals. The functions are only deleted if their norm is smaller than *thresh* (default 0.1)

The thresholds can also be specified on the ``THRESH`` directive.

.. _pao-based_local_correlation_treatments--options-for-selection-of-domains:

Options for selection of domains
================================

The following sections describe the most important options which affect the domains.

.. _pao-based_local_correlation_treatments--standard-domains:

Standard domains
================

Standard domains are always determined first. They are used to define strong, close, weak, and distant pairs. More accurate results can be obtained with extended domains, as described in section `extended domains <pao-based_local_correlation_treatments.html#extended-domains>`__.

* **``THRBP``\ =\ *value*** Threshold for selecting the atoms contributing to orbital domains using the method of Boughton and Pulay (BP). As many atoms as needed to fulfill the BP criterion are included in a domain. The order in which atoms are considered depends on the parameter ``MAXBP``, see below. The default is ``THRBP=0.98``. ``THRBP=1.0`` includes all atoms into each orbital domain, i.e., leads to full domains. If no pairs are neglected, this should yield the canonical MP2 energy. The criterion is somewhat basis dependent. See section `orbital domains <pao-based_local_correlation_treatments.html#orbital-domains>`__ for recommended values of this threshold.
* **``CHGMIN``\ =\ *value*** determines the minimum allowed Mulliken (or Löwdin) charge for an atom (except H) in a domain, i.e., atoms with a smaller (absolute) charge are not included, even if the ``THRBP`` criterion is not fulfilled (default 0.01).
* **``CHGMINH``\ =\ *value*** as ``CHGMIN``, but used for H-atoms (default 0.03).
* **``CHGMAX``\ =\ *value*** If the atomic charge is larger than this value, the atom is included, independent of any ranking.
* **``MAXBP``\ =\ *maxbp*** If *maxbp=1*, the atoms are ranked according to their contribution to the Boughton-Pulay overlap. If *maxbp=0* (default), the atoms are ranked according to atomic charges. In both cases atoms with charges greater than ``CHGMAX`` are always included, and atoms with the same charges are added as groups.
* **``MULLIKEN``\ =\ *option*** Determines the method to determine atomic charges. ``MULLIKEN=0`` (default): squares of diagonal elements of :math:`{\bf S}^{\frac{1}{2}} {\bf C}` are used (Löwdin charges); ``MULLIKEN=1``: Mulliken gross charges are used. The first choice is less basis set dependent and more reliable with diffuse basis sets.
* **``MERGEDOM``\ =\ *number*** If *number* is greater than zero, all orbital domains containing *number* or more atoms in common are merged (*number=1* is treated as *number=2*, default 0). This is particularly useful for geometry optimizations of conjugated or aromatic systems like, e.g., benzene. In the latter case, ``MERGEDOM=1`` causes the generation of full :math:`\pi`-domains, i.e., the domains for all three :math:`\pi`-orbitals comprise all carbon basis functions. Note that the merged domains are generated after the above print of orbital domains, and information about merged domains is printed separately. See section `gradients and frequency calculations <pao-based_local_correlation_treatments.html#gradients-and-frequency-calculations>`__ for further discussion of geometry optimizations.

There are some other options which should normally not be modified:

This parameter determines the method for eliminating redundant functions of pair domains.
*ibaso=0*: The space of normalized eigenvectors of :math:`{\bf \tilde S}^{ij}`, which correspond to small eigenvalues, is eliminated (default). Any other value is not recommended and not further documented.

Activates elimination of basis functions corresponding to core orbitals. If *nshell=1*, only :math:`1s`-functions are eliminated from projected space. If *nshell=2* (default) :math:`1s` functions on first-row atoms, and :math:`1s`, :math:`2s`, and :math:`2p`-functions are eliminated on second-row atoms. Nothing is eliminated on H or He atoms. If effective core potentials are used, nothing is deleted at the corresponding atom. Also, functions are only deleted if the norm of the projected function is below ``THRCOR`` (default 0.1)

.. _pao-based_local_correlation_treatments--extended-domains:

Extended domains
================

There are two alternative modes for domain extensions: either *distance criteria* ``REXT``, ``REXTS``, ``REXTC``, or ``REXTW`` can be used. These are in Bohr and refer to the minimum distance between any atom in a standard orbital domain :math:`[ij]` and another atom. If an atom is found within the given distance, all PAOs at this atom are added to the domain :math:`[ij]`. Alternatively, *connectivity criteria* ``IEXT``, ``IEXTS``, ``IEXTC``, or ``IEXTW`` can be used. These refer to the number of bonds between any atom contained in the standard domain :math:`[ij]` and another atom. The advantage of distance criteria is that they select also atoms within the given radius which are not connected to the present domain by bonds. On the other hand, the connectivity criteria are independent of different bond lengths, e.g., for first and second-row atoms. Only one of the two possibilities can be used, i.e., they are mutually exclusive.

* **``REXT``\ =\ *value*** Distance criterion for extension of all pair domains.
* **``REXTS``\ =\ *value*** Distance criterion for extension of strong pair domains.
* **``REXTC``\ =\ *value*** Distance criterion for extension of strong and close pair domains.
* **``REXTW``\ =\ *value*** Distance criterion for extension of strong, close, and weak pair domains.
* **``IEXT``\ =\ *value*** Connectivity criterion for extension of all pair domains.
* **``IEXTS``\ =\ *value*** Connectivity criterion for extension of strong pair domains.
* **``IEXTC``\ =\ *value*** Connectivity criterion for extension of strong and close pair domains.
* **``IEXTW``\ =\ *value*** Connectivity criterion for extension of strong, close, and weak pair domains.

By default, domains are not extended, i.e., the default values of all parameters listed above are zero. Note that the pair classes are determined on the basis of the standard domains, and therefore domain extensions have no effect on the pair lists.

Also note that the computational effort increases with the fourth power of the domain sizes and can therefore increase quite dramatically when extending domains. This does not affect the linear scaling behaviour in the asymptotic limit.

.. _pao-based_local_correlation_treatments--manually-defining-orbital-domains-domain:

Manually Defining orbital domains (DOMAIN)
==========================================

It is possible to define the domains “by hand”, using the ``DOMAIN`` directive:

``DOMAIN,orbital,atom1, atom2 …``

where *orbital* has the form ``iorb.isym``, e.g., 3.1 for the third orbital in symmetry 1, and *atomi* are the atomic labels as given in the Z-matrix geometry input, or, alternatively, the Z-matrix row numbers. All basis functions centred at the given atoms are included into the domain. For instance

``DOMAIN,3.1,C1,C2``

defines a domain for a bicentric bond between the carbon atoms ``C1`` and ``C2``. The ``DOMAIN`` directive must be given after any ``OCC``, ``CLOSED``, or ``CORE`` directives. Note that the order of the localized orbitals depends on the localization procedure, and could even change as function of geometry, and therefore manual ``DOMAIN`` input should be used with great care. The domains of all orbitals which are not explicitly defined using ``DOMAIN`` directive are determined automatically as usual.

.. _pao-based_local_correlation_treatments--options-for-selection-of-pair-classes:

Options for selection of pair classes
-------------------------------------

There are two alternative modes for defining the pair classes: either *distance criteria* ``RCLOSE``, ``RWEAK``, ``RDIST``, ``RVDIST`` can be used. These are in Bohr and refer for a given orbital pair :math:`(ij)` to the minimum distance :math:`R^{(ij)}` between any atom in the standard orbital domains :math:`[i]` and any atom in the standard orbital domains :math:`[j]` . Alternatively, the *connectivity criteria* ``ICLOSE``, ``IWEAK``, ``IDIST``, ``IVDIST`` can be used. These refer to the minimum number of bonds between any atom contained in the standard domain :math:`[i]` and any atom contained in the standard domain :math:`[j]` The advantage of using connectivity criteria is the independence of the bond lengths, while the advantage of distance criteria (default) is that they are also effective in non-bonding situations. Only one of the two possibilities can be used, i.e., they are mutually exclusive. The use of distance criteria is the default. Using connectivity criteria for pair selection requires to set the option ``USE_DIST=0``.

* ``USE_DIST`` (default 1) If nonzero, use distance criteria, otherwise connectivity criteria.
* ``CHGMIN_PAIRS`` Only atoms in the primary domains are considered for the pair classification if the atomic Löwdin charge is larger than ``CHGMIN_PAIRS`` (default value 0.2). This criterion was introduced in order to reduce the dependence of the pair selection on localization tails.
* ``RCLOSE`` (default 1) Strong pairs are defined by :math:`0 \le R^{(ij)} \lt {\tt RCLOSE}`. Close pairs are defined by :math:`{\tt RCLOSE} \le R^{(ij)} \lt {\tt RWEAK}`.
* ``RWEAK`` (default 3) Weak pairs are defined by :math:`{\tt RWEAK} \le R^{(ij)} \lt {\tt RDIST}`.
* ``RDIST`` (default 8) Distant pairs are defined by :math:`{\tt RDIST} \le R^{(ij)} \lt {\tt RVDIST}`.
* ``RVDIST`` (default 15) Very distant pairs for which :math:`R^{(ij)} \ge`\ ``RVDIST`` are neglected.
* ``ICLOSE`` (default 1) Strong pairs are separated by less that ``ICLOSE`` bonds. Close orbital pairs are separated by at least ``ICLOSE`` bonds but less than ``IWEAK`` bonds.
* ``IWEAK`` (default 2) Weak orbital pairs are separated by at least ``IWEAK`` bonds but less than ``IDIST`` bonds.
* ``IDIST`` (default 5) Distant orbital pairs are separated by at least ``IDIST`` bonds but less than ``IVDIST`` bonds.
* ``IVDIST`` (default 8) Very distant orbital pairs (neglected) are separated by at least ``IVDIST`` bonds.
* ``KEEPCL`` (default 0) If ``KEEPCL=1``, the LMP2 amplitudes of close pairs are included in the computation of the strong pair LCCSD residuals. If ``KEEPCL=2`` all close pairs are fully included in the LCCSD (this does not affect the triples list). This option is not yet implemented as efficiently as it could, and can therefore lead to a significant increase of the CPU time.

Setting ``RCLOSE`` or ``RWEAK`` to zero means that all pairs up to the corresponding class are treated as strong pairs (``RWEAK=0`` implies ``RCLOSE=0``). For instance, ``RCLOSE``\ =0 means that strong and close pairs are fully included in the LCCSD (in this case ``KEEPCL=1`` has no effect). Note, however, that setting ``RCLOSE``\ =0 increases the length of the triples list. Setting ``RDIST=0`` means that all distant pairs are treated as weak pairs. This does not affect ``RWEAK`` and ``RCLOSE`` and has no effect unless multipole approximations are used for distant pairs. Setting ``RVDIST=0`` means that no very distant pairs are neglected. Again, this has no effect on the other distance parameters.

.. _pao-based_local_correlation_treatments--directives:

Directives
----------

.. _pao-based_local_correlation_treatments--the-local-directive:

The LOCAL directive
===================

The ``LOCAL`` directive can be used to specify options for local calculations. If this directive is inside the command block of a local calculation, the options are used only for the current calculation, and this is entirely equivalent as if they were specified on the command line. The ``LOCAL`` directive can also be given outside a command block, and in this case the options are used for all subsequent local correlation calculations in the same input.

Example:

.. code-block:: text

   DF-LMP2,THRBP=0.985

is equivalent to

.. code-block:: text

   {DF-LMP2
   LOCAL,THRBP=0.985}

In the following example the ``LOCAL`` directive is global and acts on all subsequent local calculations, i.e. both calculations will use ``THRBP=0.985``

.. code-block:: text

   LOCAL,THRBP=0.985
   DF-LMP2       !local MP2 calculation
   OPTG          !geometry optimization using the DF-LMP2 energy
   DF-LCCSD(T)   !local coupled cluster at the optimized structure.

.. _pao-based_local_correlation_treatments--the-multp-directive:

The MULTP directive
===================

The ``MULTP`` directive turns on the multipole approximations for distant pairs, as described in Ref. [8]. Further options can be given as described above for the ``LOCAL`` directive.

``LOCAL,MULTP,options``

is equivalent to

``MULTP,options``

The level of the multipole approximation can be chosen using option ``DSTMLT`` (default 3) ( 1 means dipole approximation, 2 quadrupole approximation and so on).

The multipole approximation reduces the computational cost of LMP2 calculations for very large molecules, but leads to some additional errors, see Ref. [8]. It is normally not recommended to be used in coupled-cluster calculations and should never be used for computing intermolecular forces. It can also not be used in geometry optimizations or gradient calculations.

.. _pao-based_local_correlation_treatments--saving-the-wavefunction-save:

Saving the wavefunction (SAVE)
==============================

The wavefunction can be saved for later restart using

``SAVE,record``

where *record* has the usual form, e.g., 4000.2 means record 4000 on file 2. If this directive is given, the domain information as well as the amplitudes are saved (for MPn the amplitudes are not saved). If just the domain information should be stored, the ``SAVE`` option on the ``LOCAL`` directive must be used (cf. section `summary of options <pao-based_local_correlation_treatments.html#summary-of-options>`__).

.. _pao-based_local_correlation_treatments--restarting-a-calculation-start:

Restarting a calculation (START)
================================

Local CCSD, DCSD or QCISD calculations can be restarted using

``START,record [sec:locstart]``

The record given must have been saved in a previous local calculation using the ``SAVE`` directive (otherwise this directive is ignored). If the ``START`` directive is given, the domain information as well as the amplitudes of the previous calculation are used for restart. It is possible, for instance, to start a local CCSD calculation with the amplitudes previously saved for a local QCISD calculation (but of course it is not possible to use a record saved for a non-local CCSD or QCISD calculation). If it is intended only to use the domain information but not the amplitudes for a restart, the ``START`` option on the command line or ``LOCAL`` directive must be used (cf. section `summary of options <pao-based_local_correlation_treatments.html#summary-of-options>`__).

.. _pao-based_local_correlation_treatments--correlating-subsets-of-electrons-region:

Correlating subsets of electrons (REGION)
=========================================

In large molecules, it may be sufficient to correlate only the electrons in the vicinity of an *active group*, and to treat the rest of the molecule at the SCF level. This approach can even be extended, different correlation levels may be used for different sections of the system. The ``REGION`` directive allows the specification of a subset of atoms:

``REGION,METHOD=method,[DEFAULT=default_method], [TYPE=INCLUSIVE|EXCLUSIVE], atom1, atom2 …``

The orbitals located at these atoms will be treated at the level specified in *method*. The remaining orbitals will be treated as defined in *default*. If not given by the user, the latter option will be set to ``HF``.

The orbital selection can be done in two ways. If *type* is set to ``INCLUSIVE``, any orbital containing one of the atoms in its domain centre list will be included. If type is set to ``EXCLUSIVE``, the program will only add orbitals whose domains are exclusively covered by the given atoms. Any local correlation treatment can be given as *method*, with the restriction that only ``MP2`` and ``HF`` can be used as *default_method*. Up to two ``REGION`` directives may be included in a single calculation, ordered according to the correlation level (*method*) specified for the region. The highest level region should be given last.

It is advisable to check the region orbital list and the orbital domains printed by the program. The use of regions may significantly reduce the computation time, and, provided the active atoms are sensibly chosen, may give still sufficiently accurate results for the *active group*, e.g. bond lengths and bond angles.

.. _pao-based_local_correlation_treatments--domain-merging-mergedom:

Domain Merging (MERGEDOM)
=========================

The restriction of the virtual space in local calculations may result in discontinuities for reaction path calculations due to changes of the geometry dependent domains. This may be avoided by the use of a ``MERGEDOM`` directive

``MERGEDOM,[NEIGHBOUR=value],[CENTERS=[atom1, atom2…]], [RECORD=…],CHECK``

This directive provides augmented domains, which can be saved (using option or directive ``SAVE``, see section `saving the wavefunction (SAVE) <pao-based_local_correlation_treatments.html#saving-the-wavefunction-save>`__) for later use in reaction paths or in single point calculations (in cases where the orbital domain description is unbalanced). The use of the *neighbour* option works in the same way as the local option ``MERGEDOM``, with *value* specifying the number of coincident centres. If the *centres* option is used, an atom list should be given (enclosed by square brackets). The domains of all orbitals located exclusively at these atoms will be merged, and the resulting merged domains will be used for all these orbitals.

One may also give a *record* number from a previously saved local calculation. The domain list contained in the record will be matched to the current one, and orbital domains augmented (merged) to include both sets. This domain definition should then be adequate for calculations on both points (and all those in between). This procedure can be repeated to include more geometries. In this way domains can be defined that are appropriate for a whole range of geometries (e.g. a reaction path), and if these domains are used in all calculations a strictly smooth potential energy surface is obtained.

.. _pao-based_local_correlation_treatments--energy-partitioning-for-molecular-cluster-calculations-enepart:

Energy partitioning for molecular cluster calculations (ENEPART)
================================================================

The local character of occupied and virtual orbitals in the local correlation treatment also offers the appealing possibility to decompose the intermolecular interaction energy of molecular clusters into individual contributions of different excitation classes. This allows to distinguish between intramolecular-, dispersive-, and ionic components of the correlation contribution to the interaction energy (cf. M. Schütz, G. Rauhut and H.J. Werner, J. Phys. Chem. **102**, 5197 (1998)). The energy partitioning algorithm is activated either by supplying the ``ENEPART`` directive:

``ENEPART,[epart],[iepart]``

or by giving the parameters as options on the command line.

The *epart* parameter determines the cutoff distance for (intramolecular) bond lengths (in a.u., default 3 a.u.) and is used to automatically determine the individual monomer subunits of the cluster. The *iepart* parameter enables the energy partitioning, if set to a value larger than zero (default 1). Additionally, if iepart is set to 2, a list of all intermolecular pair energies and their components is printed.

The output section produced by the energy partitioning algorithm will look similar to the following example:

.. code-block:: text

    energy partitioning enabled !
    centre groups formed for cutoff [au] = 3.00
     1   :O1  H11 H12
     2   :O2  H21 H22
    energy partitioning relative to centre groups:
    intramolecular correlation:      -.43752663
    exchange dispersion       :       .00000037
    dispersion energy         :      -.00022425
    ionic contributions       :      -.00007637

The centre groups correspond to the individual monomers determined for *epart=3*. In the present example, two water monomers were found. The correlation energy is partitioned into the four components shown above. The exchange dispersion, dispersion and ionic components reflect directly the related intermolecular components of the complex, while the intramolecular correlation contribution to the interaction energy has to be determined by a super-molecular calculation, i.e. by subtracting the (two) corresponding monomer correlation energies from the intramolecular correlation component of the complex given in the output.

Alternatively, the following form can be used:

``ENEPART,RMAX=[r1,r2,r3,…]``

and the program will then print the energy contributions of all pairs in the ranges between the given distances (in bohr, enclosed by square brackets, e.g., ``enepart,rmax=[0,3,5,7,9,11]``). A second list in which the contributions are given as a function of the number of bonds between the pair domains will also be printed.

.. _pao-based_local_correlation_treatments--split-coulomb-operator-treatment:

Split Coulomb operator treatment
--------------------------------

See :doc:`Split Coulomb operator treatment (ATTENUATE) <split_coulomb_operator_treatment_attenuate>`.

.. _pao-based_local_correlation_treatments--doing-it-right:

Doing it right
--------------

The local correlation methods in Molpro employ localized molecular orbitals (LMOs). Pipek-Mezey localization is recommended, but Boys localization is also possible. The virtual orbital space is spanned by non-orthogonal projected atomic orbitals (PAOs). The local character of this basis makes it possible to introduce two distinct approximations: first, excitations are restricted to *domains*, which are subspaces of (PAOs) that are spatially close to the orbitals from which the electrons are being excited. Secondly, the orbital pairs are classified according to their importance (based on distance or connectivity criteria), and only *strong pairs* are treated at the highest level (e.g. CCSD). The remaining *weak* and *distant* pairs are treated at the LMP2 level, and *very distant* pairs are neglected. These approximations lead to linear scaling of the computational resources as a function of the molecular size.

Naturally, such approximation can introduce some errors, and therefore the user has to be more careful than with standard black box methods. On the other hand, the low-order scaling makes it possible to treat much larger systems at high levels of theory than it was possible so far.

This section summarizes some important points to remember when performing local correlation calculations.

.. _pao-based_local_correlation_treatments--basis-sets:

Basis sets
==========

For numerical reasons, it is useful to eliminate projected core orbitals, since these may have a very small norm. By default, projected core orbitals are eliminated if their norm is smaller than 0.1 (this behaviour can be changed using the ``DELCOR`` and ``THRCOR`` options). For local calculations we recommend the use of generally contracted basis sets, e.g., the correlation consistent cc-pVnZ sets of Dunning and coworkers. For these basis sets the core basis functions are uniquely defined, and will always be eliminated if the defaults for ``DELCOR`` and ``THRCOR`` are used.

The correlation consistent basis sets are also recommended for all density fitting calculations, since optimized fitting basis sets are available for each basis.

.. _pao-based_local_correlation_treatments--symmetry-and-orientation:

Symmetry and Orientation
========================

**1. Turn off symmetry!** Otherwise, you won’t get appropriately localized orbitals (local orbitals will tend to be symmetry equivalent instead of symmetry adapted). Symmetry can be used only if all atoms are symmetry unique. This allows the local treatment of planar molecules in :math:`C_s` symmetry. But note that neither the multipole program nor the density fitting programs support symmetry at all, so choose always :math:`C_1` symmetry for DF-calculations or with the ``MULTP`` option.

To turn off symmetry, add ``NOSYM`` or ``SYMMETRY,NOSYM`` *before* the geometry block, e.g.

.. code-block:: text

   nosym
   geometry={
     O1
     H1,O1,roh
     H2,O1,roh,h1,hoh
   }

**2. Use NOORIENT!** We recommend to use the ``NOORIENT`` option in the geometry input, to avoid unintended rotations of the molecule when the geometry changes. This is particularly important for geometry optimizations and for domain restarts in calculations of interaction energies (see section `intermolecular interactions <pao-based_local_correlation_treatments.html#intermolecular-interactions>`__).

.. _pao-based_local_correlation_treatments--localization:

Localization
============

By default, Pipek-Mezey localization is used and performed automatically in the beginning of a local correlation calculation. Thus

.. code-block:: text

   df-hf        !Hartree-Fock with density fitting
   df-lmp2      !LMP2 using the Pipek-Mezey LMOs

is equivalent to

.. code-block:: text

   df-hf        !Hartree-Fock with density fitting
   locali,pipek !Orbital localization using the Pipek-Mezey criterion
   df-lmp2      !LMP2 using the Pipek-Mezey LMOs

Boys localization can be used as well, but in this case the localization must be done beforehand, e.g.

.. code-block:: text

   df-hf        !Hartree-Fock with density fitting
   locali,boys  !Orbital localization using the Boys criterion
   df-lmp2      !LMP2 using the Boys LMOs

Poor localization is sometimes an intrinsic problem, in particular for strongly conjugated systems or when diffuse basis sets are used. This is caused by localization tails due to the overlapping diffuse functions. The problem is particularly frequent in calculations of systems with short bonds, e.g., aromatic molecules. It can be avoided using directive

``PIPEK,DELETE=$n$``

with :math:`n=1` or :math:`2`. This means that the contributions of the :math:`n` most diffuse basis functions of each angular momentum type are ignored in the localization. This often yields much better localized orbitals when diffuse basis sets are used. For aug-cc-pVTZ, :math:`n=2` has been found to work very well, while for aug-cc-pVDZ :math:`n`\ =1

In rare cases it might also happen that the localization procedure does not converge. It is them possible to choose a second-order Newton-Raphson localization scheme, using the directive

``PIPEK,METHOD=2,[DELETE=$n$]``

This happens for example in LMP2 optimizations of benzene or other highly symmetric aromatics, where the Pipek-Mezey localization has redundant orbital rotations. Instead of ``PIPEK,METHOD=2`` one can also use option ``CPLSOLVE=2``.

Normally (default) one can use

``PIPEK,METHOD=3,[DELETE=$n$]``

which performs standard Pipek-Mezey iterations, which usually converge quickly.

.. _pao-based_local_correlation_treatments--orbital-domains:

Orbital domains
===============

The orbital domains are determined automatically using the procedure of Boughton and Pulay, `J. Comput. Chem. <https://dx.doi.org/10.1002/jcc.540140615>`__ **14**, 736 (1993) and `J. Chem. Phys. <https://dx.doi.org/10.1063/1.471289>`__ **104**, 6286 (1996). For higher accuracy the domains can be extended, and in this way the canonical result can be systematically approached (cf. Ref. [1] and section `extended domains <pao-based_local_correlation_treatments.html#extended-domains>`__). Details are described in section `options for selection of domains <pao-based_local_correlation_treatments.html#options-for-selection-of-domains>`__.

In most cases, the domain selection is uncritical for saturated molecules. Nevertheless, in particular for delocalized systems, it is recommended always to check the orbital domains, which are printed in the beginning of each local calculation. For such checking, the option ``DOMONLY=1`` can be used to stop the calculation after the domain generation. The orbital domains consist of all basis functions for a subset of atoms. These atoms are selected so that the domain spans the corresponding localized orbital with a preset accuracy (alterable with option ``THRBP``). A typical domain output, here for water, looks like this:

.. code-block:: text

    Orbital domains
   
      Orb.   Atom    Charge       Crit.
      2.1    1 O1     1.17        0.00
             3 H2     0.84        1.00
      3.1    1 O1     2.02        1.00
      4.1    1 O1     1.96        1.00
      5.1    1 O1     1.17        0.00
             2 H1     0.84        1.00

This tells you that the domains for orbitals 2.1 and 5.1 comprise the basis functions of the oxygen atom and and one hydrogen atom, while the domains for orbitals 3.1 and 4.1 consist of the basis function on oxygen only. The latter ones correspond to the oxygen lone pairs, the former to the two OH bonds, and so this is exactly what one would expect. For each domain of AOs, corresponding projected atomic orbitals (PAOs) are generated, which span subspaces of the virtual space and into which excitations are made. Options which affect the domain selection are described in section `options for selection of domains <pao-based_local_correlation_treatments.html#options-for-selection-of-domains>`__. Improper domains can result from poorly localized orbitals (see section `localization <pao-based_local_correlation_treatments.html#localization>`__ or a forgotten ``NOSYM`` directive. This does not only negatively affect performance and memory requirements, but can also lead to unexpected results.

The default for the selection criterion ``THRBP`` is 0.98. This works usually well for small basis sets like cc-pVDZ. For larger basis sets like cc-pVTZ we recommend to use a slightly larger value of 0.985 to ensure that enough atoms are included in each domain. For cc-pVQZ recommend ``THRBP=0.990`` is recommended. In cases of doubt, compare the domains you get with a smaller basis (e.g., cc-pVDZ).

The choice of domains usually has only a weak effect on near-equilibrium properties like equilibrium geometries and harmonic vibrational frequencies. More critical are energy differences like reaction energies or barrier heights. In cases where the electronic structure strongly changes, e.g., when the number of double bonds changes, it is recommended to compare DF-LMP2 and DF-MP2 results before performing expensive LCCSD(T) calculations. More balanced results and smooth potentials can be obtained using the ``MERGEDOM`` directive, see section `domain Merging (MERGEDOM) <pao-based_local_correlation_treatments.html#domain-merging-mergedom>`__.

.. _pao-based_local_correlation_treatments--freezing-domains:

Freezing domains
================

In order to obtain smooth potential energy surfaces, domains must be frozen. The domain information can be stored using the ``SAVE`` option and recovered using the ``START`` option. Alternatively, the ``SAVE`` and ``START`` can be used, see section `saving the wavefunction (SAVE) <pao-based_local_correlation_treatments.html#saving-the-wavefunction-save>`__. In the latter case, also the CCSD amplitudes are saved/restarted. Freezing domains is particularly important in calculations of intermolecular interactions, see section `intermolecular interactions <pao-based_local_correlation_treatments.html#intermolecular-interactions>`__. Domains that are appropriate for larger ranges of geometries, such as reaction pathways, can be generated using the ``MERGEDOM`` directive, section `domain Merging (MERGEDOM) <pao-based_local_correlation_treatments.html#domain-merging-mergedom>`__. The domains are automatically frozen in geometry optimizations and frequency calculations, see section `gradients and frequency calculations <pao-based_local_correlation_treatments.html#gradients-and-frequency-calculations>`__. Note, however, that this automatic procedure only works if a single local calculation is involved in the optimization. In case of optimizations with counterpoise correction the domains for the complex and each monomer must be frozen individually in different records using the ``SAVE`` and ``START`` directives.

.. _pao-based_local_correlation_treatments--pair-classes:

Pair Classes
============

The *strong*, *close*, *weak* and *distant* pairs are selected using distance or connectivity criteria as described in more detail in section `options for selection of pair classes <pao-based_local_correlation_treatments.html#options-for-selection-of-pair-classes>`__. *Strong* pairs are treated by CCSD, all other pairs by LMP2. In triples calculations, all orbital triples :math:`(ijk)` are included for which :math:`(ij)`, :math:`(ik)`, and :math:`(jk)` are *close pairs*. In addition, one of these pairs is restricted to be strong. The triples energy depends on the strong and close pair amplitudes. The close pair amplitudes are taken from the LMP2 calculation. Thus, increasing the distance or connectivity criteria for close and weak pairs will lead to more accurate triples energies. While for near equilibrium properties like geometries and harmonic vibrational frequencies the default values are normally appropriate, larger distance criteria are sometimes needed when computing energy differences, in particular barrier heights. In cases of doubt, ``RWEAK`` should first be increased until convergence is reached, and then ``RCLOSE`` can be varied as well. Such tests can be performed with small basis sets like cc-pVDZ, and the optimized values then be used in the final calculations with large basis sets.

.. _pao-based_local_correlation_treatments--gradients-and-frequency-calculations:

Gradients and frequency calculations
====================================

Geometry optimizations [15-17] and numerical frequency calculations [18-20] can be performed using analytical energy gradients [15-17] for local MP2. LMP2 geometry optimizations are particularly attractive for weakly bound systems, since virtually BSSE free structures are obtained (see section `intermolecular interactions <pao-based_local_correlation_treatments.html#intermolecular-interactions>`__ and Refs. [21-23]). For reasons of efficiency it is strongly advisable to use the DF-LMP2 Gradient [17] for all geometry optimizations. Setting ``SCSGRD=1`` on the ``DF-LMP2`` command or ``DFIT`` directive activates the gradient with respect to Grimme's SCS scaled MP2 energy functional (see also section DFIT). Analytical energy gradients are not yet available for the multipole approximation of distant pairs, and therefore ``MULTP`` cannot be used in geometry optimizations or frequency calculations.

In geometry optimizations, the domains are allowed to vary in the initial optimization steps. When the stepsize drops below a certain threshold (default 0.01) the domains are automatically frozen. In numerical Hessian or frequency calculations the domains are also frozen. It is therefore not necessary to include ``SAVE`` and ``START`` options.

Particular care must be taken in optimizations of highly symmetric aromatic systems, like, e.g., benzene. In :math:`D_{6h}` symmetry, the localization of the :math:`\pi`-orbitals is not unique, i.e., the localized orbitals can be rotated around the :math:`C_6` axis without changing the localization criterion. This redundancy is lost if the symmetry is slightly distorted, which can lead to sudden changes of the localized orbitals. If now the domains are kept fixed using the ``SAVE`` and ``START`` options, a large error in the energy might result. On the other hand, if the domains are not kept fixed, their size and quality might change during the optimization, again leading to spurious energy changes and divergence of the optimization.

The best way to avoid this problem is to use the ``MERGEDOM=1`` option (see section `options for selection of domains <pao-based_local_correlation_treatments.html#options-for-selection-of-domains>`__). If this option is given, the domains for the :math:`\pi` orbitals will comprise the basis functions of all six carbon atoms, and the energy will be invariant with respect to unitary transformations among the three :math:`\pi` orbitals. Note that this problem does not occur if the symmetry of the aromatic system is lowered by a substituent.

Redundant orbital rotations can also lead to convergence difficulties of the ``Pipek-Mezey`` localization. This can be overcome by using

``PIPEK,METHOD=2``

With ``METHOD=2``, the second derivatives of the localization criterion with respect to the orbital rotations is computed and diagonalized, and rotations corresponding to zero eigenvalues are eliminated. This method converges quadratically and should be used when highly symmetric aromatic systems are optimized. With ``METHOD=3`` (default) standard Pipek-Mezey method are performed.

Finally, we note that the LMP2 gradients are quite sensitive to the accuracy of the SCF convergence (as is also the case for MP2). If very accurate structures are required, or if numerical frequencies are computed from the gradients, the default SCF accuracy might be insufficient. We recommend in such cases to add an ``ACCU,14`` directive (possibly even ``ACCU,16``) after the ``HF`` command. Indicative of insufficient SCF accuracy are small positive energy changes near the end of the geometry optimization.

.. _pao-based_local_correlation_treatments--intermolecular-interactions:

Intermolecular interactions
===========================

Local methods are particularly useful for the calculation of weak intermolecular interactions since the basis set superposition error (BSSE) is largely reduced [1,13,14] and counterpoise corrections are usually not necessary (provided the BSSE of the underlying Hartree-Fock is small). However, one must be careful to define the domains properly and to include all intermolecular pairs at the highest computational level. A convenient way to define appropriate domains and pair lists is to use the option ``INTERACT=1``. If this option is given, individual molecules are identified automatically and all intermolecular pairs are automatically treated as strong pairs and included in the LCCSD. Similarly, appropriate triples lists are generated for LCCSD(T) calculations. It is required that all orbital domains are located on individual molecules. Note however that the inclusion of the intermolecular pairs strongly increases the number of strong pairs and triples, and therefore high-level calculations can become very expensive.

For calculations of interaction potentials of weakly interacting systems, the domains of the subsystems should be determined at a very large distance and saved using the ``SAVE=``\ *record* option on the ``LOCAL`` or ``MULTP`` directive, or the ``SAVE`` directive (see section `saving the wavefunction (SAVE) <pao-based_local_correlation_treatments.html#saving-the-wavefunction-save>`__). If the asymptotic energy is not needed it is sufficient to do this initial calculation using option ``DOMONLY=1``). These domains should then be reused in the subsequent calculations at all other intermolecular distances by using the ``START``\ =\ *record* option or the ``START`` directive (see section `restarting a calculation (START) <pao-based_local_correlation_treatments.html#restarting-a-calculation-start>`__). Only in this way the basis set superposition error is minimized and normally negligible (of course, this does not affect the BSSE for the SCF, and therefore the basis set should be sufficiently large to make the SCF BSSE negligible).

Usually, diffuse basis functions are important for obtaining accurate intermolecular interactions. When diffuse basis sets are used, it may happen that the Pipek-Mezey localization does not yield well localized orbitals. This problem can in most cases be overcome by using the directive

``PIPEK,DELETE=$n$``

as described in section `localization <pao-based_local_correlation_treatments.html#localization>`__

A final warning concerns local density fitting (see sections `Density-fitted LMP2 (DF-LMP2), LDCSD (DF-LDCSD), and coupled cluster (DF-LCCSD(T0)) <pao-based_local_correlation_treatments.html#density-fitted-lmp2-df-lmp2-ldcsd-df-ldcsd-and-coupled-cluster-df-lccsd-t0>`__ and :doc:`density fitting <density_fitting>`): local fitting must not be used in counterpoise calculations, since no fitting functions would be present on the dummy atoms and this can lead to large errors.

For examples and discussions of these aspects see Refs. [21-23]

.. _pao-based_local_correlation_treatments--efficient-and-accurate-treatment-of-close-pairs-in-local-ccsd-t:

Efficient and accurate treatment of close pairs in local CCSD(T)
================================================================

As discussed above, efficient LCCSD(T) calculations employ a hierarchical treatment of the LMO pairs, which are distinguished into the pair classes *strong*, *close*, *weak*, and *very distant*. Only the strong pairs are actually treated at the full coupled cluster level, while for close and weak pairs only LMP2 is used (and very distant pairs are omitted altogether). Consequently, *intermolecular pairs* in bigger molecules or clusters, which are usually not strong, are only treated at the LMP2 level, which is often poor (since van der Waals interactions are only captured at the lowest level of perturbation theory) and compromises the otherwise high accuracy of coupled cluster like LCCSD(T). By setting the keyword ``how_treatclswk`` on the ``local`` card appropriately, it is possible to treat the close pairs at a higher level than LMP2, *i.e.*,

* ``how_treatclswk=1`` local MP2
* ``how_treatclswk=2`` direct local RPA
* ``how_treatclswk=3`` local ring-CCD3
* ``how_treatclswk=4`` local ring-CCD
* ``how_treatclswk=5`` local CCD[S]-R\ :math:`^{-6}`

These methods for close pairs are discussed in detail in Refs. [24-25]. The philosophy is to include all diagrams with R\ :math:`^{-6}` decay behavior up to a certain order of perturbation theory. *E.g.*, LringCCD3 denotes local ring CCD up to third-order diagrams, and LCCD[S]-R\ :math:`^{-6}` is full local CCD with a perturbative singles correction, yet omitting all diagrams with decay behavior quicker than R\ :math:`^{-6}` (like ladder diagrams). As shown in Ref. [25], the LCCD[S]-R\ :math:`^{-6}` provides excellent intermolecular interaction energies, virtually indistinguishable from LCCSD, at a much lower cost (mainly due to the omission of ladders). We therefore recommend to use either LringCCD3 or LCCD[S]-R\ :math:`^{-6}`. Note that it is essential to couple strong and close pairs in such calculations, *i.e.*, to set ``keepcls=1`` (*vide supra*). As an example, the input segment to set all intermolecular pairs to close and treat them at the level of LCCD[S]-R\ :math:`^{-6}` is

.. code-block:: text

   local,keepcls=1,interact=1,interpair=1,how_treatclswk=5

See also the input example `h2o_dimer_lccsdhybrids.inp <media/examples/h2o_dimer_lccsdhybrids.inp>`__.

.. _pao-based_local_correlation_treatments--density-fitted-lmp2-df-lmp2-ldcsd-df-ldcsd-and-coupled-cluster-df-lccsd-t0:

Density-fitted LMP2 (DF-LMP2), LDCSD (DF-LDCSD), and coupled cluster (DF-LCCSD(T0))
-----------------------------------------------------------------------------------

[sec:locdf]

Density-fitting LMP2, LDCSD and LCCSD calculations can be performed by adding the prefix ``DF-`` to the command name. The input is as follows:

``DF-LMP2,[options]\\``
``DF-LCCSD(T),[options]``

Options for density fitting can be mixed with any options for ``LOCAL``. Options for density fitting can also be given on a ``DFIT`` directive (see section :doc:`density fitting <density_fitting>`).

The most important options for density fitting in local methods are

* **``BASIS_MP2``\ =\ *string*** Fitting basis set used in LMP2 and in LCCSD for integrals with up to 2 external orbitals. If a correlation consistent basis set is used (e.g. cc-pVTZ) the corresponding fitting basis for MP2 us used by default (cc-pVTZ/MP2FIT). Otherwise the fitting basis set must be defined in a preceding basis block (see section :doc:`basis input <basis_input>`).
* **``BASIS_CCSD``\ =\ *string*** Fitting basis set used in LCCSD for integrals over 3- and 4-external orbitals. The default is ``BASIS_MP2`` and this is usually sufficient. However, the accurate approximation of 4-external integrals in LCCSD requires larger fitting basis sets than LMP2. Therefore, in order to minimize fitting errors, it is recommended to use the next larger fitting basis, e.g., ``BASIS_CCSD=VQZ`` for orbital basis ``VTZ``.
* **``LOCFIT``\ =\ *value*:** If ``LOCFIT=1`` local fitting is enabled. This is necessary to achieve linear scaling in DF-LMP2 (see Refs. [11-14]). The errors introduced by local fitting are usually very small, but there are some exceptions. For instance, ``LOCFIT=1`` must not be used in counterpoise calculations, see section `intermolecular interactions <pao-based_local_correlation_treatments.html#intermolecular-interactions>`__) Note that for small molecules ``LOCFIT=1`` can be more expensive than ``LOCFIT=0``.

For further details and options for density fitting see section :doc:`density fitting <density_fitting>`.
