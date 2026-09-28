# Minimax Curvature of Smooth Flat-Endpoint Graphs

*Exact relaxed value, non-attainment, an explicit smooth approximation family with an exact global discrete minimiser, and quantitative convergence.*

---

## Abstract

We study the problem of minimising the maximum curvature of a $C^\infty$ graph $y=\gamma(x)$ over a fixed horizontal span $L$ with a fixed vertical rise $H$, horizontal endpoint tangents, and all endpoint derivatives of positive order equal to zero. After the tangent-sine change of variables, the problem becomes a Lipschitz-constrained integral optimisation. We prove that its infimum is $K^*=4|H|/(L^2+H^2)$ if $|H|<L$ and $2/L$ if $|H|\ge L$, and that it is not attained in the smooth flat-endpoint class. For $|H|<L$ the unique relaxed ($C^{1,1}$) minimiser is a pair of circular arcs, while for $|H|\ge L$ minimising graph sequences develop unbounded slope. We then construct an explicit $C^\infty$ finite-dimensional family $\mathcal A_N$, prove that its unique global minimiser is determined by a single strictly monotone scalar equation, and show that the corresponding maximal curvatures converge to the infimum with an explicit $O(1/N)$ bound and, for $|H|<L$, a first-order asymptotic expansion. These rates concern the constructed family only. The result is a constructive smooth approximation to the relaxed double-arc extremal.

---

## Contents

0. Introduction and summary of results
1. The problem and its formulation
2. Preliminaries: the tangent-sine transformation
3. The exact relaxed problem and non-attainment
4. The smooth finite-dimensional family and its exact global minimiser
5. Convergence and asymptotics
6. Numerical implementation
7. Numerical experiments
8. Relation to the literature
9. Concluding remarks and open problems

Appendix A. Reproducibility and implementation checks

---

## 0. Introduction and summary of results

**Motivation.** A curvature bound favours circular-arc behaviour, while $C^\infty$ flatness at the endpoints of a transition forbids the exact saturated-curvature profile. This creates a natural relaxation-and-approximation problem: determine the exact relaxed curvature threshold, understand why the smooth problem has no minimiser, and construct smooth curves whose excess maximal curvature can be quantified.

**Setting.** Let $a_0<a_1$ and $b_0,b_1\in\mathbb R$, and put $L=a_1-a_0$, $H=b_1-b_0$. We look for a $C^\infty$ **graph** $y=\gamma(x)$, $x\in[a_0,a_1]$, joining $(a_0,b_0)$ to $(a_1,b_1)$, all of whose derivatives of order $\ge 1$ vanish at both endpoints, and whose maximal curvature is as small as possible. The optimisation variable is the graph function $\gamma(x)$, not an arbitrary arc-length-parametrised planar curve; the arc length is free. This distinction is essential when comparing with the fixed-length minimax-curvature literature (§8). For $H\neq 0$ define

$$
K^*=\begin{cases}\dfrac{4|H|}{L^2+H^2}, & |H|<L,\\[3mm] \dfrac{2}{L}, & |H|\ge L.\end{cases}
$$

Three classes of curves appear and must not be confused:

$$
\underbrace{\mathcal A}_{\text{smooth flat-endpoint graphs}}\ \subset\ \underbrace{\mathcal B}_{C^{1,1}\text{ graphs, horizontal end tangents}}\ \subset\ \text{graphs}\ \subset\ \text{general planar curves (§8).}
$$

A minimiser in a larger class need not belong to a smaller one, and results for general planar curves do not automatically solve the graph problems studied here.

**Theorem A (sharp value for the flat-endpoint graph problem; non-attainment).** For the class $\mathcal A$ of smooth flat-endpoint graphs, the infimum of the maximal curvature equals $K^*$ (Theorem 3.2 and Corollary 5.2). Every $\gamma\in\mathcal A$ has maximal curvature strictly larger than $K^*$ (Corollary 3.6), so the infimum is not attained when $H\ne0$. If $|H|<L$, the same value is attained in the relaxed class $\mathcal B$ by a unique graph, the double circular arc of radius $(L^2+H^2)/(4|H|)$ (Proposition 3.4, Theorem 3.5). If $|H|\ge L$, the relaxed graph problem also fails to attain its infimum, and every minimising sequence has unbounded graph slope (Theorem 3.5, Proposition 3.7).

**Theorem B (exact smooth finite-dimensional minimiser).** For each $N\ge3$ there is an explicitly defined, nonempty family $\mathcal A_N\subset\mathcal A$, represented by $N-1$ signed-curvature coefficients subject to two equality constraints and one open condition, which contains a unique global minimiser $\gamma_N$ of the maximal curvature. Its coefficient vector is $c^N=t_N\hat c$, where $\hat c$ is an explicit saturated sign vector and $t_N$ is the unique solution of a strictly increasing scalar equation $g_N(t)=|H|$. In particular $J(\gamma_N)=t_N$ (Theorem 4.11).

**Theorem C (value and curve convergence).** The exact finite-dimensional minimisers satisfy $t_N>K^*$ for every $N$ and $t_N\to K^*$, with an explicit upper bound of order $1/N$ on the relative gap (Corollary 5.2). For $|H|<L$,

$$
\frac{t_N}{K^*}-1=\frac{2L^2}{L^2+H^2}\,\frac1N+O(N^{-2}),
\qquad\text{equivalently}\qquad
t_N-K^*=\frac{8|H|L^2}{(L^2+H^2)^2}\,\frac1N+O(N^{-2}),
$$

and $\gamma_N\to\gamma_{\rm arc}$ in $C^1$ with rate $O(1/N)$; in particular the lengths converge. The signed curvatures converge in $L^p$ for every finite $p$, but not uniformly (Theorem 5.4). These rates are properties of the family $\mathcal A_N$; they are not claimed to be optimal among all smooth approximations.

**Status of the results.** The bounded-curvature and saturated-curvature mechanisms behind the relaxed problem are classical (§8). *Theorem A* is an exact solution of a specific formulation: the fixed-span, fixed-rise graph problem with flat endpoint jets, its threshold $|H|=L$, its relaxation and the non-attainment result. *Theorem B* is the main constructive contribution: the discrete problem is not merely solved numerically, since its global minimiser is identified analytically, and what remains is one monotone scalar root problem. *Theorem C* is the quantitative contribution; the explicit first-order coefficient is more distinctive than the relaxed value itself.

**Contributions.**
- We reduce the flat-endpoint graph problem to a one-dimensional Lipschitz optimisation and determine its exact relaxed value.
- We prove non-attainment in the $C^\infty$ flat-endpoint class and identify the unique $C^{1,1}$ double-arc relaxed minimiser when $|H|<L$.
- We construct a $C^\infty$ finite-dimensional family $\mathcal A_N$ whose global minimiser is characterised exactly by a saturated coefficient profile and one monotone scalar equation.
- We prove value convergence with an explicit $O(1/N)$ bound and derive a first-order asymptotic expansion for $|H|<L$.
- We prove $C^1$ convergence of the curves and $L^p$, but not $L^\infty$, convergence of the signed curvatures.

The saturated-curvature geometry itself is classical; the contribution is the exact treatment of this graph/flatness formulation and the explicit smooth approximation theory.

**The three regimes.**
- *$H=0$.* The constant graph is the unique minimiser in $\mathcal B$ (and lies in $\mathcal A$), with $J=0$ (Remark 3.8).
- *$0<|H|<L$.* The relaxed problem has the double arc as unique minimiser; the smooth problem has no minimiser.
- *$|H|\ge L$.* The relaxed infimum $2/L$ is not attained even in $\mathcal B$; minimising sequences necessarily have unbounded slope. This is a degeneracy of the graph representation, not a statement about general planar curves.

**Roadmap.**
- *Continuous problem (§§2–3):* sharp envelope $\to$ double arc $\to$ non-attainment.
- *Discrete smooth problem (§4):* positive basis $\to$ comparison principle $\to$ exact global minimiser.
- *Asymptotics (§5):* discrete minimiser $\to$ value convergence $\to$ $C^1$ and $L^p$ convergence.

**Proof architecture.**

```
curvature of the graph y = gamma(x)
        |
        v
u = gamma' / sqrt(1 + gamma'^2)          (sine of the tangent angle)
        |-- |u'| = curvature             (Lemma 2.2)
        |-- H = int F(u) dx              (F increasing)
        v
Lipschitz envelope  u <= K T             (Lemma 2.3)
        v
double circular arc                      (Section 3)
        |-- exact relaxed value K*
        |-- non-attainment in the smooth class
        v
smooth hats B_j  ->  curvature coefficients c_j      (Section 4)
        v
summation-by-parts comparison  u_c <= t Psi_N         (Lemmas 4.9, 4.10)
        v
c = t_N c_hat, with t_N the root of one monotone equation   (Theorem 4.11)
        v
value, curve and curvature asymptotics   (Section 5)
```

---

## 1. The problem and its formulation

### 1.1 Data, admissible class, cost

Throughout, $I=[a_0,a_1]$, $L=a_1-a_0>0$, $H=b_1-b_0$. Here $C^\infty(I)$ denotes the functions on the closed interval all of whose derivatives exist on the open interval and extend continuously to $I$; derivatives at $a_0,a_1$ are understood one-sidedly.

**Definition 1.1 (admissible class).**

$$
\mathcal A=\Big\{\gamma\in C^\infty(I):\ \gamma(a_0)=b_0,\ \gamma(a_1)=b_1,\ \gamma^{(n)}(a_0)=\gamma^{(n)}(a_1)=0\ \ \text{for all } n\ge 1\Big\}.
$$

*Remark 1.2.* The flatness condition must be imposed for $n\ge1$ only; for $n=0$ it would contradict the endpoint values unless $b_0=b_1=0$. If $\gamma\in C^\infty(\mathbb R)$ is constant on $(-\infty,a_0]$ and on $[a_1,\infty)$, then its restriction to $I$ satisfies the flatness conditions (all derivatives of order $\ge 1$ vanish on the open half-lines and are continuous). This is the only direction of this equivalence that will be used.

*Remark 1.2a (dimensions).* $x$, $y$, $L$ and $H$ have the dimension of length; curvatures such as $K^*=4H/(L^2+H^2)$ have dimension $1/\text{length}$; relative gaps $t_N/K^*-1$ and the resolution $N$ are dimensionless. All formulas below are consistent with this, which is a useful check on the explicit expressions.

**Definition 1.3 (curvature and cost).** For $\gamma\in C^2(I)$,

$$
\kappa_\gamma(x)=\frac{|\gamma''(x)|}{\big(1+\gamma'(x)^2\big)^{3/2}},\qquad J(\gamma)=\max_{x\in I}\kappa_\gamma(x).
$$

The maximum exists because $\kappa_\gamma$ is continuous on the compact interval $I$.

**Problem (P).** Find $\gamma^*\in\mathcal A$ such that

$$
J(\gamma^*)=\inf_{\gamma\in\mathcal A}J(\gamma).
$$

### 1.2 The relaxed class

**Definition 1.4.**

$$
\mathcal B=\Big\{\gamma\in W^{2,\infty}(I):\ \gamma(a_i)=b_i,\ \gamma'(a_i)=0,\ i=0,1\Big\},
$$

where each element of $W^{2,\infty}(I)$ is identified with its canonical $C^{1,1}$ representative: $\gamma\in C^1(I)$, $\gamma'$ is Lipschitz, and $\gamma''\in L^\infty(I)$ exists almost everywhere. For $\gamma\in\mathcal B$, $\gamma''$ exists almost everywhere and is essentially bounded, and we set $J(\gamma)=\operatorname{ess\,sup}_I\kappa_\gamma$. Clearly $\mathcal A\subset\mathcal B$, and the two definitions of $J$ agree on $\mathcal A$ since $\kappa_\gamma$ is then continuous.

### 1.3 Normalisation

The maps $x\mapsto x-a_0$, $y\mapsto y-b_0$ and $y\mapsto -y$ preserve curvature and map $\mathcal A$ and $\mathcal B$ onto the corresponding classes for the transformed data. Therefore we may and do assume:

> **Standing assumption.** $a_0=0$, $b_0=0$, $H>0$. Thus $I=[0,L]$ and the conditions are $\gamma(0)=0$, $\gamma(L)=H$.

(The case $H=0$ is settled in Remark 3.8.) After normalisation $H$ denotes the positive rise; for general data it is to be read as $|b_1-b_0|$ in all formulas below. Results for general data are recovered by

$$
\gamma(x)=b_0+\operatorname{sgn}(H)\,\tilde\gamma(x-a_0),
$$

where $\tilde\gamma$ solves the normalised problem with height $|H|$.

We use throughout the **tent function** and the **sign function**

$$
T(x)=\min(x,\,L-x),\qquad \sigma(x)=\operatorname{sgn}(L/2-x),\qquad x\in[0,L].
$$

---

## 2. Preliminaries: the tangent-sine transformation

### 2.1 The functions $G$ and $F$

Define

$$
G(p)=\frac{p}{\sqrt{1+p^2}}\quad(p\in\mathbb R),\qquad F(v)=\frac{v}{\sqrt{1-v^2}}\quad(v\in(-1,1)).
$$

**Lemma 2.1.**
1. $G:\mathbb R\to(-1,1)$ and $F:(-1,1)\to\mathbb R$ are smooth, odd, strictly increasing and mutually inverse. Moreover $G'(p)=(1+p^2)^{-3/2}\in(0,1]$ and $F'(v)=(1-v^2)^{-3/2}\ge 1$, and $F'$ is increasing on $[0,1)$.
2. For $0\le a\le 1$: $\displaystyle\int_0^aF(v)\,dv=1-\sqrt{1-a^2}$ (an improper but convergent integral when $a=1$).
3. For $\tfrac12\le v<1$: $F(v)\ge \dfrac{1}{2\sqrt{2(1-v)}}$.

*Proof.* (1) Direct differentiation gives
$$G'(p)=(1+p^2)^{-1/2}-p^2(1+p^2)^{-3/2}=(1+p^2)^{-3/2},$$
$$F'(v)=(1-v^2)^{-1/2}+v^2(1-v^2)^{-3/2}=(1-v^2)^{-3/2}.$$
If $v=G(p)$, then $v^2(1+p^2)=p^2$ and $\operatorname{sgn}v=\operatorname{sgn}p$, hence $p=v/\sqrt{1-v^2}=F(v)$. Monotonicity of $F'$ on $[0,1)$ is clear.

(2) We have $\frac{d}{dv}\big(-\sqrt{1-v^2}\big)=F(v)$. The case $a=1$ follows by monotone convergence, since $F\ge0$ on $[0,1)$.

(3) Write $F(v)=v/\sqrt{(1-v)(1+v)}$ and use $v\ge\frac12$ and $1+v\le 2$. $\blacksquare$

### 2.2 The tangent-sine variable

For a graph, $G(\gamma')=\sin\theta$, where $\theta$ is the angle between the tangent and the horizontal.

**Lemma 2.2.** Let $\gamma\in\mathcal B$ and $u:=G\circ\gamma'$.
1. $u$ is Lipschitz on $[0,L]$, $\max_{[0,L]}|u|<1$, $u(0)=u(L)=0$, and $\gamma'=F(u)$.
2. $u'=\gamma''/(1+\gamma'^2)^{3/2}$ almost everywhere. Hence $\kappa_\gamma=|u'|$ a.e. and $J(\gamma)=\|u'\|_{L^\infty}=\operatorname{Lip}(u)$.
3. $H=\displaystyle\int_0^LF\big(u(x)\big)\,dx$.
4. Conversely, suppose $u$ is Lipschitz on $[0,L]$ with $\max|u|<1$, $u(0)=u(L)=0$ and $\int_0^LF(u)=H$. Then $\gamma(x):=\int_0^xF(u)$ belongs to $\mathcal B$, and its tangent-sine variable is $u$.
5. If $\gamma\in\mathcal A$, then $u\in C^\infty[0,L]$ and $\kappa_\gamma=|u'|$ everywhere.

*Proof.*

(1) $\gamma'$ is Lipschitz and $G$ is $1$-Lipschitz because $|G'|\le1$, so $u$ is Lipschitz. $u$ is continuous with values in $(-1,1)$ on a compact set, so $\max|u|<1$. Next, $u(0)=G(\gamma'(0))=G(0)=0$, and similarly $u(L)=0$. Finally $\gamma'=F(u)$ because $F=G^{-1}$.

(2) At every point where $\gamma'$ is differentiable (almost every point), the chain rule gives $u'=G'(\gamma')\gamma''=\gamma''/(1+\gamma'^2)^{3/2}$. For a Lipschitz function on an interval, $\|u'\|_{L^\infty}=\operatorname{Lip}(u)$. Indeed, a Lipschitz function is absolutely continuous and differentiable almost everywhere. On the one hand, $|u(x)-u(y)|=\big|\int_y^xu'\big|\le\|u'\|_\infty|x-y|$, so $\operatorname{Lip}(u)\le\|u'\|_\infty$. On the other hand, at every point $x$ of differentiability, $|u'(x)|=\lim_{\delta\to0}|u(x+\delta)-u(x)|/|\delta|\le\operatorname{Lip}(u)$, so $\|u'\|_\infty\le\operatorname{Lip}(u)$.

(3) $\gamma$ is $C^1$, so $H=\gamma(L)-\gamma(0)=\int_0^L\gamma'=\int_0^LF(u)$.

(4) Let $\bar v:=\max|u|<1$. On $[-\bar v,\bar v]$, $F$ is $C^1$ with $|F'|\le F'(\bar v)$, so $F\circ u$ is Lipschitz and $\gamma\in W^{2,\infty}$. The boundary values are $\gamma(0)=0$ and $\gamma(L)=H$, and the boundary slopes are $\gamma'(0)=F(u(0))=F(0)=0=\gamma'(L)$. Finally $G(\gamma')=G(F(u))=u$.

(5) $u=G\circ\gamma'$ is a composition of smooth maps, and the formula in (2) holds pointwise. $\blacksquare$

**Lemma 2.3 (tent bound).** If $u$ is Lipschitz on $[0,L]$ with constant $K$ and $u(0)=u(L)=0$, then $u\le KT$ on $[0,L]$.

*Proof.* For every $x\in[0,L]$, $u(x)=u(x)-u(0)\le Kx$ and $u(x)=u(x)-u(L)\le K(L-x)$. $\blacksquare$

The tent $KT$ is itself $K$-Lipschitz and vanishes at both endpoints, so it is the *pointwise maximal* function among all $K$-Lipschitz functions vanishing at $0$ and $L$. Since $F$ is increasing, it therefore also maximises the height integral $\int_0^LF(u)$ among all tangent-sine variables with Lipschitz constant at most $K$ (whenever $KT<1$).

*Reformulation.* By Lemma 2.2(1)–(4), the map $\gamma\mapsto G\circ\gamma'$ is a bijection from $\mathcal B$ onto
$$
\mathcal U=\Big\{u\ \text{Lipschitz on }[0,L]:\ u(0)=u(L)=0,\ \max_{[0,L]}|u|<1,\ \int_0^LF(u)=H\Big\},
$$
with inverse $u\mapsto\int_0^xF(u)$, and $J(\gamma)=\operatorname{Lip}(u)$. Hence minimising $J$ over $\mathcal B$ is equivalent to minimising $\operatorname{Lip}(u)$ over $\mathcal U$.

*Why this reduction matters.* $u=\gamma'/\sqrt{1+\gamma'^2}$ is the sine of the tangent angle, and $u'=\gamma''/(1+\gamma'^2)^{3/2}$ is the signed curvature with $x$ as the graph parameter. Thus the geometric $L^\infty$-curvature objective becomes the $L^\infty$ norm of a first derivative, while the endpoint height becomes a monotone integral constraint. The continuous extremal problem is consequently a *Lipschitz-envelope problem*, which Lemma 2.3 solves.

*Terminology.* For $\gamma\in\mathcal B$ we call $k:=u'$ (defined almost everywhere, as an element of $L^\infty$) the **signed curvature**, and $\kappa=|k|$ the (unsigned) **curvature**. For $\gamma\in\mathcal A$ both are continuous and defined everywhere. Statements about $L^\infty$ norms of $k$ refer to equivalence classes, so representatives differing on null sets are identified.

### 2.3 The rise of a double arc

For $\ell>0$ let $T_\ell(y)=\min(y,\ell-y)$ on $[0,\ell]$, so that $T=T_L$. For $0<K\le 2/\ell$ put

$$
Y_\ell(K):=\int_0^\ell F\big(K\,T_\ell(y)\big)\,dy .
$$

The integrand is nonnegative. When $K=2/\ell$ it is $+\infty$ only at $y=\ell/2$, and the integral is understood in the Lebesgue sense.

For $0<H<\ell$ define

$$
K^*(\ell):=K^*(\ell,H):=\frac{4H}{\ell^2+H^2}.
$$

The rise $H$ is fixed throughout, so we usually suppress it from the notation.

**Lemma 2.4.**
1. $Y_\ell(K)=\dfrac2K\Big(1-\sqrt{1-K^2\ell^2/4}\Big)$. In particular $Y_\ell(2/\ell)=\ell$.
2. $Y_\ell$ is continuous and strictly increasing on $(0,2/\ell]$, and $Y_\ell(K)\to0$ as $K\to0$.
3. $Y_\ell\in C^1(0,2/\ell)$ and $Y_\ell'(K)=\int_0^\ell F'(KT_\ell)\,T_\ell\,dy\ \ge\ \ell^2/4$.
4. If $0<H<\ell$, then $K^*(\ell)\in(0,2/\ell)$, $Y_\ell(K^*(\ell))=H$, and $K^*(\ell)$ is the unique solution of $Y_\ell(K)=H$ in $(0,2/\ell]$. Moreover
$$\frac2\ell-K^*(\ell)=\frac{2(\ell-H)^2}{\ell(\ell^2+H^2)}.$$
5. *(Shift identity.)* For $0\le c<L/2$ and $0<K\le 2/(L-2c)$,
$$\int_0^LF\big(K\,(T-c)_+\big)\,dx=Y_{L-2c}(K).$$

*Proof.*

(1) $T_\ell$ is symmetric about $\ell/2$, so
$$Y_\ell(K)=2\int_0^{\ell/2}F(Ky)\,dy=\frac2K\int_0^{K\ell/2}F(v)\,dv.$$
Now apply Lemma 2.1(2) with $a=K\ell/2\le1$.

(2) Continuity follows from the formula in (1). For strict monotonicity, let $K_1<K_2$. Since $T_\ell>0$ on $(0,\ell)$ and $F$ is strictly increasing, $F(K_1T_\ell)<F(K_2T_\ell)$ on $(0,\ell)$, and both integrals are finite by (1). For the limit, use $1-\sqrt{1-s}\le s$ for $s\in[0,1]$: this gives $Y_\ell(K)\le \frac2K\cdot\frac{K^2\ell^2}{4}=\frac{K\ell^2}2\to0$.

(3) Fix $K'<2/\ell$. For $K\le K'$, the $K$-derivative of the integrand is $F'(KT_\ell)T_\ell$, which is bounded by $F'(K'\ell/2)\,\ell/2$. Hence we may differentiate under the integral. Since $F'\ge 1$, we get $Y_\ell'(K)\ge\int_0^\ell T_\ell=\ell^2/4$.

(4) The identity for $2/\ell-K^*(\ell)$ is a direct computation:
$$\frac2\ell-\frac{4H}{\ell^2+H^2}=\frac{2\ell^2+2H^2-4H\ell}{\ell(\ell^2+H^2)}.$$
Its right-hand side is positive, so $K^*(\ell)<2/\ell$.

Now let $K=K^*(\ell)$. Then $K\ell/2=\frac{2H\ell}{\ell^2+H^2}$, and
$$1-\Big(\frac{K\ell}2\Big)^2=\frac{(\ell^2-H^2)^2}{(\ell^2+H^2)^2}.$$
Since $H<\ell$, the square root of this is $\frac{\ell^2-H^2}{\ell^2+H^2}$, so $1-\sqrt{\,\cdot\,}=\frac{2H^2}{\ell^2+H^2}$. Therefore
$$Y_\ell(K)=\frac{\ell^2+H^2}{2H}\cdot\frac{2H^2}{\ell^2+H^2}=H.$$
Uniqueness follows from (2).

(5) Both $T$ and $(T-c)_+$ are symmetric about $L/2$, and $(T-c)_+=0$ on $[0,c]$. Hence
$$\int_0^LF\big(K(T-c)_+\big)=2\int_c^{L/2}F\big(K(x-c)\big)\,dx=2\int_0^{(L-2c)/2}F(Ky)\,dy=Y_{L-2c}(K),$$
using the first identity in the proof of (1). $\blacksquare$

*Geometric meaning.* With $R=1/K$, part (1) reads
$$Y_\ell(K)=2\Big(R-\sqrt{R^2-\ell^2/4}\Big).$$
This is the height gained by two circular arcs of radius $R$ that each start horizontally and span a horizontal distance $\ell/2$ (Pythagoras). The function $KT_\ell$ is precisely the tangent-sine variable of this double arc.

---

## 3. The exact relaxed problem and non-attainment

**Definition 3.1.** Set $K^*:=K^*(L)=\dfrac{4H}{L^2+H^2}$ if $H<L$, and $K^*:=\dfrac2L$ if $H\ge L$.

**Theorem 3.2 (lower bound).** $J(\gamma)\ge K^*$ for every $\gamma\in\mathcal B$.

*Proof.* Let $\gamma\in\mathcal B$, let $u$ be its tangent-sine variable, and let $K:=J(\gamma)=\operatorname{Lip}(u)$ (Lemma 2.2). By Lemma 2.3, $u\le KT$.

*Step 1: if $K<2/L$, then $H\le Y_L(K)$.* Indeed, $KT\le KL/2<1$ on $[0,L]$, so both $u$ and $KT$ take values in $(-1,1)$. Since $F$ is increasing, $F(u)\le F(KT)$ pointwise. Integrating and using Lemma 2.2(3) gives $H\le\int_0^LF(KT)=Y_L(K)$.

*Step 2: the case $H\ge L$.* If $K<2/L$, Step 1 and Lemma 2.4(2) give $H\le Y_L(K)<Y_L(2/L)=L\le H$, a contradiction. Hence $K\ge 2/L=K^*$.

*Step 3: the case $H<L$.* If $K\ge2/L$, then $K>K^*$, since $H<L$ implies $K^*<2/L$ (Lemma 2.4(4)). If $K<2/L$, Step 1 gives $Y_L(K)\ge H=Y_L(K^*)$, and strict monotonicity of $Y_L$ (Lemma 2.4(2)) yields $K\ge K^*$. $\blacksquare$

In words: a curve whose curvature never exceeds $K$ cannot rise, over $[0,L]$, more than the double arc of curvature $K$.

**Definition 3.3 (double arc).** For $0<H<L$ let $R^*=1/K^*=(L^2+H^2)/(4H)$, and define

$$
u_{\rm arc}:=K^*T,\qquad \gamma_{\rm arc}(x):=\int_0^xF\big(K^*T(\xi)\big)\,d\xi .
$$

**Proposition 3.4.** Let $0<H<L$.
1. $\gamma_{\rm arc}\in\mathcal B$ and $J(\gamma_{\rm arc})=K^*$.
2. Explicitly,
$$\gamma_{\rm arc}(x)=\begin{cases}R^*-\sqrt{R^{*2}-x^2}, & 0\le x\le L/2,\\[1mm] H-R^*+\sqrt{R^{*2}-(L-x)^2}, & L/2\le x\le L.\end{cases}$$
The graph consists of two circular arcs of radius $R^*$, centred at $(0,R^*)$ and $(L,H-R^*)$. They are tangent to $y=0$ at the origin, tangent to $y=H$ at $(L,H)$, and tangent to each other at $(L/2,H/2)$.
3. $\gamma_{\rm arc}\in C^{1,1}(I)$, but $\gamma_{\rm arc}\notin C^2(I)$; in particular $\gamma_{\rm arc}\notin\mathcal A$.

*Proof.*

(1) $u_{\rm arc}=K^*T$ is Lipschitz with $\operatorname{Lip}(u_{\rm arc})=K^*$, because $|T'|=1$ a.e. Its maximum is $K^*L/2<1$ (Lemma 2.4(4)), and $u_{\rm arc}(0)=u_{\rm arc}(L)=0$. Also $\int_0^LF(u_{\rm arc})=Y_L(K^*)=H$. Lemma 2.2(4) gives $\gamma_{\rm arc}\in\mathcal B$ with tangent-sine variable $u_{\rm arc}$, and Lemma 2.2(2) gives $J(\gamma_{\rm arc})=K^*$.

(2) *Left half.* For $0\le x\le L/2$ we have $K^*x\le K^*L/2<1$, so Lemma 2.1(2) gives
$$\int_0^xF(K^*s)\,ds=\frac{1-\sqrt{1-K^{*2}x^2}}{K^*}=R^*-\sqrt{R^{*2}-x^2}.$$

*Right half.* For $x\ge L/2$, the symmetry of $T$ gives $\int_x^LF(K^*T)=\int_0^{L-x}F(K^*s)\,ds$. Hence $\gamma_{\rm arc}(x)=H-\int_x^LF(K^*T)$ has the stated form.

*Circles.* The points $(x,y)$ with $x^2+(y-R^*)^2=R^{*2}$ and $y\le R^*$ satisfy $y=R^*-\sqrt{R^{*2}-x^2}$; the right arc is analogous. Tangency at the midpoint follows from $\gamma_{\rm arc}\in C^1$, and $\gamma_{\rm arc}(L/2)=H/2$ because the two halves contribute equally.

(3) $\gamma_{\rm arc}\in C^{1,1}$ by (1). On $(0,L/2)$ we have $\gamma_{\rm arc}''(x)=K^*F'(K^*x)$, so the one-sided second derivative at $0$ is
$$\gamma_{\rm arc}''(0^+)=K^*\neq0,$$
whereas every element of $\mathcal A$ satisfies $\gamma''(0)=0$. This endpoint obstruction alone shows $\gamma_{\rm arc}\notin\mathcal A$. In addition, on $(L/2,L)$, by symmetry, $\gamma_{\rm arc}''(x)=-K^*F'\big(K^*(L-x)\big)$; the one-sided limits of $\gamma_{\rm arc}''$ at $L/2$ are $\pm K^*F'(K^*L/2)\neq0$, so $\gamma_{\rm arc}''$ jumps and $\gamma_{\rm arc}\notin C^2(I)$. $\blacksquare$

**Theorem 3.5 (equality cases).**
1. If $0<H<L$, $\gamma\in\mathcal B$ and $J(\gamma)=K^*$, then $\gamma=\gamma_{\rm arc}$. That is, $\gamma_{\rm arc}$ is the unique minimiser in $\mathcal B$, as a graph function.
2. If $H\ge L$, then $J(\gamma)>2/L$ for every $\gamma\in\mathcal B$.

*Proof.*

(1) Here $K=K^*<2/L$, so Step 1 of the proof of Theorem 3.2 applies:
$$0\le\int_0^L\big(F(K^*T)-F(u)\big)=Y_L(K^*)-H=0.$$
The integrand is continuous and nonnegative, so it vanishes identically. Since $F$ is injective, $u=K^*T$. Hence $\gamma'=F(u)=\gamma_{\rm arc}'$, and $\gamma=\gamma_{\rm arc}$ because both vanish at $0$.

(2) By Theorem 3.2, $J(\gamma)\ge 2/L$; suppose $J(\gamma)=2/L$. Then $u\le (2/L)T$ (Lemma 2.3), and $v_0:=\max u<1$ (Lemma 2.2(1)).

The set $U=\{x:(2/L)T(x)>v_0\}$ is an open interval of positive length around $L/2$. On $[0,L]\setminus\{L/2\}$ we have $(2/L)T<1$, so $F(u)\le F\big((2/L)T\big)$, and the inequality is strict on $U\setminus\{L/2\}$.

Since $\int_0^LF\big((2/L)T\big)=Y_L(2/L)=L$ is finite, we conclude $H=\int_0^LF(u)<L\le H$, a contradiction. $\blacksquare$

**Corollary 3.6.** $J(\gamma)>K^*$ for every $\gamma\in\mathcal A$.

*Proof.* We have $\mathcal A\subset\mathcal B$, so $J\ge K^*$ by Theorem 3.2. If $H<L$, equality would force $\gamma=\gamma_{\rm arc}\notin\mathcal A$ (Theorem 3.5(1) and Proposition 3.4(3)). If $H\ge L$, equality is impossible by Theorem 3.5(2). $\blacksquare$

Consequently, Problem (P) has a solution if and only if $\inf_{\mathcal A}J$ is attained. We prove in §5 that $\inf_{\mathcal A}J=K^*$, so (P) has **no solution**.

**Proposition 3.7 (degeneracy when $H\ge L$).** If $H\ge L$ and $(\gamma_k)\subset\mathcal B$ satisfies $J(\gamma_k)\to 2/L$, then $\|\gamma_k'\|_\infty\to\infty$.

*Proof.* Suppose not. Then along a subsequence $\|\gamma_k'\|_\infty\le P$ for some $P<\infty$, so the tangent-sine variables satisfy $u_k\le v_P:=G(P)<1$. Writing $J_k=J(\gamma_k)$, Lemma 2.3 gives
$$u_k\le w_k:=\min(J_kT,\,v_P),\qquad\text{hence}\qquad H=\int F(u_k)\le\int F(w_k).$$

As $k\to\infty$, $w_k\to w:=\min\big((2/L)T,\,v_P\big)$ pointwise, with $0\le F(w_k)\le F(v_P)$. By dominated convergence, $H\le\int_0^LF(w)$.

On the nonempty open interval where $(2/L)T>v_P$ we have $w<(2/L)T$. Therefore $\int F(w)<\int F\big((2/L)T\big)=L\le H$, a contradiction. $\blacksquare$

Thus, for $H\ge L$ the fixed-span graph representation becomes degenerate: every minimising sequence has unbounded graph slope. This does not by itself characterise the limiting behaviour in a larger class of parametrised planar curves; see Remark 5.5.

*Remark 3.8 (the case $H=0$).* If $b_0=b_1$, the constant graph $\gamma\equiv b_0$ lies in $\mathcal A$ and has $J=0$. It is the unique minimiser in $\mathcal B$: if $J(\gamma)=0$, then $u'=0$ a.e. by Lemma 2.2(2), so $u$ is constant, and $u(0)=0$ forces $u\equiv0$, hence $\gamma'\equiv0$ and $\gamma\equiv b_0$.

---

## 4. The smooth finite-dimensional family and its exact global minimiser

### 4.1 The flat smooth step

Let $\varphi(\tau)=e^{-1/\tau}$ for $\tau>0$ and $\varphi(\tau)=0$ for $\tau\le0$. It is classical that $\varphi\in C^\infty(\mathbb R)$. Define

$$
S(\tau)=\frac{\varphi(\tau)}{\varphi(\tau)+\varphi(1-\tau)},\qquad I(\tau)=\int_0^\tau S(s)\,ds,\qquad \iota:=I(1/2).
$$

**Lemma 4.1.**
1. $S\in C^\infty(\mathbb R)$, $S=0$ on $(-\infty,0]$ and $S=1$ on $[1,\infty)$. For $0<\tau<1$, $S(\tau)=\big(1+e^{1/\tau-1/(1-\tau)}\big)^{-1}\in(0,1)$. All derivatives of $S$ vanish at $0$ and at $1$.
2. $S$ is strictly increasing on $[0,1]$.
3. $S(\tau)+S(1-\tau)=1$ for all $\tau\in\mathbb R$; in particular $S(1/2)=1/2$.
4. $I(1)=\tfrac12$, $\iota<\tfrac14$, $I(\tau)<\tau$ for $\tau\in(0,1]$, and $0\le I(\tau)-(\tau-\tfrac12)_+\le\iota$ for $\tau\in[0,1]$.
5. $0\le S'\le 2$ on $\mathbb R$, and $S'(\tau)=2$ if and only if $\tau=\tfrac12$.

*Proof.*

(1) The denominator is positive on $\mathbb R$, because for every $\tau$ at least one of $\tau$ and $1-\tau$ is positive. Hence $S$ is smooth. The values outside $(0,1)$ are immediate, and the formula on $(0,1)$ follows by dividing numerator and denominator by $\varphi(\tau)$. Since $S$ is smooth and constant on $(-\infty,0]$ and on $[1,\infty)$, all its derivatives vanish at $0$ and $1$.

(2) The exponent $1/\tau-1/(1-\tau)$ is strictly decreasing on $(0,1)$, since its derivative is $-1/\tau^2-1/(1-\tau)^2<0$.

(3) Exchanging $\tau\leftrightarrow1-\tau$ in the definition gives $S(1-\tau)=1-S(\tau)$.

(4) *Value of $I(1)$.* By (3), $I(1)=\int_0^1S(1-\tau)\,d\tau=\int_0^1(1-S)$, hence $2I(1)=1$.

*Bound on $\iota$.* By (2) and (3), $S<\frac12$ on $(0,\frac12)$, so $\iota<\frac14$.

*$I(\tau)<\tau$.* Since $S<1$ on $(0,1)$, $I(\tau)<\tau$ for $\tau\in(0,1]$.

*The last estimate.* For $\tau\le\frac12$, $0\le I(\tau)\le I(\frac12)=\iota$. For $\tau\ge\frac12$, set $q(\tau)=I(\tau)-\tau+\frac12$. Then $q'=S-1\le0$, $q(\frac12)=\iota$ and $q(1)=0$, so $q\in[0,\iota]$.

(5) Outside $(0,1)$, $S'=0$. On $(0,1)$ write $S=1/(1+e^{q})$ with $q(\tau)=1/\tau-1/(1-\tau)$. Then $S'=-q'\,S(1-S)$, where $-q'=1/\tau^2+1/(1-\tau)^2>0$ and $S(1-S)=e^{q}/(1+e^{q})^2=1/\big(4\cosh^2(q/2)\big)$; in particular $S'>0$.

Substitute $\tau=(1+\sigma)/2$ with $\sigma\in(-1,1)$. Then
$$-q'=\frac{8(1+\sigma^2)}{(1-\sigma^2)^2},\qquad \frac q2=-a,\qquad a:=\frac{2\sigma}{1-\sigma^2}.$$
Since $1+a^2=\big((1+\sigma^2)/(1-\sigma^2)\big)^2$, we have $\sqrt{1+a^2}=\frac{1+\sigma^2}{1-\sigma^2}$ and $\frac1{1-\sigma^2}=\frac{1+\sqrt{1+a^2}}2$. Therefore
$$S'=\frac{2(1+\sigma^2)}{(1-\sigma^2)^2\cosh^2a}=\frac{b\,(1+b)}{\cosh^2a},\qquad b:=\sqrt{1+a^2}.$$
Now $b(1+b)=b+1+a^2$ and $2\cosh^2a=1+\cosh 2a$, so $S'\le2$ is equivalent to $b+a^2\le\cosh2a$. This holds because $b\le1+\tfrac{a^2}2$ and $\cosh 2a\ge1+2a^2$, which give $b+a^2\le1+\tfrac32a^2\le1+2a^2\le\cosh2a$. The middle inequality is strict unless $a=0$, that is, unless $\sigma=0$, i.e. $\tau=\frac12$; and at $\tau=\frac12$ we have $S'=8\cdot\frac14=2$. $\blacksquare$

Numerically, $\iota\approx0.068887$.

### 4.2 Smooth hats

*Design requirements.* The basis is chosen so that four properties hold simultaneously:
- every curve built from it is $C^\infty$ and flat at both endpoints, which needs compactly supported $C^\infty$ basis functions with flat edges;
- the basis functions are nonnegative and form a partition of unity between neighbouring knots, so that on each cell the curvature is a convex combination of two coefficients;
- each basis function equals $1$ at its own knot and $0$ at the others, so that the coefficients are the curvature values at the knots;
- consequently $J(\gamma_c)=\|c\|_\infty$ exactly (Proposition 4.3), and the positivity and translation structure needed for the comparison principle (Lemmas 4.9–4.10) are available.

Fix $N\ge3$, let $h=L/N$, and define the knots $x_j=jh$ ($0\le j\le N$) and the cells $Q_i=[x_i,x_{i+1}]$ ($0\le i\le N-1$). Put

$$
S_i(x):=S\Big(\frac{x-x_i}{h}\Big),\qquad B_j:=S_{j-1}-S_j\qquad(1\le j\le N-1).
$$

**Lemma 4.2.** For $1\le j\le N-1$:
1. $B_j\in C^\infty(\mathbb R)$, $0\le B_j\le1$, $B_j=0$ outside $(x_{j-1},x_{j+1})$, $B_j(x_j)=1$, and $B_j(x_i)=0$ for $i\ne j$.
2. On a cell $Q_i$, write $x=x_i+\tau h$ with $\tau\in[0,1]$. Then $B_i=1-S(\tau)$ and $B_{i+1}=S(\tau)$ (for those indices in $\{1,\dots,N-1\}$), and every other $B_j$ vanishes on $Q_i$.
3. *(Translation.)* $B_{j+1}(x)=B_j(x-h)$ for $1\le j\le N-2$.
4. *(Reflection.)* $B_j(L-x)=B_{N-j}(x)$.
5. $\int_{\mathbb R}B_j=h$.

*Proof.*

(1)–(2) By Lemma 4.1, $B_j$ equals $0-0$ for $x\le x_{j-1}$, equals $S(\tau)-0$ on $Q_{j-1}$, equals $1-S(\tau)$ on $Q_j$, and equals $1-1=0$ for $x\ge x_{j+1}$. The knot values follow from $S(0)=0$ and $S(1)=1$. We have $B_j\ge0$ because $S_{j-1}\ge S_j$ ($S$ is nondecreasing and $(x-x_{j-1})/h\ge(x-x_j)/h$), and $B_j\le1$ because $S_{j-1}\le1$ and $S_j\ge0$.

(3) $S_i(x-h)=S_{i+1}(x)$, so $B_j(x-h)=S_j(x)-S_{j+1}(x)=B_{j+1}(x)$.

(4) Since $\frac{L-x-x_i}{h}=1-\frac{x-x_{N-i-1}}{h}$, Lemma 4.1(3) gives $S_i(L-x)=1-S_{N-i-1}(x)$. Hence
$$B_j(L-x)=\big(1-S_{N-j}(x)\big)-\big(1-S_{N-j-1}(x)\big)=B_{N-j}(x).$$

(5) By (2) and Lemma 4.1(4),
$$\int B_j=h\int_0^1S+h\int_0^1(1-S)=\frac h2+\frac h2=h.\qquad\blacksquare$$

### 4.3 The class $\mathcal A_N$ and Problem $(\mathrm P_N)$

For $c=(c_1,\dots,c_{N-1})\in\mathbb R^{N-1}$ set $c_0=c_N=0$ and define

$$
k_c:=\sum_{j=1}^{N-1}c_jB_j,\qquad u_c(x):=\int_0^xk_c,\qquad \gamma_c(x):=\int_0^xF\big(u_c(\xi)\big)\,d\xi\quad(\text{when }\max_{[0,L]}|u_c|<1).
$$

The admissible coefficient set and the corresponding class of curves are

$$
\mathcal C_N:=\Big\{c:\ \sum_jc_j=0,\ \max_{[0,L]}|u_c|<1,\ \int_0^LF(u_c)=H\Big\},\qquad \mathcal A_N:=\{\gamma_c:\ c\in\mathcal C_N\}.
$$

**Proposition 4.3.** Let $c\in\mathcal C_N$.
1. On each cell $Q_i$, with $x=x_i+\tau h$: $k_c(x)=c_i\big(1-S(\tau)\big)+c_{i+1}S(\tau)$.
2. $\gamma_c\in\mathcal A$.
3. $\kappa_{\gamma_c}=|k_c|$ on $[0,L]$, and $J(\gamma_c)=\|c\|_\infty:=\max_j|c_j|$.

*Proof.*

(1) This is Lemma 4.2(2).

(2) By Lemma 4.2(1), $k_c$ extends by zero to a $C^\infty$ function on $\mathbb R$ supported in $[0,L]$, with all derivatives vanishing at $0$ and $L$. Let $\tilde u(x)=\int_{-\infty}^xk_c$. Then $\tilde u\in C^\infty(\mathbb R)$, $\tilde u=0$ on $(-\infty,0]$ and $\tilde u=u_c$ on $[0,L]$. For $x\ge L$, Lemma 4.2(5) gives $\tilde u(x)=\sum_jc_j\int B_j=h\sum_jc_j=0$.

Thus $\tilde u$ is smooth, supported in $[0,L]$, with $\sup|\tilde u|<1$. Consequently $F\circ\tilde u\in C^\infty(\mathbb R)$ is supported in $[0,L]$, and $\tilde\gamma(x):=\int_{-\infty}^xF(\tilde u)$ is smooth on $\mathbb R$. It equals $0$ on $(-\infty,0]$ and $\int_0^LF(u_c)=H$ on $[L,\infty)$, and it coincides with $\gamma_c$ on $[0,L]$. By Remark 1.2, $\gamma_c\in\mathcal A$.

(3) The tangent-sine variable of $\gamma_c$ is $G(\gamma_c')=G(F(u_c))=u_c$, so Lemma 2.2(5) gives $\kappa_{\gamma_c}=|u_c'|=|k_c|$. By (1), on each cell $k_c$ is a convex combination of $c_i$ and $c_{i+1}$ (with $c_0=c_N=0$), hence $|k_c|\le\|c\|_\infty$. By Lemma 4.2(1), $k_c(x_j)=c_j$. Therefore $\max|k_c|=\|c\|_\infty$. $\blacksquare$

**Problem $(\mathrm P_N)$.** Minimise $J$ over $\mathcal A_N$. (The set $\mathcal C_N$, hence $\mathcal A_N$, is nonempty; an explicit element is constructed in Theorem 4.11.) Equivalently, by Proposition 4.3,

$$
\min_{c\in\mathcal C_N}\|c\|_\infty .
$$

In epigraph form, this is the nonlinear program

$$
\min_{(c,t)\in\mathbb R^{N-1}\times\mathbb R} t\quad\text{s.t.}\quad -t\le c_j\le t,\quad \sum_jc_j=0,\quad \int_0^LF(u_c)\,dx=H,\quad \max|u_c|<1 .
$$

All constraints are linear except one smooth equality and the open constraint $\max|u_c|<1$.

*Remark 4.4.* $N\ge3$ is necessary. For $N=2$ the constraint $\sum c_j=0$ forces $c_1=0$, hence $u_c=0$ and $\int F(u_c)=0\ne H$.

### 4.4 The saturated coefficient profile

Let $n=N-1$ and define

$$
\hat c_j:=\operatorname{sgn}(N-2j)=\operatorname{sgn}(L/2-x_j)\quad(1\le j\le n),\qquad \hat C_j:=\hat c_1+\dots+\hat c_j,\quad \hat C_0:=0 .
$$

Explicitly, $\hat c=(1,\dots,1,-1,\dots,-1)$ when $N$ is odd, and $\hat c=(1,\dots,1,0,-1,\dots,-1)$ when $N$ is even.

**Lemma 4.5.**
1. $\hat c_{N-j}=-\hat c_j$, and $\sum_j\hat c_j=0$.
2. $\hat C_j=\min(j,\,n-j)$ for $0\le j\le n$.

*Proof.*

(1) We have $N-2(N-j)=-(N-2j)$. Pairing $j$ with $N-j$ in the sum gives $0$; the index $j=N/2$, present when $N$ is even, is paired with itself and has $\hat c_{N/2}=0$.

(2) *Case $j\le n/2$.* Every $i\le j$ satisfies $2i\le n<N$, so $\hat c_i=1$ and $\hat C_j=j=\min(j,n-j)$.

*Case $j\ge n/2$.* Using $\hat C_n=0$, we have $\hat C_j=-\sum_{i=j+1}^n\hat c_i$. Every $i\ge j+1$ satisfies $2i\ge n+2>N$, so $\hat c_i=-1$ and $\hat C_j=n-j=\min(j,n-j)$. $\blacksquare$

Define

$$
\psi_N:=k_{\hat c},\qquad \Psi_N:=u_{\hat c},\qquad M_N:=\max_{[0,L]}\Psi_N,\qquad \Phi_N:=(T-h/2)_+ .
$$

**Lemma 4.6 (explicit form of $\Psi_N$).** Write $x=x_i+\tau h\in Q_i$.

*(i) $N=2p+1$ odd ($p\ge1$).* The midpoint $L/2=x_p+h/2$ is the centre of $Q_p$. For $x\in[0,L/2]$:

| cell | $\psi_N$ | $\Psi_N$ |
|---|---|---|
| $Q_0$ | $S(\tau)$ | $h\,I(\tau)$ |
| $Q_i$, $1\le i\le p-1$ | $1$ | $x-h/2$ |
| $Q_p\cap[0,L/2]$ ($\tau\le\frac12$) | $1-2S(\tau)$ | $x-h/2-2h\,I(\tau)$ |

*(ii) $N=2p$ even ($p\ge2$).* The midpoint $L/2=x_p$ is a knot. For $x\in[0,L/2]$:

| cell | $\psi_N$ | $\Psi_N$ |
|---|---|---|
| $Q_0$ | $S(\tau)$ | $h\,I(\tau)$ |
| $Q_i$, $1\le i\le p-2$ | $1$ | $x-h/2$ |
| $Q_{p-1}$ | $1-S(\tau)$ | $x-h/2-h\,I(\tau)$ |

*(iii)* $\psi_N(L-x)=-\psi_N(x)$ and $\Psi_N(L-x)=\Psi_N(x)$ on $[0,L]$, and $\Psi_N(L)=0$.

*Proof.* The formulas for $\psi_N$ follow from Proposition 4.3(1) and the values of $\hat c$:
- for $N$ odd, $\hat c_i=1$ for $1\le i\le p$ and $\hat c_i=-1$ for $p+1\le i\le 2p$;
- for $N$ even, $\hat c_i=1$ for $i\le p-1$, $\hat c_p=0$, and $\hat c_i=-1$ for $i\ge p+1$.

We obtain $\Psi_N$ by integrating cell by cell.
- *First cell.* $\Psi_N(x_0+\tau h)=hI(\tau)$, so $\Psi_N(x_1)=hI(1)=h/2$ (Lemma 4.1(4)).
- *Bulk cells.* $\Psi_N(x)=h/2+(x-x_1)=x-h/2$.
- *Switching cell, $N$ odd.* $\Psi_N(x_p+\tau h)=(x_p-h/2)+h\int_0^\tau(1-2S)=x-h/2-2hI(\tau)$.
- *Switching cell, $N$ even.* $\Psi_N(x_{p-1}+\tau h)=(x_{p-1}-h/2)+h(\tau-I(\tau))=x-h/2-hI(\tau)$.

When the bulk is empty ($N=3$ or $N=4$), the value $\Psi_N(x_1)=h/2=x_1-h/2$ is still consistent with these formulas.

For (iii), Lemma 4.2(4) and Lemma 4.5(1) give
$$\psi_N(L-x)=\sum_j\hat c_jB_{N-j}(x)=\sum_i\hat c_{N-i}B_i(x)=-\psi_N(x).$$
Also $\Psi_N(L)=h\sum_j\hat c_j=0$. Hence
$$\Psi_N(L-x)=\Psi_N(L)-\int_{L-x}^L\psi_N=-\int_0^x\psi_N(L-s)\,ds=\Psi_N(x).\qquad\blacksquare$$

**Lemma 4.7 (properties of $\Psi_N$).**
1. $\Psi_N\in C^\infty[0,L]$; $0\le\psi_N\le1$ on $[0,L/2]$; $\Psi_N$ is nondecreasing on $[0,L/2]$; $M_N=\Psi_N(L/2)$; and $\Psi_N'(L/2)=0$.
2. $0\le\Psi_N\le T$ on $[0,L]$, $\Psi_N>0$ on $(0,L)$, and $\Psi_N<T$ on $(0,h]$.
3. $|\Psi_N-\Phi_N|\le h/2$ on $[0,L]$. Moreover $\Psi_N=\Phi_N$ and $\psi_N=\sigma$ outside a set $E_N$, which is the union of $Q_0$, $Q_{N-1}$ and the switching cell(s) ($Q_p$ if $N=2p+1$; $Q_{p-1}\cup Q_p$ if $N=2p$). Hence $|E_N|\le4h$.
4. $(T-h)_+\le\Psi_N\le T$, and $L/2-h\le M_N<L/2$.

*Proof.*

(1) $\Psi_N=u_{\hat c}$ is smooth (proof of Proposition 4.3). By Lemma 4.6, $\psi_N\in[0,1]$ on $[0,L/2]$, because $S$, $1-2S(\tau)$ for $\tau\le\frac12$, and $1-S$ all lie in $[0,1]$. Therefore $\Psi_N$ is nondecreasing on $[0,L/2]$, and by symmetry nonincreasing on $[L/2,L]$, so $M_N=\Psi_N(L/2)$. Finally, $\Psi_N'(L/2)=\psi_N(L/2)$, which equals $1-2S(\frac12)=0$ for odd $N$ and $1-S(1)=0$ for even $N$.

(2) On $[0,L/2]$, $\Psi_N(x)=\int_0^x\psi_N\in[0,x]=[0,T(x)]$; the other half follows by symmetry.

*Positivity.* For $x\in(0,L/2]$, $\Psi_N(x)\ge\Psi_N(\min(x,h))=hI(\min(x,h)/h)>0$, since $S>0$ on $(0,1)$.

*Strict inequality on $(0,h]$.* There $\Psi_N=hI(\tau)<h\tau=x$ by Lemma 4.1(4).

(3) On $[0,L/2]$ we have $T(x)=x$ and $\Phi_N=(x-h/2)_+$. Going through the cells of Lemma 4.6:
- on $Q_0$: $\Psi_N-\Phi_N=h\big(I(\tau)-(\tau-\frac12)_+\big)\in[0,\iota h]$;
- on the bulk cells: $\Psi_N=\Phi_N$ (because $x\ge h$ there);
- on the switching cell for odd $N$: $\Phi_N-\Psi_N=2hI(\tau)\in[0,2\iota h]$ for $\tau\le\frac12$;
- on the switching cell for even $N$: $\Phi_N-\Psi_N=hI(\tau)\in[0,h/2]$.

Since $\iota<\frac14$, all deviations are at most $h/2$.

*Right half.* $T$, $\Phi_N$ and $\Psi_N$ are symmetric about $L/2$, and the reflection maps $Q_i$ onto $Q_{N-1-i}$. This transfers the estimates to $[L/2,L]$ and identifies $E_N$.

*$\psi_N=\sigma$ outside $E_N$.* On the bulk cells of the left half, $\psi_N=1=\sigma$. On the right half, $\psi_N=-1=\sigma$ by antisymmetry.

(4) By (3), $\Psi_N\ge\Phi_N-h/2\ge T-h$; together with $\Psi_N\ge0$ this gives $\Psi_N\ge(T-h)_+$. Hence $M_N=\Psi_N(L/2)\ge L/2-h$.

Finally, $M_N=\int_0^{L/2}\psi_N<L/2$. Indeed $\psi_N\le1$ on $[0,L/2]$, and $\psi_N=S(\tau)<1$ on the interior of $Q_0\subset[0,L/2]$ (recall $h\le L/3$). $\blacksquare$

### 4.5 The exact global minimiser of $(\mathrm P_N)$

Let $t_{\max}:=1/M_N$ and define

$$
g_N(t):=\int_0^LF\big(t\,\Psi_N(x)\big)\,dx,\qquad 0\le t<t_{\max}.
$$

**Lemma 4.8.** $g_N$ is continuous and strictly increasing on $[0,t_{\max})$, $g_N(0)=0$, and $g_N(t)\to+\infty$ as $t\uparrow t_{\max}$. Consequently, for every $H>0$ there is a unique $t_N\in(0,t_{\max})$ with $g_N(t_N)=H$.

*Proof.*

*Continuity.* For $0\le t\le t'<t_{\max}$ we have $0\le t\Psi_N\le t'M_N<1$, so the integrand is continuous in $(t,x)$ on the compact set $[0,t']\times[0,L]$.

*Strict monotonicity.* This follows from $\Psi_N>0$ on $(0,L)$ (Lemma 4.7(2)) and the strict monotonicity of $F$.

*Divergence.* By monotone convergence, $g_N(t)\uparrow\int_0^LF(t_{\max}\Psi_N)$, where we set $F(1)=+\infty$. Let $A=\max|\Psi_N''|<\infty$. Since $\Psi_N'(L/2)=0$ and $\Psi_N(L/2)=M_N$, Taylor's formula gives $M_N-\Psi_N(x)\le\frac A2(x-L/2)^2$. Hence
$$1-t_{\max}\Psi_N(x)\le\beta\,(x-L/2)^2,\qquad \beta:=\tfrac{t_{\max}A}{2}+1>0 .$$
Choose $\delta\in(0,L/2]$ with $\beta\delta^2\le\frac12$. For $|x-L/2|<\delta$ we have $v:=t_{\max}\Psi_N(x)\in[\frac12,1]$, and Lemma 2.1(3) gives
$$F(v)\ge\frac{1}{2\sqrt{2\beta}\,|x-L/2|}\qquad(\text{trivially if } v=1).$$
This lower bound is not integrable near $L/2$, so the limit is $+\infty$. In words: $\Psi_N$ attains its maximum at $L/2$ with zero derivative, so near the maximum the integrand behaves like the reciprocal of the distance to $L/2$. This divergence is exactly what guarantees that the scalar root exists for *every* $H>0$.

*Existence and uniqueness of $t_N$.* These follow from the intermediate value theorem and strict monotonicity. $\blacksquare$

**Lemma 4.9 (summation by parts).** For $1\le j\le N-1$ let $U_j(x)=\int_{-\infty}^xB_j$, and for $1\le j\le N-2$ let $D_j:=U_j-U_{j+1}$.
1. $D_j\ge0$ on $\mathbb R$, and $D_j(x_j)=h/2$.
2. For every $c\in\mathbb R^{N-1}$ with $\sum_jc_j=0$,
$$u_c=\sum_{j=1}^{N-2}C_j\,D_j\quad\text{on }[0,L],\qquad C_j:=c_1+\dots+c_j .$$

*Proof.*

(1) Each $U_j$ is nondecreasing because $B_j\ge0$. By Lemma 4.2(3),
$$U_{j+1}(x)=\int_{-\infty}^xB_j(s-h)\,ds=U_j(x-h)\le U_j(x).$$
Moreover $D_j(x_j)=U_j(x_j)-U_{j+1}(x_j)=\int_{x_{j-1}}^{x_j}B_j-0=h/2$.

(2) By linearity, $u_c=\sum_{j=1}^nc_jU_j$ with $n=N-1$. Put $C_0=0$ and write $c_j=C_j-C_{j-1}$. Then
$$\sum_{j=1}^n(C_j-C_{j-1})U_j=\sum_{j=1}^nC_jU_j-\sum_{j=0}^{n-1}C_jU_{j+1}=C_nU_n-C_0U_1+\sum_{j=1}^{n-1}C_j\,(U_j-U_{j+1}).$$
Now $C_0=0$ by definition and $C_n=\sum_jc_j=0$ by hypothesis, and $n-1=N-2$. $\blacksquare$

**Lemma 4.10 (comparison).** Let $c\in\mathbb R^{N-1}$ with $\sum_jc_j=0$ and $\|c\|_\infty\le t$. Then $u_c\le t\,\Psi_N$ on $[0,L]$. If equality holds on all of $[0,L]$, then $c=t\hat c$.

*Proof.*

*Bound on the partial sums.* We have $C_j=\sum_{i\le j}c_i\le tj$ and $C_j=-\sum_{i>j}c_i\le t(n-j)$. By Lemma 4.5(2), $C_j\le t\min(j,n-j)=t\hat C_j$.

*Comparison.* Applying Lemma 4.9 to both $c$ and $\hat c$ (both have zero sum),
$$t\Psi_N-u_c=\sum_{j=1}^{N-2}\big(t\hat C_j-C_j\big)\,D_j .$$
This is a sum of nonnegative functions, so it is $\ge0$.

*Equality case.* If the sum vanishes identically, then every term vanishes identically. Evaluating the $j$-th term at $x_j$, where $D_j(x_j)=h/2>0$, gives $C_j=t\hat C_j$ for $1\le j\le N-2$. Also $C_n=0=t\hat C_n$. Taking differences, $c_j=C_j-C_{j-1}=t\hat c_j$ for all $j$. $\blacksquare$

Lemma 4.10 is the discrete analogue of the tent-envelope argument of §3. The partial sums $C_j$ play the role of the cumulative signed curvature, that is, of $u$ at the knots (indeed $u_c(x_j)=h\,(C_{j-1}+C_j)/2$), and the extremal partial sums $t\min(j,n-j)$ are attained by the saturated sign vector $\hat c$.

**Theorem 4.11 (unique global minimiser of $(\mathrm P_N)$).** Let $N\ge3$ and let $t_N$ be as in Lemma 4.8. Then $c^N:=t_N\hat c\in\mathcal C_N$, and every $c\in\mathcal C_N$ satisfies $\|c\|_\infty\ge t_N$, with equality if and only if $c=c^N$. Thus $c^N$ is the unique *global* minimiser. Equivalently, the curve

$$
\gamma_N(x)=\int_0^xF\big(t_N\Psi_N(\xi)\big)\,d\xi
$$

is the unique minimiser of $J$ over $\mathcal A_N$, and $J(\gamma_N)=t_N$.

*Proof.*

*Feasibility of $c^N$.* $\sum_jc^N_j=0$ by Lemma 4.5(1). $u_{c^N}=t_N\Psi_N\in[0,t_NM_N]\subset[0,1)$. $\int F(u_{c^N})=g_N(t_N)=H$. Also $\|c^N\|_\infty=t_N$, since $\hat c_1=1$.

*Lower bound.* Let $c\in\mathcal C_N$ and $t:=\|c\|_\infty$. Suppose $t<t_N$. By Lemma 4.10, $u_c\le t\Psi_N$, and both functions take values in $(-1,1)$ (note $t\Psi_N\le tM_N<1$). Since $F$ is increasing,
$$H=\int_0^LF(u_c)\le g_N(t)<g_N(t_N)=H,$$
a contradiction. Hence $t\ge t_N$.

*Uniqueness.* If $t=t_N$, then $F(u_c)\le F(t_N\Psi_N)$ pointwise, and both integrals equal $H$. The functions are continuous, so $F(u_c)\equiv F(t_N\Psi_N)$, hence $u_c\equiv t_N\Psi_N$, and Lemma 4.10 gives $c=c^N$.

The statement about $J$ follows from Proposition 4.3(3). $\blacksquare$

The reduction is exact at the level of the finite-dimensional model: no approximation is involved in Theorem 4.11, and numerical quadrature enters only when the scalar function $g_N$ is evaluated in an implementation (§6).

The optimal tangent-sine profile $u_N=t_N\Psi_N$ is nonnegative. This is a property of the minimiser, not of the feasible set: feasible $u_c$ may change sign, but the comparison principle shows that the relevant extremal is the maximal nonnegative envelope $t\Psi_N$.

*Remark 4.12 (geometry of $\gamma_N$).* The coefficient vector $c^N$ is a saturated ("bang-bang") sign profile, with a zero middle coefficient when $N$ is even. The curvature function itself is not bang-bang; it is a smoothed saturated-curvature profile with plateaus and transition layers. Precisely, the signed curvature of $\gamma_N$, viewed as a function of $x$, is $k_N=u_N'=t_N\psi_N$. It consists of five pieces:
- a smooth ramp from $0$ to $t_N$ on $Q_0$;
- the constant value $t_N$ (a circular arc of radius $1/t_N$);
- a smooth switch from $t_N$ to $-t_N$ across the middle cell or cells (an inflection);
- the constant value $-t_N$;
- a smooth ramp back to $0$ on $Q_{N-1}$.

Thus $\gamma_N$ is the double arc with its three curvature discontinuities smoothed over one cell each (two cells for the inflection when $N$ is even). For general data,

$$
\gamma_N(x)=b_0+\operatorname{sgn}(H)\int_{a_0}^xF\big(t_N\Psi_N(\xi-a_0)\big)\,d\xi,
$$

with $t_N$ computed for $|H|$.

---

## 5. Convergence and asymptotics

Throughout this section $h=L/N$ and $K^*(\ell)=4H/(\ell^2+H^2)$.

**Theorem 5.1.** For every $N\ge3$:
1. $t_N>K^*$.
2. If $H<L$ and $N>2L/(L-H)$, then $t_N\le K^*(L-2h)$.
3. If $H\ge L$, then $t_N<2/(L-2h)$.
4. If $H<L$, $N>2L/(L-H)$ and $t_N<2/L$, then
$$\big|t_N-K^*(L-h)\big|\le\frac{8\,t_N\,h^2}{(L-h)^2\,\big(1-t_N^2L^2/4\big)^{3/2}} .$$

*Proof.*

(1) We have $\gamma_N\in\mathcal A$ (Proposition 4.3(2)), so $t_N=J(\gamma_N)>K^*$ by Corollary 3.6.

(2) Let $\ell:=L-2h$; the hypothesis says $\ell>H$. Put $t_{\rm up}:=K^*(\ell)\in(0,2/\ell)$.
- If $t_{\rm up}\ge t_{\max}$, then $t_N<t_{\max}\le t_{\rm up}$.
- Otherwise $g_N(t_{\rm up})$ is defined. By Lemma 4.7(4), $\Psi_N\ge(T-h)_+$; since $F$ is increasing, Lemma 2.4(5) with $c=h$ gives
$$g_N(t_{\rm up})\ge\int_0^LF\big(t_{\rm up}(T-h)_+\big)=Y_\ell(t_{\rm up})=H=g_N(t_N).$$
Since $g_N$ is strictly increasing, $t_N\le t_{\rm up}$.

(3) By Lemma 4.7(4), $t_N<t_{\max}=1/M_N\le1/(L/2-h)=2/(L-2h)$.

(4) *Comparison of $g_N$ with a shortened double arc.* Fix $t\in[0,2/L)$. By Lemma 4.7(2),(4), both $t\Psi_N$ and $t\Phi_N$ take values in $[0,tL/2]\subset[0,1)$, where $F$ is Lipschitz with constant $F'(tL/2)$ (Lemma 2.1(1)). By Lemma 4.7(3), $F(t\Psi_N)=F(t\Phi_N)$ outside $E_N$, while on $E_N$
$$|F(t\Psi_N)-F(t\Phi_N)|\le F'(tL/2)\,t\,\frac h2 .$$
Lemma 2.4(5) with $c=h/2$ gives $\int_0^LF(t\Phi_N)=Y_{L-h}(t)$. Integrating over $E_N$, whose measure is at most $4h$,
$$\big|g_N(t)-Y_{L-h}(t)\big|\le 4h\cdot F'(tL/2)\,t\,\frac h2=\frac{2t\,h^2}{(1-t^2L^2/4)^{3/2}} .$$

*Inversion.* Let $\ell'=L-h>H$ and $s_N:=K^*(\ell')$, so that $Y_{\ell'}(s_N)=H=g_N(t_N)$ (Lemma 2.4(4)). Both $t_N$ and $s_N$ lie in $(0,2/\ell')$, because $t_N<2/L<2/\ell'$. By the mean value theorem and $Y_{\ell'}'\ge\ell'^2/4$ (Lemma 2.4(3)),
$$\frac{\ell'^2}{4}\,|t_N-s_N|\le|Y_{\ell'}(t_N)-Y_{\ell'}(s_N)|=|Y_{\ell'}(t_N)-g_N(t_N)|\le\frac{2t_Nh^2}{(1-t_N^2L^2/4)^{3/2}} .$$
Dividing by $\ell'^2/4$ gives the claim. $\blacksquare$

**Corollary 5.2 (convergence of the values).**

1. $t_N\to K^*$, with explicit relative bounds:
$$0<\frac{t_N}{K^*}-1\le\frac{4h(L-h)}{(L-2h)^2+H^2}\quad(H<L,\ N>\tfrac{2L}{L-H}),\qquad 0<\frac{t_N}{K^*}-1<\frac{2}{N-2}\quad(H\ge L).$$
2. $\inf_{\mathcal A}J=K^*$, the infimum is not attained, Problem (P) has no solution, and $(\gamma_N)_{N\ge3}$ is a minimising sequence in $\mathcal A$.
3. If $H<L$, then
$$\frac{t_N}{K^*}-1=\frac{2L^2}{(L^2+H^2)\,N}+O(N^{-2}).$$

*Proof.*

(1) *Case $H<L$.* Theorem 5.1(1),(2) give $K^*<t_N\le K^*(L-2h)$, and
$$\frac{K^*(L-2h)}{K^*}-1=\frac{(L^2+H^2)-\big((L-2h)^2+H^2\big)}{(L-2h)^2+H^2}=\frac{4h(L-h)}{(L-2h)^2+H^2}\to0 .$$

*Case $H\ge L$.* Theorem 5.1(1),(3) give $2/L<t_N<2/(L-2h)$, and $\frac{L}{L-2h}-1=\frac{2h}{L-2h}=\frac{2}{N-2}$.

(2) Since $\gamma_N\in\mathcal A$ and $J(\gamma_N)=t_N\to K^*$, we get $\inf_{\mathcal A}J\le K^*$. Theorem 3.2 gives the reverse inequality, and Corollary 3.6 shows that no element of $\mathcal A$ attains it.

(3) Write $s_N=K^*(L-h)$ and decompose
$$\frac{t_N}{K^*}-1=\Big(\frac{s_N}{K^*}-1\Big)+\frac{t_N-s_N}{K^*}.$$

*First term.* In absolute form,
$$K^*(L-h)-K^*(L)=K^*(L)\,\frac{2Lh-h^2}{(L-h)^2+H^2},\qquad\text{i.e.}\qquad \frac{s_N}{K^*}-1=\frac{2Lh-h^2}{(L-h)^2+H^2}.$$
A direct computation shows
$$\frac{2Lh-h^2}{(L-h)^2+H^2}-\frac{2Lh}{L^2+H^2}=\frac{h^2(3L^2-H^2)-2Lh^3}{\big((L-h)^2+H^2\big)(L^2+H^2)}=O(h^2).$$

*Second term.* By (1), $t_N\to K^*<2/L$, so the hypotheses of Theorem 5.1(4) hold for all large $N$. Moreover
$$1-t_N^2L^2/4\ \to\ 1-K^{*2}L^2/4=\Big(\frac{L^2-H^2}{L^2+H^2}\Big)^2>0 .$$
Hence Theorem 5.1(4) gives $(t_N-s_N)/K^*=O(h^2)$.

Since $h=L/N$, the first term is $2L^2/\big((L^2+H^2)N\big)+O(N^{-2})$, which proves (3). Multiplying by $K^*=4H/(L^2+H^2)$ gives the absolute form
$$t_N-K^*=\frac{8HL^2}{(L^2+H^2)^2}\,\frac1N+O(N^{-2}).\qquad\blacksquare$$

*Remark 5.3 (where the first-order coefficient comes from).* Theorem 5.1(4) says that, up to $O(N^{-2})$, the best candidate on $N$ cells is exactly as good as the true optimum on an interval shortened by one cell. The mechanism has three parts.
- *Endpoint layers.* In the bulk $\Psi_N=T-h/2$ exactly: each of the two endpoint smoothing layers delays the tent by half a cell, so together they produce an effective shortening of the span by one cell, $L\mapsto L-h$.
- *Central switch.* The curvature switch occupies a set of width $O(h)$ on which $\Psi_N$ differs from the shifted tent $\Phi_N$ by $O(h)$; its contribution to the height integral is therefore $O(h)\cdot O(h)=O(h^2)$, i.e. second order.
- *Inversion.* The height map $K\mapsto Y_{L-h}(K)$ has derivative bounded below by $(L-h)^2/4$, so an $O(h^2)$ error in height becomes an $O(h^2)$ error in $t_N$, while the effective shortening changes the value by exactly $K^*(L-h)-K^*(L)$, whose leading term is the coefficient $2L^2/((L^2+H^2)N)$ in relative form.

**Theorem 5.4 (convergence of the curves, $H<L$).** Let $u_N:=t_N\Psi_N$ and $k_N:=t_N\psi_N$ be the tangent-sine variable and the signed curvature of $\gamma_N$. For the double arc, let $u_{\rm arc}=K^*T$ and $k_{\rm arc}:=K^*\sigma$ (a.e.).
1. $\|u_N-u_{\rm arc}\|_\infty\le t_Nh+(t_N-K^*)\,L/2$.
2. Let $\bar v:=\frac12(1+K^*L/2)<1$. For all $N$ large enough that $t_NL/2\le\bar v$,
$$\|\gamma_N'-\gamma_{\rm arc}'\|_\infty\le F'(\bar v)\,\|u_N-u_{\rm arc}\|_\infty,\qquad \|\gamma_N-\gamma_{\rm arc}\|_\infty\le L\,\|\gamma_N'-\gamma_{\rm arc}'\|_\infty .$$
Hence $\gamma_N\to\gamma_{\rm arc}$ in $C^1[0,L]$ at rate $O(1/N)$.
3. For $1\le p<\infty$: $\|k_N-k_{\rm arc}\|_{L^p}\le (t_N-K^*)L^{1/p}+2t_N(4h)^{1/p}\to0$.
4. $\|k_N-k_{\rm arc}\|_{L^\infty}\ge K^*$ for every $N$, so the curvatures do not converge uniformly.
5. The lengths converge: $\big|\ell(\gamma_N)-\ell(\gamma_{\rm arc})\big|\le L\,\|\gamma_N'-\gamma_{\rm arc}'\|_\infty=O(1/N)$, where $\ell(\gamma)=\int_0^L\sqrt{1+\gamma'^2}$ and $\ell(\gamma_{\rm arc})=2R^*\arcsin\big(L/(2R^*)\big)$.

*Proof.*

(1) By Lemma 4.7(4), $0\le T-\Psi_N\le h$. Hence
$$|u_N-u_{\rm arc}|\le t_N|\Psi_N-T|+|t_N-K^*|\,T\le t_Nh+(t_N-K^*)L/2 .$$

(2) We have $\bar v<1$ because $K^*L/2<1$ (Lemma 2.4(4)), and $t_NL/2\le\bar v$ for large $N$ because $t_N\to K^*$. Then $0\le u_N\le t_NT\le\bar v$ and $0\le u_{\rm arc}\le K^*L/2\le\bar v$. Since $\gamma_N'=F(u_N)$ and $\gamma_{\rm arc}'=F(u_{\rm arc})$, the mean value theorem on $[0,\bar v]$ gives the first estimate. The second follows by integration, because $\gamma_N(0)=\gamma_{\rm arc}(0)=0$. The rate comes from (1) and Corollary 5.2(1).

(3) By Lemma 4.7(3), $\psi_N=\sigma$ outside $E_N$, so there $|k_N-k_{\rm arc}|=t_N-K^*$. On $E_N$, $|k_N-k_{\rm arc}|\le t_N+K^*<2t_N$. Minkowski's inequality and $|E_N|\le4h$ give the bound.

(4) $k_N$ is continuous with $k_N(L/2)=t_N\psi_N(L/2)=0$. Given $\varepsilon>0$, there is $\delta>0$ with $|k_N|<\varepsilon$ on $(L/2-\delta,L/2+\delta)$, while $|k_{\rm arc}|=K^*$ a.e. there. Hence $|k_N-k_{\rm arc}|>K^*-\varepsilon$ on a set of positive measure.

(5) The function $p\mapsto\sqrt{1+p^2}$ is $1$-Lipschitz, which gives the inequality; the rate follows from (2). For the value of $\ell(\gamma_{\rm arc})$: each arc has radius $R^*$ and turns through the angle $\arcsin(L/(2R^*))$, since $\sin\theta=u_{\rm arc}=K^*L/2$ at the midpoint. $\blacksquare$

*Hierarchy of convergence.* Three different statements hold, and it is worth keeping them apart:
- *values:* $t_N\to K^*$ (Corollary 5.2), in all regimes;
- *curves:* $\gamma_N\to\gamma_{\rm arc}$ in $C^1$ for $H<L$ (Theorem 5.4(2)), together with the lengths;
- *curvatures:* only $k_N\to k_{\rm arc}$ in $L^p$, $1\le p<\infty$, not uniformly.

Uniform curvature convergence is impossible within this family, because every $k_N$ is continuous while the limiting signed curvature has a jump at the midpoint. The failure is therefore a structural consequence of the non-attainment result, not a defect of the numerical approximation.

The rates in Theorem 5.4 and Corollary 5.2 are properties of the particular family $(\gamma_N)$. They are not lower bounds for the approximation of $K^*$ by arbitrary smooth admissible curves; how fast $K^*$ can be approached in terms of other complexity measures is not addressed here.

*Remark 5.5 (the degenerate regime $H\ge L$).* Here $t_NM_N>\frac2L\big(\frac L2-h\big)=1-\frac2N$, hence
$$\|\gamma_N'\|_\infty=F(t_NM_N)\ge F(1-2/N)\to\infty .$$
This agrees with Proposition 3.7, which says that *every* sequence in $\mathcal B$ with $J\to2/L$ has unbounded slopes. Consequently no such sequence has a subsequence converging in $C^1([0,L])$, or in any topology that controls $\|\gamma'\|_\infty$. We do not analyse the behaviour of the sequence in weaker topologies.

*Heuristic geometric interpretation (not proved here).* The natural geometric limit has a vertical tangent at the midpoint when $H=L$, and a vertical segment when $H>L$. These statements are not consequences of Proposition 3.7 and are recorded only as intuition.

---

## 6. Numerical implementation

This section provides implementation and numerical-stability guarantees. The main mathematical contribution is Theorem 4.11 together with §5; the material here is not part of it.

**Notation.** $t_N$ always denotes the *exact* root of $g_N(t)=H$ (Lemma 4.8). The value actually computed with quadrature and floating-point arithmetic is denoted $\widehat t_N$. Its error splits as
$$
|\widehat t_N-t_N|\ \le\ \underbrace{\varepsilon_{\rm quad}}_{\text{quadrature of }g_N\ (\text{Prop. 6.1})}+\underbrace{\varepsilon_{\rm root}}_{\text{root-finding tolerance}}+\underbrace{\varepsilon_{\rm fp}}_{\text{floating-point rounding}} .
$$
Proposition 6.1(3) bounds the first term asymptotically, the second is set by the stopping criterion, and the third is not bounded rigorously here (no interval arithmetic is used); Appendix A reports how the three were monitored.

### Algorithm 1 (best candidate at resolution $N$)

The exact mathematical algorithm has two steps: construct $\Psi_N$, and solve the monotone scalar equation $g_N(t)=H$. Quadrature is an implementation layer for the second step.

**Input:** $a_0<a_1$, $b_0\ne b_1$, $N\ge3$.

1. Set $L=a_1-a_0$, $H=|b_1-b_0|$, $s=\operatorname{sgn}(b_1-b_0)$, $h=L/N$.
2. Evaluate $\Psi_N$ by Lemma 4.6 on $[0,L/2]$ and by symmetry (Lemma 4.6(iii)) on $[L/2,L]$. The only transcendental ingredient is $I(\tau)=\int_0^\tau S$, a one-dimensional integral of an explicit smooth function, evaluated by composite Gauss–Legendre quadrature.
3. Compute $\widehat t_N\approx t_N$, the root of $g_N(t)=H$ on $(0,1/M_N)$, by bisection or Brent's method, with $g_N$ evaluated by quadrature.
4. Output $\widehat t_N$ and $\gamma_N(x)=b_0+s\int_{a_0}^xF\big(\widehat t_N\Psi_N(\xi-a_0)\big)\,d\xi$.

*Convergence of step 3 (exact arithmetic).* By Lemma 4.8, $g_N-H$ is continuous and strictly increasing, negative at $0$, and positive near $1/M_N$. Bisection started on $[0,t_{\rm hi}]$ with $g_N(t_{\rm hi})>H$ therefore converges to $t_N$, with error at most $2^{-k}t_{\rm hi}$ after $k$ steps.

### Proposition 6.1 (discretisation of the height integral)

The message of this proposition is: the discrete quadrature problem retains the exact comparison structure under any positive-weight quadrature, but *existence* of a quadrature root requires an additional condition, because a quadrature rule may fail to sample the midpoint, where $\Psi_N$ is maximal.

Let $Q(f)=\sum_iw_if(\xi_i)$ be a quadrature rule with nodes $\xi_i\in[0,L]$ and positive weights $w_i$, and set
$$
g_N^Q(t):=Q\big(F(t\Psi_N)\big),\qquad 0\le t<t_{\max}=1/M_N .
$$
Let $(\mathrm P_N^Q)$ denote Problem $(\mathrm P_N)$ with the height condition $\int_0^LF(u_c)=H$ replaced by $Q\big(F(u_c)\big)=H$ (the conditions $\sum_jc_j=0$ and $\max_{[0,L]}|u_c|<1$ are kept).

1. *Conditional structure.* Assume that every interval $(x_{j-1},x_{j+2})$, $1\le j\le N-2$, contains a node. If the equation $g_N^Q(t)=H$ has a root $t^Q\in(0,t_{\max})$, then this root is unique, and $c=t^Q\hat c$ is the unique minimiser of $(\mathrm P_N^Q)$.
2. *Existence of the root.* A root $t^Q\in(0,t_{\max})$ exists in each of the following cases:
   - (a) $L/2$ is a node. (For even $N$, $L/2=x_{N/2}$ is a knot, so this holds whenever the knots are nodes; for odd $N$ it must be imposed separately.)
   - (b) For some $t_1\in(t_N,t_{\max})$, $\ \sup_{0\le t\le t_1}|g_N^Q(t)-g_N(t)|<\min\big(H,\ g_N(t_1)-H\big)$.
3. *Accuracy.* Fix $N$ and $t_1\in(t_N,t_{\max})$, and let $\Delta$ be the step of a uniform subdivision of $[0,L]$.
   - (a) For the composite trapezoidal rule and every $r\in\mathbb N$ there is $C_{r,N,t_1}$ with $\sup_{0\le t\le t_1}|g_N^\Delta(t)-g_N(t)|\le C_{r,N,t_1}\Delta^{2r}$.
   - (b) For the composite $G$-point Gauss–Legendre rule there is $C_{G,N,t_1}$ with $\sup_{0\le t\le t_1}|g_N^\Delta(t)-g_N(t)|\le C_{G,N,t_1}\Delta^{2G}$.

   Consequently, for all sufficiently small $\Delta$ the root $\widehat t_N=t_N^\Delta$ exists, and $|t_N^\Delta-t_N|=O(\Delta^{2r})$ for every $r$ in case (a), $O(\Delta^{2G})$ in case (b).

*Proof.*

(1) *Monotonicity.* A node $\xi\in(x_0,x_3)\subset(0,L)$ exists by hypothesis, and $\Psi_N(\xi)>0$ there (Lemma 4.7(2)); hence $g_N^Q$ is strictly increasing, and the root is unique.

*Feasibility.* $c=t^Q\hat c$ satisfies $\sum_jc_j=0$, $0\le u_c=t^Q\Psi_N\le t^QM_N<1$, and $Q(F(u_c))=g_N^Q(t^Q)=H$.

*Optimality.* Let $c$ be feasible with $t:=\|c\|_\infty<t^Q$. By Lemma 4.10, $u_c\le t\Psi_N$ on $[0,L]$, with both sides in $(-1,1)$, so $F(u_c)\le F(t\Psi_N)$ pointwise. Since the weights are positive, $H=Q(F(u_c))\le g_N^Q(t)<g_N^Q(t^Q)=H$, a contradiction.

*Uniqueness.* If $\|c\|_\infty=t^Q$, the same argument gives $F(u_c)\le F(t^Q\Psi_N)$ pointwise and equal $Q$-values, so $u_c(\xi_i)=t^Q\Psi_N(\xi_i)$ at every node. By Lemma 4.9, $0=t^Q\Psi_N(\xi_i)-u_c(\xi_i)=\sum_j\big(t^Q\hat C_j-C_j\big)D_j(\xi_i)$ with nonnegative terms, so each term vanishes. Now $D_j(x)=\int_{x-h}^xB_j>0$ exactly for $x\in(x_{j-1},x_{j+2})$; choosing a node there gives $C_j=t^Q\hat C_j$ for $1\le j\le N-2$, and $c=t^Q\hat c$ follows as in Lemma 4.10.

(2)(a) Since $M_N=\Psi_N(L/2)$, the term of $g_N^Q(t)$ at the node $L/2$ is $w\,F(tM_N)\to\infty$ as $t\uparrow t_{\max}$. As $g_N^Q$ is continuous with $g_N^Q(0)=0<H$, a root exists.

(2)(b) The hypothesis gives $g_N^Q(0)=0<H$ and $g_N^Q(t_1)>g_N(t_1)-\big(g_N(t_1)-H\big)=H$; continuity gives a root in $(0,t_1)$.

(3) For $0\le t\le t_1$ we have $0\le t\Psi_N\le t_1M_N<1$, so $f_t=F(t\Psi_N)$ and all its $x$-derivatives are continuous in $(t,x)$ on $[0,t_1]\times[0,L]$; in particular they are bounded uniformly in $t$.

(a) $f_t$ extends to a $C^\infty$ function on $\mathbb R$ supported in $[0,L]$, all of whose derivatives vanish at $0$ and $L$ (because $\Psi_N$ is flat there). The endpoint corrections in the Euler–Maclaurin formula therefore vanish, and its remainder is bounded by $C_r\Delta^{2r}\int_0^L|\partial_x^{2r}f_t|$.

(b) This is the standard error bound for composite Gauss–Legendre rules, $|E|\le c_G\,L\,\Delta^{2G}\max_x|\partial_x^{2G}f_t|$.

*Root perturbation.* Let $\varepsilon_\Delta$ denote the supremum in (a) or (b). Once $\varepsilon_\Delta<\min(H,g_N(t_1)-H)$, part (2)(b) gives a root $t_N^\Delta\in(0,t_1)$. Moreover $g_N'(t)=\int F'(t\Psi_N)\Psi_N\ge\mu:=\int_0^L\Psi_N>0$, so
$$\mu\,|t_N^\Delta-t_N|\le|g_N(t_N^\Delta)-g_N(t_N)|=|g_N(t_N^\Delta)-g_N^\Delta(t_N^\Delta)|\le\varepsilon_\Delta. \qquad\blacksquare$$

*Remark 6.1a (why the hypotheses matter).* Without a node at $L/2$ and without an accuracy condition, a root need not exist. Take $N=3$ and the one-node rule $Q(f)=L\,f(x_1)$ with $x_1=L/3$, which satisfies the node condition of part (1). Then $\Psi_3(x_1)=h/2=L/6<M_3$, so $g_3^Q(t)=L\,F(t\,L/6)$ stays below $L\,F\big(L/(6M_3)\big)<\infty$ on $[0,t_{\max})$, and for $H\ge L\,F\big(L/(6M_3)\big)$ the equation $g_3^Q(t)=H$ has no root in $(0,t_{\max})$. This shows that the earlier, unconditional version of part (1) was false.

*Remark 6.1b (the accompanying program).* The program uses the composite $10$-point Gauss–Legendre rule on $NM$ equal sub-intervals ($M=16$ by default). Its nodes are interior to the sub-intervals, so $L/2$ is never a node, and existence of the discrete root rests on part (2)(b). The program checks the bracket $g_N^Q(t_{\rm hi})>H$ at $t_{\rm hi}=(1-10^{-14})/M_N$ explicitly and stops with an error if it fails. In all tests with $|H|<L$ it succeeded; in the degenerate regime $|H|\ge L$ it can fail for large $N$, in line with Remark 5.5.

### Algorithm 2 (a priori certified tolerance)

Given $\varepsilon>0$ and $H<L$, choose the smallest $N>2L/(L-H)$ such that

$$
\frac{4h(L-h)}{(L-2h)^2+H^2}\le\varepsilon,\qquad h=L/N .
$$

For $H\ge L$, take $N\ge2+2/\varepsilon$. By Corollary 5.2(1), the exact minimiser $\gamma_N$ of the constructed family then satisfies $J(\gamma_N)\le(1+\varepsilon)K^*$. Algorithm 2 therefore returns a mathematically certified member of $\mathcal A_N$; it does not certify optimality among all $C^\infty$ admissible graphs at finite $N$, and the certificate concerns the exact $t_N$, not the floating-point value $\widehat t_N$.

Asymptotically the certified choice is $N\approx4L^2/\big((L^2+H^2)\varepsilon\big)$. The expansion of Corollary 5.2(3) *suggests* that the resolution actually required is asymptotically $N\sim2L^2/\big((L^2+H^2)\varepsilon\big)$; this is a prediction, not a certified finite-$N$ bound, because no explicit bound on the $O(N^{-2})$ remainder is proved. The practical alternative is to compute $\widehat t_N$ and test the gap $\widehat t_N/K^*-1$ directly, which is possible because $K^*$ is known in closed form.

### Algorithm 3 (independent numerical sanity check; not part of the proof)

The epigraph program $(\mathrm P_N)$ can be handed to a generic solver such as SLSQP, started from a non-optimal feasible point (for instance a cosine curvature profile rescaled to satisfy the height constraint). By Theorem 4.11, any method that is guaranteed to return a *global* minimiser must return $t_N\hat c$. SLSQP is a local method and carries no such guarantee, so its agreement with $t_N\hat c$ only validates the implementation on the tested instance; it is also not needed to compute $\gamma_N$.

### Remark 6.2 (smoothness versus optimality)

The price of a small gap is a fast change of curvature. Since $k_N=t_N\psi_N$, Lemma 4.6 gives $|k_N'|=t_NS'(\tau)/h$ on the first and last cells. On the switching cell it gives $|k_N'|=2t_NS'(\tau)/h$ for odd $N$, and $|k_N'|=t_NS'(\tau)/h$ on each of the two switching cells for even $N$. Elsewhere $k_N'=0$. By Lemma 4.1(5), $\max S'=S'(\tfrac12)=2$, hence exactly
$$
\max_{[0,L]}|k_N'|=\begin{cases}4t_N/h=4t_NN/L, & N\text{ odd},\\ 2t_N/h=2t_NN/L, & N\text{ even}.\end{cases}
$$
This grows linearly with $N$. Even $N$ halves the maximal rate of change of curvature, at the price of a larger second-order term in the gap (Appendix A). In practice $N$ should be chosen by balancing the admissible excess over $K^*$ against the admissible rate of change of curvature; the corresponding optimisation problem for $\|dk/ds\|_\infty$ is the minimax-spirality problem discussed in §8. The linear growth of $\|k_N'\|_\infty$ is a property of the present smoothing family, not an optimality statement about spirality.

---

## 7. Numerical experiments

Data: $L=1$, $H=0.5$, so $K^*=1.6$, $R^*=0.625$, and the predicted first-order constant is $2L^2/(L^2+H^2)=1.6$. All values below are floating-point values $\widehat t_N$; implementation details are in Appendix A.

**Table 1. Value of the best candidate and its gap.**

| $N$ | $\widehat t_N$ | $\widehat t_N/K^*-1$ | $N\,(\widehat t_N/K^*-1)$ | $N\,(\widehat t_N/K^*-1)-1.6$ | bound of Cor. 5.2(1) |
|---|---|---|---|---|---|
| 5 | 2.2784680449 | $4.24\times10^{-1}$ | 2.120 | $5.2\times10^{-1}$ | — |
| 17 | 1.7622201421 | $1.01\times10^{-1}$ | 1.724 | $1.2\times10^{-1}$ | $2.15\times10^{-1}$ |
| 65 | 1.6401364655 | $2.51\times10^{-2}$ | 1.631 | $3.1\times10^{-2}$ | $5.09\times10^{-2}$ |
| 257 | 1.6100084967 | $6.26\times10^{-3}$ | 1.608 | $7.6\times10^{-3}$ | $1.26\times10^{-2}$ |
| 1025 | 1.6025005305 | $1.56\times10^{-3}$ | 1.602 | $1.9\times10^{-3}$ | $3.13\times10^{-3}$ |
| 4097 | 1.6006250332 | $3.91\times10^{-4}$ | 1.600 | $4.8\times10^{-4}$ | $7.81\times10^{-4}$ |

The column $N(\widehat t_N/K^*-1)$ approaches $1.6$, and its deviation from $1.6$ decays like $1/N$ ($N$ times the deviation is close to $2$ for large $N$), consistent with the $O(N^{-2})$ remainder in Corollary 5.2(3). The computed values are consistent with the analytic bound in every displayed row. For $N=5$ the hypothesis $N>2L/(L-H)=4$ holds, but $L-2h=0.6$ gives a bound larger than $1$, so it is omitted.

**Table 2. Second-order comparison with the shortened double arc (Theorem 5.1(4)).**

| $N$ | $\widehat t_N$ | $K^*(L-2h)$ | $K^*(L-h)$ | $N^2\,\lvert \widehat t_N-K^*(L-h)\rvert$ |
|---|---|---|---|---|
| 17 | 1.7622201421 | 1.9444911690 | 1.7608530084 | 0.395 |
| 65 | 1.6401364655 | 1.6815083827 | 1.6400601679 | 0.322 |
| 257 | 1.6100084967 | 1.6200938835 | 1.6100038697 | 0.306 |
| 1025 | 1.6025005305 | 1.6050058615 | 1.6025002436 | 0.302 |
| 4097 | 1.6006250332 | 1.6012503662 | 1.6006250152 | 0.300 |

The last column is bounded, as asserted by Theorem 5.1(4). The proven constant in that theorem tends to about $60$ for this example, so the bound is valid but not sharp.

**Length.** The total length of $\gamma_N$ converges to that of the double arc, $2R^*\arcsin(L/2R^*)=1.1591190225$, in agreement with Theorem 5.4(5): for $N=5,17,65,257,1025$ the computed lengths are $1.19017$, $1.16788$, $1.16137$, $1.15969$, $1.15926$.

---

## 8. Relation to the literature

The present problem belongs to several established lines of work, but its precise combination of graph constraints, endpoint flatness and smooth finite-dimensional approximation is more specialised. Saturated-curvature and circular-arc phenomena are classical in bounded-curvature optimal control, while the pure $L^\infty$ (minimax) curvature variational problem has been developed more recently in work on the $\infty$-elastica and on minimax-curvature curves.

**Bounded-curvature geometry.** Dubins' classical theory [1] concerns *shortest* paths under a prescribed curvature bound with fixed endpoints and tangents; saturated curvature and circular arcs are therefore longstanding features of bounded-curvature optimal control. Our problem is different: the horizontal span and vertical rise are prescribed, the curve is required to be a graph, and the objective is to minimise the maximal curvature rather than the length.

**$L^\infty$ curvature and $\infty$-elastica.** Moser [2] studied the minimisation of the $L^\infty$ norm of the curvature for curves in $\mathbb R^n$ of fixed length with prescribed endpoints and endpoint tangents, characterising solutions by a system of differential equations and classifying them; Gallagher and Moser [3] extended the framework to Riemannian manifolds. These works provide the closest variational background for the relaxed objective used here.

**Direct minimax-curvature problems.** Kaya, Noakes and Schrader [4] formulated the planar fixed-length minimax-curvature problem directly as an optimal-control problem, classified the solution types, and reduced it to a finite-dimensional computation with six variables. This is the closest prior work in spirit; its finite-dimensional reduction is unrelated to the family $\mathcal A_N$. The formulation here is complementary: span and rise are prescribed, the curve is a graph, the arc length is free, the endpoint tangents are horizontal, and all positive-order endpoint derivatives are required to vanish.

**Minimax spirality.** The minimax-spirality problem of Kaya, Noakes and Schrader [5], which minimises the $L^\infty$ norm of the arc-length derivative of the curvature and leads to Euler spirals, is the natural comparison for the curvature-variation quantity of Remark 6.2.

**Perfect splines and $L^\infty$ extremal problems.** The saturated derivative structure and its control interpretation are related to the classical theory of $L^\infty$ extremal problems and perfect splines of Fisher and Jerome [6, 7], McClure [8] and Schoenberg [9]. The present construction differs in using a $C^\infty$ flat bump basis whose integrated tangent-sine profile enters the nonlinear height constraint through $F(u)$.

**Route design.** In road and railway engineering, two opposite circular arcs joined tangentially form the classical *reverse curve*, and transition curves with prescribed smoothness of the curvature at their endpoints are standard design elements. The double arc and the smoothing of its curvature jumps thus have direct engineering counterparts, usually treated with different objectives and terminology.

**Comparison.**

| Work | Objective | Main constraints | Saturated / circular structure | Finite-dimensional reduction | Relation to this paper |
|---|---|---|---|---|---|
| Dubins (1957) [1] | minimise length | curvature bound; endpoints and tangents | yes (arcs and segments) | structural classification | classical bounded-curvature predecessor |
| Moser (2022) [2] | minimise $\|\kappa\|_\infty$ | fixed length; endpoints and tangents | structured $\infty$-elastica | ODE characterisation | continuous variational framework |
| Gallagher–Moser (2023) [3] | minimise $\|\kappa\|_\infty$ | fixed length, Riemannian manifold | generalised structure | ODE system | broader geometric framework |
| Kaya–Noakes–Schrader (2024) [4] | minimax curvature | fixed planar length; endpoints and tangents | yes | six variables | closest direct prior problem |
| Kaya–Noakes–Schrader (2026) [5] | minimax spirality | fixed planar length; endpoints and tangents | Euler-spiral structure | finite-dimensional methods | curvature-variation trade-off |
| Fisher–Jerome, McClure, Schoenberg [6–9] | $L^\infty$ extremal problems | differential and interpolation constraints | perfect splines, bang-bang | yes | precedent for the discrete comparison |
| This paper | minimise maximal graph curvature | fixed span and rise; flat smooth graph endpoints | double arc in the relaxation | exact $\mathcal A_N$ minimiser via one scalar root | specific graph and smooth-discretisation results |

**Specific contribution.** Within the literature surveyed here, we did not find a treatment combining the exact fixed-span/fixed-rise graph formulation, the proof of non-attainment under the stated $C^\infty$ flat-endpoint condition, the explicit smooth family $\mathcal A_N$, the exact discrete comparison theorem leading to the unique global minimiser $t_N\hat c$, and the first-order asymptotic formula for $t_N/K^*-1$. We regard these results, rather than the general saturated-curvature geometry, as the principal mathematical contribution.

**Limitations of this positioning.** The literature search supports the positioning above but does not establish an exhaustive priority claim. Variants of the graph problem, the smooth transition construction or the finite-dimensional approximation may occur in optimisation, geometric design, spline theory, route engineering or numerical analysis under different terminology. The novelty claim is therefore deliberately restricted to the exact formulation and results proved here.

**References**

1. L. E. Dubins, On curves of minimal length with a constraint on average curvature, and with prescribed initial and terminal positions and tangents, *Amer. J. Math.* 79 (1957), 497–516.
2. R. Moser, Structure and classification results for the $\infty$-elastica problem, *Amer. J. Math.* 144 (2022), 1299–1329.
3. E. Gallagher and R. Moser, The $\infty$-elastica problem on a Riemannian manifold, *J. Geom. Anal.* 33 (2023), no. 7, Paper 226.
4. C. Y. Kaya, L. Noakes and P. Schrader, Curves of minimax curvature, arXiv:2404.12574 (2024).
5. C. Y. Kaya, L. Noakes and P. Schrader, Curves of minimax spirality, *ESAIM: COCV* 32 (2026), Article 6, doi:10.1051/cocv/2025095.
6. S. D. Fisher and J. W. Jerome, The existence, characterization and essential uniqueness of solutions of $L^\infty$ extremal problems, *Trans. Amer. Math. Soc.* 187 (1974), 391–404, doi:10.1090/S0002-9947-1974-0364983-X.
7. S. D. Fisher and J. W. Jerome, Perfect spline solutions to $L^\infty$ extremal problems, *J. Approx. Theory* 12 (1974), 78–90.
8. D. E. McClure, Perfect spline solutions of $L_\infty$ extremal problems by control methods, *J. Approx. Theory* 15 (1975), 226–242, doi:10.1016/0021-9045(75)90105-7.
9. I. J. Schoenberg, The perfect B-splines and a time-optimal control problem, *Israel J. Math.* 10 (1971), 261–274, doi:10.1007/BF02771643.

---

## 9. Concluding remarks and open problems

1. **The graph problem.** For the fixed-span, fixed-rise graph problem with flat endpoint jets considered here, the sharp relaxed maximal-curvature value is $K^*=4|H|/(L^2+H^2)$ when $|H|<L$, and $2/L$ otherwise. It is not attained by any smooth flat-endpoint graph. When $|H|<L$ it is attained, uniquely in the $C^{1,1}$ graph class, by the double circular arc of radius $(L^2+H^2)/(4|H|)$. This gives an exact solution of the stated graph-constrained problem at the relaxed level, and an explicit smooth approximation scheme in the original class.

2. **Smooth approximation.** Within the explicit smooth family $\mathcal A_N$, the problem has a unique global minimiser, with a saturated coefficient profile, characterised exactly by one strictly monotone scalar equation. Its maximal curvature exceeds the infimum by an amount with a certified upper bound of order $1/N$, asymptotically equal to $2L^2K^*/\big((L^2+H^2)N\big)$, and for $|H|<L$ the curves converge in $C^1$ to the double arc.

3. **Key mechanism.** All proofs rest on one comparison principle, used twice.
   - *Continuous version.* The tangent-sine variable $u$ satisfies $|u'|=\kappa$ and vanishes at both ends, so $u\le KT$; since the height $\int F(u)$ is increasing in $u$, the double arc is extremal.
   - *Discrete version.* Summation by parts turns the coefficient bound $|c_j|\le t$ into the pointwise bound $u_c\le t\Psi_N$.

4. **Scope.** The graph restriction is essential when $|H|\ge L$, where the graph problem degenerates (Proposition 3.7).

5. **Open problems.**
   - *Arc-length parametrised extension.* Replace the graph restriction by arbitrary regular planar curves with prescribed endpoints and horizontal end tangents, where $\kappa=|\theta'(s)|$ in arc length and vertical tangents are allowed, and determine the exact analogue of the transition at $|H|=L$.
   - *Complexity lower bounds.* Given a smoothness or complexity measure (for instance $\|k'\|_\infty$, the number of transition layers, or a Sobolev norm), determine the optimal asymptotic relation between excess curvature and complexity. The rate $O(1/N)$ proved here is specific to $\mathcal A_N$.
   - *Joint curvature/spirality problem.* Determine the Pareto frontier for simultaneous control of $\|k\|_\infty$ and $\|dk/ds\|_\infty$ (cf. [5]), rather than treating the latter only as a diagnostic, for instance through a regularised objective $\|k\|_\infty+\lambda\|k'\|_\infty$ or a bound on $\|dk/ds\|_\infty$.

---

## Appendix A. Reproducibility and implementation checks

**Implementation checks** ($N=41$ unless stated otherwise).
- The profile lemma: $\max|\Psi_N-\Phi_N|/h$ equals $2\iota\approx0.138$ for odd $N$ and $0.5$ for even $N$ (Lemma 4.7(3)).
- Remark 6.2: the maximal rate of change of curvature is $272.9535=4t_{41}\cdot41$ for $N=41$ and $133.4652=2t_{40}\cdot40$ for $N=40$.
- Quadrature refinement: doubling the number of Gauss–Legendre sub-intervals ($M=16\to32$) leaves $t_{41}$ unchanged in double precision and changes the total length by about $10^{-15}$.
- Independent geometric checks: the length of the polygon through $2\times10^5$ points of the computed curve agrees with the computed total length to $5\times10^{-12}$; centred finite differences of the computed $\gamma_N$ and length$(x)$ agree with the computed $\gamma_N'$ and $\sqrt{1+\gamma_N'^2}$ to about $5\times10^{-9}$, which is the size of the finite-difference error itself.
- *Independent numerical sanity check (not part of the proof).* A local SLSQP solve of $(\mathrm P_{15})$, started from a cosine curvature profile, returned coefficients $\pm1$ times $1.7857667825$, agreeing with $\widehat t_{15}$ to all ten displayed digits. SLSQP is a local method, so this only validates the implementation on the tested instance.
- *Parity.* For even $N$ the second-order diagnostic $N^2|\widehat t_N-K^*(L-h)|$ settles near $3.9$ (values $4.30$, $3.95$, $3.88$, $3.86$ for $N=18,66,258,1026$), compared with about $0.30$ for odd $N$ (Table 2); both are consistent with the $O(N^{-2})$ term of Theorem 5.1(4).

**Reproducibility.** All computations use IEEE double precision.
- *Quadrature.* The values of $t_N$ in Tables 1 and 2 were computed twice: with the composite trapezoidal rule ($64$ points per cell), and with the composite $10$-point Gauss–Legendre rule on $16$ sub-intervals per cell, as in the accompanying program. The two numerical evaluations agreed to all displayed digits in double precision; this is a reproducibility statement, and quadrature refinement was used as a diagnostic, not as a proof of accuracy.
- *The integral $I(\tau)$.* It is tabulated on $256$ equal sub-intervals of $[0,1]$ by the $10$-point Gauss–Legendre rule, and completed by the same rule on the last partial sub-interval.
- *Root finding.* $t_N$ is computed by Brent's method on $[0,(1-10^{-14})/M_N]$, with absolute tolerance $10^{-15}$ and relative tolerance $4\varepsilon_{\rm mach}$.
- *Endpoint residual.* The residual $\gamma_N(1)-0.5\approx6\times10^{-16}$ is computed with the same quadrature as the root, so it measures root-finding and rounding error only; the quadrature error is assessed separately by refinement and by the independent checks listed above.
- *Curvature check.* The identity "maximal curvature $=t_N$" is exact by Proposition 4.3, so recomputing it from $\gamma_N'$ and $\gamma_N''$ only checks the implementation, not the theory.