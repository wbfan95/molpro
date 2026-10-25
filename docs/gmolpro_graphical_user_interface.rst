.. _gmolpro_graphical_user_interface--gmolpro-graphical-user-interface:

gmolpro graphical user interface
================================

`introduction to gmolpro <https://vimeo.com/493402264>`__

gmolpro is a GTK-based graphical interface to Molpro that runs on Linux and macOS workstations.

Basic Molpro inputs can be very quickly generated. Sensible basis sets and input parameters are suggested.
The preparation of inputs is supported through an expert system that interacts with Molpro’s registry of commands, methods, and basis sets, guiding the user toward feasible combinations of calculation types (single point, optimization, etc.), methods, basis sets, and options.

Checks are implemented so that the geometry, charge, and spin are consistent, and only appropriate methods are selected. Reasonable default settings are provided so that an input can be easily set up. It also provides a plain-text editor to allow further editing of existing job inputs, or simply copy in general input files.

Molecular structures can be constructed and edited using an
integrated builder derived from the `PQSMol <http://www.pqs-chem.com/software.php>`__ interface to the `PQS <http://www.pqs-chem.com/software.php>`__ package, see also the `corresponding manual (pdf file) <http://www.pqs-chem.com/downloads/PQSMol-man.pdf>`__. It incorporates fragment libraries (over 200 molecules and functional groups), force fields, and an optimization based on force fields. Jobs can then be submitted and managed on the local computer or a remote machine.

Visualisation of results includes interactive display of structures (also for the individual optimisation steps), orbitals, property maps, and vibrational modes.
Outputs from Molpro calculations set up with gmolpro, as well as output files from general input files can be visualised;
e.g. orbitals with all angular momenta implemented in Molpro (*s, p, d, f, g, h, i*) may be quickly visualised.

one of the i-orbitals: `window-h-i6plus-occupied.png <media/window-h-i6plus-occupied.png>`__

.. _gmolpro_graphical_user_interface--prerequisites:

Prerequisites
=============

gmolpro (present release: version 2.8.0) should be used together with Molpro2025.2. On Mac, the package you download is already bundled with this Molpro version. On Linux, gmolpro does not come bundled with Molpro, and you need a separate installation of Molpro. Note that on macOS, gmolpro starts without visiting shell initialisation scripts if you start it by clicking on the icon in the Mac Dock.

It requires

- a macOS (12.X i.e. Monterey or later) or Linux (Ubuntu 18.04 or later, Debian 11 or later, Fedora  42 or later, or openSUSE 15.6 or later) workstation; other macOS or Linux versions ***may (and often will)*** work
- a licence token which is valid for molpro and gmolpro. It may be installed in ``$HOME/.molpro/token`` . Alternatively (useful for group licences) on Linux, it may be installed in the place as described in the :doc:`installation_guide <installation_guide>`, and on Mac in ``/Applications/gmolpro.app/Contents/Resources/molpro/lib/.token`` (the gmolpro app should always be installed in the default place ``/Applications/gmolpro.app`` )

.. list-table::
   :header-rows: 1

   * - gmolpro release versus ...
     - ... recommended Molpro version
     - remarks
   * - 2.10.0
     - 2025.4 (Linux: needs separate installation; Mac: bundled with 2025.4.0)
     - 
   * - 2.9.0
     - 2025.3 (Linux: needs separate installation; Mac: bundled with 2025.3.0)
     - 
   * - 2.8.0
     - 2025.2 (Linux: needs separate installation; Mac: bundled with 2025.2.0)
     - Molpro versions from 2025.2 on need gmolpro version at least 2.8.0 because the basis set library has been extended
   * - 2.7.0
     - 2025.1 (Linux: needs separate installation; Mac: bundled with 2025.1.0)
     - Molpro versions beyond 2025.1 need gmolpro version at least 2.7.0 because the xml file will be split in xml and xml-sidecar
   * - 2.6.0
     - bundled with 2024.3.0
     - 
   * - 2.5.0
     - bundled with 2024.2.0
     - linux version of Molpro2024.2.0 needs glibc >= 2.27
   * - 2.4.0
     - bundled with 2024.1.0
     - 
   * - 2.3.0
     - bundled with 2024.1.0
     - 
   * - 2.2.0
     - bundled with 2023.2.0
     - 
   * - 2.1.0
     - bundled with 2022.2.3
     - 
   * - 2.0.0
     - bundled with 2022.2.2
     - 
   * - 1.4.0
     - 2022.1
     - 
   * - 1.3.1
     - 2021.3
     - 
   * - 1.1
     - 2021.1
     - 

Hint: very old versions (2.2.0 and before) may need to set the variable LIBGL_ALWAYS_SOFTWARE to TRUE (e.g. in bash ``export LIBGL_ALWAYS_SOFTWARE=1``) on some platforms such as openSUSE15.5, before starting gmolpro (bug in the Mesa library)

``On fedora, dnf install gdk-pixbuf2-xlib gdk-pixbuf2-modules-extra may be necessary.``

In general, packages may have to be installed if they were not shipped with the operating system, e.g. freeglut.

.. _gmolpro_graphical_user_interface--projects:

Projects
========

All files belonging to a particular calculation (input, output, geometry etc.), as well as additional data, are contained in a *project*, which is implemented as a filesystem directory (a bundle). gMolpro automatically creates and maintains these projects. Project directories have extension ``.molpro``, e.g. ``c2h2.molpro``.

.. _gmolpro_graphical_user_interface--starting-gmolpro:

Starting gMolpro
================

.. list-table::

   * - `starting gmolpro <https://vimeo.com/471037256>`__
     - gmolpro can be started either by typing ``gmolpro`` in a terminal window, or by launching the gmolpro application in the way that is usual on your system.  When it opens, you are presented with the splash screen, which gives the opportunity to start a new project or open an existing one. Let's make a new one. We are first of all prompted to specify where to save it; from that point on, all changes to the project are written immediately to file without any save or similar commands. Next, we see two windows, denoted *input* (blue) and *build* (lilac). In the input window, we can set  parameters for the calculation, whereas in the build window, we construct the molecular geometry. Let's construct a favourite molecule by taking it from the built-in library of molecular fragments. There is more you can do to build and edit the structure, but for now we will switch to the input window and run a calculation. We need to tell it at the minimum what method (let's choose B3LYP) to use, and for now we will just leave all other options alone. We can then use the ``Run`` button to launch the job. At this point, it is fine to close the project even if the job has not yet finished; we are then returned to the splash screen, where you can open another project, or quit.

.. _gmolpro_graphical_user_interface--windows:

Windows
=======

gMolpro displays four different windows. The ``input`` (blue) and ``build`` (lilac) windows support preparation of a job, where as the ``output`` (white), ``view`` (brown) windows, which appear only once a job has started, show results. Switching between windows can be achieved using the ``Windows`` menu or with the keyboard shortcuts shown in the menu.

.. _gmolpro_graphical_user_interface--input-window-blue:

Input Window (blue)
===================

.. list-table::

   * - `input window <https://vimeo.com/778042061>`__
     - The window guides though the options for a calculation, constructing Molpro input for DFT and single-reference calculations. Generally, one should go through this window from top to bottom, since some settings depend on each other. Let's look at the possibilities. The geometry can be imported from an xyz file(``Import Geometry``) or generated using the ``Builder Window``. Imported xyz files are not modified in the project, but can change during the calculation due to orientation or geometry optimization, and the optimized geometries can be exported and reused in subsequent calculations. The next important decision is the overall type of calculation - single geometry or structure optimization, with or without harmonic frequencies.  We should then choose the method; let's try a correlated-wavefunction CCSD(T) calculation. The default for the Hamiltonian model is to use pseudopotentials to represent core electrons where appropriate, but you can choose instead to include all electrons, either non-relativistically or with a scalar relativistic Hamiltonian. There is also the possibility to specify whether and how core orbitals are included in the correlation treatment. The final principal choice is the basis set. The guided proposals for this are dependent on the method, Hamiltonian and core correlation. You should first choose the overall quality - double, triple,... zeta - and then select within that if desired. It's also possible to specify the basis set element by element.  The remainder of the input is associated with further options to control the running of the calculation and what it produces.

**Further notes:**

* Density fitting can be switched on or off by clicking the ``Density Fitting`` button (depending on the method).
* ``Pseudopot. if available`` means to use (small core) pseudopotentials together with the associated basis sets when these are available (heavier elements), and all-electron basis sets for all other elements.
* ``Core-correlation:`` ``mixed`` means to include outer core orbitals for elements left of the p-block in the periodic system. ``small`` means also to include (outer) core orbitals of other elements. Note that the basis sets depend on these settings.
* ``Basis sets:`` first choose the quality (e.g. TZ, QZ), and then the default basis set. The recommended basis sets depend on the method. If the default basis is not available for some atom(s), or the use of other basis sets is desired for some atoms, use the element specific basis pulldown menu.
* The right-hand pane showing the input is not directly editable when in "guided mode". However, one can leave guided mode by clicking on this pane, and then any valid Molpro input can be entered.  It is not possible to return to guided mode once it has been left. Externally-created projects also will open in this freehand mode.

.. _gmolpro_graphical_user_interface--builder-window-lilac:

Builder Window (lilac)
======================

.. list-table::

   * - `starting gmolpro <https://vimeo.com/778043408>`__
     - This window is used to build and pre-optimize molecular structures. On the right-hand side one can choose building blocks or fragments, which are then connected to the molecule in the left window. This is best illustrated by an example. Let’s build glycine, NH\ :sub:`2`\ CH\ :sub:`2`\ COOH. The easiest is of course to take it from the provided structures (click fragment - amino_acids - gly), but we can also build it step by step. Click ``Building Blocks``, choose ``C`` in the periodic table, click on the symbol for C with 4 single bonds. The atom appears in the ``Segment Window``. Click ``+`` in the lower icon list under the left window and click on the left window. The C-atom is copied to that position. Now continue to add the NH\ :sub:`2` group: Click on ``Fragments``, ``FUNCTIONAL_GROUPS``, ``amino``. Then click in the left window on the dangling bond to which you want to add the amino group. Next add the COOH group similarly. At this point, we have the full structure, but with some remaining dangling bonds that should be terminated with hydrogen. We do this by clicking on ``H`` in the upper left corner of the left window. Conformational and other adjustments can be carried out by, for example, rotating about bonds: click ``Rotate About a Bond`` in the bottom list of the left window, select the bond by clicking on it, then drag with the mouse to rotate. The structure can be preoptimized using a force field via the ``Optimize`` menu on top of the left window, or ``Optimize`` upper button.

.. _gmolpro_graphical_user_interface--output-window-white:

Output window (white)
=====================

.. list-table::

   * - `output window <media/output_window.jpg>`__
     - This window displays, with continuous update, the raw output produced by Molpro once the job has started. A second tab is provided for inspecting the log file that is used, for example, in geometry optimisations.

.. _gmolpro_graphical_user_interface--view-window-brown:

View window (brown)
===================

.. list-table::

   * - `starting gmolpro <https://vimeo.com/471041694>`__
     - The view window shows the final structure, ie after any geometry optimisation. It can also be used to display properties such as vibrational modes and orbitals, as well as the history of the geometry optimisation.  In this example, a geometry optimisation and frequency calculation has already been carried out for glycine, and localised orbitals have been obtained. Notice that, as in the build window, you can alter the view, rotating by dragging with the mouse, or zooming using the centre mouse button (Linux) or command-key and mouse (macOS). First, let's check what happened in the optimisation by clicking the ``Optimization History`` button. We can play a movie of the optimisation, or pick a particular point and export its geometry. The ``Vibrational Frequencies`` button shows the spectrum, from which individual modes can be selected and animated. The ``Orbitals`` buttons brings up an energy level diagram from which individual orbitals can be selected. If more than one type of orbital has been calculated, you can choose the active set. Choose further display options from the ``Display/Orbital`` menu.

.. _gmolpro_graphical_user_interface--running-calculations-on-remote-servers:

Running calculations on remote servers
--------------------------------------

.. list-table::

   * - `running on remote servers <https://vimeo.com/778043635>`__
     - When you click ``Run`` in the input window, by default, the calculation will be run on your local machine. gmolpro needs a local installation of Molpro. Support for running the calculation on another machine, with options such as process number and memory, is provided. One or more *backends* are defined in a file ``~/.sjef/molpro/backends.xml``. A backend is simply a specification of commands to launch, check and kill a job, and patterns to interpret status checks. One can then select which backend is assigned to the project, and this selection is remembered in the project's registry. The run command defined in the backend can be simply ``molpro``, or might be the name of a custom script to present a job to a scheduler such as Slurm.  The name of the command can be followed by parameters, which can also be specified in substitutable form, which lets you define per-project options to be used in the job submission and (optionally) their default values, e.g. for memory, number of parallel processes, job-scheduling parameters etc. These values can be modified in the "Run parameters" pulldown for a chosen backend.

Configuring a backend is requires usually just the hostname (which will be connected to with ssh, and which should be accessible without password; the shell on the remote machine is expected to be able to execute basic shell commands) and the name of the run command.  The run command script may contain any specified options, followed by a single argument that is the name of the input to Molpro. The ``molpro`` command conforms to this; for more complex requirements, for example for constructing a batch job, a wrapper script will be needed.
Further help is available on `the detailed syntax of the backend.xml file <https://molpro.gitlab.io/sjef/master/md__builds_molpro_sjef_lib_backends.html>`__.

If you wish to launch jobs on remote systems:

- a file ``~/.sjef/molpro/backends.xml`` is necessary on the local machine, which specifies the remote machine and how jobs are submitted
- Molpro must be installed on the remote machine. Jobs will fail if Molpro is not found on the remote machine.
- If jobs are managed by a scheduler, an appropriate script that constructs and submits the job is needed, with the name of the input file as its single argument, possibly preceded by options.

.. _gmolpro_graphical_user_interface--frequently-asked-questions:

Frequently asked questions
--------------------------

.. _gmolpro_graphical_user_interface--frequencies-or-optimisation-cannot-be-visualised-icon-is-greyed-out:

Frequencies or optimisation cannot be visualised - icon is greyed out
=====================================================================

The GUI searches for orbitals, and then displays which properties are available for these
orbitals.
Default is the last set of orbitals. If there is more than one set of orbitals, then it may
be necessary to load a different set of orbitals. E.g. in DFT calculations, the orbitals may
be written again at the very end. Then it may be necessary to load a set of orbitals written
before, to be able to visualise frequencies.

.. _gmolpro_graphical_user_interface--orbitals-cannot-be-visualised-icon-is-greyed-out:

Orbitals cannot be visualised - icon is greyed out
==================================================

Molpro must be run with flags ``--xml-output --xml-orbdump``    , i.e.:

``molpro --xml-output --xml-orbdump myinput.inp``

.. _gmolpro_graphical_user_interface--some-hints:

Some hints
----------

.. _gmolpro_graphical_user_interface--visualise-results-from-any-molpro-calculation:

Visualise results from any Molpro calculation
=============================================

If you did not use the GUI to generate the input, but want to visualise the output, then this can be
done in the following way:

1) run your input (e.g. h2o-demo.inp)

.. code-block:: text
   :caption: h2o-demo.inp

   geomtyp=xyz;
   geometry={
   3
   
   O  0.000000000000 0.000000000000 0.347935996933
   H  0.903964236600 0.000000000000 -0.173967998467
   H  -0.903964236600 0.000000000000 -0.173967998467
   }
   basis={
   default=cc-pV(T+d)Z-PP
   }
   {RHF}
   {OPTG}
   {FREQ}

with flags to generate xml output and orbitals in xml format

``molpro --xml-output --xml-orbdump  h2o-demo.inp``

2)  start gmolpro

3)  click on "New project", and choose a project name such as e.g.:  dummy

4) In any of the windows which open, in the toolbar at the top, there is a pulldown menu with an item

Window/Visualise results from/Molpro output (xml)

and then choose  h2o-demo.xml

The brown window opens, and there you may now visualise orbitals, go through the optimisation, animate frequencies etc.

.. _gmolpro_graphical_user_interface--visualize-an-input-structure:

Visualize an input structure
============================

To check a structure used in an input file, proceed like this:

1) Run the input, in addition with the flag --geometry

``molpro --geometry --xml-output --xml-orbdump  my-molecule.inp``

Note that it needs at least one jobstep, e.g. "hf" though this jobstep will not be executed.
Proceed as in "Visualise results from any Molpro calculation":

2,3,4) start gmolpro; click on "New project", and choose a project name such as e.g.: "dummy";
use the pulldown item Window/Visualise results from/Molpro output (xml),
and then choose my-molecule.xml

.. _gmolpro_graphical_user_interface--input-files-with-more-than-one-optimisation-etc:

Input files with more than one optimisation etc
===============================================

In freehand input or with input files not generated with the GUI, more general xml files can be generated.
Output files (xml files) with several optimisations, frequency calculations, or even different molecules within one xml file can be handled. Start from the brown window, open the orbital window, and then select and load an orbital set. A corresponding optimisation or vibrational modes may now be displayed.

.. _gmolpro_graphical_user_interface--more-general-inputs:

More general inputs
===================

The GUI helps to quickly generate a basic input. If you want a more general input, you can (in the blue window) in any stage click on the button "Switch to free-hand input".
Now you can edit the input manually. You may then run the input from the GUI with the "Run" button, and visualise with the brown window.

.. _gmolpro_graphical_user_interface--using-the-builder-alone-general-hints:

Using the builder alone: general hints
======================================

Already the builder alone is very powerful. Besides building molecules, it contains a large database of pre-built molecules. Also, a force-field optimisation may be performed, the point group determined etc.
The geometries in the builder are continuously saved to a file within the project. E.g. if the project is called mymolecule.molpro , then the xyz file of the molecule is stored in mymolecule.molpro/mymolecule.xyz . Obviously, this file may be copied to some other place, used by other programs etc.

.. _gmolpro_graphical_user_interface--using-the-builder-alone-visualise-an-xyz-file-or-a-trajectory-set-of-xyz-files:

Using the builder alone: visualise an xyz file or a trajectory (set of xyz files)
=================================================================================

To visualise an xyz file, start gmolpro, and open a new project. Then do ``Geometry/Import to builder window ...`` and select the xyz file to be visualised.

This allows also to visualise a trajectory. The trajectory must be a set of xyz files appended to each other.

.. _gmolpro_graphical_user_interface--running-several-instances-of-gmolpro-at-the-same-time-mac:

Running several instances of gmolpro at the same time (Mac)
===========================================================

To run several instances of gmolpro at the same time on Mac, open a terminal and type in the terminal:

``/Applications/gmolpro.app/Contents/MacOS/gmolpro &``

for each instance required.

.. _gmolpro_graphical_user_interface--retina-screens-mac:

Retina screens (Mac)
====================

If the molecule is not properly displayed, e.g. like this
`retina1.png <media/retina1.png>`__ or like that:

.. image:: /media/retina2.png
   :alt: retina2.png
   :width: 300px

-> Please use the switch Display/Retina screen.

This switches between factor 1 and 2. If you need a more general factor, please edit the line in $HOME/.pqsmol/gmolpro.conf
where it says:

retina_factor   1.000000

and insert the factor needed.

.. _gmolpro_graphical_user_interface--for-developers-using-a-different-molpro-version:

For developers: Using a different Molpro version
================================================

From version 2.0.0 on (and from 2.7.0, only the Mac version), gmolpro is bundled with Molpro, and uses this version of Molpro.
If you do not want to use the Molpro version in the bundle, then this can be achieved in the following way.
Open a terminal, and:

1)  If you use bash, export MOLPRO_ROOT:

``export MOLPRO_ROOT=/path/to/your/molproversion/``

where ``/path/to/your/molproversion/bin/molpro`` should be the script to run Molpro, and the binary should be found at ``/path/to/your/molproversion/bin/molpro.exe``

2) Then start gmolpro from the same terminal (note that on Mac, you cannot use a version installed in the Dock, as MOLPRO_ROOT is only known in the terminal where it was exported; also .bashrc is not read when you open gmolpro by clicking its icon in the Dock)
