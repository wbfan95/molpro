.. raw:: html

   <span id="printing-matrices-print"></span>

.. _matrix_operations--matrix-operations:

Matrix operations
=================

``MATROP;``

``MATROP performs simple matrix manipulations for matrices whose dimensions are those of the one particle basis set. To do so, first required matrices are loaded into memory using the LOAD command. To each matrix an internal name (an arbitrary user defined string) is assigned, by which it is referenced in further commands. After performing operations, the resulting matrices can be saved to a dump record using the SAVE directive. Numbers, e.g. traces or individual matrix elements, can be saved in variables.``

*code* may be one of the following:

* ``LOAD`` Loads a matrix from a file
* ``SAVE`` Saves a matrix to a file
* ``ADD`` Adds matrices
* ``TRACE`` Forms the trace of a matrix or of the product of two matrices
* ``MULT`` Multiplies two matrices
* ``TRAN`` Transforms a matrix
* ``DMO`` Transforms density into MO basis
* ``NATORB`` Computes natural orbitals
* ``DIAG`` Diagonalizes a matrix
* ``OPRD`` Forms an outer product of two vectors
* ``DENS`` Forms a closed-shell density matrix
* ``FOCK`` Computes a closed-shell fock matrix
* ``COUL`` Computes a coulomb operator
* ``EXCH`` Computes an exchange operator
* ``PRINT`` Prints a matrix
* ``PRID`` Prints diagonal elements of a matrix
* ``PRIO`` Prints orbitals
* ``PRIC`` Prints the transpose of a matrix in scientific notation
* ``ELEM`` Assigns a matrix element to a variable
* ``READ`` Reads a square matrix from input
* ``WRITE`` Writes a square matrix to a file
* ``SET`` Assigns a value to a variable
* ``ADDVEC`` Adds a multiple of a column of one matrix to a column of a second matrix

Note that the file name appearing in above commands is converted to lower case on unix machines.

See the following subsections for explanations.

.. _matrix_operations--calling-the-matrix-facility-matrop:

Calling the matrix facility (MATROP)
====================================

The program is called by the input card ``MATROP`` without further specifications.

``MATROP``

It can be followed by the following commands in any order, with the restriction that a maximum of 50 matrices can be handled. The first entry in each command line is a command keyword, followed by the name of the result matrix. If the specified result matrix *result* already exists, it is overwritten, otherwise a new matrix is created. All matrices needed in the operations must must have been loaded or defined before, unless otherwise stated.

If a backquote (‘) is appended to a name, the matrix is transposed.

.. _matrix_operations--loading-matrices-load:

Loading matrices (LOAD)
=======================

All matrices which are needed in any of the subsequent commands must first be loaded into memory using the ``LOAD`` command. Depending on the matrix type, the ``LOAD`` command has slightly different options. In all forms of ``LOAD`` *name* is an arbitrary string (up to 16 characters long) by which the loaded matrix is denoted in subsequent commands.

.. _matrix_operations--loading-orbitals:

Loading orbitals
================

``LOAD,name,ORB [,record] [,specifications]``

loads an orbital coefficient matrix from the given dump record. If the record is not specified, the last dump record is used. Specific orbitals sets can be selected using the optional *specifications*, as explained in section `selecting orbitals and density matrices (ORBITAL, DENSITY) <general_program_structure.html#selecting-orbitals-and-density-matrices-orbital-density>`__. The keyword ``ORB`` needs not to be given if *name*\ =\ ``ORB``.

.. _matrix_operations--loading-density-matrices:

Loading density matrices
========================

``LOAD,name,DEN [,record] [,specifications]``

loads a density matrix from the given dump record. If the record is not given, the last dump record is used. Specific densities sets can be selected using the optional *specifications*, as explained in section `selecting orbitals and density matrices (ORBITAL, DENSITY) <general_program_structure.html#selecting-orbitals-and-density-matrices-orbital-density>`__. The keyword ``DEN`` needs not to be given if *name*\ =\ ``DEN``.

Example,

``load,trdm,dens,6000.2,stateb=1.1,statek=3.2``

loads a transition density matrix that has previously been saved on record 6000.2. The bra state is the first state in symmetry 1, and ket is the third state in symmetry 2.

An equivalent input would be

``load,trdm,dens,6000.2,stateb=1,statek=3,symb=1,symk=2``

.. _matrix_operations--loading-the-ao-overlap-matrix-s:

Loading the AO overlap matrix S
===============================

``LOAD,name,S``

loads the overlap matrix in the AO basis. The keyword ``S`` needs not to be given if *name*\ =\ ``S``.

.. _matrix_operations--loading-s-1-2:

Loading S^{-1/2}
================

``LOAD,name,SMH``

loads :math:`{\bf S}^{-1/2}`, where **S** is the overlap matrix in the AO basis. The keyword ``SMH`` needs not to be given if *name*\ =\ ``SMH``.

.. _matrix_operations--loading-the-one-electron-hamiltonian:

Loading the one-electron hamiltonian
====================================

``LOAD,name,H0``

``LOAD,name,H01``

loads the one-electron hamiltonian in the AO basis. ``H01`` differs from ``H0`` by the addition of perturbations, if present (see sections `dipole fields (DIP) <properties_and_expectation_values.html#dipole-fields-dip>`__, `quadrupole fields (QUAD) <properties_and_expectation_values.html#quadrupole-fields-quad>`__). The keyword ``H0`` (``H01``) needs not to be given if *name*\ =\ ``H0`` (``H01``). The nuclear energy associated to ``H0`` or ``H01`` is internally stored.

.. _matrix_operations--loading-the-kinetic-or-potential-energy-operators:

Loading the kinetic or potential energy operators
=================================================

``LOAD,name,EKIN``

``LOAD,name,EPOT``

loads the individual parts of the one-electron hamiltonian in the AO basis. ``EPOT`` is summed for all atoms. The nuclear energy is associated to ``EPOT`` and internally stored. The keyword ``EKIN`` (``EPOT``) needs not to be given if *name*\ =\ ``EKIN`` (``EPOT``).

.. _matrix_operations--loading-one-electron-property-operators:

Loading one-electron property operators
=======================================

``LOAD,name,OPER,opname,[isym],x,y,z``

loads one-electron operator *opname*, where *opname* is a keyword specifying the operator (a component must be given). See section `One-electron operators and expectation values (GEXPEC) <program_control.html#one-electron-operators-and-expectation-values-gexpec>`__ for valid keys. *isym* is the total symmetry of the operator (default 1). If just the operator name is given, it is computed at the origin. If the operator name is appended by a center number in parenthesis, it is computed at this center [e.g. ``DELTA(1)``]. If it is appended by (0), it is computed at the given coordinates *x,y,z* (in a.u.), e.g. ``DELTA(0),,0,0,4``

If the operator is not available yet in the operator record, it is automatically computed. The nuclear value is associated internally to *name* and also stored in variable ``OPNUC`` (this variable is overwritten for each operator which is loaded, but can be copied to another variable using the ``SET`` command. Note that the electronic part of dipole and quadrupole operators are multiplied by -1.

.. _matrix_operations--loading-matrices-from-plain-records:

Loading matrices from plain records
===================================

``LOAD,name,TRIANG,record,[isym] LOAD,name,SQUARE,record,[isym]``

Loads a triangular or square matrix from a plain record (not a dump record or operator record). If *isym* is not given, 1 is assumed.

.. _matrix_operations--saving-matrices-save:

Saving matrices (SAVE)
----------------------

``SAVE,name,record [,type],[subtype]``

At present, *type* can be ``DENSITY``, ``ORBITALS``, ``FOCK``, ``H0``, ``ORBEN``, ``OPER``, ``TRIANG``, ``SQUARE``, or ``VECTOR``. If *type* and/or *subtype* are not given but known from ``LOAD`` or another command, this is assumed. *subtype* can for example be ``ALPHA`` or ``BETA`` for UHF orbitals, or ``NATORB`` for natural orbitals. Orbitals, density matrices, fock matrices, and orbital energies are saved to a dump record (the same one should normally be used for all these quantities); if *record* is textual rather than a number, it will instead be interpreted as a file name, and the data will be written in `FCIDUMP <https://gitlab.com/molpro/fcidump>`__ format to that file. If *type* is ``H0``, the one-electron hamiltonian is overwritten by the current matrix and the nuclear energy is modified according to the value associated to *name*. The nuclear energy is also stored in the variable ``ENUC``. All other matrices can be saved in triangular or square form to plain records using the ``TRIANG`` and ``SQUARE`` options, respectively (for triangular storage, the matrix is symmetrized before being stored). Eigenvectors can be saved in plain records using the ``VECTOR`` option. Only one matrix or vector can be stored in each plain record.

One-electron operators can be stored in the operator record using

``SAVE,name,OPER, [PARITY=np], [NUC=opnuc], CENTRE=icen],[COORD=[x,y,z]]``

The user-defined operator *name* can can then be used on subsequent ``EXPEC`` or ``GEXPEC`` cards. :math:`np=1,0,-1` for symmetric, square, antisymmetric operators, respectively (default 1). If ``CENTRE`` is specified, the operator is assumed to have its origin at the given centre, where *icen* refers to the row number of the z-matrix input. The coordinates can also be specified explicitly using ``COORD``. By default, the coordinates of the last read operator are assumed, or otherwise zero.

If ``NATURAL`` orbitals are generated and saved in a dump record, the occupation numbers are automatically stored as well. This is convenient for later use, e.g., in ``MOLDEN``.

.. _matrix_operations--adding-matrices-add:

Adding matrices (ADD)
---------------------

``ADD,result [,fac1],mat1 [,fac2],mat2,…``

calculates *result = fac1 :math:`\cdot` mat1 + fac2 :math:`\cdot` mat2* + …

The strings *result*, *mat1*, *mat2* are internal names specifying the matrices. *mat1*, *mat2* must exist, otherwise an error occurs. If *result* does not exist, it is created.

The factors *fac1*, *fac2* are optional (may be variables). If not given, one is assumed.

The nuclear values associated to the individual matrices are added accordingly and the result is associated to *result*.

.. _matrix_operations--trace-of-a-matrix-or-the-product-of-two-matrices-trace:

Trace of a matrix or the product of two matrices (TRACE)
--------------------------------------------------------

``TRACE,variable, mat1,,[factor]``

Computes *variable* = *factor*\*tr(*mat1*).

``TRACE,variable, mat1, mat2,[factor],[facnuc]``

Computes *variable* = *factor*\*trace(*mat1 :math:`\cdot` mat2*) + facnuc\*opnuc.

The result of the trace operation is stored in the ``MOLPRO`` variable *variable*, which can be used in subsequent operations.

If *factor* is not given, one is assumed. If *facnuc* is given, the nuclear contribution multiplied by facnuc is added. It is assumed that either *mat1* or *mat2* has a nuclear contribution. The default for *facnuc* is zero.

.. _matrix_operations--setting-variables-set:

Setting variables (SET)
-----------------------

``SET,variable,value``

Assigns *value* to ``MOLPRO`` variable *variable*, where *value* can be an expression involving any number of variables or numbers. Indexing of *variable* is not possible, however.

.. _matrix_operations--multiplying-matrices-mult:

Multiplying matrices (MULT)
---------------------------

``MULT,result, mat1, mat2,[fac1],[fac2]``

calculates *result = fac2 \* result + fac1 \* mat1 :math:`\cdot` mat2*

The strings *result* , *mat1* , *mat2* are the internal names of the matrices. If *fac1* is not given, *fac1=1* is assumed. If *fac2* is not given, *fac2=0* is assumed. If a backquote (‘) is appended to *mat1* or *mat2* the corresponding matrix is transposed before the operation. If a backquote is appended to *result*, the resulting matrix is transposed.

.. _matrix_operations--transforming-operators-tran:

Transforming operators (TRAN)
-----------------------------

``TRAN,result, Op, C``

calculates *result* = *C(T)\*Op\*C*. The strings *result*, *C*, and *Op* are the internal names of the matrices. If a backquote (‘) is appended to *C* or *Op* the corresponding matrix is transposed before the operation. Thus,

``TRAN,result, Op, C‘``

computes *result* = *C\*Op\*C(T)*.

.. _matrix_operations--transforming-density-matrices-into-the-mo-basis-dmo:

Transforming density matrices into the MO basis (DMO)
-----------------------------------------------------

``DMO,result, D, C``

calculates *result* = *C(T)\*S\*D\*S\*C*. The strings *result*, *C*, and *D* are internal names.

.. _matrix_operations--diagonalizing-a-matrix-diag:

Diagonalizing a matrix DIAG
---------------------------

``DIAG,eigvec,eigval,matrix [,iprint]``

Diagonalizes *matrix*. The eigenvectors and eigenvalues are stored internally with associated names *eigvec* and *eigval*, respectively (arbitrary strings of up to 16 characters). The if *iprint*.gt.0, the eigenvalues are printed. If *iprint.gt.1*, also the eigenvectors are printed.

.. _matrix_operations--generating-natural-orbitals-natorb:

Generating natural orbitals (NATORB)
------------------------------------

``NATORB,name,dens,thresh``

computes natural orbitals for density matrix *dens*. Orbitals with occupation numbers greater or equal to *thresh* (default 1.d-4) are printed.

.. _matrix_operations--forming-an-outer-product-of-two-vectors-oprd:

Forming an outer product of two vectors (OPRD)
----------------------------------------------

``OPRD,result,matrix,orb1,orb2,factor``

Takes the column vectors *v1* and *v2* from *matrix* and adds their outer product to *result*. *v1* and *v2* must be given in the form *icol.isym*, e.g., 3.2 means the third vector in symmetry 2. The result is

:math:`result(a,b)=result(a,b) + factor*v1(a)*v2(b)`

If *result* has not been used before, it is zeroed before performing the operation.

.. _matrix_operations--combining-matrix-columns-addvec:

Combining matrix columns (ADDVEC)
---------------------------------

``ADDVEC,result,orbr,source,orbs,factor``

Takes the column vector *orbs* from *source* and adds it to column *orbr* of *result*. *v1* and *v2* must be given in the form *icol.isym*, e.g., 3.2 means the third vector in symmetry 2.

.. _matrix_operations--forming-a-closed-shell-density-matrix-dens:

Forming a closed-shell density matrix (DENS)
--------------------------------------------

``DENS,density,orbitals,iocc$_1$, iocc$_2 \ldots$``

Forms a closed-shell density matrix *density* from the given *orbitals*. The number of occupied orbitals in each symmetry :math:`i` must be provided in *iocc:math:`_i`*.

.. _matrix_operations--computing-a-fock-matrix-fock:

Computing a fock matrix (FOCK)
------------------------------

``FOCK,f,d``

computes a closed shell fock matrix using density *d*. The result is stored in *f*.

.. _matrix_operations--computing-a-coulomb-operator-coul:

Computing a coulomb operator (COUL)
-----------------------------------

``COUL,J,d``

computes a coulomb operator J(d) using density *d*.

.. _matrix_operations--computing-an-exchange-operator-exch:

Computing an exchange operator (EXCH)
-------------------------------------

``EXCH,K,d``

computes an exchange operator K(d) using density *d*.

.. _matrix_operations--printing-matrices-print:

Printing matrices (PRINT)
-------------------------

``PRINT,name,[ncol(1), ncol(2),…]``

prints matrix *name*. *ncol(isym)* is the number of columns to be printed for row symmetry *isym* (if not given, all columns are printed). For printing orbitals one can also use ``ORB``.

.. _matrix_operations--printing-diagonal-elements-of-a-matrix-prid:

Printing diagonal elements of a matrix (PRID)
---------------------------------------------

``PRID,name prints the diagonal elements of matrix name.``

.. _matrix_operations--printing-orbitals-prio:

Printing orbitals (PRIO)
------------------------

``PRIO,name,$n_1,n_2,n_3,\ldots,n_8$``

prints orbitals *name*. The first :math:`n_i` orbitals are printed in symmetry :math:`i`. If :math:`n_i=0`, all orbitals of that symmetry are printed.

.. _matrix_operations--printing-a-matrix-transpose-in-scientific-notation-pric:

Printing a matrix transpose in scientific notation(PRIC)
--------------------------------------------------------

``PRIC,name,[ncol(1), ncol(2),…]``

prints the transpose of matrix *name* in scientific notation (comma delimited). *ncol(isym)* is the number of columns to be printed for row symmetry *isym* (if not given, all columns are printed). For printing orbitals one can also use ``ORB``.

.. _matrix_operations--assigning-matrix-elements-to-a-variable-elem:

Assigning matrix elements to a variable (ELEM)
----------------------------------------------

``ELEM,name,matrix, col,row``

assigns elements (col,row) of *matrix* to variable *name*. *col* and *row* must be given in the form *number.isym*, where *number* is the row or column number in symmetry *isym*. The product of the row and column symmetries must agree with the matrix symmetry.

.. _matrix_operations--setting-a-matrix-element-to-a-variable-poke:

Setting a matrix element to a variable (POKE)
---------------------------------------------

``POKE,name,matrix, col,row``

sets elements (col,row) of *matrix* to variable *name*. *col* and *row* must be given in the form *number.isym*, where *number* is the row or column number in symmetry *isym*. The product of the row and column symmetries must agree with the matrix symmetry.

.. _matrix_operations--reading-a-matrix-from-the-input-file-read:

Reading a matrix from the input file (READ)
-------------------------------------------

``READ``,\ *name*,[[TYPE=]\ *type*],[[SUBTYPE=]\ *subtype*],[[SYM=]\ *symmetry*], [FILE=\ *file*],[TRANS]
{ *values* }

Reads a square matrix (symmetry 1) from input or an ASCII file. The *values* can be in free format, but their total number must be correct. Comment lines starting with ’#’, ’\*’, or ’!’ are skipped. If the data are given in input, the data block must be enclosed either by curly brackets or the first line must be ``BEGIN_DATA`` and the last line ``END_DATA``. If a *filename* is specified as option, the data are read from this file. In this case, the ``BEGIN_DATA``, ``END_DATA`` lines in the file are optional, and no data block must follow.
If ``TRANS`` is given, the matrix is read columnwise, otherwise rowwise

For compatibility with older versions, the data can also be included in the input using the ``INCLUDE`` command (see section `input format <definition_of_molpro_input_language.html#input-format>`__). In this case, the include file must contain the ``BEGIN_DATA`` and ``END_DATA`` lines (this is automatically the case if the file has been written using the ``MATROP,WRITE`` directive).

*type* is a string which can be used to assign a matrix type. If appropriate, this should be any of the ones used in the ``LOAD`` command. In addition, ``SUBTYPE`` can be specified if necessary. This describes, e.g., the type of orbitals or density matrices (e.g., for natural orbitals *TYPE*\ =\ ``ORB`` and *SUBTYPE*\ =\ ``NATURAL``). The matrix symmetry needs to be given only if it is not equal to 1.

.. _matrix_operations--writing-a-matrix-to-an-ascii-file-write:

Writing a matrix to an ASCII file (WRITE)
-----------------------------------------

``WRITE,name[,filename[,status[,format]]]``

Writes a matrix to an ASCII file. If *filename* is not given the matrix is written to the output file, otherwise to the specified file (*filename* is converted to lower case). If *filename*\ =\ ``PUNCH`` it is written to the current punch file.

If *status*\ =\ ``NEW``, ``ERASE`` or ``REWIND``, a new file is written, otherwise as existing file is appended.

If *format*\ =\ ``SCIENTIFIC``, or ``FLOAT`` the output is given in the scientific notation (floating point).

.. _matrix_operations--examples:

Examples
--------

The following example shows various uses of the ``MATROP`` commands.

.. code-block:: text
   :caption: examples/matrop.inp

   ***,h2o matrop examples
   geometry={o;h1,o,r;h2,o,r,h1,theta}   !Z-matrix geometry input
   r=1 ang                               !bond length
   theta=104                             !bond angle
   hf                                    !do scf calculation
   {multi
   natorb
   canonical}
   {matrop
   load,D_ao,DEN,2140.2                  !load mcscf density matrix
   load,Cnat,ORB,2140.2,natural          !load mcscf natural orbitals
   load,Ccan,ORB,2140.2,canonical        !load mcscf canonical orbitals
   load,Dscf,DEN,2100.2                  !load scf density matrix
   load,S                                !load overlap matrix
   
   prio,Cnat,4,1,2                       !prints occupied casscf orbitals
   
   elem,d11,Dscf,1.1,1.1                 !print element D(1,1)
   elem,d21,Dscf,2.1,1.1                 !print element D(2,1)
   elem,d12,Dscf,1.1,2.1                 !print element D(1,2)
   
   tran,S_mo,s,Cnat                      !transform s into MO basis (same as above)
   print,S_mo                            !print result - should be unit matrix
   
   trace,Nao,S_mo                        !trace of S_MO = number of basis functions
   trace,Nel,D_ao,S                      !form trace(DS) = number of electrons
   
   mult,SC,S,Cnat                        !form SC=S*Cnat
   tran,D_nat,D_ao,SC                    !transform density to natural MO (could also be done using dmo)
   
   prid,D_nat                            !print diagonal elements (occupation numbers)
   
   dmo,D_can,D_ao,Ccan                   !transform D_ao to canonical MO basis. Same as above simplified
   add,D_neg,-1,D_can                    !multiply d_can by -1
   diag,U,EIG,D_neg                      !diagonalizes density D_can
   mult,Cnat1,Ccan,U                     !transforms canonical orbitals to natural orbitals
   prio,Cnat1,4,1,2                      !prints new natural orbitals
   
   natorb,Cnat2,D_ao                     !make natural orbitals using MCSCF density D_ao directly
   prio,Cnat2,4,1,2                      !prints new natural orbitals (should be the same as above)
   
   add,diffden,D_ao,-1,Dscf              !form mcscf-scf difference density
   natorb,C_diff,diffden                 !make natural orbitals for difference density
   
   write,diffden,denfile                 !write difference density to ASCII file denfile
   save,C_diff,2500.2                    !store natural orbitals for difference density in dump record 2500.2
   }

This second example adds a quadrupole field to ``H0``. The result is exactly the same as using the ``QUAD`` command. ``H0`` is overwritten by the modified one-electron matrix, and the nuclear energy is automatically changed appropriately. The subsequent SCF calculations use the modified one-electron operator.

Note that it is usually recommended to add fields with the D͡IP, ``QUAD``, or ``FIELD`` commands.

.. code-block:: text
   :caption: examples/matropfield.inp

   R    =    0.96488518 ANG
   THETA=  101.90140469
   geometry={H1
             O,H1,R;
             H2,O,R,H1,THETA}
   {hf;wf,10,1}
   
   field=0.05             !define field strength
   
   {matrop
   load,h0,h0             !load one-electron hamiltonian
   load,xx,oper,xx        !load second moments
   load,yy,oper,yy
   load,zz,oper,zz
   add,h01,h0,field,zz,-0.5*field,xx,-0.5*field,yy   !add second moments to h0 and store in h01
   save,h01,1210.1,h0}    !save h0
   hf                     !do scf with modified h0
   
   {matrop
   load,h0,h0             !load h0
   load,qmzz,oper,qmzz    !load quadrupole moment qmzz
   add,h01,h0,field,qmzz  !add quadrupole moment to h0  (same result as above with second moments)
   save,h01,1210.1,h0}    !save h0
   hf                     !do scf with modified h0
   
   quad,,,field           !add quadrupole field to h0
   hf                     !do scf with modified h0 (same result as above with matrop)
   
   field,zz,field,xx,-0.5*field,yy,-0.5*field   ! (add general field; same result as above)
   hf                     !do scf with modified h0 (same result as above with matrop)
   
   field,zz,field       !same as before with separate field commands
   field+,xx,-0.5*field
   field+,yy,-0.5*field
   hf                     !do scf with modified h0 (same result as above with matrop)

.. _matrix_operations--exercise-scf-program:

Exercise: SCF program
---------------------

``Write a closed-shell SCF program for H$_2$O using MATROP!``

Hints:

First generate a starting orbital guess by finding the eigenvectors of *h0*. Store the orbitals in a record. Basis and geometry are defined in the usual way before the first call to ``MATROP``.

Then use a ``MOLPRO``\   ``DO`` loop and call ``MATROP`` for each iteration. Save the current energy in a variable (note that the nuclear energy is stored in variable ``ENUC``). Also, compute the dipole moment in each iteration. At the end of the iteration perform a convergence test on the energy change using the ``IF`` command. This must be done outside ``MATROP`` just before the ``ENDDO``. At this stage, you can also store the iteration numbers, energies, and dipole moments in arrays, and print these after reaching convergence using ``TABLE``. For the following geometry and basis set

.. code-block:: text

   geometry={o;h1,o,r;h2,o,r,h1,theta}   !Z-matrix geometry input
   r=1 ang                               !bond length
   theta=104                             !bond angle
   basis=vdz                             !basis set
   thresh=1.d-8                          !convergence threshold

the result could look as follows:

.. code-block:: text

    SCF has converged in 24 iterations
   
       ITER       E             DIP
        1.0   -68.92227207    2.17407361
        2.0   -71.31376891   -5.06209922
        3.0   -73.73536433    2.10199751
        4.0   -74.64753557   -1.79658706
        5.0   -75.41652680    1.43669203
        6.0   -75.77903293    0.17616098
        7.0   -75.93094231    1.05644998
        8.0   -75.98812258    0.63401784
        9.0   -76.00939154    0.91637513
       10.0   -76.01708679    0.76319435
       11.0   -76.01988143    0.86107911
       12.0   -76.02088864    0.80513445
       13.0   -76.02125263    0.83990621
       14.0   -76.02138387    0.81956198
       15.0   -76.02143124    0.83202128
       16.0   -76.02144833    0.82464809
       17.0   -76.02145450    0.82912805
       18.0   -76.02145672    0.82646089
       19.0   -76.02145752    0.82807428
       20.0   -76.02145781    0.82711046
       21.0   -76.02145792    0.82769196
       22.0   -76.02145796    0.82734386
       23.0   -76.02145797    0.82755355
       24.0   -76.02145797    0.82742787

It does not converge terribly fast, but it works!
