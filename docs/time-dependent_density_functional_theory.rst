.. _time-dependent_density_functional_theory--time-dependent-density-functional-theory:

Time-dependent density functional theory
========================================

Excitation energies and linear response properties can be calculated utilising the time-dependent density functional theory (TDDFT) method. The program should normally be called after a Kohn-Sham or Hartree-Fock calculation because it looks for the most recent orbital dump record to read in the MO coefficients and orbital energies. Further settings like the functional type and quadrature grid are then adopted from the previous ground-state calculation, yet some may also be modified via input commands in the TDDFT program. Detailed descriptions for the different calculation modes are given in the following subsections.

.. _time-dependent_density_functional_theory--tddft-program:

TDDFT program
=============

Assuming that the molecule has :math:`C_{2v}` symmetry, a typical input for calculating the 6 lowest roots of the Hessian for IRREp 1 and 3, respectively, reads

.. code-block:: text

    ks,<func>
    tddft,states=[-6.1,-6.3]

The type of the xc kernel is usually adjusted automatically using the parameters from the previous ground-state KS calculation. However, various user inputs are available to change this, see below. Currently,  density functionals of the (hybrid) LDA or GGA type as well as range-separated LDA/GGA functionals are supported in TDDFT. Note, however, that currently unsupported meta GGA’s (or special xc potentials for which
the kernel can not (easily) be derived) may be combined with existing adiabatic LDA (ALDA) xc kernels.

Excitation energies for spin-unrestricted wave functions can be computed, too, using, e.g.

.. code-block:: text

    uhf
    tddft,states=[...]

for time-dependent Hartree-Fock (TDHF) or

.. code-block:: text

    uks,<func>
    tddft,states=[...]

for time-dependent DFT.

The program can be run in various integral transformation modes using

.. code-block:: text

     tddft,inttype=<ityp>

with ``ityp=[ao|mo|mo(df)|df]``. With ``ityp=ao`` (set as the default) an MO-AO transformation of the excitation vectors is performed. This requires the 4-indexed Coulomb repulsion integrals in the AO basis to be
stored on disk. ``ityp=mo`` means that a full 4-index MO transformation to the Coulomb and exchange operators (2-external MO integrals) is performed. These are then used to build the Hessian-vector products
in each TDDFT Davidson iteration step. While this option is faster than ``ityp=ao`` it requires a larger amount of disk space available.

While both, ``ityp=ao`` and ``ityp=mo`` require the storage of the 4-indexed AO integrals on disk, it is also possible to avoid this using density-fitting

.. code-block:: text

     df-tddft,...

in which case only 3-indexed integrals are used to compute the Hessian-vector products. While this requires an additional auxiliary basis set to be defined, the program can usually detect the fitting basis
set that corresponds to the given orbital basis automatically, so that normally no additional information needs to be passed to the program. If a special fitting basis set shall be used one can add

.. code-block:: text

     df-tddft,basis=<auxbas>...

with ``auxbas`` corresponding to a basis set keyword that was defined in the ``basis`` section.

Note that density-fitting can also be used in conjunction with ``inttype=mo`` in which case the Coulomb and exchange integrals are computed using density-fitting, thus avoiding the storage of the 4-indexed AO
integrals.

The following list summarises the keywords available in the TDDFT program:

* ``STATES`` A list which supplies the number of excitations to be calculated per IRREp: [N\ :math:`_1`.IRREP\ :math:`_1`,N\ :math:`_2`.IRREP\ :math:`_2`,\ :math:`\dots`]
* ``BASIS`` Sets the auxiliary basis set if ``MODE``\ =1,\ ``DFIT=.true.``
* ``FXKS`` Factor that determines the amount of the ALDA exchange (Slater-Dirac) kernel (if ``XCMODE``\ :math:`\le 10`).
* ``FCKS`` Factor that determines the amount of the ALDA correlation (VWN5) kernel (if ``XCMODE``\ :math:`\le 10`).
* ``FXHF`` Factor that determines the amount of exact Hartree-Fock exchange.
* ``XCKERNEL`` XC kernel type which can take the settings: ``XCKERNEL=[lda|gga|lda(df)|gga(df)]``. Concerning ``lda(df)|gga(df)``, see ``FITFXC`` option below.
* ``XCMODE`` Sets the type of exchange-correlation kernel routines to be used in the Hessian-vector transformations. ``XCMODE``\ =1-10 :math:`\rightarrow` reserved for ALDA kernels, ``XCMODE``\ =11-20 :math:`\rightarrow` reserved for GGA kernels. (normally not required)
* ``TRIPLET`` Set to :math:`\ne 0` if triplet excitations instead of singlet excitations shall be computed.
* ``CORE`` Set the number of core orbitals.
* ``TOLORB`` Threshold for orbital screening (default: :math:`1e-5`).
* ``NBLOCK`` Block size of numerical quadrature batches used in xc kernel integrations.
* ``FITFXC`` Compute the xc kernel contribution to the Hessian via density-fitting in df-tddft calculations. With ``FITFXC``\ =\ :math:`1` the xc kernel integrals in the auxiliary basis are computed in advance and then are simply loaded during the DF-construction of the Hessian-vector products, which is usually the fastest option. With ``FITFXC``\ =\ :math:`2` the xc contribution to the Hessian is fitted  via a contraction with the density fitting coefficients during the Davidson iterations. (default: ``FITFXC``\ =\ :math:`0`)
* ``SING`` Use a singularity correction to fix the potentially singular auxiliary integrals over the xc kernel, see `https://doi.org/10.1063/1.4893990 <https://doi.org/10.1063/1.4893990>`__. (default: ``SING``\ =1)
* ``ESHIFT`` Parameter for singularity correction in FXCFIT case (see `https://doi.org/10.1063/1.4893990 <https://doi.org/10.1063/1.4893990>`__. default::math:`1d-5`).
* ``FSCAL`` Parameter for singularity correction in FXCFIT case (see `https://doi.org/10.1063/1.4893990 <https://doi.org/10.1063/1.4893990>`__. default::math:`1d-4`).
* ``THRRHODUM`` Skip quadrature points around dummy centres if the density is lower than the given threshold when ``FITFXC``\ :math:`>0` is used. (default: ``THRRHODUM``\ =0d0)
* ``FIT1MOD`` Switch between dfit (0) and ri technique (1) for ``FITFXC``\ :math:`=1` case. (default: ``FIT1MOD``\ =\ :math:`1`).
* ``COULGRID`` If :math:`>0` compute the Coulomb kernel contribution via numerical quadrature rather than calculating the Coulomb integrals explicitly. Note: this option is not available with all settings and is normally only used in conjunction with range-separated density functionals in which case the full-range Coulomb integrals are not available on disk (``INTTYPE``\ =\ :math:`0,1` case). (default: ``COULGRID``\ =\ :math:`0`)
* ``TRIPLET`` Compute triplet excitation energies instead of singlet excitations (note: singlet and triplet excitations are obtained both simultaneously in case of unrestricted calculations, so the option only makes sense for the closed-shell case) (default: ``TRIPLET``\ =\ :math:`0`).
* ``FXCOP`` Calculate the 4-indexed Fxc operator integrals if ``inttype=mo(df)`` (default: ``FXCOP``\ =\ :math:`0`)
* ``FULLDIAG`` Perform a full diagonalisation of the Hessian if ``inttype=mo(df)`` (default: ``FULLDIAG``\ =\ :math:`0`)
* ``DIAGNOST`` Print the :math:`\Lambda` values from Tozers diagnostic test in the summary table, see `https://doi.org/10.1063/1.2831900 <https://doi.org/10.1063/1.2831900>`__ for details. This can help to identify local vs. Rydberg vs. nonlocal charge-transfer excitations. (default: ``DIAGNOST``\ =\ :math:`0`)
* ``PRINTSTEP`` If symmetry is used, print a summary table including the excitation energies for each IRREp. (default: ``PRINTSTEP``\ =0)
* ``NCOEFFPRI`` Number of excitation vector coefficients to be printed in the summary table (default: ``NCOEFFPRI``\ =\ :math:`4`)
* 

.. code-block:: text

Parameters which influence the behaviour of the Davidson solvers that can be used (should normally only be modified if convergence is hampered for some reason):

* ``MAXITDAV:MAXIT`` Maximum number of iterations (default: :math:`50`).
* ``DEGTHR:THRDEG`` Threshold to test degenerate states. If, via the number of states requested, one 'cuts' through a degeneracy (as is tested through the orbital energy differences) the program adds further states to be computed in order to improve/enable convergency (default: :math:`1d-5`).
* ``DAVMOD`` Davidson solver mode that can have values 1-5. Default: ``DAVMOD``\ =5 (recommended).
* ``MAXVEC`` Maximum number of expansion vectors in the eigensolver procedure.
* ``STARTVEC`` Number of start unit vectors (default: ``STARTVEC``\ ="0", meaning that the program usually sets the number of vectors to ``NSTATES`` at the beginning).
* ``THRE`` Energy threshold value. Default: ``THRE``\ =1d-6.
* ``THRV`` Residual threshold value (Euclidean norm of V). Default: ``THRV``\ =1d-4.
* ``THRS`` Threshold for smallest eigenvalue of S (``DAVMOD``\ =5, default: ``THRS``\ =1d-6).
* ``THRS_UPDATE`` Threshold for smallest eigenvalue of S of update vectors (``DAVMOD``\ =5, default: ``THRS``\ =1d-4).
* ``THRD`` Threshold for norm of expansion vectors (``DAVMOD``\ =5, default: ``THRS``\ =-1d0).
* ``THRQ`` If the norm of a new computed expansion vector is smaller than this value, it will be discarded in the iterative update of the vector space (for ``DAVMOD``\ =1,2). Default: ``THRR``\ =1d-2.
* ``USYM`` If ``DAVMOD``\ =1,2 either compute a symmetrised subspace Hessian (``USYM``\ =0) or not (``USYM``\ =1). Default: ``USYM``\ =0.
* ``DEFL`` Perform deflation step in the Davidson solver (``DAVMOD``\ =1,2). Default: ``DEFL``\ =1.
* ``SHIFT`` Denominator shift (``DAVMOD``\ =5, default: ``SHIFT``\ =0d0).
* ``PROJECT`` If true, project new vectors against old ones ``DAVMOD``\ =5, default: ``PROJECT``\ =1).
* ``CHECK`` If :math:`>0` print energy checks at the end (``DAVMOD``\ =5, default: ``CHECK``\ =0).
* ``REPLACE_DIAG`` If true, use exact hessian diag for lowest vectors (``DAVMOD``\ =5, default: ``REPLACE_DIAG``\ =0).
* ``SOLVER_MODE`` If 0, compute hred directly; if 1, hred=bred\*ared (``DAVMOD``\ =5, default: ``SOLVER_MODE``\ =-1).
* 

A number of options from the list above can be given separately in the TDDFT command group, e.g.:

.. code-block:: text

    {tddft,...; core,...; fxks,...}

Some of them are exclusive, namely:

* ``STABIL`` Perform a stability analysis of the SCF wave function (computes the lowest eigenvalue of the electronic Hessian :math:`{\bf A}+{\bf B}`).
* ``SAVE`` Save the excitation vectors to a record for, e.g., restarting another TDDFT calculation from these
* ``READ`` Read excitation vectors from a record and use these as the initial start vectors (it goes without saying that the dimensions etc. should match exactly those of the current calculation)
* ``NVIR`` Truncate the number of virtual orbitals (only possible with ``inttype=mo(df)``)
* ``NCOREX`` Specify the number of core orbitals set exclusively for the exchange contribution to the Hessian, ie., this setting enables to use different sizes for the core for the Coulomb and the exchange contributions.

Default values for all parameters may also be looked up in the ``tddft.registry`` file.

.. _time-dependent_density_functional_theory--analysing-the-spectrum:

Analysing the spectrum
======================

By default, Molpro prints oscillator strengths and the transition moments corresponding to the excitations computed at the end of the calculation in a summary table.
Using

.. code-block:: text

   tddft,...; gnuplot,<spec.gp>

where ``spec.gp`` is a generic file name, the spectrum can be exported to a file which can be loaded with `Gnuplot <http://www.gnuplot.info>`__.
For example, for the water molecule (PBE0 functional) the resulting plot for the absorption spectrum is `h2o-spectrum.pdf <media/h2o-spectrum.pdf>`__.
Note that the shape of the plot can be adapted by modifying the value of sigma in ``'spec.gp`` which denotes the standard deviation in units of 1 nm\ :math:`^{-1}`
for the Gaussian approximations for the respective transitions.

The excitation vectors can be exported to formats for visualisation by using either

.. code-block:: text

   tddft,...; molden,<vecs.mold>

which exports the excitation densities to a file which can be read with the program `Molden <https://www3.cmbi.umcn.nl/molden>`__ (vectors are stored as MO
coefficients, so can be visualised using the orbital selection interface of Molden) or, alternatively, via

.. code-block:: text

   tddft,...; cube,<vecs.cube>

in which case for each excitation a Gaussian cube file is created which can be visualised with various external programs, e.g.,  `JMol <http://jmol.sourceforge.net>`__. Note that these two options currently are implemented only for closed-shell restricted calculations.

For 'large' molecules one should be aware of the fact the TDDFT excitations can be strongly shifted compared to the experiment due to the charge transfer
problem (see, e.g., `https://doi.org/10.1103/PhysRevA.80.012507 <https://doi.org/10.1103/PhysRevA.80.012507>`__). It is strongly recommended to use hybrid or (much better) range-separated density functionals
to obtain reliable results for the transition energies for such systems. Note that the failure for Rydberg excitations for standard DFT methods can be
resolved using asymptotically corrected xc potentials, see section `Asymptotic correction for xc-potentials(ASYMP) <the_density_functional_program.html#asymptotic-correction-for-xc-potentials-asymp>`__
and the paper by Handy and Tozer `http://dx.doi.org/10.1063/1.477711 <http://dx.doi.org/10.1063/1.477711>`__ for more details.

In order to be able to distinguish between the different types of excitations, apart from the plotting options described above, one can print the
values of :math:`\Lambda` described in the paper by Peach, Benfield, Helgaker and Tozer `https://doi.org/10.1063/1.2831900 <https://doi.org/10.1063/1.2831900>`__:

.. code-block:: text

    tddft,diagnost=1,...

The values are defined as
.. math::

   \Lambda=\frac{\sum_{ia}\kappa_{ia}O_{ia}}{\sum_{ia} \kappa_{ia}}

with
.. math::

   O_{ia}=\langle|\phi_i||\phi_a|\rangle=\int d{\bf r} |\phi_i({\bf r})||\phi_a({\bf r})|

where :math:`\kappa_{ia}` is a coefficient of the excitation vector and :math:`O_{ia}` corresponds to the spatial overlap between an occupied orbital :math:`\phi_i` and an unoccupied orbital :math:`\phi_a`,
see `https://doi.org/10.1063/1.2831900 <https://doi.org/10.1063/1.2831900>`__ for more details. Note that the value of :math:`\Lambda` can depend on both the functional type as well as the basis set. As a rule of thumb, values of :math:`\Lambda<0.3` obtained with the B3LYP functional indicate a strongly nonlocal character (the smaller the more nonlocal)

.. _time-dependent_density_functional_theory--response-properties-from-the-coupled-perturbed-kohn-sham-method:

Response properties from the coupled perturbed Kohn-Sham method =
=================================================================

The linear response to (frequency-dependent) perturbations can be calculated with the TDDFT program using
(use ``states=[]`` explicitly in order to skip the calculation of excitation energies):

.. code-block:: text

    tddft,states=[],...; prop,<op1>,<op2>,...; om,<om1>,<om2>,...

where ``<op>`` can be any operator given in the section
`One-electron operators and expectation values (GEXPEC) <program_control.html#one-electron-operators-and-expectation-values-gexpec>`__.
A list of frequencies (:math:`\omega`) can be specified by ``om,...`` where positive values denote real frequencies while in case of negative values
the response to perturbations oscillating at imaginary frequencies is calculated. Real and imaginary input values can be mixed
arbitrarily. If static response properties are requested, too, the value of ``om=0.0`` should be inserted at the beginning of the
list (note that if the list of :math:`\omega`'s is omitted in the input, the static response is calculated by default).

For the calculation of multipole-multipole polarisabilities it is possible to use the short-hand input variant

.. code-block:: text

    tddft,states=[],...; prop,q1,q2,q3

in which case all :math:`l=1,2,3` rank responses (dipole, quadrupole and octopole) are computed without having to
insert all individual cartesian components. If all components for a given rank are given, the program performs
a transformation to the corresponding spherical harmonics representation and prints the results in the output
as well.

.. _time-dependent_density_functional_theory--dispersion-coefficients:

Dispersion coefficients
=======================

Dispersion coefficients can be calculated using

.. code-block:: text

     tddft,states=[],...; prop,...; disp,<nfreq>

where ``nfreq`` denotes the number of quadrature points for the numerical calculation of the
integral over imaginary frequencies with the Casimir-Polder integral transform. Normally, values
of the order of ``nfreq``\ =\ :math:`10` are sufficient for accurate integrations. The Gauss-Legendre
quadrature scheme as described in the paper by `Amos et al. <https://doi.org/10.1021/j100257a010>`__
is used in the response program.

The isotropic leading order :math:`C_6` dispersion coefficient between two monomers :math:`A` and :math:`B` is given
by
.. math::

   C_6^{AB} = \frac{3}{\pi}\int_0^\infty d{\omega}~\alpha^A(i\omega)\alpha^B(i\omega)

with :math:`\alpha^A` and :math:`\alpha^B` denoting the isotropic dipole-dipole polarisabilities
of the two monomers. The :math:`C_6` coefficients are computed automatically if ``prop,q1``
is used. Higher order coefficients :math:`C_8` and :math:`C_{10}` can be computed as well
if quadrupole-quadrupole and dipole-octopole polarisabilities are available (``prop,q1,q2`` or ``prop,q1,q2,q3``).
Note that the :math:`C_{10}` coefficients are computed even if no octopole moments are given in the input file.
The values then contain only the quadrupole-quadrupole :math:`\times` quadrupole-quadrupole polarisability
contributions.

For obtaining accurate results: use asymptotically corrected xc potentials 'and' basis sets
with 'enough' diffuse functions!

The following options can be set in the TDDFT response program:

* ``LESOLVE`` In case of unsymmetric Hessians (hybrid or range-separated functionals) one can choose between two different linear solvers (default: ``LESOLVE``\ =\ :math:`1`). Otherwise, a standard conjugate gradient solver is used to solve the response equations.
* ``THRCG`` Convergence threshold value for the (conjugate gradient) solver (default: ``THRCG``\ =\ :math:`1d-8`)

.. _time-dependent_density_functional_theory--rotatory-strengths:

Rotatory strengths
==================

Rotatory strengths for the excitations requested can be calculated with

.. code-block:: text

   {tddft,states=...,cdspec=1,...}

These can be used to simulate CD spectra for optically active molecules. Since the conventional length representation of the underlying transition moments is not gauge-invariant (and so can strongly deviate from the cbs result for small basis sets), also the velocity representation for the electric transition dipole moments are computed and printed in the output, see, e.g., works by Autschbach *et al.* `https://doi.org/10.1063/1.1436466 <https://doi.org/10.1063/1.1436466>`__.

Rotatory strenghths can be currently computed only for the spin-restricted TDDFT case.

.. _time-dependent_density_functional_theory--excited-state-gradient-calculations:

Excited state gradient calculations =
-------------------------------------

For performing TDDFT gradient calculations and geometry optimisations for excited states the value of the
``grad parameter needs to be set to 1 (>0) in the tddft command:``

.. code-block:: text

       tddft,grad=1,....

Currently this is possible for closed-shell singlet excited states using LDA, GGA, hybrid-GGA or range-separated hybrid functionals.

In TDDFT gradient calculations it is recommended to set tighter thresholds for the convergence of the excited state vectors
and for the iterative solution of the Z-vector equation. E.g., for small systems the following settings
would be reasonable:

.. code-block:: text

       tddft,grad=1,thrv=1d-8,thrcg=1d-12,....

while for larger systems the threshold values may be set larger but should normally be more tight compared
to conventional TDDFT energy calculations, see above.
The TDDFT program then computes the excited state density matrix as well as the excited state contribution to
the overlap lagrangian and writes these to internal records for later use.
The gradient can then be computed with the force program, see chapter :doc:`Energy gradients <energy_gradients>` for more details:

.. code-block:: text

       tddft,grad=1,....
       force

and geometry optimisations can be done with the :doc:`optg <geometry_optimization_optg>` command:

.. code-block:: text

       tddft,grad=1,....
       optg

Note that by default the gradient is computed for the lowest excitation of a given symmetry
(calculations for multiple symmetries are not allowed for gradient calculations). This can be
changed by setting the parameter ``gradvec``, e.g.

.. code-block:: text

       tddft,grad=1,states=[-4.2],gradvec=4,....

will compute the gradient for the 4th excited state of the second symmetry. It is necessary, of course, that the number
of states requested by the ``states`` command  is equal to or larger than ``gradvec``. Note that
an eigenvector-following method like is implemented in the EOM-CCSD program is not yet available for
TDDFT geometry optimisations. Because of this it might happen that the initial
starting guess is not followed strictly when there are crossings with other close excitations on
the PES. This will be improved in a future version of the program.

There are a few special parameters which can influence the behaviour of tddft gradient calculations. Most of them are
for debugging purpose and should normally not changed compared to their default values set in the registry file.

* ``GRADEXC`` If set to ``GRADEXC``\ =0 the ground-state DFT gradient contribution for the xc energy are computed with the standard DFT routines. When set to ``GRADEXC``\ =1 both the xc energy and kernel gradient contributions are computed simultaneously in a separate routine.
* ``GRADPRI`` Print the gradient at various stages in the program if set >0.
* ``DENSVD`` Use singular value decomposed density matrices in some AO based xc routines.
* ``DFGRADMODE`` Switch between different df-gradient modes for the calculation of the 2el-contribution to the tddft gradient.
* ``THRDDEC`` Threshold for singular value decompositions of AO-basis density matrices.
* ``MAXAUX`` Maximum number of auxiliary functions for transformed integral blocks in the density-fitting Fock routine.
* ``MAXBAT`` Maximum number of loop batches in df gradient routines.
* ``DISK`` Use disk (=1) or a global array (=0) to store half-transformed integrals in the density-fitting Fock routine. This setting will only be used during the calculation of the gradient terms.

.. _time-dependent_density_functional_theory--nonadiabatic-coupling-matrix-elements:

Nonadiabatic coupling matrix elements =
---------------------------------------

First order nonadiabatic coupling matrix elements (NACME's) between the ground state and an excited state can be computed using TDDFT response theory (and so can be obtained even when the wave functions of the respective states are not known explicitly). In general a NACME between two states :math:`n` and :math:`m` is given as
.. math::

   \tau^\xi_{nm}=\langle \Psi_n|\frac{\partial}{\partial \xi}|\Psi_m\rangle

where :math:`\xi` is a cartesian nuclear coordinate and :math:`\Psi_n` and :math:`\Psi_m` are the wave functions of the two states. In order to derive an expression for the first-order NACME from time-dependent response theory one considers the time evolution of the imaginary matrix element
.. math::

   C_\lambda^\xi(t)=\langle \Psi_\lambda(t)|\frac{\partial}{\partial\xi}|\Psi_\lambda(t)\rangle

under the influence of a monochromatic one-particle perturbation :math:`\hat{W}` and finds that the NACME is given by the residues of :math:`\overline{C}^{\xi(1)}` at the excitation energies :math:`\omega_n`
.. math::

   \tau_{0n}^\xi = \frac{2\pi i\mbox{Res}[\overline{C}^{\xi(1)}(\omega); \omega_n] }{\langle \Psi_0|\hat{\overline{W}}(\omega)|\Psi_n\rangle}

Following the work of Send and Furche `https://doi.org/10.1063/1.3292571 <https://doi.org/10.1063/1.3292571>`__ this term can be computed using TDDFT ground-state response theory, thus without knowledge of the excited state wave function. The resulting expression that was derived by Send and Furche includes Pulay type terms that greatly reduce the basis set dependence of the NACME's and that reduces to the exact Chernyak–Mukamel formula `https://doi.org/10.1063/1.480511 <https://doi.org/10.1063/1.480511>`__ for first-order NACMEs in the complete basis-set limit, see `https://doi.org/10.1063/1.3292571 <https://doi.org/10.1063/1.3292571>`__.

In Molpro, first-order NACME's can be computed with the TDDFT program by setting the logical-type option ``nacme=1`` (true), for example:

.. code-block:: text

   {tddft,states=[-4.1],nacme=1,nacmevec=2,...}

The option ``nacmevec`` can be used to set the state :math:`n` for which :math:`\tau_{0n}^\xi` shall be computed (otherwise NACME's for all states requested will be calculated). In the above example the four lowest excitations are computed and then the NACME :math:`\tau_{02}^\xi` is computed. Of course, ``nacmevec`` must be lower than or equal to the number of excitations requested.

First-order NACME's from TDDFT response theory have been implemented for closed and open-shell Hartree-Fock, LDA and GGA-type functionals.
