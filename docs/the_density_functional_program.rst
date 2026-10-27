.. raw:: html

   <span id="angular-integration-grid-angular"></span>

.. raw:: html

   <span id="asymptotic-correction-for-xc-potentials-asymp"></span>

.. raw:: html

   <span id="atom-partitioning-of-integration-grid-voronoi"></span>

.. raw:: html

   <span id="density-source-density-odensity"></span>

.. raw:: html

   <span id="directives"></span>

.. raw:: html

   <span id="double-hybrid-functionals-dh-dsdh"></span>

.. raw:: html

   <span id="dump-integrand-values-dftdump"></span>

.. raw:: html

   <span id="empirical-damped-dispersion-correction"></span>

.. raw:: html

   <span id="exact-exchange-computation-exchange"></span>

.. raw:: html

   <span id="exact-exchange-kohn-sham-methods"></span>

.. raw:: html

   <span id="exchange-correlation-potential-potential"></span>

.. raw:: html

   <span id="fractional-orbital-occupation-calculations"></span>

.. raw:: html

   <span id="grid-blocking-factor-dftblock"></span>

.. raw:: html

   <span id="grid-caching-gridsave-nogridsave"></span>

.. raw:: html

   <span id="grid-printing-gridprint"></span>

.. raw:: html

   <span id="grid-symmetry-gridsym-nogridsym"></span>

.. raw:: html

   <span id="libxc-functionals"></span>

.. raw:: html

   <span id="local-hartree-fock-lhf-method"></span>

.. raw:: html

   <span id="neese-grids-grid-name-neese"></span>

.. raw:: html

   <span id="nonlocal-dft-nldft"></span>

.. raw:: html

   <span id="numerical-integration-grid-control-grid"></span>

.. raw:: html

   <span id="optimised-effective-potential-oep-method"></span>

.. raw:: html

   <span id="options"></span>

.. raw:: html

   <span id="orientation-of-atomic-grids-orient"></span>

.. raw:: html

   <span id="radial-integration-grid-radial"></span>

.. raw:: html

   <span id="random-phase-approximation"></span>

.. raw:: html

   <span id="rangehybrid-methods-rangehybrid"></span>

.. raw:: html

   <span id="sg-grids-grid-name-sg"></span>

.. raw:: html

   <span id="target-quadrature-accuracy-gridthresh"></span>

.. raw:: html

   <span id="thresholds-dftthresh"></span>

.. raw:: html

   <span id="time-dependent-density-functional-theory"></span>

.. raw:: html

   <span id="van-der-waals-df-s"></span>

.. _the_density_functional_program--the-density-functional-program:

The density functional program
==============================

Density-functional theory calculations may be performed using one of the following commands:

* ``DFT`` calculate functional of a previously computed density.
* **``RKS`` or ``RKS-SCF``** calls the spin-restricted Kohn-Sham program. ``KS`` and ``KS-SCF`` are aliases for ``RKS``.
* **``UKS`` or ``UKS-SCF``** calls the spin-unrestricted Kohn-Sham program

Each of these commands may be qualified with the key-names of the functional(s) which are to be used, and further options:

*command, key1, key2, key3, :math:`\ldots`*, *options*

If no functional keyname is given, the default is ``LDA`` (see below). Following this command may appear directives specifying options for the density-functional modules (see section `directives <the_density_functional_program.html#directives>`__) or the Hartree-Fock program (see section `options <the_scf_program.html#options>`__).

On completion of the functional evaluation, or self-consistent Kohn-Sham calculation, the values of the individual functionals are stored in the Molpro vector variable ``DFTFUNS``; the total is in ``DFTFUN``, and the corresponding individual functional names in ``DFTNAME``.

Energy gradients are available for self-consistent Kohn-Sham calculations.

Density fitting can be used for closed and open-shell spin-restricted KS and is invoked by a prefix ``DF-`` (``DF-KS`` or ``DF-RKS``, see section :doc:`density fitting <density_fitting>`). For UKS, only Coulomb fitting is possible (``CF-UKS``). Density fitting is highly recommended (unless explicit symmetry handling is required), as the induced errors are negligible and it offers *massive* speed increases, particularly for pure functionals. For details see R. Polly, H.-J. Werner, F. R. Manby, and Peter J. Knowles, *Fast Hartree-Fock theory using local density fitting approximations*, `Mol. Phys. <https://dx.doi.org/10.1080/0026897042000274801>`__ **102**, 2311 (2004). **All publications resulting from DF-HF or DF-KS calculations should cite this work.**

Normally, sensible defaults are used to define the integration grid. The accuracy can be controlled using options as described in section `options <the_density_functional_program.html#options>`__ or directives as described in section `directives <the_density_functional_program.html#directives>`__. More control is provided by the ``GRID`` command, as described in section `numerical integration grid control (GRID) <the_density_functional_program.html#numerical-integration-grid-control-grid>`__. **It is recommended to use tighter grid thresholds than those set by default in Molpro if meta-GGA type functionals are used in the calculation, see also `J. Chem. Phys. 157, 234106 (2022) <https://doi.org/10.1063/5.0119622>`__ where the accuracy of different DFT quadrature grids is analysed for different functionals!**

.. _the_density_functional_program--options:

Options
=======

The following options may be specified on the ``KS`` or ``UKS`` command lines:

* **``GRIDTHR``\ =\ *target*** Specifies the grid target accuracy (per atom). The default is 1.d-6 unless this has been modified using a global ``THRESH, GRID`` option.
* **``COARSEGRID`` (logical)** If *true*, perform initial iterations with a coarser grid. Default is *false*.
* **``GRIDMAX``\ =\ *gridmax*** In the initial iterations, the grid accuracy is min(*gridmax, target\*coarsefac*) (only if COARSEGRID is set).
* **``COARSEFAC``\ =\ *coarsefac*** Factor for initial grid accuracy (see above). The default is 1000.
* **``GRIDGRAD``\ =\ *0 or 1*** Defines whether grid weight derivatives are included in analytical gradient calculations (default: 0). Disabling these can improve convergence in geometry optimizations.
* **``DFTFAC``\ =\ ``[``\ *fac1,fac2,..*\ ``]``** Factors for each functional. The number of given values must agree with the number of functionals.
* **``EXFAC``\ =\ *factor*** Fraction of exact exchange added to the functional. The default depends on the functional.
* **``TOLORB``\ =\ *value*** Threshold for orbital screening (default depends on energy threshold).

In addition, all options valid for HF (see section `options <the_scf_program.html#options>`__) can be given.

.. _the_density_functional_program--directives:

Directives
==========

The following options may be used to control the operation of the DFT modules. In the Kohn-Sham case, these may come in any order before or after directives for the SCF program as described in Section :doc:`the SCF program <the_scf_program>`.

.. _the_density_functional_program--density-source-density-odensity:

Density source (DENSITY, ODENSITY)
==================================

``DENSITY,orbc.filec,$\dots$ ODENSITY,orbo.fileo,$\dots$``

For non-self-consistent ``DFT`` calculations, specifies the source of the density matrix. The total density is read from *orbc.filec*, with further options specifying density sets in the standard way as described in Section `selecting orbitals and density matrices (ORBITAL, DENSITY) <general_program_structure.html#selecting-orbitals-and-density-matrices-orbital-density>`__. ``ODENSITY`` can be used to specify the spin density. The defaults are the densities last written by an SCF or MCSCF program.

.. _the_density_functional_program--thresholds-dftthresh:

Thresholds (DFTTHRESH)
======================

``DFTTHRESH,key1=value1,key2=value2$\ldots$``

Sets various truncation thresholds. *key* can be one of the following.

* ``TOTAL`` Overall target accuracy (per atom) of density functional. Defaults to the value of the global threshold command:gthresh ``GRID`` or the value specified by option ``GRID``. For proper use of this threshold, other thresholds should be left at their default value of zero.
* ``ORBITAL`` Orbital truncation threshold.
* ``DENSITY`` Density truncation threshold.
* ``FOCK`` Fock matrix truncation threshold.

.. _the_density_functional_program--exact-exchange-computation-exchange:

Exact exchange computation (EXCHANGE)
=====================================

``EXCHANGE,factor``

For Kohn-Sham calculations, compute exchange energy according to Hartree-Fock formalism and add the contribution scaled by *factor* to the fock matrix and the energy functional. Otherwise, the default is *factor=0*, i.e., the exchange is assumed to be contained in the functional, and only the Coulomb interaction is calculated explicitly.

``DFTFACTOR,fac1, fac2, ...``

Provide a factor for each functional specified. The functionals will be combined accordingly. By default, all factors are one.

.. _the_density_functional_program--double-hybrid-functionals-dh-dsdh:

Double-hybrid functionals (DH, DSDH)
====================================

``DH, ax, ac``

initiates a double-hybrid calculation (Ref. [1]) where :math:`a_x` is the fraction of HF exchange and :math:`a_c` is the fraction of MP2 correlation. A self-consistent KS calculation is performed with functional :math:`a_x E_x^{\text{HF}} + (1-a_x) E_x^{\text{DFT}}[\rho] + (1-a_c) E_c^{\text{DFT}}[\rho]`. One then needs to call the MP2 program to add the MP2 contribution :math:`a_c E_c^{\text{MP2}}`. If :math:`a_c` is not given, :math:`a_c=a_x^2` is assumed, according to Ref. [2].
``DSDH, ax, ac``

initiates a density-scaled double-hybrid calculation (Ref. [2]) where :math:`a_x` is the fraction of HF exchange and :math:`a_c` is the fraction of MP2 correlation. A self-consistent KS calculation is performed with functional :math:`a_x E_x^{\text{HF}} + (1-a_x) E_x^{\text{DFT}}[\rho] + E_c^{\text{DFT}}[\rho] - a_c E_c^{\text{DFT}}[\rho_{1/\sqrt{a_c}}]`, where :math:`\rho_{1/\sqrt{a_c}}` is the scaled density. In the case of meta-GGA functionals, the kinetic energy density :math:`\tau` is also scaled, according to Ref. [3]. One then needs to call the MP2 program to add the MP2 contribution :math:`a_c E_c^{\text{MP2}}`. If :math:`a_c` is not given, :math:`a_c=a_x^2` is assumed, according to Ref. [2].

Example of input for B2-PLYP calculation (Ref. [1]):
``{ks,b,lyp;dh,0.53,0.27;}\\``
``mp2,ksfock;``

Note that the option ``ksfock`` needs to be added to the ``mp2`` command which will choose the KS hamiltonian instead of the Fock matrix as :math:`H_0` in the MP2 program. This affects only the denominators used in the second-order correlation energy terms. Additional singles contributions that would enter with ``ksfock`` due to the violation of Brillouin's theorem are not computed in the closed-shell MP2 program.

Example of input for 1DH-BLYP calculation (Ref. [2]):
``{ks,b,lyp;dh,0.65;}\\``
``mp2,ksfock;``

Example of input for DS1DH-TPSS calculation (Ref. [3]):
``{ks,tpss;dsdh,0.725;}\\``
``mp2.ksfock;``

``Unrestricted calculations (uks, ump2) can also be done.``

References:
:math:`[1]` S. Grimme, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.2148954>`__ **124**, 034108 (2006).
:math:`[2]` K. Sharkas, J. Toulouse, A. Savin, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3544215>`__ **134**, 064113 (2011).
:math:`[3]` S. M. O. Souvi, K. Sharkas, J. Toulouse, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.4865963>`__ **140**, 084107 (2014).

.. _the_density_functional_program--rangehybrid-methods-rangehybrid:

Rangehybrid methods (RANGEHYBRID)
=================================

For coupling of short-range (sr-)DFT with long-range (lr-)ab-initio methods, one first has to specify the coupling parameter :math:`\mu` in the sr interelectronic interaction :math:`\sum_{i<j} {\rm erf} (\mu r_{ij})/r_{ij}`; this can be done by setting a variable (e.g. ``mu=0.5``). As a next step, long-range ERIs have to be calculated by calling the integral program (e.g. ``int;erf,mu;``).

Then sr-DFT/lr-HF calculations can be performed by calling the RKS program with the additional subcommand ``rangehybrid``. Available short-range functionals are ``exerf`` and ``ecerf`` for sr-LDA, and ``exerfpbe`` and ``ecerfpbe`` for sr-PBE; as usual, the functionals have to be specified after the ``rks`` command (e.g. ``rks,exerf,ecerf;``). The underlying short-range LDA correlation functional is that of S. Paziani, S. Moroni, P. Gori-Giorgi, G.B. Bachelet, `Phys. Rev. B <https://dx.doi.org/10.1103/PhysRevB.73.155111>`__ **73**, 155111 (2006).

Moreover, range-separated KS calculations can also be performed using functionals from the `LibXC library <the_density_functional_program.html#libxc-functionals>`__, including the CAM-B3LYP functional (``HYB_GGA_XC_CAM_B3LYP``) and the :math:`\omega`\ B97X functional (``HYB_GGA_XC_WB97X``). When using those functionals parameters for the range-separation parameter ``MU`` as well as the short- and long-range intrection factors (``SRFAC`` and ``LRFAC``) do not need to be explicitly entered in the input but are taken from the LibXC internal database instead. There are several ways to overwrite these via user input as shown for the CAM-B3LYP functional in the following example:

.. code-block:: text

   !no explicit parameter input
   ks,HYB_GGA_XC_CAM_B3LYP
   
   !pass parameters to integral program
   {int; ERFLERFC,mu=0.33,srfac=0.19,lrfac=0.65}
   {ks,HYB_GGA_XC_CAM_B3LYP}
   
   !pass parameters as DFT options
   {ks,HYB_GGA_XC_CAM_B3LYP,mu=0.33,srfac=0.19,lrfac=0.65}
   
   !density-fitting case: no explicit parameter input
   {df-ks,HYB_GGA_XC_CAM_B3LYP}
   
   !now use modified parameters in the integral program
   {int; ERFLERFC,mu=0.2,srfac=0.23,lrfac=0.8}
   ks,HYB_GGA_XC_CAM_B3LYP
   
   !or as an option to KS (in which case the integral program will be automatically executed with the new settings)
   {ks,HYB_GGA_XC_CAM_B3LYP,mu=0.2,srfac=0.23,lrfac=0.8}

When using any of Molpro's internal range-separated functionals instead (including ``EXERFPBE``, ``ECERFPBE``, ``SRB88``, ``SRLYP``, ``EXERF``, ``ECERF`` and more) the following default values for the underlying parameters will be used if no input is made to change them: ``MU``\ =0.5, ``SRFAC``\ =0.0, ``LRFAC``\ =1.0. Note that changing the parameters will only work locally for the respective calculation, but Molpro will reset to the default again if a successive RS DFT calculation is done without specifying the parameters on the input.

Finally, sr-DFT/lr-post-HF calculations can be done by adding, within a call of the chosen post-HF program, two subcommands: ``srxcdft`` followed by the desired short-range functionals (e.g. ``srxcdft,exerf,ecerf;``), and ``dftden`` followed by the record number from which the density for the sr functionals is taken. Implementations are available for ``ci``, ``mp2``, ``ccsd``, ``ccsd(t)``, ``rpatddft``, and the corresponding local MP2 and CC methods w/wo density-fitting.

General two-parameter range-separated double hybrids (RSDH) as described in [1] are also available.
Example of a RSDH calculation with the approximation 3 of Ref. [1] for the short-range density functional:

.. code-block:: text

   mu=0.46
   lambda=0.58
   {int; erflerfc,mu=$mu,srfac=$lambda}
   {rks,exsrlpbe,ecsqrtlpbe;rangehybrid;orbital,7000.2}
   {mp2; srxcdft,exsrlpbe,ecsqrtlpbe;dftden,7000.2}

Example of a RSDH calculation with the approximation 4 of Ref. [1] for the short-range density functional:

.. code-block:: text

   mu=0.62
   lambda=0.60
   {int; erflerfc,mu=$mu,srfac=$lambda}
   {ks,exerfpbe,ecerfpbe; rangehybrid; dsrsdh; orbital,7000.2}
   mp2

Note that the ``erflerfc`` option to the integral program can be used to calculate arbitrary mixtures of short-range and long-range Coulomb repulsion integrals via, e.g.,

.. code-block:: text

   mu=0.5    !range-separation parameter
   sr=0.5    !scaling factor for erfc interaction
   lr=0.5    !scaling factor for erf interaction
   {int;erflerfc,mu=$mu,srfac=$sr,lrfac=$lr}

which corresponds to the interaction operator :math:`\mbox{lr}\cdot\frac{\mbox{erf}(\mu r_{12})}{r_{12}} + \mbox{sr}\cdot\frac{\mbox{erfc}(\mu r_{12})}{r_{12}}`. Setting ``lr=1`` and ``sr=1`` would therefore mean that Molpro will calculate the full-range Coulomb integrals.

The MP2 calculation can also be replaced by a RPA calculation, like in the RS2H+RPAxSO2 method of Ref. [2].
Example of a RS2H+RPAxSO2 calculation:

.. code-block:: text

   mu=0.48
   lambda=0.34
   {int; erflerfc,mu,lambda}
   {rks,exsrlpbe,ecsqrtlpbe; rangehybrid; orbital,7000.2}
   {rpatddft; ecorr,SO2-RCCD;orb,7000.2}

Reference
:math:`[1]` C. Kalai and J. Toulouse, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.5025561>`__ **148**, 164105 (2018).
:math:`[2]` C. Kalai, B. Mussard, and J. Toulouse, `J. Chem. Phys. <https://doi.org/10.1063/1.5108536>`__ **151**, 074102 (2019).

.. _the_density_functional_program--exchange-correlation-potential-potential:

Exchange-correlation potential (POTENTIAL)
==========================================

``POTENTIAL,rec.fil``

For stand-alone DFT calculations, compute exchange-correlation potential pseudo-matrix elements, defined formally as the differential of the sum of all specified functionals with respect to elements of the atomic orbital density matrix. The matrix is written to record *rec* on file *fil*.

.. _the_density_functional_program--grid-blocking-factor-dftblock:

Grid blocking factor (DFTBLOCK)
===============================

``DFTBLOCK,nblock``

Respecify the number of spatial integration points treated together as a block in the DFT integration routines (default 128). Increasing *nblock* may enhance efficiency on, e.g., vector architectures, but leads to increased memory usage.

.. _the_density_functional_program--dump-integrand-values-dftdump:

Dump integrand values(DFTDUMP)
==============================

``DFTDUMP,file,status``

Write out values of the integrand at grid points to the file *file*. The first line of *file* contains the number of functional components; there then follows a line for each functional giving the input key of the functional. Subsequent lines give the functional number, cartesian coordinates, integrand value and integration weight with Fortran format ``(I2,3F15.10,F23.15)``.

.. _the_density_functional_program--asymptotic-correction-for-xc-potentials-asymp:

Asymptotic correction for xc-potentials(ASYMP)
==============================================

``ASYMP,shift,$\alpha$,$\beta$,b``

Activates the gradient-regulated asymptotic correction (GRAC) approach for exchange-correlation potentials of Grüning *et al.* (`J. Chem. Phys. <https://dx.doi.org/10.1063/1.1327260>`__ **114**, 652 (2001)). The user has to supply a *shift* parameter (:math:`\Delta_{\text{xc}}`) for the bulk potential which should approximate the difference between the HOMO energy (:math:`\varepsilon_{\text{HOMO}}`) obtained from the respective standard Kohn-Sham calculation and the (negative) ionisation potential of the monomer (:math:`\text{IP}`):

.. math::

   \Delta_{\text{xc}}=\varepsilon_{\text{HOMO}}-(-\text{IP})

This method accounts for the derivative discontinuity of the exact xc-potential and that is missing in approximate ones. The parameters :math:`\alpha` and :math:`\beta` determine the interpolation function (see Eq. (2.3) in the above reference) and are set to :math:`\alpha=0.5` and :math:`\beta=40` by default, respectively. The parameter *b* is the parameter of the asymptotic xc-potential from van Leeuwen and Baerends (`Phys. Rev. A <https://dx.doi.org/10.1103/PhysRevA.49.2421>`__ **49**, 2421 (1994), Eqns. (54,55)) and is set to *b*\ =0.05 by default.

In case of gradient or laplacian functionals the modified GRAC scheme of Bast *et al.* (Chem. Phys. Chem. **9**, 445 (2008)) is used.

If *shift* is set to zero in the input the program will estimate the ionisation energy from the HOMO energy during the SCF (as soon as the HOMO energy is converged to a given threshold) and then sets the bulk shift automatically. This is done by using a linear fit of DFT HOMO energies to ionisation energies calculated with the :math:`\Delta`\ SCF method for a range of molecules (see also S. Hirata *et al.*, J. Phys. Chem. A, **107**, 10154 (2003)).

.. _the_density_functional_program--testing-the-xc-functional-implementation-dfttest:

Testing the xc functional implementation (DFTTEST)
==================================================

Using the directive ``DFTTEST`` it is possible to test the xc potential matrix elements against numerical derivatives. For this, use

.. code-block:: text

   {dft,<functional>; dfttest,1}

upon which a list with the analytical/numerical xc potential matrix elements is printed in the output file. Note that, by definition, some functionals implemented in Molpro will fail this test, e.g., LB94 which computes the van Leuween-Baerends xc potential that has no well defined xc functional that it is based upon (the B88 exchange functional is computed for LB94 instead).

It is also possible to compute the overlap matrix (and thus the electron number) within the DFT program. For this the test functional ``STEST`` has to be used (as the only functional on the input):

.. code-block:: text

   {dft,stest; dfttest,0}

The additional directive ``dfttest,0`` also will print a list of the overlap matrix elements and ``dfttest,1`` will, again, also test the functional derivatives. This test is useful to investigate the accuracy of the quadrature grid, see section `numerical integration grid control (GRID) <the_density_functional_program.html#numerical-integration-grid-control-grid>`__.

.. _the_density_functional_program--numerical-integration-grid-control-grid:

Numerical integration grid control (GRID)
-----------------------------------------

Density functionals are evaluated through numerical quadrature on a grid in three-dimensional space. Although the sensible defaults will usually suffice, the parameters that define the grid can be specified by using the ``GRID`` command, which should be presented *before* the ``DFT`` or ``KS`` commands that will use the grid, but after the geometry definition. Typically, the input file then could look like

.. code-block:: text

   {grid,<grid options>; <grid directives>}
   {ks,...}

All grid parameters that are modified through the options and directives of the ``GRID`` program are changed globally, i.e., any subsequent program using a quadrature grid in Molpro will use the grid determined by GRID unless they use any local redefinitions of grid parameters.  Alternatively, any available
options for ``GRID`` (but not directives that require multiple input values) can be used within the ``KS`` program:

.. code-block:: text

   {ks,...,<grid options>}

Note that then, however, the modifications to the grid parameters are only applied during the KS calculation but they are reset to their default state afterwards. Also note that the directives which are available for ``GRID`` can not be used with ``KS``, so these can be exclusively only used for ``GRID``.
The grid parameters are stored internally on a record whose location can be changed by

``GRID,[record=orb.file],[status=status]``

By default Molpro uses the record *orb.file* = 1800.2 to store the grid parameters that are independent of the geometry. The information on disk consists of two parts: the parameters necessary to define the grid (record on file 2), and a cache of the evaluated grid points and weights (corresponding record on file 1, usually 1800.1). The latter is flagged as ‘dirty’ whenever any parameters are changed, and whenever the geometry changes; if the cache is dirty, then when an attempt is made to use the grid, it will be recalculated, otherwise the cached values are used.

If *status* is ``OLD``, an attempt to restore the grid from a previous calculation is performed; effectively, the old grid provides a template of parameters which can be adjusted using the parameter commands described below. If *status* is ``NEW``, the grid is always created with default parameters. If *status* is ``UNKNOWN`` (the default), a new grid is created if record *orb.file* does not exist; otherwise the old grid is used.

The ``GRID`` command may be followed by a number of parameter-modifying directives. The currently implemented default parameters are equivalent to the following input commands.

.. code-block:: text

   RADIAL,LOG,3,1.0,20,25,25,30
   ANGULAR,LEBEDEV,0.0,0.0
   LMIN,0,0,0,0
   LMAX,53,53,53,53
   VORONOI,10
   GRIDSAVE
   GRIDSYM

Options that have a single values directives can be given as an option to ``GRID`` or ``KS``:

.. code-block:: text

   {GRID,GRIDTHR=...,FACNEIGH=...}
   
   or
   
   {KS,GRIDTHR=...,FACNEIGH=...}

where ``GRIDTHR`` just takes a scalar value for the global grid threshold value, so using the corresponding directive will be still necessary if
different thresholds for the radial and angular grid shall be used, see below.

Molpro can use both an internal implementation to compute the quadrature grid (termed *dftgrid* here) and an external library called *libxcgrid*. For adaptive (pruned) grids, that are computed by default, one can switch between the two cases using

.. code-block:: text

   {grid,name=PRUNED}

for using *xcgrid* and

.. code-block:: text

   {grid,name=OLD}

to reset to *dftgrid* again. *xcgrid* in addition also contains implementations for some fixed quadrature grids, see below. Most of the options and directives described in the following can be used in conjunction with both programs. However, some can only be exclusively used with either of the two codes. To highlight this in the following, the *dftgrid*-exclusive options will be marked by ``dftgrid.png?nolink&50`` whereas the *libxcgrid*-exclusive ones by ``xcgrid.png?nolink&50``.

.. _the_density_functional_program--summary-of-options-and-directives-for-grid:

Summary of options and directives for GRID
==========================================

Almost all grid parameters can be controlled through respective options given on the GRID card:

.. code-block:: text

   {grid,option1=value1,option2=value2,...}

A limited number of subcommands (directives) are also available that can be used in the input like:

.. code-block:: text

   {grid; directive1,val1a,val1b,...; directive2,val2a,val2b,}

where *val1a*,\ *val1b*,... are lists of comma-separated values for the first directive, etc.

The following table summarises the options that can be used for GRID. The last two columns displays if the respective option is available with the ``dftgrid.png?nolink&50`` and ``xcgrid.png?nolink&50`` programs. A detailed description of the different options will be given in the upcoming sections.

.. list-table::
   :header-rows: 2

   * - Options for GRID
     - 
     - 
     - 
     - 
     - 
     - 
     - 
     - 
   * - group
     - name
     - default value
     - description
     - ``dftgrid.png?nolink&50``
     - ``xcgrid.png?nolink&50``
     - 
     - 
     - 
   * - grid type
     - ``NAME``
     - *old*
     - select pruned or fixed standard grids
     - ✔
     - ✔
     - 
     - 
     - 
   * - accuracy
     - ''GRIDTHR
     - THRESHOLD_OVERALL
     - GRID
     - THRGRID''
     - *acc*\ =1d-6
     - target grid threshold
     - ✔
     - ✔
   * - 
     - ''GRIDTHR_RAD
     - THRESHOLD_RADIAL
     - ACCR''
     - *acc*/2
     - target threshold for radial grid
     - ✔
     - ✔
     - 
   * - 
     - ''GRIDTHR_ANG
     - THRESHOLD_ANGULAR
     - ACCA''
     - *acc*/10
     - target threshold for angular grid
     - ✔
     - ✔
     - 
   * - 
     - ''GRIDACC
     - MODE''
     - *default*
     - global mode for grid accuracy
     - ✔
     - ✔
     - 
     - 
   * - 
     - ``ANGLEVEL``
     - ✘
     - use fixed angular grids in three-zone decomposition of radial grid
     - ✔
     - 
     - 
     - 
     - 
   * - radial integration grid
     - ``RADIAL_SCHEME``
     - *log*
     - radial integration scheme
     - ✔
     - ✔
     - 
     - 
     - 
   * - 
     - ''GRIDTHR_RAD
     - THRESHOLD_RADIAL
     - ACCR''
     - *acc*/2
     - target threshold for radial grid
     - ✔
     - ✔
     - 
   * - 
     - ``RADIAL_SCALING``
     - ✘
     - scaling factors for atomic radial grids
     - 
     - ✔
     - 
     - 
     - 
   * - 
     - ``MIN_NR``
     - [20,25,25,30]
     - lower bound for degrees of quadrature for H,He, 2nd row, 3rd row, other elements
     - ✔
     - ✔
     - 
     - 
     - 
   * - 
     - ``MAX_NR``
     - [500,500,500,500]
     - upper bound for degrees of quadrature for H,He, 2nd row, 3rd row, other elements
     - ✔
     - ✔
     - 
     - 
     - 
   * - angular integration grid
     - ``ANGULAR_SCHEME``
     - *lebedev*
     - angular integration scheme
     - ✔
     - ✔
     - 
     - 
     - 
   * - 
     - ''THRESHOLD_ANGULAR
     - GRIDTHR_ANG
     - ACCA''
     - *acc*/10
     - target threshold for angular grid
     - ✔
     - ✔
     - 
   * - 
     - ``ANGLEVEL``
     - ✘
     - use fixed angular grids in three-zone decomposition of radial grid
     - ✔
     - 
     - 
     - 
     - 
   * - 
     - ``MIN_L``
     - [0,0,0,0]
     - minimum angular order for H,He, 2nd row, 3rd row, other elements
     - ✔
     - ✔
     - 
     - 
     - 
   * - 
     - ``MAX_L``
     - [59,59,59,59]
     - maximum angular order for H,He, 2nd row, 3rd row, other elements
     - ✔
     - ✔
     - 
     - 
     - 
   * - atom partitioning
     - ``VORONOI_SCHEME``
     - *murray*
     - type of step function
     - ✔
     - ✔
     - 
     - 
     - 
   * - 
     - ``SIZEADJ``
     - *treutler*
     - size adjustment method
     - ✔
     - ✔
     - 
     - 
     - 
   * - 
     - ``BECKE_MMU``
     - 3
     - :math:`m_\mu` recursion value in Becke scheme
     - ✔
     - ✔
     - 
     - 
     - 
   * - 
     - ``MURRAY_MMU``
     - 10
     - :math:`m_\mu` recursion value in Murray scheme
     - ✔
     - ✔
     - 
     - 
     - 
   * - 
     - ``PRUNING_VORONOI_PAIRS``
     - *all*
     - limit Voronoi pairs taken into account for pruning
     - 
     - ✔
     - 
     - 
     - 
   * - pruning
     - ``PRUNING_INTEGRAND``
     - *PW91MOL*
     - model functional used for angular pruning
     - 
     - ✔
     - 
     - 
     - 
   * - 
     - ''FACNEIGH
     - FAC_NEIGHBOUR
     - FAC_NEIGHBOR''
     - 4.0
     - scaling factor for the selection of neighbour atoms for the calculation of the test density
     - ✔
     - ✔
     - 
   * - 
     - ``FROM_MIN_ORDER``
     - *true*
     - order of pruning (starting from lowest or highest value of :math:`L`)
     - 
     - ✔
     - 
     - 
     - 
   * - 
     - ``PRUNEMETH``
     - 1
     - pruning method
     - ✔
     - 
     - 
     - 
     - 
   * - 
     - ``PRUNEFUNC``
     - 0
     - pruning function
     - ✔
     - 
     - 
     - 
     - 
   * - 
     - ``SMOOTHL``
     - 0
     - smooth :math:`L(r)` profile obtained after grid pruning
     - ✔
     - 
     - 
     - 
     - 
   * - fixed standard grids
     - ``NEESE_INDEX``
     - 4
     - index for Neese type grid
     - 
     - ✔
     - 
     - 
     - 
   * - 
     - ``NEESE_MAX_ORDER``
     - 29
     - maximum order for NEESE type grid when ``NEESE_INDEX`` < 3
     - 
     - ✔
     - 
     - 
     - 
   * - 
     - ``NEESE_INT_ACC``
     - 4.67
     - Neese parameter for number of radial points for Neese type grid when ``NEESE_INDEX`` < 3
     - 
     - ✔
     - 
     - 
     - 
   * - other
     - ''WEIGHT_CUT
     - WCUT''
     - 1d-20
     - threshold value to discard grid points with small integration weights
     - ✔
     - ✔
     - 
     - 
   * - 
     - ``ORIENT``
     - 2
     - orientation of atomic grids
     - ✔
     - 
     - 
     - 
     - 

.. list-table::
   :header-rows: 2

   * - Directives for GRID
     - 
     - 
     - 
     - 
     - 
   * - group
     - name
     - default values
     - description
     - ``dftgrid.png?nolink&50``
     - ``xcgrid.png?nolink&50``
   * - radial integration grid
     - ``RADIAL``
     - *log*,3,1.0,20,25,25,30
     - method and parameters for radial grid
     - ✔
     - ✔
   * - angular integration grid
     - ``ANGULAR``
     - *lebedev*,0.0,0.0
     - method and parameters for angular grid
     - ✔
     - ✔
   * - 
     - ``LMIN``
     - 0,0,0,0
     - minimum angular order for H,He, 2nd row, 3rd row, other elements
     - ✔
     - ✔
   * - 
     - ``LMAX``
     - 59,59,59,59
     - maximum angular order for H,He, 2nd row, 3rd row, other elements
     - ✔
     - ✔
   * - atom partitioning
     - ``VORONOI``
     - *murray*,10,2
     - step function method, :math:`m_\mu` recursion value and type of weights
     - ✔
     - ✔
   * - other
     - ``GRIDSAVE``
     - ✘
     - enable grid caching
     - ✔
     - ✔
   * - 
     - ``NOGRIDSAVE``
     - ✘
     - disable grid caching
     - ✔
     - ✔
   * - 
     - ``GRIDSYM``
     - ✘
     - force use of any point-group symmetry
     - ✔
     - 
   * - 
     - ``NOGRIDSYM``
     - ✘
     - disable use of any point-group symmetry
     - ✔
     - 
   * - 
     - ``GRIDPRINT``
     - *grid*\ =0
     - print grid points at different printing levels
     - ✔
     - ✔
   * - 
     - ``PRINTL``
     - 0
     - print angular grid orders for each radial grid point
     - ✔
     - ✔

.. _the_density_functional_program--target-quadrature-accuracy-gridthr:

Target quadrature accuracy (GRIDTHR)
====================================

``GRIDTHR|THRESHOLD_OVERALL|GRID|THRGRID=acc``

``GRIDTHR_RAD|THRESHOLD_RADIAL|ACCR=accr``

``GRIDTHR_ANG|THRESHOLD_ANGULAR|ACCA=acca``

Specify the target accuracy of integration. If options ``GRIDTHR_RAD`` and ``GRIDTHR_ANG`` are missing, radial and angular grids are generated adaptively, with the aim of integrating a model functional to the specified accuracy. *acc* is an overall target accuracy, and is the one that should normally be used; radial and angular grid target accuracies are generated algorithmically from it, namely, the scaled values *accr*\ =\ *acc*/2 and *acca*\ =\ *acc*/10 will then be used. However, they can be adjusted individually by using the options ``GRIDTHR_RAD`` and ``GRIDTHR_ANG`` respectively.

.. _the_density_functional_program--setting-a-global-level-for-the-accuracy-of-the-grid-gridacc:

Setting a global level for the accuracy of the grid (GRIDACC)
=============================================================

``GRIDACC|MODE=[old,default,low,high,veryhigh]``

The accuracy of the numerical quadrature depends on a number of different parameters whose effect may not be very transparent for the user. However, a fine-tuning of the grid parameters in order to control the accuracy of the grid is not necessary when using the global option ``GRIDACC`` that can have the four values *default*,\ *low*,\ *high* and *veryhigh*. ``GRIDACC``\ =\ *default* uses sensible settings for the grid parameters that should suffice for most kinds of calculations and is set by default. In contrast, ``GRIDACC``\ =\ *low* may be used when the accuracy of the DFT integration is not so relevant (e.g., for computing starting guesses) and ``GRIDACC``\ =\ *high* or ``GRIDACC``\ =\ *veryhigh* are recommended for benchmark calculations. The setting of ``GRIDACC``\ =\ *old* is for keeping backwards compatibility with older versions of Molpro (< 2021.x) where the default values for the grid parameters differed from the current ones.

.. _the_density_functional_program--radial-integration-grid-radial:

Radial integration grid (RADIAL)
================================

``RADIAL,method,accr,$m_r$,scale,$n_0,n_1,n_2,n_3$``

``RADIAL_SCHEME=method``

``THRESHOLD_RADIAL|GRIDTHR_RAD|ACCR=accr``

``RADIAL_SCALING``\ =[*atom1*,\ *atom2*,...] ``dftgrid.png?nolink&50``

``MIN_NR,$n_0,n_1,n_2,n_3$``

``MAX_NR,$n_0,n_1,n_2,n_3$``

Specify the details of the radial quadrature scheme. A number of different radial schemes are available, specified by *method* = ``EM``, ``BECKE``, ``AHLRICHS``, ``MULTIEXP``, ``DE2``, ``MK2CG`` or ``LOG``, with the latter being the default.

``EM|EULER-MACLAURIN`` is the Euler-Maclaurin scheme defined by C. W. Murray, N. C. Handy and G. J. Laming, `Mol. Phys. <https://dx.doi.org/10.1080/00268979300100651>`__ **78**, 997 (1993). :math:`m_r`, for which the default value is 2, is defined in equation (6) of the above as

.. math::

   r = \alpha {x^{m_r}\over (1-x)^{m_r}}

whilst *scale* (default value 1) multiplied by the Bragg-Slater radius of the atom gives the scaling parameter :math:`\alpha`.

``LOG|MURA-KNOWLES`` is the scheme described by M. E. Mura and P. J. Knowles, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.471749>`__ **104**, 9848 (1996). It is based on the transformation

.. math::

   r = - \alpha \log_e (1-x^{m_r})\; ,

with :math:`0\le x \le 1` and simple Gauss quadrature in :math:`x`-space. The recommended value of :math:`m_r` is 3 for molecular systems, giving rise to the Log3 grid; :math:`m_r`\ =4 is more efficient for atoms. :math:`\alpha` is taken to be *scale* times the recommended value for :math:`\alpha` given by Mura and Knowles, and *scale* defaults to 1.

``BECKE`` ``dftgrid.png?nolink&50`` is as defined by A. D. Becke, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.454033>`__ **88**, 2547 (1988). It is based on the transformation

.. math::

   r = \alpha {(1+x)\over (1-x)} \; ,
   \label{eqn:Becke}

using points in :math:`-1\le x \le +1` and standard Gauss-Chebyshev quadrature of the second kind for the :math:`x`-space quadrature. Becke chose his scaling parameters to be half the Bragg-Slater radius except for hydrogen, for which the whole Bragg-Slater radius was used, and setting *scale* to a value other than 1 allows a different :math:`\alpha` to be used. :math:`m_r` is not necessary for this radial scheme.

``AHLRICHS`` is the radial scheme defined by O. Treutler and R. Ahlrichs, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.469408>`__ **102**, 346 (1995). It is based on the transformation (their M4 mapping)

.. math::

   r= {\alpha \over \log_e 2} (1+x)^{0.6} \log_e\left( {2\over 1-x}\right)\; ,

with using standard Gauss-Chebyshev quadrature of the second kind for the :math:`x`-space integration. :math:`m_r` is not necessary for this radial scheme.

``CHEBY`` ``dftgrid.png?nolink&50`` 2nd kind Chebyshev quadrature

``MULTIEXP`` ``xcgrid.png?nolink&50``   `J. Comput. Chem. <https://doi.org/10.1007/s00214-011-0985-x>`__ **24**, 732 (2003)

``MK2GC`` ``xcgrid.png?nolink&50`` Gauss-Chebyshev quadrature with abscissas

.. math::

   x_i = \cos\left(i \pi \over n+1 \right)

``DE2|DOUBLEXP`` ``xcgrid.png?nolink&50`` Double Exponential quadrature of Mitani *et al.* `Theor. Chem. Acc. <https://dx.doi.org/10.1063/1.454033>`__ **130**, 645 (2011),  `Theor. Chem. Acc. <https://dx.doi.org/10.1007/s00214-012-1169-z>`__ **131**, 1169 (2012) based on the transformation

.. math::

   r=\exp(\alpha x_i-e^{-x_i})

:math:`n_0`, :math:`n_1`, :math:`n_2`, :math:`n_3` are the degrees of quadrature :math:`n_r` (see equation (3) of Murray et al.), for hydrogen/helium, first row, second row, and other elements respectively.

``accr`` specifies a target accuracy; the number of radial points is chosen according to a model, instead of using an explicit :math:`n_i`. The stricter of :math:`n_i`, ``accr`` is used, unless either is zero, in which case it is ignored. Molpro will then set ``accr``\ =\ ``acc``/2d0 where ``acc`` is the global threshold for the grid accuracy that can be set with the option ``GRIDTHR``.

An atom dependent radial scaling factor can be set with the option ``RADIAL_SCALING``, e.g. ``RADIAL_SCALING``\ =[1.0,1.1,1.1] could be a possible modification of the radial grids for H\ :math:`_2`\ O ``xcgrid.png?nolink&50``. Note that factors for all atoms must be given, otherwise the option will be ignored. The option can also be used to modify the scalar *scale* factor for ``dftgrid.png?nolink&50`` in which case only a single value needs to be given that will then be used to scale the radial grids for all atoms.

The size of the radial grid is evaluated from the ``GRIDTHR_RAD`` option:
.. math::

   n_{\text{rad}}(A) = -\log_{10} accr - 30 + (n_A - 1) * 15

where :math:`accr` is the threshold and :math:`n_A` is the period of atom.

The minimum and maximum values of the number of radial points is also restricted by ``xcgrid.png?nolink&50``:

``GRID,name=PRUNED,min_nr=[Row1,Row2,Row3,Row4+]``

and

``GRID,name=PRUNED,max_nr=[Row1,Row2,Row3,Row4+]``

for each atom based on its periodic row.

.. _the_density_functional_program--angular-integration-grid-angular:

Angular integration grid (ANGULAR)
==================================

``ANGULAR,method,acca,crowd\\``
``LMIN,$l^{\text{min}}_0,l^{\text{min}}_1,l^{\text{min}}_2,l^{\text{min}}_3$\\``
``LMAX,$l^{\text{max}}_0,l^{\text{max}}_1,l^{\text{max}}_2,l^{\text{max}}_3$\\``
``MIN_L``\ =[Row1,Row2,Row3,Row4+] ``xcgrid.png?nolink&50``
``MAX_L``\ =[Row1,Row2,Row3,Row4+] ``xcgrid.png?nolink&50``
``ANGULAR_SCHEME=lebedev|legendre|lobatto\\``
``ANGLEVEL``\ =\ *1*-*8* ``dftgrid.png?nolink&50``
``THRESHOLD_ANGULAR|GRIDTHR_ANG|ACCA=acca``

Specify the details of the angular quadrature scheme. The default choice for *method* is ``LEBEDEV`` (ie. as in A. D. Becke, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.454033>`__ **88**, 2547 (1988)) which provides angular grids of octahedral symmetry. An alternative choice for *method* is ``LEGENDRE``  ``dftgrid.png?nolink&50`` which gives Gauss-Legendre quadrature in :math:`\theta` and simple quadrature in :math:`\phi`, as defined by C. W. Murray, N. C. Handy and G. J. Laming, `Mol. Phys. <https://dx.doi.org/10.1080/00268979300100651>`__ **78**, 997 (1993). Similarly, *method*\ =\ ``LOBATTO``\ ``dftgrid.png?nolink&50`` defines a spherical quadrature over :math:`\theta` and :math:`\phi` space using Lobatto's formula and using the size reduction described by Treutler and Ahlrichs `J. Chem. Phys. <https://dx.doi.org/10.1063/1.469408>`__ **102**, 346 (1995). Both, *method*\ =\ ``LEGENDRE`` and ``LOBATTO`` are suitable options if highly accurate angular integrations need to be performed.

Each type of grid specifies a family of which the various members are characterized by a single quantum number :math:`l`; spherical harmonics up to degree :math:`l` are integrated exactly. :math:`l^{\text{min}}_i` and :math:`l^{\text{max}}_i, i=0,1,2,3` specify allowed ranges of :math:`l` for H–Be, B–Ca, Sc–Ba, and La– respectively. The :math:`l^{\text{min}}_i` are further moderated at run time so that for any given atom they are not less than :math:`2i+4` or twice the maximum angular momentum of the basis set on the atom; this constraint can be overridden by giving a negative value in ``LMIN``, and in this case just its absolute value will be used as the lower bound. For the Lebedev grids, if the value of :math:`l` is not one of the set implemented in Molpro (3, 5, 7, 9, 11, 13, 15, 17, 19, 23, 29, 41, 47, 53), then :math:`l` is increased to give the next largest angular grid available. In general, different radial points will have different :math:`l`, and in the absence of any moderation described below, will be taken from :math:`l^{\text{max}}_i`.

``xcgrid.png?nolink&50``\ The maximum allowed angular order is set by the row in the periodic table: ``GRID,name=PRUNED,max_l=[Row1,Row2,Row3,Row4+]``. The default value is [53,53,53,53]. Additionally, the minimum angular order can be set: ``GRID,name=PRUNED,min_l=[Row1,Row2,Row3,Row4+]``. The default value is [3,3,3,3]. This minimum is also modified to be at least :math:`2*l+1` where :math:`l` is the maximum angular momentum of the basis set.

*crowd* is a parameter to control the reduction of the degree of quadrature close to the nucleus, where points would otherwise be unnecessarily close together; larger values of crowd mean less reduction thus larger grids. A very large value of this parameter, or, conventionally, setting it to zero, will switch off this feature. The exact formula used for capping the :math:`L_\mathrm{max}` value at a radial point :math:`r_i` for an atom with a Bragg radius of :math:`R^\mathrm{Bragg}` is :math:`L_\mathrm{max}=min(L_\mathrm{max},max(L_\mathrm{min},min((crowd*r_i/R^\mathrm{Bragg})*(L_\mathrm{max}+1),10^6)-1))`. ``dftgrid.png?nolink&50``

*acca* is a target energy accuracy. It is used to reduce :math:`l` for a given radial point as far as possible below :math:`l^{\text{max}}_i` but not lower than :math:`l^{\text{max}}_i`. The implementation uses the error in the angular integral of the kernel of a model functional using a sum of approximate atomic densities. If *acca* is zero, the global threshold is used instead, or else it is ignored.

``ANGLEVEL`` ``dftgrid.png?nolink&50`` is an option that defines a fixed Lebedev order for three different radial zones defined by the ranges [1...\ *N*\ :math:`_{rad}`/3], [*N*\ :math:`_{rad}`/3+1...\ *N*\ :math:`_{rad}`/2] and [*N*\ :math:`_{rad}`/2+1...\ *N*\ :math:`_{rad}`] with *N*\ :math:`_{rad}` being the number of radial quadrature points and the order is from close to nucleus to far distant radial points. The idea of this definition is that only low Lebedev orders are needed in the first and second zone while higher orders are required in the outer third zone in order to achieve reasonable accuracies for the integration. It is possible to choose between seven different schemes ``ANGLEVEL``\ =1 to ``ANGLEVEL``\ =7 where the grid sizes increases in that order. Fairly accurate results should be accessible with intermediate levels ``ANGLEVEL``\ =3,4. It is also possible to select ``ANGLEVEL``\ =8 in which case the :math:`L=59` (1202-point) Lebedev grid is used at each radial point for highly accurate integrations.

.. _the_density_functional_program--pruning-integrand-and-neighbour-atoms-in-grid-generation-facneigh:

Pruning integrand and neighbour atoms in grid generation (FACNEIGH)
===================================================================

``PRUNING_INTEGRAND``\ =\ *SAD*,\ *PW91*,\ *PW91MOL* ``xcgrid.png?nolink&50``

``FROM_MIN_ORDER=0,1``

``FACNEIGH|FAC_NEIGHBOUR|FAC_NEIGHBOR=facn``

The grid generation for the angular grid depends on the integration of a test density functional around a sphere around each atom at a given radial point.
The procedure is that first a target value for the highest possible Lebedev order :math:`L` is computed and then that starting from the lowest value of :math:`L` (up-pruning) the integral is computed again until the deviation to the target value gets smaller than the threshold specified by the value for ``GRIDTHR_ANG``\ =acca, see also section `Angular integration grid <the_density_functional_program.html#angular-integration-grid-angular>`__. It is also possible to start from the largest possible value of :math:`L` by setting ``FROM_MIN_ORDER``\ =0 ``xcgrid.png?nolink&50`` (down-pruning) and so the optimal value of :math:`L` will then be found by seeking for the first one where the angular threshold is no longer obeyed. This option is expected to be more accurate but can also lead to larger grid sizes than the default option of ``FROM_MIN_ORDER``\ =1.

One can choose between the three different integrands ``PRUNING_INTEGRAND``\ =\ *SAD*,\ *PW91*,\ *PW91MOL* ``xcgrid.png?nolink&50``. *SAD* just defines a superposition of Slater atomic densities, *PW91* is a pseudo-density functional based on the PW91 xc functional and *PW91MOL* is a refinement of *PW91* where the procedure to find the optimal value of :math:`L` is slightly different (e.g., a linear regression is performed in order to determine :math:`L` with this integrand). Note that *PW91MOL* is set by default and is available both with ``dftgrid.png?nolink&50`` and  ``xcgrid.png?nolink&50``. In contrast, integrands *SAD* and *PW91* can only be used with ``xcgrid.png?nolink&50``.

The test functional is computed from the superposition of (Slater) atomic densities including the atom itself, plus a set of neighbour atoms. The latter includes all atoms that are within a range of ``DIST``\*\ ``FACNEIGH`` apart from the atom with ``DIST`` being the (squared!) distance of the closest atom. ``FACNEIGH`` is currently set to 4.0 by default and governs the shape of the test density on the sphere. Increasing this value will implicitly lead to more angular points at (particularly) large radial grid points but also increases the overall accuracy of the quadrature. For benchmark calculations it can be therefore recommended to set ``FACNEIGH`` larger than the current threshold. Note that the same can also be achieved by reducing the value of the overall ``GRIDTHR`` threshold value, yet, it has been found that resetting ``FACNEIGH`` can be more effective for intermediate sized grids.

.. _the_density_functional_program--atom-partitioning-of-integration-grid-voronoi:

Atom partitioning of integration grid (VORONOI)
===============================================

``VORONOI,$m_\mu$,vortyp``

``VORONOI_SCHEME``\ =\ *murray*,\ *becke*,\ *stratmann* ``xcgrid.png?nolink&50``

``SIZEADJ=becke,treutler,none``

``BECKE_MMU=mmu``

``MURRAY_MMU=mmu``

``PRUNING_VORONOI_PAIRS=all,atom``

Controls Becke-Voronoi partitioning of space. By default, the algorithm of C. W. Murray, N. C. Handy and G. J. Laming, `Mol. Phys. <https://dx.doi.org/10.1080/00268979300100651>`__ **78**, 997 (1993) is used, with :math:`m_\mu` defined by equation (24). The default value is 10.
``vortyp`` defines the type of grid weights to be computed: 1: raw  weights,  2: full voronoi,  4: pair voronoi. The default is
``vortyp=2.``

``xcgrid.png?nolink&50`` It is possible to choose between the three different step functions ``VORONOI_SCHEME``\ =\ *murray*,\ *becke* and *stratmann*.
The Murray and Becke scheme employ a recursive formula that increases the steepness of the function. The recursion limit is
given by its *mmu* value. In case of *becke* the default value of :math:`m_\mu`\ =3 is being used. This can be modified from the default for each case using the options ``BECKE_MMU`` or ``MURRAY_MMU``.

For heteronuclear molecules Molpro uses Treutler and Ahlrichs atomic size adjustment for the smoothing function
`J. Chem. Phys. <https://doi.org/10.1063/1.469408>`__ **102**, 346 (1995) (Eq.(13)). Alternatively, the scheme by Becke
`J. Chem. Phys. <https://doi.org/10.1063/1.454033>`__ **88**, 2547 (1988).
can be used by setting ``SIZEADJ``\ =\ *becke*. Possible choices for ``SIZEADJ`` are *becke*, *treutler* and *none*\ ``dftgrid.png?nolink&50``, the latter meaning that no size adjustment is being used.

``xcgrid.png?nolink&50`` On-the-fly grid pruning can be expensive for large molecules because of the cubic scaling of Voronoi partitioning. Pruning is performed in under mpp parallelisation, with each process pruning each atom. If it is still too expensive, Voronoi partitioning can be limited for the pruning algorithm to quadratic scaling: ``GRID,name=PRUNED,pruning_voronoi_pairs=ATOM`` but can result in a less accurate grid.

.. _the_density_functional_program--discarding-grid-points-with-tiny-weights-weightcut:

Discarding grid points with tiny weights (WEIGHT_CUT)
=====================================================

``WEIGHT_CUT|WCUT=thr``

Grid points very close to the nucleus can have very small grid weights which can drop below machine precision (~10d-16) when the radial grid is very large. These can be discarded with the option ``WEIGHT_CUT``\ =\ *thr*, i.e., grid points with weights smaller than *thr* will then not be used in the numerical integration anymore. While this can make the integration a little bit more efficient, a truncation of the grid with this option can prevent to achieve high accuracies in the numerical integration below, e.g., micro-hartree accuracies for energies. Therefore by default ``WEIGHT_CUT`` is set to a very small number that is well below machine precision (``WEIGHT_CUT``\ =1d-20) so that effectively all grid points close to the nucleus are taken into account for the integration.

.. _the_density_functional_program--grid-symmetry-gridsym-nogridsym:

Grid symmetry (GRIDSYM,NOGRIDSYM)
=================================

``NOGRIDSYM``

switches off the use of symmetry in generating the integration grid, whereas

``GRIDSYM``

forces the use of any point-group symmetry.

.. _the_density_functional_program--grid-printing-gridprint:

Grid printing (GRIDPRINT)
=========================

``GRIDPRINT,key=value,$\dots$``

controls printing of the grid, which by default is not done. At present, the only possible value for *key* is ``GRID``, and *value* should be specified as an integer. ``GRID=0`` causes the total number of integration points to be evaluated and reported; ``GRID=1`` additionally shows the number of points on each atom; ``GRID=2`` causes the complete set of grid points and weights to be printed.

.. _the_density_functional_program--orientation-of-atomic-grids-orient:

Orientation of atomic grids (ORIENT)
====================================

The orientation of the atomic grids can be controlled with the option ``ORIENT`` that can take the values 0, 1 and 2. ``ORIENT``\ =0 means that the grids are not oriented with respect to the atomic coordinates. This, however, can lead to non-invariant KS energies with respect to rotations of the molecule which is particularly significant for small grids. The setting ``ORIENT``\ =1 uses the method of B. G. Johnson *et al.* `Chem. Phys. Lett. <https://doi.org/10.1016/0009-2614(94)00199-5>`__ **220**, 377 (1994) which constructs rotationally invariant DFT grids. The method of Johnson *et al.* uses, however, the whole molecule to determine the orientation on each atom which might not be ideal for very large molecules or molecular clusters in various applications (determination of conformer energy differences, potential energy surfaces, or geometry optimisations). This can be resolved by the setting ``ORIENT``\ =2 which emphasises the local environment in the orientation of the atomic grids. This is the current default in Molpro (version 2023.1 and higher).

.. _the_density_functional_program--adaptive-molpro-grid-amg:

= Adaptive Molpro Grid (AMG)
============================

By default Molpro generates a quadrature grid which prunes the angular grid using an adaptive scheme which takes the molecular environment into account. Several pruning methods and functions can be set. The pruning method used can be controlled via the option

``GRID,prunmeth=[1-5]`` ``dftgrid.png?nolink&50``

where ``prunmeth`` can be set to method identifiers in the range of 1 to 5 (default is: ``prunemeth=1``).

The pruning function :math:`\mathcal{S}` (a spherical integral at the given radial grid point) is computed for a model density using a superposition of Slater's densities for the current geometry for the maximum angular grid order set (:math:`L_\mathrm{max}=59`) and then the respective algorithms find the lowest possible value of :math:`L` (at each radial grid point) for which the difference :math:`\Delta \mathcal{S}(L)=|\mathcal{S}(L_\mathrm{max})-\mathcal{S}(L)|` is below a threshold given by the input parameter ``GRIDTHR``. The function :math:`\mathcal{S}` can be adjusted with

``GRID,prunefunc=[0-1]`` ``dftgrid.png?nolink&50``

with ``prunefunc=0`` being the default. The basic difference between ``prunefunc=0`` and ``prunefunc=1`` is that the former one only uses pair Voronoi weights (leading to potentially linear scaling for large molecules) while the latter is implemented with full Voronoi weights (cubic scaling of the adaptive grid generation). ``prunefunc=1`` sometimes yields more accurate results for small sized grids than ``prunefunc=0`` for GGA-type functionals.

A detailed description of the AMG method can be found in `J. Chem. Phys. <https://doi.org/10.1063/5.0119622>`__ **157**, 234106 (2022) which also compares the accuracy yielded by the AMG grids to a range of other fixed grid methods for thermochemical properties.

**Important note for calculations of open-shell atoms:**
The adaptive grid method can not properly set the angular grids for open-shell atoms, because the pruning function is spherically symmetric and so very small angular grids are assigned for each radial grid point. This, however, is not sufficient for describing the spin orbitals properly on the grid. Therefore it is necessary to explicitly change the grid settings for such cases in the input file, using either

.. code-block:: text

    {grid,...; lmin,31,31,31,31}

which raises the lowest possible angular momenta to :math:`L=31` (which seems sufficient for, e.g., triplet carbon) or by using a fixed grid, e.g.:

.. code-block:: text

    {grid,...,anglevel=4}

with ``anglevel=4`` using a medium sized grid, see section `Angular integration grid <the_density_functional_program.html#angular-integration-grid-angular>`__ for details.

.. _the_density_functional_program--fixed-standard-grids:

Fixed standard grids
--------------------

``xcgrid.png?nolink&50`` There are three alternative types of pruned grids that can be used; ``PRUNED``, ``NEESE`` and ``SG``. They can be selected by setting the ``name`` option:

``GRID,name=PRUNED``

or

``GRID,name=NEESE``

or

``GRID,name=SGx``

with ``SGx``\ =\ ``SG0``,\ ``SG1``,\ ``SG2`` or ``SG3``.

``NEESE`` and ``SG`` are fixed-pruned grids and are defined in sections `NEESE Grids (GRID,NAME=NEESE) <the_density_functional_program.html#neese-grids-grid-name-neese>`__ and `SG Grids (GRID,name=SG) <the_density_functional_program.html#sg-grids-grid-name-sg>`__ respectively. ``PRUNED`` grids compute angular order pruning on-the-fly based on the molecular geometry. The ``PRUNED`` grid also features the most diverse set of options that can be tuned to balance accuracy and grid size, see sections `Radial integration grid <the_density_functional_program.html#radial-integration-grid-radial>`__, `Angular integration grid <the_density_functional_program.html#angular-integration-grid-angular>`__ and `Atom partitioning of integration grid <the_density_functional_program.html#atom-partitioning-of-integration-grid-voronoi>`__.

.. _the_density_functional_program--neese-grids-grid-name-neese:

Neese Grids (GRID,name=NEESE)
=============================

``xcgrid.png?nolink&50`` The NEESE grid is a fixed-pruned grid.

The size of the grid should set using the ``neese_index``:

``grid,name=NEESE,neese_index=value``

which links the angular size using ``neese_max_order`` and radial size using ``neese_int_acc``, which are defined below. The ``value`` can be set from 3 to 12. Using ``neese_index=3`` sets ``neese_int_acc=4.34`` and ``neese_max_order=23``. Increasing the index by 1 increases ``neese_int_acc`` by 0.33 (effectively 5 radial points) and ``neese_max_order`` by 6.

The grid is defined with 5 shells with boundaries at fixed radii. The angular order of each shell is defined relative to a maximum order, :math:`m`, as :math:`m-18, m-12, m-6, m, m-6`. It can be set using:

``grid,name=NEESE,neese_max_order=value``

Ahlrichs quadrature is used for the radial grid. The number of points used for atom :math:`A` is defined by the Krack-Köster formula [1]:

.. math::

   n_{\text{rad}}(A) = -5 (3 \log 10^{-\tt{int\_acc}} - n_A + 8 )

where :math:`n_A` is the period of atom :math:`A`. ``int_acc`` is set using:

``grid,name=NEESE,neese_int_acc=value``

where ``value`` would take values from 4.34 upwards.

References:
:math:`[1]` Krack, M., Köster, A.M., 1998. An adaptive numerical integrator for molecular integrals. `J. Chem. Phys. <https://dx.doi.org/10.1063/1.475719>`__ **108**, 3226-3234. https://doi.org/10.1063/1.475719

.. _the_density_functional_program--sg-grids-grid-name-sg:

SG Grids (GRID,name=SG)
=======================

``xcgrid.png?nolink&50`` The fixed-pruned Standard Grid (SG) can be used:

``GRID,name=SG0\\``
``GRID,name=SG1\\``
``GRID,name=SG2\\``
or
``GRID,name=SG3\\``

``SG0`` is a small fixed-pruned grid by Chien and Gill[1]. It is defined for atoms in the first three rows except He, Ne and Ar. Less than 1500 points is produced per atom. The MultiExp radial grid and Becke’s Voronoi partitioning step function are used. The 18 point Lebedev angular grids are replaced with 14 point ones.

``SG2`` and ``SG3`` are larger fixed grids by Dasgupta and Herbert [3] that were developed to achieve high accuracies for chemical properties. They are based on the ``DE2`` (DoubleExp) radial quadrature scheme, see section `Radial integration grid <the_density_functional_program.html#radial-integration-grid-radial>`__.

References:
:math:`[1]` Chien, S.-H., Gill, P.M.W., 2006. SG-0: A small standard grid for DFT quadrature on large systems. `J. Comput. Chem. <https://dx.doi.org/10.1002/jcc.20383>`__ **27**, 730-739. https://doi.org/10.1002/jcc.20383 :math:`[2]` Gill, P.M.W., Johnson, B.G., Pople, J.A., 1993. A standard grid for density functional calculations. Chem. Phys. Let. 209, 506-512. https://doi.org/10.1016/0009-2614(93)80125-9
:math:`[3]` Dasgupta, S. Herbert, J. M., 2017. Standard Grids for High-Precision Integration of Modern Density Functionals: SG-2 and SG-3. `J. Comput. Chem. <https://dx.doi.org/10.1002/jcc.24761>`__ **38**, 869–882. https://doi.org/10.1002/jcc.24761

.. _the_density_functional_program--density-functionals:

Density Functionals
-------------------

Widely used functional combinations can be specified via convenient keywords. These can be entered, for example via ``{df-rks,pbe}`` (do a single KS calculation with PBE) or ``{dfunc,pbe}`` (which will instruct all following KS calculations to use PBE by default). The following table lists the defined alias density functional combinations:

.. list-table::
   :header-rows: 1

   * - alias
     - 
     - 
     - Ref
   * - ``B``
     - ``B88``\ dftfun:B88
     - 1
     - `10.1103/PhysRevA.38.3098 <https://dx.doi.org/10.1103/PhysRevA.38.3098>`__
   * - ``B-LYP``
     - ``B88``\ dftfun:B88:``LYP``\ dftfun:LYP
     - 1:1
     - 
   * - ``BLYP``
     - ``B88``\ dftfun:B88:``LYP``\ dftfun:LYP
     - 1:1
     - 
   * - ``B-P``
     - ``B88``\ dftfun:B88:``P86``\ dftfun:P86
     - 1:1
     - 
   * - ``BP86``
     - ``B88``\ dftfun:B88:``P86``\ dftfun:P86
     - 1:1
     - 
   * - ``B-VWN``
     - ``B88``\ dftfun:B88:``VWN5``\ dftfun:VWN5
     - 1:1
     - 
   * - ``B3LYP``
     - ``EXACT``\ dftfun:EXACT:``B88``\ dftfun:B88:``DIRAC``\ dftfun:DIRAC:``LYP``\ dftfun:LYP:``VWN5``\ dftfun:VWN5
     - 0.2:0.72:0.08:0.81:0.19
     - 
   * - ``B3LYP3``
     - ``EXACT``\ dftfun:EXACT:``B88``\ dftfun:B88:``DIRAC``\ dftfun:DIRAC:``LYP``\ dftfun:LYP:``VWN3``\ dftfun:VWN3
     - 0.2:0.72:0.08:0.81:0.19
     - 
   * - ``B3LYP5``
     - ``EXACT``\ dftfun:EXACT:``B88``\ dftfun:B88:``DIRAC``\ dftfun:DIRAC:``LYP``\ dftfun:LYP:``VWN5``\ dftfun:VWN5
     - 0.2:0.72:0.08:0.81:0.19
     - 
   * - ``B88X``
     - ``B88``\ dftfun:B88
     - 1
     - `10.1103/PhysRevA.38.3098 <https://dx.doi.org/10.1103/PhysRevA.38.3098>`__
   * - ``B97``
     - ``EXACT``\ dftfun:EXACT:``B97DF``\ dftfun:B97DF
     - 0.1943:1
     - 
   * - ``B97R``
     - ``EXACT``\ dftfun:EXACT:``B97RDF``\ dftfun:B97RDF
     - 0.21:1
     - 
   * - ``BECKE``
     - ``B88``\ dftfun:B88
     - 1
     - `10.1103/PhysRevA.38.3098 <https://dx.doi.org/10.1103/PhysRevA.38.3098>`__
   * - ``BH-LYP``
     - ``EXACT``\ dftfun:EXACT:``B88``\ dftfun:B88:``LYP``\ dftfun:LYP
     - 0.5:0.5:1
     - 
   * - ``CS``
     - ``CS1``\ dftfun:CS1
     - 1
     - 
   * - ``D``
     - ``DIRAC``\ dftfun:DIRAC
     - 1
     - 
   * - ``HFB``
     - ``B88``\ dftfun:B88
     - 1
     - `10.1103/PhysRevA.38.3098 <https://dx.doi.org/10.1103/PhysRevA.38.3098>`__
   * - ``HFS``
     - ``DIRAC``\ dftfun:DIRAC
     - 1
     - 
   * - ``LDA``
     - ``DIRAC``\ dftfun:DIRAC:``VWN5``\ dftfun:VWN5
     - 1:1
     - 
   * - ``LSDAC``
     - ``PW92C``\ dftfun:PW92C
     - 1
     - `10.1103/PhysRevB.45.13244 <https://dx.doi.org/10.1103/PhysRevB.45.13244>`__
   * - ``LSDC``
     - ``PW92C``\ dftfun:PW92C
     - 1
     - `10.1103/PhysRevB.45.13244 <https://dx.doi.org/10.1103/PhysRevB.45.13244>`__
   * - ``LYP88``
     - ``LYP``\ dftfun:LYP
     - 1
     - 
   * - ``MM05``
     - ``EXACT``\ dftfun:EXACT:``M05X``\ dftfun:M05X:``M05C``\ dftfun:M05C
     - 0.28:0.72:1
     - `10.1063/1.2126975 <https://dx.doi.org/10.1063/1.2126975>`__
   * - ``MM05-2X``
     - ``EXACT``\ dftfun:EXACT:``M052XX``\ dftfun:M052XX:``M052XC``\ dftfun:M052XC
     - 0.56:0.44:1
     - `10.1021/ct0502763 <https://dx.doi.org/10.1021/ct0502763>`__
   * - ``MM06``
     - ``EXACT``\ dftfun:EXACT:``M06X``\ dftfun:M06X:``M06C``\ dftfun:M06C
     - 0.27:0.73:1
     - `10.1007/s00214-007-0310-x <https://dx.doi.org/10.1007/s00214-007-0310-x>`__
   * - ``MM06-2X``
     - ``EXACT``\ dftfun:EXACT:``M062XX``\ dftfun:M062XX:``M062XC``\ dftfun:M062XC
     - 0.54:0.46:1
     - `10.1007/s00214-007-0310-x <https://dx.doi.org/10.1007/s00214-007-0310-x>`__
   * - ``MM06-L``
     - ``M06LX``\ dftfun:M06LX:``M06LC``\ dftfun:M06LC
     - 1:1
     - `10.1063/1.2370993 <https://dx.doi.org/10.1063/1.2370993>`__
   * - ``MM06-HF``
     - ``EXACT``\ dftfun:EXACT:``M06HFX``\ dftfun:M06HFX:``M06HFC``\ dftfun:M06HFC
     - 1:1:1
     - `10.1021/jp066479k <https://dx.doi.org/10.1021/jp066479k>`__
   * - ``PBE``
     - ``PBEX``\ dftfun:PBEX:``PBEC``\ dftfun:PBEC
     - 1:1
     - `10.1103/PhysRevLett.77.3865 <https://dx.doi.org/10.1103/PhysRevLett.77.3865>`__
   * - ``PBE0``
     - ``EXACT``\ dftfun:EXACT:``PBEX``\ dftfun:PBEX:``PBEC``\ dftfun:PBEC
     - 0.25:0.75:1
     - `10.1063/1.478522 <https://dx.doi.org/10.1063/1.478522>`__
   * - ``PBE0MOL``
     - ``EXACT``\ dftfun:EXACT:``PBEX``\ dftfun:PBEX:``PW91C``\ dftfun:PW91C
     - 0.25:0.75:1
     - 
   * - ``PBEREV``
     - ``PBEXREV``\ dftfun:PBEXREV:``PBEC``\ dftfun:PBEC
     - 1:1
     - 
   * - ``PW91``
     - ``PW91X``\ dftfun:PW91X:``PW91C``\ dftfun:PW91C
     - 1:1
     - `10.1103/PhysRevB.46.6671 <https://dx.doi.org/10.1103/PhysRevB.46.6671>`__
   * - ``S``
     - ``DIRAC``\ dftfun:DIRAC
     - 1
     - 
   * - ``S-VWN``
     - ``DIRAC``\ dftfun:DIRAC:``VWN5``\ dftfun:VWN5
     - 1:1
     - 
   * - ``SLATER``
     - ``DIRAC``\ dftfun:DIRAC
     - 1
     - 
   * - ``VS99``
     - ``VSXC``\ dftfun:VSXC
     - 1
     - 
   * - ``VWN``
     - ``VWN5``\ dftfun:VWN5
     - 1
     - 
   * - ``VWN80``
     - ``VWN5``\ dftfun:VWN5
     - 1
     - 
   * - ``M05``
     - ``EXACT``\ dftfun:EXACT:``XC-M05``\ dftfun:XC-M05
     - 0.28:1
     - `10.1063/1.2126975 <https://dx.doi.org/10.1063/1.2126975>`__
   * - ``M05-2X``
     - ``EXACT``\ dftfun:EXACT:``XC-M05-2X``\ dftfun:XC-M05-2X
     - 0.56:1
     - `10.1021/ct0502763 <https://dx.doi.org/10.1021/ct0502763>`__
   * - ``M06``
     - ``EXACT``\ dftfun:EXACT:``XC-M06``\ dftfun:XC-M06
     - 0.27:1
     - `10.1007/s00214-007-0310-x <https://dx.doi.org/10.1007/s00214-007-0310-x>`__
   * - ``M06-2X``
     - ``EXACT``\ dftfun:EXACT:``XC-M06-2X``\ dftfun:XC-M06-2X
     - 0.54:1
     - `10.1007/s00214-007-0310-x <https://dx.doi.org/10.1007/s00214-007-0310-x>`__
   * - ``M06-L``
     - ``XC-M06-L``\ dftfun:XC-M06-L
     - 1
     - `10.1063/1.2370993 <https://dx.doi.org/10.1063/1.2370993>`__
   * - ``M06-HF``
     - ``EXACT``\ dftfun:EXACT:``XC-M06-HF``\ dftfun:XC-M06-HF
     - 1:1
     - `10.1021/jp066479k <https://dx.doi.org/10.1021/jp066479k>`__
   * - ``M08-HX``
     - ``EXACT``\ dftfun:EXACT:``XC-M08-HX``\ dftfun:XC-M08-HX
     - 0.5223:1
     - 
   * - ``M08-SO``
     - ``EXACT``\ dftfun:EXACT:``XC-M08-SO``\ dftfun:XC-M08-SO
     - 0.5679:1
     - 
   * - ``M11-L``
     - ``XC-M11-L``\ dftfun:XC-M11-L
     - 1
     - 
   * - ``TPSS``
     - ``TPSSX``\ dftfun:TPSSX:``TPSSC``\ dftfun:TPSSC
     - 1:1
     - `10.1103/PhysRevLett.91.146401 <https://dx.doi.org/10.1103/PhysRevLett.91.146401>`__
   * - ``TPSSH``
     - ``EXACT``\ dftfun:EXACT:``TPSSX``\ dftfun:TPSSX:``TPSSC``\ dftfun:TPSSC
     - 0.1:0.9:1
     - `10.1063/1.1626543 <https://dx.doi.org/10.1063/1.1626543>`__
   * - ``M12HFC``
     - ``EXACT``\ dftfun:EXACT:``M12C``\ dftfun:M12C
     - 1:1
     - `10.1063/1.4768228 <https://dx.doi.org/10.1063/1.4768228>`__
   * - ``HJSWPBE``
     - ``HJSWPBEX``\ dftfun:HJSWPBEX:``PBEC``\ dftfun:PBEC
     - 1:1
     - `10.1063/1.2921797 <https://dx.doi.org/10.1063/1.2921797>`__
   * - ``HJSWPBEH``
     - ``EXACT``\ dftfun:EXACT:``HJSWPBEX``\ dftfun:HJSWPBEX:``PBEC``\ dftfun:PBEC
     - 0.2:0.8:1
     - `10.1063/1.3073302 <https://dx.doi.org/10.1063/1.3073302>`__
   * - ``TCSWPBE``
     - ``EXERFPBE``\ dftfun:EXERFPBE:``ECERFPBE``\ dftfun:ECERFPBE
     - 1:1
     - `10.1063/1.1824896 <https://dx.doi.org/10.1063/1.1824896>`__
   * - ``PBESOL``
     - ``PBESOLX``\ dftfun:PBESOLX:``PBESOLC``\ dftfun:PBESOLC
     - 1:1
     - `10.1103/PhysRevLett.100.136406 <https://dx.doi.org/10.1103/PhysRevLett.100.136406>`__

.. _the_density_functional_program--technical-definitions-of-density-functional-inputs:

Technical definitions of density functional inputs
==================================================

In the following, :math:`\rho_\alpha` and :math:`\rho_\beta` are the :math:`\alpha` and :math:`\beta` spin densities; the total spin density is :math:`\rho`;

The gradients of the density enter through

.. math::

   \begin{aligned}
   \sigma_{\alpha\alpha} &=& \nabla\rho_\alpha \cdot \nabla\rho_\alpha \; ,
   \sigma_{\beta\beta} = \nabla\rho_\beta \cdot \nabla\rho_\beta\; ,
   \sigma _{\alpha\beta}= \nabla\rho_\alpha \cdot \nabla\rho_\beta \; , \nonumber
   \\
   \sigma &=& \sigma_{\alpha\alpha}+\sigma_{\beta\beta}+2\sigma _{\alpha\beta}.
   \\
   \chi_\alpha&=& \frac{\sqrt{\sigma_{\alpha\alpha}}}{\rho_\alpha^{4/3}}\;,
   \chi_\beta = \frac{\sqrt{\sigma_{\beta\beta}}}{\rho_\beta^{4/3}}\;.\\
   \upsilon_\alpha&=&\nabla^2\rho_\alpha \; ,
   \upsilon_\beta=\nabla^2\rho_\beta \; ,
   \upsilon=\upsilon_\alpha+\upsilon_\beta \;.\end{aligned}

Additionally, the kinetic energy density for a set of (Kohn-Sham) orbitals generating the density can be introduced through

.. math::

   \begin{aligned}
   \tau_\alpha&=&\sum_i^\alpha
   \left|{\bf\nabla}\phi_i\right|^2
   \; , \tau_\beta=\sum_i^\beta
   \left|{\bf\nabla}\phi_i\right|^2
   \;,
   \tau=\tau_\alpha+\tau_\beta \;.\end{aligned}

All of the available functionals are of the general form

.. math::

   \begin{aligned}
   F\left[\rho_s,\rho_{\bar{s}},
   \sigma_{ss},\sigma_{\bar{s}\bar{s}},\sigma_{s\bar{s}},
   \tau_s,\tau_{\bar{s}},
   \upsilon_s,\upsilon_{\bar{s}}
   \right] &=&
   \int d^3{\bf r}
   K\left(\rho_s,\rho_{\bar{s}},
   \sigma_{ss},\sigma_{\bar{s}\bar{s}},\sigma_{s\bar{s}},
   \tau_s,\tau_{\bar{s}},
   \upsilon_s,\upsilon_{\bar{s}}
   \right)\end{aligned}

where :math:`\bar{s}` is the conjugate spin to :math:`s`.

.. _the_density_functional_program--lists-of-component-density-functionals:

Lists of component density functionals
======================================

Below is a list of the primary correlation and exchange functionals supported by Molpro. These can be combined into total density functionals. For example, the following input will produce a B3LYP calculation:

``{dfunc,B88,DIRAC,LYP,VWN5,dftfac=[0.72,0.08,0.81,0.19],exfac=0.2}{df-rks}``

Note that many commonly used combinations of primary functionals are predefined as alias keywords (e.g., ``{df-rks,b3lyp}`` is an equivalent input. See above).

* ``B86`` Xalpha beta gamma. Divergence free semiempirical gradient-corrected exchange energy functional. :math:`\lambda=\gamma` in ref.

`doi:10.1063/1.450025 <http://dx.doi.org/10.1063/1.450025>`__

* ``B86MGC`` Xalpha beta gamma with Modified Gradient Correction. B86 with modified gradient correction for large density gradients.

`doi:10.1063/1.451353 <http://dx.doi.org/10.1063/1.451353>`__

* ``B86R`` Xalpha beta gamma Re-optimised. Re-optimised :math:`\beta` of B86 used in part 3 of Becke’s 1997 paper.

`doi:10.1063/1.475007 <http://dx.doi.org/10.1063/1.475007>`__

* ``B88`` Becke 1988 Exchange Functional

`doi:10.1103/PhysRevA.38.3098 <http://dx.doi.org/10.1103/PhysRevA.38.3098>`__

* ``B88C`` Becke 1988 Correlation Functional. Correlation functional depending on B86MGC exchange functional with empirical atomic parameters, :math:`t` and :math:`u`. The exchange functional that is used in conjunction with B88C should replace B88MGC here.

`doi:10.1063/1.454274 <http://dx.doi.org/10.1063/1.454274>`__

* ``B95`` Becke 1995 Correlation Functional. :math:`tau` dependent Dynamical correlation functional.

`doi:10.1063/1.470829 <http://dx.doi.org/10.1063/1.470829>`__

* ``B97DF`` Density functional part of B97. This functional needs to be mixed with 0.1943\*exact exchange.

`doi:10.1063/1.475007 <http://dx.doi.org/10.1063/1.475007>`__

* ``B97RDF`` Density functional part of B97 Re-parameterized by Hamprecht et al. Re-parameterization of the B97 functional in a self-consistent procedure by Hamprecht et al. This functional needs to be mixed with 0.21\*exact exchange.

`doi:10.1063/1.477267 <http://dx.doi.org/10.1063/1.477267>`__
\* ``BR`` Becke-Roussel Exchange Functional. A. D. Becke and M. R. Roussel,\ `Phys. Rev. A <https://dx.doi.org/10.1103/PhysRevA.39.3761>`__ **39**, 3761 (1989)

.. math::

   K=\frac{1}{2}\sum_s \rho_s U_s

where

.. math::

   U_s=-(1-e^{-x}-xe^{-x}/2)/b

.. math::

   b=\frac{x^3e^{-x}}{8\pi\rho_s}

and :math:`x` is defined by the nonlinear equation

.. math::

   \frac{xe^{-2x/3}}{x-2}=\frac{2\pi^{2/3}\rho_s^{5/3}}{3Q_s}

where

.. math::

   Q_s=(\upsilon_s-2\gamma D_s)/6

.. math::

   D_s=\tau_s-\frac{\sigma_{ss}}{4\rho_s}

and

.. math::

   \gamma=1.

* ``BRUEG`` Becke-Roussel Exchange Functional — Uniform Electron Gas Limit. A. D. Becke and M. R. Roussel,\ `Phys. Rev. A <https://dx.doi.org/10.1103/PhysRevA.39.3761>`__ **39**, 3761 (1989) As for ``BR`` but with :math:`{\gamma=0.8}`.
* ``BW`` Becke-Wigner Exchange-Correlation Functional. Hybrid exchange-correlation functional comprising Becke’s 1998 exchange and Wigner’s spin-polarised correlation functionals.

`doi:10.1039/FT9959104337 <http://dx.doi.org/10.1039/FT9959104337>`__

* ``CS1`` Colle-Salvetti correlation functional. R. Colle and O. Salvetti, Theor. Chim. Acta 37, 329 (1974); C. Lee, W. Yang and R. G. Parr, `Phys. Rev. B <https://dx.doi.org/10.1103/PhysRevB.37.785>`__ **37**, 785(1988) ``CS1`` is formally identical to ``CS2``, except for a reformulation in which the terms involving :math:`\upsilon` are eliminated by integration by parts. This makes the functional more economical to evaluate. In the limit of exact quadrature, ``CS1`` and ``CS2`` are identical, but small numerical differences appear with finite integration grids.

\* ``CS2`` Colle-Salvetti correlation functional. R. Colle and O. Salvetti, Theor. Chim. Acta 37, 329 (1974); C. Lee, W. Yang and R. G. Parr, `Phys. Rev. B <https://dx.doi.org/10.1103/PhysRevB.37.785>`__ **37**, 785(1988) ``CS2`` is defined through

.. math::

   \begin{aligned}
     K &=&
     -a \left({
     \rho+2b\rho^{-5/3}
     \left[
     \rho_\alpha t_{\alpha} + \rho_\beta t_{\beta}
     -\rho t_W
     \right]
     e^{-c\rho^{-1/3}}
     \over 1+d \rho^{-1/3}
     }\right)
     \end{aligned}

where

.. math::

   \begin{aligned}
     t_{\alpha} &=&\frac{\tau_\alpha}{2}-\frac{\upsilon_\alpha}{8}
     \\
     t_{\beta} &=&\frac{\tau_\beta}{2}-\frac{\upsilon_\beta}{8}
     \\
     t_{W} &=& {1\over 8} {\sigma \over \rho} - {1\over 2} \upsilon
     \end{aligned}

and the constants are :math:`a=0.04918, b=0.132, c=0.2533, d=0.349`.

* ``DIRAC`` Slater-Dirac Exchange Energy. Automatically generated Slater-Dirac exchange.

`doi:10.1103/PhysRev.81.385 <http://dx.doi.org/10.1103/PhysRev.81.385>`__

* ``ECERF`` Short-range LDA correlation functional. Local-density approximation of correlation energy

for short-range interelectronic interaction :math:`{\rm erf}(\mu r_{21})/r_{12}`,
S. Paziani, S. Moroni, P. Gori-Giorgi, and G. B. Bachelet, `Phys. Rev. B <https://dx.doi.org/10.1103/PhysRevB.73.155111>`__ **73**, 155111 (2006).

.. math::

   \begin{aligned}
   & &
   \epsilon_c^{\rm SR}(r_s,\zeta,\mu)  =  \epsilon_c^{\rm PW92}(r_s,\zeta)-
   \nonumber \\
   & & \frac{[\phi_2(\zeta)]^3Q\left(\frac{\mu\sqrt{r_s}}{\phi_2(\zeta)}\right)+a_1 \mu^3+a_2 \mu^4+
    a_3\mu^5+a_4\mu^6+a_5\mu^8}{(1+b_0^2\mu^2)^4},\end{aligned}

where

.. math::

   Q(x)=\frac{2\ln(2)-2}{\pi^2}\ln\left(\frac{1+a\,x+b\,x^2+c\,x^3}{1+a\,x+
   d\,x^2}\right),

with :math:`a=5.84605`, :math:`c=3.91744`, :math:`d=3.44851`, and :math:`b=d-3\pi\alpha/(4\ln(2)-4)`. The parameters :math:`a_i(r_s,\zeta)` are given by

.. math::

   \begin{aligned}
   a_1 & = & 4 \,b_0^6 \,C_3+b_0^8 \,C_5, \nonumber \\
   a_2 & = & 4 \,b_0^6 \,C_2+b_0^8\, C_4+6\, b_0^4 \epsilon_c^{\rm PW92}, \nonumber \\
   a_3 & = & b_0^8 \,C_3, \nonumber \\
   a_4 & = & b_0^8 \,C_2+4 \,b_0^6\, \epsilon_c^{\rm PW92} \nonumber, \\
   a_5 & = & b_0^8\,\epsilon_c^{\rm PW92}, \nonumber\end{aligned}

with

.. math::

   \begin{aligned}
   C_2 & = & -\frac{3(1\!-\!\zeta^2)\,g_c(0,r_s,\zeta\!=\!0)}{8\,r_s^3} \nonumber \\
   C_3 & = &  - (1\!-\!\zeta^2)\frac{g(0,r_s,\zeta\!=\!0)}{\sqrt{2\pi}\, r_s^3}
   \nonumber \\
   C_4 & = & -\frac{9\, c_4(r_s,\zeta)}{64 r_s^3} \nonumber \\
   C_5 & =  & -\frac{9\, c_5(r_s,\zeta)}{40\sqrt{2 \pi} r_s^3}\nonumber \\
   c_4(r_s,\zeta)
   & = & \left(\frac{1\!+\!\zeta}{2}\right)^2g''\left(0,
   r_s\left(\frac{2}{1\!+\!\zeta}\right)^{1/3}\!\!\!\!\!\!\!\!, \,\,\,\,\,\zeta\!=\!1\right)+ \left(\frac{1\!-\!\zeta}{2}\right)^2 \times \nonumber  \\ & & g''\left(0,
   r_s\left(\frac{2}{1\!-\!\zeta}\right)^{1/3}\!\!\!\!\!\!\!\!, \,\,\,\,\,\zeta\!=\!1\right)
   + (1\!-\!\zeta^2)D_2(r_s)-\frac{\phi_8(\zeta)}{5\,\alpha^2\,r_s^2}
   \nonumber \\
   c_5(r_s,\zeta)
   & = & \left(\frac{1\!+\!\zeta}{2}\right)^2g''\left(0,
   r_s\left(\frac{2}{1\!+\!\zeta}\right)^{1/3}\!\!\!\!\!\!\!\!, \,\,\,\,\,\zeta\!=\!1\right)+
     \left(\frac{1\!-\!\zeta}{2}\right)^2 \times \nonumber \\  & & g''\left(0,
   r_s\left(\frac{2}{1\!-\!\zeta}\right)^{1/3}\!\!\!\!\!\!\!\!, \,\,\,\,\,\zeta\!=\!1\right)+  (1\!-\!\zeta^2)D_3(r_s),\end{aligned}

and

.. math::

   \begin{aligned}
   \phantom{\bigl[} b_0(r_s)  =   0.784949\,r_s  \\
   \phantom{\Biggl[} g''(0,r_s,\zeta\!=\!1)  =   \frac{2^{5/3}}{5\,\alpha^2 \,r_s^2} \,
   \frac{1-0.02267 r_s}{\left(1+0.4319 r_s+0.04 r_s^2\right)} \\
   \phantom{\Biggl[}D_2(r_s)  =  \frac{e^{-  0.547 r_s}}{r_s^2}\left(-0.388 r_s+0.676 r_s^2\right) \\
   \phantom{\Biggl[}D_3(r_s)  =  \frac{e^{-0.31 r_s}}{r_s^3}\left(-4.95 r_s+ r_s^2\right).\end{aligned}

Finally, :math:`\epsilon_c^{\rm PW92}(r_s,\zeta)` is the Perdew-Wang parametrization of the correlation energy of the standard uniform electron gas [J.P. Perdew and Y. Wang, `Phys. Rev. B <https://dx.doi.org/10.1103/PhysRevB.45.13244>`__ **45**, 13244 (1992)], and

.. math::

   g(0,r_s,\zeta\!=\!0)=\frac{1}{2}(1-Br_s+Cr_s^2+Dr_s^3+Er_s^4)\,{\rm e}^{-dr_s},

is the on-top pair-distribution function of the standard jellium model [P. Gori-Giorgi and J.P. Perdew, `Phys. Rev. B <https://dx.doi.org/10.1103/PhysRevB.64.155102>`__ **64**, 155102 (2001)], where :math:`B=-0.0207`, :math:`C=0.08193`, :math:`D=-0.01277`, :math:`E=0.001859`, :math:`d=0.7524`. The correlation part of the on-top pair-distribution function is :math:`g_c(0,r_s,\zeta\!=\!0)=g(0,r_s,\zeta\!=\!0)-\frac{1}{2}`.

* ``ECERFPBE`` Range-Separated Correlation Functional. Toulouse-Colonna-Savin range-separated correlation functional based on PBE, see J. Toulouse et al., `J. Chem. Phys. <https://dx.doi.org/10.1063/1.1824896>`__ **122**, 014110 (2005).

`doi:10.1063/1.1824896 <http://dx.doi.org/10.1063/1.1824896>`__

* ``EXACT`` Exact Exchange Functional. Hartree-Fock exact exchange functional can be used to construct hybrid exchange-correlation functional.
* ``EXERF`` Short-range LDA correlation functional. Local-density approximation of exchange energy

for short-range interelectronic interaction :math:`{\rm erf}(\mu r_{12})/r_{12}`,
A. Savin, in Recent Developments and Applications of Modern Density Functional Theory, edited by J.M. Seminario (Elsevier, Amsterdam, 1996).

.. math::

   \begin{aligned}
   \epsilon_x^{\rm SR}(r_s,\zeta,\mu)  & = & \frac{3}{4\pi}\frac{\phi_4(\zeta)}{\alpha\,r_s}- \frac{1}{2}(1\!+\!\zeta)^{4/3}
   f_x\left(r_s,\mu(1\!+\!\zeta)^{-1/3}\right)+ \nonumber \\
   & & \frac{1}{2}(1\!-\!\zeta)^{4/3}
   f_x\left(r_s,\mu(1\!-\!\zeta)^{-1/3}\right)\end{aligned}

with

.. math::

   \phi_n(\zeta)=\frac{1}{2}\left[ (1\!+\!\zeta)^{n/3}+(1\!-\!\zeta)^{n/3} \right],

.. math::

   \begin{aligned}
   f_x(r_s,\mu)  & =  & -\frac{\mu}{\pi}\biggl[(2y-4y^3)\,e^{-1/4y^2}-
   3y+4y^3+ \sqrt{\pi}\,{\rm erf}\left(\frac{1}{2y}\right)\biggr], \nonumber \\
   \qquad y  & =  & \frac{\mu\,\alpha\,r_s}{2},\end{aligned}

and :math:`\alpha=(4/9\pi)^{1/3}`.

* ``EXERFPBE`` Range-Separated Exchange Functional. Toulouse-Colonna-Savin range-separated exchange functional based on PBE, see J. Toulouse et al., `J. Chem. Phys. <https://dx.doi.org/10.1063/1.1824896>`__ **122**, 014110 (2005).

`doi:10.1063/1.1824896 <http://dx.doi.org/10.1063/1.1824896>`__

* ``G96`` Gill’s 1996 Gradient Corrected Exchange Functional

`doi:G96 <http://dx.doi.org/G96>`__

* ``HCTH120`` Handy least squares fitted functional

`doi:10.1063/1.480732 <http://dx.doi.org/10.1063/1.480732>`__

* ``HCTH147`` Handy least squares fitted functional

`doi:10.1063/1.480732 <http://dx.doi.org/10.1063/1.480732>`__

* ``HCTH93`` Handy least squares fitted functional

`doi:10.1063/1.477267 <http://dx.doi.org/10.1063/1.477267>`__

* ``HJSWPBEX`` Meta GGA Correlation Functional. Henderson-Janesko-Scuseria range-separated exchange functional based on a model of an exchange hole derived by a constraint-satisfaction technique, see T. M. Henderson et al., `J. Chem. Phys. <https://dx.doi.org/10.1063/1.2921797>`__ **128**, 194105 (2008).

`doi:10.1063/1.2921797 <http://dx.doi.org/10.1063/1.2921797>`__

* ``LTA`` Local tau Approximation. LSDA exchange functional with density represented as a function of :math:`\tau`.

`doi:10.1063/1.479374 <http://dx.doi.org/10.1063/1.479374>`__

* ``LYP`` Lee, Yang and Parr Correlation Functional. C. Lee, W. Yang and R. G. Parr, `Phys. Rev. B <https://dx.doi.org/10.1103/PhysRevB.37.785>`__ **37**, 785(1988); B. Miehlich, A. Savin, H. Stoll and H. Preuss, `Chem. Phys. Lett. <https://dx.doi.org/10.1016/0009-2614(89)87234-3>`__ **157**, 200 (1989).

`doi:10.1103/PhysRevB.37.785,10.1016/0009-2614(89)87234-3 <http://dx.doi.org/10.1103/PhysRevB.37.785,10.1016/0009-2614(89)87234-3>`__

* ``M052XC`` M05-2X Meta-GGA Correlation Functional

`doi:10.1021/ct0502763 <http://dx.doi.org/10.1021/ct0502763>`__

* ``M052XX`` M05-2X Meta-GGA Exchange Functional

`doi:10.1021/ct0502763 <http://dx.doi.org/10.1021/ct0502763>`__

* ``M05C`` M05 Meta-GGA Correlation Functional

`doi:10.1063/1.2126975 <http://dx.doi.org/10.1063/1.2126975>`__

* ``M05X`` M05 Meta-GGA Exchange Functional

`doi:10.1063/1.2126975 <http://dx.doi.org/10.1063/1.2126975>`__

* ``M062XC`` M06-2X Meta-GGA Correlation Functional

`doi:10.1007/s00214-007-0310-x <http://dx.doi.org/10.1007/s00214-007-0310-x>`__

* ``M062XX`` M06-2X Meta-GGA Exchange Functional

`doi:10.1007/s00214-007-0310-x <http://dx.doi.org/10.1007/s00214-007-0310-x>`__

* ``M06C`` M06 Meta-GGA Correlation Functional

`doi:10.1007/s00214-007-0310-x <http://dx.doi.org/10.1007/s00214-007-0310-x>`__

* ``M06HFC`` M06-HF Meta-GGA Correlation Functional

`doi:10.1021/jp066479k <http://dx.doi.org/10.1021/jp066479k>`__

* ``M06HFX`` M06-HF Meta-GGA Exchange Functional

`doi:10.1021/jp066479k <http://dx.doi.org/10.1021/jp066479k>`__

* ``M06LC`` M06-L Meta-GGA Correlation Functional

`doi:10.1063/1.2370993 <http://dx.doi.org/10.1063/1.2370993>`__

* ``M06LX`` M06-L Meta-GGA Exchange Functional

`doi:10.1063/1.2370993 <http://dx.doi.org/10.1063/1.2370993>`__

* ``M06X`` M06 Meta-GGA Exchange Functional

`doi:10.1007/s00214-007-0310-x <http://dx.doi.org/10.1007/s00214-007-0310-x>`__

* ``M12C`` Meta GGA Correlation Functional. Meta-GGA correlation functional based on first principles, see M. Modrzejewski et al., `J. Chem. Phys. <https://dx.doi.org/10.1063/1.4768228>`__ **137**, 204121 (2012).

`doi:10.1063/1.4768228 <http://dx.doi.org/10.1063/1.4768228>`__

* ``MK00`` Exchange Functional for Accurate Virtual Orbital Energies

`doi:10.1063/1.481298 <http://dx.doi.org/10.1063/1.481298>`__

* ``MK00B`` Exchange Functional for Accurate Virtual Orbital Energies. MK00 with gradient correction of the form of B88X but with different empirical parameter.

`doi:10.1063/1.481298 <http://dx.doi.org/10.1063/1.481298>`__

* ``P86`` .. Gradient correction to VWN.

`doi:10.1103/PhysRevB.33.8822 <http://dx.doi.org/10.1103/PhysRevB.33.8822>`__

* ``PBEC`` PBE Correlation Functional

`doi:10.1103/PhysRevLett.77.3865 <http://dx.doi.org/10.1103/PhysRevLett.77.3865>`__

* ``PBESOLC`` PBEsol Correlation Functional

`doi:10.1103/PhysRevLett.100.136406 <http://dx.doi.org/10.1103/PhysRevLett.100.136406>`__

* ``PBESOLX`` PBEsol Exchange Functional

`doi:10.1103/PhysRevLett.100.136406 <http://dx.doi.org/10.1103/PhysRevLett.100.136406>`__

* ``PBEX`` PBE Exchange Functional

`doi:10.1103/PhysRevLett.77.3865 <http://dx.doi.org/10.1103/PhysRevLett.77.3865>`__

* ``PBEXREV`` Revised PBE Exchange Functional. Changes the value of the constant R from the original PBEX functional

`doi:10.1103/PhysRevLett.80.890 <http://dx.doi.org/10.1103/PhysRevLett.80.890>`__

* ``PW86`` .. GGA Exchange Functional.

`doi:10.1103/PhysRevB.33.8800 <http://dx.doi.org/10.1103/PhysRevB.33.8800>`__

* ``PW91C`` Perdew-Wang 1991 GGA Correlation Functional

`doi:10.1103/PhysRevB.46.6671 <http://dx.doi.org/10.1103/PhysRevB.46.6671>`__

* ``PW91X`` Perdew-Wang 1991 GGA Exchange Functional

`doi:10.1103/PhysRevB.46.6671 <http://dx.doi.org/10.1103/PhysRevB.46.6671>`__

* ``PW92C`` Perdew-Wang 1992 GGA Correlation Functional. Electron-gas correlation energy.

`doi:10.1103/PhysRevB.45.13244 <http://dx.doi.org/10.1103/PhysRevB.45.13244>`__

* ``STEST`` Test for number of electrons
* ``TFKE`` Thomas-Fermi Kinetic Energy. Automatically generated Thomas-Fermi Kinetic Energy.

`doi:10.1017/S0305004100011683 <http://dx.doi.org/10.1017/S0305004100011683>`__

* ``TH1`` Tozer and Handy 1998. Density and gradient dependent first row exchange-correlation functional.

`doi:10.1063/1.475638 <http://dx.doi.org/10.1063/1.475638>`__

* ``TH2`` .. Density and gradient dependent first row exchange-correlation functional.

`doi:10.1021/jp980259s <http://dx.doi.org/10.1021/jp980259s>`__

* ``TH3`` .. Density and gradient dependent first and second row exchange-correlation functional.

`doi:TH3/4 <http://dx.doi.org/TH3/4>`__

* ``TH4`` .. Density an gradient dependent first and second row exchange-correlation functional.

`doi:TH3/4 <http://dx.doi.org/TH3/4>`__

* ``THGFC`` .. Density and gradient dependent first row exchange-correlation functional for closed shell systems. Total energies are improved by adding :math:`DN`, where :math:`N` is the number of electrons and :math:`D=0.1863`.

`doi:10.1016/S0009-2614(97)00586-1 <http://dx.doi.org/10.1016/S0009-2614(97)00586-1>`__

* ``THGFCFO`` .. Density and gradient dependent first row exchange-correlation functional. FCFO = FC + open shell fitting.

`doi:10.1016/S0009-2614(97)00586-1 <http://dx.doi.org/10.1016/S0009-2614(97)00586-1>`__

* ``THGFCO`` .. Density and gradient dependent first row exchange-correlation functional.

`doi:10.1016/S0009-2614(97)00586-1 <http://dx.doi.org/10.1016/S0009-2614(97)00586-1>`__

* ``THGFL`` .. Density dependent first row exchange-correlation functional for closed shell systems.

`doi:10.1016/S0009-2614(97)00586-1 <http://dx.doi.org/10.1016/S0009-2614(97)00586-1>`__

* ``TPSSC`` TPSS Correlation Functional. J. Tao, J. P. Perdew, V. N. Staroverov, and G. E. Scuseria, `Phys. Rev. Lett. <https://dx.doi.org/10.1103/PhysRevLett.91.146401>`__ **91**, 146401 (2003).

`doi:10.1103/PhysRevLett.91.146401 <http://dx.doi.org/10.1103/PhysRevLett.91.146401>`__

* ``TPSSX`` TPSS Exchange Functional. J. Tao, J. P. Perdew, V. N. Staroverov, and G. E. Scuseria, `Phys. Rev. Lett. <https://dx.doi.org/10.1103/PhysRevLett.91.146401>`__ **91**, 146401 (2003).

`doi:10.1103/PhysRevLett.91.146401 <http://dx.doi.org/10.1103/PhysRevLett.91.146401>`__

* ``VSXC`` .

`doi:10.1063/1.476577 <http://dx.doi.org/10.1063/1.476577>`__

* ``VW`` von Weizsäcker kinetic energy. Automatically generated von Weizsäcker kinetic energy.

`doi:10.1007/BF01337700 <http://dx.doi.org/10.1007/BF01337700>`__

* ``VWN3`` Vosko-Wilk-Nusair (1980) III local correlation energy. VWN 1980(III) functional

`doi:VWN80 <http://dx.doi.org/VWN80>`__

* ``VWN5`` Vosko-Wilk-Nusair (1980) V local correlation energy. VWN 1980(V) functional. The fitting parameters for :math:`\Delta\varepsilon_{c}(r_{s},\zeta)_{V}` appear in the caption of table 7 in the reference.

`doi:VWN80 <http://dx.doi.org/VWN80>`__

* ``XC-M05-2X`` M05-2X Meta-GGA Exchange-Correlation Functional. Here it means M05-2X exchange-correlation part which excludes HF exact exchange term. Y. Zhao, N. E. Schultz, and D. G. Truhlar, `J. Chem. Theory Comput. <https://dx.doi.org/10.1021/ct0502763>`__ **2**, 364 (2006).

`doi:10.1021/ct0502763 <http://dx.doi.org/10.1021/ct0502763>`__

* ``XC-M05`` M05 Meta-GGA Exchange-Correlation Functional. Here it means M05 exchange-correlation part which excludes HF exact exchange term. Y. Zhao, N. E. Schultz, and D. G. Truhlar, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.2126975>`__ **123**, 161103 (2005).

`doi:10.1063/1.2126975 <http://dx.doi.org/10.1063/1.2126975>`__

* ``XC-M06-2X`` M06-2X Meta-GGA Exchange-Correlation Functional. Here it means M06-2X exchange-correlation part which excludes HF exact exchange term. Y. Zhao and D. G. Truhlar, Theor. Chem. Acc. 120, 215 (2008).

`doi:10.1007/s00214-007-0310-x <http://dx.doi.org/10.1007/s00214-007-0310-x>`__

* ``XC-M06-HF`` M06-HF Meta-GGA Exchange-Correlation Functional. Here it means M06-HF exchange-correlation part which excludes HF exact exchange term. Y. Zhao and D. G. Truhlar, J. Phys. Chem. A 110, 13126 (2006).

`doi:10.1021/jp066479k <http://dx.doi.org/10.1021/jp066479k>`__

* ``XC-M06-L`` M06-L Meta-GGA Exchange-Correlation Functional. Y. Zhao and D. G. Truhlar, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.2370993>`__ **125**, 194101 (2006).

`doi:10.1063/1.2370993 <http://dx.doi.org/10.1063/1.2370993>`__

* ``XC-M06`` M06 Meta-GGA Exchange-Correlation Functional. Here it means M06 exchange-correlation part which excludes HF exact exchange term. Y. Zhao and D. G. Truhlar, Theor. Chem. Acc. 120, 215 (2008).

`doi:10.1007/s00214-007-0310-x <http://dx.doi.org/10.1007/s00214-007-0310-x>`__

* ``XC-M08-HX`` M08-HX Meta-GGA Exchange-Correlation Functional. Here it means M08-HX exchange-correlation part which excludes HF exact exchange term. Y. Zhao and D. G. Truhlar, `J. Chem. Theory Comput. <https://dx.doi.org/10.1021/ct800246v>`__ **4**, 1849 (2008).

`doi:10.1021/ct800246v <http://dx.doi.org/10.1021/ct800246v>`__

* ``XC-M08-SO`` M08-SO Meta-GGA Exchange-Correlation Functional. Here it means M08-SO exchange-correlation part which excludes HF exact exchange term. Y. Zhao and D. G. Truhlar, `J. Chem. Theory Comput. <https://dx.doi.org/10.1021/ct800246v>`__ **4**, 1849 (2008).

`doi:10.1021/ct800246v <http://dx.doi.org/10.1021/ct800246v>`__

* ``XC-M11-L`` M11-L Exchange-Correlation Functional. R. Peverati and D. G. Truhlar, Journal of Physical Chemistry Letters 3, 117 (2012).

`doi:10.1021/jz201525m <http://dx.doi.org/10.1021/jz201525m>`__

* ``XC-SOGGA`` SOGGA Exchange-Correlation Functional. Y. Zhao and D. G. Truhlar, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.2912068>`__ **128**, 184109 (2008).

`doi:10.1063/1.2912068 <http://dx.doi.org/10.1063/1.2912068>`__

* ``XC-SOGGA11-X`` SOGGA11-X Exchange-Correlation Functional. Here it means SOGGA11-X exchange-correlation part which excludes HF exact exchange term. R. Peverati and D. G. Truhlar, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3663871>`__ **135**, 191102 (2011).

`doi:10.1063/1.3663871 <http://dx.doi.org/10.1063/1.3663871>`__

* ``XC-SOGGA11`` SOGGA11 Exchange-Correlation Functional. R. Peverati, Y. Zhao and D. G. Truhlar, J. Phys. Chem. Lett. 2 (16), 1991 (2011).

`doi:10.1021/jz200616w <http://dx.doi.org/10.1021/jz200616w>`__

.. _the_density_functional_program--libxc-functionals:

LibXC functionals
=================

Functionals from the LibXC library `https://www.tddft.org/programs/libxc <https://www.tddft.org/programs/libxc>`__ can be used with the dft/ks programs by entering the functional names as given
in the LibXC documentation. For example

.. code-block:: text

   ks,GGA_X_B88,GGA_C_LYP

defines an input for the B-LYP functional using the LibXC functional implementation instead of the internal Molpro ones.
Correspondingly,

.. code-block:: text

   ks,HYB_GGA_XC_B3LYP

defines a hybrid B3LYP calculation that would correspond to

.. code-block:: text

   ks,b88,dirac,lyp,vwn3; dftfac,0.72,0.08,0.81,0.19; exchange,0.2

using the corresponding individual functionals from Molpro. Note the LibXC's B3LYP does *not* correspond to Molpro's B3LYP, since the latter uses the VWN5 version of the VWN local correlation
functional instead of the VWN3 version.

Calculations with range-separated functionals require some more input in order to get integrals for the corresponding
long-range erf interaction. For example

.. code-block:: text

   omega=0.3    !range-separation parameter
   srx=0.157706 !short-range exchange
   {int; ERFLERFC,mu=$omega,srfac=$srx}
   ks,HYB_GGA_XC_WB97X

will have to be entered in the input file for performing calculations with the wB97X functional by Chai and Head-Gordon `https://doi.org/10.1063/1.2834918 <https://doi.org/10.1063/1.2834918>`__.

The explicit input for the omega and short-range exchange scaling factor (``srx``) can be avoided if the calculation is run in density-fitting mode, like:

.. code-block:: text

   df-ks,HYB_GGA_XC_WB97X

For getting the corresponding wB97X-D functional `https://doi.org/10.1039/B810189B <https://doi.org/10.1039/B810189B>`__, add the D2-type dispersion correction

.. code-block:: text

   df-ks,HYB_GGA_XC_WB97X; disp,d2

see section `the density functional program#Empirical damped dispersion correction <the_density_functional_program.html#empirical-damped-dispersion-correction>`__ for more details.

Another class of functionals are vdwDF's (van-der-Waals density functionals) which include also a nonlocal correlation functional part, see for instance the review
`https://doi.org/10.1088/0034-4885/78/6/066501 <https://doi.org/10.1088/0034-4885/78/6/066501>`__. Molpro currently supports calculations with the VV10 (Vydrov & Van Voorhis 2010) functional
`https://doi.org/10.1063/1.3521275 <https://doi.org/10.1063/1.3521275>`__. The local part for this functional can be taken from LibXC:

.. code-block:: text

   ks,GGA_XC_VV10

Regarding input descriptions for the nonlocal functional contribution, browse to section `the density functional program#van-der-Waals DF's <the_density_functional_program.html#van-der-waals-df-s>`__.

**Important note regarding some functionals from LibXC that also are available in Molpro's internal functional library:**
A number of functionals which are both available in LibXC and Molpro may give slightly different results in total energies (in the micro hartree range for small molecules) due to truncation of significant digits of underlying parameters. An example for this is the PBE functional `https://doi.org/10.1103/PhysRevLett.77.3865 <https://doi.org/10.1103/PhysRevLett.77.3865>`__ in which case the implementation in Molpro uses parameters taken only from the PBE paper some of which are truncated compared to the original source, see references in the PBE paper. Compared to this, LibXC uses a more accurate representation of the parameters in terms of significant digits, resulting to differences in the micro hartree range. Such differences are unlikely to have any effect on energy differences, such as reaction or atomisation energies, but should be kept in mind when comparing total energies calculated with the Molpro and LibXC functionals, respectively.

Functionals known to yield slightly different results according to this:

.. list-table::
   :header-rows: 1

   * - Molpro
     - LibXC
   * - PBEX
     - GGA_X_PBE
   * - PBEXREV
     - GGA_X_PBE_R
   * - PBEC
     - GGA_C_PBE
   * - PBESOLC
     - GGA_C_PBE_SOL
   * - PW91C
     - GGA_C_PW91
   * - HCTH93
     - GGA_XC_HCTH_93
   * - HCTH120
     - GGA_XC_HCTH_120
   * - M06LX
     - MGGA_X_M06_L
   * - B95
     - MGGA_C_BC95
   * - TPSSC
     - MGGA_C_TPSS
   * - M06C
     - MGGA_C_M06
   * - M06HFC
     - MGGA_C_M06_HF
   * - M062XC
     - MGGA_C_M06_2X
   * - M06LC
     - MGGA_C_M06_L
   * - M05C
     - MGGA_C_M05
   * - M052XC
     - MGGA_C_M05_2X
   * - M06X
     - HYB_MGGA_X_M06
   * - M062XX
     - HYB_MGGA_X_M06_2X

.. _the_density_functional_program--implementing-new-functionals:

Implementing new functionals
============================

New functionals are implemented based upon the automatic code generation (ACG) program (`doi:10.1016/S0010-4655(01)00148-5 <http://dx.doi.org/10.1016/S0010-4655(01)00148-5>`__). In order to work the program requires the maple mathematics program and an XSLT parser, defined by the variable XSLT in CONFIG.

The format of the input file is an XML file containing all of the information about the new functional. All density functional XML files are placed in the directory ``lib/df`` and are automatically activated on the next instance of the ``make`` command in the Molpro base directory.

The root element of the XML document is ``content``. At the next level the element, ``functional`` is expected, 1 per file.

The ``functional`` element has an ``id`` attribute which is used as the keyword for the functional in Molpro, and optional ``doi`` attribute for specifying a reference. The allowed elements are defined in the following table:

.. list-table::
   :header-rows: 1

   * - Elements allowed for defining functionals
     - 
   * - title
     - Text to appear as a heading for the functional documentation
   * - tex
     - Text to document the functional

The final element is ``maple`` for which multiple cases are allowed. A typical maple expression such as

.. code-block:: text

   A:=1.2:

is written as

.. code-block:: text

   <maple lhs="A">1.2</maple>.

To input a Maple procedure such as

.. code-block:: text

   add_together:=proc(a,b) a+b end:

one should write

.. code-block:: text

   <maple lhs="add_together" proc="a,b">a+b</maple>.

As an example the Perdew-Wang 1991 GGA exchange functional is given below:

.. code-block:: text

   <?xml version="1.0" encoding="ISO-8859-1"?>
   <content>
    <functional id="PW91X">
     <title>Perdew-Wang 1991 GGA Exchange Functional</title>
     <maple lhs="g">1/2*E(2*rho(s))</maple>
     <maple lhs="G">1/2*E(2*rho(s))</maple>
     <maple lhs="E" proc="n"> -3/(4*Pi)*(3*Pi^2)^(1/3)*n^(4/3)*F(S)</maple>
     <maple lhs="S">chi(s)/(2*(6*Pi^2)^(1/3))</maple>
     <maple lhs="F" proc="S">
      (1+0.19645*S*arcsinh(7.7956*S) + (0.2743-0.1508*exp(-100*S^2))*S^2)/
      (1+0.19645*S*arcsinh(7.7956*S)+0.004*S^4)
     </maple>
    </functional>
   </content>

.. _the_density_functional_program--note-on-minnesota-density-functionals:

Note on Minnesota Density Functionals
=====================================

It has been observed by Mardirossian and Head-Gordon that several density functionals from the Minnesota group, including M06, M11, M06-L, M06-HF and M11-L, exhibit a very slow convergence of intermolecular interaction energies with respect to the basis set, see `JCTC 9 (2013) 4453 <https://pubs.acs.org/doi/10.1021/ct400660j>`__. Apparently, this problem can not be cured by larger integration grids and originates from a contribution to the exchange enhancement factor whose shape can strongly depend on the chosen basis set. Based on these observations it is recommended to use basis sets which were originally employed to develop these functionals.

.. _the_density_functional_program--note-on-mk00-and-mk00b-functionals:

= Note on MK00 and MK00B functionals
====================================

The MK00 and MK00B functionals (termed MGGA_X_MK00 and MGGA_X_MK00B in LibXC) `J. Chem. Phys. 112, 7002–7007 (2000) <https://doi.org/10.1063/1.481298>`__ should better not be used in general calculations with Molpro due to the problem that the denominators :math:`\tau-\upsilon/4` in the functional can be zero or even turn negative, producing unphysical results.

.. _the_density_functional_program--implementing-new-hybrid-functionals:

Implementing new hybrid-functionals
-----------------------------------

Hybrid functionals are defined in the file ``lib/dalias.registry``. Entries can be added to this file as required, and then run ``make`` to update the other registry files.

.. _the_density_functional_program--exact-exchange-kohn-sham-methods:

Exact exchange Kohn-Sham methods
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A number of exact exchange Kohn-Sham methods are implemented in Molpro. Here, in contrast to standard hybrid functionals, the functional derivative of the exact exchange energy is taken with respect to the electron density:
\begin{equation}

.. code-block:: text

     v_{\text{x}}({\bf r})=\frac{\delta E_{\text{x}}[\rho]}{\delta\rho({\bf r})} \label{eq:vx}

\end{equation}
which yields a *local* exchange potential opposed to the Hartree-Fock method in which the potential is nonlocal. Due to this, while total energies from exact exchange KS methods are close to HF energies, orbitals and orbital energies can strongly differ from each other. The advantage of exact exchange KS methods is that the orbitals and orbital energies can directly be used as input data for time-dependent DFT methods employing local KS kernels for calculating response properties or excitation energies, see also section `Time-dependent density functional theory <the_density_functional_program.html#time-dependent-density-functional-theory>`__. Moreover, orbitals from exact exchange KS calculations are also suitable for use in DFT-SAPT calculations (section :doc:`symmetry-adapted intermolecular perturbation theory <symmetry-adapted_intermolecular_perturbation_theory>`) because the local exact exchange potential :math:`v_{\text{x}}({\bf r})` possesses the correct asymptotic behaviour and thus yields an improved description of the electronic density in the asymptotic range.

Since the exact exchange energy is only an implicit functional of the density (through the direct dependency on the occupied molecular orbitals) the functional derivative in Eq. \eqref{eq:vx} can not be obtained by a direct differentiation. Two different methods are implemented in Molpro by which the local exchange potential can be computed, the LHF (Local Hartree-Fock) method by Della Sala and Görling [1] and the Optimised Effective Potential (OEP) method employing the auxiliary basis set implementation of Ref. [5]. The two different approaches are described in the following subsections.

Note that (almost) all methods described in this section can **only be run without using symmetry**. Furthermore, for most of the approaches also no open-shell implementation is available.

**Bibliography**:
:math:`[1]` F. Della Sala and A. Görling, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.1398093>`__ **115**, 5718 (2001)
:math:`[2]` A. Heßelmann and F.R. Manby, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.2072887>`__ **123**, 164116 (2005)
:math:`[3]` A. Görling, A. Heßelmann, M. Jones and M. Levy, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.2826366>`__ **128**, 104104 (2008)
:math:`[4]` A. Heßelmann and A. Görling, `Chem. Phys. Lett. <https://dx.doi.org/10.1016/j.cplett.2008.02.042>`__ **455**, 110 (2008)
:math:`[5]` A. Heßelmann, A. Götz, F. Della Sala and A. Görling, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.2751159>`__ **127**, 054102 (2007)
:math:`[6]` A. Heßelmann, `J. Chem. Theory Comput. <https://dx.doi.org/10.1021/acs.jctc.7b01233>`__ **14**, 1943 (2018)

.. _the_density_functional_program--local-hartree-fock-lhf-method:

Local Hartree-Fock (LHF) method
-------------------------------

The LHF method is an *approximate* exact exchange KS method which derives the local exchange potential by starting from the assumption that the HF and the exchange-only KS determinants are identical, see Ref. [1]. An advantage of the method is that the approach always yields smooth and physically correct potentials (cf. the next section and Refs. [3,4]). A disadvantage of the LHF method is that the potential has to be computed on a numerical grid which can be quite costly, particularly due to the fact that the Slater potential contribution to :math:`v_{\text{x}}` requires a computation of the electrostatic potential of the product of two AO basis functions on the grid [1]. The use of the density-fitting approach of Ref. [2], however, significantly reduces this cost, see below.

The LHF functional is only implemented for closed-shell systems in Molpro. No point group symmetry can be used in both iterative and non-iterative (T)LHF calculations.

A standard LHF calculation with Molpro can be performed with the Kohn-Sham DFT program using

.. code-block:: text

      ks,lhf

During the SCF iterations, the program prints out the HOMO eigenvalue and the Slater exchange energy which should be identical to the exact exchange energy. It is always good to check in the output that the latter holds true.

Instead of performing the LHF calculation self-consistently, it is also possible to do a one-step LHF calculation using orbitals and orbital energies from a different HF/KS calculation as input. This can be done by calling the LHF program directly, e.g.

.. code-block:: text

      {hf; save,2100.2}
      {lhf,orb=2100.2}

The following options can be used with the LHF program:

* ``ORB`` orbital record containing previous orbitals (mandatory)
* ``LHFFIT`` use density fitting to compute the exchange matrix
* ``POT`` record in which to write the local exchange potential
* ``RESTART`` recompute the LHF orbitals and orbital energies from an already computed exchange potential
* ``SLA`` if set to 2, compute the Slater potential with the method described in appendix A in Ref. [1] (default: 1)
* ``BLOCK`` batch size for numerical grid
* ``PUNCH`` if set to 1, the Slater potential and the response potential will be written to the files ’slater.dat’ and ’response.dat’ (names can be changed by setting the variables SLATER and RESPONSE in the Molpro input file before calling the LHF program). The ’response.dat’ file will also contain the total exchange potential. The default is to not punch out the potentials.
* ``DAMP`` scale the response potential by :math:`\rho/(\rho+\mathrm{damp})` in order to force the potential to decay more rapidly in the asymptotic range (typical value :math:`\mathrm{damp}=1d-5`). Not used by default, but can be helpful in cases where the convergence of the KS calculation is slow.

To significantly speed up the computation of the Slater potential contribution, the density-fitting method of Ref. [2] can be used. It is automatically switched to if a density-fitted KS calculation is performed:

.. code-block:: text

      df-ks,lhf

Note, however, that now an additional auxiliary basis set with the name DFLHF needs to be added in the basis input section which, e.g.:

.. code-block:: text

      ...
      set,dflhf
      default,avtz/jkfit
      ...

Notice that the use of the underlying JKFit basis sets that correspond to the given orbital basis set are most suitable, because the fitting is performed for products of two occupied molecular orbitals. Moreover, note that **no contracted auxiliary basis sets** can be used with the DF-LHF program.

There also exists a one-step density-fitting analogue to the LHF program:

.. code-block:: text

      {hf; save,2100.2}
      {dflhf,orb=2100.2}

In addition to the options for the LHF program given above, the DFLHF program has the further options

* ``POISSON`` set to :math:`\ne 0` for using a mixed Poisson/Gaussian auxiliary basis set to further speed up the calculation of the Slater potential, see Ref. [2]. The Poisson auxiliary basis set needs to be supplied in the basis input section.
* ``INT`` switch 3-index integral routine to be used (can take the values 1,2 or 3 (default is 2))

It is also possible to reuse the exchange potential computed by the LHF/DFLHF programs in a subsequent KS calculation. In this case, the potential is kept fixed during the SCF and only the Coulomb potential is variationally optimised. This can be done by, e.g. (’tlhf’ denoting ’Transformation Local Hartree-Fock’)

.. code-block:: text

      {hf; save,2100.2}
      {lhf,orb=2100.2}
      {ks,tlhf}

The LHF functional can also be combined with other functionals as in common hybrid-DFT methods. For example, the hybrid PBE0 functional (including 25 percent exact exchange) would be implemented by

.. code-block:: text

      {ks,lhf,pbex,pbec; dftfac,0.25,0.75,1.0}

.. _the_density_functional_program--optimised-effective-potential-oep-method:

Optimised Effective Potential (OEP) method
------------------------------------------

The functional derivative of the exchange energy can also be calculated by using the optimised effective potential method (OEP) which was originally derived by Talman and Shadwick ( `Phys. Rev. A <https://dx.doi.org/10.1103/PhysRevA.14.36>`__ **14**, 36 (1976)). This method sometimes is also denoted as EXX (Exact Exchange) method if used in conjunction with exchange-only KS methods.

Unfortunately, OEP methods can be numerically unstable if finite basis sets are used (which is, of course, generally the case), see Refs. [3] and [4]. The reason for this originates from the fact that the OEP equation is a response-type equation where the underlying (static) KS response function is described in terms of products of occupied and unoccupied orbitals. It turns out that it generally is difficult to adequately represent the (potentially linearly dependent) occ-virt space by an auxiliary function space [3,4]. To be able to obtain physically sound OEP (exchange) potentials, it is necessary to either employ regularisation techniques to eliminate the small eigenvalues of the response matrix (see, e.g., T. Heaton-Burgess, F. A. Bulat, W. Yang, `Phys. Rev. Lett. <https://dx.doi.org/10.1103/PhysRevLett.98.256401>`__ **98**, 256401 (2007)), or to use auxiliary basis sets that are *balanced* to the orbital basis set. As a rule of thumb, the attribute ’balanced’ here means that the potential does not change anymore when the orbital basis space is increased while the auxiliary basis set is kept fixed [4,5].

Balanced orbital-auxiliary basis sets have been derived for a limited number of elements in Ref. [5]. They can be specified in the basis input section by

.. code-block:: text

      set,orbital
      default,avtz-orb-oep
      set,oep
      default,avtz-aux-oep

(see the oepbas.libmol file in the library directory for all available OEP basis sets).

Auxiliary basis set OEP/EXX calculations based on the approach of Ref. [5] can be performed with the EXX program, which, using the most essential options, can be called as

.. code-block:: text

      {exx,orb=<orb.rec>,homo=1,charge=1}

where the supplement of previous orbitals in a given record is mandatory. Furthermore, the options ``homo=1`` and ``charge=1`` activate the HOMO and the charge constraints to the potential which adds to the numerical stability of the OEP method, see Ref. [5].

Note that the OEP orbital basis sets are uncontracted and therefore calculations for larger molecules can become quite expensive. Meaningful OEP calculations can, however, also be performed with standard contracted basis sets if some regularisation techniques are used in the solution to the OEP equation. For this, it is recommended to use

.. code-block:: text

      {exx,...,oep=7,gamma=3d-4}

where :math:`\gamma` is a regularisation factor used in a Tikhonov regularisation approach to the solution of the OEP equation, see Ref. [6].

Further options to the EXX program are:

* ``MAXIT`` maximum number of iterations
* ``SCFTHR`` threshold for energy convergence
* ``OEP`` choose between 7 (!) different OEP routines (an explanation of all these would blow up this section significantly, default is OEP=1)
* ``PRINT`` debug print level
* ``FERAMA`` use Fermi-Amaldi potential (instead of OEP potential)
* ``ELP`` use Effective Local Potential method by Staroverov *et al.* (`J. Chem. Phys. <https://dx.doi.org/10.1063/1.2345650>`__ **125**, 081104 (2006))
* ``DFIT`` if set to :math:`\ne` 0, use density fitting for two-electron integrals
* ``DIRECT`` set to :math:`\ne` 0 for integral-direct calculation (not very efficient at the moment)
* ``ITVREF`` the reference potential can be calculated with the ELP method using OEP=4 or OEP=5. With the setting of ITVREF to a value :math:`n`, the reference potential can be held fixed from iteration :math:`n+1` onwards (to speed up the calculation).

The underlying OEP module, that is called inside the EXX program, has the further options:

* ``VREF`` can be set to ’BASIS’ or ’BASIS2’ according to the two schemes described in Ref. [5] to determine the coefficients for the reference potential
* ``VREST`` can be set to zero to omit calculation of the rest potential
* ``AUX`` norm (should be ’J’)
* ``ATOM1`` set (x,y,z) coordinates for a starting position used for plotting the potential
* ``ATOM2`` set (x,y,z) coordinates for a terminal position used for plotting the potential
* ``SYMCEN1/2`` do not use!
* ``TEST`` can be used to switch on several tests during the generation of the OEP potential
* ``POT`` enter a name of the file to which the potential is written to (along a line that can be specified with ATOM1/2, see above)
* ``CHARGE`` set to :math:`\ne` 0 for activating the charge condition
* ``HOMO`` set to :math:`\ne` 0 for activating the HOMO condition
* ``HOMO1`` can additionally be used to fix the orbital energy of an orbital whose energy lies below the HOMO level (is not available for all OEP routines)
* ``RESPEIG`` set to :math:`\ne` 0 to print out the eigenvalues of the response matrix (useful to test stability of the OEP method)
* ``RHS`` set to :math:`\ne` 0 for printing the right-hand side in the output
* ``XPRINT`` set to :math:`\ne` 0 for printing the response matrix
* ``SOLVE`` matrix inversion methods to solve the OEP equation. The different options are: GESV (default), SVD, SVD2, TIKH
* ``THR`` threshold value for singular value decomposition (SVD) or Tikhonov regularisation (TIKH)
* ``FILTER`` an integer number can be entered to filter out the response function eigenvectors with the lowest eigenvalues in an SVD matrix inversion
* ``SVD`` here, SVD is used to perform a singular value decomposition of the (aux\ :math:`|`\ occ\ :math:`\times`\ virt) 3-index integrals
* ``SVDTHR`` the corresponding SVD threshold for this
* ``CONTR`` set to :math:`\ne` 0 to use contraction of auxiliary basis through the SVD of (aux\ :math:`|`\ occ\ :math:`\times`\ virt) integrals
* ``LAPLACE`` solve OEP within the AO basis set making use of the Laplace transformation
* ``VXDUMP`` dump the nonlocal and local exchange potentials to a record
* ``OEPDUMP`` dump record for OEP which contains the orbitals, the density and the eigenvalues
* ``SAVE`` record in which the coefficients of the potential can be written to
* ``READ`` record from which the coefficients can be read
* ``OEPPRINT`` debug print level
* ``HOMOORB`` specify an orbital dump record from a previous calculation used to determine the vector for the HOMO condition (useful if the HOMO swaps with a lower lying level with a different method)
* ``FIXEIG`` can be used to specify the number of an orbital whose eigenvalue should be fixed (see also HOMO1 option)
* ``EQNORM`` set the norm for the OEP equation (not available for all OEP routines)
* ``ELPMODE`` switch the mode in ELP calculations
* ``EXIT`` can be used to deallocate some arrays that are used during the OEP calculation
* ``CONV`` threshold for testing the energy convergence. When the energy change is below this threshold, the exchange potential will be kept fixed and will not be calculated anymore.
* ``VXDIFF`` specify a record number for a record in which to write the matrix :math:`\langle i|v_x^{\text{NL}}-v_x|j\rangle` containing the difference of the nonlocal and the local exact exchange potentials. This is required in TDDFT calculations employing the exact-exchange KS kernel.
* ``THRS`` an eigenvalue threshold used in the decomposition of the overlap matrix, used to reduce the auxiliary function space (not available in all OEP routines)
* ``GAMMA`` Tikhonov regularisation factor (only used for OEP=7 case). A value of :math:`\gamma=3\cdot 10^{-4}` should conventionally be used.

Like in case of the LHF method, there also exists a one-step OEP program which takes orbitals from a preceeding SCF calculations, solves the OEP equations in this basis, and writes out the new orbitals and eigenvalues to a new record. A typical example that additionally also writes out the matrix elements :math:`\langle i|v_x^{\text{NL}}-v_x|j\rangle` to a record is given by:

.. code-block:: text

      {hf; save,2100.2}
      {oep,orb=2100.2,vxdiff=5000.2,gamma=3d-4,homo=1}

It is possible to do hybrid EXX-GGA calculations by using the ``EXXHYXB`` program. In addition to the options given above for the ``EXX`` program it can read the directives for standard KS calculations (see section `directives <the_density_functional_program.html#directives>`__). Further options for the ``EXXHYXB`` program are:

* ``XFAX`` factor for exact exchange
* ``ADD`` set to :math:`\ne` 0 in order to add the GGA contribution to the xc matrix to the rhs of the OEP equation
* ``SHIFT`` if set to a value :math:`\ne` 0 the asymptotic correction method for the xc potential described in Ref. [6] will be used

As an example, for using the local PBE0 functional employing the asymptotic correction method of Ref. [6] (LPBE0AC xc potential) the following input may be used:

.. code-block:: text

      {ks,lda; save,2100.2}
      {exxhyb,orb=2100.2,oep=7,homo=1,charge=1,add=1,xfac=0.25,shift=1
       func,pbex,pbec; dftfac,0.75,1.0}

Spin-unrestricted calculations with the EXX or the hybrid-EXX methods can be done by using the ``UEXX`` and the ``UEXXHYXB`` programs. Here the initial orbitals to be supplied have to stem from a preceeding unrestricted HF or KS calculation.

.. _the_density_functional_program--van-der-waals-df-s:

van-der-Waals DF's
~~~~~~~~~~~~~~~~~~

Long-range correlation interactions can be described by so-called van-der-Waals density functionals
(vdwDF's) that are designed to correct the qualitatively wrong asymptotic behaviour of the xc energy
between two noncovalently bonded systems. vdwDF's are clearly different to standard density functionals
in that they are defined in terms of a nonlocal integral kernel :math:`\phi({\bf r}_1,{\bf r}_2)`: :math:`E_c^{vdwDF}=\int{\bf r}_1\int{\bf r_2}\rho({\bf r}_1) \phi({\bf r}_1,{\bf r}_2) \rho({\bf r}_2)`
where :math:`\phi` itself is a (nonlocal) function of the density :math:`\rho` and its derivative(s) :math:`\nabla\rho`. Due to this, the integral can
normally not be calculated analytically and requires a double-space integration using numerical quadrature techniques.

vdwDF correlation energies can be calculated both non-selfconsistently, calling the ``vdwDF`` program, and selfconsistently
using the ``ks`` program. An non-selfconsistent calculation for the VV10 functional by Vydrov & Van Voorhis `https://doi.org/10.1063/1.3521275 <https://doi.org/10.1063/1.3521275>`__ would
look like

.. code-block:: text

   {ks,GGA_XC_VV10; save,2100.2}
   eloc=energy
   {vdwDF; vv10,den=2100.2,toten=1}
   evv10=energy

where variable ``eloc`` stores the total energy for the standard Kohn-Sham calculation with the local part to the functional (``GGA_XC_VV10``) and
``evv10`` stores the sum of ``eloc`` plus the energy contribution for the nonlocal correlation part (``vv10``). Note that the VV10 functional is currently the only available
option to vdwDF. It can take the following suboptions:

* ``DEN`` Dump record containing the density matrix (must be supplied)
* ``TOTEN`` If ``TOTEN>0`` the total energy will be printed (and stored in the intrinsic ``energy`` variable) reading in the previous SCF energy
* ``GTHR`` This can be used to alter the threshold for the grid accuracy. It is particularly useful for larger systems where the double-space integration becomes more expensive and where the integration (probably) need not be highly accurate. Default: ``GTHR=<global grid threshold set in dft/ks>``.
* ``NBLOCK`` Block size for grid batches. Default: ``NBLOCK=0`` which actually means that no grid batching is performed at all (requiring more memory consumption).
* ``B`` The ``B`` parameter from the VV10 functional that is functional dependent. The program can detect a few number of functionals automatically and sets the value of ``B`` to the optimised values determined by Hujo and Grimme `https://doi.org/10.1039/C1CP20591A <https://doi.org/10.1039/C1CP20591A>`__. The default value is ``B=5.9`` that should be used in conjunction with the local ``GGA_XC_VV10`` functional part.

To use the complete VV10 functional in a self-consistent KS calculation, use:

.. code-block:: text

   ks,GGA_XC_VV10,vv10nl

i.e., append the nonlocal functional keyword ``vv10nl`` to the functional list. Further functional specific input can be added via, e.g.

.. code-block:: text

   ks,GGA_XC_VV10,vv10nl; vdwdf,print=1,gthr=1d-8,b=5.9

see the corresponding options to vdwDF above. The only new option in SCF calculations is a print option that can be used to switch on ``print=1`` and
off ``print=0`` the printing of the VV10NL correlation energies during the SCF. By default this is activated ``print>0``.

.. _the_density_functional_program--empirical-damped-dispersion-correction:

Empirical damped dispersion correction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Empirical damped dispersion corrections can be calculated in addition to Kohn-Sham calculations. This is particularly important in cases where long-range correlation effects become dominant.

The dispersion correction can be added to the DFT energy by using

.. code-block:: text

    ks,<func>; disp,<x>

or

.. code-block:: text

    ks,<func>,disp=<x>

The total energy will then be calculated as

.. math::

   E_{\text{DFT-D2}}=E_{\text{DFT}}+E_{\text{disp}}(\mbox{D2})

if :math:`x=d2` (see Ref. [2]),
.. math::

   E_{\text{DFT-D3}}=E_{\text{DFT}}+E_{\text{disp}}(\mbox{D3})

if :math:`x=d3` (see Ref. [3]), and
.. math::

   E_{\text{DFT-D4}}=E_{\text{DFT}}+E_{\text{disp}}(\mbox{D4})

if :math:`x=d4` (see Ref. [4]).

Currently the default dispersion correction added to the DFT energy is the D4 dispersion correction developed by Grimme *et al.*, see Ref. [4].

The ``disp,d3`` keyword can have the following additional options:

* ``FUNC`` Functional name (default: ``FUNC='pbe'``).
* ``VERSION`` Can have values 2 and 3 according to parametrisations from Refs. [2] and [3] (default: ``VERSION=3``)
* ``ANAL`` Performs a detailed analysis of pair contributions.
* ``GRAD`` Cartesian gradients are computed.
* ``ABC`` Calculate three-body dispersion contribution if ``ABC``\ :math:`\ne`\ 0.
* ``NOABC`` Do not calculate three-body dispersion contribution if ``NOABC``\ :math:`\ne`\ 0.
* ``NUM`` Calculate gradient numerically.
* ``OLD`` Same as ``VERSION=2``.
* ``ZERO`` DFT-D3 original zero-damping.
* ``BJ`` DFT-D3 with Becke-Johnson finite-damping.
* ``BJM`` Revised DFT-D3 with Becke-Johnson damping.
* ``CNTHR`` Neglect threshold in Bohr for CN (default=40).
* ``CUTOFF`` Neglect threshold in Bohr for :math:`E_{\text{disp}}`, (default=95).
* ``TZ`` Use special parameters for calculations with triple-zeta basis sets. Preliminary results in the SI of Ref. [3] indicate that results are slightly worse than with the default parameters and QZVP type basis sets. This option should be carefully tested for future use in very large computations.

(see also '`https://www.chemie.uni-bonn.de/pctc/mulliken-center/software/dft-d3 <https://www.chemie.uni-bonn.de/pctc/mulliken-center/software/dft-d3>`__ for further documentation).

The DFT-D4 program (``disp,d4``) accepts the options:

* ``CHRG`` Molecular charge.
* ``S6`` Scaling factor for leading order term.
* ``S8`` Scaling factor for :math:`C_8` dependent term.
* ``S9`` Scaling factor for :math:`C_9` dependent term.
* ``A1`` Parameter in Becke-Johnson damping function.
* ``A2`` Parameter in Becke-Johnson damping function.
* ``DFA`` Name of density functional (useful if the name conventions for functionals in the D4 program are different from Molpro's).
* ``LMBD`` Treatment of many-body dispersion. ``LMBD=0``: skip calculation of many-body dispersion interactions, ``LMBD=1``: full RPA-like MBD, ``LMBD=2``: Axilrod-Teller-Muto three-body term, ``LMBD=3``: D3-like approximated ATM term
* ``NOMB`` same as ``LMBD=0``
* ``GRAD`` Calculate gradient if ``LMBD=0``\ :math:`\ne 0`.
* ``HESS`` Calculate hessian (currently not used in Molpro).
* ``PRINT`` Set print level (always highest is set automatically with dispcorr4 command).
* ``G_A`` Charge scale height.
* ``G_C`` Charge scale steepness.
* ``REFQ`` Kind of charge model.

(see also '`https://github.com/dftd4/dftd4 <https://github.com/dftd4/dftd4>`__ for further documentation).

Alternatively, the D2, D3 or D4 dispersion corrections can also be calculated separately from the DFT calculation using the following template:

.. code-block:: text

    ks,<func>
    eks=energy
    <dispcorr3,dispcorr4>
    eks_plus_disp=eks+edisp

using ``dispcorr3`` for DFT-D3 or ``dispcorr4`` for DFT-D4.

The older DFT-D1 [1] or DFT-D2 [2] dispersion corrections by Grimme can be calculated by using the input

.. code-block:: text

    ks,<func>
    eks=energy
    dispcorr
    eks_plus_disp=eks+edisp

with the following options to ``dispcorr``:

* ``MODE`` Adjusts the parametrisation used: ``MODE=1`` uses parameters from Ref. [1] and ``MODE=2`` uses parameters from Ref. [2] (default: ``MODE=1``)
* ``SCALE,S6`` Overall scaling parameter :math:`s_6` (see Eq. \eqref{eq:edisp}) and Refs. [2,3] for optimised values).
* ``ALPHA`` Damping function parameter (see Eq. \eqref{eq:fdamp}). Smaller values lead to larger corrections for intermediate distances.
* ``DAMP`` Choose damping function 'GRIMME' or 'CHAI' (default:'GRIMME'). With ``DAMP='CHAI``' the damping function by Chai and Head-Gordon can be activated that is used, e.g., in the wB97XD functional, see Ref.[5]
* ``A`` Parameter ``a`` in the damping function of Chai et al., see Ref. [5]
* ``GRAD`` Calculate gradient if ``GRAD>0``

In the DFT-D1 and DFT-D2 method the dispersion energy is calculated as
\begin{equation}\label{eq:edisp}
E_{\text{disp}}=-s_6\sum_{i,j<i}^{N_{\text{atoms}}}f_{\text{damp}}(R_{ij})

.. code-block:: text

                      \frac{C_6^{ij}}{R_{ij}^6}~.

\end{equation}
where :math:`N_{\text{atoms}}` is the total number of atoms, :math:`R_{ij}` is the interatomic distance of atoms :math:`i` and :math:`j`, :math:`s_6` is a global scaling parameter depending on the choice of the functional used and the :math:`C_6^{ij}` values are calculated from atomic dispersion coefficients :math:`C_6^i` and :math:`C_6^j` in the following way:

.. math::

   \begin{aligned}
   C_6^{ij}&=&2\frac{C_6^i C_6^j}{C_6^i + C_6^j} \qquad \text{(Ref.\ [1])}\\
   C_6^{ij}&=&\sqrt{C_6^i C_6^j} \qquad \text{(Ref.\ [2])}\end{aligned}

The function :math:`f_{\text{damp}}` damps the dispersion correction for shorter interatomic distances and is given by:
\begin{equation}\label{eq:fdamp}
f_{\text{damp}}(R_{ij})=\frac{1}{1+\exp{[-\alpha(R_{ij}/

.. code-block:: text

                  (R_{\text{vdW}}^i+R_{\text{vdW}}^j)-1)]}}

\end{equation}
with :math:`R_{\text{vdW}}^i` being the van-der-Waals radius for atom :math:`i` and :math:`\alpha` is a parameter that is usually set to 23 (Ref. [1]) or 20 (Ref. [2]).

Major changes in the D3 and D4 dispersion corrections compared to D2 are:

* The hybridisation states of the atoms are taken into account in the evaluation of the dispersion coefficients [3].
* The dispersion coefficients are dependent on local atomic charges obtained from a self-consistent tight-binding calculation [4]. Many-body interactions can be taken into account additionally.

Gradient contributions from the D3 and D4 dispersion correction are automatically computed in DFT geometry optimisations.

Note that not all functionals implemented in Molpro (and Libxc) are known to the D4 program (and vice versa). And in some cases the functionals supported by D4 might have a different identifier than used in Molpro. To see which functionals can be used with D4, see the documentation at `https://github.com/dftd4/dftd4 <https://github.com/dftd4/dftd4>`__. Most functionals supported by D4 can also be given by their Libxc names, for example
<code> ks,gga_x_b88,gga_c_p86,disp=d4 </code>
using the ``B88`` exchange and ``P86`` correlation functional names as defined in the Libxc library. For compound functionals like B+P86 it is important to *insert the exchange functional first and the correlation functional second*!

References:
:math:`[1]` S. Grimme, J. Comp. Chem. **25**, 1463 (2004).
:math:`[2]` S. Grimme, J. Comp. Chem. **27**, 1787 (2006).
:math:`[3]` S. Grimme, J. Antony, S. Ehrlich and H. Krieg, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3382344>`__ **132**, 154104 (2010)
:math:`[4]` E. Caldeweyher, C. Bannwarth, and S. Grimme `J. Chem. Phys. <https://dx.doi.org/10.1063/1.4993215>`__ **147**, 034112 (2017)
:math:`[5]` J.-D. Chai, M. Head-Gordon `Phys. Chem. Chem. Phys. <https://dx.doi.org/10.1039/b810189b>`__ **10**, 6615 (2008)

.. _the_density_functional_program--nonlocal-dft-nldft:

Nonlocal DFT (NLDFT)
~~~~~~~~~~~~~~~~~~~~

The deficiency of standard DFT functionals to describe long-range correlation energies (a.k.a. dispersion interactions) can be corrected through a double-Hirshfeld partitioning of the correlation functional energy density, using different weight functions :math:`w_A` and :math:`\widetilde{w}_A` for the local (:math:`A=B`) and nonlocal (:math:`A\ne B`) terms (:math:`A,B`: atom indices):

\begin{align}
E_{\text{c}}^{\text{NLDFT}}[\rho]=\sum_{A}^{N}\int d{\bf r}
\, w_{A}^{2}({\bf r})\, z(\rho,\nabla\rho,\dots)+2\sum_{A}^{N}
\sum_{B<A}^{N}\int d{\bf r}\,\widetilde{w}_{A}({\bf r})
\widetilde{w}_{B}({\bf r})\, z(\rho,\nabla\rho,\dots)\label{eq:EcNLDFT}
\end{align}

The Hirshfeld weights :math:`w_A` of the local part of the correlation functional (first term on the rhs in Eq. \eqref{eq:EcNLDFT} are determined by using analytical expressions for the atomic densities (:math:`\rho_A`) using Slaters rules. In contrast to this, the weights for the nonlocal part of the correlation energy (second term on the rhs in Eq. \eqref{eq:EcNLDFT} are determined by modified atomic densities using

\begin{align}
\widetilde{\rho}_{A}({\bf r}) & = & \mathcal{N}\left(\rho_{A}({\bf r})+

.. code-block:: text

      f(r,p_{1},p_{2})\frac{p_{3}}{r^{6}}\right)\nonumber \\
    & = & \mathcal{N}\left(\rho_{A}({\bf r})+\Big(\frac{1}{2}
     \Big[\mathrm{erf}(p_{1}(r+p_{2}))+\mathrm{erf}(p_{1}(r-p_{2}))\Big]\Big)^{6}
     \frac{p_{3}}{r^{6}}\right)\label{eq:RhoTilde}

\end{align}

with :math:`\mathcal{N}`: normalisation constant, :math:`r`: distance from nucleus and :math:`p_1,p_2,p_3`: parameters (see Ref. [1] for details). Due to the :math:`1/r^{6}` long-range tail of the modified densities :math:`\widetilde{\rho}_{A}`, the atom-atom contribution to :math:`E_{\text{c}}^{\text{NLDFT}}` in Eq. \eqref{eq:EcNLDFT} adapts to the correct long-range behaviour of the correlation energy so that the NLDFT functional, unlike standard DFT functionals, can describe dispersion interactions, see Ref. [1]. Note that compared to the explicit damped dispersion corrections described in section `empirical damped dispersion correction <the_density_functional_program.html#empirical-damped-dispersion-correction>`__ the NLDFT functional of Eq. \eqref{eq:EcNLDFT} also describes changes in the exchange-correlation potential due to the modification of the correlation energy density.

Since the densities :math:`\widetilde{\rho}_{A}` defined in Eq. \eqref{eq:RhoTilde} contain atomic parameters, calculations with the NLDFT functionals should be carried out only for systems containing atoms which were already parametrised, namely H, C, N, O, F, Si, P, S and Cl, see table 1 in Ref. [1]. Moreover, the NLDFT functional should (and can) only be used in conjunction with the PBE correlation functional. For the exchange functional part, the revised PBE exchange functional (with :math:`\kappa=0.9`) from Ref. [1] should be used. NLDFT calculations can then be done by adding the keyword ``nldft`` to the input for the Kohn-Sham calculation:

.. code-block:: text

      ks,pbec,revpbex; nldft

Note in this case that it is important to name the ``pbec`` functional first in the list of functionals. This is necessary, because the xc potential contributions from various functionals are accumulated during the construction of the xc matrix while the NLDFT double-Hirshfeld decomposition is to be done for the correlation energy functional only, see Eq. \eqref{eq:EcNLDFT}.

At the end of a NLDFT calculation the atom-atom decomposition of the correlation energy as well as the sum of the local and nonlocal correlation energy terms are printed. Furthermore, the sum of atom-atom contributions for which :math:`R_{AB}<3.0` and :math:`R_{AB}<6.0` bohr are displayed.

All publications resulting from the use of this method should acknowledge Ref. [1] which describes the functional and analyses its performance for a wide range of different benchmark data bases. In addition, Ref. [2], which shows the performance of the NLDFT functional for describing the binding energies of large supramolecular complexes, may be cited. The performance of the NLDFT functional for geometry optimisations is investigated in Ref. [3].

References:

:math:`[1]` A. Heßelmann, `J. Chem. Theory Comput. <https://dx.doi.org/10.1021/ct300735g>`__ **9**, 273 (2013)
:math:`[2]` A. Heßelmann and T. Korona, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.4893990>`__ **141**, 094107 (2014)
:math:`[3]` A. Heßelmann, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.5032175>`__ **149**, 044103 (2018)

.. _the_density_functional_program--fractional-orbital-occupation-calculations:

Fractional orbital occupation calculations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Spin-unrestricted UHF or UKS calculations, as well as RPA calculations, can be done with fractional orbital occupation numbers. In particular, this allows one to perform calculations with fractional electron numbers, useful for example for analysing approximations (see Ref. [1]).

Occupation numbers can be given separately for alpha and beta orbitals, respectively, by using the following commands *before* calling the ``uhf`` or ``uks`` program:

``FRACOCCA,<orbital_index>,<occupation_number>``

``FRACOCCB,<orbital_index>,<occupation_number>``

where ``orbital_index`` is the index of the orbital in the order used for constructing the density matrix, and ``occupation_number`` is the occupation number of this orbital between 0 and 1. These commands can be repeated in case of several fractionally occupied orbitals. When specifying the charge and the wave function, all fractionally occupied orbitals must be considered as occupied orbitals.

For DFT calculations, the implementation has only been done for the option ``matrix=0`` in the ``uks`` command. Furthermore, the option ``old`` must be added to the ``uks`` command in order to redirect Molpro to the old unrestricted SCF program (the setting of fractional occupations is not available in the new SCF code).

Example of a PBE calculation on the fractional C cation with 5.3 electrons:

.. code-block:: text

   symmetry,nosym
   geom={C}
   fracocca,4,0.3
   {uks,pbe,matrix=0,old; wf,6,0,2}

Example of a RSH calculation on the fractional CO anion with 14.8 electrons:

.. code-block:: text

   symmetry,nosym
   angstrom
   geom={
   2
   
   C 0 0 0
   O 0 0 1.128}
   set,charge=-1
   fracocca,8,0.8
   {int;erf,0.5}
   {uks,ecerfpbe,exerfpbe,matrix=0,old; rangehybrid;wf,15,0,1}

Example of a HF calculation on the H atom with 0.5 alpha electron and 0.5 beta electron:

.. code-block:: text

   symmetry,nosym
   geom={H}
   set,charge=-1
   fracocca,1,.5
   fracoccb,1,.5
   {uhf,old; wf,2,0,0}

Subsequent RPA correlation calculations (see `here <kohn-sham_random-phase_approximation.html#random-phase-approximation-rpatddft-program>`__) will be automatically done with fractional orbital occupation numbers.

References
:math:`[1]` B. Mussard, J. Toulouse, `Mol. Phys. <https://doi.org/10.1080/00268976.2016.1213910>`__, **115**, 161 (2017).

.. _the_density_functional_program--examples:

Examples
~~~~~~~~

The following shows the use of both non-self-consistent and self-consistent DFT.

.. code-block:: text
   :caption: examples/cndft.inp

   geometry={c;n,c,r}
   r=1.1 angstrom
   dfunc,b-lyp
   rhf;method(1)=program
   dft;edf(1)=dftfun
   uhf;method(2)=program
   dft;edf(2)=dftfun
   uks;method(3)=program,edf(3)=dftfun
   dft;method(4)=program,edf(4)=dftfun
   table,dftname,dftfuns
   table,method,edf
