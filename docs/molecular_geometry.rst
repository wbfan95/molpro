.. raw:: html

   <span id="counterpoise-calculations"></span>

.. raw:: html

   <span id="dummy-centres"></span>

.. raw:: html

   <span id="geometry-files"></span>

.. raw:: html

   <span id="geometry-specifications"></span>

.. raw:: html

   <span id="lattice-of-point-charges"></span>

.. raw:: html

   <span id="redefining-and-printing-atomic-masses"></span>

.. raw:: html

   <span id="symmetry-specification"></span>

.. raw:: html

   <span id="visualization-of-results-using-molden"></span>

.. raw:: html

   <span id="writing-files-for-postprocessing-put"></span>

.. raw:: html

   <span id="xyz-input"></span>

.. raw:: html

   <span id="z-matrix-input"></span>

.. _molecular_geometry--molecular-geometry:

Molecular geometry
==================

.. _molecular_geometry--geometry-specifications:

Geometry specifications
=======================

The geometry may be given in standard Z-matrix form, or XYZ form, either in the input or in a separate file (see section `geometry files <molecular_geometry.html#geometry-files>`__). The geometry specifications are given in the form

``[SYMMETRY, options ]``

``[ORIENT, options ]``

``[ANGSTROM]``

``[BOHR]``

``GEOMETRY={ atom specifications }``

``GEOMETRY must come after the other commands that modify the way the geometry is constructed. The following are permitted as SYMMETRY options:``

Any valid combination of symmetry generators, as described in section `symmetry specification <molecular_geometry.html#symmetry-specification>`__ below.

Disable use of symmetry. Instead of ``SYMMETRY,NOSYM`` also just ``NOSYM`` can be used.

Enable use of symmetry.

The following are permitted as ``ORIENT`` options:

* ``CHARGE`` Orient molecule such that origin is centre of nuclear charge, and axes are eigenvectors of quadrupole moment.
* ``MASS`` Orient molecule such that origin is centre of mass, and axes are eigenvectors of inertia tensor (default for Z-matrix input). Alternatively, the symmetry centre can be specified as ``CENTRE=MASS|CHARGE``.
* ``NOORIENT`` Disable re-orientation of molecule (default for XYZ-input).
* **``SIGNX=``\ :math:`\pm1`** Force first non-zero :math:`x`-coordinate to be positive or negative, respectively. Similarly, ``SIGNY``, ``SIGNZ`` can be set for the :math:`y`- and :math:`z`-coordinates, respectively. This can be useful to fix the orientation of the molecule across different calculations and geometries. Alternatively, the system variables ``ZSIGNX``, ``ZSIGNY``, ``ZSIGNZ`` can be set to positive or negative values to achieve the same effect.
* ``PLANEXZ`` For the :math:`C_{2v}` and :math:`D_{2h}` point groups, force the primary plane to be :math:`xz` instead of the default :math:`yz`. The geometry builder attempts by swapping coordinate axes to place as many atoms as possible in the primary plane, so for the particular case of a planar molecule, this means that all the atoms will lie in the primary plane. The default implements recommendation :math:`5a` and the first part of recommendation :math:`5b` specified in `J. Chem. Phys. <https://dx.doi.org/10.1063/1.1740655>`__ **23**, 1997 (1955). ``PLANEYZ`` and ``PLANEXY`` may also be specified, but note that the latter presently generates an error for :math:`C_{2v}`.

``ANGSTROM Forces bond lengths that are specified by numbers, or variables without associated units, to use the values as a number of Ångstrom, rather than Bohr.``

``BOHR Forces bond lengths that are specified by numbers, or variables without associated units, to use the values as a number of Bohr. This is useful in the case of xyz-input with coordinates given in Bohr.``

.. _molecular_geometry--z-matrix-input:

Z-matrix input
==============

The general form of an atom specification line is

``[group[,]]atom, $p_1$, $r$, $p_2$, $\alpha$, $p_3$, $\beta$, $J$``

or, alternatively,

``[group[,]]atom, $p_1$, $x$, $y$, $z$``

where

* ***group*** atomic group number (optional). Can be used if different basis sets are used for different atoms of the same kind. The basis set is then referred to by this group number and not by the atomic symbol.
* ***atom*** chemical symbol of the new atom placed at position :math:`p_0`. This may optionally be appended (without blank) by an integer, which can act as sequence number, e.g., ``C1``, ``H2``, etc. Dummy centres with no charge and basis functions are denoted X, optionally appended by a number, e.g, X1.
* :math:`p_1` atom to which the present atom is connected. This may be either a number *n*, where :math:`n` refers to the :math:`n`\ ’th line of the Z-matrix, or an alphanumeric string as specified in the *atom* field of a previous card, e.g., ``C1``, ``H2`` etc. The latter form works only if the atoms are numbered in a unique way.
* :math:`r` Distance of new atom from :math:`p_1`. This value is given in bohr, unless ``ANG`` has been specified directly before or after the symmetry specification.
* :math:`p_2` A second atom needed to define the angle :math:`\alpha(p_0,p_1,p_2)`. The same rules hold for the specification as for :math:`p_1`.
* :math:`\alpha` Internuclear angle :math:`\alpha(p_0,p_1,p_2)`. This angle is given in degrees and must be in the range :math:`0 \lt \alpha \lt 180^{0}`.
* :math:`p_3` A third atom needed to define the dihedral angle :math:`\beta(p_0,p_1,p_2,p_3)`. Only applies if :math:`J=0`, see below.
* :math:`\beta` Dihedral angle :math:`\beta(p_0,p_1,p_2,p_3)` in degree. This angle is defined as the angle between the planes defined by :math:`(p_0,p_1,p_2)` and :math:`(p_1,p_2,p_3)` (:math:`-180^{0} \le \beta \le 180^{o}`). Only applies if :math:`J=0`, see below.
* :math:`J` If this is specified and nonzero, the new position is specified by two bond angles rather than a bond angle and a dihedral angle. If :math:`J=\pm 1`, :math:`\beta` is the angle :math:`\beta(p_0,p_1,p_3)`. If :math:`J=1`, the triple vector product :math:`({\bf p}_1-{\bf p}_0) \cdot [({\bf p}_1-{\bf p}_2) \times ({\bf p}_1-{\bf p}_3)]` is positive, while this quantity is negative if :math:`J=-1`.
* ***x,y,z*** Cartesian coordinates of the new atom. This form is assumed if :math:`p_1\le0`; if :math:`p_1\lt 0`, the coordinates are frozen in geometry optimizations.

All atoms, including those related by symmetry transformations, should be specified in the Z-matrix. Note that for the first atom, no coordinates need be given, for the second atom only :math:`p_1,r` are needed, whilst for the third atom :math:`p_3,\beta,J` may be omitted. The 6 missing coordinates are obtained automatically by the program, which translates and re-orients the molecule such that the origin is at the centre of mass, and the axes correspond to the eigenvectors of the inertia tensor (see also ``CHARGE`` option above).

Variable names, and in general expressions that are linear in all dependent variables, may be used as well as fixed numerical values for the parameters :math:`r`, :math:`\alpha` and :math:`\beta`. These expressions are evaluated as late as possible, so that it is possible, for example, to set up loops in which these parameters are changed; the geometry optimizer also understands this construction, and will optimize the energy with respect to the value of the variables. Non-linear expressions should not be used, because the geometry optimization module is unable to differentiate them.

Once the reorientation has been done, the program then looks for symmetry (:math:`D_{2h}` and subgroups), unless the ``NOSYM`` option has been given. It is possible to request that reduced symmetry be used by using appropriate combinations of the options ``X,Y,Z,XY,XZ,YZ,XYZ``. These specify symmetry operations, the symbol defining which coordinate axes change sign under the operation. The point group is constructed by taking all combinations of specified elements. If symmetry is explicitly specified in this way, the program checks to see that the group requested can be used, swapping the coordinate axes if necessary. This provides a mechanism for ensuring that the same point group is used, for example, at all points in the complete generation of a potential energy surface, allowing the safe re-utilization of neighbouring geometry molecular orbitals as starting guesses, etc.. When there is point-group symmetry, it is important to ensure that the dependence of the Z-matrix geometry on variables is such that the symmetry cannot be broken by any variation of those variables form their initial values; for example, for the water molecule in C2v symmetry, the two O-H distances should be specified using the same variable. Otherwise, numerical noise accumulated during geometry optimisation can cause the symmetry to break, leading to undefined behaviour.

Note that symmetry is not implemented in density fitting methods, and in these cases the NOSYM option is implied automatically.

Also note that by default the automatic orientation of the molecule only takes place if the geometry is defined by internal (Z-matrix) coordinates. In case of ``XYZ`` Input the orientation is unchanged, unless the ``MASS`` option is specified in the geometry block.

An input for H2O could look like this:

.. code-block:: text
   :caption: examples/h2o_zmatrix1.inp

   angstrom
   geometry={
   o;
   h1,o,1.0;
   h2,o,1.0,h1,104.0
   }
   hf

Alternatively, this could be used:

.. code-block:: text
   :caption: examples/h2o_zmatrix2.inp

   geometry={
   O,-1,  0.000000000,    0.000000000,   -0.130186067
   H,-1,  0.000000000,    1.489124508,    1.033245507
   H,-1,  0.000000000,   -1.489124508,    1.033245507
   }
   hf

.. _molecular_geometry--xyz-input:

XYZ input
=========

Simple cartesian coordinates in Ångstrom units can be read as an alternative to a Z matrix, either directly from the input stream, or from a file (see section  `geometry files <molecular_geometry.html#geometry-files>`__).). This facility is triggered by setting the Molpro variable ``GEOMTYP`` to the value ``XYZ`` before the geometry specification is given, but usually this does not need to be done, as a geometry specification where the first line is a single integer will be recognized as XYZ format, as will the case of the first line consisting of a chemical symbol followed by three cartesian coordinates. The geometry block should then contain the cartesian coordinates in XYZ format (Minnesota Supercomputer Center, Inc.). Only fixed numerical values are allowed. In contrast to z-matrix input, expressions containing variables are not permitted. Note that it is possible to present cartesian coordinates using expressions, via the cartesian variant of z-matrix input described above.

The XYZ file format consists of two header lines, the first of which contains the number of atoms, and the second of which is a title. The remaining lines each specify the coordinates of one atom, with the chemical symbol in the first field, and the :math:`x`, :math:`y`, :math:`z` coordinates following. A sequence number may be appended to the chemical symbol; it is then interpreted as the atomic group number, which can be used when different basis sets are wanted for different atoms of the same kind. The basis set is then specified for this group number rather than the atomic symbol. As a further extension, the first two header lines can be omitted.

Note that for XYZ input the default is not to reorient the molecule. Orientation can be forced, however, by the ``MASS`` or ``CHARGE`` options on the ``ORIENT`` directive. If orientation is requested, any approximately-obeyed point-group symmetry is discovered, and the geometry refined to obey that symmetry as closely as possible, as described in `J. Math. Chem. 60, 161-171 (2022) <https://doi.org/10.1007/s10910-021-01302-x>`__.

.. code-block:: text
   :caption: examples/h2o_xyzinput.inp

   geomtyp=xyz
   bohr
   geometry={
   3           ! number of atoms
   This is an example of geometry input for water with an XYZ file
   O ,0.0000000000,0.0000000000,-0.1302052882
   H ,1.4891244004,0.0000000000, 1.0332262019
   H,-1.4891244004,0.0000000000, 1.0332262019
   }
   hf

The `XYZ format <https://en.wikipedia.org/wiki/XYZ_file_format>`__ had been specified within the documentation distributed with the Minnesota Supercomputer Center’s XMol package. Note that Molpro has the facility to write XYZ files with the ``PUT`` command (see section `writing files for postprocessing(PUT) <molecular_geometry.html#writing-files-for-postprocessing-put>`__).

.. _molecular_geometry--geometry-files:

Geometry Files
--------------

Using the format

``GEOMETRY=file``

the geometry definitions are read from *file*, instead of inline.
For the name of the *file* and the characters allowed, similar recommendations hold as for the Molpro input file, see
https://www.molpro.net/develop/manual/doku.php?id=quickstart#how_to_run_molpro  .
The geometry file together with a path to it may however be used.

For series of similar calculations for different molecules the filename can be provided as a variable via the molpro script. The general format is

``geometry=string1$var1$var2'string2'$var3.extension``

where ``$var1, $var2, $var3`` etc are either integer numbers (provided via the ``-V`` molpro option) or string variables (provided via the ``--name`` molpro option). Variable names end before the next dollar ($), quote ('), full stop (.) or blank (end of line). Any number of variables is possible, although usually one is sufficient. ``.extension`` is appended as given. Strings in quotes between variables are also included as given. The (optional) first string (string1 above) must not be in quotes.

Examples:

``geometry=$mol.xyz``

.. code-block:: text

with ``molpro --name mol=h2o ...``. Alternatively

``geometry=$mol``

with ``molpro --name mol=h2o.xyz ...``. Both forms evaluate to ``geometry=h2o.xyz``.

Another useful possibility is

``geometry=product$n.xyz``

with ``molpro -V n=3 ...``, which evaluates to ``geometry=product3.xyz``.

Note that the variables defining the geometry filename cannot be defined in the input file, they can only be provided via the molpro script.

.. _molecular_geometry--symmetry-specification:

Symmetry specification
----------------------

If standard Z-matrix input is used, ``MOLPRO`` determines the symmetry automatically by default. However, sometimes it is necessary to use a lower symmetry or a different orientation than obtained by the default, and this can be achieved by explicit specification of the symmetry elements to be used, as described below.

Generating symmetry elements, which uniquely specify the point group, can be specified on the ``SYMMETRY`` directive. This must be given *before* the geometry block. Each symmetry directive only affects the subsequent geometry block; after a geometry block has been processed, the defaults are restored. Note that the specification of symmetry elements inside the geometry block is no longer allowed.

The dimension of the point group is 2\*\*(number of fields given). Each field consists of one or more of ``X, Y``, or ``Z`` (with no intervening spaces) which specify which coordinate axes change sign under the corresponding generating symmetry operation. It is usually wise to choose :math:`z` to be the unique axis where appropriate (essential for :math:`C_2` and :math:`C_{2h}`). In that case, the possibilities are:

* **(null card)** :math:`C_1` (i.e., no point group symmetry)
* ``Z`` :math:`C_s`
* ``XY`` :math:`C_2`
* ``XYZ`` :math:`C_i`
* ``X,Y`` :math:`C_{2v}`
* ``XY,Z`` :math:`C_{2h}`
* ``XZ,YZ`` :math:`D_2`
* ``X,Y,Z`` :math:`D_{2h}`

Note that Abelian point group symmetry only is available, so for molecules with degenerate symmetry, an Abelian subgroup must be used — e.g, :math:`C_{2v}` or :math:`D_{2h}` for linear molecules.

See section `symmetry <general_program_structure.html#symmetry>`__ for more details of symmetry groups and ordering of the irreducible representations. Also see section `Z-matrix input <molecular_geometry.html#z-matrix-input>`__ for more information about automatic generation of symmetry planes.

Note that by default the automatic orientation of the molecule only takes place if the geometry is defined by internal (Z-matrix) coordinates. In case of ``XYZ`` Input the orientation is unchanged, unless the ``MASS`` option is specified in the geometry block.

.. _molecular_geometry--writing-files-for-postprocessing-put:

Writing files for postprocessing(PUT)
-------------------------------------

The ``PUT`` command may be used at any point in the input to print, or write to a file, the current geometry. The syntax is

``PUT,style,file,status,info``

If *style* is ``GAUSSIAN``, a complete Gaussian input file will be written; in that case, ``info`` will be used for the first (route) data line, and defaults to ‘\ ``# SP``\ ’.

If *style* is ``XYZ``, an XYZ file will be written (see also section `XYZ input <molecular_geometry.html#xyz-input>`__). If *style* is ``XYZGRAD``, an XYZ file including energy gradients will be written (columns are: x,y,z,charge,gx,gy,gz; gradient is given in -1\*eV/A) If *style* is ``CRD``, the coordinates will be written in CHARMm CRD format.

If *style* is ``MOLDEN``, an interface file for the `MOLDEN <https://www3.cmbi.umcn.nl/molden>`__ visualization program is created; further details and examples are given below.

If *style* is ``IRSPEC``, a gnuplot input file will be written, which can be used to plot an IR spectrum. The gnuplot file contains Lorentz functions with the results of the previous vibrational calculation (``VSCF`` `the VSCF program (VSCF) <vibrational_scf_programs.html#the-vscf-program-vscf>`__, ``VCI`` `the VCI program (VCI) <vibration_correlation_programs.html#the-vci-program-vci>`__). Input examples can be found in these chapters.

If *style* is ``XML``, a dump of the current state is written, including variables, geometry, basis set, latest orbitals. The file format is well-formed XML, according to the
https://www.molpro.net/schema/molpro-output.xsd schema. In this case, additional options can be given:

* **``INDEX``,\ *n*** Insert an ``index=“n”`` attribute into the ``<molecule>`` node that is produced.
* ``NOFREQUENCIES`` Skip output of normal modes
* ``NOORBITALS`` Skip output of molecular orbitals
* ``NOSKIPVIRT`` Include virtual, as well as occupied, molecular orbitals
* ``NOBASIS`` Skip output of basis set specification
* ``NOVARIABLES`` Skip output of Molpro variables
* ``KEEPSPH`` Express orbitals in terms of spherical-harmonic functions rather than converting to cartesian
* ``NOCOMPRESS`` By default the orbitals are stored with lossy compression (approximately 32-bit precision) on a separate binary sidecar file. This option forces instead the full writing of the orbitals in ASCII to the xml stream

If *style* is ``TREXIO``, then the geometry and orbitals are written to a `TREXIO <https://github.com//trex-coe/trexio>`__ file. As with ``XML``, the orbitals can be controlled or omitted using the ``NOORBITALS`` and ``NOSKIPVIRT`` options.

If *style* is of the form ``BABEL/``\ *format*, then, where possible, the external shell command ``obabel`` will be used to convert the geometry to any format supported by the `OpenBabel <http://openbabel.org>`__ package. For the possible values of *format*, see `OpenBabel’s documentation <http://openbabel.org/docs/current/FileFormats/Overview.html>`__. If ``obabel`` is not installed on the system, then nothing happens.

If *style* is omitted, the Z-matrix, current geometry, and, where applicable, gradient are written.

*file* specifies a file name to which the data is written; if blank, the data is written to the output stream. If *status* is omitted or set to ``NEW``, any old contents of the file are destroyed; otherwise the file is appended.

A subcommand ``ORBITAL`` can be given, using the syntax given in section `selecting orbitals and density matrices (ORBITAL, DENSITY) <general_program_structure.html#selecting-orbitals-and-density-matrices-orbital-density>`__, to specify a set of orbitals other than the default. Using this keyword is recommended if several orbitals sets are computed with one input file, and especially necessary when orbitals such as natural orbitals from CCSD shall be exported.

.. _molecular_geometry--visualization-of-results-using-molden:

Visualization of results using Molden
=====================================

Geometry, molecular orbital, and normal mode information, when available, is dumped by ``PUT,MOLDEN`` in the format that is usable by `MOLDEN <https://www3.cmbi.umcn.nl/molden>`__.

The example below generates all the information required to plot the molecular orbitals of water, and to visualize the normal modes of vibration:

.. code-block:: text
   :caption: examples/h2o_put_molden.inp

   ***,H2O
   geometry={angstrom;o;h,o,roh;h,o,roh,h,theta};
   roh=1.0
   theta=104.0
   rhf;
   optg;
   {frequencies;
   print,low,img;}
   put,molden,h2o.molden;

The example below does a difference density by presenting its natural orbitals to MOLDEN. Note that although MOLDEN has internal features for difference density plots, the approach shown here is more general in that it bypasses the restriction to STO-3G, 3-21G, 4-31G and 6-31G basis sets.

.. code-block:: text
   :caption: examples/h2o_diffden_molden.inp

   gprint,orbitals
   symmetry,y,planexz
   geometry={O;H1,O,r;h2,O,r,h1,alpha}
   r=1.8
   alpha=104
   int;
   {hf;wf,10,1;orbital,2100.2}
   {multi;wf,10,1;orbital,2140.2}
   
   {matrop
   load,dscf,density,2100.2       !load scf density
   load,dmcscf,density,2140.2     !load mcscf density
   add,ddiff,dmcscf,-1,dscf       !compute dmcscf-dscf
   natorb,neworb1,dscf
   natorb,neworb2,dmcscf
   natorb,neworbs,ddiff
   save,neworbs,2110.2
   save,ddiff,2110.2}
   
   put,molden,h2o_ddens.molden;orb,2110.2

.. _molecular_geometry--lattice-of-point-charges:

Lattice of point charges
------------------------

``LATTICE,[INFILE=input_file,] [OUTFILE= output_file,]  [VARGRAD,] [NUCONLY,] [REMOVE]``

Includes a lattice of point charges, for use in QM/MM calculations for example (see section :doc:`QM/MM interfaces <qm_mm_interfaces>`). An external file (*input_file*) should be given as input, with the following format:

*Comment line*
*number of point charges N*
:math:`x1,y1,z1,q1,`\ *flag*\ :math:`1`
:math:`\vdots`
:math:`xN,yN,zN,qN,`\ *flag*\ :math:`N`
The :math:`x,y` and :math:`z` fields stand for the point charge coordinates (in Å), :math:`q` for its charge and *flag=1* indicates that gradients should be computed for this lattice point (0 means no gradient). :math:`x,y`, :math:`z`, :math:`q` are floating point numbers, *flag* is an integer, e.g.:

.. code-block:: text

    0.0 , 0.0 , 5.0 , 1.0 , 1

or (commas are optional here):

.. code-block:: text

    0.0  0.0  5.0 1.0 1

*outfile* specifies a file name to which the lattice gradient is written; if blank, it will be written to the output stream.

* ``VARGRAD`` (logical) Stores the lattice gradient in variable ``VARGRAD``.
* ``NUCONLY`` (logical) Disables gradient evaluation with respect to the lattice, independent of *flag* in the lattice file.
* ``REMOVE`` (logical) Removes the lattice.

Symmetry is not supported for lattice gradients.

Note that the nuclear repulsion energy (and therefore also the total energy) is computed without including the Coulomb interaction between the point charges.

.. _molecular_geometry--redefining-and-printing-atomic-masses:

Redefining and printing atomic masses
-------------------------------------

The current masses of all atoms can be printed using

``MASS, PRINT``

The atomic masses can be redefined using

``MASS, [type,] [symbol=mass, …]``

The optional keyword *type* can take either the value ``AVER[AGE]`` for using average isotope masses, or ``ISO[TOPE]`` for using the masses of the most abundant isotopes. This affects only the rotational constants and vibrational frequencies. As in most quantum chemistry packages, the default for *type* is ``AVERAGE``. If ``INIT`` is given, all previous mass definitions are deleted and the defaults are reset.

Individual masses can be changed by the following entries, where *symbol* is the chemical symbol of the atom and *mass* is the associated mass. Several entries can be given on one ``MASS`` card, and/or several ``MASS`` cards can follow each other. The last given mass is used.

Note that specifying different isotope masses for symmetry related atoms lowers the symmetry of the system if the molecular centre of mass is taken as the origin. This effect can be avoided by using the charge centre as origin, i.e., specifying ``CHARGE`` as the option to an ``ORIENT`` directive before the ``GEOMETRY`` input:

``ORIENT,CHARGE; GEOMETRY={ ...}``

.. _molecular_geometry--example-two-different-masses-for-hydrogen-in-hd:

Example: two different masses for hydrogen in HD
================================================

In analogy to defining two different basis sets for the same element (see  `Examples for basis input <basis_input.html#examples>`__), also two different masses can be defined.

.. code-block:: text
   :caption: examples/hd.inp

   geometry={
   2
   
   H1 0 0 0
   H2 0 0 1.0
   }
   
   mass,H1=1.008
   mass,H2=2.014
   
   basis={
   default=cc-pVDZ;
   }
   
   hf
   optg
   freq
   
   

For performing counterpoise corrected geometry optimizations see section `optimizing counterpoise corrected energies <geometry_optimization_optg.html#optimizing-counterpoise-corrected-energies>`__.

.. _molecular_geometry--dummy-centres:

Dummy centres
-------------

``DUMMY,[SKIP],atom1,atom2,$\ldots$``

Sets nuclear charges on atoms 1,2 etc. to zero, for doing counterpoise calculations, for example. *atom1, atom2,*\ :math:`\dots` can be Z-matrix row numbers or tag names. Ranges of consecutive atoms can be given as *atom1,-atom2*, which means from *atom1* to *atom2* (here *atom1* and *atom2* are z-matrix or xyz row numbers)

If the option ``SKIP`` is given, basis functions at the specified atoms are not included. This option is not possible with zmatrix geometry inputs, xyz inputs have to be used.

Note that the current setting of dummies is remembered by the program across restarts via the ``MOLPRO`` variable ``DUMMYATOMS``. Dummies can be reset to their original charges using a ``DUMMY`` card with no entries. Dummy centres are also reset to their original charges if (i) an ``INT`` command is encountered, or (ii) a new geometry input is encountered.

The program does not recognize automatically if the symmetry is reduced by defining dummy atoms. Therefore, for a given dummy atom, either all symmetry equivalent atoms must also be dummies, or the symmetry must be reduced manually as required. An error will result if the symmetry is not consistent with the dummy centre definitions.

.. _molecular_geometry--counterpoise-calculations:

Counterpoise calculations
=========================

Counterpoise corrections are easily performed using dummy cards. One first computes the energy of the total system, and then for the subsystems using dummy cards. The process can, however, be automated using the command

``COUNTERPOISE [, key1=value, key2=value,…...]``

Without any options, this will calculate the ghost-orbital corrections to dimer interaction energies using the last energy calculation to define the dimer and the methods to be used. First of all, the molecule is automatically partitioned into fragments. This is done by assigning all interatomic distances as either intra- or intermolecular, comparing the distance with the scaled sum of Bragg radii of the two atoms. The default scale factor is 1.4, but it can be changed with ``SCALE=``\ *scale*; for the S66 database of intermolecular interactions, correct partitioning is obtained with a scale factor in the range 1.2 to 1.95. If all of the distances are intramolecular, then it will be assumed that the system is not a non-bonded complex, and the counterpoise calculation will not be done at all. This gives support for running the same Molpro input for both dimers and monomers. At present, partitioning into more than two fragments is discovered, but there is no supporting implementation of the counterpoise correction.

The counterpoise procedure performs four calculations. For each of the identified monomers, it calculates the energy at the dimer geometry using first the dimer basis set, and secondly just the basis functions tied to the monomer atoms. The difference between these, the counterpoise correction, is reported, and added to the previously-calculated dimer energy.

Further options that specify the calculation to be run can be specified exactly as for geometry optimisations; see section `options to select the wavefunction and energy to be optimized <geometry_optimization_optg.html#options-to-select-the-wavefunction-and-energy-to-be-optimized>`__ for further details.

.. _molecular_geometry--example-interaction-energy-of-oh-ar:

Example: interaction energy of OH-Ar
====================================

.. code-block:: text
   :caption: examples/ohar_bsse.inp

   ***,OH(2Sig+)-Ar linear
   geometry={x1;                 !dummy center in center of mass
   o,x1,ro;h,x1,rh,o,180;        !geometry of OH
   ar,x1,rar,o,theta,h,0}        !geometry of Ar
   roh=1.8                       !OH bond-length
   rar=7.5                       !distance of Ar from center of mass
   theta=0                       !angle OH-Ar
   rh=roh*16/17                  !distance of O from center of mass
   ro=roh*1/17                   !distance of H from center of mass
   basis=avdz                    !basis set
   
   text,calculation for complex
   {rhf;occ,8,3,3;wf,27,1,1}     !RHF for total system
   rccsd(t)                      !CCSD(T) for total system
   e_ohar=energy                 !save energy in variable e_ohar
   
   text,cp calculation for OH
   dummy,ar                      !make Ar a dummy center
   {rhf;occ,3,1,1;wf,9,1,1}      !RHF for OH
   rccsd(t)                      !CCSD(T) for OH
   e_oh=energy                   !save energy in variable e_oh
   
   text,cp calculation for Ar
   dummy,o,h                     !make OH dummy
   hf                            !scf for Ar
   ccsd(t)                       !CCSD(T) for Ar
   e_ar=energy                   !save energy in variable e_ar
   
   text,separate calculation for OH
   geometry={O;H,O,roh}          !geometry for OH alone
   {rhf;occ,3,1,1;wf,9,1,1}      !RHF for OH
   rccsd(t)                      !CCSD(T) for OH
   e_oh_inf=energy               !save energy in variable e_oh_inf
   
   text,separate calculation for Ar
   geometry={AR}                 !geometry for OH alone
   hf                            !scf for Ar
   ccsd(t)                       !CCSD(T) for Ar
   e_ar_inf=energy               !save energy in variable e_ar_inf
   
   de=(e_ohar-e_oh_inf-e_ar_inf)*tocm    !compute uncorrected interaction energy
   de_cp=(e_ohar-e_oh-e_ar)*tocm         !compute counter-poise corrected interaction energy
   bsse_oh=(e_oh-e_oh_inf)*tocm          !BSSE for OH
   bsse_ar=(e_ar-e_ar_inf)*tocm          !BSSE for Ar
   bsse_tot=bsse_oh+bsse_ar              !total BSSE

For performing counterpoise corrected geometry optimizations see section `optimizing counterpoise corrected energies <geometry_optimization_optg.html#optimizing-counterpoise-corrected-energies>`__.
