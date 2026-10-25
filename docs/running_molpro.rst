.. _running_molpro--running-molpro:

Running Molpro
==============

On Unix systems, Molpro is accessed using the *molpro* unix command. The syntax is

``molpro options datafile``

Molpro’s execution is controlled by user-prepared data; if *datafile* is not given on the command line, the data is read from standard input, and program results go to standard output. Otherwise, data is taken from *datafile,* and the output is written to a file whose name is generated from *datafile* by removing any trailing suffix, and appending ``.out``. The name *datafile* must not contain parenthesis, brackets, or other special characters like exclamation marks (!), question marks (?), slashes (/), backslashes (\), blanks( ), equality signs(:math:`=`), commas (,), semicolons (;), asterisks (\*), or any kind of quotes. If the output file already exists, then the old file is appended to the same name with suffix ``.out_1``, and then deleted. This provides a mechanism for saving old output files from overwriting. Note that the above behaviour can be modified with the ``-o`` or ``-s`` options.

For example, a serial Molpro calculation is started using

``molpro mymolecule.inp``

and this creates an output ``mymolecule.out``. For larger calculations, it may be necessary to specify how much dynamic (stack) memory molpro can allocate, using the ``-m`` option:

``molpro -m100 mymolecule.inp``

This allocates 100 MW (megawords) of stack memory. Further options are necessary for parallel execution, see section `specifying parallel execution <running_molpro_on_parallel_computers.html#specifying-parallel-execution>`__. For parallel executions, it is very important to read and understand also sections `GA Installation notes <running_molpro_on_parallel_computers.html#ga-installation-notes>`__ and `memory specifications <running_molpro_on_parallel_computers.html#memory-specifications>`__.

.. _running_molpro--general-options:

General Options
===============

Most options are not required, since sensible system defaults are usually set. Options as detailed below may be given, in order of decreasing priority, on the command line, in the environment variable MOLPRO_OPTIONS, or in the files ``./molpro.rc`` and ``$HOME/.molprorc``.

* **``-o`` :math:`|` ``--output`` *outfile*** [option:o] specifies a different output file.
* **``-d`` :math:`|` ``--directory`` *directory*** specifies the scratch directory for the program.
* **``--backup`` *nfile*** enables the saving of previous output files, up to a maximum of  *nfile*. If *nfile* is omitted, it defaults to infinity. The names of the backup files are constructed by appending ``_`` and a sequence number to the output file name, and both regular and xml-format files are processed, together with any log file.
* **``-a`` :math:`|` ``--append-backup``** Previous output files are concatenated by appending, instead of being kept separate.
* ``--directory-backup`` Backup files are stored in a single separate subdirectory, named *datafile*\ ``.d``, with subdirectories ``01``, ``02``, :math:`\dots`. ``--directory-backup`` and ``--append-backup`` are mutually exclusive, and switching one of them on will force the other to be switched off. ``--no-append-backup`` ``--no-directory-backup`` can also be specified with the same effect, except that they do not also imply ``--backup``.
* **``--backup-directory`` *dir*** In the case of ``--directory-backup``, use //// dir as the location of backup files instead of the default.
* **``-s`` :math:`|` ``--nobackup``** disables the mechanism whereby an existing output file is saved.
* **``-v`` :math:`|` ``--verbose``** causes the procedure to echo debugging information; ``--noverbose`` selects quiet operation (default).
* ``-k //key//`` where *key* is the licence key. This is normally not necessary since the key should be installed globally when installing Molpro.
* **``-m`` :math:`|` ``--memory`` *memory* (in megawords)** specifies the working (stack) memory to be assigned to the program, in 8-byte words. For details, see section `memory allocation <general_program_structure.html#memory-allocation>`__.
* **``-M`` :math:`|` ``--memory-per-node`` *M*** total memory per node (stack + GA, in megawords) For details, see section `memory allocation <general_program_structure.html#memory-allocation>`__
* **``-I`` :math:`|` ``--main-file-repository`` *directory*** specifies the directory where the permanent copy of any integral file (file 1) resides. This may be a pathname which is absolute or relative to the current directory (e.g., ’\ ``.``\ ’ would specify the current directory). Normally, the ``-I`` directory should be equal to the ``-d`` working directory to avoid copying of large integral files, since after completion of the job the file will be copied to the directory given after ``-I``. On some main frames, the scratch directory is erased automatically after a job has terminated, and in such cases a different ``-I`` directory, e.g., ``$HOME/int``, can be specified (environment variables will be expanded at run time). In view of the large integral file sizes, this should be used with care, however. Note that in parallel runs with more than 1 processor the integral file will never be copied, and cannot be restarted.
* **``-W`` :math:`|` ``--wavefunction-file-repository`` *directory*** is similar to ``--main-file-repository`` except that it refers to the directory for the wavefunction files (2,3 and 4). This determines the destination of permanent wavefunction (dump) files used for storing information like orbitals or CI-vectors etc. These files are essential for restarting a job. As explained for the integral files above, permanent wavefunction files will be copied to *directory* after completion of the job. The default for *directory* is ``$HOME/wfu``.
* **``-X`` :math:`|` ``--xml-output``** specifies that an additional XML output file suitable for automatic post-processing will be written, with suffix .xml. Important data such as input, geometries, and results are stored in a `marked-up format <https://www.molpro.net/schema/molpro-output.xsd>`__. ``--no-xml-output`` switches off this behaviour.
* ``--xml-orbdump`` If this option, which is the default, is given, more data such as the basis set and the occupied orbitals are dumped to the XML file, ready for interpretation by iMolpro or gmolpro. Orbitals are written whenever they are created, except in a geometry optimisation or finite-displacement frequency calculation. For jobs that create many orbital sets, to avoid creating large files, the writing of orbitals can be switched off with ``-no-xml-orbdump``, or by setting the variable ``NO_XML_ORBDUMP`` in the input file.
* ``--stdout`` Write the plain-text output to standard output instead of the ``.out`` file. The ``.xml`` file is unaffected. This option can be useful when using an integrated development environment.
* **``-L`` :math:`|` ``--library`` *directory*** specifies the directory where the basis set library files (``LIBMOL*``) are found.
* ``--geometry`` Use this to obtain an XML output with geometry information, but without performing any electronic structure calculation (e.g. to visualise the geometry). Note that it needs at least one jobstep, e.g. “hf” though this jobstep will not be executed.
* ``--no-flush6`` Don’t flush the output, this might increase performance on some systems as the expense of being able to poll the output.
* **``-g`` :math:`|` ``--use-logfile``** Use a separate logfile for more in-depth output.
* ``--nouse-logfile`` All output will be in the regular output file.
* **``-E`` :math:`|` ``--exclusive-file-implementation``** Specify file implementation. This is mainly for debugging, eg. reproducing non-shared file problems on a system with shared files, normally the default should be used.
* **``--name`` *name=string*** Set string variable on the command line, eg. ``--name`` basis=vtz.
* **``-V`` :math:`|` ``--var`` *name=value*** Set variable on the command line, eg. ``--var`` len=1.2.
* **``-k`` :math:`|` ``--licence-token``** Specify licence token on the command line.
* ``--version`` Print Molpro version and exit
* ``--database`` Instead of executing Molpro, instead run one of the database utility scripts as described in section `interrogation and manipulation of databases <post-processing_of_output_and_databases.html#interrogation-and-manipulation-of-databases>`__.
* ``--sysid`` For debugging when the getinfo.sh script does not give the correct sysid.

.. _running_molpro--options-for-launching-molpro:

Options for launching Molpro
============================

These options are for the ``molpro`` shell script which is used to launch the ``molpro.exe`` MPI program. These options should be given on the command line or in the ``MOLPRO_OPTIONS`` environment variable as both of these are parsed by the shell script and used to launch ``molpro.exe``, they should not be given in ``.molprorc`` or any other configuration files since these are not read until after ``molpro.exe`` is launched.

* **``-n`` :math:`|` ``--tasks`` *tasks*** specifies the number of parallel processes to be set up.
* **``-N`` :math:`|` ``--task-specification`` *node1:tasks1,node2:tasks2:math:`\dots`*** *node1, node2* etc. specify the host names of the nodes on which to run.

.. _running_molpro--options-for-parallel-execution:

Options for parallel execution
==============================

The options specific to parallel execution are described `here <running_molpro_on_parallel_computers.html#specifying-parallel-execution>`__.

It is very important to read :doc:`running Molpro on parallel computers <running_molpro_on_parallel_computers>` before executing parallel Molpro calculations.
