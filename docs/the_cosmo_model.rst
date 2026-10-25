.. _the_cosmo_model--the-cosmo-model:

The COSMO model
===============

The Conductor-like Screening Model (COSMO) (A. Klamt and G. Schüürmann, J. Chem. Soc. Perkin Trans. II 799-805 (1993)) is currently available for HF (``RHF,UHF``) and DFT (``RKS,UKS``) energy calculations and the corresponding gradients.

The COSMO model is invoked by the ``COSMO`` card:

``COSMO[,option$_1$=value$_1$, option$_2$=value$_2, \ldots$]``

where option can be

* ``NPPA`` size of the underlying basis grid. The value must satisfy: :math:`value = 10 \times 3^k \times 4^l +2` (default = 1082; type integer).
* ``NSPA`` number of segments for non hydrogen atoms. The value must satisfy: :math:`values = 10 \times 3^k \times 4^l +2` (default = 92; type integer).
* ``CAVITY`` the intersection seams of the molecular surface are closed (1) or open (0) (default = 1; type integer).
* ``EPSILON`` dielectric permittivity (default = -1.d0, which means :math:`\epsilon=\infty`; type real)
* ``DISEX`` distance criteria for the :math:`\bf A`-matrix setup. Short range interactions (segment centre distances :math:`<` DISEX :math:`\times` mean atomic diameter) are calculated using the underlying basis grid. Long range interactions are calculated via the segment centres (default = 10.d0; type float).
* ``ROUTF`` factor used for outer cavity construction. The radii of the outer cavity are defined as: :math:`r^{out}_i=r_i+ROUTF \times RSOLV` (default = 0.85d0; type float)
* ``PHSRAN`` phase offset of coordinate randomization (default = 0.d0; type float)
* ``AMPRAN`` amplitude factor of coordinate randomization (default = 1.0d-5; type float)
* ``RSOLV`` additional radius for cavity construction (default = -1d0, the optimized H radius is used; type float).
* ``MAXNPS`` maximal number of surface segments (default = -1, will be estimated; type integer).

It is recommended to change the default values for problematic cases only.

By default the program uses optimized radii if existent and 1.17\ :math:`\times`\ vdW radius else. The optimized radii [Å] are: H=1.30, C=2.00, N=1.83, O=1.72, F=1.72, S=2.16, Cl=2.05, Br=2.16, I=2.32. Own proposals can be given directly subsequent to the cosmo card:
``RAD,symbol, radius``

where the *radius* has to be given in Å.

Example:
``cosmo rad,O,1.72 rad,H,1.3   Output file:\\``
The COSMO output file will be written after every converged SCF calculation. The segment charges and potentials are corrected by the outlying charge correction. For the total charges and energies corrected and uncorrected values are given. The normal output file contains uncorrected values only. It is recommended to use the corrected values from the output file.

Optimizations:
It is recommended to use optimizer that operates with gradients exclusively. Line search techniques that use energies tends to fail, because of the energy discontinuities which may occur due to a reorganization of the segments after a geometry step. For the same reasons numerical gradients are not recommended.

.. _the_cosmo_model--basic-theory:

BASIC THEORY
============

COSMO is a continuum solvation model, in which the solvent is represented as a dielectric continuum of permittivity :math:`\epsilon`. The solute molecule is placed in a cavity inside the continuum. The response of the continuum due to the charge distribution of the solute is described by the generation of a screening charge distribution on the cavity surface. This charge distribution can be calculated by solving the boundary equation of vanishing electrostatic potential on the surface of a conductor. After a discretization of the cavity surface into sufficiently small segments, the vector of the screening charges on the surface segments is

.. math::

   {\bf q^{*}} = -{\bf A^{-1}} \Phi

where :math:`\Phi` is the vector of the potential due to the solute charge distribution on the segments, and :math:`\bf A` is the interaction matrix of the screening charges on the segments. This solution is exact for an electric conductor. For finite dielectrics the true dielectric screening charges can be approximated very well by scaling the charge density of a conductor with :math:`f(\epsilon)`.

.. math::

   {\bf q} = f(\epsilon) {\bf q^{*}} ; \quad f(\epsilon) = (\epsilon - 1)/(\epsilon + 0.5)

In every SCF step the screening charges :math:`\bf q` have to be generated from the potential :math:`\Phi`, and then added to the Hamiltonian as external point charges. The total energy of the system is

.. math::

   E_{tot} = E_{0} + E_{diel}; \quad E_{diel} = \frac{1}{2} \Phi {\bf q}

where :math:`E_{0}` is the bare self-energy of the system and :math:`E_{diel}` the dielectric energy.
Cavity construction:
First a surface of mutually excluding spheres of radius :math:`R_i+rsolv` is constructed, where the :math:`R_i` are the radii of the atoms, defined as element specific radii and :math:`rsolv` is some radius representing a typical maximum curvature of a solvent molecular surface. :math:`rsolv` should not be misinterpreted as a mean solvent radius, nor modified for different solvents. Every atomic sphere is represented by an underlying basis grid of ``nppa`` points per full atom. Basis grid points which intersect a sphere of a different atom are neglected. In a second step the remainder of the basis grid points are projected to the surface defined by the radii :math:`R_i`. As a third step of the cavity construction the remaining basis grid points are gathered to segments, which are the areas of constant screening charges in the numerical solution. Finally, the intersection seams between the atoms are filled with additional segments.
Now the A-matrix can be set up. The matrix elements will be calculated from the basis grid points of the segments for close and medium segment distances (governed by the ``disex`` value), or using the segment centres for large segment distances.
Outlying charge correction:
The non vanishing electron density outside the cavity causes an error that can be corrected by the outlying charge correction. This correction uses the potential on the so called outer surface (defined by the radii :math:`R_i+\mbox{rsolv} \times \mbox{routf}`) to estimate a correction term for the screening charges and the energies (A. Klamt and V. Jonas, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.472829>`__ **105**, 9972-9981(1996)). The correction will be performed once at the end of a converged SCF calculation. All corrected values can be found in the COSMO output file.

Three example inputs can be found in `cosmo_water1.inp <media/examples/cosmo_water1.inp>`__, `cosmo_water2.inp <media/examples/cosmo_water2.inp>`__ and `cosmo_water3.inp <media/examples/cosmo_water3.inp>`__.
