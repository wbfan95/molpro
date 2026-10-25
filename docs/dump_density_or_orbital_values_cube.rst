.. _dump_density_or_orbital_values_cube--dump-density-or-orbital-values-cube:

Dump density or orbital values (CUBE)
=====================================

``CUBE,filename,iflag,$n_1$,$n_2$,$n_3$``

calls a module which dumps the values of various properties on a spatial parallelopipedal grid to an external file. The purpose is to allow plotting of orbitals, densities and other quantities by external programs. The format of the file is intended to be the same as that produced by other programs.

* ***filename*** is the unix path name of the file to be written, and its specification is mandatory.
* ***iflag*** If *iflag* is negative (default), a formatted file will be written, otherwise unformatted fortran i/o will be used.
* **:math:`n_1`,\ :math:`n_2`,\ :math:`n_3`** specify the number of grid points in each of three dimensions. If not specified, sensible defaults are chosen.

By default, the last density computed is evaluated on the grid, and written to *filename*. This behaviour can be modified by one or more of the following subcommands.

.. _dump_density_or_orbital_values_cube--step-setting-the-point-spacing:

STEP — setting the point spacing
================================

``STEP,[stepx],[stepy], [stepz]\\``
*stepx,stepy, stepz* specify the point spacing in each of three axis directions. By default, the value of *stepx,stepy, stepz* is determined by the number of grid points, the Bragg radii of the atoms, and some related parameters.

.. _dump_density_or_orbital_values_cube--density-source-of-density:

DENSITY — source of density
===========================

``DENSITY,[density-source]\\``
``GRADIENT,[density-source]\\``
``LAPLACIAN,[density-source]``

Compute the density and, optionally, its gradient and laplacian. *:math:`<`density-source:math:`>`* may be a record number containing the required density, and may contain further qualification, such as set or state number, in the usual way. By default, the last computed density is taken.

Example:

.. code-block:: text

   {multi;wf,spin=0,symmetry=1;state,2;dm;orbital,2140.2}
   {cube,multi_1;density,2140.2,state=1.1}   ! cube for state 1
   {cube,multi_2;density,2140.2,state=2.1}   ! cube for state 2
   {mrci;wf,spin=0,symmetry=1;state,2;dm,3000.2}   !save densities in record 3000.2
   {cube,mrci_1;density,3000.2,state=1.1}    ! cube for state 1
   {cube,mrci_2;density,3000.2,state=2.1}    ! cube for state 2

.. _dump_density_or_orbital_values_cube--potential-field-compute-electrostatic-potential-or-field:

POTENTIAL, FIELD — compute electrostatic potential or field
===========================================================

``POTENTIAL,[density-source]\\``
``FIELD,[density-source]\\``

*:math:`<`density-source:math:`>`* is interpreted as for ``DENSITY``

.. _dump_density_or_orbital_values_cube--orbital-source-of-orbitals:

ORBITAL — source of orbitals
============================

``ORBITAL,[orbital-list],[RECORD=orbital-source]``

*:math:`<`orbital-list:math:`>`* is a list of one or more orbital numbers of the form *number.symmetry* or keywords chosen from ``HOMO``, ``LUMO``, ``OCC`` (all occupied orbitals), ``ALL``. If nothing is specified, the default is ``HOMO``. *:math:`<`orbital-source:math:`>`* may be a record number containing the required density, and may contain further qualification, such as set number, in the usual way. By default, the last computed orbitals are taken.

Note that the CUBE file format precludes simultaneous orbital and density dumps.

.. _dump_density_or_orbital_values_cube--axis-direction-of-grid-axes:

AXIS — direction of grid axes
=============================

``AXIS,x,y,z``

*x,y,z* specify the unnormalised direction cosines of one of the three axes defining the grid. Up to three ``AXIS`` commands can be given, but none is required. Axes need not be orthogonal. By default, the first axis is the cartesian :math:`x`, the second is orthogonal to the first and to the cartesian :math:`z`, and the third is orthogonal to the first two.

.. _dump_density_or_orbital_values_cube--bragg-spatial-extent-of-grid:

BRAGG — spatial extent of grid
==============================

Based on the direction of the coordinate axes, a parallelopiped (in the usual case of orthogonal axes, a cuboid) is constructed to contain the molecule completely. The atoms are assumed to be spherical, with an extent proportional to their Bragg radii, and the constant of proportionality can be changed from the default value using

``BRAGG,scale``

After the parallelopiped has been constructed, the grid is laid out with equal spacing to cover it using the number of points specified on the ``CUBE`` command.

.. _dump_density_or_orbital_values_cube--origin-centroid-of-grid:

ORIGIN — centroid of grid
=========================

``ORIGIN,x,y,z``

*x,y,z* specify the centroid of the grid. It is usually not necessary to use this option, since the default should suffice for most purposes.

.. _dump_density_or_orbital_values_cube--title-user-defined-title:

TITLE — user defined title
==========================

``TITLE,title``

Set a user defined title in the cube file.

.. _dump_density_or_orbital_values_cube--description-user-defined-description:

DESCRIPTION — user defined description
======================================

``DESCRIPTION,description``

Set a user defined description in the cube file.

.. _dump_density_or_orbital_values_cube--format-of-cube-file:

Format of cube file
===================

The formatted cube file contains the following records

* ``(A)`` job title.
* ``(A)`` brief description of the file contents.
* ``(I5,3F12.6)`` number of atoms, coordinates of grid origin (bohr).
* ``(I5,3F12.6)`` number of grid points :math:`n_1`, step vector for first grid dimension.
* ``(I5,3F12.6)`` number of grid points :math:`n_2`, step vector for second grid dimension.
* ``(I5,3F12.6)`` number of grid points :math:`n_3`, step vector for third grid dimension.
* ``(I5,4F12.6)`` atomic number, charge and coordinates; one such record for each atom.
* ``(6E13.5)`` :math:`n_1 \times n_2` records of length :math:`n_3` containing the values of the density or orbital at each grid point. With default choice of the axes, the inner loop will be over :math:`n_3` points along the cartesian :math:`z` axis, and the outer loop over :math:`n_1` points along the cartesian :math:`x` axis.

In the case of a number of orbitals :math:`m`, a separate cube file for each orbital will be written that have the file names <name>_orbital_<num>.<sym>.cube where <num>.<sym> is the num'th orbital in symmetry sym.

In the case of the density gradient, the cube file will contain a record with a length of :math:`3n_3`, with the three cartesian components contiguous. In the latter case the density data will be written as well to a separate cube file. The file names for the different density data are marked with the
extensions <name>_density.cube, <name>_gradient.cube and <name>_laplacian.cube.

.. _dump_density_or_orbital_values_cube--example:

Example
=======

The following example shows how cube density and orbital data can be written using the RHF density source for the water molecule:

.. code-block:: text
   :caption: examples/cube.inp

   geometry={o;h1,o,r;h2,o,r,h1,theta}
   r=1 ang
   theta=104
   rhf
   {cube,h2o.cube}
   {cube,h2o.cube;orbital,homo}
   {cube,h2o.cube;density}
   {cube,h2o.cube;gradient}
   {cube,h2o.cube;laplacian}
