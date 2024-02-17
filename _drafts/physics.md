---
title: 'Physics 🍊⭐'
date: 2023-01-01
permalink: /note/physics
tags:
  - note
toc: true
---

Equations of fundamental physics.

{% include toc %}

## Thermodynamics / 熱力学

### Laws of thermodynamics / 熱力学法則

$$
\begin{align*}
dU &= dQ + dW \\
dS &\geq 0
\end{align*}
$$
{: .notice--info}

### Ideal gas / 理想気体

$$
\begin{align*}
PV &= nRT \\
dU &= nC_v dT
\end{align*}
$$
{: .notice--info}

### Thermodynamic function / 熱力学関数

$$
\begin{align*}
dU &= TdS - PdV + \mu dN \\
dH &= TdS + VdP + \mu dN \\
dF &= -SdT - PdV + \mu dN \\
dG &= -SdT + VdP + \mu dN
\end{align*}
$$
{: .notice--info}

### Thermal equilibrium / 熱平衡

$$
\begin{align*}
& dQ = 0 : & dS \geq 0 \\
& dT = dV = 0 : & dF \leq 0 \\
& dT = dP = 0 : & dG \leq 0
\end{align*}
$$
{: .notice--info}

### Classical statistics / 古典統計

$$
\begin{align*}
f_i &= A e^{-\epsilon_i/kT} \\
\Omega_i &= \frac{1}{h^d}\int_{V_i}d\hat{q}d\hat{p}
\end{align*}
$$
{: .notice--info}

### Microcanonical ensemble / 小正準集団

$$
\begin{align*}
& W(E,V,N) \\
& S = k\log W
\end{align*}
$$
{: .notice--info}

### Canonical ensemble / 正準集団

$$
\begin{align*}
& Z(T,V,N) = \sum_i e^{-E_i/kT} \\
& F = -kT\log Z
\end{align*}
$$
{: .notice--info}

### Grand canonical ensemble / 大正準集団

$$
\begin{align*}
& \Xi(T,V,\mu) = \sum_{N,i} e^{-(E_i-\mu N)/kT} \\
& J = -kT\log \Xi
\end{align*}
$$
{: .notice--info}

### Quantum statistics / 量子統計

$$
\begin{align*}
f^{FD}_i &= \frac{1}{e^{(\epsilon_i-\mu)/kT}+1} \\
f^{BE}_i &= \frac{1}{e^{(\epsilon_i-\mu)/kT}-1}
\end{align*}
$$
{: .notice--info}