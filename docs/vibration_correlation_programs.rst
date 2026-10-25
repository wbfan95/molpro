.. raw:: html

   <span id="the-vci-program-vci"></span>

.. raw:: html

   <span id="the-vibrational-mp2-program-vmp2"></span>

.. raw:: html

   <span id="the-vibrational-multi-reference-ci-program-vmrci"></span>

.. _vibration_correlation_programs--vibration-correlation-programs:

Vibration correlation programs
==============================

.. _vibration_correlation_programs--the-vci-program-vci:

The VCI program (VCI)
=====================

``VCI,options``

``VCI calculations account for vibration correlation effects and use potential energy surfaces as generated from the XSURF program and a basis of VSCF modals or harmonic oscillator functions. For each vibrational state an individual VCI calculation will be performed. As VCI calculations may require substantial computer resources, these calculations can be rather expensive. Currently, two different VCI programs (configuration selective and conventional) are available (see below).  The details of the VCI program are described in:\\``

T. Mathea, G. Rauhut, *Advances in vibrational configuration interaction theory - part 1: Efficient calculation of vibrational angular momentum terms.* `J. Comput. Chem. <https://onlinelibrary.wiley.com/doi/abs/10.1002/jcc.26762>`__ **42**, 2321–2333 (2021).
T. Mathea, T. Petrenko, G. Rauhut, *Advances in vibrational configuration interaction theory - part 2: Fast screening of the correlation space.*. `J. Comput. Chem. <https://onlinelibrary.wiley.com/doi/abs/10.1002/jcc.26764>`__ **43**, 6–18 (2022).
B. Schröder, G. Rauhut, *From the automated calculation of potential energy surfaces to accurate vibrational spectra*, `J. Phys. Chem. Lett. <https://doi.org/10.1021/acs.jpclett.4c00186>`__ **15**, 3159 (2024).

.. _vibration_correlation_programs--options:

Options
=======

The following *options* are available:

* **``CIMAX``\ =\ *value*** ``CIMAX`` is the maximum excitation level (maximum sum of quantum numbers) of configurations within the correlation space corresponding to ``CITYPE`` and ``LEVEX``. In principle, a triple configuration :math:`(1^42^43^4)` would contribute to the VCI space. However, ``CIMAX=7`` restricts this to :math:`(1^42^3)`, :math:`(1^32^33^1)`, :math:`(1^32^23^2), ...`. The default is ``CIMAX=12`` for 3D potentials and ``CIMAX=15`` for 4D potentials.
* **``CITYPE``\ =\ *n*** ``CITYPE`` defines the maximum number of simultaneous excitations with respect to the different modes, i.e. Singles, Doubles, Triples, ... and thus determines the kind of calculations, i.e. VCISD, VCISDT, ... The default is ``CITYPE=4`` (VCISDTQ) for 3D potentials and ``CITYPE=5`` for 4D potentials, which appears to be a fair compromise between accuracy and computational speed. The maximum excitation level is currently limited to ``CITYPE=9``.
* **``CLCTYPE``\ =\ *n*** (=2 Default) All VCI programs are based on a real configuration basis. If the state of interest is specified by the :math:`l` quantum number (symmetric top or linear molecules) an appropriate start vector for the iterative eigenvalue solver will be generated automatically. The option ``CLCTYPE`` allows to use different start vectors.
* **``CONT``\ =\ *n*** Within the evaluation of the VCI integrals contraction schemes are used to reduce the computational effort. In the analytical VCI program values 0, 1 and 2 are supported. Memory demands and CPU speed-ups increase with increasing values. The default is set to 2, but will be reduced in dependence on the available memory.
* **``DIAG``\ =\ *n*** In the configuration selective VCI program different diagonalization schemes can be used. ``DIAG``\ =\ ``TRS`` uses our residual-based algorithm for the calculation of eigenpairs (RACE), which is the default. Once ``MULTIVCI`` has been switched off, also ``DIAG=CON``, ``DIAG=JAC`` and ``DIAG=HJD`` can be used. ``DIAG``\ =\ ``CON`` specifies a conventional non-iterative diagonalization as used. ``DIAG``\ =\ ``JAC`` uses a Jacobi-Davidson scheme and ``DIAG``\ =\ ``HJD`` denotes a disk-based Jacobi-Davidson algorithm.
* **``EXPORT``\ =\ *variable*** If *variable* is set to ``FCON``, important VCI information will be passed to the Franck-Condon calculation. Within Franck-Condon calculations this option *has to be* used.
* **``GSMODALS``\ =\ *n*** By default all VCI calculations will employ ground-state based VSCF modals, ``GSMODALS=1``. ``GSMODALS=0`` uses the state-specific VSCF modals the subsequent VCI calculations. In any case, individual VCI calculations will be performed for each vibrational state (in contrast to just one VCI calculations from which all solutions will be retrieved) and thus the final VCI wave functions may not be strictly orthogonal to each other once the VCI space is incomplete.
* **``INFO``\ =\ *n*** ``INFO=1`` provides a list of the values of all relevant program parameters (options).
* **``LEVEX``\ =\ *n*** ``LEVEX`` determines the level of excitation within one mode, i.e. :math:`0\rightarrow 1`, :math:`0\rightarrow 2`, :math:`0\rightarrow 3`, ... The default is ``LEVEX=5``, which was found to be sufficient for many applications.
* **``POT``\ =\ *variable*** VCI solutions can be obtained using a potential in grid representation, i.e. ``POT=GRID`` (default), or in an analytical representation, ``POT=POLY``, ``POT=GAUSS`` or ``POT=BSPLINE``. In the latter cases the ``POLY`` program needs to be called prior to the ``VSCF`` and ``VCI`` programs in order to transform the potential.
* **``MPG``\ =\ *n*** By default the symmetry of the molecule will be recognized automatically within the ``VCI`` calculations. ``MPG=1`` switches symmetry off.
* **``MULTIVCI``\ =\ *n*** (=0 Default) ``MULTIVCI=1`` calls a multi-state VCI, which allows for the simultaneous calculation of several vibrational states, which is particularly useful in case of resonances. See also the option ``NSTSEL``. Besides this the multi-state VCI program in connected with advanced features for the state assignment.
* **``NDIM``\ =\ *n*** The expansion of the potential in the ``VCI`` calculation can differ from the expansion in the ``XSURF`` calculation. However, only values less or equal to the one used in the surface calculation can be used. Default: ``NDIM=3``.
* **``NDIMDIP``\ =\ *n*** Term after which the :math:`n`-body expansions of the dipole surfaces are truncated. The default is set to 3. Note that ``NDIMDIP`` has to be lower or equal to ``NDIM``.
* **``NDIMPOL``\ =\ *n*** Term after which the :math:`n`-body expansions of the polarizability tensor surfaces are truncated. The default is set to 0. Note that ``NDIMPOL`` has to be lower or equal to ``NDIM``.
* **``NDIMQUAD``\ =\ *n*** Term after which the :math:`n`-body expansions of the quadrupole tensor surfaces are truncated. The default is set to 0. Note that ``NDIMQUAD`` has to be lower or equal to ``NDIM``.
* **``NSTSEL``\ =\ *n*** (=0 (off) Default) Once switched on (``NSTSEL=1``) the configuration selection procedure acts on several states simultaneously. The number and identity of these states will be automatically determined. Be aware, that this option leads to a significant increase of CPU time due to enlarged correlation spaces.
* **``PRINT``\ =\ *n*** This option provides an extended output. ``PRINT=1`` prints the vibrationally averaged rotational constants for all computed states and the associated vibration-rotation constants :math:`\alpha`. ``PRINT=2`` prints the effective 1D polynomials in case that the potential is represented in terms of polynomials, see the option ``POT=POLY`` and the ``POLY`` program. In addition the generalized VSCF property integrals, i.e. :math:`\left < VSCF \left | q_i^r \right | VSCF \right >` are printed. These integrals allow for the calculation of arbitrary vibrationally averaged properties once the property surfaces are available. Default: ``PRINT=0``.
* **``REFERENCE``\ =\ *n*** This keyword specifies the reference for the definition of the configurations. By default, ``REFERENCE=0`` the reference for all state-specific calculations is the vibrational ground-state configuration. This leads to a violation of the Brillouin condition, but often to also to faster convergence. ``REFERENCE=1`` uses the VSCF configuration as reference for generating all excited configurations. This is the proper way of doing it, but usually requests higher excitation levels.

<!--

* **``SADDLE``\ =\ *n*** By default, i.e. ``SADDLE=0``, the ``VCI`` program assumes, that the reference point of the potential belongs to a local minimum. Once the PES calculation has been started from a transition state, this information must be provided to the ``VCI`` program by using ``SADDLE=1``. Currently, the ``VCI`` program can only handle symmetrical double-minimum potentials. -->
* **``SELSCHEME``\ =\ *n*** By default ``SELSCHEME``\ =1, configurations will be selected by a perturbative criterion. Alternative one may use a criterion based on 2\ :math:`\times`\ 2 VCI matrices (``SELSCHEME``\ =2). Usually the differences are extremely small and the matrix based criterion is slightly more time-consuming.
* **``SKIPDIAG``\ =\ *n*** If ``SKIPDIAG=//n//`` with *n*>1 is set (default: 2), the configuration selection based on a VMP2-like wavefunction is used after the *n*\ th iteration step, as long as the energy difference between the energy eigenvalues of the last  two iteration steps is less than ``THRDIAG`` (see below). ``SKIPDIAG=2`` usually leads to appropriate results.
* **``SKIPSAVE``\ =\ *n*** In cases of small deviations with respect to the norm of the VMP2-like wavefunction, ``SKIPSAVE=1`` may be used to further reduce the computational cost for configuration selection. Note, that renormalization is not possible anymore in this case. The default is ``SKIPSAVE=0`` (disabled).
* **``SUBSPACE``\ =\ *n*** ``SUBSPACE=1``, which is the default, enables the use of prediagonalization of physically meaningful subspaces.
* **``THERMO``\ =\ *n*** ``THERMO=1`` allows for the improved calculation of thermodynamical quantities (compare the ``THERMO`` keyword in combination with a harmonic frequency calculation). However, the approach used here is an approximation: While the harmonic approximation is still retained in the equation for the partition functions, the actual values of the frequencies entering into these functions are the anharmonic values derived from the ``VCI`` calculation. Default: ``THERMO=0``.
* **``THRCF``\ =\ *value*** ``THRCF`` is the threshold for selecting individual configurations. The default is given by ``THRCF``\ =\ :math:`5\cdot 10^{-10}`.
* **``THRDIAG``\ =\ *value*** The default is ``THRDIAG=1.0d0`` (wavenumbers). ``THRDIAG`` refers to the energy difference between the energy eigenvalues of two consecutive iterations. The VMP2-like wavefunction is employed for configuration selection if the respective energy difference is smaller than ``THRDIAG``, i.e. VCI matrix diagonalizations/eigenvector determinations are omitted.
* **``THRECORR``\ =\ *value*** Convergence criterion in the case the VMP2-like wavefunction is used for configuration selection. If the sum of energy corrections given by the configurations selected in a specific iteration step is smaller than ``THRECORR``, the final VCI matrix is set-up and the eigenvector is determined. The default is ``THRECORR=1.0d0`` (wavenumbers).
* **``THRSEL``\ =\ *value*** ``THRSEL`` controls the determination of the iterative configuration selection scheme. By default the wavefunction is considered to be converged once energy changes drop below ``THRSEL``\ =0.02 cm\ :math:`^{-1}`.
* **``THRUP``\ =\ *value*** Within the perturbative selection criterion, unselected configurations are excluded from the procedure based on a criterion, which checks on the selection of configuration, which are excited in the same modes. The default is ``THRUP``\ =\ :math:`10^{-9}`.
* **``VAM``\ =\ *n*** ``VAM=0``: switches off all vibrational angular momentum terms and the Watson correction term.

  * ``VAM=1``: adds the Watson correction term as a pseudo-potential like contribution to the fine grid of the potential. In the analytical representation of the potential this will already be done in the ``POLY`` program.
  * ``VAM=2``: the 0D terms of the vibrational angular momentum terms, i.e. :math:`\frac{1}{2} \sum_{\alpha\beta} \hat{\pi}_\alpha\mu_{\alpha\beta} \hat{\pi}_\beta`, and the Watson correction term are included. The VAM-terms will be added to the diagonal elements of the VCI-matrix only. This approximations works rather well for many applications.
  * ``VAM=3``: (default) the :math:`\mu` tensor is given as the inverse of the moment of inertia tensor at equilibrium geometry, i.e. the 0th order term of the :math:`\mu`-tensor expansion, but it is added to all elements of the VCI matrix.
  * ``VAM=4``: extends the constant :math:`\mu`-tensor (0D) by 1D terms. The 1D VAM-terms will be added to the diagonal elements of the VCI-matrix only. 
  * ``VAM=5``: includes 0D and 1D :math:`\mu`-tensor, which are added to all elements of the VCI matrix. Prescreening is used for the 1D terms.
  * ``VAM=6``: includes 0D and 1D terms of the :math:`\mu`-tensor without prescreening.
  * ``VAM=7``: includes 0D, 1D and 2D terms of the :math:`\mu`-tensor, which are added to all elements of the VCI matrix. Prescreening is used for the 2D terms only.
  * ``VAM=8``: includes 0D, 1D and 2D terms of the :math:`\mu`-tensor without any prescreening. Note that the 1D and 2D corrections increase the computational cost considerably and are only available for non-linear molecules.
* **``VERSION``\ =\ *n*** The ``VCI`` program offers 2 different kinds of ``VCI`` implementations: ``VERSION=1`` (which is the default) is a configuration selective and most efficient ``VCI`` program. ``VERSION=2`` is a conventional ``VCI`` program without configuration selection and is operative only in combination with ``MULTIVCI=0``. This version is thus computationally extremely demanding.

.. _vibration_correlation_programs--rovibrational-rvci-calculations:

Rovibrational (RVCI) calculations
=================================

``ROVIB,options``

By default, the ``VCI`` program calculates purely vibrational states only. However, the ``ROVIB`` directive allows for the calculation of rovibrational transitions for molecules with Abelian point groups. This includes also the IR intensities once dipole moment surfaces have been computed and Raman intensities if they are available and requested in the vibrational calculation. For details see:

S. Erfort, M. Tschoepe, G. Rauhut, *Towards a fully automated calculation of rovibrational infrared intensities for semi-rigid polyatomic molecules*, J. Chem. Phys. **152**, 244104 (2020).
S. Erfort, M. Tschoepe, G. Rauhut, *Efficient and automated quantum chemical calculation of rovibrational nonresonant Raman spectra.*, J. Chem. Phys. **156**, 124102 (2022).
D.F. Dinu, M. Tschoepe, B. Schroeder, K.R. Liedl, G. Rauhut, *Determination of spectroscopic constants from rovibrational configuration interaction calculations.*, J. Chem. Phys. **157**, 154107 (2022).

The following *options* are available:

* **``DUMP_EN``\ =\ *string*** File name for dumping the rovibrational state list.
* **``DUMP_IR``\ =\ *string*** File name for dumping the rovibrational infrared line list. Activates calculation of rovibrational intensities.
* **``DUMP_PFIT``\ =\ *string*** File name for dumping the term energies for the fitted spectroscopic parameters.
* **``DUMP_QUAD``\ =\ *string*** File name for dumping the line list for quadrupole transitions. Activates calculation of rovibrational intensities.
* **``DUMP_RAMAN``\ =\ *string*** File name for dumping the rovibrational Raman line list. Activates calculation of rovibrational intensities.
* **``HOTB``\ =\ *n*** (=0 (off) Default) The calculation of vibrational hot bands can be switched on with ``HOTB=1``.
* **``INFO``\ =\ *n*** (=1 Default) Additional rovibrational output. By default this will print the nuclear spin statistical weights. ``INFO=2`` provides additional details on the calculation and assignment of nuclear spin statistical weights. ``INFO=3`` enables further integrals, etc.
* **``IRUNIT``\ =\ *string*** The default unit for the IR intensities in HITRAN units, i.e. cm\ :math:`^{-1}`/(molecule cm\ :math:`^{-2}`). Alternatively, one may use ``IRUNIT=KMMOL`` to specify km/mol.
* **``JMAX``\ =\ *n*** By default VCI calculations will be performed for non-rotating molecules, i.e. ``J=0``. Rovibrational levels can be computed for arbitrary numbers of ``J$=n$``. This keyword is not mandatory as a default for ``JMAX`` will be determined from the partition function.
* **``JMAX_PRINT``\ =\ *n*** (=3 Default for ``JMAX``>3) This option controls the printout in rovibrational calculations, i.e. the maximum J value, up to which information shall be printed.
* **``LLPRINT``\ =\ *n*** This keyword controls the rovibrational line list printout. ``LLPRINT=1`` prints the transition moments, ``LLPRINT=2`` symmetry information, ``LLPRINT=3`` the Einstein A coefficients, ``LLPRINT=4`` the oscillator strength, and ``LLPRINT=5`` vibrational hot bands. Any of these numbers can be combined, e.g. ``LLPRINT=123`` prints the transition moments, symmetry information and the Einstein A coefficients. This keyword or the ``DUMP_IR`` and/or ``DUMP_RAMAN`` keyword have to be set in order to compute rovibrational intensities.
* **``NDIMCOR``\ =\ *n*** (=2) Order of the :math:`\mu`-tensor expansion within Coriolis coupling terms. ``NDIMCOR=0`` denotes no Coriolis coupling. ``NDIMCOR=1`` considers 0th order terms, ``NDIMCOR=2`` uses 1st order term, ``NDIMCOR=3`` is the highest implemented value and uses 2nd order terms.
* **``NDIMDIP``\ =\ *n*** (Default is identical to preceding VCI calculation) Order of the :math:`n`-mode expansion of the dipole surfaces used for the calculation of the vibrational transition moments in rovibrational intensities.
* **``NDIMPOL``\ =\ *n*** (Default is identical to preceding VCI calculation) Order of the :math:`n`-mode expansion of the polarizability surfaces used for the calculation of the vibrational transition moments in rovibrational intensities.
* **``NDIMQUAD``\ =\ *n*** (Default is identical to preceding VCI calculation) Order of the :math:`n`-mode expansion of the quadrupole surfaces used for the calculation of the vibrational transition moments in rovibrational intensities.
* **``NDIMROT``\ =\ *n*** (=3) Order of the :math:`\mu`-tensor expansion within rotational terms. ``NDIMROT=1`` considers 0th order terms, ``NDIMROT=2`` uses 1st order terms up to ``NDIMROT=4`` for 3rd order terms.
* **``NSSW``\ =\ *'i-j-k...'*** The nuclear spin statistical weights will be determined automatically. However, the can also be provided explicitly by this keyword. The number of NSSWs must match the number of irreps and the different NSSWs need to be separated by minus signs.
* **``PARTF``\ =\ *0,1,2*** (= 1 Default) Mode rovibrational partition function. If equals ``0``, then partition function gets not calculated. For ``PARTF=1`` partition function is calculated with separation approximation and for ``PARTF=2`` only all RVCI energies are used.
* **``PFIT``\ =\ *value*** (=0 Default) Fitting of spectroscopic parameters for asymmetric tops using Watson's reduced operator. ``PFIT=1`` activates the fitting procedure if ``JMAX>0``. IR Intensities are not needed for the fitting! By setting ``PFIT=2`` additional printout of the optimization algorithm is provided.
* **``PFITCUT``\ =\ *0,1*** (=0 Default) By default, the whole reference data set is used by PFIT. Setting this keyword to (1) will activate a filter that cuts data points with a high residuum from the data set and improves overall convergence slightly.
* **``PFITLIN``\ =//0/1//** (=0 Default) Choose whether state energies (0) or transition frequencies (1) should be used as reference data for fitting.
* **``PFITORD``\ =//2/4/6//** (=6 Default) Select between quadratic, quartic, and sextic expansion of the Watson operator.
* **``PFITQNC``\ =\ *value*** (=0.999d0 Default) By default, RVCI states with a quantum number assignment confidence below 0.999d0 are not considered in the reference data used by PFIT. Be aware that by changing this value, the fitting results can either improve or deteriorate!
* **``PFITRED``\ =//A/S//** (=A Default) Select between A- and S-reduction of the Watson operator.
* **``PFITREF``\ =\ *value*** (=0 Default) By default, the spectroscopic parameters are fitted with respect to the vibrational ground state. The fitting can be performed for vibrationally excited states, too. Be aware, that Watson's reduced operator may not be appropriate for resonant vibrational states!
* **``RBAS``\ =\ *n*** (=5 Default) Definition of the rotational basis in rovibrational calculations.

  * ``RBAS=1`` refers to a primitive symmetric top basis :math:`|Jk>`.
  * ``RBAS=2`` a symmetrized rotational basis by employing Wang combinations is used, i.e. :math:`|J K \tau> = i^\sigma/\sqrt{2} (|JK> + (-1)^{J+K+\tau}|J-K>)`.
  * ``RBAS=3`` refers to a molecule specific rotational basis (MSRB) obtained from a linear combination of primitive symmetric top functions.
  * ``RBAS=4`` uses a molecule specific rotational basis (MSRB) generated from a linear combination of Wang combinations.
  * ``RBAS=5`` symmetrized Wang combinations are used, i.e. :math:`|J K \tau> = i^\tau(-1)^\sigma/\sqrt{2} (|JK> + (-1)^{J+K+\tau}|J-K>)`, which results in a real-valued RVCI matrix, while all other bases lead to a complex RVCI matrix.
* **``RAMAN_POLANG``\ =\ *value*** (=90 Default) Raman polarization angle defining the prefactors mixing the isotropic and anisotropic Raman transition moments for the calculation of Raman intensities.
* **``RAMAN_FAC(n)``\ =\ *value*** Set the prefactors for the isotropic and anisotropic Raman transition moments for the calculation of Raman intensities manually. :math:`n=0` will set the value for :math:`R_0`, :math:`n=2` the one for :math:`R_2`.
* **``RAMAN_LFREQ``\ =\ *value*** (=680 Default, in nm) Raman exciting radiation (laser) frequency.
* **``SPARSITY``\ =\ *0,1*** (=1 (on) Default) allows to use sparsity within the storage of the RVCI eigenvectors, which also accelerates the calculation of the infrared intensities.
* **``SYM``\ =\ *0,1*** (=1 (on) Default) Abelian point group symmetry is exploited within the construction of the RVCI matrix.
* **``TEMP``\ =\ *value*** (=300 Default, in Kelvin) Spectra for a given temperature can be calculated using the temperature dependent thermal occupation prefactor and the corresponding partition function value.
* **``THRHOTB``\ =\ *n*** (=5d-2 Default) Minimum of the relative thermal occupation for the lower vibrational mode, in order to be considered as a hot band.
* **``THRROTPF``\ =\ *value*** (=\ :math:`10^{-4}` Default) Threshold for the relative deviation within the iterative determination of the rotational partition function.
* **``THRRVINT``\ =\ *value*** (=10\ :math:`^{-6}` Default) Threshold for printing rovibrational lines relative to the intensity of the strongest line.
* **``THRSPARS``\ =\ *n*** (=5 Default) general sparsity threshold for RVCI eigenvectors. :math:`n` refers to the actual threshold of :math:`10^{-n}/(J+1)` with :math:`J` being the rotational quantum number.
* **``THRVIBPF``\ =\ *value*** (=\ :math:`10^{-4}` Default) Threshold for the relative deviation within the iterative determination of the vibrational partition function.

.. _vibration_correlation_programs--explicit-definition-of-the-correlation-space:

Explicit definition of the correlation space
============================================

``LEVEX,options\\``
Within the VCI program the correlation space can be specified in a general manner (keyword ``LEVEX``), which means that the same number of modals for each mode will be used. Alternatively, one may use the ``LEVEX`` directive. This allows to specify the correlation spaces for the individual modes.

* **``MODE(n)``\ =\ *m*** The number of correlating modals for mode *n* is set to *m*.

.. _vibration_correlation_programs--examples:

Examples
========

The following input example for a grid based calculation of anharmonic frequencies and intensities (1) optimizes the geometry of water, (2) computes the harmonic frequencies, (3) generates a potential energy surface around the equilibrium structure, (4) computes the vibrational wave function and the infrared intensities at the ``VSCF`` level, and finally (5) a ``VCI`` calculation will be performed. Vibrational angular momentum terms (``VAM``) are included even for the non-diagonal elements of the VCI matrix.

.. code-block:: text

   memory,20,m
   basis=vdz
   orient,mass
   geometry={
      3
   Water
   O          0.0675762564        0.0000000000       -1.3259214590
   H         -0.4362118830       -0.7612267436       -1.7014971211
   H         -0.4362118830        0.7612267436       -1.7014971211
   }
   
   mass,iso
   
   hf
   mp2
   optg                                     !(1) optimizes the geometry
   frequencies,symm=auto                    !(2) compute harmonic frequencies
   
   label1
   int
   {hf
   start,atden}
   {mp2
   cphf,1}
   
   {xsurf,sym=auto                          !(3) generate potential energy surface
    intensity,dipole=2}
   poly
   vscf,pot=poly                            !(4) do a VSCF calculation
   vci,pot=poly,vam=3                       !(5) do a VCI calculation
   put,irspec,irspec.gnu                    !writes a gnuplot file to plot an IR
                                            !spectrum of the last VCI calculation

The following input example for an analytical calculation of anharmonic frequencies and intensities (1) optimizes the geometry of water, (2) computes the harmonic frequencies,(3) generates a potential energy surface around the equilibrium structure, (4) converts the potential energy surface into an analytical representation (5) computes the nuclear wave function and the infrared intensities at the ``VSCF`` level, and finally (6) performs a ``VCI`` calculation. Vibrational angular momentum terms (``VAM``) are included even for the non-diagonal elements of the VCI matrix.

.. code-block:: text

   memory,20,m
   basis=vdz
   orient,mass
   geometry={
      3
   Water
   O          0.0675762564        0.0000000000       -1.3259214590
   H         -0.4362118830       -0.7612267436       -1.7014971211
   H         -0.4362118830        0.7612267436       -1.7014971211
   }
   
   mass,iso
   
   hf
   mp2
   optg                                     !(1) optimizes the geometry
   frequencies,symm=auto                    !(2) compute harmonic frequencies
   
   label1
   int
   {hf
   start,atden}
   {mp2
   cphf,1}
   
   {xsurf,sym=auto                          !(3) generate potential energy surface
    intensity,dipole=2}
   poly,dipole=1                            !(4) converts potential energy surface
                                            !    to a polynomial representation
   vscf,pot=poly                            !(5) do a VSCF calculation
   vci,pot=poly,vam=3                       !(6) do a VCI calculation
   put,irspec,irspec.gnu                    !writes a gnuplot file to plot an IR
                                            !spectrum of the last VCI calculation

.. _vibration_correlation_programs--record-handling:

Record handling
===============

``DISK,options``

The ``DISK`` directive allows to specify explicitly, from where the potential information shall be taken and where it shall be stored to disk. This can also be accomplished in an automated manner. These features are only relevant for the simulation of vibronic spectra as one has to deal with several PESs in the same input. For simple VCI calculations, no information is needed here.

The following *options* are available:

* **``AUTO``\ =\ *n*** Rather than using the options ``START`` and ``SAVE`` one may simply assign a label *n* to a a certain PES and all the records will be set automatically.
* **``SAVE``\ =\ *record*** This keyword specifies the record where to dump the VCI information.
* **``START``\ =\ *record*** This card specifies the record from where to read the VSCF information. As the VSCF information usually is stored in the same record as the polynomials, it is usually defined in the ``POLY`` program.

.. _vibration_correlation_programs--the-vibrational-m-ller-plesset-programs-vmp2-vmp3-vmp4:

The vibrational Møller-Plesset programs (VMP2, VMP3, VMP4)
----------------------------------------------------------

``VMPx,options``

The ``VMPx`` (x=2,3,4) programs allow to perform 2nd to 4th order vibrational Møller-Plesset calculations. 3rd and 4th order perturbation theory is only available for polynomial based PESs. Any properties (except energies) will always be computed at the level of VMP2. Most of the keywords as described for the ``VCI`` program are also valid for these perturbational programs, i.e. ``CITYPE, LEVEX, CIMAX, NDIM, VAM, MPG`` and ``INFO``.

The following *additional options* are available:

* **``QDEG``\ =\ *n*** (=0 default) Quasi-degenerate VMP2 theory (QDVMP2) can be called by ``QDEG=1`` for polynomial based PESs.

.. code-block:: text

   basis=vdz
   orient,mass
   geomtyp=xyz
   geometry={
      3
   Water
   O          0.0675762564        0.0000000000       -1.3259214590
   H         -0.4362118830       -0.7612267436       -1.7014971211
   H         -0.4362118830        0.7612267436       -1.7014971211
   }
   
   hf
   mp2
   optg
   frequencies,symm=auto
   
   label1
   {hf
    start,atden}
   {mp2
    cphf,1}
   
   {xsurf,sym=auto
    intensity,dipole=2}
   poly,show=1
   vscf,pot=poly
   vmp2,pot=poly
