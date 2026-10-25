.. raw:: html

   <span id="cphf-for-gradients-expectation-values-and-polarizabilities"></span>

.. raw:: html

   <span id="density-fitting-mp2-df-mp2-ri-mp2"></span>

.. raw:: html

   <span id="expectation-values-for-mp2"></span>

.. raw:: html

   <span id="expectation-values-for-mp3"></span>

.. raw:: html

   <span id="natural-orbitals"></span>

.. raw:: html

   <span id="polarizabilities-and-second-order-properties-for-mp2"></span>

.. raw:: html

   <span id="saving-the-density-matrix"></span>

.. raw:: html

   <span id="spin-component-scaled-mp2-scs-mp2"></span>

.. _moller_plesset_perturbation_theory--m-ller-plesset-perturbation-theory:

Møller Plesset perturbation theory
==================================

Closed-shell Møller-Plesset perturbation theory up to full fourth order [MP4(SDTQ)] is part of the coupled-cluster program.

The commands ``MP2, MP3, MP4`` perform the MP calculations up to the specified order (lower orders are included).

``MP4;NOTRIPL; performs MP4(SDQ) calculations.``

Normally, no further input is needed if the ``MPn`` card directly follows the corresponding HF-SCF. Otherwise, occupancies and orbitals can be specified as in the CI program. The resulting energies are stored in variables as explained in section `special variables <variables.html#special-variables>`__.

Dual basis set calculations are possible for the closed-shell methods, see section `dual basis set calculations <the_closed_shell_ccsd_program.html#dual-basis-set-calculations>`__.

.. _moller_plesset_perturbation_theory--expectation-values-for-mp2:

Expectation values for MP2
==========================

``EXPEC[,[TYPE=]type][,opname]``

One-electron properties can be computed if an ``EXPEC`` card follows the ``MP2`` card (the ``GEXPEC`` directive has no effect in this case). Properties are obtained as analytical energy derivatives with or without taking into account the orbital relaxation, which can be specified as

* **``TYPE``:** *type*\ =\ ``RELAX``: Compute fully relaxed properties with taking into account the orbital relaxation (default). Nonrelaxed properties are also computed and printed. For MP2, this option is highly recommended.

*type*\ =\ ``NORELAX``: Compute properties without taking into account the orbital relaxation.

Note that, in MP2, calculation of fully relaxed properties may be much more expensive than computing only the energy or properties without the orbital relaxation effect. The syntax for operators *opname* is explained in section `One-electron operators and expectation values (GEXPEC) <program_control.html#one-electron-operators-and-expectation-values-gexpec>`__. See also ``DM`` in section `saving the density matrix <moller_plesset_perturbation_theory.html#saving-the-density-matrix>`__, and ``NATORB`` in section `natural orbitals <moller_plesset_perturbation_theory.html#natural-orbitals>`__.

.. _moller_plesset_perturbation_theory--expectation-values-for-mp3:

Expectation values for MP3
==========================

``EXPEC``\ [,\ *opname*] Fully relaxed one-electron properties are available for MP3 (see section `First- and second-order properties for CCSD from expectation-value CC theory (XCCSD) <excited_states_with_equation-of-motion_ccsd_eom-ccsd.html#first-and-second-order-properties-for-ccsd-from-expectation-value-cc-theory-xccsd>`__, Paper 2). Currently, this is only working without frozen core orbitals, i.e. ``CORE,0`` must be specified. MP2 properties are also computed and printed.

.. _moller_plesset_perturbation_theory--saving-the-density-matrix:

Saving the density matrix
=========================

``DM,record.ifil;``

The first-order density matrix in AO basis is stored in record *record* on file *ifil*. Two types of density matrices are stored in the same record: the one without orbital relaxation contribution is stored as *set 1*, meanwhile with the orbital relaxation contribution, it is stored as *set 2*. If the ``NORELAX`` directive is given on the ``EXPEC`` card prior to the ``DM`` card, only the orbital unrelaxed density matrix is computed and stored. See also ``NATORB`` in section `natural orbitals <moller_plesset_perturbation_theory.html#natural-orbitals>`__.

.. _moller_plesset_perturbation_theory--natural-orbitals:

Natural orbitals
================

``NATORB,[RECORD=]record.ifil,[PRINT=nprint],[CORE[=natcor]];``

Calculate natural orbitals. The number of printed external orbitals in any given symmetry is *nprint*) (default 2). *nprint=-1* suppressed the printing. The natural orbitals and the density matrix are saved in a dump record *record* on file *ifil*. If *record.ifil* is specified on a ``DM`` card (see above), this record is used. If different records are specified on the ``DM`` and ``NATORB`` cards, an error will result. The record can also be given on the ``SAVE`` card. Natural orbitals are computed for both the nonrelaxed and relaxed density matrices if available, which are stored in the same record as *set 1* and *set 2*, respectively.

Note that the effective (relaxed) density matrix of non-variational methods like MP2, CCSD, or CCSD(T) does not strictly behave as a density matrix. For instance, it has non-zero matrix elements between core and valence orbitals, and therefore core orbitals are affected by the natural orbital transformation. Also, occupation numbers can be greater than 2.0 or less than 0.0. If ``CORE`` is given (*natcor=1*), the core orbitals are frozen by excluding them from the natural orbital transformation.

.. _moller_plesset_perturbation_theory--polarizabilities-and-second-order-properties-for-mp2:

Polarizabilities and second-order properties for MP2
====================================================

Analytical MP2 static dipole polarizabilities and other second order properties can be computed using the ``POLARI``. By default the dipole operator is used, but other one-electron operators can be specified on the ``POLARI`` directive. Currently, this is only working without frozen core orbitals, i.e., C͡ORE,0 must be given. This option is only available without using the density fitting approximation. The dipole polarizabilities are stored in the variables ``POLXX, POLXY, POLXZ, POLYY, POLYZ, POLZZ``.

Example:

.. code-block:: text

   { mp2
    core,0
    polari,dm,qm}

Computes the full tensors for the dipole and quadrupole operators.

Nonsymmetrized first-order perturbed density matrix resulting from CP equations for MP2 can be stored for further use if ``RECMP2=``\ *record.ifil* is given.

.. _moller_plesset_perturbation_theory--cphf-for-gradients-expectation-values-and-polarizabilities:

CPHF for gradients, expectation values and polarizabilities
===========================================================

The accuracy and other parameters of the CPHF calculations necessary to compute gradients and response properties can be modified using the ``CPHF`` directive:

``CPHF, [THRMIN=thrmin], [THRMAX=thrmax], [MAXIT=maxit], [SHIFT=shift], [SAVE=record], [START=record], [DIIS=idiis], [DISM=idism]``

* ``THRMIN`` CPHF convergence threshold (default 1.d-6). ``THRESH`` and ``ACCU`` are aliases for this.
* ``THRMAX`` initial CPHF convergence threshold in geometry optimizations. Once the geometry is converged to a certain accuracy (depending on ``OPTCONV``), the threshold is stepwise reduced to ``THRMIN``.

The default is ``THRMAX``\ =min(1.d-6,\ ``THRMIN``\*100); Values larger than 1.d-6 are ignored.

* ``MAXIT`` Maximum number of iterations (default 50).
* ``SHIFT`` Level shift for CPHF (default 0.1).
* ``DIIS`` First macroiteration in which DIIS is used (default 1)
* ``DISM`` First microiteration in which DIIS is used (default 1; in microiterations the core contribution is frozen).
* ``SAVE`` Record on which the CPHF solution can be saved for later restarts. The solution is saved automatically in geometry optimizations and frequency calculations.
* ``START`` Record from which initial guess is read. A starting guess is read automatically in geometry optimizations and frequency calculations.

In density-fitting MP2, only ``THRMIN`` is active, the rest of the options are handled automatically.

.. _moller_plesset_perturbation_theory--density-fitting-mp2-df-mp2-ri-mp2:

Density-fitting MP2 (DF-MP2, RI-MP2)
====================================

``DF-MP2,options``

invokes the density fitted MP2 program. The present implementation works only without symmetry. ``RI-MP2`` is an alias for the command ``DF-MP2``.

The following options can be specified:

* **``BASIS_MP2``\ =\ *basis*:** Fitting basis set. *basis* can either refer to a basis set defined in a ``BASIS`` block, or to a default fitting basis set (only available for correlation consistent basis sets). If a correlation consistent orbital basis set is used, the corresponding MP2 fitting basis is generated by default. In all other cases, the fitting basis must be defined.
* **``THRAO``\ =\ *value*:** Screening threshold for 3-index integrals in the AO basis
* **``THRMO``\ =\ *value*:** Screening threshold for 3-index integrals in the MO basis
* **``THROV``\ =\ *value*:** Screening threshold for 2-index integrals of fitting basis.
* **``THRPROD``\ =\ *value*:** Screening product threshold for first half transformation.
* **``SPARSE``\ =\ *value*:** If Non-zero, use sparse algorithm in second-half transformation (default).

See section :doc:`density fitting <density_fitting>` for a more general description of density fitting. Expectation values and gradients can also be computed with ``DF-MP2``.

.. _moller_plesset_perturbation_theory--spin-component-scaled-mp2-scs-mp2:

Spin-component scaled MP2 (SCS-MP2)
===================================

The spin-component scaled MP2 energy as proposed by Grimme (`J. Chem. Phys. <https://dx.doi.org/10.1063/1.1569242>`__ **118**, 9095 (2003)) is printed automatically using the default scaling factors (1.2 for antiparallel spin, 1/3 for parallel spin). These factors can be modified using the options ``SCSFACS`` and ``SCSFACT``, respectively, i.e.

``MP2, SCSFACS=facs, SCSFACT=fact``

The SCS-MP2 total energy is stored in the variable ``EMP2_SCS``. Gradients and first-order properties can be computed for SCS-MP2 by setting the option ``SCSGRD=1``. This only operational for density fitted MP2 and local MP2 methods, i.e. using

``DF-MP2,[DF_BASIS=fitbasis],SCSGRD=1,[ SCSFACS=facs], [SCSFACT=fact]``

followed by ``FORCES`` or ``OPTG``. In these cases, the SCS-MP2 total energy replaces the MP2 total energy in the variable ``EMP2``. Expectation values can also be computed with ``DF-SCS-MP2``, where the SCS-MP2 density matrix is used instead of the MP2 density matrix (see section `expectation values for MP2 <moller_plesset_perturbation_theory.html#expectation-values-for-mp2>`__). For DF-LMP2 see section :doc:`PAO-based local correlation treatments <pao-based_local_correlation_treatments>`.

.. _moller_plesset_perturbation_theory--perturbation-adapted-perturbation-theory-papt:

Perturbation-adapted Perturbation Theory (PAPT)
===============================================

The perturbation-adapted zero-order hamiltonian described in J. Chem. Phys. 156, 011101 (2022); https://doi.org/10.1063/5.0079853 is available for closed-shell systems by putting

``PAPT``

in the input before ``MP2``, ``MP3``, ``MP4`` or ``CCSD(T)``. The effect of the ``PAPT`` is to define a new set of orbitals and effective hamiltonian eigenvalues that are used in subsequent correlation treatments.
