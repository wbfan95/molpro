.. raw:: html

   <span id="print-options"></span>

.. _local_methods_for_excited_states--local-methods-for-excited-states:

Local methods for excited states
================================

.. _local_methods_for_excited_states--local-cc2-and-adc-2:

Local CC2 and ADC(2)
====================

Bibliography:
**General local CC2 for excited states:**
:math:`[1]` D. Kats, T. Korona and M. Schütz, *Local CC2 electronic excitation energies for large molecules with density fitting*, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.2339021>`__ **125**, 104106 (2006).
:math:`[2]` D. Kats, T. Korona and M. Schütz, *Transition strengths and first-order properties of excited states from local coupled cluster CC2 response theory with density fitting*, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.2755778>`__ **127**, 064107 (2007).
**Laplace transformed local CC2 for excited states:**
:math:`[3]` D. Kats and M. Schütz, *A multistate local coupled cluster CC2 response method based on the Laplace transform*, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3237134>`__ **131**, 124117 (2009).
:math:`[4]` D. Kats and M. Schütz, *Local Time-Dependent Coupled Cluster Response for Properties of Excited States in Large Molecules*, Z. Phys. Chem. **224**, 601 (2010).
:math:`[5]` K. Freundorfer, D. Kats, T. Korona and M. Schütz, *Local CC2 response method for triplet states based on Laplace transform: Excitation energies and first-order properties*, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3506684>`__ **133**, 244110 (2010).
:math:`[6]` K. Ledermüller, D.Kats and M. Schütz, *Local CC2 response method based on the Laplace transform: Orbital-relaxed first-order properties for excited states*, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.4818586>`__ **139**, 084111 (2013).
**Analytical nuclear gradients for ground and excited states:**
:math:`7]` K. Ledermüller and M. Schütz, *Local CC2 response method based on the Laplace transform: Analytic energy gradients for ground and excited states*, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.4872169>`__ **140**, 164113 (2014).
:math:`8]` M. Schütz, *Oscillator strengths, first-order properties, and nuclear gradients for local ADC(2)*, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.4921839>`__ **142**, 214103 (2015).
**Previous work on local methods for excited states (LEOM-CCSD):**
:math:`[9]` T. Korona and H.-J. Werner *Local treatment of electron excitations in the EOM-CCSD method*, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.1537718>`__ **118**, 3006 (2003).

All publications resulting from use of this program must acknowledge Ref. [3] when calculating singlet states, Ref. [5] when calculating triplet states and properties, and Refs. [6-8] when calculating orbital relaxed properties or analytic gradients, *e.g.*, when performing geometry optimizations of excited states.

The command ``LT-DF-LCC2`` calls the Laplace transformed LCC2 program, while the command ``LT-DF-LADC(2)`` calls LADC(2). The excited states of interest should be specified on the ``EOM`` card. An LCC2 linear response calculation invokes a LCC2 ground state calculation which includes all strong pairs. Close, weak, etc. pairs are neglected, *i.e.*, not included neither in the LCC2 ground state calculations, nor in terms of the excited state calculation involving ground state amplitudes. For that reason, a sufficiently long list of strong pairs should be used in LCC2 linear response calculations (default is inclusion of all pairs with interorbital distance up to 10 bohrs). In contrast, an LADC(2) calculation usually invokes only a ground state LMP2 calculation involving strong, close, and weak pairs (all these pairs are later included in the excited state calculation). For ADC(2), a distinction of strong and weak pairs is sensible, since for ADC(2) transition moments second order doubles (and singles) are required, which are obtained from a partial local MP4 calculation that is restricted to strong pairs only (*vide infra*).

**Note: Geometry optimizations using the LT methods are no longer supported. Analytical energy gradients are disabled unless the Molpro variable ``ENABLE_LTGRAD=1`` is set before FORCES or OPTG.**

.. _local_methods_for_excited_states--options-for-eom:

Options for EOM
===============

see also section `options for EOM <excited_states_with_equation-of-motion_ccsd_eom-ccsd.html#options-for-eom>`__.

In the case of LT-DF-LCC2/ADC(2) multistate calculations are possible, and it is recommended to calculate more states as needed.

The parameters on the ``EOM`` card:

``EOM,-n.1, key1=value1, key2=value2,…``

where *n.1* is the last state of interest, e.g., with ``EOM``,\ *-5.1* the four lowest excited states will be calculated. The following keywords ``key`` are possible:

* **``SINGLET``\ =\ *ising*** If set to 1, singlet states will be calculated (default).
* **``TRIPLET``\ =\ *itrip*** If set to 1, triplet states will be calculated (not implemented for ADC(2)).
* **``EXFILE``\ =\ *record.ifil*** Record for converged CIS eigenvectors (default 6100.2).
* **``SAVE``\ =\ *record.ifil*** Record for save of restart information.
* **``SAVET``\ =\ *record.ifil*** Record for restart information for triplet states (if calculated together with singlet states).
* **``START``\ =\ *record.ifil*** Record for restart of previous calculation.
* **``STARTT``\ =\ *record.ifil*** Record for restart of previous calculation (if calculated together with singlet states).
* **``NSRCH4ST``\ =\ *nst*** In the first *nst* iterations in the Davidson diagonalisation the excited state domains are determined for each basis vector in the Davidson subspace ("search for states") (default 7).
* **``THRLCH``\ =\ *thrlch*** threshold for the Davidson procedure. If smaller than zero, the Davidson procedure is skipped and DIIS is started directly instead (possible only for restart, ``SAVE`` and ``START`` have to be identical).
* **``THRLCD``\ =\ *thrlcd*** threshold for DIIS.
* **``ADC2``\ =\ *adc2*** if :math:`=1`, do ADC(2) calculation instead of CC2.
* **``LTGS``\ =\ *ltgs*** if :math:`=1`, use LT-DF-LMP2 for the ground state.

Default local approximations are defined according to procedure described in Ref. [3] (Laplace domains).

* **``INTFRAC``\ =\ *fracint*** Rough criterion for specifying eom-domains from laplace-transformed integrals (default 0.8).
* **``INTEXC``\ =\ *excint*** Criterion for specifying important orbitals from laplace-transformed integrals (default 0.999).
* **``REALFRAC``\ =\ *fracreal*** Exact criterion for specifying eom-domains from laplace-transformed integrals (default 0.98).
* **``FULLFRAC``\ =\ *fracfull*** Check for all orbital domains (complete sum over all orbitals) (default 0.95).

To switch to local approximations calculated according to Ref. [9] (Boughton-Pulay procedure for excited states), set ``INTFRAC`` to zero.

Occupied orbital pair lists are calculated from important orbitals (Refs. [1,5]).

* **``EWEAKPAIR``\ =\ *ewpair*** Distance criterion for excited state orbital pairs definition (default 5).
* **``ALLSTRONG``\ =\ *allstr*** Different possibilities for excited state orbital pairs:

0: :math:`[ij]\leq` *ewpair*, :math:`[im]\leq` *ewpair*, :math:`[mn]\leq` *ewpair*;
1: :math:`\forall [ij]`, :math:`\forall [im]`, :math:`[mn]\leq` *ewpair*;
2: :math:`\forall [ij]`, :math:`[im]\leq` *ewpair*, :math:`[mn]\leq` *ewpair* (default);
where :math:`i`, :math:`j` are important orbitals and :math:`m`, :math:`n` non-important. More detailed see Ref. [1].

One can try to improve the convergence of iterative procedures by changing following parameters

* **``PRECOND``\ =\ *prec*** Type of preconditioner in LT-DF-LCC2/ADC(2) and DF-CIS:

0: canonical orbital energies;
3: solving linear equations including diagonal part of :math:`(H-F)^{\rm CIS}` with MINRES (default).

* **``HSCAL``\ =\ *hscl*** Scaling factor for diagonal part of :math:`(H-F)^{\rm CIS}` matrix in the case of linear equations preconditioner (default 0.7).

Properties are also activated on the ``EOM`` card:

* **``PROPES``\ =\ *prop*** States for which properties (dipole moments) should be calculated,

``e.g., PROPES=-3.1+5.1-8.1+15.1 $\Longrightarrow$ 2.1 3.1 5.1 6.1 7.1 8.1 15.1``

* **``TRANES``\ =\ *tran*** States for which transition moments should be calculated, syntax like for properties.
* **``DENSAVE``\ =\ *rec.ifil*** Record, where densities calculated for states *prop* can be saved (for printing, see `print options <local_methods_for_excited_states.html#print-options>`__)

As already mentioned above, ADC(2) transition moments require second-order ground-state singles and doubles amplitudes [see e.g. G. Wälz, D. Kats, D. Usvyat, T. Korona and M. Schütz, `Phys. Rev. A <https://dx.doi.org/10.1103/PhysRevA.86.052519>`__ **86**, 052519 (2012); ADC(2) is equivalent to TD-UCC[2]-H]. This is done by carrying out a partial local MP4 calculation, with second-order doubles restricted to strong pairs. For ADC(2) excitation energies or first-order properties just the first-order LMP2 amplitudes are required. Strong, close, and weak pairs actually all enter the subsequent excited state LADC(2) calculations, whereas in LCC2 response calculations only ground state amplitudes of strong pairs do enter the response. Since LCC2 calculations are cheap in comparison (and no higher-order ground state amplitudes are needed for properties or transition strengths as in ADC(2), a distinction of strong pairs treated by LCC2, and weak pairs treated by LMP2 does not make much sense.

By default, orbital un-relaxed properties are computed. In order to calculate also orbital relaxed properties the option ``ORBREL`` on the ``LOCAL`` card should be set to 1, *i.e.*,

.. code-block:: text

   LOCAL,ORBREL=1

This also applies to the calculation of nuclear gradients. Options concerning nuclear gradients, which are also activated on the ``EOM`` card, are

* **``GSONLY``\ =0 or 1** 1: only ground state gradient is calculated
* **``GRADSTATE``\ =\ *gradstate*** Excited state for which the gradient is to be calculated, e.g., ``GRADSTATE=2.1``; must be combined with ``GSONLY=0``
* **``GRADDIIS``\ =0 or 1** 0: DIIS after Davidson diagonalization is switched off for all states except *gradstate*
* **``NOFOLLOWGRAD``\ =0 or 1** 0: tries to follow a state in a geometry optimization after crossing on the basis of the overlap with eigenvector of previous geometry; 1: calculate gradient of state number *gradstate* regardless of crossing
* **``ONLYTOTZLM``\ =0 or 1** 1: only total, rather than ground- and excited state Lagrange multipliers for orbital variations are computed. Hence, only one set of CPL and CPHF equations need to be solved rather than two. However, orbital relaxed properties are then not available.

.. _local_methods_for_excited_states--parameters-on-laplace-card:

Parameters on LAPLACE card
==========================

* ``NPOINTS`` Number of quadrature points (default (for CC2) 3).
* ``NPOINTS\_CC2S`` Number of quadrature points in CC2 in "search for states" (default 1).
* ``DISTRF`` Type of distribution function in functional for determination of Laplace points:

0: integral with f_x=1;
4: sum of distributions f_x (default).

* ``NULLPOINT`` If larger than zero, use also a Laplace-point with t=0. In case of CC2 is always zero.

.. _local_methods_for_excited_states--print-options:

Print options
=============

Setting ``GPRINT,CIVECTOR=1`` prints the ten largest canonical contributions from singles vectors in each iteration.

``For EOMPRINT card:``

* ``LOCEOM`` :math:`\geq 0`: print eom domain informations
* ``POPUL`` :math:`\leq 0`: dont print population analysis

The densities saved with ``DENSAVE`` can be written into a cube file. Corresponding commands in the :doc:`CUBE module <dump_density_or_orbital_values_cube>` are

* **``DENSITY``,\ *rec.ifil*,\ ``cc2``** Creates a cube file from the ground state density saved on record *rec.ifil*.
* **``DENSITY``,\ *rec.ifil*,\ ``full,state``\ =\ *st.1*** Creates a cube file from the excited state density of state *st.1*.
* **``DENSITY``,\ *rec.ifil*,\ ``diff,state``\ =\ *st.1*** Creates a cube file from the difference density (``full`` - ``cc2``) for state *st.1*.

.. _local_methods_for_excited_states--examples:

Examples
========

Example 1:

.. code-block:: text

   ***,The five lowest singlet excited states of water molecule
   memory,64,m
   gdirect
   symmetry,nosym;orient,noorient
   geometry={
   o ,,  0.000,  0.000,  0.119
   h1,,  1.423,  0.000, -0.947
   h2,, -1.423,  0.000, -0.947 }
   basis={
   default,vdz
   set,mp2fit
   default,vdz/mp2fit
   set,jkfit
   default,vdz/jkfit }
   hf
   {lt-df-lcc2                     !ground state CC2
   eom,-6.1                        !five lowest states
   eomprint,popul=-1,loceom=-1 }   !minimize the output

The excitation energies (in eV) stand after the calculation in array ``OMEGAF_S`` for singlet states and in ``OMEGAF_T`` for triplet states.

Example 2:

.. code-block:: text

   ***,The five lowest triplet excited states and properties
   memory,64,m
   gdirect
   symmetry,nosym;orient,noorient
   geometry={
   o ,,  0.000,  0.000,  0.119
   h1,,  1.423,  0.000, -0.947
   h2,, -1.423,  0.000, -0.947 }
   basis={
   default,vdz
   set,mp2fit
   default,vdz/mp2fit
   set,jkfit
   default,vdz/jkfit }
   hf
   {lt-df-lcc2                     !ground state CC2
   !five lowest triplet states, dipole moments for four lowest, density saved:
   eom,-6.1,triplet=1,singlet=0,propes=-5.1,densave=5000.2
   eomprint,popul=-1,loceom=-1 }   !minimize the output
   !ground state density, file h2o0_density.cube:
   {cube,h2o0,,80,80,80
   density,5000.2,cc2 }
   !difference excited state density, file h2o1_density.cube:
   {cube,h2o1,,80,80,80
   density,5000.2,diff,state=2.1 }

In order to set up an input for a geometry optimization of an excited state we recommend to use the input examples `furan_opt_ltdflcc2lr.inp <media/examples/furan_opt_ltdflcc2lr.inp>`__ (for local CC2) and `furan_opt_ltdflucc2lr.inp <media/examples/furan_opt_ltdflucc2lr.inp>`__ (for local ADC(2) aka TD-LUCC[2]-H) as templates. Provided that second-order methods like CC2 or ADC(2) are appropriate for the state to be optimized, it is recommended to use local ADC(2) rather than local CC2, since the former is considerably faster. Even if a local CC2 optimized geometry of an excited state is required, it is wise to preoptimize with local ADC(2). For a comparison of the performance of these two methods in geometry optimizations we refer to Ref. [8].

**Note: Geometry optimizations using the LT methods are no longer supported. Analytical energy gradients are disabled unless the Molpro variable ``ENABLE_LTGRAD=1`` is set before FORCES or OPTG.**
