.. raw:: html

   <span id="commands"></span>

.. raw:: html

   <span id="data"></span>

.. raw:: html

   <span id="directives"></span>

.. raw:: html

   <span id="expressions"></span>

.. raw:: html

   <span id="input-format"></span>

.. raw:: html

   <span id="intrinsic-functions"></span>

.. raw:: html

   <span id="options"></span>

.. raw:: html

   <span id="setting-variables"></span>

.. raw:: html

   <span id="variables"></span>

.. _definition_of_molpro_input_language--definition-of-molpro-input-language:

Definition of Molpro input language
===================================

.. _definition_of_molpro_input_language--input-format:

Input format
============

Molpro’s execution is controlled by an input file. In general, each input record begins with a keyword, which may be followed by data or other keywords. Molpro input contains commands, directives, options and data. The commands and directives are sequentially executed in the order they are encountered. Furthermore, procedures can be defined anywhere in the input, which can include any number of commands and directives. They are only executed when called (which may be before or after the definition in the input file).

The input file can be written in free format. The following conversions take place:

* **, (comma)** move to next tab stop, i.e. this delimits input fields
* **; (semicolon)** end of record, i.e. a new record is started
* **! (exclamation mark)** ignore rest of input line (useful for comments)
* **``---`` (three dashes)** end of file (rest of input is ignored)

Input may be given upper or lower case. The input processor converts all characters to upper case. All integers are appended with “.” (only floating point numbers are read by the program).

Several logical input records can actually be typed on one line and separated by semicolons, i.e., a given input line may contain many actual commands (separated by semicolons), or just one, as you prefer. These basic command units (records) delimited by semicolons are also frequently referred to as *cards* throughout this manual.

Exception to these general rules are:

* ``***`` first data line always (can be omitted)
* ``INCLUDE`` include other input file
* ``FILE`` definition of named files
* ``TEXT`` prints text
* ``TITLE`` defines a title for the run or a table
* ``CON`` specifies orbital configurations
* ``---`` last line of input

These commands always occupy a whole line. Using ``INCLUDE`` it is possible to open secondary input files. If an ``INCLUDE`` command is encountered, the new input file is opened and read until its end. Input is then continued after the include card in the first file. ``INCLUDE``\ ’s may be nested.

A Molpro input record (card) contains a number of input *fields*. Input fields may be up to 256 characters wide and contain either expressions or strings. The fields can be separated by commas or blanks. We recommend the general use of commas in order to avoid unexpected results.

Each line may start with a label. A label is separated from the body of the line by a colon (:). The colon is part of the label. The length of the label must not exceed 6 characters (including the colon) and the labels must be unique. Labels may be useful with ``GOTO`` commands. Example:

``GOTO,START:\\``
``…\\``
``START: CCSD(T)``

Here ``START:`` is a label, and ``CCSD(T)`` is a command.

Strings containing blanks can be entered using quotes. For instance, ``’This is a string’`` is interpreted as one string, but ``This is a string`` is a sequence of four strings in four subsequent fields. Strings in quotes are not converted to upper case.

Input lines may be concatenated using :math:`\backslash` at the end of the line(s) to be continued. Any number of lines may be concatenated up to a total length of 1024 characters (only 500 characters are possible on older IBM systems).

Filenames may be up to 31 characters long, provided that long filenames are supported by the Unix system used. An exception are older CRAY systems, which allow only 8 characters for the names of binary Molpro files.

.. _definition_of_molpro_input_language--commands:

Commands
========

A command invokes a particular program. It may be followed by local input for this program, enclosed in curly brackets((Depending on the parameter ``STRICTCHECK`` in file ``lib/variable.registry`` the program may tolerate directives given after commands without curly brackets. The program checks for ambiguities in the input. A directive is considered ambiguous if a command or procedure with the same name is known, and the directive is not in a command block (i.e., no curly brackets are used). ``STRICTCHECK=0``: The input checker tolerates ambiguous directives if they are followed by a non ambiguous directive which is valid for the current command. ``STRICTCHECK=1``: The input checker does not tolerate any ambiguous directives. ``STRICTCHECK=2``: The input checker does not tolerate any directives outside curly brackets. The default is ``STRICTCHECK=0``, which gives the maximum possible compatibility to previous Molpro versions.
))

The general format is either

``COMMAND, options``

or

``{ COMMAND,options\\``
*directives*
*data*
}

Examples for commands are ``HF, MP2, CCSD(T), MCSCF, MRCI``. Examples for directives are ``OCC, CLOSED, WF, PRINT``. Directives can be in any order, unless otherwise noted. Data can follow certain directives. For the format of options, directives and data see subsections `directives <definition_of_molpro_input_language.html#directives>`__, `options <definition_of_molpro_input_language.html#options>`__, and `data <definition_of_molpro_input_language.html#data>`__, respectively.

In the following, such a sequence of input will be denoted a *command block*. Special command blocks are the geometry and basis blocks.

The options given on the command line may include any options relevant to the current program. For instance, in DF-LMP2-R12 this could be options for density fitting, local, explicit, and/or thresholds. Alternatively, options can be specified on individual directives like

``DFIT,options\\``
``LOCAL,options\\``
``EXPLICIT,options\\``
``THRESH,options``

In these cases, only the options belong to the corresponding directive are valid; thus, if an option for ``EXPLICIT`` would be specified, e.g., on the ``DFIT`` directive, an error would result. This error would be detected already in the input prechecking stage.

As already mentioned, the use of curly brackets is normally compulsory if more than one input line is needed. In the case of one-line commands, curly brackets are needed as well if the next command or procedure has the same name as a directive valid for the current command.

Note: ``DIRECT`` and associated options cannot be specified on command lines any more.

.. _definition_of_molpro_input_language--directives:

Directives
==========

Directives serve to specify input data and special options for programs. They start with a keyword, followed by data and/or options. The general format is

``DIRECTIVE,data,options``

The format of data and options is specified in the subsequent sections. Data must always be given before any options.

Examples for directives are

``OCC,CORE, CLOSED, WF, LOCAL, DFIT, …``

.. _definition_of_molpro_input_language--global-directives:

Global directives
=================

Certain directives can be given anywhere in the input, i.e. either inside or outside command blocks. If they are given inside of command blocks, the specified options are valid only locally for the current program. However, if they are given outside a command block, they act globally, and are used for all programs executed after the input has been encountered. Local options have preference over global options.

The following directives can be either local or global:

``Wavefunction definition: OCC,CORE, CLOSED, FROZEN, WF\\``
Thresholds and options: ``LOCAL``, ``DFIT``, ``DIRECT``, ``EXPLICIT``, ``THRESH``, ``PRINT``, ``GRID``

If such options are given outside a command block, a context can be specified

``DIRECTIVE,data,CONTEXT=context,``

e.g.,

``OCC,3,1,1,CONTEXT=HF\\``
``OCC,4,1,2,CONTEXT=MCSCF``

``CONTEXT`` can be any valid command name (or any valid alias for this), but internally these are converted to one of the following: ``HF`` (Hartree-Fock and DFT), ``MC`` (MCSCF and CASSCF), ``CC`` (single reference correlation methods, as implemented in the CCSD program), ``CI`` (multireference correlation methods, as implemented in the MRCI program). The directive will then be applied to one of the four cases. Several contexts can be specified separated by colon, e.g.,

``CONTEXT=HF:CCSD\\``
If only a single context is given (no colon), shortcuts for the specifying the ``CONTEXT`` option are obtained by postfixing *context* to the command name, e.g.,

``OCC_HF,3,1,1\\``
``OCC_MCSCF,4,1,2``

If no context is given, the default is ``HF``. The default occupations for single reference methods (e.g., MP2, CCSD) are the ones used in ``HF``, the defaults for multireference methods (e.g. RS2, MRCI) correspond to those used in ``MCSCF``.

.. _definition_of_molpro_input_language--options:

Options
=======

Options have the general form ``NAME``\ [=\ *value*]

where value can be a number, and expression, or a string. Several options are separated by comma or blank. ``NAME`` must begin with a character [A-Z]. If options are given on a ``COMMAND`` line or on directives within a command block, they are valid only for the corresponding program (see Sec. `directives <definition_of_molpro_input_language.html#directives>`__). If options are given in a procedure, they are valid only in the procedure and procedures called from the current procedure; whenever a procedure is terminated, the options of the previous level are restored.

Options can also be single keywords, like ``SYM`` or ``NOSYM``. In this case, the option is switched on or off, depending whether or not the key begins with ``NO``. Alternatively, such logical options can also be set or unset using ``NAME=ON`` or ``NAME=OFF``. For instance, ``SYM=OFF`` is equivalent to ``NOSYM``. Furthermore, ``YES`` and ``NO`` are aliases for ``ON`` and ``OFF``, respectively.

.. _definition_of_molpro_input_language--data:

Data
====

Data are defined as a sequence of numbers, expressions, or strings, separated by commas or blanks. Generally, the order of data is essential. Empty fields are interpreted as zeros. Strings and variables must begin with a character [A-Z]. If :math:`+` or :math:`-` follows blank and directly precedes a number or variable it is interpreted as sign and not a binary operator. If there are no blanks before and after such operators, or blanks follow them, they are interpreted as binary operators. Examples:

.. list-table::

   * - ``3 - 4 4``
     - yields [-1,4]
   * - ``3-4 4``
     - yields [-1,4]
   * - ``3 -4 4``
     - yields [3,-4,4]
   * - ``3,-4 4``
     - yields [3,-4,4]
   * - ``3, -4, 4``
     - yields [3,-4,4]

Expressions (including numbers) may contain variables.

Examples for the use of data: geometry and basis input, ``LATTICE``, ``OCC``, ``CLOSED``, ``CORE``, ``WF`` directives.

In some cases several lines of data are needed for a certain command or directive; in such cases the data must follow directly the corresponding command\ :math:`|`\ directive, and must be enclosed in square brackets:

``COMMAND,options \\``
:math:`\left[ data \right]`

Normally, the input format of data is ``MOLPRO`` style, i.e., numbers are separated by commas, and variables as well as expressions can be used.

If data are included using external files, the input format of *data* is free format: no commas are needed, but no variables and expressions can be used.

.. _definition_of_molpro_input_language--expressions:

Expressions
===========

[sec:expressions]

In any input field, if not stated otherwise, data can be entered in the form of expressions. Numbers and variables are special cases of expressions. An expression is typed in Fortran style and may contain any number of nested parenthesis. The standard intrinsic functions are also available (see next section). Molpro understands both arithmetic and logical expressions. The result of an arithmetic expression is a *real* (double precision) number. Internally, all integers are also converted to *real* numbers. The result of a logical expression is either ``.TRUE.`` or ``.FALSE.``. Internally, ``.TRUE.`` is stored as a one (1.0), and ``.FALSE.`` as zero (0.0). Expressions may contain any number of variables.

The following standard operations can be performed :

* ``expr + expr`` Addition
* ``expr - expr`` Subtraction
* ``expr * expr`` Multiplication
* ``expr / expr`` Division
* ``expr .OR. expr`` Logical ``OR``
* ``expr .AND. expr`` Logical ``AND``
* ``expr .XOR. expr`` Exclusive ``OR``
* ``.NOT.expr`` Logical ``NOT``
* ``expr .GT. expr`` Greater Than
* ``expr .EQ. expr`` Equal
* ``expr .LT. expr`` Less Than
* ``expr .GE. expr`` Greater Equal
* ``expr .LE. expr`` Less Equal
* ``expr .NE. expr`` Not Equal
* ``expr **expr`` Exponentiation
* ``expr ^ expr`` Exponentiation
* ``(expr)`` Parenthesis (no effect)
* ``-expr`` Change sign
* ``+expr`` Keep sign (no effect)

.. _definition_of_molpro_input_language--intrinsic-functions:

Intrinsic functions
===================

Expressions may contain the following intrinsic functions:

* ``ABS(expr)`` Absolute value
* ``MAX(expr,expr, ...)`` Largest value of arbitrary number of numbers or expressions
* ``MIN(expr,expr, ...)`` Smallest value of arbitrary number of numbers of expressions
* ``EXP(expr)`` Exponential
* ``LOG(expr)`` Natural Logarithm
* ``LOG10(expr)`` Common Logarithm
* ``SQRT(expr)`` Square Root
* ``NINT(expr)`` Next nearest integer
* ``INT(expr)`` Truncate to integer
* ``SIN(expr)`` Sine
* ``COS(expr)`` Cosine
* ``TAN(expr)`` Tangent
* ``ASIN(expr)`` Arcsine
* ``ACOS(expr)`` Arccosine
* ``ATAN(expr)`` Arctangent
* ``COSH(expr)`` Hyperbolic cosine
* ``SINH(expr)`` Hyperbolic sine
* ``TANH(expr)`` Hyperbolic tangent
* ``MOD(expr1 , expr2 )`` Remainder: ``expr1-INT(expr1/expr2)*expr2``

Note: all trigonometric functions use or produce angles in degrees.

.. _definition_of_molpro_input_language--variables:

Variables
=========

[sec:variables1]

.. _definition_of_molpro_input_language--setting-variables:

Setting variables
=================

Data and results can be stored in Molpro variables. Variables can be of type string, floating, or logical and may be used anywhere in the input.

The syntax for setting variables is

``VARNAME1=expression [unit],VARNAME2=expression [unit]``

where unit is optional. If a variable is undefined, zero is assumed.

Variables are useful for running the same input with different actual parameters (e.g. geometries or basis function exponents), and to store and manipulate the results. *Arrays* are variables with an index in parenthesis, e.g., ``var(1)``. The number of elements in an array ``var`` is ``#var``. The array length can be reset to zero by the ``CLEAR`` directive or simply by modifying ``#var``. Variables and variable arrays may be displayed at any place in the output by the ``SHOW`` command, and whole tables of variables can be generated using the ``TABLE`` command. For more details about variables see section :doc:`variables <variables>`.

.. _definition_of_molpro_input_language--string-variables:

String variables
================

Special care is necessary when using strings. In order to avoid unexpected results, either a $ has to be prefixed whenever a string variable is set, or the string has to be given in quotes. Possible forms are

``$name=string\\``
``name=’string’\\``
``name=string variable\\``
``$name=string variable\\``
Examples:

.. code-block:: text

    string1='This is a string'  !define a string variable. Text in quotes is not
                                ! converted to upper case.
    string2=string1             !assign string variable string1 to a new variable.
    $string3=string1            !equivalent to previous case.
    $string4=mystring           !define a string variable. Since ''mystring'' is not
                                !given in quotes, !it will be converted to upper case.
    string5=mystring            !string5 will not be a string variable since $ is missing.

yields

.. code-block:: text

    SETTING STRING1        =    This is a string
    SETTING STRING2        =    This is a string
    SETTING STRING3        =    This is a string
    SETTING STRING4        =    MYSTRING
    VARIABLE MYSTRING UNDEFINED, ASSUMING 0
    SETTING STRING5        =         0.00000000

For more information concerning strings and string variables, see section `string variables <variables.html#string-variables>`__

.. _definition_of_molpro_input_language--procedures:

Procedures
----------

.. _definition_of_molpro_input_language--procedure-definition:

Procedure definition
====================

Procedures are sequences of commands and/or options. They can be defined anywhere in the input as

``[PROC ]procname=$\{$\\``
*command blocks*
*directives*
:math:`\}`

or

``PROC procname\\``
*command blocks*
*directives*
``ENDPROC``

In order to avoid unexpected results, *procname* must differ from all known command names. Procedures must not contain geometry blocks.

Note that procedures are not executed when encountered in the input, but only when called. Procedure definitions must not be nested. Procedures can contain procedure calls up to a nesting level of 10.

.. _definition_of_molpro_input_language--procedure-calls:

Procedure calls
===============

Procedures can be called anywhere in the input. The syntax is the same as for commands (cf. section `commands <definition_of_molpro_input_language.html#commands>`__), except that the procedure name replaces the command name.

``PROCEDURE``

No options are allowed on procedure calls. However, specific options may be set using directives within the procedure, and these are then valid for all programs within the procedure which follow the directive. When execution of the procedure is finished, the previous global options are restored. The hierarchy in which options are processed is as follows:

Global options
Options in procedures
Command line options
Options given on directives within a command block
The last option set is then actually used. Thus, options specified on command lines or within command blocks have preference over procedure options, and procedure options have preference over global options.
