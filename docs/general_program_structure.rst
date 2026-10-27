.. raw:: html

   <span id="data-set-manipulation"></span>

.. raw:: html

   <span id="default-procedures"></span>

.. raw:: html

   <span id="defining-orbital-subspaces"></span>

.. raw:: html

   <span id="defining-orbital-subspaces-occ-closed-core-frozen"></span>

.. raw:: html

   <span id="defining-the-wavefunction"></span>

.. raw:: html

   <span id="files"></span>

.. raw:: html

   <span id="input-structure"></span>

.. raw:: html

   <span id="memory-allocation"></span>

.. raw:: html

   <span id="molpro-help"></span>

.. raw:: html

   <span id="multiple-passes-through-the-input"></span>

.. raw:: html

   <span id="plugins"></span>

.. raw:: html

   <span id="records"></span>

.. raw:: html

   <span id="restart"></span>

.. raw:: html

   <span id="selecting-orbitals-and-density-matrices-orbital-density"></span>

.. raw:: html

   <span id="summary-of-keywords-known-to-the-controlling-program"></span>

.. raw:: html

   <span id="symmetry"></span>

.. _general_program_structure--general-program-structure:

General program structure
=========================

This chapter gives an overview of the most important features of Molpro. For the new user, it is essential to understand the strategies and conventions described in this section, in particular the meaning of *files* and *records*, and the use of *symmetry*. This chapter will focus on general aspects; detailed information about each command will be given in later chapters. Information about commands and parameters can also be obtained using the Molpro help facility (see section `molpro help <general_program_structure.html#molpro-help>`__).

.. _general_program_structure--input-structure:

Input structure
===============

A typical ``MOLPRO`` input has the following structure:

.. code-block:: text

   ***,title                    !title (optional)
   memory,4,m                   !memory specification (optional)
   file,1,name.int              !permanent named integral file (optional)
   file,2,name.wfu              !permanent named wavefunction file (optional)
   
   gprint,options               !global print options (optional)
   gthresh,options              !global thresholds (optional)
   gdirect[,options]            !global direct (optional)
   gexpec,opnames               !global definition of one-electron operators (optional)
   
   basis=basisname              !basis specification. If not present, cc-pVDZ is used
   geometry={...}               !geometry specification
   
   var1=value,var2=value,...    !setting variables for geometry and/or wavefunction definitions
   
   {command,options             !program or procedure name
    directive,data,option       !directives for command (optional)
   ...
   }                            !end of command block
   ---                          !end of input (optional)

If the memory card is given, it should be the first card (after the optional title card). If any file cards are given, they should follow immediately. The order of ``basis``, ``geometry``, ``gprint``, ``gdirect``, ``gthresh``, ``gexpec``, and variable definitions is arbitrary. It is possible to call several programs one after each other. It is also possible to redefine basis set and/or geometry between the call to programs; the program will recognize automatically if the integrals have to be recomputed.

.. _general_program_structure--files:

Files
=====

Molpro uses three sequential text files, namely the *input file*, the *output file*, and the *punch file*. The punch file is a short form of the output which contains the most important data and results, such as geometries, energies, dipole moments, etc. The punch file can be processed by the separate program *READPUN*, which selects specific results by keywords and is able to produce ordered tables in user supplied format. Furthermore, there are up to 9 binary Molpro files available, each one known to the program simply by its number (1 to 9). By default, they are temporary files, usually allocated dynamically by the program, but they can be connected to permanent files with the ``FILE`` command. Each file is direct access, and word addressable (word=64 bit usually), but is organised in *records* of any length. The name, address and length of each record is held in a directory at the start of the file.

File 1 is the *main file*, holding basis set, geometry, and the one and two electron integrals. By default, file 2 is the *dump file* and used to store the wavefunction information, i.e. orbitals, CI coefficients, and density matrices. File 3 is an auxiliary file which can be used in addition to file 2 for restart purposes. Often files 1 and 2 (and 3) are declared as permanent files (see ``FILE``) to enable restarts. Storing the wavefunction information on file 2 is useful, since the integral file is overwritten at each new geometry, while the orbitals and CI coefficients of one calculation can be used as a starting guess for the next calculation at a neighbouring geometry. Files 4 to 8 are used as scratch space, e.g., for sorting the integrals, storage of transformed integrals and of the CI vectors. These files should normally not be made permanent.

Note that the file name appearing in molpro input is always converted to lower case on unix machines.

.. _general_program_structure--records:

Records
=======

Record names are positive integers, and are usually referred to in the format *record.file*, e.g., 2100.2 means the record called 2100 on file 2. Note that these names are quite arbitrary, and their numerical values have nothing to do with the order of the records in the file. Record names :math:`\le` 2000 are reserved for standard quantities (e.g. integrals, properties etc.) and you should never use these in an input, unless you know exactly what you are doing. Some important default records to remember are

* **2100** RHF dump record (closed and open-shell)
* **2200** UHF dump record
* **2140** MCSCF dump record
* **4100** CPHF restart information
* **5000** MCSCF gradient information
* **5100** CP-MCSCF gradient information
* **5200** MP2 gradient information
* **5300** Hessian restart information
* **5400** Frequencies restart information
* **6300** Domain restart information

If an input contains several wavefunction calculations of the same type, e.g., several MCSCF calculations with different active spaces, the record number will be increased by 1 for each calculation of the same type. Thus, the results of the first SCF calculation in an input are stored in dump record 2100.2, the second SCF in record 2101.2, the first MCSCF in 2140.2, the second MCSCF in 2141.2 and so on. Note that these numbers refer to the occurrence in the input and not on the order in which the calculations are performed in the actual run. If an input or part of it is repeated using ``DO`` loops, this ensures that each calculation will start with the orbitals from the corresponding orbitals from the previous cycle, as long as the order of the commands in the input remains unchanged. If for instance the first SCF would be skipped in the second cycle using some ``IF`` / ``ENDIF`` structure, the second SCF would still use record 2101.2. Thus, under most circumstances the program defaults are appropriate, and the user does not have to specify the records.

After a restart this logic will still work correctly if the number and sequence of ``SCF`` and ``MCSCF`` commands is kept unchanged. Thus, if you want to skip certain parts of the input after a restart, it is recommended to use ``IF`` / ``ENDIF`` structures or the ``GOTO`` command rather than to delete or comment certain commands. If for some reason this is not possible, the ``START`` and ``ORBITAL`` directives can be used to specify explicitely the records to be used.

In general we recommend the use of program defaults whenever possible, since this minimizes the probability of input errors and frustration!

After completion of each program step, Molpro prints a summary of the records on each file.

.. _general_program_structure--restart:

Restart
=======

Information from the permanent files is automatically recovered in subsequent calculations. This can be controlled using the ``RESTART`` directive.

.. _general_program_structure--data-set-manipulation:

Data set manipulation
=====================

It is possible to truncate files and rename or copy records using the ``DATA`` command. Several standard matrix operations can be performed with ``MATROP``, e.g., printing records, linearly combining or multiplying matrices, or forming the trace of a product of two matrices.

.. _general_program_structure--memory-allocation:

Memory allocation
=================

Molpro can allocate memory dynamically as required by the user. Thus it is not necessary to maintain different versions of the program with different memory sizes. There are two ways to specify the memory: (1) ``MEMORY`` card in Molpro input file; (2) options ``-m`` or ``--memory`` or ``-M`` in the Molpro command line. The latter method is recommended. Please refer to sections `memory specifications <running_molpro_on_parallel_computers.html#memory-specifications>`__ for more details and important information regarding parallel processing.

If memory is specified using both methods at the same time, ``MEMORY`` card will take precedence. If both ways are omitted, the program will use a default memory size (currently it is :math:`32000000` words, i.e. 256 MB). Please note that: (1) memory specification is in megawords. 1 word is 8 bytes (i.e., the memory size to store one double precision data). (2) memory specification is for each process.

.. _general_program_structure--memory-directive-in-the-input-file:

Memory directive in the input file
==================================

``MEMORY,[STACK=]m,[GA=G],[Total=M],[GA_PREALLOC=$0|1$]``

By default, all memory specifications are in megawords. The numbers (*m, G, M*) can be appended by a scaling unit, which can be ``K``, ``M``, or ``G`` (case insensitive). If the unit is ``K``, the specification is assumed to be in kilowords (:math:`10^3` words), ``M`` means megawords (:math:`10^6` words), and ``G`` means gigawords (:math:`10^9` words). Blanks or commas have to be inserted between the number and the unit, i.e., 100 m or 100,m are possible specifications of the memory size.

Examples:

* ``MEMORY,90`` requests 90 000 000 words of memory
* ``MEMORY,500 K`` requests 500 000 words of memory
* ``MEMORY,2 M`` requests 2 000 000 words of memory
* ``MEMORY,100,M`` requests 100 000 000 words of memory
* ``memory,100 m`` requests 100 000 000 words of memory
* ``MEMORY,1 g`` requests :math:`10^9` words of memory

Optionally, the requested GA space or the total allocatable memory (stack memory + GA) can be used. These options have the same meaning and effect as the ``-G`` and ``-M`` command line options, cf. section `memory specifications <running_molpro_on_parallel_computers.html#memory-specifications>`__. ``GA_PREALLOC=0`` or ``GA_PREALLOC=1`` disables or enables GA preallocation, respectively (see sections `GA Installation notes <running_molpro_on_parallel_computers.html#ga-installation-notes>`__ and `memory specifications <running_molpro_on_parallel_computers.html#memory-specifications>`__).

.. _general_program_structure--memory-option-in-command-line:

Memory option in command line
=============================

``-m $|$ --memory nscale``

The ``scale`` (``k``, ``m``, ``g`` and ``K``, ``M``, ``G``) is case sensitive, lower case for decimal and upper case for binary. ``k, m, g`` stand for 1000, 1000 000 and :math:`10^9`; ``K, M, G`` stand for :math:`2^{10}`, :math:`2^{20}` and :math:`2^{30}`.

Examples:

* ``-m 1k`` requests 1000 words of memory
* ``-m 1K`` requests 1024 words of memory
* ``-m 1m`` requests 1000000 words of memory
* ``-m 1M`` requests 1048576 words of memory
* ``-m 1g`` requests :math:`10^9` words of memory
* ``-m 1G`` requests :math:`2^{30}` words of memory

For more information please refer to section `memory specifications <running_molpro_on_parallel_computers.html#memory-specifications>`__.

.. _general_program_structure--memory-in-parallel:

Memory in parallel
==================

The memory specification is for each process. So the total requested memory in parallel calculation will be the specified memory amount multiplied by the number of compute processes. For example, specifying :math:`100 * 10^6` words for a job with 4 compute processes:

* ``memory,100,m`` in input file
* ``-m 100m`` in command line

the total requested memory will be :math:`100 * 10^6 * 8 * 4 = 3.2 * 10^9` bytes.

In addition, some methods need an significant amount of global array (GA) memory. Please refer to sections `GA Installation notes <running_molpro_on_parallel_computers.html#ga-installation-notes>`__ and `memory specifications <running_molpro_on_parallel_computers.html#memory-specifications>`__ for important information regarding parallel processing.

.. _general_program_structure--multiple-passes-through-the-input:

Multiple passes through the input
---------------------------------

It is possible to perform loops over parts of the input using ``DO`` loops, very much as in ``FORTRAN`` programs. ``DO`` loops may be nested to any reasonable depth. This can be conveniently used, for instance, to compute automatically whole potential energy surfaces.

.. _general_program_structure--symmetry:

Symmetry
--------

Molpro can use Abelian point group symmetry only. For molecules with degenerate symmetry, an Abelian subgroup must be used — e.g., :math:`C_{2v}` or :math:`D_{2h}` for linear molecules. The symmetry group which is used is defined in the integral input by combinations of the symmetry elements :math:`x`, :math:`y`, and :math:`z`, which specify which coordinate axes change sign under the corresponding generating symmetry operation. It is usually wise to choose :math:`z` to be the unique axis where appropriate (essential for :math:`C_2` and :math:`C_{2h}`). The possibilities in this case are shown in Table `symmetry <general_program_structure.html#symmetry>`__.

Normally, Molpro determines the symmetry automatically, and rotates and translates the molecule accordingly. However, explicit symmetry specification is sometimes useful to fix the orientation of the molecule or to use lower symmetries.

.. list-table::
   :header-rows: 2

   * - The symmetry generators for the point groups
     - 
   * - Generators
     - Point group
   * - (null card)
     - :math:`C_1` (i.e. no point group symmetry)
   * - ``X`` (or ``Y`` or ``Z``)
     - :math:`C_s`
   * - ``XY``
     - :math:`C_2`
   * - ``XYZ``
     - :math:`C_i`
   * - ``X,Y``
     - :math:`C_{2v}`
   * - ``XY,Z``
     - :math:`C_{2h}`
   * - ``XZ,YZ``
     - :math:`D_2`
   * - ``X,Y,Z``
     - :math:`D_{2h}`

The irreducible representations of each group are numbered 1 to 8. Their ordering is important and given in the tables below. Also shown in the tables are the transformation properties of products of :math:`x`, :math:`y`, and :math:`z`. :math:`s` stands for an isotropic function, e.g., :math:`s` orbital, and for these groups, this gives also the transformation properties of :math:`x^2`, :math:`y^2`, and :math:`z^2`. Orbitals or basis functions are generally referred to in the format  *number.irrep*, i.e. 3.2 means the third orbital in the second irreducible representation of the point group used.

.. list-table::
   :header-rows: 2

   * - Numbering of the irreducible representations in :math:`D_{2h}`
     - 
     - 
   * - No.
     - Name
     - Function
   * - 
     - :math:`D_{2h}`
     - 
   * - 1
     - :math:`A_{g}`
     - :math:`s`
   * - 2
     - :math:`B_{3u}`
     - :math:`x`
   * - 3
     - :math:`B_{2u}`
     - :math:`y`
   * - 4
     - :math:`B_{1g}`
     - :math:`xy`
   * - 5
     - :math:`B_{1u}`
     - :math:`z`
   * - 6
     - :math:`B_{2g}`
     - :math:`xz`
   * - 7
     - :math:`B_{3g}`
     - :math:`yz`
   * - 8
     - :math:`A_{u}`
     - :math:`xyz`

.. list-table::
   :header-rows: 2

   * - Numbering of the irreducible representations in the four-dimensional groups
     - 
     - 
     - 
     - 
     - 
     - 
   * - No.
     - Name
     - Function
     - Name
     - Function
     - Name
     - Function
   * - 
     - :math:`C_{2v}`
     - 
     - :math:`C_{2h}`
     - 
     - :math:`D_2`
     - 
   * - 1
     - :math:`A_1`
     - :math:`s, z`
     - :math:`A_g`
     - :math:`s, xy`
     - :math:`A`
     - :math:`s`
   * - 2
     - :math:`B_1`
     - :math:`x, xz`
     - :math:`A_u`
     - :math:`z`
     - :math:`B_3`
     - :math:`x, yz`
   * - 3
     - :math:`B_2`
     - :math:`y, yz`
     - :math:`B_u`
     - :math:`x, y`
     - :math:`B_2`
     - :math:`y, xz`
   * - 4
     - :math:`A_2`
     - :math:`xy`
     - :math:`B_g`
     - :math:`xz, yz`
     - :math:`B_1`
     - :math:`xy`

.. list-table::
   :header-rows: 2

   * - Numbering of the irreducible representations in the two-dimensional groups
     - 
     - 
     - 
     - 
     - 
     - 
   * - No.
     - Name
     - Function
     - Name
     - Function
     - Name
     - Function
   * - 
     - :math:`C_{s}`
     - 
     - :math:`C_{2}`
     - 
     - :math:`C_{i}`
     - 
   * - 1
     - :math:`A^{'}`
     - :math:`s, x, y, xy`
     - :math:`A`
     - :math:`s, z, xy`
     - :math:`A_g`
     - :math:`s, xy, xz, yz`
   * - 2
     - :math:`A^{''}`
     - :math:`z, xz, yz`
     - :math:`B`
     - :math:`x, y, xz, yz`
     - :math:`A_u`
     - :math:`x, y, z`

.. _general_program_structure--defining-the-wavefunction-wf:

Defining the wavefunction (WF)
------------------------------

In all program modules where such information is required, the total symmetry of the :math:`N`-electron wavefunction is defined on ``WF`` (wavefunction) cards in the following way:

``WF,nelec,irrep,spin``

or, alternatively

``WF,[NELEC=nelec],[SYM[METRY]=irrep],[spin=spin],[CHARGE=charge]``

where *nelec* is the total number of electrons, *irrep* is the number of the irreducible representation, and *spin* equals :math:`2 \times S`, where :math:`S` is the total spin quantum number. Instead of *nelec* also *charge* can be given, which specifies the total charge of the molecule. For instance, for a calculation in :math:`C_{2v}` symmetry with 10 electrons, ``WF,10,3,0`` denotes a :math:`^1B_2` state, and ``WF,10,1,2`` a :math:`^3A_1` state. The charge can also be defined by setting the variable ``CHARGE``:

``SET,CHARGE=charge``

This charge will be used in all energy calculations following this input. Note that ``SET`` is required, since ``CHARGE`` is a system variable (cf. section `system variables <variables.html#system-variables>`__).

Although in principle each program unit requires a ``WF`` command, in practice it is seldom necessary to give it. The program remembers the information on the ``WF`` card, and so one might typically specify the information in an SCF calculation, but then not in subsequent MCSCF or CI calculations; this also applies across restarts. *nelec* defaults to the sum of the nuclear charges. Molpro attempts to find the ground state configuration from the Aufbau principle and sets *spin* and *irrep* correspondingly; thus in many cases, it is not necessary to specify a ``WF`` card at all.

If the ``WF`` directive is given outside an command input block, it is treated as global, i.e., the given values are used for all subsequent calculations. Setting the variables ``NELEC``, ``SPIN``, or ``SYMMETRY``, has the same effect giving these on a global ``WF`` directive. If the global ``WF`` directive is given after the variable definition, the values of the variables are replaced by the values given on the ``WF`` directive. Vice versa, if a variable definition follows a global ``WF`` directive, the new value of the variable is used in the following. Note that ``WF`` input cards in command blocks have preference over global ``WF`` directives or input variables.

.. _general_program_structure--defining-orbital-subspaces-occ-closed-core-frozen:

Defining orbital subspaces (OCC,CLOSED,CORE,FROZEN)
---------------------------------------------------

In the SCF, MCSCF, and CI programs it may be necessary to specify how many orbitals in each symmetry are *occupied* (or *internal* in CI), and which of these are *core* or *closed shell* (doubly occupied in all CSFs). This information is provided on the ``OCC``, ``CORE``, and ``CLOSED`` cards in the following way:

``OCC,$m_1,m_2,\ldots,m_8$; CORE,$co_1,co_2,\ldots,co_8$; CLOSED,$cl_1,cl_2,\ldots,cl_8$; FROZEN,$fr_1,fr_2,\ldots,fr_8$;``

where :math:`m_i` is the number of occupied orbitals (including core/frozen and closed), :math:`co_i` the number of core orbitals, and :math:`cl_i` is the number of closed-shell orbitals (including the core orbitals) in the irreducible representation :math:`i`. In general, $m_i \ge
cl_i\ :math:`, and`\ cl_i \ge co_i$. It is assumed that these numbers refer to the first orbitals in each irrep. ``FROZEN`` only exists in the MCSCF program and denotes frozen core orbitals that are not optimized (note that in older Molpro versions frozen core orbitals were denoted ``CORE``).

For ``CORE`` the following special input possibilities exist (also available as global CORE command):

``CORE,SMALL\\``
``CORE,MIXED\\``
``CORE,LARGE\\``
``CORE,SYM1=spdf,SYM2=spdf,...``

``SMALL`` means that all atomic orbitals are correlated for which the cc-pwCVXZ basis are optimized (typically one additional shell of each angular momentum below the valence shell). For :math:`n`\ d transition metals, the :math:`n`\ s, :math:`(n+1)`\ s, :math:`n`\ p, :math:`n`\ d orbitals are correlated.

``MIXED`` corresponds to ``SMALL`` but the next lower s and p shells of the p-block elements are not correlated.

Note that until Molpro 2021.3, the 2s and 2p shells of the second-row elements Al - Ar were correlated with ``MIXED``, but for consistency this has been changed in 2021.4. The old behaviour can be recovered using ``MIXED_OLD``.

``LARGE`` means that no inner shells are correlated (default). In transition metals the outermost d-shell and in f-elements the outermost f-shell are treated as valence and always correlated.

The most general core definition is possible using the last possibility, where *SYM1, SYM2* etc are atomic symbols and *spdf* are the numbers of core orbitals at the given atom for each angular momentum. For example, for bromine ``CORE,Br=21`` is equivalent to ``CORE,SMALL``, ``CORE,Br=32`` is equivalent to ``CORE,MIXED``, and ``CORE,Br=321`` is equivalent to ``CORE,LARGE``. Trailing zeros are optional, i.e. Br=3200, 320, or 32 are equivalent. Atom-specific core specifications cannot exceed the number of large core orbitals for each angular momentum.

Optionally, SMALL, MIXED, or LARGE can be followed by specifications for individual atoms. In this case these default apply to all atoms that are not explicitly specified.

The table below summarizes the number of shells that are **not** correlated with the three core-orbital specifications.
The cases where mixed and small differ are shown as italic.
Note that for the post-d p-block elements "mixed" includes correlation of the outermost d-shell, which is not the case for the large core.
For calculations including outer core orbitals the correlation consistent CVXZ or (preferably) wCVXZ basis sets [K. A. Peterson, and T. H. Dunning Jr., `J. Chem. Phys. <https://doi.org/10.1063/1.1520138>`__ **117**, 10548--10560 (2002)] should be used.
But note these are not appropriate to correlate inner-shell core electrons.

.. list-table::
   :header-rows: 2

   * - 
     - 
     - 
     - Number of shells
     - 
     - 
     - 
   * - Elements
     - Outer core
     - Valence
     - All occupied
     - Large core
     - Small core
     - Mixed core
   * - 
     - 
     - 
     - (spdf)
     - (spdf)
     - (spdf)
     - (spdf)
   * - Z=1,2
     - 1s
     - 
     - (1000)
     - (0000)
     - (0000)
     - (0000)
   * - Z=3-4
     - 1s
     - 2s
     - (2000)
     - (1000)
     - (0000)
     - (0000)
   * - Z=5-10
     - 1s
     - 2s2p
     - (2100)
     - (1000)
     - (0000)
     - *(1000)*
   * - Z=11-12
     - 2s2p
     - 3s
     - (3100)
     - (2100)
     - (1000)
     - (1000)
   * - Z=13-18
     - 2s2p
     - 3s3p
     - (3200)
     - (2100)
     - (1000)
     - *(2100)*
   * - Z=19-20
     - 3s3p
     - 4s
     - (4200)
     - (3200)
     - (2100)
     - (2100)
   * - Z=21-30
     - 3s3p
     - 4s3d
     - (4210)
     - (3200)
     - (2100)
     - (2100)
   * - Z=31-36
     - 3s3p3d
     - 4s4p
     - (4310)
     - (3210)
     - (2100)
     - *(3200)*
   * - Z=37-38
     - 4s4p
     - 5s
     - (5310)
     - (4310)
     - (3210)
     - (3210)
   * - Z=39-48
     - 4s4p
     - 5s4d
     - (5320)
     - (4310)
     - (3210)
     - (3210)
   * - Z=49-54
     - 4s4p4d
     - 5s5p
     - (5420)
     - (4320)
     - (3210)
     - *(4310)*
   * - Z=55-56
     - 5s5p
     - 6s
     - (6420)
     - (5420)
     - (4320)
     - (4320)
   * - Z=57-71
     - 4s4p4d
     - 5s6s5p5d4f
     - (6431)
     - (4320)
     - (3210)
     - (3210)
   * - Z=72-80
     - 5s5p
     - 6s5d
     - (6431)
     - (5421)
     - (4321)
     - (4321)
   * - Z=81-86
     - 5s5p5d
     - 6s6p
     - (6531)
     - (5431)
     - (4321)
     - *(5421)*
   * - Z=87-88
     - 6s6p
     - 7s
     - (7531)
     - (6531)
     - (5431)
     - (5431)
   * - Z=89-103
     - 5s5p5d
     - 6s7s6p6d5f
     - (7542)
     - (5431)
     - (4321)
     - (4321)
   * - Z=104-112
     - 6s6p
     - 7s6d
     - (7542)
     - (6532)
     - (5432)
     - (5432)
   * - Z=113-118
     - 6s6p6d
     - 7s7p
     - (7642)
     - (6542)
     - (5432)
     - (5432)

The program automatically checks if the orbitals with the lowest orbital energies correspond to the requested core orbitals, and if necessary orbitals are swapped as required. Within the set of core orbitals, this check can only be performed if ``SMALL`` or ``MIXED`` is given. If one specifies the absolute number of core orbitals the check is not possible since the program does not know which type the core orbitals should have.

Note that the ``OCC`` and ``CLOSED`` cards have slightly different meanings in the SCF, MCSCF and CI or CCSD programs. In SCF and MCSCF, *occupied* orbitals are those which occur in any of the CSFs. In electron correlation methods (CI, MPn, CCSD etc), however, ``OCC`` denotes the orbitals which are occupied in any of the *reference* CSFs. In the MCSCF, ``FROZEN`` orbitals are doubly occupied in all CSFs and *frozen* (not optimized), while  *closed* denotes all doubly occupied orbitals (frozen plus optimized). In the CI and CCSD programs, *core* orbitals are those which are not correlated and *closed* orbitals are those which are doubly occupied in all reference CSFs.

``OCC``, ``CORE`` and ``CLOSED`` directives are generally required in each program module where they are relevant; however, the program remembers the most recently used values, and so the directives may be omitted if the orbital spaces are not to be changed from their previous values. Note that this information is also preserved across restarts. Note also, as with the ``WF`` information, sensible defaults are assumed for these orbital spaces. For full details, see the appropriate program description.

The orbital spaces may also be defined outside command blocks, and then the directive is treated as global, i.e., it is used in all subsequent programs. Spaces specific to certain wavefunction types can be defined by specifying the program name with a ``CONTEXT`` option, e.g.,

``OCC,4,2,1,CONTEXT=MULTI``

Alternatively, the context can be appended to the directive name with an underscore. For example

``OCC_MULTI,4,2,1``

is equivalent to the previous form.

The occupation and core settings are usually molecule specific and depend on the symmetry and charges. They can also change if dummy atoms are defined. Therefore, global settings should be used with care. In molpro2021.4 or later it is possible to specify global core types (``CORE,SMALL|MIXED|LARGE``); these work also if the molecule or symmetry changes, or if dummy atoms are used. Specifying core orbitals in this way is preferable since the orbitals are appropriately reordered, if necessary (see above). Note that contexts cannot be given if core types are given; also atom-specific core definitions are only possible within command blocks.

Local input given within command blocks has preference over global input.

.. _general_program_structure--selecting-orbitals-and-density-matrices-orbital-density:

Selecting orbitals and density matrices (ORBITAL, DENSITY)
----------------------------------------------------------

[sec:orbitals] As outlined in section `records <general_program_structure.html#records>`__, the information for each SCF or MCSCF calculation is stored in a *dump record*. Dump records contain orbitals, density matrices, orbital energies, occupation numbers, fock matrices and other information as wavefunction symmetries etc. Subsequent calculation can access the orbitals and density matrices from a particular record using the ``ORBITAL`` and ``DENSITY`` directives, respectively. These input cards have the same structure in all programs. The general format of the ``ORBITAL`` and ``DENSITY`` directives is as follows:

``ORBITAL[,[RECORD=]record] [,[TYPE=]orbtype] [,STATE=state] [,SYM[METRY]=symmetry]]``

``DENSITY[,[RECORD=]record] [,[TYPE=]dentype] [,STATE[B]=stateb] [,SYM[B]=symb] [,SPIN[B]=spinb] [,MS2[B]=ms2b] [,STATEK=statek] [,SYMK=symk] [,SPINK=spink] [,MS2K=ms2k] [,[N]ELEC=nelec] [,SET=iset]``

where the (optional) specifications can be used to select specific orbitals or densities, if several different orbital sets are stored in the same record. If a specification is not given, it is not checked and the last written set that fulfills all other criteria is used. The meaning of the individual specifications are as follows:

* ***orbtype*** Orbital type. This can be one of

``CANONICAL``: canonical or pseudo-canonical orbitals;
``NATURAL: natural orbitals;\\``
``LOCAL: localized orbitals;\\``
``LOCAL(PM): localized Pipek-Mezey orbitals;\\``
``LOCAL(BOYS): localized Boys orbitals;\\``
``PROJECTED``: projected virtual orbitals used in local calculations.
Without further specification, the most recently computed orbitals of the specified type are used. If the orbital type is not specified, the program will try to find the most suitable orbitals automatically. For instance, in MRCI calculations ``NATURAL`` orbitals will be used preferentially if available; MRPT (CASPT2) calculations will first search for ``CANONICAL`` orbitals, and local calculations will first look for ``LOCAL`` orbitals. Therefore, in most cases the orbital type needs not to be specified.

* ***state*** Specifies a particular state in the form :math:`istate.isym`. For instance, 2.1 refers to the second state in symmetry 1. This can be used if density matrices or natural orbitals have been computed for different states in a state-averaged CASSCF calculation. If not given, the last written orbitals are used. A state-averaged density can be selected using ``STATE=AV[ERAGED]``. The specification of :math:`isym` is optional; it can also be defined using the ``SYMMETRY`` key.
* ***dentype*** Density type. This can be one of

``CHARGE: charge density;\\``
``SPIN: UHF spin density;\\``
``TRANSITION: transition density matrix;\\``
The default is ``CHARGE``.

* ***symmetry*** Specifies a particular state symmetry. Alternatively, the state symmetry can be specified using ``STATE`` (see above).
* ***spin*** Spin quantum number, i.e. 0 for singlet, 1/2 for doublet, 1 for triplet, etc. Alternatively ``MS2`` can be used.
* ***ms2*** :math:`2 M_S`, i.e. 0 for singlet, 1 for doublet, 2 for triplet etc. Alternatively, ``SPIN`` can be used.
* ***nelec*** Number of electrons.
* ***iset*** Set number of orbitals. The orbital sets are numbered in the order they are stored.

In some cases (e.g. in ``MATROP``) transition density matrices can be specified. In this case ``STATEB``, ``SYMB``, ``MS2B``, ``SPINB`` refer to the bra state and ``STATEK``, ``SYMK``, ``MS2K``, ``SPINK`` refer to the ket state. If bra and ket differ, ``TYPE=TRANSITION`` is implied, and ``SYMMETRY`` is automatically set to the product symmetry of bra and ket. If ``STATEK``, ``SYMK``, ``MS2K``, ``SPINK`` are not given, they are assumed to be equal to the corresponding bra quantities. See section :doc:`matrix operations <matrix_operations>` for examples.

If ``OVL`` is specified, the starting orbitals are obtained by maximizing the overlap with previous orbitals. By default, this is used if the basis dimension of the previous orbitals is different then the current one. If ``OVL`` is specified this procedure is used even if the basis dimensions are the same, which is occasionally useful if the contraction scheme changed.

If ``NOCHECK`` is specified, some consistency checks for finding correct orbitals are skipped, and error messages like "ORBITALS CORRESPOND TO DIFFERENT GEOMETRY" are ignored.

If ``IGNORE_ERROR`` is specified, MPn or triples calculations can be forced with other than canonical orbitals. Note that this can lead to meaningless results! Note that in MULTI ``IGNORE_ERROR`` must be given on the ``START`` directive, since in this program ``ORBITAL`` is used to define the new orbitals.

If any of the above options are given, they must be obeyed strictly, i.e., the program aborts if the request cannot be fulfilled.

Examples:

.. code-block:: text

   ORBITAL,2100.2                    !Use SCF orbitals
   ORBITAL,2140.2                    !Use (state-averaged) MCSCF orbitals
   ORBITAL,2140.2,CANONICAL          !use canonical MCSCF orbitals
   ORBITAL,2140.2,NATURAL,STATE=2.1  !use natural MCSCF orbitals for second state in sym. 1

.. _general_program_structure--plugins:

Plugins
-------

Molpro can host suitably prepared external programs as “plugins”. They are launched using MPI’s spawn mechanism, and therefore the user must take care of any job-scheduling constraints on the number and placement of MPI processes. The following syntax in the input file will cause the plugin to be launched.

``PLUGIN,COMMAND=command,PROCS=procs``

*command* is the name of the executable of the plugin. It can be given as an absolute path name, or a relative path. If it is a simple name (no ``/`` characters), it will be searched for in the same directory as Molpro’s executable, and this will be the normal mode of use. If the plugin is not found, and *command* does not have a filename suffix, then the suffix ``.exe`` will be assumed.

``PROCS=``\ *procs* specifies the number of processes for the plugin, and can be omitted, in which case the number is the same as in the host Molpro instance.

Example:

.. code-block:: text

   PLUGIN, COMMAND='Block', PROCS=128

Most plugins work by requesting the information they need from Molpro. This is typically information about the molecule and hamiltonian, plus an input file consisting of options. For some plugins, Molpro is aware of the structure of this input file, and will construct it by merging user-specified options with defaults. For example,

.. code-block:: text

   GLOBAL,FCIQMC,TIME=20,CALCRDMONFLY=3
   PLUGIN,COMMAND='neci'

.. _general_program_structure--summary-of-keywords-known-to-the-controlling-program:

Summary of keywords known to the controlling program
----------------------------------------------------

This is a summary of all keywords presently implemented in the controlling program. Each module knows further keywords, which are described in the chapters about the individual programs. For detailed information about the use of the commands listed below, consult the following chapters.

* ***Program control:***
* ``**`` indicates start of a new calculation
* ``MEMORY`` allocates dynamic memory
* ``PUNCH`` opens a punch file
* ``FILE`` connects units to permanent files
* ``RESTART`` recovers file information
* ``INCLUDE`` includes other input files
* ``BASIS`` can be used to define default basis sets
* ``GEOMETRY`` can be used to specify the geometry
* ``ZMAT`` can be used to define the Z-matrix
* ``PARALLEL`` can be used to control parallelization
* ``STATUS`` checks status of program steps
* **``PRINT``,\ ``GPRINT``** controls global print levels
* **``THRESH``,\ ``GTHRESH``** controls global thresholds
* **``DIRECT``,\ ``GDIRECT``** flags direct computation of integrals and for setting direct options
* **``EXPEC``,\ ``GEXPEC``** controls computation of expectation values
* ``TEXT`` prints text
* ``EXIT`` stops execution
* ``DO`` controls do loops
* ``ENDDO`` end of do loops
* ``IF`` controls conditional actions
* ``ELSEIF`` controls conditional actions
* ``ENDIF`` end of ``IF block``
* ``GOTO`` used to skip part of input and for loops over input
* ``LABEL`` no action
* ``DATA`` data set management
* **``DELETE``, ``ERASE``** data set deletion
* ``MATROP`` performs matrix operations
* ``GRID`` Define grid
* ``CUBE`` Dump data to grid
* ``CARTESIAN`` Use cartesian basis functions
* ``SPHERICAL`` Use spherical harmonic basis functions
* ``USER`` calls user-supplied subroutine
* ``---`` last line of input

* ***Variables:***
* ``SET`` sets variables (obsolete)
* ``SETI`` sets variables or numbers to their inverse (obsolete)
* ``SETA`` sets variable arrays (obsolete)
* ``CLEAR`` clears variables
* ``CLEARALL`` clears all variables
* ``GETVAR`` recovers variables from file
* ``SHOW`` displays the values of variables
* ``TABLE`` prints tables

* ***Wave function optimization:***
* ``INT`` calls the machine default integral program. This is optional and needs not to be given.
* ``LSINT`` calls the spin-orbit integral program
* ``CPP`` compute core polarization potential integrals
* **``HF`` or ``RHF``** calls spin-restricted Hartree-Fock program (open or closed shell)
* ``UHF`` calls spin-unrestricted Hartree-Fock program
* ``DFT`` calls the density functional program
* **``KS``, ``RKS``** call the Kohn-Sham spin restricted density functional program
* ``UKS`` call the Kohn-Sham spin-unrestricted density functional program
* **``MULTI``, ``MCSCF``, or ``CASSCF``** calls MCSCF/CASSCF program
* ``CASVB`` calls the CASVB valence bond program
* **``CI``, ``MRCI``, or ``CI-PRO``** calls internally contracted MRCI program (only pairs contracted)
* **``CIC`` or ``MRCIC``** calls the faster internally contracted MRCI program (pairs and singles contracted)
* ``CIPT2`` calls internally contracted CIPT2 program
* **``ACPF``, ``AQCC``** calls internally contracted MR-ACPF program
* ``CEPA`` calls single-reference CEPA program (closed- or open-shell)
* **``RS2``, ``RS3``** calls internally contracted multireference perturbation theory program (only pairs contracted)
* **``CASPT2`` or ``RS2C``** calls faster program for internally contracted multireference perturbation theory
* ``NEVPT2`` calls NEVPT2 program
* ``MP2`` calls closed-shell MP2 program
* ``MP3`` calls closed-shell MP3 program
* ``MP4`` calls closed-shell MP4 program
* ``CISD`` calls closed-shell CISD program
* ``CCSD`` calls closed-shell coupled cluster program
* ``DCSD`` calls closed-shell distingusihable cluster program
* ``BCCD`` calls closed-shell Brueckner CCD program
* **``QCI``,\ ``QCSID``** calls closed-shell quadratic configuration interaction program
* ``UCCSD`` calls spin-unrestricted open-shell coupled cluster program (based on RHF reference function)
* ``RCCSD`` calls spin-restricted open-shell coupled cluster program (based on RHF reference function)
* **``FCI`` or ``FULLCI``** calls determinant based full CI program

* ***Local correlation methods:***
* ``LMP2`` calls closed-shell PAO-LMP2 program
* ``LMP3`` calls closed-shell PAO-LMP3 program
* ``LMP4`` calls closed-shell PAO-LMP4 program
* ``LCISD`` calls closed-shell PAO-LCISD program
* ``LCCSD`` calls closed-shell PAO-LCCSD program
* ``PNO-LMP2`` calls PNO-LMP2 program
* ``PNO-LCCSD`` calls PNO-LCCSD program, equivalent to ``PNO-RCCSD``
* ``PNO-RCCSD`` calls PNO-RCCSD program
* ``PNO-UCCSD`` calls PNO-UCCSD program
* ``PNO-CASPT2`` calls PNO-CASPT2 program

* ***Explicitly correlated methods:***
* ``MP2-R12`` calls MP2-R12 program
* ``MP2-F12`` calls MP2-F12 program
* ``CCSD-F12`` calls CCSD-F12 program
* ``LMP2-R12`` calls PAO-LMP2-R12 program
* ``LMP2-F12`` calls PAO-LMP2-F12 program
* ``LCCSD-F12`` calls PAO-LCCSD-F12 program
* ``PNO-LMP2-F12`` calls PNO-LMP2-F12 program
* ``PNO-LCCSD-F12`` calls PNO-LCCSD-F12 program, equivalent to ``PNO-RCCSD-F12``
* ``PNO-RCCSD-F12`` calls PNO-RCCSD-F12 program
* ``PNO-UCCSD-F12`` calls PNO-UCCSD-F12 program
* ``RS2-F12`` calls explicitly correlated multireference perturbation theory program
* ``MRCI-F12`` calls explicitly correlated internally contracted MRCI program

* ***Orbital manipulation:***
* ``LOCALI`` calls orbital localization program
* ``MERGE`` calls orbital manipulation program

* ***Properties and wavefunction analysis:***
* ``POP`` calls population analysis program
* ``DMA`` calls distributed multipole analysis program
* **``IBBA`` or ``IBO``** calls intrinsic bond orbital analysis program
* ``PROPERTY`` calls properties program
* ``DIP`` adds dipole field to :math:`h`
* ``QUAD`` adds quadrupole field to :math:`h`
* ``LATTICE`` read or disable lattice of point charges
* ***Gradients and geometry optimization:***
* ``FORCES`` calls gradient program
* ``OPTG`` performs automatic geometry optimization
* ``MIN`` performs energy minimization with respect to some parameters
* ``PUT`` print or write geometry to a file
* ``HESSIAN`` calculate Hessian
* ``FREQUENCY`` calculate vibrational frequencies
* ``MASS`` define atomic masses
* ``DDR`` evaluates approximate non-adiabatic coupling matrix elements

The command names for single reference coupled cluster methods ``QCISD, CCSD, LQCISD, LCCSD, PNO-LCCSD, PNO-RCCSD, PNO-UCCSD`` (including the explicitly correlated variants) can be appended by ``(T)`` and then a perturbative correction for triple excitations will be computed (e.g., ``CCSD(T)``, ``PNO-LCCSD(T)-F12`` etc.)

``HF``, ``KS``, ``UHF``, ``UKS``, ``MP2``, ``CCSD``, ``MCSCF``, ``RS2``, and all PAO-based local correlation methods can be prepended by ``DF-`` to invoke density fitting (PNO always implies density fitting).

``HF``, ``KS``, ``UHF``, ``UKS`` can be pretended by ``LDF-`` to invoke local density fitting approximations.

.. _general_program_structure--molpro-help:

Molpro help
-----------

The help command can be used to obtain a short description of commands, input parameters, and variables. The syntax is:

``HELP,set,name,[keys]``

where *set* is either ``COMMAND``, ``VARIABLE``, or the name of the input set (e.g., ``THRESH``, ``PRINT``, ``LOCAL``, ``EOM``, ``CFIT``), and *name* is the name of the parameter. If *name* is blank, all parameters of the set are shown. Optionally, *keys* can be specified to request specific information (e.g., ``short_description``, ``long_description``, ``default_value``, ``type``, ``program``). If *keys* are not given, ``short_description`` is assumed.

.. code-block:: text
   :caption: examples/help.inp

   ***,demonstrate help facility in Molpro
   help,command,help    !print help about help
   help,thresh,energy   !print help about threshold energy
   help,thresh,energy,default_value  !print help about threshold energy and its default
   help,thresh          !print short description of all thresholds
   help,thresh,nonexistent  !this does not exist and gives an error message

Currently, help is only available for a limited number of parameters and commands. However, the database will be extended in the near future.
