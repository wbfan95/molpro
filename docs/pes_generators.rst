.. raw:: html

   <span id="extended-pes-generator-xsurf"></span>

.. raw:: html

   <span id="potential-energy-surfaces-surf"></span>

.. _pes_generators--pes-generators:

PES generators
==============

.. _pes_generators--potential-energy-surfaces-xsurf:

POTENTIAL ENERGY SURFACES (XSURF)
=================================

``{XSURF,options}``

The ``XSURF`` program allows for the calculation of the potential energy surface around a reference structure as required for the calculation of anharmonic frequencies (see the ``VSCF``, ``VCI`` or ``VPT2`` programs). The reference structure is supposed to be a (local) minimum or a transition state of a double-minimum potential. The potential is represented by energy grid points rather than an analytical representation. Within the ``XSURF`` program the potential energy surface is expanded in terms of normal coordinates, linear combination of normal coordinates or localized normal coordinates. ``XSURF`` can handle :math:`n`-mode and Taylor expansions of the PES of arbitrary order, e.g.
.. math::

   V(q_1,\dots,q_{3N-6}) = \sum_i V_i(q_i) + \sum_{i<j} V_{ij}(q_i,q_j) + \sum_{i<j<k} V_{ijk}(q_i,q_j,q_k) + \dots

with

.. math::

   \begin{eqnarray*}
   V_i(q_i) & = & V_i^0(q_i) - V(0) \\
   V_{ij}(q_i,q_j) & = & V_{ij}^0(q_i,q_j) - \sum_{r\in\{i,j\}} V_r(q_r) - V(0) \\
   V_{ijk}(q_i,q_j,q_k) & = & V_{ijk}^0(q_i,q_j,q_k) - \sum_{\stackrel{\scriptstyle r,s\in\{i,j,k\}}{r>s}} V_{rs}(q_r,q_s) - \sum_{r\in\{i,j,k\}} V_r(q_r) - V(0)\\
   V_{ijkl}(q_i,q_j,q_k,q_l) & = & \dots
   \label{diff4}\end{eqnarray*}

where :math:`q_i` denotes the coordinates. This expansion needs to be terminated after an :math:`n`-body contribution as controlled by the keyword ``NDIM``.
Moreover, it can handle any kind of symmetry, e.g. non-Abelian point groups or permutational symmetry. A harmonic frequency calculation needs to be performed first. This can be done by the ``FREQ`` program or the ``VFREQ`` directive of the ``XSURF`` program. For technical reasons the ``XSURF`` program always requires curly brackets around its call.
The ``XSURF`` program is fully parallelized in a sense that the calculation of different grid points is send to different processors (embarrassingly parallel ``MPPX`` scheme).  For example, the input for the calculation of a CCSD surface looks like:

.. code-block:: text

   label1
   hf
   ccsd
   {xsurf,sym=auto}

As the elongations along different coordinates within the build-up of the PES will lead to different molecular point groups for the individual electronic structure calculations, any symmetry-specific information in that part of the input needs to be avoided. The ``XSURF`` program is based on an iterative algorithm, i.e. grid points will be added automatically to the grid representation of the potential until a convergence threshold will be met. This guarantees a well-balanced description of the different terms in the expansion of the potential and simultaneously minimizes the number of *ab initio* calculations for a representation of the potential. For further details see:

G. Rauhut, *Efficient Calculation of Potential Energy Surfaces for the Generation of Vibrational Wave Functions*, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.1804174>`__ **121**, 9313 (2004).
B. Ziegler, G. Rauhut, *Rigorous use of symmetry within the construction of multidimensional potential energy surfaces*, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.5047912>`__ **149**, 164110 (2018).
B. Ziegler, G. Rauhut, *Localized Normal Coordinates in Accurate Vibrational Structure Calculations: Benchmarks for Small Molecules*, `J. Chem. Theory Comput. <https://dx.doi.org/10.1021/acs.jctc.9b00381>`__ **15**, 4187 (2019)

.. _pes_generators--options:

Options
=======

The following *options* are available:

* **``CORRECT``\ =\ *n*** (=1 (on) Default) If a certain subsurface does not converge despite increasing the number of ab initio calculations, symmetry in this subsurface (if any) will be neglected in order to avoid any errors due to inaccuracies in the displacement vectors and the subsurface will be recalculated accordingly. This option is automatically switched off in any Taylor expansions of the PES.
* **``DELAUTO``\ =\ *variable***\ (=\ *off* Default) If ``DELAUTO``\ =\ *on*, all not converged surfaces of the highest considered dimension are deleted. It only works after a restart from an external file.
* **``INFO``\ =\ *n*** (=1 Default) ``INFO``\ =0 suppresses any information about the program parameters and symmetry information. ``INFO``\ =1 refers to the standard output, while ``INFO``\ =2 provides additional information about the symmetry recognition.
* **``LOWERDIM``\ =\ *n*** (=2 Default) In order to determine energy differences for the subsurfaces, contributions of subsurfaces of lower order need to be subtracted from those of current order. The lower order energy contribution can be determined in three different ways: ``LOWERDIM``\ =1 uses Kronecker product fitting of the lower order terms and ``LOWERDIM``\ =2 retrieves this information from the intermediate fine grid representation of the underlying subsurfaces.
* **``MAXxD``\ =\ *n*** The maximum number of coarse grid points can be controlled by the keywords ``MAX1D, MAX2D, MAX3D, MAX4D``. These 4 keywords determine the maximum number of *ab initio* calculations in one dimension for each 1D, 2D, 3D and 4D surface. The defaults are currently ``MAX1D=14``, ``MAX2D=14``, ``MAX3D=12``, ``MAX4D=10``. Presently, values larger than 24 are not supported.
* **``MINxD``\ =\ *n*** The minimum number of coarse grid points can be controlled by the keywords ``MIN1D, MIN2D, MIN3D, MIN4D``. These 4 keywords determine the minimum number of *ab initio* calculations in one dimension for each 1D, 2D, 3D and 4D surface. The defaults are currently ``MIN1D=4, MIN2D=4, MIN3D=4, MIN4D=4``. Presently, values larger than 24 are not supported.
* **``MINxD_CRIT1``\ =\ *n*** Minimum number of ab initio calculations per dimension, which are needed before a subsurfaces can be declared to be converged according to criterion 1. For dimension 1-3 the default is 6, while it is reduced to 4 for all higher order subsurfaces.
* **``MPG``\ =\ *n*** Symmetry of the normal modes is recognized by the program automatically. Symmetry of the modes will be determined even if the ``NOSYM`` keyword is used in the electronic structure calculations. In certain cases numerical noise can be very high and thus prohibits a correct determination of the symmetry labels. Symmetry can be switched off by using ``MPG=1``.
* **``NDIM``\ =\ *n*** The keyword ``NDIM=n`` terminates the expansion of the PES after the :math:`n`-body term. The default is set to 3. Please note, when you use ``NDIM=4`` as a keyword for the ``XSURF`` program, you need to pass this information to the ``VSCF`` and ``VCI`` programs also. Otherwise these programs will neglect the 4-body terms.
* **``NGRID``\ =\ *n*** Based on a coarse grid of *ab initio* points a fine grid will be generated from automated interpolation techniques. The keyword ``NGRID=n`` determines the number of equidistant grid points in one dimension. ``NGRID=n`` has to be an even number. The default is currently set to 16.
* **``NSA``\ =\ *n*** (=1 Default) This option prints out some information about the progress of the ``XSURF`` calculation. ``NSA``\ =1 prints this information is an additional file, which will be deleted once the ``XSURF`` calculation is completed, ``NSA``\ =2 prints this information to the console.
* **``ONLYHEAD``\ =\ *n*** (=0 (off) Default) If set to 1, the ``XSURF`` calculation will be terminated after writing the header of the external restart file, i.e. prior to the calculation of the 1D terms. The call of any other programs beyond ``XSURF`` will be ignored.
* ``ORIENT`` Allows to specify a certain orientation of the molecule. With ``ORIENT=//yes//`` (Default) the orientation is chosen automatically according to the asymmetric parameter of the molecule. To choose a certain orientation, ``ORIENT=//XC//`` need to be set. X represents a number from 1 to 3 (in arabic or roman letters), and C need to be set to **r** or **l**. For example, ``ORIENT=//IIl//`` orientates the molecule according to the **IIl** convention. ``ORIENT=//old//`` does not rotate the molecule at all.
* **``RDM``\ =\ *n*** (=0 (off) Default) Degenerate modes can be rotated in a manner, that the corresponding 1D potentials will be identical. By default, this feature is switched off, but can be activated by ``RDM``\ =1. Typically this results in rotational angles of 45 or 135 degrees.
* **``RDM_THR``\ =\ *n*** (=1.0d-10 Default) This threshold controls, if the potentials of two degenerate modes are identical or not. See the keyword ``RDM``\ =\ *n*.
* **``SKIP``\ =\ *n*** (=1 (on) Default) By default, (pre)screening of any terms higher than 2D of the PES expansion is switched on. It can be deactivated by ``SKIP``\ =0.
* **``SKIPCRIT``\ =\ *n*** (=1 Default) ``SKIPCRIT`` defines the method and thus the criterion for (pre)screening of the high-order terms of the PES expansion. ``SKIPCRIT``\ =1 activates prescreening and ``SKIPCRIT``\ =2 screening. In the latter case a label must be defined (see ``SKIPLABEL``).
* **``SKIPLAB``\ =\ *variable*** The name of the label in the input stream must be defined, which determines the electronic structure level to be used for screening the high-order terms of a PES expansion.
* **``SKIP_THRx(i)``\ =\ *value*** (:math:`x`\ =1,2 :math:`i`\ =1,2,...) Definition of thresholds used for prescreening (``SKIP_THR1``) and screening ``SKIP_THR2`` (see option ``SKIPCRIT``). :math:`i` specifies the individual orders of the :math:`n`-mode expansion of the PES. The defaults are ``SKIP_THR1(1)``\ =0.0d0, ``SKIP_THR1(2)``\ =0.0d0, ``SKIP_THR1(3)``\ =1.0d-18, ``SKIP_THR1(4)``\ =1.0d-27 and ``SKIP_THR2(1)``\ =0.0d0, ``SKIP_THR2(2)``\ =0.0d0, ``SKIP_THR2(3)``\ =1.0d-2, ``SKIP_THR2(4)``\ =1.0d-1. All other thresholds are not yet defined and need to be entered explicitly.
* **``START1D``\ =\ *label*** (=LABEL1 default) Sets the label to start the calculations for the 1D terms of the potential.
* **``STOP``\ =\ *i*** (=1000 Default) The calculation of an :math:`n`-mode expansion of a PES can be terminated at lower orders, specified by ``STOP``, while all information for the high-order terms is already provided in the header of the external restart file and the potential information once a multi-level scheme has been used.
* **``SYM``\ =\ *variable*** Symmetry within electronic structure calculations can be exploited by the keyword ``SYM=Auto`` (which is the default). Usually this leads to significant time savings. The symmetry recognition can be switched off by ``SYM=NOSYM`` as certain calculations may cause some trouble (e.g. local correlation methods). Symmetry in electronic structure calculations may not be mistaken by the symmetry of the mode-coupling terms (see keyword ``MPG``). Once ``SYM=Auto`` is used, it is advisable to insert an ``INT`` card prior to the call of the Hartree-Fock program.
* **``THRDEGx``\ =\ *value*** (:math:`x`\ =1,2,...) Threshold used for recognizing degeneracies within the individual orders of the PES expansion. The defaults are ``THRDEG1``\ =5.0d-5, ``THRDEG2``\ =1.0d-5,\ ``THRDEG3``\ =5.0d-6,\ ``THRDEG4``\ =1.0d-6.
* **``THRFITx``\ =\ *value*** (:math:`x`\ =1,2,...) Threshold used for testing on convergence of a subsurface according to criterion 1 for the individual orders of the PES expansion. The defaults are ``THRFIT1``\ =2.0d-3, ``THRFIT2``\ =5.0d-3,\ ``THRFIT3``\ =5.0d-3,\ ``THRFIT4``\ =2.0d-2. Criterion 1 controls the convergence of the intermediate fine grid.
* **``THRLOWx``\ =\ *value*** (:math:`x`\ =1,2,...) Threshold used for testing on convergence of a subsurface according to criterion 2 for the individual orders of the PES expansion. The defaults are ``THRLOW1``\ =0.0d0, ``THRLOW2``\ =5.0d-7,\ ``THRLOW3``\ =1.0d-6,\ ``THRLOW4``\ =2.0d-6. Criterion 2 controls the convergence with respect to the ab initio single points.
* **``THRSED``\ =\ *value*** (=1.0d-6 Default) Threshold for determining symmetry elements of the molecule.
* **``THRSYMx``\ =\ *value*** (:math:`x`\ =1,2,...) Threshold used for recognizing symmetry within a subsurface of the PES expansion - in dependence on the order of the expansion term. The defaults are ``THRSYM1``\ =5.0d-5, ``THRSYM2``\ =1.0d-5,\ ``THRSYM3``\ =5.0d-6,\ ``THRSYM4``\ =5.0d-6,\ ``THRSYM5``\ =1.0d-7.
* **``USEMRCC``\ =\ *n*** Once the MRCC program of M. Kallay or the Gecco program of A. Köhn is used for determining individual grid points, the option ``USEMRCC=1`` needs to be set, which is needed to ensure proper communication between Molpro and Mrcc. Default: ``USEMRCC=0``.
* **``VAR1D``\ =\ *variable*** The ``XSURF`` program reads the energy of electronic structure calculations from the internal Molpro variables, e.g. ``ENERGY``, ``EMP2``, :math:`\dots`. The internal variable is specified by the keyword ``VAR1D``. The default for the ``VAR1D`` keyword is the internal variable ``ENERGY``.
* **``VIBIRREP``\ =\ *variable*** The irreps of the vibrations within the XSURF, VSCF and VCI programs may differ from those within the FREQ program as the molecules will be be reoriented according to the conventions (see keyword ``ORIENT``). In order to use the same irreps as in the FREQ program, one may use ``VIBIRREP=Sort``.

<!--  \* **``GMAT``\ =\ *n*** If the vibrational frequencies sould be computed with the Gmatrix formalism, :math:`n` determines the dimension of the expansion of the Wilson Gmatrix. Higher than 2 is not recommended

* **``PSEUDOPOT``\ =\ *n***. If the vibrational frequencies sould be computed with the Gmatrix formalism, :math:`n` determines the dimension of the expansion of the Wilson pseudopotential. Higher than 2 is not recommended-->

The following example shows the input of a calculation which computes energy and dipole surfaces at the MP2/cc-pVTZ level and subsequently determines the anharmonic frequencies at the VSCF and VCI levels. Hartree-Fock calculations will not be restarted and the runtime option --logfile-scratch directs the .log-files to the scratch directory as defined by the $TMPDIR variable.

.. code-block:: text

   !options: --logfile-scratch
   memory,20,m
   orient,mass
   geometry={
      3
   Water
   O          0.0675762564        0.0000000000       -1.3259214590
   H         -0.4362118830       -0.7612267436       -1.7014971211
   H         -0.4362118830        0.7612267436       -1.7014971211
   }
   
   mass,iso
   basis=vdz
   
   hf
   mp2
   optg
   frequencies,symm=auto
   
   label1
   int
   {hf
    start,atden}
   {mp2
    cphf,1}
   
   vibstate,combi=1
   {xsurf,sym=auto
    intensity,dipole=2}
   poly
   vscf,pot=poly
   vci,pot=poly

.. _pes_generators--intensities:

Intensities
-----------

``INTENSITY,options``

The ``INTENSITY`` directive of the ``XSURF`` program provides options for controlling the calculations of property surfaces as needed for the calculation of intensities. Currently, dipole surfaces (infrared intensities), polarizability tensor surfaces (Raman intensities) and quadrupole tensor surfaces are supported. The calculation of dipole surfaces can be combined with the calculation of polarizability or quadrupole surfaces, but the latter two exclude each other. Property surfaces can be computed for all those methods for which analytical expressions are available in Molpro. Considering dipole surfaces for the calculation of infrared intensities, for all methods except Hartree-Fock this requires the keyword ``CPHF,1`` after the keyword for the electronic structure method. In multi-level schemes for which the variables ``VAR1D``, ``VAR2D`` and ``VAR3D`` are set individually, the VARDIP\ *n*\ D[X,Y,Z] variables have to be set accordingly. The determination of dipole surfaces beyond Hartree-Fock quality effectively doubles the computation time for surface calculations.

.. _pes_generators--options-1:

Options
=======

* **``DIPOLE``\ =\ *n*** Allows to switch between the different dipole surface calculations. ``DIPOLE=0`` switches off all dipole calculations. ``DIPOLE=1`` (this is the default) computes the dipole surfaces at the Hartree Fock level of theory, and therefore does not increase the computation time of the electronic structure calculations. ``DIPOLE=2`` switches on the dipole surfaces at the full level of theory, therefore ``CPHF,1`` is required. This effectively doubles the computation time for surface calculations.
* **``NDIMDIP``\ =\ *n*** This denotes the term after which the :math:`n`-body expansion of the dipole surfaces is truncated. The default is set to 3. Note that ``NDIMDIP`` has to be lower or equal to ``NDIM``.
* **``NDIMPOL``\ =\ *n*** This variable denotes the term after which the :math:`n`-body expansion of the polarizability tensor surfaces is truncated. The default is set to 0. Note that ``NDIMPOL`` has to be lower or equal to ``NDIM`` and must be smaller than 4. Note that currently only Hartree-Fock and MP2 polarizabilities are supported, which requires the ``POLARI`` keyword in the respective programs. Besides that, the frozen core approximation cannot yet be employed within the calculation of MP2 polarizabilities.
* **``NDIMQUAD``\ =\ *n*** This variable denotes the term after which the :math:`n`-body expansion of the quadrupole tensor surfaces is truncated. The default is set to 0. Note that ``NDIMQUAD`` has to be lower or equal to ``NDIM`` and must be smaller than 4.
* **``POLYSYM``\ =\ *variable*** (=ON Default). Symmetry in the polarizability surfaces differs from symmetry in energy or dipole surfaces and its recognition can be switched on or off. Symmetry is only detected based on geometrical parameters.
* **``QUADYSYM``\ =\ *variable*** (=ON Default). Symmetry in the quadrupole surfaces differs from symmetry in energy or dipole surfaces and its recognition can be switched on or off. Symmetry is only detected based on geometrical parameters.
* **``VARDIPxDX``\ =\ *variable*** (x=1..4) Variable which is used for the :math:`x` direction of the dipole moment for 1D surfaces.
* **``VARDIPxDY``\ =\ *variable*** (x=1..4) Variable which is used for the :math:`y` direction of the dipole moment for 1D surfaces.
* **``VARDIPxDZ``\ =\ *variable*** (x=1..4) Variable which is used for the :math:`z` direction of the dipole moment for 1D surfaces.
* **``VARPOLxDXX``\ =\ *variable*** (x=1..4) Variable which is used for the :math:`xx` component of the polarizability tensor for 1D surfaces.
* **``VARPOLxDYY``\ =\ *variable*** (x=1..4) Variable which is used for the :math:`yy` component of the polarizability tensor for 1D surfaces.
* **``VARPOLxDZZ``\ =\ *variable*** (x=1..4) Variable which is used for the :math:`zz` component of the polarizability tensor for 1D surfaces.
* **``VARPOLxDXY``\ =\ *variable*** (x=1..4) Variable which is used for the :math:`xy` component of the polarizability tensor for 1D surfaces.
* **``VARPOLxDXZ``\ =\ *variable*** (x=1..4) Variable which is used for the :math:`xz` component of the polarizability tensor for 1D surfaces.
* **``VARPOLxDYZ``\ =\ *variable*** (x=1..4) Variable which is used for the :math:`yz` component of the polarizability tensor for 1D surfaces.

An example for a calculation, which provides both, infrared and Raman intensities, is given below.

.. code-block:: text

   label1
   {hf
    start,atden}
   {mp2
    core,0
    polari}
   
   {xsurf,info=1
    intensity,ndimpol=3 }
   
   poly,ndimpol=3
   vscf,pot=poly,ndimpol=3,info=1
   vci,pot=poly,version=4,ndimpol=3,info=1

A calculation for quadrupole intensities would require an input like

.. code-block:: text

   label1
   {hf
    start,atden}
   {ccsd(t);expec,qm}
   
   {xsurf,info=1
    intensity,ndimquad=3 }

.. _pes_generators--restart-capabilities:

Restart capabilities
--------------------

``DISK,options``

As ``XSURF`` calculations are very demanding it is highly recommended to dump the grid representation of the potential to disk. This allows for convenient restarts for subsequent vibrational structure calculations. Note, that restarts can also be performed for incomplete potentials.

.. _pes_generators--options-2:

Options
=======

* **``AUTO``\ =\ *n*** For Franck-Condon calculations this allows to specify the number of the two potential energy surfaces.
* **``DUMP``\ =\ *file name*** The potential can be dumped into an external ASCII-file which can be used for restarting. Its name must be provided as the argument of the ``DUMP`` keyword, e.g. ``DUMP=’formaldehyde.pot’``. The ASCII-file provides the interface to other programs and offers the possibility for controlled storage and modification of the computed potentials. Dipole and polarizability surfaces will also be dumped if available.
* **``EXTERN``\ =\ *file name*** ``XSURF`` calculations are restartable at any point of a truncated calculation as long as the automatically generated file \*.pot_RESTART is available.
* **``SAVE``\ =\ *record*** Once a complete surface has been generated, a record can be specified, where to dump the potential in the temporary binary files. Once this keyword is not provided explicitly, the potential will be dumped in record 5600.2
* **``TIME``\ =\ *value*** (=3600.00 Default) Time given in seconds for the next dumping of the restart file. For long lasting electronic structure single point calculations it is useful to increase this value.
* **``WHERE``\ =\ *variable*** In combination with the keywords ``DUMP`` and ``EXTERN`` for an external restart file, the keyword ``WHERE`` specifies the path for the external ASCII file. Two options are available, ``WHERE=home`` and ``WHERE=scr``. As the external files can be huge for ``XSURF`` calculations, they will be stored on the scratch disk given by the Molpro variable ``$TMPDIR`` by default.

.. _pes_generators--taylor-expansions:

Taylor expansions
-----------------

``VTAYLOR,options``

By default, the ``XSURF`` program generates an :math:`n`-mode expansion. However, the program structure allows also to retrieve a Taylor expansion of the potential, which is identical with a Taylor expansion obtained by differentiation. In principal Taylor expansions of arbitrary order can be generated, but of course it must be guaranteed that the order of coupling terms is sufficiently high, e.g. a sextic force field cannot be obtained from a ``NDIM``\ =4 calculation, because this calculation generates coupling terms with at most 4 different indices. In such a case, the missing terms will simply be neglected.

.. _pes_generators--options-3:

Options
=======

* **``ORDER``\ =\ *n*** (=5 Default) Number of basis functions within the Taylor expansion.
* **``POINTS``\ =\ *n*** (=5 Default) Number of ab initio points controlling the accuracy of the derivatives (e.g. 5-point formula).
* **``SCALE``\ =\ *value*** (=1.0d-1 Default) This keyword controls the step width.
* **``TYPE``\ =\ *variable***

  * ``TYPE``\ =\ ``QFF`` (corresponds to ``POINTS``\ =5 and ``ORDER``\ =5) specifies a full quartic force field.
  * ``TYPE``\ =\ ``SQFF`` specifies a semi-quartic force field (as used in VPT2 calculations).
  * ``TYPE``\ =\ ``SEXTIC`` (corresponds to ``POINTS``\ =7 and ``ORDER``\ =7) is the shortcut for a sextic force field.

.. _pes_generators--multi-level-calculations:

Multi-level calculations
------------------------

``VMULT,options``

The level of the electronic structure calculations can be changed for the different :math:`i`-body terms in the expansion of the potential. As a consequence, the keywords ``START2D``, ``START3D``, ``VAR2D`` and ``VAR3D`` exist in full analogy to the keywords ``START1D`` and ``VAR1D`` in standard calculations (see above). The number always represents the level of the expansion term. Such calculations are termed multi-level calculations. There does *not* exist a corresponding set of keywords for the 4-body terms. 4-body terms will always use the variables specified for the 3-body terms (this restriction is lifted in the ``XSURF`` program.

.. _pes_generators--options-4:

Options
=======

* **``MULTI``\ =\ *n*** The keywords ``START1D``, ``START2D``, ``START3D`` in combination with the commands ``VAR1D``, ``VAR2D`` and ``VAR3D`` allow for the calculation of multi-level potential energy surfaces. This would imply in principle that the 1D term of the potential needs to be computed at all three levels and the 2D term at two computational levels. As certain low level results are byproducts of more sophisticated methods (e.g. the HF energy is a byproduct of an MP2 calculation or the MP2 energy is a byproduct of a CCSD(T) calculation) the computational overhead can be avoided by the ``MULTI`` option.

  * ``MULTI=1:`` This is the default and most expensive choice. The 1D potential will be computed at all 3 levels of theory. Likewise, the 2D potential will be calculated at 2 levels explicitly. An example would be: <code>

1D: CCSD(T)/cc-pVTZ
2D: MP4(SDQ)/cc-pVTZ
3D: MP2/cc-pVDZ

.. code-block:: text

{XSURF,Sym=auto

.. code-block:: text

      VMULT,Start2D=label2,Start3D=label3,Multi=1}

  * ``MULTI=2:`` All information is provided by the preceding calculations and thus no part of the potential has to be computed twice. Examples: <code>

1D: CCSD(T)/cc-pVTZ
2D: CCSD(T)/cc-pVTZ
3D: MP2/cc-pVTZ

{XSURF,Sym=auto

.. code-block:: text

    VMULT,Start2D=label1,Start3D=label2
    VMULT,Var3D=EMP2,Multi=2}

</code><code>
1D: CCSD(T)/cc-pVTZ
2D: MP2/cc-pVTZ
3D: MP2/cc-pVTZ

{XSURF,Sym=auto

.. code-block:: text

    VMULT,Start2D=label2,Start3D=label2
    VMULT,Var2D=EMP2,Var3D=EMP2,Multi=2}

  * ``MULTI=3:`` The 2D potential provides all information for the 3D part while there is no connection between 1D and 2D. Consequently, the 1D contributions need to be computed twice (at the 1D and 2D levels) while all other terms will be computed just once. Examples: <code>

1D: CCSD(T)/cc-pVTZ
2D: MP4(SDQ)/cc-pVTZ
3D: MP2/cc-pVTZ

{XSURF,Sym=auto

.. code-block:: text

    VMULT,Start2D=label2,Start3D=label3
    VMULT,Var3D=EMP2,Multi=3}

</code> <code>
1D: CCSD(T)/cc-pVTZ
2D: MP4(SDQ)/cc-pVTZ
3D: MP4(SDQ)/cc-pVTZ

{XSURF,Sym=auto

.. code-block:: text

    VMULT,Start2D=label2,Start3D=label2,Multi=3}

  * ``MULTI=4:`` The 1D calculation provides all information for the 2D potential but does not so for the 3D part. Hence, the 1D contribution and the 2D contributions need to be computed twice. Examples <code>

1D: CCSD(T)/cc-pVTZ
2D: CCSD(T)/cc-pVTZ
3D: MP4(SDQ)/cc-pVTZ

{XSURF,Sym=auto

.. code-block:: text

    VMULT,Start2D=label1,Start3D=label2,Multi=4}

</code> <code>
1D: CCSD(T)/cc-pVTZ
2D: MP2/cc-pVTZ
3D: MP2/cc-pVDZ

{XSURF,Sym=auto

.. code-block:: text

    VMULT,Start2D=label2,Start3D=label3
    VMULT,Var2D=EMP2,Multi=4}

* **``STARTxD``\ =\ *label*** (x=2..4) Definition of the label in the input stream specifying the 2nd, 3rd and 4th electronic structure method of the multi-level scheme.
* **``VARxD``\ =\ *variable*** Molpro variable to be read for the higher levels of the multi-level scheme.

In 2D and 4D calculations (i.e. ``NDIM=2,4``) the ``VMULT`` command can be used as well. In 4D calculations the last level must always be identical to the 3D level. In 2D the meaning of ``MULTI=1`` and ``MULTI=3`` is the same. Likewise, ``MULTI=2`` and ``MULTI=4`` are the same in case of 2D calculations. ``START2D`` and ``START3D`` define labels in the input stream in order to compute the 2D and 3D terms at different levels of electronic structure theory than the 1D terms. The use of the ``START2D`` and ``START3D`` commands usually requests the use of ``GOTO`` commands in the input. The keywords ``VAR2D`` and ``VAR3D`` are defined in full analogy to the ``VAR1D`` option. They specify the internal variable (e.g. ENERGY, EMP2, CCSD, ...) to be read out for a given grid point.

The following example shows a 1D:CCSD(T)/cc-pVTZ; 2D:MP4(SDQ)/cc-pVTZ and 3D:MP2/cc-pVTZ multi-level calculation. As the MP2 energy is a byproduct of the CCSD(T) and MP4(SDQ) calculations only the 1D grid points will be computed twice (at the CCSD(T) and MP4(SDQ) levels). The 1D and 2D energies will be obtained from the internal variable ``ENERGY`` while the 3D energies make use of the ``EMP2`` variable.

.. code-block:: text

   !options: --logfile-scratch
   memory,50,m
   orient,mass
   geometry={
   6
   Ethene
   C          0.0000000000        0.0000000000       -0.6685890718
   C          0.0000000000        0.0000000000        0.6685890718
   H          0.0000000000       -0.9240027061       -1.2338497710
   H          0.0000000000        0.9240027061       -1.2338497710
   H          0.0000000000        0.9240027061        1.2338497710
   H          0.0000000000       -0.9240027061        1.2338497710
   }
   
   mass,iso
   basis=vtz
   
   hf
   ccsd(t)
   optg
   freq,symm=auto
   
   label1
   int
   {hf
    start,atden}
   ccsd(t)
   goto,label4
   
   label2
   int
   {hf
    start,atden}
   {mp4
    notripl}
   goto,label4
   
   label3
   int
   {hf
    start,atden}
   mp2
   
   label4
   {xsurf,sym=auto
    vmult,start2D=label2,start3D=label3,Var3D=EMP2,Multi=3}
   poly
   vscf,pot=poly
   vci,pot=poly

However, if you need a more specialized multi-level scheme, ``XSURF`` provides an expert mode. Within this you can for example change the method for 3D and 4D terms. When calculating an ab initio point for an :math:`n` dimensional body term, two aspects need to be considered. First, you may check whether information for higher-order terms can be retrieved from low-order terms, e.g. the MP2 energy is a byproduct of a CCSD calculation. Second, if the information cannot be retrieved, single-point calculations at different electronic structure levels may be repeated for the low-order terms. All this information is internally stored in a matrix.

.. math::

   \begin{aligned}
   M&=&\left(\begin{array}{cccc}
   1&0&-1&1\\
   0&1&-2&1\\
   0&0&1&1\\
   0&0&0&1
   \end{array}\right)\end{aligned}

The columns of the matrix belong to the method and the lines to the dimension. The only important numbers are therefore the upper diagonals. A :math:`1` means calculate something and a number smaller than one, that the information is somewhere available. This matrix is an example for the following set of methods:

.. code-block:: text

   1D: CCSD(T)/cc-pVTZ
   2D: CCSD(T)/cc-pVTZ
   3D: MP2/cc-pVTZ
   4D: HF/minao

For the other multi cases (see above) the matrix elements look like:

\* ``MULTI=1``:

.. math::

   M=\left(\begin{array}{ccc}
   1&1&1\\
   0&1&1\\
   0&0&1
   \end{array}\right)

\* ``MULTI=2``:

.. math::

   M_1=\left(\begin{array}{ccc}
   1&0&-1\\
   0&1&-2\\
   0&0&1
   \end{array}\right); \qquad
   M_2=\left(\begin{array}{ccc}
   1&-1&0\\
   0&1&0\\
   0&0&1
   \end{array}\right)

\* ``MULTI=3``:

.. math::

   M_1=\left(\begin{array}{ccc}
   1&1&-2\\
   0&1&-2\\
   0&0&1
   \end{array}\right); \qquad
   M_2=\left(\begin{array}{ccc}
   1&1&0\\
   0&1&0\\
   0&0&1
   \end{array}\right)

\* ``MULTI=4``:

.. math::

   M_1=\left(\begin{array}{ccc}
   1&0&1\\
   0&1&1\\
   0&0&1
   \end{array}\right); \qquad
   M_2=\left(\begin{array}{ccc}
   1&-1&1\\
   0&1&1\\
   0&0&1
   \end{array}\right)

These expert multi level matrices can be set by ``MMAT(x,y)``\ =\ *n*. Only non-zero elements need to be set.

.. _pes_generators--linear-combinations-of-normal-coordinates:

Linear combinations of normal coordinates
-----------------------------------------

``LINCOMB,options``

The ``LINCOMB`` directive allows for the calculation of linear combinations of normal coordinates for the expansion of the potential. This is realized by 2x2 Jacobi rotations. At most 3N-6/2 rotations can be provided in the input.

.. _pes_generators--options-5:

Options
=======

* **``ANGLE``\ =\ *value*** Rotation angle in degree. This keyword requires the specification of two normal coordinates provided by ``NM1`` and ``NM2``.
* **``BLx``\ =\ *n*** This option assigns mode :math:`n` to block :math:`x`. For example, the line ``LINCOMB,BL1=1,BL1=2,BL2=5,BL2=6`` for a 4-atomic molecule assigns modes 1 and 2 to a 1st block and thus these two modes will be localized afterwards. Modes 3 and 4 will not be affected and thus refer to standard normal coordinates, while modes 5 and 6 constitute a 2nd block
* **``LOCAL``\ =\ *n*** ``LOCAL``\ =1 localizes the normal coordinates of the CH-stretchings. Note that this destroys symmetry of these modes. Usually localization has strong impact on subsequent ``VSCF`` calculations. ``LOCAL``\ =2 localizes the normal coordinates of a molecular cluster to the contributing entities. This localization scheme localizes within the individual irreps, which usually leads to a very faint localization. Switching symmetry off by ``MPG``\ =1 in the ``XSURF`` program leads to a much stronger localization.
* **``NM1``\ =\ *n*, ``NM2``\ =\ *m*** Denotes the normal coordinates to be rotated.
* **``THRLOC``\ =\ *value*** (=1.0d-6 Default) Threshold within the localization procedure.

.. _pes_generators--scaling-of-individual-normal-coordinates:

Scaling of individual normal coordinates
----------------------------------------

``SCALNM,options``

The ``SCALNM`` directive allows for the scaling with respect to the individual normal coordinates or an automated scaling of all of them. This is the recommended choice for potentials dominated by quartic rather than quadratic terms. At most 3N-6 individual scale factors and shift parameters can be provided. In particular the ``AUTO`` option was found to be very helpful in practical applications.

.. _pes_generators--options-6:

Options
=======

* **``AUTO``\ =//on / off//** ``AUTO``\ =\ *on* (default) switches on an automatic scaling procedure of the potential in order to determine meaningful elongations and ``SHIFT`` values with respect to all coordinates, i.e. for each normal mode an optimized scaling parameter ``SFAC`` and ``SHIFT`` parameter will be determined. Usually this results in an increased number of 1D grid points. The ``AUTO`` keyword intrinsically depends on the thresholds and parameters, which can be controlled by the keywords ``THRSHIFT``, ``ITMAX``, ``LEVMAX``, ``DENSMAX``, and ``DENSMIN``.
* **``DENSMAX``\ =\ *value*** (=1.d-2 default) Threshold for the maximum vibrational density on the edges of the potential needed for the automated upscaling of the potentials (see keyword ``AUTO``).
* **``DENSMIN``\ =\ *value*** (=1.d-4 default) Threshold for the minimum vibrational density on the edges of the potential needed for the automated downscaling of the potentials (see keyword ``AUTO``).
* **``ITMAX``\ =\ *n*** (=10 default) Specifies the maximum number of iterations within the automatic scaling of the potentials (see Keyword ``AUTO``).
* **``LEVMAX``\ =\ *n*** Maximum number of vibrational states to be included for controlling the automated scaling and shifting procedure. The default is set to 5. This value should support subsequent VCI calculations.
* **``MODE``\ =\ *n*** Denotes the normal coordinate to be scaled or shifted.
* **``SFAC``\ =\ *value*** Scaling factor for mode ``MODE``. The default is 1.0.
* **``SHIFT``\ =\ *n*** Allows to shift the potential with respect to the specified coordinate by *n* or *-n* grid points, respectively. Default: ``SHIFT=0``.
* **``SHOW``\ =\ *n*** (=0 default) Addition printing within the scaling procedure is switched on by ``SHOW=1``.
* **``THRSHIFT``\ =\ *value*** Threshold controlling the automated shifting of potentials as obtained from the state densities on the lhs and rhs of the potentials. The default is given as ``THRSHIFT=0.05``.

<!--==== Scaling of individual internal coordinates ====

``SCALIC,options``

The ``SCALIC`` directive allows for the scaling with respect to the individual internal coordinates or an automated scaling of all of them.

.. _pes_generators--options-7:

Options
=======

* **``AUTO``\ =//on / off//** ``AUTO``\ =\ *on* (default) switches on an automatic scaling procedure of the potential in order to determine meaningful elongations and ``SHIFT`` values with respect to all coordinates, i.e. for each normal mode an optimized scaling parameter ``SFAC`` and ``SHIFT`` parameter will be determined. Usually this results in an increased number of 1D grid points. The ``AUTO`` keyword intrinsically depends on the thresholds and parameters, which can be controlled by the keywords ``THRSHIFT``, ``ITMAX``, ``LEVMAX``, ``DENSMAX``, and ``DENSMIN``.
* **``DENSMAX``\ =\ *value*** (=1.d-2 default) Threshold for the maximum vibrational density on the edges of the potential needed for the automated upscaling of the potentials (see keyword ``AUTO``).
* **``DENSMIN``\ =\ *value*** (=1.d-4 default) Threshold for the minimum vibrational density on the edges of the potential needed for the automated downscaling of the potentials (see keyword ``AUTO``).
* **``LEVMAX``\ =\ *n*** Maximum number of vibrational states to be included for controlling the automated scaling and shifting procedure. The default is set to 5. This value should support subsequent VCI calculations.
* **``MIN(n)``\ =\ *value*** Defines the minimum :math:`value` of coordinate :math:`n`.
* **``MAX(n)``\ =\ *value*** Defines the maximum :math:`value` of coordinate :math:`n`.

-->

.. _pes_generators--fit-functions:

Fit Functions
-------------

``FIT,options``

A fit function has to be defined for each coordinate. These fit functions are used as an intermediate fit to generate a fine grid representation of the potential energy surface. The fit functions can be defined either by the user or automatically via cross-validation. If no electronic structure level for the cross-validation is provided by the user, polynomials are used as a default. This directive also exists in the ``POLY`` program. If no fit functions are defined within the ``XSURF`` program, but in the ``POLY`` program, the fit functions of the ``POLY`` program are also used in the ``XSURF`` program.

.. _pes_generators--options-8:

Options
=======

* **``COORD(x)``\ =\ *variable*** Defines the fit function for coordinate :math:`x`. The possible fit functions are B-splines (*bspline*), Gaussian functions (*gauss*), Morse functions (*morse*), polynomials (*poly*) and trigonometric functions (*trigo*).
* **``FITLABEL``\ =\ *variable*** The name of the label defined in the input stream. The label contains the electronic structure level which should be used for the cross-validation.
* **``FITMETHOD``\ =\ *n*** (=1 Default) Within the iterative build-up of the individual subsurfaces, intermediate fitting will be used. This can be based on true multidimensional Kronecker product fitting (``FITMETHOD``\ =1) or on fitting along one-dimensional cuts (``FITMETHOD``\ =2).
* **``FITxD``\ =\ *n*** The maximum order of the polynomials used for fitting within the iterative interpolation scheme can be controlled by the keywords ``FIT1D, FIT2D, FIT3D, FIT4D``. The default is given by 9. However in certain cases higher values may be necessary, but require an appropriate number of coarse grid points, which can be controlled by ``MIN1D`` etc. (See ``XSURF`` options)
* **``ONLY``\ =\ *variable*** Sets one fit function for all coordinates. The possible fit functions are the same as for the option ``COORD``.

.. _pes_generators--point-selection:

Point Selection
---------------

``POINTS,options``

The positioning of the ab initio single points along a coordinate can be controlled by this directive. The default is currently an empirically fixed distribution. Alternatively one can use a positioning based on Gaussian process regression.

.. _pes_generators--options-9:

Options
=======

* **``GPRDERIV``\ =\ *n*** (=\ *2* Default) Up to the dimension *n*, the derivatives obtained by a Gaussian process regression are used to weight the variance.
* **``GPRGRIDxD``\ =\ *n***. The number *n* of grid points for which the variance is computed for the dimension **x**. Only odd values are possible. As a default, the maximum number of *ab initio* points is used. (See keyword ``MAXxD``)
* **``GPRPRExD``\ =\ *n***. For higher dimensions, it is recommended that the variance is not computed for all desired points. Instead a pre-selection, also based on gaussian process regression is used. With this keyword, *n* points are used for the pre-selection of the dimension **x**. Negative values will switch the pre-selection off. For the 1D and 2D, no pre-selection is done by default. The default for higher dimensions is set to 4. Not, that this value has to be considered adequately with respect to the keyword ``GPRGRIDxD``.
* **``POINT_SCHEME``\ =\ *variable*** (=\ ``NOSHIFT`` Default) The distribution of ab initio points along a coordinate is determined by a fixed point scheme. This distribution has been generated for potentials, which have not been shifted. For strongly shifted potentials, improved point schemes can be used by the option ``POINT_SCHEME``\ =\ ``SHIFT``.
* **``TYPE``\ =\ *variable*** (=\ *fix* Default) In the case ``TYPE=gpr``, the variance obtained by a Gaussian process regression is used to determine new points were the energy as to be computed.

.. _pes_generators--calculation-of-normal-coordinates:

Calculation of normal coordinates
---------------------------------

``VFREQ,options``

Usually, the displacements vectors of the normal coordinates are retrieved from a preceding harmonic frequency calculation called by the ``FREQ`` program. Alternatively, these vectors can be obtained from the ``XSURF`` program and the ``VFREQ`` directive. However, this alternative is solely based on a twofold numerical differentiation and does not take advantage out of analytical derivatives. However it offers a couple of options, which are not available in the ``FREQ`` program.

.. _pes_generators--options-10:

Options
=======

* **``COORD``\ =\ *n*** (=2 Default) Symmetry adapted coordinates, ``COORD``\ =1, or Cartesian coordinates, ``COORD``\ =2, may be used within the numerical differentiation.
* **``METHOD``\ =\ *n*** (=1 Default) This option specifies the number of points within the numerical differentiation, i.e. ``METHOD``\ =1 refers to the standard 3-point formula (central differences), ``METHOD``\ =2 denotes the more accurate 5-point formula and ``METHOD``\ =3 the 7-point formula.
* **``PRINT``\ =\ *n*** (=1 Default) Printout control.
* **``START``\ =\ *label*** This sets the label in the input stream to determine the electronic structure level to be used.
* **``STEP``\ =\ *value*** (=1.0d-2 Default) This option specifies the step width within the numerical differentiation.

.. _pes_generators--visualization-and-interfaces:

Visualization and interfaces
----------------------------

``GRAPH,options``

The ``GRAPH`` directive is the interface to programs for visualizing potential terms and to provide potential information for any other programs in a most simple manner.

.. _pes_generators--options-11:

Options
=======

* **``DIRECTORY``\ =\ *path*** (=./plots1 Default) Path or name of the directory to be specified for dumping the files for visualisation. See the keyword ``NDIM``.
* **``MOLDEN``\ =\ *file name*** This allows to dump a file, which can directly read in by the Molden or Wxmacmolplot programs. This allows for the visualisation of the geometry and the harmonic frequencies of the molecule.
* **``NDIM``\ =\ *n*** (=0 Default) This keyword writes all *n*\ D surfaces and a corresponding Gnuplot script in a separate subdirectory (``plots1``) in the *home*-directory in order to allow for visualization of the computed *n*\ D surfaces. E.g. the command "gnuplot plotV1D.gnu" in the ``plots1`` directory produces .eps files for all 1D surfaces.

.. _pes_generators--modeling-of-high-order-n-body-terms:

Modeling of high-order n-body terms
-----------------------------------

``REPAR,options``

Within the framework of multi-level calculations (see the directive ``VMULT``), 3D and 4D terms can be modeled. The modeling scheme is based on a reparametrization of the semiempirical AM1 method. Consequently, in the input stream the energy variable to be read in must refer to a semiempirical calculation. After the 2D terms the program optimizes the semiempirical parameters in order to represent the 1D and 2D surfaces best.

.. _pes_generators--options-12:

Options
=======

* **``ITMAX1D``\ =\ *n*** The maximum number of iterations in the local optimization of the semiempirical parameters can be controlled by ``ITMAX1D`` and ``ITMAX2D``. The defaults are ``ITMAX1D``\ =100 and ``ITMAX2D``\ =150.
* **``RMS1D``\ =\ *value*** The keywords ``RMS1D`` and ``RMS2D`` specify the threshold for terminating the 1D and 2D iterations in the local optimization of the semiempirical parameters. The defaults are given by ``RMS1D``\ =1.d-6 and ``RMS2D``\ =1.d-6.

The following example shows the input for a surface calculation in which the 3D terms will be modeled.

.. code-block:: text

   memory,20,m
   orient,mass
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
   freq
   
   label1
   abinitio
   basis=vdz
   int
   rhf
   mp2
   goto,label4
   
   label2
   semi,am1
   int
   rhf
   
   label4
   {xsurf
    vmult,start2D=label1,start3D=label2,multi=4
    repar}
   poly
   vscf,pot=poly
   vci,pot=poly

.. _pes_generators--error-correction-schemes:

Error correction schemes
------------------------

``ALTER,options``

The ``ALTER`` directive of the ``XSURF`` program allows to apply error correction schemes for individual single point calculations. For example, in case that the Hartree Fock calculation for a certain grid point did not converge and the ``ORBITAL`` directive in the subsequent electron correlation calculation uses the ``IGNORE_ERROR`` option, an alternative calculation scheme can be provided, e.g. MCSCF in contrast to RHF.
It allows to apply error correction schemes for individual single point calculations. For example, in case that the Hartree Fock calculation for a certain grid point did not converge and the ``ORBITAL`` directive in the subsequent electron correlation calculation uses the ``IGNORE_ERROR`` option, an alternative calculation scheme can be provided, e.g. MCSCF in contrast to RHF. The ``ALTER`` directive always requests to specify a new label, which replaces the old one. If more than one label shall be replaced, the ``ALTER`` directive needs to be called repeatedly.

.. _pes_generators--options-13:

Options
=======

* **``NEW``\ =\ *label*** Specification of the new label.
* **``OLD``\ =\ *label*** Specification of the old label.

Note that DFT calculations often still converge when RHF calculations already fail to do so.
The following example demonstrates the use of the ``ALTER`` directive within a multi-level PES calculation. In case that the RHF calculation for the 1D or 2D terms does not converge, this will be recognized by the UCCSD(T)-F12a calculations. The option ``orbital,ignore_error=2`` prevents a termination of Molpro and the programs tries to enforce convergence by the recipe specified below ``label5``.

.. code-block:: text

   !options: --logfile-scratch
   memory,500,m
   gthresh,optgrad=1.d-7,twoint=1.d-14,prefac=1.d-16
   geometry={
   O   ,,     -0.4187902305    ,   -2.0024156961    ,    0.0000000000
   N   ,,      0.9293931761    ,   -0.1403574221    ,    0.0000000000
   N   ,,     -0.3385150234    ,    2.0246339597    ,    0.0000000000
   H   ,,     -2.2504006895    ,    1.9819452952    ,    0.0000000000
   H   ,,      0.6869538492    ,    3.6185403577    ,    0.0000000000
   }
   
   basis=vtz-f12
   mass,iso
   
   charge=1
   {rhf
    start,atden}
   uccsd(t)-f12a
   optg
   freq,symm=auto
   
   {rhf
    start,atden}
   {uccsd(t)-f12a,freeze_save=1891.2}
   
   label1
   symmetry,auto
   charge=1
   {rhf
    start,atden}
   {uccsd(t)-f12a,freeze_start=1891.2;orbital,ignore_error=2}
   goto,label4
   
   label2
   symmetry,nosym
   charge=1
   {uks,b3lyp
    start,atden}
   goto,label4
   
   label5
   symmetry,nosym
   basis=vtz-f12
   int
   {rhf
    start,atden
    save,2111.2}
   {multi
    occ,13
    closed,11
    wf,23,1,1
    canonical,3111.2
    start,2111.2}
   {rhf
    start,3111.2}
   {uccsd(t)-f12a,freeze_start=1891.2}
   
   label4
   {xsurf,sym=auto
    alter,old=label1,new=label5
    vmult,start2D=label1,start3D=label2,multi=4
    disk,where=home,dump='N2H2O.pot'}
   

.. _pes_generators--deleting-individual-surfaces:

Deleting individual surfaces
----------------------------

``DELETE,surface labels``

The ``DELETE`` directive allows to eliminate individual surfaces within the multi-mode expansion of the potential. Unlike the ``SKIP`` keyword, this directive can only be used once a calculation is restarted from a completed potential energy surface calculation. This directive is meant for studying the impact of individual surfaces or to eliminate troublesome surfaces, which failed to converge in the iterative fitting procedure.

.. list-table::

   * - ``DELETE``,\ *i*,\ *j*
     - deletes the 2D surface :math:`ij`
   * - ``DELETE``,\ *i*,\ *j*,\ *k*
     - deletes the 3D surface :math:`ijk`
   * - ``DELETE``,\ *i*,\ *j*,\ *k*,\ *l*
     - deletes the 4D surface :math:`ijkl`

.. _pes_generators--selection-of-modes:

Selection of Modes
------------------

``VIBMODE,options``

The ``VIBMODE`` directive allows to span the PES only with predefined modes. The following options can be combined in various ways.

.. _pes_generators--options-14:

Options
=======

* **``ENERGHIGH``\ =\ *value*** Modes with a frequency lower than **value** are used to span the surface (according to the harmonic frequencies)
* **``ENERGLOW``\ =\ *value*** Modes with a frequency higher than **value** are used to span the surface (according to the harmonic frequencies)
* **``HIGH``\ =\ *n*** the highest **n** modes are used to span the surface
* **``LOW``\ =\ *n*** the lowest **n** modes are used to span the surface
* **``MODE``\ =\ *n*** Mode which is used to span the surface (can be used multiple times)

.. _pes_generators--interface-to-other-programs:

Interface to other programs
---------------------------

``INTERFACE,options``

The ``INTERFACE`` directive allows for the communication with other programs. It writes information about the individual grid points of a PES to an external ASCII file, which can be processed by other software. <!-- Likewise, files in the same structure with additional information from external programs can be read in. After reading in all data points, the date points will be transformed into a fine grid and fitted to polynomials.-->

.. _pes_generators--options-15:

Options
=======

<!--  \* **``COPY``\ =\ *n*** (=0 Default) Once new data have been generated in the external ASCII file, the coefficients of the corresponding polynomials can be displayed in the ``POLY`` program using the option ``COEF_INTERFACEx`` with (x=1,2...). It is also possible to replace the energy or dipole surfaces generated by Molpro by these new quantities by ``COPY=ENE`` or ``COPY=DIP``. -->

* **``DATA``\ =\ *n*** (=1 Default) ``DATA=1`` provides detailed information about each single point of the PES in a formatted output. ``DATA=2`` provides the geometry and energy of a given point in a single line. New information about this point needs to be added at the end of the line. ``DATA=2`` prints the displacements along the coordinates and the energy in a single line. Again, new information needs to be added at the end of this line.
* **``FILE``\ =\ *file name*** Specifies the name of the external file.
* **``NDIM``\ =\ *n*** (=0 Default) Dimension of the :math:`n`-mode expansion to which the geometry information shall be dumped.

.. code-block:: text

     <!-- * **''NRES''=//n//** (=1 Default) Number of columns being added to the external file by an external program. -->

* **``SURFACE``\ =\ *n*** (=0 Default) Information about the energy values printed in the external file. ``SURFACE=0`` refers to absolute energies (minus the reference energy), while ``SURFACE=1`` refers to energy differences belonging to the individual increments of the subsurfaces.

<!--  \* **``TYPE``\ =\ *variable*** (=OUT Default) This option controls, if the file shall be written ``TYPE=OUT`` or read in ``TYPE=IN``. -->

* **``ZERO``\ =\ *n*** (=1 Default) If set to 1, geometries of lower orders of the :math:`n`-mode representation will be printed, i.e. the external file contains redundant data. ``ZERO=0`` neglects all redundancies and prints only unique points. As a consequence, an external file generated this way cannot be read in again for technical reasons.

.. _pes_generators--grid-computing:

Grid Computing
--------------

``XGRIDCOMP,options``

The ``GRIDCOMP`` directive of the ``XSURF`` program allows to interface Molpro with a grid computing client such as Segl. It is also possible to use the grid computing interface without any grid computing client by using scripts, which will automatically been generated within the individual calls of ``XGRIDCOMP``. The charge of the molecule as well as some other general commands are transferred to the individual grid point command files, which are printed out in the subdirectory points. If there are any doubts whether the specified command is transferred to the single point or not, the command should be given within the definition of the electronic structure calculations. Note, grid computing is needed is very special cases, when the standard "XSURF" procedure shall be bypassed.

.. _pes_generators--options-16:

Options
=======

* **``CORES``\ =\ *n*** Number of cores to be used within the grid computing.
* **``FILE``\ =\ *n*** (n=1..2) specifies the file number of the Molpro \*.wfu file (see the ``FILE`` command of Molpro).
* **``LOOP``\ =\ *n*** When processing the batches of single point calculations, the grid computing interface needs to know, if it is the very first batch (``LOOP``\ =0), in which just input files for Molpro will be generated or if it is one of the subsequent batches (``LOOP``\ =1), in which also the outputs of processed single point calculations need to be read in.
* **``MEMORY``\ =\ *n*** Denotes the amount of memory (in MW) which is needed in each single point calculation. The default is given by 100 MW.
* **``WFU``\ =\ *file name*** If additional information need to be read in from a .wfu file, this can be specified here.

.. code-block:: text

   !options: --logfile-scratch
   memory,50,m
   orient,mass
   geometry={
   6
   Ethene
   C          0.0000000000        0.0000000000       -0.6685890718
   C          0.0000000000        0.0000000000        0.6685890718
   H          0.0000000000       -0.9240027061       -1.2338497710
   H          0.0000000000        0.9240027061       -1.2338497710
   H          0.0000000000        0.9240027061        1.2338497710
   H          0.0000000000       -0.9240027061        1.2338497710
   }
   
   mass,iso
   basis=vtz
   
   hf
   ccsd(t)
   optg
   freq,symm=auto
   
   label1
   int
   {hf
    start,atden}
   ccsd(t)
   goto,label4
   
   label2
   int
   {hf
    start,atden}
   {mp4
    notripl}
   goto,label4
   
   label3
   int
   {hf
    start,atden}
   mp2
   
   label4
   {xsurf,sym=auto
    xgridcomp,memory=10,loop=0
    vmult,start2D=label2,start3D=label3,Var3D=EMP2,Multi=3
    disk,where=home,dump='ethene.pot'}
   vscf
   vci

To generate a potential energy surface with the grid computing interface, follow these steps:

* Run a Molpro calculation on the master control file (see the example above) to generate the control files for the individual single points.
* Use the generated xgridcomp.sh to run the individual single point calculations.
* Increase the ``loop`` option to 1, read in the generated \*.pot file (using the ``EXTERN`` command) and dump to a new \*.pot file, e.g. ethene_2.pot.
* Repeat the last steps until all single point calculations have been performed.

.. _pes_generators--extending-existing-potentials:

Extending existing potentials
-----------------------------

``VADD,options``

In practice one may come to the conclusion that the :math:`n`-mode expansion of an existing potential has been truncated too early and one needs to extend the order. Once the level of the electronic structure calculations shall not be changed between the highest existing order and the one to be added, one can simply restart the calculation from the existing restart file by increasing the option ``NDIM`` in the input stream. However, if one needs to alter the electronic structure level, the ``VADD`` directive needs to be used.

.. _pes_generators--options-17:

Options
=======

* **``START``\ =\ *label*** Specification of the label for the order to be added.
* **``QCOORD``\ =\ *variable*** (=POT Default) This option specifies from where to take the displacement vectors for the normal coordinates. By default they are taken from the external restart file, but ``QCOORD``\ =\ *FREQ* allows to take them from a new harmonic frequency calculation.

.. _pes_generators--quality-check:

Quality Check
-------------

``CHECK,options``

The ``CHECK`` directive of the ``XSURF`` program allows for a quality check of a completed surface. This routine simply computes the exact *ab initio* energies at randomly selected grid points and compares these values with the interpolated ones, which will be used subsequently for the determination of the wavefunction. This program is fully parallelized.

.. _pes_generators--options-18:

Options
=======

* **``NDIM``\ =\ *n*** Denotes the level to be checked, i.e. 1 corresponds to 1D, etc. Note, levels below :math:`n` will not be checked automatically.
* **``POINTSxD``\ =\ *value*** Determines the number of grid points in one dimension to be checked. The default is set to 4.

.. _pes_generators--additional-properties:

Additional properties
---------------------

``EXTRADATA,options``

The ``XSURF`` programs allows to compute energy surfaces, dipole surfaces and polarizability surfaces. In addition to that, arbitrary property surfaces can be generated and dumped into an external restart file.

.. _pes_generators--options-19:

Options
=======

* **``NDIM``\ =\ *n*** Dimension of the :math:`n`-mode expansion to be used for the new property.
* **``NEL``\ =\ *n*** Number of data to be read in for one point.
* **``VARx``\ =\ *variable*** (x=number) Name of the variable, which shall be read from the input file.

<!--==== Internal Coordinates ====

``INTC,options``

The ``XSURF`` programs allows to compute the desired surfaces with the use of internal coordinates.

.. _pes_generators--options-20:

Options
=======

* **``TYPE``\ =\ *variable*** Type of internal Coordinate. **variable=**

  * zmat: Zmatrix coordinates (need to be provided via the Input geometry)
  * ozmat: Zmatrix coordinates (internally generated)
  * pzmat: projected Zmatrix coordinates (Zmatrix needs to be provided via the Input geometry)
  * opzmat: projected Zmatrix coordinates (Zmatrix is internally generated)
  * nzmat: NOMODECO Zmatrix coordinates (Zmatrix needs to be provided via the Input geometry)
  * onzmat: NOMODECO Zmatrix coordinates (Zmatrix is internally generated)
  * deloc: Delocalised internal coordinates
  * natint: Natural internal coordinates
  * pnatint: projected Natural internal coordinates
  * poly: polyspherical internal coordiantes
* **``ECKART``\ =\ *n*** If :math:`n=1`, the geometry is rotated according to the eckart conditions which is recommended for the use of other properties than the energy
* **``NDIMGMAT``\ =\ *n*** Determines the order of the expansion of the Wilson G matrix. Higher than dimension 2 is not recommended
* **``NDIMVG``\ =\ *n***. Determines the order of the expansion of the Pseudopotential. Higher than the dimension 2 is not recommended
* **``RADII``\ =\ *x*** :math:`x` is the threshold for detecting a bon between two atoms
* **``CUTOFF``\ =\ *x*** :math:`x` is the threshold for detecting clusters (not useable currently)
* **``THRGEOM``\ =\ *x*** Threshold to determine if the geometry is converged
* **``ITMAX``\ =\ *n*** Defines the maximum number of iteration when elongate the geometries
* **``PSCRLAB``\ =\ *label*** Defines a label for precomputing the surface to determine a first scaling
* **``ELONG``\ =\ *n*** Defines different ways on how to compute the elongations within the backtransformation from internal to Cartesian coordinates

    * For Z-Matrix based coordinates it can be either a simple construction(:math:`n=0`) or the HOPE algorithm (:math:`n=1`)
    * For NatInt coordinates it can either be a standard B matrix algorithm (:math:`n=0`), virtuel geometries (:math:`n=1`) or subsequent elongation of single coordinates (:math:`n=3`)
* **``VAM``\ =\ *n*** If :math:`n=1`, rovibrational coupling is considered when the G-matrix is computed-->

.. _pes_generators--recommendations:

Recommendations
---------------

It is recommended to

* use the ``ORIENT,MASS`` keyword in order to rotate the molecule into standard orientation. This is necessary for a full exploitation of symmetry within the generation of the potential energy surface.
* use the ``MASS,ISO`` keyword to use the most available isotopes.
* use multi-level schemes in combination with symmetry and run Molpro in parallel in order to speed up the calculations. Explicitly correlated methods are preferable over conventional approaches.
* always dump the potential energy surface to an external file.

<!--

.. _pes_generators--the-old-pes-generator-surf:

THE OLD PES GENERATOR (SURF)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``SURF,options``

The old ``SURF`` program for generating potential energy surfaces is still implemented, but is no longer supported. Several keywords are specific to the ``XSURF`` core and cannot be used together with ``SURF``. The new and much improved ``XSURF`` code follows the same philosophy and many options are the same as in the old ``SURF`` code, but ``XSURF`` cannot read any potential files being generated by ``SURF``. If you need to use the old ``SURF`` program, see older versions of the manual for the corresponding keywords.
-->
