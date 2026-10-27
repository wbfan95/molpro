.. _density_functional_descriptions--density-functional-descriptions:

Density functional descriptions
===============================

.. _density_functional_descriptions--b86-xalpha-beta-gamma:

B86: Xalpha beta gamma
======================

Divergence free semiempirical gradient-corrected exchange energy functional. :math:`\lambda=\gamma` in ref.

.. math::

   g=-{\frac {c \left( \rho \left( s \right)  \right) ^{4/3} \left( 1+
   \beta\, \left( \chi \left( s \right)  \right) ^{2} \right) }{1+\lambda
   \, \left( \chi \left( s \right)  \right) ^{2}}}

.. math::

   G=-{\frac {c \left( \rho \left( s \right)  \right) ^{4/3} \left( 1+
   \beta\, \left( \chi \left( s \right)  \right) ^{2} \right) }{1+\lambda
   \, \left( \chi \left( s \right)  \right) ^{2}}}

.. math::

   c=3/8\,\sqrt [3]{3}{4}^{2/3}\sqrt [3]{{\pi }^{-1}}

.. math::

   \beta= 0.0076

.. math::

   \lambda= 0.004

.. _density_functional_descriptions--b86mgc-xalpha-beta-gamma-with-modified-gradient-correction:

B86MGC: Xalpha beta gamma with Modified Gradient Correction
===========================================================

B86 with modified gradient correction for large density gradients.

.. math::

   g=-c \left( \rho \left( s \right)  \right) ^{4/3}-{\frac {\beta\,
    \left( \chi \left( s \right)  \right) ^{2} \left( \rho \left( s
    \right)  \right) ^{4/3}}{ \left( 1+\lambda\, \left( \chi \left( s
    \right)  \right) ^{2} \right) ^{4/5}}}

.. math::

   G=-c \left( \rho \left( s \right)  \right) ^{4/3}-{\frac {\beta\,
    \left( \chi \left( s \right)  \right) ^{2} \left( \rho \left( s
    \right)  \right) ^{4/3}}{ \left( 1+\lambda\, \left( \chi \left( s
    \right)  \right) ^{2} \right) ^{4/5}}}

.. math::

   c=3/8\,\sqrt [3]{3}{4}^{2/3}\sqrt [3]{{\pi }^{-1}}

.. math::

   \beta= 0.00375

.. math::

   \lambda= 0.007

.. _density_functional_descriptions--b86r-xalpha-beta-gamma-re-optimised:

B86R: Xalpha beta gamma Re-optimised
====================================

Re-optimised :math:`\beta` of B86 used in part 3 of Becke’s 1997 paper.

.. math::

   g=-{\frac {c \left( \rho \left( s \right)  \right) ^{4/3} \left( 1+
   \beta\, \left( \chi \left( s \right)  \right) ^{2} \right) }{1+\lambda
   \, \left( \chi \left( s \right)  \right) ^{2}}}

.. math::

   G=-{\frac {c \left( \rho \left( s \right)  \right) ^{4/3} \left( 1+
   \beta\, \left( \chi \left( s \right)  \right) ^{2} \right) }{1+\lambda
   \, \left( \chi \left( s \right)  \right) ^{2}}}

.. math::

   c=3/8\,\sqrt [3]{3}{4}^{2/3}\sqrt [3]{{\pi }^{-1}}

.. math::

   \beta= 0.00787

.. math::

   \lambda= 0.004

.. _density_functional_descriptions--b88-becke-1988-exchange-functional:

B88: Becke 1988 Exchange Functional
===================================

.. math::

   G=- \left( \rho \left( s \right)  \right) ^{4/3} \left( c+{\frac {\beta
   \, \left( \chi \left( s \right)  \right) ^{2}}{1+6\,\beta\,\chi \left(
   s \right) {\it arcsinh} \left( \chi \left( s \right)  \right) }}
    \right)

.. math::

   g=- \left( \rho \left( s \right)  \right) ^{4/3} \left( c+{\frac {\beta
   \, \left( \chi \left( s \right)  \right) ^{2}}{1+6\,\beta\,\chi \left(
   s \right) {\it arcsinh} \left( \chi \left( s \right)  \right) }}
    \right)

.. math::

   c=3/8\,\sqrt [3]{3}{4}^{2/3}\sqrt [3]{{\pi }^{-1}}

.. math::

   \beta= 0.0042

.. _density_functional_descriptions--b88c-becke-1988-correlation-functional:

B88C: Becke 1988 Correlation Functional
=======================================

Correlation functional depending on B86MGC exchange functional with empirical atomic parameters, :math:`t` and :math:`u`. The exchange functional that is used in conjunction with B88C should replace B88MGC here.

.. math::

   f=- 0.8\,\rho \left( a \right) \rho \left( b \right) {q}^{2} \left( 1-{
   \frac {\ln  \left( 1+q \right) }{q}} \right)

.. math::

   q=t \left( x+y \right)

.. math::

   x= 0.5\, \left( c\sqrt [3]{\rho \left( a \right) }+{\frac {\beta\,
    \left( \chi \left( a \right)  \right) ^{2}\sqrt [3]{\rho \left( a
    \right) }}{ \left( 1+\lambda\, \left( \chi \left( a \right)  \right) ^
   {2} \right) ^{4/5}}} \right) ^{-1}

.. math::

   y= 0.5\, \left( c\sqrt [3]{\rho \left( b \right) }+{\frac {\beta\,
    \left( \chi \left( b \right)  \right) ^{2}\sqrt [3]{\rho \left( b
    \right) }}{ \left( 1+\lambda\, \left( \chi \left( b \right)  \right) ^
   {2} \right) ^{4/5}}} \right) ^{-1}

.. math::

   t= 0.63

.. math::

   g=- 0.01\,\rho \left( s \right) d{z}^{4} \left( 1-2\,{\frac {\ln
    \left( 1+1/2\,z \right) }{z}} \right)

.. math::

   z=2\,ur

.. math::

   r= 0.5\,\rho \left( s \right)  \left( c \left( \rho \left( s \right)
    \right) ^{4/3}+{\frac {\beta\, \left( \chi \left( s \right)  \right) ^
   {2} \left( \rho \left( s \right)  \right) ^{4/3}}{ \left( 1+\lambda\,
    \left( \chi \left( s \right)  \right) ^{2} \right) ^{4/5}}} \right) ^{
   -1}

.. math::

   u= 0.96

.. math::

   d=\tau \left( s \right) -1/4\,{\frac {\sigma \left( {\it ss} \right) }{
   \rho \left( s \right) }}

.. math::

   G=- 0.01\,\rho \left( s \right) d{z}^{4} \left( 1-2\,{\frac {\ln
    \left( 1+1/2\,z \right) }{z}} \right)

.. math::

   c=3/8\,\sqrt [3]{3}{4}^{2/3}\sqrt [3]{{\pi }^{-1}}

.. math::

   \beta= 0.00375

.. math::

   \lambda= 0.007

.. _density_functional_descriptions--b95-becke-1995-correlation-functional:

B95: Becke 1995 Correlation Functional
======================================

:math:`tau` dependent Dynamical correlation functional.

.. math::

   T=[ 0.031091, 0.015545, 0.016887]

.. math::

   U=[ 0.21370, 0.20548, 0.11125]

.. math::

   V=[ 7.5957, 14.1189, 10.357]

.. math::

   W=[ 3.5876, 6.1977, 3.6231]

.. math::

   X=[ 1.6382, 3.3662, 0.88026]

.. math::

   Y=[ 0.49294, 0.62517, 0.49671]

.. math::

   P=[1,1,1]

.. math::

   f={\frac {E}{1+l \left(  \left( \chi \left( a \right)  \right) ^{2}+
    \left( \chi \left( b \right)  \right) ^{2} \right) }}

.. math::

   g={\frac {F\epsilon \left( \rho \left( s \right) ,0 \right) }{H \left(
   1+\nu\, \left( \chi \left( s \right)  \right) ^{2} \right) ^{2}}}

.. math::

   G={\frac {F\epsilon \left( \rho \left( s \right) ,0 \right) }{H \left(
   1+\nu\, \left( \chi \left( s \right)  \right) ^{2} \right) ^{2}}}

.. math::

   E=\epsilon \left( \rho \left( a \right) ,\rho \left( b \right)
    \right) -\epsilon \left( \rho \left( a \right) ,0 \right) -\epsilon
    \left( \rho \left( b \right) ,0 \right)

.. math::

   l= 0.0031

.. math::

   F=\tau \left( s \right) -1/4\,{\frac {\sigma \left( {\it ss} \right) }{
   \rho \left( s \right) }}

.. math::

   H=3/5\,{6}^{2/3} \left( {\pi }^{2} \right) ^{2/3} \left( \rho \left( s
    \right)  \right) ^{5/3}

.. math::

   \nu= 0.038

.. math::

   \epsilon \left( \alpha,\beta \right) = \left( \alpha+\beta \right)
    \left( e \left( r \left( \alpha,\beta \right) ,T_{{1}},U_{{1}},V_{{1}}
   ,W_{{1}},X_{{1}},Y_{{1}},P_{{1}} \right) -{\frac {e \left( r \left(
   \alpha,\beta \right) ,T_{{3}},U_{{3}},V_{{3}},W_{{3}},X_{{3}},Y_{{3}},P
   _{{3}} \right) \omega \left( \zeta \left( \alpha,\beta \right)
    \right)  \left( 1- \left( \zeta \left( \alpha,\beta \right)  \right) ^
   {4} \right) }{c}}+ \left( e \left( r \left( \alpha,\beta \right) ,T_{{2
   }},U_{{2}},V_{{2}},W_{{2}},X_{{2}},Y_{{2}},P_{{2}} \right) -e \left( r
    \left( \alpha,\beta \right) ,T_{{1}},U_{{1}},V_{{1}},W_{{1}},X_{{1}},Y
   _{{1}},P_{{1}} \right)  \right) \omega \left( \zeta \left( \alpha,\beta
    \right)  \right)  \left( \zeta \left( \alpha,\beta \right)  \right) ^{
   4} \right)

.. math::

   r \left( \alpha,\beta \right) =1/4\,\sqrt [3]{3}{4}^{2/3}\sqrt [3]{{
   \frac {1}{\pi \, \left( \alpha+\beta \right) }}}

.. math::

   \zeta \left( \alpha,\beta \right) ={\frac {\alpha-\beta}{\alpha+\beta}}

.. math::

   \omega \left( z \right) ={\frac { \left( 1+z \right) ^{4/3}+ \left( 1-z
    \right) ^{4/3}-2}{2\,\sqrt [3]{2}-2}}

.. math::

   e \left( r,t,u,v,w,x,y,p \right) =-2\,t \left( 1+ur \right) \ln
    \left( 1+1/2\,{\frac {1}{t \left( v\sqrt {r}+wr+x{r}^{3/2}+y{r}^{p+1}
    \right) }} \right)

.. math::

   c= 1.709921

.. _density_functional_descriptions--b97df-density-functional-part-of-b97:

B97DF: Density functional part of B97
=====================================

This functional needs to be mixed with 0.1943\*exact exchange.

.. math::

   T=[ 0.031091, 0.015545, 0.016887]

.. math::

   U=[ 0.21370, 0.20548, 0.11125]

.. math::

   V=[ 7.5957, 14.1189, 10.357]

.. math::

   W=[ 3.5876, 6.1977, 3.6231]

.. math::

   X=[ 1.6382, 3.3662, 0.88026]

.. math::

   Y=[ 0.49294, 0.62517, 0.49671]

.. math::

   P=[1,1,1]

.. math::

   A=[ 0.9454, 0.7471,- 4.5961]

.. math::

   B=[ 0.1737, 2.3487,- 2.4868]

.. math::

   C=[ 0.8094, 0.5073, 0.7481]

.. math::

   \lambda=[ 0.006, 0.2, 0.004]

.. math::

   d=1/2\, \left( \chi \left( a \right)  \right) ^{2}+1/2\, \left( \chi
    \left( b \right)  \right) ^{2}

.. math::

   f= \left( \epsilon \left( \rho \left( a \right) ,\rho \left( b \right)
    \right) -\epsilon \left( \rho \left( a \right) ,0 \right) -\epsilon
    \left( \rho \left( b \right) ,0 \right)  \right)  \left( A_{{0}}+A_{{1
   }}\eta \left( d,\lambda_{{1}} \right) +A_{{2}} \left( \eta \left( d,
   \lambda_{{1}} \right)  \right) ^{2} \right)

.. math::

   \eta \left( \theta,\mu \right) ={\frac {\mu\,\theta}{1+\mu\,\theta}}

.. math::

   g=\epsilon \left( \rho \left( s \right) ,0 \right)  \left( B_{{0}}+B_{{
   1}}\eta \left(  \left( \chi \left( s \right)  \right) ^{2},\lambda_{{2}
   } \right) +B_{{2}} \left( \eta \left(  \left( \chi \left( s \right)
    \right) ^{2},\lambda_{{2}} \right)  \right) ^{2} \right) -3/8\,\sqrt [
   3]{3}{4}^{2/3}\sqrt [3]{{\pi }^{-1}} \left( \rho \left( s \right)
    \right) ^{4/3} \left( C_{{0}}+C_{{1}}\eta \left(  \left( \chi \left( s
    \right)  \right) ^{2},\lambda_{{3}} \right) +C_{{2}} \left( \eta
    \left(  \left( \chi \left( s \right)  \right) ^{2},\lambda_{{3}}
    \right)  \right) ^{2} \right)

.. math::

   G=\epsilon \left( \rho \left( s \right) ,0 \right)  \left( B_{{0}}+B_{{
   1}}\eta \left(  \left( \chi \left( s \right)  \right) ^{2},\lambda_{{2}
   } \right) +B_{{2}} \left( \eta \left(  \left( \chi \left( s \right)
    \right) ^{2},\lambda_{{2}} \right)  \right) ^{2} \right) -3/8\,\sqrt [
   3]{3}{4}^{2/3}\sqrt [3]{{\pi }^{-1}} \left( \rho \left( s \right)
    \right) ^{4/3} \left( C_{{0}}+C_{{1}}\eta \left(  \left( \chi \left( s
    \right)  \right) ^{2},\lambda_{{3}} \right) +C_{{2}} \left( \eta
    \left(  \left( \chi \left( s \right)  \right) ^{2},\lambda_{{3}}
    \right)  \right) ^{2} \right)

.. math::

   \epsilon \left( \alpha,\beta \right) = \left( \alpha+\beta \right)
    \left( e \left( r \left( \alpha,\beta \right) ,T_{{1}},U_{{1}},V_{{1}}
   ,W_{{1}},X_{{1}},Y_{{1}},P_{{1}} \right) -{\frac {e \left( r \left(
   \alpha,\beta \right) ,T_{{3}},U_{{3}},V_{{3}},W_{{3}},X_{{3}},Y_{{3}},P
   _{{3}} \right) \omega \left( \zeta \left( \alpha,\beta \right)
    \right)  \left( 1- \left( \zeta \left( \alpha,\beta \right)  \right) ^
   {4} \right) }{c}}+ \left( e \left( r \left( \alpha,\beta \right) ,T_{{2
   }},U_{{2}},V_{{2}},W_{{2}},X_{{2}},Y_{{2}},P_{{2}} \right) -e \left( r
    \left( \alpha,\beta \right) ,T_{{1}},U_{{1}},V_{{1}},W_{{1}},X_{{1}},Y
   _{{1}},P_{{1}} \right)  \right) \omega \left( \zeta \left( \alpha,\beta
    \right)  \right)  \left( \zeta \left( \alpha,\beta \right)  \right) ^{
   4} \right)

.. math::

   r \left( \alpha,\beta \right) =1/4\,\sqrt [3]{3}{4}^{2/3}\sqrt [3]{{
   \frac {1}{\pi \, \left( \alpha+\beta \right) }}}

.. math::

   \zeta \left( \alpha,\beta \right) ={\frac {\alpha-\beta}{\alpha+\beta}}

.. math::

   \omega \left( z \right) ={\frac { \left( 1+z \right) ^{4/3}+ \left( 1-z
    \right) ^{4/3}-2}{2\,\sqrt [3]{2}-2}}

.. math::

   e \left( r,t,u,v,w,x,y,p \right) =-2\,t \left( 1+ur \right) \ln
    \left( 1+1/2\,{\frac {1}{t \left( v\sqrt {r}+wr+x{r}^{3/2}+y{r}^{p+1}
    \right) }} \right)

.. math::

   c= 1.709921

.. _density_functional_descriptions--b97rdf-density-functional-part-of-b97-re-parameterized-by-hamprecht-et-al:

B97RDF: Density functional part of B97 Re-parameterized by Hamprecht et al
==========================================================================

Re-parameterization of the B97 functional in a self-consistent procedure by Hamprecht et al. This functional needs to be mixed with 0.21\*exact exchange.

.. math::

   T=[ 0.031091, 0.015545, 0.016887]

.. math::

   U=[ 0.21370, 0.20548, 0.11125]

.. math::

   V=[ 7.5957, 14.1189, 10.357]

.. math::

   W=[ 3.5876, 6.1977, 3.6231]

.. math::

   X=[ 1.6382, 3.3662, 0.88026]

.. math::

   Y=[ 0.49294, 0.62517, 0.49671]

.. math::

   P=[1,1,1]

.. math::

   A=[ 0.955689, 0.788552,- 5.47869]

.. math::

   B=[ 0.0820011, 2.71681,- 2.87103]

.. math::

   C=[ 0.789518, 0.573805, 0.660975]

.. math::

   \lambda=[ 0.006, 0.2, 0.004]

.. math::

   d=1/2\, \left( \chi \left( a \right)  \right) ^{2}+1/2\, \left( \chi
    \left( b \right)  \right) ^{2}

.. math::

   f= \left( \epsilon \left( \rho \left( a \right) ,\rho \left( b \right)
    \right) -\epsilon \left( \rho \left( a \right) ,0 \right) -\epsilon
    \left( \rho \left( b \right) ,0 \right)  \right)  \left( A_{{0}}+A_{{1
   }}\eta \left( d,\lambda_{{1}} \right) +A_{{2}} \left( \eta \left( d,
   \lambda_{{1}} \right)  \right) ^{2} \right)

.. math::

   \eta \left( \theta,\mu \right) ={\frac {\mu\,\theta}{1+\mu\,\theta}}

.. math::

   g=\epsilon \left( \rho \left( s \right) ,0 \right)  \left( B_{{0}}+B_{{
   1}}\eta \left(  \left( \chi \left( s \right)  \right) ^{2},\lambda_{{2}
   } \right) +B_{{2}} \left( \eta \left(  \left( \chi \left( s \right)
    \right) ^{2},\lambda_{{2}} \right)  \right) ^{2} \right) -3/8\,\sqrt [
   3]{3}{4}^{2/3}\sqrt [3]{{\pi }^{-1}} \left( \rho \left( s \right)
    \right) ^{4/3} \left( C_{{0}}+C_{{1}}\eta \left(  \left( \chi \left( s
    \right)  \right) ^{2},\lambda_{{3}} \right) +C_{{2}} \left( \eta
    \left(  \left( \chi \left( s \right)  \right) ^{2},\lambda_{{3}}
    \right)  \right) ^{2} \right)

.. math::

   G=\epsilon \left( \rho \left( s \right) ,0 \right)  \left( B_{{0}}+B_{{
   1}}\eta \left(  \left( \chi \left( s \right)  \right) ^{2},\lambda_{{2}
   } \right) +B_{{2}} \left( \eta \left(  \left( \chi \left( s \right)
    \right) ^{2},\lambda_{{2}} \right)  \right) ^{2} \right) -3/8\,\sqrt [
   3]{3}{4}^{2/3}\sqrt [3]{{\pi }^{-1}} \left( \rho \left( s \right)
    \right) ^{4/3} \left( C_{{0}}+C_{{1}}\eta \left(  \left( \chi \left( s
    \right)  \right) ^{2},\lambda_{{3}} \right) +C_{{2}} \left( \eta
    \left(  \left( \chi \left( s \right)  \right) ^{2},\lambda_{{3}}
    \right)  \right) ^{2} \right)

.. math::

   \epsilon \left( \alpha,\beta \right) = \left( \alpha+\beta \right)
    \left( e \left( r \left( \alpha,\beta \right) ,T_{{1}},U_{{1}},V_{{1}}
   ,W_{{1}},X_{{1}},Y_{{1}},P_{{1}} \right) -{\frac {e \left( r \left(
   \alpha,\beta \right) ,T_{{3}},U_{{3}},V_{{3}},W_{{3}},X_{{3}},Y_{{3}},P
   _{{3}} \right) \omega \left( \zeta \left( \alpha,\beta \right)
    \right)  \left( 1- \left( \zeta \left( \alpha,\beta \right)  \right) ^
   {4} \right) }{c}}+ \left( e \left( r \left( \alpha,\beta \right) ,T_{{2
   }},U_{{2}},V_{{2}},W_{{2}},X_{{2}},Y_{{2}},P_{{2}} \right) -e \left( r
    \left( \alpha,\beta \right) ,T_{{1}},U_{{1}},V_{{1}},W_{{1}},X_{{1}},Y
   _{{1}},P_{{1}} \right)  \right) \omega \left( \zeta \left( \alpha,\beta
    \right)  \right)  \left( \zeta \left( \alpha,\beta \right)  \right) ^{
   4} \right)

.. math::

   r \left( \alpha,\beta \right) =1/4\,\sqrt [3]{3}{4}^{2/3}\sqrt [3]{{
   \frac {1}{\pi \, \left( \alpha+\beta \right) }}}

.. math::

   \zeta \left( \alpha,\beta \right) ={\frac {\alpha-\beta}{\alpha+\beta}}

.. math::

   \omega \left( z \right) ={\frac { \left( 1+z \right) ^{4/3}+ \left( 1-z
    \right) ^{4/3}-2}{2\,\sqrt [3]{2}-2}}

.. math::

   e \left( r,t,u,v,w,x,y,p \right) =-2\,t \left( 1+ur \right) \ln
    \left( 1+1/2\,{\frac {1}{t \left( v\sqrt {r}+wr+x{r}^{3/2}+y{r}^{p+1}
    \right) }} \right)

.. math::

   c= 1.709921

.. _density_functional_descriptions--br-becke-roussel-exchange-functional:

BR: Becke-Roussel Exchange Functional
=====================================

A. D. Becke and M. R. Roussel,\ `Phys. Rev. A <https://dx.doi.org/10.1103/PhysRevA.39.3761>`__ **39**, 3761 (1989)

.. math::

   K=\frac{1}{2}\sum_s \rho_s U_s

where

.. math::

   U_s=-(1-e^{-x}-xe^{-x}/2)/b

.. math::

   b=\frac{x^3e^{-x}}{8\pi\rho_s}

and :math:`x` is defined by the nonlinear equation

.. math::

   \frac{xe^{-2x/3}}{x-2}=\frac{2\pi^{2/3}\rho_s^{5/3}}{3Q_s}

where

.. math::

   Q_s=(\upsilon_s-2\gamma D_s)/6

.. math::

   D_s=\tau_s-\frac{\sigma_{ss}}{4\rho_s}

and

.. math::

   \gamma=1.

.. _density_functional_descriptions--brueg-becke-roussel-exchange-functional-uniform-electron-gas-limit:

BRUEG: Becke-Roussel Exchange Functional — Uniform Electron Gas Limit
=====================================================================

A. D. Becke and M. R. Roussel,\ `Phys. Rev. A <https://dx.doi.org/10.1103/PhysRevA.39.3761>`__ **39**, 3761 (1989)

As for ``BR`` but with :math:`{\gamma=0.8}`.

.. _density_functional_descriptions--bw-becke-wigner-exchange-correlation-functional:

BW: Becke-Wigner Exchange-Correlation Functional
================================================

Hybrid exchange-correlation functional comprising Becke’s 1998 exchange and Wigner’s spin-polarised correlation functionals.

.. math::

   \alpha=-3/8\,\sqrt [3]{3}{4}^{2/3}\sqrt [3]{{\pi }^{-1}}

.. math::

   g=\alpha\, \left( \rho \left( s \right)  \right) ^{4/3}-{\frac {\beta\,
    \left( \rho \left( s \right)  \right) ^{4/3} \left( \chi \left( s
    \right)  \right) ^{2}}{1+6\,\beta\,\chi \left( s \right) {\it arcsinh}
    \left( \chi \left( s \right)  \right) }}

.. math::

   G=\alpha\, \left( \rho \left( s \right)  \right) ^{4/3}-{\frac {\beta\,
    \left( \rho \left( s \right)  \right) ^{4/3} \left( \chi \left( s
    \right)  \right) ^{2}}{1+6\,\beta\,\chi \left( s \right) {\it arcsinh}
    \left( \chi \left( s \right)  \right) }}

.. math::

   f=-4\,c\rho \left( a \right) \rho \left( b \right) {\rho}^{-1} \left( 1
   +{\frac {d}{\sqrt [3]{\rho}}} \right) ^{-1}

.. math::

   \beta= 0.0042

.. math::

   c= 0.04918

.. math::

   d= 0.349

.. _density_functional_descriptions--cs1-colle-salvetti-correlation-functional:

CS1: Colle-Salvetti correlation functional
==========================================

R. Colle and O. Salvetti, Theor. Chim. Acta 37, 329 (1974); C. Lee, W. Yang and R. G. Parr, `Phys. Rev. B <https://dx.doi.org/10.1103/PhysRevB.37.785>`__ **37**, 785(1988)

``CS1`` is formally identical to ``CS2``, except for a reformulation in which the terms involving :math:`\upsilon` are eliminated by integration by parts. This makes the functional more economical to evaluate. In the limit of exact quadrature, ``CS1`` and ``CS2`` are identical, but small numerical differences appear with finite integration grids.

.. _density_functional_descriptions--cs2-colle-salvetti-correlation-functional:

CS2: Colle-Salvetti correlation functional
==========================================

R. Colle and O. Salvetti, Theor. Chim. Acta 37, 329 (1974); C. Lee, W. Yang and R. G. Parr, `Phys. Rev. B <https://dx.doi.org/10.1103/PhysRevB.37.785>`__ **37**, 785(1988)

``CS2`` is defined through

.. math::

   \begin{aligned}
     K &=&
     -a \left({
     \rho+2b\rho^{-5/3}
     \left[
     \rho_\alpha t_{\alpha} + \rho_\beta t_{\beta}
     -\rho t_W
     \right]
     e^{-c\rho^{-1/3}}
     \over 1+d \rho^{-1/3}
     }\right)
     \end{aligned}

where

.. math::

   \begin{aligned}
     t_{\alpha} &=&\frac{\tau_\alpha}{2}-\frac{\upsilon_\alpha}{8}
     \\
     t_{\beta} &=&\frac{\tau_\beta}{2}-\frac{\upsilon_\beta}{8}
     \\
     t_{W} &=& {1\over 8} {\sigma \over \rho} - {1\over 2} \upsilon
     \end{aligned}

and the constants are :math:`a=0.04918, b=0.132, c=0.2533, d=0.349`.

.. _density_functional_descriptions--dirac-slater-dirac-exchange-energy:

DIRAC: Slater-Dirac Exchange Energy
===================================

Automatically generated Slater-Dirac exchange.

.. math::

   g=-c \left( \rho \left( s \right)  \right) ^{4/3}

.. math::

   c=3/8\,\sqrt [3]{3}{4}^{2/3}\sqrt [3]{{\pi }^{-1}}

.. _density_functional_descriptions--ecerf-short-range-lda-correlation-functional:

ECERF: Short-range LDA correlation functional
=============================================

Local-density approximation of correlation energy
for short-range interelectronic interaction :math:`{\rm erf}(\mu r_{21})/r_{12}`,
S. Paziani, S. Moroni, P. Gori-Giorgi, and G. B. Bachelet, `Phys. Rev. B <https://dx.doi.org/10.1103/PhysRevB.73.155111>`__ **73**, 155111 (2006).

.. math::

   \nonumber
   \epsilon_c^{\rm SR}(r_s,\zeta,\mu) =\epsilon_c^{\rm PW92}(r_s,\zeta)-
    \frac{[\phi_2(\zeta)]^3Q\left(\frac{\mu\sqrt{r_s}}{\phi_2(\zeta)}\right)+a_1 \mu^3+a_2 \mu^4+
    a_3\mu^5+a_4\mu^6+a_5\mu^8}{(1+b_0^2\mu^2)^4},

where

.. math::

   Q(x)=\frac{2\ln(2)-2}{\pi^2}\ln\left(\frac{1+a\,x+b\,x^2+c\,x^3}{1+a\,x+
   d\,x^2}\right),

with :math:`a=5.84605`, :math:`c=3.91744`, :math:`d=3.44851`, and :math:`b=d-3\pi\alpha/(4\ln(2)-4)`. The parameters :math:`a_i(r_s,\zeta)` are given by

.. math::

   \begin{aligned}
   a_1 & = & 4 \,b_0^6 \,C_3+b_0^8 \,C_5, \nonumber \\
   a_2 & = & 4 \,b_0^6 \,C_2+b_0^8\, C_4+6\, b_0^4 \epsilon_c^{\rm PW92}, \nonumber \\
   a_3 & = & b_0^8 \,C_3, \nonumber \\
   a_4 & = & b_0^8 \,C_2+4 \,b_0^6\, \epsilon_c^{\rm PW92} \nonumber, \\
   a_5 & = & b_0^8\,\epsilon_c^{\rm PW92}, \nonumber\end{aligned}

with

.. math::

   \begin{aligned}
   C_2 & = & -\frac{3(1\!-\!\zeta^2)\,g_c(0,r_s,\zeta\!=\!0)}{8\,r_s^3} \nonumber \\
   C_3 & = &  - (1\!-\!\zeta^2)\frac{g(0,r_s,\zeta\!=\!0)}{\sqrt{2\pi}\, r_s^3}
   \nonumber \\
   C_4 & = & -\frac{9\, c_4(r_s,\zeta)}{64 r_s^3} \nonumber \\
   C_5 & =  & -\frac{9\, c_5(r_s,\zeta)}{40\sqrt{2 \pi} r_s^3}\nonumber \\
   c_4(r_s,\zeta)
   & = & \left(\frac{1\!+\!\zeta}{2}\right)^2g''\left(0,
   r_s\left(\frac{2}{1\!+\!\zeta}\right)^{1/3}\!\!\!\!\!\!\!\!, \,\,\,\,\,\zeta\!=\!1\right)+ \left(\frac{1\!-\!\zeta}{2}\right)^2 \times \nonumber  \\ & & g''\left(0,
   r_s\left(\frac{2}{1\!-\!\zeta}\right)^{1/3}\!\!\!\!\!\!\!\!, \,\,\,\,\,\zeta\!=\!1\right)
   + (1\!-\!\zeta^2)D_2(r_s)-\frac{\phi_8(\zeta)}{5\,\alpha^2\,r_s^2}
   \nonumber \\
   c_5(r_s,\zeta)
   & = & \left(\frac{1\!+\!\zeta}{2}\right)^2g''\left(0,
   r_s\left(\frac{2}{1\!+\!\zeta}\right)^{1/3}\!\!\!\!\!\!\!\!, \,\,\,\,\,\zeta\!=\!1\right)+
     \left(\frac{1\!-\!\zeta}{2}\right)^2 \times \nonumber \\  & & g''\left(0,
   r_s\left(\frac{2}{1\!-\!\zeta}\right)^{1/3}\!\!\!\!\!\!\!\!, \,\,\,\,\,\zeta\!=\!1\right)+  (1\!-\!\zeta^2)D_3(r_s),\end{aligned}

and

.. math::

   \begin{aligned}
   \phantom{\bigl[} b_0(r_s)  =   0.784949\,r_s  \\
   \phantom{\Biggl[} g''(0,r_s,\zeta\!=\!1)  =   \frac{2^{5/3}}{5\,\alpha^2 \,r_s^2} \,
   \frac{1-0.02267 r_s}{\left(1+0.4319 r_s+0.04 r_s^2\right)} \\
   \phantom{\Biggl[}D_2(r_s)  =  \frac{e^{-  0.547 r_s}}{r_s^2}\left(-0.388 r_s+0.676 r_s^2\right) \\
   \phantom{\Biggl[}D_3(r_s)  =  \frac{e^{-0.31 r_s}}{r_s^3}\left(-4.95 r_s+ r_s^2\right).\end{aligned}

Finally, :math:`\epsilon_c^{\rm PW92}(r_s,\zeta)` is the Perdew-Wang parametrization of the correlation energy of the standard uniform electron gas [J.P. Perdew and Y. Wang, `Phys. Rev. B <https://dx.doi.org/10.1103/PhysRevB.45.13244>`__ **45**, 13244 (1992)], and

.. math::

   g(0,r_s,\zeta\!=\!0)=\frac{1}{2}(1-Br_s+Cr_s^2+Dr_s^3+Er_s^4)\,{\rm e}^{-dr_s},

is the on-top pair-distribution function of the standard jellium model [P. Gori-Giorgi and J.P. Perdew, `Phys. Rev. B <https://dx.doi.org/10.1103/PhysRevB.64.155102>`__ **64**, 155102 (2001)], where :math:`B=-0.0207`, :math:`C=0.08193`, :math:`D=-0.01277`, :math:`E=0.001859`, :math:`d=0.7524`. The correlation part of the on-top pair-distribution function is :math:`g_c(0,r_s,\zeta\!=\!0)=g(0,r_s,\zeta\!=\!0)-\frac{1}{2}`.

.. _density_functional_descriptions--ecerfpbe-range-separated-correlation-functional:

ECERFPBE: Range-Separated Correlation Functional
================================================

Toulouse-Colonna-Savin range-separated correlation functional based on PBE, see J. Toulouse et al., `J. Chem. Phys. <https://dx.doi.org/10.1063/1.1824896>`__ **122**, 014110 (2005).

.. _density_functional_descriptions--exact-exact-exchange-functional:

EXACT: Exact Exchange Functional
================================

Hartree-Fock exact exchange functional can be used to construct hybrid exchange-correlation functional.

.. _density_functional_descriptions--exerf-short-range-lda-correlation-functional:

EXERF: Short-range LDA correlation functional
=============================================

Local-density approximation of exchange energy
for short-range interelectronic interaction :math:`{\rm erf}(\mu r_{12})/r_{12}`,
A. Savin, in Recent Developments and Applications of Modern Density Functional Theory, edited by J.M. Seminario (Elsevier, Amsterdam, 1996).

.. math::

   \epsilon_x^{\rm SR}(r_s,\zeta,\mu)  = \frac{3}{4\pi}\frac{\phi_4(\zeta)}{\alpha\,r_s}- \frac{1}{2}(1\!+\!\zeta)^{4/3}
   f_x\left(r_s,\mu(1\!+\!\zeta)^{-1/3}\right)+\frac{1}{2}(1\!-\!\zeta)^{4/3}
   f_x\left(r_s,\mu(1\!-\!\zeta)^{-1/3}\right)       \nonumber

with

.. math::

   \phi_n(\zeta)=\frac{1}{2}\left[ (1\!+\!\zeta)^{n/3}+(1\!-\!\zeta)^{n/3} \right],

.. math::

   f_x(r_s,\mu) =  -\frac{\mu}{\pi}\biggl[(2y-4y^3)\,e^{-1/4y^2}-
   3y+4y^3+ \sqrt{\pi}\,{\rm erf}\left(\frac{1}{2y}\right)\biggr],
   \qquad y=\frac{\mu\,\alpha\,r_s}{2},

and :math:`\alpha=(4/9\pi)^{1/3}`.

.. _density_functional_descriptions--exerfpbe-range-separated-exchange-functional:

EXERFPBE: Range-Separated Exchange Functional
=============================================

Toulouse-Colonna-Savin range-separated exchange functional based on PBE, see J. Toulouse et al., `J. Chem. Phys. <https://dx.doi.org/10.1063/1.1824896>`__ **122**, 014110 (2005).

.. _density_functional_descriptions--g96-gill-s-1996-gradient-corrected-exchange-functional:

G96: Gill’s 1996 Gradient Corrected Exchange Functional
=======================================================

.. math::

   \alpha=-3/8\,\sqrt [3]{3}{4}^{2/3}\sqrt [3]{{\pi }^{-1}}

.. math::

   g= \left( \rho \left( s \right)  \right) ^{4/3} \left( \alpha-{\frac {1
   }{137}}\, \left( \chi \left( s \right)  \right) ^{3/2} \right)

.. math::

   G= \left( \rho \left( s \right)  \right) ^{4/3} \left( \alpha-{\frac {1
   }{137}}\, \left( \chi \left( s \right)  \right) ^{3/2} \right)

.. _density_functional_descriptions--hcth120-handy-least-squares-fitted-functional:

HCTH120: Handy least squares fitted functional
==============================================

.. math::

   T=[ 0.031091, 0.015545, 0.016887]

.. math::

   U=[ 0.21370, 0.20548, 0.11125]

.. math::

   V=[ 7.5957, 14.1189, 10.357]

.. math::

   W=[ 3.5876, 6.1977, 3.6231]

.. math::

   X=[ 1.6382, 3.3662, 0.88026]

.. math::

   Y=[ 0.49294, 0.62517, 0.49671]

.. math::

   P=[1,1,1]

.. math::

   A=[ 0.51473, 6.9298,- 24.707, 23.110,- 11.323]

.. math::

   B=[ 0.48951,- 0.2607, 0.4329,- 1.9925, 2.4853]

.. math::

   C=[ 1.09163,- 0.7472, 5.0783,- 4.1075, 1.1717]

.. math::

   \lambda=[ 0.006, 0.2, 0.004]

.. math::

   d=1/2\, \left( \chi \left( a \right)  \right) ^{2}+1/2\, \left( \chi
    \left( b \right)  \right) ^{2}

.. math::

   f= \left( \epsilon \left( \rho \left( a \right) ,\rho \left( b \right)
    \right) -\epsilon \left( \rho \left( a \right) ,0 \right) -\epsilon
    \left( \rho \left( b \right) ,0 \right)  \right)  \left( A_{{0}}+A_{{1
   }}\eta \left( d,\lambda_{{1}} \right) +A_{{2}} \left( \eta \left( d,
   \lambda_{{1}} \right)  \right) ^{2}+A_{{3}} \left( \eta \left( d,
   \lambda_{{1}} \right)  \right) ^{3}+A_{{4}} \left( \eta \left( d,
   \lambda_{{1}} \right)  \right) ^{4} \right)

.. math::

   \eta \left( \theta,\mu \right) ={\frac {\mu\,\theta}{1+\mu\,\theta}}

.. math::

   g=\epsilon \left( \rho \left( s \right) ,0 \right)  \left( B_{{0}}+B_{{
   1}}\eta \left(  \left( \chi \left( s \right)  \right) ^{2},\lambda_{{2}
   } \right) +B_{{2}} \left( \eta \left(  \left( \chi \left( s \right)
    \right) ^{2},\lambda_{{2}} \right)  \right) ^{2}+B_{{3}} \left( \eta
    \left(  \left( \chi \left( s \right)  \right) ^{2},\lambda_{{2}}
    \right)  \right) ^{3}+B_{{4}} \left( \eta \left(  \left( \chi \left( s
    \right)  \right) ^{2},\lambda_{{2}} \right)  \right) ^{4} \right) -3/8
   \,\sqrt [3]{3}{4}^{2/3}\sqrt [3]{{\pi }^{-1}} \left( \rho \left( s
    \right)  \right) ^{4/3} \left( C_{{0}}+C_{{1}}\eta \left(  \left( \chi
    \left( s \right)  \right) ^{2},\lambda_{{3}} \right) +C_{{2}} \left(
   \eta \left(  \left( \chi \left( s \right)  \right) ^{2},\lambda_{{3}}
    \right)  \right) ^{2}+C_{{3}} \left( \eta \left(  \left( \chi \left( s
    \right)  \right) ^{2},\lambda_{{3}} \right)  \right) ^{3}+C_{{4}}
    \left( \eta \left(  \left( \chi \left( s \right)  \right) ^{2},\lambda
   _{{3}} \right)  \right) ^{4} \right)

.. math::

   \epsilon \left( \alpha,\beta \right) = \left( \alpha+\beta \right)
    \left( e \left( r \left( \alpha,\beta \right) ,T_{{1}},U_{{1}},V_{{1}}
   ,W_{{1}},X_{{1}},Y_{{1}},P_{{1}} \right) -{\frac {e \left( r \left(
   \alpha,\beta \right) ,T_{{3}},U_{{3}},V_{{3}},W_{{3}},X_{{3}},Y_{{3}},P
   _{{3}} \right) \omega \left( \zeta \left( \alpha,\beta \right)
    \right)  \left( 1- \left( \zeta \left( \alpha,\beta \right)  \right) ^
   {4} \right) }{c}}+ \left( e \left( r \left( \alpha,\beta \right) ,T_{{2
   }},U_{{2}},V_{{2}},W_{{2}},X_{{2}},Y_{{2}},P_{{2}} \right) -e \left( r
    \left( \alpha,\beta \right) ,T_{{1}},U_{{1}},V_{{1}},W_{{1}},X_{{1}},Y
   _{{1}},P_{{1}} \right)  \right) \omega \left( \zeta \left( \alpha,\beta
    \right)  \right)  \left( \zeta \left( \alpha,\beta \right)  \right) ^{
   4} \right)

.. math::

   r \left( \alpha,\beta \right) =1/4\,\sqrt [3]{3}{4}^{2/3}\sqrt [3]{{
   \frac {1}{\pi \, \left( \alpha+\beta \right) }}}

.. math::

   \zeta \left( \alpha,\beta \right) ={\frac {\alpha-\beta}{\alpha+\beta}}

.. math::

   \omega \left( z \right) ={\frac { \left( 1+z \right) ^{4/3}+ \left( 1-z
    \right) ^{4/3}-2}{2\,\sqrt [3]{2}-2}}

.. math::

   e \left( r,t,u,v,w,x,y,p \right) =-2\,t \left( 1+ur \right) \ln
    \left( 1+1/2\,{\frac {1}{t \left( v\sqrt {r}+wr+x{r}^{3/2}+y{r}^{p+1}
    \right) }} \right)

.. math::

   c= 1.709921

.. _density_functional_descriptions--hcth147-handy-least-squares-fitted-functional:

HCTH147: Handy least squares fitted functional
==============================================

.. math::

   T=[ 0.031091, 0.015545, 0.016887]

.. math::

   U=[ 0.21370, 0.20548, 0.11125]

.. math::

   V=[ 7.5957, 14.1189, 10.357]

.. math::

   W=[ 3.5876, 6.1977, 3.6231]

.. math::

   X=[ 1.6382, 3.3662, 0.88026]

.. math::

   Y=[ 0.49294, 0.62517, 0.49671]

.. math::

   P=[1,1,1]

.. math::

   A=[ 0.542352, 7.01464,- 28.3822, 35.0329,- 20.4284]

.. math::

   B=[ 0.562576,- 0.0171436,- 1.30636, 1.05747, 0.885429]

.. math::

   C=[ 1.09025,- 0.799194, 5.57212,- 5.86760, 3.04544]

.. math::

   \lambda=[ 0.006, 0.2, 0.004]

.. math::

   d=1/2\, \left( \chi \left( a \right)  \right) ^{2}+1/2\, \left( \chi
    \left( b \right)  \right) ^{2}

.. math::

   f= \left( \epsilon \left( \rho \left( a \right) ,\rho \left( b \right)
    \right) -\epsilon \left( \rho \left( a \right) ,0 \right) -\epsilon
    \left( \rho \left( b \right) ,0 \right)  \right)  \left( A_{{0}}+A_{{1
   }}\eta \left( d,\lambda_{{1}} \right) +A_{{2}} \left( \eta \left( d,
   \lambda_{{1}} \right)  \right) ^{2}+A_{{3}} \left( \eta \left( d,
   \lambda_{{1}} \right)  \right) ^{3}+A_{{4}} \left( \eta \left( d,
   \lambda_{{1}} \right)  \right) ^{4} \right)

.. math::

   \eta \left( \theta,\mu \right) ={\frac {\mu\,\theta}{1+\mu\,\theta}}

.. math::

   g=\epsilon \left( \rho \left( s \right) ,0 \right)  \left( B_{{0}}+B_{{
   1}}\eta \left(  \left( \chi \left( s \right)  \right) ^{2},\lambda_{{2}
   } \right) +B_{{2}} \left( \eta \left(  \left( \chi \left( s \right)
    \right) ^{2},\lambda_{{2}} \right)  \right) ^{2}+B_{{3}} \left( \eta
    \left(  \left( \chi \left( s \right)  \right) ^{2},\lambda_{{2}}
    \right)  \right) ^{3}+B_{{4}} \left( \eta \left(  \left( \chi \left( s
    \right)  \right) ^{2},\lambda_{{2}} \right)  \right) ^{4} \right) -3/8
   \,\sqrt [3]{3}{4}^{2/3}\sqrt [3]{{\pi }^{-1}} \left( \rho \left( s
    \right)  \right) ^{4/3} \left( C_{{0}}+C_{{1}}\eta \left(  \left( \chi
    \left( s \right)  \right) ^{2},\lambda_{{3}} \right) +C_{{2}} \left(
   \eta \left(  \left( \chi \left( s \right)  \right) ^{2},\lambda_{{3}}
    \right)  \right) ^{2}+C_{{3}} \left( \eta \left(  \left( \chi \left( s
    \right)  \right) ^{2},\lambda_{{3}} \right)  \right) ^{3}+C_{{4}}
    \left( \eta \left(  \left( \chi \left( s \right)  \right) ^{2},\lambda
   _{{3}} \right)  \right) ^{4} \right)

.. math::

   \epsilon \left( \alpha,\beta \right) = \left( \alpha+\beta \right)
    \left( e \left( r \left( \alpha,\beta \right) ,T_{{1}},U_{{1}},V_{{1}}
   ,W_{{1}},X_{{1}},Y_{{1}},P_{{1}} \right) +{\frac {e \left( r \left(
   \alpha,\beta \right) ,T_{{3}},U_{{3}},V_{{3}},W_{{3}},X_{{3}},Y_{{3}},P
   _{{3}} \right) \omega \left( \zeta \left( \alpha,\beta \right)
    \right)  \left( 1- \left( \zeta \left( \alpha,\beta \right)  \right) ^
   {4} \right) }{c}}+ \left( e \left( r \left( \alpha,\beta \right) ,T_{{2
   }},U_{{2}},V_{{2}},W_{{2}},X_{{2}},Y_{{2}},P_{{2}} \right) -e \left( r
    \left( \alpha,\beta \right) ,T_{{1}},U_{{1}},V_{{1}},W_{{1}},X_{{1}},Y
   _{{1}},P_{{1}} \right)  \right) \omega \left( \zeta \left( \alpha,\beta
    \right)  \right)  \left( \zeta \left( \alpha,\beta \right)  \right) ^{
   4} \right)

.. math::

   r \left( \alpha,\beta \right) =1/4\,\sqrt [3]{3}{4}^{2/3}\sqrt [3]{{
   \frac {1}{\pi \, \left( \alpha+\beta \right) }}}

.. math::

   \zeta \left( \alpha,\beta \right) ={\frac {\alpha-\beta}{\alpha+\beta}}

.. math::

   \omega \left( z \right) ={\frac { \left( 1+z \right) ^{4/3}+ \left( 1-z
    \right) ^{4/3}-2}{2\,\sqrt [3]{2}-2}}

.. math::

   e \left( r,t,u,v,w,x,y,p \right) =-2\,t \left( 1+ur \right) \ln
    \left( 1+1/2\,{\frac {1}{t \left( v\sqrt {r}+wr+x{r}^{3/2}+y{r}^{p+1}
    \right) }} \right)

.. math::

   c= 1.709921

.. _density_functional_descriptions--hcth93-handy-least-squares-fitted-functional:

HCTH93: Handy least squares fitted functional
=============================================

.. math::

   T=[ 0.031091, 0.015545, 0.016887]

.. math::

   U=[ 0.21370, 0.20548, 0.11125]

.. math::

   V=[ 7.5957, 14.1189, 10.357]

.. math::

   W=[ 3.5876, 6.1977, 3.6231]

.. math::

   X=[ 1.6382, 3.3662, 0.88026]

.. math::

   Y=[ 0.49294, 0.62517, 0.49671]

.. math::

   P=[1,1,1]

.. math::

   A=[ 0.72997, 3.35287,- 11.543, 8.08564,- 4.47857]

.. math::

   B=[ 0.222601,- 0.0338622,- 0.012517,- 0.802496, 1.55396]

.. math::

   C=[ 1.0932,- 0.744056, 5.5992,- 6.78549, 4.49357]

.. math::

   \lambda=[ 0.006, 0.2, 0.004]

.. math::

   d=1/2\, \left( \chi \left( a \right)  \right) ^{2}+1/2\, \left( \chi
    \left( b \right)  \right) ^{2}

.. math::

   f= \left( \epsilon \left( \rho \left( a \right) ,\rho \left( b \right)
    \right) -\epsilon \left( \rho \left( a \right) ,0 \right) -\epsilon
    \left( \rho \left( b \right) ,0 \right)  \right)  \left( A_{{0}}+A_{{1
   }}\eta \left( d,\lambda_{{1}} \right) +A_{{2}} \left( \eta \left( d,
   \lambda_{{1}} \right)  \right) ^{2}+A_{{3}} \left( \eta \left( d,
   \lambda_{{1}} \right)  \right) ^{3}+A_{{4}} \left( \eta \left( d,
   \lambda_{{1}} \right)  \right) ^{4} \right)

.. math::

   \eta \left( \theta,\mu \right) ={\frac {\mu\,\theta}{1+\mu\,\theta}}

.. math::

   g=\epsilon \left( \rho \left( s \right) ,0 \right)  \left( B_{{0}}+B_{{
   1}}\eta \left(  \left( \chi \left( s \right)  \right) ^{2},\lambda_{{2}
   } \right) +B_{{2}} \left( \eta \left(  \left( \chi \left( s \right)
    \right) ^{2},\lambda_{{2}} \right)  \right) ^{2}+B_{{3}} \left( \eta
    \left(  \left( \chi \left( s \right)  \right) ^{2},\lambda_{{2}}
    \right)  \right) ^{3}+B_{{4}} \left( \eta \left(  \left( \chi \left( s
    \right)  \right) ^{2},\lambda_{{2}} \right)  \right) ^{4} \right) -3/8
   \,\sqrt [3]{3}{4}^{2/3}\sqrt [3]{{\pi }^{-1}} \left( \rho \left( s
    \right)  \right) ^{4/3} \left( C_{{0}}+C_{{1}}\eta \left(  \left( \chi
    \left( s \right)  \right) ^{2},\lambda_{{3}} \right) +C_{{2}} \left(
   \eta \left(  \left( \chi \left( s \right)  \right) ^{2},\lambda_{{3}}
    \right)  \right) ^{2}+C_{{3}} \left( \eta \left(  \left( \chi \left( s
    \right)  \right) ^{2},\lambda_{{3}} \right)  \right) ^{3}+C_{{4}}
    \left( \eta \left(  \left( \chi \left( s \right)  \right) ^{2},\lambda
   _{{3}} \right)  \right) ^{4} \right)

.. math::

   \epsilon \left( \alpha,\beta \right) = \left( \alpha+\beta \right)
    \left( e \left( r \left( \alpha,\beta \right) ,T_{{1}},U_{{1}},V_{{1}}
   ,W_{{1}},X_{{1}},Y_{{1}},P_{{1}} \right) -{\frac {e \left( r \left(
   \alpha,\beta \right) ,T_{{3}},U_{{3}},V_{{3}},W_{{3}},X_{{3}},Y_{{3}},P
   _{{3}} \right) \omega \left( \zeta \left( \alpha,\beta \right)
    \right)  \left( 1- \left( \zeta \left( \alpha,\beta \right)  \right) ^
   {4} \right) }{c}}+ \left( e \left( r \left( \alpha,\beta \right) ,T_{{2
   }},U_{{2}},V_{{2}},W_{{2}},X_{{2}},Y_{{2}},P_{{2}} \right) -e \left( r
    \left( \alpha,\beta \right) ,T_{{1}},U_{{1}},V_{{1}},W_{{1}},X_{{1}},Y
   _{{1}},P_{{1}} \right)  \right) \omega \left( \zeta \left( \alpha,\beta
    \right)  \right)  \left( \zeta \left( \alpha,\beta \right)  \right) ^{
   4} \right)

.. math::

   r \left( \alpha,\beta \right) =1/4\,\sqrt [3]{3}{4}^{2/3}\sqrt [3]{{
   \frac {1}{\pi \, \left( \alpha+\beta \right) }}}

.. math::

   \zeta \left( \alpha,\beta \right) ={\frac {\alpha-\beta}{\alpha+\beta}}

.. math::

   \omega \left( z \right) ={\frac { \left( 1+z \right) ^{4/3}+ \left( 1-z
    \right) ^{4/3}-2}{2\,\sqrt [3]{2}-2}}

.. math::

   e \left( r,t,u,v,w,x,y,p \right) =-2\,t \left( 1+ur \right) \ln
    \left( 1+1/2\,{\frac {1}{t \left( v\sqrt {r}+wr+x{r}^{3/2}+y{r}^{p+1}
    \right) }} \right)

.. math::

   c= 1.709921

.. _density_functional_descriptions--hjswpbex-meta-gga-correlation-functional:

HJSWPBEX: Meta GGA Correlation Functional
=========================================

Henderson-Janesko-Scuseria range-separated exchange functional based on a model of an exchange hole derived by a constraint-satisfaction technique, see T. M. Henderson et al., `J. Chem. Phys. <https://dx.doi.org/10.1063/1.2921797>`__ **128**, 194105 (2008).

.. _density_functional_descriptions--lta-local-tau-approximation:

LTA: Local tau Approximation
============================

LSDA exchange functional with density represented as a function of :math:`\tau`.

.. math::

   g=1/2\,E \left( 2\,\tau \left( s \right)  \right)

.. math::

   E \left( \alpha \right) =1/9\,c{5}^{4/5}\sqrt [5]{9} \left( {\frac {
   \alpha\,\sqrt [3]{3}}{ \left( {\pi }^{2} \right) ^{2/3}}} \right) ^{4/5
   }

.. math::

   c=-3/4\,\sqrt [3]{3}\sqrt [3]{{\pi }^{-1}}

.. math::

   G=1/2\,E \left( 2\,\tau \left( s \right)  \right)

.. _density_functional_descriptions--lyp-lee-yang-and-parr-correlation-functional:

LYP: Lee, Yang and Parr Correlation Functional
==============================================

C. Lee, W. Yang and R. G. Parr, `Phys. Rev. B <https://dx.doi.org/10.1103/PhysRevB.37.785>`__ **37**, 785(1988); B. Miehlich, A. Savin, H. Stoll and H. Preuss, `Chem. Phys. Lett. <https://dx.doi.org/10.1016/0009-2614(89)87234-3>`__ **157**, 200 (1989).

.. math::

   f=-4\,A\rho \left( a \right) \rho \left( b \right)  \left( 1+{\frac {d}
   {\sqrt [3]{\rho}}} \right) ^{-1}{\rho}^{-1}-AB\omega\, \left( \rho
    \left( a \right) \rho \left( b \right)  \left( 8\,{2}^{2/3}{\it cf}\,
    \left(  \left( \rho \left( a \right)  \right) ^{8/3}+ \left( \rho
    \left( b \right)  \right) ^{8/3} \right) + \left( {\frac {47}{18}}-{
   \frac {7}{18}}\,\delta \right) \sigma- \left( 5/2-1/18\,\delta \right)
    \left( \sigma \left( {\it aa} \right) +\sigma \left( {\it bb} \right)
    \right) -1/9\, \left( \delta-11 \right)  \left( {\frac {\rho \left( a
    \right) \sigma \left( {\it aa} \right) }{\rho}}+{\frac {\rho \left( b
    \right) \sigma \left( {\it bb} \right) }{\rho}} \right)  \right) -2/3
   \,{\rho}^{2}\sigma+ \left( 2/3\,{\rho}^{2}- \left( \rho \left( a
    \right)  \right) ^{2} \right) \sigma \left( {\it bb} \right) + \left(
   2/3\,{\rho}^{2}- \left( \rho \left( b \right)  \right) ^{2} \right)
   \sigma \left( {\it aa} \right)  \right)

.. math::

   \omega={e^{-{\frac {c}{\sqrt [3]{\rho}}}}}{\rho}^{-11/3} \left( 1+{
   \frac {d}{\sqrt [3]{\rho}}} \right) ^{-1}

.. math::

   \delta={\frac {c}{\sqrt [3]{\rho}}}+d{\frac {1}{\sqrt [3]{\rho}}}
    \left( 1+{\frac {d}{\sqrt [3]{\rho}}} \right) ^{-1}

.. math::

   {\it cf}=3/10\,{3}^{2/3} \left( {\pi }^{2} \right) ^{2/3}

.. math::

   A= 0.04918

.. math::

   B= 0.132

.. math::

   c= 0.2533

.. math::

   d= 0.349

.. _density_functional_descriptions--m052xc-m05-2x-meta-gga-correlation-functional:

M052XC: M05-2X Meta-GGA Correlation Functional
==============================================

.. math::

   T=[ 0.031091, 0.015545, 0.016887]

.. math::

   U=[ 0.21370, 0.20548, 0.11125]

.. math::

   V=[ 7.5957, 14.1189, 10.357]

.. math::

   W=[ 3.5876, 6.1977, 3.6231]

.. math::

   X=[ 1.6382, 3.3662, 0.88026]

.. math::

   Y=[ 0.49294, 0.62517, 0.49671]

.. math::

   P=[1,1,1]

.. math::

   \epsilon \left( \alpha,\beta \right) = \left( \alpha+\beta \right)
    \left( e \left( r \left( \alpha,\beta \right) ,T_{{1}},U_{{1}},V_{{1}}
   ,W_{{1}},X_{{1}},Y_{{1}},P_{{1}} \right) -{\frac {e \left( r \left(
   \alpha,\beta \right) ,T_{{3}},U_{{3}},V_{{3}},W_{{3}},X_{{3}},Y_{{3}},P
   _{{3}} \right) \omega \left( \zeta \left( \alpha,\beta \right)
    \right)  \left( 1- \left( \zeta \left( \alpha,\beta \right)  \right) ^
   {4} \right) }{c}}+ \left( e \left( r \left( \alpha,\beta \right) ,T_{{2
   }},U_{{2}},V_{{2}},W_{{2}},X_{{2}},Y_{{2}},P_{{2}} \right) -e \left( r
    \left( \alpha,\beta \right) ,T_{{1}},U_{{1}},V_{{1}},W_{{1}},X_{{1}},Y
   _{{1}},P_{{1}} \right)  \right) \omega \left( \zeta \left( \alpha,\beta
    \right)  \right)  \left( \zeta \left( \alpha,\beta \right)  \right) ^{
   4} \right)

.. math::

   r \left( \alpha,\beta \right) =1/4\,\sqrt [3]{3}{4}^{2/3}\sqrt [3]{{
   \frac {1}{\pi \, \left( \alpha+\beta \right) }}}

.. math::

   \zeta \left( \alpha,\beta \right) ={\frac {\alpha-\beta}{\alpha+\beta}}

.. math::

   \omega \left( z \right) ={\frac { \left( 1+z \right) ^{4/3}+ \left( 1-z
    \right) ^{4/3}-2}{2\,\sqrt [3]{2}-2}}

.. math::

   e \left( r,t,u,v,w,x,y,p \right) =-2\,t \left( 1+ur \right) \ln
    \left( 1+1/2\,{\frac {1}{t \left( v\sqrt {r}+wr+x{r}^{3/2}+y{r}^{p+1}
    \right) }} \right)

.. math::

   c= 1.709921

.. math::

   {\it tausMFM}=1/2\,\tau \left( s \right)

.. math::

   {\it ds}=2\,{\it tausMFM}-1/4\,{\frac {\sigma \left( {\it ss} \right) }
   {\rho \left( s \right) }}

.. math::

   {\it Gab} \left( {\it chia},{\it chib} \right) =\sum _{i=0}^{n}{\it
   cCab}_{{i}} \left( {\frac {{\it yCab}\, \left( {{\it chia}}^{2}+{{\it
   chib}}^{2} \right) }{1+{\it yCab}\, \left( {{\it chia}}^{2}+{{\it chib}
   }^{2} \right) }} \right) ^{i}

.. math::

   {\it Gss} \left( {\it chis} \right) =\sum _{i=0}^{n}{\it cCss}_{{i}}
    \left( {\frac {{\it yCss}\,{{\it chis}}^{2}}{1+{\it yCss}\,{{\it chis}
   }^{2}}} \right) ^{i}

.. math::

   n=4

.. math::

   {\it cCab}=[ 1.0, 1.09297,- 3.79171, 2.82810,- 10.58909]

.. math::

   {\it cCss}=[ 1.0,- 3.05430, 7.61854, 1.47665,- 11.92365]

.. math::

   {\it yCab}= 0.0031

.. math::

   {\it yCss}= 0.06

.. math::

   f= \left( \epsilon \left( \rho \left( a \right) ,\rho \left( b \right)
    \right) -\epsilon \left( \rho \left( a \right) ,0 \right) -\epsilon
    \left( \rho \left( b \right) ,0 \right)  \right) {\it Gab} \left( \chi
    \left( a \right) ,\chi \left( b \right)  \right)

.. math::

   g=1/2\,{\frac {\epsilon \left( \rho \left( s \right) ,0 \right) {\it
   Gss} \left( \chi \left( s \right)  \right) {\it ds}}{{\it tausMFM}}}

.. math::

   G=1/2\,{\frac {\epsilon \left( \rho \left( s \right) ,0 \right) {\it
   Gss} \left( \chi \left( s \right)  \right) {\it ds}}{{\it tausMFM}}}

.. _density_functional_descriptions--m052xx-m05-2x-meta-gga-exchange-functional:

M052XX: M05-2X Meta-GGA Exchange Functional
===========================================

.. math::

   g=-3/4\,{\frac {\sqrt [3]{6}\sqrt [3]{{\pi }^{2}} \left( \rho \left( s
    \right)  \right) ^{4/3}F \left( S \right) {\it Fs} \left( {\it ws}
    \right) }{\pi }}

.. math::

   G=-3/4\,{\frac {\sqrt [3]{6}\sqrt [3]{{\pi }^{2}} \left( \rho \left( s
    \right)  \right) ^{4/3}F \left( S \right) {\it Fs} \left( {\it ws}
    \right) }{\pi }}

.. math::

   S=1/12\,{\frac {\chi \left( s \right) {6}^{2/3}}{\sqrt [3]{{\pi }^{2}}}
   }

.. math::

   F \left( S \right) =1+R-R \left( 1+{\frac {\mu\,{S}^{2}}{R}} \right) ^{
   -1}

.. math::

   R= 0.804

.. math::

   \mu=1/3\,\delta\,{\pi }^{2}

.. math::

   \delta= 0.066725

.. math::

   n=11

.. math::

   A=[ 1.0,- 0.56833,- 1.30057, 5.50070, 9.06402,- 32.21075,- 23.73298,
    70.22996, 29.88614,- 60.25778,- 13.22205, 15.23694]

.. math::

   {\it Fs} \left( {\it ws} \right) =\sum _{i=0}^{n}A_{{i}}{{\it ws}}^{i}

.. math::

   {\it ws}={\frac {{\it ts}-1}{{\it ts}+1}}

.. math::

   {\it ts}={\frac {{\it tslsda}}{{\it tausMFM}}}

.. math::

   {\it tslsda}=3/10\,{6}^{2/3} \left( {\pi }^{2} \right) ^{2/3} \left(
   \rho \left( s \right)  \right) ^{5/3}

.. math::

   {\it tausMFM}=1/2\,\tau \left( s \right)

.. _density_functional_descriptions--m05c-m05-meta-gga-correlation-functional:

M05C: M05 Meta-GGA Correlation Functional
=========================================

.. math::

   T=[ 0.031091, 0.015545, 0.016887]

.. math::

   U=[ 0.21370, 0.20548, 0.11125]

.. math::

   V=[ 7.5957, 14.1189, 10.357]

.. math::

   W=[ 3.5876, 6.1977, 3.6231]

.. math::

   X=[ 1.6382, 3.3662, 0.88026]

.. math::

   Y=[ 0.49294, 0.62517, 0.49671]

.. math::

   P=[1,1,1]

.. math::

   \epsilon \left( \alpha,\beta \right) = \left( \alpha+\beta \right)
    \left( e \left( r \left( \alpha,\beta \right) ,T_{{1}},U_{{1}},V_{{1}}
   ,W_{{1}},X_{{1}},Y_{{1}},P_{{1}} \right) -{\frac {e \left( r \left(
   \alpha,\beta \right) ,T_{{3}},U_{{3}},V_{{3}},W_{{3}},X_{{3}},Y_{{3}},P
   _{{3}} \right) \omega \left( \zeta \left( \alpha,\beta \right)
    \right)  \left( 1- \left( \zeta \left( \alpha,\beta \right)  \right) ^
   {4} \right) }{c}}+ \left( e \left( r \left( \alpha,\beta \right) ,T_{{2
   }},U_{{2}},V_{{2}},W_{{2}},X_{{2}},Y_{{2}},P_{{2}} \right) -e \left( r
    \left( \alpha,\beta \right) ,T_{{1}},U_{{1}},V_{{1}},W_{{1}},X_{{1}},Y
   _{{1}},P_{{1}} \right)  \right) \omega \left( \zeta \left( \alpha,\beta
    \right)  \right)  \left( \zeta \left( \alpha,\beta \right)  \right) ^{
   4} \right)

.. math::

   r \left( \alpha,\beta \right) =1/4\,\sqrt [3]{3}{4}^{2/3}\sqrt [3]{{
   \frac {1}{\pi \, \left( \alpha+\beta \right) }}}

.. math::

   \zeta \left( \alpha,\beta \right) ={\frac {\alpha-\beta}{\alpha+\beta}}

.. math::

   \omega \left( z \right) ={\frac { \left( 1+z \right) ^{4/3}+ \left( 1-z
    \right) ^{4/3}-2}{2\,\sqrt [3]{2}-2}}

.. math::

   e \left( r,t,u,v,w,x,y,p \right) =-2\,t \left( 1+ur \right) \ln
    \left( 1+1/2\,{\frac {1}{t \left( v\sqrt {r}+wr+x{r}^{3/2}+y{r}^{p+1}
    \right) }} \right)

.. math::

   c= 1.709921

.. math::

   {\it tausMFM}=1/2\,\tau \left( s \right)

.. math::

   {\it ds}=2\,{\it tausMFM}-1/4\,{\frac {\sigma \left( {\it ss} \right) }
   {\rho \left( s \right) }}

.. math::

   {\it Gab} \left( {\it chia},{\it chib} \right) =\sum _{i=0}^{n}{\it
   cCab}_{{i}} \left( {\frac {{\it yCab}\, \left( {{\it chia}}^{2}+{{\it
   chib}}^{2} \right) }{1+{\it yCab}\, \left( {{\it chia}}^{2}+{{\it chib}
   }^{2} \right) }} \right) ^{i}

.. math::

   {\it Gss} \left( {\it chis} \right) =\sum _{i=0}^{n}{\it cCss}_{{i}}
    \left( {\frac {{\it yCss}\,{{\it chis}}^{2}}{1+{\it yCss}\,{{\it chis}
   }^{2}}} \right) ^{i}

.. math::

   n=4

.. math::

   {\it cCab}=[ 1.0, 3.78569,- 14.15261,- 7.46589, 17.94491]

.. math::

   {\it cCss}=[ 1.0, 3.77344,- 26.04463, 30.69913,- 9.22695]

.. math::

   {\it yCab}= 0.0031

.. math::

   {\it yCss}= 0.06

.. math::

   f= \left( \epsilon \left( \rho \left( a \right) ,\rho \left( b \right)
    \right) -\epsilon \left( \rho \left( a \right) ,0 \right) -\epsilon
    \left( \rho \left( b \right) ,0 \right)  \right) {\it Gab} \left( \chi
    \left( a \right) ,\chi \left( b \right)  \right)

.. math::

   g=1/2\,{\frac {\epsilon \left( \rho \left( s \right) ,0 \right) {\it
   Gss} \left( \chi \left( s \right)  \right) {\it ds}}{{\it tausMFM}}}

.. math::

   G=1/2\,{\frac {\epsilon \left( \rho \left( s \right) ,0 \right) {\it
   Gss} \left( \chi \left( s \right)  \right) {\it ds}}{{\it tausMFM}}}

.. _density_functional_descriptions--m05x-m05-meta-gga-exchange-functional:

M05X: M05 Meta-GGA Exchange Functional
======================================

.. math::

   g=-3/4\,{\frac {\sqrt [3]{6}\sqrt [3]{{\pi }^{2}} \left( \rho \left( s
    \right)  \right) ^{4/3}F \left( S \right) {\it Fs} \left( {\it ws}
    \right) }{\pi }}

.. math::

   G=-3/4\,{\frac {\sqrt [3]{6}\sqrt [3]{{\pi }^{2}} \left( \rho \left( s
    \right)  \right) ^{4/3}F \left( S \right) {\it Fs} \left( {\it ws}
    \right) }{\pi }}

.. math::

   S=1/12\,{\frac {\chi \left( s \right) {6}^{2/3}}{\sqrt [3]{{\pi }^{2}}}
   }

.. math::

   F \left( S \right) =1+R-R \left( 1+{\frac {\mu\,{S}^{2}}{R}} \right) ^{
   -1}

.. math::

   R= 0.804

.. math::

   \mu=1/3\,\delta\,{\pi }^{2}

.. math::

   \delta= 0.066725

.. math::

   n=11

.. math::

   A=[ 1.0, 0.08151,- 0.43956,- 3.22422, 2.01819, 8.79431,- 0.00295,
    9.82029,- 4.82351,- 48.17574, 3.64802, 34.02248]

.. math::

   {\it Fs} \left( {\it ws} \right) =\sum _{i=0}^{n}A_{{i}}{{\it ws}}^{i}

.. math::

   {\it ws}={\frac {{\it ts}-1}{{\it ts}+1}}

.. math::

   {\it ts}={\frac {{\it tslsda}}{{\it tausMFM}}}

.. math::

   {\it tslsda}=3/10\,{6}^{2/3} \left( {\pi }^{2} \right) ^{2/3} \left(
   \rho \left( s \right)  \right) ^{5/3}

.. math::

   {\it tausMFM}=1/2\,\tau \left( s \right)

.. _density_functional_descriptions--m062xc-m06-2x-meta-gga-correlation-functional:

M062XC: M06-2X Meta-GGA Correlation Functional
==============================================

.. math::

   T=[ 0.031091, 0.015545, 0.016887]

.. math::

   U=[ 0.21370, 0.20548, 0.11125]

.. math::

   V=[ 7.5957, 14.1189, 10.357]

.. math::

   W=[ 3.5876, 6.1977, 3.6231]

.. math::

   X=[ 1.6382, 3.3662, 0.88026]

.. math::

   Y=[ 0.49294, 0.62517, 0.49671]

.. math::

   P=[1,1,1]

.. math::

   \epsilon \left( \alpha,\beta \right) = \left( \alpha+\beta \right)
    \left( e \left( r \left( \alpha,\beta \right) ,T_{{1}},U_{{1}},V_{{1}}
   ,W_{{1}},X_{{1}},Y_{{1}},P_{{1}} \right) -{\frac {e \left( r \left(
   \alpha,\beta \right) ,T_{{3}},U_{{3}},V_{{3}},W_{{3}},X_{{3}},Y_{{3}},P
   _{{3}} \right) \omega \left( \zeta \left( \alpha,\beta \right)
    \right)  \left( 1- \left( \zeta \left( \alpha,\beta \right)  \right) ^
   {4} \right) }{c}}+ \left( e \left( r \left( \alpha,\beta \right) ,T_{{2
   }},U_{{2}},V_{{2}},W_{{2}},X_{{2}},Y_{{2}},P_{{2}} \right) -e \left( r
    \left( \alpha,\beta \right) ,T_{{1}},U_{{1}},V_{{1}},W_{{1}},X_{{1}},Y
   _{{1}},P_{{1}} \right)  \right) \omega \left( \zeta \left( \alpha,\beta
    \right)  \right)  \left( \zeta \left( \alpha,\beta \right)  \right) ^{
   4} \right)

.. math::

   r \left( \alpha,\beta \right) =1/4\,\sqrt [3]{3}{4}^{2/3}\sqrt [3]{{
   \frac {1}{\pi \, \left( \alpha+\beta \right) }}}

.. math::

   \zeta \left( \alpha,\beta \right) ={\frac {\alpha-\beta}{\alpha+\beta}}

.. math::

   \omega \left( z \right) ={\frac { \left( 1+z \right) ^{4/3}+ \left( 1-z
    \right) ^{4/3}-2}{2\,\sqrt [3]{2}-2}}

.. math::

   e \left( r,t,u,v,w,x,y,p \right) =-2\,t \left( 1+ur \right) \ln
    \left( 1+1/2\,{\frac {1}{t \left( v\sqrt {r}+wr+x{r}^{3/2}+y{r}^{p+1}
    \right) }} \right)

.. math::

   c= 1.709921

.. math::

   {\it Gab} \left( {\it chia},{\it chib} \right) =\sum _{i=0}^{n}{\it
   cCab}_{{i}} \left( {\frac {{\it yCab}\, \left( {{\it chia}}^{2}+{{\it
   chib}}^{2} \right) }{1+{\it yCab}\, \left( {{\it chia}}^{2}+{{\it chib}
   }^{2} \right) }} \right) ^{i}

.. math::

   {\it Gss} \left( {\it chis} \right) =\sum _{i=0}^{n}{\it cCss}_{{i}}
    \left( {\frac {{\it yCss}\,{{\it chis}}^{2}}{1+{\it yCss}\,{{\it chis}
   }^{2}}} \right) ^{i}

.. math::

   n=4

.. math::

   {\it cCab}=[ 0.8833596, 33.57972,- 70.43548, 49.78271,- 18.52891]

.. math::

   {\it cCss}=[ 0.3097855,- 5.528642, 13.47420,- 32.13623, 28.46742]

.. math::

   {\it yCab}= 0.0031

.. math::

   {\it yCss}= 0.06

.. math::

   x=\sqrt { \left( \chi \left( a \right)  \right) ^{2}+ \left( \chi
    \left( b \right)  \right) ^{2}}

.. math::

   {\it tausMFM}=1/2\,\tau \left( s \right)

.. math::

   {\it tauaMFM}=1/2\,\tau \left( a \right)

.. math::

   {\it taubMFM}=1/2\,\tau \left( b \right)

.. math::

   {\it zs}=2\,{\frac {{\it tausMFM}}{ \left( \rho \left( s \right)
    \right) ^{5/3}}}-{\it cf}

.. math::

   z=2\,{\frac {{\it tauaMFM}}{ \left( \rho \left( a \right)  \right) ^{5/
   3}}}+2\,{\frac {{\it taubMFM}}{ \left( \rho \left( b \right)  \right) ^
   {5/3}}}-2\,{\it cf}

.. math::

   {\it cf}=3/5\,{6}^{2/3} \left( {\pi }^{2} \right) ^{2/3}

.. math::

   {\it ds}=1-{\frac { \left( \chi \left( s \right)  \right) ^{2}}{4\,{
   \it zs}+4\,{\it cf}}}

.. math::

   h \left( x,z,{\it d0},{\it d1},{\it d2},{\it d3},{\it d4},{\it d5},
   \alpha \right) ={\frac {{\it d0}}{\lambda \left( x,z,\alpha \right) }}+
   {\frac {{\it d1}\,{x}^{2}+{\it d2}\,z}{ \left( \lambda \left( x,z,
   \alpha \right)  \right) ^{2}}}+{\frac {{\it d3}\,{x}^{4}+{\it d4}\,{x}^
   {2}z+{\it d5}\,{z}^{2}}{ \left( \lambda \left( x,z,\alpha \right)
    \right) ^{3}}}

.. math::

   \lambda \left( x,z,\alpha \right) =1+\alpha\, \left( {x}^{2}+z \right)

.. math::

   {\it dCab}=[ 0.1166404,- 0.09120847,- 0.06726189, 0.00006720580,
    0.0008448011, 0.0]

.. math::

   {\it dCss}=[ 0.6902145, 0.09847204, 0.2214797,- 0.001968264,-
    0.006775479, 0.0]

.. math::

   {\it aCab}= 0.003050

.. math::

   {\it aCss}= 0.005151

.. math::

   f= \left( \epsilon \left( \rho \left( a \right) ,\rho \left( b \right)
    \right) -\epsilon \left( \rho \left( a \right) ,0 \right) -\epsilon
    \left( \rho \left( b \right) ,0 \right)  \right)  \left( {\it Gab}
    \left( \chi \left( a \right) ,\chi \left( b \right)  \right) +h
    \left( x,z,{\it dCab}_{{0}},{\it dCab}_{{1}},{\it dCab}_{{2}},{\it
   dCab}_{{3}},{\it dCab}_{{4}},{\it dCab}_{{5}},{\it aCab} \right)
    \right)

.. math::

   g=\epsilon \left( \rho \left( s \right) ,0 \right)  \left( {\it Gss}
    \left( \chi \left( s \right)  \right) +h \left( \chi \left( s \right)
   ,{\it zs},{\it dCss}_{{0}},{\it dCss}_{{1}},{\it dCss}_{{2}},{\it dCss}
   _{{3}},{\it dCss}_{{4}},{\it dCss}_{{5}},{\it aCss} \right)  \right) {
   \it ds}

.. math::

   G=\epsilon \left( \rho \left( s \right) ,0 \right)  \left( {\it Gss}
    \left( \chi \left( s \right)  \right) +h \left( \chi \left( s \right)
   ,{\it zs},{\it dCss}_{{0}},{\it dCss}_{{1}},{\it dCss}_{{2}},{\it dCss}
   _{{3}},{\it dCss}_{{4}},{\it dCss}_{{5}},{\it aCss} \right)  \right) {
   \it ds}

.. _density_functional_descriptions--m062xx-m06-2x-meta-gga-exchange-functional:

M062XX: M06-2X Meta-GGA Exchange Functional
===========================================

.. math::

   g=-3/4\,{\frac {\sqrt [3]{6}\sqrt [3]{{\pi }^{2}} \left( \rho \left( s
    \right)  \right) ^{4/3}F \left( S \right) {\it Fs} \left( {\it ws}
    \right) }{\pi }}

.. math::

   G=-3/4\,{\frac {\sqrt [3]{6}\sqrt [3]{{\pi }^{2}} \left( \rho \left( s
    \right)  \right) ^{4/3}F \left( S \right) {\it Fs} \left( {\it ws}
    \right) }{\pi }}

.. math::

   S=1/12\,{\frac {\chi \left( s \right) {6}^{2/3}}{\sqrt [3]{{\pi }^{2}}}
   }

.. math::

   F \left( S \right) =1+R-R \left( 1+{\frac {\mu\,{S}^{2}}{R}} \right) ^{
   -1}

.. math::

   R= 0.804

.. math::

   \mu=1/3\,\delta\,{\pi }^{2}

.. math::

   \delta= 0.066725

.. math::

   n=11

.. math::

   A=[ 0.4600000,- 0.2206052,- 0.09431788, 2.164494,- 2.556466,- 14.22133,
    15.55044, 35.98078,- 27.22754,- 39.24093, 15.22808, 15.22227]

.. math::

   {\it Fs} \left( {\it ws} \right) =\sum _{i=0}^{n}A_{{i}}{{\it ws}}^{i}

.. math::

   {\it ws}={\frac {{\it ts}-1}{{\it ts}+1}}

.. math::

   {\it ts}={\frac {{\it tslsda}}{{\it tausMFM}}}

.. math::

   {\it tslsda}=3/10\,{6}^{2/3} \left( {\pi }^{2} \right) ^{2/3} \left(
   \rho \left( s \right)  \right) ^{5/3}

.. math::

   {\it tausMFM}=1/2\,\tau \left( s \right)

.. _density_functional_descriptions--m06c-m06-meta-gga-correlation-functional:

M06C: M06 Meta-GGA Correlation Functional
=========================================

.. math::

   T=[ 0.031091, 0.015545, 0.016887]

.. math::

   U=[ 0.21370, 0.20548, 0.11125]

.. math::

   V=[ 7.5957, 14.1189, 10.357]

.. math::

   W=[ 3.5876, 6.1977, 3.6231]

.. math::

   X=[ 1.6382, 3.3662, 0.88026]

.. math::

   Y=[ 0.49294, 0.62517, 0.49671]

.. math::

   P=[1,1,1]

.. math::

   \epsilon \left( \alpha,\beta \right) = \left( \alpha+\beta \right)
    \left( e \left( r \left( \alpha,\beta \right) ,T_{{1}},U_{{1}},V_{{1}}
   ,W_{{1}},X_{{1}},Y_{{1}},P_{{1}} \right) -{\frac {e \left( r \left(
   \alpha,\beta \right) ,T_{{3}},U_{{3}},V_{{3}},W_{{3}},X_{{3}},Y_{{3}},P
   _{{3}} \right) \omega \left( \zeta \left( \alpha,\beta \right)
    \right)  \left( 1- \left( \zeta \left( \alpha,\beta \right)  \right) ^
   {4} \right) }{c}}+ \left( e \left( r \left( \alpha,\beta \right) ,T_{{2
   }},U_{{2}},V_{{2}},W_{{2}},X_{{2}},Y_{{2}},P_{{2}} \right) -e \left( r
    \left( \alpha,\beta \right) ,T_{{1}},U_{{1}},V_{{1}},W_{{1}},X_{{1}},Y
   _{{1}},P_{{1}} \right)  \right) \omega \left( \zeta \left( \alpha,\beta
    \right)  \right)  \left( \zeta \left( \alpha,\beta \right)  \right) ^{
   4} \right)

.. math::

   r \left( \alpha,\beta \right) =1/4\,\sqrt [3]{3}{4}^{2/3}\sqrt [3]{{
   \frac {1}{\pi \, \left( \alpha+\beta \right) }}}

.. math::

   \zeta \left( \alpha,\beta \right) ={\frac {\alpha-\beta}{\alpha+\beta}}

.. math::

   \omega \left( z \right) ={\frac { \left( 1+z \right) ^{4/3}+ \left( 1-z
    \right) ^{4/3}-2}{2\,\sqrt [3]{2}-2}}

.. math::

   e \left( r,t,u,v,w,x,y,p \right) =-2\,t \left( 1+ur \right) \ln
    \left( 1+1/2\,{\frac {1}{t \left( v\sqrt {r}+wr+x{r}^{3/2}+y{r}^{p+1}
    \right) }} \right)

.. math::

   c= 1.709921

.. math::

   {\it Gab} \left( {\it chia},{\it chib} \right) =\sum _{i=0}^{n}{\it
   cCab}_{{i}} \left( {\frac {{\it yCab}\, \left( {{\it chia}}^{2}+{{\it
   chib}}^{2} \right) }{1+{\it yCab}\, \left( {{\it chia}}^{2}+{{\it chib}
   }^{2} \right) }} \right) ^{i}

.. math::

   {\it Gss} \left( {\it chis} \right) =\sum _{i=0}^{n}{\it cCss}_{{i}}
    \left( {\frac {{\it yCss}\,{{\it chis}}^{2}}{1+{\it yCss}\,{{\it chis}
   }^{2}}} \right) ^{i}

.. math::

   n=4

.. math::

   {\it cCab}=[ 3.741593, 218.7098,- 453.1252, 293.6479,- 62.87470]

.. math::

   {\it cCss}=[ 0.5094055,- 1.491085, 17.23922,- 38.59018, 28.45044]

.. math::

   {\it yCab}= 0.0031

.. math::

   {\it yCss}= 0.06

.. math::

   x=\sqrt { \left( \chi \left( a \right)  \right) ^{2}+ \left( \chi
    \left( b \right)  \right) ^{2}}

.. math::

   {\it tausMFM}=1/2\,\tau \left( s \right)

.. math::

   {\it tauaMFM}=1/2\,\tau \left( a \right)

.. math::

   {\it taubMFM}=1/2\,\tau \left( b \right)

.. math::

   {\it zs}=2\,{\frac {{\it tausMFM}}{ \left( \rho \left( s \right)
    \right) ^{5/3}}}-{\it cf}

.. math::

   z=2\,{\frac {{\it tauaMFM}}{ \left( \rho \left( a \right)  \right) ^{5/
   3}}}+2\,{\frac {{\it taubMFM}}{ \left( \rho \left( b \right)  \right) ^
   {5/3}}}-2\,{\it cf}

.. math::

   {\it cf}=3/5\,{6}^{2/3} \left( {\pi }^{2} \right) ^{2/3}

.. math::

   {\it ds}=1-{\frac { \left( \chi \left( s \right)  \right) ^{2}}{4\,{
   \it zs}+4\,{\it cf}}}

.. math::

   h \left( x,z,{\it d0},{\it d1},{\it d2},{\it d3},{\it d4},{\it d5},
   \alpha \right) ={\frac {{\it d0}}{\lambda \left( x,z,\alpha \right) }}+
   {\frac {{\it d1}\,{x}^{2}+{\it d2}\,z}{ \left( \lambda \left( x,z,
   \alpha \right)  \right) ^{2}}}+{\frac {{\it d3}\,{x}^{4}+{\it d4}\,{x}^
   {2}z+{\it d5}\,{z}^{2}}{ \left( \lambda \left( x,z,\alpha \right)
    \right) ^{3}}}

.. math::

   \lambda \left( x,z,\alpha \right) =1+\alpha\, \left( {x}^{2}+z \right)

.. math::

   {\it dCab}=[- 2.741539,- 0.6720113,- 0.07932688, 0.001918681,-
    0.002032902, 0.0]

.. math::

   {\it dCss}=[ 0.4905945,- 0.1437348, 0.2357824, 0.001871015,-
    0.003788963, 0.0]

.. math::

   {\it aCab}= 0.003050

.. math::

   {\it aCss}= 0.005151

.. math::

   f= \left( \epsilon \left( \rho \left( a \right) ,\rho \left( b \right)
    \right) -\epsilon \left( \rho \left( a \right) ,0 \right) -\epsilon
    \left( \rho \left( b \right) ,0 \right)  \right)  \left( {\it Gab}
    \left( \chi \left( a \right) ,\chi \left( b \right)  \right) +h
    \left( x,z,{\it dCab}_{{0}},{\it dCab}_{{1}},{\it dCab}_{{2}},{\it
   dCab}_{{3}},{\it dCab}_{{4}},{\it dCab}_{{5}},{\it aCab} \right)
    \right)

.. math::

   g=\epsilon \left( \rho \left( s \right) ,0 \right)  \left( {\it Gss}
    \left( \chi \left( s \right)  \right) +h \left( \chi \left( s \right)
   ,{\it zs},{\it dCss}_{{0}},{\it dCss}_{{1}},{\it dCss}_{{2}},{\it dCss}
   _{{3}},{\it dCss}_{{4}},{\it dCss}_{{5}},{\it aCss} \right)  \right) {
   \it ds}

.. math::

   G=\epsilon \left( \rho \left( s \right) ,0 \right)  \left( {\it Gss}
    \left( \chi \left( s \right)  \right) +h \left( \chi \left( s \right)
   ,{\it zs},{\it dCss}_{{0}},{\it dCss}_{{1}},{\it dCss}_{{2}},{\it dCss}
   _{{3}},{\it dCss}_{{4}},{\it dCss}_{{5}},{\it aCss} \right)  \right) {
   \it ds}

.. _density_functional_descriptions--m06hfc-m06-hf-meta-gga-correlation-functional:

M06HFC: M06-HF Meta-GGA Correlation Functional
==============================================

.. math::

   T=[ 0.031091, 0.015545, 0.016887]

.. math::

   U=[ 0.21370, 0.20548, 0.11125]

.. math::

   V=[ 7.5957, 14.1189, 10.357]

.. math::

   W=[ 3.5876, 6.1977, 3.6231]

.. math::

   X=[ 1.6382, 3.3662, 0.88026]

.. math::

   Y=[ 0.49294, 0.62517, 0.49671]

.. math::

   P=[1,1,1]

.. math::

   \epsilon \left( \alpha,\beta \right) = \left( \alpha+\beta \right)
    \left( e \left( r \left( \alpha,\beta \right) ,T_{{1}},U_{{1}},V_{{1}}
   ,W_{{1}},X_{{1}},Y_{{1}},P_{{1}} \right) -{\frac {e \left( r \left(
   \alpha,\beta \right) ,T_{{3}},U_{{3}},V_{{3}},W_{{3}},X_{{3}},Y_{{3}},P
   _{{3}} \right) \omega \left( \zeta \left( \alpha,\beta \right)
    \right)  \left( 1- \left( \zeta \left( \alpha,\beta \right)  \right) ^
   {4} \right) }{c}}+ \left( e \left( r \left( \alpha,\beta \right) ,T_{{2
   }},U_{{2}},V_{{2}},W_{{2}},X_{{2}},Y_{{2}},P_{{2}} \right) -e \left( r
    \left( \alpha,\beta \right) ,T_{{1}},U_{{1}},V_{{1}},W_{{1}},X_{{1}},Y
   _{{1}},P_{{1}} \right)  \right) \omega \left( \zeta \left( \alpha,\beta
    \right)  \right)  \left( \zeta \left( \alpha,\beta \right)  \right) ^{
   4} \right)

.. math::

   r \left( \alpha,\beta \right) =1/4\,\sqrt [3]{3}{4}^{2/3}\sqrt [3]{{
   \frac {1}{\pi \, \left( \alpha+\beta \right) }}}

.. math::

   \zeta \left( \alpha,\beta \right) ={\frac {\alpha-\beta}{\alpha+\beta}}

.. math::

   \omega \left( z \right) ={\frac { \left( 1+z \right) ^{4/3}+ \left( 1-z
    \right) ^{4/3}-2}{2\,\sqrt [3]{2}-2}}

.. math::

   e \left( r,t,u,v,w,x,y,p \right) =-2\,t \left( 1+ur \right) \ln
    \left( 1+1/2\,{\frac {1}{t \left( v\sqrt {r}+wr+x{r}^{3/2}+y{r}^{p+1}
    \right) }} \right)

.. math::

   c= 1.709921

.. math::

   {\it Gab} \left( {\it chia},{\it chib} \right) =\sum _{i=0}^{n}{\it
   cCab}_{{i}} \left( {\frac {{\it yCab}\, \left( {{\it chia}}^{2}+{{\it
   chib}}^{2} \right) }{1+{\it yCab}\, \left( {{\it chia}}^{2}+{{\it chib}
   }^{2} \right) }} \right) ^{i}

.. math::

   {\it Gss} \left( {\it chis} \right) =\sum _{i=0}^{n}{\it cCss}_{{i}}
    \left( {\frac {{\it yCss}\,{{\it chis}}^{2}}{1+{\it yCss}\,{{\it chis}
   }^{2}}} \right) ^{i}

.. math::

   n=4

.. math::

   {\it cCab}=[ 1.674634, 57.32017, 59.55416,- 231.1007, 125.5199]

.. math::

   {\it cCss}=[ 0.1023254,- 2.453783, 29.13180,- 34.94358, 23.15955]

.. math::

   {\it yCab}= 0.0031

.. math::

   {\it yCss}= 0.06

.. math::

   x=\sqrt { \left( \chi \left( a \right)  \right) ^{2}+ \left( \chi
    \left( b \right)  \right) ^{2}}

.. math::

   {\it tausMFM}=1/2\,\tau \left( s \right)

.. math::

   {\it tauaMFM}=1/2\,\tau \left( a \right)

.. math::

   {\it taubMFM}=1/2\,\tau \left( b \right)

.. math::

   {\it zs}=2\,{\frac {{\it tausMFM}}{ \left( \rho \left( s \right)
    \right) ^{5/3}}}-{\it cf}

.. math::

   z=2\,{\frac {{\it tauaMFM}}{ \left( \rho \left( a \right)  \right) ^{5/
   3}}}+2\,{\frac {{\it taubMFM}}{ \left( \rho \left( b \right)  \right) ^
   {5/3}}}-2\,{\it cf}

.. math::

   {\it cf}=3/5\,{6}^{2/3} \left( {\pi }^{2} \right) ^{2/3}

.. math::

   {\it ds}=1-{\frac { \left( \chi \left( s \right)  \right) ^{2}}{4\,{
   \it zs}+4\,{\it cf}}}

.. math::

   h \left( x,z,{\it d0},{\it d1},{\it d2},{\it d3},{\it d4},{\it d5},
   \alpha \right) ={\frac {{\it d0}}{\lambda \left( x,z,\alpha \right) }}+
   {\frac {{\it d1}\,{x}^{2}+{\it d2}\,z}{ \left( \lambda \left( x,z,
   \alpha \right)  \right) ^{2}}}+{\frac {{\it d3}\,{x}^{4}+{\it d4}\,{x}^
   {2}z+{\it d5}\,{z}^{2}}{ \left( \lambda \left( x,z,\alpha \right)
    \right) ^{3}}}

.. math::

   \lambda \left( x,z,\alpha \right) =1+\alpha\, \left( {x}^{2}+z \right)

.. math::

   {\it dCab}=[- 0.6746338,- 0.1534002,- 0.09021521,- 0.001292037,-
    0.0002352983, 0.0]

.. math::

   {\it dCss}=[ 0.8976746,- 0.2345830, 0.2368173,- 0.0009913890,-
    0.01146165, 0.0]

.. math::

   {\it aCab}= 0.003050

.. math::

   {\it aCss}= 0.005151

.. math::

   f= \left( \epsilon \left( \rho \left( a \right) ,\rho \left( b \right)
    \right) -\epsilon \left( \rho \left( a \right) ,0 \right) -\epsilon
    \left( \rho \left( b \right) ,0 \right)  \right)  \left( {\it Gab}
    \left( \chi \left( a \right) ,\chi \left( b \right)  \right) +h
    \left( x,z,{\it dCab}_{{0}},{\it dCab}_{{1}},{\it dCab}_{{2}},{\it
   dCab}_{{3}},{\it dCab}_{{4}},{\it dCab}_{{5}},{\it aCab} \right)
    \right)

.. math::

   g=\epsilon \left( \rho \left( s \right) ,0 \right)  \left( {\it Gss}
    \left( \chi \left( s \right)  \right) +h \left( \chi \left( s \right)
   ,{\it zs},{\it dCss}_{{0}},{\it dCss}_{{1}},{\it dCss}_{{2}},{\it dCss}
   _{{3}},{\it dCss}_{{4}},{\it dCss}_{{5}},{\it aCss} \right)  \right) {
   \it ds}

.. math::

   G=\epsilon \left( \rho \left( s \right) ,0 \right)  \left( {\it Gss}
    \left( \chi \left( s \right)  \right) +h \left( \chi \left( s \right)
   ,{\it zs},{\it dCss}_{{0}},{\it dCss}_{{1}},{\it dCss}_{{2}},{\it dCss}
   _{{3}},{\it dCss}_{{4}},{\it dCss}_{{5}},{\it aCss} \right)  \right) {
   \it ds}

.. _density_functional_descriptions--m06hfx-m06-hf-meta-gga-exchange-functional:

M06HFX: M06-HF Meta-GGA Exchange Functional
===========================================

.. math::

   g=-3/4\,{\frac {\sqrt [3]{6}\sqrt [3]{{\pi }^{2}} \left( \rho \left( s
    \right)  \right) ^{4/3}F \left( S \right) {\it Fs} \left( {\it ws}
    \right) }{\pi }}+{\it eslsda}\,h \left( \chi \left( s \right) ,{\it zs
   } \right)

.. math::

   G=-3/4\,{\frac {\sqrt [3]{6}\sqrt [3]{{\pi }^{2}} \left( \rho \left( s
    \right)  \right) ^{4/3}F \left( S \right) {\it Fs} \left( {\it ws}
    \right) }{\pi }}+{\it eslsda}\,h \left( \chi \left( s \right) ,{\it zs
   } \right)

.. math::

   S=1/12\,{\frac {\chi \left( s \right) {6}^{2/3}}{\sqrt [3]{{\pi }^{2}}}
   }

.. math::

   F \left( S \right) =1+R-R \left( 1+{\frac {\mu\,{S}^{2}}{R}} \right) ^{
   -1}

.. math::

   R= 0.804

.. math::

   \mu=1/3\,\delta\,{\pi }^{2}

.. math::

   \delta= 0.066725

.. math::

   n=11

.. math::

   A=[ 0.1179732,- 1.066708,- 0.1462405, 7.481848, 3.776679,- 44.36118,-
    18.30962, 100.3903, 38.64360,- 98.06018,- 25.57716, 35.90404]

.. math::

   {\it Fs} \left( {\it ws} \right) =\sum _{i=0}^{n}A_{{i}}{{\it ws}}^{i}

.. math::

   {\it ws}={\frac {{\it ts}-1}{{\it ts}+1}}

.. math::

   {\it ts}={\frac {{\it tslsda}}{{\it tausMFM}}}

.. math::

   {\it tslsda}=3/10\,{6}^{2/3} \left( {\pi }^{2} \right) ^{2/3} \left(
   \rho \left( s \right)  \right) ^{5/3}

.. math::

   {\it eslsda}=-3/8\,\sqrt [3]{3}{4}^{2/3}\sqrt [3]{{\pi }^{-1}} \left(
   \rho \left( s \right)  \right) ^{4/3}

.. math::

   d=[- 0.1179732,- 0.002500000,- 0.01180065, 0.0, 0.0, 0.0]

.. math::

   \alpha= 0.001867

.. math::

   {\it zs}=2\,{\frac {{\it tausMFM}}{ \left( \rho \left( s \right)
    \right) ^{5/3}}}-{\it cf}

.. math::

   h \left( x,z \right) ={\frac {d_{{0}}}{\lambda \left( x,z,\alpha
    \right) }}+{\frac {d_{{1}}{x}^{2}+d_{{2}}z}{ \left( \lambda \left( x,z
   ,\alpha \right)  \right) ^{2}}}+{\frac {d_{{3}}{x}^{4}+d_{{4}}{x}^{2}z+
   d_{{5}}{z}^{2}}{ \left( \lambda \left( x,z,\alpha \right)  \right) ^{3}
   }}

.. math::

   \lambda \left( x,z,\alpha \right) =1+\alpha\, \left( {x}^{2}+z \right)

.. math::

   {\it cf}=3/5\,{6}^{2/3} \left( {\pi }^{2} \right) ^{2/3}

.. math::

   {\it tausMFM}=1/2\,\tau \left( s \right)

.. _density_functional_descriptions--m06lc-m06-l-meta-gga-correlation-functional:

M06LC: M06-L Meta-GGA Correlation Functional
============================================

.. math::

   T=[ 0.031091, 0.015545, 0.016887]

.. math::

   U=[ 0.21370, 0.20548, 0.11125]

.. math::

   V=[ 7.5957, 14.1189, 10.357]

.. math::

   W=[ 3.5876, 6.1977, 3.6231]

.. math::

   X=[ 1.6382, 3.3662, 0.88026]

.. math::

   Y=[ 0.49294, 0.62517, 0.49671]

.. math::

   P=[1,1,1]

.. math::

   \epsilon \left( \alpha,\beta \right) = \left( \alpha+\beta \right)
    \left( e \left( r \left( \alpha,\beta \right) ,T_{{1}},U_{{1}},V_{{1}}
   ,W_{{1}},X_{{1}},Y_{{1}},P_{{1}} \right) -{\frac {e \left( r \left(
   \alpha,\beta \right) ,T_{{3}},U_{{3}},V_{{3}},W_{{3}},X_{{3}},Y_{{3}},P
   _{{3}} \right) \omega \left( \zeta \left( \alpha,\beta \right)
    \right)  \left( 1- \left( \zeta \left( \alpha,\beta \right)  \right) ^
   {4} \right) }{c}}+ \left( e \left( r \left( \alpha,\beta \right) ,T_{{2
   }},U_{{2}},V_{{2}},W_{{2}},X_{{2}},Y_{{2}},P_{{2}} \right) -e \left( r
    \left( \alpha,\beta \right) ,T_{{1}},U_{{1}},V_{{1}},W_{{1}},X_{{1}},Y
   _{{1}},P_{{1}} \right)  \right) \omega \left( \zeta \left( \alpha,\beta
    \right)  \right)  \left( \zeta \left( \alpha,\beta \right)  \right) ^{
   4} \right)

.. math::

   r \left( \alpha,\beta \right) =1/4\,\sqrt [3]{3}{4}^{2/3}\sqrt [3]{{
   \frac {1}{\pi \, \left( \alpha+\beta \right) }}}

.. math::

   \zeta \left( \alpha,\beta \right) ={\frac {\alpha-\beta}{\alpha+\beta}}

.. math::

   \omega \left( z \right) ={\frac { \left( 1+z \right) ^{4/3}+ \left( 1-z
    \right) ^{4/3}-2}{2\,\sqrt [3]{2}-2}}

.. math::

   e \left( r,t,u,v,w,x,y,p \right) =-2\,t \left( 1+ur \right) \ln
    \left( 1+1/2\,{\frac {1}{t \left( v\sqrt {r}+wr+x{r}^{3/2}+y{r}^{p+1}
    \right) }} \right)

.. math::

   c= 1.709921

.. math::

   {\it Gab} \left( {\it chia},{\it chib} \right) =\sum _{i=0}^{n}{\it
   cCab}_{{i}} \left( {\frac {{\it yCab}\, \left( {{\it chia}}^{2}+{{\it
   chib}}^{2} \right) }{1+{\it yCab}\, \left( {{\it chia}}^{2}+{{\it chib}
   }^{2} \right) }} \right) ^{i}

.. math::

   {\it Gss} \left( {\it chis} \right) =\sum _{i=0}^{n}{\it cCss}_{{i}}
    \left( {\frac {{\it yCss}\,{{\it chis}}^{2}}{1+{\it yCss}\,{{\it chis}
   }^{2}}} \right) ^{i}

.. math::

   n=4

.. math::

   {\it cCab}=[ 0.6042374, 177.6783,- 251.3252, 76.35173,- 12.55699]

.. math::

   {\it cCss}=[ 0.5349466, 0.5396620,- 31.61217, 51.49592,- 29.19613]

.. math::

   {\it yCab}= 0.0031

.. math::

   {\it yCss}= 0.06

.. math::

   x=\sqrt { \left( \chi \left( a \right)  \right) ^{2}+ \left( \chi
    \left( b \right)  \right) ^{2}}

.. math::

   {\it tausMFM}=1/2\,\tau \left( s \right)

.. math::

   {\it tauaMFM}=1/2\,\tau \left( a \right)

.. math::

   {\it taubMFM}=1/2\,\tau \left( b \right)

.. math::

   {\it zs}=2\,{\frac {{\it tausMFM}}{ \left( \rho \left( s \right)
    \right) ^{5/3}}}-{\it cf}

.. math::

   z=2\,{\frac {{\it tauaMFM}}{ \left( \rho \left( a \right)  \right) ^{5/
   3}}}+2\,{\frac {{\it taubMFM}}{ \left( \rho \left( b \right)  \right) ^
   {5/3}}}-2\,{\it cf}

.. math::

   {\it cf}=3/5\,{6}^{2/3} \left( {\pi }^{2} \right) ^{2/3}

.. math::

   {\it ds}=1-{\frac { \left( \chi \left( s \right)  \right) ^{2}}{4\,{
   \it zs}+4\,{\it cf}}}

.. math::

   h \left( x,z,{\it d0},{\it d1},{\it d2},{\it d3},{\it d4},{\it d5},
   \alpha \right) ={\frac {{\it d0}}{\lambda \left( x,z,\alpha \right) }}+
   {\frac {{\it d1}\,{x}^{2}+{\it d2}\,z}{ \left( \lambda \left( x,z,
   \alpha \right)  \right) ^{2}}}+{\frac {{\it d3}\,{x}^{4}+{\it d4}\,{x}^
   {2}z+{\it d5}\,{z}^{2}}{ \left( \lambda \left( x,z,\alpha \right)
    \right) ^{3}}}

.. math::

   \lambda \left( x,z,\alpha \right) =1+\alpha\, \left( {x}^{2}+z \right)

.. math::

   {\it dCab}=[ 0.3957626,- 0.5614546, 0.01403963, 0.0009831442,-
    0.003577176, 0.0]

.. math::

   {\it dCss}=[ 0.4650534, 0.1617589, 0.1833657, 0.0004692100,-
    0.004990573, 0.0]

.. math::

   {\it aCab}= 0.003050

.. math::

   {\it aCss}= 0.005151

.. math::

   f= \left( \epsilon \left( \rho \left( a \right) ,\rho \left( b \right)
    \right) -\epsilon \left( \rho \left( a \right) ,0 \right) -\epsilon
    \left( \rho \left( b \right) ,0 \right)  \right)  \left( {\it Gab}
    \left( \chi \left( a \right) ,\chi \left( b \right)  \right) +h
    \left( x,z,{\it dCab}_{{0}},{\it dCab}_{{1}},{\it dCab}_{{2}},{\it
   dCab}_{{3}},{\it dCab}_{{4}},{\it dCab}_{{5}},{\it aCab} \right)
    \right)

.. math::

   g=\epsilon \left( \rho \left( s \right) ,0 \right)  \left( {\it Gss}
    \left( \chi \left( s \right)  \right) +h \left( \chi \left( s \right)
   ,{\it zs},{\it dCss}_{{0}},{\it dCss}_{{1}},{\it dCss}_{{2}},{\it dCss}
   _{{3}},{\it dCss}_{{4}},{\it dCss}_{{5}},{\it aCss} \right)  \right) {
   \it ds}

.. math::

   G=\epsilon \left( \rho \left( s \right) ,0 \right)  \left( {\it Gss}
    \left( \chi \left( s \right)  \right) +h \left( \chi \left( s \right)
   ,{\it zs},{\it dCss}_{{0}},{\it dCss}_{{1}},{\it dCss}_{{2}},{\it dCss}
   _{{3}},{\it dCss}_{{4}},{\it dCss}_{{5}},{\it aCss} \right)  \right) {
   \it ds}

.. _density_functional_descriptions--m06lx-m06-l-meta-gga-exchange-functional:

M06LX: M06-L Meta-GGA Exchange Functional
=========================================

.. math::

   g=-3/4\,{\frac {\sqrt [3]{6}\sqrt [3]{{\pi }^{2}} \left( \rho \left( s
    \right)  \right) ^{4/3}F \left( S \right) {\it Fs} \left( {\it ws}
    \right) }{\pi }}+{\it eslsda}\,h \left( \chi \left( s \right) ,{\it zs
   } \right)

.. math::

   G=-3/4\,{\frac {\sqrt [3]{6}\sqrt [3]{{\pi }^{2}} \left( \rho \left( s
    \right)  \right) ^{4/3}F \left( S \right) {\it Fs} \left( {\it ws}
    \right) }{\pi }}+{\it eslsda}\,h \left( \chi \left( s \right) ,{\it zs
   } \right)

.. math::

   S=1/12\,{\frac {\chi \left( s \right) {6}^{2/3}}{\sqrt [3]{{\pi }^{2}}}
   }

.. math::

   F \left( S \right) =1+R-R \left( 1+{\frac {\mu\,{S}^{2}}{R}} \right) ^{
   -1}

.. math::

   R= 0.804

.. math::

   \mu=1/3\,\delta\,{\pi }^{2}

.. math::

   \delta= 0.066725

.. math::

   n=11

.. math::

   A=[ 0.3987756, 0.2548219, 0.3923994,- 2.103655,- 6.302147, 10.97615,
    30.97273,- 23.18489,- 56.73480, 21.60364, 34.21814,- 9.049762]

.. math::

   {\it Fs} \left( {\it ws} \right) =\sum _{i=0}^{n}A_{{i}}{{\it ws}}^{i}

.. math::

   {\it ws}={\frac {{\it ts}-1}{{\it ts}+1}}

.. math::

   {\it ts}={\frac {{\it tslsda}}{{\it tausMFM}}}

.. math::

   {\it tslsda}=3/10\,{6}^{2/3} \left( {\pi }^{2} \right) ^{2/3} \left(
   \rho \left( s \right)  \right) ^{5/3}

.. math::

   {\it eslsda}=-3/8\,\sqrt [3]{3}{4}^{2/3}\sqrt [3]{{\pi }^{-1}} \left(
   \rho \left( s \right)  \right) ^{4/3}

.. math::

   d=[ 0.6012244, 0.004748822,- 0.008635108,- 0.000009308062,
    0.00004482811, 0.0]

.. math::

   \alpha= 0.001867

.. math::

   {\it zs}=2\,{\frac {{\it tausMFM}}{ \left( \rho \left( s \right)
    \right) ^{5/3}}}-{\it cf}

.. math::

   h \left( x,z \right) ={\frac {d_{{0}}}{\lambda \left( x,z,\alpha
    \right) }}+{\frac {d_{{1}}{x}^{2}+d_{{2}}z}{ \left( \lambda \left( x,z
   ,\alpha \right)  \right) ^{2}}}+{\frac {d_{{3}}{x}^{4}+d_{{4}}{x}^{2}z+
   d_{{5}}{z}^{2}}{ \left( \lambda \left( x,z,\alpha \right)  \right) ^{3}
   }}

.. math::

   \lambda \left( x,z,\alpha \right) =1+\alpha\, \left( {x}^{2}+z \right)

.. math::

   {\it cf}=3/5\,{6}^{2/3} \left( {\pi }^{2} \right) ^{2/3}

.. math::

   {\it tausMFM}=1/2\,\tau \left( s \right)

.. _density_functional_descriptions--m06x-m06-meta-gga-exchange-functional:

M06X: M06 Meta-GGA Exchange Functional
======================================

.. math::

   g=-3/4\,{\frac {\sqrt [3]{6}\sqrt [3]{{\pi }^{2}} \left( \rho \left( s
    \right)  \right) ^{4/3}F \left( S \right) {\it Fs} \left( {\it ws}
    \right) }{\pi }}+{\it eslsda}\,h \left( \chi \left( s \right) ,{\it zs
   } \right)

.. math::

   G=-3/4\,{\frac {\sqrt [3]{6}\sqrt [3]{{\pi }^{2}} \left( \rho \left( s
    \right)  \right) ^{4/3}F \left( S \right) {\it Fs} \left( {\it ws}
    \right) }{\pi }}+{\it eslsda}\,h \left( \chi \left( s \right) ,{\it zs
   } \right)

.. math::

   S=1/12\,{\frac {\chi \left( s \right) {6}^{2/3}}{\sqrt [3]{{\pi }^{2}}}
   }

.. math::

   F \left( S \right) =1+R-R \left( 1+{\frac {\mu\,{S}^{2}}{R}} \right) ^{
   -1}

.. math::

   R= 0.804

.. math::

   \mu=1/3\,\delta\,{\pi }^{2}

.. math::

   \delta= 0.066725

.. math::

   n=11

.. math::

   A=[ 0.5877943,- 0.1371776, 0.2682367,- 2.515898,- 2.978892, 8.710679,
    16.88195,- 4.489724,- 32.99983,- 14.49050, 20.43747, 12.56504]

.. math::

   {\it Fs} \left( {\it ws} \right) =\sum _{i=0}^{n}A_{{i}}{{\it ws}}^{i}

.. math::

   {\it ws}={\frac {{\it ts}-1}{{\it ts}+1}}

.. math::

   {\it ts}={\frac {{\it tslsda}}{{\it tausMFM}}}

.. math::

   {\it tslsda}=3/10\,{6}^{2/3} \left( {\pi }^{2} \right) ^{2/3} \left(
   \rho \left( s \right)  \right) ^{5/3}

.. math::

   {\it eslsda}=-3/8\,\sqrt [3]{3}{4}^{2/3}\sqrt [3]{{\pi }^{-1}} \left(
   \rho \left( s \right)  \right) ^{4/3}

.. math::

   d=[ 0.1422057, 0.0007370319,- 0.01601373, 0.0, 0.0, 0.0]

.. math::

   \alpha= 0.001867

.. math::

   {\it zs}=2\,{\frac {{\it tausMFM}}{ \left( \rho \left( s \right)
    \right) ^{5/3}}}-{\it cf}

.. math::

   h \left( x,z \right) ={\frac {d_{{0}}}{\lambda \left( x,z,\alpha
    \right) }}+{\frac {d_{{1}}{x}^{2}+d_{{2}}z}{ \left( \lambda \left( x,z
   ,\alpha \right)  \right) ^{2}}}+{\frac {d_{{3}}{x}^{4}+d_{{4}}{x}^{2}z+
   d_{{5}}{z}^{2}}{ \left( \lambda \left( x,z,\alpha \right)  \right) ^{3}
   }}

.. math::

   \lambda \left( x,z,\alpha \right) =1+\alpha\, \left( {x}^{2}+z \right)

.. math::

   {\it cf}=3/5\,{6}^{2/3} \left( {\pi }^{2} \right) ^{2/3}

.. math::

   {\it tausMFM}=1/2\,\tau \left( s \right)

.. _density_functional_descriptions--m12c-meta-gga-correlation-functional:

M12C: Meta GGA Correlation Functional
=====================================

Meta-GGA correlation functional based on first principles, see M. Modrzejewski et al., `J. Chem. Phys. <https://dx.doi.org/10.1063/1.4768228>`__ **137**, 204121 (2012).

.. _density_functional_descriptions--mk00-exchange-functional-for-accurate-virtual-orbital-energies:

MK00: Exchange Functional for Accurate Virtual Orbital Energies
===============================================================

.. math::

   g=-3\,{\frac {\pi \, \left( \rho \left( s \right)  \right) ^{3}}{\tau
    \left( s \right) -1/4\,\upsilon \left( s \right) }}

.. _density_functional_descriptions--mk00b-exchange-functional-for-accurate-virtual-orbital-energies:

MK00B: Exchange Functional for Accurate Virtual Orbital Energies
================================================================

MK00 with gradient correction of the form of B88X but with different empirical parameter.

.. math::

   g=-3\,{\frac {\pi \, \left( \rho \left( s \right)  \right) ^{3}}{\tau
    \left( s \right) -1/4\,\upsilon \left( s \right) }}-{\frac {\beta\,
    \left( \rho \left( s \right)  \right) ^{4/3} \left( \chi \left( s
    \right)  \right) ^{2}}{1+6\,\beta\,\chi \left( s \right) {\it arcsinh}
    \left( \chi \left( s \right)  \right) }}

.. math::

   \beta= 0.0016

.. math::

   G=-3\,{\frac {\pi \, \left( \rho \left( s \right)  \right) ^{3}}{\tau
    \left( s \right) -1/4\,\upsilon \left( s \right) }}-{\frac {\beta\,
    \left( \rho \left( s \right)  \right) ^{4/3} \left( \chi \left( s
    \right)  \right) ^{2}}{1+6\,\beta\,\chi \left( s \right) {\it arcsinh}
    \left( \chi \left( s \right)  \right) }}

.. _density_functional_descriptions--p86:

P86: .
======

Gradient correction to VWN.

.. math::

   f=\rho\,e+{\frac {{e^{-\Phi}}C \left( r \right) \sigma}{d{\rho}^{4/3}}}

.. math::

   r=1/4\,\sqrt [3]{3}{4}^{2/3}\sqrt [3]{{\frac {1}{\pi \,\rho}}}

.. math::

   x=\sqrt {r}

.. math::

   \zeta={\frac {\rho \left( a \right) -\rho \left( b \right) }{\rho}}

.. math::

   k=[ 0.0310907, 0.01554535,-1/6\,{\pi }^{-2}]

.. math::

   l=[- 0.10498,- 0.325,- 0.0047584]

.. math::

   m=[ 3.72744, 7.06042, 1.13107]

.. math::

   n=[ 12.9352, 18.0578, 13.0045]

.. math::

   e=\Lambda+\omega\,y \left( 1+h{\zeta}^{4} \right)

.. math::

   y={\frac {9}{8}}\, \left( 1+\zeta \right) ^{4/3}+{\frac {9}{8}}\,
    \left( 1-\zeta \right) ^{4/3}-9/4

.. math::

   h=4/9\,{\frac {\lambda-\Lambda}{ \left( \sqrt [3]{2}-1 \right) \omega}}
   -1

.. math::

   \Lambda=q \left( k_{{1}},l_{{1}},m_{{1}},n_{{1}} \right)

.. math::

   \lambda=q \left( k_{{2}},l_{{2}},m_{{2}},n_{{2}} \right)

.. math::

   \omega=q \left( k_{{3}},l_{{3}},m_{{3}},n_{{3}} \right)

.. math::

   q \left( A,p,c,d \right) =A \left( \ln  \left( {\frac {{x}^{2}}{X
    \left( x,c,d \right) }} \right) +2\,c\arctan \left( {\frac {Q \left( c
   ,d \right) }{2\,x+c}} \right)  \left( Q \left( c,d \right)  \right) ^{-
   1}-cp \left( \ln  \left( {\frac { \left( x-p \right) ^{2}}{X \left( x,c
   ,d \right) }} \right) +2\, \left( c+2\,p \right) \arctan \left( {\frac
   {Q \left( c,d \right) }{2\,x+c}} \right)  \left( Q \left( c,d \right)
    \right) ^{-1} \right)  \left( X \left( p,c,d \right)  \right) ^{-1}
    \right)

.. math::

   Q \left( c,d \right) =\sqrt {4\,d-{c}^{2}}

.. math::

   X \left( i,c,d \right) ={i}^{2}+ci+d

.. math::

   \Phi= 0.007390075\,{\frac {z\sqrt {\sigma}}{C \left( r \right) {\rho}^{
   7/6}}}

.. math::

   d=\sqrt [3]{2}\sqrt { \left( 1/2+1/2\,\zeta \right) ^{5/3}+ \left( 1/2-
   1/2\,\zeta \right) ^{5/3}}

.. math::

   C \left( r \right) = 0.001667+{\frac { 0.002568+\alpha\,r+\beta\,{r}^{2
   }}{1+\xi\,r+\delta\,{r}^{2}+10000\,\beta\,{r}^{3}}}

.. math::

   z= 0.11

.. math::

   \alpha= 0.023266

.. math::

   \beta= 0.000007389

.. math::

   \xi= 8.723

.. math::

   \delta= 0.472

.. _density_functional_descriptions--pbec-pbe-correlation-functional:

PBEC: PBE Correlation Functional
================================

.. math::

   f=\rho\, \left( \epsilon \left( \rho \left( a \right) ,\rho \left( b
    \right)  \right) +H \left( d,\rho \left( a \right) ,\rho \left( b
    \right)  \right)  \right)

.. math::

   G=\rho\, \left( \epsilon \left( \rho \left( s \right) ,0 \right) +C
    \left( Q,\rho \left( s \right) ,0 \right)  \right)

.. math::

   d=1/12\,{\frac {\sqrt {\sigma}{3}^{5/6}}{u \left( \rho \left( a
    \right) ,\rho \left( b \right)  \right) \sqrt [6]{{\pi }^{-1}}{\rho}^{
   7/6}}}

.. math::

   u \left( \alpha,\beta \right) =1/2\, \left( 1+\zeta \left( \alpha,\beta
    \right)  \right) ^{2/3}+1/2\, \left( 1-\zeta \left( \alpha,\beta
    \right)  \right) ^{2/3}

.. math::

   H \left( d,\alpha,\beta \right) =1/2\, \left( u \left( \rho \left( a
    \right) ,\rho \left( b \right)  \right)  \right) ^{3}{\lambda}^{2}\ln
    \left( 1+2\,{\frac {\iota\, \left( {d}^{2}+A \left( \alpha,\beta
    \right) {d}^{4} \right) }{\lambda\, \left( 1+A \left( \alpha,\beta
    \right) {d}^{2}+ \left( A \left( \alpha,\beta \right)  \right) ^{2}{d}
   ^{4} \right) }} \right) {\iota}^{-1}

.. math::

   A \left( \alpha,\beta \right) =2\,\iota{\lambda}^{-1} \left( {e^{-2\,{
   \frac {\iota\,\epsilon \left( \alpha,\beta \right) }{ \left( u \left(
   \rho \left( a \right) ,\rho \left( b \right)  \right)  \right) ^{3}{
   \lambda}^{2}}}}}-1 \right) ^{-1}

.. math::

   \iota= 0.0716

.. math::

   \lambda=\nu\,\kappa

.. math::

   \nu=16\,{\frac {\sqrt [3]{3}\sqrt [3]{{\pi }^{2}}}{\pi }}

.. math::

   \kappa= 0.004235

.. math::

   Z=- 0.001667

.. math::

   \phi \left( r \right) =\theta \left( r \right) -Z

.. math::

   \theta \left( r \right) ={\frac {1}{1000}}\,{\frac { 2.568+\Xi\,r+\Phi
   \,{r}^{2}}{1+\Lambda\,r+\Upsilon\,{r}^{2}+10\,\Phi\,{r}^{3}}}

.. math::

   \Xi= 23.266

.. math::

   \Phi= 0.007389

.. math::

   \Lambda= 8.723

.. math::

   \Upsilon= 0.472

.. math::

   T=[ 0.031091, 0.015545, 0.016887]

.. math::

   U=[ 0.21370, 0.20548, 0.11125]

.. math::

   V=[ 7.5957, 14.1189, 10.357]

.. math::

   W=[ 3.5876, 6.1977, 3.6231]

.. math::

   X=[ 1.6382, 3.3662, 0.88026]

.. math::

   Y=[ 0.49294, 0.62517, 0.49671]

.. math::

   P=[1,1,1]

.. math::

   \epsilon \left( \alpha,\beta \right) =e \left( r \left( \alpha,\beta
    \right) ,T_{{1}},U_{{1}},V_{{1}},W_{{1}},X_{{1}},Y_{{1}},P_{{1}}
    \right) -{\frac {e \left( r \left( \alpha,\beta \right) ,T_{{3}},U_{{3
   }},V_{{3}},W_{{3}},X_{{3}},Y_{{3}},P_{{3}} \right) \omega \left( \zeta
    \left( \alpha,\beta \right)  \right)  \left( 1- \left( \zeta \left(
   \alpha,\beta \right)  \right) ^{4} \right) }{c}}+ \left( e \left( r
    \left( \alpha,\beta \right) ,T_{{2}},U_{{2}},V_{{2}},W_{{2}},X_{{2}},Y
   _{{2}},P_{{2}} \right) -e \left( r \left( \alpha,\beta \right) ,T_{{1}}
   ,U_{{1}},V_{{1}},W_{{1}},X_{{1}},Y_{{1}},P_{{1}} \right)  \right)
   \omega \left( \zeta \left( \alpha,\beta \right)  \right)  \left( \zeta
    \left( \alpha,\beta \right)  \right) ^{4}

.. math::

   r \left( \alpha,\beta \right) =1/4\,\sqrt [3]{3}{4}^{2/3}\sqrt [3]{{
   \frac {1}{\pi \, \left( \alpha+\beta \right) }}}

.. math::

   \zeta \left( \alpha,\beta \right) ={\frac {\alpha-\beta}{\alpha+\beta}}

.. math::

   \omega \left( z \right) ={\frac { \left( 1+z \right) ^{4/3}+ \left( 1-z
    \right) ^{4/3}-2}{2\,\sqrt [3]{2}-2}}

.. math::

   e \left( r,t,u,v,w,x,y,p \right) =-2\,t \left( 1+ur \right) \ln
    \left( 1+1/2\,{\frac {1}{t \left( v\sqrt {r}+wr+x{r}^{3/2}+y{r}^{p+1}
    \right) }} \right)

.. math::

   c= 1.709921

.. math::

   C \left( d,\alpha,\beta \right) =K \left( Q,\alpha,\beta \right) +M
    \left( Q,\alpha,\beta \right)

.. math::

   M \left( d,\alpha,\beta \right) = 0.5\,\nu\, \left( \phi \left( r
    \left( \alpha,\beta \right)  \right) -\kappa-3/7\,Z \right) {d}^{2}{e^
   {- 335.9789467\,{\frac {{3}^{2/3}{d}^{2}}{\sqrt [3]{{\pi }^{5}\rho}}}}}

.. math::

   K \left( d,\alpha,\beta \right) = 0.2500000000\,{\lambda}^{2}\ln
    \left( 1+2\,{\frac {\iota\, \left( {d}^{2}+N \left( \alpha,\beta
    \right) {d}^{4} \right) }{\lambda\, \left( 1+N \left( \alpha,\beta
    \right) {d}^{2}+ \left( N \left( \alpha,\beta \right)  \right) ^{2}{d}
   ^{4} \right) }} \right) {\iota}^{-1}

.. math::

   N \left( \alpha,\beta \right) =2\,\iota{\lambda}^{-1} \left( {e^{-4\,{
   \frac {\iota\,\epsilon \left( \alpha,\beta \right) }{{\lambda}^{2}}}}}-
   1 \right) ^{-1}

.. math::

   Q=1/12\,{\frac {\sqrt {\sigma \left( {\it ss} \right) }\sqrt [3]{2}{3}^
   {5/6}}{\sqrt [6]{{\pi }^{-1}}{\rho}^{7/6}}}

.. _density_functional_descriptions--pbesolc-pbesol-correlation-functional:

PBESOLC: PBEsol Correlation Functional
======================================

.. _density_functional_descriptions--pbesolx-pbesol-exchange-functional:

PBESOLX: PBEsol Exchange Functional
===================================

.. _density_functional_descriptions--pbex-pbe-exchange-functional:

PBEX: PBE Exchange Functional
=============================

.. math::

   g=1/2\,E \left( 2\,\rho \left( s \right)  \right)

.. math::

   G=1/2\,E \left( 2\,\rho \left( s \right)  \right)

.. math::

   E \left( n \right) =-3/4\,{\frac {\sqrt [3]{3}\sqrt [3]{{\pi }^{2}}{n}^
   {4/3}F \left( S \right) }{\pi }}

.. math::

   S=1/12\,{\frac {\chi \left( s \right) {6}^{2/3}}{\sqrt [3]{{\pi }^{2}}}
   }

.. math::

   F \left( S \right) =1+R-R \left( 1+{\frac {\mu\,{S}^{2}}{R}} \right) ^{
   -1}

.. math::

   R= 0.804

.. math::

   \mu=1/3\,\delta\,{\pi }^{2}

.. math::

   \delta= 0.066725

.. _density_functional_descriptions--pbexrev-revised-pbe-exchange-functional:

PBEXREV: Revised PBE Exchange Functional
========================================

Changes the value of the constant R from the original PBEX functional

.. math::

   g=1/2\,E \left( 2\,\rho \left( s \right)  \right)

.. math::

   G=1/2\,E \left( 2\,\rho \left( s \right)  \right)

.. math::

   E \left( n \right) =-3/4\,{\frac {\sqrt [3]{3}\sqrt [3]{{\pi }^{2}}{n}^
   {4/3}F \left( S \right) }{\pi }}

.. math::

   S=1/12\,{\frac {\chi \left( s \right) {6}^{2/3}}{\sqrt [3]{{\pi }^{2}}}
   }

.. math::

   F \left( S \right) =1+R-R \left( 1+{\frac {\mu\,{S}^{2}}{R}} \right) ^{
   -1}

.. math::

   R= 1.245

.. math::

   \mu=1/3\,\delta\,{\pi }^{2}

.. math::

   \delta= 0.066725

.. _density_functional_descriptions--pw86:

PW86: .
=======

GGA Exchange Functional.

.. math::

   g=1/2\,E \left( 2\,\rho \left( s \right)  \right)

.. math::

   E \left( n \right) =-3/4\,\sqrt [3]{3}\sqrt [3]{{\pi }^{-1}}{n}^{4/3}F
    \left( S \right)

.. math::

   F \left( S \right) = \left( 1+ 1.296\,{S}^{2}+14\,{S}^{4}+ 0.2\,{S}^{6}
    \right) ^{1/15}

.. math::

   S=1/12\,{\frac {\chi \left( s \right) {6}^{2/3}}{\sqrt [3]{{\pi }^{2}}}
   }

.. math::

   G=1/2\,E \left( 2\,\rho \left( s \right)  \right)

.. _density_functional_descriptions--pw91c-perdew-wang-1991-gga-correlation-functional:

PW91C: Perdew-Wang 1991 GGA Correlation Functional
==================================================

.. math::

   f=\rho\, \left( \epsilon \left( \rho \left( a \right) ,\rho \left( b
    \right)  \right) +H \left( d,\rho \left( a \right) ,\rho \left( b
    \right)  \right)  \right)

.. math::

   G=\rho\, \left( \epsilon \left( \rho \left( s \right) ,0 \right) +C
    \left( Q,\rho \left( s \right) ,0 \right)  \right)

.. math::

   d=1/12\,{\frac {\sqrt {\sigma}{3}^{5/6}}{u \left( \rho \left( a
    \right) ,\rho \left( b \right)  \right) \sqrt [6]{{\pi }^{-1}}{\rho}^{
   7/6}}}

.. math::

   u \left( \alpha,\beta \right) =1/2\, \left( 1+\zeta \left( \alpha,\beta
    \right)  \right) ^{2/3}+1/2\, \left( 1-\zeta \left( \alpha,\beta
    \right)  \right) ^{2/3}

.. math::

   H \left( d,\alpha,\beta \right) =L \left( d,\alpha,\beta \right) +J
    \left( d,\alpha,\beta \right)

.. math::

   L \left( d,\alpha,\beta \right) =1/2\, \left( u \left( \rho \left( a
    \right) ,\rho \left( b \right)  \right)  \right) ^{3}{\lambda}^{2}\ln
    \left( 1+2\,{\frac {\iota\, \left( {d}^{2}+A \left( \alpha,\beta
    \right) {d}^{4} \right) }{\lambda\, \left( 1+A \left( \alpha,\beta
    \right) {d}^{2}+ \left( A \left( \alpha,\beta \right)  \right) ^{2}{d}
   ^{4} \right) }} \right) {\iota}^{-1}

.. math::

   J \left( d,\alpha,\beta \right) =\nu\, \left( \phi \left( r \left(
   \alpha,\beta \right)  \right) -\kappa-3/7\,Z \right)  \left( u \left(
   \rho \left( a \right) ,\rho \left( b \right)  \right)  \right) ^{3}{d}^
   {2}{e^{-{\frac {400}{3}}\,{\frac { \left( u \left( \rho \left( a
    \right) ,\rho \left( b \right)  \right)  \right) ^{4}{3}^{2/3}{d}^{2}}
   {\sqrt [3]{{\pi }^{5}\rho}}}}}

.. math::

   A \left( \alpha,\beta \right) =2\,\iota{\lambda}^{-1} \left( {e^{-2\,{
   \frac {\iota\,\epsilon \left( \alpha,\beta \right) }{ \left( u \left(
   \rho \left( a \right) ,\rho \left( b \right)  \right)  \right) ^{3}{
   \lambda}^{2}}}}}-1 \right) ^{-1}

.. math::

   \iota= 0.09

.. math::

   \lambda=\nu\,\kappa

.. math::

   \nu=16\,{\frac {\sqrt [3]{3}\sqrt [3]{{\pi }^{2}}}{\pi }}

.. math::

   \kappa= 0.004235

.. math::

   Z=- 0.001667

.. math::

   \phi \left( r \right) =\theta \left( r \right) -Z

.. math::

   \theta \left( r \right) ={\frac {1}{1000}}\,{\frac { 2.568+\Xi\,r+\Phi
   \,{r}^{2}}{1+\Lambda\,r+\Upsilon\,{r}^{2}+10\,\Phi\,{r}^{3}}}

.. math::

   \Xi= 23.266

.. math::

   \Phi= 0.007389

.. math::

   \Lambda= 8.723

.. math::

   \Upsilon= 0.472

.. math::

   T=[ 0.031091, 0.015545, 0.016887]

.. math::

   U=[ 0.21370, 0.20548, 0.11125]

.. math::

   V=[ 7.5957, 14.1189, 10.357]

.. math::

   W=[ 3.5876, 6.1977, 3.6231]

.. math::

   X=[ 1.6382, 3.3662, 0.88026]

.. math::

   Y=[ 0.49294, 0.62517, 0.49671]

.. math::

   P=[1,1,1]

.. math::

   \epsilon \left( \alpha,\beta \right) =e \left( r \left( \alpha,\beta
    \right) ,T_{{1}},U_{{1}},V_{{1}},W_{{1}},X_{{1}},Y_{{1}},P_{{1}}
    \right) -{\frac {e \left( r \left( \alpha,\beta \right) ,T_{{3}},U_{{3
   }},V_{{3}},W_{{3}},X_{{3}},Y_{{3}},P_{{3}} \right) \omega \left( \zeta
    \left( \alpha,\beta \right)  \right)  \left( 1- \left( \zeta \left(
   \alpha,\beta \right)  \right) ^{4} \right) }{c}}+ \left( e \left( r
    \left( \alpha,\beta \right) ,T_{{2}},U_{{2}},V_{{2}},W_{{2}},X_{{2}},Y
   _{{2}},P_{{2}} \right) -e \left( r \left( \alpha,\beta \right) ,T_{{1}}
   ,U_{{1}},V_{{1}},W_{{1}},X_{{1}},Y_{{1}},P_{{1}} \right)  \right)
   \omega \left( \zeta \left( \alpha,\beta \right)  \right)  \left( \zeta
    \left( \alpha,\beta \right)  \right) ^{4}

.. math::

   r \left( \alpha,\beta \right) =1/4\,\sqrt [3]{3}{4}^{2/3}\sqrt [3]{{
   \frac {1}{\pi \, \left( \alpha+\beta \right) }}}

.. math::

   \zeta \left( \alpha,\beta \right) ={\frac {\alpha-\beta}{\alpha+\beta}}

.. math::

   \omega \left( z \right) ={\frac { \left( 1+z \right) ^{4/3}+ \left( 1-z
    \right) ^{4/3}-2}{2\,\sqrt [3]{2}-2}}

.. math::

   e \left( r,t,u,v,w,x,y,p \right) =-2\,t \left( 1+ur \right) \ln
    \left( 1+1/2\,{\frac {1}{t \left( v\sqrt {r}+wr+x{r}^{3/2}+y{r}^{p+1}
    \right) }} \right)

.. math::

   c= 1.709921

.. math::

   C \left( d,\alpha,\beta \right) =K \left( Q,\alpha,\beta \right) +M
    \left( Q,\alpha,\beta \right)

.. math::

   M \left( d,\alpha,\beta \right) = 0.5\,\nu\, \left( \phi \left( r
    \left( \alpha,\beta \right)  \right) -\kappa-3/7\,Z \right) {d}^{2}{e^
   {- 335.9789467\,{\frac {{3}^{2/3}{d}^{2}}{\sqrt [3]{{\pi }^{5}\rho}}}}}

.. math::

   K \left( d,\alpha,\beta \right) = 0.2500000000\,{\lambda}^{2}\ln
    \left( 1+2\,{\frac {\iota\, \left( {d}^{2}+N \left( \alpha,\beta
    \right) {d}^{4} \right) }{\lambda\, \left( 1+N \left( \alpha,\beta
    \right) {d}^{2}+ \left( N \left( \alpha,\beta \right)  \right) ^{2}{d}
   ^{4} \right) }} \right) {\iota}^{-1}

.. math::

   N \left( \alpha,\beta \right) =2\,\iota{\lambda}^{-1} \left( {e^{-4\,{
   \frac {\iota\,\epsilon \left( \alpha,\beta \right) }{{\lambda}^{2}}}}}-
   1 \right) ^{-1}

.. math::

   Q=1/12\,{\frac {\sqrt {\sigma \left( {\it ss} \right) }\sqrt [3]{2}{3}^
   {5/6}}{\sqrt [6]{{\pi }^{-1}}{\rho}^{7/6}}}

.. _density_functional_descriptions--pw91x-perdew-wang-1991-gga-exchange-functional:

PW91X: Perdew-Wang 1991 GGA Exchange Functional
===============================================

.. math::

   g=1/2\,E \left( 2\,\rho \left( s \right)  \right)

.. math::

   G=1/2\,E \left( 2\,\rho \left( s \right)  \right)

.. math::

   E \left( n \right) =-3/4\,{\frac {\sqrt [3]{3}\sqrt [3]{{\pi }^{2}}{n}^
   {4/3}F \left( S \right) }{\pi }}

.. math::

   S=1/12\,{\frac {\chi \left( s \right) {6}^{2/3}}{\sqrt [3]{{\pi }^{2}}}
   }

.. math::

   F \left( S \right) ={\frac {1+ 0.19645\,S{\it arcsinh} \left(  7.7956\,
   S \right) + \left(  0.2743- 0.1508\,{e^{-100\,{S}^{2}}} \right) {S}^{2}
   }{1+ 0.19645\,S{\it arcsinh} \left(  7.7956\,S \right) + 0.004\,{S}^{4}
   }}

.. _density_functional_descriptions--pw92c-perdew-wang-1992-gga-correlation-functional:

PW92C: Perdew-Wang 1992 GGA Correlation Functional
==================================================

Electron-gas correlation energy.

.. math::

   T=[ 0.031091, 0.015545, 0.016887]

.. math::

   U=[ 0.21370, 0.20548, 0.11125]

.. math::

   V=[ 7.5957, 14.1189, 10.357]

.. math::

   W=[ 3.5876, 6.1977, 3.6231]

.. math::

   X=[ 1.6382, 3.3662, 0.88026]

.. math::

   Y=[ 0.49294, 0.62517, 0.49671]

.. math::

   P=[1,1,1]

.. math::

   f=\rho\,\epsilon \left( \rho \left( a \right) ,\rho \left( b \right)
    \right)

.. math::

   \epsilon \left( \alpha,\beta \right) =e \left( r \left( \alpha,\beta
    \right) ,T_{{1}},U_{{1}},V_{{1}},W_{{1}},X_{{1}},Y_{{1}},P_{{1}}
    \right) -{\frac {e \left( r \left( \alpha,\beta \right) ,T_{{3}},U_{{3
   }},V_{{3}},W_{{3}},X_{{3}},Y_{{3}},P_{{3}} \right) \omega \left( \zeta
    \left( \alpha,\beta \right)  \right)  \left( 1- \left( \zeta \left(
   \alpha,\beta \right)  \right) ^{4} \right) }{c}}+ \left( e \left( r
    \left( \alpha,\beta \right) ,T_{{2}},U_{{2}},V_{{2}},W_{{2}},X_{{2}},Y
   _{{2}},P_{{2}} \right) -e \left( r \left( \alpha,\beta \right) ,T_{{1}}
   ,U_{{1}},V_{{1}},W_{{1}},X_{{1}},Y_{{1}},P_{{1}} \right)  \right)
   \omega \left( \zeta \left( \alpha,\beta \right)  \right)  \left( \zeta
    \left( \alpha,\beta \right)  \right) ^{4}

.. math::

   r \left( \alpha,\beta \right) =1/4\,\sqrt [3]{3}{4}^{2/3}\sqrt [3]{{
   \frac {1}{\pi \, \left( \alpha+\beta \right) }}}

.. math::

   \zeta \left( \alpha,\beta \right) ={\frac {\alpha-\beta}{\alpha+\beta}}

.. math::

   \omega \left( z \right) ={\frac { \left( 1+z \right) ^{4/3}+ \left( 1-z
    \right) ^{4/3}-2}{2\,\sqrt [3]{2}-2}}

.. math::

   e \left( r,t,u,v,w,x,y,p \right) =-2\,t \left( 1+ur \right) \ln
    \left( 1+1/2\,{\frac {1}{t \left( v\sqrt {r}+wr+x{r}^{3/2}+y{r}^{p+1}
    \right) }} \right)

.. math::

   c= 1.709921

.. _density_functional_descriptions--stest-test-for-number-of-electrons:

STEST: Test for number of electrons
===================================

.. math::

   g=\rho \left( s \right)

.. _density_functional_descriptions--tfke-thomas-fermi-kinetic-energy:

TFKE: Thomas-Fermi Kinetic Energy
=================================

Automatically generated Thomas-Fermi Kinetic Energy.

.. math::

   g={\it ctf}\, \left( \rho \left( s \right)  \right) ^{5/3}

.. math::

   {\it ctf}=3/10\,{2}^{2/3}{3}^{2/3} \left( {\pi }^{2} \right) ^{2/3}

.. _density_functional_descriptions--th1-tozer-and-handy-1998:

TH1: Tozer and Handy 1998
=========================

Density and gradient dependent first row exchange-correlation functional.

.. math::

   t=[7/6,4/3,3/2,5/3,4/3,3/2,5/3,{\frac {11}{6}},3/2,5/3,{\frac {11}{6}},
   2,3/2,5/3,{\frac {11}{6}},2,7/6,4/3,3/2,5/3,1]

.. math::

   u=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0]

.. math::

   v=[0,0,0,0,1,1,1,1,2,2,2,2,0,0,0,0,0,0,0,0,0]

.. math::

   w=[0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0]

.. math::

   \omega=[- 0.728255, 0.331699,- 1.02946, 0.235703,- 0.0876221, 0.140854,
    0.0336982,- 0.0353615, 0.00497930,- 0.0645900, 0.0461795,- 0.00757191,
   - 0.00242717, 0.0428140,- 0.0744891, 0.0386577,- 0.352519, 2.19805,-
    3.72927, 1.94441, 0.128877]

.. math::

   n=21

.. math::

   R_{{i}}= \left( \rho \left( a \right)  \right) ^{t_{{i}}}+ \left( \rho
    \left( b \right)  \right) ^{t_{{i}}}

.. math::

   S_{{i}}= \left( {\frac {\rho \left( a \right) -\rho \left( b \right) }{
   \rho}} \right) ^{2\,u_{{i}}}

.. math::

   X_{{i}}=1/2\,{\frac { \left( \sqrt {\sigma \left( {\it aa} \right) }
    \right) ^{v_{{i}}}+ \left( \sqrt {\sigma \left( {\it bb} \right) }
    \right) ^{v_{{i}}}}{{\rho}^{4/3\,v_{{i}}}}}

.. math::

   Y_{{i}}= \left( {\frac {\sigma \left( {\it aa} \right) +\sigma \left( {
   \it bb} \right) -2\,\sqrt {\sigma \left( {\it aa} \right) }\sqrt {
   \sigma \left( {\it bb} \right) }}{{\rho}^{8/3}}} \right) ^{w_{{i}}}

.. math::

   f=\sum _{i=1}^{n}\omega_{{i}}R_{{i}}S_{{i}}X_{{i}}Y_{{i}}

.. math::

   G=\sum _{i=1}^{n}1/2\,\omega_{{i}} \left( \rho \left( s \right)
    \right) ^{t_{{i}}} \left( \sqrt {\sigma \left( {\it ss} \right) }
    \right) ^{v_{{i}}} \left( {\frac {\sigma \left( {\it ss} \right) }{
    \left( \rho \left( s \right)  \right) ^{8/3}}} \right) ^{w_{{i}}}
    \left(  \left( \rho \left( s \right)  \right) ^{4/3\,v_{{i}}} \right)
   ^{-1}

.. _density_functional_descriptions--th2:

TH2: .
======

Density and gradient dependent first row exchange-correlation functional.

.. math::

   t=[{\frac {13}{12}},7/6,4/3,3/2,5/3,{\frac {17}{12}},3/2,5/3,{\frac {11
   }{6}},5/3,{\frac {11}{6}},2,5/3,{\frac {11}{6}},2,7/6,4/3,3/2,5/3]

.. math::

   u=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1]

.. math::

   v=[0,0,0,0,0,1,1,1,1,2,2,2,0,0,0,0,0,0,0]

.. math::

   w=[0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0]

.. math::

   \omega=[ 0.678831,- 1.75821, 1.27676,- 1.60789, 0.365610,- 0.181327,
    0.146973, 0.147141,- 0.0716917,- 0.0407167, 0.0214625,- 0.000768156,
    0.0310377,- 0.0720326, 0.0446562,- 0.266802, 1.50822,- 1.94515,
    0.679078]

.. math::

   n=19

.. math::

   R_{{i}}= \left( \rho \left( a \right)  \right) ^{t_{{i}}}+ \left( \rho
    \left( b \right)  \right) ^{t_{{i}}}

.. math::

   S_{{i}}= \left( {\frac {\rho \left( a \right) -\rho \left( b \right) }{
   \rho}} \right) ^{2\,u_{{i}}}

.. math::

   X_{{i}}=1/2\,{\frac { \left( \sqrt {\sigma \left( {\it aa} \right) }
    \right) ^{v_{{i}}}+ \left( \sqrt {\sigma \left( {\it bb} \right) }
    \right) ^{v_{{i}}}}{{\rho}^{4/3\,v_{{i}}}}}

.. math::

   Y_{{i}}= \left( {\frac {\sigma \left( {\it aa} \right) +\sigma \left( {
   \it bb} \right) -2\,\sqrt {\sigma \left( {\it aa} \right) }\sqrt {
   \sigma \left( {\it bb} \right) }}{{\rho}^{8/3}}} \right) ^{w_{{i}}}

.. math::

   f=\sum _{i=1}^{n}\omega_{{i}}R_{{i}}S_{{i}}X_{{i}}Y_{{i}}

.. math::

   G=\sum _{i=1}^{n}1/2\,\omega_{{i}} \left( \rho \left( s \right)
    \right) ^{t_{{i}}} \left( \sqrt {\sigma \left( {\it ss} \right) }
    \right) ^{v_{{i}}} \left( {\frac {\sigma \left( {\it ss} \right) }{
    \left( \rho \left( s \right)  \right) ^{8/3}}} \right) ^{w_{{i}}}
    \left(  \left( \rho \left( s \right)  \right) ^{4/3\,v_{{i}}} \right)
   ^{-1}

.. _density_functional_descriptions--th3:

TH3: .
======

Density and gradient dependent first and second row exchange-correlation functional.

.. math::

   t=[7/6,4/3,3/2,5/3,{\frac {17}{12}},3/2,5/3,{\frac {11}{6}},5/3,{\frac
   {11}{6}},2,5/3,{\frac {11}{6}},2,7/6,4/3,3/2,5/3,{\frac {13}{12}}]

.. math::

   u=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0]

.. math::

   v=[0,0,0,0,1,1,1,1,2,2,2,0,0,0,0,0,0,0,0]

.. math::

   w=[0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0]

.. math::

   \omega=[- 0.142542,- 0.783603,- 0.188875, 0.0426830,- 0.304953,
    0.430407,- 0.0997699, 0.00355789,- 0.0344374, 0.0192108,- 0.00230906,
    0.0235189,- 0.0331157, 0.0121316, 0.441190,- 2.27167, 4.03051,-
    2.28074, 0.0360204]

.. math::

   n=19

.. math::

   R_{{i}}= \left( \rho \left( a \right)  \right) ^{t_{{i}}}+ \left( \rho
    \left( b \right)  \right) ^{t_{{i}}}

.. math::

   S_{{i}}= \left( {\frac {\rho \left( a \right) -\rho \left( b \right) }{
   \rho}} \right) ^{2\,u_{{i}}}

.. math::

   X_{{i}}=1/2\,{\frac { \left( \sqrt {\sigma \left( {\it aa} \right) }
    \right) ^{v_{{i}}}+ \left( \sqrt {\sigma \left( {\it bb} \right) }
    \right) ^{v_{{i}}}}{{\rho}^{4/3\,v_{{i}}}}}

.. math::

   Y_{{i}}= \left( {\frac {\sigma \left( {\it aa} \right) +\sigma \left( {
   \it bb} \right) -2\,\sqrt {\sigma \left( {\it aa} \right) }\sqrt {
   \sigma \left( {\it bb} \right) }}{{\rho}^{8/3}}} \right) ^{w_{{i}}}

.. math::

   f=\sum _{i=1}^{n}\omega_{{i}}R_{{i}}S_{{i}}X_{{i}}Y_{{i}}

.. math::

   G=\sum _{i=1}^{n}1/2\,\omega_{{i}} \left( \rho \left( s \right)
    \right) ^{t_{{i}}} \left( \sqrt {\sigma \left( {\it ss} \right) }
    \right) ^{v_{{i}}} \left( {\frac {\sigma \left( {\it ss} \right) }{
    \left( \rho \left( s \right)  \right) ^{8/3}}} \right) ^{w_{{i}}}
    \left(  \left( \rho \left( s \right)  \right) ^{4/3\,v_{{i}}} \right)
   ^{-1}

.. _density_functional_descriptions--th4:

TH4: .
======

Density an gradient dependent first and second row exchange-correlation functional.

.. math::

   t=[7/6,4/3,3/2,5/3,{\frac {17}{12}},3/2,5/3,{\frac {11}{6}},5/3,{\frac
   {11}{6}},2,5/3,{\frac {11}{6}},2,7/6,4/3,3/2,5/3,{\frac {13}{12}}]

.. math::

   u=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0]

.. math::

   v=[0,0,0,0,1,1,1,1,2,2,2,0,0,0,0,0,0,0,0]

.. math::

   w=[0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0]

.. math::

   \omega=[ 0.0677353,- 1.06763,- 0.0419018, 0.0226313,- 0.222478,
    0.283432,- 0.0165089,- 0.0167204,- 0.0332362, 0.0162254,- 0.000984119,
    0.0376713,- 0.0653419, 0.0222835, 0.375782,- 1.90675, 3.22494,-
    1.68698,- 0.0235810]

.. math::

   n=19

.. math::

   R_{{i}}= \left( \rho \left( a \right)  \right) ^{t_{{i}}}+ \left( \rho
    \left( b \right)  \right) ^{t_{{i}}}

.. math::

   S_{{i}}= \left( {\frac {\rho \left( a \right) -\rho \left( b \right) }{
   \rho}} \right) ^{2\,u_{{i}}}

.. math::

   X_{{i}}=1/2\,{\frac { \left( \sqrt {\sigma \left( {\it aa} \right) }
    \right) ^{v_{{i}}}+ \left( \sqrt {\sigma \left( {\it bb} \right) }
    \right) ^{v_{{i}}}}{{\rho}^{4/3\,v_{{i}}}}}

.. math::

   Y_{{i}}= \left( {\frac {\sigma \left( {\it aa} \right) +\sigma \left( {
   \it bb} \right) -2\,\sqrt {\sigma \left( {\it aa} \right) }\sqrt {
   \sigma \left( {\it bb} \right) }}{{\rho}^{8/3}}} \right) ^{w_{{i}}}

.. math::

   f=\sum _{i=1}^{n}\omega_{{i}}R_{{i}}S_{{i}}X_{{i}}Y_{{i}}

.. math::

   G=\sum _{i=1}^{n}1/2\,\omega_{{i}} \left( \rho \left( s \right)
    \right) ^{t_{{i}}} \left( \sqrt {\sigma \left( {\it ss} \right) }
    \right) ^{v_{{i}}} \left( {\frac {\sigma \left( {\it ss} \right) }{
    \left( \rho \left( s \right)  \right) ^{8/3}}} \right) ^{w_{{i}}}
    \left(  \left( \rho \left( s \right)  \right) ^{4/3\,v_{{i}}} \right)
   ^{-1}

.. _density_functional_descriptions--thgfc:

THGFC: .
========

Density and gradient dependent first row exchange-correlation functional for closed shell systems. Total energies are improved by adding :math:`DN`, where :math:`N` is the number of electrons and :math:`D=0.1863`.

.. math::

   t=[7/6,4/3,3/2,5/3,4/3,3/2,5/3,{\frac {11}{6}},3/2,5/3,{\frac {11}{6}},
   2]

.. math::

   v=[0,0,0,0,1,1,1,1,2,2,2,2]

.. math::

   \omega=[- 0.864448, 0.565130,- 1.27306, 0.309681,- 0.287658, 0.588767,-
    0.252700, 0.0223563, 0.0140131,- 0.0826608, 0.0556080,- 0.00936227]

.. math::

   n=12

.. math::

   R_{{i}}= \left( \rho \left( a \right)  \right) ^{t_{{i}}}+ \left( \rho
    \left( b \right)  \right) ^{t_{{i}}}

.. math::

   X_{{i}}=1/2\,{\frac { \left( \sqrt {\sigma \left( {\it aa} \right) }
    \right) ^{v_{{i}}}+ \left( \sqrt {\sigma \left( {\it bb} \right) }
    \right) ^{v_{{i}}}}{{\rho}^{4/3\,v_{{i}}}}}

.. math::

   f=\sum _{i=1}^{n}\omega_{{i}}R_{{i}}X_{{i}}

.. math::

   G=\sum _{i=1}^{n}1/2\,{\frac {\omega_{{i}} \left( \rho \left( s
    \right)  \right) ^{t_{{i}}} \left( \sqrt {\sigma \left( {\it ss}
    \right) } \right) ^{v_{{i}}}}{{\rho}^{4/3\,v_{{i}}}}}

.. _density_functional_descriptions--thgfcfo:

THGFCFO: .
==========

Density and gradient dependent first row exchange-correlation functional. FCFO = FC + open shell fitting.

.. math::

   t=[7/6,4/3,3/2,5/3,4/3,3/2,5/3,{\frac {11}{6}},3/2,5/3,{\frac {11}{6}},
   2,3/2,5/3,{\frac {11}{6}},2,7/6,4/3,3/2,5/3]

.. math::

   u=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1]

.. math::

   v=[0,0,0,0,1,1,1,1,2,2,2,2,0,0,0,0,0,0,0,0]

.. math::

   w=[0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0]

.. math::

   \omega=[- 0.864448, 0.565130,- 1.27306, 0.309681,- 0.287658, 0.588767,-
    0.252700, 0.0223563, 0.0140131,- 0.0826608, 0.0556080,- 0.00936227,-
    0.00677146, 0.0515199,- 0.0874213, 0.0423827, 0.431940,- 0.691153,-
    0.637866, 1.07565]

.. math::

   n=20

.. math::

   R_{{i}}= \left( \rho \left( a \right)  \right) ^{t_{{i}}}+ \left( \rho
    \left( b \right)  \right) ^{t_{{i}}}

.. math::

   S_{{i}}= \left( {\frac {\rho \left( a \right) -\rho \left( b \right) }{
   \rho}} \right) ^{2\,u_{{i}}}

.. math::

   X_{{i}}=1/2\,{\frac { \left( \sqrt {\sigma \left( {\it aa} \right) }
    \right) ^{v_{{i}}}+ \left( \sqrt {\sigma \left( {\it bb} \right) }
    \right) ^{v_{{i}}}}{{\rho}^{4/3\,v_{{i}}}}}

.. math::

   Y_{{i}}= \left( {\frac {\sigma \left( {\it aa} \right) +\sigma \left( {
   \it bb} \right) -2\,\sqrt {\sigma \left( {\it aa} \right) }\sqrt {
   \sigma \left( {\it bb} \right) }}{{\rho}^{8/3}}} \right) ^{w_{{i}}}

.. math::

   f=\sum _{i=1}^{n}\omega_{{i}}R_{{i}}S_{{i}}X_{{i}}Y_{{i}}

.. math::

   G=\sum _{i=1}^{n}1/2\,\omega_{{i}} \left( \rho \left( s \right)
    \right) ^{t_{{i}}} \left( \sqrt {\sigma \left( {\it ss} \right) }
    \right) ^{v_{{i}}} \left( {\frac {\sigma \left( {\it ss} \right) }{
    \left( \rho \left( s \right)  \right) ^{8/3}}} \right) ^{w_{{i}}}
    \left(  \left( \rho \left( s \right)  \right) ^{4/3\,v_{{i}}} \right)
   ^{-1}

.. _density_functional_descriptions--thgfco:

THGFCO: .
=========

Density and gradient dependent first row exchange-correlation functional.

.. math::

   t=[7/6,4/3,3/2,5/3,4/3,3/2,5/3,{\frac {11}{6}},3/2,5/3,{\frac {11}{6}},
   2,3/2,5/3,{\frac {11}{6}},2,7/6,4/3,3/2,5/3]

.. math::

   u=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1]

.. math::

   v=[0,0,0,0,1,1,1,1,2,2,2,2,0,0,0,0,0,0,0,0]

.. math::

   w=[0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0]

.. math::

   \omega=[- 0.962998, 0.860233,- 1.54092, 0.381602,- 0.210208, 0.391496,-
    0.107660,- 0.0105324, 0.00837384,- 0.0617859, 0.0383072,- 0.00526905,-
    0.00381514, 0.0321541,- 0.0568280, 0.0288585, 0.368326,- 0.328799,-
    1.22595, 1.36412]

.. math::

   n=20

.. math::

   R_{{i}}= \left( \rho \left( a \right)  \right) ^{t_{{i}}}+ \left( \rho
    \left( b \right)  \right) ^{t_{{i}}}

.. math::

   S_{{i}}= \left( {\frac {\rho \left( a \right) -\rho \left( b \right) }{
   \rho}} \right) ^{2\,u_{{i}}}

.. math::

   X_{{i}}=1/2\,{\frac { \left( \sqrt {\sigma \left( {\it aa} \right) }
    \right) ^{v_{{i}}}+ \left( \sqrt {\sigma \left( {\it bb} \right) }
    \right) ^{v_{{i}}}}{{\rho}^{4/3\,v_{{i}}}}}

.. math::

   Y_{{i}}= \left( {\frac {\sigma \left( {\it aa} \right) +\sigma \left( {
   \it bb} \right) -2\,\sqrt {\sigma \left( {\it aa} \right) }\sqrt {
   \sigma \left( {\it bb} \right) }}{{\rho}^{8/3}}} \right) ^{w_{{i}}}

.. math::

   f=\sum _{i=1}^{n}\omega_{{i}}R_{{i}}S_{{i}}X_{{i}}Y_{{i}}

.. math::

   G=\sum _{i=1}^{n}1/2\,\omega_{{i}} \left( \rho \left( s \right)
    \right) ^{t_{{i}}} \left( \sqrt {\sigma \left( {\it ss} \right) }
    \right) ^{v_{{i}}} \left( {\frac {\sigma \left( {\it ss} \right) }{
    \left( \rho \left( s \right)  \right) ^{8/3}}} \right) ^{w_{{i}}}
    \left(  \left( \rho \left( s \right)  \right) ^{4/3\,v_{{i}}} \right)
   ^{-1}

.. _density_functional_descriptions--thgfl:

THGFL: .
========

Density dependent first row exchange-correlation functional for closed shell systems.

.. math::

   t=[7/6,4/3,3/2,5/3]

.. math::

   \omega=[- 1.06141, 0.898203,- 1.34439, 0.302369]

.. math::

   n=4

.. math::

   R_{{i}}= \left( \rho \left( a \right)  \right) ^{t_{{i}}}+ \left( \rho
    \left( b \right)  \right) ^{t_{{i}}}

.. math::

   f=\sum _{i=1}^{n}\omega_{{i}}R_{{i}}

.. _density_functional_descriptions--tpssc-tpss-correlation-functional:

TPSSC: TPSS Correlation Functional
==================================

J. Tao, J. P. Perdew, V. N. Staroverov, and G. E. Scuseria, `Phys. Rev. Lett. <https://dx.doi.org/10.1103/PhysRevLett.91.146401>`__ **91**, 146401 (2003).

.. _density_functional_descriptions--tpssx-tpss-exchange-functional:

TPSSX: TPSS Exchange Functional
===============================

J. Tao, J. P. Perdew, V. N. Staroverov, and G. E. Scuseria, `Phys. Rev. Lett. <https://dx.doi.org/10.1103/PhysRevLett.91.146401>`__ **91**, 146401 (2003).

.. _density_functional_descriptions--vsxc:

VSXC: .
=======

.. math::

   p=[- 0.98, 0.3271, 0.7035]

.. math::

   q=[- 0.003557,- 0.03229, 0.007695]

.. math::

   r=[ 0.00625,- 0.02942, 0.05153]

.. math::

   t=[- 0.00002354, 0.002134, 0.00003394]

.. math::

   u=[- 0.0001283,- 0.005452,- 0.001269]

.. math::

   v=[ 0.0003575, 0.01578, 0.001296]

.. math::

   \alpha=[ 0.001867, 0.005151, 0.00305]

.. math::

   g= \left( \rho \left( s \right)  \right) ^{4/3}F \left( \chi \left( s
    \right) ,{\it zs},p_{{1}},q_{{1}},r_{{1}},t_{{1}},u_{{1}},v_{{1}},
   \alpha_{{1}} \right) +{\it ds}\,\epsilon \left( \rho \left( s \right) ,0
    \right) F \left( \chi \left( s \right) ,{\it zs},p_{{2}},q_{{2}},r_{{2
   }},t_{{2}},u_{{2}},v_{{2}},\alpha_{{2}} \right)

.. math::

   G= \left( \rho \left( s \right)  \right) ^{4/3}F \left( \chi \left( s
    \right) ,{\it zs},p_{{1}},q_{{1}},r_{{1}},t_{{1}},u_{{1}},v_{{1}},
   \alpha_{{1}} \right) +{\it ds}\,\epsilon \left( \rho \left( s \right) ,0
    \right) F \left( \chi \left( s \right) ,{\it zs},p_{{2}},q_{{2}},r_{{2
   }},t_{{2}},u_{{2}},v_{{2}},\alpha_{{2}} \right)

.. math::

   f=F \left( x,z,p_{{3}},q_{{3}},r_{{3}},t_{{3}},u_{{3}},v_{{3}},\alpha_{
   {3}} \right)  \left( \epsilon \left( \rho \left( a \right) ,\rho
    \left( b \right)  \right) -\epsilon \left( \rho \left( a \right) ,0
    \right) -\epsilon \left( \rho \left( b \right) ,0 \right)  \right)

.. math::

   x= \left( \chi \left( a \right)  \right) ^{2}+ \left( \chi \left( b
    \right)  \right) ^{2}

.. math::

   {\it zs}={\frac {\tau \left( s \right) }{ \left( \rho \left( s \right)
    \right) ^{5/3}}}-{\it cf}

.. math::

   z={\frac {\tau \left( a \right) }{ \left( \rho \left( a \right)
    \right) ^{5/3}}}+{\frac {\tau \left( b \right) }{ \left( \rho \left( b
    \right)  \right) ^{5/3}}}-2\,{\it cf}

.. math::

   {\it ds}=1-{\frac { \left( \chi \left( s \right)  \right) ^{2}}{4\,{
   \it zs}+4\,{\it cf}}}

.. math::

   F \left( x,z,p,q,c,d,e,f,\alpha \right) ={\frac {p}{\lambda \left( x,z,
   \alpha \right) }}+{\frac {q{x}^{2}+cz}{ \left( \lambda \left( x,z,
   \alpha \right)  \right) ^{2}}}+{\frac {d{x}^{4}+e{x}^{2}z+f{z}^{2}}{
    \left( \lambda \left( x,z,\alpha \right)  \right) ^{3}}}

.. math::

   \lambda \left( x,z,\alpha \right) =1+\alpha\, \left( {x}^{2}+z \right)

.. math::

   {\it cf}=3/5\,{3}^{2/3} \left( {\pi }^{2} \right) ^{2/3}

.. math::

   T=[ 0.031091, 0.015545, 0.016887]

.. math::

   U=[ 0.21370, 0.20548, 0.11125]

.. math::

   V=[ 7.5957, 14.1189, 10.357]

.. math::

   W=[ 3.5876, 6.1977, 3.6231]

.. math::

   X=[ 1.6382, 3.3662, 0.88026]

.. math::

   Y=[ 0.49294, 0.62517, 0.49671]

.. math::

   P=[1,1,1]

.. math::

   \epsilon \left( \alpha,\beta \right) = \left( \alpha+\beta \right)
    \left( e \left( l \left( \alpha,\beta \right) ,T_{{1}},U_{{1}},V_{{1}}
   ,W_{{1}},X_{{1}},Y_{{1}},P_{{1}} \right) -{\frac {e \left( l \left(
   \alpha,\beta \right) ,T_{{3}},U_{{3}},V_{{3}},W_{{3}},X_{{3}},Y_{{3}},P
   _{{3}} \right) \omega \left( \zeta \left( \alpha,\beta \right)
    \right)  \left( 1- \left( \zeta \left( \alpha,\beta \right)  \right) ^
   {4} \right) }{c}}+ \left( e \left( l \left( \alpha,\beta \right) ,T_{{2
   }},U_{{2}},V_{{2}},W_{{2}},X_{{2}},Y_{{2}},P_{{2}} \right) -e \left( l
    \left( \alpha,\beta \right) ,T_{{1}},U_{{1}},V_{{1}},W_{{1}},X_{{1}},Y
   _{{1}},P_{{1}} \right)  \right) \omega \left( \zeta \left( \alpha,\beta
    \right)  \right)  \left( \zeta \left( \alpha,\beta \right)  \right) ^{
   4} \right)

.. math::

   l \left( \alpha,\beta \right) =1/4\,\sqrt [3]{3}{4}^{2/3}\sqrt [3]{{
   \frac {1}{\pi \, \left( \alpha+\beta \right) }}}

.. math::

   \zeta \left( \alpha,\beta \right) ={\frac {\alpha-\beta}{\alpha+\beta}}

.. math::

   \omega \left( z \right) ={\frac { \left( 1+z \right) ^{4/3}+ \left( 1-z
    \right) ^{4/3}-2}{2\,\sqrt [3]{2}-2}}

.. math::

   e \left( r,t,u,v,w,x,y,p \right) =-2\,t \left( 1+ur \right) \ln
    \left( 1+1/2\,{\frac {1}{t \left( v\sqrt {r}+wr+x{r}^{3/2}+y{r}^{p+1}
    \right) }} \right)

.. math::

   c= 1.709921

.. _density_functional_descriptions--vw-von-weizs-cker-kinetic-energy:

VW: von Weizsäcker kinetic energy
=================================

Automatically generated von Weizsäcker kinetic energy.

.. math::

   g={\frac {c\sigma \left( {\it ss} \right) }{\rho \left( s \right) }}

.. math::

   G={\frac {c\sigma \left( {\it ss} \right) }{\rho \left( s \right) }}

.. math::

   c=1/8

.. _density_functional_descriptions--vwn3-vosko-wilk-nusair-1980-iii-local-correlation-energy:

VWN3: Vosko-Wilk-Nusair (1980) III local correlation energy
===========================================================

VWN 1980(III) functional

.. math::

   x=1/4\,\sqrt [6]{3}{4}^{5/6}\sqrt [6]{{\frac {1}{\pi \,\rho}}}

.. math::

   \zeta={\frac {\rho \left( a \right) -\rho \left( b \right) }{\rho}}

.. math::

   f=\rho\,e

.. math::

   k=[ 0.0310907, 0.01554535,-1/6\,{\pi }^{-2}]

.. math::

   l=[- 0.409286,- 0.743294,- 0.228344]

.. math::

   m=[ 13.0720, 20.1231, 1.06835]

.. math::

   n=[ 42.7198, 101.578, 11.4813]

.. math::

   e=\Lambda+z \left( \lambda-\Lambda \right)

.. math::

   y={\frac {9}{8}}\, \left( 1+\zeta \right) ^{4/3}+{\frac {9}{8}}\,
    \left( 1-\zeta \right) ^{4/3}-9/4

.. math::

   \Lambda=q \left( k_{{1}},l_{{1}},m_{{1}},n_{{1}} \right)

.. math::

   \lambda=q \left( k_{{2}},l_{{2}},m_{{2}},n_{{2}} \right)

.. math::

   q \left( A,p,c,d \right) =A \left( \ln  \left( {\frac {{x}^{2}}{X
    \left( x,c,d \right) }} \right) +2\,c\arctan \left( {\frac {Q \left( c
   ,d \right) }{2\,x+c}} \right)  \left( Q \left( c,d \right)  \right) ^{-
   1}-cp \left( \ln  \left( {\frac { \left( x-p \right) ^{2}}{X \left( x,c
   ,d \right) }} \right) +2\, \left( c+2\,p \right) \arctan \left( {\frac
   {Q \left( c,d \right) }{2\,x+c}} \right)  \left( Q \left( c,d \right)
    \right) ^{-1} \right)  \left( X \left( p,c,d \right)  \right) ^{-1}
    \right)

.. math::

   Q \left( c,d \right) =\sqrt {4\,d-{c}^{2}}

.. math::

   X \left( i,c,d \right) ={i}^{2}+ci+d

.. math::

   z=4\,{\frac {y}{9\,\sqrt [3]{2}-9}}

.. _density_functional_descriptions--vwn5-vosko-wilk-nusair-1980-v-local-correlation-energy:

VWN5: Vosko-Wilk-Nusair (1980) V local correlation energy
=========================================================

VWN 1980(V) functional. The fitting parameters for :math:`\Delta\varepsilon_{c}(r_{s},\zeta)_{V}` appear in the caption of table 7 in the reference.

.. math::

   x=1/4\,\sqrt [6]{3}{4}^{5/6}\sqrt [6]{{\frac {1}{\pi \,\rho}}}

.. math::

   \zeta={\frac {\rho \left( a \right) -\rho \left( b \right) }{\rho}}

.. math::

   f=\rho\,e

.. math::

   k=[ 0.0310907, 0.01554535,-1/6\,{\pi }^{-2}]

.. math::

   l=[- 0.10498,- 0.325,- 0.0047584]

.. math::

   m=[ 3.72744, 7.06042, 1.13107]

.. math::

   n=[ 12.9352, 18.0578, 13.0045]

.. math::

   e=\Lambda+\alpha\,y \left( 1+h{\zeta}^{4} \right)

.. math::

   y={\frac {9}{8}}\, \left( 1+\zeta \right) ^{4/3}+{\frac {9}{8}}\,
    \left( 1-\zeta \right) ^{4/3}-9/4

.. math::

   h=4/9\,{\frac {\lambda-\Lambda}{ \left( \sqrt [3]{2}-1 \right) \alpha}}
   -1

.. math::

   \Lambda=q \left( k_{{1}},l_{{1}},m_{{1}},n_{{1}} \right)

.. math::

   \lambda=q \left( k_{{2}},l_{{2}},m_{{2}},n_{{2}} \right)

.. math::

   \alpha=q \left( k_{{3}},l_{{3}},m_{{3}},n_{{3}} \right)

.. math::

   q \left( A,p,c,d \right) =A \left( \ln  \left( {\frac {{x}^{2}}{X
    \left( x,c,d \right) }} \right) +2\,c\arctan \left( {\frac {Q \left( c
   ,d \right) }{2\,x+c}} \right)  \left( Q \left( c,d \right)  \right) ^{-
   1}-cp \left( \ln  \left( {\frac { \left( x-p \right) ^{2}}{X \left( x,c
   ,d \right) }} \right) +2\, \left( c+2\,p \right) \arctan \left( {\frac
   {Q \left( c,d \right) }{2\,x+c}} \right)  \left( Q \left( c,d \right)
    \right) ^{-1} \right)  \left( X \left( p,c,d \right)  \right) ^{-1}
    \right)

.. math::

   Q \left( c,d \right) =\sqrt {4\,d-{c}^{2}}

.. math::

   X \left( i,c,d \right) ={i}^{2}+ci+d

.. _density_functional_descriptions--xc-m05-m05-meta-gga-exchange-correlation-functional:

XC-M05: M05 Meta-GGA Exchange-Correlation Functional
====================================================

Here it means M05 exchange-correlation part which excludes HF exact exchange term. Y. Zhao, N. E. Schultz, and D. G. Truhlar, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.2126975>`__ **123**, 161103 (2005).

.. _density_functional_descriptions--xc-m05-2x-m05-2x-meta-gga-exchange-correlation-functional:

XC-M05-2X: M05-2X Meta-GGA Exchange-Correlation Functional
==========================================================

Here it means M05-2X exchange-correlation part which excludes HF exact exchange term. Y. Zhao, N. E. Schultz, and D. G. Truhlar, `J. Chem. Theory Comput. <https://dx.doi.org/10.1021/ct0502763>`__ **2**, 364 (2006).

.. _density_functional_descriptions--xc-m06-m06-meta-gga-exchange-correlation-functional:

XC-M06: M06 Meta-GGA Exchange-Correlation Functional
====================================================

Here it means M06 exchange-correlation part which excludes HF exact exchange term. Y. Zhao and D. G. Truhlar, Theor. Chem. Acc. 120, 215 (2008).

.. _density_functional_descriptions--xc-m06-2x-m06-2x-meta-gga-exchange-correlation-functional:

XC-M06-2X: M06-2X Meta-GGA Exchange-Correlation Functional
==========================================================

Here it means M06-2X exchange-correlation part which excludes HF exact exchange term. Y. Zhao and D. G. Truhlar, Theor. Chem. Acc. 120, 215 (2008).

.. _density_functional_descriptions--xc-m06-hf-m06-hf-meta-gga-exchange-correlation-functional:

XC-M06-HF: M06-HF Meta-GGA Exchange-Correlation Functional
==========================================================

Here it means M06-HF exchange-correlation part which excludes HF exact exchange term. Y. Zhao and D. G. Truhlar, J. Phys. Chem. A 110, 13126 (2006).

.. _density_functional_descriptions--xc-m06-l-m06-l-meta-gga-exchange-correlation-functional:

XC-M06-L: M06-L Meta-GGA Exchange-Correlation Functional
========================================================

Y. Zhao and D. G. Truhlar, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.2370993>`__ **125**, 194101 (2006).

.. _density_functional_descriptions--xc-m08-hx-m08-hx-meta-gga-exchange-correlation-functional:

XC-M08-HX: M08-HX Meta-GGA Exchange-Correlation Functional
==========================================================

Here it means M08-HX exchange-correlation part which excludes HF exact exchange term. Y. Zhao and D. G. Truhlar, `J. Chem. Theory Comput. <https://dx.doi.org/10.1021/ct800246v>`__ **4**, 1849 (2008).

.. _density_functional_descriptions--xc-m08-so-m08-so-meta-gga-exchange-correlation-functional:

XC-M08-SO: M08-SO Meta-GGA Exchange-Correlation Functional
==========================================================

Here it means M08-SO exchange-correlation part which excludes HF exact exchange term. Y. Zhao and D. G. Truhlar, `J. Chem. Theory Comput. <https://dx.doi.org/10.1021/ct800246v>`__ **4**, 1849 (2008).

.. _density_functional_descriptions--xc-m11-l-m11-l-exchange-correlation-functional:

XC-M11-L: M11-L Exchange-Correlation Functional
===============================================

R. Peverati and D. G. Truhlar, Journal of Physical Chemistry Letters 3, 117 (2012).

.. _density_functional_descriptions--xc-sogga-sogga-exchange-correlation-functional:

XC-SOGGA: SOGGA Exchange-Correlation Functional
===============================================

Y. Zhao and D. G. Truhlar, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.2912068>`__ **128**, 184109 (2008).

.. _density_functional_descriptions--xc-sogga11-sogga11-exchange-correlation-functional:

XC-SOGGA11: SOGGA11 Exchange-Correlation Functional
===================================================

R. Peverati, Y. Zhao and D. G. Truhlar, J. Phys. Chem. Lett. 2 (16), 1991 (2011).

.. _density_functional_descriptions--xc-sogga11-x-sogga11-x-exchange-correlation-functional:

XC-SOGGA11-X: SOGGA11-X Exchange-Correlation Functional
=======================================================

Here it means SOGGA11-X exchange-correlation part which excludes HF exact exchange term. R. Peverati and D. G. Truhlar, `J. Chem. Phys. <https://dx.doi.org/10.1063/1.3663871>`__ **135**, 191102 (2011).
