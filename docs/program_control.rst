.. raw:: html

   <span id="allocating-dynamic-memory-memory"></span>

.. raw:: html

   <span id="checking-the-program-status-status"></span>

.. raw:: html

   <span id="do-loops-do-enddo"></span>

.. raw:: html

   <span id="ending-a-job"></span>

.. raw:: html

   <span id="example-for-computing-expectation-values"></span>

.. raw:: html

   <span id="example-for-computing-relativistic-corrections"></span>

.. raw:: html

   <span id="global-print-options-gprint-nogprint"></span>

.. raw:: html

   <span id="global-thresholds-gthresh"></span>

.. raw:: html

   <span id="goto-commands"></span>

.. raw:: html

   <span id="if-statements"></span>

.. raw:: html

   <span id="including-secondary-input-files-include"></span>

.. raw:: html

   <span id="labels-label"></span>

.. raw:: html

   <span id="one-electron-operators-and-expectation-values-gexpec"></span>

.. raw:: html

   <span id="procedures-proc-endproc"></span>

.. raw:: html

   <span id="restarting-a-job-restart"></span>

.. raw:: html

   <span id="starting-a-job"></span>

.. _program_control--program-control:

Program control
===============

.. _program_control--starting-a-job:

Starting a job (\*\*\*)
=======================

The first card of each input should be:

``*,text``

where *text* is arbitrary. If file 1 is restarted, *text* must always be the same. The effect of this card is to reset all program counters, etc. If the ``***`` card is omitted, *text* assumes its default value, which is all blank.

.. _program_control--ending-a-job:

Ending a job (---)
==================

The end of the input is signaled by either an end of file, or a

``---``

card. All input following the ``---`` card is ignored.

Alternatively, a job can be stopped at at some place by inserting an ``EXIT`` card. This could also be in the middle of a ``DO`` loop or an ``IF`` block. If in such a case the ``---`` card would be used, an error would result, since the ``ENDDO`` or ``ENDIF`` cards would not be found.

.. _program_control--restarting-a-job-restart:

Restarting a job (RESTART)
==========================

In contrast to Molpro92 and older versions, the current version of Molpro attempts to recover all information from all permanent files by default. If a restart is unwanted, the ``NEW`` option can be used on the ``FILE`` directive. The ``RESTART`` directive as described below can still be used as in Molpro92, but is usually not needed.

``RESTART,$r_1,r_2,r_3,r_4,\ldots$;``

The :math:`r_i` specify which files are restarted. These files must have been allocated before using ``FILE`` cards. There are two possible formats for the :math:`r_i`:

* **a) :math:`0 < r_i < 10`:** Restart file :math:`r_i` and restore all information.
* **b) :math:`r_i=name.nr`:** Restart file :math:`nr` but truncate before record *name*.

If all :math:`r_i=0`, then all permanent files are restarted. However, if at least one :math:`r_i` is not equal to zero, only the specified files are restarted.

Examples:

* ``RESTART;`` will restart all permanent files allocated with ``FILE`` cards (default)
* ``RESTART,1;`` will restart file 1 only
* ``RESTART,2;`` will restart file 2 only
* ``RESTART,1,2,3;`` will restart files 1-3
* ``RESTART,2000.1;`` will restart file 1 and truncate before record 2000.

.. _program_control--including-secondary-input-files-include:

Including secondary input files (INCLUDE)
=========================================

``INCLUDE,file[,ECHO];``

Insert the contents of the specified *file* in the input stream. In most implementations the file name given is used directly in a Fortran open statement. If *file* begins with the character ``’/’``, then it will be interpreted as an absolute file name. Otherwise, it will be assumed to be a path relative to the directory from which the Molpro has been launched. If, however, the file is not found, an attempt will be made instead to read it relative to the system ``lib/include`` directory, where any standard procedures may be found.

If the ``ECHO`` option is specified, the included file is echoed to the output in the normal way, but by default its contents are not printed. The included file may itself contain ``INCLUDE`` commands up to a maximum nesting depth of 10.

For the name of the *file* and the characters allowed, similar recommendations hold as for the Molpro input file, see
https://www.molpro.net/develop/manual/doku.php?id=quickstart#how_to_run_molpro  .
The include file together with a path to it may however be used.

.. _program_control--allocating-dynamic-memory-memory:

Allocating dynamic memory (MEMORY)
==================================

``MEMORY,n,scale;``

Sets the limit on dynamic memory to :math:`n` floating point words. For details, see section `memory allocation <general_program_structure.html#memory-allocation>`__.

.. _program_control--do-loops-do-enddo:

DO loops (DO/ENDDO)
===================

``DO`` loops can be constructed using the ``DO`` and ``ENDDO`` commands. The general format of the ``DO`` command is similar to Fortran:

``DO`` *variable*\ ``=``\ *start, end* [[,]\ *increment*] [[,]\ *unit*]

where *start, end, increment* may be expressions or variables. The default for *increment* is 1. In contrast to Fortran, these variables can be modified within the loop (to be used with care!). For instance:

.. code-block:: text

   DR=0.2
   DO R=1.0,6.0,DR,ANG
   IF (R.EQ.2) DR=0.5
   IF (R.EQ.3) DR=1.0
   ....
   ENDDO

performs the loop for the following values of ``R``: ``1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.5, 3.0, 4.0, 5.0, 6.0`` Ångstrøm. The same could be achieved as follows:

.. code-block:: text

   RVEC=[1.0,1.2,1.4,1.6,1.8,2.0,2.5,3.0,4.0,5.0,6.0] ANG
   DO I=1,#RVEC
   R=RVEC(I)
   ....
   ENDDO

Up to 20 ``DO`` loops may be nested. Each ``DO`` must end with its own ``ENDDO``.

Jumps into ``DO`` loops are possible if the ``DO`` variables are known. This can be useful in restarts, since it allows to continue an interrupted calculation without changing the input (all variables are recovered in a restart).

See `introductory examples <introductory_examples.html#do-loops>`__ for two examples of using do loops.

.. _program_control--branching-if-elseif-endif:

Branching (IF/ELSEIF/ENDIF)
===========================

``IF`` blocks and ``IF/ELSEIF`` blocks can be constructed as in ``FORTRAN``.

.. _program_control--if-statements:

IF statements
=============

``IF`` blocks have the same form as in Fortran:

``IF (logical expression) THEN statements ENDIF``

If only one statement is needed, the one-line form

``IF (logical expression) statement``

can be used, except if *statement* is a procedure name.

``ELSE`` and ``ELSE IF`` can be used exactly as in Fortran. ``IF`` statements may be arbitrarily nested. Jumps into ``IF`` or ``ELSE IF`` blocks are allowed. In this case no testing is performed; when an ``ELSE`` is reached, control continues after ``ENDIF``.

The logical expression may involve logical comparisons of algebraic expressions or of strings. Examples:

.. code-block:: text

   IF(STATUS.LT.0) THEN
   TEXT,An error occurred, calculation stopped
   STOP
   ENDIF

.. code-block:: text

   IF($method.eq.'HF') then
   ...
   ENDIF

In the previous example the dollar and the quotes are optional:

.. code-block:: text

   IF(METHOD.EQ.HF) then
   ...
   ENDIF

.. _program_control--goto-commands:

GOTO commands
=============

``GOTO`` commands can be used to skip over parts of the input. The general form is

``GOTO,command,[n],[nrep]``

Program control skips to the :math:`|n|`\ ’th occurrence of *command* (Default: :math:`n=1`). *command* must be a keyword in the first field of an input line. If *n* is positive, the search is forward starting from the current position. If *n* is negative, search starts from the top of the input. The ``GOTO`` command is executed at most *nrep* times. The default for *nrep* is 1 if :math:`n \lt 0` and infinity otherwise. We recommend that ``GOTO`` commands are never used to construct loops.

Alternatively, one can jump to labels using

``GOTO,label``

Since labels must be unique, the search starts always from the top of the input. It is required that the *label* ends with a colon.

.. _program_control--labels-label:

Labels (LABEL)
==============

``LABEL``

This is a dummy command, sometimes useful in conjunction with ``GOTO``.

.. _program_control--procedures-proc-endproc:

Procedures (PROC/ENDPROC)
-------------------------

Procedures can be defined at any place of the input or in ``INCLUDE`` files as follows:

.. code-block:: text

   PROC name 
   statements 
   ENDPROC

Alternatively, one can use the form

``PROC name[=]{statements}``

In the latter case, it is required that the left curly bracket (:math:`\{`) appears on the same line as ``PROC``, but *statements* can consist of several lines. If in the subsequent input *name* is found as a command *in the first field* of a line, it is substituted by the *statements*. Example:

.. code-block:: text

   proc runscf1
   nogprint,variable
   if(#symmetry.ne.0) set,scfsym=symmetry(1)
   if(#scfsy.ne.0) set,scfsym=scfsy
   if(#scfsymm.ne.0) set,scfsym=scfsymm
   if(#scfsymmetry.ne.0) set,scfsym=scfsymmetry
   if(#scfsym.eq.0) set,scfsym=1
   set,symmetry(1)=scfsym
   if(orbital.eq.0) then
     hf
   else if(lastorb.ne.'RHF'.or.lastspin.ne.spin(1).or.lastsym.ne.scfsym(1).or. \
           lastnelec.ne.nelec(1)) then
     if(spin(1).eq.0.and.mod(nelec(1),2).ne.0) set,spin(1)=1
     hf
   end if
   if(#spin.eq.0) spin=mod(nelec,2)
   endproc

Alternatively, this could be written as

.. code-block:: text

   proc runscf2={
   nogprint,variable
   if(#symmetry.ne.0) set,scfsym=symmetry(1)
   if(#scfsy.ne.0) set,scfsym=scfsy
   if(#scfsymm.ne.0) set,scfsym=scfsymm
   if(#scfsymmetry.ne.0) set,scfsym=scfsymmetry
   if(#scfsym.eq.0) set,scfsym=1
   set,symmetry(1)=scfsym
   if(orbital.eq.0) then
     hf
   else if(lastorb.ne.'RHF'.or.lastspin.ne.spin(1).or.lastsym.ne.scfsym(1).or. \
           lastnelec.ne.nelec(1)) then
     if(spin(1).eq.0.and.mod(nelec(1),2).ne.0) set,spin(1)=1
     hf
   end if
   if(#spin.eq.0) spin=mod(nelec,2)
   }

Procedures may be nested up to a depth of 10. In the following example ``runscf`` is a procedure:

.. code-block:: text

   proc runmp2
   runscf
   if(spin.eq.0) then
   mp2
   else
   rmp2
   end if
   nogprint,variable
   saveccsd
   printdip=0
   printresults
   endproc

Note: Procedure names are substituted only if found in the first field of an input line. Therefore, they must not be used on one-line ``IF`` statements; please use ``IF / ENDIF`` structures instead.

If as first statement of a procedure ``ECHO`` is specified, the substituted commands of the present and lower level procedures will be printed. If ``ECHO`` is specified in the main input file, all subsequent procedures are printed.

Certain important input data can be passed to the program using variables. For instance, occupancy patterns, symmetries, number of electrons, and multiplicity can be defined in this way (see section `special variables <variables.html#special-variables>`__ for more details). This allows a quite general use of procedures.
Procedures can also be used in geometry optimizations or extrapolations, for example:

.. code-block:: text
   :caption: examples/h2o_proc_mrci.inp

   geometry={h1;o,h1,r;h2,o,r,h1,theta}
   r=1.9
   theta=102
   runmrci={if(.not.scfdone) hf;multi;mrci}
   
   runmrci
   extrapolate,procedure=runmrci,bases=vtz:vqz

.. code-block:: text
   :caption: examples/h2o_proc_ccsd.inp

   symmetry,x
   geometry={h1;o,h1,r;h2,o,r,h1,theta}
   r=1.9
   theta=102
   runmp2={{hf;occ,4,1};mp2}
   runlmp2={hf;lmp2}
   optg,procedure=runmp2
   optg,procedure=runlmp2
   runccsdt={hf;ccsd(t)}
   extrapolate,procedure=runccsdt,basis=vtz:vqz

.. _program_control--default-procedures:

Default Procedures
------------------

Many standard calculations can be used with the ``run`` command, see `Simplified input <introductory_examples.html#simplified-input>`__. They allow to write simple inputs in the most compact way.

Further predefined procedures are available in ``lib/include/procedures``:

.. code-block:: text

   runscf, rundft, runmp2, rundf-hf, rundt-mp2, runldf-hf, runldf-hf, runpno-lmp2, runmp3, runmp4, runmp4sdq,  runccsd, runccsdt, runbccd, runbccdt, runqcisd runqcisdt, runuccsd, runuccsdt, runcas, runmrpt, runcaspt2, runcaspt3, runmrci, runacpf, optscf, optdft, optmp2, optcas, optmrci, optccsd, optccsdt, freqscf, freqdft, freqmp2, freqccsd, freqccsdt, freqcas, freqmrci, rundf-lmp2, optdf-lmp2, freqdf-lmp2

With Molpro 2025.4 or later most of these procedures are obsolete and can be replaced by single line input using the ``run`` command, see section :doc:`Simple Input <quickstart>`.

A line

.. code-block:: text

   include procedures

is necessary to include these procedures. Some procedures use variables SYMMETRY, SPIN, STATE, NELEC to define state symmetries, spins, and charges, respectively. For example, the procedure ``runmrci`` can be used for a calculation of a vertical ionization potential of H\ :math:`_2`\ O as follows:

.. code-block:: text
   :caption: examples/h2o_IP_with_runmrci.inp

   ***,h2o IP
   include procedures
   r=1 ang           !set bond distance
   theta=104 degree  !set bond angle
   
   basis=vtz         !define basis set
   
   geometry          !geometry input block
   o                 !z-matrix
   h1,o,r
   h2,o,r,h1,theta
   endg              !end of geometry input
   runmrci           !compute mrci energy of water using defaults
   eh2o=energy       !save mrci energy in variable eh2o
   
   set,nelec=9       !set number of electrons to 9
   set,symmetry=2    !set wavefunction symmetry to 2
   runmrci           !compute mrci energy of h2o+ (2b2 state)
   
   ipci=(energy-eh2o)*toev  !compute mrci ionization potential in ev

For further examples see `oh_runccsdt.inp <media/examples/oh_runccsdt.inp>`__, `oh_runmrci1.inp <media/examples/oh_runmrci1.inp>`__, `oh_runmrci2.inp <media/examples/oh_runmrci2.inp>`__, `oh_runmrci3.inp <media/examples/oh_runmrci3.inp>`__, `oh_runmrci4.inp <media/examples/oh_runmrci4.inp>`__.

Note: At present, all variables are *global*, i.e., variables are commonly known to all procedures and all variables defined in procedures will be subsequently known outside the procedures as well. The reason is that procedures are included into the internal input deck at the beginning of the job and not at execution time; for the same reason, variable substitution of procedure names is not possible, e.g. one cannot use constructs like

.. code-block:: text

   method=scf
   $method       !this does not work!

.. _program_control--text-cards-text:

Text cards (TEXT)
-----------------

``TEXT,xxxxxx``

will just print *xxxxxx* in the output. If the text contains variables which are preceded by a dollar ($), these are replaced by their actual values, e.g.

.. code-block:: text

   r=2.1
   text,Results for R=$r

will print

``Results for R=2.1``

.. _program_control--checking-the-program-status-status:

Checking the program status (STATUS)
------------------------------------

``STATUS,[ALL|LAST|commands],[IGNORE|STOP|CRASH],[CLEAR]``

This command checks and prints the status of the specified program steps. *commands* may be a list of commands for wavefunction calculations previously executed in the current job. If no *command* or ``LAST`` is specified, the status of the last step is checked. If ``ALL`` is given, all program steps are checked.

If ``CRASH`` or ``STOP`` is given, the program will crash or stop, respectively, if the status was not o.k. (``STOP`` is default). If ``IGNORE`` is given, any bad status is ignored. If ``CLEAR`` is specified, all status information for the checked program steps is erased, so there will be no crash at subsequent status checks.

Examples:

* ``STATUS,HF,CRASH;`` will check the status of the last ``HF-SCF`` step and crash if it was not o.k. (i.e. no convergence). ``CRASH`` is useful to avoid that the next program in a chain is executed.
* ``STATUS,MULTI,CI,STOP;`` will check the status of the most previous ``MULTI`` and ``CI`` steps and stop if something did not converge.
* ``STATUS,RHF,CLEAR;`` will clear the status flag for last ``RHF``. No action even if ``RHF`` did not converge.

Note that the status variables are not recovered in a restart.

By default, the program automatically does the following checks:

1.) If an orbital optimization did not converge, and the resulting orbitals are used in a subsequent correlation calculation, an error will result. This error exit can be avoided using the ``IGNORE_ERROR`` option on the ``ORBITAL`` directive.

2.) If a ``CCSD|QCI|BCC|LMPn`` calculation did not converge, further program steps which depend on the solution (e.g, Triples, CPHF, EOM) will not be done and an error will result. This can be avoided using the ``NOCHECK`` option on the command line.

3.) In geometry optimizations or frequency calculations no convergence will lead to immediate error exits.

.. _program_control--global-thresholds-gthresh:

Global Thresholds (GTHRESH)
---------------------------

[command:gthresh]

A number of global thresholds can be set using the ``GTHRESH`` command outside the individual programs (the first letter ``G`` is optional, but should be used to avoid confusion with program specific ``THRESH`` cards). The syntax is

``GTHRESH,key1=value1,key2=value2,…``

*key* can be one of the following.

* ``ZERO`` Numerical zero (default 1.d-12)
* ``ONEINT`` Threshold for one-electron integrals (default 1.d-12, but not used at present)
* ``TWOINT`` Threshold for the neglect of two-electron integrals (default 1.d-12)
* ``PREFAC`` Threshold for test of prefactor in ``TWOINT`` (default 1.d-14)
* ``LOCALI`` Threshold for orbital localization (default 1.d-8)
* ``EORDER`` Threshold for reordering of orbital after localization (default 1.d-4)
* ``ENERGY`` Convergence threshold for energy (default 1.d-6)
* ``GRADIENT`` Convergence threshold for orbital gradient in ``MCSCF`` (default 1.d-2)
* ``STEP`` Convergence threshold for step length in MCSCF orbital optimization (default 1.d-3)
* ``ORBITAL`` Convergence threshold for orbital optimization in the SCF program (default 1.d-5).
* ``CIVEC`` Convergence threshold for CI coefficients in ``MCSCF`` and reference vector in ``CI`` (default 1.-d.5)
* ``COEFF`` Convergence threshold for coefficients in ``CI`` and ``CCSD`` (default 1.d-4)

* ``PRINTCI`` Threshold for printing CI coefficients (default 0.05)
* ``PUNCHCI`` Threshold for punching CI coefficients (default 99 - no punch)
* ``SYMTOL`` Threshold for finding symmetry equivalent atoms (default 1.d-6)
* ``GRADTOL`` Threshold for symmetry in gradient (default 1.d-6).
* ``THROVL`` Threshold for smallest allowed eigenvalue of the overlap matrix (default 1.d-8)
* ``THRDLOV`` Threshold for removing linear dependent basis functions and orbitals
* ``THRORTH`` Threshold for orthonormality check (default 1.d-8)
* ``THRPRINT`` Threshold for printing orbitals (thrprint=-1 : column-wise; thrprint=0 : row-wise, as in Molpro2015 and earlier versions ; thrprint :math:`>0`: print only coefficients that are larger than the threshold together with labels (default: thrprint=0.25)

.. _program_control--global-print-options-gprint-nogprint:

Global Print Options (GPRINT/NOGPRINT)
--------------------------------------

[command:gprint]

Global print options can be set using the ``GPRINT`` command outside the individual programs (the first letter ``G`` is optional, but should be used to avoid confusion with program specific ``PRINT`` cards). The syntax is

``GPRINT,key1[=value1],key2[=value2],…\\``
``NOGPRINT,key1,key2,…``

Normally, *value* can be omitted, but values :math:`\gt 0` may be used for debugging purposes, giving more information in some cases. The default is no print for all options, except for ``DISTANCE``, ``ANGLES`` (default=0), and ``VARIABLE``. ``NOGPRINT``,\ *key* is equivalent to ``PRINT``,\ *key*\ ``=-1``. *key* can be one of the following:

* ``BASIS`` Print basis information
* ``DISTANCE`` Print bond distances (default)
* ``ANGLES`` Print bond angle information (default). If :math:`\gt` 0, dihedral angles are also printed.
* ``ORBITAL`` Print orbitals in ``SCF`` and ``MCSCF``
* ``ORBEN`` Print orbital energies in ``SCF``
* ``CIVECTOR`` Print ``CI`` vector in ``MCSCF``
* ``PAIRS`` Print pair list in ``CI, CCSD``
* ``CS`` Print information for singles in ``CI, CCSD``
* ``CP`` Print information for pairs in ``CI, CCSD``
* ``REF`` Print reference CSFs and their coefficients in ``CI``
* ``PSPACE`` Print p-space configurations
* ``MICRO`` Print micro-iterations in ``MCSCF`` and ``CI``
* ``CPU`` Print detailed CPU information
* ``IO`` Print detailed I/O information
* ``VARIABLE`` Print variables each time they are set or changed (default).

.. _program_control--one-electron-operators-and-expectation-values-gexpec:

One-electron operators and expectation values (GEXPEC)
------------------------------------------------------

The operators for which expectation values are requested, are specified by keywords on the global ``GEXPEC`` directive. By default, only dipole moments are computed. The first letter ``G`` is optional, but should be used to avoid confusion with program specific ``EXPEC`` cards, which have the same form as ``GEXPEC``. For all operators specified on the ``GEXPEC`` card, expectation values are computed in all subsequent programs that generate the first-order density matrix. This is always the case for variational wavefunctions, i.e., HF, DFT, MCSCF, MRCI. For non-variational wavefunctions such as MP2, MP3, QCISD, QCISD(T), CCSD, or CCSD(T) the density matix is not computed by default, since this requires considerable additional effort (solving z-vector equations). The GEXPEC directive does not affect such programs. In some cases [currently for MP2, MP3, QCISD, QCISD(T), and CCSD] the ``EXPEC`` directive that is specific to those programs can be used to request the property calculation.

For a number of operators it is possible to use *generic* operator names, e.g., ``DM`` for dipole moments, which means that all three components ``DMX``, ``DMY``, and ``DMZ`` are computed. Alternatively, individual components may be requested.

The general format is as follows:

``[G]EXPEC,opname[,][icen,[x,y,z]],...``

where

* ***opname*** operator name (string), either generic or component.
* ***icen*** z-matrix row number or z-matrix symbol used to determine the origin (x,y,z must not be specified).

If *icen*\ :math:`=0` or blank, the origin must be specified in *x,y,z*

Several ``GEXPEC`` cards may follow each other, or several operators may be specified on one card.

Examples:

``GEXPEC,QM`` computes quadrupole moments with origin at (0,0,0),

``GEXPEC,QM1`` computes quadrupole moments with origin at centre 1.

``GEXPEC,QM,O1`` computes quadrupole moments with origin at atom ``O1``.

``GEXPEC,QM,,1,2,3`` computes quadrupole moments with origin at (1,2,3).

The following table summarizes all available operators:

.. list-table::
   :header-rows: 2

   * - One-electron operators and their components
     - 
     - 
     - 
   * - Generic name
     - Parity
     - Components
     - Description
   * - ``OV``
     - 1
     - 
     - Overlap
   * - ``EKIN``
     - 1
     - 
     - Kinetic energy
   * - ``POT``
     - 1
     - 
     - potential energy
   * - ``DELTA``
     - 1
     - 
     - delta function
   * - ``DEL4``
     - 1
     - 
     - :math:`\Delta^4`
   * - ``DARW``
     - 1
     - 
     - one-electron Darwin term, i.e., ``DELTA`` with appropriate factors summed over atoms.
   * - ``MASSV``
     - 1
     - 
     - mass-velocity term, i.e., ``DEL4`` with appropriate factor.
   * - ``REL``
     - 1
     - 
     - total Cowan-Griffin Relativistic correction, i.e., ``DARW``\ +\ ``MASSV``.
   * - ``DM``
     - 1
     - ``DMX``, ``DMY``, ``DMZ``
     - dipole moments
   * - ``SM``
     - 1
     - ``XX``, ``YY``, ``ZZ``, ``XY``, ``XZ``, ``YZ``
     - second moments
   * - ``TM``
     - 1
     - ``XXX``, ``XXY``, ``XXZ``, ``XYY``, ``XYZ``, ``XZZ``, ``YYY``, ``YYZ``, ``YZZ``, ``ZZZ``
     - third moments
   * - ``MLTP``\ *n*
     - 1
     - all unique Cartesian products of order :math:`n`
     - multipole moments
   * - ``QM``
     - 1
     - ``QMXX``, ``QMYY``, ``QMZZ``, ``QMXY``, ``QMXZ``, ``QMYZ``, ``QMRR``\ =\ ``XX + YY + ZZ``, ``QMXX``\ =(3 ``XX`` - ``RR``)/2, ``QMXY``\ =3 *XY* / 2 etc.
     - quadrupole moments and :math:`R^2`
   * - ``EF``
     - 1
     - ``EFX``, ``EFY``, ``EFZ``
     - electric field
   * - ``FG``
     - 1
     - ``FGXX``, ``FGYY``, ``FGZZ``, ``FGXY``, ``FGXZ``, ``FGYZ``
     - electric field gradients
   * - ``DMS``
     - 1
     - ``DMSXX``, ``DMSYX``, ``DMSZX``, ``DMSXY``, ``DMSYY``, ``DMSZY``, ``DMSXZ``, ``DMSYZ``, ``DMSZZ``
     - diamagnetic shielding tensor
   * - ``LOP``
     - -1
     - ``LX``, ``LY``, ``LZ``
     - Angular momentum operators :math:`\hat L_x`, :math:`\hat L_y`, :math:`\hat L_z`
   * - ``LOP2``
     - 1
     - ``LXLX, LYLY, LZLZ``, ``LXLY, LXLZ, LYLZ``
     - one electron parts of products of angular momentum operators. The symmetric combinations :math:`\frac{1}{2} (\hat L_x \hat L_y+\hat L_y \hat L_x)` etc. are computed.
   * - ``VELO``
     - -1
     - ``D/DX``, ``D/DY``, ``D/DZ``
     - velocity
   * - ``LS``
     - -1
     - ``LSX``, ``LSY``, ``LSZ``
     - spin-orbit operators
   * - ``ECPLS``
     - -1
     - ``ECPLSX``, ``ECPLSY``, ``ECPLSZ``
     - ECP spin-orbit operators

Expectation values are only nonzero for symmetric operators (parity=1). Other operators can be used to compute transition quantities (spin-orbit operators need a special treatment).

.. _program_control--example-for-computing-expectation-values:

Example for computing expectation values
========================================

The following job computes dipole and quadrupole moments for H\ :math:`_2`\ O.

.. code-block:: text
   :caption: examples/h2o_gexpec2.inp

   ***,h2o properties
   geometry={o;h1,o,r;h2,o,r,h1,theta}   !Z-matrix geometry input
   r=1 ang                               !bond length
   theta=104                             !bond angle
   gexpec,dm,sm,qm                       !compute dipole and quadrupole moments
   $methods=[hf,multi,ci]                !do hf, casscf, mrci
   do i=1,#methods                       !loop over methods
   $methods(i)                           !run energy calculation
   e(i)=energy
   dip(i)=dmz                            !save dipole moment in variable dip
   quadxx(i)=qmxx                        !save quadrupole moments
   quadyy(i)=qmyy
   quadzz(i)=qmzz
   smxx(i)=xx                            !save second moments
   smyy(i)=yy
   smzz(i)=zz
   enddo
   table,methods,dip,smxx,smyy,smzz        !print table of first and second moments
   table,methods,e,quadxx,quadyy,quadzz    !print table of quadrupole moments

This Job produces the following tables

.. code-block:: text

    METHODS     DIP           SMXX          SMYY          SMZZ
    HF        0.82747571   -5.30079792   -3.01408114   -4.20611391
    MULTI     0.76285513   -5.29145148   -3.11711397   -4.25941000
    CI        0.76868508   -5.32191822   -3.15540500   -4.28542917
   
    METHODS       E             QUADXX       QUADYY        QUADZZ
    HF        -76.02145798   -1.69070039   1.73937477   -0.04867438
    MULTI     -76.07843443   -1.60318949   1.65831677   -0.05512728
    CI        -76.23369821   -1.60150114   1.64826869   -0.04676756

.. _program_control--example-for-computing-relativistic-corrections:

Example for computing relativistic corrections
==============================================

.. code-block:: text
   :caption: examples/ar2_rel.inp

   ***,ar2
   geometry={ar1;ar2,ar1,r}   !geometry definition
   r=2.5 ang                  !bond distance
   {hf;                       !non-relativistic scf calculation
   expec,rel,darwin,massv}    !compute relativistic correction using Cowan-Griffin operator
   e_nrel=energy              !save non-relativistic energy in variable enrel
   show,massv,darwin,erel     !show individual contribution and their sum
   
   dkroll=1                   !use douglas-kroll one-electron integrals
   hf;                        !relativistic scf calculation
   e_dk=energy                !save relativistic scf energy in variable e_dk.
   show,massv,darwin,erel     !show mass-velocity and darwin contributions and their sum
   show,e_dk-e_nrel           !show relativistic correction using Douglas-Kroll

This jobs shows at the end the following variables:

.. code-block:: text

    MASSV / AU             =       -14.84964285
    DARWIN / AU            =        11.25455679
    EREL / AU              =        -3.59508606

.. _program_control--xml-dump-options-xml:

XML dump options (XML)
----------------------

This command allows to modify the default behaviour of the XML output.
The general format is as follows:

``XML,key1[=value1],key2[=value2],…\\``

where *key* can be one of the following:

* ``DUMPORB`` Dump occupied orbitals to XML file (default 0, unless the ``--xml-orbdump`` command line option is given).
* ``SKIPVIRT`` Omit virtual orbitals in the XML orbital dumps (default 1).
* ``PRINT`` Print record information to output file, showing from which records the orbitals etc are read (default 0).
