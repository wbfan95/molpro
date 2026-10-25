.. raw:: html

   <span id="do-loops"></span>

.. raw:: html

   <span id="geometry-optimizations"></span>

.. raw:: html

   <span id="simplified-input"></span>

.. raw:: html

   <span id="tables"></span>

.. _introductory_examples--introductory-examples:

Introductory examples
=====================

This section explains some very simple calculations in order to help the new user to understand how easy things can be.

.. _introductory_examples--using-the-molpro-command:

Using the molpro command
========================

Perform a simple SCF calculation for molecular hydrogen. The input is typed in directly and the output is sent to the terminal:

.. code-block:: text

           molpro <<!
           basis=vdz;
           geometry={angstrom;h1;h2,h1,.74}
           hf
           !

The same calculation, with the data taken from the file ``h2.inp``. The output is sent to h2.out. On completion, the file ``h2.pun`` is returned to the current directory and the file ``h2.wf`` to the directory ``$HOME/wfu`` (this is the default):

.. code-block:: text

           molpro h2.inp

h2.inp contains:

.. code-block:: text
   :caption: examples/h2.inp

           ***,H2
           file,2,h2.wf,new;
           punch,h2.pun;
           basis=vdz;
           geometry={angstrom;h1;h2,h1,.74}
           hf

As before, but the file ``h2.wf`` is sent to the directory ``/tmp/wfu``:

.. code-block:: text

   molpro -W /tmp/wfu h2.inp

.. _introductory_examples--simple-scf-calculations:

Simple SCF calculations
=======================

The first example does an SCF calculation for H\ :math:`_2`\ O, using all possible defaults.

.. code-block:: text
   :caption: examples/h2o_scf.inp

   ***,h2o                   !A title
   r=1.85,theta=104          !set geometry parameters
   geometry={O;              !z-matrix geometry input
             H1,O,r;
             H2,O,r,H1,theta}
   hf                        !closed-shell scf

In the above example, the default basis set (``VDZ``) is used. We can modify the default basis using a ``BASIS`` directive as you can see in the modified example shown in [[
basis_input#default_basis_sets\|default basis sets]].

.. _introductory_examples--geometry-optimizations:

Geometry optimizations
======================

Now we can also do a geometry optimization, simply by adding the card ``OPTG``.

.. code-block:: text
   :caption: examples/h2o_scfopt_631g.inp

   ***,h2o                   !A title
   r=1.85,theta=104          !set geometry parameters
   geometry={O;              !z-matrix geometry input
             H1,O,r;
             H2,O,r,H1,theta}
   basis=6-31g**             !use Pople basis set
   hf                        !closed-shell scf
   optg                      !do scf geometry optimization

.. _introductory_examples--ccsd-t:

CCSD(T)
=======

The following job does a CCSD(T) calculation using a larger (``VTZ``) basis (this includes an :math:`f` function on oxygen and a :math:`d` function on the hydrogens).

.. code-block:: text
   :caption: examples/h2o_ccsdt_vtz.inp

   ***,h2o                   !A title
   r=1.85,theta=104          !set geometry parameters
   geometry={O;              !z-matrix geometry input
             H1,O,r;
             H2,O,r,H1,theta}
   basis=VTZ                 !use VTZ basis
   hf                        !closed-shell scf
   ccsd(t)                   !do ccsd(t) calculation

Alternatively, the input could be written as

.. code-block:: text

   ***,h2o                   !A title
   r=1.85,theta=104          !set geometry parameters
   geometry={O;              !z-matrix geometry input
             H1,O,r;
             H2,O,r,H1,theta}
   
   run ccsd(t) basis=vtz

or, even shorter:

.. code-block:: text

   r=1.85,theta=104          !set geometry parameters
   run ccsd(t) basis=vtz geometry={O;H1,O,r;H2,O,r,H1,theta}

In these cases the Hartree-Fock calculation (hf) is implied by the ``run`` command. For more details and examples see :doc:`Simple Input <quickstart>`.

.. _introductory_examples--casscf-and-mrci:

CASSCF and MRCI
===============

Perhaps you want to do a CASSCF and subsequent MRCI for comparison. The following uses the full valence active space in the CASSCF and MRCI reference function.

.. code-block:: text
   :caption: examples/h2o_mrci_vtz.inp

   ***,h2o                   !A title
   r=1.85,theta=104          !set geometry parameters
   geometry={o;              !z-matrix geometry input
             h1,O,r;
             h2,O,r,H1,theta}
   basis=vtz                 !use VTZ basis
   hf                        !closed-shell scf
   ccsd(t)                   !do ccsd(t) calculation
   casscf                    !do casscf calculation
   mrci                      !do mrci calculation

.. _introductory_examples--simplified-input:

Simplified input
================

It is possible to use the ``RUN`` command to execute single programs. In this case the input can be written in a single line. For more details and examples see :doc:`Simple Input <quickstart>`.

.. _introductory_examples--tables:

Tables
======

You may now want to print a summary of all results in a table. To do so, you must store the computed energies in variables:

.. code-block:: text
   :caption: examples/h2o_table.inp

   ***,h2o                   !A title
   r=1.85,theta=104          !set geometry parameters
   geometry={o;              !z-matrix geometry input
             h1,O,r;
             h2,O,r,H1,theta}
   basis=vtz                 !use VTZ basis
   hf                        !closed-shell scf
   e(1)=energy               !save scf energy in variable e(1)
   method(1)=program         !save the string 'HF' in variable method(1)
   
   ccsd(t)                   !do ccsd(t) calculation
   e(2)=energy               !save ccsd(t) energy in variable e(2)
   method(2)=program         !save the string 'CCSD(T)' in variable method(2)
   
   casscf                    !do casscf calculation
   e(3)=energy               !save scf energy in variable e(3)
   method(3)=program         !save the string 'CASSCF' in variable method(3)
   mrci                      !do mrci calculation
   e(4)=energy               !save scf energy in variable e(4)
   method(4)=program         !save the string 'MRCI' in variable method(4)
   
   table,method,e            !print a table with results
   title,Results for H2O, basis=$basis  !title for the table

.. code-block:: text
   :caption: examples/h2o_tab.inp

   ***,h2o scf (C2v)
   file,1,h2o.int,new
   file,2,h2o.wfu,new
   
   theta=104                 !set geometry parameters
   basis={                   !define  basis
   sp,o,dz;c;d,o,1d          !DZP basis for O
   s,h,dz;c;p,h,1p           !DZP basis for H
   }
   
   symmetry,x,y
   geometry={
   o
   h,,1.4,,r(i)
   h,,-1.4,,r(i)}
   r=[1.85,1.90]
   
   do i=1,#r
   {hf;occ,3,1,1;             !closed-shell scf
   expec,qm}
   e(i)=energy
   de(i)=(e(i)-e(1))*tokcal
   dip(i)=dmz(1)
   quadx(i)=qmxx(1)
   quady(i)=qmyy(1)
   quadz(i)=qmzz(1)
   enddo
   
   {table,e,dip,quadx,quady,quadz,de
   save,h2o.tab
   title,Using defaults
   head,energy,'dipole moment','quadrupole z'
   }
   
   {table,e,dip,quadx,quady,quadz,de
   save,h2o.tab
   ftyp,f,d,f,d,f,f
   digits,8,4,4,4,4,2
   title,Using ftyp=f,d,f,d,f,f and digits=8,4,4,4,4,2
   head,energy,'dipole moment','quadrupole z'
   }
   
   {table,e,dip,quadx,quady,quadz,de
   save,h2o.tab
   format,(5x,f14.8,f10.4,2x,f9.4,2x,2f12.3,5x,f9.2)
   title,Using explicit format=(5x,f14.8,f10.4,2x,f9.4,2x,2f12.3,5x,f9.2)
   head,energy,'dipole moment','quadrupole z'
   }
   ---

This job produces the following table:

.. code-block:: text

    Results for H2O, basis=VTZ
   
    METHOD        E
    HF        -76.05480122
    CCSD(T)   -76.33149220
    CASSCF    -76.11006259
    MRCI      -76.31960943

.. _introductory_examples--procedures:

Procedures
==========

``You could simplify this job by defining a procedure SAVE_E as follows:``

.. code-block:: text
   :caption: examples/h2o_proce.inp

   ***,h2o                   !A title
   
   proc save_e               !define procedure save_e
   if(#i.eq.0) i=0           !initialize variable i if it does not exist
   i=i+1                     !increment i
   e(i)=energy               !save scf energy in variable e(i)
   method(i)=program         !save the present method in variable method(i)
   endproc                   !end of procedure
   
   
   r=1.85,theta=104          !set geometry parameters
   geometry={o;              !z-matrix geometry input
             h1,O,r;
             h2,O,r,H1,theta}
   basis=vtz                 !use VTZ basis
   hf                        !closed-shell scf
   save_e                    !call procedure, save results
   
   ccsd(t)                   !do ccsd(t) calculation
   save_e                    !call procedure, save results
   
   casscf                    !do casscf calculation
   save_e                    !call procedure, save results
   
   mrci                      !do mrci calculation
   save_e                    !call procedure, save results
   
   table,method,e            !print a table with results
   title,Results for H2O, basis=$basis  !title for the table

The job produces the same table as before.

For more details about procedures and further examples see `Procedures section of Program control <program_control.html#procedures-proc-endproc>`__.

.. _introductory_examples--do-loops:

Do loops
========

Now you have the idea that one geometry is not enough. Why not compute the whole surface? ``DO`` loops make it easy. Here is an example, which computes a whole potential energy surface for :math:`\rm H_2O`.

.. code-block:: text
   :caption: examples/h2o_pes_ccsdt.inp

   ***,H2O potential
   symmetry,x                           !use cs symmetry
   geometry={
            o;                          !z-matrix
            h1,o,r1(i);
            h2,o,r2(i),h1,theta(i) }
   basis=vdz                             !define basis set
   angles=[100,104,110]                  !list of angles
   distances=[1.6,1.7,1.8,1.9,2.0]       !list of distances
   i=0                                   !initialize a counter
   do ith=1,#angles                      !loop over all angles H1-O-H2
   do ir1=1,#distances                   !loop over distances for O-H1
   do ir2=1,ir1                          !loop over O-H2 distances(r1.ge.r2)
   i=i+1                                 !increment counter
   r1(i)=distances(ir1)                  !save r1 for this geometry
   r2(i)=distances(ir2)                  !save r2 for this geometry
   theta(i)=angles(ith)                  !save theta for this geometry
   hf;                                   !do SCF calculation
   escf(i)=energy                        !save scf energy for this geometry
   ccsd(t);                              !do CCSD(T) calculation
   eccsd(i)=energc                       !save CCSD energy
   eccsdt(i)=energy                      !save CCSD(T) energy
   enddo                                 !end of do loop ith
   enddo                                 !end of do loop ir1
   enddo                                 !end of do loop ir2
   {table,r1,r2,theta,escf,eccsd,eccsdt   !produce a table with results
   head, r1,r2,theta,scf,ccsd,ccsd(t)    !modify column headers for table
   save,h2o.tab                          !save the table in file h2o.tab
   title,Results for H2O, basis $basis   !title for table
   sort,3,1,2}                           !sort table

This produces the following table.

.. code-block:: text

    Results for H2O, basis VDZ
   
        R1    R2   THETA       SCF            CCSD           CCSD(T)
       1.6   1.6   100.0   -75.99757338   -76.20140563   -76.20403920
       1.7   1.6   100.0   -76.00908379   -76.21474489   -76.21747582
       1.7   1.7   100.0   -76.02060127   -76.22812261   -76.23095473
       ...
       2.0   1.9   110.0   -76.01128923   -76.22745359   -76.23081968
       2.0   2.0   110.0   -76.00369171   -76.22185092   -76.22537212

You can use also use ``DO`` loops to repeat your input for different methods.

.. code-block:: text
   :caption: examples/h2o_manymethods.inp

   ***,h2o benchmark
   $method=[hf,fci,ci,cepa(0),cepa(1),cepa(2),cepa(3),mp2,mp3,mp4,\
         qci,ccsd,bccd,qci(t),ccsd(t),bccd(t),casscf,mrci,acpf]
   basis=dz                                !Double zeta basis set
   geometry={o;h1,o,r;h2,o,r,h1,theta}     !Z-matrix for geometry
   r=1 ang, theta=104                      !Geometry parameters
   do i=1,#method                          !Loop over all requested methods
   $method(i);                             !call program
   e(i)=energy                             !save energy for this method
   enddo
   escf=e(1)                               !scf energy
   efci=e(2)                               !fci energy
   table,method,e,e-escf,e-efci            !print a table with results
   !Title for table:
   title,Results for H2O, basis $basis, R=$r Ang, Theta=$theta degree

This calculation produces the following table.

.. code-block:: text

    Results for H2O, basis DZ, R=1 Ang, Theta=104 degree
   
    METHOD        E             E-ESCF       E-EFCI
    HF        -75.99897339     .00000000    .13712077
    FCI       -76.13609416    -.13712077    .00000000
    CI        -76.12844693    -.12947355    .00764722
    CEPA(0)   -76.13490643    -.13593304    .00118773
    CEPA(1)   -76.13304720    -.13407381    .00304696
    CEPA(2)   -76.13431548    -.13534209    .00177868
    CEPA(3)   -76.13179688    -.13282349    .00429728
    MP2       -76.12767140    -.12869801    .00842276
    MP3       -76.12839400    -.12942062    .00770015
    MP4       -76.13487266    -.13589927    .00122149
    QCI       -76.13461684    -.13564345    .00147732
    CCSD      -76.13431854    -.13534515    .00177561
    BCCD      -76.13410586    -.13513247    .00198830
    QCI(T)    -76.13555640    -.13658301    .00053776
    CCSD(T)   -76.13546225    -.13648886    .00063191
    BCCD(T)   -76.13546100    -.13648762    .00063315
    CASSCF    -76.05876129    -.05978790    .07733286
    MRCI      -76.13311835    -.13414496    .00297580
    ACPF      -76.13463018    -.13565679    .00146398

One can do even more fancy things, like, for instance, using macros, stored as string variables, see `Macro definitions using string variables <variables.html#macro-definitions-using-string-variables>`__.
