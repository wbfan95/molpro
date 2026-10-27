.. _the_tdhf_and_tdks_programs--the-tdhf-and-tdks-programs:

The TDHF and TDKS programs
==========================

Real-time electronic dynamics using time-dependent Hartree-Fock and time-dependent Kohn-Sham theories can be performed using the commands ``TDHF`` and ``TDKS`` respectively, which have to be preceded by a ``HF`` and ``KS`` command. Unrestricted versions are available through ``TDUHF`` and ``TDUKS`` and should be preceded by ``UHF`` and ``UKS`` runs respectively. All methods require symmetry to be switched off. For details on the theory and methods see H. Eshuis, G. G. Balint-Kurti and F. R. Manby, *J. Chem. Phys.* :math:`\mathbf{128}`, 114113 (2008), and references therein. The commands take several options:

.. code-block:: text

   command,t=,dt=,ns=,ng=,grsize=,print=;
   PULSE,options

The total propagation time (in au) is set by *t*; *dt* sets the timestep and *ns* the number of steps, where two of the three have to be provided. *ng* sets the number of grid points in one dimension (default = 0) and *grsize* the grid size in bohr (default = 10 bohr). Setting *ng* :math:`>2` switches on the calculation of quantum currents (see below). The option *print* determines the level of output (0=normal output, 1=object linear in matrices, 2=matrices as well, :math:`>2` debug). The subcommand ``PULSE`` determines the envelope used, and takes several options depending on the envelope selected. Possibilities are:

``NONE: no pulse, no options``

``STEP, e_x, e_y, e_z, length\\``
a DC-field of strength :math:`e_q` is applied in the :math:`q`\ th direction for a total time *length* (in au)

``DC, e_x, e_y, e_z, \alpha\\``
a DC-field of strength :math:`e_q` is applied in the :math:`q`\ th direction. The field is switched on exponentially with a rate determined by :math:`\alpha`.

``TRAP, e_x, e_y, e_z, \omega, \alpha\\``
an oscillating field of strength :math:`e_q` is applied in the :math:`q`\ th direction. The field oscillates with angular frequency :math:`\omega`. The envelope reaches :math:`e_q` in one period of the field, stays constant for :math:`\alpha` periods and then decays to zero in one period.

``CW, e_x, e_y, e_z, \omega\\``
an oscillating field of strength :math:`e_q` is applied in the :math:`q`\ th direction. The field oscillates with angular frequency :math:`\omega`. No envelope present.

``CWSIN, e_x, e_y, e_z, \omega, \alpha\\``
an oscillating field of strength :math:`e_q` is applied in the :math:`q`\ th direction. The field oscillates with angular frequency :math:`\omega` and is switched on using a :math:`\sin^2` envelope, where :math:`\alpha` determines how fast the field is switched on.

``CWGAUSS, e_x, e_y, e_z, \omega, \alpha\\``
like ``CWSIN``, but with a Gaussian envelope

The finite pulses ``TRAP`` and ``STEP`` produce an absorption spectrum obtained from the time-dependent dipole moment sampled after the field is switched off. It is located in //(:math:`input).spec//, or in //molpro.spec// when running interactively, and contains of 4 columns, which contain energy (eV) and the absorption in the`\ x,
y,z$ direction respectively.

All runs produce a file *($input).dat* (or *molpro.dat*) which contains time-dependent properties, like the components of the field, components of the dipole moment, total energy, orbital occupation numbers, orbital energies and total number of electrons. The Molpro output file specifies the order of the data in the file. For very long runs the size of the file is restricted by printing only every twentieth set of data.

In case of an unrestricted run three files are produced:  //(:math:`input).dat, (`\ input)a.dat, (:math:`input)b.dat//. The first file contains the generic data about the field, total energy, dipole moments and the expectation value of the total spin operator. The other two files contain the orbital energies and occupation numbers for the`\alpha\ :math:`and`\beta$ electrons respectively.

``TDKS`` and ``TDUKS`` use the options provided by the ``KS`` and ``UKS`` commands. At the moment ``TDKS``/``TDUKS`` suffers from numerical instabilities when using strong fields. Divergence of the energy is observed, possibly due to the use of quadrature for the evaluation of the potential.

Quantum currents will be calculated when choosing :math:`ng>2`. A cubic grid will be computed of size *grsize* with a total of :math:`ng^3` gridpoints. The imaginary part of the density will be summed at every timestep and after the dynamics the total current will be evaluated at every gridpoint. The user can extract the required data from this array by printing out parts of it, or by integrating over point, but this requires actual coding, as this has not been implemented sufficiently neat. It is also straightforward to evaluate the currents at every timestep or at selected timesteps. This is not done automatically, because it slows down the dynamics considerably.
