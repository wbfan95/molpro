.. raw:: html

   <span id="calculate-an-eom-ccsd-state-most-similar-to-a-given-cis-state"></span>

.. raw:: html

   <span id="eom-ccsd-transition-moments-for-hydrogen-fluoride"></span>

.. raw:: html

   <span id="excited-states-with-cis"></span>

.. raw:: html

   <span id="first-and-second-order-properties-for-ccsd-from-expectation-value-cc-theory-xccsd"></span>

.. raw:: html

   <span id="options-for-eom"></span>

.. raw:: html

   <span id="options-for-eompar-card"></span>

.. raw:: html

   <span id="options-for-eomprint-card"></span>

.. raw:: html

   <span id="pes-for-lowest-excited-states-for-hydrogen-fluoride"></span>

.. _excited_states_with_equation-of-motion_ccsd_eom-ccsd--excited-states-with-equation-of-motion-ccsd-eom-ccsd:

Excited states with equation-of-motion CCSD (EOM-CCSD)
======================================================

Excitation energies for singlet states can be computed using equation-of-motion (<nowiki>EOM</nowiki>) approach. For the excitation energies the <nowiki>EOM</nowiki>-CCSD method gives the same results as linear response CCSD (LR-CCSD) theory. Accurate results can only be expected for excited states dominated by single excitations. The states to be computed are specified on an ``<nowiki>EOM</nowiki>`` input card, which is a subcommand of ``CCSD``. The following input forms are possible

``<nowiki>EOM</nowiki>, state1, state2, state3, …``

Computes the given states. Each state is specified in the form *number.sym*, e.g., 5.3 means the fifth state in symmetry 3. Note that state 1.1 corresponds to the ground state CCSD wavefunction and is ignored if given.

``<nowiki>EOM</nowiki>, $-n1.sym1$, $-n2,sym2$, …``

computes the first :math:`n1` states in symmetry *sym1*, :math:`n2` in *sym2* etc.

``<nowiki>EOM</nowiki>, $n1.sym1$, $-n2,sym1$, …``

computes states :math:`n1` through :math:`n2` in symmetry *sym1*.

The different forms can be combined, e.g.,

``<nowiki>EOM</nowiki>, $-3.1$, $2.2$, $2.3$, $-5.3$``

computes states 1-3 in symmetry 1, the second excited state in symmetry 2, and the second through fifth excited states in symmetry 3. Note that state 1.1 is the ground-state CCSD wavefunction.

By default, an error exit will result if the CCSD did not converge and a subsequent <nowiki>EOM</nowiki> calculation is attempted. The error exit can be avoided using the ``NOCHECK`` option on the CCSD command (see also CCSD(T)).

.. _excited_states_with_equation-of-motion_ccsd_eom-ccsd--options-for-eom:

Options for EOM
===============

Normally, no further input is needed for the calculation of excitation energies.

EOM-CCSD amplitudes can be saved using ``SAVE=``\ *record.ifil*. The vectors will be saved after every refreshing of the iteration space and at the end of the calculation. The calculation can be restarted from the saved vectors, if ``START=``\ *record.ifil* is specified. The set of vectors to be computed can be different in old and restarted calculations. However, if both cards (``SAVE`` and ``START``) are specified and the records for saving and restarting are identical, the sets of vectors should be also identical, otherwise chaos. The identical ``SAVE`` and ``START`` records can be useful for potential energy surfaces calculations, see section `PES for lowest excited states for hydrogen fluoride <excited_states_with_equation-of-motion_ccsd_eom-ccsd.html#pes-for-lowest-excited-states-for-hydrogen-fluoride>`__.

By default, only excitation energies are calculated, since the calculation of properties is about two times as expensive, as the calculation of energies only. The one-electron properties and transition moments (expectation type, as defined in: J.F. Stanton and R.J. Bartlett, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.464746>`__ **98**, 7029 (1993)) can be calculated by adding ``TRANS=1`` to ``EOM`` card. The CCSD ground state is treated as a special case. If ``RELAX`` option is specified on the ``EXPEC`` card, also the relaxed one-electron density matrix is calculated for the ground state. (Currently, the relaxed CCSD density matrix through the EOM program is available for all-electron calculations only.) By default, dipole moments are calculated. Other required properties can be specified using ``EXPEC`` card. Properties are saved in ``MOLPRO`` variables, e.g. the :math:`x`-component of the dipole moment is saved in ``DMX``, its pure electron part in ``DMXE``, transition moment – in ``TRDMX`` (left and right transition moments are stored separately). If ``DENSAVE=``\ *record.ifil* is specified, excited-state densities are saved to *record.ifil*, otherwise they are saved to the record given in ``DM`` card. If ``TRANS=2``, transition density matrices from/to the ground state will be saved provided that ``DENSAVE=``\ *record.ifil* or ``DM`` card are specified and nonzero. If ``TRANS=3``, transition moments among excited states are also calculated, and finally if ``TRANS=4``, all transition densities will be saved (note that the last option should be used with caution because the number of densities to be stored will quickly exceed the allowed maximum). For an example see section `EOM-CCSD transition moments for hydrogen fluoride <excited_states_with_equation-of-motion_ccsd_eom-ccsd.html#eom-ccsd-transition-moments-for-hydrogen-fluoride>`__.

When properties are needed, the left EOM-CCSD wave functions are calculated first. It is possible to use them as starting guesses for the right EOM-CCSD wave functions. This option is controlled by ``STARTLE`` (default 0). If ``STARTLE``\ =1, left vectors are just used as a start for right vectors; if ``STARTLE``\ =2, starting vectors, obtained from the left vectors are additionally biorthogonalized to the left vectors; finally, if ``STARTLE``\ =3, also the final right vectors are biorthogonalized to the left vectors. The last possibility is of particular importance for degenerate states.

It is possible to make the program to converge to a vector, which resembles a specified singles vector. This option is switched on by ``FOLLOW``\ =\ :math:`n` card (usually :math:`n`\ =2 should be set). ``FOLLOW`` card should be always accompanied with ``EXFILE=``\ *record.ifil* card, where *record.ifil* contains singles vectors from a previous calculation, see section `calculate an EOM-CCSD state most similar to a given CIS state <excited_states_with_equation-of-motion_ccsd_eom-ccsd.html#calculate-an-eom-ccsd-state-most-similar-to-a-given-cis-state>`__.

.. _excited_states_with_equation-of-motion_ccsd_eom-ccsd--options-for-eompar-card:

Options for EOMPAR card
=======================

Normally, no further input is needed. However, some defaults can be changed using the ``EOMPAR`` directive:

``EOMPAR, key1=value1, key2=value2,…``

where the following keywords ``key`` are possible:

* **``MAXDAV``\ =\ *nv*** Maximum value of expansion vectors per state in Davidson procedure (default 20).
* **``INISINGL``\ =\ *ns*** Number of singly excited configurations to be included in initial Hamiltonian (default 20; the configurations are ordered according to their energy). Sometimes ``INISINGL`` should be put to zero in order to catch states dominated by double excitations.
* **``INIDOUBL``\ =\ *nd*** Number of doubly excited configurations to be included in initial Hamiltonian (default 10).
* **``INIMAX``\ =\ *nmax*** Maximum number of excited configurations to be included in initial Hamiltonian. By default, :math:`nmax=ns+nd`.
* **``MAXITER``\ =\ *itmax*** Maximum number of iterations in EOM-CCSD (default 50).
* **``MAXEXTRA``\ =\ *maxex*** Maximum number of extra configurations allowed to be included in initial Hamiltonian (default 0). In the case of near degeneracy it is better to include a few extra configurations to avoid a slow convergence.
* **``EOMLOCAL``\ =\ *eoml*** If set to 0, non-local calculation (default). ``EOMLOCAL``\ =1 switches on the local module (experimental!).
* **``INIMAX``\ =\ *ini*** Number of CSFs included in initial Hamiltonian, used only if ``INISINGL`` and ``INIDOUBL`` are both zero.

All keywords can be abbreviated by at least four characters.

.. _excited_states_with_equation-of-motion_ccsd_eom-ccsd--options-for-eomprint-card:

Options for EOMPRINT card
=========================

The following print options are mostly for testing purposes and for looking for the convergence problems.

``EOMPRINT, key1=value1, key2=value2,…``

where the following keywords ``key`` are possible:

* **``DAVIDSON``\ =\ *ipr*** Information about Davidson procedure:

*ipr=1* print results of each "small diagonalization"
*ipr=2* also print warning information about complex eigenvalues
*ipr=3* also print hamiltonian and overlap matrix in trial space.

* **``DIAGONAL``\ =\ *ipr*** Information about configurations:

*ipr=1* print the lowest approximate diagonal elements of the transformed hamiltonian
*ipr=2* print orbital labels of important configurations
*ipr=3* print all approximate diagonal elements
*ipr=4* also print the long form of above.

* **``PSPACE``\ =\ *ipr*** Print information about the initial approximate hamiltonian:

*ipr=2* print the approximate hamiltonian used to find the first approximation.

* **``HEFF``\ =\ *ipr*** Print information about effective Hamiltonian:

*ipr=2* print columns of effective hamiltonian and overlap matrix in each iteration

* **``RESIDUUM``\ =\ *ipr*** Print information about residual vectors:

*ipr=-1* no print in iteration
*ipr=0* print energy values + residuum norm (squared) for each iteration (default)
*ipr=1* also print warning about complex eigenvalue, and a warning when no new vectors is added to the trial space due to the too small norm of the residuum vector.
*ipr=2* also print how many vectors are left

* **``LOCEOM``\ =\ *ipr*** *ipr=1* prints overlaps of sample and tested vectors in each iteration, if ``FOLLOW`` card is present. Increasing *ipr* switches on more and more printing, mostly related to the local EOM-CCSD method.
* **``POPUL``\ =\ *ipr*** if *ipr=1*, do a population analysis of the singles part of the rhs EOM-CCSD wave function. By default the Löwdin method is used. The Mulliken analysis can be forced by adding ``MULLPRINT=1`` to ``EOM`` card. Note that a more correct (but more expensive) approach is to calculate and analyse the EOM-CCSD density matrix, see section `options for EOM <excited_states_with_equation-of-motion_ccsd_eom-ccsd.html#options-for-eom>`__.
* **``INTERMED``\ =\ *ipr*** Print intermediates dependent on ground state CCSD amplitudes:

*ipr=0* no print (default)
*ipr=1* print newly created intermediates
*ipr=2* also print more intermediates-related information

.. _excited_states_with_equation-of-motion_ccsd_eom-ccsd--examples:

Examples
========

.. _excited_states_with_equation-of-motion_ccsd_eom-ccsd--pes-for-lowest-excited-states-for-hydrogen-fluoride:

PES for lowest excited states for hydrogen fluoride
===================================================

This example shows how to calculate potential energy surfaces for several excited states using restart from a previous calculation.

.. code-block:: text
   :caption: examples/hf_eom_pes.inp

   ***, PES for several lowest states of hydrogen fluoride
   basis=avdz                                       ! define basis set
   geometry={h;f,h,r}                               ! z-matrix
   r=0.8 Ang                                        ! start from this distance
   do n=1,100                                       ! loop over distances
   rr(n)=r                                          ! save distance for table
   hf                                               ! do SCF calculation
   ccsd                                             ! do CCSD calculation, try to restart
   start,4000.2,save,4000.2                         ! and save final T amplitudes
   eom,-2.1,-1.2,-1.4,start=6000.2,save=6000.2      ! do EOM-CCSD calculation, try to restart
                                                    ! and save final excited states' amplitudes
   
   
   
   ebase(n)=energy(1)                               ! save ground state energy for this geometry
   e2(n)=energy(2)-energy(1)                        ! save excitation energies for this geometry
   e3(n)=energy(3)-energy(1)
   e4(n)=energy(4)-energy(1)
   r=r+0.01                                         ! increment distance
   enddo                                            ! end of do loop
   table,rr,ebase,e2,e3,e4                          ! make table with results
   digits,2,8,5,5,5,5,5,5,5,5                       ! modify number of digits
   head,R(Ang),EGRST,E_EXC(2.1),E_EXC(1.2),E_EXC(1.4)! modify headers of table
   ! title of table
   title,EOM-CCSD excitation energies for hydrogen fluoride (in hartree), basis $basis
   save,hf_eom_ccsd.tab                             ! save table in file

This calculation produces the following table:

.. code-block:: text

    EOM-CCSD excitation energies for hydrogen fluoride (in hartree), basis AVDZ
   
      R(ANG)        EGRST     E_EXC(2.1)  E_EXC(1.2)  E_EXC(1.4)
        0.80   -100.23687380     0.56664     0.41204     0.56934
        0.81   -100.24094256     0.56543     0.40952     0.56812
        0.82   -100.24451598     0.56422     0.40695     0.56690

etc.

.. _excited_states_with_equation-of-motion_ccsd_eom-ccsd--eom-ccsd-transition-moments-for-hydrogen-fluoride:

EOM-CCSD transition moments for hydrogen fluoride
=================================================

This example shows how to calculate and store CCSD and EOM-CCSD density matrices, calculate dipole and quadrupole moments (transition moments from the ground to excited states are calculated), and how to use the EOM-CCSD excited state density for Mulliken population analysis.

.. code-block:: text
   :caption: examples/hf_eom_prop.inp

   ***, Properties and transition moments for several lowest states of hydrogen fluoride
   basis=avdz                                       ! define basis set
   geometry={h;f,h,r}                               ! z-matrix
   r=0.92 Ang                                       ! define distance
   
   hf                                               ! do SCF calculation
   {ccsd                                            ! do CCSD calculation
   dm,5600.2                                        ! density matrices will be stored here
   expec,response,qm                                ! require quadrupole moments
   eom,-3.1,-2.2,-2.3,-2.4,trans=1}                 ! do EOM-CCSD calculation + properties
   
   pop;density,5600.2,state=2.4                     ! make population analysis for state 2.4

This calculation produces the following table:

.. code-block:: text

   --------------------------------------------------------------------------------
                           Final Results for EOM-CCSD
                                (moments in a.u.)
   --------------------------------------------------------------------------------
   
     State    Exc. Energy (eV)            X              Y              Z
      2.1         14.436
   
    Right transition moment           0.00000000     0.00000000     0.65349466
    Left  transition moment           0.00000000     0.00000000     0.68871635
    Dipole strength                   0.45007246
    Oscillator strength               0.15917669
    Dipole moment                     0.00000000     0.00000000     0.88758090

etc.

.. _excited_states_with_equation-of-motion_ccsd_eom-ccsd--calculate-an-eom-ccsd-state-most-similar-to-a-given-cis-state:

Calculate an EOM-CCSD state most similar to a given CIS state
=============================================================

This example shows how to force the convergence of the EOM-CCSD program to a state, which resembles at most a given CIS state.

.. code-block:: text
   :caption: examples/hf_eom_conv.inp

   ***, EOM-CCSD, vector following procedure
   basis=avdz                                     ! define basis set
   geometry={h;f,h,r}                             ! z-matrix
   r=0.92 Ang                                     ! define distance
   hf;save,2100.2                                 ! do SCF calculation, save orbitals
   cis,-4.4,exfile=6000.2                         ! do CIS calculation, save amplitudes
   ccsd;save,4000.2                               ! do CCSD calculation, save amplitudes
   eom,-4.4,checkovlp=1,exfile=6000.2             ! do EOM-CCSD calculation,
                                                  ! check overlap of singles with CIS vectors
                                                  ! stored in record given in exfile
   eompar,inisingl=200,inidoubl=0                 ! for first approximation take 200 single CSF
                                                  ! of approximate hamiltonian
   ccsd;start,4000.2                              ! do CCSD calculation, try to restart
   eom,2.4,follow=2,exfile=6000.2,checkovlp=1     ! do EOM-CCSD calculation for state closest
                                                  ! to 2.4 CIS state, check overlap of singles
                                                  ! with CIS vectors stored in exfile
   eompar,inisingl=200,inidoubl=0
   eomprint,loce=1                                ! print overlaps of sample and EOM vectors in
                                                  ! each iteration

.. _excited_states_with_equation-of-motion_ccsd_eom-ccsd--excited-states-with-cis:

Excited states with CIS
-----------------------

Excitation energies can also be calculated using the Configuration-Interaction Singles (CIS) method. By default, singlet excited states are calculated. Triplet excited states can be obtained by setting ``triplet``\ =1 in ``EOM`` card. This method cannot be expected to give accurate results, but can be used for quite large molecules. The states to be computed are specified as in ``EOM``. Setting ``trans``\ =1 switches on the calculation of dipole transition moments (length gauge), while ``trans``\ =2 allows to obtain additionally one-electron properties of excited states. By default, dipole moments are calculated. Other required properties can be specified using ``EXPEC`` card. ``trans``\ =0 and 1 work in direct mode.

.. code-block:: text

   hf
   cis,-3.1,1.2,trans=2

.. _excited_states_with_equation-of-motion_ccsd_eom-ccsd--first-and-second-order-properties-for-ccsd-from-expectation-value-cc-theory-xccsd:

First- and second-order properties for CCSD from expectation-value CC theory (XCCSD)
------------------------------------------------------------------------------------

[cprop_ccsd] First-order and frequency-dependent second-order properties, derived from the expressions based on the expectation value of a one-electron operator, can be obtained with the ``CPROP`` directive for the closed-shell CCSD method. For first-order properties obtained from the energy-derivative approach see section `expectation values <the_closed_shell_ccsd_program.html#expectation-values>`__. The expectation-value methods utilized in the program are described in the following papers:

:math:`[1]` B. Jeziorski and R. Moszynski, *Int. J. Quantum Chem.*, **48**, 161 (1993);
:math:`[2]` T. Korona and B. Jeziorski, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.2364489>`__ **125**, 184109 (2006);
:math:`[3]` R. Moszynski, P. S. Żuchowski and B. Jeziorski, *Coll. Czech. Chem. Commun.*, **70**, 1109 (2005);
:math:`[4]` T. Korona, M. Przybytek and B. Jeziorski, `Mol. Phys. <https://dx.doi.org/10.1080/00268970600673975>`__ **104**, 2303 (2006),
:math:`[5]` T. Korona, *Theor. Chem. Acc.*, **129**, 15 (2011).

Note that properties obtained from the expectation-value expression with the coupled cluster wave function **are not** equivalent to these derived from gradient or linear-response methods, although the results obtained with both methods are quite similar. In XCC the exponential ansatz for the wave function is utilized for the bra side, too.

For the first-order properties the one-electron operators should be specified in the ``EXPEC`` card, while for the second-order properties – in the ``POLARI`` card. A density can be saved by specifying the ``DM`` card.

For the first-order properties the option ``XDEN=1`` should be usually given. Other options specify a type of the one-electron density, which can be either the density directly derived from the expectation-value expression, see Eq. (8) of Paper 2, or the modified formula, rigorously correct through the :math:`{\cal O}(W^3)` Møller-Plesset (MP) order, denoted as :math:`\bar X(3)_{\rm resp}` in Papers 1 and 2. In the first case the option ``PROP_ORDER``\ =\ *n* can be used to specify the approximation level for single and double excitation parts of the so-called :math:`S` operator (see [2], Eq. (9)); :math:`n=\pm 2,\pm 3,\pm 4`, where for a positive :math:`n`: all approximations to :math:`S` up to :math:`n` are used, and for a negative :math:`n` only a density with :math:`S` obtained on the :math:`|n|` level will be calculated. Another option related to the :math:`S` operator is ``HIGHW``\ =\ *n*, where :math:`n=0,1`; if :math:`n`\ =0, some parts of :math:`S_1` and :math:`S_2` operators of a high MP order are neglected. Below an example of a standard use of this method is given:

``CPROP,XDEN=1,PROP_ORDER=-3,HIGHW=0``

The combination above is also available by writing ``EXPEC,XCCSD`` after the ``CCSD`` card. A cheap method denoted as XCCSD(3), obtained by a simplification of the original XCCSD formula, is available by setting

``CPROP,XDEN=-21``

or by writing ``EXPEC,XCCSD(3)`` after the ``CCSD`` card.

In the second case the options ``X3RESP=1`` and the ``CPHF,1`` card (or alternatively the ``EXPEC`` card) should be specified,

``CPROP,XDEN=1,X3RESP=1;CPHF,1``

For the second-order properties always the following options should be given:

``CPROP,PROPAGATOR=1,EOMPROP=1``

The recommended CCSD(3) model from Paper 4 requires that additionally the ``PROP_ORDER=3`` and ``HIGHW=0`` options are specified. Frequencies for dynamic properties (in atomic units) should be given in variables ``OMEGA_RE`` (real parts) and ``OMEGA_IM`` (imaginary parts). If one of these arrays is not given, it is filled with zeros. Other options for the second-order properties involve

* ``OMEGAG`` (default 0.3). There are two linear-equation solvers, ``OMEGAG`` is a minimum frequency, for which the second solver (working for large frequencies) is used.
* ``DISPCOEF=n`` if :math:`n>0`, calculate dispersion integrals for the van der Waals coefficients with operators given in the ``POLARI`` card, using :math:`n` as a number of frequencies for the numerical integration. In this case the frequency values given in ``OMEGA_RE`` and ``OMEGA_IM`` are ignored. If two molecules are calculated in the same script one after another, also the mixed dispersion integrals are calculated. The isotropic :math:`C_6` coefficient is stored in a variable ``DISPC6``, the isotropic :math:`C_9` nonadditive coefficient – in a variable ``DISPC9``. All necessary informations for the calculation of dispersion integrals are written to the ascii file *name.dispinfo*, where *name* is the name of the ``MOLPRO`` script.
* ``THRPROPAG`` if given, use this threshold as a convergence criterion for the linear-equation solver for the first-order perturbed CCSD amplitudes.
* **``STARTT1``\ =\ *n*** various start options for the iterative linear-equation solver for the first-order perturbed CCSD amplitudes, the most useful is :math:`n=0` (zero start) and :math:`n=7` (start from the negative of the r.h.s. vector rescaled by some energetic factors dependent on the diagonal of the Fock matrix and the specified frequency).
