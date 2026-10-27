.. raw:: html

   <span id="bibliography"></span>

.. _multireference_local_correlation_methods_pno-caspt2--multireference-local-correlation-methods-pno-caspt2:

Multireference local correlation methods (PNO-CASPT2)
=====================================================

In this section multireference local correlation methods are described. Many keywords are similar to :doc:`PNO-based single-reference methods <local_correlation_methods_with_pair_natural_orbitals_pnos>` and :doc:`RS2 methods <multireference_rayleigh_schroedinger_perturbation_theory>`. The corresponding publications can be found in `#bibliography <multireference_local_correlation_methods_pno-caspt2.html#bibliography>`__

In order to avoid an expensive canonical integral transformation and the storage of the resulting integrals (which can be huge for large molecules), it is necessary to store the CASSCF wavefunction(s) using the ``CIREC`` option, see `Saving the CI vectors <the_mcscf_program_multi.html#saving-the-ci-vectors>`__. The same ``CIREC`` option must be given on the ``PNO_CASPT2`` command line. Note that the record number is automatically increased by 100 for each ``WF`` directive (i.e. different spatial or spin symmetry) in the CASSCF program (Multi). An example is given below.

.. code-block:: text
   :caption: examples/h2o_pno_caspt2.inp

    gprint,orbitals,civector
    basis=avtz,h=vtz
   
    geometry=h2o.xyz
   
    set,charge=1
    {df-multi;                                                                     ! casscf, state averaged
    wf,spin=1;state,2                                                              ! doublet, 2 states
    wf,spin=3;                                                                     ! quartet
    natorb,cirec=5140.2}                                                           ! save casscf wavefunctions
   
   {pno-caspt2,cirec=5140.2,shift=0.3;state,1,1;wf,spin=1}                         ! first doublet state
   {pno-caspt2,cirec=5140.2,shift=0.3;state,1,2;wf,spin=1}                         ! second doublet state
   {pno-caspt2,cirec=5240.2,shift=0.3;wf,spin=3}                                   ! quartet state
   
   {pno-caspt2,cirec=5140.2,shift=0.3;state,2;wf,spin=1}                           ! MS-CASPT2 for doublet states

.. _multireference_local_correlation_methods_pno-caspt2--single-state-pno-caspt2:

Single-state PNO-CASPT2
=======================

The program can be invoked using **``PNO-CASPT2``, *options***.

Many default settings for local approximations are similar to `default settings in PNO-LMP2 <local_correlation_methods_with_pair_natural_orbitals_pnos.html#default-and-tight-settings>`__.

.. _multireference_local_correlation_methods_pno-caspt2--options:

Options
=======

General local correlation options
``IEXT, REXT,THRDIST, FITLMO, LOCFIT_PNO, THRLOC``
can be found in options for `PNO <local_correlation_methods_with_pair_natural_orbitals_pnos.html#options>`__ or `PAO <pao-based_local_correlation_treatments.html#general-options>`__ based methods.

.. _multireference_local_correlation_methods_pno-caspt2--pno-caspt2-specific-options:

PNO-CASPT2 specific options
===========================

``THRPNO_EN (default: 0.997) completeness threshold for PNO construction``

``THRPNO_OCC (default: 1.D-8) occupation number threshold for PNO construction``

``THRPNOP2_EN/THRPNOP1_EN/THRPNOP0_EN (default: THRPNO_EN) as THRPNO_EN, but only for P2/P1/P0 excitation subspace``

``THRPNOP2_OCC/THRPNOP1_OCC/THRPNOP0_OCC (default: THRPNO_OCC) as THRPNO_OCC, but only for P2/P1/P0 excitation subspace``

``FCLOS`` (default: *false*) use closed-shell Fock matrix :math:`f^c` in the right-hand side of the PNO-CASPT2 amplitude equations. Recommended if an averaged Fock matrix is used in the zero-order Hamiltonian

``SHIFT`` (default: *0.0*) level shift to reduce the intruder state problem (see `level shifts in RS2 <multireference_rayleigh_schroedinger_perturbation_theory.html#level-shifts>`__)

``CIREC`` record for CASSCF CI vectors stored in ``MULTI``. If given, these are used without performing an extra reference CI. The CI vectors have to be saved in multi using the ``save,cirec`` directive (see examples below).

``USE_SINGLES`` (default: *0*) if set to 1 explicit single excitations are used in the amplitude equations

``DIAG_DENF`` (default: *1*) the Gamma matrix is diagonalized in PNO-CASPT2 (makes H0 block-diagonal)

``THRDLP`` threshold for projection of redundant configurations in P1 and P0 subspaces

``THRDLS`` threshold for projection of redundant configurations in the remaining configuration subspaces

Using the directive ``STATE`` one can specify the state of interest (see `the single-root excited state calculation in RS2 <multireference_rayleigh_schroedinger_perturbation_theory.html#excited-state-calculations>`__).

**Note:**  level shifts have to be given as options. The ``SHIFT`` directive refers to denominator shifts, which affect the convergence but not the Hamiltonian and the results.

.. _multireference_local_correlation_methods_pno-caspt2--multi-state-pno-caspt2:

Multi-state PNO-CASPT2
----------------------

Multi-state calculations are possible by specifying multiple states on the ``STATE`` card.

An effective Hamiltonian
\begin{equation}
H_{MN}^\textrm{eff}=\frac{1}{2}\left(  \langle M\|\hat H ~^N\hat T_2\|N\rangle + \langle M \| ~^M\hat T_2^{\dagger} \hat H \| N\rangle\right) + \delta_{MN} \langle M \| \hat H \| N \rangle.
\end{equation}
is constructed using state-specific PNO-CASPT2 amplitudes and diagonalized.

.. _multireference_local_correlation_methods_pno-caspt2--additional-options:

Additional options
==================

``H0`` (default: *0*) use CASPT2\ **D** (*=1*) or CASPT2\ **D2** (*=2*) approximations (see `J. Chem. Phys. <https://doi.org/10.1063/1.5097644>`__ **150**, 214107 (2019))

``COUPCOR`` (default: *0*) use coupling corrections for the above approximations (*1*: simple Lagrangian correction **Dc** or **D2c**; *2*: additional relaxation correction **Dcr** or **D2cr**)

.. _multireference_local_correlation_methods_pno-caspt2--bibliography:

Bibliography
------------

PNO-CASPT2:

* F. Menezes, D. Kats, and H.-J. Werner, *Local Complete Active Space Second-Order Perturbation Theory Using Pair Natural Orbitals (PNO-CASPT2)* `J. Chem. Phys. <https://doi.org/10.1063/1.4963019>`__ **145**, 124115 (2016)

Multi-state PNO-CASPT2:

* D. Kats and H.-J. Werner, *Multi-State Local Complete Active Space Second-Order Perturbation Theory Using Pair Natural Orbitals (PNO-MS-CASPT2)* `J. Chem. Phys. <https://doi.org/10.1063/1.5097644>`__ **150**, 214107 (2019)
