.. raw:: html

   <span id="auxiliary-basis-sets-for-density-fitting-or-resolution-of-the-identity"></span>

.. raw:: html

   <span id="cartesian-and-spherical-harmonic-basis-functions"></span>

.. raw:: html

   <span id="contracted-set-definitions"></span>

.. raw:: html

   <span id="default-basis-sets"></span>

.. raw:: html

   <span id="default-basis-sets-for-individual-atoms"></span>

.. raw:: html

   <span id="examples"></span>

.. raw:: html

   <span id="primitive-set-definition"></span>

.. raw:: html

   <span id="the-basis-set-library"></span>

.. _basis_input--basis-input:

Basis input
===========

.. _basis_input--overview-sets-and-the-basis-library:

Overview: sets and the basis library
====================================

Basis functions are used in Molpro not just for representing orbitals, but also for providing auxiliary sets for density fitting (see :doc:`density fitting <density_fitting>`) and for simplifying integrals through approximate identity resolution in explicitly-correlated methods (see :doc:`explicitly correlated methods <explicitly_correlated_methods>`). In order to accommodate this, the program maintains internally a number of different *sets*. The first of these always has the name ``ORBITAL`` and is the primary basis set for representing orbitals, and others can be defined as necessary as described below, or else are constructed automatically by the program when required. In the latter case, the density-fitting and other modules attempt to guess a reasonable library fitting basis that should be appropriate for the orbital basis set; it is advisable to check the choice when using anything other than a standard orbital basis set.

The basis sets may either be taken from the library, or may be specified explicitly, or any combination. Optionally, the basis function type can be chosen using the ``CARTESIAN`` or ``SPHERICAL`` commands.

.. _basis_input--cartesian-and-spherical-harmonic-basis-functions:

Cartesian and spherical harmonic basis functions
================================================

[command:spherical]

``MOLPRO`` uses spherical harmonics (:math:`5d`, :math:`7f`, etc) by default, even for Pople basis sets like ``6-31G**``. This behaviour may be different to that of other programs; However, cartesian functions can be requested using the ``CARTESIAN`` command.

``CARTESIAN``

If this command is encountered, the logical ``MOLPRO`` variable ``CARTESIAN`` is set to true (1.0), and all subsequent calculations use cartesian basis functions. This is remembered across restarts. One can switch back to spherical harmonics using the command.

``SPHERICAL``

It should be noted that there are the following disadvantages and limitations when using cartesian basis functions:

- the basis sets are larger and more linearly dependent;
- density fitting routines are much slower with cartesian basis functions than with spherical harmonics;
- some programs cannot use cartesian basis functions at all, e.g. the PNO programs, gradients with density fitting, or F12 calculations.

Since Molpro 2022.2 all auxiliary basis sets (e.g. for density fitting or RI) use spherical functions by default, independent of the ``CARTESIAN`` setting. Cartesian auxiliary functions can be used by defining the basis sets in a basis block using, e.g.,

``set, name, context=jkfit, [attributes=]cartesian\\``
\....

but this is not recommended since such sets become often linearly dependent.

.. _basis_input--the-basis-set-library:

The basis set library
=====================

The basis set library consists of a set of plain text files that constitute a database of commonly-used basis sets (primitive gaussians and associated contractions) and effective core potentials. These files can be found in the source tree as ``lib/*.libmol``.

Many of the basis sets are taken directly from the Basis Set Exchange  `database <https://www.basissetexchange.org>`__, but there are others, notably the Stuttgart `effective core potentials and bases <http://www.tc.uni-koeln.de/PP/index.en.html>`__ and Grant Hill's database for correlation consistent basis sets, `ccRepo <http://www.grant-hill.group.shef.ac.uk/ccrepo>`__.

.. _basis_input--default-basis-sets:

Default basis sets
==================

If a basis is not specified at all for any unique atom group, then the program assumes a global default. Presently, this default is ``VDZ``, but may be overridden using

``BASIS,basis``

or

``BASIS=basis``

*basis* is looked up in the file ``lib/defbas``, which generates an appropriate request for a complete contracted set, together in some cases with an ECP, from the library. This mapping includes the following commonly-used basis sets:

* All of the Dunning correlation consistent basis sets, through the use of either the standard name of the basis set (``cc-pVXZ``, ``aug-cc-pVXZ``) or an abbreviation (``VXZ``, ``AVXZ``). For Al-Ar the tight-d augmented sets are obtained through the standard name ``cc-pV(X+d)Z``, ``aug-cc-pV(X+d)Z`` or ``VXZ+d``, ``AVXZ+d``. Sets X=D,T,Q,5 are available for H-Kr with X=6 available for B-Ne and Al-Ar.
* The correlation consistent basis sets for core correlation, ``cc-pCVXZ``, ``aug-cc-pCVXZ`` or ``CVXZ``, ``ACVXZ`` (X=D,T,Q,5), and the newer ”weighted sets” ``cc-pwCVXZ``, ``aug-cc-pwCVXZ`` or ``WCVXZ``, ``AWCVXZ`` (X=D,T,Q,5). These are available for Li-Kr (CVXZ do not include Sc-Zn).
* Douglas-Kroll-Hess relativistic versions of the correlation consistent basis sets are available through use of the standard or abbreviated names with extension -DK, e.g., ``cc-pVXZ-DK`` or ``VXZ-DK`` (2nd-order DKH). X=D-5 are available for H-Kr, while X=T are available for Y-Cd and Hf-Hg, X=D,T,Q for In-Xe, Tl-Rn, K-Ca, and Rb-Sr. Sets contracted for 3rd-order DKH with extension -DK3 are available for Hf-Hg (X=T) and X=D,T,Q for In-Xe, Tl-Rn, La-Lu, Ac-Lr, Cs-Ba, and Fr-Ra. Most of these sets have also been contracted for the eXact-2-Component (X2C) Hamiltonian as detailed below.
* The F12 basis sets of Peterson and co-workers for explicitly correlated calculations, ``cc-pVXZ-F12``, ``cc-pCVXZ-F12`` or ``VXZ-F12``, ``CVXZ-F12`` with X=D,T,Q are available for H-Ar, while ``cc-pVXZ-PP-F12`` or ``VXZ-PP-F12`` with X=D,T,Q are available for Cu-Kr, Ag-Xe, and Au-Rn.
* The Turbomole def2 family of basis sets, ``SV(P)``, ``SVP``, ``TZVP``, ``TZVPP``, ``QZVP``, and ``QZVPP``. These are available for the entire periodic table except for the f-block elements.
* The older segmented Dunning/Hay double-zeta sets for the first row (``DZ`` and ``DZP``).
* The Roos ANO basis sets for H-Ar (``ROOS``).
* The Stuttgart ECPs and associated basis sets (e.g., ``ECP10MDF``), as well as the ECP-based correlation consistent basis sets of Peterson and co-workers, ``cc-pVXZ-PP``, ``aug-cc-pVXZ-PP``, ``cc-pwCVXZ-PP``, ``aug-cc-pwCVXZ-PP`` or ``VXZ-PP``, ``AVXZ-PP``, ``WCVXZ-PP``, ``AWCVXZ-PP``. The latter are available for Cu-Kr, Y-Xe, and Hf-Rn (core correlation sets currently only for transition metals).
* The Hay ECPs and corresponding basis sets (``ECP1`` and ``ECP2``).
* Other members of the Karlsruhe basis sets (``SV``, ``TZV``, and, for some elements, ``TZVPPP``).
* The Binning/Curtiss sets for Ga–Kr (``BINNING-SV``, ``BINNING-SVP``, ``BINNING-VTZ`` and ``BINNING-VTZP``)
* Most of the Pople basis sets, using their standard names (e.g., ``6-31G*, 6-311++G(D,P)``, etc.). Note that specially in this case, the mechanism described below using parenthesized modifiers to restrict the basis set is disabled to allow the full range of standard basis sets to be specified.

Short names for the available correlation-consistent default basis sets with ``X=D|T|Q|5`` are listed in the following table.
Augmented sets are as non-augmented and therefore not listed.
The short names of augmented sets have prefix ``a``, ``da``, ``ta``, for singly, doubly, or triply augmented sets, e.g. ``avtz``.
Note that not all cardinal numbers may be available for each Z.

Valence basis sets:

.. list-table::
   :header-rows: 1

   * - short name
     - full name
     - range Z
   * - vxz
     - cc-pVXZ
     - 1-36
   * - vxz-f12
     - cc-pVXZ-F12
     - 1-18

Core-valence basis sets:

.. list-table::
   :header-rows: 1

   * - short name
     - full name
     - range Z
   * - cvxz
     - cc-pCVXZ
     - 3-18, 20, 31-36 (except for 20 these point to cc-pwCVXZ-DK)
   * - wcvxz
     - cc-pwCVXZ
     - 3-36
   * - cvxz-f12
     - cc-pCVXZ-F12
     - 3-18

Basis sets for relativistic calculations:

.. list-table::
   :header-rows: 1

   * - short name
     - full name
     - range Z
   * - vxz-x2c
     - cc-pVXZ-X2C
     - 1-2, 5-10, 13-20, 37-38, 55-71, 87-103
   * - cvxz-x2c
     - cc-pCVXZ-X2C
     - 5-10, 13-18

.. list-table::

   * - vxz-dk
     - cc-pVXZ-DK
     - 1-103
   * - wcvxz-dk
     - cc-pwCVXZ-DK
     - 3-53, 72-86
   * - wcvxz-dk3
     - cc-pwCVXZ-DK3
     - 49-103
   * - wcvxz-x2c
     - cc-pwCVXZ-X2C
     - 5-10, 13-20, 37-38, 55-71, 87-103

Pseudo-potential basis sets. The number of core electrons contained in the pseudo-potential corresponds to the number in its name:

.. list-table::
   :header-rows: 1

   * - short name
     - full name
     - pseudo-pot.
     - range Z
   * - vxz-pp
     - cc-pVXZ-PP
     - all electron
     - 1-18
   * - vxz-pp
     - cc-pVXZ-PP
     - ECP10MDF
     - 19-20, 29-36
   * - vxz-pp
     - cc-pVXZ-PP
     - ECP28MDF
     - 37-54
   * - vxz-pp
     - cc-pVXZ-PP
     - ECP46MDF
     - 55-56
   * - vxz-pp
     - cc-pVXZ-PP
     - ECP60MDF
     - 72-86, 90-92
   * - vxz-pp
     - cc-pVXZ-PP
     - ECP78MDF
     - 87-88

.. list-table::

   * - wcvxz-pp
     - cc-pwCVXZ-PP
     - all electron
     - 1-18
   * - wcvxz-pp
     - cc-pwCVXZ-PP
     - ECP10MDF
     - 19-20, 29-36
   * - wcvxz-pp
     - cc-pwCVXZ-PP
     - ECP28MDF
     - 37-54
   * - wcvxz-pp
     - cc-pwCVXZ-PP
     - ECP46MDF
     - 55-56
   * - wcvxz-pp
     - cc-pwCVXZ-PP
     - ECP60MDF
     - 72-86, 90-92
   * - wcvxz-pp
     - cc-pwCVXZ-PP
     - ECP78MDF
     - 87-88

.. list-table::

   * - vxz-pp-f12
     - cc-pVXZ-PP-F12
     - ECP10MDF
     - 29-36
   * - vxz-pp-f12
     - cc-pVXZ-PP-F12
     - ECP28MDF
     - 47-54
   * - vxz-pp-f12
     - cc-pVXZ-PP-F12
     - ECP60MDF
     - 79-86

Karlsruhe (Turbomole) basis sets (def2 and dhf). These are also available as augmented and doubly augmented basis sets:

.. list-table::
   :header-rows: 1

   * - short name
     - full name
     - pseudo-pot.
     - range Z
   * - TZVPP
     - def2-TZVPP
     - all electron
     - 1-36
   * - TZVPP
     - dhf-TZVPP
     - ECP28MDF
     - 37-48
   * - TZVPP
     - def2-TZVPP
     - ECP28MDF
     - 49-52
   * - TZVPP
     - dhf-TZVPP
     - ECP28MDF
     - 53
   * - TZVPP
     - def2-TZVPP
     - ECP28MDF
     - 54
   * - TZVPP
     - dhf-TZVPP
     - ECP46MDF
     - 55-56
   * - TZVPP
     - def2-TZVPP
     - ECP46MWB
     - 57
   * - TZVPP
     - def2-TZVPP
     - ECP28MWB
     - 58-71
   * - TZVPP
     - dhf-TZVPP
     - ECP60MDF
     - 72-79
   * - TZVPP
     - def2-TZVPP
     - ECP60MWB
     - 80
   * - TZVPP
     - def2-TZVPP
     - ECP60MDF
     - 81-86

Karlsruhe (Turbomole) basis sets with diffuse functions:

.. list-table::
   :header-rows: 1

   * - short name
     - full name
     - pseudo-pot.
     - range Z
   * - TZVPPD
     - def2-TZVPPD
     - all-electron
     - 1 - 36
   * - 
     - def2-TZVPPD
     - ECP28MWB
     - 37-38
   * - 
     - def2-TZVPPD
     - ECP28MWB
     - 39-48
   * - TZVPPD
     - def2-TZVPPD
     - ECP28MDF
     - 49-52
   * - 
     - def2-TZVPPD
     - ECP28MDF
     - 53
   * - TZVPPD
     - def2-TZVPPD
     - ECP28MDF
     - 54
   * - 
     - def2-TZVPPD
     - ECP46MWB
     - 55-56
   * - TZVPPD
     - def2-TZVPPD
     - ECP46MWB
     - 57
   * - 
     - def2-TZVPPD
     - ECP60MWB
     - 72-79
   * - TZVPPD
     - def2-TZVPPD
     - ECP60MWB
     - 80
   * - TZVPPD
     - def2-TZVPPD
     - ECP60MDF
     - 81-86

In addition, many density fitting and resolution of the identity (RI) basis sets are available. For the correlation consistent basis sets of Dunning, the appropriate VXZ/JKFIT, VXZ/MP2FIT, AVXZ/MP2FIT sets of Weigend are chosen automatically in density fitted calculations (augmented versions AVXZ/JKFIT for Fock-matrix fitting are also available). For the def2 family of orbital basis sets, the appropriate auxiliary sets (e.g., TZVPP/JFIT, TZVPP/JKFIT, TZVPP/MP2FIT) are used. In principle these JKFIT sets are universal and also applicable in combination with the AVXZ basis sets. Initial results indicate that they also work well with the cc-pVXZ-PP and aug-cc-pVXZ-PP series of basis sets.

For explicitly correlated F12 calculations that use the cc-pVXZ-F12 or cc-pVXZ-PP-F12 orbital basis sets, the corresponding VXZ-F12/OPTRI or VXZ-PP-F12/OPTRI basis sets are used by default to construct the complementary auxiliary orbital basis (CABS). For other orbital basis sets, appropriate JKFIT sets are utilized by default.

Example:

``BASIS=VTZ``

generates valence triple zeta basis set for all atoms. Thus, the input

.. code-block:: text
   :caption: examples/h2o_scf_vtz.inp

   ***,h2o cc-pVTZ basis     !A title
   r=1.85,theta=104          !set geometry parameters
   geometry={O;              !z-matrix geometry input
             H1,O,r;
             H2,O,r,H1,theta}
   basis=VTZ                 !use VTZ basis
   hf                        !closed-shell scf

performs a Hartree-Fock calculation for H\ :math:`_2`\ O using the cc-pVTZ basis set.

Default basis sets can be defined anywhere in the input before the energy calculation to which it should apply using a single ``BASIS`` card as shown above. The default basis set applies to all types of atoms but can be superceded by different basis sets for specific atoms as explained in the next section. Some restrictions concerning the maximum angular momentum functions to be used, or the number of contracted functions are possible as follows:

The maximum angular momentum in the basis set can be reduced using syntax such as

``BASIS,VQZ(D)``

which would omit the :math:`f` and :math:`g` functions that would normally be present in the VQZ basis set.

``BASIS,VQZ(D/P)``

would specify additionally a maximum angular momentum of :math:`1` on hydrogen, i.e. would omit :math:`d` orbitals on hydrogen.

For generally contracted basis sets, an extended syntax can be used to explicitly give the number of contracted functions of each angular momentum. For example,

``BASIS,ROOS(3s2p1d/2s)``

generates a ``6-31G*``-sized basis set from the Roos ANO compilation.

Notes: *basis* must not be variable called BASIS. Furthermore, input like

``$BASIS=[AVDZ, AVTZ, AVQZ]``

is not allowed, i.e. the keyword ``BASIS`` must not be preceded with $. One can loop over several basis sets using, for example, using

.. code-block:: text

   
   $aobases=[AVDZ, AVTZ, AVQZ]
   do ibas=1,#aobases
   basis=aobases(ibas)
   ...
   enddo

.. _basis_input--default-basis-sets-for-individual-atoms:

Default basis sets for individual atoms
=======================================

Different default basis sets for individual atoms can be specified with one-line ``BASIS`` commands by adding after the default basis *atom1=name1, atom2=name2,…*, where *atomi* are the chemical symbols, and *namei* are the associated basis set names. The name conventions for the atom specific basis sets work exactly as described above for default basis sets. Examples:

``basis=vtz,h=vdz``

uses cc-pVTZ as a general default, but for hydrogen atoms cc-pVDZ is used.

``basis,vtz,h=vdz``

or

``basis,default=vtz,h=vdz``

are equivalent to the above. Note that the default basis has to be specified before any atom specific sets.

Since Molpro2024.2 one can also define basis sets for ranges of atoms. The range is given as atom1-atom2, where Z(atom2)>Z(atom1), for example

``basis,default=awcvtz,h=vtz,b-cl=avtz``

.. _basis_input--basis-blocks:

Basis blocks
============

More specific basis set definitions for individual atoms can be given in ``BASIS`` input blocks, which have the following general form:

.. code-block:: text

   BASIS
   SET,setname1,[options]
   DEFAULT=name
   atom1=name1
   atom2=name2
   primitive basis set specifications
   SET,setname2,[options]
   ...
   END

Instead of the ``BASIS`` …\ ``END`` block one can also use the structure ``BASIS={…}``

Any number of basis sets can be be given in a basis block. The definition of each basis set is started by a ``SET`` directive, on which the name of the basis and further options can be specified.

By default, the first set in a basis block is the orbital basis, and in this case the directive ``SET,ORBITAL`` can be omitted.

``DEFAULT`` specifies the default basis set, exactly as on one line basis input. It can be followed by specifications for individual atoms, e.g. O=AVTZ. The default and atom specifications can also be merged to one line, separated by commas, e.g.

``DEFAULT=VTZ,O=AVTZ,H=VDZ``

Here the basis sets ``AVTZ``, ``VDZ`` overwrite the default basis set VTZ for the atoms O and H, respectively. This is exactly as described in section `default basis sets for individual atoms <basis_input.html#default-basis-sets-for-individual-atoms>`__ for one-line basis inputs.

The specifications ``SET``, ``DEFAULT``, ``atom=name`` are all optional. If ``DEFAULT`` is not given, the previous default, as specified on the last previous ``BASIS`` card, is used.

Several ``BASIS`` cards and/or blocks can immediately follow each other. Always the last specification for a given atom and setname is used (the default setname is ``ORBITAL``).

If a basis is not specified at all for any unique atom group, then the program assumes VDZ.

If the setnames are ``JFIT``, ``JKFIT``, ``MP2FIT``, ``CCSDFIT``, ``OPTRI`` and/or ``CABS`` , these basis are used automatically all programs where needed (unless different basis sets are defined in the input for these programs). Note, however, that this is not the case if  different names (e.g. JK) are used. In this case one would need to give, for example,

``DF-HF,BASIS=JK``

in order to use the auxiliary basis in DF-HF.

.. _basis_input--auxiliary-basis-sets-for-density-fitting-or-resolution-of-the-identity:

Auxiliary basis sets for density fitting or resolution of the identity
======================================================================

As described in the previous section, several basis sets can be defined in a basis block. The definition of each basis starts with a line

``SET``,\ *name*,[``CONTEXT=``\ *context*] where *name* is an arbitrary name that can be used later to choose the basis set using options like ``df_basis=``\ *name*, ``ri_basis=``\ *name* etc. ``CONTEXT`` can optionally be specified to select the basis types ``JFIT``, ``JKFIT``, ``MP2FIT``, ``CCSDFIT``, ``OPTRI``, or ``CABS``. This affects the choice of default basis sets. For example

.. code-block:: text

   basis={
   default=avtz    !default orbital basis set
   set,df,context=mp2fit,[attributes=type]
   default,avtz    !use avtz/mp2fit
   set,jk,context=jkfit
   default,avtz    !use avtz/jkfit
   }

is equivalent to

.. code-block:: text

   basis={
   default=avtz          !default orbital basis set
   set,df
   [attributes,type]
   default,avtz/mp2fit   !use avtz/mp2fit
   set,jk
   default,avtz/jkfit    !use vtz/jkfit
   }

If the setname begins with ``JFIT``, ``JKFIT``, ``MP2FIT``, ``CCSDFIT``, ``OPTRI``, or ``CABS``, these strings define the default context. If the setnames correspond exactly to the context name, the corresponding sets are used automatically where needed (e.g. ``JKFIT`` in DF-HF and ``MP2FIT`` in DF-MP2).

Optionally, the basis function type ``CARTESIAN`` (6d, 10f etc) or ``SPHERICAL`` (5d, 7f etc) can be chosen using ``ATTRIBUTE``. By default, the same type as for the orbital basis is used. Normally, ``SPHERICAL`` is used and recommended. Density fitting with CARTESIAN is limited to g-functions in the orbital basis. Furthermore, density fitting with CARTESIAN is much slower than with SPHERICAL.

Specific basis sets for individual atoms or explicit input of exponents and contraction coefficients can be given exactly in the same way as for orbital basis sets.

.. _basis_input--primitive-set-definition:

Primitive set definition
========================

Default basis sets given using one-line ``BASIS`` commands or ``DEFAULT`` directives in a basis block can be overwritten by explicit specifications of basis functions (type, exponents, contraction coefficients).

A group of basis functions is defined by a data card specifying a set of primitive gaussians, optionally followed by one or more cards specifying particular contractions of primitives to be included in the final basis (see section `contracted set definitions <basis_input.html#contracted-set-definitions>`__ for specification of contractions).

If an individual basis function type (:math:`s`, :math:`p`, :math:`d`, etc.) is specified for an atom, it is required that all other types are also defined, i.e., as soon as an explicit definition of a basis function for an atom is given, all defaults are erased for this atom.

There are four different input forms for basis functions, as explained below under a) to d). In case that options (e.g. ``SCALE``, ``NPRIM``) are specified, they can be given in any order, but no value without option key must be given after an option.

In all four cases *type* defines the angular symmetry (``S, P, D, F, G, H,`` or ``I``). *type* can include several types, e.g., ``SPD`` or ``DF`` (this usually makes sense only with default library contractions or no contractions). The basis is loaded for all atoms with tag name *atom* in the geometry input. If *atom* is an integer, it refers to a z-matrix row.

If individual basis functions are specified, and "+" is given before the type (e.g. ``+S``, ``+P``) these functions are added to an existing default basis (only with molpro2026.1 or later).

a) Library basis sets:

*type,atom,name,scale2,nprim*;

or

``type,atom,name,[SCALE=scale$|$SCALE2=scale2],[NPRIM=nprim$|$DELETE=ndel];``

Load basis named *name* from the library.

If ``SCALE`` or ``SCALE2`` is present, all exponents are scaled by *scale* or *scale\*\*2*, respectively. If ``NPRIM`` is specified, the first *nprim* exponents only are taken from the library. If *nprim* is negative or ``DELETE=``\ *ndel* is given, the last :math:`|nprim|` (:math:`ndel`) basis functions from the library set are deleted. In these cases only a single angular momentum (e.g. *s* or *p*) is allowed in *type*. Associated with the library basis may be a set of default contraction coefficients which may be accessed in subsequent contraction cards. *type* can include several types, e.g., ``SPD`` or ``DF``. This usually makes sense only with default contractions, i.e., such cards should be followed only by “\ ``C``\ ” without any other specifications for contractions.

b) Explicit basis input:

*type,atom,exp1,exp2,*\ :math:`\ldots`\ *expn;expn+1,*\ :math:`\ldots`;

General specification of exponents; continuation onto subsequent cards (separated by semicolon) is permitted as shown (the first card can hold up to 19 exponents, each following card 20 exponents).

The exponents (and other numerical parameters described below such as numbers of functions, and contraction coefficients) can be given as general input expressions, possibly involving variables. It is important to note, however, that these expressions are evaluated typically just once, at the same time as the complete basis set is parsed. This generally happens the first time that the basis set is required, perhaps before the first SCF calculation can be done. If the variables on which the basis depends are altered, this will not be noticed by the program, and the new basis set will not be used for subsequent stages of the computation. If, however, a new basis block is presented in the input, then the program marks as outdated any quantities such as integrals that have been calculated with the old basis set; subsequent job steps will then use the new basis.

If "+" is given before the type (e.g. +s, +p) these functions are added to a previously defined default basis.

c) Even tempered basis sets:

``type,atom,EVEN,nprim,ratio,centre,dratio``

or

``type,atom,EVEN,NPRIM=nprim,[RATIO=ratio],[CENTRE=centre],[DRATIO=dratio]``

Generates a generalized even tempered set of functions. The number of functions :math:`n` is specified by *nprim*, their geometric mean :math:`c` by *centre*, the mean ratio of successive exponents :math:`r` by *ratio*, and the variation of this ratio, :math:`d`, by *dratio*. If *centre* is not given, the previous basis of the same type is extended by diffuse functions. This also holds if a default basis has been specified (only with molpro2026.1 or later). If in this case *ratio* is not given, :math:`r` is determined from the exponents of the last two function of the previous basis. If this is not possible, the default :math:`r=2.5` is adopted. :math:`d=1` (the default) specifies a true even-tempered set, but otherwise the ratio between successive exponents changes linearly; the exponents are given explicitly by

.. math::

   \log e_i =
   \log c
   + ((n+1)/2-i) \,\log r
   + \frac12 ((n+1)/2-i)^2 \,\log d
   \quad
   i=1,2,\dots,n

* **Example 1** ``SP,1,VTZ;C;SP,1,EVEN,1;``

generates the generally contracted :math:`s` and :math:`p` triple-zeta basis sets for atom 1 and extends these by one diffuse function.

* **Example 2** ``SPD,1,VTZ,DELETE=1;C; SP,1,EVEN,NPRIM=2,RATIO=2.5;``

generates the generally contracted :math:`s`, :math:`p` triple-zeta basis sets for atom 1. Two energy optimized :math:`d`-functions of Dunning are included. The last :math:`s` and :math:`p` functions are deleted and replaced by two even tempered functions with ratio 2.5.

d) 3-term tempered basis sets:

``type,atom,EVEN3,nprim,$\alpha$, $\beta$, $\gamma$``

Generates a 3-parameter set of *nprim* functions with exponents given by

.. math::

   e_0 = \alpha ; \qquad e_i=e_{i-1} \,\beta \left(1+\frac{\gamma \cdot i^2}{( { {nprim}}+1)^2}\right)
   , \quad i=1,\dots  {{nprim}}-1

e) Regular even tempered basis sets:

``type,atom,EVENR,nprim,aa,ap,bb,bp``

Generates an even tempered set of *nprim* functions according to the “regular” prescription described in M W Schmidt and K Ruedenberg, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.438165>`__ **71**, 3951 (1970). If any of the parameters *aa, ap, bb, bp* is zero or omitted, the values are taken from table III of the above.

f) Even tempered basis set with confined progression:

``type,atom,EVENP,nprim,$\alpha$,$\beta$,$\gamma$``

Generates an even tempered basis set with *nprim* functions and a maximal exponent given by :math:`\alpha`. The progression (ratio) between the first and second exponent is adjusted using parameter :math:`\beta` and the progression between the last but one and the last exponent is adjusted with parameter :math:`\gamma`. In between the progression is linearly interpolated. The explicit values of the progression factors are given by:

:math:`p(\beta)=\frac{\mathrm{exponent^i}}{\mathrm{exponent^{i+1}}}= \frac{5}{\pi}(\arctan(\beta-2.5)+\frac{\pi}{2})+\sqrt{2}`

so that for :math:`\beta \ll 0: p \rightarrow \sqrt{2}` and for :math:`\beta \gg 0: p \rightarrow 5+\sqrt{2}` which limits the progression factors in between these two values and enables unconstrained basis set optimisations. For :math:`\beta \approx 0` the progression has a factor of about 2.

``type,atom,EVENP2,nprim,$\alpha$,$\beta$,$\gamma$,$\delta$``

Generalises confined progression tempered basis sets by a third parameter (now :math:`\gamma`) which defines the progression as above in the centre. The ratio factors are then determined by interpolating between :math:`p(\beta)\rightarrow p(\gamma)` and :math:`p(\gamma)\rightarrow p(\delta)`.

.. _basis_input--contracted-set-definitions:

Contracted set definitions
==========================

``a) C,first.last,c1,c2,$\ldots$cn;cn+1,$\ldots$;``

General specification of a contracted function. *first.last* defines the range of primitives to be contracted. The order corresponds to the primitives as specified on the previous input card. *c1, c2*\ :math:`\ldots` are the :math:`last-first+1` contraction coefficients. Continuation onto a subsequent card is permitted as shown.

``b) C;``

Use default contractions from the library. This applies to both the number of contracted primitives and also to the number of different contraction sets.

``c) $n$C,first.last;``

:math:`n` contracted functions taken from library. *first.last* defines the range of primitives to be contracted. If :math:`n` is omitted and *first.last* is specified, :math:`n=1`. If *first.last* is omitted, the library default values are used. If both :math:`n` and *first.last* are omitted, default values for both are used.

``d) $n$C,first.last,record.file,orb.sym;``

:math:`n` contracted functions taken from orbitals *orb*, :math:`orb+1`,..,\ :math:`orb+n-1` of symmetry *sym* on molpro file *record.file*. The first nonzero coefficient in the specified orbital corresponds to the first associated basis function. *first.last* specifies the range of primitives to be contracted. If *first.last* is omitted, all coefficients from the specified orbitals are used.

``2C,1.12,2100.2,1.1\\``
generates two contractions, using the first 12 coefficients from orbitals 1.1 and 2.1. The orbitals are read from record 2100.2.

.. _basis_input--examples:

Examples
========

This shows the use of default basis sets for H\ :math:`_2`\ O:

.. code-block:: text
   :caption: examples/h2o_vqz_fp.inp

   ***,H2O
   basis=VQZ(f/p)
   R=0.95 ANG,THETA=104 DEGREE
   geometry={O;H1,O,R;H2,O,R,H1,THETA}
   hf              !do closed-shell SCF

This is equivalent to the explicit input form

.. code-block:: text
   :caption: examples/h2o_vqz_fp_explicit.inp

   ***,H2O
   R=0.95 ANG,THETA=104 DEGREE
   geometry={O;H1,O,R;H2,O,R,H1,THETA}
   basis={spdf,o,vqz;c;sp,h,vqz,c;}
   hf              !do closed-shell SCF

The following example shows how to use two different basis sets for the same element:

.. code-block:: text
   :caption: examples/h2o_two_hydrogen_bases.inp

   gprint,basis
   nosym
   
   geometry={Angstrom,Degree
   O
   H2 1 1.0
   H3 1 1.0 2 109
   }
   
   basis={
   default=cc-pVDZ;
   sp,h2,aug-cc-pVDZ;c
   spd,h3,cc-pVTZ;c
   }
   hf

The following example shows how to code the vtz basis set explicitly (exponents + contraction):

.. code-block:: text
   :caption: examples/h2o_scf_vtz_explicitbasisinput.inp

   gprint,basis
   r=1.85,theta=104          !set geometry parameters
   geometry={O;              !z-matrix geometry input
             H1,O,r;
             H2,O,r,H1,theta}
   !use VTZ basis, explicitly give exponents and contraction coefficients
   basis={
   s,1,15330.000000,2299.000000,522.400000,147.300000,47.550000,16.760000,6.207000,1.752000,0.688200,0.238400;
   c,1.10,0.000508,0.003929,0.020243,0.079181,0.230687,0.433118,0.350260,0.042728,-0.008154,0.002381;
   c,1.10,-0.000115,-0.000895,-0.004636,-0.018724,-0.058463,-0.136463,-0.175740, 0.160934, 0.603418, 0.378765;
   c,8.8,1.0
   c,10.10,1.0
   p,1,34.460000,7.749000,2.280000,0.715600,0.214000
   c,1.5,0.015928,0.099740,0.310492,0.491026,0.336337   
   c,4.4,1.0
   c,5.5,1.0
   d,1,2.314000,0.645000
   f,1,1.428000
   
   s,2,33.870000,5.095000,1.159000,0.325800,0.102700
   c,1.5,0.006068,0.045308,0.202822,0.503903,0.383421
   c,4.4,1.0
   c,5.5,1.0
   p,2,1.407000,0.388000
   d,2,1.057000
   
   s,3,33.870000,5.095000,1.159000,0.325800,0.102700
   c,1.5,0.006068,0.045308,0.202822,0.503903,0.383421
   c,4.4,1.0
   c,5.5,1.0
   p,3,1.407000,0.388000
   d,3,1.057000
   }
   hf                        !closed-shell scf

See `basis sets for explicitly correlated methods <explicitly_correlated_methods.html#basis-sets>`__ for examples when using explicitly correlated methods.
