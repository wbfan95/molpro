.. raw:: html

   <span id="adaptive-neo"></span>

.. _nuclear-electronic_orbital_method--nuclear-electronic-orbital-neo-method:

Nuclear-electronic orbital (NEO) method
=======================================

The `Nuclear-electron orbital (NEO) <https://doi.org/10.1021/acs.chemrev.9b00798>`__ method pioneered by Hammes-Schiffer and coworkers is available in ``Molpro`` for (local) density fitted spin-restricted NEO-Hartree-Fock as well as NEO-RKS. It allows to handle a selected number of hydrogen nuclei as quantum particles by building a second Fock-matrix for the latter, coupling both subsystems (electrons and quantum protons) by a Coulomb operator. Further information about the method can be found `here <https://doi.org/10.1021%2Facs.jctc.3c01055>`__.

* **``DF-NEO-RHF``, *options*** calls the density-fitted NEO-Hartree-Fock program
* **``LDF-NEO-RHF``, *options*** calls the local density-fitted NEO-Hartree-Fock program
* **``DF-NEO-RKS``, *options*** calls the density-fitted NEO-DFT program

Currently, all NEO programs require the use of the ``gdirect`` option and are not available with symmetry.

.. _nuclear-electronic_orbital_method--density-fitting-neo-hartree-fock:

Density fitting NEO-Hartree-Fock
================================

Using

.. code-block:: text

   DF-NEO-RHF, options

enables the density fitting NEO-RHF program. Through the density fitting approximation in the electronic subsystem as well as the Coulomb coupling the computational scaling for small to mid-size systems is drastically reduced. The calculation parameters can be fine tuned with the options described in :doc:`the SCF program <the_scf_program>` section and :doc:`density fitting <density_fitting>` section. However, NEO calculations require some additional parameters explained in the following.

.. _nuclear-electronic_orbital_method--local-density-fitting-neo-hartree-fock:

Local density fitting NEO-Hartree-Fock
======================================

Using

.. code-block:: text

   LDF-NEO-RHF, options

enables the local density fitting NEO-RHF program. The local density fitting of the electronic subsystem leads to further speed-ups in particular for large molecular systems. The specific parameters for local density fitting can be adjusted with the options given in the `the SCF program#local density fitting Hartree-Fock <the_scf_program.html#local-density-fitting-hartree-fock>`__ section.

.. _nuclear-electronic_orbital_method--density-fitting-neo-dft:

Density fitting NEO-DFT
=======================

The spin-restricted NEO-DFT program with density fitting for electron-repulsion integrals is available through

.. code-block:: text

   DF-NEO-RKS,functional,options
   NEOEPC,epc-functional

Currently only standard grids are supported (``SG1``, ``SG2`` and ``SG3``). The use of ``SG3`` is recommended for its numerical stability. If no grid is defined, the program defaults to ``SG2`` and issues a warning. The DFT functional for electronic exchange and correlation is defined as an option (*functional*), similar to a regular DFT calculation. However, in the case of NEO-DFT one also requires the definition of an electron-proton correlation (epc) functional (*epc-functional*). The program currently supports ``epc17.1``, ``epc17.2``, ``epc18.1`` and ``epc18.2``, as provided through the libxc library. We recommend the use of the epc17.2 functional for NEO-DFT calculations in general.

The definition of the quantum nuclei as well as the thresholds for the convergence of the nuclear cycles follows the same procedure as NEO-HF.

.. _nuclear-electronic_orbital_method--neo-specific-options:

NEO specific options
====================

.. _nuclear-electronic_orbital_method--basis-sets:

Basis sets
==========

The basis definition for NEO calculations must be given accordingly to the following basis block layout

.. code-block:: text

    basis={
    default=minao         #Basis definition for the electronic subsystem
   
    set,nucbas
    default=neo-basis
    H1=pb4-f2             #Basis definition for the nuclear subsystem
   
    set,nucfit
    default=neo-basis
    H1=10s10p10d10f       #Basis definition for the nuclear density fitting
    }

The electronic basis set can be freely chosen from the Molpro basis set library. At the current stage no user defined mixed basis sets are possible within the NEO programs.

The nuclear basis set is defined via the ``nucbas`` keyword. The default basis for nuclear basis sets must be defined in every case as the ``neo-basis``. Afterwards, the selected NEO centers can be assigned with the desired basis set. It is highly recommended to use the specifically tailored `PB basis sets <https://doi.org/10.1063/5.0009233>`__ for multicomponent methods developed by Hammes-Schiffer and coworkers. Note that all NEO centers need to be assigned individually with the same basis set.

The density fitting basis for the nuclear subsystem is defined via the ``nucfit`` keyword. In order to avoid issues in basis set assignments for the classical nuclei, the default basis must be assigned as the ``neo-basis``. Afterwards all NEO centers must be assigned the same fitting basis set (two have been included in the basis library), or a new set must be defined. For the fitting of the PB basis sets the even tempered 10s10p10d10f to 12s12p12d12f12g basis sets are recommended.

.. _nuclear-electronic_orbital_method--neo-centers:

NEO centers
===========

The desired NEO centers must be declared immediately before the NEO computation explicitly via

.. code-block:: text

   qnuc, H1, ...

.. code-block:: text

Additionally, the chosen quantum mechanical nuclei must be given as first atoms in the geometry definition as shown for a water molecule below

.. code-block:: text

   3
   Water molecule with one NEO center
   H1  -3.5008791    1.2736107    0.7596000
   O   -3.9840791    1.3301107   -0.0574000
   H   -4.9109791    1.2967107    0.1521000

.. _nuclear-electronic_orbital_method--starting-options:

Starting options
================

In order to provide suitable starting orbitals for the NEO computation three options can be chosen.

* The first option is to carry out a regular Hartree-Fock computation before the NEO program is called. Thereby, the program reads the electronic orbitals from the default RHF record. In order to give a specific record the **``START``, *record*** keyword in the NEO program input card can be employed.
* The second option is especially beneficial for large systems, since the computational costs of a prior RHF calculation is avoided. One makes use of the natural orbitals from a diagonal density matrix constructed using atomic orbitals. Atomic occupation numbers are employed as electronic starting orbitals. This option can be used via the ``NEOATDEN`` keyword in the NEO program input card. This is only available in NEO-RHF.
* The third option is to start from a prior NEO computation via the **``NEOSTART``, *electronic record*, *nuclear record*** keyword. This can be used as a minimal-basis NEO guess for `the SCF program#handling difficult cases: when the SCF cycle does not converge <the_scf_program.html#handling-difficult-cases-when-the-scf-cycle-does-not-converge>`__.

.. _nuclear-electronic_orbital_method--thresholds:

Thresholds
==========

The thresholds for the NEO computation can be adjusted with the following keywords

* **``NEOTHRE``, *number*** sets the overall NEO energy threshold for SCF convergence
* **``NEOTHRIE``, *number*** sets the energy threshold for the electronic subsystem SCF convergence
* **``NEOTHRIN``, *number*** sets the energy threshold for the nuclear subsystem SCF convergence
* **``NEOTHRIG``, *number*** sets the gradient threshold for both subsystems
* **``NEOTHRID``, *number*** sets the density threshold for both subsystems

For robust convergence it is recommended to use higher thresholds for the SCF computations of both subsystems than the overall NEO energy.

.. _nuclear-electronic_orbital_method--additional-options:

Additional options
==================

* **``NEOIT``, *iterations*** sets the overall NEO cycles
* **``NEORD``, *number*** sets the start for the fast rotational update of the orbitals in LDF-NEO-RHF
* ``NOBLOCKDIAG`` disables the block diagonalization of the nuclear starting guess (this is generally not recommended!!)
* ``NEOMIXBAS`` enables the use of user-defined mixed basis sets (see example for use)

.. _nuclear-electronic_orbital_method--adaptive-neo:

Adaptive NEO
------------

Optimization of quantum nuclei positions with the adaptive NEO approach, where the nuclear centroids are computed on-the-fly during the SCF iterations. This procedure is available by using the

.. code-block:: text

   ADAPTIVE

keyword in the NEO program input card. This approach is so far only available for NEO-RHF calculations.

.. _nuclear-electronic_orbital_method--threshold:

Threshold
=========

The thresholds for the convergence criteria of the nuclear centers during an adaptive NEO computation can be adjusted with the following keyword

* **``ADTHRES``, *number*** sets the convergence threshold for the nuclear centers in atomic units
* **``ADITER``, *number*** sets the initial iteration for the start of the adaptive procedure (default=2)

.. _nuclear-electronic_orbital_method--damping:

Damping
=======

The shift of the nuclear basis function center towards the charge centroid can be damped with the following keyword

* **``ADDUMP``, *number*** sets the damping factor of the nuclear centroid shift

.. _nuclear-electronic_orbital_method--neo-examples:

NEO examples
------------

The first example shows the input of a ``DF-NEO-RHF`` calculation for a water molecule with two NEO centers starting with the ``NEOATDEN`` option and individual thresholds.

.. code-block:: text

   memory,50,m
   gdirect
   nosym
   
   geometry={
   3
   
   H1  -3.5008791    1.2736107    0.7596000
   H2  -4.9109791    1.2967107    0.1521000
   O   -3.9840791    1.3301107   -0.0574000
   }
   
   charge=0
   
   basis={
   default=cc-pvdz
   
   set,nucbas
   default=neo-basis
   H1=pb4-f2
   H2=pb4-f2
   
   set,nucfit
   default=neo-basis
   H1=10s10p10d10f
   H2=10s10p10d10f
   }
   
   qnuc,H1,H2
   
   {df-neo-rhf,maxdis=10,maxit=200,df_basis=cc-pvdz
   neothre,1.d-6
   neothrie,1.d-7
   neothrin,1.d-7
   neothrg,1.d-7
   neothrd,1.d-7
   neoatden}

The second example shows the input of a ``DF-NEO-RKS`` calculation. The grid used is ``SG3``, with the B3LYP functional used for the electron-electron exchange-correlation and epc17.2 for the electron-proton correlation.

.. code-block:: text

   memory,50,m
   gdirect
   nosym
   noextra
   geometry={
   3
   
   H1  -3.5008791    1.2736107    0.7596000
   H2  -4.9109791    1.2967107    0.1521000
   O   -3.9840791    1.3301107   -0.0574000
   }
   charge=0
   basis={
   default=cc-pvdz
   set,nucbas
   default=neo-basis
   H1=pb4-D
   H2=pb4-D
   set,nucfit, context=JKFIT
   default=cc-pvdz
   H1=10s10p10d10f
   H2=10s10p10d10f
   }
   {grid,name=SG2}
   {df-rks,b3lyp,df_basis=cc-pvdz}
   qnuc,H1,H2
   {df-neo-rks,b3lyp,df_basis=cc-pvtz
   NEOEPC,EPC17.2
   }

The following example shows the input of a ``LDF-NEO-RHF`` computation of the same molecule starting from a prior RHF calculation. In this example a :doc:`cube <dump_density_or_orbital_values_cube>` file is requested. This will output the quantum nuclei density.

.. code-block:: text

   memory,50,m
   gdirect
   nosym
   
   geometry={
   3
   
   H1  -3.5008791    1.2736107    0.7596000
   H2  -4.9109791    1.2967107    0.1521000
   O   -3.9840791    1.3301107   -0.0574000
   }
   
   charge=0
   
   basis={
   default=cc-pvdz
   
   set,nucbas
   default=neo-basis
   H1=pb4-f2
   H2=pb4-f2
   
   set,nucfit
   default=neo-basis
   H1=10s10p10d10f
   H2=10s10p10d10f
   }
   
   {rhf}
   
   qnuc,H1,H2
   
   {ldf-neo-rhf,maxdis=10,maxit=200,df_basis=cc-pvdz}
   
   {cube,nuclear.cube;density,2102.2}

The following example shows a NEO calculation, where a user-defined mixed basis set is used. Thereby, the electronic basis set at the quantum nuclei is larger than for regular hydrogen atoms. The use of the ``NEOMIXBAS`` requires the additional definition of the ``elebas`` and ``elefit`` basis sets as shown below.

.. code-block:: text

   memory,50,m
   gdirect
   nosym
   
   geometry={
   3
   
   H1  -3.5008791    1.2736107    0.7596000
   H2  -4.9109791    1.2967107    0.1521000
   O   -3.9840791    1.3301107   -0.0574000
   }
   
   charge=0
   
   basis={
   default=cc-pvtz
   H1=cc-pv5z
   
   set,nucbas
   default=neo-basis
   H1=pb4-f2
   
   set,nucfit
   default=neo-basis
   H1=10s10p10d10f
   
   set,elebas
   default=cc-pvtz
   H1=cc-pv5z
   
   set,elefit,context=jkfit
   default=cc-pvtz
   H1=cc-pv5z
   }
   
   qnuc,H1
   
   {df-neo-rhf,maxdis=10,maxit=1000,df_basis=elefit
   neoatden
   neomixbas
   }

The example below shows the input for an adaptive NEO calculation, where the nuclear basis function centers convergence is set below 1E-5 bohr and a damping factor of 0.5 is applied.

.. code-block:: text

   memory,50,m
   gdirect
   nosym
   
   geometry={
   3
   
   H1  -3.5008791    1.2736107    0.7596000
   H2  -4.9109791    1.2967107    0.1521000
   O   -3.9840791    1.3301107   -0.0574000
   }
   
   charge=0
   
   basis={
   default=cc-pvdz
   
   set,nucbas
   default=neo-basis
   H1=pb4-f2
   
   set,nucfit
   default=neo-basis
   H1=10s10p10d10f
   }
   
   {rhf}
   
   qnuc,H1
   
   {df-neo-rhf,maxdis=10,maxit=500,df_basis=cc-pvdz
   adaptive
   adthres,1.d-5
   addump,0.5
   }

.. _nuclear-electronic_orbital_method--bibliography:

Bibliography
------------

.. _nuclear-electronic_orbital_method--neo-methodology:

NEO methodology
===============

Simon P. Webb, Tzvetelin Iordanov, and Sharon Hammes-Schiffer `Multiconfigurational nuclear-electronic orbital approach: Incorporation of nuclear quantum effects in electronic structure calculations <https://doi.org/10.1063/1.1494980>`__ *J. Chem. Phys.* **2002** *117* (9), 4106–4118.

Fabijan Pavošević, Tanner Culpitt, and Sharon Hammes-Schiffer `Multicomponent Quantum Chemistry: Integrating Electronic and Nuclear Quantum Effects via the Nuclear–Electronic Orbital Method <https://doi.org/10.1021/acs.chemrev.9b00798>`__ *Chemical Reviews* **2020** *120* (9), 4222-4253.

.. _nuclear-electronic_orbital_method--pb-basis-sets:

PB basis sets
=============

Qi Yu, Fabijan Pavošević, and Sharon Hammes-Schiffer `Development of nuclear basis sets for multicomponent quantum chemistry methods <https://doi.org/10.1063/5.0009233>`__ *J. Chem. Phys.* **2020** *152* (24), 244123.

.. _nuclear-electronic_orbital_method--l-df-neo-rhf:

(L)DF-NEO-RHF
=============

Lukas Hasecke, and Ricardo A. Mata `Nuclear Quantum Effects Made Accessible: Local Density Fitting in Multicomponent Methods <https://doi.org/10.1021/acs.jctc.3c01055>`__ *J. Chem. Theory Comput.* **2023** *19* (22), 8223–8233.

.. _nuclear-electronic_orbital_method--df-neo-rks:

DF-NEO-RKS
==========

Lukas Hasecke, Maximilian Breitenbach, Martí Gimferrer, Rainer Oswald, and Ricardo A. Mata `Addressing Anharmonic Effects with Density-Fitted Multicomponent Density Functional Theory <https://doi.org/10.1021/acs.jpca.5c00382>`__ *J. Phys. Chem. A* **2025** *129* (15), 3560-3566.
