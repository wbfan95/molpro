.. raw:: html

   <span id="calling-the-dma-program-dma"></span>

.. raw:: html

   <span id="calling-the-natural-bond-orbital-analysis-program-nbo"></span>

.. raw:: html

   <span id="calling-the-population-analysis-program-pop"></span>

.. raw:: html

   <span id="calling-the-property-program-property"></span>

.. raw:: html

   <span id="defining-the-density-matrix-density"></span>

.. raw:: html

   <span id="defining-the-radius-of-multipole-sites-radius"></span>

.. raw:: html

   <span id="dipole-fields-dip"></span>

.. raw:: html

   <span id="distributed-multipole-analysis"></span>

.. raw:: html

   <span id="general-fields-field"></span>

.. raw:: html

   <span id="intermolecular-interaction-energies"></span>

.. raw:: html

   <span id="linear-molecules-linear-general"></span>

.. raw:: html

   <span id="maximum-rank-of-multipoles-limit"></span>

.. raw:: html

   <span id="mulliken-population-analysis"></span>

.. raw:: html

   <span id="natural-bond-orbital-analysis"></span>

.. raw:: html

   <span id="omitting-nuclear-contributions-nonuclear"></span>

.. raw:: html

   <span id="orbital-analysis-orbital"></span>

.. raw:: html

   <span id="populations-of-basis-functions-individual"></span>

.. raw:: html

   <span id="printing-options"></span>

.. raw:: html

   <span id="quadrupole-fields-quad"></span>

.. raw:: html

   <span id="relativistic-corrections"></span>

.. raw:: html

   <span id="specification-of-multipole-sites-add-delete"></span>

.. _properties_and_expectation_values--properties-and-expectation-values:

Properties and expectation values
=================================

.. _properties_and_expectation_values--the-property-program:

The property program
====================

The property program allows the evaluation of one-electron operators and expectation values. Normally, the operators are computed automatically when using the global ``GEXPEC`` directive (see section `One-electron operators and expectation values (GEXPEC) <program_control.html#one-electron-operators-and-expectation-values-gexpec>`__) or the ``EXPEC`` or ``TRAN`` commands in the SCF, MCSCF, and CI programs. The explicit use of the property program is only necessary in the rare case that the user is interested in an orbital analysis of the properties.

.. _properties_and_expectation_values--calling-the-property-program-property:

Calling the property program (PROPERTY)
=======================================

``PROPERTY``

invokes the property program.

.. _properties_and_expectation_values--expectation-values-density:

Expectation values (DENSITY)
============================

``DENSITY [,record.file] [,specifications]``

If this card is present, the density matrix will be read from record  *record.file* and property expectation values will be calculated. If the specification *record.file* is omitted, the last dump record is used. Density matrices for specific states can be selected using *specifications*, as explained in section `selecting orbitals and density matrices (ORBITAL, DENSITY) <general_program_structure.html#selecting-orbitals-and-density-matrices-orbital-density>`__. Note that the density matrices are stored in the same record as the orbitals.

.. _properties_and_expectation_values--orbital-analysis-orbital:

Orbital analysis (ORBITAL)
==========================

``ORBITAL [,record.file]  [,specifications]``

If this card is present, the orbitals are read from record *record.file* and an orbital analysis of the expectation values is printed (the density matrix must also be provided!). If *record.file* is omitted, the last dump record is used. This is only meaningful for diagonal density matrices (SCF or natural orbitals). Natural orbitals for specific states can be selected using *specifications*, as explained in section `selecting orbitals and density matrices (ORBITAL, DENSITY) <general_program_structure.html#selecting-orbitals-and-density-matrices-orbital-density>`__.

.. _properties_and_expectation_values--specification-of-one-electron-operators:

Specification of one-electron operators
=======================================

The required operators are specified by code words. Optionally, the geometry or the nuclear centre at which the operator is computed can be specified.

For each operator, an input card of the following form is required:

*code,centre,x,y,z,,factor*

*code* specifies the property. The available operators are given in section `One-electron operators and expectation values (GEXPEC) <program_control.html#one-electron-operators-and-expectation-values-gexpec>`__.

The other parameters have the following meaning:

* ***centre*** row number of Z–matrix or atomic symbol defining the centre at which property shall be calculated; if  *centre*\ :math:`\ne 0` you need not read in coordinates.
* ***x,y,z*** cartesian coordinates of the point (only if *centre*\ =0).
* ***factor*** the operator is multiplied by this factor. The default is *factor*\ =1 except for ``REL``. In this cases proper factors for relativistic corrections are used unless *factor* is given. The two commas before factor are needed to preserve compatibility with ``Molpro96``.

.. _properties_and_expectation_values--printing-options:

Printing options
================

``PRINT,print``

This card is used to control output, mainly for debugging purposes.

* ***print*\ :math:`= 0`** no test output (default)
* ***print*\ :math:`> 0`** operators are printed.

.. _properties_and_expectation_values--examples:

Examples
========

The following example computes the dipole quadrupole moments of water and prints an orbital analysis. By default, the origin is at the centre of mass, and this is taken as origin for the quadrupole moments.

.. code-block:: text
   :caption: examples/h2o_property.inp

   ***,h2o properties
   geometry={o;h1,o,r;h2,o,r,h1,theta}   !Z-matrix geometry input
   r=1 ang                               !bond length
   theta=104                             !bond angle
   hf                                    !do scf calculation
   {property                             !call property program
   orbital                               !read scf orbitals
   density                               !read scf density matrix
   dm                                    !compute dipole moments and print orbital contributions
   qm}                                   !compute quadrupole moments and print orbital contributions
   {multi;wf;state,2;dm                  !do full-valence CASSCF
   natorb,state=1.1                      !compute natural orbitals for state 1.1
   natorb,state=2.1}                     !compute natural orbitals for state 2.1
   
   {property                             !call property program
   orbital,state=1.1                     !read casscf natural orbitals for state 1.1
   density,state=1.1                     !read casscf density matrix for state 1.1
   dm                                    !compute dipole moments and print orbital contributions
   qm}                                    !compute quadrupole moments and print orbital contributions
   
   {property                             !call property program
   orbital,state=2.1                     !read casscf natural orbitals for state 2.1
   density,state=2.1                     !read casscf density matrix for state 2.1
   dm                                    !compute dipole moments and print orbital contributions
   qm}                                   !compute quadrupole moments and print orbital contributions

Alternatively, the dipole and quadrupole moments can be computed directly in the SCF and MCSCF programs, but in this case no orbital contributions are printed:

.. code-block:: text
   :caption: examples/h2o_gexpec1.inp

   ***,h2o properties
   geometry={o;h1,o,r;h2,o,r,h1,theta}   !Z-matrix geometry input
   r=1 ang                               !bond length
   theta=104                             !bond angle
   gexpec,dm,qm                          !global request of dipole and quadrupole moments
   hf                                    !do scf calculation
   {multi;wf;state,2                     !do full-valence CASSCF
   natorb,state=1.1                      !compute natural orbitals for state 1.1
   natorb,state=2.1}                     !compute natural orbitals for state 2.1

There is a another example described in the `Program Control <program_control.html#example-for-computing-expectation-values>`__ section, as well as:

.. code-block:: text
   :caption: examples/h2o_prop.inp

   ***,H2O properties
   r=1.85                                            !define initial bond distance
   theta=104                                         !define initial bond angle (=2 theta)
   geometry={o;h1,o,r;h2,o,r,h1,theta}               !geometry input
   Basis={
   s,1,v;c,1.6;                                      !van Duijneveld 13s, first 6 contracted
   p,1,v;c,1.4;                                      !van Duijneveld 8p, first 4 contracted
   d,1,3d;f,1,2f                                     !Dunning optimized 3d, 2f
   s,2,v;c,1.4;p,2,3p}                               !8s3p basis for H
   
   gexpec,qm,ef1,ef2,fg,,0,0,0.5                     !Field gradient at (0,0,0.5)
   
   hf                                                !closed-shell SCF
   
   pop                                               !Mulliken population analysis using scf density
   
   {dma                                              !distributed multipole analysis using scf density
   limit,,3};                                        !limit to rank 3
   
   multi                                             !full valence CASSCF
   
   {pop;                                             !Mulliken population analysis using mcscf density
   individual}                                       !give occupations of individual basis functions
   
   {dma;                                             !distributed multipole analysis using mcscf density
   limit,,3}                                         !limit to rank 3
   
   {ci                                               !MRCI with casscf reference
   natorb,2350.2
   dm,2350.2}                                        !save MRCI density matrix on record 2350, file 2
   
   {pop;density,2350.2;                              !Mulliken population analysis using MRCI density
   individual}                                       !give occupations of individual basis functions
   
   {property;
   density,2350.2;                                   !use property program to compute expectation values
   orbital,2350.2;
   qm;ef,1;ef,2;fg,,,,0.5}                           !same operators as before
   ---

.. _properties_and_expectation_values--distributed-multipole-analysis:

Distributed multipole analysis
------------------------------

Any density matrix can be analysed using the distributed multipole analysis described by Stone, `Chem. Phys. Lett. <https://dx.doi.org/10.1016/0009-2614(81)85452-8>`__ **83**, 233 (1981). The multipole moments arising from the overlap of each pair of primitives are calculated with respect to the overlap centre, and then shifted to the nearest of a number of  *multipole sites*. By default these comprise all atoms specified in the integral input. However the list of multipole sites can be modified by deleting and/or adding sites, and also by restricting the rank of multipole which may be transferred to any given site. The atomic charges are stored in the ``MOLPRO`` variable ``ATCHARGE``. The i’th element in ``ATCHARGE`` corresponds to the i’th row of the Z-matrix input.

Options may appear in any order, except ``DENSITY``, which must be first if given.

The present version does not allow generally contracted AO basis sets.

.. _properties_and_expectation_values--calling-the-dma-program-dma:

Calling the DMA program (DMA)
=============================

``DMA;``

This command initializes the DMA program.

.. _properties_and_expectation_values--specifying-the-density-matrix-density:

Specifying the density matrix (DENSITY)
=======================================

``DENSITY,record.file [,specifications]``

The density matrix to be analysed is that found in record *record* on file *file*. If omitted, *record.file* defaults to current orbital record. If specified, ``DENSITY`` must appear first in the input. Density matrices for specific states can be selected using *specifications*, as explained in section `selecting orbitals and density matrices (ORBITAL, DENSITY) <general_program_structure.html#selecting-orbitals-and-density-matrices-orbital-density>`__.

.. _properties_and_expectation_values--linear-molecules-linear-general:

Linear molecules (LINEAR, GENERAL)
==================================

``GENERAL;``

(default) invokes the normal program, which copes with any geometry.

``LINEAR``

invokes a faster program which can be used when all the atoms are arranged parallel to the :math:`z`-axis and only the :math:`m=0` components of the multipoles are required.

.. _properties_and_expectation_values--maximum-rank-of-multipoles-limit:

Maximum rank of multipoles (LIMIT)
==================================

``LIMIT,name,lmax;``

*lmax* is the highest rank of multipole that is to be calculated by the program. Default (and maximum) is 10 for the general program and 20 for the linear one. If *name* is specified, the limit applies only to multipole site *name*.

.. _properties_and_expectation_values--omitting-nuclear-contributions-nonuclear:

Omitting nuclear contributions (NONUCLEAR)
==========================================

``NONUCLEAR``

The nuclear contributions to properties are not to be evaluated.

.. _properties_and_expectation_values--specification-of-multipole-sites-add-delete:

Specification of multipole sites (ADD, DELETE)
==============================================

``ADD,name,x,y,z,lmax,radius;``

Add a new site at (:math:`x`, :math:`y`, :math:`z`) with the *name* specified. The multipole rank is limited to *lmax* if a value is specified, otherwise the value of lmax specified by the ``LIMIT`` directive is used. No account is taken of symmetry; every site in a symmetry-equivalent set must be specified explicitly. The *radius* of the site may also be specified (default 1.0).

``DELETE,name``

Delete all atoms with the *name* given from consideration as a multipole site. Note that original atoms from the integral program have names :math:`1,2,3,\ldots` as printed in integral output. ``DELETE,ALL`` deletes all atoms and gives the multipoles with respect to the origin only.

.. _properties_and_expectation_values--defining-the-radius-of-multipole-sites-radius:

Defining the radius of multipole sites (RADIUS)
===============================================

``RADIUS,name,r;``

Assign radius :math:`r` to all sites with the *name* given. The program moves multipoles at an overlap centre :math:`P` to the site :math:`S` for which the value of :math:`|P-S|/r(S)` is smallest. In the absence of a ``RADIUS`` directive, all sites are given radius 1.

.. _properties_and_expectation_values--notes-and-references:

Notes and references
====================

The multipoles produced by this analysis are given in their spherical harmonic definitions. Explicit formulae for translating between the cartesian and spherical harmonic definitions of the multipole moments are given in, *Explicit formulae for the electrostatic energy, forces and torques between a pair of molecules of arbitrary symmetry*, S. L. Price, A. J. Stone, and M. Alderton, Molec. Phys., 52, 987 (1984).

For examples of the use of ``DMA`` analysis see, Price and Stone, `Chem. Phys. Lett. <https://dx.doi.org/10.1016/0009-2614(83)80079-7>`__ **98**, 419 (1983); Buckingham and Fowler, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.445721>`__ **79**, 6426 (1983).

.. _properties_and_expectation_values--examples-1:

Examples
========

The following input calculates SCF multipole moments for water.

.. code-block:: text
   :caption: examples/h2o_dma.inp

   ***,h2o distributed multipole analysis
   geometry={o;h1,o,r;h2,o,r,h1,theta}   !Z-matrix geometry input
   r=1 ang                               !bond length
   theta=104                             !bond angle
   basis=6-311g**
   hf                                    !do scf calculation
   {dma;limit,,4}                        !results for total multipoles are

.. _properties_and_expectation_values--mulliken-population-analysis:

Mulliken population analysis
----------------------------

.. _properties_and_expectation_values--calling-the-population-analysis-program-pop:

Calling the population analysis program (POP)
=============================================

``POP;``

Invokes Mulliken analysis program, which analyses any density matrix into its contributions from s,p,d,f... basis functions on each atom. In the case of Hartree-Fock, density functional, and MCSCF calculations, the density matrix is taken from the last dump record, unless overridden with the ``DENSITY`` card. For other methods, the density matrix has to be written and then must be referred to with the ``DENSITY`` card.

The subcommands may be abbreviated by the first four characters. The atomic charges are stored in the ``MOLPRO`` variable ``ATCHARGE``. The i’th element in ``ATCHARGE`` corresponds to the i’th row of the Z-matrix input.

.. _properties_and_expectation_values--defining-the-density-matrix-density:

Defining the density matrix (DENSITY)
=====================================

``DENSITY,record.file [,specifications]``

Take density matrix to be analysed from record *record* on file *file*. Density matrices for specific states can be selected using *specifications*, as explained in section `selecting orbitals and density matrices (ORBITAL, DENSITY) <general_program_structure.html#selecting-orbitals-and-density-matrices-orbital-density>`__. Note that the density matrices are stored in the same record as the orbitals.

.. _properties_and_expectation_values--populations-of-basis-functions-individual:

Populations of basis functions (INDIVIDUAL)
===========================================

``INDIVIDUAL;``

.. _properties_and_expectation_values--examples-2:

Examples
========

.. code-block:: text
   :caption: examples/h2o_pop.inp

   ***,h2o population analysis
   geometry={o;h1,o,r;h2,o,r,h1,theta}   !Z-matrix geometry input
   r=1 ang                               !bond length
   theta=104                             !bond angle
   basis=6-311g**
   hf                                    !do scf calculation
   pop;                                  !Mulliken population analysis using mcscf density
   individual                            !give occupations of individual basis functions

If specified, the Mulliken populations of each individual basis function are printed.

The following example shows how to compute the population first on the Hartree-Fock level, and then on the CI level.

.. code-block:: text
   :caption: examples/ch4_ci_pop.inp

   geomtyp=xyz;
   geometry={
   c            -1.058493    -0.384055     0.000000
   h            -1.058493     0.695337     0.000000
   h            -0.040825    -0.743829     0.000000
   h            -1.567327    -0.743829     0.881326
   h            -1.567327    -0.743829    -0.881326
   }
   basis={
   default=def2-SVP
   }
   hf;
   pop;
   ci;dm,9000.2;
   pop;density,9000.2

In the following example, the population for charge and spin is computed:

.. code-block:: text
   :caption: examples/li_pop.inp

   geometry={li}
   basis=vdz
   hf
   pop;
   pop;density,type=spin

.. _properties_and_expectation_values--natural-bond-orbital-analysis:

Natural Bond Orbital Analysis
-----------------------------

.. _properties_and_expectation_values--calling-the-natural-bond-orbital-analysis-program-nbo:

Calling the Natural Bond Orbital analysis program (NBO)
=======================================================

``NBO,[WITH_CORE=core_option],[LEVEL=level],[KEEP_WBI=wbi_option];``

The Natural Bond Orbital Analysis of Weinhold and coworkers (`J. Chem. Phys. <https://dx.doi.org/10.1063/1.449486>`__ **83**, 735 (1985), `J. Chem. Phys. <https://dx.doi.org/10.1063/1.449360>`__ **83**, 1736 (1985) and J. Chem. Phys. 78 (1983) 4066) can be called by the use of the ``NBO`` card. It reads from a density or orbital record, and performs the necessary transformations to Natural Atomic Orbitals (NAO), Natural Bond Orbitals (NBO) and Natural Localized Molecular Orbitals (NLMO). The latter can also be saved to a record and later used in local correlation treatments (cf. Section :doc:`PAO-based local correlation treatments <pao-based_local_correlation_treatments>`). By default, the full orbital space is used. The core orbitals can, however, be left out of the procedure if *core_option*\ =0.

One can choose to truncate the transformation series (e.g., only compute the NAO orbitals), with help of the ``LEVEL`` keyword. If *level*\ =1, only the NAO transformation will be carried out. For *level*\ =2 the NBO transformation is performed, and for 3 the NLMO (default).

Sometimes, the NBO procedure will not converge due to a bad ordering on the 2-center bond search. The first run is based on the Wiberg bond index, but the algorithm switches to the atom ordering on the subsequent runs. This can be avoided by the use of the option ``KEEP_WBI``. If *wbi_option*\ =1, the Wiberg bond index is used in all iterations.

.. _properties_and_expectation_values--saving-the-nlmo-orbitals-save:

Saving the NLMO orbitals (SAVE)
===============================

``SAVE,record.file;``

The NLMO orbitals are saved in the specified *record*, together with the NPA charges.

.. _properties_and_expectation_values--finite-field-calculations:

Finite field calculations
-------------------------

Dipole moments, quadrupole moments etc. and the corresponding polarizabilities can be obtained as energy derivatives by the finite difference approximation. This is most easily done with the ``DIP``, ``QUAD``, or ``FIELD`` commands, which add a specified amount of the dipole, quadrupole, or any general, operators to the Hamiltonian. An error will result if the added perturbation is not totally symmetric (symmetry 1). Note that the orbitals must be recomputed before performing a correlation calculation.

.. _properties_and_expectation_values--dipole-fields-dip:

Dipole fields (DIP)
===================

``DIP,dx,dy,dz;\\``
``DIP+,dx,dy,dz;``

Add a finite combination of the dipole operators :math:`\vec\mu=(\mu_x, \mu_y, \mu_z)`, :math:`H_1=\vec d \cdot \vec \mu` ( :math:`\vec d=(\textit{dx},\textit{dy},\textit{dz})`)  to the Hamiltonian (both the 1-electron operator and the core energy). ``DIP+`` adds to any existing field, otherwise any previous perturbation is removed.

The perturbed hamiltonian represents a physical system in a uniform electric field with electric field strength :math:`\vec F= -\vec d`. Therefore the corresponding energy-derivative form of the dipole moment projection in this direction can be obtained as

.. math::

   |\vec F|^{-1}\vec F \cdot \vec \mu  = |2\vec d|^{-1}(E(\vec d)-E(-\vec d)) + O(|\vec d|^2)= |\vec d|^{-1}(E(\vec d)-E(\vec 0)) + O(|\vec d|).

The diagonal polarisability in this direction can similarly be calculated via
.. math::

   \alpha_{\vec d, \vec d}  = - |\vec d|^{-2}(E(\vec d)+E(-\vec d)-2E(\vec 0)) + O(|\vec d|^2).

.. _properties_and_expectation_values--quadrupole-fields-quad:

Quadrupole fields (QUAD)
========================

``QUAD,qxx,qyy,qzz,qxy,qxz,qyz;\\``
``QUAD+,qxx,qyy,qzz,qxy,qxz,qyz;``

Exactly as the ``DIP`` command, but adds a combination of quadrupole operators to the Hamiltonian.

.. _properties_and_expectation_values--general-fields-field:

General fields (FIELD)
======================

``FIELD,oper1,fac1, oper2,fac2, …;\\``
``FIELD+,oper1,fac1, oper2,fac2, …;\\``

Adds one-electron operators *oper1*, *oper2*, …with the corresponding factors *fac1*, *fac2*, …to the one-electron hamiltonian. The available operators are given in section `One-electron operators and expectation values (GEXPEC) <program_control.html#one-electron-operators-and-expectation-values-gexpec>`__. An error will result if the added perturbation is not totally symmetric (symmetry 1).

``FIELD+`` adds to any existing field, otherwise any previous field is removed.

Note that ``FIELD`` does currently not modify core polarization potentials (CPP). If CPPs are present, only ``DIP`` and ``QUAD`` should be used.

.. _properties_and_expectation_values--examples-3:

Examples
========

The first examples shows various possibilities to add perturbations to the one-electron hamiltonian.

.. code-block:: text
   :caption: examples/field.inp

   ***,H2O finite fields
   R     =    0.96488518 ANG
   THETA =  101.90140469
   geometry={H1
             O,H1,R;
             H2,O,R,H1,THETA}
   {hf;wf,10,1}           !scf without field
   
   f=0.05
   
   dip,,,f                !add dipole (z) field to h0
   hf                     !do scf with modified h0
   
   field,dmz,f            !add dipole (z) field to H0
                          !same result as previous example
   hf                     !do scf with modified h0
   
   quad,,,f               !add quadrupole (qmzz) field to h0
   hf                     !do scf with modified h0
   
   field,qmzz,f           !add quadrupole (qmzz) field to h0;
                          !same result as previous example
   hf                     !do scf with modified h0
   
   field,zz,f,xx,-0.5*f,yy,-0.5*f
                          !add general field; same result as quad above
   hf                     !do scf with modified h0
   
   field,zz,f           !same as before with separate field commands
   field+,xx,-0.5*f
   field+,yy,-0.5*f
   hf                     !do scf with modified h0
   
   field                  !remove field
   hf                     !scf without field

The second example shows how to compute dipole moments and polarizabilities using finite fields.

.. code-block:: text
   :caption: examples/h2o_field.inp

   ***,H2O finite field calculations
   
   r=1.85,theta=104                   !set geometry parameters
   geometry={O;                       !z-matrix input
             H1,O,r;
             H2,O,r,H1,theta}
   basis=avtz                         !define default basis
   field=[0,0.005,-0.005]             !define finite field strengths
   $method=[hf,mp4,ccsd(t),casscf,mrci]
   
   k=0
   do i=1,#field                      !loop over fields
     dip,,,field(i)                   !add finite field to H
     do m=1,#method                   !loop over methods
       k=k+1
       $method(m)                     !calculate energy
       e(k)=energy                    !save energy
     enddo
   enddo
   
   k=0
   n=#method
   do m=1,#method
     k=k+1
     energ(m)=e(k)
     dipmz(m)=(e(k+n)-e(k+2*n))/(field(2)-field(3))   !dipole moment as first energy derivative
     dpolz(m)=(e(k+n)+e(k+2*n)-2*e(k))/((field(2)-field(1))*(field(3)-field(1)))  !polarizability as second der.
   enddo
   
   table,method,energ,dipmz,dpolz
   title,results for H2O, r=$R, theta=$theta, basis=$basis
   ---

.. _properties_and_expectation_values--derivatives-with-respect-to-fields-dipole-quadrupole-second-and-third-moments:

Derivatives with respect to fields (dipole, quadrupole, second and third moments)
---------------------------------------------------------------------------------

Derivatives with respect to fields can be computed with the keywords ``FGRAD`` (1st derivative) and ``FPOL`` (2nd derivative). The fields may be dipole (``DM``), quadrupole (``QM``), second (``SM``) and third (``TM``) moments, and also their individual components (e.g. ``DMX``, ``XZ``, ``QMXY``, ``XXX``).

Second derivatives include a minus sign, e.g.

.. math::

   -\frac{\partial^2 E}{\partial d_i \partial d_j}

where :math:`d_i` are the components of the dipole field.

The syntax for the first or second derivative with respect to a dipole field is like this:

``FGRAD,OPER=DM,PROC=myproc``
or
``FPOL,OPER=DM,PROC=myproc``

where ``myproc`` has to be defined.

By default a two-point formula is used for first derivatives (keyword ``CENTRAL``). Alternatively, a forward-difference formula ``FORWARD`` (fast, but inaccurate) or a fourpoint formula may be used ``FOURPOINT`` .

For second derivatives, central (1 central point + 2 more points for the diagonal part, 2\*2 points for the off-diagonal part) and four-point formulas (central point + 4 more points for the diagonal part, 4\*4 points for the off-diagonal part) are implemented. If available, analytical first gradients may be used with the keyword ``use_grad`` so that only the second derivative is done numerically. This may require the ``expec`` keyword to compute the analytical first derivative.

The default step size is 0.001 a.u. and may be changed with the option ``STRENGTH``.

The quadrupole tensor is traceless which is exploited by default in the case of first derivatives. It may be switched off with ``ZERO_TRACE_UNUSED``

The energy calculation has to be done with a ``PROCEDURE`` (alternatively, ``STARTCMD`` may also be used).

.. _properties_and_expectation_values--examples-4:

Examples
========

This example shows how dipole, quadrupole and third moments can be obtained by computing derivatives with respect to the corresponding fields, and the dipole polarizability.

.. code-block:: text
   :caption: examples/h2o2_fgrad_fpol.inp

   geometry={4
   H2O2
   O1      0.0000   0.7375  -0.0528
   O2      0.0000  -0.7375  -0.0528
   H3      0.8190   0.8170   0.4220
   H4     -0.8190  -0.8170   0.4220
   }
   
   basis=def2-svp
   {hf}
   {mp2;expec,dm,qm,tm}
   
   fgrad,dm,proc=myproc
   fgrad,qm,proc=myproc
   fgrad,tm,proc=myproc
   fpol,dm,proc=myproc
   
   proc myproc
   {hf}
   {mp2}
   endproc
   
   
   

``This example shows how use_grad may be used:``

.. code-block:: text
   :caption: examples/h2o_fpol_dm_use_grad_ccsd.inp

   geometry={   3
   H2O
   O          0.0000000000        0.0000000000       -0.0573384885
   H          0.7581330543        0.0000000000        0.5338192442
   H         -0.7581330543        0.0000000000        0.5338192442
   }
   
   basis=def2-svp
   {hf}
   
   !use first analytical derivative
   fpol,dm,proc=myproc,use_grad
   
   proc myproc
   {hf}
   {ccsd
   expec,dm}
   endproc
   
   
   !compare with twofold numerical derivative
   fpol,dm,proc=myproc

.. _properties_and_expectation_values--relativistic-corrections:

Relativistic corrections
------------------------

Relativistic corrections may be calculated within the Cowan-Griffin approach by computing expectation values of the mass-velocity and 1-electron Darwin integrals; these should be generated using the property integral program with keyword ``REL`` The expectation values can be computed within the SCF, MCSCF and CI programs in the usual way using the ``EXPEC`` command, again with the keyword ``REL``. The mass-velocity and Darwin terms, and their sum are subsequently available through the Molpro variables ``MASSV``, ``DARWIN`` and ``EREL`` respectively. An example can be found `here <program_control.html#example-for-computing-relativistic-corrections>`__.
