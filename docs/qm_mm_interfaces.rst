.. _qm_mm_interfaces--qm-mm-interfaces:

QM/MM interfaces
================

The Molpro program package can be used in combination with other software to perform hybrid Quantum Mechanics/Molecular Mechanics (QM/MM) calculations. Through the use of point charges, electrostatic embedding can be used for both energy and gradient runs. In particular, lattices of point charges can be included in an external file, gradients with respect to charge positions can be computed, as described in section `lattice of point charges <molecular_geometry.html#lattice-of-point-charges>`__. Gradients with respect to QM nuclear positions can be computed (and include the effect of the MM charges) as usual using the FORCE command (section :doc:`energy gradients <energy_gradients>`).

Although Molpro itself does not offer any interface to force field programs, the coupling is supplied by other commercial and non-commercial software. The following is a list of QM/MM software which allow the use of Molpro .

.. _qm_mm_interfaces--chemshell:

Chemshell
=========

The Chemshell computational chemistry environment (https://chemshell.org) offers an interface to many well known force field software (CHARMM, GROMOS, GULP,...). The program supports several geometry optimization algorithms; a molecular dynamics driver for :math:`NVE`, :math:`NVT` and :math:`NPT` ensembles; Monte Carlo; and many other utilities.

The Chemshell Manual can be found at the following website:

https://chemshell.org/documentation/

Instructions on the use of Molpro are available therein. Also concerning the Chemshell environment, a free Graphical User Interface (GUI) has been released. The CCP1GUI facilitates the input for hybrid calculations, allows visualisation of molecular structures and includes molecule editing tools.
