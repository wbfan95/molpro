.. _chemical_shieldings_magnetizability_and_rotational_g-tensor--chemical-shieldings-magnetizability-and-rotational-g-tensor:

Chemical shieldings, magnetizability, and rotational g-tensor
=============================================================

Bibliography:
:math:`[1]` S. Loibl, F.R. Manby, M. Schütz, *Density fitted, local Hartree-Fock treatment of NMR chemical shifts using London atomic orbitals*, `Mol. Phys. <https://dx.doi.org/10.1080/00268970903580133>`__ **108**, 477 (2010).
:math:`[2]` S. Loibl and M. Schütz, *NMR shielding tensors for density fitted local second-order Møller-Plesset perturbation theory using gauge including atomic orbitals*, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.4744102>`__ **137**, 084107 (2012).
:math:`[3]` S. Loibl and M. Schütz, *Magnetizability and rotational g tensors for density fitted local second-order Møller-Plesset perturbation theory using gauge-including atomic orbitals*, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.4884959>`__ **141**, 024108 (2014).

All publications resulting from use of this program must acknowledge the above.

The command ``nmrshld`` invokes the calculation of NMR chemical shielding tensors at the level of (local) density-fitted HF (GIAO-DF-HF) or local density-fitted MP2 (GIAO-DF-LMP2). Note: Chemical shieldings at the level of MP2 are only implemented for DF-LMP2.
For the calculation of the chemical shielding tensor a preceding DF-HF, respectively, DF-LMP2 calculation is required. Symmetry has to be set to ``nosym``. For the GIAO-DF-HF code one can use canonical orbitals from the DF-HF run or localized orbitals (recommended).
Example:

.. code-block:: text

   ***,Chemical shielding tensors for water molecule
   symmetry,nosym
   GEOMETRY={    !geometry input
   h1;o,h1,r1;h2,o,r2,h1,theta}
   r1=0.9583 ang
   r2=0.9583 ang
   theta=104.2
   basis={       !specify basis
   default,cc-pVDZ
   set,mp2fit
   default,vdz/mp2fit
   set,jkfit
   default,vdz/jkfit
   }
   df-hf,df_basis=jkfit
   df-lmp2,df_basis=mp2fit
   nmrshld;comp      !invoke calculations of shieldings, print the components

The shielding calculation returns the chemical shielding tensors :math:`\sigma` and a summary of the chemical shifts (i.e. the arithmetic mean of the diagonal elements) for each nucleus in the order they were specified in the geometry input. The directive ``comp`` additionally prints the diamagnetic and paramagnetic contributions (for further information see R. Ditchfield, Mol. Phys. 27(4), 789 (1974)) for all shielding tensors.
Additionally, the calculation of magnetizabilities and rotational :math:`g` tensors has been implemented: the command ``magprop`` invokes the calculation of magnetizabilities and chemical shielding tensors. The directive ``comp`` can be specified. The command ``magnetiz`` invokes a pure magnetizability calculation. Note that a pure magnetizability calculation takes nearly as long as a chemical shielding calculation and hence does not provide any advantage in comparison to ``magprop``. See also the input examples `gly1_mag.inp <media/examples/gly1_mag.inp>`__ and `h2o_mag.inp <media/examples/h2o_mag.inp>`__.
If one is interested in the calculation of rotational :math:`g` tensors the molecule has to be aligned in the principal axis system with the command ``orient,mass``. Otherwise, the results are meaningless.
