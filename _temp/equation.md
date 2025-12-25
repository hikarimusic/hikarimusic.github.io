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
{: .notice--info}

# Electromagnetism / 電磁気学

$$
\begin{aligned}
&\nabla\cdot \mathbf{E} = \frac{\rho}{\varepsilon_0} \\
&\nabla\times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t} \\
&\nabla\cdot \mathbf{B} = 0 \\
&\nabla\times \mathbf{B} = \mu_0 \mathbf{J} + \mu_0\varepsilon_0 \frac{\partial \mathbf{E}}{\partial t}
\end{aligned}
$$
{: .notice--info}

# Statistical Mechanics / 統計力学

$$
\begin{aligned}
& S = - k_B \sum_i p_i \ln p_i \\
& \delta S = 0 \\
& dU = T\,dS - P\,dV + \mu\,dN
\end{aligned}
$$
{: .notice--info}

# Quantum Mechanics / 量子力学

$$
\begin{aligned}
& |\psi\rangle \in \mathcal{H} \\
& \hat{A} = \hat{A}^\dagger \\
& P(a_n) = |\langle a_n | \psi \rangle|^2 \\
& i\hbar \frac{\partial}{\partial t} |\psi(t)\rangle = \hat{H}|\psi(t)\rangle
\end{aligned}
$$
{: .notice--info}

## Formulation / 定式化

### State / 状態

$$
\begin{aligned}
& \langle m | n \rangle = \delta_{mn} && \langle a | a' \rangle = \delta(a - a') \\
& \sum_n |n\rangle\langle n| = \mathbb I && \int |a\rangle\langle a| \, da = \mathbb I \\
& |\psi\rangle = \sum_n |n\rangle\langle n|\psi\rangle && |\psi\rangle = \int |a\rangle\langle a|\psi\rangle \, da
\end{aligned}
$$
{: .notice--info}

### Observable / オブザーバブル

$$
\begin{aligned}
& \hat{A}|a\rangle = a|a\rangle \quad \langle a | a \rangle = \mathbb I \\
& a = a^* \quad \langle a_n | a_m \rangle = \delta_{nm} \\
& \hat{A} = \sum_a a |a\rangle\langle a| \quad \hat{A} = \int a |a\rangle\langle a| \, da
\end{aligned}
$$
{: .notice--info}

### Measurement / 測定

$$
\begin{aligned}
& p(a) = \langle \psi | \hat{P}_a | \psi \rangle \\
& \langle \hat{A} \rangle = \langle \psi | \hat{A} | \psi \rangle \\
& |\psi\rangle \to \frac{\hat{P}_a |\psi\rangle}{\sqrt{\langle \psi | \hat{P}_a | \psi \rangle}}
\end{aligned}
$$
{: .notice--info}

### Evolution / 発展

$$
\begin{aligned}
& |\psi(t)\rangle = \hat U(t,t_0)\,|\psi(t_0)\rangle \\
& \hat U^\dagger(t,t_0)\,\hat U(t,t_0) = \mathbb I \\
& \hat U(t,t_0) = \exp\left[-\frac{i}{\hbar}\,\hat H\,\bigl(t-t_0\bigr)\right] \\
& \hat U(t,t_0) = \mathcal T \exp\left[-\frac{i}{\hbar}\int_{t_0}^{t}\hat H(t')\,dt'\right] \\
\end{aligned}
$$
{: .notice--info}

### Wave function / 波動関数

$$
\begin{aligned}
& |\psi\rangle \to \psi \\
& \hat{x} \to x \\
& \hat{p} \to -i\hbar \frac{d}{dx}
\end{aligned}
$$
{: .notice--info}

### Schrödinger equation / シュレーディンガー方程式

$$
\begin{aligned}
& -\frac{\hbar^2}{2m} \frac{\partial^2\Psi(x,t)}{\partial x^2} + V(x)\Psi(x,t) = i\hbar \frac{\partial\Psi(x,t)}{\partial t} \\
& -\frac{\hbar^2}{2m} \frac{d^2\psi(x)}{dx^2} + V(x)\psi(x) = E\psi(x)
\end{aligned}
$$
{: .notice--info}

### Change of basis / 基底変換

$$
\begin{aligned}
& \langle x | x' \rangle = \delta(x - x') && \langle p | p' \rangle = \delta(p - p') \\
& \langle x | p \rangle = \frac{1}{\sqrt{2\pi\hbar}} e^{\frac{i}{\hbar}px} && \langle p | x \rangle = \frac{1}{\sqrt{2\pi\hbar}} e^{-\frac{i}{\hbar}px} \\
& \phi(p) = \frac{1}{\sqrt{2\pi\hbar}} \int_{-\infty}^{\infty} \psi(x) e^{-\frac{i}{\hbar}px} dx && \psi(x) = \frac{1}{\sqrt{2\pi\hbar}} \int_{-\infty}^{\infty} \phi(p) e^{\frac{i}{\hbar}px} dp
\end{aligned}
$$
{: .notice--info}

### Uncertainty principle / 不確定性原理

$$
\begin{aligned}
& [\hat{x}, \hat{p}] = i\hbar \\
& \Delta x \Delta p \geq \frac{\hbar}{2}
\end{aligned} \\
\psi(x) = \frac{1}{(2\pi\sigma^2)^{1/4}} \exp\left[-\frac{(x-x_0)^2}{4\sigma^2}\right] \exp\left[\frac{i}{\hbar}p_0(x-x_0)\right]
$$
{: .notice--info}

### Probability current / 確率流密度

$$
\begin{aligned}
& \frac{\partial |\Psi|^2}{\partial t} = -\nabla \cdot \mathbf{j} \\
& \mathbf{j} = \frac{\hbar}{2mi} (\Psi^* \nabla \Psi - \Psi \nabla \Psi^*)
\end{aligned}
$$
{: .notice--info}

### Ehrenfest's theorem / エーレンフェストの定理

$$
\begin{aligned}
& \frac{d}{dt} \langle \hat{A} \rangle = \frac{1}{i\hbar} \langle [\hat{A}, \hat{H}] \rangle \\
& \frac{d}{dt} \langle \hat{x} \rangle = \left\langle \frac{\partial \hat{H}}{\partial \hat{p}} \right\rangle \\
& \frac{d}{dt} \langle \hat{p} \rangle = \left\langle -\frac{\partial \hat{H}}{\partial \hat{x}} \right\rangle
\end{aligned}
$$
{: .notice--info}
