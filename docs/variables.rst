.. raw:: html

   <span id="clearing-variables"></span>

.. raw:: html

   <span id="indexed-variables-vectors"></span>

.. raw:: html

   <span id="macro-definitions-using-string-variables"></span>

.. raw:: html

   <span id="reading-variables-from-an-external-file"></span>

.. raw:: html

   <span id="setting-variables"></span>

.. raw:: html

   <span id="special-variables"></span>

.. raw:: html

   <span id="string-variables"></span>

.. raw:: html

   <span id="system-variables"></span>

.. raw:: html

   <span id="the-show-command"></span>

.. raw:: html

   <span id="variables-set-by-the-program"></span>

.. raw:: html

   <span id="vector-operations"></span>

.. _variables--variables:

Variables
=========

Data may be stored in *variables*. A variable can be of type *string*, *real* or *logical*, depending on the type of the expression in its definition. Any sequence of characters which is not recognized as expression or variable is treated as string. In this section, we will discuss only *real* and *logical* variables. *String* variables will be discussed in more detail in section `string variables <variables.html#string-variables>`__. Variables can be used anywhere in the input, but they can be set only outside the input blocks for specific programs. For example, if a variable is used within the input block for ``HF``, it must have been set before the ``HF{...}`` input block.

Molpro automatically stores various results and data in system variables (see section `variables set by the program <variables.html#variables-set-by-the-program>`__), which can be used for further processing. A new feature of Molpro2002 is that most system variables are write protected and cannot be overwritten by the user. The input is automatically checked before the job starts, and should a system variable be set in the input the job will stop immediately with an error message. Only in some exceptions (see section `system variables <variables.html#system-variables>`__), system variables can be modified using the ``SET`` command (but not with the simple ``NAME``\ =\ *value* syntax). Note that due to the changed usage and syntax of the ``SET`` command, compatibility with Molpro92 input syntax is no longer maintained.

.. _variables--setting-variables:

Setting variables
=================

A variable can be defined using

*variable1=*\ *value1*, *variable2=*\ *value2*, …

A variable definition is recognized by the equals sign in the *first* field of the input card. For example,

``THRESH,ENERGY=1.d-8,GRADIENT=1.d-5``

does *not* define variables; here ``ENERGY`` and ``GRADIENT`` are options for the ``THRESH`` directive.

Variables can have different types:

* **Numbers:** The value is a number or an expression. The general form of *value* is

*expression* [,] [*unit*]
*unit* is an optional string which can be used to associate a unit to the value. ``ANG[STROM]``, ``DEGREE``, ``HARTREE`` are examples. Undefined variables in expressions are assumed to be zero (and defined to be zero at the same time).

* **Logicals:** The value can be ``.TRUE.`` or ``.FALSE.`` (``.T.`` and .F. also work), or a logical expression. Internally, ``.TRUE.`` is stored as 1 and ``.FALSE.`` as zero.
* **Strings:** The value can either be a string enclosed in quotes or a string variable. See section `string variables <variables.html#string-variables>`__ for more details.

.. _variables--indexed-variables:

Indexed variables
=================

Variables can be indexed, but only one-dimensional indexing is available. Indexed variables can be defined either individually, e.g.

.. code-block:: text

   R(1)=1.0 ANG
   R(2)=1.2 ANG
   R(3)=1.3 ANG

or as a vector of values enclosed by square brackets:

``R=[1.0,1.1,1.2] ANG``

Subranges can also be defined, e.g.

.. code-block:: text

   R(1)=1.0 ANG
   R(2:3)=[1.1,1.2] ANG

leads to the same result as the above two forms.

The type of each element depends on the type of the assigned value, and it is possible to mix types in one variable. Example:

.. code-block:: text

   geometry={he}
   hf
   result=[program,energy,status.gt.0]

yields:

.. code-block:: text

   RESULT(1)      =    HF-SCF
   RESULT(2)      =        -2.85516048  AU
   RESULT(3)      =    TRUE

In this example the variables ``PROGRAM``, ``ENERGY``, and ``STATUS`` are system variables, which are set by the program (see section `system variables <variables.html#system-variables>`__).

.. _variables--string-variables:

String variables
================

As explained already in section `setting variables <variables.html#setting-variables>`__, string variables can be set as other variables in the form

``variable = ’string’\\``
``variable = string_variable``

Strings must be enclosed by quotes. Otherwise the string is assumed to be a variable, and if this is undefined it is assumed to be zero.

Alternatively, if the name of the variable is preceded by a dollar ($), all values are assumed to be a string. This can be a string variable, a quoted string, or an unquoted string. Note that unquoted strings are converted to upper case. Also note that quotes are compulsory if the string contains blanks.

Example:

``$str=[a,b+4,’This is an example for strings’]``

yields

.. code-block:: text

   STR(1)         =    A
   STR(2)         =    B+4
   STR(3)         =    This is an example for strings

As a general rule, string variables are replaced by their value only if they are preceded by a dollar ($)
(exceptions: in variable definitions, on ``SHOW`` cards, and in logical expressions on ``IF`` cards, the dollar is optional). This is a precaution to avoid commands which have the same name as a variable being interpreted as variables. Variables may also appear on ``TEXT`` or ``TITLE`` cards or in strings, but must be preceded by $ in these cases. Example:

.. code-block:: text

   $METHOD=MCSCF
   R=1.5
   TEXT,$method results for R=$R Bohr

prints

``MCSCF results for R=1.5 Bohr``

String variables can be concatenated with strings or other string variables in the following way. Assume that variable ``PROGRAM`` has the value ``MRCI``. Setting

``METHOD=’$PROGRAM+Q’``

sets ``METHOD`` to ``MRCI+Q``. Alternatively, if we would also have a variable ``VERSION`` with value ``Q``, we could write

``METHOD=’$PROGRAM+$VERSION’``

Again, the value of ``METHOD`` would be ``MRCI+Q``. Note that the quotes are necessary in these cases.

Substring operations are not implemented.

.. _variables--system-variables:

System variables
================

As mentioned above, most system variables cannot be written by the user. In some exceptions, it is possible to redefine them using the ``SET`` command:

``SET,variable = expression [,] [unit]``

This holds for the following variables:

* ``CHARGE`` Total charge of the molecule
* ``NELEC`` Number of electrons
* ``SPIN`` Spin quantum number, given as :math:`2\cdot M\_S` (integer)
* ``SCFSPIN`` Same as ``SPIN``, but only for HF
* ``MCSPIN`` Same as ``SPIN``, but only for MCSCF
* ``CISPIN`` Same as ``SPIN``, but only for MRCI
* ``STATE`` State to be optimized
* ``MCSTATE`` Same as ``STATE`` but only for MCSCF
* ``CISTATE`` Same as ``STATE`` but only for MRCI
* ``SYMMETRY`` State symmetry
* ``SCFSYM[METRY]`` Same as ``SYMMETRY`` but only for HF
* ``MCSYM[METRY]`` Same as ``SYMMETRY`` but only for MCSCF
* ``CISYM[METRY]`` Same as ``SYMMETRY`` but only for MRCI
* ``LQUANT`` Lambda quantum number for linear molecules
* ``OPTCONV`` Geometry optimization convergence criterion
* ``PROGRAM`` Last program name
* ``CPUSTEP`` CPU-time of last program step
* ``SYSSTEP`` System-time of last program step
* ``WALLSTEP`` Elapsed-time of last program step
* ``FOCKDONE`` Indicates if closed-shell fock operator is available.
* ``MAXBASIS`` Max number of basis sets stored on dump files. If the maximum is reached, the last one is overwritten when a new one is made, and all information (including dump records etc) of the previous basis is lost. The default is the maximum possible number of basis sets (30), which cannot be exceeded.

.. _variables--macro-definitions-using-string-variables:

Macro definitions using string variables
========================================

String variables for which the stored string has the form of an algebraic expression are evaluated to a number if they are preceded by two dollars (''

.. math::

   ''). Example:
   <code>
   string='a+b'
   a=3
   b=4
   text,This is string $string which evaluates to

string

prints

``* This is string a+b which evaluates to 7``

This can be used to define simple macros, which can be used at various places in the subsequent input. For instance,

.. code-block:: text

   ECORR='ENERGY-ESCF' !define a macro
   HF                  !do SCF calculation
   ESCF=ENERGY         !store SCF energy in variable ESCF
   MULTI               !do CASSCF
   DEMC=$$ECORR        !store CASSCF correlation energy in variable DEMC
   MRCI                !do MRCI
   DECI=$$ECORR        !store MRCI correlation energy in variable DECI

Here is an example of advanced use of macros and string variables:

.. code-block:: text
   :caption: examples/oh_macros.inp

   ***,test for parser
   text,This fancy input demonstrates how string variables and macros can be used
   text
   basis=vdz               !define basis set
   geometry={O;H,O,r}      !define geometry (z-matrix)
   
   text,methods
   $method=[rhf,2[casscf,2[mrci]]]
   text,active spaces
   $spaces=['[3,1,1]',3['[4,2,2]'],3['[5,2,2]']]
   text,symmetries
   $symset=['1',2['[1,2,3]','1','2']]
   text,weight factors for state averaged casscf
   $weights=['1','[1,1,1]',2[' '],'[1,0.5,0.5]',2[' ']]
   text,scf occupation
   set,scfocc=[3,2[1]]
   text,bond distance
   r=1.85
   
   hf
   do i=1,#method         !loop over methods
   mcocc=$$spaces(i)      !set active space for this run
   set,symmetry=$$symset(i)   !set symmetries for this run
   set,weight=$$weights(i)    !set weights for this run
   $method(i)             !now run method
   e(i)='$energy'         !save energies in strings
   dipol(i)='$dmz'        !save dipole moments in strings
   enddo
   table,method,spaces,symset,weights,e,dipol
   title,Results for OH, r=$r, basis=$basis
   head,method,spaces,symmetries,weights,energies,'dipole moments'
   exit

.. _variables--indexed-variables-vectors:

Indexed Variables (Vectors)
===========================

Variables may be indexed, but only one-dimensional arrays (vectors) are supported. The index may itself be a variable. For instance

``METHOD(I)=PROGRAM\\``
``E(I)=ENERGY``

are valid variable definitions, provided ``I``, ``PROGRAM``, and ``ENERGY`` are also defined variables. Indices may be nested to any depth.

Different elements of an array can be of different type (either *real* or *logical*). However, only one *unit* can be assigned to an array. String variables have no associated value and cannot be mixed with the other variable types. Therefore, a given variable name can only be used either for a *string* variable or a *real* (*logical*) variable.

Vectors (arrays) can be conveniently defined using square brackets:

``R=[1.0,1.2,1.3] ANG``

This defines an array with three elements, which can be accessed using indices; for instance, ``R(2)`` has the value ``1.2 ANG``. A repeat specifier can be given in front of the left bracket: ``5[0]`` is equivalent to ``[0,0,0,0,0]``. Brackets can even be nested: for instance, ``2[1,2,2[2.1,3.1]]`` is equivalent to ``[1,2,2.1,3.1,2.1,3.1,1,2,2.1,3.1,2.1,3.1]``.

Arrays can be appended from a given position just by entering additional elements; for instance,

``R(4)=[1.4,1.5] ANG``

or

``R(4:)=[1.4,1.5] ANG``

extends the above array to length 5. Previously defined values can be overwritten. For instance

``R(2)=[1.25,1.35,1.45]``

modifies the above vector to (1.0, 1.25, 1.35, 1.45, 1.5).

If no index is given on the left hand side of the equal sign, an existing variable of the same name is replaced by the new values, and all old values are lost. For instance

* ``THETA=[100,110,120,130]`` set four values
* **…**
* ``THETA(1)=104`` replace ``THETA(1)`` by a new value; ``THETA(2:4)`` are unchanged
* **…**
* ``THETA=[140,150]`` old variable ``THETA`` is replaced; ``THETA(3:4)`` are deleted

Square brackets can also be used to define an array of strings, e.g.,

``METHOD=[INT,HF,CASSCF,MRCI]``

These could be used as follows:

.. code-block:: text

   DO I=1,4
   $METHOD(I)
   ENDDO

The above input would be equivalent to

.. code-block:: text

   INT
   HF
   CASSCF
   MRCI

The current length of an array can be accessed by preceding ``#`` to the variable name. For instance, in the above examples ``#R`` and ``#METHOD`` have the values 5 and 4, respectively. If a variable is not defined, zero is returned but no error occurs. This can be used to test for the existence of a variable, for example:

``IF(#SPIN.EQ.0.AND.#NELEC.EQ.1) SET,SPIN=MOD(NELEC,2)``

This defines variable ``SPIN`` if it is unknown and if ``NELEC`` is a scalar (one dimensional) variable.

.. _variables--vector-operations:

Vector operations
=================

The following simple vector operations are possible:

* Copying or appending a vector to another vector. For instance ``S=R`` copies a vector ``R`` to a vector ``S``. ``S(3)=R`` copies ``R`` to ``S(3), S(4), …``. ``S(#S+1)=R`` appends vector ``R`` to vector ``S``. It is also possible to access a range of subsequent elements in a vector: ``S=R(2:4)`` copies elements 2 to 4 of ``R`` to ``S(1), S(2), S(3)``. Note that ``R(2:)`` denotes elements ``R(2)`` to ``R(#R)``, but ``R(2)`` denotes a single element of ``R``.
* Vector-scalar operations: ``R=R*2`` multiplies each element of ``R`` by 2. Instead of the number 2, also scalar (one dimensional) variables or expressions can be used, e.g., ``R=R*ANG`` converts all elements of ``R`` from Ångstrøm to bohr, or ``Z=R*COS(THETA)`` creates a vector ``Z`` with elements ``Z(i) = R(i)*COS(THETA)``. All other algebraic operators can be used instead of “\*”. Note that the scalar must come last since the first variable in the expression determines the vector length.
* Vector-vector operations: If ``A`` and ``B`` are vectors of the same length, then ``A \times B`` is also a vector of this length. Here :math:`\times` stands for any algebraic operator, and the operation is done for each pair of corresponding elements. For instance, ``A + B`` adds the vectors ``A`` and ``B``, and ``A * B`` multiplies their elements. Note that the latter case is not a scalar product. If an attempt is made to connect two vectors of different lengths by an algebraic operator, an error occurs.
* Intrinsic functions: Assume ``THETA=[100,110,120,-130]`` to be a vector of angles (in degrees). In this case ``X=2*COS(THETA)`` is also a vector containing the cosines of each element of ``THETA`` multiplied by two, i.e., ``X(i) = 2*COS(THETA(i))``. ``MAX(THETA)`` or ``MIN(THETA)`` return the maximum and minimum values, respectively, in array ``THETA``. Vector operations can also be nested, e.g., ``MAX(ABS(THETA))`` returns the maximum value in array ``ABS(THETA)``.

At present, vector operations are not supported with ``string`` variables.

.. _variables--special-variables:

Special variables
=================

.. code-block:: text

    ==== Variables set by the program ====

A number of variables are predefined by the program. The following variables can be used to convert between atomic units and other units:

.. code-block:: text

   EV=1.d0/27.2113839d0 HARTREE
   KELVIN=1.d0/3.157747d5 HARTREE
   KJOULE=1.d0/2625.500d0 HARTREE
   KCAL=1.d0/627.5096d0 HARTREE
   CM=1.d0/219474.63067d0 HARTREE
   CM-1=1.d0/219474.63067d0 HARTREE
   HZ=1.d0/6.5796839207d15 HARTREE
   HERTZ=1.d0/6.5796839207d15 HARTREE
   ANG=1.d0/0.529177210903d0 BOHR
   ANGSTROM=1.d0/0.529177210903d0 BOHR
   
   TOEV=27.2113839d0 EV
   TOK=3.157747d5 K
   TOKELVIN=3.157747d5 K
   TOCM=219474.63067d0 CM-1
   TOHERTZ=6.5796839207d15 HZ
   TOHZ=6.5796839207d15 HZ
   TOKJ=2625.500d0 KJ/MOL
   TOKJOULE=2625.500d0 KJ/MOL
   TOKCAL=627.5096d0 KCAL/MOL
   TOA=0.529177210903d0 ANGSTROM
   TOANG=0.529177210903d0 ANGSTROM
   TODEBYE=2.54158d0 DEBYE

Further variables which are set during execution of the program:

* ``INTYP`` defines integral program to be used. Either ``INTS`` (Seward) or ``INTP`` (Argos).
* ``INTDONE`` has the value ``.true.`` if the integrals are done for the current geometry.
* ``CARTESIAN`` Set to one if Cartesian basis functions are used.
* ``SCFDONE`` has the value ``.true.`` if an SCF calculation has been done for the current geometry.
* ``NUMVAR`` number of variables presently defined
* ``STATUS`` status of last step (1=no error, -1=error or no convergence)
* ``CHARGE`` Total charge of the molecule
* ``NELEC`` number of electrons in last wavefunction
* ``SPIN`` spin multiplicity minus one of last wavefunction
* ``ORBITAL`` record of last optimized orbitals (set but never used in the program)
* ``LASTORB`` Type of last optimized orbitals (``RHF``, ``UHF``, ``UHFNAT``, or ``MCSCF``).
* ``LASTSYM`` Symmetry of wavefunction for last optimized orbitals.
* ``LASTSPIN`` :math:`2*M_S` for wavefunctions for last optimized orbitals.
* ``LASTNELEC`` Number of electrons in wavefunction for last optimized orbitals.
* ``ENERGR(istate)`` Reference energy for state *istate* in MRCI and CCSD.
* ``ENERGY(istate)`` last computed total energy for state *istate* for the method specified in the input (e.g., ``HF``, ``MULTI``, ``CCSD(T)``, or ``CCSD[T]``.
* ``ENERGY_AVRG`` State-averaged energy of the MCSCF program multi.
* ``ENERGY_METHOD`` String variable holding name of the method used for calculating ``ENERGY``
* ``ENERGY_BASIS`` String variable holding name of the orbital basis-set used for calculating ``ENERGY``
* ``GEOMETRY_METHOD`` Equal to the value of ``ENERGY_METHOD`` for the most recent geometry optimisation
* ``GEOMETRY_BASIS`` Equal to the value of ``ENERGY_BASIS`` for the most recent geometry optimisation
* ``ENERGD(istate)`` Total energy for state *istate* including Davidson correction (set only in ``CI``).
* ``ENERGP(istate)`` Total energy for state *istate* including Pople correction (set only in ``CI``).
* ``ENERGT(1)`` Total energy including perturbative triples ``(T)`` correction (set only in ``CCSD(T), QCI(T)``).
* ``ENERGT(2)`` Total energy including perturbative triples ``[T]`` correction (set only in ``CCSD(T), QCI(T)``).
* ``ENERGT(3)`` Total energy including perturbative triples ``-t`` correction (set only in ``CCSD(T), QCI(T)``).
* ``EMP2`` holds MP2 energy in MPn, CCSD, BCCD, or QCISD calculations, and RS2 energy in MRPT2 (CASPT2) calculations.
* ``EMP3`` holds MP3 energy in MP3 and MP4 calculations, and RS3 energy in MRPR3 (CASPT3) calculations.
* ``EMP4`` holds MP4(SDQ) energy in MP4 calculations. The MP4(SDTQ) energy is stored in variable ``ENERGY``.
* ``METHODC`` String variable holding name of the methods used for ``ENERGC``, e.g., ``CCSD, BCCD, QCI``.
* ``METHODT(1)`` String variable holding name of the methods used for ``ENERGT(1)``, e.g., ``CCSD(T), BCCD(T), QCI(T)``.
* ``METHODT(2)`` String variable holding name of the methods used for ``ENERGT(2)``, e.g., ``CCSD[T], BCCD[T], QCI[T]``.
* ``METHODT(3)`` String variable holding name of the methods used for ``ENERGT(3)``, e.g., ``CCSD-T, BCCD-T, QCI-T``.
* ``ENERGC`` Total energy excluding perturbative triples correction (set only in ``QCI`` or ``CCSD`` with triples correction enabled).
* ``DFTFUN`` total value of density functional in ``DFT`` or ``KS``.
* ``DFTFUNS(ifun)`` value of ``ifun``\ ’th component of density functional in ``DFT`` or ``KS``.
* ``DFTNAME(ifun)`` name of ``ifun``\ ’th component of density functional in ``DFT`` or ``KS``.
* ``DFTFAC(ifun)`` factor multiplying ``ifun``\ ’th component of density functional in ``DFT`` or ``KS``.
* ``DFTEXFAC`` factor multiplying exact exchange in ``KS``.
* ``PROP(istate)`` computed property for state *istate*. See below for the names ``PROP`` of various properties.
* ``PROGRAM`` last program called, as specified in the input (e.g., ``HF``, ``CCSD(T)``, etc.)
* ``ITERATIONS`` Number of iterations used. Set negative if no convergence or max number of iterations reached.
* ``CPUSTEP`` User-CPU time in seconds for last program called.
* ``SYSSTEP`` System-CPU time in seconds for last program called.
* ``WALLSTEP`` Elapsed time in seconds for last program called.

The variable names for properties are the same as used on the ``EXPEC`` input cards.

* ``OV`` Overlap
* ``EKIN`` Kinetic energy
* ``POT`` Potential
* ``DELTA`` Delta function
* ``DEL4`` :math:`\nabla^4`
* ``DARWIN`` Darwin term of relativistic correction
* ``MASSV`` Mass-velocity term of relativistic correction
* ``EREL`` Total relativistic correction
* ``DMX, DMY, DMZ`` Dipole moments
* ``XX, YY, ZZ, XY, XZ, XY`` Second moments
* ``XXX, XXY, XXZ, XYY, XYZ, XZZ, YYY, YYZ, YZZ, ZZZ`` Third moments
* ``QMXX, QMYY, QMZZ, QMXY, QMXZ, QMXY`` Quadrupole moments
* ``EFX, EFY, EFZ`` Electric field
* ``FGXX, FGYY, FGZZ, FGXY, FGXZ, FGXY`` Electric field gradients
* ``D/DX, D/DY, D/DZ`` Velocity
* ``LSX, LSY, LSZ`` One-electron spin-orbit
* ``LL`` Total angular momentum squared :math:`L^2`
* ``LX, LY, LZ`` Electronic angular momentum
* ``LXLX, LYLY, LZLZ, LXLY, LXLZ, LYLZ`` Two-electron angular momentum

By default, only the dipole moments are computed and defined. The values of other properties are only stored in variables if they are requested by ``EXPEC`` cards. If more than one state is computed (e.g., in state-averaged MCSCF, corresponding arrays ``PROP(istate)`` are returned. If properties are computed for more than one center, the center number is appended to the name, e.g. ``EFX1``, ``EFX2`` etc.

If transition properties are computed, their values are stored in corresponding variables with prefix ``TR``, e.g., ``TRDMX, TRDMY, TRDMZ`` for transition dipole moments. If more than two states are computed, the index is :math:`(i-1)*(i-2)/2+j`, where :math:`i \gt j \ge 1` are state numbers. In a state-averaged calculation, states are counted sequentially for all state symmetries.

For instance, in the following state-averaged MCSCF

``MULTI;WF,14,1,0;STATE,3;WF,14,2,0;STATE,2;WF,14,3,0``

the states are counted as

.. list-table::

   * - :math:`i`
     - 1
     - 2
     - 3
     - 4
     - 5
     - 6
     - 
   * - Symmetry
     - 1
     - 1
     - 1
     - 2
     - 2
     - 3
     - 
   * - Root in Sym.
     - 1
     - 2
     - 3
     - 1
     - 2
     - 1
     - 

.. _variables--variables-recognized-by-the-program:

Variables recognized by the program
===================================

All variables described below are checked by the program, but not set (except ``NELEC`` and ``SPIN``). If these are not defined by the user, the program uses its internal defaults. The variables are only recognized and used if defined using the ``SET`` command, e.g.

``SET,MCOCC=[6,3,2]\\``
``SET,STATE=2``

etc.

Variables recognized by the SCF program:

* ``CHARGE`` Total charge of the molecule (can be given instead of nelec)
* ``NELEC`` number of electrons
* ``SPIN`` spin multiplicity minus one
* ``SCFSYM[METRY]`` wavefunction symmetry
* ``SYMMETRY`` ``as SCFSYMM``; only used if ``SCFSYMM`` is not present.
* ``SCFOC[C]`` number of occupied orbitals in each symmetry for ``SCF``
* ``SCFCL[OSED]`` number of closed-shell orbitals in each symmetry for ``SCF``
* ``SCFORB`` record of saved orbitals in ``SCF``
* ``SCFSTART`` record of starting orbitals used in ``SCF``

Variables recognized by the MCSCF program:

* ``CHARGE`` Total charge of the molecule (can be given instead of nelec)
* ``NELEC`` number of electrons
* ``MCSYM[METRY]`` wavefunction symmetry. This can be an array for state-averaged calculations.
* ``SYMMETRY`` as ``MCSYMM``; only used if ``MCSYMM`` is not present.
* ``MCSPIN`` spin multiplicity minus one. This can be an array for state-averaged calculations, but different spin multiplicities can only be used in determinant CASSCF. If only one value is specified, this is used for all states
* ``SPIN`` as ``MCSPIN``; only used if ``MCSPIN`` is not present.
* ``MCSTATE`` number of states for each symmetry in ``MCSCF``
* ``STATE`` as ``MCSTATE``; only used if ``MCSTATE`` is not present.
* ``WEIGHT`` weight factors for all states defined by ``SYMMETRY`` and ``STATE``
* ``LQUANT`` Eigenvalues of :math:`L_z^2` for linear molecules for each state defined by ``SYMMETRY`` and ``STATE``.
* ``MCSELECT`` records from which configurations can be selected and selection threshold
* ``SELECT`` as ``MCSELECT``; only used if ``MCSELECT`` is not present.
* ``MCRESTRICT`` can be used to define occupancy restrictions
* ``RESTRICT`` as ``MCRESTRCT``; only used if ``MCRESTRICT`` is not present:
* ``CONFIG`` if set to .true. or to one triggers use of CSFs
* ``MCOC[C]`` number of occupied orbitals in each symmetry
* ``OCC`` as ``MCOCC``; only used if ``MCOCC`` is not present.
* ``MCCL[OSED]`` number of optimized closed-shell orbitals in each symmetry
* ``CLOSED`` as ``MCCLOSED``; only used if ``MCCLOSED`` is not present.
* ``MCFROZEN`` number of frozen core orbitals in each symmetry
* ``FROZEN`` as ``MCFROZEN``; only used if ``MCFROZEN`` is not present.
* ``MCSTART`` record of starting orbitals
* ``COREORB`` record of frozen core orbitals
* ``MCORB`` record for saving optimized orbitals
* ``MCSAVE`` records for saving CI wavefunction (like ``SAVE`` card in MCSCF)

Variables recognized by the CI/CCSD program:

* ``CHARGE`` Total charge of the molecule (can be given instead of nelec)
* ``NELEC`` number of electrons
* ``SPIN`` spin multiplicity minus one
* ``CISYM[METRY]`` wavefunction symmetry. If this is an array, only SYMMETRY(1) is used.
* ``SYMMETRY`` as ``CISYMM``; only used if ``CISYMM`` is not present.
* ``CISTATE`` number of states in CI
* ``STATE`` as ``CISTATE``, only used if ``CISTATE`` is not present.
* ``CISELECT`` records from which configurations can be selected
* ``SELECT`` as ``CISELECT``; only used if ``CISELCT`` is not present.
* ``CIRESTRICT`` defines occupancy restrictions
* ``RESTRICT`` as ``RESTRICT``; only used if ``CIRESTRICT`` is not present.
* ``CIOC[C]`` number of occupied orbitals in each symmetry
* ``OCC`` ``as CIOCC``; only used if ``CIOCC`` is not present.
* ``CICL[OSED]`` number of closed-shell orbitals in each symmetry
* ``CLOSED`` ``as CICLOSED``; only used if ``CICLOSED`` is not present.
* ``CICO[RE]`` number of core orbitals in each symmetry
* ``CORE`` ``as CICORE``; only used if ``CICORE`` is not present.
* ``CIORB`` record of orbitals used in CI
* ``CISAVE`` records for saving CI wavefunction (like ``SAVE`` card in CI)
* ``CISTART`` records for restarting with previous CI wavefunction (like ``START`` card in CI)

Variables recognized by the DFT/KS program:

* **``DF(ifun)`` or ``DFTNAME(ifun)``** name of ``ifun``\ ’th component of density functional.
* ``DFTFAC(ifun)`` factor multiplying ``ifun``\ ’th component of density functional.
* ``DFTEXFAC`` factor multiplying exact exchange in ``KS``.

Example for the use of these variables for a state-averaged MCSCF (note that system variables can only be modified using the SET command, see section `system variables <variables.html#system-variables>`__):

* ``SET,NELEC=9`` defines number of electrons
* ``SET,SPIN=1`` defines wavefunction to be a doublet
* ``SET,SYMMETRY=[1,2,3]`` defines wavefunction symmetries for state averaged calculation
* ``SET,STATE=[2,1,1]`` defines number of states to be averaged in each symmetry
* ``WEIGHT=[2,2,1,1]`` defines weights for the above four states
* ``OCC=[5,2,2]`` number of occupied orbitals in each symmetry
* ``CLOSED=2`` number of closed-shell orbitals in symmetry 1
* ``MCORB=3100.2`` record for optimized orbitals
* ``MULTI`` do mcscf with above parameters

Note: Setting the variables ``NELEC``, ``SPIN``, or ``SYMMETRY``, has the same effect giving these on a global ``WF`` directive. If the global ``WF`` directive is given after the variable definition, the values of the variables are replaced by the values given on the ``WF`` directive. Vice versa, if a variable definition follows a global ``WF`` directive, the new value of the variable is used in the following. Note that ``WF`` input cards in command blocks have preference over global ``WF`` directives or input variables.

.. _variables--displaying-variables:

Displaying variables
--------------------

Variables or the results of expressions can be displayed in the output using ``SHOW`` and ``TABLE``.

.. _variables--the-show-command:

The SHOW command
================

The general form of the ``SHOW`` command is as follows:

``SHOW[ncol,format],expression``

where *expression* can be an expression or variable, *ncol* is the number of values printed per line (default 6), and *format* is a format (default 6F15.8). This can be used to print vectors in matrix form. The specification of *ncol* and *format* is optional. Assume that ``E`` is a vector:

* ``SHOW,E`` prints ``E`` using defaults.
* ``SHOW[n],E`` prints ``E`` with ``n`` elements per line; (if ``n>6``, more than one line is needed, but in any case a new line is started after ``n`` elements).
* ``SHOW[n,10f10.4],E`` prints ``E`` in the format given, with newline forced after ``n`` elements.

Note that the total length of the format should not exceed 100 characters (a left margin of 30 characters is always needed).

A *wild card* format can be used to show several variables more easily:

``SHOW,qm*,dm*``

shows all variables whose names begin with ``QM`` and ``DM``. Note that no letters must appear after the ``*``, i.e., the wild card format is less general than in ``UNIX`` commands.

See the ``TABLE`` command for another possibility to tabulate results.

.. _variables--clearing-variables:

Clearing variables
------------------

Variables can be deleted using

``CLEAR,name1, name2, …``

Wild cards can be used as in ``SHOW``, e.g.,

``CLEAR,ENERG*``

clears all variables whose names begin with ``ENERG``. All variables can be cleared using

``CLEARALL``

The length of vectors can be truncated simply by redefining the length specifier: ``#R=2`` truncates the array ``R`` to length 2. Higher elements are no longer available (but could be redefined). Setting ``#R=0`` is equivalent to the command ``CLEAR,R``.

.. _variables--reading-variables-from-an-external-file:

Reading variables from an external file
---------------------------------------

Variables can be read from an external file using

``READVAR, filename, [option]``

Such files can be saved, for instance by the geometry optimization program, and reused later to recover a certain optimized geometry. The format of the input in *filename* is the same as for ordinary input.

If *option*\ =\ ``NOINDEX|IGNOREINDEX`` is given then variable indices are ignored and only the last value saved is read (without index). This can be useful if for example a file saved with ``SAVEACT`` in a geometry optimization is read, and it is intended to continue with the variables that were saved last.
