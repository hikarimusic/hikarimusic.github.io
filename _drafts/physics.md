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








## Classical Mechanics / 古典力学

### Equations of Motion / 運動方程式

$$
\begin{align*}
\mathbf{r'} &= \mathbf{r} - \mathbf{v}t\\
q_i' &= q_i'(q_j,\dots)
\end{align*}
$$
{: .notice--info}

$$
\begin{align*}
L(q_i, \dot{q_i}, \dots) &= T - U \\
\delta\int_{t_1}^{t_2}L\,dt &= 0
\end{align*}
$$
{: .notice--info}

$$
\begin{align*}
\frac{\partial L}{\partial q_i} - \frac{d}{dt}\frac{\partial L}{\partial\dot{q_i}} &= 0 \\
-\mathbf{\nabla} U = m\ddot{\mathbf{r}}
\end{align*}
$$
{: .notice--info}

### Conservation Law / 保存則

$$
\begin{align*}
& U = U(\mathbf{r}): && \frac{1}{2}m\mathbf{\dot{r}}^2+U = const.\\
& U = U(\mathbf{r_i},\dots): && \sum_{i}\frac{1}{2}m_i\mathbf{\dot{r_i}}^2+U=const.
\end{align*}
$$
{: .notice--info}

$$
\begin{align*}
& U = const.: && m\mathbf{\dot{r}} = const. \\
& U = \sum_{i,j}U_{ij}(|\mathbf{r_i}-\mathbf{r_j}|): && \sum_{i}m_i\mathbf{\dot{r_i}} = const.
\end{align*}
$$
{: .notice--info}

$$
\begin{align*}
& U = U(|\mathbf{r}|): && \mathbf{r}\times m\mathbf{\dot{r}} = const. \\
& U = \sum_{i}U(|\mathbf{r_i}|)+\sum_{i,j}U_{ij}(|\mathbf{r_i}-\mathbf{r_j}|): && \sum_{i}\mathbf{r_i}\times m_i\mathbf{\dot{r_i}} = const. 
\end{align*}
$$
{: .notice--info}