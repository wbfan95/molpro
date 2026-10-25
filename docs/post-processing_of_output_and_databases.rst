.. raw:: html

   <span id="databases"></span>

.. raw:: html

   <span id="interrogation-and-manipulation-of-databases"></span>

.. _post-processing_of_output_and_databases--post-processing-of-output-and-databases:

Post-processing of output and databases
=======================================

.. _post-processing_of_output_and_databases--output:

Output
======

Molpro produces an output file that is in XML format with appropriate mark-up for all important results. This file, which has a ``.xml`` suffix, conforms strictly to a `well-defined schema <https://www.molpro.net/schema/molpro-output.xsd>`__, and the the schema definition file can be found in the main Molpro source or installation tree in the directory ``lib/schema``. The principal elements of marked-up output are

* **jobstep** The results from one job step.
* **molecule** A container for data on a single molecule.
* **cml:molecule** Molecular geometry in the Chemical Markup Language (CML) format.
* **property** A computed property, for example an energy or dipole moment.
* **table** The output of Molpro’s ``TABLE`` command in XHTML format.
* **basisSet** A self-contained description of the orbital basis set.
* **orbitals** A set of orbitals.
* **vibrations** Harmonic normal vibrational modes.
* **variables** Molpro’s internal variables.
* **platform** Information about the computing system on which a job was run.

Not all of these elements are produced by default in the regular job transcript ``.xml`` file; some of them can result from using the ``PUT,XML`` to make a separate dump file.

``molpro-output`` is understood by several post-processing programs, including `Jmol <https://jmol.org>`__, `sjef <https://github.com/molpro/sjef>`__, `iMolpro <https://github.com/molpro/iMolpro>`__, and gmolpro. There is extensive support for it in the `pymolpro <https://github.com/molpro/pymolpro>`__ library, which should be the normal route for accessing data. Pymolpro is available on `conda forge <https://conda-forge.org/>`__, and some examples of its use can be found `here <https://molpro.github.io/pymolpro/examples.html>`__.

.. _post-processing_of_output_and_databases--databases:

Databases
=========

Pymolpro also provides a facility  to store and interrogate sets of molecules, together with information about how they are to be combined in balanced chemical equations. This collection of information is referred to as a *database*, and can be generated completely manually, or partially by running appropriate Molpro calculations; the library contains also a number of the standard quantum chemistry benchmark sets. Analysis of the database can give a summary of the energy changes associated with each described reaction, and two or more similar databases can be compared reaction by reaction, to give a statistical analysis of the differences between them. See pymolpro documentation for `details <https://molpro.github.io/pymolpro/pymolpro.html#module-pymolpro.database>`__ and `examples <https://molpro.github.io/pymolpro/examples/thermochemical_benchmark_Bak2000_atomisations.html>`__.
