.. raw:: html

   <span id="methods-available-in-the-mrcc-program"></span>

.. raw:: html

   <span id="options-for-mrcc"></span>

.. _the_mrcc_program_of_m._kallay_mrcc--the-mrcc-program-of-m-kallay-mrcc:

The MRCC program of M. Kallay (MRCC)
====================================

An interface exists to use the MRCC program of M. Kallay and J. Gauss within Molpro. The license and source code of the MRCC program must be obtained from Mihaly Kallay ``http://www.mrcc.hu/``. Currently, only single reference methods with ``RHF`` reference functions are supported. Perturbative methods and CCn methods are only available for closed-shell. Furthermore, only serial execution is supported under Molpro, i.e. the mpp version cannot be used.

.. _the_mrcc_program_of_m._kallay_mrcc--installing-mrcc:

Installing MRCC
===============

Please refer to the MRCC documentation on how to install the MRCC program. The MRCC executables must be found in PATH in order for Molpro to use them.

.. _the_mrcc_program_of_m._kallay_mrcc--running-mrcc:

Running MRCC
============

The ``MRCC`` program is invoked by the command

``MRCC,options\\``
*directives*

The available options summarized in `#options for MRCC <the_mrcc_program_of_m._kallay_mrcc.html#options-for-mrcc>`__. For a detailed description please refer to the MRCC manual of M. Kallay (file ”manual” the mrcc directory).

In Molpro the method to be used can be given as a string (option ``METHOD``\ =\ *string*). The available methods and the corresponding ``MRCC`` input parameters (see MRCC manual) as specified in `#methods available in the MRCC program <the_mrcc_program_of_m._kallay_mrcc.html#methods-available-in-the-mrcc-program>`__.

Directives are usually not necessary, but the ``CORE``, ``OCC``, ``ORBITAL``, ``MAXIT``, directives work as in the Molpro CCSD program. In addition, the number of states can be given on a ``STATE`` directive and this has the same meaning as the ``EOM_NSTATES`` option.

.. _the_mrcc_program_of_m._kallay_mrcc--options-for-mrcc:

Options for MRCC
================

.. list-table::
   :header-rows: 1

   * - Option
     - Alias
     - Default value((-1 means default value taken from Molpro))
     - Meaning
   * - ``METHOD``
     - ``CALC``
     - ``CC(n)``
     - Computational method. See `this section <the_mrcc_program_of_m._kallay_mrcc.html#methods-available-in-the-mrcc-program>`__.
   * - ``EXCITATION``
     - ``LEVEL``
     - -1
     - Excitation level in cluster operator
   * - ``RESTART_CC``
     - ``RESTART``
     - 0
     - Restart option. If 1, restart with previous amplitudes.
   * - ``DIRECTORY``
     - ``DIR``
     - ’  ’
     - Subdirectory in which MRCC runs
   * - 
     - 
     - 
     - (necessary for restart jobs)
   * - ``EOM_NSING``
     - ``NSING``
     - -1
     - Number of excited singlet states in closed-shell case
   * - ``EOM_NTRIP``
     - ``NTRIP``
     - 0
     - Number of excited triplet states in closed-shell case
   * - ``EOM_NSTATES``
     - ``NDOUB`` , ``NSTATES``
     - -1
     - Number of states in open shell case.
   * - ``SYMM``
     - ``SYMMETRY``
     - -1
     - Symmetry of excited states
   * - ``DENSITY``
     - ``IDENS``
     - 0
     - Parameter for density calculation
   * - ``HF``
     - 
     - 1
     - 1 for canonical Hartree-Fock orbitals, 0 otherwise
   * - ``SPATIAL``
     - 
     - 1
     - 0 for spin-restricted orbitals, 1 for spin-unrestricted orbitals
   * - ``NACTO``
     - 
     - 0
     - Number of active occupied orbitals
   * - ``NACTV``
     - 
     - 0
     - Number of active virtual orbitals
   * - ``SACC``
     - 
     - 0
     - Spin-adapted coupled cluster
   * - ``DBOC``
     - 
     - 0
     - Diagonal BO correction (``DBOC`` :math:`\ne 0` cannot be used with Molpro, see MRCC manual)
   * - ``MEMORY``
     - 
     - -1
     - Memory
   * - ``TOL``
     - ``ENERGY``
     - -1.0
     - Energy convergence threshold
   * - ``FREQ``
     - 
     - 0.0
     - Frequency for dynamic polarizabilities
   * - ``FILE``
     - 
     - ``fort``
     - Name for MRCC fortran files
   * - ``CONVER``
     - ``ICONV``
     - 0
     - See mrcc manual
   * - ``CS``
     - 
     - 1
     - See mrcc manual
   * - ``DIAG``
     - 
     - 0
     - See mrcc manual
   * - ``MAXEX``
     - 
     - 0
     - See mrcc manual
   * - 
     - 
     - 
     - 

.. _the_mrcc_program_of_m._kallay_mrcc--methods-available-in-the-mrcc-program:

Methods available in the MRCC program
=====================================

.. list-table::
   :header-rows: 2

   * - Key
     - MRCC parameters
     - 
     - Notes
   * - 
     - ``METHOD``
     - ``LEVEL``
     - 
   * - *CI(n) configuration interaction methods*
     - 
     - 
     - 
   * - ``CISD``
     - 0
     - 2
     - 
   * - ``CISDT``
     - 0
     - 3
     - 
   * - ``CISDTQ``
     - 0
     - 4
     - 
   * - ``CI(N)``
     - 0
     - N
     - Specify excitation level N using ``LEVEL``
   * - *CC(N) coupled cluster methods*
     - 
     - 
     - 
   * - ``CCSD``
     - 1
     - 2
     - 
   * - ``CCSDT``
     - 1
     - 3
     - 
   * - ``CCSDTQ``
     - 1
     - 4
     - 
   * - ``CC(N)``
     - 1
     - N
     - Specify excitation level N using ``LEVEL``
   * - *CC(N-1)[N] coupled cluster methods*
     - 
     - 
     - 
   * - ``CCSD[T]``
     - 2
     - 3
     - 
   * - ``CCSDT[Q]``
     - 2
     - 4
     - 
   * - ``CC(N-1)[N]``
     - 2
     - N
     - Specify excitation level N using ``LEVEL``
   * - *CC(N-1)(N) coupled cluster methods. Also computes [n] corrections*
     - 
     - 
     - 
   * - ``CCSD(T)``
     - 3
     - 3
     - 
   * - ``CCSDT(Q)``
     - 3
     - 4
     - 
   * - ``CC(N-1)(N)``
     - 3
     - N
     - Specify excitation level N using ``LEVEL``
   * - *CC(n-1)(n)_L methods (also computes (n) and [n] corrections)*
     - 
     - 
     - 
   * - ``CCSD(T)_L``
     - 4
     - 3
     - 
   * - ``CCSDT(Q)_L``
     - 4
     - 4
     - 
   * - ``CC(N-1)(N)_L``
     - 4
     - N
     - Specify excitation level N using ``LEVEL``
   * - *CC(n)-1a  methods*
     - 
     - 
     - 
   * - ``CCSDT-1A``
     - 5
     - 3
     - 
   * - ``CCSDTQ-1A``
     - 5
     - 4
     - 
   * - ``CC(N)-1A``
     - 5
     - N
     - Specify excitation level N using ``LEVEL``
   * - *CC(n)-1b  methods*
     - 
     - 
     - 
   * - ``CCSDT-1B``
     - 6
     - 3
     - 
   * - ``CCSDTQ-1B``
     - 6
     - 4
     - 
   * - ``CC(N)-1B``
     - 6
     - N
     - Specify excitation level N using ``LEVEL``
   * - *CCn methods (only for ground states)*
     - 
     - 
     - 
   * - ``CC3``
     - 7
     - 3
     - 
   * - ``CC4``
     - 7
     - 4
     - 
   * - ``CCN``
     - 7
     - N
     - Specify excitation level N using ``LEVEL``
   * - *CC(n)-3 methods*
     - 
     - 
     - 
   * - ``CCSDT-3``
     - 8
     - 3
     - 
   * - ``CCSDTQ-3``
     - 8
     - 4
     - 
   * - ``CC(N)-3``
     - 8
     - N
     - Specify excitation level N using ``LEVEL``

.. _the_mrcc_program_of_m._kallay_mrcc--examples:

Examples
========

Closed-shell ground-state calculations for H2O:

.. code-block:: text
   :caption: examples/h2o_mrcc.inp

   ***,mrcc calculations for h2o
   gthresh,energy=1.d-8
   
   geometry={
   o;h1,o,r;h2,o,r,h1,theta}
   theta=104
   r=1 ang
   basis=vdz
   
   hf
   mrcc,method=cc3;                    !CC3 calculation
   method(1)=program
   e(1)=energy                         !the final energy is returned in variable energy
   
   ccsd(t)                             !CCSD(T) calculation using Molpro
   method(2)='CCSD(T) (MOLPRO)'
   e(2)=energy
   
   mrcc,method=ccsd(t)                 !CCSD(T) calculation using MRCC
   method(3)='CCSD(T) (MRCC)'
   e(3)=energy
   
   mrcc,method=ccsdt,dir=mrccdir       !CCSDT calculation, run in directory mrccdir
   method(4)=program
   e(4)=energy
   
   mrcc,method=ccsdt(q),restart=1,dir=mrccdir !CCSDT(Q) calculation
                                              !restart with previous amplitudes
   method(5)=program
   e(5)=energy
   
   mrcc,method=CC(n),excitation=4,restart=1,dir=mrccdir !CCSDTQ calculation
   method(6)=program
   e(6)=energy
   
   table,method,e

This yields

.. code-block:: text

    METHOD                 E
    CC3                -76.23912734
    CCSD(T) (MOLPRO)   -76.23905150
    CCSD(T) (MRCC)     -76.23905150
    CCSDT              -76.23922746
    CCSDT(Q)           -76.23976632
    CCSDTQ             -76.23973043

Excitation energies for H2O:

.. code-block:: text
   :caption: examples/h2o_mrcc_eom.inp

   ***,h2o excitation energies
   gthresh,energy=1.d-8
   geometry={
   o;h1,o,r;h2,o,r,h1,theta}
   theta=104
   r=1 ang
   basis=vdz
   hf
   
   ii=0
   s=2                        !number of states in each symmetry
   do sym=1,4                 !loop over irreps
   ccsd;eom,-(s+0.1*sym);$p=molpro;save_energy
   mrcc,method=ccsd, symm=sym,nstates=2;$p=mrcc;save_energy
   mrcc,method=ccsdt,symm=sym,nstates=2;$p=mrcc;save_energy
   s=1
   enddo
   
   {table,method,prog,states,e,exc
    sort,3}
   
   save_energy={       !procedure to save results in variables
   !nogprint,variable
   e1=energy(1)
   do i=1,#energy
   ii=ii+1
   e(ii)=energy(i)
   method(ii)=program
   prog(ii)=p
   states(ii)=i+0.1*sym
   exc(ii)=(e(ii)-e1)*toev
   end do
   }

This yields

.. code-block:: text

    METHOD   PROG    STATES       E             EXC
    CCSD     MOLPRO     1.1   -76.23580212    0.000
    CCSD     MRCC       1.1   -76.23580212    0.000
    CCSDT    MRCC       1.1   -76.23922746    0.000
    CCSD     MOLPRO     1.2   -76.23580212    0.000
    CCSD     MRCC       1.2   -76.23580212    0.000
    CCSDT    MRCC       1.2   -76.23922746    0.000
    CCSD     MOLPRO     1.3   -76.23580212    0.000
    CCSD     MRCC       1.3   -76.23580212    0.000
    CCSDT    MRCC       1.3   -76.23922746    0.000
    CCSD     MOLPRO     1.4   -76.23580212    0.000
    CCSD     MRCC       1.4   -76.23580212    0.000
    CCSDT    MRCC       1.4   -76.23922746    0.000
    CCSD     MOLPRO     2.1   -75.85033256   10.489
    CCSD     MRCC       2.1   -75.85033257   10.489
    CCSDT    MRCC       2.1   -75.85316687   10.505
    CCSD     MOLPRO     2.2   -75.95093334    7.752
    CCSD     MRCC       2.2   -75.95093335    7.752
    CCSDT    MRCC       2.2   -75.95299013    7.789
    CCSD     MOLPRO     2.3   -75.77630664   12.504
    CCSD     MRCC       2.3   -75.77630665   12.504
    CCSDT    MRCC       2.3   -75.77972816   12.504
    CCSD     MOLPRO     2.4   -75.87776149    9.743
    CCSD     MRCC       2.4   -75.87776150    9.743
    CCSDT    MRCC       2.4   -75.88051189    9.761

Open-shell ground-state calculations for O2:

.. code-block:: text
   :caption: examples/o2_mrcc.inp

   ***,O2 tests
   gthresh,energy=1.d-8
   
   geometry={o1;o2,o1,r1}
   r1=2.2
   set,state=1,symmetry=4,spin=2  ! Triplet sigma- state
   basis=vdz
   
   rhf
   uccsd(t)
   method(1)='UCCSD(T) MOLPRO'
   e(1)=energy
   
   rccsd(t)
   method(2)='RCCSD(T) MOLPRO'
   e(2)=energy
   
   mrcc,method=ccsdt,dir=mrccdir
   method(3)='CCSDT MRCC'
   e(3)=energy
   
   mrcc,method=ccsdtq,restart=1,dir=mrccdir
   method(4)='CCSDT MRCC'
   e(4)=energy
   
   table,method,e

This yields

.. code-block:: text

    METHOD                 E
    UCCSD(T) MOLPRO   -149.9815472
    RCCSD(T) MOLPRO   -149.9812566
    CCSDT MRCC        -149.9816705
    CCSDT MRCC        -149.9832255
