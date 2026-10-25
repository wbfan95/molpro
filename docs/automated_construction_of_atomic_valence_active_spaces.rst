.. _automated_construction_of_atomic_valence_active_spaces--automated-construction-of-atomic-valence-active-spaces-avas:

Automated construction of atomic valence active spaces (AVAS)
=============================================================

Atomic valence active spaces (AVAS) as described by Knizia et al. can be generated using the AVAS program.
AVAS can be used in two different modes: either as an independent program, or within the Hartree-Fock program using the converged orbitals. The default behaviour in both cases differs slightly, as described below.

.. _automated_construction_of_atomic_valence_active_spaces--avas-as-independent-program:

AVAS as independent program =
=============================

``{AVAS,options\\``
*[directives]*
``CENTER,number,atomic orbital specification\\``
``CENTER,number,atomic orbital specification\\``
...
}

Any number of ``CENTER`` directives can follow each other, and these must directly follow ``AVAS``. If symmetry is used, all symmetry equivalent centers are included automatically, and only one of them needs to be given. If symmetry equivalent centers are explicitly given, the *atomic orbital specifications* on these must be identical, otherwise an error will result.

The *atomic orbital specifications* are of the form

*[n]type*

where *n* is the principal quantum number, and *type* is ``s, p, d``,…. Alternatively, individual components such as ``px, py, pz``, or ``d0, d1+, d1-, d2+, d2-`` can also be given, and then only the specified functions are used (otherwise all components are included). If the principal quantum number :math:`n` is given, the :math:`n-l`\ ’th atomic function of the given type will be used (e.g., for ``2s`` the second :math:`s`-function, for ``2p``, the first :math:`p` function, for ``4d`` the second :math:`d` function). If :math:`n` is not given, the first function of the given type is used.

From Molpro version 2022.2 :math:`n` is the principal quantum number, independent of how many orbitals are in pseudopotentials (ECPs). This is different to earlier versions, were :math:`n` counted the number of orbitals outside the ECP.

Example:

.. code-block:: text

   AVAS
   CENTER, 1, 3d                  !include 3d orbitals for center 1
   CENTER, 2, 2s,2p               !include 2s, 2p orbitals for center 2

The optional *directives* can be:

``OCC, number of occupied orbitals in each symmetry (see below)\\``
``CLOSED, number of closed-shell orbitals in each symmetry (see below)\\``
``WF, …`` (c.f. section `defining the wavefunction <general_program_structure.html#defining-the-wavefunction>`__)
``START,startrecord\\``
``ORBITAL,dumprecord\\``

If a *startrecord* is given, the initial orbitals will be read from this record. If this is not given, an atomic density guess is carried out. This requires one Fock matrix calculation, which is done using density fitting.

*dumprecord* defaults to 2110.2. If an existing dumprecord is given, a new orbital set will be created in that record. If the record contains already previous AVAS orbitals, these are overwritten.

If the occupations (``OCC``, ``CLOSED``) are given, they should normally correspond to the HF occupations.
In Molpro 2021 or later there is a subtle difference in the use of these directives:

If ``OCC`` is given, the occupied (or only closed-shell, see option ``OPEN`` below) and virtual spaces are projected independently. Projected orbitals resulting from the occupied space are copied to the top of the specified occupied space, and those resulting from the virtual space follow thereafter. Depending on the threshold ``THR``, the total number of projected orbitals can be larger than the number of target functions. This happens if a target function contributes both in the occupied and virtual spaces.

If only ``CLOSED`` is given, all orbitals (occupied and virtual) are projected together, and the resulting projected orbitals follow the specified closed-shell space. In this case the number of projected orbitals should normally equal the number of target functions and is independent of the threshold ``THR`` (unless this is very close to 1).

If both ``OCC`` and ``CLOSED`` are given, ``OCC`` has preference. If none of them is given and option ``NELA`` is given, the number of closed-shell orbitals is determined from the number of electrons minus the number of active electrons (NELA) and the behaviour is as with ``CLOSED`` only. The number of closed-shell orbitals in each symmetry is determined by the Aufbau principle using the initial orbital energies.

If neither ``OCC`` and ``CLOSED`` nor ``NELA`` are given, the number of occupied orbitals is determined from the number of electrons and the MS2 value (i.e. the number of open-shell orbitals in a HF determinant), and the behaviour is as described for ``OCC``, except that the number of occupied orbitals in each symmetry is determined by the Aufbau principle using the initial orbital energies.

Note that the described behavior only applies if AVAS is used as independent program. If it is called within the HF program (see below), the occupations are as in the Hartree-Fock wavefunctions and should not be specified.

The following *options* exist:

* **``THR``\ =\ *value*** Threshold for active space selection (default: 0.3)
* **``MINAO_BASIS``\ =\ *name*** Minimal atomic basis set (default ``MINAO``) The specified basis set should be generally contracted, so that the first CGTOs for each angular momentum correspond to the atomic core and valence orbitals. If non-valence orbitals are requested (e.g. 4d for first-row transition metals) the basis must contain at least two CGTOs of the corresponding angular momentum. In this case the default MINAO would is not sufficient and a larger basis must be specified, e.g., VTZ (or, equivalently, cc-pVTZ).
* **``CORE=``\ *val*** If ``CORE=1`` core orbitals are included in the projection (default: ``CORE=0``)
* **``OPEN=``\ *val*** If ``OPEN=1`` closed-shell and open-shell orbitals are included together in the projection (default: ``OPEN=0`` if called from RHF, ``OPEN=1`` if called using the ``AVAS`` command). ``OPEN=1`` will not keep the open-shell RHF energy invariant.
* **``VIRT=``\ *val*** If ``VIRT=0`` virtual orbitals are not projected (default: ``VIRT=1``)
* **``NELA=``\ *val*** Number of active electrons. If ``OCC`` and ``CLOSED`` are not given, this determines the number of closed-shell orbitals.

A subsequent CASSCF (MULTI) calculation will automatically use the generated active space (unless specified otherwise) and use the AVAS orbitals (unless different orbitals are specified on a ``START`` directive).

It is recommended to first do a CASCI calculation using

.. code-block:: text

   GPRINT,ORBITALS,CIVECTOR
   {CASSCF;DONT,ORBI;NATORB}

and check the occupation numbers. Orbitals with very small occupation numbers or with occupation numbers close to 2.0 should then be manually excluded from the active space.

Example for a double d-shell CASSCF for the Cu-atom:

.. code-block:: text
   :caption: examples/cu_avas.inp

    print,orbitals,civector
    geometry={Cu}
    basis={
    default,vtz
    set,avas
    default,vtz
    sp,cu,vtz;c
    d,cu,vtz
    c,1.8,  0.002646  0.020501  0.082753  0.209939  0.327763  0.345424  0.271188  0.145080 !3d
    c,1.8, -0.003764 -0.029110 -0.121384 -0.314695 -0.384907  0.076640  0.525780  0.337258 !4d
    }
   
    {avas,minao_basis=avas
    center,1,4s,3d,4d}   !generate AVAS starting orbitals for the subsequent CASSCF
    {df-casscf}

.. _automated_construction_of_atomic_valence_active_spaces--avas-within-hf-or-ks:

AVAS within HF or KS
--------------------

In this case the converged HF orbitals are used, and the closed-shell valence orbitals (excluding core orbitals) and virtual orbitals are projected independently, and the active orbitals resulting from these two subspaces are determined. IF ``OPEN=0`` (default in this case) the open-shell orbitals remain unchanged and are subsequently added to the active space. In this way, a CASCI using the generated active space will never give a higher energy than the RHF energy, and according to preliminary experience this yields the best starting orbitals for a subsequent CASSCF calculation. The inactive, active and virtual subspaces are made pseudo-canonical by block-diagonalizing the Fock matrix.

The general input is

``{[DF-]HF;...\\``
``AVAS,options\\``
``CENTER,number,atomic orbital specification\\``
``CENTER,number,atomic orbital specification\\``
...
}
