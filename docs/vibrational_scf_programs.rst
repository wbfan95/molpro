.. raw:: html

   <span id="the-vibstate-program-vibstate"></span>

.. raw:: html

   <span id="the-vmcscf-program-vmcscf"></span>

.. raw:: html

   <span id="the-vscf-program-vscf"></span>

.. _vibrational_scf_programs--the-vscf-programs-vscf:

The VSCF programs (VSCF)
========================

``VSCF,options [vscf]``

The ``VSCF`` program is exclusively based on the Watson Hamiltonian
\begin{align}
\hat{H} = \frac{1}{2} \sum_{\alpha\beta} ( \hat{J}_\alpha - \hat{\pi}_\alpha) \mu_{\alpha\beta}
(\hat{J}_\beta - \hat{\pi}_\beta)
-\frac{1}{8}\sum_\alpha \mu_{\alpha\alpha} -\frac{1}{2}\sum_i \frac{\partial^2}{\partial q_i^2}  + V(q_1,\dots,q_{3N-6})
\label{eq:1}
\end{align}
in which the potential energy surfaces, :math:`V(q_1,\dots,q_{3N-6})`, are provided by the ``XSURF`` module. The Watson correction term and the 0th order term of the vibrational angular momentum terms are by default (``VAM=2``) included. As VSCF calculations are extremely fast, these calculations cannot be restarted. For details see:

J. Meisner, P.P. Hallmen, J. Kästner, G. Rauhut, *Vibrational analysis of methyl cation - rare gas atom complexes: CH:math:`_3^+`-Rg (Rg=He, Ne, Ar, Kr)*, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.5084100>`__ **150**, 084306 (2019).
G. Rauhut, T. Hrenar, *A Combined Variational and Perturbational Study on the Vibrational Spectrum of P:math:`_2`F:math:`_4`*, Chem. Phys. **346**, 160 (2008).

The following *options* are available:

* **``AVERAGE``\ =\ *n*** (=0 default) By default state-specific VSCF calculations will be performed. ``AVERAGE=1`` allows for configuration averaged VSCF calculations, i.e. CAVSCF. The averaging will be performed for those states being defined by the ``VIBSTATE`` program (see below). The vibrational ground state will always be excluded. An identical weight factor will be used for all states, i.e. the inverse of the number of states.
* **``BASIS``\ =\ *variable*** ``BASIS=DGB`` (default) defines a mode-specific basis of distributed Gaussians and distributes the Gaussians in a way, that the overlap integral between two functions is always the same (controlled by ``THRBASOVLP``). This guarantees that an increasing number of basis functions will always lead to an improvement. ``BASIS=HO`` defines a harmonic oscillator basis. Using this basis together with ``MAXITER=0`` and ``VAM=0`` provides a simple harmonic oscillator basis to be used in all subsequent programs, e.g. in the VCI program.
* **``INFO``\ =\ *n*** ``INFO=1`` provides a list of the values of all relevant program parameters (options).
* **``MAXITER``\ =\ *n*** (=999 default) This key sets the maximum number of iterations to be performed in the VSCF program.
* **``MUPLOT``\ =\ *n*** (=0 default) plots all :math:`\mu`-tensor surfaces up to *n*\ D and a corresponding Gnuplot script in a separate subdirectory (``plots``). This option works only in combination with ``POT=POLY``. The ``VAM`` option has to be set accordingly, i.e. you must at least use ``VAM=4``.
* **``NBAS``\ =\ *n*** The number of basis functions (distributed Gaussians or harmonic oscillator functions) to be used for solving the VSCF equations can be controlled by ``NBAS``\ =\ *n*. The default is ``NBAS=18`` for a basis of distributed Gaussians, while its is ``NBAS=16`` for a harmonic oscillator basis. This option is only active once an analytical representation of the potential has been chosen, see the option ``POT`` and the ``POLY`` program.
* **``NDIM``\ =\ *n*** (=3 default) The expansion order of the potential in the ``VSCF`` calculation can differ from the expansion order in the ``XSURF`` calculation. However, only values less or equal to the one used in the surface calculation can be used.
* **``NDIMDIP``\ =\ *n*** Term after which the :math:`n`-body expansions of the dipole surfaces shall be truncated. The default is set to 3. Note that ``NDIMDIP`` has to be lower or equal to ``NDIM``.
* **``NDIMPOL``\ =\ *n*** Term after which the :math:`n`-body expansions of the polarizability tensor surfaces are truncated. The default is set to 0. Note that ``NDIMPOL`` has to be lower or equal to ``NDIM``.
* **``NDIMQUAD``\ =\ *n*** Term after which the :math:`n`-body expansions of the quadrupole tensor surfaces are truncated. The default is set to 0. Note that ``NDIMQUAD`` has to be lower or equal to ``NDIM``.
* **``ORTHO``\ =\ *n*** Determines the type of orthogonalization within the VSCF program. ``ORTHO=1`` invokes a symmetrical orthogonalization, ``ORTHO=2`` a canonical one and ``ORTHO=3`` uses a canonical one together with an elimination of linear dependencies (see also keyword ``THRLINDEP``. The default is ``ORTHO=1``.
* **``POT``\ =\ *variable*** (=\ ``GRID`` default) VSCF solutions can be obtained using a potential in grid representation, i.e. ``POT=GRID``, or in an analytical representation, ``POT=POLY``, ``POT=BSPLINE``, ``POT=GAUSS``. In the latter cases the ``POLY`` program needs to be called prior to the ``VSCF`` program in order to transform the potential.
* **``PRINT``\ =\ *n*** (=0 default) This option provides an extended output. ``PRINT=1`` prints the vibrationally averaged rotational constants for all computed states and the associated vibration-rotation constants :math:`\alpha`. Moreover, the temperature dependence of bond lengths will also be printed, when the potential is represented by a linear combination of basis functions. ``PRINT=2`` prints the effective 1D polynomials in case that the potential is represented in terms of polynomials, see the option ``POT=POLY`` and the ``POLY`` program. In addition the generalized VSCF property integrals, i.e. :math:`\left < VSCF \left | q_i^r \right | VSCF \right >` are printed. These integrals allow for the calculation of arbitrary vibrationally averaged properties once the property surfaces are available. Default: ``PRINT=0``.

/\*  \* **``SADDLE``\ =\ *n*** By default, i.e. ``SADDLE=0``, the ``VSCF`` program assumes, that the reference point of the potential belongs to a local minimum. Once the PES calculation has been started from a transition state, this information must be provided to the ``VSCF`` program by using ``SADDLE=1``. Currently, the ``VSCF`` program can only handle symmetrical double-minimum potentials. \*/

* **``SOLVER``\ =\ *n*** For solving the one-dimensional Schrödinger equation within a grid representation two different algorithms can be used. The default, i.e. ``SOLVER=1``, calls the discrete variable representation (DVR) as proposed by Hamilton and Light. Alternatively, the collocation algorithm of Young and Peet can be used (``SOLVER=2``).
* **``THERMO``\ =\ *n*** ``THERMO=1`` allows for the improved calculation of thermodynamical quantities (compare the ``THERMO`` keyword in combination with a harmonic frequency calculation). However, the approach used here is an approximation: While the harmonic approximation is still retained in the equation for the partition functions, the actual values of the frequencies entering into these functions are the anharmonic values derived from the ``VSCF`` calculation. Default: ``THERMO=0``.
* **``THRBASOVLP``\ =\ *value*** Overlap between two Gaussian basis functions, once ``BASIS=DGB`` has been chosen. The default is 0.75.
* **``THRLINDEP``\ =\ *value*** Threshold for eliminating linear dependencies in the VSCF procedure (see keyword ``BASIS=DGB``). The default is ``THRLINDEP=1e-8``.
* **``VAM``\ =\ *n*** The 0D terms of the vibrational angular momentum terms, i.e. :math:`\frac{1}{2} \sum_{\alpha\beta} \hat{\pi}_\alpha\mu_{\alpha\beta} \hat{\pi}_\beta`, and the Watson correction term are by default (``VAM=2``) included.

  * ``VAM=1`` adds the Watson correction term (see Eq. \eqref{eq:1}) as a pseudo-potential like contribution to the fine grid of the potential (grid version only). Once an analytical representation of the potential is used, the consideration of the Watson correction term is controlled in the ``POLY`` program.
  * ``VAM=2`` accounts for the 0th order terms of an n-mode expansion of the :math:`\mu`-tensor within the VSCF iterations.
  * ``VAM=3`` does not include any VAM terms in the VSCF iterations, but instead accounts for them in the VMP1 energy correction.
  * ``VAM=4`` truncates the expansion of the effective moment of inertia tensor after the 1D terms (rather than the 0D term in case of ``VAM=2`` or ``VAM=3``). These terms are only included in the VMP1 energy correction. Note that values higher than 2 are only active for non-linear molecules.
  * ``VAM=5`` truncates the series after the 2D term. In almost all cases ``VAM=2`` is fully sufficient. Vibrational angular momentum terms are accounted for in a perturbational manner and do not affect the wavefunction.
* **``WFPRINT``\ =\ *n*** (=0 default) This key allows for the printing of the effective potentials and of the *n* lowest modals. The corresponding gnuplot files will be dumped into the directory plotwf.

The following input example for a polynomial based calculation of anharmonic frequencies and intensities at the ``VSCF`` level (1) optimizes the geometry of water, (2) computes the harmonic frequencies,(3) generates a potential energy surface around the equilibrium structure, (4) transforms the grid points to polynomials and (5) computes the nuclear wave function and the infrared intensities at the ``VSCF`` level. Vibrational angular momentum terms (``VAM``) are included. Note, that it is recommended to perform a ``VCI`` calculation after a ``VSCF`` calculation. The details of the ``VCI`` input are described in the next chapter `the VCI program (VCI) <vibration_correlation_programs.html#the-vci-program-vci>`__.

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
   {hf
   start,atden}
   {mp2
   cphf,1}
   
   {xsurf,sym=auto                          !(3) generate potential energy surface
    intensity,dipole=2}
   poly                                     !(4) transform to polynomials
   vscf,pot=poly                            !(5) do a VSCF calculation

<!--

.. _vibrational_scf_programs--internal-coordinates:

Internal Coordinates
====================

!ONLY IN BETA!!!!!!! It is not advisable to use it that way, it is only the first draft(Also the code :D )!!!
``INTC,options``
The ``INTC`` directive allows the VSCF/VCI calculation in internal coordinates.

.. _vibrational_scf_programs--options:

Options
=======

* **``DIAGVSCF``\ =\ *n*''** If :math:`n=1` (Default), only the diagonal G-Matrix will be used in the VSCF calculation
* **``TDIAG``\ =\ *n*''** :math:`n` equals the dimension of the multimode expansion of the diagonal elements of the G-matrix
* **``TOFFDIAG``\ =\ *n*''** :math:`n` equals the dimension of the multimode expansion of the off-diagonal elements of the G-matrix
* **``DERIVG``\ =\ *n*''** :math:`n` equals the dimension of the multimode expansion of the derivative of the G-matrix
* **``PSEUDOPOT``\ =\ *n*''** :math:`n` equals the dimension of the multimode expansion of the pseudopotential
* **``LEVEX``\ =\ *n*\ ``**, **``\ CITYPE\ ``=//n//``**, **``CIMAX``\ =\ *n*''** compare to VCI, Cleanup necessary
* **``EIGVAL``\ =\ *n*''** only computes the :math:`n` lowest eigenvalues of the VCI matrix, default is 20.
* **``SYM``\ =\ *n*''** :math:`n=0`: No symmetry at all, :math:`n=1`: Sorts according to symmetry in VCI-Matrix and prints the full matrix (DEBUGGING, Only when all coordinates are symmetric), :math:`n=2`: uses symmetry blocking of the VCI matrix (Only when all coordinates are symmetric)
* **``CONT``\ =\ *n*''** If :math:`n=0`, no VCI calculation will be done, with :math:`n=1`\ (Default) a VCI calculation is done.

-->

.. _vibrational_scf_programs--record-handling:

Record handling
---------------

``DISK,options``

The ``DISK`` directive allows to specify explicitly, from where the potential information shall be taken and where it shall be stored to disk. This can also be accomplished in an automated manner. These features are only relevant for the simulation of vibronic spectra as one has to deal with several PESs in the same input. For simple VCI calculations, no information is needed here.

The following *options* are available:

* **``AUTO``\ =\ *n*** Rather than using the options ``START`` and ``SAVE`` one may simply assign a label *n* to a certain PES and all the records will be set automatically.
* **``SAVE``\ =\ *record*** This specifies the record, where to dump the VSCF information. Usually this is the same record as specified in the ``START`` option. Note that the VSCF information is currently stored in the same record as the polynomial information.
* **``START``\ =\ *record*** Polynomial and other information shall be read from the specified record. This must be the same record, to which the polynomials have been dumped in the ``POLY`` program.

.. _vibrational_scf_programs--the-vibstate-program-vibstate:

The VIBSTATE program (VIBSTATE)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``VIBSTATE,options``

The ``VIBSTATE`` program allows to specify the vibrational states to be calculated in the following vibrational SCF and vibration correlation programs. Within the input stream, the ``VIBSTATE`` program needs to be called prior to the first call of the VSCF program. By default, the fundamental modes of the molecule are calculated only. In order to define the list of states to be calculated, the following keywords are available:

* **``COMBI``\ =\ *n*** Choosing ``COMBI``\ =\ *n* allows for the calculation of the vibrational overtones and combination bands. The value of :math:`n` controls the excitation level, i.e. the number of states to be computed increases very rapidly for large values of *n*. Therefore, by default the upper limit is set to 5000 cm\ :math:`^{-1}`, but this cutoff can be changed by the option ``UBOUND``. Note that, ``COMBI=1`` and ``COMBI=2`` generate the same vibrational states.
* **``UBOUND``\ =\ *value*** The upper energy limit for the generated states is controlled by the keyword ``UBOUND``, i.e. states, for which the harmonic estimate is larger than *value*, will not be computed. The default is set to 5000 cm\ :math:`^{-1}`.
* **``LQUANT``\ =\ *n*** (=0 default) If the molecule of interest belongs to a non-Abelian point group, real linear combinations of complex basis functions can be used as startvectors for the VCI calculation by setting ``LQUANT=1``. For symmetric top molecules the default is ``LQUANT=1`` and ``LQUANT=0`` for asymmetric top molecules.  By using this option, also the mapping between real and complex coordinates will be given in the output.
* **``VSTATEONLY``\ = *n*** (=0 default) Once additional vibrational states have been defined by using the ``VSTATE`` directive, the VSCF program can be forced to compute just these states by the option ``VSTATEONLY=1``. Note that the vibrational ground state will always be computed and needs not to be specified explicitly.
* **``IRREP``\ =\ *string*** By setting ``IRREP``\ =\ *string*, only states defined by the keywords ``COMBI``, ``UBOUND``, ``LQUANT`` and userdefined states via the ``VSTATE`` directive with the chosen irreducible representation (irrep) are calculated. Depending on the point group of the molecule, the following irreps are available: A, A`, A``, A1, A1`, A1``, A2, A2`, A2``, Ag, A1g, A2g, Au, A1u, A2u, B, B1, B2, B3, Bg, B1g, B2g, B3g, Bu, B1u, B2u, B3u, E, E`, E``, E1, E1`, E1``, E2, E2`, E2``, Eg, E1g, E2g, Eu, E1u, E2u, T, T1, T2, Tg, T1g, T2g, Tu, T1u, T2u.

.. _vibrational_scf_programs--definition-of-vibrational-states:

Definition of vibrational states
--------------------------------

``VSTATE,options``

By this directive, userdefined vibrational states can be defined. It specifies the occupation number vector of the vibrational state to be calculated. If only those vibrational states shall be computed, which are defined by the ``VSTATE``, ``VSTATEONLY=1`` in the ``VIBSTATE`` program has to be set.

* **``MODE(n)``\ =\ *m*** The :math:`n`\ th mode of the molecule is supposed to have the quantum number *m*. If several modes are excited, the option can be repeated accordingly, e.g. ``VSTATE,MODE(1)=3,MODE(3)=2,MODE(6)=2``. All other modes are not excited and thus have the quantum number 0.
* 
* **``LQUANT(n)``\ =\ *m*** For symmetric top and linear molecules the specification of the quantum number :math:`l` is supported by the keyword ``LQUANT``. With ``LQUANT(n)=l`` the :math:`n`\ th mode is supposed to have the quantum number :math:`l` corresponding to the angular momentum. The occupation number must be set by the keyword ``MODE(n)``. E.g., ``VSTATE,MODE(3)=2,LQUANT(3)=2``. All :math:`l`-quantum numbers not set will have a value of zero. Note that this option can only be used for degenerate mode pairs. The counting of modes in this context belongs to the complex representation.

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
   {hf
   start,atden}
   {mp2
   cphf,1}
   
   {xsurf,sym=auto                          !(3) generate potential energy surface
    intensity,dipole=2}
   {vibstate,vstateonly=1                   !(4) only user defined states shall be computed
    vstate,mode(3)=1}                            the fundamental of mode(3) shall be computed
   poly                                     !(5) transform to polynomials
   vscf,pot=poly                            !(6) do a VSCF calculation

.. _vibrational_scf_programs--exclusion-of-vibrational-states:

Exclusion of vibrational states
-------------------------------

``EXCLUDE,options\\``
By this directive, user defined vibrational states can be excluded from the generated list of states. The state to be skipped is defined via ``MODE`` as described in the context of the directive ``VSTATE``.
