.. raw:: html

   <span id="assigning-punch-files-punch"></span>

.. raw:: html

   <span id="data"></span>

.. raw:: html

   <span id="delete"></span>

.. raw:: html

   <span id="erase"></span>

.. raw:: html

   <span id="file"></span>

.. raw:: html

   <span id="molpro-system-parameters-gparam"></span>

.. _file_handling--file-handling:

File handling
=============

.. _file_handling--file:

FILE
====

The ``FILE`` directive is used to open permanent files, which can be used for later restarts. The file name must not contain parenthesis, brackets, exclamation marks, or other special characters like exclamation marks (!), question marks (?), slashes (/), backslashes (\), blanks( ), equality signs(:math:`=`), commas (,), semicolons (;), asterisks (\*), or any kind of quotes(underscore is allowed). The syntax in Molpro94 and later versions is

``FILE,file,name,[status]``

*file* is the logical Molpro file number (1-9). *name* is the file name (will be converted to lower case). *status* can be one of the following:

* ``UNKNOWN`` A permanent file is opened. If it exists, it is automatically restarted. This is the default.
* ``OLD`` Same effect as ``UNKNOWN``. No error occurs if the file does not exist.
* ``NEW`` A permanent file is opened. If it already exists, it is erased and not restarted.
* ``ERASE`` Same effect as ``NEW``.
* ``SCRATCH`` A temporary file is opened. If it already exists, it is erased and not restarted. After the job has finished, the file is no longer existent.
* ``DELETE`` Same effect as ``SCRATCH``.

Note that ``RESTART`` is now the default for all permanent files. All temporary files are usually allocated automatically where needed. I/O buffers are allocated at the top of the dynamic memory, and the available memory decreases by the size of the buffers. The ``MEMORY`` card must therefore be presented before the first ``FILE`` card!

Examples:

* ``FILE,1,H2O.INT`` allocates permanent file 1 with name ``H2O.INT``. Previous information on the file is recovered.
* ``FILE,2,H2O.WFU,NEW`` allocates permanent file 2 with name ``H2O.WFU``. All previous information on the file is erased.

Note that filenames are converted to lower case on unix machines.

.. _file_handling--delete:

DELETE
======

``DELETE,file1, file2, …``

Deletes the specified files. *file* refers to the logical Molpro file numbers as specified on the ``FILE`` card.

.. _file_handling--erase:

ERASE
=====

``ERASE,file1, file2, …``

Erases the specified files. *file* refers to the logical Molpro file numbers as specified on the ``FILE`` card.

.. _file_handling--data:

DATA
====

The ``DATA`` command can be used to modify the Molpro binary files.

* **``RENAME``,\ *rec1*,\ *rec2*** used to rename *rec1* to *rec2*. *rec1* and *rec2* must be given in the form *name.ifil*, where *ifil* is the number of a Molpro binary file (alias for ``NAME``).
* ``TRUNCATE,nen`` used to truncate files after *nen-1* records (alias for ``NEN``).
* ``TRUNCATE,rec`` used to truncate before record *rec*. *rec* must be given in the form *name.ifil*, where *ifil* is the number of a Molpro binary file.
* ``COUNT`` Alias for ``NRE`` (presently not used)
* **``COPY``,\ *rec1*,\ *rec2*** Copies record *rec1* to *rec2*. *rec1* and *rec2* must be given in the form *nam1.ifil1*, *nam2.ifil2*. If *nam2=0*, *nam2=nam1*. If *nam1=0*, all records are copied from file *ifil1* to file *ifil2*.

.. _file_handling--assigning-punch-files-punch:

Assigning punch files (PUNCH)
=============================

``PUNCH,filename,[REWIND]``

Opens punch file named *filename*. If this file already exists, it is appended, unless the ``REWIND`` or ``NEW`` option is specified; in that case, any previous information on the punch file is overwritten. See ``FILE`` for machine dependent interpretation of filename. The punch file contains all important results (geometries, energies, dipole, transition moments etc). It can be read by a separate program *READPUN*, which can produce tables in user supplied format.

Example:

* ``PUNCH,H2O.PUN`` allocates punch file ``H2O.PUN``

Note that the file name is converted to lower case on unix machines.

.. _file_handling--molpro-system-parameters-gparam:

MOLPRO system parameters (GPARAM)
=================================

The ``GPARAM`` card allows to change ``MOLPRO`` system parameters. This should only be used by experts!

``GPARAM,option=value,$\ldots$``

The following options can be given in any order.

* ``NOBUFF`` if present, disable system buffering
* ``LSEG`` disk sector length
* ``INTREL`` number of integer words per real word (should never be modified!)
* ``IBANK`` number of memory banks. Default is 2, which should always be o.k.
* ``IVECT`` 0=scalar, 1=vector machine
* ``MINVEC`` minimum vector length for call to mxmb
* ``LTRACK`` page size in buffer routines (must be multiple of *lseg*)
* ``LENBUF`` length of integral buffer (file 1)
* ``NTR`` length of integral records (must be multiple of :math:`3 \cdot`\ *ltrack*)
* ``LTR`` disk sector length assumed in CI (default 1 is reasonable)
* ``NCACHE`` machine cache size in bytes
* ``IASYN`` if nonzero, use asynchronous I/O on CONVEX
* ``MXMBLK`` column/row block size for mxma
* ``MXMBLN`` link block size for mxma
* ``NCPUS`` maximum number of cpus to be used in multitasking
* ``MINBR1`` min number of floating point ops per processor
* ``MXDMP`` highest file number to be treated as dump file with full functionality (:math:`1 \le.` ``MXDMP``\ :math:`\le.3`).

The ``MXDMP`` option is for experts only! This prevents basis and geometry information from being written to dump files with higher file number than the given *value*, and can sometimes be useful for counterpoise corrected geometry optimizations. Note that some functionality is lost by giving this option, and errors will result unless all input is correct!
