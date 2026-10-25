.. raw:: html

   <span id="how-to-use-the-scripts"></span>

.. raw:: html

   <span id="input-file"></span>

.. _instantons--instantons:

Instantons
==========

Instantons can be located within the ring-polymer formalism using the ``INSTANTON`` command:
``INSTANTON[, key1=value, key2=value, …]\\``
These instantons can be used to compute either the thermal reaction rate or the tunnelling splitting between degenerate potential wells. The behaviour can be controlled with the ``splitting`` option. It is a good idea to turn symmetry off (using ``nosym``) during the calculation as the ring-polymer beads do not necessarily share the same symmetry operations as the transition state or well minima.

.. _instantons--thermal-reaction-rates:

Thermal reaction rates
======================

Quantum rate calculations proceed via an instanton which is equivalent to the transition state on the ring-polymer surface. These stationary points are computed using a quasi-Newton saddle-point search with Powell’s Hessian update. Because of the known symmetry of the final geometry (that the ring polymer folds back on itself), only half of the beads need be specified.

The geometry of the transition state should be specified with the ``geometry`` keyword, and the classical TST rate through this point is compared with the rate computed from the instanton. The action of the instanton, its fluctuations and rotations are printed to the output file. Molpro computes the tunnelling factor which is the ratio of these rates and the rate itself can be calculated if the reactant partition function is known. It is necessary to converge the results in the large-:math:`N` limit.

References for the ring-polymer instanton method are:

* J. O. Richardson and S. C. Althorpe. “Ring-polymer molecular dynamics rate-theory in the deep-tunneling regime: Connection with semiclassical instanton theory.” `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3267318>`__ **131**, 214106 (2009).
* J. O. Richardson. “Derivation of instanton rate theory from first principles.” `J. Chem. Phys. <https://dx.doi.org/10.1063/1.4943866>`__ **144**, 114106 (2016).
* A. N. Beyer, J. O. Richardson, P. J. Knowles, J. Rommel and S. C. Althorpe “Quantum tunneling rates of gas-phase reactions from on-the-fly instanton calculations.” *J. Phys. Chem. Lett.* **7**, 4374-4379 (2016).

Upon reaching the ``INSTANTON`` command, Molpro reads in data from the input ``xyz`` file including the temperature and number of beads. :math:`\beta`, :math:`\beta/N` and the bead masses in atomic units are computed and printed to the output file. Next the values of the potential, moments of inertia and frequencies of the transition-state, whose geometry is supplied in the input file, are computed using calls to the procedures ``beadpot`` and ``beadfreq1``. It is also determined whether or not the geometry is linear in order to define the correct rotational partition function. The user must ensure that the transition state is optimized sufficiently using ``optg,root=2`` before the ``INSTANTON`` command. A warning will ensue if this is not the case. An approximate cross-over temperature :math:`\beta_{\text{c}}=2\pi/\hbar\omega_{\text{b}}`, where :math:`\mathrm{i}\omega_{\text{b}}` is the imaginary frequency, below which instantons exist is printed along with the fluctuations of a ring-polymer collapsed at the transition state.

Next begins the instanton optimization. The ring-polymer gradient is computed and, unless it is already sufficiently converged, an initial Hessian using ``beadfreq2``. This does not need to be accurate although it may reduced the number of iterations if it is. At each iteration, the quasi-Newtonian algorithm diagonalizes the Hessian and takes a step upwards in the direction of the lowest eigenmode and downwards in all others. The step length is determined by the gradient and the values of the lowest two eigenvalues and is scaled down if it exceeds ``STEPMAX``. The potential and gradient of the new geometry are then computed using ``beadgrad`` and the Hessian is updated using Powell’s scheme. If the matrix is very large, diagonalization can become the slowest step in this process. In this case the option ``banded`` can be supplied to convert the half-ring-polymer Hessian into banded form which speeds up the computation.

Upon convergence of the gradient or if the maximum number of iterations is reached, the full-ring-polymer Hessian is computed using ``beadfreq3`` and diagonalized. This matrix cannot be computed in banded form. There should be one imaginary mode, zero modes corresponding to translations and rotations and an extra zero mode due to the permutational symmetry of the ring polymer. The normalization constant for this zero mode, :math:`B_N` is computed and should not be zero. The eigenvector corresponding to the imaginary eigenvalue is also computed and printed. If Molpro is run in parallel with :math:`n` processes, the eigenvalues are computed on process 0 and the lowest eigenvector in process :math:`n-1`. Using the instanton’s action and comparing its rotational and vibrational partition functions with those of the collapsed ring polymer, one obtains the tunnelling factor.

.. _instantons--tunnelling-splittings:

Tunnelling splittings
=====================

Instantons used to compute tunnelling splittings are local minima on the ring-polymer surface. They are located using the limited-memory Broyden-Fletcher-Goldfarb-Shanno (L-BFGS) method. All publications describing work using this method should quote at least one of these references:

* J. Nocedal. “Updating quasi-Newton matrices with limited storage”. *Math. Comput.* **35**, 773 (1980).
* D. C. Liu and J. Nocedal. “On the limited memory BFGS method for large scale optimization”. *Math. Program.* **45**, 503 (1989).

The geometry of the well minimum should be specified with the ``geometry`` keyword. The action of the instanton, its fluctuations and the fluctuations about the well minimum are printed to the output file. Molpro computes the tunnelling-matrix element which can be used to construct the tunnelling-splitting pattern for a molecular cluster with two or more degenerate wells as described in the latter of the two references. It is necessary to converge the results in the limit that :math:`\beta\rightarrow\infty` and :math:`\beta/N\rightarrow0`.

References for the ring-polymer instanton method are:

* J. O. Richardson and S. C. Althorpe. “Ring-polymer instanton method for calculating tunneling splittings.” `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3530589>`__ **134**, 054109 (2011).
* J. O. Richardson, S. C. Althorpe and D. J. Wales. “Instanton calculations of tunneling splittings for water dimer and trimer.” `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3640429>`__ **135**, 124109 (2011).

.. _instantons--input-file:

Input file
==========

An input file should be supplied in ``xyz`` format containing the Cartesian coordinates (in Ångstroms) of the beads used to initialize the instanton optimization. A rate calculation requires :math:`N/2` beads, whereas a tunnelling-splitting calculation requires :math:`N`. The first line contains the number of atoms in the system and the second has two numbers: :math:`N`, the number of beads, and :math:`T`, temperature in Kelvin (for the case of a rate calculation) or :math:`\beta`, the reciprocal temperature in atomic units (for the case of a tunnelling-splittings calculation). These two lines appear before the coordinates of each bead which are given one atom per line including the element symbol.

.. _instantons--procedures:

Procedures
==========

A few procedures must be defined. ``beadpot`` defines the method for computing the potential energy of a single bead geometry. ``beadgrad`` gives the method for computing the gradient for a bead using the ``force`` command. ``beadfreq1``, ``beadfreq2`` and ``beadfreq3`` define methods for computing frequencies of the transition state/well minimum, of the initial (pre-optimized) ring-polymer beads and of the final (optimized) beads. Because the procedure ``beadfreq1`` is only called once directly after ``beadpot``, it is not necessary to recalculate the wave-function in this case. For the tunnelling-splitting calculations, ``beadfreq2`` is not used as the L-BFGS optimization proceeds without a Hessian.

.. _instantons--options:

Options
=======

* ``SPLITTING`` runs the tunnelling splitting calculation instead of a rate calculation. The default is False.
* **``INPUT``\ =\ *filename*** file containing initial instanton geometry in format described in section `input file <instantons.html#input-file>`__. The default is initial.xyz.
* **``OUTPUT``\ =\ *filename*** file containing final instanton geometry in format described in section `input file <instantons.html#input-file>`__. The default is final.xyz.
* **``SAVE``\ =\ *filename*** file containing transition-state data, including potential, Hessian eigenvalues and the number of imaginary and zero frequencies. The default is ’.’ in which case no files are read or written.
* **``REACTANT``\ =\ *value*** value of potential (in :math:`E_{\text{h}}`) of reactant states used to scale the instanton action in a rate calculation only. The default is 0.
* **``MAXIT``\ =\ *integer*** maximum number of optimization cycles. The default is 50.
* **``GRADIENT``\ =\ *value*** required accuracy of the optimized ring-polymer gradient. The default is :math:`3 \cdot 10^{-4}`.
* **``STEPMAX``\ =\ *value*** maximum allowed step (in Bohr) in the quasi-Newton instanton optimization. Attempted steps larger than this are scaled down. The default is :math:`0\cdot3` :math:`a_0`.
* **``MSAVE``\ =\ *integer*** number of gradients saved from previous iterations used in the L-BFGS optimization. The default is 3.
* **``SAVEHESS``\ =\ *filename*** file containing bead Hessians. The default is ’.’ in which case no files are written.
* **``READHESS``\ =\ *filename*** reads file containing bead Hessians. The default is ’.’ in which case no files are read.
* ``BANDED`` Uses a banded-matrix eigensolver in the quasi-Newton optimization. The default is False.
* ``DISPLACEMENT`` Run parallel over atomic displacements instead of over beads when calculating bead Hessians. The default is False.

.. _instantons--parallelization:

Parallelization
===============

The ring-polymer instanton approach is naturally parallelized by computing the energies and gradients of each bead on separate processors. It is recommended for the number of processors used to be a factor of the number of beads.

.. _instantons--examples:

Examples
========

Here we give an example for calculating the rate of the :math:`\mathrm{H+H_2\rightarrow H_2+H}` reaction at 250 K using MRCI. The Molpro input file is below and requires also `instanton_initial.xyz <media/examples/instanton_initial.xyz>`__.

.. code-block:: text
   :caption: examples/instanton.inp

   ***, H + H2 instanton
   
   proc beadpot={
   gthresh,gradient=1d-8
   hf
   casscf
   mrci
   }
   
   proc beadgrad={
   beadpot
   force,numerical,dstep=1e-4
   }
   
   proc beadfreq1={
   frequencies
   }
   proc beadfreq2={
   beadpot
   frequencies,forward
   }
   proc beadfreq3={
   beadpot
   frequencies,print=0
   }
   
   symmetry,nosym
   
   geometry={ ! optimized geometry at transition state
       3
    MRCI/VDZ  ENERGY=-1.64651538 ! comment line
    H         -0.9401271688        0.0000000000        0.0000000000
    H          0.0033328462        0.0000000000        0.0000000000
    H          0.9467943226        0.0000000000        0.0000000000
   }
   
   mass,isotope,print
   basis=vdz
   
   instanton, input='instanton_initial.xyz', \\
      output='instanton_final.xyz', reactant=-1.66295138342 \\
   !, save='instanton_ts.dat' \\
   !, readhess='initial.hess' \\
   !, savehess='finial.hess'
   text, $action   $perm   $rotratio   $fluctratio   $tunfac

An example calculation of the tunnelling splitting in the :math:`\mathrm{HO_2}` cluster using UHF is provided by the input below which requires the `splitting_initial.xyz <media/examples/splitting_initial.xyz>`__ input file.

.. code-block:: text
   :caption: examples/splitting.inp

   ***, hydroperoxyl HO2 splitting instanton
   if(NPROC_MPP.gt.1) then
   skipped
   endif
   FILE,2,ho2inst.wfu,new
   
   proc beadpot={
   {uhf;wf,sym=1,spin=1}
   }
   
   proc beadgrad={
   beadpot
   force
   }
   
   proc beadfreq1={
   frequencies
   }
   proc beadfreq3={
   beadpot
   frequencies
   }
   
   geometry={ ! optimized geometry at well minimum
       3
    UHF-SCF002/VDZ  ENERGY=-150.16631226 ! comment line
   H 0.904294157899999895 0.919502897200000113 0
   O 0.681281911699999965 -0.00702956160000003938 0
   O -0.683576069499999939 0.00706386439999998061 0
   }
   
   mass,isotope,print
   basis=vdz
   
   instanton, splitting, input='splitting_initial.xyz', \\
      output='splitting_final.xyz', maxit=200
   table,action,fluctratio,tunsplit*1e9

In both examples, data is saved to a ``.wfu`` file. If another instanton calculation at a different temperature or with a different number of beads is run, some information can be recovered by using ``frequencies,read=5300.2`` in ``beadfreq1``.

.. _instantons--instanton-scripts:

Instanton scripts
=================

Four python scripts are available in Molpro which can ease the calculation of instantons. For usage and options, run the scripts with the -h flag. All scripts are written in python3 and require the use of the vmd.py module. For UNIX based operating systems, the module should be placed in a directory included in ``$PYTHONPATH``, while the other scripts should be placed somewhere in ``$PATH``.

All scripts require the *numpy*, *scipy* and *matplotlib* libraries. These can be installed via pip3:

.. code-block:: text

   pip3 install numpy scipy matplotlib

.. _instantons--how-to-use-the-scripts:

How to use the scripts
======================

**initial_instanton.py** creates an initial guess for a half-instanton configuration for a given number of beads. It uses the transition state geometry and the mass-weighted eigenvector corresponding to the imaginary mode. As a result you must have a Molpro xml file as a result of a previous frequencies calculation.

Example:

.. code-block:: text

   python3 initial_instanton.py file.xml -o initial.xyz -s 0.1 -N 16 -T 300

This will generate 16 bead geometries in the file ’initial.xyz’ and labeled by the given temperature. A sensible temperature should be less than the cross-over temperature. If a temperature is not supplied, the -g option can be given and a suitable estimate temperature will be generated; this is chosen to be at least 20 Kelvin below the cross-over temperature. See ref for more details on how the bead geometries are generated. Choosing an s value should be done with trial and error to give a small but observable stretch. However s=0.1 is often good enough.

For more information on how the initial bead geometries are calculated, see:

A. N. Beyer, J. O. Richardson, P. J. Knowles, J. Rommel and S. C. Althorpe “Quantum tunneling rates of gas-phase reactions from on-the-fly instanton calculations.” *J. Phys. Chem. Lett.* **7**, 4374-4379 (2016).

**interpolate_instaton.py** creates an initial guess for a half-instanton configuration using inputs of a previously optimized instanton for a different number of beads or different temperature. Note that the half-instanton will only have N/2 beads. If temperature is not given, the same is retained from the input file. If the number of beads is not given, the previous number is doubled. This script will also interpolate the Hessians of each bead if provided with the correct file (use the hessfile option in the input to save the final bead Hessians).

Example:

.. code-block:: text

   python3 interpolate_instanton.py final.xyz -o initial.xyz -N 32 -T 300

Assuming ’final.xyz’ has 16/2 (8) bead geometries, this will place 32/2 (16) bead geometries into ’inital.xyz’ labeled with the temperature.

**plot_instanton.py** uses matplotlib to plot the reaction pathway. An output file can be generated which can then be plotted using other plotting programs (eg. gnuplot). It uses a set of optimized bead geometries and the final bead energies contained in a Molpro xml file. This is the potential along the mass-weighted path length and so also uses the atomic masses also contained in a Molpro xml file.

Example:

.. code-block:: text

   python3 plot_instaton.py final.xyz file.xml -o instanton.plot

The -r flag can be used to specify the reactant energy to scale the plot with respect to this number.
