.. raw:: html

   <span id="brueckner-coupled-cluster-calculations-bccd"></span>

.. raw:: html

   <span id="coupled-cluster-ccsd"></span>

.. raw:: html

   <span id="distinguishable-cluster-dcd"></span>

.. raw:: html

   <span id="dual-basis-set-calculations"></span>

.. raw:: html

   <span id="expectation-values"></span>

.. raw:: html

   <span id="natural-orbitals"></span>

.. raw:: html

   <span id="quadratic-configuration-interaction-qci"></span>

.. raw:: html

   <span id="quasi-variational-coupled-cluster-qvccd"></span>

.. raw:: html

   <span id="saving-the-density-matrix"></span>

.. raw:: html

   <span id="saving-the-wavefunction"></span>

.. raw:: html

   <span id="singles-doubles-configuration-interaction-cisd"></span>

.. raw:: html

   <span id="starting-wavefunction"></span>

.. raw:: html

   <span id="the-brueckner-directive"></span>

.. raw:: html

   <span id="the-diis-directive"></span>

.. _the_closed_shell_ccsd_program--the-closed-shell-ccsd-program:

The closed shell CCSD program
=============================

Bibliography:

C. Hampel, K. Peterson, and H.-J. Werner, `Chem. Phys. Lett. <https://dx.doi.org/10.1016/0009-2614(92)86093-W>`__ **190**, 1 (1992)

All publications resulting from use of this program must acknowledge the above.

The CCSD program is called by the CISD, CCSD, BCCD, or QCI directives. CID or CCD can be done as special cases using the ``NOSINGL`` directive. The code also allows to calculate Brueckner orbitals (QCI and CCSD are identical in this case). Normally, no further input is needed if the ``CCSD`` card follows the corresponding HF-SCF. Optional ``ORBITAL``, ``OCC``, ``CLOSED``, ``CORE``, ``SAVE``, ``START``, ``PRINT`` options work as described for the MRCI program in section :doc:`the MRCI program <the_mrci_program>`. The only special input directives for this code are ``BRUECKNER`` and ``DIIS``, as described below.

The following options may be specified on the command line:

* ``NOCHECK`` Ignore convergence checks.
* ``DIRECT`` Do calculation integral direct.
* ``NOSING`` Do not include singly external configurations.
* **``MAXIT=``\ *value*** Maximum number of iterations.
* **``SHIFTS=``\ *value*** Denominator shift for update of singles.
* **``SHIFTP=``\ *value*** Denominator shift for update of doubles.
* **``THRDEN=``\ *value*** Convergence threshold for the energy.
* **``THRVAR=``\ *value*** Convergence threshold for CC amplitudes. This applies to the square sum of the changes of the amplitudes.
* **``SAVE=``\ *record*** Save CCSD wavefunction to this record
* **``START=``\ *record*** Restart CCSD wavefunction from a previously written record
* **``HO=``\ *operator*** Specifies the zeroth-order Hamiltonian in closed-shell CCSD calculations with KS orbitals. ``H0=MP``: Moeller Plesset partitioning (default); the Fock matrix is computed and block diagonalised. The eigenvalues are used in the MP2 and (T) denominators. ``H0=KS``: The KS Fock matrix is used as zeroth-order Hamiltonian, and its eigenvalues are used in the denominators.
* ``KSFOCK`` Forces the use of the KS Fock operator in the subsequent calculation. This is required for double-hybrid and RPA calculations.

The convergence thresholds can also be modified using

``THRESH,ENERGY=thrden,COEFF=thrvar``

Convergence is reached if the energy change is smaller than *thrden* (default 1.d-6) *and* the square sum of the amplitude changes is smaller than *thrvar* (default (1.d-10). The ``THRESH`` card must follow the command for the method (e.g., ``CCSD``) and then overwrites the corresponding global options (see ``GTHRESH``, sec. `global Thresholds (GTHRESH) <program_control.html#global-thresholds-gthresh>`__).

The computed energies are stored in variables as explained in section `special variables <variables.html#special-variables>`__. As well as the energy, the :math:`T_1` diagnostic (T. J. Lee and P. R. Taylor, Int. J. Quant. Chem. S23 (1989) 199) and the :math:`D_1` diagnostic (C. L. Janssen and I. M. B. Nielsen, Chem. Phys. Lett. 290 (1998), 423, and T. J. Lee. Chem. Phys. Lett. 372 (2003), 362) are printed and stored for later analysis in the variables T1DIAG and D1DIAG, respectively.

For geometry optimization and computing first-order properties see section `expectation values <the_closed_shell_ccsd_program.html#expectation-values>`__.

.. _the_closed_shell_ccsd_program--coupled-cluster-ccsd:

Coupled-cluster, CCSD
=====================

The command ``CCSD`` performs a closed-shell coupled-cluster calculation. Using the ``CCSD(T)`` command, the perturbative contributions of connected triple excitations are also computed.

If the CCSD is not converged, an error exit will occur if triples are requested. This can be avoided using the ``NOCHECK`` option:

``CCSD(T),NOCHECK``

In this case the (T) correction will be computed even if the CCSD did not converge. Note: ``NOCHECK`` has no effect in geometry optimizations or frequency calculations.

For further information on triples corrections see under RCCSD.

In cases that the Hartree-Fock reference determinant does not sufficiently dominate the wavefunction, the program will stop with a message ``UNREASONABLE NORM. CALCULATION STOPPED``. This can be avoided by setting the option ``CC_NORM_MAX``\ =\ *value* on the CCSD command line. The calculation is stopped if the square norm of the wavefunction (in intermediate normalization) exceeds ``1+nval*CC_NORM_MAX``, where nval is the number of correlated valence orbitals. The default value is ``CC_NORM_MAX=0.2``.

CCSD calculations with KS orbitals are possible. Optionally, the ``H0`` option can be used to specify the zeroth-order Hamiltonian (see options above). If KS or other non-HF reference states (like the Brueckner determinant) are employed in the calculation of the triples (T) additional singles terms are computed, see J. D. Watts, J. Gauss, R. Bartlett `J. Chem. Phys. <https://doi.org/10.1063/1.464480>`__ **98**, 8718 (1993). This can be switched on/off with the option ``TRIP_FIA=1/0``. If ``TRIP_FIA=1`` the second order singles energy is computed in the triples program and if greater in magnitude than ``THR_E2SING`` the additional terms will be computed.
``THR_E2SING=1d-6`` is the default setting for this threshold, which can also be altered via giving this keyword as an option to the CCSD program.

.. _the_closed_shell_ccsd_program--quadratic-configuration-interaction-qci:

Quadratic configuration interaction, QCI
========================================

``QCI`` or ``QCISD`` performs quadratic configuration interaction, QCISD. Using the ``QCI(T)`` or ``QCISD(T)`` commands, the contributions of connected triples are also computed by perturbation theory. Normally, no further input is needed if the ``QCI`` card follows the corresponding HF-SCF. Otherwise, occupancies and orbitals can be specified as in the CI program. For modifying DIIS directives, see section `the DIIS directive <the_closed_shell_ccsd_program.html#the-diis-directive>`__.

For avoiding error exits in case of no convergence, see ``CCSD(T)``.

.. _the_closed_shell_ccsd_program--brueckner-coupled-cluster-calculations-bccd:

Brueckner coupled-cluster calculations, BCCD
============================================

``BCCD,[SAVEORB=record],[PRINT],[TYPE=,type]``

In addition, the same options as for CCSD can be used.

``BCCD`` performs a Brueckner coupled-cluster calculation and computes Brueckner orbitals. With these orbitals, the amplitudes of the singles vanish at convergence. Using the ``BCCD(T)`` command, the contributions of connected triples are also computed by perturbation theory. Normally, no further input is needed if the ``BCCD`` card follows the corresponding HF-SCF. Otherwise, occupancies and orbitals can be specified as in the CI program. ``BRUECKNER`` parameters can be modified using the ``BRUECKNER`` directive.

The Brueckner orbitals and approximate density matrix can be saved on a ``MOLPRO`` dump record using the ``SAVEORB`` option. The orbitals are printed if the ``PRINT`` option is given. ``TYPE`` can be used to specify the type of the approximate density to be computed:

* ``TYPE=REF`` Compute and store density of reference determinant only (default). This corresponds to the BOX (Brueckner orbital expectation value) method of `Chem. Phys. Lett. <https://dx.doi.org/10.1016/S0009-2614(99)01251-8>`__ **315**, 248 (1999).
* ``TYPE=TOT`` Compute and store density with contribution of pair amplitudes (linear terms). Normally, this does not seem to lead to an improvement.
* ``TYPE=ALL`` Compute and store both densities

Note: The expectation variables are stored in variables as usual. In the case that both densities are made, the variables contain two values, the first corresponding to ``REF`` and the second to ``TOT`` (e.g., DMZ(1) and DMZ(2)). If ``TYPE=REF`` or ``TYPE=TOT`` is give, only the corresponding values are stored.

For avoiding error exits in case of no convergence, see ``CCSD(T)``.

.. _the_closed_shell_ccsd_program--the-brueckner-directive:

The BRUECKNER directive
=======================

``BRUECKNER,orbbrk,ibrstr,ibrueck,brsfak;``

This directive allows the modification of options for Brueckner calculations. Normally, none of the options has to be specified, and the ``BCCD`` command can be used to perform a Brueckner CCD calculation.

* ***orbbrk*:** if nonzero, the Brueckner orbitals are saved on this record.
* ***ibrstr*:** First iteration in which orbitals are modified (default=3).
* ***ibrueck*:** Iteration increment between orbital updates (default=1).
* ***brsfak*:** Scaling factor for singles in orbital updates (default=1).

.. _the_closed_shell_ccsd_program--singles-doubles-configuration-interaction-cisd:

Singles-doubles configuration interaction, CISD
-----------------------------------------------

Performs closed-shell configuration interaction, CISD. The same results as with the CI program are obtained, but this code is somewhat faster. Normally, no further input is needed. For specifying DIIS directives, see section `the DIIS directive <the_closed_shell_ccsd_program.html#the-diis-directive>`__

.. _the_closed_shell_ccsd_program--quasi-variational-coupled-cluster-qvccd:

Quasi-variational coupled cluster, QVCCD
----------------------------------------

Performs closed-shell quasi-variational coupled cluster, QVCCD Normally the effect of single excitations needs to be included through orbital optimisation, and this can be done either through the Brueckner condition (``BQVCCD``), or through variational minimisation of the energy functional with respect to orbital rotations (``OQVCCD``).

J. B. Robinson and P. J. Knowles, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3680560>`__ **136**, 054114 (2012)

The effects of triple excitations can be included using the standard perturbation theory, ``OQVCCD(T)``. The renormalised, ``OQVCCDR(T)``, and asymmetric renormalised, ``OQVCCDAR(T)``, methods can also be used to include the effects of the triples, while avoiding the overcorrection of the standard triples correction due to small energy differences appearing in the denominator.

J. B. Robinson and P. J. Knowles, `Phys. Chem. Chem. Phys. <https://dx.doi.org/10.1039/C2CP40698E>`__ **14**, 6729-6732 (2012)

J. B. Robinson and P. J. Knowles, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.4791636>`__ **138**, 074104 (2013)

J. A. Black and P. J. Knowles, `Mol. Phys. <https://dx.doi.org/10.1080/00268976.2017.1400698>`__ **116**, 1421-1427 (2018)

.. _the_closed_shell_ccsd_program--distinguishable-cluster-dcd:

Distinguishable cluster, DCD
----------------------------

``DCSD``, ``BDCD``, or ``ODCD`` perform closed-shell distinguishable cluster calculations with singles, Brueckner orbitals, or optimized orbitals, respectively. All CCSD and BCCD options (:doc:`the closed shell CCSD program <the_closed_shell_ccsd_program>`) can also be used for distinguishable cluster calculations. The analytical gradients (`analytical energy gradients <energy_gradients.html#analytical-energy-gradients>`__), explicit correlation (:doc:`explicitly correlated methods <explicitly_correlated_methods>`), open-shell versions (:doc:`open-shell coupled cluster theories <open-shell_coupled_cluster_theories>`), and a linear-scaling implementation (:doc:`PAO-based local correlation treatments <pao-based_local_correlation_treatments>`) are all available for the DCSD method. All reported calculations using this feature should cite:

D. Kats and F. R. Manby, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.4813481>`__ **139**, 021102 (2013)

D. Kats, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.4892792>`__ **141**, 061101 (2014)

D. Kats, `Mol. Phys. <https://dx.doi.org/10.1080/00268976.2017.1417646>`__ **116**, 1435 (2018) (for Spin-Component Scaled DC)

.. _the_closed_shell_ccsd_program--the-diis-directive:

The DIIS directive
------------------

[sec:ccdiis]

``DIIS,itedis,incdis,maxdis,itydis;``

This directive allows to modify the DIIS parameters for CCSD, QCISD, or BCCD calculations.

* ***itedis*:** First iteration in which DIIS extrapolation may be performed (default=2).
* ***incdis*:** Increment between DIIS iterations (default=1).
* ***maxdis*:** Maximum number of expansion vectors to be used (default=6).
* ***itydis*:** DIIS extrapolation type. itydis=1 (default): residual is minimized. itydis=2: :math:`\Delta T` is minimized.

In addition, there is a threshold *THRDIS* which may be modified with the ``THRESH`` directive. DIIS extrapolation is only done if the variance is smaller than *THRDIS*.

.. _the_closed_shell_ccsd_program--saving-the-wavefunction:

Saving the wavefunction
-----------------------

``SAVE,record;``

* ***record*:** record name for save of wavefunction. The wavefunction is saved in each iteration. This has the same effect as the ``SAVE`` option.

.. _the_closed_shell_ccsd_program--starting-wavefunction:

Starting wavefunction
---------------------

``START,record;``

* ***record*:** record name from which the wavefunction is restored for a restart. This has the same effect as the ``START`` option. If the option ``MAXIT=1`` is set on the CCSD command line, no further iterations will be performed. (Note: in this case there is no check whether the previous wavefunction was converged.) It is then for example possible to compute the triples correction using the restarted CCSD wavefunction.

.. _the_closed_shell_ccsd_program--examples:

Examples
--------

.. _the_closed_shell_ccsd_program--single-reference-correlation-treatments-for-h2o:

Single-reference correlation treatments for H2O
===============================================

.. code-block:: text
   :caption: examples/h2o_ccsd.inp

   ***,h2o test
   geometry={o;h1,o,r;h2,o,r,h1,theta}   !Z-matrix geometry input
   basis=vtz                             !cc-pVTZ basis set
   r=1 ang                               !bond length
   theta=104                             !bond angle
   hf                                    !do scf calculation
   
   text,examples for single-reference correlation treatments
   
   ci                                    !CISD using MRCI code
   cepa(1)                               !cepa-1 using MRCI code
   mp2                                   !Second-order Moeller-Plesset
   mp3                                   !Second and third-order MP
   mp4                                   !Second, third, and fourth-order MP4(SDTQ)
   mp4;notripl                           !MP4(SDQ)
   cisd                                  !CISD using special closed-shell code
   ccsd(t)                               !coupled-cluster CCSD(T)
   qci(t)                                !quadratic configuration interaction QCISD(T)
   bccd(t)                               !Brueckner CCD(T) calculation
   ---

.. _the_closed_shell_ccsd_program--single-reference-correlation-treatments-for-n2f2:

Single-reference correlation treatments for N2F2
================================================

.. code-block:: text
   :caption: examples/n2f2_ccsd.inp

   ***,N2F2 CIS GEOMETRY (C2h)
   rnn=1.223,ang                         !define N-N distance
   rnf=1.398,ang                         !define N-F distance
   alpha=114.5;                          !define FNN angle
   geometry={N1
             N2,N1,rnn
             F1,N1,rnf,N2,alpha
             F2,N2,rnf,N1,alpha,F1,180}
   basis=vtz                             !cc-pVTZ basis set
   $method=[hf,cisd,ccsd(t),qcisd(t),bccd(t)]  !all methods to use
   do i=1,#method                        !loop over requested methods
   $method(i)                            !perform calculation for given methods
   e(i)=energy                           !save energy in variable e
   enddo                                 !end loop over methods
   table,method,e                        !print a table with results
   title,Results for n2f2, basis=$basis  !title of table

This calculation produces the following table:

.. code-block:: text

    Results for n2f2, basis=VTZ
   
    METHOD          E            E-ESCF
    CISD       -308.4634948   -0.78283137
    BCCD(T)    -308.6251173   -0.94445391
    CCSD(T)    -308.6257931   -0.94512967
    QCISD(T)   -308.6274755   -0.94681207

.. _the_closed_shell_ccsd_program--expectation-values:

Expectation values
------------------

``EXPEC[,[METHOD=]method][,[TYPE=]type][,opname]``

One-electron properties in closed-shell QCISD, QCISD(T), CCD, CCSD, CCSD(T), and DCSD can be computed by using ``EXPEC``. (the ``GEXPEC`` directive has no effect in this case). The following options can be specified

* **``METHOD``:** *method*\ =\ ``EDERIV``: Default case. Properties are obtained as analytical energy derivatives.

*method*\ =\ ``XCCSD``: expectation-value CCSD method (with the exponential ansatz used also for bra) – see section `First- and second-order properties for CCSD from expectation-value CC theory (XCCSD) <excited_states_with_equation-of-motion_ccsd_eom-ccsd.html#first-and-second-order-properties-for-ccsd-from-expectation-value-cc-theory-xccsd>`__.
*method*\ =\ ``XCCSD(3)``: A simplified version of XCCSD – see section `First- and second-order properties for CCSD from expectation-value CC theory (XCCSD) <excited_states_with_equation-of-motion_ccsd_eom-ccsd.html#first-and-second-order-properties-for-ccsd-from-expectation-value-cc-theory-xccsd>`__. It is also available for the local CCSD method.

* **``TYPE``:** *type*\ =\ ``RELAX``: Compute fully relaxed properties with taking into account the orbital relaxation (default). Nonrelaxed properties are also computed and printed.

*type*\ =\ ``NORELAX``: Compute properties without taking into account the orbital relaxation. The ``TYPE`` option has only effect for the analytical energy derivatives.

Note that, in CCSD, the orbital relaxation effect on properties is less pronounced than, for example, in MP2. By default, only dipole moments are computed. The syntax for operators *opname* is explained in section `One-electron operators and expectation values (GEXPEC) <program_control.html#one-electron-operators-and-expectation-values-gexpec>`__. See also ``DM`` in section `saving the density matrix <the_closed_shell_ccsd_program.html#saving-the-density-matrix>`__, and ``NATORB`` in section `natural orbitals <the_closed_shell_ccsd_program.html#natural-orbitals>`__.

.. _the_closed_shell_ccsd_program--saving-the-density-matrix:

Saving the density matrix
-------------------------

``DM,record.ifil;``

The first-order density matrix in AO basis is stored in record *record* on file *ifil*. For details, see section `saving the density matrix <moller_plesset_perturbation_theory.html#saving-the-density-matrix>`__. See also ``NATORB`` in section `natural orbitals <the_closed_shell_ccsd_program.html#natural-orbitals>`__.

.. _the_closed_shell_ccsd_program--natural-orbitals:

Natural orbitals
----------------

``NATORB,[RECORD=]record.ifil,[PRINT=nprint],[CORE[=natcor]];``

Calculate natural orbitals. The options are the same as for MP2. For details, see section `natural orbitals <moller_plesset_perturbation_theory.html#natural-orbitals>`__.

.. _the_closed_shell_ccsd_program--dual-basis-set-calculations:

Dual basis set calculations
---------------------------

Dual basis set calculations are possible with the closed-shell MP2 and CCSD codes (conventional and local, also with density fitting where available). Normally this means that the Hartree-Fock calculation is done with a smaller basis set than the correlation calculation. In MOLPRO, two possibilities exist: the recommended one is to perform the HF and MP2 or CCSD calculations using the same basis set, and only omit higher angular momentum functions in the HF. This means that the resulting HF orbitals can be used directly in the correlation calculation. Alternatively, one can use entirely different basis sets in HF and the correlation calculation; in this case the orbitals in the correlation calculation are determined by a least square fit to the HF orbitals. This is less efficient (in particular in fully direct calculations) and somewhat less accurate. In any case, a new Fock matrix is computed in the MP2/CCSD program and block diagonalized in the occupied and virtual orbital subspaces. A perturbative singles correction is applied in the MP2 in order to reduce the HF basis set error.

Typically, the input is as follows:

.. code-block:: text

    basis=vtz(d/p)   !triple zeta basis set without f on heavy atoms and without d on hydrogen
    hf               !Hartree-Fock in the small basis
    basis=vtz        !full cc-pVTZ basis set to be used in ccsd
    ccsd(t),dual=1   !ccsd calculation

The option ``dual=1`` is required, otherwise the program will stop with an error message saying that the basis set of the reference orbitals is inconsistent. This is a precaution in order to avoid unexpected results.

Similarly, this works for other closed-shell single reference methods such as ``MP2, QCISD, MP2-F12, CCSD-F12``, and for the local variants ``LMP2, LQCISD, LCCSD`` in either conventional or direct mode. Furthermore, dual basis set ``DF-LMP2, DF-LCCSD, DF-LMP2-F12`` calculations are possible.
