.. _minimization_of_functions--minimization-of-functions:

Minimization of functions
=========================

The minimization of general functions of one or more variables can be carried out using the command:

``MINIMIZE, func, x$_1$[, x$_2$, x$_3$, …]``

where *func* represents a function of up to 50 variables *x:math:`_1`, x:math:`_2`, …*. Two different optimization methods can be selected as described below which do or do not use numerical derivative information.

The optimization method, as well as finer control over *func*, can be chosen using the ``METHOD`` directive

``METHOD, key [, key1=value, key2=value, …] [minimize:method]``

where *key* defines the optimization method. Valid options for *key* are:

* ``BFGS`` Broyden-Fletcher-Goldfarb-Shanno conjugate gradient method, which uses numerical gradients (default)
* ``SIMPLEX`` Downhill simplex method, which uses only function evaluations

Options to these methods, *key1, key2, …*, are:

* **``VARSCALE``\ =\ *vscale*** Optimization in space of scaled variables.

*vscale=0* no scaling (not recommended)
*vscale=1* optimization in the space of ln(:math:`x`)
*vscale=2* optimization in space of initial value scaling, e.g., :math:`x_1/x_{1i}` (default)

* **``THRESH``\ =\ *thresh*** Required accuracy of either the gradient (BFGS) or parameters (SIMPLEX). The default is :math:`1 \cdot 10^{-4}` for BFGS and :math:`1 \cdot 10^{-2}` for SIMPLEX. Note that previously this pertained to the function value in the Simplex case.
* **``VSTEP``\ =\ *epsd*** Step size for numerical gradients (BFGS) or initial SIMPLEX vertices
* **``PROC``\ =\ *procname*** Specifies the procedure to be executed in each optimization step. This defines a complete function evaluation (if needed, numerical gradients will be evaluated using this procedure as well)
* **``STARTCMD``\ =\ *command*** Specifies a start command. In each optimization step all input beginning with *command* to the current ``MINIMIZE`` is processed.

Miscellaneous directives (separated by semicolons or linebreaks)

* **``MAXIT``,\ *maxit*** maximum number of optimization cycles. The default is 30 for BFGS and 100 for SIMPLEX.

.. _minimization_of_functions--examples:

Examples
========

.. _minimization_of_functions--geometry-optimization:

Geometry optimization
=====================

.. code-block:: text
   :caption: examples/min_optgeo.inp

   ***, Simple geometry optimization
   
   basis=vdz
   
   geometry={
   O
   H 1 r
   H 1 r 2 theta}
   
   r=1.8
   theta=104
   
   hf
   mp2
   
   {minimize,energy,r,theta}
   ---

.. _minimization_of_functions--basis-function-optimizations:

Basis function optimizations
============================

.. code-block:: text
   :caption: examples/basisopt_simple.inp

   ***, Optimization of 2 d functions
   
   geometry={Ne}
   
   dexp=[2.0,1.0]
   
   basis={
   sp,Ne,vdz;c;
   d,Ne,dexp(1),dexp(2)
   }
   
   hf
   mp2
   eval=energy
   
   minimize,eval,dexp(1),dexp(2)
   ---

.. code-block:: text
   :caption: examples/basisopt_proc.inp

   ***, Optimization of 2 d functions
   
   geometry={Ne}
   
   dexp=[2.0,1.0]
   
   {minimize,eval,dexp(1),dexp(2)
   method,bfgs,varscale=1,thresh=1e-5,proc=optd}
   
   
   proc optd
   
   basis={
   sp,Ne,vdz;c;
   d,Ne,dexp(1),dexp(2)
   }
   
   hf
   mp2
   eval=energy
   
   endproc

.. code-block:: text
   :caption: examples/basisopt_cv.inp

   ***, MP2 optimization of core-valence cc-pCVDZ functions
   
   geometry={Ne}
   
   sexp=20.
   pexp=30.
   
   {minimize,ecv,sexp,pexp
   method,bfgs,varscale=1,thresh=1e-5,proc=myopt}
   
   
   proc myopt
   
   basis={
   spd,Ne,vdz;c;
   s,Ne,sexp
   p,Ne,pexp
   }
   
   hf
   {mp2;core,1}
   eval=energy
   
   {mp2;core,0}
   eall=energy
   
   ecv=eall-eval
   
   endproc

.. _minimization_of_functions--intersection-points:

Intersection points
===================

.. code-block:: text
   :caption: examples/min_intersect.inp

   ***, Try to find intersection seam of singlet-triplet CH2 as function of angle
   
   basis=vdz
   
   geometry={
   C
   H 1 r
   H 1 r 2 theta}
   
   r=1.6
   angles=[70,75,80,85,90]
   
   do i=1,#angles
   
    theta=angles(i)
   
    {minimize,ediff,r
    method,bfgs,thresh=1e-5,proc=findit}
   
    ropt(i)=r
    eseam(i)=etriplet
    converge(i)=ediff
   
   enddo
   
   table,angles,ropt,eseam,converge
   digit,0,3,5,6
   
   
   proc findit
   
    {hf;wf,8,2,2}
    etriplet=energy
   
    {hf;wf,8,1,0}
    esinglet=energy
   
    ediff=(etriplet-esinglet)**2
   
   endproc
   ---
