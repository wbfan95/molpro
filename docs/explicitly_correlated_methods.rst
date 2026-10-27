.. raw:: html

   <span id="analytical-gradients-for-mp2-f12-and-ccsd-t-f12"></span>

.. raw:: html

   <span id="basis-sets"></span>

.. raw:: html

   <span id="cabs-singles-correction"></span>

.. raw:: html

   <span id="ccsd-t-f12"></span>

.. raw:: html

   <span id="choosing-the-ansatz-and-the-level-of-approximation"></span>

.. raw:: html

   <span id="df-lmp2-f12-and-df-lccsd-t-f12-calculations-with-local-approximations"></span>

.. raw:: html

   <span id="expectation-values-for-mp2-f12-and-ccsd-t-f12"></span>

.. raw:: html

   <span id="options"></span>

.. raw:: html

   <span id="variables-set-by-the-f12-programs"></span>

.. raw:: html

   <span id="wave-function-ans-tze"></span>

.. _explicitly_correlated_methods--explicitly-correlated-methods:

Explicitly correlated methods
=============================

Explicitly correlated calculations provide a dramatic improvement of the basis set convergence of MP2, CCSD, CASPT2, and MRCI correlation energies. Such calculations can be performed using the commands of the form

*command*, *options*

where *command* can be one of the following:

* **MP2-F12** Closed-shell canonical MP2-F12. By default, the fixed amplitude ansatz (``FIX``, see below) is used, but other ansätze are also possible. The F12-corrections is computed using density fitting, and then added to the MP2 correlation energy obtained without density fitting.
* **DF-MP2-F12** As MP2-F12, but the DF-MP2 correlation energy is used. This is less expensive than MP2-F12.
* **DF-LMP2-F12** Closed-shell DF-MP2-F12 with localized orbitals. Any method and ansatz as described in `J. Chem. Phys. <https://dx.doi.org/10.1063/1.2712434>`__ **126**, 164102 (2007) can be used (cf. sections `wave function Ansätze <explicitly_correlated_methods.html#wave-function-ans-tze>`__,\ `choosing the ansatz and the level of approximation <explicitly_correlated_methods.html#choosing-the-ansatz-and-the-level-of-approximation>`__).
* **DF-RMP2-F12** Spin-restricted open-shell DF-RMP2-F12 using ansatz 3C. Any method as described in `J. Chem. Phys. <https://dx.doi.org/10.1063/1.2889388>`__ **128**, 154103 (2008) can be used (cf. sections `wave function Ansätze <explicitly_correlated_methods.html#wave-function-ans-tze>`__,\ `choosing the ansatz and the level of approximation <explicitly_correlated_methods.html#choosing-the-ansatz-and-the-level-of-approximation>`__).
* **CCSD-F12** Closed-shell CCSD-F12 approximations as described in `J. Chem. Phys. <https://dx.doi.org/10.1063/1.2817618>`__ **127**, 221106 (2007). By default, the fixed amplitude ansatz is used and the CCSD-F12A and CCSD-F12B energies are computed. Optionally, the command can be appended by A or B, and then only the corresponding energy is computed. For more details see section `CCSD(T)-F12 <explicitly_correlated_methods.html#ccsd-t-f12>`__.
* **CCSD-F12c** Closed-shell CCSD(F12\*) approximation as proposed by Hättig, Tew and Köhn. In Molpro this is denoted f12c. As compared to CCSD-F12a/b it requires additional computational effort. Since in some parts the implementation is brute-force without paging algorithms, large memory may be required. In most cases there is no gain in accuracy as compared to f12b and therefore the use of this method is normally not recommended. Currently CCSD-F12c is not available for open-shell cases.
* **CCSD(T)-F12** Same as CCSD-F12, but perturbative triples are added.
* **CCSD(T)-F12c** Same as CCSD-F12c, but perturbative triples are added.
* **UCCSD-F12** Open-shell unrestricted UCCSD-F12 approximations as described by G. Knizia, T. B. Adler, and H.-J. Werner, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3054300>`__ **130**, 054104 (2009). Restricted open-shell Hartree-Fock (RHF) orbitals are used. Optionally, the command can be appended by A or B, and then only the corresponding energy is computed. For more details see section `CCSD(T)-F12 <explicitly_correlated_methods.html#ccsd-t-f12>`__.
* **UCCSD(T)-F12** Same as UCCSD-F12, but perturbative triples are added.
* **RCCSD(T)-F12** Similar to UCCSD(T)-F12, but the partially spin-adapted scheme is used.
* **DCSD-F12** Closed-shell CCSD-F12 approximations applied to DCSD method, see CCSD-F12 for more details.
* **UDCSD-F12** Open-shell unrestricted CCSD-F12 approximations applied to DCSD method, see UCCSD-F12 for more details.
* **RDCSD-F12** Open-shell partially spin-adapted CCSD-F12 approximations applied to DCSD method.
* **RS2-F12** CASPT2-F12 method as described in `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3489000>`__ **133**, 141103 (2010).
* **MRCI-F12** MRCI-F12 method as described in `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3528720>`__ **134**, 034113 (2011), `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3587632>`__ **134**, 184104 (2011), and `Mol. Phys. <https://dx.doi.org/10.1080/00268976.2013.779393>`__ **111**, 607 (2013).
* **PNO-LMP2-F12**, **PNO-LCCSD-F12**, and **PNO-LCCSD(T)-F12** (closed and open shell) are also available, please refer to the :doc:`corresponding sections. <local_correlation_methods_with_pair_natural_orbitals_pnos>`

**Published work arising from these methods should cite the following:**
F. R. Manby, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.1594713>`__ **119**, 4607 (2003)
(for the density fitting approximations in linear R12 methods)
A. J. May and F. R. Manby, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.1780891>`__ **121**, 4479 (2004)
(for the frozen geminal expansions)
H.-J. Werner and F. R. Manby, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.2150817>`__ **124**, 054114 (2006);
F. R. Manby, H.-J. Werner, T. B. Adler and A. J. May, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.2173247>`__ **124**, 094103 (2006);
H.-J. Werner, T. B. Adler, and F. R. Manby, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.2712434>`__ **126**, 164102 (2007)
(for all other closed-shell MP2-F12 methods).
G. Knizia and H.-J. Werner, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.2889388>`__ **128**, 154103 (2008)
(for all open-shell F12 calculations).
T. B. Adler, G. Knizia and H.-J. Werner, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.2817618>`__ **127**, 221106 (2007)
(for CCSD(T)-F12).
G. Knizia,T. B. Adler, and H.-J. Werner, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3054300>`__ **130**, 054104 (2009)
(for CCSD(T)-F12 and UCCSD(T)-F12 calculations).
T. B. Adler and H.-J. Werner, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3160675>`__ **130**, 241101 (2009)
(for LCCSD-F12).
K.A. Peterson, T. B. Adler, and H.-J. Werner, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.2831537>`__ **128**, 084102 (2008)
(for the VnZ-F12 basis sets)
K. E. Yousaf and K. A. Peterson, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3009271>`__ **129**, 184108 (2009)
(for the VnZ-F12/OPTRI basis sets)
K. E. Yousaf and K. A. Peterson, `Chem. Phys. Lett. <https://dx.doi.org/10.1016/j.cplett.2009.06.003>`__ **476**, 303 (2009)
(for the AVnZ/OPTRI basis sets)
H.-J. Werner, G. Knizia, and F. R. Manby (`Mol. Phys. <https://dx.doi.org/10.1080/00268976.2010.526641>`__ **109**, 407 (2011);
Kirk A. Peterson , C. Krause, H. Stoll, J. G. Hill, and H.-J. Werner, `Mol. Phys. <https://dx.doi.org/10.1080/00268976.2011.624129>`__ **109**, 2607 (2011)
(for calculations with multiple geminal exponents).
H.-J. Werner, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.2982419>`__ **129**, 101103 (2008);
T. B. Adler, F. R. Manby, and H.-J. Werner, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3040174>`__ **130**, 054106 (2009);
T. B. Adler and H.-J. Werner, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3160675>`__ **130**, 241101 (2009);
T. B. Adler and H.-H. Werner, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3647565>`__ **135**, 144117 (2011)
(for all local local F12 calculations)
T. Shiozaki and H.-J. Werner, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3489000>`__ **133**, 141103 (2010);
T. Shiozaki, G. Knizia, and H.-J. Werner, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3528720>`__ **134**, 034113 (2011);
T. Shiozaki and H.-J. Werner, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3587632>`__ **134**, 184104 (2011);
T. Shiozaki and H.-J. Werner, `Mol. Phys. <https://dx.doi.org/10.1080/00268976.2013.779393>`__ **111**, 607 (2013)
(for all explicitly correlated multireference calculations).
D. Kats, D. Kreplin, H.-J. Werner, F. R. Manby, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.4907591>`__ **142**, 064111 (2015)
(for DCSD-F12, RDCSD-F12, and UDCSD-F12 calculations).
D. Kats, `Mol. Phys. <https://dx.doi.org/10.1080/00268976.2017.1417646>`__ **116**, 1435 (2018) (for SCS-DCSD-F12).
W. Győrffy, G. Knizia, and H.-J. Werner, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.5003065>`__ **147**, 214101 (2017);
W. Győrffy and H.-J. Werner, J. Chem. Phys. **148**, 114104 (2018); https://doi.org/10.1063/1.5020436
(for all gradient and property calculations using F12 gradients).

In the following, we briefly summarize the ansätze and approximations that can be used in single-reference treatments. For more details and further references to related work of other authors see H.-J. Werner, T. B. Adler, and F. R. Manby, *General orbital invariant MP2-F12 theory*, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.2712434>`__ **126**, 164102 (2007) (in the following denoted **I**). More information about MRCI-F12 calculations are given in section `explicitly correlated MRCI-F12 <the_mrci_program.html#explicitly-correlated-mrci-f12>`__

For computing first-order properties and geometry optimization see section `analytical gradients for MP2-F12 and CCSD(T)-F12 <explicitly_correlated_methods.html#analytical-gradients-for-mp2-f12-and-ccsd-t-f12>`__.

For explicitly correlated local methods for large molecules see :doc:`Local correlation methods with pair natural orbitals (PNOs). <local_correlation_methods_with_pair_natural_orbitals_pnos>`

.. _explicitly_correlated_methods--reference-functions:

Reference functions
===================

The MP2-F12, CCSD-F12, and UCCSD-F12 methods must use conventional (non-density fitted) spin-restricted Hartree-Fock reference functions (HF or RHF). DF-HF cannot be used for these methods. This restriction is necessary to ensure that the Fock matrix is diagonal and consistent with the integrals used in these methods. For DF-MP2-F12, DF-LMP2-F12, and DF-RMP2-F12 either HF or DF-HF reference functions can be used.

Currently, only finite dipole fields can be applied, other perturbations are not yet supported. ECPs can be used, but this is still experimental and not extensively benchmarked. The Douglas-Kroll-Hess or eXact-2-Component Hamiltonians cannot currently be used in combination with F12 methods.

.. _explicitly_correlated_methods--wave-function-ans-tze:

Wave function Ansätze
=====================

The so called ”ansatz” determines the definition of the explicitly correlated wave function. This is to be distinguished from the various approximations that can be used to approximate the Hamiltonian matrix elements. Generally, we use ansatz **3** (cf. **I**), for which the projector has the form

.. math::

   \begin{aligned}
     \hat Q_{12} &=& (1-\hat o_1) (1 - \hat o_2) (1 - \hat v_1 \hat v_2),\nonumber\end{aligned}

where :math:`\hat o_i` is a one-electron projector for electron :math:`i` onto the occupied space, and :math:`\hat v_i` projects onto the virtual orbital space. In the case that domain approximations are used in local explicitly correlated wave functions, the operators :math:`\hat v` are replaced by operators :math:`\hat d^{ij}` that project just onto the domain for the orbital pair :math:`ij`.

In MOLPRO the following wave function ansätze can be used:

.. _explicitly_correlated_methods--the-general-ansatz:

The general ansatz
==================

The conventional external pair functions are augmented by terms of the form
\begin{align}

.. code-block:: text

    |u_{ijp}^{\rm F12}\rangle &=&  \sum_{p=\pm 1} \sum_{kl} T^{ijp}_{kl} \hat Q_{12} \hat F_{12} |kl\rangle \label{eq:uij}\end{align}

This ansatz is orbital invariant (i.e., the same results are obtained with canonical or localized orbitals), but it often suffers from geminal basis set superposition errors. Furthermore, singularities may occur in the zeroth-order Hamiltonian, in particular for larger systems. Therefore, this ansatz is normally not recommended.

.. _explicitly_correlated_methods--the-diagonal-ansatz-d:

The diagonal ansatz (D)
=======================

The sum over :math:`kl` in equation \eqref{eq:uij} is restricted to :math:`ij`. This ansatz is not orbital invariant and size consistent only when localized orbitals are used. However, geminal basis set superposition errors are absent and therefore the results are often more accurate than with the general ansatz.

.. _explicitly_correlated_methods--the-fixed-amplitude-ansatz-fix:

The fixed amplitude ansatz (FIX)
================================

The diagonal ansatz is used and the amplitudes of the explicitly correlated configurations are determined by the wavefunction cusp conditions, i.e.

.. math::

   \begin{aligned}
    T^{ij,1}_{ij} &=& \frac{1}{2} \nonumber\\
    T^{ij,-1}_{ij} &=& \frac{1}{4}\nonumber\end{aligned}

This ansatz is orbital invariant, size consistent and free of GBSSE.

.. _explicitly_correlated_methods--ri-approximations:

RI Approximations
-----------------

Various approximations such as A, B, C, HY1, HY2 exist for the matrix elements of the first-order Hamiltonian (see **I**). They differ in the way the RI approximations are made. In the limit of a complete RI basis, approximations B and C are identical and yield the exact result for a given wave function ansatz. We generally recommend approximation C, which is simpler and more efficient than approximation B. Normally, the union of the AO and RI basis sets is used to approximate the resolution of the identity (CABS approach). In the hybrid approximations (HY1, HY2, HX) only the AO basis is used in some less important terms. Together with the recommended approximation C, HY1 or HY2 can be used; HY2 is more accurate, HY1 more efficient. In most cases, approximation 3C(HY1) provides an excellent compromise between accuracy and efficiency. In approximation A, all terms involving exchange operators are neglected. This approximation is used along with local approximations in our low-order scaling LMP2-F12/3\*A(loc) method that can be applied to large molecules (cf. section `DF-LMP2-F12 and DF-LCCSD(T)-F12 calculations with local approximations <explicitly_correlated_methods.html#df-lmp2-f12-and-df-lccsd-t-f12-calculations-with-local-approximations>`__)

If the extended Brillouin condition (EBC, see **I**) is assumed, the explicitly correlated and conventional amplitude equations decouple and can be solved independently. These approximations are denoted by a star, e.g. **3**\*C.

.. _explicitly_correlated_methods--basis-sets:

Basis sets
----------

In MOLPRO the F12 integrals can only be computed using density fitting (DF) approximations. The many electron integrals are approximated by resolutions of the identity (RI) expansions. Thus, F12 calculations require three different basis sets: the orbital (AO) basis, the DF basis, and the RI basis.

We recommend as AO basis sets the augmented correlation consistent basis sets (denoted AVnZ) or the specially optimized correlation consistent F12 basis sets (denoted VnZ-F12, cf. K.A. Peterson and H.-J. Werner, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.2831537>`__ **128**, 084102 (2008)). Normally, triples zeta basis sets (AVTZ or VTZ-F12) yield excellent results that are close to the basis set limit. Diffuse basis functions are rather essential both for the HF and MP2-F12 energies, and therefore the standard VTZ sets are not recommended. If the AVnZ, [A]VnZ-F12, or VnZ-PP-F12 orbital basis sets are used, suitable density fitting (DF) basis and resolution of the identity (RI) basis sets are automatically chosen. For the AVnZ orbital basis sets, AVnZ/MP2FIT and VnZ/JKFIT basis sets are used by default for the DF and RI, respectively. The associated optimized CABS basis set of Peterson et al. can be chosen by specifying ``RI_BASIS=OPTRI``. For the [a]VnZ-F12 and [a][c]VnZ-PP-F12 orbital basis, the associated CABS (OPTRI) basis sets are used by default. However, OPTRI sets are not yet available for all elements, and in such cases an alternative RI basis must be explicitly specified using the ``RI_BASIS`` option.

Other basis sets can be chosen using the ``DF_BASIS``, ``DF_BASIS_EXCH`` and ``RI_BASIS`` options (cf. section `options <explicitly_correlated_methods.html#options>`__). See section :doc:`density fitting <density_fitting>` for more details about density fitting.

This is an example for using multiple basis sets for density fitting and resolution of the identity

.. code-block:: text
   :caption: examples/h2o_basissets1.inp

   ***,h2o
   geom={o;
         h1,o,r;
         h2,o,r,h1,theta}
   r=0.97 ang
   theta=104
   
   basis={
   default,avtz
   set,df
   default,avtz/mp2fit   !density fitting basis
   set,jk
   default,avtz/jkfit    !density fitting basis for Fock and exchange matrices
   set,ri
   default,avtz/optri    !ri cabs basis
   }
   hf
   ccsd(t)-f12,df_basis=df,df_basis_exch=jk,ri_basis=ri

The following two examples yield identical results:

.. code-block:: text
   :caption: examples/h2o_basissets2.inp

   ***,h2o
   geom={o;
         h1,o,r;
         h2,o,r,h1,theta}
   r=0.97 ang
   theta=104
   
   basis={
   default,avtz
   set,df,context=mp2fit
   default,avtz          !density fitting basis
   set,jk,context=jkfit
   default,avtz          !density fitting basis for Fock and exchange matrices
   set,ri,context=optri
   default,avtz          !ri cabs basis
   }
   hf
   ccsd(t)-f12,df_basis=df,df_basis_exch=jk,ri_basis=ri

.. code-block:: text
   :caption: examples/h2o_basissets3.inp

   ***,h2o
   geom={o;
         h1,o,r;
         h2,o,r,h1,theta}
   r=0.97 ang
   theta=104
   
   basis=avtz
   hf
   ccsd(t)-f12,df_basis=avtz/mp2fit,df_basis_exch=avtz/jkfit,ri_basis=avtz/optri

In the latter example the specifications MP2FIT and JKFIT could be omitted, i.e. the input

``ccsd(t)-f12,df_basis=avtz,df_basis_exch=vtz,ri_basis=optri``

would be equivalent. In fact, since default density fitting basis sets are used

``ccsd(t)-f12,ri_basis=optri``

would be sufficient. Note, however, that without the specification OPTRI the avtz/jkfit basis set would be used for the RI. For example,

.. code-block:: text

   basis=avtz
   hf
   ccsd(t)-f12

is equivalent to

.. code-block:: text

   basis=avtz
   hf
   ccsd(t)-f12,df_basis=avtz/mp2fit,df_basis_exch=vtz/jkfit,ri_basis=vtz/jkfit

If the VnZ-F12 basis sets are used, the OPTRI sets are used by default, i.e.,

.. code-block:: text

   basis=vtz-f12
   hf
   ccsd(t)-f12

is equivalent to

.. code-block:: text

   basis=vtz-f12
   hf
   ccsd(t)-f12,df_basis=avtz/mp2fit,df_basis_exch=vtz/jkfit,\\
   ri_basis=vtz-f12/optri

.. _explicitly_correlated_methods--symmetry:

Symmetry
--------

Symmetry cannot be used in DF-LMP2-F12 calculations. However, in MP2-F12, DF-MP2-F12, DF-RMP2-F12, CCSD(T)-F12 and UCCSD(T)-F12 calculations Abelian symmetry can be used as usual; in these cases the preceding DF-MP2-F12 calculations will be automatically performed without symmetry, and the integrals that are necessary for subsequent CCSD-F12 or UCCSD-F12 calculations will be transformed to the symmetry adapted basis. This is fully automatic and transparent to the user. Note, however, that the prefix DF- turns off symmetry automatically, and if you want to use symmetry in the HF calculations preceding the DF-MP2-F12 or DF-MP2-F12 calculations the symmetry elements (or ``AUTO``) must be specified using the ``SYMMETRY`` directive (setting ``SYMMETRY,AUTO`` works fine).

.. _explicitly_correlated_methods--options:

Options
-------

There are many options available, but these are hardly needed. Normally, when standard orbital basis sets such as aug-cc-PVTZ or VTZ-F12 are used, appropriate defaults are used and no further options are needed. A typical input simply reads

.. code-block:: text

   basis=vtz-f12
   hf
   ccsd(t)-f12

We recommend to specify options only when necessary and when it is well understood what they mean!

Options for canonical and local versions:

* ``DF_BASIS=basis`` Select the basis for density fitting (see section :doc:`density fitting <density_fitting>` for details). *basis* can either refer to a set name defined in the basis block, or to a default MP2 fitting basis (e.g., ``DF_BASIS=VTZ`` generates the ``VTZ/MP2FIT`` basis). By default, the MP2FIT basis that corresponds to the orbital basis is used.
* ``DF_BASIS_EXCH=basis`` Select the density fitting basis for computing the exchange and Fock operators. By default, the JKFIT basis sets which correspond to the orbital basis are used.
* ``RI_BASIS=basis`` Select the basis for the resolution of the identity (RI). This can refer to a default basis set or a set name defined in a basis block. For F12 methods the Hartree-Fock JKFIT basis sets perform well for the RI, despite having been optimized for other purposes. These sets are used by default for the AVnZ orbital basis sets. The basis type can be appended to the basis name after a slash, e.g.

``RI_BASIS=AVQZ/JKFIT`` would use the specified JKFIT set, or ``RI_BASIS=AVQZ/OPTRI`` would use the optimized CABS basis sets of Peterson et al. These are recommended for the AVnZ and VnZ-F12 basis sets and used by default for the latter ones. Note that each OPTRI basis is associated to a specific orbital basis. Therefore, the name of the OPTRI basis must either be the same as that of the orbital basis, or be omitted, e.g., ``RI_BASIS=OPTRI`` selects automatically the correct set for the current orbital basis. In case of R12-methods (which are not recommended to be used), the RI basis should be chosen to be a large uncontracted AO basis (at least AVQZ). Contraction/uncontraction can be forced appending ``(CONTRACT)`` or ``(UNCONTRACT)`` to the basis name, e.g.,
``RI_BASIS=AVQZ(UNCONTRACT)/ORBITAL``. If other options are given in parenthesis, these can be separated by commas, e.g.,
``RI_BASIS=AVQZ(f/d,UNCONTRACT)/ORBITAL.\\``
Alternative forms, which should work as well, are
``RI_BASIS=AVQZ(f/d)(UNCONTRACT)/ORBITAL\\``
or
``RI_BASIS=AVQZ(f/d)/ORBITAL(UNCONTRACT).\\``
Note that the CONTRACT/UNCONTRACT option cannot be used with basis set names previously defined in a basis block.

* ``CONTEXT=context`` Can be used to change the default type for the RI basis, e.g. ``CONTEXT=OPTRI`` will use the OPTRI basis sets that correspond to the VnZ-F12 or AVnZ basis sets.
* ``ANSATZ=ansatz`` Select the explicitly correlated ansatz *ansatz* methods. See section `choosing the ansatz and the level of approximation <explicitly_correlated_methods.html#choosing-the-ansatz-and-the-level-of-approximation>`__ for the possibilities and further details.
* ``GEM_BASIS`` Basis set name for geminal expansion; atom labels are ignored. This can either be ``OPTFULL`` (full nonlinear fit of the geminal expansion), ``EVEN`` (even tempered fit), or refer to a set name defined in a previous ``BASIS`` block. Default is ``OPTFULL``.
* ``GEM_TYPE`` Frozen geminal type: ``LINEAR`` or ``SLATER``, default is ``SLATER``.
* ``GEM_NUMBER`` Number of Gaussian geminal functions (default 6).
* ``GEM_CENTRE`` Centre of even tempered geminal exponents, if ``GEM_BASIS=EVEN`` (default 1.0).
* ``GEM_RATIO`` Ratio of even tempered geminal exponents, if ``GEM_BASIS=EVEN`` (default 3.0).
* ``GEM_BETA`` Exponent for Slater-type frozen geminal, or parameter for weight function in other frozen geminal models (default 1.0 :math:`a_0^{-1}`). It is possible to specify extra exponents for core-core and core-valence correlation. If two values are given (in square brackets), the first is used for valence pairs, the second for core-core (cc) and core-valence (cv) pairs. If three values are given, the first is used for vv, the second for cv, and the third for cc correlation.
* ``GEM_OMEGA`` Exponent for weighting function (default -1, which means a value derived from ``GEM_BETA``).
* ``GEM_MOM`` Exponent for r in omega fitting (default 0).
* ``GEM_M`` Exponent for r in weighting function (default 0).
* ``GEM_MAXIT`` Max. number of iterations in geminal optimization (default 200).
* ``GEM_PRINT`` Print parameter for geminal optimization (default 0).
* ``GEM_DEBUG`` Debug option for geminal optimization (default 0).
* ``GEM_ACC`` Convergence threshold for geminal line search (default 0.001).
* ``GEM_FAC`` Scaling factor for exponents in geminal optimization (default 1.0).
* ``GEM_METHOD`` Geminal optimization method (augmented Hessian (``AH``) or Newton-Raphson (``NR``), default ``AH``).
* ``GEM_TRUST`` Trust ratio in AH geminal optimization (default 0.4).
* ``GEM_SHIFT`` Hessian shift in AH geminal optimization (default 0).
* ``GEM_NUMERICAL`` Flags numerical integration in geminal optimization (default 0).
* ``GEM_PLOT`` Geminal plot file (default blank).
* ``GEM_OPT_FULL`` If nonzero (default), fit each geminal independently to Gaussians (if several exponents are used). If zero, the first exponent is fitted, unless ``GEM_BETA_OPT`` is specified.
* ``GEM_BETA_OPT`` Exponent used to fit the Gaussian expansion.
* ``SIM_MULTGEM`` Only for calculation with multiple exponents: if nonzero, loop externally over integral program for different exponents. This is implied automatically if each geminal is fitted independently. If the same Gaussian exponents are used for each Slater exponent, ``SIM_MULTGEM=0`` can be used (default). In this case the integral program handles the general contractions (slightly faster).
* **``PRINT``\ =\ *ipri*** Select output level:

  * **ipri=0** Standard output
  * **ipri=1** Standard output plus more detailed information about integral evaluations.
  * **ipri=2** Debugging output
* ``THRBINV`` Threshold below which non-physical eigenvalues are projected from approximate B matrices
* ``THRAOF12`` Threshold for integral screening contribution.

.. _explicitly_correlated_methods--choosing-the-ansatz-and-the-level-of-approximation:

Choosing the ansatz and the level of approximation
--------------------------------------------------

The Ansatz can be chosen using the ``ANSATZ`` option and/or by options on the command line.

* ``3A`` Ansatz 3A;
* ``3*A`` Ansatz 3A with EBC approximation
* ``3B`` Ansatz 3B
* ``3*B`` Ansatz 3B with EBC approximation
* ``3C`` Ansatz 3C
* ``3*C`` Ansatz 3C with EBC approximation

The ansatz can be further detailed by appending options in parenthesis, e.g.

``ANSATZ=3B(D)``

These options can be one of

* ``D`` Use diagonal ansatz
* ``FIX`` Use diagonal ansatz with fixed amplitudes (orbital invariant)
* ``FIXC`` Use diagonal ansatz with fixed amplitudes and canonical orbitals
* ``DX`` Use diagonal ansatz and assume X-matrix to be diagonal (only for Ansatz 3A)
* ``GBC`` Use GBC approximation (only for 3B, default in 3A)
* ``EBC`` Use EBC approximation (same as \*)
* ``HX1`` Use HX1 approximation (only for 3B).
* ``HY1`` Use HY1 approximation (only for 3B and 3C).
* ``HY2`` Use HY2 approximation (only for 3B and 3C).
* ``HY`` Default hybrid approximation. HX1 and HY2 approximation in 3B, HY2 in 3C.
* ``NOZ`` Neglect Z terms (only for 3B and 3C).
* ``NOX`` Neglect X terms (only for 3A and 3B).

Several options separated by commas can be given. For instance

``ANSATZ=3C(FIX,HY1)``

uses the diagonal ansatz 3C(D) with fixed coefficients and the hybrid (HY1) approximation.

Alternatively or in addition, the following options can be given on the command line:

* ``DIAG=1`` Use diagonal ansatz.
* ``DIAGX=1`` Use diagonal ansatz and assume X-matrix to be diagonal.
* ``GBC=1`` Use GBC approximation (only for 3B, default in 3A).
* ``EBC=1`` Use EBC approximation (same as \*).
* ``HYBRID=n`` Use HYn approximation.
* ``HYBRIDX=1`` Use HX1 approximation.
* ``NOZ=1`` Neglect Z terms (only 3B and 3C).
* ``NOX=1`` Neglect X terms (only 3A and 3B).
* ``FIX=1`` Use diagonal ansatz with fixed coefficient approximation (orbital invariant).
* ``FIX=2`` Use diagonal ansatz with fixed coefficient approximation. Evaluate only first order energy expression, not the Hylleraas functional. Very fast but less accurate and reliable!
* ``FIXCAN=1`` Use diagonal ansatz with fixed coefficient approximation and canonical orbitals. A non-iterative method is used to evaluate the energy. This is equivalent to ``FIX=1,CANONICAL=1`` and is most efficient.
* ``FIXCAN=-1`` As ``FIXCAN=1``, but equations are solved iteratively (test purpose only).
* ``CABS=1`` Use CABS (default). If ``CABS=0`` is given, CABS is disabled. However, if ``RI_BASIS=OPTRI``, the orbital and OPTRI basis sets are automatically merged, and then exactly the same results as with ``CABS=1`` are obtained.
* ``ORTHO_CABS=1`` Construct CABS basis from orthogonal MOs and ABS basis rather than AO and RI basis.
* **``THRABS=``\ *thrabs*** Threshold for smallest eigenvalue of S in auxiliary ABS (only used with ``ORTHO_CABS=1``; default=\ ``THRCABS``).
* **``THRCABS=``\ *thrcabs*** Threshold for smallest eigenvalue of S in CABS (default 1.d-8).
* **``THRCABS_REL=``\ *thrcabs_rel*** Relative CABS threshold (default 1.d-9). The actual threshold is ``max(thrcabs,eigmax*thrcabs_rel``, where ``eigmax`` is the largest eigenvalue of the overlap matrix.
* **``PRINT=``\ *level*** Print parameter. ``PRINT=1`` give information about all computed integrals and the iterations.
* **``DEBUG=``\ *level*** Can be used to obtain extended debug print.
* ``SOLVE=0`` Use a most efficient pair-specific fully iterative method (default).
* ``SOLVE=1`` Use simple fully iterative method.
* ``SOLVE=2`` Use pair specific iterative method (more expensive).
* ``SOLVE=3`` Use pair specific non iterative method (most expensive, only with canonical orbitals).
* ``CANONICAL=1`` Use canonical orbitals and full domains.
* ``DOMSEL=1`` Use full domains and localized orbitals (unless ``CANONICAL=1`` is given).
* ``SCALE_TRIP=1`` Scale triples energy as explained in section `CCSD(T)-F12 <explicitly_correlated_methods.html#ccsd-t-f12>`__.
* ``CABS_SINGLES`` If set to one, include CABS singles correction (default=1)
* ``CORE_SINGLES`` If set to one, include CABS singles correction for core orbitals (default=0)
* ``EXTGEN`` For open-shell systems: If 1 (default,recommended), include all occupied valence orbital pairs for :math:`mn` in :math:`T^{ij}_{mn}`, independent of spin (as described in `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3054300>`__ **130**, 054104 (2009), section II.E). If 0, use only pairs mn where the spins of :math:`i` and :math:`m`, and :math:`j` and :math:`n` are equal.

For instance

``ANSATZ=3C,fix=1,hybrid=1,canonical=1``

implies a canonical 3C calculation with diagonal ansatz 3C, using fixed coefficient and hybrid approximations. The combination of the options ``fix=1`` and ``canonical=1`` implies a non-iterative calculation of the energy and is recommended. The above is equivalent to all of the following:

``ANSATZ=3C(FIXC,HY1)\\``
``ANSATZ=3C(D,FIXC,HY1)\\``
``ANSATZ=3C(D,HY1,FIX),canonical=1``

Note that the HF convergence threshold should be rather strict to obtain accurate results (use ``ACCU,14`` in the HF).

Numerous further options are for specialist use only and not described here. See ``explicit.registry`` for a full list.

.. _explicitly_correlated_methods--cabs-singles-correction:

CABS Singles correction
-----------------------

By default, the perturbative CABS singles correction as described in `J. Chem. Phys. <https://dx.doi.org/10.1063/1.2817618>`__ **127**, 221106 (2007) and `J. Chem. Phys. <https://dx.doi.org/10.1063/1.2889388>`__ **128**, 154103 (2008) is included in the reference energy of all MP2-F12, CCSD-F12, and CCSD(T)-F12 calculations (closed and open-shell). Since Molpro 2025.3 this is also the case in the PNO-F12 programs. An exception is LMP2-F12/3\*A(loc), which is done with a different program. In this cases the F12 correction can be computed beforehand and is then added automatically (see section :doc:`Local correlation methods with pair natural orbitals (PNOs). <local_correlation_methods_with_pair_natural_orbitals_pnos>`) The corrected reference energy is stored in variable ``ENERGR``, so that ``ENERGY-ENERGR`` are the total correlation energies. For the setting of other variables by the F12 programs see section `variables set by the F12 programs <explicitly_correlated_methods.html#variables-set-by-the-f12-programs>`__.

The singles correction can be turned off by option ``CABS_SINGLES=0``, e.g.

``MP2-F12,CABS_SINGLES=0``

One can use the MP2-F12 or RMP2-F12 program to only compute the cabs singles correction using
``CABS_SINGLES=-1``. In this case the program exits after computing the correction. This can be useful for using the singles correction in subsequent local correlation calculations. It is stored in variable ``EF12_RHFRELAX``. This can also be done by the commands ``CABS`` or ``DF-CABS``.

.. code-block:: text

The contribution of core orbitals to the singles energy is not included by default, but can be turned on by option ``CORE_SINGLES``, e.g.

``MP2-F12,CORE_SINGLES=1``

However, we do not recommended the use of core singles, because they depend sensitively on the CABS basis construction and do not offer significant improvements in relative energies.

The cabs-singles correction can also be computed using the command

``DF-CABS``

This is equivalent to ``DF-MP2-F12,CABS_SINGLES=-1``, which means that only the CABS correction is computed.

By default, a two-step orthonormalization procedure is used to compute the CABS basis. A simplified 1-step version can be chosen using option  ``ORTHO-CABS=0`` (this is the default in the PNO-F12 program). The effect on relative energies is usually negligible.

.. _explicitly_correlated_methods--pair-specific-geminal-exponents:

Pair specific geminal exponents
-------------------------------

Different Slater exponents can be used for core-core, core-valence and valence-valence pairs as described in H.-J. Werner, G. Knizia, and F. R. Manby, `Mol. Phys. <https://doi.org/10.1080/00268976.2010.526641>`__ **109**, 407 (2011). The exponents are specified using the ``GEM_BETA`` option, e.g., ``GEM_BETA=[1.0, 1.7, 2.5]`` (see options, section `options <explicitly_correlated_methods.html#options>`__). The three values are used for vv, cv, cc pairs, respectively. In most cases, core pairs can be defined by using the ``CORE`` directive: all orbitals that are not core and do not belong to the default valence shell are then treated as core. If part of the default valence shell is to be taken as core (e.g., the 3d shell in first-row transition metals), the core can be defined via the ``PRCORE`` variable, e.g., ``prcore=[4,2,2,1,4,2,2,1]`` for Cu\ :math:`_2`. This variable must then be defined before the F12 calculation that should use it. The following example shows calculation for Br\ :math:`_2`, in which the :math:`3d` shell is treated as core.

.. code-block:: text
   :caption: examples/br2_f12_multgem.inp

   gthresh,energy=1.d-8
   geometry={br;br,br,rmin}
   
   rmin=2.281 ANG
   
   basis={
   ecp,Br,ecp10mdf
   sp,Br,aug-cc-pVTZ-PP;c;
   d,Br,338.996,103.217,42.3638,18.4356,8.37254,3.80222,1.68677,0.677520
   c,1.8,0.001524,0.015673,0.072400,0.186303,0.323881,0.374534,0.257418,0.068051
   d,Br,2.9173,0.6300,0.2228
   f,Br,1.4417
   
   set,dfmp
   s,Br,40.9778,22.0940,14.1569,6.30933,3.49893,2.07145,1.22411,0.706125,0.421245,0.235424,0.133413
   p,Br,31.5779,17.7012,10.3673,5.56829,3.34725,1.86205,1.12814,0.520803,0.290648,0.155863
   d,Br,35.4419,14.4095,7.13728,4.02429,2.19901,1.18121,0.537101,0.320289,0.151982
   f,Br,16.6283,7.92639,3.69263,1.89967,1.02171,0.418748
   g,Br,58.3022,21.9356,7.85160,5.60937,2.04334,1.37529
   h,Br,7.51453,3.15089
   
   set,ri
   s,Br,18.7563,9.07737,4.87021,2.00555,0.900841,0.080149
   p,Br,26.0294,17.4402,5.55778,3.70554,2.47230,1.18351,0.511543,0.177391
   d,Br,15.9542,11.4584,8.89027,1.44361,0.945611,0.334128
   f,Br,42.4889,15.5186,10.3279,6.36172,2.80704,0.961178,0.415934
   g,Br,24.3260,9.29525,3.78033,1.65385,0.919948
   h,Br,18.4810,7.54637,2.84990,0.966374
   i,Br,11.4466
   }
   
   explicit,ri_basis=ri,df_basis=dfmp,df_basis_exch=def2-qzvpp/jkfit
   
   hf;accu,16
   i=1
   {mp2-f12,gem_beta=[1.25];core,2,1,1,,2,1,1}
   emp2f12(i)=energy-energr
   ef12_vv(i)=energ_vv
   ef12_cv(i)=energ_cv
   ef12_cc(i)=energ_cc
   $beta(i)='[1.25]'
   i=i+1
   {mp2-f12,gem_beta=[0.8,1.7];core,2,1,1,,2,1,1}
   emp2f12(i)=energy-energr
   ef12_vv(i)=energ_vv
   ef12_cv(i)=energ_cv
   ef12_cc(i)=energ_cc
   $beta(i)='[0.8,1.7]'
   
   i=i+1
   {mp2-f12,gem_beta=[0.8,1.7,2.2];core,2,1,1,,2,1,1}
   emp2f12(i)=energy-energr
   ef12_vv(i)=energ_vv
   ef12_cv(i)=energ_cv
   ef12_cc(i)=energ_cc
   $beta(i)='[0.8,1.7,2.2]'
   
   table,beta,ef12_cc,ef12_cv,ef12_vv,emp2f12
   Title,Results for Br2, basis vdz-f12

.. _explicitly_correlated_methods--ccsd-t-f12:

CCSD(T)-F12
-----------

The CCSD-F12 and UCCSD-F12 programs first do DF-MP2-F12/3C(FIX) (closed-shell) or DF-RMP2-F12/3C(FIX) (open-shell) calculations, and then perform the CCSD-F12 (UCCSD-F12) without density fitting. By default, the CCSD-F12A and CCSD-F12B energies are both computed. A specific method can be requested by appending A or B to the -F12 suffix. Furthermore, instead of the 3C(FIX) ansatz, different ansätze (e.g. 3C) can be used. In this case the amplitudes of the explicitly correlated terms are determined in the MP2-F12 calculation and kept fixed in the CCSD-F12.

It should be noted that these methods involve approximations and do not yield the exact CCSD-F12 energies. Preliminary experience has shown that the CCSD-F12A method slightly overestimates the correlation energies, while CCSD-F12B underestimates them. For AVDZ or AVTZ basis sets, CCSD-F12A usually gives very good results, but for larger basis sets it may overestimate the basis set limit and converge from below to the limit. Thus, convergence may not be monotonic, and extrapolation of the correlation energies should not be attempted. CCSD-F12B usually converges monotonically from below to the limit and gives best results for AVQZ and larger basis sets. Thus, we currently recommend CCSD-F12A for AVDZ and AVTZ basis sets, and CCSD-F12B for larger basis sets (rarely needed).

The perturbative triples correction can be invoked by using CCSD(T)-F12 or UCCSD(T)-F12. There is no direct F12 correction to the triples, and therefore the basis set error of the triples is not affected by the F12 (small changes of the triples energy arise from the fact that the doubles amplitudes are affected by the F12 terms). In many cases, a simple and pragmatic improvement of the triples energy can be obtained by scaling the triples energy contribution as

.. math::

   \begin{aligned}
   \Delta E_{(T*)} &=& \Delta E_{(T)}*E_{corr}^{MP2-F12}/E_{corr}^{MP2} \nonumber\end{aligned}

This can be done automatically by setting option ``SCALE_TRIP=1``, i.e.

``CCSD(T)-F12,SCALE_TRIP=1``

.. _explicitly_correlated_methods--perturbative-f12-correction:

Perturbative F12 correction
---------------------------

F12 can be used together with the Brueckner and orbital-optimized CCD and DCD methods as described in D. Kats and D. P. Tew, JCTC **15**, 13 (2019).

For this, first a standard Brueckner or orbital optimized CCD or DCD calculation is performed, and the orbitals and amplitudes are stored. After converting the orbital record to the normal HF-type record by using ``hf,maxit=0``, the orbitals and the amplitudes are read in by the corresponding CCSD-F12 or DCSD-F12 method with an option ``pertcalc`` set to 1 (use contravariant amplitudes instead of the Lagrange multipliers) or 2 (use true Lagrange multipliers – possible only for orbital-optimized methods and recommended). The final energy is printed together with a relaxation correction, which yields results closer to the fully relaxed F12 treatment, and the uncorrected value is printed in the next line.

It is advisable to set the ``SHIFTS`` and ``SHIFTP`` options to zero (and use the imaginary level shift ``SHIFTSI`` and ``SHIFTPI`` if needed). The option ``nofai_singles``\ =0 can be set to use the full Fock matrix in the CABS singles correction and the singles residual, which takes the final energy closer to the CCSD/DCSD CBS results. If the iterative MP2 struggles to converge, one can set ``shiftimp2`` to a very large number (e.g., 1000).

Example:

.. code-block:: text

   memory,32,m
   geometry={o;h1,o,r;h2,o,r,h1,theta}
   r=        0.96487698 ang
   theta=  102.18130898 degree
   
   basis= vdz
   
   hf
   {odcd
   brueckner,saveorb=3100.2
   save,6000.2
   }
   {hf,maxit=0
   start,3100.2
   orbital,3200.2
   }
   {dcsd-f12b,shiftimp2=1000.d0,pertcalc=2,SHIFTS=0,SHIFTP=0
   start,6000.2
   orbital,3200.2
   }

.. _explicitly_correlated_methods--df-lmp2-f12-and-df-lccsd-t-f12-calculations-with-local-approximations:

DF-LMP2-F12 and DF-LCCSD(T)-F12 calculations with local approximations
----------------------------------------------------------------------

Local variants of the DF-MP2-F12 and CCSD(T)-F12 methods are invoked by the commands ``DF-LMP2-F12``, ``DF-LCCSD-F12``, ``DF-LCCSD(T)-F12`` with ansatz 3\*A(LOC) [for DF-LCCSD-F12 fixed amplitudes are used, i.e., the default is 3\*A(LOC,FIX)]. **Note: The methods and options described in this section refer the older PAO-based local methods. Explicitly correlated variants of the more recent and more accurate PNO methods are also available and described in section :doc:`local correlation methods with pair natural orbitals (PNOs) <local_correlation_methods_with_pair_natural_orbitals_pnos>`.**

The DF-LMP2-F12 calculations are performed with a different program than non-local calculations. The (LOC) option implies that the LMP2 calculation with domain approximations is performed, and by default a local projector as first described in H.-J. Werner, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.2982419>`__ **129**, 101103 (2008) is used [see also T. B. Adler, F. R. Manby, and H.-J. Werner, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3040174>`__ **130**, 054106 (2009); T. B. Adler and H.-J. Werner, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3160675>`__ **130**, 241101 (2009); T. B. Adler and H.-H. Werner, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3647565>`__ **135**, 144117 (2011)]
This yields very similar results as the corresponding canonical methods at much lower cost ((ANSATZ=3\*A(LOC,FIX) is exactly equivalent to ANSATZ=3\*A(FIX,NOX),PROJF=2,CABS=0,CABS_SINGLES=0, but if the latter options are used the non-local program is used to compute the F12 correction and local approximations are only simulated. CABS singles can then be included by omitting the CABS_SINGLES=0 option.
)) and the method can be applied to quite large molecules.

Special options for these local variants are (local RI works only with ansatz 3\*A):

* ``PAIRS`` Specifies which pairs to be treated by R12 or F12

(``STRONG|CLOSE|WEAK|ALL``; pairs up to the given level are included). The default is ``ALL``. Note that even with ``ALL`` very distant pairs are neglected if these are neglected in the LMP2 as well.

* ``USEVRT`` If zero, the :math:`1-pp+po+op-p'o-op'` form of the projector is used, and local RI approximations apply to :math:`p` and :math:`p'`. If set to 1, the :math:`1+oo-vv-p'o-op'` form of the projector is used; any local RI approximation then applies only to the RI contribution :math:`p'`.
* ``USEPAO`` If ``USEPAO=1`` use pair-specific local projectors instead of :math:`vv`. This is the default if either the ansatz contains ’(LOC)’ or if domain approximations are made in the LMP2 (i.e., ``DOMSEL<1`` is explicitly specified). Otherwise the default is ``USEPAO=0``. ``USEPAO=1`` automatically implies ``USEVRT=1``, i.e. local RI approximations only affect the RI contributions :math:`p'`. Furthermore, if ``USEPAO=1`` is specified and ``DOMSEL`` is not given, default domains are assumed in the LMP2. If ``USEPAO=0``, full domains (``DOMSEL=1``) will be used.
* ``FULLAO`` if ``USEVRT=0`` and ``FULLAO=1``, local RI approximations only apply to the RI contributions :math:`p'`. This should give the same results as ``USEVRT=1`` (only applies if ``USEPAO=0``).
* ``DEBUG`` Parameter for debug print
* ``LOCFIT_F12`` If set to one, use local fitting. Default is no local fitting (``LOCFIT_F12=0``)
* ``LOCFIT_R12`` Alias for ``LOCFIT_F12``. Local fitting is not recommended in R12 calculations.
* ``FITDOM`` Determine how the base fitting domains are determined (only applies if ``LOCFIT_F12=1``):

0: Fitdomains based on united operator domains;
1: Fitdomains based in orbital domains (default);
2: Fitdomains based on united pair domains using strong pairs;
3: Fitdomains based on united pair domains using strong, close and weak pairs. Note: This is the only option implemented in the DF-LMP2 program. Therefore, the DF-LMP2 and DF-LMP2-F12 programs might give slightly different results if default values are used.

* ``RDOMAUX`` Distance criterion for density fitting domain extensions in case of local fitting. The default depends on ``FITDOM``.
* ``IDOMAUX`` Connectivity criterion for density fitting domain extensions in case of local fitting.
* ``RAODOM`` Distance criterion for RI domain extensions. Zero means full RI basis (default). If ``USEPAO=1`` or ``USEVRT=1`` or ``FULLAO=1`` a value of 5 bohr is recommended. In other cases the local RI domains must be very large (``RAODOM>12``) and the use of local RI approximations is not recommended.
* ``IAODOM`` Connectivity criterion for RI domain extensions. Zero means full RI basis (default). Values greater or equal to 2 should lead to sufficiently accurate results, provided the local projector (``USEPAO=1``) is used.
* ``THRAO`` Screening threshold for coulomb integrals in the AO or RI basis.
* ``THRAOF12`` Screening threshold for F12 integrals.
* ``THRMO`` Screening threshold for half transformed integrals.
* ``THRPROD`` Product screening threshold in the first half transformation.
* ``NOMP2`` If set to 1, only the F12 calculation is performed, and the LMP2 is skipped. This is sometimes useful if full domains are used, since the iterative LMP2 then causes a big overhead and needs a lot of memory. It is then more efficient to do the a DF-MP2 calculation separately and compute the total energy as the sum of the DF-MP2 energy and the F12 energy
* ``PROJF`` Values greater than 0 invoke the local projector. ``PROJF=1`` project vv parts only (this is formally the most accurate case but only possible with the canonical program [``ANSATZ=3*A(FIX,NOX)``], ``PROJF=2`` project vv and vo parts (default). This is unavoidable if the local program is used [``ANSATZ=3*A(LOC)``].
* ``MODOMC`` If :math:`\gt 0`, core contributions are neglected in the projector. This is a necessary approximation in order to compute the LCCSD-F12 coupling terms efficiently (implementation not yet finished). Setting ``MODOMC=0`` avoids the approximation. Note that the results in `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3647565>`__ **135**, 144117 (2011) have been obtained using ``MODOMC=0``.

Further options for density fitting are described in section :doc:`density fitting <density_fitting>`, and further options to choose the ansatz in section `choosing the ansatz and the level of approximation <explicitly_correlated_methods.html#choosing-the-ansatz-and-the-level-of-approximation>`__.

Typical inputs for calculations with local approximations are:

.. code-block:: text

   !parameters for local density fitting:
   DFIT,LOCFIT_F12=1,FITDOM_MP2=1,IDOMAUX_MP2=3,DSCREEN=1
   !LMP2-F12(loc) with local RI:
   {DF-LMP2-F12,ANSATZ=3*A(LOC),DOMSEL=0.985,RAODOM=5,PAIRS=WEAK}

This would perform a local MP2 with a Boughton-Pulay domain completeness criterion of 0.985. In the F12 part, distant pairs are not included (``PAIRS=WEAK``) and the local projector is used (``USEPAO=1``, default). Local density fitting and local RI approximations are used.

A corresponding non-local calculation (still using localized orbitals and the diagonal ansatz) would be

.. code-block:: text

   {DF-LMP2-F12,ANSATZ=3*A(LOC),DOMSEL=1.0,USEVRT=1,NOMP2=1}
   ecorr_F12=ef12
   
   {DF-MP2}
   ecorr_MP2=energy-energr             !mp2 correlation energy
   ecorr_MP2_F12=ecorr_MP2+ecorr_F12   !total correlation energy

Note: The use of local DF and RI domains is still experimental and should be use with care!

.. _explicitly_correlated_methods--variables-set-by-the-f12-programs:

Variables set by the F12 programs
---------------------------------

The following variables are set by the F12 programs:

* ``ENERGR`` Reference energy. This includes the perturbative CABS singles correction if computed.
* ``ENERGY`` Total energy of the requested method (including the F12 and singles corrections). ``ENERGY(1)`` and ``ENERGY(2)`` hold the F12A and F12B values, respectively (if both are computed).
* ``ENERGC`` Total CCSD-F12 energies in ccsd-f12 or uccsd-f12 calculations. ``ENERGC(1)`` and ``ENERGC(2)`` hold the F12A and F12B values, respectively (if both are computed). The difference of ``ENERGY`` and ``ENERGC`` is the triples energy contribution.
* ``ENERGT`` Triples energy contribution. This is a vector. The corresponding methods are stored in ``METHODT`` (strings).
* ``EMP2`` Total MP2 energy (excluding F12 correction, but including the singles correction).
* ``EMP2_SCS`` Total SCS-MP2 energy (excluding F12 correction, but including the singles correction).
* ``EMP2_SING`` Singlet MP2 correlation energy (excluding F12 correction).
* ``EMP2_TRIP`` Triplet MP2 correlation energy (excluding F12 correction).
* ``EMP2_STRONG`` Strong pair contribution to the LMP2 correlation energy (where applicable).
* ``EMP2_CLOSE`` Close pair contribution to the LMP2 correlation energy (where applicable).
* ``EMP2_WEAK`` Weak pair contribution to the LMP2 correlation energy (where applicable).
* ``EMP2_DIST`` Distant pair F12 contribution to the LMP2-F12 correlation energy (where applicable).
* ``EF12`` F12 contribution to the MP2-F12 correlation energy for the requested ansatz.
* ``EF12S`` F12 contribution to the MP2-F12 correlation energy using EBC approximation for the requested ansatz.
* ``EF12D`` F12 contribution to the MP2-F12 correlation energy using EBC approximation and diagonal (DX) approximation for the requested ansatz.
* ``EF12_SING`` Singlet F12 contribution to the MP2-F12 correlation energy for the requested ansatz.
* ``EF12_TRIP`` Triplet F12 contribution to the MP2-F12 correlation energy for the requested ansatz.
* ``EF12_STRONG`` Strong pair F12 contribution to the LMP2-F12 correlation energy (where applicable).
* ``EF12_CLOSE`` Close pair F12 contribution to the LMP2-F12 correlation energy (where applicable).
* ``EF12_WEAK`` Weak pair F12 contribution to the LMP2-F12 correlation energy (where applicable).
* ``EF12_DIST`` Distant pair F12 contribution to the LMP2-F12 correlation energy (where applicable).
* ``EF12_SCS`` F12 contribution to the MP2-F12 correlation energy for the requested ansatz.
* ``EF12_SINGLES`` Total CABS singles contribution (in closed-shell case equal to ``EF12_RHFRELAX``).
* ``EF12_RHFRELAX`` CABS singles correction of the reference energy (only the spin-free contribution is used).
* ``ANSATZ`` The requested ansatz (string variable)

Variables corresponding to ``EF12_`` exist also for ``EF12S_`` and ``EF12D_``.

In case of doubt or problems, try in a test calculation

``SHOW,ENERG*,EMP2*,EF12*``

This should show all relevant variables that exist. Note that system variables are internally stored with an underscore as a prefix, and this may be shown by the SHOW command. The variables can be accessed with or without underscore (but if the user defines a variable with the same name then the underscore is needed to access the system variable and not the user variable).

.. _explicitly_correlated_methods--analytical-gradients-for-mp2-f12-and-ccsd-t-f12:

Analytical gradients for MP2-F12 and CCSD(T)-F12
------------------------------------------------

Analytical energy gradients are available for DF-MP2-F12, DF-CCSD-F12, and DF-CCSD(T)-F12 methods using the density fitting approximation. The ``AIC`` density fitting integral program computes the two- and three-index integrals and integral derivatives required. Analytical gradients are available only for a subset of approximations listed above. For the rest of F12 approximations, equilibrium geometries and other properties can be computed by using numerical differentiation of the energies. In the following, we describe only those options which must be used for analytical gradients.

Explicitly correlated property calculations can be performed using the commands followed by ``FORCE`` or ``OPTG`` of the form, for example for geometry optimizations,

*command*, *options*;
``OPTG``

where *command* can be one of the following:

* ``DF-MP2-F12`` Closed-shell canonical MP2-F12 using the density fitting approximation for all integrals and their derivatives as described in `J. Chem. Phys. <https://dx.doi.org/10.1063/1.5003065>`__ **147**, 214101 (2017), doi: 10.1063/1.5003065. Only the fixed amplitude approximation without forming CABS orbitals is considered.
* ``DF-CCSD-F12`` Closed-shell CCSD-F12 approximations using the density fitting approximation for all integrals and their derivatives as described in `J. Chem. Phys. <https://dx.doi.org/10.1063/1.5020436>`__ **148**, 114104 (2018), doi: 10.1063/1.5020436. Only the fixed amplitude ansatz is used without constructing CABS orbitals. Both CCSD-F12a and F12b explicitly correlated coupled cluster approximations are available. By default, the CCSD-F12b approximation is used. Some parts the implementation are brute-force, therefore large memory and disk space may be required.
* ``DF-CCSD(T)-F12`` Same as DF-CCSD-F12, but perturbative triples are added. The scaled version of (T) is currently not available. See details in `J. Chem. Phys. <https://dx.doi.org/10.1063/1.5020436>`__ **148**, 114104 (2018).

**Note: analytical gradients are only computed if certain Ansätze and options are used, see below. If these are not given, numerical gradients are used.**

The analytical gradients for F12 methods are implemented using the integrated tensor framework (ITF) of G. Knizia. This program uses slightly different RI approximations than the standard F12 programs. In particular, the CABS approach is not used and the CABS singles correction is not available. Due to the different RI treatment, the energies are only identical to the standard ones if the OPTRI basis sets are used. In this case the RI basis is the union of the orbital basis and the OPTRI basis, and exactly the same results as with the CABS approach are obtained. It is therefore recommended to use the OPTRI basis when available.

A typical input reads:

.. code-block:: text

   basis=avtz
   df-hf
   df-ccsd(t)-f12,ri_basis=optri
   optg

For DF-MP2-F12 further options need to be specified:

.. code-block:: text

   basis=avtz
   df-hf
   df-mp2-f12,ansatz=3*C(FIX,HY1),cabs=0,cabs_singles=0,ri_basis=optri
   optg

The Ansatz can be chosen using the ``ANSATZ`` option and/or by options on the command line. For analytical gradients, the following approximation are available for DF-MP2-F12 and DF-CCSD(T)-F12:

* **[\tt{ansatz=3C(FIX,HY1)}]** Ansatz 3C with hybrid approximation, see `J. Chem. Phys. <https://dx.doi.org/10.1063/1.2712434>`__ **126**, 164102 (2007);
* ``ansatz=3*C(FIX,HY1)`` Ansatz 3C with EBC and hybrid approximations;
* ``ansatz=3*A(FIX)`` Ansatz 3A with EBC approximation;

For DF-MP2-F12, further options must be specified

* ``CABS=0`` Do not use CABS orbitals.
* ``CABS_SINGLES=0`` Do not add CABS singles correction.

Overall, the following commands and options are valid for DF-MP2-F12:

.. code-block:: text

   df-mp2-f12,ansatz=3C(FIX,HY1),cabs=0,cabs_singles=0
   df-mp2-f12,ansatz=3*C(FIX,HY1),cabs=0,cabs_singles=0
   df-mp2-f12,ansatz=3*A(FIX),cabs=0,cabs_singles=0

For DF-CCSD-F12 and DF-CCSD(T)-F12, the options ``cabs=0,cabs_singles=0`` and the ansatz specifications ``HY1, FIX`` are implied by the ``DF-`` prefix, since there are no corresponding standard methods. It is therefore sufficient to specify the ansatz in short form

.. code-block:: text

   df-ccsd(t)-f12,ansatz=3C
   df-ccsd(t)-f12,ansatz=3*C
   df-ccsd(t)-f12,ansatz=3*A

These are equivalent, respectively, to the following specifications:

.. code-block:: text

   df-ccsd(t)-f12,ansatz=3C(FIX,HY1),cabs=0,cabs_singles=0
   df-ccsd(t)-f12,ansatz=3*C(FIX,HY1),cabs=0,cabs_singles=0
   df-ccsd(t)-f12,ansatz=3*A(FIX),cabs=0,cabs_singles=0

The default Ansatz is ``3*C``, and thus

.. code-block:: text

   df-ccsd(t)-f12

corresponds to DF-CCSD(T)-F12b/3\*C(FIX,HY1) without CABS treatment and without CABS singles correction. Fixed amplitudes, ``FIX``, are always used in CCSD(T)-F12. By default, the explicitly correlated coupled cluster approximation F12b is used. Optionally, F12a or F12b can be appended to the command in order to choose the corresponding approximation, such as

.. code-block:: text

   df-ccsd(t)-f12a

or

.. code-block:: text

   df-ccsd(t)-f12b

Note that, property calculations including CABS singles corrections must be done by combining numerical derivatives for HF+CABS singles method and F12 analytical gradients. For geometry optimizations see details in `adding CABS singles correction in CCSD(T)-F12 geometry optimization <geometry_optimization_optg.html#adding-cabs-singles-correction-in-ccsd-t-f12-geometry-optimization>`__.

.. _explicitly_correlated_methods--expectation-values-for-mp2-f12-and-ccsd-t-f12:

Expectation values for MP2-F12 and CCSD(T)-F12
==============================================

``EXPEC[,[TYPE=]type][,opname]``

One-electron properties can be computed if an ``EXPEC`` directive follows the ``DF-MP2-F12``, ``DF-CCSD``, or ``DF-CCSD(T)`` cards (the ``GEXPEC`` directive has no effect in this case). Properties are obtained as analytical energy derivatives with or without taking into account the orbital relaxation, which can be specified as

* **``TYPE``:** *type*\ =\ ``RELAX``: Compute fully relaxed properties with taking into account the orbital relaxation (default). Nonrelaxed properties are also computed and printed. For MP2, this option is highly recommended.

*type*\ =\ ``NORELAX``: Compute properties without taking into account the orbital relaxation.

* ***opname*:** Currently only dipole moment can be computed, *opname*\ =\ ``DM``.

The same restrictions for the ansatz as described for gradients in section `analytical gradients for MP2-F12 and CCSD(T)-F12 <explicitly_correlated_methods.html#analytical-gradients-for-mp2-f12-and-ccsd-t-f12>`__ apply. For ``DF-MP2-F12`` the ansatz must be specified, since without ``EXPEC`` a different ``DF-MP2-F12`` program is used, and ansatz 3C is the default. Slightly different RI approximations are used with the gradient ``DF-MP2-F12`` code, and this leads to slightly different energies even with the same ansatz specified.

Note also that calculations including CABS singles corrections must be done by adding the CABS singles contribution computed separately. The syntax for operators *opname* is explained in section `One-electron operators and expectation values (GEXPEC) <program_control.html#one-electron-operators-and-expectation-values-gexpec>`__. See also ``DM`` in section `saving the density matrix <moller_plesset_perturbation_theory.html#saving-the-density-matrix>`__, and ``NATORB`` in section `natural orbitals <moller_plesset_perturbation_theory.html#natural-orbitals>`__.
