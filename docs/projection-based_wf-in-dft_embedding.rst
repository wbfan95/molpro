.. raw:: html

   <span id="density-threshold-method"></span>

.. raw:: html

   <span id="examples"></span>

.. raw:: html

   <span id="getting-started"></span>

.. raw:: html

   <span id="improved-efficiency-using-basis-set-truncation"></span>

.. raw:: html

   <span id="tt-embed-options"></span>

.. _projection-based_wf-in-dft_embedding--projection-based-wf-in-dft-embedding:

Projection-based WF-in-DFT embedding
====================================

Embedding methods allow a system to be divided into two smaller subsystems, each of which can be treated using a different level of theory. For example, in wavefunction-in-DFT (WF-in-DFT) embedding, a WF-level (e.g. HF, MP2, CCSD(T), CASSCF, etc.) calculation is performed on one subsystem, while a DFT-level calculation is performed on the other subsystem. The interactions between the two subsystems are calculated at the DFT level. The primary advantage of WF-in-DFT embedding is that it facilitates the application of an accurate, systematically improvable WF method to regions where such accuracy is required, while a more efficient DFT method is applied to the remainder of the system. The overall strategy for projection-based WF-in-DFT embedding is described as follows:

(1) A DFT calculation is performed on the full system to obtain a set of canonical molecular orbitals (MOs).

(2) The canonical orbitals are localized using a localization method such as Pipek-Mezey or intrinsic bond orbitals (IBOs).

(3) The occupied localized MOs (LMOs) are partitioned into two subsystems, labeled the active subsystem (A) and the frozen subsystem (B).

(4) The interaction potential between the two subsystems is calculated at the DFT level.

(5) A WF-level calculation is performed on the LMOs in the active subsystem, embedded in the DFT-level interaction potential produced by the electrons in the frozen subsystem (B).

Note: WF-in-DFT embedding is not implemented with symmetry.

It is possible to replace the WF-level calculation on subsystem A with a DFT-level calculation, which corresponds to DFT-in-DFT embedding. Since the interaction potential between the subsystems is calculated at the DFT level, the result of a DFT-in-DFT embedding calculation is numerically identical to the results of a DFT calculation on the full system. Similarly, it is possible to replace the DFT-level calculation with a HF-level calculation, which corresponds to WF-in-HF embedding.

Molpro implements the numerically exact projection-based WF-in-DFT embedding method for open and closed shell systems developed in the following papers:

F. R. Manby, M. Stella, J. D. Goodpaster, and T. F. Miller III, `J. Chem. Theory Comput. <https://dx.doi.org/10.1021/ct300544e>`__ **8**, 2564 (2012)

T. A. Barnes, J. D. Goodpaster, F. R. Manby, and T. F. Miller III, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.4811112>`__ **139**, 024103 (2013)

J. D. Goodpaster, T. A. Barnes, F. R. Manby, and T. F. Miller III, J. Chem. Phys., 140, 18A507 (2014)

S. J. Bennie, M. Stella, T. F. Miller III and F. R. Manby, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.4923367>`__ **143**, 024105 (2015)

S. J. R. Lee, F. Ding, F. R. Manby, T. F. Miller III, arXiv e-prints, (2019), arXiv:1903.05830

S. J. R. Lee, M. Welborn, F. R. Manby, and T. F. Miller III, Acc. Chem. Res., acs.accounts.8b00672 (2019).

All publications resulting from the use of this method must acknowledge the above.

.. _projection-based_wf-in-dft_embedding--getting-started:

Getting Started
===============

The WF-in-DFT embedding program is called by the ``EMBED`` directive. When using this directive, the user must specify which MOs are associated with the active subsystem. This can be most directly accomplished through the ``ORBS`` option:

* ``ORBS``\ =\ *[orbital1,orbital2,orbital3...]* where *orbital1* is an integer indicating that MO number *orbital1* is associated with the active subsystem. The minimum input to run using the ``ORBS`` array is: ``proc ccsdt_proc`` ``endproc`` ``{ks}`` ``{=[orbital1]}``

The KS calculation is performed on the full system. The ``EMBED`` directive indicates the beginning of an embedding calculation in which subsystem A corresponds to the single MO *orbital1*. The HF and CCSD(T) calculations are performed on subsystem A, embedded in a subsystem interaction potential calculated at the KS level.

Alternatively to setting the ``ORBS`` array, the user can instead specify the ``ATOMS`` option:

* ``ATOMS``\ =\ *[atom1,atom2,atom3...]* where *atom1* is the name of an atom from the geometry specification. (The atoms’ indices may also be supplied. However, Molpro will sometimes reorder atoms.) Any MO having a Mulliken population greater than ``CHARGE_THRESHOLD`` (see `{\tt EMBED} Options <projection-based_wf-in-dft_embedding.html#tt-embed-options>`__) on the sum of the listed atoms is associated with subsystem A. The minimum input to run using the ``ATOMS`` option is: ``proc ccsdt_proc`` ``endproc`` ``{ks}`` ``{=[atom1,...]}``

CASSCF calculations can be used as the WF method, but some care must be taken for the specification of the active space. In particular, the ``OCC``, ``CLOSED``, and ``FROZEN`` cards must be specified, and they must correspond to the number of ``OCC``, ``CLOSED``, and ``FROZEN`` orbitals within the active subsystem:

``proc multi_proc``

``endproc``

``{ks}``

``{[atom1,atom2,...]}``

.. _projection-based_wf-in-dft_embedding--options:

Options
=======

.. _projection-based_wf-in-dft_embedding--embed-options:

EMBED Options
=============

The following options may be specified on the ``EMBED`` command line:

* ``ORBS``\ =\ *[orbital1,orbital2,orbital3...]* The ORBS option is described in the section Getting Started (`getting Started <projection-based_wf-in-dft_embedding.html#getting-started>`__).
* ``ATOMS``\ =\ *[atom1,atom2,atom3...]* The ATOMS option is described in the section Getting Started (`getting Started <projection-based_wf-in-dft_embedding.html#getting-started>`__).
* ``MU``\ =value (default 1.d6) The value of the coefficient for the level shift used in the projection-based embedding calculations. The projection-based embedding method is in principle numerically exact in the limit of infinite ``MU``, but in practice very large values of ``MU`` will lead to machine-precision errors. Typically, changing ``MU`` by 1-2 orders of magnitude relative to the default value should have only negligible impact on the energy.
* ``CHARGE_THRESHOLD``\ =value (default 0.4) This option is only relevant if the ``ATOMS`` option is present. Any MO having a summed Mulliken population on atoms specified by the ``ATOMS`` option that is greater than ``CHARGE_THRESHOLD`` is associated with the active subsystem.
* ``N_ORBITALS``\ =value (default none) If the ``ATOMS`` option is present, as an alternative to defining ``CHARGE_THRESHOLD``, one can instead define ``N_ORBITALS``. In this case, the ``N_ORBITALS`` MOs with the largest summed Mulliken population on the atoms specified by the ``ATOMS`` option are associated with the active system. This can be particularly useful for ensuring that the number of MOs in the active subsystem remains constant when calculating the potential energy surface of a reaction.
* ``LOC_METHOD``\ =value (default ``IBBA``) When localized MOs are not provided to the embedding program, determines which localization method will be used to generate them. Valid options are ``IBBA`` (default), which refers to Knizia’s IBO localization method ``PM``, which refers to Pipek-Mezey localization, and ``NONE`` which tells the embedding program not to localize the provided orbitals.
* ``HIGHPROC``\ =value Name of procedure for performing the high-level calculation on subsystem A.

\* ``LOWPROC``\ =value Name of procedure for performing the low-level calculation. This is called to compute an energy correction when basis-set truncation is used (read section `improved efficiency using basis set truncation <projection-based_wf-in-dft_embedding.html#improved-efficiency-using-basis-set-truncation>`__ for more details). In this case the final energy is corrected by adding the difference between the low-level calculation in subsystem A with and without basis-set truncation, to give a total energy expression

.. math::

   E = E_{\text{WF-in-DFT}}^{\text{trunc. basis}}
       + E_{\text{DFT-in-DFT}}^{\text{whole basis}}
       - E_{\text{DFT-in-DFT}}^{\text{trunc. basis}}

It is important not to specify the number of electrons or spin state in this procedure, as this is determined automatically from the density partitioning specified through other options.

* ``ORBITAL,[record],local`` This card specifies the orbital record from which MOs corresponding to a HF-level or DFT-level calculation on the full system are read. These MOs should be localized prior to use by the embedding calculation, as shown in the following example: ``proc ccsdt_proc`` ``endproc`` ``{ks;orbital,2200.2}`` ``{ibba;orbital,2200.2;save,2200.2}`` ``{embed,highproc=ccsdt_proc,atoms=[atom1];orbital,2200.2,local}`` If this card is not present, the last calculated HF or DFT MOs are localized using the Intrinsic Basis Bonding Analysis algorithm and then employed by the embedding calculation. Thus the preceding example is equivalent to: ``proc ccsdt_proc`` ``endproc`` ``{ks}`` ``{=[atom1]}``
* ``PRINT``\ =value (default 1) Level of output. The value print=1 prints the atoms and molecular orbitals in the active region, the localized molecular orbital composition as well as the active and frozen electrons.
* ``METHOD``\ =method (default ``PROJECTOR``) Selects projection-based embedding as the default embedding method when calling the ``EMBED`` directive, which is discussed in the current section (:doc:`projection-based WF-in-DFT embedding <projection-based_wf-in-dft_embedding>`).

.. _projection-based_wf-in-dft_embedding--scf-options-related-to-embed:

SCF options related to EMBED
============================

* ``HF_COR``\ =value (default 1) By default (HF_COR=1) calculates the perturbative correction to level-shift projector. This can be turned off by specifying HF_COR=0. This option must be specified in the SCF directive and not in the EMBED directive.

.. _projection-based_wf-in-dft_embedding--density-fitting:

Density fitting
===============

Density fitting may be enabled by specifying ``DF-EMBED`` in place of the ``EMBED`` command. **It is strongly recommended that both ``EMBED`` and the mean-field calculation that preceded it be run with density fitting.**

``{df-embed,atoms=[atom1,atom2,...]}``

Further density fitting options may be supplied to the ``CFIT`` directive (see section :doc:`density fitting <density_fitting>`).

.. _projection-based_wf-in-dft_embedding--saving-orbitals-and-densities:

Saving orbitals and densities
=============================

The following options may be used to save densities and orbitals for later analysis. If AO truncation is employed (``truncate``), these densities and orbitals represent the truncated basis.

* ``SAVE_DEN_A``\ =record_name This option saves the subsystem A density to the specified record.
* ``SAVE_DEN_B``\ =record_name This option saves the subsystem B density to the specified record.
* ``SAVE_ORBS``\ =record_name This option saves all orbitals to the specified record, in the order: subsystem A orbitals, subsystem B orbitals, virtual orbitals.

.. _projection-based_wf-in-dft_embedding--improved-efficiency-using-basis-set-truncation:

Improved efficiency using basis set truncation
----------------------------------------------

By default, the calculation on the active subsystem (subsystem A) is performed using all basis functions employed by the calculation on the full system. The computational cost of a high-level WF calculation on even a small active subsystem can thus be prohibitively high if the full system is sufficiently large. This cost can be greatly reduced by performing the calculation on the active subsystem using only the basis functions that are most important for representation of the MOs associated with the active subsystem. The density threshold method is implemented to facilitate truncation of the active subsystem basis set, and this method is described in the subsections below.

.. _projection-based_wf-in-dft_embedding--density-threshold-method:

Density threshold method
========================

The density threshold truncation method requires just one parameter to be adjusted for all types of molecular system and functions that are important in the long range are automatically kept. At its low truncation limit it produces the full basis embedding answer or at high truncation it’s limit is a result constructed from just the functions on the active embedding region. Application of this method involves slightly different input options:

* ``truncate=value`` (default 0.0) The ``truncate`` option invokes the use of the density threshold method, and must always be be given with a positive number when this method is used. The ``truncate`` value is the minimum gross Mulliken population that each basis function is compared against. Environment functions with a greater gross populations than this value are grouped (according to angular momentum partners i.e px, with py and pz) and are kept. Environment functions lower than truncate are grouped and discarded from the post embedding calculation. Setting ``truncate=0.0`` is equivalent to the case in which the basis set is not truncated as all functions have a gross population greater than 0. For accurate type-in-type energies, ``truncate`` should typically be no more than 0.001, although convergence with respect to this parameter slightly varies according to the system and degree of delocalization. For example: ``proc ccsdt_proc`` ``endproc`` ``{ks;orbital,2100.2}`` ``{ibba,bonds=1;orbital,2100.2;save,2100.2}`` ``{embed,highproc=ccsdt_proc,truncate=0.001;orbital,2100.2,local}``
* ``STOREAO`` Stores the list of AO functions used for the truncated active subsystem to a record on Molpro’s file system. If this record is present it will be used as the list of AO basis functions to construct the truncated basis of the active subsystem. This option can be used to retain the same selected AO functions along a geometry scan or a reaction coordinate to ensure a smooth potential energy surface. If one were to do a dissociation reaction, it is recommended that the calculations always go from associated to dissociated in order to benefit from this option.
* ``LOWPROC``\ =value Name of procedure to be used for the type-in-type correction. More details available in the section `{\tt EMBED} Options <projection-based_wf-in-dft_embedding.html#tt-embed-options>`__.

When using this method, the following should be taken into consideration:
(1) The accuracy of this truncation method is sensitive to the size of the basis set. For this reason, it is recommended to use at least a triple-zeta basis set.
(2) It is recommended to use Knizia’s IBO localization method, which reduces the orbital tails.
(3) For accurate HF-in-HF and DFT-in-DFT results, it is recommended to use a value for ``truncate`` of less than 0.0001. This is especially important when embedding across covalent bonds.
(4) The geometry must be in Cartesian coordinates.

All publications resulting from the use of this method must acknowledge the following:

S. J. Bennie, M. Stella, T. F. Miller III and F. R. Manby, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.4923367>`__ **143**, 024105 (2015).

.. _projection-based_wf-in-dft_embedding--gradients-for-projection-based-wf-in-dft-embedding:

Gradients for Projection-based WF-in-DFT Embedding
--------------------------------------------------

Analytical nuclear gradients have been implemented for projection-based wavefunction-in-DFT (WF-in-DFT) embedding with and without density threshold truncation. The current available methods that can be used for the WF method on the active subsystem (subsystem A) are CCSD(T), CCSD, MP2, and HF. The current available methods that can be used for the low-level SCF method are LDA, GGAs, hybrid GGAs and HF. ECP gradients should also work for WF-in-DFT both with and without density threshold truncation.

**Important Notes:**

- Only closed-shell gradients are supported right now.
- Embedding gradients currently only supports Pipek-Mezey localized orbitals such that the core and valence are localized together. Therefore, when calling Pipek-Mezey localization the core option must be specified to be 0 so core and valence orbitals are localized together.
- Embedding gradients do not include the projector correction so the option ``HF_COR`` must be set to 0.
- If density threshold truncation (`density threshold method <projection-based_wf-in-dft_embedding.html#density-threshold-method>`__) is used a lowproc must be specified for the type-in-type correction.
- Density fitting embedding gradients are not supported right now.
- Please note the following embedding gradient methods have not yet been implemented: Multireference-WF-in-DFT, and DFT-in-DFT embedding.

Example input files for gradients are located under the examples section (`examples <projection-based_wf-in-dft_embedding.html#examples>`__)

All publications resulting from the use of this method must acknowledge the analytical WF-in-DFT nuclear gradients paper.

S. J. R. Lee, F. Ding, F. R. Manby, T. F. Miller III, arXiv e-prints, (2019), arXiv:1903.05830

.. _projection-based_wf-in-dft_embedding--embedding-gradient-options:

Embedding Gradient Options
==========================

* ``GRAD`` This option must be present in the ``EMBED`` directive when calculating a projection-based embedding gradient.
* ``CPKSTHR``\ =value (default 1.d-6) This option specifies the convergence threshold for the solutions of the coupled-perturbed Kohn-Sham equations.

.. _projection-based_wf-in-dft_embedding--embedding-gradient-best-practices:

Embedding Gradient Best Practices
=================================

* We have found the best agreement between numerical gradients and analytical gradients when using the Neese (NEESE) grids.
* Grid weight derivatives should be calculated for all DFT quantities.

.. _projection-based_wf-in-dft_embedding--examples:

Examples
--------

.. _projection-based_wf-in-dft_embedding--projection-based-embedding:

Projection-Based Embedding
==========================

This example performs a HF-in-HF and CCSD(T)-in-HF calculation on methanol. The HF-in-HF energy is numerically identical to the HF energy of the full system. By replacing the initial HF calculation on the full system with a DFT calculation, it is possible to perform HF-in-DFT and CCSD(T)-in-DFT calculations.

.. code-block:: text
   :caption: examples/embed_proj_methanol.inp

   !methanol
   memory,100,m
   symmetry,nosym ! Embedding is not implemented with symmetry
   
   r1=2.648205499 ! Bohr
   r2=1.780518852 ! Bohr
   r3=2.064847045 ! Bohr
   a1=110.61344
   d1=0
   d2=119.9573
   
   {gthresh,grid=1e-12,orbital=1e-8,coeff=1e-7}
   
   geometry= {C;
              O,C,r1;
              H1,O,r2,C,a1;
              H2,C,r3,O,a1,H1,d1;
              H3,C,r3,O,a1,H1,d2;
              H4,C,r3,O,a1,H1,-d2}
   
   basis,def2-svp
   
   ! Step 1: Perform a HF calculation on the full system.
   {df-hf}
   
   ! Step 2: Perform orbital localization.
   ! Localized MOs are saved to record 3100.2
   {ibba;save,3100.2}
   
   ! Step 3: Define the procedure that will be used for the embedded calculation.
   !         Here, we define a standard CCSD(T) calculation.
   proc embedded_ccsdt
       ! Step 3a: Call HF. In this procedure, only subsystem A will be calculated.
       ! This corresponds to a HF-in-HF calculation.
       {df-hf}
   
       ! Step 3b: Call CCSD(T). This will perform a CCSD(T)-in-HF calculation
       {df-ccsd(t)}
   endproc
   
   ! Step 4: Perform the embedding calculation. This requires:
   ! Specification of embedded MOs
   ! Location of localized orbitals
   ! The procedure to run on the embedded subsystem A.
   {df-embed,orbs=[1,6,7,8,9],highproc=embedded_ccsdt      ! The active subsystem corresponds to the indicated MOs
   orbital,3100.2,local}             ! Use the localized MOs from record 3100.2

.. _projection-based_wf-in-dft_embedding--embedded-multiconfigurational-calculations:

Embedded Multiconfigurational Calculations
==========================================

This example performs an MCSCF-in-DFT calculation on butene.

.. code-block:: text
   :caption: examples/embed_mrci.inp

   !butene
   symmetry,nosym ! Embedding is not implemented with symmetry
   
   {gthresh,grid=1e-12,orbital=1e-8,coeff=1e-7}
   
   geometry={
   C1,,          0.835432384 ,   0.049538050 ,  -1.305177530
   C2,,         -0.187431703 ,  -1.125601622 ,   1.070665830
   C3,,         -0.143380420 ,   0.687719249 ,   3.341106035
   H1,,         -2.118667450 ,  -1.789600571 ,   0.735591607
   H2,,          0.942690000 ,  -2.802115823 ,   1.537268881
   H3,,         -0.860542916 ,  -0.240216354 ,   5.042940132
   H4,,         -1.309266799 ,   2.354788168 ,   2.978399494
   H5,,          1.778149207 ,   1.339614495 ,   3.742333311
   C4,,         -0.440429873 ,   0.344384131 ,  -3.450328416
   H6,,          2.782544497 ,   0.715697009 ,  -1.206788342
   H7,,         -0.434433198 ,  -1.089606640 ,  -4.914726597
   H8,,         -1.545390643 ,   2.035286250 ,  -3.818951212
   } !Geometry is in Bohr
   
   basis=def2-svp
   
   ! Step 1: Perform DFT on full system.
   ! Level shift added for improved convergence for this system.
   !  The system is a butene where the double bond is twisted by 90 degrees.
   {rks,b-lyp,shifta=-0.3}
   
   ! Step 2: Define the procedure that will be used for the embedded calculation.
   !         Here, we define a standard MRCI calculation.
   proc embedded_mrci
       ! Step 2a: Generate initial orbitals for MCSCF.
       {rhf}
   
       ! Step 2b: Perform MCSCF calculation.
       ! When performing an embedded MCSCF calculation, always specify the active space.
       {mcscf;
       config,csf;
       OCC,9;
       closed,7;
       frozen,2;}
   
       ! Step 2c: Add dynamic correlation
       {mrci}
   endproc
   
   ! Step 3: Call embedding code and specify the atoms corresponding to the twisted double bond. Provide the procedure for the embedded calculation.
   {embed,atoms=[C1,C4,H6,H7,H8],highproc=embedded_mrci}

.. _projection-based_wf-in-dft_embedding--density-threshold-truncation:

Density Threshold Truncation
============================

This example performs a CCSD(T)-in-B3LYP calculation on a water dimer, using the density-threshold method with a truncate value of 0.001.

.. code-block:: text
   :caption: examples/embed_trunc2.inp

   !water dimer
   memory,150,m
   
   {gthresh,orbital=1e-8,coeff=1e-7}
   
   geometry={
   O1,,          2.872302451  , -0.739837226  ,  2.587473481
   H11,,         1.114872273  , -1.362093804  ,  2.841067168
   H12,,         3.830013761  , -1.316171569  ,  4.018958028
   O2,,          1.378439935  ,  3.695314083  , -0.113721828
   H21,,         2.070708975  ,  2.651580550  ,  1.227452707
   H22,,         2.064068477  ,  2.891071211  , -1.605148488
   } !Geometry is in Bohr
   
   Basis,avtz
   
   ! Step 1: Perform an LDA calculation on the full system
   {df-ks}
   
   ! Step 2: Perform orbital localization.
   {ibba;save,3100.2}
   
   ! Step 3: Define the procedure that will be used for the embedded calculation.
   !         Here, we define a standard CCSD(T) calculation.
   proc embedded_ccsdt
       ! Step 3a: Perform a HF-in-LDA calculation
       {df-hf;noenest}
   
       ! Step 3b: Perform a CCSD(T)-in-LDA calculation
       {df-ccsd(t)}
   endproc
   
   ! Step 4: Run the embedding calculation
   ! using truncation with the density threshold method.
   {df-embed,N_orbitals=5,truncate=0.0001,atoms=[O1,H11,H12],highproc=embedded_ccsdt;orbital,3100.2,local}

.. _projection-based_wf-in-dft_embedding--open-shell-system:

Open Shell System
=================

This example performs a RCCSD(T)-in-LDA calculation on the methoxy radical.

.. code-block:: text
   :caption: examples/embed_open.inp

   !Methoxy Radical
   memory,100,M
   zsymel=nosym  ! Embedding is not implemented with symmetry
   
   {gthresh,grid=1e-12,orbital=1e-8,coeff=1e-7}
   
   Geometry={
   O1,,          2.328578323  , -0.516253350  , -0.241152468
   H1,,         -3.930899693  ,  0.818199944  ,  0.136592671
   C1,,         -2.292181882  , -0.433746123  , -0.018359872
   H2,,         -2.391620554  , -1.802771746  ,  1.530291417
   C2,,          0.160581025  ,  1.056429748  ,  0.096479104
   H3,,          0.284618712  ,  2.116540479  ,  1.878957579
   H4,,          0.248705545  ,  2.426749515  , -1.444737877
   H5,,         -2.407046505  , -1.464278195  , -1.802909809
   }! Geometry is in Bohr
   
   basis,def2-svp
   
   ! Step 1: Perform a DFT calculation on the full system.
   {ks,lda;wf,25,1,1}
   
   ! Step 2: Perform orbital localization.
   {ibba}
   
   ! Step 3: Define the procedure that will be used for the embedded calculation.
   !         Here, we define a standard CCSD(T) calculation.
   proc embedded_ccsdt
       ! Step 3a: Call HF. In this procedure,  only subsystem A will be calculated.
       ! This corresponds to a HF-in-LDA calculation.
       {hf}
   
       ! Step 3b: Call CCSD(T). This will perform a RCCSD(T)-in-LDA calculation
       {rccsd(t)}
   endproc
   
   ! Step 4: Perform the embedded calculation.
   {embed,atoms=[O1],highproc=embedded_ccsdt}

.. _projection-based_wf-in-dft_embedding--ccsd-t-in-lda-gradient-calculation:

CCSD(T)-in-LDA Gradient Calculation
===================================

This example performs a CCSD(T)-in-LDA gradient calculation on ethanol.

.. code-block:: text
   :caption: examples/embed_grad_ccsd_t-in-lda.inp

   !strained_ethanol
   memory,200,M
   symmetry,nosym ! Embedding is not implemented with symmetry
   
   {gthresh,orbital=1.0d-07}
   
   ! Geometry in bohr
   geometry={
   O1,,     -6.287074 ,  5.128142 ,  0.368844
   H2,,     -4.331335 ,  5.076727 ,  0.829762
   C3,,     -7.553333 ,  1.646329 ,  0.142339
   C4,,     -5.608539 ,  2.964896 ,  0.000000
   H5,,     -9.487950 ,  1.458382 , -0.789351
   H6,,     -8.648844 ,  0.140577 ,  1.411194
   H7,,     -7.564298 , -0.311707 , -0.867451
   H8,,     -4.507431 ,  2.577084 , -1.650962
   H9,,     -4.726024 ,  2.654073 ,  1.792503
   }
   
   basis={default,sto-3g}
   
   {grid,name=NEESE,neese_index=4}
   
   ! Step 1: Perform a LDA calculation on the full system.
   {rks,LDA;core,0}
   
   ! Step 2: Perform orbital localization.
   !         Embedding gradients currently only supports Pipek-Mezey localized orbitals
   !         such that the core and valence are localized together.
   !         Therefore, core must be specified to be 0 so core and valence orbitals are
   !         localized together.
   {locali,pipek;core,0}
   
   ! Step 3: Define the procedure that will be used for the embedded calculation.
   !         Here, we define a standard CCSD(T) gradient calculation (the {force} call
   !         must be present).
   !         HF_COR should be set to 0 when doing gradients so the projector correction
   !         is not added.
   !         The frozen-core approximation for correlated calculations can be turned on
   !         by specifying the correct number of core orbitals in Subsystem A.
   !         (1 core orbital for the Oxygen in this case)
   proc hi_proc
      {HF,hf_cor=0;core,1}
      {CCSD(T);core,1;cphf,thrmin=1.d-7}
      {force}
   endproc
   
   ! Step 4: Perform the embedding calculation. This requires:
   !         Specification of the option grad to tell the embedding code gradients
   !         are requested.
   !         Specification of embedded atoms.
   !         The procedure to run on the embedded subsystem A.
   !         Any embedding options such as cpksthr which controls the level
   !         of convergence of the CPKS solutions.
   {embed,grad,highproc=hi_proc,atoms=[O1,H2],cpksthr=1.d-7}
   
   ! Step 5: The force command must specified after the embedding command so the
   !         embedding gradient is calculated.
   {force,gridgrad=1}

.. _projection-based_wf-in-dft_embedding--ccsd-t-in-lda-gradient-calculation-w-density-threshold-truncation:

CCSD(T)-in-LDA Gradient Calculation w/ Density Threshold Truncation
===================================================================

This example performs a CCSD(T)-in-LDA gradient calculation with density threshold truncation on ethanol.

.. code-block:: text
   :caption: examples/embed_grad_ccsd_t-in-lda_ao_trunc.inp

   !strained_ethanol
   memory,200,M
   symmetry,nosym ! Embedding is not implemented with symmetry
   
   {gthresh,orbital=1.0d-07}
   
   ! Geometry in bohr
   geometry={
   O1,,     -6.287074 ,  5.128142 ,  0.368844
   H2,,     -4.331335 ,  5.076727 ,  0.829762
   C3,,     -7.553333 ,  1.646329 ,  0.142339
   C4,,     -5.608539 ,  2.964896 ,  0.000000
   H5,,     -9.487950 ,  1.458382 , -0.789351
   H6,,     -8.648844 ,  0.140577 ,  1.411194
   H7,,     -7.564298 , -0.311707 , -0.867451
   H8,,     -4.507431 ,  2.577084 , -1.650962
   H9,,     -4.726024 ,  2.654073 ,  1.792503
   }
   
   basis={
   default,def2-svp
   }
   
   {grid,name=NEESE,neese_index=4}
   
   ! Step 1: Perform a LDA calculation on the full system.
   {rks,LDA;core,0}
   
   ! Step 2: Perform orbital localization.
   !         Embedding gradients currently only supports Pipek-Mezey localized orbitals
   !         such that the core and valence are localized together.
   !         Therefore, core must be specified to be 0 so core and valence orbitals are
   !         localized together.
   {locali,pipek;core,0}
   
   ! Step 3: Define the procedure that will be used for the type-in-type correction.
   !         This procedure needs to call the same DFT method used in Step 1.
   !         Except now the {force} call must be present so the type-in-type
   !         contributions to the embedding gradient can be added.
   proc low_proc
       {rks,LDA;core,0}
       {force,gridgrad=1}
   endproc
   
   ! Step 4: Define the procedure that will be used for the embedded calculation.
   !         Here, we define a standard CCSD(T) gradient calculation (the {force} call
   !         must be present).
   !         HF_COR should be set to 0 when doing gradients so the projector correction
   !         is not added.
   !         The frozen-core approximation for correlated calculations can be turned on
   !         by specifying the correct number of core orbitals in Subsystem A.
   !         (1 core orbital for the Oxygen in this case)
   proc hi_proc
      {HF,hf_cor=0;core,1}
      {CCSD(T);core,1;cphf,thrmin=1.d-7}
      {force}
   endproc
   
   ! Step 5: Perform the embedding calculation. This requires:
   !         1) Specification of the option grad to tell the embedding code gradients
   !         are requested.
   !         2) Specification of embedded atoms.
   !         3) The procedure to run on the embedded subsystem A.
   {embed,grad,highproc=hi_proc,atoms=[O1,H2],lowproc=low_proc,truncate=1e-4,ao_per_atom}
   
   ! Step 6: The force command must specified after the embedding command so the
   !         embedding gradient is calculated.
   {force,gridgrad=1}

.. _projection-based_wf-in-dft_embedding--mp2-in-lda-geometry-optimization:

MP2-in-LDA Geometry Optimization
================================

This example performs a MP2-in-LDA geometry optimization on ethanol.

.. code-block:: text
   :caption: examples/embed_grad_opt.inp

   !ethanol
   memory,200,M
   
   {gthresh,grid=1d-12,orbital=1.0d-07}
   
   ! Original geometry
   symmetry,nosym
   geometry={
   O1         -3.3322316672        2.7486714246        0.4634782128
   H2         -2.4357007108        3.2239754945        0.4835540980
   C3         -4.1946894574        0.5410193913       -0.0217296115
   C4         -2.9359507722        1.4310420137        0.0489661919
   H5         -4.9218723840        0.9675783876       -0.7301767123
   H6         -4.6706714295        0.4744353658        0.9687956993
   H7         -3.9246181899       -0.4721658034       -0.3558474595
   H8         -2.4446716957        1.4212399976       -0.9554187232
   H9         -2.2101426141        0.9539365224        0.7529059549
   }
   
   basis={
   default,sto-3g
   }
   
   proc hi_proc1
      {HF,hf_cor=0;core,0;start,2102.2;save,2102.2}
      {MP2;core,0;cphf,thrmin=1.d-7}
      {force}
   endproc
   
   proc runembed
       {rks,LDA;core,0;start,2101.2;save,2101.2}
       {locali,pipek;core,0}
       {embed,grad,highproc=hi_proc1,orbs=[9,10,11,12,13]}
   endproc
   
   {optg,procedure=runembed}

.. _projection-based_wf-in-dft_embedding--mp2-in-lda-geometry-optimization-w-density-threshold-truncation:

MP2-in-LDA Geometry Optimization w/ Density Threshold Truncation
================================================================

This example performs a MP2-in-LDA geometry optimization with density threshold truncation on ethanol.

.. code-block:: text
   :caption: examples/embed_grad_opt_ao_trunc.inp

   !ethanol
   memory,200,M
   
   {gthresh,grid=1d-12,orbital=1.0d-07}
   
   ! Original geometry
   symmetry,nosym
   geometry={
   O1         -3.3265927677        2.7508371961        0.4722099522
   H2         -2.4299560718        3.2260275232        0.4808555391
   C3         -4.1955133281        0.5390054989       -0.0225174814
   C4         -2.9373667449        1.4340964566        0.0502923154
   H5         -4.9209868031        0.9595827880       -0.7359982137
   H6         -4.6761386977        0.4760110751        0.9660347037
   H7         -3.9228360337       -0.4750976765       -0.3498843604
   H8         -2.4504497951        1.4273894050       -0.9556425922
   H9         -2.2107086788        0.9518805278        0.7491777878
   }
   
   basis={
   default,sto-3g
   }
   
   ! This works without specifying the start record for each calculation.
   ! However, I would highly recommend specifying the start and save dump records
   ! to ensure that it always works.
   proc low_proc
       {rks,LDA,hf_cor=0;core,0;start,2103.2;save,2103.2}
       {force}
   endproc
   
   proc hi_proc1
       {HF,hf_cor=0;core,0;start,2104.2;save,2104.2}
       {MP2;core,0;cphf,thrmin=1.d-7}
       {force}
   endproc
   
   proc runembed
       {rks,LDA;core,0;start,2100.2;save,2100.2}
       {locali,pipek,thrpip=1.0d-14;core,0}
       {embed,grad,highproc=hi_proc1,lowproc=low_proc,truncate=0.01,orbs=[9,10,11,12,13]}
   endproc
   
   {optg,procedure=runembed}
