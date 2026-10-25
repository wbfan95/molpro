.. raw:: html

   <span id="ccsd-t-f12"></span>

.. raw:: html

   <span id="choice-of-domains"></span>

.. raw:: html

   <span id="closed-shell-correlation-methods"></span>

.. raw:: html

   <span id="convergence-thresholds"></span>

.. raw:: html

   <span id="density-fitting-approximations"></span>

.. raw:: html

   <span id="explicitly-correlated-methods"></span>

.. raw:: html

   <span id="extended-domains"></span>

.. raw:: html

   <span id="geometry-optimization"></span>

.. raw:: html

   <span id="how-to-run-molpro"></span>

.. raw:: html

   <span id="integral-direct-calculations"></span>

.. raw:: html

   <span id="local-correlation-treatments"></span>

.. raw:: html

   <span id="localization"></span>

.. raw:: html

   <span id="memory-control"></span>

.. raw:: html

   <span id="method-and-wavefunction-specification"></span>

.. raw:: html

   <span id="options"></span>

.. raw:: html

   <span id="options-for-selection-of-pair-classes"></span>

.. raw:: html

   <span id="orbital-localization"></span>

.. raw:: html

   <span id="osv-calculations"></span>

.. raw:: html

   <span id="restarting-calculations"></span>

.. raw:: html

   <span id="the-general-ansatz-tt-ansatz-3c-full"></span>

.. raw:: html

   <span id="variables"></span>

.. raw:: html

   <span id="wave-function-ans-tze"></span>

.. _quickstart--quickstart:

Quickstart
==========

The intention of this *quickstart* section is to get you started quickly. Most input is explained using simple examples. Default values are used as much as possible to make the inputs very simple. Naturally, this is by no means an exhaustive description of Molpro. A more systematic and complete explanation of all features of Molpro can be found in the later sections of the manual. We strongly recommend that you read the introductory chapters of the reference manual once you have gained a basic feeling how things are done with Molpro. In particular, the first chapters of the reference manual explain in more detail the use of symmetry, and the data structures (files and records) in Molpro.

Very simple and mostly self explanatory input for HF, DFT, and most wavefunction correlation methods is described in the following section. Alternatively, a new Molpro user can use the iMolpro graphical user interface, which allows to create inputs for DFT and single-reference methods as well.

.. _quickstart--simple-input:

Simple input
============

it is possible to write Molpro input for DFT and single-reference methods in a single line. A simple DFT geometry calculation can be done as follows:

``run DF-KS,b3lyp geometry=h2o.xyz basis=avtz``

where avtz is a short name for the aug-cc-pVTZ basis, and
the geometry is provided in an external file holding the x,y,z coordinates in Angstrom. Alternatively, the geometry can be given as z-matrix in curly brackets.

The prefix DF- turns on density fitting approximations for the integrals, which is strongly recommended for efficiency, in particular for larger molecules.

A most simple example for a CCSD(T) input is:

``run CCSD(T) geometry=h2o.xyz basis=avtz``

The entries can come in any order, for example

``run basis=avtz method=CCSD(T) geometry=h2o.xyz``

works as well. The key "method=" is optional. Entries on the "run" command must be separated by blank or semicolon (;) (but semicolon cannot follow ``run``). Some commands or directives can have options, which are separated by commas. Blanks before and after commas, semicolons, or equal signs (:math:`=`) are ignored. Input can be given in upper or lower or mixed case.

The run command line can optionally be split to two or multiple lines between the entries that are separated by blank or semicolon. In this case the whole block must be embraced by curly brackets, e.g.

``{run CCSD(T)\\``

.. code-block:: text

    geometry=h2o.xyz\\
    basis=avtz}''

In detail, the following methods are possible:

.. code-block:: text

    <code>

rhf          !closed or open-shell spin-restricted Hartree-Fock
uhf          !closed or open-shell spin-unrestricted Hartree-Fock
rks          !closed or open-shell spin-restricted Kohn-Sham DFT
uks          !closed or open-shell spin-unrestricted Kohn-Sham DFT
mp2          !second-order Moeller-Plesset perturbation theory
mp3          !third-order Moeller-Plesset perturbation theory
mp4          !fourth-order Moeller-Plesset perturbation theory
cc2          !second-order coupled-cluster approximation (can compute excitation energies)
cisd         !single-reference singles and doubles configuration interaction
cepa         !single-reference singles and doubles coupled-electron pair approximation
ccsd         !coupled cluster with singles and doubles
ccsd(t)      !coupled cluster with singles and doubles and perturbative treatment of triples
bccd         !Brueckner coupled cluster with doubles
bccd(t)      !Brueckner coupled cluster with doubles and perturbative treatment of triples
qcisd        !Quadratic configuration interaction with singles and doubles
qcisd(t)     !Quadratic configuration interaction with perturbative treatment of triples
pno-lmp2     !local pno-lmp2
pno-lccsd    !local coupled cluster with singles and doubles
pno-lccsd(t) !local coupled cluster with singles, doubles, and perturbative triples
multi        !mcscf/casscf
casscf       !same as multi
mrci         !multi-reference CI with internally contracted doubles
mrcic        !multi-reference CI with internally contracted singles and doubles
caspt2       !caspt2
nevpt2       !n-electron valence perturbation theory
rs2c         !same as caspt2
rs2          !old less contracted version of caspt2

All higher order methods contain the lower-level ones. For example, ccsd(t) contains HF, MP2, and CCSD, and MRCI contains CASPT2.

``For larger molecules, it is advisable to use density fitted methods (activated by the prefix DF-). Note that in some other programs this is denoted RI-approximation, but in Molpro RI refers to resolution of the identity approximations of the many-electron integrals in F12 methods. This is distinct from DF-approximations of standard 2-electron Coulomb integrals.``

The following ones are efficiently implemented:

.. code-block:: text

    <code>

df-rhf       !closed or open-shell spin-restricted Hartree-Fock
df-uhf       !closed or open-shell spin-unrestricted Hartree-Fock
df-rks       !closed or open-shell spin-restricted Kohn-Sham DFT
df-uks       !closed or open-shell spin-unrestricted Kohn-Sham DFT
df-mp2       !second-order Moeller-Plesset perturbation theory
df-cc2       !second-order coupled-cluster approximation
df-multi     !mcscf/casscf
df-casscf    !same as df-multi
df-caspt2    !caspt2
df-nevpt2    !n-electron valence perturbation theory
df-rs2c      !same as df-caspt2
df-rs2       !old less contracted version of caspt2

PNO methods are density fitted in any case.

For most listed correlation methods, explicitly correlated versions are available by appending -F12 to the command [e.g. ccsd(t)-f12, or pno-lccsd(t)-f12]. ``The use of F12 methods is strongly recommended since the basis set error is much reduced.`` Appropriate basis sets for such calculations are avtz or avtz-f12. F12 is not available for MRCIC and NEVPT2.

Method, geometry, and basis set are compulsory for running a calculation. By default, only a single energy calculation is done. However, other calculation types can be requested by specifying one of the following directives (the parts in brackets can be omitted or are optional):

.. code-block:: text

    <code>

optg[eometry]                    !optimize the geometry
freq[quencies]                   !optimize the geometry and compute the harmonic vibrational frequencies (wavenumber).
extrapolate,basis=basis1:basis2  !carry out a basis set extrapolation using basis1 and basis2.
interact[,do_nocp]               !automatically compute CP-corrected interaction energies for a dimer.

.. code-block:: text

                                    !If do_nocp is given, the CP-uncorrected values are computed as well.

Note that optg and freq are not possible for PNO methods, since no analytical energy gradients are available.

The following further options are can be given on the run line (alternative values separated by \|):

.. code-block:: text

   symmetry=specifications          !specify the symmetry planes
   orient[=mass|charge]             !orient the molecule according to symmetry and origin either at the center or mass or charge (default mass)
   charge=value                     !total charge of the molecule (default 0)
   spin=value                       !number of open-shell orbitals, i.e. 1 for doublet, 2 for triplet etc.
   wfsym=value                      !specifies the symmetry (irreducible representation) of the wavefunction. See manual for details.
   states=number                    !Number of states in multi and mrci
   thre=value                       !energy convergence threshold (default 1d-6). 'energy' is an alias for thre.
   thrg=value                       !gradient threshold in geometry optimisations (default 3d-4). 'gradient' is an alias for thrg.
   functional=name                  !DFT functional
   disp=d3|d4                       !DFT dispersion correction
   dk2|dk3                          !Douglas-Kroll Hess second or third order Hamiltonian
   dkho=n                           !n-th order Douglas-Kroll Hess Hamiltonian

In addition, any valid options for individual methods, as described in the manual, can be given after the command or directives (separated by commas). An example for a DFT frequency calculation with density fitting is

Some further examples:

1.) DFT frequency calculation with density fitting:

``run df-ks functional=b3lyp geometry=h2o.xyz basis=def2-tzvp freq``

This could also be written as

``run df-ks,b3lyp geometry=h2o.xyz basis=def2-tzvp freq``

The geometry is optimised before computing the hessian.

2.) PNO-LCCSD(T)-F12 calculation of an intermolecular interaction energy:

``run pno-lccsd(t)-f12,domopt=tight+ geometry=h2odim.xyz basis=avtz,h=vtz interact``

This automatically implies to run a df-hf calculation beforehand.

3.) CCSD(T) with basis set extrapolation:

``run ccsd(t) geometry=h2o.xyz extrapolate,basis=avtz:avqz``

This automatically implies HF calculations before the CCSD(T) ones.

4.) Internally contracted MRCI with a CASSCF reference function:

``run mrci geometry=h2o.xyz basis=avqz``

5.) Internally contracted CASPT2 with a CASSCF reference function:

``run caspt2 geometry=h2o.xyz basis=avtz``

6.) TDDFT excitation energies:

``run df-tddft,states=[4.1,4.2,4.3,4.4] functional=b3lyp basis=avtz geometry=h2o.xyz``

This computes 4 excited states for each of the four IRREPS of C2v.

7.) CC2 excitation energies:

``run df-cc2,states=[4.1,4.2,4.3,4.4] basis=avtz geometry=h2o.xyz``

This computes the ground state and 4 excited states for each of the four IRREPS of C2v.

8.)CASSCF calculation using state-averaging over three state symmetries:

``run casscf wfsym=[2,3,1] spin=1 geometry={O;H,O,1.83}``

This carries out a state-averaged CASSCF calculation for symmetries 2,3,1 (:math:`^2\Pi_x`,\ :math:`^2\Pi_y`, and :math:`^2\Sigma^+`).

9. )MRCI calculation using state-averaged CASSCF reference functions:

``run mrci wfsym=[2,3,1] spin=1 geometry={O;H,O,1.83}``

In this case first a state-averaged CASSCF calculation for symmetries 2,3,1 (:math:`^2\Pi_x`,\ :math:`^2\Pi_y`,  and :math:`^2\Sigma^+`) is carried out. Subsequently an MRCI calculation is done for each state symmetry separately.

10.) Several run command lines can follow each other. For example, compute the lowest ionisation potential of H2O using MRCI:

.. code-block:: text

   run mrci basis=vtz geometry=h2o.xyz  !casscf/mrci for neutral ground state
   eci=energy                           !save mrci energy in variable eci
   eda=energd                           !save mrci+q (Davidson corrected) energy in variable eda
   run mrci charge=1 wfsym=3 spin=1     !calculation for 2B2 state
   ipci=(energy-eci)*toev               !compute mrci ionization potential in ev  
   ipda=(energd-eda)*toev               !compute mrci+q ionization potential in ev

11.) It is also possible to combine the run command with other standard molpro input, for example:

.. code-block:: text

   geometry={O;                 !Z-matrix for water
             H1,O,R;
             H2,O,R,H1,THETA}
   basis=vtz                    !use VTZ basis
   R=0.96 Ang                   !start bond distance
   Theta=104                    !start bond angle
   
   run mp2 optg                 !optimize MP2 energy
   mp4                          !do single-point MP4 at MP2 geometry
   ccsd(t)                      !do single-point CCSD(T) at MP2 geometry

The following sections give more basic information about carrying electronic structure calculations with Molpro.

.. _quickstart--how-an-ab-initio-calculation-works:

How an ab initio calculation works
==================================

The electronic structure of molecules can be treated only by quantum mechanics, since the electrons are very quickly moving particles. Of course, this manual cannot teach you the underlying theory, and it is assumed that you are familiar with it. We just want to remind you of some basic approximations, which are made in any *ab initio* calculation, independent of which program is used.

Firstly, the Born-Oppenheimer approximation is applied, which means that the nuclear and electronic motions are decoupled and treated separately (in some cases, non-adiabatic couplings are taken into account at a later stage). Thus, each electronic structure calculation is performed for a fixed nuclear configuration, and therefore the positions of all atoms must be specified in an input file. The *ab initio* program like Molpro then computes the electronic energy by solving the electronic Schrödinger equation for this fixed nuclear configuration. The electronic energy as function of the 3N-6 internal nuclear degrees of freedom defines the potential energy surface (PES). The PES is in general very complicated and can have many minima and saddle points. The minima correspond to equilibrium structures of different isomers or molecules, and saddle points to transition states between them. The aim of most calculations is to find these structures and to characterize the potential and the molecular properties in the vicinity of the stationary points of the PES.

Secondly, the electronic Schrödinger equation cannot be solved exactly, except for very simple systems like the hydrogen atom. Therefore, the electronic wavefunction is represented in certain finite basis sets, and the Schrödinger equation is transformed into an algebraic equation which can be solved using numerical methods. There are two classes of approximations: one concerning the choice of basis functions to represent the one-electron functions called *molecular orbitals*, and one concerning the choice of :math:`N`\ –electron functions to represent the many-electron electronic wavefunction.

In most programs, and also in Molpro, Gaussian basis functions are used to approximate the molecular orbitals, since the required integrals can be computed very quickly in this basis. Many optimized basis sets are available in the Molpro *basis set library*, and in most cases the basis set can be selected using a simple keyword in the input.

The many-electron wavefunction for the molecule is represented as a linear combination of antisymmetrized products (Slater determinants) of the molecular orbitals. In a *full configuration interaction* calculation (FCI) all possible Slater determinants for a given orbital basis are used, and this gives the best possible result for the chosen one-electron basis. However, the number of Slater determinants which can be constructed is enormous, and very quickly increases with the number of electrons and orbitals. Therefore, approximations have to be made, in which the wavefunction is expanded in only a subset of all possible of Slater determinants (or configuration state functions (CSFs), which are symmetry adapted linear combinations of Slater determinants).

Once such approximations are introduced, it matters how the orbitals are determined. The simplest choice is to use a single Slater determinant and to optimize the orbitals variationally. This is the *Hartree-Fock* (HF) *self consistent field* (SCF) method, and it is usually the first step in any *ab initio* calculation.

In the Hartree-Fock approximation each electron moves in an average potential of the remaining electrons, but has no knowledge of the positions of these. Thus, even though the Coulomb interaction between the electrons is taken into account in an averaged way, the electrons with opposite spin are unable to avoid each other when they come close, and therefore the electron repulsion is overestimated in Hartree-Fock. The purpose of post-Hartree-Fock *electron correlation* methods is to correct for this by taking the instantaneous correlation of the electrons into account. The corresponding energy lowering is called *electron correlation energy*. There are many different methods available and implemented in Molpro to approximate and optimize the wavefunction, for instance Møller-Plesset (MP) perturbation theory, configuration interaction (CI), or coupled cluster (CC) methods. Also density functional (DFT) methods take into account electron correlation, even though in a less systematic and less well defined way than *ab initio* methods.

One point of warning should be noticed here: electron correlation treatments require much larger one-electron basis sets than Hartree-Fock or DFT to yield converged results. Such calculations can therefore be expensive. For a fixed basis set, a correlation calculation is usually much more expensive than a HF calculation, and therefore many unexperienced people are tempted to use small basis sets for a correlation calculation. However, this is not reasonable at all, and for meaningful calculations one should at least use a triple-zeta basis with several polarization functions (e.g. cc-pVTZ). Using explicitly-correlated methods discussed later, the basis set problem is much alleviated.

Finally, it should also be noted that the HF approximation, and all single reference methods which use the HF determinant as zeroth order approximation, are usually only appropriate near the equilibrium structures. In most cases they are not able to dissociate molecular bonds correctly, or to describe electronically excited or (nearly) degenerate states. In such cases multireference methods, which use a multiconfiguration SCF wavefunctions (MCSCF) as zeroth order approximation, offer a reasonable alternative. Complete active space SCF (CASSCF) is a special variant of MCSCF. In Molpro various multireference electron correlation methods are implemented, e.g., multireference perturbation theory (MRPT, CASPT2) and multireference configuration interaction (MRCI), and variants of these such as multireference coupled-pair functional (MR-ACPF).

As you will see, it is quite easy to run an electronic structure calculation using Molpro, and probably you will have done your first successful run within the next 10 minutes. However, the art is to know which basis set and method to use for a particular problem in order to obtain an accurate result for a minimum possible cost. This is something which needs a lot of experience and which we cannot teach you here. We can only encourage you not to use Molpro or any other popular electronic structure program simply as a black box without any understanding or critical assessment of the methods and results!

Literature: `//Introduction to Computational Chemistry//, F. Jensen, Wiley, 2006 <http://www.amazon.com/Introduction-Computational-Chemistry-Frank-Jensen/dp/0470011874/ref=ed_oe_p>`__

.. _quickstart--how-to-run-molpro:

How to run Molpro
=================

In order to run Molpro you have first to write an input file. This can be done in any directory of your choice. Input files can have any name, but it is best to avoid using a file name with extension ``.out``. Furthermore, the name must not contain parenthesis, brackets, or other special characters like exclamation marks (!), question marks (?), slashes (/), backslashes (\), blanks( ), equality signs(:math:`=`), commas (,), semicolons (;), asterisks (\*), or any kind of quotes.  It is often convenient to name the input file as ``h2o.inp``, ``benzene.inp``, depending on the molecule, or whatever you like.

Simple examples for input files will be given in the following sections. Once the input file is ready, a Molpro calculation can be started using the ``molpro`` command. Assume the input file is called ``h2o.inp``. The command to run Molpro is then simply

``molpro h2o.inp &``

This will create an output file ``h2o.out``, i.e. the extension ``.inp`` is replaced by ``.out``. The same would happen with any other extension, e.g., ``h2o.com``, ``h2o.input``, ``h2o.test`` would all produce the output in ``h2o.out``. If ``h2o.out`` already exists, the old output will be moved to a backup directory that is, by default, created with the name ``h2o.d``. In this way old outputs are not lost. This mechanism can be disabled using the ``-s`` option:

``molpro -s h2o.inp &``

would not save an existing output file but simply overwrite it. If you want to give your output a different name than the default one, you can use the ``-o`` option, for instance

``molpro -o water.output h2o.inp &``

As well as producing the ``.out`` file, a structured XML file is created with suffix ``.xml``. This file can be useful for automated post-processing of results, for example graphical rendering by :doc:`gmolpro <gmolpro_graphical_user_interface>`.

There are many other options for the ``molpro`` command, most of which, however, do not often need to be specified. You can find a full description in the Molpro reference manual. Some of the more important ones are

- The amount of memory Molpro is allowed to use can be specified using the ``-m`` option, e.g., ``molpro -m 4M h2o.inp`` & This means that 4 megawords (MW) of memory are allocated by molpro (see also ``memory`` input card, section `memory control <quickstart.html#memory-control>`__.
- For running in parallel (assuming that the program has been suitably compiled), ``molpro -n 8 h2o.inp`` & will run 8 cooperative processes. Depending on how the program has been built, this will result in 7- or 8-way parallel execution.
- Optionally, but not by default, it is possible so specify one or more named files in the input, and these are used by the program to store intermediate parameters and results, that can be used to restart (see section `restarting calculations <quickstart.html#restarting-calculations>`__). If nothing is given in the input, these files are still present, but they are temporary, and disappear at the end of the job. For performance reasons, the program runs in scratch directory, for example a high-performance file system. By default, the location of this directory is ``/tmp/$USER``, or taken from the environment variable TMPDIR (if set), but it can be controlled using the ``-d`` option, for example ``molpro -d /scratch/$USER h2o.inp`` & At the end of the job, the named files are copied to a permanent location. The most important file for a restart is file 2, which contains the wave function information (cf. section `restarting calculations <quickstart.html#restarting-calculations>`__). By default, this file is copied into the directory $HOME/wfu, but this directory can be changed with the -W option. At the beginning of the job, if appropriate files exist in the permanent location, they are copied in to the scratch directory.

.. _quickstart--how-to-prepare-an-input-file:

How to prepare an input file
============================

As explained in the introduction, the input file should contain the following minimum information.

* Geometry specification.
* Specification of one-electron basis set (although there is a default).
* Specification of the method to compute the many-electron wavefunction. Several calculations of different type can follow each other.

We will consider these three in turn.

All input can be given in upper or lower case and in free format. Most input lines start with a keyword, which is followed by numbers or other specifications (options). The different entries on each line should be separated by commas (see next section for more explanation about this).

.. _quickstart--geometry-specification:

Geometry specification
======================

The simplest way to specify the coordinates of the atoms is to use cartesian coordinates and the *XYZ* input format, which is standard in many programs. In this case the geometry input looks as follows (example for formaldehyde).

.. code-block:: text

   geometry={
      4
     FORMALDEHYDE
   C          0.0000000000        0.0000000000       -0.5265526741
   O          0.0000000000        0.0000000000        0.6555124750
   H          0.0000000000       -0.9325664988       -1.1133424527
   H          0.0000000000        0.9325664988       -1.1133424527
   }

As seen in the example, the geometry is specified within the *geometry block*, enclosed by ``geometry={`` and ``}``. The first line of the *xyz* geometry block holds the number of atoms (free format). The second line is an arbitrary title. Finally there is one line for each atom specifying the cartesian coordinates (:math:`x, y, z`) in Ångstrøm. For simplicity, the first two lines can also be omitted.

Alternatively, the geometry can be specified in the *Z–matrix* form, which is also used in many other programs. In this case, the geometry is defined by distances and angles. This is a little more involved, and here we give only a simple example, again for formaldehyde.

.. code-block:: text

   angstrom
   geometry={
   C
   O   C  1.182
   H1  C  1.102  O  122.1789
   H2  C  1.102  O  122.1789  H1  180
   }

Here, 1.182 and 1.102 are the C-O and the C-H bond distances, respectively. 122.1789 is the H-O-C angle, and 180 is the angle between the H1-C-O and H2-C-O planes (dihedral angle). Note that by default the bond distances are in atomic units (bohr), but one can give the ``angstrom`` keyword to use Ångstrøm.

As an alternative to the *xyz* input explained above, it is also possible to specify cartesian coordinates in a Z–matrix. In this case the form is

.. code-block:: text

   angstrom
   geometry={
   C,,        0.0000000000 ,     0.0000000000 ,    -0.5265526741
   O,,        0.0000000000 ,     0.0000000000 ,     0.6555124750
   H,,        0.0000000000 ,    -0.9325664988 ,    -1.1133424527
   H,,        0.0000000000 ,     0.9325664988 ,    -1.1133424527
   }

Again, atomic units are the default, other than for the *xyz* input, where the coordinates need to be given in Ångstrøm. In order to use Ångstrøm, the ``angstrom`` command must be given before the geometry block.

Instead of constant numbers it is also possible to use variables in the Z–matrix input. For instance, the input for formaldehyde can be written as

.. code-block:: text

   geometry={
   C
   O  , C , rco
   H1 , C , rch , O , hco
   H2 , C , rch , O , hco , H1 , 180
   }
   
   rco=1.182 Ang
   rch=1.102 Ang
   hco=122.1789 Degree

The values of the variables can be changed in the course of the calculations, so that calculations can be performed for different geometries in one run. This will be explained in more detail later.

By default, the program repositions and rotates the molecule so that the coordinate axes have the centre of mass of the molecule as origin, and are aligned with the principal inertial axes. This behaviour is usually what is required, in order that the program can recognize and exploit point-group symmetry, but can be changed through parameters specified on the ``ORIENT`` command (see manual). By default, the program tries to find and use the maximum abelian point-group symmetry, but this behaviour can be controlled using the ``SYMMETRY`` command (see manual).

.. _quickstart--basis-set-specification:

Basis set specification
=======================

In many cases the one-electron basis set can be specified in the simple form

``basis=name``

where *name* refers to the basis set name in the library. You can find all possible basis sets on the Molpro Web page. Popular and often used for high-level calculations are the correlation-consistent polarized basis sets of Dunning and coworkers, denoted ``cc-pVDZ`` (double zeta), ``cc-pVTZ`` (triple zeta), ``cc-pVQZ`` (quadruple zeta), ``cc-pV5Z`` (quintuple zeta). These names can be used directly or abbreviated by ``VDZ``, ``VTZ``, ``VQZ`` and so on. For computing certain properties like electron affinities, polarizabilities, or intermolecular potentials additional diffuse basis functions are needed, and such functions are included in the augmented correlation-consistent basis sets, denoted ``aug-cc-pVDZ``, ``aug-cc-pVTZ`` etc. These names can be abbreviated by ``AVDZ``, ``AVTZ``, ``AVQZ`` etc.

Another popular choice are the Gaussian basis sets of Pople and coworkers, e.g. ``6-31G**`` (double zeta), ``6-311G(2DF,2PD)`` (triple zeta), ``6-311G++(2DF,2PD)`` (augmented triple zeta) etc. It should be noted here that by default Molpro uses spherical harmonics (:math:`5d`, :math:`7f` etc), while ``Gaussian`` uses cartesian functions (:math:`6d`, :math:`10f` etc). This yields slightly different energies. Cartesian functions can also be used in Molpro, but then the keyword

``cartesian``

has to be given before the basis set specification.

It also possible to use different basis sets for different atoms. In this case the simplest input reads for example

``basis,c=vtz,o=avtz,h=vdz``

Basis sets can also be specified manually (exponents and contraction coefficients). Refer to the Molpro reference manual for details.

If no basis set is specified at all, Molpro uses ``cc-pVDZ``, but this does not mean that this is a sensible choice!

.. _quickstart--method-and-wavefunction-specification:

Method and wavefunction specification
=====================================

After defining the geometry and basis set (in any order) one has to specify the methods to be used. This is simply done by keywords, which are normally the same as the usual abbreviations for the methods (``HF`` for Hartree-Fock, ``MP2`` for second-order Møller-Plesset perturbation theory, or ``CCSD(T)`` for coupled-cluster with singles and doubles and perturbative triples. In most cases, the first step is a Hartree-Fock calculation, in which the molecular orbitals to be used in subsequent electron correlation treatments are optimized. An arbitrary number of different methods can be executed after each other, just by giving the corresponding keywords. For example

.. code-block:: text

   geometry={...}
   basis=...
   hf        !orbital optimization using HF
   mp2       !MP2 calculation using the HF orbitals
   mp4       !MP4 calculation using the HF orbitals
   ccsd(t)   !CCSD(T) calculation using the HF orbitals

Note, however that MP2 is part of MP4 and CCSD, and therefore the mp2 calculation in the above input is redundant.

.. _quickstart--variables:

Variables
=========

Molpro stores all important results in variables. For example, the Hartree-Fock program sets the variables ``ENERGY, DMX, DMY, DMZ``, holding the final energy and dipole moments. These variables can be used for further analysis. For a list of variables set by other programs see section `variables <quickstart.html#variables>`__. Variables can be used in expressions, quite similar to fortran.

For example, it is possible to compute a reaction energy in one job. Let’s take CO + H\ :math:`_2` :math:`\rightarrow` H\ :math:`_2`\ CO as a simple example.

.. code-block:: text

   ***,example for reaction energy
   
   basis=avtz               !basis set (used for all molecules)
   
   geometry={c;o,c,2.13}    !geometry for CO
   hf                       !do Hartree-Fock calculation
   ccsd(t)                  !ccsd(t) calculation
   e_co=energy              !save energy for the CO molecule
   
   geometry={h1;h2,H1,1.4}  !geometry for H2
   hf                       !do Hartree-Fock calculation
   ccsd(t)                  !ccsd(t) calculation
   e_h2=energy              !save energy for the CO molecule
   
   geometry={               !geometry for H2CO
   C
   O  , C , rco
   H1 , C , rch , O , hco
   H2 , C , rch , O , hco , H1 , 180
   }
   
   rco=1.182 Ang
   rch=1.102 Ang
   hco=122.1789 Degree
   hf                       !do Hartree-Fock calculation
   ccsd(t)                  !ccsd(t) calculation
   e_h2co=energy            !save energy for H2CO
   
   de=(e_h2co-e_h2-e_co)*tokJ   !reaction energy in Kilojoule.

.. _quickstart--hartree-fock:

Hartree-Fock
------------

.. _quickstart--closed-shell-hartree-fock-calculations:

Closed-shell Hartree-Fock calculations
======================================

The Hartree-Fock program is invoked by the command

``hf``

The program will then first compute the one-and two-electron integrals and store these on disk. Once this step is completed, the self-consistent field calculation, which is iterative, is carried out, using the precomputed integrals (for integral-direct calculations, in which the integrals are not stored but recomputed whenever needed, see section `Integral-direct calculations <quickstart.html#integral-direct-calculations>`__).

Now you are ready to try your first Molpro calculation. The complete input for a HF calculation for formaldehyde is

.. code-block:: text

   ***,formaldehyde
   print,basis,orbitals   ! this is optional: print the basis set and
                          ! the occupied orbitals
   geometry={             ! define the nuclear coordinates
   C
   O  , C , rco
   H1 , C , rch , O , hco
   H2 , C , rch , O , hco , H1 , 180
   }
   
   rco=1.182 Ang
   rch=1.102 Ang
   hco=122.1789 Degree
   
   basis=vdz              ! Select basis set
   hf                     ! Invoke Hartree-Fock program
   ---

The first line, starting with ``**`` is optional and is used to specify a title. The last line, ``—`` is also optional. This indicates the end of the input; any further input after ``—`` is ignored. Any text written after an exclamation mark is treated as comment and also ignored. Blanks and blank lines have no effect.

If you inspect the output, you will find that Molpro detected that the molecule has :math:`C_{2v}` symmetry, and that there are 5 orbitals belonging to the irreducible representation :math:`a_1`, one belonging to :math:`b_1`, and two to :math:`b_2`. In Molpro the irreducible representations are numbered, and in the :math:`C_{2v}` group the numbering is 1–4 for :math:`a_1`, :math:`b_1`, :math:`b_2`, and :math:`a_2`, respectively. The third orbital in symmetry :math:`a_1` is denoted 3.1, the second orbital in symmetry :math:`b_2` is denoted 2.3. Please take a little time to study the output in order to understand these conventions.

In the current case, Molpro has worked out the number of occupied orbitals in each symmetry automatically according to the Aufbau principle. This works in most but not all cases. You can specify the number of occupied orbitals in each symmetry using the ``occ`` directive. In the current case, it would read

``occ,5,1,2``

and the meaning of this should be quite obvious from the above.

If special directives are given for a command, like above ``occ`` is a directive for command ``hf``, the command and the associated directives have to be enclosed by curly brackets, e.g.

.. code-block:: text

   {hf                     ! Invoke Hartree-Fock program
   occ,5,1,2}              ! Specify number of occupied orbitals in each irrep

This is called a command block. The curly brackets are needed to avoid ambiguities, since some directives can also be used outside command blocks. Please refer to the manual for more details.

Each command or directive can either begin on a new line, or be separated by semicolons. For instance

.. code-block:: text

   {hf;occ,5,1,2}

is equivalent to the previous example.

.. _quickstart--open-shell-hartree-fock-calculations:

Open-shell Hartree-Fock calculations
====================================

In the above example all orbitals are doubly occupied, and therefore the total symmetry of the ground state wavefunction, which is the direct product of the spin-orbital symmetries, is :math:`A_1`. Since all electrons are paired, it is a singlet wavefunction, :math:`^1A_1`.

Even though most stable molecules in the electronic ground states are closed-shell singlet states, this is not always the case. Open-shell treatments are necessary for radicals or ions. As a first simple example we consider the positive ion of formaldehyde, H\ :math:`_2`\ CO\ :math:`^+`. In this case it turns out that the lowest cation state is :math:`^2B_2`, i.e., one electron is removed from the highest occupied orbital in symmetry :math:`b_2` (denoted 2.3 in Molpro, see above). By default Molpro assumes that the number of electrons equals the total nuclear charge. Therefore, in order to compute an ion, one has to specify the number of electrons. Alternatively, the total charge of the molecule can be given (see below). Furthermore, one has to specify the symmetry and spin of the wavefunction. This is done using the ``wf`` directive (``wf`` stands for *wavefunction*):

``wf,15,3,1``

The first entry on a ``wf`` card is the number of electrons. The second entry is the total symmetry of the wavefunction. For a doublet this equals the symmetry of the singly occupied molecular orbital. Finally, the third entry specifies the number of singly occupied orbitals, or, more generally the total spin. Zero means singlet, 1 doublet, 2 triplet and so on. Alternatively, the ``WF`` card can be written in the form

``wf,charge=1,symmetry=3,spin=1``

where now the total charge of the molecule instead of the number of electrons is given. In this case the number of electrons is computed automatically from the nuclear and total charges.

In summary, the input for H\ :math:`_2`\ CO\ :math:`^+` is

.. code-block:: text

   
   {geometry specification}
   {basis specification}
   
   {hf          !invoke spin restricted Hartree-Fock program (rhf can also be used)
   occ,5,1,2    !number of occupied orbitals in the irreps a1, b1, b2, respectively
   wf,15,3,1}   !define wavefunction: number of electrons, symmetry and spin
   ---

Note the curly brackets, which are required and enclose the command block ``hf``.

As a second example we consider the ground state of O\ :math:`_2`, which is :math:`^3\Sigma^-_g`. The geometry specification is simply

.. code-block:: text

   geometry={     !geometry specification, using z-matrix
   o1
   o2,o1,r
   }
   
   r=2.2 bohr   !bond distance

Molpro is unable to use non-abelian point groups, and can therefore only use :math:`D_{2h}` in the present case. The axis of a linear molecule is placed on the :math:`z`\ –axis of the coordinate system. Then the symmetries of the :math:`\sigma_g`, :math:`\pi_{u,x}`, :math:`\pi_{u,y}`, :math:`\sigma_u`, :math:`\pi_{g,x}`, :math:`\pi_{g,y}` orbitals are 1,2,3,5,6,7, respectively. It is easier to remember that the irreducible representations in :math:`D_{2h}` are carried by the functions (molpro symmetry numbers in parenthesis) :math:`s(1), x(2), y(3), xy(4), z(5), xz(6), yz(7), xyz(8)`. The order in :math:`C_{2v}` is the same, but then there are only the first four irreducible representations.

The electron configuration of the electronic ground state of O\ :math:`_2` is

:math:`1\sigma_g^2 1\sigma_u^2 2\sigma_g^2 2\sigma_u^2 3\sigma_g^2 1\pi_{u,x}^2 1\pi_{u,y}^2 1\pi_{g,x}^1 1\pi_{g,y}^1`.

Thus, the number of occupied orbitals in the 8 different irreducible representations of the :math:`D_{2h}` point group are specified as

``occ,3,1,1,0,2,1,1,0``

The product symmetry of the singly occupied orbitals 1.6 (:math:`xz`) and 1.7 (:math:`yz`) is 4 (:math:`xy`), and therefore the symmetry of the total wavefunction is 4 (please refer to the Molpro reference manual for a more complete account of symmetry groups and the numbering of irreducible representations). Thus, the ``wf`` card reads

.. code-block:: text

   wf,16,4,2      !16 electrons, symmetry 4, triplet (2 singly occupied orbitals)

This is still not unambiguous, since the product symmetry of :math:`\pi_{u,x}` (2) and :math:`\pi_{u,y}` (3) is also 4, and therefore the program might not be able to decide if it should singly occupy the :math:`\pi_u` or :math:`\pi_g` orbitals. Therefore, the singly occupied orbitals can be specified using the ``open`` directive:

``open,1.6,1.7``

This now defines the wavefunction uniquely. In summary, the input for O\ :math:`_2` reads

.. code-block:: text

   ***,O2
   print,basis,orbitals
   geometry={                 !geometry specification, using z-matrix
   o1
   o2,o1,r
   }
   
   r=2.2 bohr                 !bond distance
   
   basis=vtz                  !triple-zeta basis set
   
   {hf                        !invoke RHF program
   wf,16,4,2                  !define wavefunction: 16 electrons, symmetry 4, triplet
   occ,3,1,1,,2,1,1           !number of occupied orbitals in each symmetry
   open,1.6,1.7}              !define open shell orbitals

In fact, the last 2 lines are not necessary in the present case, since the correct configuration can be automatically determined using the Aufbau principle, but this might not always be true.

.. _quickstart--single-reference-electron-correlation-treatments:

Single-reference electron correlation treatments
------------------------------------------------

Once the Hartree-Fock calculation is done, electron correlation effects can be taken into account using various methods. Each available method in Molpro is specified by a different keyword.

.. _quickstart--closed-shell-correlation-methods:

Closed-shell correlation methods
================================

For closed-shell calculations the following methods/keys are available:

.. code-block:: text

   mp2     !second-order Moeller-Plesset perturbation theory
   lmp2    !second-order local Moeller-Plesset perturbation theory
   mp3     !third-order Moeller-Plesset perturbation theory
   mp4     !fourth-order Moeller-Plesset perturbation theory
   ci      !singles and doubles configuration interaction (using MRCI program)
   cisd    !singles and doubles configuration interaction (using CCSD program)
   cepa(1) !Coupled electron pair approximation, version 1
   cepa(2) !Coupled electron pair approximation, version 2
   cepa(3) !Coupled electron pair approximation, version 3
   acpf    !Averaged couplec pair functional
   ccsd    !Coupled cluster with singles and doubles
   ccsd(t) !Coupled cluster with singles and doubles and perturbative
           !treatment of triples
   bccd    !Brueckner coupled cluster with doubles
   bccd(t) !Brueckner coupled cluster with doubles and perturbative
           !treatment of triples
   qcisd   !Quadratic configuration interaction with singles and doubles
   qcisd(t)!Quadratic configuration interaction with perturbative
           !treatment of triples

There are also explicitly correlated and local variants of many of these methods, see sections `explicitly correlated methods <quickstart.html#explicitly-correlated-methods>`__ and `local correlation treatments <quickstart.html#local-correlation-treatments>`__, respectively.

One or more of these commands should be given after the Hartree-Fock input. Note that some methods include others as a by-product; for example, it is wasteful to ask for ``mp2`` and ``mp4``, since the MP4 calculation returns all of the second, third and fourth order energies. CCSD also returns the MP2 energy.

By default, only the valence electrons are correlated. To modify the space of uncorrelated inner-shell (core) orbitals, the ``core`` directive can be used, on which the numbers of core orbitals in each symmetry are specified in the same way as the occupied orbitals on the ``occ`` card. In order to correlate all electrons in a molecule, use

``core``

without any further arguments (all entries zero). This card must follow the directive for the method, e.g.,

.. code-block:: text

   {MP2     !second-order Moeller-Plesset perturbation theory
   core}    !correlate all electrons

Note, however, that special basis sets are needed for correlating inner shells, and it does make not much sense to do such calculations with the standard basis sets described above. The correlation-consistent core-valence basis sets (cc-pCV\ :math:`x`\ Z where :math:`x` is D, T, Q, :math:`5,\dots`) are available for this purpose.

.. code-block:: text

   {MP2     !second-order Moeller-Plesset perturbation theory
   core,2}  !don't correlate electrons in the orbitals 1.1 and 2.1.

The number of occupied orbitals is automatically remembered from the preceding HF calculation. If necessary for special purposes, it can be specified using ``occ`` cards as in HF. The orbitals are taken from the most recent HF calculation in the input. See the Molpro reference manual for other choices of orbitals.

Example for a complete CCSD(T) calculation for formaldehyde:

.. code-block:: text

   ***,formaldehyde
   print,basis,orbitals   !this is optional: print the basis set and the occupied orbitals
   angstrom
   geometry={             !define the nuclear coordinates
   C
   O  , C , rco
   H1 , C , rch , O , hco
   H2 , C , rch , O , hco , H1 , 180
   }
   
   rco=1.182 Ang
   rch=1.102 Ang
   hco=122.1789 Degree
   
   basis=vdz              !Select basis set
   hf                     !Perform HF calculation
   ccsd(t)                !Perform CCSD(T) calculation

.. _quickstart--open-shell-correlation-methods:

Open-shell correlation methods
==============================

For open shell the following single-reference methods are implemented in Molpro:

.. code-block:: text

   ump2    !second-order Moeller-Plesset perturbation theory with UHF reference
   rmp2    !second-order Moeller-Plesset perturbation theory with RHF reference.
   ci      !singles and doubles configuration interaction (using the MRCI program)
   rcisd   !spin-restricted singles and doubles configuration interaction
   ucisd   !spin-unrestricted singles and doubles configuration interaction
   rccsd   !partially spin adapted coupled cluster with singles and doubles
   rccsd(t)!partially spin adapted coupled cluster with perturbative
           !treatment of triples
   uccsd   !spin-unrestricted coupled cluster with singles and doubles
   uccsd(t)!spin-unrestricted coupled cluster with perturbative
           !treatment of triples

Again, there are also explicitly correlated and local variants of many of these methods, see sections `explicitly correlated methods <quickstart.html#explicitly-correlated-methods>`__ and `local correlation treatments <quickstart.html#local-correlation-treatments>`__, respectively.

Note that all methods except ``ump2`` use spin-restricted Hartree-Fock (RHF) reference functions. This is also the case for the ``ucisd`` and ``uccsd`` methods, in which the correlated wavefunction may be slightly spin contaminated, even though the RHF reference function is spin adapted. ``ump2`` is not generally recommended, since spin contamination can lead to large errors.

Core orbitals can be specified as for the closed-shell methods. The number of electrons and occupations as well as the orbitals are taken from the most recent RHF calculation. It is possible to modify these defaults using ``occ``, ``closed``, ``wf``, or ``orbital`` directives; see the Molpro reference manual for details.

The following is an example of a complete CCSD(T) calculation for O\ :math:`_2`.

.. code-block:: text

   ***,O2
   print,basis,orbitals
   geometry={                 !geometry specification, using z-matrix
   o1
   o2,o1,r
   }
   
   r=2.2 bohr                 !bond distance
   
   basis=vtz                  !triple-zeta basis set
   
   {hf                        !invoke RHF program
   wf,16,4,2                  !define wavefunction: 16 electrons, symmetry 4, triplet
   occ,3,1,1,,2,1,1           !number of occupied orbitals in each symmetry
   open,1.6,1.7}              !define open shell orbitals
   
   rccsd(t)                   !perform partially spin adapted CCSD(T)

.. _quickstart--mcscf-and-casscf-calculations:

MCSCF and CASSCF calculations
-----------------------------

In the MCSCF method a multiconfiguration wavefunction is variationally optimized with respect to simultaneous variations of the orbitals and configuration coefficients. As explained in section `method and wavefunction specification <quickstart.html#method-and-wavefunction-specification>`__, the Hartree-Fock wavefunction is uniquely defined by specifying the number of occupied orbitals in each symmetry and possibly the singly occupied orbitals. In the MCSCF case some more information is necessary. We will begin to explain the input for CASSCF (complete active space SCF), which is the simplest case.

.. _quickstart--complete-active-space-self-consistent-field-casscf:

Complete Active Space Self-Consistent Field, CASSCF
===================================================

In a CASSCF wavefunction the occupied orbital space is divided into a set of *inactive* or *closed-shell* orbitals and a set of *active* orbitals. All inactive orbitals are doubly occupied in each Slater determinant. On the other hand, the active orbitals have varying occupations, and all possible Slater determinants (or CSFs) are taken into account which can be generated by distributing the :math:`N_{act}=N_{el}-2 m_{\text{closed}}` electrons in all possible ways among the active orbitals, where :math:`m_{\text{closed}}` is the number of closed-shell (inactive) orbitals, and :math:`N_{el}` is the total number of electrons. Thus, it corresponds to a full CI in the active space.

The CASSCF program is invoked using the

``casscf``

Aliases for this command are ``mcscf`` or ``multi``. This command is optionally followed by further input defining the wavefunction. The inactive orbital space is defined using the ``closed`` directive.

``closed,$n_1,n_2,\ldots,n_d$``

where :math:`n_i` is the number of doubly occupied (inactive) orbitals in irreducible representation :math:`i`. The total number of occupied orbitals is specified using the ``occ`` directive, as in Hartree-Fock.

``occ,$m_1,m_2,\ldots,m_d$``

where :math:`m_i \ge n_i`. The number of active orbitals in irreducible representations :math:`i` is then :math:`m_i - n_i`. Note that the inactive orbitals are always the first in each symmetry, i.e., inactive and active spaces cannot be mixed. The number of electrons, as well as the symmetry of the wavefunction and the total spin is specified using the ``wf`` directive, as explained already for open-shell HF:

``wf, $N_{el},isym,ms2$``

where :math:`isym` is the symmetry of the total wavefunction (the direct product of the symmetries of all occupied spin orbitals), and :math:`ms2=2S` defines the spin (0=singlet, 1=doublet, 2=triplet etc).

From the above it follows that the number of active electrons is

.. math::

   N_{act} = N_{el} - 2 \sum_i^{m_{\text{closed}}} n_i

By default, the inactive space consists of all inner-shell orbitals, and the active space of all valence orbitals which are obtained from the atomic valence orbitals (full valence active space). The default number of electrons equals the sum of nuclear charges, the default wavefunction symmetry is 1 and singlet. The default starting guess for the orbitals is taken from the most recent orbital optimization, e.g., Hartree-Fock. The simplest input for a CASSCF calculation for formaldehyde is therefore

.. code-block:: text

   ***,formaldehyde
   print,orbitals,civector   !this is optional: print the occupied orbitals
                             !and the CI vector
                             !by default, only coefficients larger than 0.05
                             !are printed.
   angstrom
   geometry={                !define the nuclear coordinates
   C
   O  , C , rco
   H1 , C , rch , O , hco
   H2 , C , rch , O , hco , H1 , 180
   }
   
   rco=1.182 Ang
   rch=1.102 Ang
   hco=122.1789 Degree
   
   basis=vdz              !Select basis set
   hf                     !Perform HF calculation
   casscf                 !Perform CASSCF calculation,
                          !using the HF orbitals as starting guess.

In this case, the carbon and oxygen :math:`1s` orbitals are inactive, and the carbon and oxygen :math:`2s`, :math:`2p` as well as the hydrogen :math:`1s` orbitals are active. This corresponds to the following input, which could be given after the ``casscf`` directive:

.. code-block:: text

   {casscf
   closed,2               !2 inactive orbitals in Symmetry 1 (a1)
   occ,7,2,3              !7a1, 2b1, 3b2 occupied orbitals
   wf,16,1,0}             !16 electrons, Symmetry 1 (A1), singlet

Thus, there are five :math:`a_1`, two :math:`b_1`, and three :math:`b_2` active orbitals. This yields 3644 CSFs or 11148 Slater determinants. *Note that the ``wf`` directive must be given after the ``occ`` and ``closed`` ones.* A shorter expansion results if the :math:`2s` orbital of oxygen is made inactive. In this case the input would be

.. code-block:: text

   {casscf
   closed,3               !3 inactive orbitals in Symmetry 1 (a1)
   occ,7,2,3              !7a1, 2b1, 3b2 occupied orbitals
   wf,16,1,0}             !16 electrons, Symmetry 1 (A1), singlet

and now only 1408 CSFs or 4036 Slater determinants are generated.

.. _quickstart--restricted-active-space-self-consistent-field-rasscf:

Restricted Active Space self-consistent field, RASSCF
=====================================================

Since the number of CSFs or Slater determinants and thus the computational cost quickly increases with the number of active orbitals, it may be desirable to use a smaller set of CSFs. One way to make a selection is to restrict the number of electrons in certain subspaces. One could for instance allow only single and double excitations from some strongly-occupied subset of active orbitals, or restrict the number of electrons to at most 2 in another subset of active orbitals. In general, such restrictions can be defined using the ``restrict`` directive:

``restrict,min, max, orbital list``

where *min* and *max* are the minimum and maximum number of electrons in the given orbital subspace, as specified in the *orbital list*. Each orbital is given in the form *number.symmetry*, e.g. 3.2 for the third orbital in symmetry 2. The ``restrict`` directives (several can follow each other) must be given after the ``wf`` card. As an example, consider the formaldehyde example again, and assume that only single and double excitations are allowed into the orbitals 6.1, 7.1, 2.2, 3.3, which are unoccupied in the HF wavefunction. Then the input would be

.. code-block:: text

   {casscf
   closed,2                        !2 inactive orbitals in Symmetry 1 (a1)
   occ,7,2,3                       !7a1, 2b1, 3b2 occupied orbitals
   wf,16,1,0                       !16 electrons, Symmetry 1 (A1), singlet
   restrict,0,2, 6.1,7.1,2.2,3.3}  !max 2 electrons in the given orbital list

One could further allow only double excitations from the orbitals 3.1, 4.1, but in this case this has no effect since no other excitations are possible anyway. In order to demonstrate such a case, we increase the number of occupied orbitals in symmetry 1 to 8, and remove the restriction for orbital 6.1.

.. code-block:: text

   {casscf
   closed,2                        !2 inactive orbitals in Symmetry 1 (a1)
   occ,8,2,3                       !7a1, 2b1, 3b2 occupied orbitals
   wf,16,1,0                       !16 electrons, Symmetry 1 (A1), singlet
   restrict,0,2, 7.1,8.1,2.2,3.3   !max 2 electrons in the given orbital list
   restrict,2,4, 3.1,4.1}          !at least 2 and max 4 electrons in the
                                   !given orbitals

It is found that this calculation is not convergent. The reason is that some orbital rotations are almost redundant with single excitations, i.e., the effect of an orbital transformation between the strongly and weakly occupied spaces can be expressed to second order by the single and double excitations. This makes the optimization problem very ill conditioned. This problem can be removed by eliminating the single excitations from / into the restricted orbital space as follows:

.. code-block:: text

   {casscf
   closed,2                        !2 inactive orbitals in Symmetry 1 (a1)
   occ,8,2,3                       !7a1, 2b1, 3b2 occupied orbitals
   wf,16,1,0                       !16 electrons, Symmetry 1 (A1), singlet
   restrict,0,2, 7.1,8.1,2.2,3.3   !max 2 electrons in the given orbital list
   restrict,-1,0 7.1,8.1,2.2,3.3   !1 electron in given orbital space not
                                   !allowed (no singles)
   restrict,2,4, 3.1,4.1           !at least 2 and max 4 electrons in the
                                   !given orbitals
   restrict,-3,0,3.1,4.1}          !3 electrons in given orbital space not
                                   !allowed (no singles)

and now the calculation converges smoothly.

Converging MCSCF calculations can sometimes be tricky and difficult. Generally, CASSCF calculations are easier to converge than restricted calculations, but even in CASSCF calculations problems can occur.

The reasons for slow or no convergence could be one or more of the following.

* Near redundancies between orbital and CI coefficient changes as shown above.

Remedy: eliminate single excitations

* Two or more weakly occupied orbitals have almost the same effect on the energy, but the active space allows the inclusion of only one of them.

Remedy: increase or reduce active space (``occ`` card).

* An active orbital has an occupation number very close to two. The program may have difficulties to decide which orbital is inactive.

Remedy: increase inactive space

* Correlation of an active orbital gives a smaller energy lowering than would be obtained by correlating an inactive orbital. The program tries to swap active and inactive orbitals.

Remedy: reduce (or possibly increase) active space.

* Another state of the same symmetry is energetically very close (nearly degenerate). The program might oscillate between the states (root flipping).

Remedy: include all nearly degenerate states into the calculation, and optimize their average energy (see below).

As a rule of thumb, it can be said that if a CASSCF calculation does not converge or converges very slowly, the active or inactive space is not chosen well.

.. _quickstart--state-averaged-mcscf:

State-averaged MCSCF
====================

In order to compute excited states it is usually best to optimize the energy average for all states under consideration. This avoids root-flipping problems during the optimization process and yields a single set of compromise orbitals for all states.

The number of states to be optimized in a given symmetry is specified on a ``state`` directive, which must follow directly after the ``wf`` directive, e.g.,

``wf,16,1,0;state,2 !optimize two states of symmetry 1``

It is also possible to optimize states of different symmetries together. In this case several ``wf`` / ``state`` directives can follow each other, e.g.,

``wf,16,1,0;state,2 !optimize two states of symmetry 1\\``
``wf,16,2,0;state,1 !optimize one states of symmetry 2``

etc. Optionally also the weights for each state can be specified, e.g.

.. code-block:: text

   wf,16,1,0;state,2;weight,0.2,0.8   !optimize two states of symmetry 1
                                      !first state has weight 0.2,
                                      !second state weight 0.8

By default, the weights of all states are identical, which is normally the most sensible choice. The following example shows a state-averaged calculation for :math:`\rm O_2`, in which the valence states (:math:`^3\Sigma_g^-`, :math:`^1\Delta_g`) are treated together.

.. code-block:: text

   ***,O2
   print,basis,orbitals
   geometry={                 !geometry specification, using z-matrix
   o1
   o2,o1,r
   }
   
   r=2.2 bohr                 !bond distance
   
   basis=vtz                  !triple-zeta basis set
   
   {hf                        !invoke RHF program
   wf,16,4,2                  !define wavefunction: 16 electrons, symmetry 4, triplet
   occ,3,1,1,,2,1,1           !number of occupied orbitals in each symmetry
   open,1.6,1.7}              !define open shell orbitals
   
   {casscf                    !invoke CASSCF program
   wf,16,4,2                  !triplet Sigma-
   wf,16,4,0                  !singlet delta (xy)
   wf,16,1,0}                 !singlet delta (xx - yy)

Note that averaging of states with different spin-multiplicity, as in the present examples, is possible only for CASSCF, but not for more restricted RASSCF or MCSCF, wavefunctions.

.. _quickstart--mcscf-with-selected-configurations:

MCSCF with selected configurations
==================================

MCSCF with arbitrary selected configuration spaces can also be performed. The only restriction is that always all CSFs with different spin couplings arising from the same orbital occupancy are included. There are two ways to select configurations. Either, they are selected from a previous calculation with a threshold, or they are defined explicitly in the input. Here we only describe the latter case; for more details please refer to the reference manual.

The configuration input starts with the ``select`` directive, and subsequently each orbital configuration is given by one line starting with the keyword ``con``, followed by the occupation numbers of the active orbitals. The following example shows an input for formaldehyde.

.. code-block:: text

   ***,formaldehyde
   angstrom
   geometry={                !define the nuclear coordinates
   C
   O  , C , rco
   H1 , C , rch , O , hco
   H2 , C , rch , O , hco , H1 , 180
   }
   
   rco=1.182 Ang
   rch=1.102 Ang
   hco=122.1789 Degree
   
   basis=vdz              !Select basis set
   hf                     !Perform HF calculation
   {mcscf                 !invoke MCSCF program
   closed,4,,1            !4a1 and 1b2 inactive orbitals
   occ,6,2,3              !6a1, 2b1, 3b2 occupied orbitals
   wf,16,1,0              !16 electrons, Symmetry 1 (A1), singlet
   select                 !start configuration selection
   con, 3.1,-3.1,1.2,-1.2,1.3,-1.3     !occupied orbitals in 1st configuration
   con, 3.1,-3.1,2.2,-2.2,1.3,-1.3
   con, 3.1,-3.1,1.2,-1.2,2.3,-2.3
   con, 3.1,4.1,1.2,2.2,1.3,-1.3
   con, 3.1,-3.1,1.2,2.2,1.3,2.3
   con, 4.1,-4.1,1.2,-1.2,1.3,-1.3}

This calculation includes all CSFs of the CASSCF with coefficients larger than 0.04.

.. _quickstart--multireference-electron-correlation-methods:

Multireference electron correlation methods
-------------------------------------------

MCSCF or CASSCF calculations usually account only for a small percentage of the dynamical correlation energy. Therefore, in order to obtain accurate results, subsequent correlation treatments are possible. This can either be done by multireference configuration interaction (MRCI) or by multireference perturbation theory (MRPT). The latter is simpler and much cheaper, but also less reliable than MRCI.

.. _quickstart--multireference-configuration-interaction-mrci:

Multireference configuration interaction (MRCI)
===============================================

MRCI calculations are invoked using the

``mrci``

or

``mrcic``

directive. ``mrcic`` is a new program that is much more efficient than ``mrci`` for cases with many inactive (closed-shell) orbitals in the reference function. Currently, it is still restricted to single-state calculations. Note that ``mrci`` and ``mrcic`` give slightly different results if inactive orbitals are present, since ``mrcic`` uses a more strongly contracted wave function ansatz [see K. R. Shamasundar, G. Knizia, and H.-J. Werner, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3609809>`__ **135**, 054101 (2011)]. See also below for ``rs2c``, which uses the same ansatz.

By default, the same occupied and closed-shell spaces as in the preceding MCSCF (CASSCF) calculation are used, and the inner-shell *core* orbitals are not correlated (i.e., the :math:`1s` orbitals of carbon or oxygen, or the :math:`1s`, :math:`2s`, and :math:`2p` orbitals in chlorine). The number of uncorrelated core orbitals can be modified using the ``core`` directive (see section `Closed-shell correlation methods <quickstart.html#closed-shell-correlation-methods>`__). It is not necessary that the reference wavefunction is exactly the same as in the MCSCF, and the ``occ``, ``closed``, ``restrict``, and ``select`` directives can be used exactly in the same way as explained for MCSCF and CASSCF.

By default, the orbitals are taken from the most recent orbital optimization calculation (HF or MCSCF/CASSCF). Other orbitals can be specified using the ``orbital`` directive. Please refer to the reference manual for further details.

The following is an example of a CASSCF/MRCI calculations for :math:`\rm O_2`.

.. code-block:: text

   ***,O2
   print,orbitals,civector    !print orbitals and ci-coefficients
   geometry={                 !geometry specification, using z-matrix
   o1
   o2,o1,r
   }
   
   r=2.2 bohr                 !bond distance
   
   basis=vtz                  !triple-zeta basis set
   
   {hf                         !invoke RHF program
   wf,16,4,2                  !define wavefunction: 16 electrons,
   symmetry 4,
                              !triplet
   occ,3,1,1,,2,1,1           !number of occupied orbitals in each symmetry
   open,1.6,1.7}             !define open shell orbitals
   
   casscf                     !casscf using full valence active space
   mrci                       !mrci using full valence casscf reference function
   {mrci                       !mrci with only 2p orbitals active, 2s closed
                              !in reference
   closed,2,,,,2}             !inactive orbitals in the reference function.

.. _quickstart--multireference-perturbation-theory-caspt2-caspt3:

Multireference perturbation theory, CASPT2, CASPT3
==================================================

The input for MRPT/CASPT2 is similar to MRCI, but the following commands are used.

.. code-block:: text

   rs2          !second-order multireference perturbation theory
   rs3          !third-order multireference perturbation theory
   rs2c         !second-order multireference perturbation theory
                !with a more contracted configuration space.

In case of ``rs2`` and ``rs3``, exactly the same configuration spaces as in the MRCI are used. In this case the excitations with two electrons in the external orbital space are *internally contracted*. The total number of correlated orbitals is restricted to 16 for machines with 32-bit integers and to 32 for machines with 64-bit integers.

In the ``rs2c`` case certain additional configuration classes involving internal and semi-internal excitations are also internally contracted (see `J. Chem. Phys. <https://dx.doi.org/10.1063/1.481132>`__ **112**, 5546 (2000)). This is exactly as in the ``mrcic`` case (see above). This method is much more efficient than ``rs2`` and more suitable for large cases. In particular, in this case only the number of *active* orbitals is restricted to 16 or 32 on 32 and 64 bit machines, respectively, and any number of closed-shell (inactive) orbitals can be used (up to a maximum as defined by a program parameter).

Note that the RS2 and RS2c methods yield slightly different results. In both cases the results also slightly differ from those obtained with the method of of Roos et al. (`J. Chem. Phys. <https://dx.doi.org/10.1063/1.462209>`__ **96**, 1218 (1992)), as implemented in ``MOLCAS``, since in the latter case *all* configuration spaces are internally contracted. This introduces some bottlenecks that are not present in Molpro.

Restricted active space (RASPT2) or general MRPT2 calculations can be performed using the ``restrict`` and/or ``select`` directives as explained in section for MCSCF and CASSCF.

MRPT2 and CASPT2 calculations often suffer from so-called intruder state problems, leading to a blow-up of the wavefunction and no convergence. This problem can often be avoided by using *level shifts*. These shifts can be specified on the ``rs2`` and ``rs2c`` cards:

``rs2,shift=value\\``
``rs2c,shift=value``

The energy is approximately corrected for the shift as proposed by Roos and Andersson. (`Chem. Phys. Lett. <https://dx.doi.org/10.1016/0009-2614(95)01010-7>`__ **245**, 215 (1995)).

Alternatively (or in addition, the IPEA shift proposed by G. Ghigo, B. O. Roos, and P.A. Malmqvist, `Chem. Phys. Lett. <https://dx.doi.org/10.1016/j.cplett.2004.08.032>`__ **396**, 142 (2004) can be used:

``rs2,ipea=value``

It is also possible to use modified zeroth-order Hamiltonians; see reference manual for further details.

Energy gradients are available for ``rs2``, including multi-state treatments. Currently, gradients are not yet available for ``rs2c``.

.. _quickstart--multi-state-caspt2:

Multi-state CASPT2
==================

Multi-state caspt2 calculations are only possible with the ``rs2`` program.

There are various possibilities how to choose the zeroth-order Hamiltonian and the configuration basis. Here we describe only the recommended method; for more details see manual.

Three options are relevant:

``rs2,xms=value,mix=nstates,root=iroot``

where

* **``xms=0``:** MS-CASPT2 method of Finley et al. CPL 288, 299 (1998)
* **``xms=1``:** Extended multi-state CASPT2 (XMS-CASPT2) method as described in `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3633329>`__ **135**, 081106 (2011). fully invariant treatment of level shifts (recommended).
* **``xms=2``:** XMS-CASPT2 method; level shift is only applied to the diagonal of H0.
* ***nstates*:** Number of states included in the calculation
* ***iroot*:** Root number to be optimized in subsequent gradient calculation (only required if gradient calculations follows)

Example:

.. code-block:: text
   :caption: examples/h2o_xms_caspt2.inp

   ***,mscaspt2 for h2o 3B2 states
   basis=vdz
   geometry={O
             H1,O,R;
             H2,O,R,H1,THETA}
   R=2.4
   Theta=98
   
   
   hf
   {multi;closed,2
   wf,10,1,2;state,3         !three 3A1 states included in sa-casscf
   wf,10,2,2;state,2         !two 3B1 states included in sa-casscf
   wf,10,3,2;state,3         !three 3B2 states included in sa-casscf
   canonical,2140.2}         !save pseudo canonical orbitals
   
   {rs2,xms=2,mix=3,root=2;  !include three B2 states,
                             !select the second state for gradients
   wf,10,3,2                 !Triplet B2 state symmetry.
   state,3}                  !The same number of states as specified for mix.
   
   optg                      !optimize the geometry

.. _quickstart--density-functional-calculations:

Density functional calculations
-------------------------------

Molpro is able to carry out standard Kohn-Sham DFT calculations using either the spin-restricted (``ks`` or ``rks``) or spin-unrestricted (``uks``) formalisms. Here is a simple example, which does a local-density approximation (LDA) calculation for formaldehyde.

.. code-block:: text

   ***,formaldehyde
   geometry={
   C
   O  , C , rco
   H1 , C , rch , O , hco
   H2 , C , rch , O , hco , H1 , 180
   }
   
   rco=1.182 Ang
   rch=1.102 Ang
   hco=122.1789 Degree
   
   rks

The exchange-correlation functional, and associated potential, are integrated numerically, and in principle it is necessary to supply parameters to allow the construction of an appropriate grid. However, the grid is built using a model adaptive scheme, and it is normally necessary to specify only the required energy accuracy. This threshold is in turn taken by default from the overall energy convergence threshold, so in most calculations it is not normally necessary to specify anything at all.

Many different exchange and correlation functionals are contained in the program. They are implemented in a modular fashion, with both computer code and documentation being built directly from their mathematical definition. This means that you can always find the precise definition of a functional in the user manual. Each functional has a keyword which is used to identify it in the input file. The functionals to be used are given one after each other as options to the ``ks`` command; for example, the following does a Kohn-Sham calculation using Becke’s exchange functional, and the Lee–Yang–Parr correlation functional.

``ks,b,lyp``

Another commonly used combination (in fact, the default) is ``ks,s,vwn`` which gives LDA (Slater–Dirac exchange, Vosko–Wilk–Nusair correlation). Finally, the program is aware of some combinations of functionals, for example ``ks,b3lyp`` which is the hybrid B3LYP functional consisting of weighted combinations of various density functionals together with a fraction of exact (Hartree–Fock) exchange.

Other options, such as the closed- and open-shell orbitals and the wavefunction symmetry can be defined as explained in section `method and wavefunction specification <quickstart.html#method-and-wavefunction-specification>`__.

.. _quickstart--geometry-optimization:

Geometry optimization
---------------------

Geometry optimizations are invoked by the ``optg`` input directive, which must follow the input of the method for which the optimization is to be performed. For instance, optimization of the geometry for formaldehyde at the MP2 level is performed with the following input

.. code-block:: text

   ***,formaldehyde
   print,basis,orbitals   !this is optional: print the basis set and the
                          !occupied orbitals
   angstrom
   geometry={             !define the nuclear coordinates
   C
   O  , C , rco
   H1 , C , rch , O , hco
   H2 , C , rch , O , hco , H1 , 180
   }
   
   rco=1.182 Ang
   rch=1.102 Ang
   hco=122.1789 Degree
   
   basis=vdz              !Select basis set
   hf                     !Perform HF calculation
   mp2                    !Perform MP2 calculation
   optg                   !Optimize geometry for MP2

Optimizations use analytical energy gradients if available; otherwise the gradients are computed by finite differences. Presently, analytical energy gradients are available for the following methods.

* ``hf`` Closed and open-shell spin restricted Hartree-Fock (RHF)
* ``uhf`` Spin-unrestricted Hartree-Fock (UHF).
* ``ks`` Spin-restricted closed and open-shell Kohn-Sham calculations.
* ``uks`` Spin-unrestricted Kohn-Sham calculations.
* ``mcscf`` MCSCF and CASSCF, including state-averaged calculations
* ``mp2`` closed-shell MP2
* ``rmp2`` open-shell RMP2
* ``lmp2`` closed-shell local MP2
* ``lrmp2`` open-shell local RMP2
* ``qcisd`` closed-shell quadratic configuration
* ``qcisd(t)`` closed-shell quadratic configuration interaction, including perturbative triple-excitation contribution
* ``dcsd`` distinguishable cluster with singles and double excitations
* ``ccsd`` closed-shell singles and doubles coupled-cluster
* ``ccsd(t)`` closed-shell coupled cluster, including triple excitations
* ``df-mp2-f12`` closed-shell MP2-F12 with density fitting (only with certain options and Ansätze, see reference manual)
* ``df-ccsd-F12`` explicitly correlated closed-shell singles and doubles coupled-cluster
* ``df-ccsd(t)-F12`` explicitly correlated closed-shell coupled cluster, including triple excitations
* ``rs2`` Second-order multireference perturbation theory, including multi-state treatments

Most gradient methods are also available with density fitting, see section `density fitting approximations <quickstart.html#density-fitting-approximations>`__. Gradients for explicitly correlated methods are only available with density fitting.

Various options are available for modifying the convergence thresholds and the optimization method. For details see the reference manual.

.. _quickstart--frequency-calculations:

Frequency calculations
----------------------

Harmonic vibrational frequencies can be computed automatically using the ``frequency`` directive. Normally, this should be preceded by a geometry optimization. A typical input reads as follows.

.. code-block:: text

   hf                     !Perform HF calculation
   mp2                    !Perform MP2 calculation
   optg                   !Optimize geometry for MP2
   frequencies,sym=auto   !Perform frequency calculation for MP2; use symmetry in hessian calculation

The second energy derivatives are computed by finite differences using analytical energy gradients when available (see section `geometry optimization <quickstart.html#geometry-optimization>`__), otherwise from energies (which may take long time and is less accurate!). Note that during frequency calculations the symmetry of the molecule may be lowered, and then the calculation may fail. It is therefore advisable to use the ``nosym`` directive as first line in the geometry input.

In the following cases the second derivatives can be computed analytically:

* ``hf`` Closed shell Hartree-Fock (RHF)
* ``mcscf`` Single state MCSCF and CASSCF without symmetry (i.e. using the ``nosym`` directive in the geometry input).

In these cases the input is

.. code-block:: text

   frequencies,analytical      !Perform frequency calculation

.. _quickstart--relativistic-effects-and-pseudopotentials:

Relativistic effects and pseudopotentials
-----------------------------------------

.. _quickstart--scalar-relativistic-effects:

Scalar relativistic effects
===========================

Scalar-relativistic effects can be included explicitly, either by means of the Pauli, the Douglas-Kroll-Hess, or eXact-2-Component Hamiltonians. In the first case, the effects are evaluated to first order in perturbation theory (including the mass-velocity and Darwin terms) by setting

``gexpec,rel``

at the beginning of the input. The relativistic contributions are stored by the program within the variable ``erel``. An example is

.. code-block:: text

   ***,Cu ground state
   
   ! Pauli Hamiltonian
   
   gexpec,rel         !compute relativistic correction using perturbation theory
   geometry={cu}      !geometry
   basis=vtz          !basis set
   hf                 !Hartree-Fock calculation
   e_rhf=energy+erel  !store total relativistic energy in variable e_rhf

To use the 2nd-order Douglas-Kroll-Hess Hamiltonian, one has to specify

``dkho=2``

at the beginning of the input (note that the order can range from 2 to 99). The relativistic contributions are then included as part of the total energies. In this case the example reads

.. code-block:: text

   ***,Cu ground state
   
   ! Douglas-Kroll-Hess Hamiltonian
   
   dkho=2         !activate 2nd-order Douglas-Kroll-Hess treatment
   geometry={cu}  !geometry
   basis=vtz-dk   !special DK basis set (mandatory!)
   hf             !Hartree-Fock
   e_rhf=energy   !Total relativistic energy

To use the eXact-2-Component (X2C) Hamiltonian, one has to specify

``dkho=101``

In this case the DK contracted basis sets can also be used, but special X2C contracted basis sets are preferred, e.g., vtz-x2c. These will be available soon.

.. _quickstart--relativistic-pseudopotentials:

Relativistic pseudopotentials
=============================

An implicit treatment of scalar-relativistic effects is possible with pseudopotentials (ECPs). In that case, one has to specify ECP parameters and basis sets within basis blocks:

``basis={... ecp,atom,ecpname\\``

Often, it is even sufficient to specify a ECP basis-set keyword like

``basis=vtz-PP``

and this will automatically select the given basis set and the associated pseudopotential. In this case the input for the copper atom calculation could be

.. code-block:: text

   ***,Cu ground state
   
   ! ECP
   
   geometry={cu}   !geometry
   basis=vtz-pp    !special pseudo potential basis set; this also selects the ECP
   hf              !HF
   e_rhf=energy    !Total energy. This does not include contributions from the core
                   !orbitals that are included in the ECP.

For a list of available ECPs, ECP basis sets, and corresponding keywords, see

.. _quickstart--spin-orbit-coupling:

Spin-orbit coupling
===================

Spin-orbit splittings can be calculated by setting up (and diagonalizing) spin-orbit matrices between scalar-relativistic states. The latter have to be calculated and stored within CI calculations:

``{ci;...;save,record1.file}\\``

In all-electron calculations, one proceeds with the calculation of SO integrals

``lsint``

(For ECP calculation, this is not needed.)

Generating and processing of SO matrices is done with

``{ci;hlsmat,keyword3,record1.file,..,recordn.file}``

where *keyword3* is ``ls`` or ``ecp`` for all-electron or ECP calculations, respectively. If ``ls`` is given (recommended), epcs will be used for all atoms that hold ecps, and and all-electron treatment for the remaining atoms. If ``ecp`` is given, spin-orbit only includes the contributions of the ecps. Alternatively, one can also use ``AFLS`` (same as or ``AMFI``) or ``ALS``. ``ALS`` means that a one-center approximation is used for the excited configurations, but a full LS calculation is done in the internal configuration space. With ``AFLS|AMFI`` the once-center approximation is also used for the internal space.

An example input with ECPs is

.. code-block:: text

   ***,Br
   geometry={br}
   basis=vtz-pp
   {rhf;wf,sym=5}
   {multi;wf,sym=2;wf,sym=3;wf,sym=5}  !2P states, state averaged
   {ci;wf,sym=2;save,5101.2}           !2Px state
   {ci;wf,sym=3;save,5102.2}           !2Py state
   {ci;wf,sym=5;save,5103.2}           !2Pz state
   {ci;hlsmat,ls,5101.2,5102.2,5103.2} !compute and diagonalize SO matrix

The corresponding input for an all-electron calculation is

.. code-block:: text

   ***,Br
   dkroll=1
   geometry={br}
   basis=vtz-dk
   {rhf;wf,sym=5}
   {multi;wf,sym=2;wf,sym=3;wf,sym=5}  !2P states, state averaged
   {lsint}                             !Compute spin-orbit 2-electron integrals
   {ci;wf,sym=2;save,6101.2}           !2Px state
   {ci;wf,sym=3;save,6102.2}           !2Py state
   {ci;wf,sym=5;save,6103.2}           !2Pz state
   {ci;hlsmat,ls,6101.2,6102.2,6103.2} !compute and diagonalize SO matrix

.. _quickstart--core-correlation:

Core correlation
----------------

By default, Molpro only correlates the valence electrons. Inner-shell correlation can be activated using the ``CORE`` directive. On this directive the number of core orbitals (not correlated) in each symmetry is given. Just ``CORE`` without any numbers means that all electrons are correlated. For example

.. code-block:: text

   {ccsd(t);core}

Normally, it is sufficient to correlate in the electrons in the :math:`n-1` shell. Note that it makes no sense at all to activate core correlation without using appropriate basis sets. Whenever available, we recommend to use the cc-pwCV\ :math:`x`\ Z or aug-cc-pwCV\ :math:`x`\ Z basis sets.

.. _quickstart--integral-direct-calculations:

Integral-direct calculations
----------------------------

With the exception of perturbative triples corrections, all methods implemented in Molpro can be performed in integral-direct mode, i.e., without storage of the two-electron integrals on disk. Naturally, this takes longer than conventional calculations, since the integrals are recomputed whenever needed. The integral-direct mode is activated by giving the ``gdirect`` directive before the first energy calculation, e.g.,

.. code-block:: text

   ***,formaldehyde
   print,basis,orbitals   !this is optional: print the basis set and the
                          !occupied orbitals
   angstrom
   geometry={             !define the nuclear coordinates
   C
   O  , C , rco
   H1 , C , rch , O , hco
   H2 , C , rch , O , hco , H1 , 180
   }
   
   rco=1.182 Ang
   rch=1.102 Ang
   hco=122.1789 Degree
   
   gdirect                !integral-direct calculation
   basis=vdz              !Select basis set
   hf                     !Perform HF calculation
   mp2                    !Perform MP2 calculation

.. _quickstart--density-fitting-approximations:

Density fitting approximations
------------------------------

Density fitting can be used to approximate the integrals in spin restricted Hartree-Fock (``HF``), density functional theory (``KS``), second-order Møller-Plesset perturbation theory (``MP2`` and ``RMP2``), explicitly correlated MP2 (MP2-F12), all levels of closed-shell local correlation methods (``LCC2``, ``LMP2``-``LMP4``, ``LQCISD(T)``, ``LCCSD(T)``), PNO-LMP2, PNO-LCCSD(T), as well as for ``CASSCF`` and ``CASPT2`` methods. In the literature the corresponding methods are often also denoted as RI-HF, RI-DFT, or RI-MP2 etc. We prefer the acronym DF since RI is used for another purpose in explicitly correlated methods (cf. section `explicitly correlated methods <quickstart.html#explicitly-correlated-methods>`__).

These methods are either direct or semi-direct, i.e. only relatively small sets of transformed four-index integrals are stored. They are very much faster than standard direct calculations and highly recommended, in particular for calculations on larger molecules. The errors caused by density fitting approximations are generally negligible.

Density fitting is invoked by adding the prefix ``DF-`` to the command name, e.g. ``DF-HF``, ``DF-KS``, ``DF-MP2`` and so on. Gradients are available for ``DF-HF``, ``DF-KS``, and ``DF-LMP2``. Symmetry is not implemented for density fitting programs. Therefore, symmetry is turned off automatically if DF- is found in the input.

By default, a fitting basis set will be chosen automatically that corresponds to the current orbital basis set and is appropriate for the method. For instance, if the orbital basis set is ``VTZ``, the default fitting basis is ``VTZ/JKFIT`` for ``DF-HF`` or ``DF-KS``, and ``VTZ/MP2FIT`` for ``DF-MP2``. Other fitting basis sets from the library can be chosen using the ``DF_BASIS`` option, e.g.

.. code-block:: text

   BASIS=VTZ             !use VTZ orbital basis
   DF-HF,DF_BASIS=VQZ    !use VQZ/JKFIT fitting basis
   DF-MP2,DF_BASIS=VQZ   !use VQZ/MP2FIT fitting basis

The program then chooses automatically the set which is appropriate for the method. Optionally, the basis type can be appended to the basis name and then this supercedes the default, e.g.

.. code-block:: text

   BASIS=VTZ                   !use VTZ orbital basis
   DF-HF,DF_BASIS=VQZ/JKFIT    !use VQZ/JKFIT fitting basis
   DF-MP2,DF_BASIS=VQZ/MP2FIT  !use VQZ/MP2FIT fitting basis

is equivalent to the previous example.

If default fitting basis sets are not available for a given orbital basis and atom, it is recommended to use the TZVPP or QZVPP basis sets (they are identical). These are the def2 sets from Turbomole, which are available for most atoms.

In density fitted local coupled cluster methods [DF-LCCSD(T)] (see section `local correlation treatments <quickstart.html#local-correlation-treatments>`__) there is an additional option ``df_basis_ccsd`` that may optionally be used to specify a basis for the 4-external integrals, e.g.

.. code-block:: text

   BASIS=VTZ                      !use VTZ orbital basis
   DF-HF                          !use VTZ/JKFIT default fitting basis
   DF-LCCSD(T),DF_BASIS_CCSD=VQZ  !use VTZ/MP2FIT basis for 0-3 external integrals
                                  !and VQZ/MP2FIT basis for 4-external integrals

If accurate absolute values of the correlation energies are needed, the cardinal number of ``df_basis_ccsd`` should be one higher than that of the orbital basis. For energy differences this has a negligible effect, and therefore the default is ``df_basis_ccsd``\ =\ ``df_basis``.

Special basis set definitions may also be needed in explicitly correlated calculations, see section `explicitly correlated methods <quickstart.html#explicitly-correlated-methods>`__.

There are many other options affecting, e.g. screening and other details, but the default values should normally be appropriate. A full description can be found in the Molpro users manual.

.. _quickstart--local-correlation-treatments:

Local correlation treatments
----------------------------

.. _quickstart--introduction:

Introduction
============

The purpose of local correlation methods is to reduce the scaling of the computational effort as function of the molecular size and to make it possible to perform accurate calculations for larger molecules. In Molpro, local correlation methods are based on the Ansatz by Pulay (`Chem. Phys. Lett. <https://dx.doi.org/10.1016/0009-2614(83)80703-9>`__ **100**, 151 (1983)). The occupied valence orbitals are localized by one of the standard localization methods (by default Pipek-Mezey localization is used) and the virtual orbital space is represented by projected atomic orbitals (PAOs). Using Molpro 2012, also orbital specific virtuals (OSVs) can be used as an alternative (see JCP, DOI http://dx.doi.org/10.1063/1.3696963) in DF-LMP2, DF-LCCSD, and DF-LCCSD(T) calculations. The orbital pairs are classified according to distance criteria. By default only *strong pairs*, in which the two orbitals are close together and which account for most of the correlation energy are treated at the highest computational level (e.g., local coupled cluster, LCCSD), while weak pairs are treated at the local MP2 (LMP2) level. Very distant pairs can be neglected. For each of the correlated pairs, a different subspace (*domain*) of virtual orbitals is automatically chosen, and the excitations are restricted into these domains. The basic features of the LCCSD method are described in `J. Chem. Phys. <https://dx.doi.org/10.1063/1.471289>`__ **104**, 6286 (1996). A detailed description of the current DF-LCCSD(T) implementation can be found in `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3641642>`__ **135**, 144116 (2011).

A very important recent improvement of the local correlation methods is the inclusion of explicitly correlated terms. These not only strongly reduce the basis set errors, but also errors due to the domain approximations. See `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3647565>`__ **135**, 144117 (2011) for this method and extensive benchmark results. It is strongly recommended to use these explicitly correlated methods.

The local correlation program of Molpro can currently perform closed-shell LMP2, LMP3, LMP4(SDTQ), LCISD, LQCISD(T), and LCCSD(T) calculations. For large molecules, all methods scale linearly with molecular size, provided very distant pairs are neglected, and the integral-direct algorithms are used.

Much higher efficiency is achieved by using density fitting (DF) approximations (see section `density fitting approximations <quickstart.html#density-fitting-approximations>`__) to compute the integrals. Density fitting is available for all local methods up to LCCSD(T), as well as for analytical LMP2 gradients. The errors introduced by DF are negligible, and the use of the DF methods is highly recommended.

Energy gradients are available for LMP2, DF-LMP2, DF-SCS-LMP2, and LQCISD (in the latter case only for ``LOCAL=1``, i.e. the local calculation is simulated using the canonical program, and savings only result from the reduced number of pairs).

Naturally, the local approximation can introduce some errors, and therefore the user has to be more careful than with standard black box methods. This problem is very much reduced, however, in the explicitly correlated methods. On the other hand, the low-order scaling makes it possible to treat much larger systems at high levels of theory than it was possible so far. Before using these methods, it is strongly recommended to read the literature in order to understand the basic concepts and approximations.

References:

:math:`[1]` C. Hampel and H.-J. Werner, *Local Treatment of electron correlation in coupled cluster (CCSD) theory*, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.471289>`__ **104**, 6286 (1996).
:math:`[2]` H.-J. Werner and M. Schütz, *An efficient local coupled-cluster method for accurate thermochemistry of large systems*, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3641642>`__ **135**, 144116 (2011).
:math:`[3]` T. B. Adler and H.-J. Werner, *An explicitly correlated local coupled-cluster method for calculations of large molecules close to the basis set limit*, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3647565>`__ **135**, 144117 (2011).

Further references can be found therein.

.. _quickstart--invoking-local-correlation-methods:

Invoking local correlation methods
==================================

The currently most accurate and recommended local correlation methods are PNO-LMP2, PNO-LCCSD, PNO-LCCSD(T), as well as their explicitly correlated variants ``PNO-LMP2-F12``, ``PNO-LCCSD-F12``, ``PNO-LCCSD(T)-F12``. These methods are available from Molpro version 2018. They can be used in a black-box manner and give results which are usually very close to the corresponding canonical ones. For a review which describes the most important options and benchmarks see Q. Ma and H.-J. Werner, WIREs Comput Mol Sci. 2018;e1371, https://doi.org/10.1002/wcms.1371. Open-shell variants are under development and will be made available soon. Please see section for further details of the PNO methods.

The older PAO-based local correlation treatments are switched on by preceding the command name by an ``L``, i.e., by using the ``LMP2``, ``LMP3``, ``LMP4``, ``LQCISD``, ``LCCSD``, or ``LCISD`` commands.

The ``LQCISD`` and ``LCCSD`` commands can be appended by a specification for the perturbative treatment of triple excitations, e.g. ``LCCSD(T)``. Density fitting can be invoked by prepending the command name by ``DF-``, e.g. ``DF-LMP2``, ``DF-LCCSD(T)``, ``DF-LCCSD(T)-F12`` etc. In density fitting calculations an additional auxiliary basis set is needed. Details about choosing such basis sets and other options for density fitting are described in sections `density fitting approximations <quickstart.html#density-fitting-approximations>`__.

The general input for local MP2 or coupled cluster calculations with density fitting (recommended) is:

* **``DF-LMP2``,\ *options*** Local MP2 calculation
* **``DF-LCCSD``,\ *options*** Local CCSD calculation (includes DF-LMP2)
* **``DF-LCCSD(T)``,\ *options*** Local density fitted CCSD(T) calculation (include DF-LMP2 and DF-LCCSD)

The explicitly correlated counterparts are

* **``DF-LMP2-F12``,\ *options***
* **``DF-LCCSD-F12``,\ *options***
* **``DF-LCCSD(T)-F12``,\ *options***

There are many options and directives to control the local approximations (e.g., domains and pair classes). Here we only described the most important ones. For a full description please read the Molpro users manual.

.. _quickstart--orbital-localization:

Orbital localization
====================

By default, the orbitals are localized using the method of Pipek and Mezey (PM). Alternatively, natural localized molecular orbitals (NLMOs) can be used [see `Mol. Phys. <https://dx.doi.org/10.1080/00268970701628209>`__ **105**, 2753 (2007)] by specifying the option ``LOC_METHOD=NLMO``. Note that analytical energy gradients can be computed only with PM orbitals.

.. _quickstart--choice-of-domains:

Choice of domains
=================

The following applies to the PAO-LMP2 and PAO-LCCSD methods. In case of the new OSV-LMP2 and OSV-LCCSD(T) methods the standard domains only affect the pair approximations. See section `OSV calculations <quickstart.html#osv-calculations>`__ for more details.

.. _quickstart--standard-domains:

Standard domains
================

Standard domains are always determined first. They are used to define strong, close, weak, and distant pairs. More accurate results can be obtained with extended domains (see section `extended domains <quickstart.html#extended-domains>`__), but these extensions do not affect the pair classification.

The domains can be determined either by the method of Boughton and Pulay (BP) [J. Comp. Chem. **14**, 736 (1993)] or using natural population analysis (NPA) as described in `Mol. Phys. <https://dx.doi.org/10.1080/00268970701628209>`__ **105**, 2753 (2007). By default, the BP method is used with PM orbitals, while NPA method is employed with NLMOs. This default behaviour can be superceded using ``THRBP``\ =\ *value* (use the BP method with the given threshold) or ``NPASEL=``\ *value* (use the NPA method with the given threshold).

This BP method is somewhat basis set dependent and therefore the default value of ``THRBP`` depends on the basis set: 0.980 for AVDZ, 0.985 for AVTZ, and 0.990 for AVQZ. The NPA method is much less basis set dependent and the default value is ``NPASEL=0.03``.

.. _quickstart--extended-domains:

Extended domains
================

In order to increase the accuracy various options can be used to extend the domains (for details see Molpro manual). But note that the computational effort increases with the fourth power of the domain sizes and can therefore increase quite dramatically when extending domains. This does not affect the linear scaling behaviour in the asymptotic limit.

.. _quickstart--osv-calculations:

OSV calculations
================

Orbital specific virtuals are used if the option ``osvsel`` is given, e.g.

``df-lccsd(t),throsv=1.d-4``

``throsv is the threshold used to select the OSVs. For a given LMO $i$, as many OSVs are included as needed to reproduce the canonical pair energy $\epsilon_{ii}$ of the diagonal pair within this accuracy. See J. Chem. Phys. http:dx.doi.org/10.1063/1.3696963 for more details and benchmarks. Note that df-lccsd-F12 methods with OSVs are not implemented.``

.. _quickstart--choice-of-pair-classes:

Choice of pair classes
======================

The *strong*, *close*, *weak* and *distant* pairs are selected using distance or connectivity criteria as described in more detail in section `options for selection of pair classes <quickstart.html#options-for-selection-of-pair-classes>`__. *Strong* pairs are treated by CCSD, all other pairs by LMP2. However, if option ``keepcls=1`` is ised, the LMP2 close pair amplitudes are included in the LCCSD amplitude equations for the strong pairs. This is recommended (and default) for OSV and F12 calculations. In triples calculations, all orbital triples :math:`(ijk)` are included for which :math:`(ij)`, :math:`(ik)`, and :math:`(jk)` are *close pairs*. In addition, one of these pairs is restricted to be strong. The triples energy depends on the strong and close pair amplitudes. Thus, increasing the distance or connectivity criteria for close and weak pairs will lead to more accurate triples energies (and also to more accurate LCCSD energies if ``keepcsl=1`` is used). While for near equilibrium properties like geometries and harmonic vibrational frequencies the default values are normally appropriate, larger distance criteria are sometimes needed when computing energy differences, in particular barrier heights. In cases of doubt, ``RWEAK`` should first be increased until convergence is reached, and then ``RCLOSE`` can be varied as well. Such tests can be performed with small basis sets like cc-pVDZ, and the optimized values then be used in the final calculations with large basis sets.

Pair approximations only affect the LCCSD calculations (LMP2 is only affected by ``verydist``). The defaults for ``IWEAK``, ``ICLOSE``, and ``KEEPCLS`` are wck=2,1,0, respectively, for PAO-LCCSD, and 3,2,1 for OSV-LCCSD and all F12 methods.

.. _quickstart--options-for-selection-of-pair-classes:

Options for selection of pair classes
=====================================

There are two alternative modes for defining the pair classes: either *distance criteria* ``RCLOSE``, ``RWEAK``, ``RDIST``, ``RVDIST`` can be used. These are in Bohr and refer for a given orbital pair :math:`(ij)` to the minimum distance :math:`R^{(ij)}` between any atom in the standard orbital domains :math:`[i]` and any atom in the standard orbital domains :math:`[j]` . Alternatively, the *connectivity criteria* ``ICLOSE``, ``IWEAK``, ``IDIST``, ``IVDIST`` can be used. These refer to the minimum number of bonds between any atom contained in the standard domain :math:`[i]` and any atom contained in the standard domain :math:`[j]` The advantage of using connectivity criteria is the independence of the bond lengths, while the advantage of distance criteria (default) is that they are also effective in non-bonding situations. Only one of the two possibilities can be used, i.e., they are mutually exclusive (except that ``RDIST`` and ``RVDIST`` can be combined with ``ICLOSE,IWEAK``). The use of distance criteria is the default. Using connectivity criteria for pair selection requires to set the option ``USE_DIST=0``. ``USE_DIST=0`` is automatically implied if and connectivity criterion is explicitly defined.

* ``RCLOSE`` (default 1) Strong pairs are defined by :math:`0 \le R^{(ij)} \lt {\tt RCLOSE}`. Close pairs are defined by :math:`{\tt RCLOSE} \le R^{(ij)} \lt {\tt RWEAK}`.
* ``RWEAK`` (default 3) Weak pairs are defined by :math:`{\tt RWEAK} \le R^{(ij)} \lt {\tt RDIST}`.
* ``RDIST`` (default 8) Distant pairs are defined by :math:`{\tt RDIST} \le R^{(ij)} \lt {\tt RVDIST}`.
* ``RVDIST`` (default 15) Very distant pairs for which :math:`R^{(ij)} \ge`\ ``RVDIST`` are neglected.
* ``ICLOSE`` (default 1) Strong pairs are separated by less that ``ICLOSE`` bonds. Close orbital pairs are separated by at least ``ICLOSE`` bonds but less than ``IWEAK`` bonds.
* ``IWEAK`` (default 2) Weak orbital pairs are separated by at least ``IWEAK`` bonds but less than ``IDIST`` bonds.
* ``IDIST`` (default 5) Distant orbital pairs are separated by at least ``IDIST`` bonds but less than ``IVDIST`` bonds.
* ``IVDIST`` (default 8) Very distant orbital pairs (neglected) are separated by at least ``IVDIST`` bonds.

Setting a distance criterion to zero means that all pairs up to the corresponding class are treated as strong pairs. For instance, ``RCLOSE``\ =0 means that strong and close pairs are fully included in the LCCSD.

.. _quickstart--doing-it-right:

Doing it right
==============

Here we summarize only a few important aspects. Further information and hints can be found in the Molpro users manual.

.. _quickstart--basis-sets:

Basis sets
==========

For local calculations we recommend the use of generally contracted basis sets, e.g., the correlation consistent cc-pVnZ sets of Dunning and coworkers. For these basis sets the core basis functions are uniquely defined, and will always be eliminated if the defaults are used.

The correlation consistent basis sets are also recommended for all density fitting and explicitly correlated calculations, since optimized fitting and RI basis sets are available for each basis.

.. _quickstart--symmetry-and-orientation:

Symmetry and Orientation
========================

In local calculation, the use of symmetry should be disabled (option ``NOSYM``), since otherwise orbital localization is not possible. We also recommend to use the ``NOORIENT`` option to avoid unintended rotations of the molecule when the geometry changes. This is particularly important for geometry optimizations and for domain restarts in calculations of interaction energies. The ``NOSYM`` and ``NOORIENT`` option can be given on a ``SYMMETRY`` directive that must precede the geometry block, e.g.,

.. code-block:: text

   symmetry,nosym,noorient
   geometry={
     O1
     H1,O1,roh
     H2,O1,roh,h1,hoh
   }

.. _quickstart--localization:

Localization
============

By default, Pipek-Mezey (PM) localization is used and performed automatically in the beginning of a local correlation calculation. As mentioned in section `orbital localization <quickstart.html#orbital-localization>`__, it is also possible to use natural localized orbitals (NLMOs).

Poor localization is sometimes an intrinsic problem, in particular for strongly conjugated systems or when diffuse basis sets are used. This is caused by localization tails due to the overlapping diffuse functions. The NLMO method is less susceptible to such problems than the PM method. With PM localization problems are particularly frequent in calculations of systems with short bonds, e.g., aromatic molecules. Often such problems can be avoided using the option ``PMDEL=``\ :math:`n` with :math:`n=1` or :math:`2`. This means that the contributions of the :math:`n` most diffuse basis functions of each angular momentum type are ignored in the localization. This often yields much better localized orbitals when diffuse basis sets are used. For aug-cc-pVTZ, :math:`n=2` has been found to work very well, while for aug-cc-pVDZ :math:`n`\ =1

.. _quickstart--orbital-domains:

Orbital domains
===============

In most cases, the domain selection (cf. section `choice of domains <quickstart.html#choice-of-domains>`__ is uncritical for saturated molecules. Nevertheless, in particular for delocalized systems, it is recommended always to check the orbital domains, which are printed in the beginning of each local calculation. The orbital domains consist of all basis functions for a subset of atoms. These atoms are selected so that the domain spans the corresponding localized orbital with a preset accuracy (alterable with option ``THRBP``). A typical domain output, here for water, looks like this:

.. code-block:: text

    Orbital domains
   
      Orb.   Atom    Charge       Crit.
      2.1    1 O1     1.17        0.00
             3 H2     0.84        1.00
      3.1    1 O1     2.02        1.00
      4.1    1 O1     1.96        1.00
      5.1    1 O1     1.17        0.00
             2 H1     0.84        1.00

This tells you that the domains for orbitals 2.1 and 5.1 comprise the basis functions of the oxygen atom and and one hydrogen atom, while the domains for orbitals 3.1 and 4.1 consist of the basis function on oxygen only. The latter ones correspond to the oxygen lone pairs, the former to the two OH bonds, and so this is exactly what one would expect. For each domain of AOs, corresponding projected atomic orbitals (PAOs) are generated, which span subspaces of the virtual space and into which excitations are made. Options which affect the domain selection are described in section `choice of domains <quickstart.html#choice-of-domains>`__. Improper domains can result from poorly localized orbitals (see section `localization <quickstart.html#localization>`__ or a forgotten ``NOSYM`` directive. This does not only negatively affect performance and memory requirements, but can also lead to unexpected results.

The choice of domains usually has only a weak effect on near-equilibrium properties like equilibrium geometries and harmonic vibrational frequencies. More critical are energy differences like reaction energies or barrier heights. In cases where the electronic structure strongly changes, e.g., when the number of double bonds changes, it is recommended to compare DF-LMP2 and DF-MP2 results before performing expensive LCCSD(T) calculations.

The effect of domain approximations is strongly reduced in explicitly correlated calculations [e.g., DF-LCCSD(T)-F12] and the use of these methods (see below) is therefore strongly recommended (but the F12 option is not available for OSV methods).

.. _quickstart--explicitly-correlated-methods:

Explicitly correlated methods
-----------------------------

Explicitly correlated calculations provide a dramatic improvement of the basis set convergence of MP2 and CCSD correlation energies. Such calculations can be performed using the commands of the form

*command*, *options*

where *command* can be one of the following:

* **MP2-F12** Closed-shell canonical MP2-F12. The F12-corrections is computed using density fitting, and then added to the MP2 correlation energy obtained without density fitting. By default, ansatz 3C(FIX) is used. Other ansätze, as fully described in `J. Chem. Phys. <https://dx.doi.org/10.1063/1.2712434>`__ **126**, 164102 (2007) can also be used (cf. section `wave function Ansätze <quickstart.html#wave-function-ans-tze>`__).
* **DF-MP2-F12** As MP2-F12, but the DF-MP2 correlation energy is used. This is less expensive than MP2-F12 since the standard two-electron integrals and the non-density fitted MP2 energy need not to be computed.
* **DF-RMP2-F12** Spin-restricted open-shell DF-RMP2-F12 as described in `J. Chem. Phys. <https://dx.doi.org/10.1063/1.2889388>`__ **128**, 154103 (2008) By default, ansatz 3C(FIX) is used, but ansatz 3C(D) can also be used (cf. sections `wave function Ansätze <quickstart.html#wave-function-ans-tze>`__).
* **CCSD-F12** Closed-shell CCSD-F12 approximations as described in `J. Chem. Phys. <https://dx.doi.org/10.1063/1.2817618>`__ **127**, 221106 (2007) and `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3054300>`__ **130**, 054104 (2009). By default, the fixed amplitude ansatz 3C(FIX) is used and the CCSD-F12a and CCSD-F12b energies are computed. Optionally, the command can be appended by A or B, and then only the corresponding energy is computed. For more details see section `CCSD(T)-F12 <quickstart.html#ccsd-t-f12>`__.
* **CCSD(T)-F12** Same as CCSD-F12, but perturbative triples are added.
* **UCCSD-F12** Open-shell unrestricted UCCSD-F12 approximations as described in `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3054300>`__ **130**, 054104 (2009). Restricted open-shell Hartree-Fock (RHF) orbitals are used. Optionally, the command can be appended by A or B, and then only the corresponding energy is computed.
* **UCCSD(T)-F12** Same as UCCSD-F12, but perturbative triples are added.
* **DF-LMP2-F12** Closed-shell DF-MP2-F12/3\*A(D) with localized orbitals. Results for the fixed amplitude method DF-MP2-F12/3\*A(FIX) are also printed In order to use local RI and DF approximations as described in `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3040174>`__ **130**, 054106 (2009) special options are necessary, see user’s manual.
* **DF-LCCSD(T)-F12** Closed-shell DF-LCCSD(T)-F12/3\*A(FIX). This includes DF-LMP2-F12.

Note that in the local methods only ansatz 3\*A should be used (default), and F12 is not available for OSV methods.

.. _quickstart--options:

Options
=======

There are many options available for explicitly correlated methods, but sensible defaults are used for all of them. For details see the Molpro reference manual. The most important options are:

* ``DF_BASIS=basis`` Select the basis for density fitting (see section `density fitting approximations <quickstart.html#density-fitting-approximations>`__ for details). *basis* can either refer to a set name defined in the basis block, or to a default MP2 fitting basis (e.g., ``DF_BASIS=VTZ`` generates the ``VTZ/MP2FIT`` basis). By default, the MP2FIT basis that corresponds to the orbital basis is used.
* ``RI_BASIS=basis`` Select the basis for the resolution of the identity (RI). By default the JKFIT basis that corresponds to the chosen orbital basis is used. In conjunction with the VnZ-F12 basis sets, it is recommended to use the VnZ-F12/OPTRI sets of Yousaf and Peterson, J. Chem. Phys. **129**, 18410 (2008).
* ``ANSATZ=ansatz`` Select the explicitly correlated ansatz *ansatz* methods. See section `wave function Ansätze <quickstart.html#wave-function-ans-tze>`__ for the defaults and the Molpro manual for further details and possibilities. Normally the defaults should be used [3C(FIX) for canonical methods and 3\*A(LOC) for local methods].
* **``GEM_BETA``\ =\ *value*** Exponent for Slater-type frozen geminal (default 1.0 :math:`a_0^{-1}`).
* **``CABS_SINGLES``\ =0** Disable CABS singles correction. The default is ``CABS_SINGLES=1``.

In the following, we briefly summarize the meaning of these options and of the approximations that can be used. For more details and further references to related work of other authors see H.-J. Werner, T. B. Adler, and F. R. Manby, *General orbital invariant MP2-F12 theory*, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.2712434>`__ **126**, 164102 (2007) and G. Knizia and T. B. Adler and H.-J. Werner, *Simplified CCSD(T)-F12 methods: Theory and benchmarks*, JCP **130**, 054104 (2009).

.. _quickstart--reference-functions:

Reference functions
===================

The MP2-F12, CCSD-F12, and UCCSD-F12 methods must use conventional (non-density fitted) spin-restricted Hartree-Fock reference functions (HF or RHF). DF-HF cannot be used for these methods. This restriction is necessary to ensure that the Fock matrix is diagonal and consistent with the integrals used in these methods. For DF-MP2-F12, DF-LMP2-F12, and DF-RMP2-F12 either HF or DF-HF reference functions can be used.

.. _quickstart--wave-function-ans-tze:

Wave function Ansätze
=====================

The so called ”ansatz” determines the definition of the explicitly correlated wave function. This is to be distinguished from the various approximations that can be used to approximate the Hamiltonian matrix elements. For details see `J. Chem. Phys. <https://dx.doi.org/10.1063/1.2712434>`__ **126**, 164102 (2007). In MOLPRO the following wave function ansätze can be used (specified using option ``ansatz``) on the command line, even though the defaults it is recommended to use the defaults:

.. _quickstart--the-general-ansatz-ansatz-3c-full:

The general ansatz (ansatz=3C(FULL))
====================================

The conventional external pair functions are augmented by terms of the form

.. math::

   |u_{ijp}^{\rm F12}\rangle =  \sum_{p=\pm 1} \sum_{kl} T^{ijp}_{kl} \hat Q_{12} \hat F_{12} |kl\rangle \label{quickeq:uij}

This ansatz is orbital invariant (i.e., the same results are obtained with canonical or localized orbitals), but it often suffers from geminal basis set superposition errors. Furthermore, singularities may occur in the zeroth-order Hamiltonian, in particular for larger systems. Therefore, this ansatz is normally not recommended.

.. _quickstart--the-diagonal-ansatz-ansatz-3c-d:

The diagonal ansatz (ansatz=3C(D)
=================================

The sum over :math:`kl` in equation (`the general ansatz ({\tt ansatz=3C(FULL)}) <quickstart.html#the-general-ansatz-tt-ansatz-3c-full>`__) is restricted to :math:`ij`. This eliminates the geminal basis set superposition errors of the general ansatz. However, since orbital invariance is lost, localized orbitals should be used to obtain size consistent wavefunctions. In most cases, this ansatz yields the most accurate results for MP2-F12 or LMP2-F12.

.. _quickstart--the-fixed-amplitude-ansatz-ansatz-3c-fix:

The fixed amplitude ansatz (ansatz=3C(FIX)
==========================================

The wave function has the same form as for the diagonal ansatz, but the amplitudes are determined from the cusp conditions and fixed, i.e., :math:`T^{ij,1}_{ij}=1/2` for singlet pairs (:math:`p=1`) and :math:`T^{ij,-1}_{ij}=1/4` for triplet pairs (:math:`p=-1`). This restores the orbital invariance, and usually the results are almost as accurate as with the diagonal ansatz. This method is size consistent for any choice of orbitals. Since the (T) correction in CCSD(T)-F12 calculations requires the use of canonical orbitals, the FIX approximation is used by default in CCSD-F12 and CCSD(T)-F12 calculations.

.. _quickstart--the-correlation-factor-f12:

The correlation factor F12
==========================

In the F12 methods, the correlation factor :math:`\hat F_{12}` is approximated by a frozen expansion of Gaussian type geminals that are functions of the interelectronic distance :math:`r_{12}`. In principle, this can be any function, but normally a Slater function

.. math::

   F_{12}(r_{12})=-\beta^{-1}\exp(-\beta r_{12})

is used. By default this function is approximated by an expansion of six Gaussian functions, and the exponents and coefficients are optimized to obtain the best least squares fit, using a suitable weight function. The exponent :math:`\beta` can be chosen using the option ``gem_beta=``\ *value* (default ``gem_beta=1.0``).

It is also possible to use geminals with different exponents for core-core and core-valence calculation [see `Mol. Phys. <https://dx.doi.org/10.1080/00268976.2010.526641>`__ **109**, 407 (2011)] In this case the exponents are specified as

``gem_beta=$[\beta_1,\beta_2]$\\``
``gem_beta=$[\beta_1,\beta_2,\beta_3]$``

The smallest :math:`\beta` value is used for valence correlation, the second-smallest for core-valence and the largest for core-core pairs. If only 2 values are given, core-core and core-valence pairs are treated with the same exponent. Note that the ``core`` directive is usually needed to include correlation of inner-shell orbitals.

In addition, also linear R12-methods (:math:`F_{12}=r_{12}`) are available (DF-MP2-R12 and DF-LMP2-R12). However, these are no longer recommended since the non-linear correlation factor yields much better accuracy, numerical stability and convergence with respect to the AO, DF and RI basis sets.

.. _quickstart--basis-sets-1:

Basis sets
==========

In MOLPRO the F12 integrals can only be computed using density fitting (DF) approximations. The many electron integrals are approximated by resolutions of the identity (RI) expansions. Thus, F12 calculations require three different basis sets: the orbital (AO) basis, the DF basis, and the RI basis.

We recommend as AO basis sets the augmented correlation consistent basis sets (denoted AVnZ) or the specially optimized correlation consistent F12 basis sets (denoted VnZ-F12, cf. K.A. Peterson, T.B. Adler, and H.-J. Werner, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.2831537>`__ **128**, 084102 (2008)). Normally, triples zeta basis sets (AVTZ or VTZ-F12) yield excellent results that are close to the basis set limit. Diffuse basis functions are rather essential both for the HF and MP2-F12 energies, and therefore the standard VTZ sets are not recommended. If the AVnZ or VnZ-F12 orbital basis sets are used, suitable density fitting (DF) basis and resolution of the identity (RI) basis sets are automatically chosen. For the AV\ :math:`nZ` basis sets, the AVnZ/MP2FIT and VnZ/JKFIT basis sets are used for the DF and RI, respectively. For the V\ :math:`n`\ Z-F12 orbital basis sets, the corresponding ``OPTRI`` CABS basis sets are used by default. Other basis sets can be chosen using the ``DF_BASIS`` and ``RI_BASIS`` options (cf. section `options <quickstart.html#options>`__). See section `density fitting approximations <quickstart.html#density-fitting-approximations>`__ for more details about density fitting.

The following example shows a ccsd(t)-f12 calculation using the VTZ-F12 basis of Peterson et al., `J. Chem. Phys. <https://dx.doi.org/10.1063/1.2831537>`__ **128**, 084102 (2008), along with the associated RI basis set of Yousaf and Peterson, J. Chem. Phys. **129**, 18410 (2008):

.. code-block:: text

   ***,formaldehyde
   geometry={
   C
   O  , C , rco
   H1 , C , rch , O , hco
   H2 , C , rch , O , hco , H1 , 180
   }
   
   rco=1.182 Ang
   rch=1.102 Ang
   hco=122.1789 Degree
   
   basis=vtz-f12
   hf
   ccsd(t)-f12,ri_basis=vtz-f12/optri,df_basis=avtz
   e_F12a=energy(1)   !save F12a energy in variable e_F12a
   e_F12b=energy(2)   !save F12b energy in variable e_F12b

The given RI and DF basis sets would also be used by default. With the AVTZ orbital basis the input would read

.. code-block:: text

   basis=avtz
   hf
   ccsd(t)-f12,ri_basis=avtz/optri,df_basis=avtz

In this case the default would be (for historical reasons and backward compatibility)

.. code-block:: text

   basis=avtz
   hf
   ccsd(t)-f12,ri_basis=vtz/jkfit,df_basis=avtz

.. _quickstart--symmetry:

Symmetry
========

Symmetry cannot be used in the local DF-LMP2-F12 and DF-LCCSD(T)-F12 calculations. However, in canonical MP2-F12, DF-MP2-F12, DF-RMP2-F12, CCSD(T)-F12 and UCCSD(T)-F12 calculations Abelian symmetry can be used as usual; in these cases the preceding DF-MP2-F12 calculations will be automatically performed without symmetry, and the integrals that are necessary for subsequent CCSD-F12 or UCCSD-F12 calculations will be transformed to the symmetry adapted basis. This is fully automatic and transparent to the user. Note, however, that the prefix DF- turns off symmetry automatically, and if you want to use symmetry in the HF calculations preceding the DF-MP2-F12 or DF-MP2-F12 calculations the symmetry elements (or ``AUTO``) must be specified either in the geometry block, or on a ``SYMMETRY`` directive preceding the geometry block.

.. _quickstart--cabs-singles-correction:

CABS Singles correction
=======================

By default, the perturbative CABS singles correction as described in `J. Chem. Phys. <https://dx.doi.org/10.1063/1.2817618>`__ **127**, 221106 (2007) and `J. Chem. Phys. <https://dx.doi.org/10.1063/1.2889388>`__ **128**, 154103 (2008) is included in the reference energy of all MP2-F12 and CCSD-F12 calculations (now also in all local F12 calculations). The corrected reference energy is stored in variable ``ENERGR``, so that ``ENERGY-ENERGR`` are the total correlation energies.

The singles correction can be turned off by option ``SINGLES=0``, e.g.

``MP2-F12,CABS_SINGLES=0``

The contribution of core orbitals to the singles energy is not included by default, but can be turned on by option ``CORE_SINGLES``, e.g.

``MP2-F12,CORE_SINGLES=1``

.. _quickstart--ccsd-t-f12:

CCSD(T)-F12
===========

The CCSD-F12 and UCCSD-F12 programs first do DF-MP2-F12/3C(FIX) (closed-shell) or DF-RMP2-F12/3C(FIX) (open-shell) calculations, and then perform the CCSD-F12 (UCCSD-F12) without density fitting. By default, the CCSD-F12a and CCSD-F12b energies are both computed. A specific method can be requested by appending A or B to the -F12 suffix. Furthermore, instead of the 3C(FIX) ansatz, different ansätze (e.g. 3C) can be used. In this case the amplitudes of the explicitly correlated terms are determined in the MP2-F12 calculation and kept fixed in the CCSD-F12.

It should be noted that these methods involve approximations and do not yield the exact CCSD-F12 energies. Extensive benchmarks have shown that the CCSD-F12a method slightly overestimates the correlation energies, while CCSD-F12b underestimates them. For AVDZ or AVTZ basis sets, CCSD-F12a usually gives very good results, but for larger basis sets it may overestimate the basis set limit and converge from below to the limit. Thus, convergence may not be monotonic, and extrapolation of the correlation energies should not be attempted. CCSD-F12b usually converges monotonically from below to the limit and gives best results for AVQZ and larger basis sets. Thus, we currently recommend CCSD-F12a for AVDZ and AVTZ basis sets, and CCSD-F12b for larger basis sets (rarely needed).

The perturbative triples correction can be invoked by using CCSD(T)-F12 or UCCSD(T)-F12. There is no direct F12 correction to the triples, and therefore the basis set error of the triples is not affected by the F12 (small changes of the triples energy arise from the fact that the doubles amplitudes are affected by the F12 terms). In many cases, a simple and pragmatic improvement of the triples energy can be obtained by scaling the triples energy contribution as

.. math::

   \Delta E_{(T*)} = \Delta E_{(T)}*E_{corr}^{MP2-F12}/E_{corr}^{MP2}

This can be done automatically by setting option ``SCALE_TRIP=1``, i.e.

``CCSD(T)-F12,SCALE_TRIP=1``

.. _quickstart--advanced-features-of-molpro:

Advanced features of Molpro
---------------------------

In the following sections, examples for some more special capabilities of Molpro are given. This description is not exhaustive. For more complete information, please refer to the reference manual.

.. _quickstart--memory-control:

Memory control
==============

Molpro stores all internal data in a single big working area, which is allocated dynamically in the beginning of the calculation. The default amount of memory is 8 MW (64 Mb). For big calculations more memory may be needed, and the default can then be modified using the ``memory`` directive. This should be the first command in the input (after the ``**`` title card, if present, as shown in the following example.

.. code-block:: text

   ***,title
   memory,16,m            !allocate 16 MW of memory
   geometry={...}         !define the nuclear coordinates
   basis=vdz              !Select basis set
   hf                     !Perform HF calculation
   ccsd(t)                !Perform ccsd(t) calculation

The amount of memory needed depends on the size of the molecule, the basis set, the symmetry of the molecule, and the methods used, and therefore it is difficult to predict it in advance. Most calculation run with 16 MW or less, but in big cases with low symmetry more may be required. A rather safe choice is to specify 64 MW, but of course this requires that your machine has sufficient memory (in this case more than 512 MB). The memory can also be given using the ``-m`` option on the ``molpro`` command line, see section `how to run {Molpro} <quickstart.html#how-to-run-molpro>`__. It a ``memory`` card is given, it has preference over the command line option.

.. _quickstart--restarting-calculations:

Restarting calculations
=======================

By default, and in all examples shown so far, scratch files are used to store all intermediate data Molpro needs, and the user will normally not see these files at all. However, it is possible to save computed data as orbitals and energies in named (permanent) files and use these for restarting a calculation at a later stage. Molpro uses a number of different files, but only one or two of them are needed for a restart. File 1 holds the one- and two electron integrals and related information, while on file 2 the wavefunction information like orbitals, orbital energies, and optionally CI-vectors are stored. Thus, file 2 is essential for restarting a calculation, while the integrals on file 1 can either be restarted or recomputed.

The use of named files can be requested using the ``file`` directive, which should be given immediately after the ``memory`` command (if present), e.g.,

.. code-block:: text

   ***,title
   memory,16,m            !allocate 16 MW of memory
   file,1,filename.int    !allocate permanent integral file
   file,2,filename.wfu    !allocate permanent wave-function (dump) file
   geometry={...}         !define the nuclear coordinates
   basis=vdz              !Select basis set
   hf                     !Perform HF calculation
   ccsd(t)                !Perform ccsd(t) calculation

If the same files are used in a subsequent calculation, Molpro will automatically recover all data saved on the given files. For instance, if the following input is used after the previous example, the integrals and orbitals will be restarted and used for the subsequent casscf and MRCI calculations:

.. code-block:: text

   ***,title
   memory,16,m            !allocate 16 MW of memory
   file,1,filename.int    !allocate permanent integral file
   file,2,filename.wfu    !allocate permanent wave-function (dump) file
   casscf                 !casscf, using previous scf orbitals as starting guess
   mrci                   !mrci using casscf reference wavefunction

If only file 2 is defined in the input, the integrals will automatically be recomputed, as in the following input. Note that in most cases, file 1 can be very large (it contains the two-electron integrals), and the cost of recomputing the integrals can be a small fraction of the overall time; it is therefore usually sensible in this way to avoid declaring the file as permanent.

.. code-block:: text

   ***,title
   memory,16,m            !allocate 16 MW of memory
   file,2,filename.wfu    !allocate permanent wave-function (dump) file
   casscf                 !casscf, using previous hf orbitals as starting guess
   mrci                   !mrci using casscf reference wavefunction

The automatic restart mechanism can be disabled by specifying ``new`` after the filename(s), e.g.,

.. code-block:: text

   ***,title
   memory,16,m                !allocate 16 MW of memory
   file,2,filename.wfu,new    !allocate a new permanent wave-function (dump) file.
                              !If the file exists, overwrite it.
   hf                         !Perform hartree-Fock calculation
   casscf                     !casscf, using hf orbitals as starting guess

Note that if permanent files are used, it is important to take care that two simultaneous jobs do not attempt to use the same file!

.. _quickstart--variables-1:

Variables
=========

Results and other values can be stored in variables for use at a later stage of the calculations. Variables can simply be set in the input as

``name=value``

Variables can also be one-dimensional arrays, in which case the format is

``name=[value1,value2,value3,...]``

The current dimension of such an array is ``#name``.

Molpro stores certain results in variables with predefined names. The most important ones are

* ``ORBITAL`` Record in which last computed orbitals are stored
* ``ENERGR(istate)`` Reference energy for state *istate* in MRCI and CCSD.
* ``ENERGY(istate)`` last computed total energy for state *istate*.
* ``ENERGC`` Total energy excluding perturbative triples correction

(set only in the CCSD/QCI program).

* ``ENERGD(istate)`` Total energy for state *istate* including Davidson correction

(set only in ``CI``).

* ``ENERGP(istate)`` Total energy for state *istate* including Pople correction

(set only in ``CI``).

* ``ENERGT(1)`` Total energy including perturbative triples ``(T)`` correction

(set only in ``CCSD(T), QCI(T)``).

* ``ENERGT(2)`` Total energy including perturbative triples ``[T]`` correction

(set only in ``CCSD(T), QCI(T)``).

* ``ENERGT(3)`` Total energy including perturbative triples ``-t`` correction

(set only in ``CCSD(T), QCI(T)``).

* ``EMP2`` holds MP2 energy in MPn, CCSD, BCCD, or QCISD calculations, and RS2 energy in MRPT2 (CASPT2) calculations.
* ``EMP3`` holds MP3 energy in MP3 and MP4 calculations, and RS3 energy in MRPT3 (CASPT3) calculations.
* ``EMP4`` holds MP4(SDQ) energy in MP4 calculations. The total MP4(SDTQ) energy is stored in variable ``ENERGY``.
* ``ZPE`` Zero-point energy in cm\ :math:`^{-1}`, set by the ``FREQUENCIES`` program.
* ``HTOTAL`` Total enthalpy at normal conditions (in a.u.), set by the ``FREQUENCIES`` program. This includes the zero-point energy.
* ``GTOTAL`` Total free energy at normal conditions (in a.u.), set by the ``FREQUENCIES`` program. This includes the zero-point energy.
* ``DMX,DMY,DMZ`` Dipole moments (when computed).
* ``STATUS`` status of last step (1=no error, -1=error or no convergence)

Variables in CCSD(T)-F12 and LCCSD(T)-F12 calculations:

* ``ENERGC(1)`` LCCSD-F12a energy
* ``ENERGC(2)`` LCCSD-F12b energy
* ``ENERGY(1)`` LCCSD(T)-F12a energy
* ``ENERGY(2)`` LCCSD(T)-F12b energy
* ``EF12`` F12 contribution to energy MP2-F12. In CCSD(T)-F12 and LCCSD(T)-F12 calculations the MP2-F12 energy can be obtained as ``EMP2+EF12``.

Variables for unit conversions. Multiplying a variable in atomic units by these variables yields:

* **``TOANG``:** distance in Å.
* **``TOKJ``:** energy in kJ.
* **``TOKCAL``:** energy in kcal.
* **``TOEV``:** energy in eV.
* **``TOCM``:** energy in cm\ :math:`^{-1}`.

See reference manual for further variables.

.. _quickstart--print-options:

Print options
=============

Molpro has very many print options as described in detail in the reference manual for the various methods, but in practice only a few of them are needed. In general, there are two kinds of print options: either global ones, specified with the ``gprint`` directive, being used by all methods, or local ones, given on ``print`` directives, being used only in one job step. The local print commands are part of the input for a specific method and must therefore directly follow the corresponding command. On the other hand, global print options act on all subsequent methods. For example

.. code-block:: text

   gprint,orbitals          !global print option: hf and casscf orbitals
                            !are printed
   hf
   casscf

.. code-block:: text

   {hf
   print,orbitals}         !local print option, hf orbitals are printed
   
   casscf                   !casscf orbitals are not printed

To avoid confusion and unexpected results, we recommend to use global print options only, except for special debugging purposes. The most important global print options are

.. code-block:: text

   gprint,basis             !print basis set information
   gprint,orbitals          !print occupied orbitals
   gprint,orbitals=2        !print occupied and the two lowest virtual orbitals
                            !in each symmetry
   gprint,civector          !print configuration coefficients

Note that by default only CI coefficients larger than 0.05 are printed. See section `convergence thresholds <quickstart.html#convergence-thresholds>`__ for modifying this threshold.

``Several print options can be given on one gprint directive, e.g.,``

``gprint,basis,orbitals=1,civector``

.. _quickstart--convergence-thresholds:

Convergence thresholds
======================

As for the print options, there are global and local thresholds, specified using the ``gthresh`` and ``thresh`` directives, respectively. Here we only mention some useful global thresholds (default values are shown).

.. code-block:: text

   gthresh,energy=1.d-6     !convergence threshold for energy.
                            !This affects all iterative methods
                            !In HF, the value is further divided by 100 to achieve good enough
                            !convergence for subsequent correlation calculations; in DFT, it is divided by 10
   gthresh,orbital=1.d-5    !convergence threshold for orbitals.
                            !This affects scf only
   gthresh,step=1.d-3       !convergence threshold for orbital rotations
                            !This affects mcscf only
   gthresh,gradient=1.d-2   !convergence threshold for gradient with respect to
                            !orbital rotations. This affects mcscf only
   gthresh,civec=1.d-5      !convergence threshold for ci-coefficients in ci and ccsd.
   gthresh,optgrad=3.d-4    !threshold for gradient in geometry optimizations
   gthresh,optenerg=1.d-6   !threshold for energy in geometry optimizations
   gthresh,twoint=1.d-11    !Threshold for neglect of small 2-electron integrals
   gthresh,compress=1.d-11  !Accuracy of integral compression (depends on twoint)
   gthresh,printci=0.05     !print all ci-coefficients larger than 0.05
   gthresh,punchci=0.05     !write all ci-coefficients larger than 0.05 to the punch file

Note that the energy threshold also affects the defaults for some other thresholds such as ``orbital``, ``step``, and ``civec``, and therefore it is normally sufficient to lower the energy threshold if high accuracy is needed.

Any number of thresholds can be specified on a single ``gthresh`` directive, e.g.,

``gthresh,energy=1.d-8,printci=0.03``

.. _quickstart--program-control-using-do-loops-if-blocks-and-goto-commands:

Program control using do loops, if blocks and goto commands
===========================================================

Molpro also allows the writing of simple input programs, which check for conditions or perform loops over certain parts of the input. ``IF`` blocks and ``DO`` loops have a similar form as in Fortran.

``One line IF:``

``IF (condition) command``

If more than one command depends on the condition, ``IF`` blocks can be used:

.. code-block:: text

   IF (condition) THEN
      commands
   END IF

or

.. code-block:: text

   IF (condition) THEN
      commands
   ELSE
      commands
   END IF

Also the structure of ``DO`` loops is as in Fortran:

.. code-block:: text

   DO ivar=istart,iend,[increment]
    commands
   ENDDO

``ivar is the loop index variable, istart, iend, increment are either numbers or variables. The default for increment is 1.``

Examples:

Loop over several geometries (potential curve for HCl):

.. code-block:: text

   ***,HCl
   geometry={        !Z-matrix geometry input
   h
   cl,h,r
   }
   
   r=1.5             !start value for bond distance
   hf                !Hartree-Fock for start geometry
   
   do i=1,10         !loop over bond distances
   
   casscf;           !perform casscf
   ecas(i)=energy    !save casscf energy in array ecas
   mrci              !perform mrci
   rhcl(i)=r         !save distances in array rhcl
   emrci(i)=energy   !save mrci energies in array emrci
   emrda(i)=energd   !save Davidson corrected energies in array emrda
   
   r=r+0.2           !increment r
   end do

Alternatively, one could predefine a number of distances:

.. code-block:: text

   ***,HCl
   
   rhcl=[1.6,1.8,2.0,2.2,2.3,2.4,2.5,2.7,3.0,3.5,4.0,5.0,6.0,7.0]
   
   geometry={        !Z-matrix geometry input
   h
   cl,h,r
   }
   
   do i=1,#rhcl      !loop over all distances
   r=rhcl(i)         !set r to current bond distance
   
   if(i.eq.1) then   !in first calculation, do Hartree-Fock
     hf              !Hartree-Fock for start geometry
   end if
   
   casscf;           !perform casscf
   ecas(i)=energy    !save casscf energy in array ecas
   mrci              !perform mrci
   rhcl(i)=r         !save distances in array rhcl
   emrci(i)=energy   !save mrci energies in array emrci
   emrda(i)=energd   !save Davidson corrected energies in array emrda
   end do

One can skip to some command later in the input using ``GOTO``. For instance

.. code-block:: text

   if(orbital.ne.0) goto casscf   !skip to casscf if an orbital record exists
   hf                             !Hartree-Fock
   casscf;                        !casscf

.. _quickstart--tables-and-plotting:

Tables and Plotting
===================

The results of the previous calculation can be printed in form of a table and plotted using the freely available plotting program ``xmgrace``. Appending the previous input by

.. code-block:: text

   {table,rhcl,ecas,emrci,emrda   !print a table
   plot,file='hcl.plot'          !generate an xmgrace plot file
   Title,Results for HCl}        !title of table

prints the following table

.. code-block:: text

    Results for HCl
   
      RHCL        ECAS           EMRCI          EMRDA
       1.6   -459.8049671   -459.9476516   -459.9549021
       1.8   -459.9690821   -460.1118784   -460.1192275
       2.0   -460.0545599   -460.1972494   -460.2046870
       2.2   -460.0940081   -460.2362450   -460.2437423
       2.3   -460.1028655   -460.2447475   -460.2522596
       2.4   -460.1067696   -460.2482178   -460.2557336
       2.5   -460.1069614   -460.2479059   -460.2554148
       2.7   -460.0998440   -460.2396165   -460.2470838
       3.0   -460.0793517   -460.2171250   -460.2244794
       3.5   -460.0401054   -460.1744682   -460.1815696
       4.0   -460.0085291   -460.1399223   -460.1467670
       5.0   -459.9768057   -460.1047967   -460.1113263
       6.0   -459.9685139   -460.0955779   -460.1020174
       7.0   -459.9668469   -460.0937046   -460.1001220

Subsequent execution of

``xmgrace hcl.plot``

yields the following plot

.. image:: /media/hcl.svg
   :alt: hcl.svg
   :width: 500px

.. _quickstart--basis-set-extrapolation:

Basis set extrapolation
=======================

Basis set extrapolation can be carried out for correlation consistent basis sets using

``EXTRAPOLATE,BASIS=basislist,options``

where basislist is a list of at least two basis sets separated by colons, e.g. AVTZ:AVQZ:AV5Z. Some extrapolation types need three or more basis sets, others only two. The default is to use :math:`n^{-3}` extrapolation of the correlation energies, and in this case two subsequent basis sets and the corresponding energies are needed. The default is not to extrapolate the reference (HF) energies; the value obtained with the largest basis set is taken as reference energy for the CBS estimate. However, extrapolation of the reference is also possible by specifying the ``METHOD_R`` option.

The simplest way to perform extrapolations for standard methods like MP2 or CCSD(T) is to use, e.g.

.. code-block:: text

   ***,H2O
   memory,32,m
   gthresh,energy=1.d-8
   
   r =   0.9572 ang, theta =  104.52
   geometry={O;
             H1,O,r;
             H2,O,r,H1,theta}
   
   basis=avtz
   hf
   ccsd(t)
   extrapolate,basis=avqz:av5z
   
   table,basissets,energr,energy-energr,energy
   head,basis,ehf,ecorr,etot

This will perform the first calculation with AVTZ basis, and then compute the estimated basis set limit using the AVQZ and AV5Z basis sets. The correlation energy obtained in the calculation that is performed immediately before the extrapolate command will be extrapolated (in this case the CCSD(T) energy), and the necessary sequence of calculations [here HF;CCSD(T)] will be automatically carried out. Unless otherwise specified (see below), the Hartree-Fock energy is taken from the largest basis set and not extrapolated.

The resulting energies are returned in variables ENERGR (reference energies), ENERGY (total energies), and ENERGD (Davidson corrected energy if available); the corresponding basis sets are returned in variable BASISSETS. The results can be printed, e.g., in a table as shown above, or used otherwise. The above input produces the table

.. code-block:: text

    BASIS       EHF           ECORR          ETOT
    AVQZ    -76.06600082   -0.29758099   -76.36358181
    AV5Z    -76.06732050   -0.30297495   -76.37029545
    CBS     -76.06732050   -0.30863418   -76.37595468

The extrapolated total energy is also returned in variable ECBS (ECBSD for Davidson corrected energy if available).

In order to extrapolate the HF energy as well (for example using Karton-Martin extrapolation), one can modify the input as follows:

``extrapolate,basis=avqz:av5z,method_r=km``

This yields

.. code-block:: text

    BASIS           EREF            ECORR           ETOT
    AVQZ        -76.06600082     -0.29758099    -76.36358181
    AV5Z        -76.06732050     -0.30297495    -76.37029545
    CBS         -76.06754138     -0.30863418    -76.37617556

Alternatively, one can do the energy calculations manually and pass the energies to be extrapolated to extrapolate via variables. This is more flexible and allows to carry out different extrapolations with the same energies.

For example:

.. code-block:: text

   ***,H2O
   memory,32,m
   gthresh,energy=1.d-8  !energy convergence threshold
   
   r =   0.9572 ang, theta =  104.52
   geometry={O;
             H1,O,r;
             H2,O,r,H1,theta}
   
   basis=vqz
   hf
   ccsd(t)
   eref(1)=energr  !VQZ reference (HF) energy
   etot(1)=energy  !VQZ ccsd(t) total energy
   
   basis=v5z
   hf
   ccsd(t)
   eref(2)=energr  !V5Z reference (HF) energy
   etot(2)=energy  !V5Z ccsd(t) total energy
   
   text,extrapolate total energy:
   extrapolate,basis=vqz:v5z,etot=etot
   
   text,extrapolate correlation energy only:
   extrapolate,basis=vqz:v5z,etot=etot,eref=eref
   
   text,extrapolate reference and correlation energies separately:
   extrapolate,basis=vqz:v5z,etot=etot,eref=eref,method_r=km

This yields

For extrapolation of the total energy:

.. code-block:: text

    BASIS           ENERGY
    VQZ         -76.35979334
    V5Z         -76.36904020
    CBS         -76.37874183

For extrapolation of the correlation energy only:

.. code-block:: text

    BASIS           EREF            ECORR           ETOT
    VQZ         -76.06483534     -0.29495800    -76.35979334
    V5Z         -76.06709083     -0.30194937    -76.36904020
    CBS         -76.06709083     -0.30928458    -76.37637541

For separate extrapolation of reference and correlation energies:

.. code-block:: text

    BASIS           EREF            ECORR           ETOT
    VQZ         -76.06483534     -0.29495800    -76.35979334
    V5Z         -76.06709083     -0.30194937    -76.36904020
    CBS         -76.06746834     -0.30928458    -76.37675292

.. _quickstart--interface-to-molden:

Interface to MOLDEN
===================

The geometries and orbitals can be saved for visualization using ``MOLDEN`` (see `''MOLDEN'' <https://www3.cmbi.umcn.nl/molden>`__) using the ``PUT`` directive. In frequency calculations, also the normal modes are saved. An example is given below:

.. code-block:: text

   ***,H2O
   angstrom                !distances in angstrom
   geometry={              !z-matrix input for h2o
   o
   h,o,roh
   h,o,roh,h,theta
   }
   
   roh=1.0                 !bond distance
   theta=104.0             !bond angle
   
   hf                      !do hartree-fock
   optg                    !optimize geometry at hf level
   frequencies             !compute harmonic frequencies
   put,molden,h2o.molden;  !save results in file h2o.molden

The file h2o.molden can be used directly as input to *MOLDEN*.
