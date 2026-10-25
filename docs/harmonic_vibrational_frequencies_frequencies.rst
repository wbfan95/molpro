.. raw:: html

   <span id="numerical-hessian-using-energy-variables-variable"></span>

.. raw:: html

   <span id="thermodynamical-properties-thermo"></span>

.. _harmonic_vibrational_frequencies_frequencies--harmonic-vibrational-frequencies-frequencies:

Harmonic vibrational frequencies (FREQUENCIES)
==============================================

``FREQUENCIES,options, [forces:frequencies]``

Calculate harmonic vibrational frequencies and normal modes. For the calculation of anharmonic vibrational frequencies see sections `POTENTIAL ENERGY SURFACES (SURF) <pes_generators.html#potential-energy-surfaces-surf>`__ to :doc:`vibration correlation programs <vibration_correlation_programs>`. The hessian is calculated analytically or numerically by finite differences in 3N cartesian coordinates (Z-Matrix coordinates will be destroyed on entry). If analytic gradients are available these are differentiated once to build the hessian, otherwise the energy is differentiated twice. If for the wavefunction method dipole moments are available, the dipole derivatives and the IR intensities are also calculated. Note that numerical hessians cannot be computed when dummy atoms holding basis functions are present. To get reasonable results it is necessary to do a geometry optimization before using the frequency calculation.

The ``FREQUENCIES`` command must be given after the energy calculation to which it refers or after ``OPTG``. If the command for the energy calculation (e.g. ``HF``, ``KS``, ``MP2``, etc.) is in a procedure, the ``OPTG`` and ``FREQUENCIES`` commands must also be in the procedure. Furthermore, no procedures without an energy calculation must directly precede ``FREQUENCIES`` or ``OPTG``.

.. _harmonic_vibrational_frequencies_frequencies--options:

Options
=======

The following *options* are available:

* ``ANALYTICAL`` Use analytical second derivatives of the energy. At present, analytical second derivatives are only possible for closed shell Hartree-Fock (HF) and MCSCF wavefunctions without symmetry. It is not yet possible to calculate IR-intensities analytically. Note that, due to technical reasons, the analytical MCSCF second derivatives have to be computed in the MCSCF-program using e.g. ``multi; cpmcscf,hess`` (see ``MULTI``) before they can be used in ``FREQUENCIES``. If analytical MCSCF second derivatives have been computed using ``multi; cpmcscf,hess``, ``FREQUENCIES`` will use them by default.
* ``CENTRAL`` Use central differences/high quality force constants (default).
* ``NUMERICAL`` Differentiate the energy twice, using central differences.
* ``FORWARD`` Use forward differences/low quality force constants (only effective if gradients are available).
* **``SYMM``\ =\ ``AUTO|NO``** During the numerical calculation of the hessian, the symmetry of the molecule may be lowered. Giving ``SYMM``\ =\ ``AUTO`` the program uses the maximum possible symmetry of the molecular wavefunction in each energy/gradient calculation, and this option therefore minimizes the computational effort. With ``SYMM``\ =\ ``NO`` no symmetry is used during the frequency calculation (default). For single reference calculations like HF, MP2, CCSD, RCCSD the ``AUTO`` option can be safely used and is recommended. However, the ``AUTO`` option cannot be used for multireference methods (MCSCF/MRCI/ACPF/AQCC/RS2). If given, the option is disabled in these cases. For these methods frequency calculations are only possible without symmetry. Symmetry is turned off automatically if the state symmetry is 1. Note that this may fail if there are lower states in other symmetries. Use of ``RESTRICT``, ``SELECT``, ``REF``, ``PROJECT``, ``LOCAL``, state-averaged MCSCF will lead on errors unless the calculation is performed in :math:`C_1` symmetry In such cases the whole calculation must be done without symmetry.
* ``AUTO`` Same as ``SYMM=AUTO``, see above.
* ``NOAUTO|NOSYM`` Same as ``SYMM=NO``, see above.
* **``HESSREC|SAVE``\ =\ *record*** Save hessian to *record*. By default the hessian is saved on record 5300.2.
* **``FREQREC``\ =\ *record*** Save frequencies and normal modes to *record* (default 5400.2) This information is used, e.g., by the VSCF/VCI program.
* **``TASKREC``\ =\ *record*** Save task information in numerical hessian calculation to the given record. This information is required for a restart of a numerical hessian calculation. By default, the information is saved on record 5500.2.
* **``READH|START``\ =\ *record*** Use hessian from previously saved on *record*. If the hessian has been computed for the current method and geometry already, it is used by default.
* **``READF``\ =\ *record*** Read frequencies and normal modes from previously saved on *record*..
* ``RESTART`` Attempt to restart a previous numerical frequency/hessian calculation using default task record.
* **``RESTART``\ =\ *record*** Attempt to restart a previous numerical frequency/hessian calculation using task record *record*.
* **``LOW``\ =\ *value*** Threshold for printing low frequencies in cm\ :math:`^{-1}`. If this option is given, frequencies below the given value are not printed. By default, all frequencies are printed.
* **``STEP``\ =\ *value*** Determines the step size of the numerical differentiation of the energy or the gradient. The default step size is 0.01 a.u.
* **``MAXTASK``\ =\ *value*** Stop the calculation if the number of tasks is exceeded (the calculation can be restarted later).
* **``MAXCPU``\ =\ *value*** Stop the calculation if the given CPU-time (in sec) exceeded (the calculation can be restarted later). Only possible in serial mode, and not for analytically computed frequencies.
* ``NEW`` Recompute hessian, even if a hessian is already available.
* ``PROJECT`` Project rotations and translations out of the hessian (default).
* ``NOPROJECT`` Don’t project rotations and translations out of the hessian.
* **``PRINT``\ =\ *value*** Print option. If *value* is greater or equal to zero, the hessian and other information is printed (default :math:`-1`).
* ``DEBUG`` Print Debug information, same as ``PRINT=1``.
* **``SCALE``\ =\ *value*** Scaling factor for frequencies. The scaled frequencies are used to compute the ZPE and thermodynamic properties.
* **``STARTCMD``\ =\ *command*** Specifies a start command. In each frequency calculation step, all input beginning with command to the current FREQ or HESSIAN command is processed.

For compatibility with older MOLPRO versions many of the options can also be set using directives, as described in the following sections.

.. _harmonic_vibrational_frequencies_frequencies--printing-options-print:

Printing options (PRINT)
========================

``PRINT,options``

This directive can be used to control the output:

The following *options* can be given:

* ``HESSIAN`` Print the force constant matrix (hessian) i.e. the second derivative matrix of the energy and the mass weighted hessian matrix.
* ``LOW`` Print low vibrational frequencies (i.e. the 5 or 6 frequencies belonging to rotations and translations) and their normal modes (default; ``LOW=-1`` suppresses the print).
* **``LOW``\ =\ *value*** Threshold for printing low vibrations in cm\ :math:`^{-1}` (default 150). If a value :math:`>0` is given, frequencies below this value are not printed.

.. _harmonic_vibrational_frequencies_frequencies--saving-the-hessian-and-other-information-save:

Saving the hessian and other information (SAVE)
===============================================

``SAVE,options``

The following *options* can be given:

* **``hessian=``\ *record*** Save hessian to *record* (same effect as option ``HESSREC``). By default the hessian is saved on record 5300.2.
* **``FREQ=``\ *record*** Save frequencies and normal modes to *record* (same effect as option ``FREQREC``). By default the frequencies are saved on record 5400.2.
* **``TASK=``\ *record*** Save task information for possible restart of hessian calculation to *record* (same effect as option ``TASKREC``). By default the frequencies are saved on record 5500.2.

.. _harmonic_vibrational_frequencies_frequencies--restarting-a-hessian-frequency-calculation-start:

Restarting a hessian/Frequency calculation (START)
==================================================

``START,options``

The following options can be given:

* **``HESSIAN=``\ *record*** Read hessian from record *record* (same effect as option ``READHESS``).
* **``TASK=``\ *record*** Read task information from record *record* and restart numerical hessian calculation (same effect as option ``RESTART``).

.. _harmonic_vibrational_frequencies_frequencies--coordinates-for-numerical-hessian-calculations-coord:

Coordinates for numerical hessian calculations (COORD)
======================================================

``COORD,type``

*type* can be one of the following:

* ``UNIQUE`` Use symmetry-unique displacements in the numerical calculation of the hessian (default).
* ``3N`` Don’t use symmetry-unique displacements (not recommended).

.. _harmonic_vibrational_frequencies_frequencies--stepsizes-for-numerical-hessian-calculations-step:

Stepsizes for numerical hessian calculations (STEP)
===================================================

``[STEP,rstep]``

determines the step size of the numerical differentiation of the energy or the gradient. The default step size is *rstep*\ =0.01 a.u.

.. _harmonic_vibrational_frequencies_frequencies--numerical-hessian-using-energy-variables-variable:

Numerical hessian using energy variables (VARIABLE)
===================================================

``VARIABLE,name; [freq:var]``

Defines a variable *name* which holds the energy value to be used for computing the hessian using finite differences. By default, this is ``ENERGY(1)`` as set by the most recent program. For other variables which can be used see section `optimizing energy variables (VARIABLE) <geometry_optimization_optg.html#optimizing-energy-variables-variable>`__. Note that numerical hessians cannot be computed when dummy atoms holding basis functions are present.

.. _harmonic_vibrational_frequencies_frequencies--thermodynamical-properties-thermo:

Thermodynamical properties (THERMO)
===================================

It is also possible to calculate the thermodynamical properties of the molecule. Since Molpro can only handle Abelian point groups it is necessary to give the point group of the molecule in the input file:

``THERMO,[SYM=pointgroup],[TEMP=value], [PRESS=value], [TMIN=value, TMAX=value, TSTEP=value]``

*pointgroup* has to be the Schoenflies Symbol (e.g. ``C3v`` for ammonia; linear molecules have to be ``C*v`` or ``D*h`` respectively). If no point group is given, the point group is determined automatically, but only Abelian groups (D2H and subgroups) are recognized. If the molecule has higher symmetry this may eventually cause deviations in the rotational entropy.

The temperature (in K), pressure (in atm) or a range of temperatures (in K) can be given as options.

If no temperature or pressure is specified the zero-point vibrational energy and the enthalpy :math:`H(T)-H(0)` [kJ/mol], heat capacity :math:`C_v` [J/mol K] and entropy :math:`S` [J/mol K] are calculated for standard temperature and pressure (:math:`T=298.150` [K], :math:`p=1` [atm]).

The ``FREQUENCIES`` program sets the variable ``ZPE`` containing the zero-point-energy of the harmonic vibrations in atomic units. If the ``THERMO`` option is used, the variables ``HTOTAL`` and ``GTOTAL``, containing the enthalpy and the free enthalpy of the system in atomic units, are also set.

.. _harmonic_vibrational_frequencies_frequencies--examples:

Examples
========

.. code-block:: text
   :caption: examples/form_freq.inp

   ***,formaldehyde frequency calculation
   
   basis=vdz
   gthresh,energy=1.d-8
   
   geomtyp=xyz
   symmetry,nosym
   geometry={
      4
   FORMALDEHYDE
   C          0.0000000000        0.0000000000       -0.5265526741
   O          0.0000000000        0.0000000000        0.6555124750
   H          0.0000000000       -0.9325664988       -1.1133424527
   H          0.0000000000        0.9325664988       -1.1133424527
   }
   
   hf;accu,14
   optg;coord,3n;
   
   {frequencies,analytic
   thermo,sym=c2v
   print,thermo}
   
   mp2
   optg;coord,3n
   {frequencies
   thermo,sym=c2v
   print,thermo}

.. code-block:: text
   :caption: examples/pf5_freq.inp

   ***, Phosphorous-pentafluoride Vibrational Frequencies
   basis=3-21G
   
   geomtyp=xyz        ! use cartesian coordinates xmol style
   symmetry,nosym     ! don't use symmetry
   geometry={         ! geometry input
   6
     PF5
     P        0.00000        0.00000        0.00000
     F        0.00000        1.11100       -1.12400
     F        0.00000       -1.52800       -0.40100
     F        0.00000        0.41700        1.52500
     F       -1.60400        0.00000        0.00000
     F        1.60400        0.00000        0.00000}
   
   rhf
   optg              ! optimize geometry
   
   frequencies       ! calculate vibrational frequencies
   print,low         ! print frequencies+modes of zero frequencies
   thermo,sym=d3h    ! calculate thermodynamical properties
   temp,200,400,50   ! temperature range 200 - 400 [K]
   ---

.. code-block:: text
   :caption: examples/h2o_freqdft.inp

   include procedures
   geometry={O;                 !Z-matrix for water
             H1,O,R;
             H2,O,R,H1,THETA}
   R=0.96 Ang                   !start bond distance
   Theta=104                    !start bond angle
   basis=6-31g**                !Pople basis set
   $functional=b3lyp            !define functional (optional, b3lyp is default)
   freqdft                      !run frequency calculation

.. code-block:: text
   :caption: examples/diboran_freq.inp

   ***, Diboran Z-Matrix
   gthresh,energy=1.d-10,thrgrad=1.d-10
   basis=sto-3g
   r1=0.9023299 ang
   r2=0.9722889 ang
   r3=1.1540618 ang
   a1=118.723 degree
   
   
   geometry={
             X1
             B1,X1,r1
             H1,X1,r2,B1,90
             B2,X1,r1,H1,90,B1,180
             H2,X1,r2,B1,90,H1,180
             H3,B1,r3,X1,a1,H1,90
             H4,B1,r3,X1,a1,H1,-90
             H5,B2,r3,X1,a1,H1,90
             H6,B2,r3,X1,a1,H1,-90}
   
   
   hf
   optg,gradient=1.d-4
   
   {frequencies,coord=nosym
   thermo,sym=d2h
   print,thermo}
   
   {frequencies,coord=sym,new
   thermo,sym=d2h
   print,thermo}
