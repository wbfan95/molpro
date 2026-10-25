.. raw:: html

   <span id="adding-cabs-singles-correction-in-ccsd-t-f12-geometry-optimization"></span>

.. raw:: html

   <span id="conical-intersection-optimization-conical"></span>

.. raw:: html

   <span id="constraint-optimisations-using-the-pqs-optimizer"></span>

.. raw:: html

   <span id="defining-active-geometry-parameters-active"></span>

.. raw:: html

   <span id="defining-inactive-geometry-parameters-inactive"></span>

.. raw:: html

   <span id="directives-for-optg"></span>

.. raw:: html

   <span id="hessian-approximations-hessian"></span>

.. raw:: html

   <span id="hessian-elements-hesselem"></span>

.. raw:: html

   <span id="hessian-update-update"></span>

.. raw:: html

   <span id="line-searching-linesearch"></span>

.. raw:: html

   <span id="miscellaneous-options"></span>

.. raw:: html

   <span id="numerical-gradients-numerical"></span>

.. raw:: html

   <span id="numerical-hessian-numhess"></span>

.. raw:: html

   <span id="optimization-coordinates-coord"></span>

.. raw:: html

   <span id="optimizing-counterpoise-corrected-energies"></span>

.. raw:: html

   <span id="optimizing-energy-variables-variable"></span>

.. raw:: html

   <span id="options-for-computing-hessians"></span>

.. raw:: html

   <span id="options-for-numerical-gradients"></span>

.. raw:: html

   <span id="options-for-optimization-methods"></span>

.. raw:: html

   <span id="options-for-the-pqs-optimizer"></span>

.. raw:: html

   <span id="options-to-modify-convergence-criteria"></span>

.. raw:: html

   <span id="options-to-select-the-wavefunction-and-energy-to-be-optimized"></span>

.. raw:: html

   <span id="printing-options-print"></span>

.. raw:: html

   <span id="reaction-path-following-options-option"></span>

.. raw:: html

   <span id="redefining-the-trust-ratio-trust"></span>

.. raw:: html

   <span id="selecting-the-optimization-method-method"></span>

.. raw:: html

   <span id="setting-a-cut-parameter-cut"></span>

.. raw:: html

   <span id="setting-a-maximum-step-size-step"></span>

.. raw:: html

   <span id="transition-state-saddle-point-optimization-root"></span>

.. _geometry_optimization_optg--geometry-optimization-optg:

Geometry optimization (OPTG)
============================

Automatic geometry optimization is invoked using the ``OPTG`` command. The ``OPT`` command available in previous MOLPRO versions is no longer needed and not available any more.

``OPTG[, key1=value, key2=value,…...]``

The ``OPTG`` command can be used to perform automatic geometry optimizations for all kinds of wavefunctions. For minimum searches, it is usually sufficient to give just the ``OPTG`` command without further options or directives, but many options are available which are described in the following sections.

The ``OPTG`` command must be given after the energy calculation to which it refers. If the commands for the energy calculation (e.g. ``HF``, ``KS``, ``MP2``, etc.) are in a procedure, the ``OPTG`` must also be in the procedure. Furthermore, no procedures without an energy calculation must directly precede ``OPTG``.

Various optimization methods can be selected as described in section `selecting the optimization method (METHOD) <geometry_optimization_optg.html#selecting-the-optimization-method-method>`__.
Molpro allows minimization (i.e. search for equilibrium geometries), transition state optimization (i.e. search for saddle points on energy surfaces), and reaction path following. Since Molpro 2023.1 the optimizer developed by J. Baker and P. Pulay (PQSOPT) is available in Molpro and used by default. The method is described in
J. Baker et al., J. Chem. Phys. 105, 192 (1996);
J. Baker and P. Pulay, J. Chem. Phys. 105, 11100 (1996);
J. Baker, J. Comput. Chem. 18, 1079 (1997);
J. Baker and P. Pulay, J. Comput. Chem. 21, 69 (2000).
It uses delocalized internal coordinates and converges often better than previous optimisers in Molpro. Furthermore, it allows for constraint optimisations. Other available algorithms are based on the *rational function* approach and the *geometry DIIS* approach. Also available is the *quadratic steepest descent following* method of Sun and Ruedenberg (see J. Sun and K. Ruedenberg, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.465994>`__ **99**, 5257 (1993)). This method is often advantageous in Transition State searches. For a detailed discussion of the various older minimization algorithms see F. Eckert, P. Pulay and H.-J. Werner, *J. Comp. Chem* **18**, 1473 (1997). Reaction path following is described in F. Eckert and H.-J. Werner, *Theor. Chem. Acc.* **100**, 21, (1998). Please refer to the references section for citations of the analytic gradient methods.

When analytical gradients are available for the optimized energy these will be used. See section `analytical energy gradients <energy_gradients.html#analytical-energy-gradients>`__ for a list of methods with analytical gradients. Otherwise the gradient will be computed numerically from finite energy differences. Normally, the last computed ground-state energy is used. But the ``VARIABLE`` directive or option can be used to optimize, e.g., Davidson corrected energies, excited states, or counterpoise corrected energies.

By default the program repeats in each geometry optimization step those commands in the input that are needed to compute the last energy *and* any ``variable=value`` assignments in between the last energy calculation and the ``OPTG`` command. For example, for MP2 gradients the commands HF and MP2 are needed. The MP2 gradients will then be computed automatically. Variables set by these programs as, e.g., ``ENERGY``, are set as usual in each optimization step. In addition, there is a variable ``OPTSTEP``, which is incremented in each optimization step. Its initial value is zero. To save the results of the initial energy calculation, one can use, e.g.,

``hf\\``
if(optstep.eq.0) e1=energy
``optg\\``

It is also possible to define procedures for the energy calculation, or to specify the first command from which the input should be repeated in each step (see section `options to select the wavefunction and energy to be optimized <geometry_optimization_optg.html#options-to-select-the-wavefunction-and-energy-to-be-optimized>`__). The section of the input which is needed for the geometry optimization must not modify variables that are used in the geometry definition (changes of such variables are ignored, and a warning message is printed).

.. _geometry_optimization_optg--options:

Options
=======

Most parameters can be given as options on the ``OPTG`` command line, as described in this section. Alternatively, directives can be used, which will be described in section `directives for OPTG <geometry_optimization_optg.html#directives-for-optg>`__.

.. _geometry_optimization_optg--options-to-select-the-wavefunction-and-energy-to-be-optimized:

Options to select the wavefunction and energy to be optimized
=============================================================

By default, the last computed energy is optimized, and all commands on which the last energy calculation depends are automatically executed. For certain purposes, e.g., optimization of counter-poise corrected energies or Davidson corrected energies, the following options can be used to alter the default behaviour.

* **``STARTCMD``\ =\ *command*** Specifies a start command. In each geometry optimization step all input beginning with *command* to the current ``OPTG`` is processed. This input must not include numerical gradient or Hessian calculations. If numerical gradients are needed, these will be computed for the final energy (or specified variable) by ``OPTG``. It is assumed that these commands have been executed before entering the ``OPTG`` program.
* **``PROC``\ =\ *procname*** specifies a procedure to be executed in each geometry optimization step. This must define a complete energy calculation (orbital optimization and correlation treatment), and must not include numerical gradient of Hessian calculations (numerical gradients will be computed automatically for the optimized energy or variable). However, the procedure can include the calculation of analytical gradients, for instance for counter-poise corrected optimizations in which a linear combination of several gradient calculations is needed.
* **``VARIABLE``\ =\ *varname*** Optimize the value of variable *varname*. This implies numerical gradients.

.. _geometry_optimization_optg--options-for-optimization-methods:

Options for optimization methods
================================

* **``METHOD``\ =\ ``PQS|RF|AH|DIIS|QSD|QSDPATH|SRMIN|SRTRANS|STSTEEP``**   

Optimization method to be used. See section `selecting the optimization method (METHOD) <geometry_optimization_optg.html#selecting-the-optimization-method-method>`__ for details.

* **``ROOT``\ =1\ :math:`|`\ 2** Minimum search (1, default) or transition state search (2).
* **``DIRECTION|IDIR``\ =\ *idir*** Determines initial step length and direction in reaction path following, see section `reaction path following options (OPTION) <geometry_optimization_optg.html#reaction-path-following-options-option>`__.
* **``STPTOL``\ =\ *value*** For reaction path following, see section `reaction path following options (OPTION) <geometry_optimization_optg.html#reaction-path-following-options-option>`__.
* **``SLMAX``\ =\ *value*** For reaction path following, see section `reaction path following options (OPTION) <geometry_optimization_optg.html#reaction-path-following-options-option>`__.
* **``STEPMAX``\ =\ *value*** Max step length in one optimization step. This also affects the step length in reaction path following. For more detailed specifications see section `setting a maximum step size (STEP) <geometry_optimization_optg.html#setting-a-maximum-step-size-step>`__.
* ``ROTATE`` (logical). If .true., the Cartesian coordinates are transformed to minimize rotations (default=.true.)

The following options are not available in PQSOPT:

* **``TRUST``\ =\ *value*** Trust ratio for Augmented Hessian method (default 0.5).
* **``AHMAX``\ =\ *value*** Maximum step size allowed in the Augmented Hessian procedure. This refers to the scaled parameter space (default 0.5).
* **``CUT``\ =\ *value*** Threshold for orthonormalization used in conjugate gradient update of Hessian (default 1.d-3).

Specific options for PQSOPT (for details see `options for the PQS optimizer <geometry_optimization_optg.html#options-for-the-pqs-optimizer>`__):

* **``OPTC``\ =\ *value*** This determines the coordinate type (default -1)
* **``IGEN``\ =\ *value*** This determines whether the internal coordinates are regenerated in each step (default 1)
* **``TYPE``\ =\ *value*** Special flag for surface/cluster optimizations (default 0)
* **``ICONS``\ =\ *value*** Special flag for constraint optimisations (default 0)

.. _geometry_optimization_optg--options-for-the-pqs-optimizer:

Options for the PQS optimizer
=============================

Convergence criteria can be specified as for other methods using the ``ENERGY``, ``GRADIENT``, and ``STEP`` options (see `options to modify convergence criteria <geometry_optimization_optg.html#options-to-modify-convergence-criteria>`__).

The maximum stepsize can be specified using the ``STEPMAX`` option (see `options for optimization methods <geometry_optimization_optg.html#options-for-optimization-methods>`__)

``Transition state optimization can be activated by setting option ROOT=2.``

Options for numerical gradients and Hessian options work as for other optimization programs (see
`options for numerical gradients <geometry_optimization_optg.html#options-for-numerical-gradients>`__ and
`options for computing Hessians <geometry_optimization_optg.html#options-for-computing-hessians>`__).

There are many further options, but only the following may be sometimes relevant:

``OPTC:``

* ``OPTC= 1`` - generate and optimize in internal coordinates; if this fails abort
* ``OPTC=-1`` - generate and optimize in internal coordinates; if this fails switch to Cartesians and continue (default)
* ``OPTC= 2``- optimize in Z-Matrix internal coordinates (not supported in Molpro)
* ``OPTC=-2`` - optimize in Z-Matrix internal coordinates (not supported in Molpro)
* ``OPTC= 3`` - large-molecule optimization in Cartesian coordinates (never tested so far)
* ``OPTC= 4`` - large-molecule optimization in delocalized internals (never tested so far)

``IGEN:``

* ``IGEN=0`` - generate a set of non-redundant internals and use throughout the optimization
* ``IGEN=1``  - generate a new set of non-redundant internals from the same primitive space every cycle (default)
* ``IGEN=2``  - generate a new set of underlying primitives and a new set of non-redundant internals every cycle (not recommended)

``ITYPE:``

* ``ITYPE=0`` - standard molecular optimization (default)
* ``ITYPE=1`` - optimization of molecule reacting/adsorbed on model surface
* ``ITYPE=2`` - optimization of molecular clusters (see below)

``ICONS:``

* ``ICONS=0`` - full optimization (no constraints, default)
* ``ICONS=1`` - constrained optimization using Lagrange multipliers (default if constraints are given see `constraint optimisations using the PQS optimizer <geometry_optimization_optg.html#constraint-optimisations-using-the-pqs-optimizer>`__)
* ``ICONS=2`` - constrained optimization using penalty functions

``Cluster optimizations:``

Cluster optimizations use inverse distance coordinates for intermolecular degrees of freedom.

* ``MOLECULES=[//n1,n2,n3,...//]`` - For cluster optimisations. The molecules must come one after the other in the geometry input. *``n1``, ``n2``,...* are the number of atoms in each molecule. The sum of these must be equal to the total number of atoms. This option sets automatically ``ITYPE=2``

.. code-block:: text

* ``CUTOFF=//value//`` - Distance cutoff for intermolecular coordinates in Angstrom. The program will generate inverse distance coordinates for between all atoms of different molecules, unless the distance is larger than this value. Default: 5 Angstrom.

* ``SCALE=//value//`` - Scaling factor for inverse distance coordinates. Typical values are between 1 and 10. Default is 1.0

Unfortunately, according to our current limited experience, the cluster optimization in pqsopt is neither well working in the original PQS program nor in Molpro and should therefore be used with care.

.. code-block:: text

``Optimizations with z-matrix input:``

By default, optimizations with z-matrix geometry input are done with the old RF optimizer, and only the active variables in the z-matrix are optimised (cf. `Defining active geometry parameters <geometry_optimization_optg.html#defining-active-geometry-parameters-active>`__). It is possible, however, to force pqs optimization by giving the optg option ``PQS`` or ``METHOD=PQS``. In this case, all cartesian coordinates will be optimised, and in each iteration the new structure is back-transformed to the z-matrix. If the z-matrix contains constants, these may change and will be overwritten. If the same variable is used in several places of the z-matrix and the corresponding new parameters are not the same, the variable is only kept in the first place, and the further ones are overwritten by the new fixed parameters. The updated z-matrix is printed in the log-file in each iteration.

.. _geometry_optimization_optg--constraint-optimisations-using-the-pqs-optimizer:

Constraint optimisations using the PQS optimizer
================================================

Constraints can be be defined in an input block (with the OPTG command block) beginning with ``CONSTRAINT`` and ending with ``END``. The possible coordinate types are:

.. code-block:: text

* ``STRE      //I  J              value//`` (Angstrom)   
* ``BEND      //I  J  K           value//`` (degrees)  
* ``TORS      //I  J  K  L        value//`` (degrees)  
* ``OUTP      //I  J  K  L        value//`` (degrees)  
* ``LINC      //I  J  K  L        value//`` (degrees)  
* ``LINP      //I  J  K  L        value//`` (degrees)  

where *I, J, K, L* refer to row numbers in the XYZ input. Alternatively, atom symbols like, e.g. H1, O, H2, can be given, but these must be unique in the input geometry. The coordinate types are:

``STRE distance constraint between any two (different) atoms.\\``
``BEND planar bend constraint between any three (different) atoms. J is the middle atom of the bend.\\``
``TORS dihedral angle (proper torsion) constraint between any four (different) atoms.``
The connectivity is I-J-K-L, with J-K being the central “bond”.
The angle is between the planes I-J-K and J-K-L.
``OUTP out-of-plane-bend constraint between any four (different) atoms. The angle is made by bond I-L with the plane J-K-L (L is the central atom) \\``
``LINC colinear bending constraint between any four (different) atoms. Bending of I-J-K in the plane J-K-L.\\``
``LINP perpendicular bending constraint between any four (different) atoms. Bending of I-J-K perpendicular to the plane J-K-L.\\``

``LINC/LINP are special angles used when four atoms are near-linear.``

The constraint values have not to be satisfied in the initial geometry. If *value* is not given, the initial value will be kept.
The number of constraints is in principle arbitrary, but currently restricted to 20.

Example: Keep the distance between atoms 2 and 3 to 1.5 ANG:

.. code-block:: text

``{OPTG\\``
CONSTRAINT
STRE,2,3,1.5
``END}\\``

**Composite constraints:**

It is possible to define linear combinations of primitive internal coordinates as constraints. These must be defined after the simple constraints (if present). Each composite constraint begins with the keyword ``COMPOSITE``. The input of each primitive is as described above, but the ``weight`` (the factor in the linear combination) replaces ``value``. The value is given at the end of the first line. Angles in the linear combinations are in radians. The general structure is:

``{OPTG,options\\``
``CONSTRAINT\\``
*simple constrains* (if present)
``COMPOSITE\\``
*type atom_list weight value*
*type atom_list weight*
...
``END}\\``

*value* is the total value of the combined constraint. Note that the weights are normalised. Example:

``COMPOSITE\\``
STRE I J    1.0
STRE J K   -1.0
BEND I J K  2.0
``END\\``

will constrain the value of :math:`6^{-1/2}(R_{IJ} - R_{JK} + 2 A_{IJK})` to whatever it is in the starting geometry.

Currently, the total number  of composite constraints is limited to 20. Note that there is no checking for incompatible or impossible constraints, and it is the user's responsibility to make correct definitions.

.. _geometry_optimization_optg--options-to-modify-convergence-criteria:

Options to modify convergence criteria
======================================

The standard Molpro convergency criterion requires the maximum component of the gradient to be less then :math:`3 \cdot 10^{-4}` [a.u.] and the maximum energy change to be less than :math:`1 \cdot 10^{-6}` [H] *or* the maximum component of the gradient to be less then :math:`3 \cdot 10^{-4}` [a.u.] and the maximum component of the step to be less then :math:`3 \cdot 10^{-4}` [a.u.].

It is also possible to use the convergency criterion of the Gaussian program package. It is somewhat weaker than the Molpro criterion and requires the maximum component of the gradient to be less then :math:`4.5 \cdot 10^{-4}` [a.u.] and the root mean square (RMS) of the gradient to be less then :math:`3\cdot 10^{-4}` [a.u.] as well as the maximum component of the optimization step to be less then :math:`0.0018` [a.u.] and the RMS of the optimization step to be less then :math:`0.0012` [a.u.].

* **``MAXIT``\ =\ *maxit*** maximum number of optimization cycles. The default is 100. It cannot be increased above 100. If an optimization did not work, restart from e.g. the structure with the lowest energy using the information in the correspoing log-file (suffix .log).
* **``GRADIENT``\ =\ *thrgrad*** required accuracy of the optimized gradient. The default is :math:`3 \cdot 10^{-4}`.
* **``ENERGY``\ =\ *threnerg*** required accuracy of the optimized energy. The default is :math:`1 \cdot 10^{-6}`.
* **``STEP``\ =\ *thrstep*** convergence threshold for the geometry optimization step. The default is :math:`3 \cdot 10^{-4}`.
* ``BAKER`` (logical). Use Baker’s convergency criteria (see J. Baker, *J. Comp. Chem.* **14**,1085 (1993)).
* ``GAUSSIAN`` (logical). Use Gaussian convergency criteria.
* **``SRMS``\ =\ *thrsrms*** sets (for Gaussian convergency criterion) the required accuracy of the RMS of the optimization step. The default is :math:`0.0012`.
* **``GRMS``\ =\ *thrgrms*** sets (for Gaussian convergency criterion) the required accuracy of the RMS of the gradient. The default is :math:`3 \cdot 10^{-4}`.
* **``FREEZE``\ =\ *thrfreez*** Freeze DFT grid and domains in local calculations if the step length is smaller than *thrfreez* (default 0.01).

Note: The defaults for the convergence parameters can also be changed by using a global ``GTHRESH`` directive, i.e.

``GTHRESH, OPTSTEP=step, OPTGRAD=grad, ENERGY=energy;``

.. _geometry_optimization_optg--options-to-specify-the-optimization-space:

Options to specify the optimization space
=========================================

If the geometry is given as Z-matrix, the default is to optimize the variables on which the Z-matrix depends. In case of ``xyz`` input, always all 3N coordinates are optimized, even if the ``xyz`` input depends on fewer variables. If Cartesian z-matrix input is used, optimization in full space is only enforced if automatic orientation is requested using the ``MASS``, or ``CHARGE`` options on the ``ORIENT`` directive. See *opt_space* in section `optimization coordinates (COORD) <geometry_optimization_optg.html#optimization-coordinates-coord>`__ for details.

* ``SPACE=ZMAT|3N`` Specifies the coordinates to be used in the optimization. Z-matrix optimization is only possible if the geometry is given as Z-matrix.
* ``OPT3N|3N`` (logical). Same as ``SPACE=3N``
* ``ZMAT`` (logical). Same as ``SPACE=ZMAT``

.. code-block:: text

.. _geometry_optimization_optg--options-to-specify-the-optimization-coordinates:

Options to specify the optimization coordinates
===============================================

These options specify the coordinates in which the optimization takes place. The default is to use local normal coordinates. See *opt_coord* in section `optimization coordinates (COORD) <geometry_optimization_optg.html#optimization-coordinates-coord>`__ for details.

* ``COORD=DELO[CALIZED]|NORMAL|NONORMAL|BMAT``
* ``NORMAL`` (logical). Same as ``COORD=NORMAL``.
* ``NONORMAL`` (logical). Same as ``COORD=NONORMAL``.
* ``BMAT`` (logical). Same as ``COORD=BMAT``.

``DELO[CALIZED] enforces full 3N optimization in delocalized internal coordinates using the PQSOPT program (available in Molpro 2023.1 or later)``

``BMAT uses an older version of optimisations using internal coordinates.``

.. _geometry_optimization_optg--options-for-numerical-gradients:

Options for numerical gradients
===============================

Numerical gradients can be computed with respect to variables on which the Z-matrix depends or with respect to Cartesian coordinates. In the latter case, it is most efficient to use symmetrical displacement coordinates. These do not change the symmetry of the molecule and the number of displacements is minimal. Alternatively (mainly for testing purpose) the gradients can be computed using symmetry unique Cartesian displacements or all 3N Cartesian displacements. In these cases the symmetry of the molecule can be reduced by the displacements and using such displacements is normally not recommended.

* ``DISPLACE=ZMAT|SYMM|UNIQUE|CART``   

Displacement coordinates to be used for numerical gradient. The default is ``ZMAT`` if the geometry is given as a zmatrix which depends on variables, and ``SYMM`` (symmetrical displacement coordinates) otherwise. The use of ``UNIQUE`` or ``CART`` is not recommended.

* ``SYMMETRY=AUTO|NOSYM`` Symmetry to be used in wavefunction calculations of numerical gradients. This option is only relevant if ``DISPLACE=UNIQUE|CART``. If ``AUTO`` is given, the maximum possible symmetry is used for each displacement. This implies that the energy is independent of the symmetry used. Note that this often not the case in MRCI or CASPT2 calculations. The option can also not be used in local correlation calculations.
* ``AUTO`` (logical). Same as ``SYMMETRY=AUTO``
* ``NOSYM`` (logical). Same as ``SYMMETRY=NOSYM``
* **``RSTEP``\ =\ *rstep*** Step length for distances in numerical gradient calculations (in bohr). The default is 0.01.
* **``DSTEP``\ =\ *dstep*** Step length for symmetrical displacements (in bohr). The default is 0.01.
* **``ASTEP``\ =\ *astep*** Step length for angles in numerical gradient calculations (in degree). The default is 1.
* ``FOURPOINT`` (logical). Use 4-point formula for accurate numerical gradient.
* ``NUMERICAL`` (logical). Force the use of numerical gradients, even if gradients are available.
* ``MPPX`` (logical). Can be used to disable mppx in the calculation of numerical gradients and hessians (see also ``MPPX_HESS`` below). ``MPPX=1`` (default) means that each geometry displacement is computed on a different processor.

In special cases the energy calculations may require several steps with different occupations and/or symmetries. In this case the ``FORCEINP`` directive must be given (see section `miscellaneous options: <geometry_optimization_optg.html#miscellaneous-options>`__).

.. _geometry_optimization_optg--options-for-computing-hessians:

Options for computing Hessians
==============================

By default, an approximate Hessian (model Hessian) is used. Optionally, a Hessian can be computed in the optimization or read from a previous Hessian or frequency calculation.

* **``NUMHESS``\ =\ *hstep*** If given, a numerical Hessian is computed in each *hstep’th* iteration. If *hstep=0* or not given, only an initial Hessian is computed.
* **``HESSREC``\ =\ *record*** Read initial Hessian from the given record. If *record* is not given or zero, the last computed Hessian is used.
* ``READHESS`` (logical). Same as ``HESSREC=0``.
* **``HESSPROC``\ =\ *procname*** specifies a procedure to be used for computing the Hessian. This procedure must be define a complete energy calculation (orbital optimization and correlation treatment). A different method can be used than for the optimized energy, but the basis must not be redefined in this procedure. For instance, an MP2 Hessian can be used for CCSD(T) optimizations, or a CASPT2 Hessian for MRCI optimizations. By default, the same procedure is used for the Hessian as for the optimized energy. Note: If a hessian procedure is used and two or more optimizations are done after each other in the same input, the complete energy calculation (including orbital optimization) must be defined before each optg command or in the optg procedure.
* **``HESSVAR``\ =\ *varname*** Compute Hessian for variable *varname*. This implies numerical calculation of the Hessian from energies. The default is to use the same variable as for the energy and gradient.
* ``HESSCENT`` Use central gradient differences for computing Hessian (only effective if gradients are available)
* ``HESSFORW`` Use forward gradient differences for computing Hessian (only effective if gradients are available). This effectively computes the Hessian at a slightly displaced geometry, but needs only half the number of displacements. This is the default.
* **``UPDATE``\ =\ ``BFGS|IBFGS|CGRD|PMS|POWELL|MS|NONE``**   

Hessian update method to be used. See section `hessian update (UPDATE) <geometry_optimization_optg.html#hessian-update-update>`__ for details.

* **``MAXUPD``\ =\ *maxupd*** Max number of Hessian updates. The count is reset to zero each time a Hessian is computed.
* ``NUMDIAG`` If true, replace diagonal elements of model hessian by diagonal numerical hessian (if available). This sometimes improves convergence, but since it may lead to symmetry breaking it is no the default.
* ``MPPX_HESS`` Can be used to disable or enable mppx in hessian calculations during the optimization. Default is setting of MPPX in section `Options for numerical gradients <geometry_optimization_optg.html#options-for-numerical-gradients>`__].

Note that there are restrictions for computing Hessians for multireference methods (MCSCF, MRCI, ACPF,AQCC,RS2). For these methods the symmetry must not change by any displacements, since this could change the occupations and states and may lead to non-contiguous potential energy surfaces. One of the following three options can be used in these cases:

* Use no symmetry from the beginning (``NOSYM``).
* Use symmetric displacement coordinates. This is the default if the optimization is done in 3N cartesian coordinates. One can use ``OPTG,DISPLACE=SYMM`` to force the use of symmetrical displacements (this creates 3N cartesian coordinates if a Z-matrix is used in the geometry input).
* Use a Z-matrix with the restriction that no variable in the Z-matrix may change the symmetry. For example, ``geometry={O;H1,O,r;H2,O,r,H1,theta}`` would work, but ``geometry={O;H1,O,r1;H2,O,r2,H1,thetai}`` would not work. In this case the program prints a warning message. If an incorrect Z-matrix is used and the symmetry changes, the program will crash.

.. _geometry_optimization_optg--miscellaneous-options:

Miscellaneous options:
======================

* ``VARSAVE`` Save Cartesian gradients in variables ``GRADX, GRADY, GRADZ``.
* ``NONUC`` Do not compute gradients at lattice points.
* ``DEBUG`` Set debug print options.
* **``PRINT``\ =\ *iprint*** Print option for optimization.
* **``SAVEXYZ``\ [=\ *file*]** Save the optimized coordinates in an xyz-file. One file is written for each step. The filename is *file*\ _\ *nn*\ ``.xyz``, where *nn* is the iteration number. For the final geometry, _\ *nn* is omitted. If filename is not given, *file* is taken to be the root name of the input, i.e. ``test.inp`` creates ``test_1.xyz`` in the first iteration and ``test.xyz`` for the converged geometry. By default, the xyz information is written to the log file in each step.
* **``SAVEACT``\ [=\ *file*]** Save optimized variables in each step. The file name is *file*\ ``.act``. If *file* is not given the root name of the input is used. The file can be read later using ``the READVAR`` command or copied into new input.
* **``SAVEGRD``\ [=\ *file*]** Write in each step the Cartesian coordinates and gradients. The file name is *file*\ ``.grd``. If file is not given, the root name of the input appended by ``.grd`` is used.
* ``APPEND`` (logical). If given, existing ``SAVEACT`` and/or ``SAVEGRD`` files are appended.
* ``REWIND`` (logical). If given, the ``SAVEACT`` and/or ``SAVEGRD`` files are rewound at each step, i.e. only the last geometry or gradient is saved, previous values are overwritten.
* ``FORCEINP`` (logical) Disables the mechanism that freezes the occupations during geometry optimizations. If this option is given, the occupations and wave function definitions given in the input for the energy calculations are strictly obeyed.

.. _geometry_optimization_optg--directives-for-optg:

Directives for OPTG
-------------------

An alternative way to specify options is to use directives, as described in this section. In some cases this allows more detailed specifications than with the options on the ``OPTG`` command. In particular, directives ``ACTIVE`` or ``INACTICE`` can be used to define the optimization space in more detail.

.. _geometry_optimization_optg--selecting-the-optimization-method-method:

Selecting the optimization method (METHOD)
==========================================

``METHOD,key;``

*key* defines the optimization method.

For *minimization* the following options are valid for *key*:

* ``PQS`` PQS optimizer (default for full (3N) optimisations).
* ``RF`` Rational Function method (default for Z-matrix optimisations).
* ``AH`` Augmented Hessian method. This is similar to ``RF`` algorithm but uses a more sophisticated step restriction algorithm.
* ``DIIS`` Pulay’s Geometry DIIS method. As an an additional option you may add the number of geometries to be used in GDIIS interpolation (default 5) and the interpolation type (i.e. the subspace in which the GDIIS interpolation is made.

``METHOD,DIIS, number, type\\``
*type* may be ``GRAD`` interpolation using the gradients (default), working good for rigid molecules, ``STEP`` interpolation using Quasi-Newton steps which could be advantageous in dealing with very floppy molecules, ``ENER`` interpolation using energies, which is an intermediate between the above two.

* ``QSD`` Quadratic steepest descent method of Sun and Ruedenberg.
* ``SRMIN`` Old version of ``QSD``.

For *transition state* searches (invoked with the ``ROOT`` option, see section `transition state (saddle point) optimization (ROOT) <geometry_optimization_optg.html#transition-state-saddle-point-optimization-root>`__) *key* can be

* ``PQS`` PQS optimizer using internal coordinates (default for full (3N optimisations).
* ``RF`` Rational Function method (default for Z-matrix optimisations).
* ``DIIS`` Pulay’s Geometry DIIS method (see above).
* ``QSD`` Quadratic Steepest Descent Transition State search using the image Hessian method (see J. Sun and K. Ruedenberg, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.467721>`__ **101**, 2157 (1994)) The use of this option is recommended for transition state searches – especially in complicated cases. The optimization step is checked and the Hessian is recalculated when approaching a troublesome region of the PES. Thus **this method is somewhat safer (and often faster) in reaching convergence than the RF or DIIS method**. The Hessian recalculation safeguard may be turned off using the ``METHOD,QSD,NOHESS`` input card.
* ``SRTRANS`` Old version of ``QSD``.

For *reaction path following* the input *key* is

* ``QSDPATH`` Quadratic Steepest Descent reaction path following. This methods determines reaction paths (intrinsic reaction coordinates, IRCs) by following the exact steepest descent lines of subsequent quadratic approximations to the potential energy surface. The Hessian matrix is calculated numerically at the first optimization step and subsequently updated by Powell or BFGS update. If a given arc length of the steepest descent lines is exceeded, the Hessian is recalculated numerically (see ``OPTION`` section `reaction path following options (OPTION) <geometry_optimization_optg.html#reaction-path-following-options-option>`__). For details see J. Sun and K. Ruedenberg, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.465995>`__ **99**, 5269 (1993) It is also possible to recalculate the Hessian after each *m* steps using the ``NUMHES``,\ *m* command (see section `numerical Hessian (NUMHESS) <geometry_optimization_optg.html#numerical-hessian-numhess>`__). If the Hessian matrix is recalculated in every optimization step (``NUMHES``,\ :math:`1`) a algorithm different to the one with updated Hessians is used, which is very accurate. Using the ``PRINT,OPT`` card, this algorithm prints in every optimization step a *reaction path point r* which is different from the point where the energy and the gradient is calculated but closer to the real reaction path (for further details of the algorithm see J. Sun and K. Ruedenberg, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.465994>`__ **99**, 5257 (1993)). For further input options of the QSD reaction path following see ``OPTION`` section `reaction path following options (OPTION) <geometry_optimization_optg.html#reaction-path-following-options-option>`__.
* ``SRSTEEP`` Old Version of ``QSDPATH``.

.. _geometry_optimization_optg--optimization-coordinates-coord:

Optimization coordinates (COORD)
================================

It is possible to use various coordinate types and algorithms for the optimization. This can be controlled by additional subcommands as described in this and the following subsections.

``COORD,[opt_space],[opt_coord],[NOROT]``

These options choose the optimization space and the coordinate system in which the optimization takes place.

*opt_space* defines the parameters to be optimized. By default, if the geometry input is given in Z-matrix format, all variables on which the Z-matrix depends are optimized. Subsets of the variables on which the Z-matrix depends can be chosen using the ``ACTIVE`` or ``INACTIVE`` subdirectives. If the Z-matrix depends on no variables or ``xyz`` input is used, all :math:`3N` cartesian coordinates are optimized.

*opt_space* can be one of the following:

* ``ZMAT`` Optimize all variables on which the Z-matrix depends (default if the geometry is given as Z-matrix).
* ``3N`` Optimize all :math:`3N` cartesian coordinates (default if the Z-matrix depends on no variables, or if xyz-input is used). Z-Matrix       input coordinates will be destroyed if 3N is used.

*opt_coord* determines the coordinates in which the optimization takes place. Optionally, delocalized internal coordinates, local normal coordinates, cartesian coordinates, or natural internal coordinates can also be used.

*opt_coord* can be one of the following:

* ``DELO[CALIZED]`` Optimization in delocalized internal coordinates using PQSOPT (available in Molpro 2023.1 or later). This is the default for full space (3N) optimisations. If the option is given, 3N optimization is enforced (but constraints can be defined).
* ``NORMAL`` Optimization in local normal coordinates.
* ``NONORM`` Don’t use local normal coordinates.
* **``BMAT``\ [=\ *filename*]** Use Pulay’s *natural internal coordinates*, see G. Fogarasi, X. Zhou, P. W. Taylor and P. Pulay *J. Am. Chem. Soc.* **114**, 8191 (1992); P. Pulay, G. Fogarasi, F. Pang, J. E. Boggs *J. Am. Chem. Soc.* **101**, 2550 (1979)). Optionally, the created coordinates as well as additional informations about this optimization are written to the specified file. These coordinates resemble in part the valence coordinates used by vibrational spectroscopist, and have the advantage of decreasing coupling between different modes. This often increases the speed of convergence. Similar coordinates are also used in the PQSOPT program (``DELO``), and mostly this converges even better.

If the option [``NOROT``] is given, the cartesian coordinates are not transformed to minimize rotations.

.. _geometry_optimization_optg--displacement-coordinates-displace:

Displacement coordinates (DISPLACE)
===================================

``DISPLACE,displacement_type``

see section `choice of coordinates (COORD) <energy_gradients.html#choice-of-coordinates-coord>`__ for details.

.. _geometry_optimization_optg--defining-active-geometry-parameters-active:

Defining active geometry parameters (ACTIVE)
============================================

``ACTIVE,param;``

Declares variable name *param* to be active in the optimization. By default, initially all variables on which the geometry depends are active; inclusion of an ``ACTIVE`` card makes all parameters inactive unless explicitly declared active (see also ``INACTIVE``).

.. _geometry_optimization_optg--defining-inactive-geometry-parameters-inactive:

Defining inactive geometry parameters (INACTIVE)
================================================

``INACTIVE,param;``

Declares variable name *param* to be inactive in the optimization. If any ``ACTIVE`` card appears in the input, this card is ignored! (see also ``ACTIVE``)

.. _geometry_optimization_optg--hessian-approximations-hessian:

Hessian approximations (HESSIAN)
================================

By default, the Molpro geometry optimization utilizes a force field approximation to the hessian (“Model Hessian”, see R. Lindh, A. Bernhardsson, G. Karlström and P. Malmqvist `Chem. Phys. Lett. <https://dx.doi.org/10.1016/0009-2614(95)00646-L>`__ **241**, 423 (1995)), which speeds up convergence significantly. The Model Hessian is parameterized for the elements up to the third row. Alternatively, the model Hessian of Schlegel can be used, or the Hessian can be computed numerically (see also section `numerical Hessian (NUMHESS) <geometry_optimization_optg.html#numerical-hessian-numhess>`__).

``HESSIAN,options``

where *options* can be

* ``MODEL`` Use Lindh’s Model Hessian in optimization (default).
* ``MODEL=SCHLEGEL`` Use Schlegel’s Model Hessian.
* ``MODEL=VDW`` Add vdW terms to Lindh’s Model Hessian.
* ``SCHLEGEL`` same as ``MODEL=SCHLEGEL``.
* ``VDW`` same as ``MODEL=VDW``.
* ``NOMODEL`` Don’t use Model Hessian approximation to the hessian.
* **``NUMERICAL``\ =\ *hstep*** Recompute Hessian after *hstep* iterations. This disables the use of a model hessian. If *hstep*\ =0, the Hessian is only computed in the first iteration. Default parameters are used for computing the numerical Hessian, unless modified using options as described for the ``NUMHESS`` directive, see Sect. `numerical Hessian (NUMHESS) <geometry_optimization_optg.html#numerical-hessian-numhess>`__. Any option valid for the ``NUMHESS`` directive may also follow the ``NUMERICAL`` option on the ``HESSIAN`` directive.
* **``READ|RECORD|HESSREC``\ =\ *record*** Read Hessian from given *record*. If *record* is not given or zero, the last computed hessian will be read. See section `numerical Hessian (NUMHESS) <geometry_optimization_optg.html#numerical-hessian-numhess>`__ for more details about numerical Hessians.
* **``UPDATE``\ =\ *type*** Method used for hessian update. See section `hessian update (UPDATE) <geometry_optimization_optg.html#hessian-update-update>`__ for possibilities and details.
* **``MAXUPD``\ =\ *maxupd*** Max number of hessian updates. The count is reset to zero each time a hessian is computed.

If the Model Hessian is disabled (``NOMODEL``) and no Hessian is read or computed, the initial hessian is assumed to be diagonal, with values 1 hartree\*bohr\ **(-2) for all lengths, 1 hartree\*radian**\ (-2) for all angles. Additional matrix elements of the hessian can be defined using the HESSELEM directive, see section `hessian elements (HESSELEM) <geometry_optimization_optg.html#hessian-elements-hesselem>`__.

In transition state searches the Hessian is evaluated numerically in the first iteration by default. Alternatively, if ``READ`` is specified, a previously computed hessian is used.

.. _geometry_optimization_optg--numerical-hessian-numhess:

Numerical Hessian (NUMHESS)
===========================

``NUMHESS,options``

or

``NUMHESS,hstep,options If this directive is present a numerical Hessian is computed using finite differences. If analytical gradients are available, one can use forward gradient differences (needs one gradient calculation for each coordinate) or central differences (more accurate, needs two gradient calculations for each coordinate). For transition state optimizations it is usually sufficient to use forward differences. If analytical gradients are not available for the optimized method, the energy is differentiated twice. In this case only central differences are possible.``

The following options can be given:

``HSTEP=hstep``
*hstep*\ =-1: Don’t calculate numerical hessian (default for minimization);
*hstep*\ =0 Calculate numerical hessian only once at the start of the optimization (default for transition state searches).
*hstep*\ =\ *n* Calculate numerical hessian after each *n* optimization steps. This is useful for difficult transition state optimizations (e.g. if the eigenvalue structure of the hessian changes during the optimization).
``FORWARD``
Use forward differences (default).
``CENTRAL``
Use the more accurate central differences.
``RSTEP=rstep``
Step length for distances (in bohr). The default is 0.01.
``ASTEP=astep``
Step length for angles (in degree). The default is 0.5 or 1 for angles below and above 90 degree, respectively.
``DSTEP=dstep``
Step length for symmetrical displacements (in bohr). The default is 0.01.
``VARIABLE=varname``
Use given variable for numerical calculation of the Hessian. Note that this disables the use of gradients, and Hessian evaluation can be very expensive.
``PROCEDURE=procname``
Procedure to be used for computing Hessian. This procedure must be define a complete energy calculation (orbital optimization and correlation treatment). A different method can be used than for the optimized energy. For instance, an MP2 hessian can be used for CCSD(T) optimizations, or a CASPT2 hessian for MRCI optimizations. By default, the same procedure is used for the hessian as for the optimized energy.
``DISPLACE=type``
*type* can be one of the following:

``SYMM``
Use symmetric displacement coordinates (default). This is the only recommended option.
``CART``
Use :math:`3N` cartesian displacements (not recommended). This requires many more energy calculations than necessary and does not preserve the molecular symmetry.
``UNIQUE``
Use symmetry-unique cartesian displacements (not recommended)

Note that the displacement type for gradient and hessian must be the same.
``CALC=icalc``
*icalc*\ =0: Recalculate the complete Hessian matrix numerically after each *hstep* optimization steps (default).
*icalc*\ =1 (currently disabled): Recalculate selected Hessian matrix elements if the relative deviation of this element before and after update (see ``UPDATE``, section `hessian update (UPDATE) <geometry_optimization_optg.html#hessian-update-update>`__) is larger than *thresh*. If *thresh* is not specified, a default value of :math:`thresh=0.05` (i.e. a maximum deviation of :math:`5 \%`) is used.
*icalc*\ =2 (currently disabled): Recalculate complete Hessian matrix if the RMS deviation of the Hessian matrix before and after update is larger than :math:`thresh`. If *thresh* is not specified a default value of :math:`thresh=0.5` :math:`a.u.` is used.
``THRESH=thresh``
Threshold for partial or dynamical update of hessian, see above

.. _geometry_optimization_optg--hessian-elements-hesselem:

Hessian elements (HESSELEM)
===========================

[optgeo:hesselem]

``HESSELEM,value, active1,active2,…``

sets the starting value for hessian matrix element between active variables *active1*, *active2* to *value*. If *active2* is omitted it defaults to *active1* (diagonal element). As many ``HESSELEM`` directives as needed may be given.

.. _geometry_optimization_optg--hessian-update-update:

Hessian update (UPDATE)
=======================

``UPDATE,[TYPE=]type,MAXUPD=maxupd``

This directive chooses the update type and limits the number of points used for the hessian update to *maxupd*. The default number of steps used in hessian update procedures is 5. If there are symmetry constraint in the coordinates of the optimization, the default number may be lower than five.

In minimizations *type* may be

* ``BFGS`` Use BFGS update of hessian (default).
* ``IBFGS`` Use BFGS update of the inverse hessian.
* ``CGRD`` Use Conjugate Gradient update (see also ``CUT``,\ ``TRUST``).
* ``NONE`` Don’t do any update.

In transition state optimizations *type* may be

* ``PMS`` Combined Powell/Murtagh-Sargent update of hessian (default).
* ``POWELL`` Use Powell’s update of the hessian.
* ``MS`` Use update procedure of Murtagh and Sargent.
* ``NONE`` Don’t do any update.

.. _geometry_optimization_optg--numerical-gradients-numerical:

Numerical gradients (NUMERICAL)
===============================

``NUMERICAL,options,active$_1$=step$_1$, active$_2$=step$_2$ …;``

With this directive the gradients are computed by finite differences. *step:math:`_i`* is the increment for the active geometry parameter :math:`active_i`. For active parameters which are not specified, the default values are used. By default, the increment is 0.01 bohr for bond distances and 0.5 or 1 degree for angles less than or greater than 90 degrees, respectively. These defaults can be modified by specifying ``RSTEP`` or ``ASTEP``. ``DSTEP`` is the length of symmetrical displacements, which are used if the optimization is performed in 3N coordinates.

For each active variable, two energy calculations are necessary in each geometry optimization step – so numerical optimizations may be expensive! In optimizations of 3N coordinates symmetrical displacement coordinates are normally used to minimize the number of energy calculations. (see section `choice of coordinates (COORD) <energy_gradients.html#choice-of-coordinates-coord>`__).

For optimization of special energies see ``VARIABLE`` section `optimizing energy variables (VARIABLE) <geometry_optimization_optg.html#optimizing-energy-variables-variable>`__.

The following options can be given:

* **``RSTEP``\ =\ *rstep*** Step length for distances (in bohr). The default is 0.01.
* **``ASTEP``\ =\ *astep*** Step length for angles (in degree). The default is 0.5 or 1 for angles below and above 90 degree, respectively.
* **``DSTEP``\ =\ *dstep*** Step length for symmetrical displacements (in bohr). The default is 0.01.
* ``CENTRAL`` Use central differences for gradient (default)
* ``FORWARD`` Use forward differences (not recommended for gradient).
* ``FOURPOINT`` Use four-point formula for very accurate numerical gradients.
* **``PROCEDURE``\ =\ *procname*** Use given procedure for numerical calculation of the gradient. This procedure must define a complete energy calculation (orbital optimization and correlation treatment).
* **``VARIABLE``\ =\ *varname*** Use given variable for numerical calculation of the gradient.
* **``DISPLACE``\ =\ *type*** The displacement type. Note that the displacement type for gradient and hessian must be the same. *type* can be one of the following:

  * ``SYMM`` Use symmetric displacement coordinates (default). This is the only recommended option.
  * ``CART`` Use :math:`3N` cartesian displacements (not recommended). This requires many more energy calculations than necessary and does not preserve the molecular symmetry.
  * ``UNIQUE`` Use symmetry-unique cartesian displacements (not recommended)

.. _geometry_optimization_optg--transition-state-saddle-point-optimization-root:

Transition state (saddle point) optimization (ROOT)
===================================================

``ROOT,root [root]``

Specifies the eigenvector of the hessian to be followed.

* ***root*\ =1** specifies a minimization (default).
* ***root*\ =2** specifies a transition state (saddle point) optimization.

In the present implementation a saddle point search is possible with the rational function method (``METHOD,RF``), the geometry DIIS method (``METHOD,DIIS``) and the quadratic steepest descent method of Sun and Ruedenberg (``METHOD,SRTRANS``).

Note that convergence is usually much more difficult to achieve than for minimizations. In particular, a good starting geometry and a good approximation to the hessian is needed. The latter is achieved by evaluating the hessian numerically (see section `numerical Hessian (NUMHESS) <geometry_optimization_optg.html#numerical-hessian-numhess>`__) or using a precomputed hessian (see section `hessian approximations (HESSIAN) <geometry_optimization_optg.html#hessian-approximations-hessian>`__).

Example:

.. code-block:: text
   :caption: examples/butane_opt_transition.inp

    ***, Bicyclo-[1.1.0]-butane Transition State
    basis=3-21G
   
    L1=1.495  ang                ! Define Active Variables
    L2=1.418  ang
    L3=1.463  ang
    L4=1.093  ang
    L5=1.111  ang
    L6=1.098  ang
    L7=1.097  ang
    L8=1.110  ang
    L9=1.106  ang
    A1=92.1   degree
    A2=62.1   degree
    A3=136.0  degree
    A4=123.5  degree
    A5=122.4  degree
    A6=124.7  degree
    A7=126.7  degree
    A8=117.9  degree
    D1=-120.4 degree
    D2=4.4    degree
    D3=108.8  degree
    D4=-107.5 degree
    D5=84.2   degree
    D6=109.3  degree
    D7=-106.1 degree
   
    geometry={C1                 ! Geometry Specification Z-Matrix
              C2  1 L1
              C3  2 L2 1 A1
              C4  1 L3 2 A2 3 D1
              H5  1 L4 2 A3 3 D2
              H6  2 L5 1 A4 4 D3
              H7  3 L6 2 A5 1 D4
              H8  3 L7 2 A6 1 D5
              H9  4 L8 1 A7 2 D6
              H10 4 L9 1 A8 2 D7}
    int
    rhf
    optg
    root,2                       ! Transition State search
    method,qsd                   ! Use Quadratic Steepest Descent Method
   

.. _geometry_optimization_optg--setting-a-maximum-step-size-step:

Setting a maximum step size (STEP)
==================================

``STEP,steplength,drmax,damax,drmax1,damax1 [optgeo:step]``

*steplength* is the initial step length in the scaled parameter space (default 0.3). In the AH-method this is dynamically adjusted, and can have a maximum value *ahmax* (see ``TRUST``).

*drmax* is the initial max change of distances (in bohr, default 0.3). In the AH-method this is dynamically adjusted up to a maximum value of *drmax1* (default 0.5 bohr).

*damax* is the initial max change of angles (in degree, default 2). In the AH-method this is dynamically adjusted up to a maximum value of *damax1* (default 10 degrees).

.. _geometry_optimization_optg--redefining-the-trust-ratio-trust:

Redefining the trust ratio (TRUST)
==================================

``TRUST,ratio,ahmax``

*ratio* determines the radius around the current minimum in which points are used to update the Hessian with the conjugate gradient method (default 0.5; see also ``UPDATE``).

*ahmax* is the maximum step size allowed in the Augmented Hessian procedure. This refers to the scaled parameter space (default 0.5). The initial step size is *stepmx* (see ``STEP`` card).

.. _geometry_optimization_optg--setting-a-cut-parameter-cut:

Setting a cut parameter (CUT)
=============================

``CUT,threshold``

Specifies a threshold for ortho-normalization used in conjugate gradient update of hessian (default 1.d-3; see also ``UPDATE``).

.. _geometry_optimization_optg--line-searching-linesearch:

Line searching (LINESEARCH)
===========================

``LINESEARCH,iflag,thrlmin,thrlmax``

Interpolate the geometry of the stationary point (minimum or saddle point) by a quartic polynomial between the current and the previous geometry. If *iflag*\ =0 or no *iflag* is set, the next optimization step will be taken from the interpolated geometry using the interpolated energy and gradient. If *iflag*\ =1 the energy and gradient will be recalculated at the interpolated geometry before taking the new optimization step. Note though, that the additional effort of recalculating the energy and gradient is usually not met by the increase of the convergence rate of the optimization. *thrlmin* and *thrlmax* are min and max thresholds for the recalculation of the energy and the gradient in case *iflag*\ =1. I.e. the recalculation just takes place if the interpolated geometry isn’t too close to the actual geometry *thrlmin* and isn’t too remote from the actual geometry *thrlmax*. Default values are *thrlmin*\ =0.001 and *thrlmax*\ =0.05 in the scaled parameter space of the optimization.

.. _geometry_optimization_optg--reaction-path-following-options-option:

Reaction path following options (OPTION)
========================================

``[optgeo:option] OPTION,key=param;\\``
where *key* can be

* ``IDIR`` If starting at a transition state (or near a transition state) determine where to take the first step. If ``IDIR=0`` is chosen, the first step will be towards the transition state. This is the default. If ``IDIR=1`` is given in the input the first optimization step will be along the ”transition vector” i.e. the hessian eigenvector to the smallest eigenvalue which points down towards the minimum. If using a larger ``IDIR`` parameter, the first step will be larger; if using a negative value, the first step will be in the opposite direction.
* ``STPTOL`` If using an updated hessian matrix, this parameter determines what update to take. If the step size between two subsequent points on which the steepest decent lines are puzzled together is smaller than *stptol* (i.e. if we are close to a minimum) the BFGS update is used, otherwise it is Powell update. The default value of *stptol* is :math:`1.d-6`. Note that the stepsize is also affected by the ``STEPMAX`` option.
* ``SLMAX`` This option is only valid with the old version of the reaction path following algorithm (i.e. ``METHOD,SRSTEEP``). In this algorithm ``slmax`` determines the frequency of the recalculation of the numerical hessian. If the total step size of the last steps exceeds *slmax* the hessian will be recalculated, otherwise it will be updated. By default *slmax* is two times the maximum step size of the optimization step *steplength* (see ``STEP`` section `setting a maximum step size (STEP) <geometry_optimization_optg.html#setting-a-maximum-step-size-step>`__). If you are using ``METHOD,QSD``, the ``SLMAX`` option is obsolete and the ``NUMHES`` command (see above) should be used instead.

These options can also be given on the ``OPTG`` command line.

.. _geometry_optimization_optg--optimizing-energy-variables-variable:

Optimizing energy variables (VARIABLE)
======================================

``VARIABLE,name; [optgeo:var]``

Defines a variable *name* which holds the energy value to be optimized in using finite differences. By default, this is ``ENERGY(1)`` as set by the most recent program. Other variables which can be used are

* **``ENERGY``\ (*i*)** holds last energy for state *i*.
* **``ENERGR``\ (*i*)** holds last reference energy for state *i*.
* **``ENERGD``\ (*i*)** holds last Davidson corrected energy for state *i*.
* **``ENERGP``\ (*i*)** holds last Pople corrected energy for state *i*.
* ``ENERGC`` holds CCSD (QCI, BCCD) energy in CCSD(T) [QCI(T), BCCD(T)] calculations (single state optimization).
* ``ENERGT(1)`` holds CCSD(T) energy in CCSD(T) calculations (single state)
* ``ENERGT(2)`` holds CCSD[T] energy in CCSD(T) calculations (single state).
* ``ENERGT(3)`` holds CCSD-T energy in CCSD(T) calculations (single state).

These variables are set automatically by the CI and/or CCSD programs. It is the user’s responsibility to use the correct variable name; an error exit occurs if the specified variable has not been defined by the last program or the user.

Note: The use of the ``VARIABLE`` option triggers ``NUMERICAL``, so optimization can be very inefficient!

.. _geometry_optimization_optg--printing-options-print:

Printing options (PRINT)
========================

``PRINT,code=level,…;``

Enables printing options. Usually level should be omitted or 0; values of :math:`level>0` produce output useful only for debugging. *code* can be

* ``HESSIAN`` prints the updated hessian matrix. Note that its diagonal elements are printed anyway.
* ``HISTORY`` prints the complete set of previous geometries, gradients and energies.
* ``GRADIENT`` prints extended gradient information
* ``OPT`` prints detailed information about the optimization process (mainly for debugging).

Several print options can be specified with one ``PRINT`` command.

.. _geometry_optimization_optg--conical-intersection-optimization-conical:

Conical Intersection optimization (CONICAL)
===========================================

[conical]

To optimize a conical intersection between two electronic states having the same spin, three vectors must be evaluated at SA-CPMCSCF level:

* Non-Adiabatic Derivative Coupling (DC).
* Gradient of the lower state (LSG).
* Gradient of the upper state (USG).

This requires three different ``CPMCSCF`` directives in the MULTI input:

``CPMCSCF, NACM, $S_i$, $S_j$, ACCU=1.0d-7, record=record1.file\\``
``CPMCSCF, GRAD, $S_i$, SPIN=Spin of state $S_i$, ACCU=1.0d-7, record=record2.file\\``
``CPMCSCF, GRAD, $S_j$, SPIN=Spin of state $S_j$, ACCU=1.0d-7, record=record3.file``

where :math:`S_i`,\ :math:`S_j` are the electronic states in the usual format *istate.istsym*, and *record[n].file* specifies the name and the file number where CPMCSCF solutions should be stored. Parameter ``SPIN`` is half of the value in the ``WF`` card used to define the electronic state.

Things to remember:

* Specify always three different *record.file* on the ``CPMCSCF`` directives.
* Evaluate the CPMCSCF for USG always last.
* Skip the DC evaluation if the conical intersection involves states with different spin (e.g., a Singlet/Triplet crossing) because the coupling is then zero.

Three sets of ``FORCE`` commands (only two for Singlet/Triplet intersection) follow the ``MULTI`` input. They will be like:

``FORCE\\``
``SAMC,record[n].file\\``
``CONICAL,record4.file[,NODC]``

where *record.file* is one of the records containing CPMCSCF info and *record4.file* points to a free record used for internal storage by the CONICAL code. *record4.file* must be the same on all the ``CONICAL`` directives. Furthermore, the present implementation works properly only if *file=1* on the ``CONICAL`` directive. The optional keyword ``NODC`` must be used in case of different spins (e.g., S/T crossing) when DC is not needed.

The actual optimization is performed using ``OPTG,STARTCMD=MULTI`` The example below optimizes the conical intersection in :math:`LiH_2` (ground and excited states are both doublets).

.. code-block:: text
   :caption: examples/lih2_D0D1.inp

   ***, LiH2
   
   basis=sto-3g
   print,orbitals,civector
   
   symmetry,x              !use only molecular plane. Both states must be in the same symmetry.
   geometry={
             Li;
             h1,Li,r;
             h2,Li,r,h1,theta}
   
   r=3.0
   theta=35
   
   {hf;wf,4,1,0}
   
   {multi;occ,6,1;wf,5,1,1;state,2                       !state averaged casscf
   CPMCSCF,NACM,1.1,2.1,accu=1.0d-7,record=5100.1        !cpmcscf for non-adiabatic couplings
   CPMCSCF,GRAD,1.1,spin=0.5,accu=1.0d-7,record=5101.1   !gradient for state 1
   CPMCSCF,GRAD,2.1,spin=0.5,accu=1.0d-7,record=5102.1}  !gradient for state 2
   
   {Force
   SAMC,5100.1             !compute coupling matrix element
   CONICAL,6100.1}         !save information for optimization of conical intersection
   
   {Force
   SAMC,5101.1             !compute gradient for state 1
   CONICAL,6100.1}         !save information for optimization of conical intersection
   
   {Force
   SAMC,5102.1             !compute gradient for state 2
   CONICAL,6100.1}         !save information for optimization of conical intersection
   
   optg,startcmd=multi     !find conical intersection

This second example optimizes the singlet-triplet intersection in :math:`LiH_2(+)` (ground state is Singlet, excited state is Triplet). Though the optimization works for this example, one has to be careful, as the intersection between states of different symmetry or spin when spin-orbit coupling is not included leads to an energy difference whose first derivative does not vanish at degeneracy. Most geometry optimisation algorithms assume the opposite.

.. code-block:: text
   :caption: examples/lih2+_S0T0.inp

   ***, LiH2
   
   basis=sto-3g
   
   symmetry,nosym
   geometry={
             Li;
             H1,Li,r;
             H2,Li,r,H1,theta}
   
   r=3.7
   theta=160
   
   {hf;wf,4,1,0}
   
   {multi;
    occ,7;
    wf,4,1,0;   !singlet state
    wf,4,1,2;   !triplet state
    CPMCSCF,GRAD,1.1,spin=0,accu=1.0d-7,record=5101.1   !cpmcscf for gradient of singlet state
    CPMCSCF,GRAD,1.1,spin=1,accu=1.0d-7,record=5100.1   !cpmcscf for gradient of triplet state
   }
   
   {Force
    SAMC,5101.1                !state averaged gradient for singlet state
    CONICAL,6100.1,NODC}       !save information for OPTCONICAL
   
   {Force
    SAMC,5100.1                !state averaged gradient for triplet state
    CONICAL,6100.1,NODC}       !save information for OPTCONICAL
   
   optg,startcmd=multi,gradient=1.d-6  !find singlet-triplet crossing point

.. _geometry_optimization_optg--using-the-slapaf-program-for-geometry-optimization:

Using the SLAPAF program for geometry optimization
--------------------------------------------------

It is optionally possible to use the ``SLAPAF`` program written by Roland Lindh for geometry optimizations. This is done by prepending the optimization method with ’SL’. The following methods are supported:

* ``SLRF`` Use the rational function approximation;
* ``SLNR`` Use the Newton-Raphson method;
* ``SLC1`` Use the C1-DIIS method;
* ``SLC2`` Use the C2-DIIS method.

When using DIIS methods (``SLC1`` or ``SLC2``), the DIIS parameters are specified in the same way as in standard molpro optimizer.

There are some differences when using the ``SLAPAF`` program:

* It is not possible to use Z-matrix coordinates in the optimization.
* Instead, one can explicitly define internal coordinates to be varied or fixed.
* Additional constraints can be imposed on the converged geometry in a flexible way.

.. _geometry_optimization_optg--defining-constraints:

Defining constraints
====================

Constraints and internal coordinates (see below) can be linear combinations of bonds, angles etc. The latter, called here primitive internal coordinates, can be specified before the constraints definition, or directly inside. The general definition of a primitive coordinate is:

``PRIMITIVE,[NAME=]symbolic name, explicit definition;``

or

``PRIM,[NAME=]symbolic name, explicit definition;``

Here *symbolic name* is the name given to the primitive coordinate (if omitted, it will be generated automatically). This name is needed for further reference of this primitive coordinate.

*explicit definition* has the form:

*type,atoms*

*type* can be one of the following:

* ``BOND`` Bond length, defined by 2 atoms.
* ``ANGLE`` Bond angle, defined by 3 atoms (angle 1–2–3).
* ``DIHEDRAL`` Dihedral angle, defined by 4 atoms (angle between the planes formed by atoms 1,2,3 and 2,3,4, respectively).
* ``OUTOFPLANE`` Out-of-plane angle, defined by 4 atoms (angle between the plane formed by atoms 2,3,4 and the bond 1–4).
* ``DISSOC`` A dissociation coordinate, defined by two groups of atoms (Not permitted with constraints).
* ``CARTESIAN`` Cartesian coordinates of an atom.

For all types except ``DISSOC`` and ``CARTESIAN``, atoms are given as:

``ATOMS=[a1,a2,a3,...]``

where the number of atoms required varies with *type* as specified above, and the atomic names *a1,a2,a3,...* can be either atomic tag names from the Z-matrix input, or integers corresponding to Z-matrix rows. Note that the square brackets are required here and do not indicate optional input.

For ``DISSOC`` the specification is as follows:

``DISSOC,GROUP1=[a1,a2,...],GROUP2=[b1,b2,...];``

The corresponding internal coordinate is the distance between the centres of mass of the two groups.

For ``CARTESIAN`` the definition is

``CARTESIAN, I, atom;``

where *I* can be one of ``X,Y,Z`` or 1,2,3 and *atom* can be a z-matrix atom name or an integer referring to the z-matrix row.

With this definition, the constraints are defined as

``CONSTRAINT``,[``VALUE=``]\ *value*,[*unit*],[[``FACTOR=``]\ *fac*,\ *prim*,[[``FACTOR=``]\ *fac*],\ *prim,...;*

where *value* is the value imposed to the constraint, and *prim* is either the name of the primitive defined before this constraint, or an explicit definition; and *fac* is a factor of the corresponding primitive in the constraint. If *fac* is omitted it is taken to be 1.

If *value* is specified in ``Angstrom`` or ``Radian``, *unit* must be given.

Examples for H\ :math:`_2`\ O in :math:`C_s` symmetry:

Constraining the bond angle to 100 degrees:

``constraint,100,deg,angle,atoms=[h1,o,h2];``

which is equivalent to

``primitive,a1,angle,atoms=[h1,o,h2];``

``constraint,100,a1;``

Keeping the two OH distances equal:

``constraint,0,bond,atoms=[h1,o],-1.,bond,atoms=[h2,o];``

which is equivalent to

``primitive,b1,bond,atoms=[h1,o];``

``primitive,b2,bond,atoms=[h2,o];``

``constraint,0,b1,-1.,b2;``

.. _geometry_optimization_optg--defining-internal-coordinates:

Defining internal coordinates
=============================

By default ``SLAPAF`` optimizes in force-constant weighted normal coordinates that are determined automatically. However, the user can define his own coordinates. The definition of internal coordinates, similar to constraints, is based on primitive coordinates. The input is:

``INTERNAL``,[[``NAME=``]\ *name*],[[``FACTOR=``]\ *fac*],\ *prim*,[[``FACTOR=``]\ *fac*],\ *prim,...;*

``FIX``, [[``NAME=``]\ *name*],[[``FACTOR=``]\ *fac*],\ *prim*,[[``FACTOR=``]\ *fac*],\ *prim,...;*

Internal coordinates that are specified using ``INTERNAL`` are varied and those using ``FIX`` are fixed to their initial values.

An important point for the definition of internal coordinates is that their total number must be equal to the number of degrees of freedom of the molecule . Otherwise an error message is generated. Only symmetry independent coordinates need to be given.

.. _geometry_optimization_optg--additional-options-for-slapaf:

Additional options for SLAPAF
=============================

Some options can be passed to the SLAPAF program. Options are specified with SLOPT subdirective:

``{opt;method=slnr;{slopt;opt1;opt2,par1,par2;opt3;...}}``

The available options are

* ``CART`` Use eigenvectors of the approximate Hessian, expressed in cartesian coordinates, as the definition of internal coordinates;
* ``NOMA`` Don’t impose any restrictions on the step size;
* ``UORD`` Order the gradients and displacement vectors according to Schlegel prior to the update of the Hessian. Default is no reordering;
* ``HWRS`` Use force field weighted internal coordinates (default);
* ``RS-P`` Activate RS-P-RFO as default for transition state search; default is RS-I-RFO;
* ``NOHW`` Use unweighted internal coordinates;
* ``PRBM`` Print B-matrix;
* **``RTHR,``\ *Thra,Thrb,Thrt*** Thresholds for redundant coordinate selection for bonds, bends and torsions, respectively. Default 0.2, 0.2, 0.2
* **``MODE,``\ *index*** Hessian vector index for mode following when calculating transition states.
* ``FIND`` Enable unconstrained optimization for constrained cases, when looking for transition states (see MOLCAS manual).
* **``GNRM,``\ *thr*** Threshold for FIND, default 0.2 (see MOLCAS manual).

For more information, please consult the MOLCAS manual.

.. _geometry_optimization_optg--examples:

Examples
--------

.. code-block:: text
   :caption: examples/h2o_optmp2.inp

   ***,H2O                      !title
   include procedures
   basis=vtz                    !use cc-pVTZ basis
   geometry={O;                 !Z-matrix for water
             H1,O,R;
             H2,O,R,H1,THETA}
   R=0.96 Ang                   !start bond distance
   Theta=104                    !start bond angle
   optmp2                       !do MP2 geometry optimization
   show,R,Theta                 !show optimized geometry parameters

.. code-block:: text
   :caption: examples/h2o_optmp2_runccsdt.inp

   include procedures
   geometry={O;                 !Z-matrix for water
             H1,O,R;
             H2,O,R,H1,THETA}
   basis=vtz                    !use VTZ basis
   R=0.96 Ang                   !start bond distance
   Theta=104                    !start bond angle
   
   hf
   mp2
   optg    !optimize MP2 energy
   mp4     !do single-point MP4 at MP2 geometry
   ccsd(t) !do single-point CCSD(T) at MP2 geometry

There is an additional example in the `introductory examples <introductory_examples.html#geometry-optimizations>`__.

.. _geometry_optimization_optg--simple-hf-optimization-using-z-matrix:

Simple HF optimization using Z-matrix
=====================================

.. code-block:: text
   :caption: examples/allene_optscf.inp

    ***, Allene geometry optimization using Z-Matrix
    basis=sto-3g
   
    rcc=1.32 ang
    rch=1.08 ang
    acc=120  degree
    Geometry={C1                       !Z-matrix input
              C2,c1,rcc
              X1,c1,rcc,c2,45
              C3,c2,rcc,c1,180,x1,0
              h1,c1,rch,c2,acc,x1,0
              h2,c1,rch,c2,acc,h1,180
              h3,c3,rch,c2,acc,h1,90
              h4,c3,rch,c2,acc,h2,90}
    hf
    optg,saveact='allene.act',savexyz='allene.xyz' !default optimization
                                                   !using model hessian.
                                                   !Save optimized variables
                                                   !in file allene.act
                                                   !Save optimized geometry
                                                   !in xyz style in
                                                   !file allene.xyz

.. _geometry_optimization_optg--optimization-using-natural-internal-coordinates-bmat:

Optimization using natural internal coordinates (BMAT)
======================================================

.. code-block:: text
   :caption: examples/allene_opt_bmat.inp

    ***, Allene geometry optimization using natural internal coordinates
    basis=sto-3g
   
    rcc=1.32 ang
    rch=1.08 ang
    acc=120  degree
    symmetry,nosym
    Geometry={C1;                       !Z-matrix input
              C2,c1,rcc
              X1,c1,rcc,c2,45
              C3,c2,rcc,c1,180,x1,0
              h1,c1,rch,c2,acc,x1,0
              h2,c1,rch,c2,acc,h1,180
              h3,c3,rch,c2,acc,h1,90
              h4,c3,rch,c2,acc,h2,90}
    hf;
    optg                !default optimization using model hessian
    coord,bmat          !use natural internal coordinates
   
    optg,coord=bmat     !same as above

.. _geometry_optimization_optg--mp2-optimization-using-a-procedure:

MP2 optimization using a procedure
==================================

.. code-block:: text
   :caption: examples/allene_optmp2.inp

    ***, Allene geometry optimization using Z-Matrix
    basis=vdz
   
    rcc=1.32 ang
    rch=1.08 ang
    acc=120  degree
    Geometry={C1                       !Z-matrix input
              C2,c1,rcc
              X1,c1,rcc,c2,45
              C3,c2,rcc,c1,180,x1,0
              h1,c1,rch,c2,acc,x1,0
              h2,c1,rch,c2,acc,h1,180
              h3,c3,rch,c2,acc,h1,90
              h4,c3,rch,c2,acc,h2,90}
   
   optg,procedure=runmp2     !use procedure optmp2
   
   runmp2={hf;mp2}         !procedure definition

.. _geometry_optimization_optg--optimization-using-geometry-diis:

Optimization using geometry DIIS
================================

.. code-block:: text
   :caption: examples/caffeine_opt_diis.inp

    ***, CAFFEINE cartesian coordinates (XYZ format)
    basis=sto-3g
    geomtyp=xyz
    geometry={
    24
               CAFFEINE CARTESIAN COORDINATES
    C          0.8423320060       -0.3654865620        0.0000000000
    C         -0.2841017540       -1.1961236000        0.0000000000
    N          2.0294818880       -1.1042264700        0.0000000000
    N          0.0774743850       -2.5357317920        0.0000000000
    N         -1.6472646000       -0.6177952290        0.0000000000
    C          1.4531962870       -2.3678913120        0.0000000000
    C          0.6373131870        1.1735112670        0.0000000000
    C         -1.7812691930        0.7688916330        0.0000000000
    N         -0.6771444680        1.6306355000        0.0000000000
    O          1.6106752160        1.9349693060        0.0000000000
    O         -2.9202890400        1.2510058880        0.0000000000
    C         -0.9202462430        3.1094501020        0.0000000000
    C         -2.8623938560       -1.4824503660        0.0000000000
    C          3.4552156930       -0.6811094280        0.0000000000
    H          2.0878150460       -3.2451913360        0.0000000000
    H         -1.4989252090        3.4222116470       -0.8897886280
    H         -1.4989252090        3.4222116470        0.8897886280
    H          0.0071905670        3.7148499490        0.0000000000
    H         -3.4903070930       -1.2888938190       -0.8907763360
    H         -3.4903070930       -1.2888938190        0.8907763360
    H         -2.6289534570       -2.5638654230        0.0000000000
    H          4.1360211370       -1.5529079440        0.0000000000
    H          3.6817059520       -0.0685850980        0.8931597470
    H          3.6817059520       -0.0685850980       -0.8931597470
    }
   
    hf
    optg,savexyz=caffeine.xyz   !save optimized geometry in file caffeine.xyz
    coord,bmat                  !Optimization in natural internal coordinates
    method,diis                 !Optimization method: Geometry DIIS
   
    optg,coord=bmat,method=diis,savexyz=caffeine.xyz   !same as above

.. _geometry_optimization_optg--transition-state-of-the-hcn-hnc-isomerization:

Transition state of the HCN – HNC isomerization
===============================================

The first example shows how to do a MP2 transition state optimization. The initial Hessian is taken from a previous HF frequency calculation.

.. code-block:: text
   :caption: examples/hcn_mp2_ts.inp

   ***, HCN <--> NHC Isomerization - Transition State Optimization and Frequencies
   
   l1=1.18268242 ang
   l2=1.40745082 ang
   a1=55.05153416 degree
   
   basis=3-21G
   
   symmetry,nosym
   geometry={
             C
             N,1,l1
             H,2,l2,1,a1}
   
   hf                       ! HF-SCF
   
   frequencies,analytical   ! Vibrational frequencies for HF-SCF (analytical Hessian)
   
   mp2                      ! MP2
   
   optg,root=2,method=rf,readhess     ! Transition State Search using Rational Function
                                      ! Optimizer and HF hessian
   
   frequencies              ! Vibrational frequencies for MP2 (numerical Hessian)
   ---

The second example shows how to do a CCSD(T) optimization with an MP2 hessian. Note that currently the CCSD(T) gradient is computed numerically using finite energy differences, and this can take long time for larger molecules. The calculation of the MP2 hessian finite differences of analytical gradients.

.. code-block:: text
   :caption: examples/hcn_ccsd_ts.inp

   ***, HCN <--> NHC Transition State Optimization and Frequencies
   
   rcn=1.18 ang
   rnh=1.40 ang
   alpha=55 degree
   
   basis=vtz
   
   geometry={
             C
             N,1,rcn
             H,2,rnh,1,alpha}
   
   hf
   ccsd(t)
   optg,numerical,root=2,hessproc=runmp2  !Transition state optimization for ccsd(t)
                                          !using mp2 hessian
   frequencies                  !CCSD(T) frequencies (using numerical second derivatives)
   
   runmp2={hf;mp2}    !procedure definition
   ---

The last example shows how to do a MRCI+Q (MRCI with Davidson correction) optimization with an CASPT2 hessian. As for CCSD(T), the MRCI+Q gradient as computed numerically, while the CASPT2 hessian is obtained using finite differences of analytical CASPT2 gradients.

.. code-block:: text
   :caption: examples/hcn_mrci_ts.inp

   ***, HCN <-> NHC Isomerization - Transition State Optimization and Frequencies
   print,orbitals,civector
   rcn=1.18 ang
   rnh=1.40 ang
   alpha=55 degree
   
   basis=vtz
   
   geometry={
             C
             N,1,rcn
             H,2,rnh,1,alpha}
   
   closed,4      ! global setting for casscf inactive space
   
   hf            ! HF-SCF
   multi         ! CASSCF
   mrci          ! MRCI
   optg,root=2,variable=energd,hessproc=runrs2   !optimize mrci+q transition state
                                                 !and caspt2 for hessian
   
   runrs2={multi;rs2}       !procedure definition for caspt2
   ---

.. _geometry_optimization_optg--reaction-path-of-the-hcn-hnc-isomerization:

Reaction path of the HCN – HNC isomerization
============================================

The following input first optimizes the transition state, and then performs reaction path calculations in both directions. The results are plotted.

.. code-block:: text
   :caption: examples/hcn_isomerization.inp

    ***, HCN <---> NHC Isomerization Reaction Path
    basis=3-21G
   
    rcn=1.18282 ang      ! Starting geometry is transition state
    rnh=1.40745 ang
    alpha=55.05 degree
   
    symmetry,x           ! Cs Symmetry
    geometry={
              C
              N,1,rcn
              H,2,rnh,1,alpha}
   
    int
    rhf,gap_min=0     !set default shift to zero to avoid convergence to wrong state
    optg,root=2,saveact=hcn_ts,rewind            ! Find and store the TS
    {optg,method=qsdpath,dir=1, numhess=5,hesscentral,saveact=hcn_path}
                                                 ! find IRC in positive direction
   
    readvar,hcn_ts.act                           ! Reset geometry to TS
    {optg,method=qsdpath,dir=-1,numhess=5,hesscentral,saveact=hcn_path,append}
                                                 !find IRC in negative direction
   
    readvar,hcn_path.act
   
    alpha=alpha*pi/180    !convert angle to radian
   
    table,irc,rcn,rnh,alpha,e_opt   !tabulate results
   
    {table,irc,e_opt                !plot energy profile as function of irc
     plot,file='hcn_eopt.plot'}
   
    {table,irc,rcn,rnh,alpha        !plot distances and angle as function of irc
     plot,file='hcn_dist.plot'}

This produces the plots

`hcn_eopt.svg <media/hcn_eopt.svg>`__

.. image:: /media/hcn_dist.svg
   :alt: hcn_dist.svg
   :width: 500px

.. _geometry_optimization_optg--optimizing-counterpoise-corrected-energies:

Optimizing counterpoise corrected energies
==========================================

Geometry optimization of counterpoise corrected energies is possible by performing for the total system as well as for each individual fragment separate ``FORCE`` calculations. The gradients and energies are added using the ``ADD`` directive. This requires that ``NOORIENT`` has been specified in the geometry input, in order to avoid errors due to unintended rotation of the system. This default can be disabled using the ``NOCHECK`` option, see ``ADD`` above.

The way a counterpoise corrected geometry optimization works is shown in the following example. Note that the total counterpoise corrected energy must be optimized, not just the interaction energy, since the interaction energy depends on the monomer geometries and has a different minimum than the total energy. The interaction energy could be optimized, however, if the monomer geometries were frozen. In any case, the last calculation before calling ``OPTG`` must be the calculation of the total system at the current geometry (in the example below the dimer calculation), since otherwise the optimizer gets confused.

.. code-block:: text
   :caption: examples/hfdimer_cpcopt1.inp

   ***,HF dimer MP2/CP optimization with relaxed monomers
   
   basis=avtz
   gthresh,energy=1.d-8
   
   ! INITIAL VALUES OF GEOMETRY VARIABLES
   
   RFF=      5.3
   R1=       1.76
   R2 =      1.75
   THETA1 =  7.0
   THETA2 = 111
   
   symmetry,x
   orient,noorient
   geometry={
         f1
         f2  f1  rff
         h1  f1  r1   f2  theta1
         h2  f2  r2   f1  theta2  h1  180.}
   
   label:
   
   text, CALCULATION AT LARGE SEPARATION
   
   rff_save=rff            !save current rff distance
   rff=1000                !dimer calculation at large separation
   
   text, HF1
   
   dummy,f2,h2;            !second hf is now dummy
   {hf;accu,16}            !scf for first monomer
   mp2;                    !mp2 for first monomer
   ehf1inf=energy          !save mp2 energy in variable
   forces;                 !compute mp2 gradient for first monomer
   
   text, HF2
   
   dummy,f1,h1;            !first hf is now dummy
   {hf;accu,16}            !scf for second monomer
   mp2;                    !mp2 for second monomer
   ehf2inf=energy          !save mp2 energy in variable
   forces;                 !compute mp2 gradient for second monomer
   add,1                   !add to previous gradient
   einf=ehf1inf+ehf2inf    !total energy of unrelaxed momomers
   
   rff=rff_save            !reset HF - HF distance to current value
   
   text, CP calculation for HF1 MONOMER
   
   dummy,f2,h2;            !second hf is now dummy
   {hf;accu,16}            !scf for first monomer
   mp2;                    !mp2 for first monomer
   ehf1=energy             !save mp2 energy in variable
   forces;                 !compute mp2 gradient for first monomer
   add,-1                  !subtract from previous gradient
   
   text, CP calculation for HF2 MONOMER
   
   dummy,f1,h1;            !first hf is now dummy
   {hf;accu,16}            !scf for second monomer
   mp2;                    !mp2 for second monomer
   ehf2=energy             !save mp2 energy in variable
   forces;                 !compute mp2 gradient for first monomer
   add,-1                  !subtract from previous gradient
   
   text, DIMER CALCULATION
   dummy                   !reset dummies
   {hf;accu,16}            !scf for dimer
   mp2;                    !mp2 for dimer
   edimer=energy           !save mp2 energy in variable
   forces;                 !compute mp2 gradient for dimer
   add,1                   !add to previous gradient
   
   optg,gradient=1.d-4,startcmd=label:   !find next energy
   
   
   text, compute optimized monomer energy
   
   rhf=r1
   geometry={h1
             F1,H1,rhf}
   
   {hf;accu,16}            !scf for relaxed monomer
   mp2;                    !mp2 for relaxed monomer
   ehf=energy              !save mp2 energy in variable
   optg                    !optimize HF structure
   
   text,optimized geometry parameters
   show,r1,r2,rhf,rff,theta1,theta2
   
   text,computed interaction energies
   decpc=(einf-ehf1-ehf2)*tocm    !counter poise correction
   de=(edimer-ehf1-ehf2)*tocm     !CPC corrected interaction energy relative to unrelaxed monomers
   erelax=(2*ehf-einf)*tocm       !relaxation energy
   derel=de-erelax                !CPC corrected interaction energy relative to relaxed monomoers

The next example shows how the same calculations can be done using numerical gradients. In this case, first the total counter-poise corrected energy is formed and then optimized. Note that the ``ADD`` command does not work for numerical gradients.

.. code-block:: text
   :caption: examples/hfdimer_cpcopt1_num.inp

   ***,HF dimer MP2/CP optimization with relaxed monomers
   
   basis=avtz
   gthresh,energy=1.d-8
   
   ! INITIAL VALUES OF GEOMETRY VARIABLES
   
   RFF=      5.3
   R1=       1.76
   R2 =      1.75
   THETA1 =  7.0
   THETA2 = 111
   
   symmetry,x
   orient,noorient
   geometry={
         f1
         f2  f1  rff
         h1  f1  r1   f2  theta1
         h2  f2  r2   f1  theta2  h1  180.}
   
   label:
   
   text, CALCULATION AT LARGE SEPARATION
   
   rff_save=rff            !save current rff distance
   rff=1000                !dimer calculation at large separation
   
   text, HF1
   
   dummy,f2,h2;            !second hf is now dummy
   {hf;accu,16}            !scf for first monomer
   mp2;                    !mp2 for first monomer
   ehf1inf=energy          !save mp2 energy in variable
   
   text, HF2
   
   dummy,f1,h1;            !first hf is now dummy
   {hf;accu,16}            !scf for second monomer
   mp2;                    !mp2 for second monomer
   ehf2inf=energy          !save mp2 energy in variable
   einf=ehf1inf+ehf2inf    !total energy of unrelaxed momomers
   
   rff=rff_save            !reset HF - HF distance to current value
   
   text, CP calculation for HF1 MONOMER
   
   dummy,f2,h2;            !second hf is now dummy
   {hf;accu,16}            !scf for first monomer
   mp2;                    !mp2 for first monomer
   ehf1=energy             !save mp2 energy in variable
   
   text, CP calculation for HF2 MONOMER
   
   dummy,f1,h1;            !first hf is now dummy
   {hf;accu,16}            !scf for second monomer
   mp2;                    !mp2 for second monomer
   ehf2=energy             !save mp2 energy in variable
   
   text, DIMER CALCULATION
   dummy                   !reset dummies
   {hf;accu,16}            !scf for dimer
   mp2;                    !mp2 for dimer
   edimer=energy           !save mp2 energy in variable
   etot=edimer-ehf2-ehf1+ehf1inf+ehf2inf  !total BSSE corrected energy
   
   optg,numerical,variable=etot,gradient=1.d-4,startcmd=label:   !optimize geometry
   
   
   text, compute optimized monomer energy
   
   rhf=r1
   geometry={h1
             F1,H1,rhf}
   
   {hf;accu,16}            !scf for relaxed monomer
   mp2;                    !mp2 for relaxed monomer
   ehf=energy              !save mp2 energy in variable
   optg                    !optimize HF structure
   
   text,optimized geometry parameters
   show,r1,r2,rhf,rff,theta1,theta2
   
   text,computed interaction energies
   decpc=(einf-ehf1-ehf2)*tocm    !counter poise correction
   de=(edimer-ehf1-ehf2)*tocm     !CPC corrected interaction energy relative to unrelaxed monomers
   erelax=(2*ehf-einf)*tocm       !relaxation energy
   derel=de-erelax                !CPC corrected interaction energy relative to relaxed monomoers

In the last example the monomer structures are kept fixed, and the interaction energy is optimized.

.. code-block:: text
   :caption: examples/hfdimer_cpcopt2.inp

   ***,HF dimer MP2/CP optimization without monomer relaxation
   
   basis=avtz
   gthresh,energy=1.d-8
   
   ! INITIAL VALUES OF GEOMETRY VARIABLES
   
   RFF=      5.3
   THETA1 =  7
   THETA2 = 111
   
   symmetry,x
   orient,noorient
   geometry={
         f1
         f2  f1  rff
         h1  f1  1.74764059   f2  theta1
         h2  f2  1.74764059   f1  theta2  h1  180.}   !using fixed HF distances of isolated HF
   
   label:
   
   text, CP calculation for HF1 MONOMER
   
   dummy,f2,h2;            !second hf is now dummy
   {hf;accu,16}            !scf for first monomer
   mp2;                    !mp2 for first monomer
   ehf1=energy             !save mp2 energy in variable
   forces;                 !compute mp2 gradient for first monomer
   scale,-1                !multiply gradient by -1
   
   text, CP calculation for HF2 MONOMER
   
   dummy,f1,h1;            !first hf is now dummy
   {hf;accu,16}            !scf for second monomer
   mp2;                    !mp2 for second monomer
   ehf2=energy             !save mp2 energy in variable
   forces;                 !compute mp2 gradient for first monomer
   add,-1                  !subtract from previous gradient
   
   text, DIMER CALCULATION
   dummy                   !reset dummies
   {hf;accu,16}            !scf for dimer
   mp2;                    !mp2 for dimer
   edimer=energy           !save mp2 energy in variable
   forces;                 !compute mp2 gradient for dimer
   add,1                   !add to previous gradient
   
   optg,gradient=1.d-5,startcmd=label:   !find next energy
   
   text,optimized geometry parameters
   show,rhf,rff,theta1,theta2
   
   text,computed interaction energies
   de=(edimer-ehf1-ehf2)*tocm     !CPC corrected interaction energy with fixed monomers

.. _geometry_optimization_optg--adding-cabs-singles-correction-in-ccsd-t-f12-geometry-optimization:

Adding CABS singles correction in CCSD(T)-F12 geometry optimization
===================================================================

Geometry optimization using CCSD(T)-F12 method including CABS singles corrections is possible by combining numerical gradients for HF+CABS singles method and analytical gradients for DF-CCSD(T)-F12 method obtained in separate ``FORCE`` calculations. The gradients are added using the ``ADD`` directive. Similarly to the example `optimizing counterpoise corrected energies <geometry_optimization_optg.html#optimizing-counterpoise-corrected-energies>`__, ``NOORIENT`` is required. The following example shows geometry optimization for the hydrogen fluoride molecule using DF-CCSD(T)-F12b method without and with CABS singles correction.

.. code-block:: text
   :caption: examples/dfccsdtf12_3stc_tight_opt.inp

   ***, geometry optimization (tight thresholds) for HF using DF-CCSD(T)-F12b/3*C(FIXC,HY1) without and with CABS singles
   gthresh,energy=1.d-10,gradient=1.d-08
   
   nosym
   noorient
   angstrom
   geometry={
       2
   
    F          0.0000000000        0.0000000000       -0.0463705158
    H          0.0000000000        0.0000000000        0.8745302823
   }
   
   
   basis=avdz
   
   ! perform geometry optimization using CCSD(T)-F12b/3*C(FIXC,HY1) without CABS singles by using analytical derivatives
   {df-hf;accu,18;}
   {df-ccsd(t)-f12,ansatz=3*C(fixc,hy1),cabs_singles=0,cabs=0,ri_basis=optri,thrcabs=1.d-10,thrcabs_rel=1.d-10,thrabs=1.d-10,thrabs_rel=1.d-10,gem_beta=1.0d0;cphf,thrmin=1.d-9;}
   {optg,energy=1.d-08,gradient=1.d-06;}
   
   ! save geometry parameters for printing
   struct,distvar=ccf12distwocabs,angvar=ccf12angwocabs,dihedvar=ccf12dihedwocabs
   
   ! perform geometry optimization using CCSD(T)-F12b/3*C(FIXC,HY1) with CABS singles by using numerical and analytical derivatives
   label1
   ! compute CABS singles forces by using numerical derivatives
   {df-hf;accu,18}
   {df-mp2-f12,cabs_singles=-1,ri_basis=optri,thrcabs=1.d-10,thrcabs_rel=1.d-10,thrabs=1.d-10,thrabs_rel=1.d-10,gem_beta=1.0d0}
   {forces,variable=ef12_singles,varsav=on,fourpoint}
   ! compute CCSD(T)-F12b/3*C(FIXC,HY1) without CABS singles forces by using analytical derivatives
   {df-hf;accu,18;}
   {df-ccsd(t)-f12,ansatz=3*C(fixc,hy1),cabs_singles=0,cabs=0,ri_basis=optri,thrcabs=1.d-10,thrcabs_rel=1.d-10,thrabs=1.d-10,thrabs_rel=1.d-10,gem_beta=1.0d0;cphf,thrmin=1.d-9;}
   {forces,varsav=on;add,1} ! add the forces
   {optg,startcmd=label1,energy=1.d-08,gradient=1.d-06;}
   
   ! save geometry parameters for printing
   struct,distvar=ccf12dist,distdef=distance,angvar=ccf12ang,angdef=angle,dihedvar=ccf12dihed,diheddef=dihedral
   
   ! compute CABS singles correction for bond length
   distcorr=ccf12dist-ccf12distwocabs
   
   ! print results
   table,distance,ccf12distwocabs,ccf12dist,distcorr
