.. _general_hints_-_frequently_asked_questions--general-hints-frequently-asked-questions:

General hints - frequently asked questions
==========================================

Molpro users should have a basic knowledge of quantum chemistry, from text books as recommended below.

Also, a basic knowledge of Linux / macOS is required.

.. code-block:: text

As an introduction, studying the examples in this manual is recommended. Also, the Molpro forum at
`https://groups.google.com/g/molpro-user <https://groups.google.com/g/molpro-user>`__
provides a lot of information. We request to post questions concerning Molpro to this forum.

Text books:

* A. Szabo and N.S. Ostlund: Modern Quantum Chemistry (McGraw-Hill, New York, 1989)
* T. Helgaker, P. Jørgensen, J. Olsen: Molecular Electronic-Structure Theory (Wiley, Chichester, 2000)
* F. Jensen: Introduction to Computational Chemistry (Wiley, Chichester, 2017)
* Christopher J. Cramer: Essentials of Computational Chemistry: Theories and Models (Wiley, Chichester, 2004)
* W.J. Hehre, L. Radom, P.v.R. Schleyer, and J.A. Pople: Ab initio molecular orbital theory (Wiley, New York, 1986)
* W. Kutzelnigg: Einführung in die Theoretische Chemie (Wiley-VCH, Weinheim, 2001)

.. _general_hints_-_frequently_asked_questions--in-a-nutshell-how-to-start:

In a nutshell: how to start
===========================

Beginners should start with Hartree-Fock (basic theory, set up an input for HF, understanding the wf-card input and so on, try out basis sets, inspect orbitals); then one may: 
- either pursue single-reference methods such as MP2, CCSD and variants 
- or progress to MCSCF (MULTI) : wf-card, occ, closed, frozen card etc; then methods such as MRCI 

After being familiar with these methods, one may explore more sophisticated tools which rely on them.

DFT is in many parts similar to Hartree-Fock concerning the input.

One should start with a basic input and then gradually increase complexity; it is not a good idea to start with
a complicated input and then change input parameters without any knowledge what these parameters are meant for.
Break problems into small pieces, and try to solve the smaller problems.

A more extended introduction how to use Molpro is in :doc:`this section of the manual <quickstart>`.

Introductory `lecture notes <https://www.cond-mat.de/events/correl21/manuscripts/doll.pdf>`__ and corresponding `slides <https://www.cond-mat.de/events/correl21/talks/doll.pdf>`__ from an autumn school in Jülich.

.. _general_hints_-_frequently_asked_questions--miscellaneous:

Miscellaneous
=============

* Computational parameters such as tolerances, thresholds have been carefully calibrated. Usually they do not need to be changed.
* ``gprint,basis,orbitals,civector`` may be inserted so that these data are available in the output file; it however makes the output file larger. Use e.g. ``gprint,orbitals=2`` to print occupied and two lowest virtual orbitals
* Molpro uses a default memory size `(see here) <general_program_structure.html#memory-allocation>`__ which should be sufficient for small systems. When requesting more memory, it is recommended to first get some experience about the memory necessary, and then request a reasonable amount of memory, and not astronomic memory for small systems.

.. _general_hints_-_frequently_asked_questions--geometry:

Geometry
========

.. code-block:: text

* The units have to be correct (Angstrom versus bohr). By default, xyz input is in Angstrom, while z-matrix coordinates are in atomic units.
* A geometry which strongly deviates from the experimental geometry may cause convergence problems. This may be due to unrealistic bond lengths or angles. E.g. breaking a bond may require to change the wave function card or method (remember the text book example of H<sub>2</sub> with a large bond length, RHF versus UHF).
* If any kind of problems in a calculation occurs, it is recommended to visualise the geometry and check it for correctness.

.. code-block:: text

.. _general_hints_-_frequently_asked_questions--basis-set:

Basis set
=========

* The basis set has to be chosen with respect to the method, and with respect to the property to be computed.
* Negatively charged atoms need diffuse basis functions. A typical example is a molecule containing oxygen, where oxygen usually becomes negatively charged.

.. _general_hints_-_frequently_asked_questions--scf-calculations:

SCF calculations
================

* Symmetry should be exploited if possible. The calculations are faster, easier to converge, and easier to analyse if symmetry is used.
* It should be checked if the symmetry and spin state is correct. The program attempts to find the ground state configuration from the Aufbau principle, but this may fail and then the wave function symmetry and spin need to be specified using a WF (wave function) directive.
* After convergence, especially of difficult cases, it is recommended to check orbitals and populations, possibly visualise orbitals.
* After converging a difficult system, it may occasionally be necessary to reorder the orbitals ("rotate" command) before performing a subsequent correlation calculation.

.. _general_hints_-_frequently_asked_questions--convergence-of-energy-calculations:

Convergence of energy calculations
==================================

Before increasing the number of iterations to very high values (such as "maxit,500") far beyond the default:

* check the geometry
* check the initial orbitals (especially in case of MRCI)
* check the choice of the active space

See also `here <the_scf_program.html#handling-difficult-cases-when-scf-does-not-converge>`__ for hints how to converge SCF calculations.

.. _general_hints_-_frequently_asked_questions--mcscf-calculations:

MCSCF calculations
==================

* The active space (occ, frozen, closed) has to be chosen carefully. (Nearly) degenerate states and low lying excited states should be included, based on e.g. SCF eigenvalues.
* AVAS may help to construct suitable starting orbitals.
* NOEXTRA may be necessary in some cases, e.g. if a previous HF calculation was done with nosym

.. _general_hints_-_frequently_asked_questions--mrci-and-caspt2-calculations:

MRCI and CASPT2 calculations
============================

.. code-block:: text

* The active space has to be reasonably chosen (occ, core, closed); e.g. typically after an MCSCF calculation, an MRCI calculation is followed with the same active space.
* When excited states are computed, then the preceding MCSCF should be state averaged, and include the excited states so that the orbitals from which the MRCI starts are reasonable. E.g.  ``multi;occ,14,4,9,2;frozen,12,1,6,0;wf,47,1,1;state,3`` may be followed by  ``mrci;occ,14,4,9,2;core,12,1,6,0;wf,47,1,1;state,3;``
* MCSCF and MRCI are not black-box like, and e.g. a visualisation of the MCSCF orbitals will help to set up the active space.

.. _general_hints_-_frequently_asked_questions--limit-of-32-active-orbitals:

Limit of 32 active orbitals
===========================

There is a limit of at most 32 active orbitals which is unlikely to be increased in the near future, see
`here <https://www.molpro.net/pipermail/molpro-user/2017-June/006959.html>`__. An active space of 32 active orbitals is however quite large, and usually smaller active spaces should be sufficient.

.. _general_hints_-_frequently_asked_questions--print-all-orbital-coefficients-instead-of-those-which-are-above-the-default-threshold:

Print all orbital coefficients instead of those which are above the default threshold
=====================================================================================

use: ``gthresh,thrprint=0`` see [[https://www.molpro.net/manual/doku.php?id=program_control&s[]=thrprint#global_thresholds_gthresh\|here]]

.. _general_hints_-_frequently_asked_questions--molpro-no-such-file-or-directory:

molpro: No such file or directory
=================================

After installation, you will usually not be able to call molpro by just typing ``molpro``, and you will get
error messages such as e.g. ``No such file or directory`` or ``command not found``.
You have to bring ``molpro`` into the path. There are various ways such as setting a symbolic link e.g.
from ``$HOME/bin/molpro`` to the installed ``molpro`` or explicity including it in the path.
Please use a search engine or a book for such questions about Linux.

.. code-block:: text

.. _general_hints_-_frequently_asked_questions--molpro-not-running:

molpro not running
==================

If molpro is in the path, but not properly running, then
``molpro -v``
may help to get information about what goes wrong.

.. _general_hints_-_frequently_asked_questions--hardware:

Hardware
========

It is recommended to use a computer with large memory (RAM) and large disk; also a large memory bandwidth is advantageous.
We can however not recommend a certain vendor or CPU. For CPU benchmarks,
`https://www.spec.org <https://www.spec.org>`__  may be useful.
