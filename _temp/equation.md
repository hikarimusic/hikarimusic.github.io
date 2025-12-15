---
title: 'Equation'
date: 2000/01/01
permalink: /temp/equation
tags:
  - note
toc: true
---

Some random equations

{% include toc %}

# Classical Mechanics / 古典力学

$$
\begin{aligned}
& S = \int_{t_1}^{t_2} L\left(q_i,\dot q_i,t\right)\,dt \\
& \delta S = 0
\end{aligned}
$$

# Electromagnetism / 電磁気学

$$
\begin{aligned}
&\nabla\cdot \mathbf{E} = \frac{\rho}{\varepsilon_0} \\
&\nabla\times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t} \\
&\nabla\cdot \mathbf{B} = 0 \\
&\nabla\times \mathbf{B} = \mu_0 \mathbf{J} + \mu_0\varepsilon_0 \frac{\partial \mathbf{E}}{\partial t}
\end{aligned}
$$

# Statistical Mechanics / 統計力学

$$
\begin{aligned}
& S = - k_B \sum_i p_i \ln p_i \\
& \delta S = 0 \\
& dU = T\,dS - P\,dV + \mu\,dN
\end{aligned}
$$

# Quantum Mechanics / 量子力学

$$
\begin{aligned}
& |\psi\rangle \in \mathcal{H} \\
& \hat{A} = \hat{A}^\dagger \\
& P(a_n) = |\langle a_n | \psi \rangle|^2 \\
& i\hbar \frac{\partial}{\partial t} |\psi(t)\rangle = \hat{H}|\psi(t)\rangle
\end{aligned}
$$

## Formulation / 定式化

### State / 状態

$$
\begin{aligned}
& \langle m | n \rangle = \delta_{mn} \quad && \langle a | a' \rangle = \delta(a - a') \\
& \sum_n |n\rangle\langle n| = \mathbb I \quad && \int |a\rangle\langle a| \, da = \mathbb I \\
& |\psi\rangle = \sum_n |n\rangle\langle n|\psi\rangle \quad && |\psi\rangle = \int |a\rangle\langle a|\psi\rangle \, da
\end{aligned}
$$

### Observable / オブザーバブル

$$
\begin{aligned}
& \hat{A}|a\rangle = a|a\rangle \quad \langle a | a \rangle = \mathbb I \\
& a = a^* \quad \langle a_n | a_m \rangle = \delta_{nm} \\
& \hat{A} = \sum_a a |a\rangle\langle a| \quad \hat{A} = \int a |a\rangle\langle a| \, da
\end{aligned}
$$

### Measurement / 測定

$$
\begin{aligned}
& p(a) = \langle \psi | \hat{P}_a | \psi \rangle \\
& \langle \hat{A} \rangle = \langle \psi | \hat{A} | \psi \rangle \\
& |\psi\rangle \to \frac{\hat{P}_a |\psi\rangle}{\sqrt{\langle \psi | \hat{P}_a | \psi \rangle}}
\end{aligned}
$$

### Evolution / 発展

$$
\begin{aligned}
& |\psi(t)\rangle = \hat U(t,t_0)\,|\psi(t_0)\rangle \\
& \hat U^\dagger(t,t_0)\,\hat U(t,t_0) = \mathbb I \\
& \hat U(t,t_0) = \exp\!\left[-\frac{i}{\hbar}\,\hat H\,\bigl(t-t_0\bigr)\right] \\
& \hat U(t,t_0) = \mathcal T \exp\!\left[-\frac{i}{\hbar}\int_{t_0}^{t}\hat H(t')\,dt'\right] \\
\end{aligned}
$$
