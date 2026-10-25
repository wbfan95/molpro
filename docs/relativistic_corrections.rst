.. _relativistic_corrections--relativistic-corrections:

Relativistic corrections
========================

There are three ways in Molpro  to take into account scalar relativistic effects:

- Use the Douglas-Kroll-Hess or eXact-2-Component (X2C) relativistic one-electron integrals.
- Compute a perturbational correction using the Cowan-Griffin operator (see section `One-electron operators and expectation values (GEXPEC) <program_control.html#one-electron-operators-and-expectation-values-gexpec>`__).
- Use relativistic effective core potentials (see section :doc:`effective core potentials <effective_core_potentials>`).

.. _relativistic_corrections--using-the-douglas-kroll-hess-or-exact-2-component-hamiltonians:

Using the Douglas–Kroll–Hess or eXact-2-Component Hamiltonians
==============================================================

For all-electron calculations, the preferred way is to use either the Douglas–Kroll–Hess (DKH) or eXact-2-Component (X2C) Hamiltonians, the former of which is available up to (in principle) arbitrary order in Molpro. DKH is activated by setting any of

``SET,DKROLL=1\\``
``SET,DKHO=$n$,  ($n=2,\dots,99$),\\``
``SET,DKHP=$m$,  ($m=1,\dots,5$)``

or for X2C by setting

``SET,DKHO=101\\``
somewhere in the input before the first energy calculation.

With MOLPRO_2026.1 or later, DKROLL and DKHO are set automatically if a DK default basis set is given. Then all atoms must have the same basis type (either -DK, -DK3, or -X2C), otherwise the program will stop with an error message. With -DK, -DK3 and -X2C the variable DKHO will be set to 2,3, or 101, respectively. Other values can be chosen by setting the variable DKHO ``after`` the basis input.

Alternatively, these values can be given as options on the ``INT`` command:

``INT,[DKROLL=1],DKHO=$n$,DKHP=$m$.``

or

``INT,DKHO=101``

The DKH option ``DKROLL`` is available for compatibility with earlier versions of Molpro. If only ``DKROLL=1`` is given, the default for ``DKHO`` is 2. Setting ``DKROLL=0`` disables DKH and X2C, independently of the setting of ``DKHO``. DKH is also disabled by setting ``DKHO=0``, unless ``DKROLL=1`` is set. In order to avoid confusion, it is recommended only to use ``DKHO`` and never set ``DKROLL``. Any of these values must be given AFTER the basis input.

The value of ``DKHP`` specifies the parametrization for the DKH treatment (it has no effect for X2C):

* **``DKHP=1``:** Optimum parametrization (OPT, default)
* **``DKHP=2``:** Exponential parametrization (EXP)
* **``DKHP=3``:** Square-root parametrization (SQR)
* **``DKHP=4``:** McWeeny parametrization (MCW)
* **``DKHP=5``:** Cayley parametrization (CAY)

**Example:**

.. list-table::

   * - ``SET,DKHO=8``
     - !
     - DKH order = 8
   * - ``SET,DKHP=2``
     - !
     - choose exponential parametrization for unitary transformations (recommended)

Up to fourth order (``DKHO=4``) the DKH Hamiltonian is independent of the chosen parametrization. Higher-order DKH Hamiltonians depend slightly on the chosen parametrization of the unitary transformations applied in order to decouple the Dirac Hamiltonian.

For details on the infinite-order DKH Hamiltonians see
M. Reiher, A. Wolf, JCP **121**, 2037–2047 (2004),
M. Reiher, A. Wolf, JCP **121**, 10945–10956 (2004).

For details on the different parametrizations of the unitary transformations see
A. Wolf, M. Reiher, B. A. Hess, JCP **117**, 9215–9226 (2002).

The current implementation is the polynomial-cost algorithm by Peng and Hirao: D. Peng, K. Hirao, JCP 130, 044102 (2009).
A detailed comparison of the capabilities of this implementation as well as the current implementation of the X2C approach is provided in:
D. Peng, M. Reiher, TCA 131, 1081 (2012).

See `here <program_control.html#example-for-computing-relativistic-corrections>`__ for an example for computing relativistic corrections.
