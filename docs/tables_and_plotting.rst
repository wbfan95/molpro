.. raw:: html

   <span id="tables"></span>

.. _tables_and_plotting--tables-and-plotting:

Tables and plotting
===================

.. _tables_and_plotting--tables:

Tables
======

Variables can be printed in Table form using the command

``TABLE,var1,var2,…``

The values of each variable are printed in one column, so all variables used must be defined for the same range, and corresponding elements should belong together. For example, if in a calculation one has stored ``R(i), THETA(i), ECI(i)`` for each geometry *i*, one can print these data simply using

``TABLE, R, THETA, ECI``

By default, the number of rows equals the number of elements of the first variable. This can be changed, however, using the ``RANGE`` subcommand.

The first ten columns of a table may contain string variables. For instance,

.. code-block:: text

   hf;etot(1)=energy;method(1)=program;cpu(1)=cpustep
   ccsd;etot(2)=energy;method(2)=program;cpu(2)=cpustep
   qci;etot(3)=energy;method(3)=program;cpu(3)=cpustep
   table,method,etot,cpu

prints a table with the ``SCF``, ``CCSD``, and ``QCI`` results in the first, second, and third row, respectively. For other use of string variables and tables see the examples in `Tables <introductory_examples.html#tables>`__ and `Macro definitions using string variables <variables.html#macro-definitions-using-string-variables>`__.

The appearance of the table may be modified using the following commands, which may be given (in any order) directly after the the ``TABLE`` card:

* **``HEADING,``\ *head1, head2,…*** Specify a heading for each column. By default, the names of the variables are used as headings.
* **``FORMAT,``\ *format*** Specify a format for each row in fortran style. *format* must be enclosed by round brackets. Normally, the program determines automatically an appropriate format, which depends on the type and size of the printed data.
* **``FTYP``,\ *typ1, typ2, typ3, …*** Simplified form to modify the format. This gives the type (``A, F``, or ``D``) for each column (sensible defaults are normally used).
* **``DIGITS``,\ *dig1, dig2, dig3, …*** Give the number of digits after the decimal points to be printed for each column (sensible defaults are normally used).
* ``TYPE`` Specify a data format for the table. The default is ``TEXT`` which gives a plain text file. Other possibilities are ``CSV`` (comma-separated fields suitable for a spreadsheet), ``LATEX`` (a LaTeX ``table`` environment), ``MATHEMATICA`` (Mathematica code that assigns the table to an array), ``MATLAB`` (Matlab code that assigns the table to an array), ``MAPLE`` (Maple code that assigns the table to an array), ``HTML`` (an HTML construction), ``PYTHON`` (a Python script that contains the data and generates a 2-dimensional plot using `matplotlib <http://matplotlib.org>`__), and ``XML`` (an XML document containing a tree representing the table. The actual format is `XHTML <http://www.w3.org/1999/xhtml>`__).
* **``SAVE``,\ *file,status*** Specify a file on which the table will be written. If *status* is ``NEW``, the file is rewound, otherwise it is appended. In the case of Python format, unless *status* is ``NEW``, any edits that have been made to a pre-existing file will be preserved, and only the table data will be replaced. If *file* has a suffix that is one of ``txt, csv, tex, m, mpl, py, html, xml``, and a ``TYPE`` command is not specified, then the type will be set to that which is conventionally appropriate for the suffix. If *file* is omitted, then a file name is automatically generated, with the form *input*.\ ``table``\ :math:`n`.\ *ext*: *input* is the basename of the input file (or ``molpro`` if running from standard input); :math:`n` is a sequence number that is incremented by one each time a table is produced; *ext* is a suffix appropriate to the file format, eg ``txt``, ``html``, etc.
* **``TITLE,``\ *title*** Specify one line of a title (several ``TITLE`` cards may follow each other). Note that titles are only displayed in the ``SAVE`` file, if the ``SAVE`` command is given before the ``TITLE`` card.
* **``SORT,``\ *col1,col2,…*** Sort rows according to increasing values of the given columns. The columns are sorted in the order they are specified.
* **``PRINT,``\ *key1,key2,…*** Specify print options (``TABLE, HEADING, TITLE, WARNING, FORMAT, SORT``). The default is print for the first three, and noprint for the last three.
* **``NOPRINT,``\ *key1,key2,…*** Disable print for given keys.
* ``NOPUNCH`` Don’t write data to the punch file (data are written by default).
* **``RANGE,``\ *start,end*** Specify start and end indices of the variables to be printed.
* ``STATISTICS`` Print also linear regression, upper and lower bounding lines, and quadratic fits of the data columns. The slopes and intercepts of these lines are saved in the Molpro variables

``REGRESSION_SLOPE, REGRESSION_INTERCEPT,\\``
``LOWERBOUNDMIN_SLOPE, LOWERBOUNDMIN_INTERCEPT,\\``
``UPPERBOUNDMIN_SLOPE, UPPERBOUNDMIN_INTERCEPT,\\``
``LOWERBOUNDMAX_SLOPE, LOWERBOUNDMAX_INTERCEPT,\\``
``UPPERBOUNDMAX_SLOPE, UPPERBOUNDMAX_INTERCEPT.``

For the Python data format, the output is a complete Python module containing the following.

* ``molpro_table`` - a dictionary containing the title and columns
* ``plot_molpro_table()`` - a function that takes table data and plots the 2nd, 3rd,... columns against the first.
* ``latex_molpro_table()`` - a function that produces a Latex table environment, optionally transposing the data.
* A main program that runs ``plot_molpro_table()`` with default options

If the output file is modified after running Molpro, a subsequent run of Molpro will replace the data, but leave the code modifications intact.

Example:

.. code-block:: text

   do i=1,37; x(i)=(i-1)*10; c(i)=cos(x(i)); s(i)=sin(x(i)); enddo
   table,x,c,s;save,trig_example.py,new,2;title,'Trigonometry';title,'sines and cosines'

followed by, in Python,

.. code-block:: text

   from trig_example import molpro_table, latex_molpro_table, plot_molpro_table
   plot_molpro_table(molpro_table,'trig_example') # produces trig_example.pdf, just like python trig_example.py
   print(latex_molpro_table(molpro_table, decimals=3, transpose=False))

The Python environment should include the ``matplotlib``, ``scipy`` and ``numpy`` packages.

.. _tables_and_plotting--plotting:

Plotting
========

``[PLOT[,col1,col2,$\dots$][,options]``

Construct input for a plotting program using the table as data. ``PLOT`` is a subcommand of ``TABLE`` and must follow ``TABLE`` or any of its valid subcommands given in the previous section. More than one ``PLOT`` command can be included within a single ``TABLE``, and each invocation generates a new plot. However, ``PLOT`` must appear after all other ``TABLE`` subcommands.

*col1*, *col2*,\ :math:`\dots` are the names of the table columns to be plotted. These must be an exact subset of those given on the ``TABLE`` command. The first column is taken as abscissa, and the values of the remainder will be plotted against it. If no columns are specified, then the entire table is plotted; if a single column is specified, it will be used as abscissa, and all other columns in the table will be plotted as ordinate. *options* can be chosen from the following.

* **``CMD=``\ *unix_plot_command*** *unix_plot_command* consists of the system command needed to start the plotting program, followed by any required options. The whole thing should normally be enclosed in quotation marks to preserve lower-case letters. The default is ``’xmgrace’``. At present, the `//Grace// <http://plasma-gate.weizmann.ac.il/Grace>`__ program (also known as *xmgrace, grace, gracebat*), with only numerical data, is supported. The output is also compatible with the portable drop-in replacement for Grace, `//AptPlot// <http://www.aptplot.com/>`__, and if *Grace* is not found on the system, Molpro will attempt to use *AptPlot* as default instead.
* **``FILE=``\ *plotfile*** By default the input file for the plotting program is saved in *input*.\ ``table``\ :math:`n`.\ ``plot``\ :math:`m`.\ ``agr``, where :math:`m` is an automatically generated sequence number. The name of the plotfile can be modified using the ``FILE`` option.
* ``INTERACTIVE`` By default, the plot is not shown on the screen but all plot data are saved in the given file. The plotting program can be started interactively by giving the ``INTERACTIVE`` option.
* **``TYPE=``\ *type*** If ``TYPE`` is specified, *type* should be set to one of ``pdf``, ``svg``, ``png``, ``jpeg`` or ``eps``. The result is that the ``gracebat`` program is executed on the plot input file to generate the graph output file in the desired format. This feature depends on the availability of ``gracebat``, and on it supporting the requested output format (for example, at present pdf is supported under Mac OS X, but not in some Linux systems).
* **``BACKGROUND=``\ *rgb*** *rgb* should be a string of six hexadecimal digits specifying the red-green-blue colour to use for the background of the plot.
* ``BACKGROUND=TRANSPARENT`` The background of the plot is made transparent (currently implemented only for ``TYPE=svg``).
* ``NOSPLINE`` Prevents spline interpolation of data points
* **``CURVE=``\ *type*** Specifies type of curve to be drawn with points. Possibilities are ``SPLINE`` (default; spline interpolation); ``NONE`` (equivalent to ``NOSPLINE``); ``REGRESSION`` (linear regression line); ``UPPERBOUNDMAX`` (maximum gradient line that bounds points from above); ``UPPERBOUNDMIN`` (minimum gradient line that bounds points from above); ``LOWERBOUNDMAX`` (maximum gradient line that bounds points from below); ``LOWERBOUNDMIN`` (minimum gradient line that bounds points from below).
* **``NSPLINE=``\ *number*** Number of interpolation points (default 20)
* **``LEGEND=’``\ *x, y*\ ``’``** Position legend at :math:`(x,y)` on plot.
* ``LEGEND=OFF`` Do not draw legend; this behaviour is chosen automatically when there is only a single ordinate dataset.
* **``PCOMMAND=’``\ *command*\ ``’``** Insert arbitrary *Grace* command into the plot file; for details, consult http://plasma-gate.weizmann.ac.il/Grace/doc/UsersGuide.html#s5.

The following additional directives can be given *before* the ``PLOT`` directive:

* **``COLOUR``,\ *icolour1, icolour2,...*** Colour map to be used for columns 1,2,...; zero means to use default values (colours black, blue, red, green cycle)
* **``COLOUR``,\ *rgb1, rgb2,...*** Absolute colours (6-hex-digit rgb values) to be used for columns 1,2,...;
* **``SYMBOL``,\ *isymb1, isymb2,...*** Symbol types to be used for columns 1,2,...; -1 means no symbols; zero means to use default values.
* **``LINEWIDTH``,\ *width1, width2,...*** Line widths to be used for columns 1,2,...; omit to use default values.
* **``LINESTYLE``,\ *style1, style2,...*** Line styles to be used for columns 1,2,...; omit to use default values.

.. _tables_and_plotting--diatomic-potential-curve-analysis:

Diatomic potential curve analysis
=================================

For the case that a table contains one or more potential energy functions for a diatomic molecule, with the first column containing bond lengths in Bohr or Ångstrom, it is possible to calculate spectroscopic constants using

``DIATOMIC[,DEGREE=n][,MASS=m][,PRINT=p]``

The data are fitted to a polynomial of degree :math:`n` (default is number of points minus 1, ie interpolation), and spectroscopic constants calculated using reduced mass :math:`m` expressed in u. Note that it is possible to constrain which bond lengths are used through the use of the ``RANGE`` subcommand.

D\ :math:`_{\rm e}` and D\ :math:`_0` are computed from the energy at the fitted minimum distance, and the energy at the longest distance along the potential curve. If the longest distance is less than 10 Å, then D\ :math:`_{\rm e}` and D\ :math:`_0` are not computed, and instead a value of 0 is printed.
