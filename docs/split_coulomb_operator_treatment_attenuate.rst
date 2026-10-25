.. _split_coulomb_operator_treatment_attenuate--split-coulomb-operator-treatment-attenuate:

Split Coulomb operator treatment (ATTENUATE)
============================================

This directive activates the method described in

G. Hetzer, M. Schütz, H. Stoll, and H.-J. Werner, *Low-order scaling local electron correlation methods II: Splitting the Coulomb operator in linear scaling local MP2*, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.1321295>`__ **113**, 9443 (2000).

This is currently not recommended for general use and we will give no support in case of trouble with this method.

The method relies on the partitioning of the Coulomb operator into a rapidly decaying short range part containing the singularity and a smooth long range part. The integrals over both parts of the Coulomb operator are then treated separately. The short range integrals are obtained by transformation of the short range integrals in the AO basis, which is faster than the conventional transformation as more efficient screening is possible. The long range integrals are treated by a multipole expansion. In contrast to conventional multipole expansions, this expansion has an infinite radius of convergence. The method is available by replacing the ``LOCAL`` or ``MULTP`` directive by the ``ATTENUATE`` directive.

``ATTENUATE,[key1=value],[key2=value2], $\ldots$``

It does everything the ``MULTP`` directive does (i. e., distant pairs are still treated by ordinary multipole expansion), plus it will enable the split Coulomb operator treatment of weak and strong pairs and select reasonable defaults. See section `summary of options <pao-based_local_correlation_treatments.html#summary-of-options>`__ for details. If you don’t want distant pairs to be treated by ordinary multipole expansion, simply specify ``DISTPAIR=0`` on the ``ATTENUATE`` directive. Note that this method will only work in the context of integral-direct calculations.

.. _split_coulomb_operator_treatment_attenuate--additional-options-available-on-the-attenuate-directive:

Additional options available on the ATTENUATE directive
=======================================================

Summary of ``attenuate`` options and their default values

.. list-table::
   :header-rows: 9

   * - Parameter
     - Default value
     - Meaning
   * - Most important options
     - 
     - 
   * - ``DECAY``
     - 0.20
     - split parameter :math:`\omega`
   * - ``SHORTMLT``
     - 15
     - level :math:`p` of monopolar multipole expansion
   * - ``LONGMLT``
     - 13
     - level :math:`p` of bipolar multipole expansion
   * - Specifying which integrals to treat by which multipole expansion type
     - 
     - 
   * - ``RMAIN``
     - 1
     - when to switch from monopolar to four-block treatment
   * - ``RIONIC``
     - 0
     - when to switch from monopolar to bipolar treatment of ionic blocks
   * - ``SUPPRESS``
     - 0
     - when to suppress cross-excited blocks
   * - Options for least squares fit generation of interaction coefficients
     - 
     - 
   * - ``FITMLTP``
     - 1
     - use least squares fit instead of Taylor
   * - ``F1DGRID``
     - 50
     - no. of quadrature points for 1D fit
   * - ``F2DGRIDR``
     - 50
     - no. of quadrature points for 2D fit :math:`r`
   * - ``F2DGRIDP``
     - 20
     - no. of quadrature points for 2D fit :math:`\phi`
   * - ``F1DBORDER``
     - 0
     - end of integration interval for 1D fit
   * - ``F2DBORDER``
     - 0
     - end of integration interval for 2D fit :math:`r`
   * - ``F1DGAMMA``
     - 1.7
     - negative exponent of weight function for 1D fit
   * - ``F2DGAMMA``
     - 1.7
     - negative exponent of weight function for 2D fit
   * - ``WEIGHT3D``
     - 1
     - use spacial instead of flat weight function
   * - Options for determination of batches
     - 
     - 
   * - ``NUMBATCH``
     - 0
     - manually set number of batches
   * - ``BATCHDIAM``
     - 35
     - maximal diameter of batches
   * - ``BATCHALGO``
     - 2
     - algorithm to determine batches
   * - ``WEIGHTPREV``
     - 0.5
     - parameter for algorithm ``BATCHALGO=1``
   * - ``RANSEED``
     - -1
     - initialize random number generator for simulated annealing
   * - Further numerical stability options
     - 
     - 
   * - ``CUTOFF``
     - 15
     - orbital cutoff
   * - ``MONOPOLE``
     - 1
     - if and how to treat monopole integrals
   * - Multipole operators
     - 
     - 
   * - ``MAXMLTPL``
     - *auto*
     - manually set level of multipole operators to create
   * - ``MULTPAGE``
     - 1
     - turn on paging of multipole operators during multipole expansion
   * - Essentially obsolete options (for Taylor expansion)
     - 
     - 
   * - ``TRUNCATE``
     - 0
     - truncation pattern of multipole expansion
   * - ``DAMP``
     - 0
     - damping function for orbitals
   * - ``SCALEDAMP``
     - 0
     - scaling factor for the damping function
   * - Stuff for debugging
     - 
     - 
   * - ``PAIREN``
     - 0
     - print a list of uncoupled pair energies

The defaults reported for the following options are likely to change in the future.

**Most important options**

* **``DECAY``\ =\ :math:`\omega`** This is the decay parameter that determines the splitting of the Coulomb operator in the split approach. Larger values of :math:`\omega` put more weight to the long range part of the operator, which means that the multipole correction will have more difficulties to converge but the transformation of the short range part will be faster. Default: 0.20
* **``SHORTMLT``\ =\ *level*** Determines the expansion level of monopolar multipole expansions in the context of the split Coulomb operator approach. Default: 15
* **``LONGMLT``\ =\ *level*** Determines the expansion level of bipolar multipole expansions in the context of the split Coulomb operator approach. Default: 13

**Specifying which integrals to treat by which multipole expansion type**

* **``RMAIN``\ =\ *distance*** When the distance between two orbitals is closer than the absolute value of *distance*, multipole corrections (in the context of the split approximation) will be carried out as monopolar expansions, otherwise a more sophisticated approach will be used involving four expansions for each pair, one for the ordinary dispersion block of the exchange matrix for the given pair, two for the two ionic exchange blocks and one for the exchange-dispersion block (see the section on energy partitioning for explanation of these terms). If *distance* is a positive value, the distance between the orbitals will be taken to be the distance between the closest atoms of the two orbital domains (as in ``WEAKPAIR``, ``DISTPAIR`` etc.), if it is a negative value, the distance of the centroids of the two orbitals will be considered. Default: 1
* **``RIONIC``\ =\ *distance*** When the distance between two orbitals is closer than *distance* [a.u.], the multipole correction of ionic blocks of the exchange operators will be carried out as monopolar expansion, otherwise a bipolar expansion will be performed. The distance is understood as the distance of the centroids of the two orbitals. Default: 0
* **``SUPPRESS``\ =\ *distance*** When the distance between two orbitals (distance of centroids) is higher than the absolute value of *distance* [a.u.], the multipole correction of the exchange-dispersion blocks of the exchange operators is suppressed. If a positive value is given, the multipole correction of the ionic exchange blocks is also suppressed. A zero value disables the suppression of multipole corrections. Default: 0

**Options for least squares fit generation of interaction coefficients**

* **``FITMLTP``\ =\ *option*** Specifies how the coefficients for the multipole expansion of long range integrals are calculated.

  * *option=0*: Taylor expansion
  * *option=1*: Least squares fit
  * Default: 1
* **``F1DGRID``\ =\ *value*** Sets the number of quadrature points used to generate integrals that arise in the one-dimensional fit (i.e. for the monopolar multipole expansion). Default: 50
* **``F2DGRIDR``\ =\ *value*** Sets the number of quadrature points used along the :math:`r` (radial) coordinate when generating integrals for the two-dimensional fit (i.e. for the bipolar multipole expansion). Default: 50
* **``F2DGRIDP``\ =\ *value*** Sets the number of quadrature points used along the :math:`\phi` (angular) coordinate for the two-dimensional integrals. Default: 20
* **``F1DBORDER``\ =\ *value*** If greater than 0, sets the upper bound of integration (in bohr) and selects the Gauss–Legendre quadrature for the one-dimensional integrals. If 0, selects Gauss–Laguerre quadrature. Default: 0
* **``F2DBORDER``\ =\ *value*** The same for the two-dimensional integrals.
* **``F1DGAMMA``\ =\ :math:`\gamma`** Sets the negative exponent of the weight function for the one-dimensional fit. Smaller values are better for more diffuse densities. Should be positive (leading to a negative exponent). Default: 1.7
* **``F2DGAMMA``\ =\ :math:`\gamma`** The same for the two-dimensional fit.
* **``WEIGHT3D``\ =\ *option*** Selects what type of weight function is used for the fits.

  * *option=0*: Flat
  * *option=1*: Spatial
  * Remember to change ``F1DGAMMA/F2DGAMMA`` accordingly when using a flat weight function, :math:`\gamma=1.0` is then a reasonable value. Default: 1

**Options for determination of batches**

* **``NUMBATCH``\ =\ *value*** If 0, selects automatic determination of the number of batches. If >0, provides a manual override for this number. Default: 0
* **``BATCHDIAM``\ =\ *value*** Maximal acceptable diameter of batches. Used to automatically determine the number of batches. If zero, disables batches (i.e., only one batch will be created). Default: 35
* **``BATCHALGO``\ =\ *option*** Selects the algorithm used to determine the batches.

  * *option=0*: Manually set batch centres. Three arrays with name ``BATCHX``, ``BATCHY``, ``BATCHZ`` have to be set in the input before the ``MP2`` command that contain the :math:`x`-, :math:`y`- and :math:`z`-coordinates of the desired batch centres.
  * *option=1*: Simple algorithm: Determines a path through the molecules and distributes the batch centres along this path.
  * *option=2*: A robust simulated annealing algorithm. Will only use atom positions as batch centres, might therefore fail for strongly separated dimers and similar systems where there is no atom near the optimal batch centre position.
  * *option=3,4*: A less robust simulated annealing algorithm that directly tries to optimize the batches instead of the batch centres.
  * Default: 2
* **``WEIGHTPREV``\ =\ *value*** Affects the one-dimensional path laid through the molecule for ``BATCHALGO=1``. Smaller values mean a more systematic, directed order of atoms from one end to the other. Larger values mean that the distance from one atom in the path to the next will become smaller. Has to be between 0 and 1. Default: 0.5
* **``RANSEED``\ =\ *value*** Negative values initialize the random number generator for the simulated annealing algorithms. Positive numbers suppress initialisation of the random number generator. Default: -1

**Further numerical stability options**

* **``CUTOFF``\ =\ *distance*** Applies a simple cutoff to orbitals before the transformation of the multipole operators. Orbital coefficients belonging to AOs that are more than *distance* [a.u.] away from the orbital centre will be deleted. *distance*\ =0 means don’t use a cutoff. Default: 15
* **``MONOPOLE``\ =\ *option*** Specifies how to treat monopole integrals. Monopole integrals should be zero due to the orthogonality between occupied and virtual orbitals. Therefore, they are usually not included in the calculation. However, this does not hold exactly when an orbital cutoff is applied. Including monopole integrals in the calculation might therefore improve the numerical stability.

  * *option=0*: Neglect monopole integrals
  * *option=1*: Use monopole integrals in the translation, but neglect them later on
  * *option=2*: Use monopole integrals everywhere (translation and expansion), only neglect monopole–\ :math:`2^{p+1}`\ pole interactions, where :math:`p` is the requested multipole level
  * *option=3*: Use monopole integrals everywhere (translation and expansion), but neglect all monopole–\ :math:`2^{p+1}`\ pole, dipole–\ :math:`2^p`\ pole, quadrupole–\ :math:`2^{p-1}`\ pole interactions and so on. This is entirely consistent, but reduces the effective multipole level by 1 as compared to the other options.
  * Default: 1

**Multipole operators**

* **``MAXMLTPL``\ =\ *option*** Defines the highest level of multipole operators that are created. Has to be greater or equal than each of ``DSTMLT``, ``LONGMLT`` and ``SHORTMLT``, is otherwise overwritten by the default, which is max(``DSTMLT``, ``LONGMLT``, ``SHORTMLT``). Greater values are a useless waste of CPU unless you save the operators for later reuse.
* **``MULTPAGE``\ =\ *option*** *option=0*: Suppress paging of multipole operators during multipole expansion. After their creation, all operators are read from disk into memory. Will crash if not enough memory is available.

  * *option=1*: Read operators from disk when needed. Small performance impact.
  * Default: 1

**Essentially obsolete option (for Taylor expansions)**

* **``TRUNCATE``\ =\ *option*** Determines if the simple or exhaustive truncation truncation scheme will be used for multipole expansions. Exhaustive truncation means that, unlike a classical multipole expansion, all interactions of multipoles up to the highest order are taken into account, e. g. in an expansion of level two, the exhaustive scheme will include quadrupole-quadrupole terms while the simple scheme won’t. Valid options are:

  * *option=0*: Always use simple truncation.
  * *option=1*: Use simple truncation for bipolar expansions, but exhaustive truncation for monopolar expansions. This significantly improves convergence when a Taylor expansion is used, but also accelerates the onset of divergent behaviour for large expansion levels and should therefore always be used in connection with a damping function for multipole operators.
  * *option=2*: Use simple truncation for monopolar expansions, but exhaustive truncation for bipolar expansions including distant pair treatment.
  * *option=3*: Always use exhaustive truncation.
  * The latter two options are not useful and only included for the sake of completeness. Default: 0
* **``DAMP``\ =\ *order*** Specifies the form of a damping function that is applied to orbitals before the transformation of the multipole operators. *order* is actually the order of a Taylor series that is part of the function and that mimics the behaviour of the monopolar multipole expansion. Only multiples of 4 are reasonable values. Higher values mean a harder damping function (i. e. less damping at short distances, but more at long distances). A value of 0 disables the damping. A value of 8 is recommended when using a Taylor expansion. Default: 0
* **``SCALEDAMP``\ =\ *scalefactor*** The damping function can additionally be scaled by the value of *scalefactor*. A value lower than 1 means the damping function will be squeezed, while a value higher than 1 will cause it to be stretched. A value of 0 disables the scaling (as well as 1). A value of 0.9 is recommended when using a Taylor expansion. Default: 0

**Stuff for debugging**

* **``PAIREN``\ =\ *option*** Prints a list of uncoupled pair energies before the MP2 iterations. Can be used as a convenient diagnostic when getting totally implausible correlation energies or no convergence or "UNREASONABLE NORM" messages.
