.. raw:: html

   <span id="adding-gradients-add"></span>

.. raw:: html

   <span id="analytical-energy-gradients"></span>

.. raw:: html

   <span id="choice-of-coordinates-coord"></span>

.. raw:: html

   <span id="defining-the-orbitals-for-scf-gradients-orbital"></span>

.. raw:: html

   <span id="difference-gradients-for-sa-mcscf-demc"></span>

.. raw:: html

   <span id="mcscf-gradients-mcscf"></span>

.. raw:: html

   <span id="non-adiabatic-coupling-matrix-elements-nacm"></span>

.. raw:: html

   <span id="numerical-gradients"></span>

.. raw:: html

   <span id="scaling-gradients-scale"></span>

.. raw:: html

   <span id="state-averaged-mcscf-gradients-with-cadpac"></span>

.. raw:: html

   <span id="state-averaged-mcscf-gradients-with-seward"></span>

.. raw:: html

   <span id="using-grid-weight-derivatives-for-dft-gradients-gridgrad"></span>

.. _energy_gradients--energy-gradients:

Energy gradients
================

.. _energy_gradients--analytical-energy-gradients:

Analytical energy gradients
===========================

Molpro uses different gradient programs:

The ``Cadpac`` gradient program is based on the ``Cadpac`` integral routines by R. D. Amos. Currently, this program works for closed shell SCF, high spin RHF, and (state averaged) MCSCF. In the MCSCF case the wavefunction must either be fully optimized, or frozen core orbitals must be taken from a closed-shell SCF calculation (but this does not work in the case of state-averaged MCSCF). Note that ``Cadpac`` does not work with generally contracted basis functions.

The ``Alaska`` gradient program is based on the ``Seward`` integral routines by R. Lindh. It allows the calculation of gradients of generally contracted basis functions for closed or open shell RHF, UHF, RKS, UKS, MCSCF, RS2 (CASPT2), local PAO-RMP2, and for closed shell MP2, LMP2, DF-LMP2, QCISD, QCISD(T), CCSD, DCSD, CCSD(T). Gradients for state averaged MCSCF wave functions can be evaluated using the RS2 gradient program, see section `State-averaged MCSCF gradients with Seward <energy_gradients.html#state-averaged-mcscf-gradients-with-seward>`__. For details about CASPT2 gradients, see section `CASPT2 gradients <multireference_rayleigh_schroedinger_perturbation_theory.html#caspt2-gradients>`__.

The ``AIC`` density fitting integral program written by G. Knizia computes two- and three-index integrals and integral derivatives. This program is used for computing gradients for the DF-MP2, DF-LMP2, DF-CCSD, DF-CCSD(T), DF-MP2-F12, DF-CCSD-F12, DF-CCSD(T)-F12, state averaged DF-MCSCF, and DF-CASPT2 methods.

By default, the program uses ``Alaska`` gradients whenever possible. However, it is possible to force the use of a particular gradient program by defining the variable ``GRADTYP`` before calling the gradient program:

``GRADTYP=ALASKA\\``
``GRADTYP=CADPAC``

The gradient program is called using the ``FORCE`` command:

``FORCE``

Normally, the ``FORCE`` command is not needed, since geometry optimizations should be performed using the ``OPTG`` procedure. An exception is the optimization of counterpoise corrected energies, which requires several force calculations (cf. section `optimizing counterpoise corrected energies <geometry_optimization_optg.html#optimizing-counterpoise-corrected-energies>`__).

The ``FORCE`` command must be given after the energy calculation to which it refers. If the command for the energy calculation (e.g. ``HF``, ``KS``, ``MP2``, etc.) is in a procedure, the ``FORCE`` must also be in the procedure. Furthermore, no procedures without an energy calculation must directly precede ``FORCE``.

If no further data cards are given, the default is to evaluate the gradient for the last optimized wavefunction. In this case no further input is needed for ordinary gradient cases (the program remembers the records on which the wavefunction information is stored). An exception is the unusual case that several different ``CPMCSCF`` calculations have been formed in a previous MCSCF calculation. In this case the ``SAMC`` directive must be used to select the desired record. If analytical gradients are not available for the last wavefunction, the gradient is computed numerically. For more details regarding numerical energy gradients see section `numerical gradients <energy_gradients.html#numerical-gradients>`__.

.. _energy_gradients--adding-gradients-add:

Adding gradients (ADD)
======================

``ADD,factor,[NOCHECK];``

If this card is present, the current gradient and energy are added to the previous ones using the given factor. This is useful for the optimization of counterpoise corrected energies (cf. `optimizing counterpoise corrected energies <geometry_optimization_optg.html#optimizing-counterpoise-corrected-energies>`__). By default, the program will stop with an error message unless ``NOORIENT`` has been specified in the geometry input. This behaviour can be disabled by the ``NOCHECK`` option. This option should only be given if all gradients which are added are evaluated at exactly the same nuclear geometry; otherwise wrong results could result due to unintended rotations of the system.

.. _energy_gradients--scaling-gradients-scale:

Scaling gradients (SCALE)
=========================

``SCALE,factor;``

If this card is present, the current gradient and energy are scaled by the give factor. This is sometimes useful for the optimization of counterpoise corrected energies (cf. `optimizing counterpoise corrected energies <geometry_optimization_optg.html#optimizing-counterpoise-corrected-energies>`__).

.. _energy_gradients--defining-the-orbitals-for-scf-gradients-orbital:

Defining the orbitals for SCF gradients (ORBITAL)
=================================================

``ORBITAL,record.file;``

In the SCF case, *record.file* specifies the location of the orbitals, which are used for constructing density matrices, etc. This card is only needed if the SCF for which the gradient is to be computed was not the most recent energy calculation.

For MCSCF wavefunctions, the ``ORBITAL`` card is not needed, because the location of the orbitals is stored in the MCSCF dump record.

.. _energy_gradients--using-grid-weight-derivatives-for-dft-gradients-gridgrad:

Using grid weight derivatives for DFT gradients (GRIDGRAD)
==========================================================

``FORCE,GRIDGRAD``\ =\ *0 or 1*

Defines whether grid weight derivatives are included in analytical gradient calculations (default: 0). Disabling these can improve convergence in geometry optimizations.

.. _energy_gradients--mcscf-gradients-mcscf:

MCSCF gradients (MCSCF)
=======================

``MCSCF,record.file;``

Triggers code for MCSCF gradient. *record.file* specifies the location of information dumped from the MCSCF program, using a ``SAVE,GRD=``\ *recmc.filmc* card. This card is not needed if the ``FORCE`` command appears directly after the corresponding MCSCF input, since the program automatically remembers where the MCSCF information was stored. The same is true if ``OPTG`` is used.

.. _energy_gradients--state-averaged-mcscf-gradients-with-seward:

State-averaged MCSCF gradients with Seward
==========================================

SA-MCSCF gradients can be computed using segmented or generally contracted basis sets using ``Seward`` and the RS2 gradient program. The ``NOEXC`` directive has to be used in the ``RS2`` input, but no ``CPMCSCF`` card is required in ``MULTI``. The RS2 gradient program does the CP-MCSCF automatically.

Example: compute SA-CASSCF gradients for :math:`^2\Pi` and :math:`^2\Sigma^+` state of OH.

.. code-block:: text
   :caption: examples/oh_samcforce.inp

   geometry={o;h,o,r}
   r=1.83
   {multi;wf,9,2,1;wf,9,3,1;wf,9,1,1}      !state averaged casscf for X(2PI) and A(2SIGMA)
   {rs2;noexc;wf,9,1,1}                    !compute A(2SIGMA) energy
   forces                                  !energy gradient for A(2SIGMA) state
   {rs2;noexc;wf,9,2,1}                    !compute A(2PI) energy
   forces                                  !energy gradient for A(2PI) state

Without the ``NOEXC`` directive, the RS2 (CASPT2) gradient would be evaluated, using the state-averaged orbitals.

.. _energy_gradients--state-averaged-mcscf-gradients-with-cadpac:

State-averaged MCSCF gradients with Cadpac
==========================================

[sec:samcgrad2] Normally, no further input is required for computing gradients for state-averaged MCSCF when ``Cadpac`` is used. Note, however, that a ``CPMCSCF,GRAD``,\ *state* directive is required in the SA-MCSCF calculation (see Section `Coupled-perturbed MCSCF <the_mcscf_program_multi.html#coupled-perturbed-mcscf>`__). The gradients are then computed automatically for the *state* specified on the ``CPMCSCF`` card. The same is true for difference gradients (``CPMCSCF,DGRAD``,\ *state1, state2*) and non-adiabatic coupling matrix elements (``CPMCSCF,NACM``,\ *state1, state2*). It is possible to do several coupled-perturbed MCSCF calculations one after each other in the same MCSCF. In this case ``FORCE`` would use the last solution by default. The information from the CPMCSCF is passed to the FORCE program in a certain records (default 5101.1, 5102.1, …). If several CPMCSCF calculations are performed in the same MCSCF, several such records may be present, and a particular one can be accessed in the ``FORCE`` program using the ``SAMC`` directive:

``SAMC,record.``

An alias for ``SAMC`` is ``CPMC``. For compatibility with earlier versions one can also use

``NACM,record``

for non-adiabatic couplings or

``DEMC,record``

for difference gradients.

Example:

.. code-block:: text

   multi;
   ....
   state,3
   cpmcscf,nacm,1.1,2.1,save=5101.1   !do cpmcscf for coupling of states 1.1 - 2.1
   cpmcscf,nacm,1.1,3.1,save=5102.1   !do cpmcscf for coupling of states 1.1 - 3.1
   cpmcscf,nacm,2.1,3.1,save=5103.1   !do cpmcscf for coupling of states 2.1 - 3.1
   
   force;samc,5101.1;                 !compute NACME for states 1.1 - 2.1
   force;samc,5102.1;                 !compute NACME for states 1.1 - 3.1
   force;samc,5103.1;                 !compute NACME for states 2.1 - 3.1

.. _energy_gradients--non-adiabatic-coupling-matrix-elements-nacm:

Non-adiabatic coupling matrix elements (NACM)
=============================================

see Section `State-averaged MCSCF gradients with Cadpac <energy_gradients.html#state-averaged-mcscf-gradients-with-cadpac>`__.

.. _energy_gradients--difference-gradients-for-sa-mcscf-demc:

Difference gradients for SA-MCSCF (DEMC)
========================================

see Section `State-averaged MCSCF gradients with Cadpac <energy_gradients.html#state-averaged-mcscf-gradients-with-cadpac>`__.

.. _energy_gradients--example:

Example
=======

.. code-block:: text
   :caption: examples/h2o_forces.inp

   ***, Calculate Gradients for Water
   alpha=104 degree           !set geometry parameters
   r=1 ang
   geometry={O;               !define z-matrix
             H1,o,r;
             H2,o,r,H1,alpha}
   basis=vdz                  !basis set
   hf                         !do scf
   forces                     !compute gradient for SCF
   mp2                        !mp2 calculation
   forces                     !mp2 gradients
   multi                      !casscf calculation
   forces                     !casscf gradient

.. _energy_gradients--numerical-gradients:

Numerical gradients
-------------------

[sec:numgrad] It is possible to compute gradients by finite differences using

``FORCE,NUMERICAL,options``

Numerical gradients are computed automatically if no analytical gradients are available for the last energy calculation. By default, no further input are needed, and the gradient will be computed for the last energy calculation. The following options can be given on the ``FORCE`` command or on subsequent directives (see subsequent sections):

* **``STARTCMD``\ =\ *command*** The input between *command* and the current ``FORCE`` command defines the energy calculation for which the gradient is computed. This input section is executed for each displacement.
* **``PROC``\ =\ *procname*** specifies a procedure to be executed for each displacement. This must define a complete energy calculation and must not contain gradient or Hessian calculations.
* **``VARIABLE``\ =\ *varname*** Compute the gradient of the value of variable *varname*. This implies numerical gradients. The variable must be set in the corresponding energy calculation.
* ``COORD=ZMAT|CART|3N`` coordinates with respect to which the gradient is evaluated. See section `choice of coordinates (COORD) <energy_gradients.html#choice-of-coordinates-coord>`__ for more information.
* ``DISPLACE=ZMAT|SYM|UNIQUE|CART``   

Displacement coordinates to be used for numerical gradient. The default is ``ZMAT`` if the geometry is given as a zmatrix which depends on variables, and ``SYM`` (symmetrical displacement coordinates) otherwise. See section `choice of coordinates (COORD) <energy_gradients.html#choice-of-coordinates-coord>`__ for more information.

* ``SYMMETRY=AUTO|NOSYM`` Symmetry to be used in wavefunction calculations of numerical gradients. This option is only relevant if ``DISPLACE=UNIQUE|CART``. If ``AUTO`` is given, the maximum possible symmetry is used for each displacement. This implies that the energy is independent of the symmetry used. Note that this often not the case in MRCI or CASPT2 calculations. The option can also not be used in local correlation calculations.
* ``AUTO`` (logical). Same as ``SYMMETRY=AUTO``
* ``ZMAT`` (logical). Same as ``COORD=ZMAT``
* ``OPT3N`` (logical). Same as ``COORD=3N``
* **``RSTEP``\ =\ *rstep*** Step length for distances in numerical gradient calculations (in bohr). The default is 0.01.
* **``DSTEP``\ =\ *dstep*** Step length for symmetrical displacements (in bohr). The default is 0.01.
* **``ASTEP``\ =\ *astep*** Step length for angles in numerical gradient calculations (in degree). The default is 1.
* ``CENTRAL`` (logical). Use 2-point central formula; needs :math:`2M` energy calculations for :math:`M` degrees of freedom.
* ``FORWARD`` (logical). Use forward gradients (needs only :math:`M+1` energy calculations, but less accurate)
* ``FOURPOINT`` (logical). Use 4-point formula for accurate numerical gradient; needs :math:`4M` energy calculations.
* ``NUMERICAL`` (logical). Force the use of numerical gradients, even if gradients are available.
* ``VARSAV`` (logical). Save gradient in variables ``GRADX``, ``GRADY``, ``GRADZ``.

Example

.. code-block:: text

   hf
   ccsd(t)
   forces,numerical

The program will then automatically repeat ``HF`` and ``CCSD(T)`` at as many geometries as needed for evaluating the gradient. This is equivalent to

.. code-block:: text

   hf
   ccsd(t)
   forces,numerical,startcmd=hf

or, using a procedure

.. code-block:: text

   forces,numerical,proc=runccsdt
   ...
   runccsdt={
   hf
   ccsd(t)}

.. _energy_gradients--choice-of-coordinates-coord:

Choice of coordinates (COORD)
=============================

By default, the numerical gradients are computed relative to all variables on which the z-matrix depends. If the z-matrix depends on no variables or on :math:`3N` variables, the gradient is computed for all :math:`3N` coordinates and symmetrical displacement coordinates are used to evaluate the gradient. This yields the minimum computational effort.

These defaults can be modified using the ``COORD`` directive:

``COORD,coord_type,[displacement_type]``

where *coord_type* can be one of the following:

* ``ZMAT`` Compute the numerical gradients for all variables on which the geometry depends (default).
* **``3N`` or ``CART``** Compute the gradients for all :math:`3N` nuclear coordinates. This is the default if the z-matrix does not depend on variables or if the ``xyz`` input format is used. If this option is used and the original geometry is given in z-matrix form, the z-matrix is lost.

The specification of *displacement_type* is optional and only affects the numerical calculation of the gradient for :math:`3N` coordinates. It can also be given using

``DISPLACE,displacement_type``

*displacement_type* can be one of the following:

* ``SYM`` Use symmetrical displacements. This yields the minimum number of displacements and always preserves the symmetry of the wavefunction. This is the default and only recommended option.
* ``CART`` Displacements are generated for all :math:`3N` Cartesian coordinates. This is normally not recommended, since in cases in which molecular symmetry is present it generates far more displacements than needed. Also, the wavefunction symmetry is not preserved, and the calculation must be done in C1 symmetry.
* ``UNIQUE`` As ``CART``, but symmetry-equivalent displacements are eliminated. Not recommended either.

.. _energy_gradients--numerical-derivatives-of-a-variable:

Numerical derivatives of a variable
===================================

Numerical derivatives of the value of a variable can be computed using

``VARIABLE,name``

The default is to compute the gradient of the current energy.

.. _energy_gradients--step-sizes-for-numerical-gradients:

Step-sizes for numerical gradients
==================================

By default, the numerical step sizes are 0.01 bohr for distances or Cartesian coordinates, and 1 degree for angles. These defaults can be changed using

``RSTEP,dr\\``
``ASTEP,da``

where *dr* is the displacement for distances (or Cartesian coordinates) in bohr, and *da* is the displacement for angles in degree. The value of ``RSTEP`` is used for symmetrical displacements. The step sizes for individual variables can be modified using

``VARSTEP,varname=value,…``

where the *value* must be in atomic units for distances and in degree for angles.

.. _energy_gradients--active-and-inactive-coordinates:

Active and inactive coordinates
===============================

By default, numerical gradients are computed with respect to all variables on which the Z-matrix depends, or for all :math:`3N` coordinates if there are no variables or ``XYZ`` inputstyle is used. One can define subsets of active variables using

``ACTIVE,variables\\``
If this card is present, all variables which are not specified are inactive. Alternatively,

``INACTIVE,variables``

In this case all variables that are not given are active.

.. _energy_gradients--saving-the-gradient-in-a-variables:

Saving the gradient in a variables
----------------------------------

If the directive

``VARSAV``

is given, the gradient is saved in variables ``GRADX``, ``GRADY``, ``GRADZ``. ``GRADX(n)`` is the derivative with respect to :math:`x` for the :math:`n`-th atom. The atoms are in the order as printed. This order can be different from the order in the input z-matrix, since the centres are reordered so that all atoms of the same type follow each other.
