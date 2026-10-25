.. _the_closed-shell_density_fitting_cc2_program_for_ground_and_excited_states--the-closed-shell-density-fitting-cc2-program-for-ground-and-excited-states:

The closed-shell density fitting CC2 program for ground and excited states
==========================================================================

The CC2 method is an approximate CCSD (coupled-cluster singles and doubles) method which retains the same singles equation as the CCSD model, but in which the doubles amplitude equation is approximated to first order in the :math:`T_2` amplitudes only. This has the major advantage that then storage of quantities that scale as :math:`N^4` with the system size either on disk or in memory can be avoided by the aid of density fitting. A corresponding density fitting implementation of CC2 has been derived by `Hättig and Weigend <https://doi.org/10.1063/1.1290013>`__ and has the advantage that ground and excited state energies and properties can be computed for systems much large in size than are possible with standard CCSD and beyond wave function methods. Note that a separate local CC2 program is also available in Molpro which further reduces the :math:`N^5` scaling of DF-CC2 to linear scaling with the aid of localisation of orbitals, see section :doc:`Local methods for excited states <local_methods_for_excited_states>`.

Bibliography:

O. Christiansen, H. Koch, and P. Jørgensen, `Chem. Phys. Lett. <https://doi.org/10.1016/0009-2614(95)00841-Q>`__ **243**, 409 (1995)

Christof Hättig and Florian Weigend, `J. Chem. Phys. <https://doi.org/10.1063/1.1290013>`__ **113**, 5154 (2000)

Christof Hättig and Andreas Köhn `J. Chem. Phys. <https://doi.org/10.1063/1.1506918>`__ **117** 6939 (2002)

To compute ground-state correlation energies using the DF-CC2 program the ``df-cc2`` command needs to be added after a Hartree-Fock calculation:

.. code-block:: text

   hf
   df-cc2

This saves the total CC2 energy in the standard variable ``ENERGY`` as usual. By default, it uses the ``MP2Fit`` auxiliary basis set which matches the corresponding orbital basis if available. It is also possible to set the ``MP2Fit`` basis set explicitly in the input file by using, e.g.

.. code-block:: text

   basis={
   set,orbital
   default,avdz
   set,mp2fit
   default,avdz/mp2fit
   }

In the corresponding basis block. See section :doc:`Density fitting <density_fitting>` for more info on how to choose the auxiliary basis set for more special cases (usually orbital basis sets other than Dunning type ones).

In order to calculate excitation energies using the DF-CC2 program the ``STATES`` option needs to be added to the ``DF-CC2`` command with a list of the required (lowest) excitations of a given symmetry, like

.. code-block:: text

   df-cc2, states=[5.1,3.4,4.6]

which will calculate :math:`5` states in symmetry :math:`1`, :math:`3` states in symmetry :math:`4` and :math:`4` states in symmetry :math:`6`, as an example. Of course, the number of states and symmetries need to be consistent with the current global settings in Molpro regarding symmetry and basis set sizes. Excitation energies are saved in the 1-rank array variable ``OMEGA``.

Transition moments can also be computed for each excited state by adding the ``TRAMOM`` option

.. code-block:: text

   df-cc2, states=[...],tramom=1

which will also automatically compute the (unrelaxed) ground state CC2 dipole moment. The latter can also be obtained using either the option ``DIPOLE``\ :math:`=1` or ``DM``\ :math:`=\langle record\rangle.\langle file \rangle` where the latter also saves the density matrix in a dump record with the corresponding name :math:`\langle record\rangle.\langle file \rangle`. Both options ``DIPOLE`` or ``DM`` do not require the calculation of excited states, of course.

The transition dipole moments are saved in the variables ``TM_L_X``, ``TM_L_Y`` and ``TM_L_Z`` for the left vector densities and ``TM_R_X``, ``TM_R_Y`` and ``TM_R_Z`` for the corresponding right vector densities, respectively. The values are ordered according to the excitations computed consecutively. The corresponding transition quadrupole moments (not traceless!) are being saved in the variables ``TMQ_L_XX``, ``TMQ_L_YY``, etc.

The following list summarises further options which can be set in the ``DF-CC2`` program in order to finetune the convergence thresholds, among other things. Note that some options are only being used in very specific parts of the program and so do not globally change anything unless the code branches out to those parts.

* **CC2_VERSION:CC2_VERS:VERSION** switch between two different CC2 program versions 1 and 2 (default '1')
* **MAXIT** maximum number of macroiterations in first iteration (default '40')
* **MAXMIC1:MAXMIC** maximum number of microiterations in first iteration (default '5')
* **MAXMIC2** maximum number of microiterations after first iteration (default '3')
* **EXTRASTATE:ADDCCS** Number of additional states in CCS (default '0')
* **MAXDIIS:MAXDIS** Max number if DIIS vectors (default '10')
* **USE_GA** If true, use GA (default '0')
* **USE_BUFFERS:USE_BUF** If true, buffer 3-index integrals in memory (default '1')
* **USE_XTRANS:XTRANS** If true, transpose X in 3-ext part (default '0')
* **MAXDAV** Maximum number of Davidson vectors per state (default '6'
* **NOPAIR** If true, omit doubles, i.e. CCS (default '0')
* **USE_DPOT** If true, use Cholesky in Davdison (default '0')
* **DO_CCS** If true, use CCS start for excited states (default '1')
* **THRDIIS:THRDIS** Energy threshold for starting DIIS (default '1d-3')
* **FACMIC** Factor of energy threshold between macroiterations (default '0.01d0')
* **STATES:STATE** Requested states
* **START** Start record
* **SAVE** Save record
* **SHIFTS:SHIFT** Denominator shift (default '0d0')
* **THRCCS** Threshold for CCs guess (default '1d-3')
* **TRIPLET** If true do triplet excitations (default '0')
* **TRIANG** If true use triangularity in pair loop (default '1')
* **DO_LEFT** Compute left eigenvectors if true (default '0')
* **DFMODE** Switch for different density fitting modes (default '0').
* **DIIS_LEFT** If true, start optimisation of left eigenvectors with DIIS, so skip Davidson (default '0')
* **TRAMOM** Compute transition moments if true (default '0')
* **DIPOL** Compute dipole moments (default '0')
* **DM** Save density matrix the the record specified (default '0.0')
* **XF_FX** Changes how the x.F+F.x amplitude contribution is computed when symmetry is being used (default '1')
* **DEGTHR:THRDEG** Threshold to test uncoupled degenerate states before excitation energy calculation (default '1d-5')
* **GA_DISK** In serial mode either use normal disk mode for GA's (set this to true) or allocate heap memory (default)
* **RESTART** Record to read/write :math:`t_1` amplitudes from/to (which can then be used to restarting a CC2 calculation at, say, a different geometry or with different settings than the previous one)

.. _the_closed-shell_density_fitting_cc2_program_for_ground_and_excited_states--computing-cc2-ground-state-densities-and-gradients:

Computing CC2 ground state densities and gradients
==================================================

To compute relaxed ground state densities the logical options ``DIPOL`` and ``RELAXED`` can be used like (true\|false cases are handled as 0\|1 cases with Molpro options):

.. code-block:: text

   df-cc2,dipol=1,relaxed=1,dm=<record.file>

where ``DM``\ =<*record.file*> can additionally be used to save the density matrix in a dump record for later usage (e.g., for computing other 1st order properties using the :doc:`properties program <properties_and_expectation_values>`. If the ``RELAXED`` variable is not given or if set to :math:`0` the program will compute the unrelaxed dipole moment instead (and the corresponding unrelaxed density matrix will then be saved by the ``DM`` option).

For computing ground state gradients the logical option ``GRAD`` can be used like:

.. code-block:: text

   df-cc2,grad=1

which will also compute the relaxed density matrix alongside (which again may be saved in a record by using ``DM``\ =<*record.file*>). Note that the ``GRAD`` option (as usual) does not need to be explicitly set if a :doc:`geometry optimisation <geometry_optimization_optg>` is being performed, that is if the ``DF-CC2`` input command is being followed by ``OPTG``

.. code-block:: text

   df-cc2
   optg

There are a few options to ``DF-CC2`` which are being used in the gradient program specifically:

* **GRAD_DFGX** Use DF (AO based) for the matrix\*vector step in the Z-Vector(CPHF) equation for the gradient (default=1).
* **MPP_OCC** Parallelise loop over occupied orbitals if :math:`N_{procs}/N_{occ}` > ``MPP_OCC`` (default=4.0).
* **PRINT_GRAD** Print different gradient contributions if set to > 0.
* **AX_MODE** Use MO based (=1) or AO based (=0) Fock matrix computation in A.x step for the Z-vector equation (only used if ``GRAD_DFGX``\ =1)
* **DENS_IJ_MODE** Switch between two different calculation modes for the occ-occ density block (default=2)
* **RELAXED** Compute relaxed dipole moment if ``DIPOL``\ =true
