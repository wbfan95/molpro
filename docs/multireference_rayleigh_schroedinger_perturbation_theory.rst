.. raw:: html

   <span id="caspt2-gradients"></span>

.. raw:: html

   <span id="excited-state-calculations"></span>

.. raw:: html

   <span id="further-options-for-caspt2-and-caspt3"></span>

.. raw:: html

   <span id="level-shifts"></span>

.. raw:: html

   <span id="modified-fock-operators-in-the-zeroth-order-hamiltonian"></span>

.. raw:: html

   <span id="multi-state-caspt2"></span>

.. _multireference_rayleigh_schroedinger_perturbation_theory--multireference-rayleigh-schr-dinger-perturbation-theory:

Multireference Rayleigh Schrödinger perturbation theory
=======================================================

Bibliography:

* Original RS2/RS3: H.-J. Werner, `Mol. Phys. <https://dx.doi.org/10.1080/002689796173967>`__ **89**, 645-661 (1996)
* New internally contracted RS2C: P. Celani and H.-J. Werner, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.481132>`__ **112**, 5546 (2000)

All publications resulting from use of this program must acknowledge the above.

The commands

* ``RS2``,\ *options*
* ``RS2C``,\ *options*
* ``RS3``,\ *options*

are used to perform second or third-order perturbation calculations. ``RS3`` always includes ``RS2`` as a first step. For closed-shell single-reference cases, this is equivalent to ``MP2`` or ``MP3`` (but a different program is used). ``RS2C`` calls a new more efficient second-order program (see below), which should normally be used if third-order is not required (note that ``RS3C`` is not available).
Analytic gradients are only available for the ``RS2`` program.

:doc:`Density fitting <density_fitting>` is also available for ``RS2`` and ``RS2C``, and as usual invoked by the prefix ``DF-``.

for ``RS2`` an explicitly correlated version as described in T. Shiozaki and H.-J. Werner, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3489000>`__ **133**, 141103 (2010) is available. This is called using the command

* ``RS2-F12``, *options*

*Options* can be the following:

* ``Gn`` Use modified zeroth order Hamiltonian, see section `modified Fock-operators in the zeroth-order Hamiltonian. <multireference_rayleigh_schroedinger_perturbation_theory.html#modified-fock-operators-in-the-zeroth-order-hamiltonian>`__
* **``SHIFT=``\ *value*** Level shift, see section `level shifts <multireference_rayleigh_schroedinger_perturbation_theory.html#level-shifts>`__
* **``IPEA=``\ *value*** IPEA shift proposed by G. Ghigo, B. O. Roos, and P.A. Malmqvist, `Chem. Phys. Lett. <https://dx.doi.org/10.1016/j.cplett.2004.08.032>`__ **396**, 142 (2004), see section `level shifts <multireference_rayleigh_schroedinger_perturbation_theory.html#level-shifts>`__.
* **``MIX=``\ *nstates*** Invokes multi-state (MS-CASPT2) treatment using *nstates* states. See section `Multi-State CASPT2 <multireference_rayleigh_schroedinger_perturbation_theory.html#multi-state-caspt2>`__ for more details.
* **``XMS=0``:** MS-CASPT2 method of Finley et al. CPL 288, 299 (1998)
* **``XMS=1``:** Extended multi-state CASPT2 (XMS-CASPT2) method as described in `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3633329>`__ **135**, 081106 (2011). fully invariant treatment of level shifts (recommended).
* **``XMS=2``:** XMS-CASPT2 method; level shift is only applied to the diagonal of H0.
* **``ROOT=``\ *ioptroot*** Root number to be optimized in geometry optimization. This refers to the *nstates* included in the MS-CASPT2. See section `CASPT2 gradients <multireference_rayleigh_schroedinger_perturbation_theory.html#caspt2-gradients>`__ for more details.
* **``SAVEH=``\ *record*** Record for saving the effective Hamiltonian in MS-CASPT2 calculations. If this is not given, a default record will be used (recommended).
* ``INIT`` (logical) Initializes a MS-CASPT2 with single state reference functions, see section `Multi-State CASPT2 <multireference_rayleigh_schroedinger_perturbation_theory.html#multi-state-caspt2>`__
* ``IGNORE`` (logical) Flags an approximate gradient calculation without CP-CASPT2; see section `CASPT2 gradients <multireference_rayleigh_schroedinger_perturbation_theory.html#caspt2-gradients>`__ for details.
* ``PROPERTIES`` or ``PROP`` (logical, default true, ``RS2C`` only) Flag on whether the expectation values of properties are computed. By default dipole moments are always computed but this may be expensive in multi-state calculations. Pass ``NOPROP`` to skip the property calculation.

In addition, all valid options for ``MRCI`` can be given (see Sect. :doc:`the MRCI program <the_mrci_program>`).

**'Note: level shifts have to be given as options.** The SHIFT directive refers to denominator shifts, which affect the convergence but not the Hamiltonian and the results.

.. _multireference_rayleigh_schroedinger_perturbation_theory--introduction:

Introduction
============

Multireference perturbation calculations are performed by the MRCI program as a special case. For RS2 (CASPT2,RASPT2) only matrix elements over a one-electron operator need to be computed, and therefore the computational effort is much smaller than for a corresponding MRCI. For RS3 (CASPT3) the energy expectation value for the first-order wavefunction must be computed and the computational effort is about the same as for one MRCI iteration. The RS2 and RS3 programs use the same configuration spaces as the MRCI, i.e., only the doubly external configurations are internally contracted.

A new version of the program has been implemented in which also subspaces of the singly external and internal configuration spaces are internally contracted (see reference given above). This program, which is called using the keyword ``RS2C``, is more efficient than ``RS2``, in particular for large molecules with many closed-shell (inactive) orbitals. It is recommended to use this program for normal applications of second-order multireference perturbation theory (CASPT2, RASPT2). Note that it gives slightly different results than ``RS2`` due to the different contraction scheme. It should also be noted that neither ``RS2`` or ``RS2C`` are identical with the CASPT2 of Roos et al. `J. Chem. Phys. <https://dx.doi.org/10.1063/1.462209>`__ **96**, 1218 (1992), since certain configuration subspaces are left uncontracted. However, the differences are normally very small. The last point that should be mentioned is that the calculation of CASPT2/RASPT2 density matrices (and therefore molecular properties) is presently possible only with the RS2 command and *not* with RS2C.

The results of multireference perturbation theory may be sensitive to the choice of the zeroth-order Hamiltonian. This dependence is more pronounced in second-order than in third-order. Several options are available, which will be described in the following sections. It may also happen that :math:`(\hat H^{(0)} - E^{(0)})` in the basis of the configuration state functions becomes (nearly) singular. This is known as "intruder state problem" and can cause convergence problems or lead to a blow-up of the wavefunction. Often, such problems can be eliminated by including more orbitals into the reference wavefunction, but of course this leads to an increase of the CPU time. The use of modified Fock operators (see below) or level shifts, as proposed by Roos and Andersson `Chem. Phys. Lett. <https://dx.doi.org/10.1016/0009-2614(95)01010-7>`__ **245**, 215 (1995) may also be helpful. Presently, only "real" level shifts have been implemented.

With no further input cards, the wavefunction definition (core, closed, and active orbital spaces, symmetry) corresponds to the one used in the most recently done SCF or MCSCF calculation. By default, a CASSCF reference space is generated. Other choices can be made using the ``OCC``, ``CORE``, ``CLOSED``, ``WF``, ``SELECT``, ``CON``, and ``RESTRICT`` cards, as described for the ``CI`` program. The orbitals are taken from the corresponding SCF or MCSCF calculation unless an ``ORBITAL`` directive is given.

For a CASPT2 calculation, the zeroth-order Hamiltonian can be brought to a block-diagonal form when (pseudo)canonical orbitals are used. This leads to fastest convergence. It is therefore recommended that in the preceding ``MULTI`` calculation the orbitals are saved using the ``CANONICAL`` directive (note that the default is ``NATORB``).

Most options for MRCI calculations (like ``STATE``, ``REFSTATE`` etc.) apply also for RS2(C) and RS3 and are not described here again. Some additional options which specific for CASPT2/3 and are described below.

.. _multireference_rayleigh_schroedinger_perturbation_theory--excited-state-calculations:

Excited state calculations
==========================

There are two possibilities to perform excited state calculations:

1) One can calculate each state separately. This is done using the card

``STATE,1,root``

where *root* is the desired root (i.e., 2 for the first excited state). In this case the Fock operator used in the zeroth-order Hamiltonian is computed using the density for the given state. Note that all states must have the same symmetry.

2) Alternatively, two or more states can be computed simultaneously, using

``STATE, n [,root1, root2, …, rootn]``

where *n* is the number of states to be computed. The default is to compute the lowest *n* roots. Optionally, this default can be modified by specifying the desired roots *rooti* as shown. One should note that this *does not* correspond to the multi-state CASPT2 as described in section `Multi-State CASPT2 <multireference_rayleigh_schroedinger_perturbation_theory.html#multi-state-caspt2>`__.

In the case that several states are computed simultaneously, the fock operator employed in the zeroth-order Hamiltonian is computed from a state-averaged density matrix, and the zeroth-order Hamiltonians for all states are constructed from the same fock operator. By default, equal weights for all states are used. This default can be modified using the ``WEIGHT`` directive

``WEIGHT,w1, w2,…,wn.``

If a ``REFSTATE`` card is given (see section `defining reference state numbers <the_mrci_program.html#defining-reference-state-numbers>`__), the state-averaged fock operator is made for all reference states, and the ``WEIGHT`` card refers to the corresponding states.

In the case of RS3 the Hamiltonian is diagonalized at the end of calculations using first-order wavefunctions, and the diagonal and transition properties are transformed accordingly. The untransformed properties, if required, can be retrieved from the output.

.. _multireference_rayleigh_schroedinger_perturbation_theory--multi-state-caspt2:

Multi-State CASPT2
==================

Multi-state CASPT2 is implemented as described by Finley et al. CPL **288**, 299 (1998).
This can be done with ``RS2`` or ``RS2C`` (since Molpro 2021).
In both cases there are two different modes in which MS-CASPT2 calculations can be performed:

- Each of the states to be mixed is computed independently, and finally all states are mixed. In the following, such calculations will be denoted "SS-SR-CASPT2" (single-state, single reference CASPT2). There is one contracted reference state for each CASPT2 calculation that is specific for the state under consideration. This is the cheapest method, but there are no gradients available in this case. It is the users responsibility to make sure that no state is computed twice.
- All *nstates* states are treated together, with *nstates* contracted reference states. This is more expensive, but should give a more balanced description since the different reference states can mix in the CASPT2. It is required that *nstates* equals the number of states specified on the ``STATE`` directive. For this case, denoted "MS-MR-CASPT2" (multi-state multi reference CASPT2), analytical energy gradients are available, see section `CASPT2 gradients <multireference_rayleigh_schroedinger_perturbation_theory.html#caspt2-gradients>`__. It is recommended to use the "extended" (XMS) multi-state CASPT2 option, which guarantees invariance of the theory with respect to unitary rotations of the reference functions. The method yields improved potentials in the vicinity of avoided crossings and conical intersections [see T. Shiozaki and H.-J. Werner, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3489000>`__ **133**, 141103 (2010) and T. Shiozaki, C. Woywod and H.-J. Werner, `Phys. Chem. Chem. Phys. <https://dx.doi.org/10.1039/C2CP43381H>`__ **15**, 262 (2013)].

With the ``RS2C`` program the two modes can be mixed, e.g., in a 3-state calculation using the SS-SR-CASPT2 for one state and the MS-MR-CASPT2 for the other two states.

Note that all states must have the same spin and spatial symmetry.

.. _multireference_rayleigh_schroedinger_perturbation_theory--performing-ss-sr-caspt2-calculations:

Performing SS-SR-CASPT2 calculations
====================================

If one wants to mix together *nstates* CASPT2 wavefunctions, a *nstates* single-state, single-reference CASPT2 calculations must be run.

The first calculation must use

``{RS2,MIX=nstates, INIT, options\\``
``STATE,1,1;}``

and the subsequent ones

``{RS2,MIX=nstates, options\\``
``STATE,1,$istate$;}``

for :math:`istate=2,\ldots,nstates`. Further *options* can be given, for instance a level shift.

At the end of each calculation, the CASPT2 wavefunction is stored, and at the end of the last CASPT2 calculation the Bloch Hamiltonian and the corresponding overlap matrix are automatically assembled and printed. The Hamiltonian is diagonalized after symmetrization following Brandow IJQC 15, 207 (1979), as well as with simple half-sum (averaging). The MS-CASPT2 energy and mixing coefficients printed in each case.

The variable MSENERGY(i) (with i=1,...nstates) is set to the multi-state energies obtained with half-sum diagonalization. If a Level Shift is present, MSENERGY(i) contains the multi-state energies obtained with half-sum diagonalization of the Bloch Hamiltonian whose diagonal elements (CASPT2 energies) have been corrected with the level shift.

Example: SS-SR-CASPT2 calculation for LiF

.. code-block:: text
   :caption: examples/lif_sr_mscaspt2.inp

   r=[3,4,5,6,7,8,9,10] ang
   
   i=1
   geometry={Li
             F,1,r(i)}
   
   basis=vtz,F=avtz
   
   hf                      !Hartree-Fock
   
   do i=1,#r               !loop over range of bond distances
   {multi
   closed,3,0,0,0
   occ,   5,2,2,0
   wf;state,2                 !SA-CASSCF for 2 states
   canonical,ci}
   
   {rs2,MIX=2,INIT
   wf;state,1,1}              !single state CASPT2 for reference state 1
   
   e1_caspt2(i)=energy     !unmixed caspt2 energy for ground state
   
   {rs2,MIX=2
   wf;state,1,2}              !single state CASPT2 for reference state 2
   
   e2_caspt2(i)=energy     !unmixed caspt2 energy for excited state
   e1_mscaspt2(i)=msenergy(1)  !ms-caspt2 energy for ground state
   e2_mscaspt2(i)=msenergy(2)  !ms-caspt2 energy for excited state
   enddo
   
   {table,r,e1_caspt2,e2_caspt2,e1_mscaspt2,e2_mscaspt2
   title,SS-SR-CASPT2 for LiF
   plot,file='lif_sr_mscaspt2.plot'
   }

This produces the plot

.. image:: /media/lif_sr_mscaspt2.svg
   :alt: lif_sr_mscaspt2.svg
   :width: 500px

.. _multireference_rayleigh_schroedinger_perturbation_theory--performing-ms-mr-caspt2-calculations:

Performing MS-MR-CASPT2 calculations
====================================

In the case of multi-state multi-reference CASPT2 calculations, only a single run is needed:

``{RS2,MIX=nstates,options\\``
``STATE,nstates}``

For using the XMS-CASPT2 method option ``XMS=1`` or ``XMS=2`` has to be set. The two variants differ in the treatment of level shifts. ``XMS=1`` is a fully invariant treatment (recommended), while with ``XMS=2`` the level shift is only applied to the diagonal of H0.

At the end of calculations, the reference states and diagonal and transition properties are transformed according of the transformation of mixed CASPT2 states. Corresponding transformed energies and properties can be obtained from MS-prefixed variables, for example MSENERGR(i) or MSTRDMZ etc.

Example: MS-MR-CASPT2 calculation for LiF

.. code-block:: text
   :caption: examples/lif_mr_mscaspt2.inp

   r=[3,4,5,6,7,8,9,10] ang
   
   i=1
   geometry={Li
             F,1,r(i)}
   
   basis=vtz,F=avtz
   
   hf                      !Hartree-Fock
   
   do i=1,#r               !loop over range of bond distances
   {multi
   closed,3,0,0,0
   occ,   5,2,2,0
   wf;state,2                 !SA-CASSCF for 2 states
   canonical,ci}
   
   {rs2,MIX=2
   wf;state,2}                !2-state MS-CASPT2 with 2 reference states
   
   e1_caspt2(i)=energu(1)      !unmixed caspt2 energy for ground state
   e2_caspt2(i)=energu(2)      !unmixed caspt2 energy for ground state
   
   e1_mscaspt2(i)=msenergy(1)  !ms-caspt2 energy for ground state
   e2_mscaspt2(i)=msenergy(2)  !ms-caspt2 energy for excited state
   
   {rs2,MIX=2,XMS=1
   wf;state,2}                !2-state XMS-CASPT2 with 2 reference states
   
   e1_xmscaspt2(i)=msenergy(1)  !ms-caspt2 energy for ground state
   e2_xmscaspt2(i)=msenergy(2)  !ms-caspt2 energy for excited state
   enddo
   
   {table,r,e1_caspt2,e2_caspt2,e1_mscaspt2,e2_mscaspt2,e1_xmscaspt2,e2_xmscaspt2
   title,MS-MR-CASPT2 for LiF
   plot,file='lif_mr_mscaspt2.plot'
   }

This produces the plot

.. image:: /media/lif_mr_mscaspt2.svg
   :alt: lif_mr_mscaspt2.svg
   :width: 500px

One can clearly see that this gives smoother potentials than the SS-SR-CASPT2 calculation in the previous section. Also, the avoided crossing is shifted to longer distances, which is due to the improvement of the electron affinity of F.

Example for XMS-CASPT2 for pyrrole :math:`B_1` states, using ``RS2C`` and density fitting

.. code-block:: text
   :caption: examples/pyrrole_xms_caspt2.inp

   ***,Pyrrole
   memory,64,M;
   
   geometry={
      10
    RS2/VTZ  ENERGY=-209.73179172
    H          0.0000000000       -0.0000000001        2.1166896815
    H          0.0000000000       -2.1059182363        0.7619888215
    H          0.0000000000        2.1059182368        0.7619888221
    H          0.0000000000        1.3572481815       -1.8483571903
    H          0.0000000000       -1.3572481818       -1.8483571900
    N          0.0000000000       -0.0000000001        1.1133413258
    C          0.0000000000        1.1228834673        0.3278824921
    C          0.0000000000       -1.1228834675        0.3278824917
    C          0.0000000000       -0.7098361247       -0.9897171173
    C          0.0000000000        0.7098361249       -0.9897171174
   }
   gexpec,sm
   
   basis=avtz
   
   {df-hf;wf,symmetry=1,spin=0}
   
   {df-multi
   occ,11,3,7,2;closed,9,0,6,0;
   wf,symmetry=1,spin=0;state,1;   !1A1 state
   wf,symmetry=2,spin=0;state,2;   !B1 states
   wf,symmetry=4,spin=0;state,2;   !A2 states
   }
   ecas=energy
   
   shift=0.2
   
   {df-rs2c,shift=shift;                !caspt2 for 1A1 state
   wf,symmetry=1,spin=0;state,1,1}
   ers2(1)=energy
   
   {df-rs2c,shift=shift,mix=2,xms=1;    !xms-caspt2 for B1 states
   wf,symmetry=2,spin=0;state,2}
   ers2(2)=msenergy(1)
   ers2(3)=msenergy(2)
   
   decas=(ecas-ecas(1))*toev        !vertical excitation energies in eV
   ders2=(ers2-ers2(1))*toev
   
   $state=[1A1,1B1,2B1]
   table,state,ecas,ers2,decas,ders2
   digits,,7,7,7,3,3,3,3

This produces:

.. code-block:: text

    STATE        ECAS           ERS2        DECAS     DERS2
    1A1     -208.9123065   -209.7453504   0.0000000   0.000
    1B1     -208.7459285   -209.5288511   4.5273758   5.891
    2B1     -208.7396855   -209.5250933   4.6972569   5.994

.. _multireference_rayleigh_schroedinger_perturbation_theory--modified-fock-operators-in-the-zeroth-order-hamiltonian:

Modified Fock-operators in the zeroth-order Hamiltonian
-------------------------------------------------------

The :math:`g_1`, :math:`g_2`, and :math:`g_3` operators proposed by Andersson [Theor. Chim. Acta **91**, 31 (1995)] as well as a further :math:`g_4` operator may be used. :math:`g_4` makes CASPT2 calculations size extensive for cases in which a molecule dissociates to high-spin open-shell (RHF) atoms.

The index *n* of the operator to be used is specified on the ``RS2``, ``RS2C``, or ``RS3`` card:

``RS2,option\\``
``RS2C,option\\``
``RS3,option``

where *option* can be ``G1``, ``G2``, ``G3``, or ``G4``. This option can be followed or preceded by other valid options.

.. _multireference_rayleigh_schroedinger_perturbation_theory--level-shifts:

Level shifts
------------

Note: level shifts have to be given as options. The SHIFT directive refers to denominator shifts, which affect the convergence but not the Hamiltonian and the results.

Level shifts are often useful to avoid intruder state problems in excited state calculations. ``MOLPRO`` allows the use of shifts as described by Roos and Andersson, `Chem. Phys. Lett. <https://dx.doi.org/10.1016/0009-2614(95)01010-7>`__ **245**, 215 (1995). The shift can be specified on the ``RS2`` or ``RS2C`` card

``RS2 [,G$n$] [,SHIFT=shift],IPEA=value\\``
``RS2C [,G$n$] [,SHIFT=shift],IPEA=value``

Typical choices for the shift is are :math:`0.1 - 0.3`. Only two figures after the decimal point are considered. The shift affects the results, the printed energies as well as the ``ENERGY`` variable include the energy correction for the shift as proposed by Roos and Andersson. At convergence, also the uncorrected energies are printed for comparison.

Alternatively (or in addition), the IPEA shift of G. Ghigo, B. O. Roos, and P.A. Malmqvist, `Chem. Phys. Lett. <https://dx.doi.org/10.1016/j.cplett.2004.08.032>`__ **396**, 142 (2004) can be used. The implementation is not exactly identical to the one in MOLCAS, since in our program the singly external configurations are not (RS2) or only partially (RS2C) contracted. In Molpro, the shift is implemented as follows:

:math:`\frac{1}{2} D_{pp} \epsilon` is added to the occupied part of the Fock matrix; in addition, :math:`2 \epsilon` is added as a general shift (not corrected). :math:`\epsilon` is the value specified with the ``IPEA`` option (default 0). A value of 0.20-0.25 is recommended. This removes intruder state problems to a large extent and usually improves the results. Note that the method is not exactly orbital invariant, and pseudo-canonical orbitals should be used (see ``CANONICAL`` option in MULTI).

It is possible to use ``SHIFT`` and ``IPEA`` simultaneously, but it does not make sense to use one of the ``G``-options together with ``IPEA``.

.. _multireference_rayleigh_schroedinger_perturbation_theory--integral-direct-calculations:

Integral direct calculations
----------------------------

``RS2, RS2C, and RS3 calculations with very large basis sets can be performed in integral-direct mode. The calculation will be direct if a global DIRECT or GDIRECT card appears earlier in the input. Alternatively, (mainly for testing) DIRECT can be specified as an option on the RS$n$[C] card:``

``RS2 [,G$n$] [,SHIFT=shift] [,DIRECT]\\``
``RS2C [,G$n$] [,SHIFT=shift] [,DIRECT]``

.. _multireference_rayleigh_schroedinger_perturbation_theory--caspt2-gradients:

CASPT2 gradients
----------------

Analytic gradients as described in P. Celani and H.-J. Werner, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.1597672>`__ **119**, 5044 (2003) are available for the ``RS2`` program.

CASPT2 analytic energy gradients are computed automatically if a ``FORCE`` or ``OPTG`` command follows (see sections :doc:`energy gradients <energy_gradients>` and :doc:`geometry optimization (OPTG) <geometry_optimization_optg>`). Analytical gradients are presently only available for ``RS2`` calculations (not ``RS2C``), and only for the standard :math:`\hat H^{(0)}` (not G1, G2 etc). Gradients can be computed for single-state calculations, as well as multi-state MS-MR-CASPT2 (see section `Multi-State CASPT2 <multireference_rayleigh_schroedinger_perturbation_theory.html#multi-state-caspt2>`__. However, only states with the same symmetry and spin and the same number of electrons as in the optimized state can be included in the preceding SA-CASSCF (CONFIG,DET must not be given in the CASSCF).

In single state calculations, the gradient is automatically computed for the state computed in CASPT2/RSPT2 (i.e., using ``STATE,1,2`` the second state in the symmetry under consideration is computed, see section `excited state calculations <multireference_rayleigh_schroedinger_perturbation_theory.html#excited-state-calculations>`__). The program works with state-averaged MCSCF (CASSCF) orbitals, and no ``CPMCSCF`` directive is needed. It is necessary that the state under consideration is included in the preceding (state-averaged) MCSCF/CASSCF. The RS2 gradient program can also be used to compute state-averaged MCSCF/CASSCF gradients by using the ``NOEXC`` directive.

In a multi-state MS-MR-CASPT2 calculation, the state for which the gradient is computed must be specified using the ``ROOT`` option (default ``ROOT=1``), i.e.,

``RS2,MIX=nstates, ROOT=ioptroot``

where :math:`1 \le ioptroot \le nstates`.

Level shifts can be used. By default, the exact gradient of the level-shift corrected energy is computed. For a non-zero shift, this requires to solve the CASPT2 Z-vector equations, which roughly doubles the computational effort. In single state calculations it is possible to ignore the effect of the level shift on the gradient and not to solve the Z-vector equation. This variant, which is described in the above paper, may be sufficiently accurate for many purposes. It is invoked using the ``IGNORE`` option, e.g.

``RS2,SHIFT=0.2,IGNORE\\``
``OPTG``

Any publications employing the CASPT2 gradients should cite the above paper. A citation for MS-CASPT2 gradient method is P. Celani and H.-J. Werner, *to be published*.

Example:

CASPT2 geometry optimizations for H\ :math:`_2`\ O:

.. code-block:: text
   :caption: examples/h2o_caspt2_opt.inp

   ***
   gthresh,energy=1.d-10
   !
   basis=vdz
   R=2.0
   R0=R
   Theta=100
   geometry={O
             H1,O,R;
             H2,O,R,H1,THETA}
   
   hf;accu,12
   
   {multi;closed,2}
   
   rs2,shift=0.3,ignoreshift      !ignore shift in computing gradient, i.e., no cp-caspt2
   optg,gradient=1.d-5
   e_opt(1)=energy
   r_opt(1)=r
   theta_opt(1)=theta
   method(1)='rs2,analytical,ignore'
   
   rs2,shift=0.3                  !exact gradient with shift
   optg,gradient=1.d-5
   e_opt(2)=energy
   r_opt(2)=r
   theta_opt(2)=theta
   method(2)='rs2,analytical,exact'
   
   rs2,shift=0.3                  !numerical gradient with shift
   optg,gradient=1.d-5,numerical,fourpoint !use four-point numerical gradient
   e_opt(3)=energy
   r_opt(3)=r
   theta_opt(3)=theta
   method(3)='rs2,numerical'
   
   rs2c,shift=0.3                 !numerical gradient of rs2c with shift
   optg,gradient=1.d-5,fourpoint  !use four-point numerical gradient
   e_opt(4)=energy
   r_opt(4)=r
   theta_opt(4)=theta
   method(4)='rs2c,numerical'
   
   table,method,r_opt,theta_opt,e_opt
   digits,,4,4,8

This produces the Table

.. code-block:: text

    METHOD                   R_OPT  THETA_OPT       E_OPT
    rs2,analytical,ignore   1.8250   102.1069   -76.22789382
    rs2,analytical,exact    1.8261   102.1168   -76.22789441
    rs2,numerical           1.8261   102.1168   -76.22789441
    rs2c,numerical          1.8260   102.1187   -76.22787681

MS-CASPT2 geometry optimization for the second excited :math:`^3B_2` state if H\ :math:`_2`\ O:

.. code-block:: text
   :caption: examples/h2o_mscaspt2_opt.inp

   ***
   gthresh,energy=1.d-12
   !
   basis=vdz
   R=2.0
   R0=R
   Theta=100
   step=0.001
   geometry={O
             H1,O,R;
             H2,O,R,H1,THETA}
   
   hf;accu,12
   
   multi        !state averaged casscf for various triplet states
   closed,2
   wf,10,1,2
   state,3
   wf,10,2,2
   state,2
   wf,10,3,2
   state,3
   canonical,2140.2
   
   rs2,mix=3,root=2,shift=0.2   !optimized second 3B2 state
   wf,10,3,2                    !3B2 wavefunction symmetry
   state,3                      !include 3 states
   optg,gradient=1.d-5          !geometry optimization using analytical gradients
   
   e_opt(1)=msenergy(2)         !optimized ms-caspt2 energy
   r_opt(1)=r                   !optimized bond distance
   theta_opt(1)=theta           !optimized bond angle
   method(1)='rs2,analytical'
   
   rs2,mix=3,shift=0.2
   wf,10,3,2                    !3B2 wavefunction symmetry
   state,3                      !include 3 states
   optg,variable=msenergy(2),gradient=1.d-5,fourpoint
                                !geometry optimization using numerical gradients
   
   e_opt(2)=msenergy(2)         !optimized ms-caspt2 energy
   r_opt(2)=r                   !optimized bond distance
   theta_opt(2)=theta           !optimized bond angle
   method(2)='rs2,numerical'
   
   table,method,r_opt,theta_opt,e_opt
   digits,,4,4,8

This produces the table

.. code-block:: text

    METHOD            R_OPT  THETA_OPT       E_OPT
    rs2,analytical   2.4259    96.7213   -75.81630628
    rs2,numerical    2.4259    96.7213   -75.81630628

.. _multireference_rayleigh_schroedinger_perturbation_theory--coupling-mrci-and-mrpt2-the-cipt2-method:

Coupling MRCI and MRPT2: The CIPT2 method
-----------------------------------------

P. Celani, H. Stoll, H.-J. Werner and P. J. Knowles, `Mol. Phys. <https://dx.doi.org/10.1080/00268970412331317788>`__ **102**, 2369 (2004).

For particularly difficult cases with strong intruder problems, or in which second-order perturbation theory fails to predict reliable results, a new method that couples MRCI and CASPT2 has been developed. This variant is invoked using the ``CIPT2`` directive:

``CIPT2``

In this case all excitations solely from active orbitals are treated by MRCI, while the remaining excitations involving inactive (closed-shell) orbitals are treated by second-order perturbation theory. Both methods are coupled by minimizing an appropriate energy functional. Of course, this method is much more expensive that MRPT2. The cost is comparable to the cost for an MRCI without correlating the inactive orbitals.

.. _multireference_rayleigh_schroedinger_perturbation_theory--further-options-for-caspt2-and-caspt3:

Further options for CASPT2 and CASPT3
-------------------------------------

Other options can be set using the ``OPTION`` command. These options are mainly used for testing purposes and should be used with care. It should be noted that the only option that can be modified in the RS2C program is ``IFDIA``: all others only work with RS2/RS3.

``OPTION,code1=value,code2=value,$\ldots$``

Of relevance for the CASPT2/3 program are the following options:

* ``IPROCS=0`` (Default). Calculation uses uncontracted singles with ``RS2``.
* ``IPROCS=1`` Non-interacting singles are projected out during update. This is an approximate procedure which should be used with care.
* ``IPROCS=2`` The singles are fully internally contracted in ``RS2``. This is achieved via a projection operator during the coefficient update and may be inefficient. G
* ``IPROCS=3`` Only singles with one or two holes in the closed-shells are internally contracted in ``RS2`` using a projection operator.
* ``IPROCI=0`` (Default). Calculation uses uncontracted internals with ``RS2``.
* ``IPROCI=1`` Internals with two holes in the inactive space are internally contracted in ``RS2`` using a projection operator.
* ``IPROCS=3,IPROCI=1`` This combination of options reproduces with ``RS2`` the ``RS2C`` result using projection operators. This requires lot of memory and disk space and it is feasible only for small molecules.
* ``IFDIA=0`` (Default). All off-diagonal elements of the effective Fock matrix are included.
* ``IFDIA=1`` The internal-external block of the Fock-matrix is neglected. This eliminates the single-pair coupling.
* ``IFDIA=2`` All off-diagonal elements of the Fock matrix are neglected. This corresponds to CASPT2D of Andersson et al. Note: in this case the result is not invariant to rotations among active orbitals!
* ``IHINT=0`` (Default). Only one-electron integrals are used in the zeroth-order Hamiltonian for all interactions.
* ``IHINT=1`` The all-internal two-electron integrals are used in the zeroth-order Hamiltonian for the internal-internal and single-single interactions.
* ``IHINT=2`` The all-internal two-electron integrals in the zeroth-order Hamiltonian are used for the internal-internal, single-single, and pair-pair interactions. Using ``IHINT=2`` and ``IDFIA=1`` corresponds to Dyall’s CAS/A method for the case that CASSCF references with no closed-shells (inactive orbitals) are used. Note that this requires more CPU time than a standard CASPT2 calculation. Moreover, convergence of the CAS/A method is often slow (denominator shifts specified on a ``SHIFT`` card may be helpful in such cases). In general, we do not recommend the use of ``IHINT`` with nonzero values.
* ``NOREF=1`` (Default). Interactions between reference configurations and singles are omitted.
* ``NOREF=0`` Interactions between reference configurations and singles are included. This causes a relaxation of the reference coefficients but may lead to intruder-state problems.
* ``IMP3=2`` After CASPT2 do variational CI using all internal configurations and the first-order wavefunctions of all states as a basis. In this case the second-order energy will correspond to the variational energy, and the third-order energy approximately to a Davidson-corrected energy. This is useful in excited state calculations with near-degeneracy situations.
