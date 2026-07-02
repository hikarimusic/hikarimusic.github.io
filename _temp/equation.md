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
\begin{aligned}{}
& \Delta E = 0 \\
& \Delta S \geq 0 \\
& p_i = \frac{1}{\Omega}
\end{aligned}
$$
{: .notice--info}

## Thermodynamics

## General Principle

## Ensemble Theory

## Ideal Classical System

## Quamtum Statistics

## Ideal Quantum System

## Interacting System

## Phase Transition

## Non-Equilibrium


# Quantum Mechanics / 量子力学

$$
\begin{aligned}{}
& |\psi\rangle \in \mathcal{H} \\
& \hat{A} = \hat{A}^\dagger \\
& P(a_n) = |\langle a_n | \psi \rangle|^2 \\
& i\hbar \frac{d}{d t} |\psi(t)\rangle  = \hat{H}|\psi(t)\rangle 
\end{aligned}
$$
{: .notice--info}


## Formalism / 形式論

### State / 状態

$$
\begin{aligned}{}
& \langle n|m\rangle = \delta_{mn}, \quad
\langle x|x'\rangle = \delta(x-x') \\
& \sum_{n}|n\rangle\langle n| = I, \quad
\int |x\rangle\langle x|\,dx = I \\
& |\psi\rangle = \sum_{n}|n\rangle\langle n|\psi\rangle, \quad
|\psi\rangle = \int |x\rangle\langle x|\psi\rangle\,dx \\
& \sum_{n}|\langle n|\psi\rangle|^{2}=1, \quad
\int |\langle x|\psi\rangle|^{2}\,dx = 1
\end{aligned}
$$
{: .notice--info}

### Observable / 観測量

$$
\begin{aligned}{}
& \hat{A}|a_n\rangle = a_n|a_n\rangle \\
& a_n = a_n^{*} \\
& \langle a_n|a_m\rangle = \delta_{nm} \\
& \hat{A} = \sum_{n}a_n|a_n\rangle\langle a_n|
= \int a|a\rangle\langle a|\,da
\end{aligned}
$$
{: .notice--info}

### Measurement / 測定

$$
\begin{aligned}{}
& \hat{P}_{a}=\sum_{\alpha}|a,\alpha\rangle\langle a,\alpha| \\
& P(a)=\langle\psi|\hat{P}_{a}|\psi\rangle \\
& |\psi\rangle \rightarrow
\frac{\hat{P}_{a}|\psi\rangle}
{\sqrt{\langle\psi|\hat{P}_{a}|\psi\rangle}} \\
& \langle\hat{A}\rangle=\langle\psi|\hat{A}|\psi\rangle
\end{aligned}
$$
{: .notice--info}

### Evolution / 時間発展

$$
\begin{aligned}{}
& |\psi(t)\rangle = \hat{U}(t,t_0)|\psi(t_0)\rangle \\
& \hat{U}^{\dagger}(t,t_0)\hat{U}(t,t_0)=I \\
& \hat{U}(t,t_0)=\exp\left[-\frac{i}{\hbar}\hat{H}(t-t_0)\right] \\
& \hat{U}(t,t_0)=\mathcal{T}\exp\left[-\frac{i}{\hbar}
\int_{t_0}^{t}\hat{H}(t')\,dt'\right]
\end{aligned}
$$
{: .notice--info}


## Wave Mechanics / 波動力学

### Wave Function / 波動関数

$$
\begin{aligned}{}
& \psi(\mathbf{r},t) = \langle \mathbf{r}|\psi(t)\rangle \\
& \phi(\mathbf{p},t) = \langle \mathbf{p}|\psi(t)\rangle \\
& \psi(\mathbf{r}) = \frac{1}{(2\pi\hbar)^{3/2}}\int \phi(\mathbf{p})e^{\frac{i}{\hbar}\mathbf{p}\cdot\mathbf{r}}\,d^{3}p \\
& \phi(\mathbf{p}) = \frac{1}{(2\pi\hbar)^{3/2}}\int \psi(\mathbf{r})e^{-\frac{i}{\hbar}\mathbf{p}\cdot\mathbf{r}}\,d^{3}r
\end{aligned}
$$
{: .notice--info}

### Operator / 演算子

$$
\begin{aligned}{}
& \hat{\mathbf{r}}\psi(\mathbf{r}) = \mathbf{r}\psi(\mathbf{r}), \quad
\hat{\mathbf{p}}\psi(\mathbf{r}) = -i\hbar\nabla\psi(\mathbf{r}) \\
& \hat{\mathbf{p}}\phi(\mathbf{p}) = \mathbf{p}\phi(\mathbf{p}), \quad
\hat{\mathbf{r}}\phi(\mathbf{p}) = i\hbar\nabla_{\mathbf{p}}\phi(\mathbf{p}) \\
& [\hat{x}_i,\hat{p}_j] = i\hbar\delta_{ij}, \quad
[\hat{x}_i,\hat{x}_j] = 0, \quad
[\hat{p}_i,\hat{p}_j] = 0
\end{aligned}
$$
{: .notice--info}


### Expectation Value / 期待値

$$
\begin{aligned}{}
& \langle \hat{A}\rangle = \int \psi^{*}(\mathbf{r})\hat{A}\psi(\mathbf{r})\,d^{3}r \\
& \Delta A\Delta B \geq \frac{1}{2}\left|\langle[\hat{A},\hat{B}]\rangle\right| \\
& \Delta x\Delta p \geq \frac{\hbar}{2}
\end{aligned}
$$
{: .notice--info}


### Schrödinger Equation / Schrödinger方程式

$$
\begin{aligned}{}
& \left[-\frac{\hbar^{2}}{2m}\nabla^{2}+V(\mathbf{r},t)\right]\psi(\mathbf{r},t)
= i\hbar\frac{\partial}{\partial t}\psi(\mathbf{r},t) \\
& \left[-\frac{\hbar^{2}}{2m}\nabla^{2}+V(\mathbf{r})\right]u(\mathbf{r})
= Eu(\mathbf{r}) \\
& \psi(\mathbf{r},t)=\sum_{n}c_{n}u_{n}(\mathbf{r})e^{-\frac{i}{\hbar}E_{n}t}
\end{aligned}
$$
{: .notice--info}


### Probability Current / 確率流

$$
\begin{aligned}{}
& \rho(\mathbf{r},t)=|\psi(\mathbf{r},t)|^{2} \\
& \mathbf{j}(\mathbf{r},t)=\frac{\hbar}{2mi}\left(\psi^{*}\nabla\psi-\psi\nabla\psi^{*}\right) \\
& \frac{\partial\rho}{\partial t}+\nabla\cdot\mathbf{j}=0
\end{aligned}
$$
{: .notice--info}


### Ehrenfest Theorem / Ehrenfestの定理

$$
\begin{aligned}{}
& \frac{d}{dt}\langle\hat{A}\rangle
= \frac{1}{i\hbar}\langle[\hat{A},\hat{H}]\rangle
+\left\langle\frac{\partial\hat{A}}{\partial t}\right\rangle \\
& \frac{d}{dt}\langle\hat{\mathbf{r}}\rangle
= \frac{\langle\hat{\mathbf{p}}\rangle}{m} \\
& \frac{d}{dt}\langle\hat{\mathbf{p}}\rangle
= -\langle\nabla V\rangle
\end{aligned}
$$
{: .notice--info}


## 1D System / 一次元系

### Boundary Conditions / 境界条件

$$
\begin{aligned}{}
& -\frac{\hbar^2}{2m} \frac{d^2\psi(x)}{dx^2} + V(x)\psi(x) = E\psi(x) \\
& V(x_0) < \infty \rightarrow \psi(x_0^+) = \psi(x_0^-), \quad \psi'(x_0^+) = \psi'(x_0^-) \\
& V(x_0) = \infty \rightarrow \psi(x_0^+) = \psi(x_0^-)
\end{aligned}
$$
{: .notice--info}


### Free Particle / 自由粒子

$$
\begin{aligned}{}
& V(x) = 0 \\
& \psi(x) = A e^{ikx} + B e^{-ikx} \\
& k = \frac{\sqrt{2mE}}{\hbar}
\end{aligned}
$$
{: .notice--info}


### Potential Step / ポテンシャル段差

$$
\begin{aligned}{}
& V(x) = \begin{cases} 0, & x < 0 \\ V_0, & x \geq 0 \end{cases} \\
& \psi(x) = \begin{cases} A e^{ik_1 x} + B e^{-ik_1 x}, & x < 0 \\ C e^{ik_2 x}, & x \geq 0 \end{cases} \\
& E > V_0: \quad k_1 = \frac{\sqrt{2mE}}{\hbar}, \quad k_2 = \frac{\sqrt{2m(E-V_0)}}{\hbar} \\
& R = \left( \frac{k_1 - k_2}{k_1 + k_2} \right)^2, \quad T = \frac{4k_1 k_2}{(k_1 + k_2)^2}
\end{aligned}
$$
{: .notice--info}


### Potential Barrier / ポテンシャル障壁

$$
\begin{aligned}{}
& V(x) = 
\begin{cases} 
0, & x < 0 \\
V_0, & 0 \leq x \leq a \\ 
0, & x > a 
\end{cases} \\
& \psi(x) = 
\begin{cases} 
A e^{ikx} + B e^{-ikx}, & x < 0 \\ 
C e^{\kappa x} + D e^{-\kappa x}, & 0 \leq x \leq a \\ 
F e^{ikx}, & x > a 
\end{cases} \\
& E < V_0: \quad k = \frac{\sqrt{2mE}}{\hbar}, \quad \kappa = \frac{\sqrt{2m(V_0-E)}}{\hbar} \\
& R = \left[ 1 + \frac{4E(V_0-E)}{V_0^2 \sinh^2(\kappa a)} \right]^{-1}, \quad T = \left[ 1 + \frac{V_0^2 \sinh^2(\kappa a)}{4E(V_0-E)} \right]^{-1}
\end{aligned}
$$
{: .notice--info}


### Square Well / 井戸型ポテンシャル

$$
\begin{aligned}{}
& V(x) = 
\begin{cases} 
0, & 0 < x < L \\ 
\infty, & x\leq 0,\; x\geq L
\end{cases} \\
& \psi_n(x) = \sqrt{\frac{2}{L}} \sin\left(\frac{n\pi x}{L}\right)\\
& E_n = \frac{\hbar^2 \pi^2 n^2}{2mL^2}, \quad n=1,2,3,\dots
\end{aligned}
$$
{: .notice--info}


### Harmonic Oscillator / 調和振動子

$$
\begin{aligned}{}
& V(x) = \frac{1}{2} m \omega^2 x^2 \\
& \psi_n(x) = \frac{1}{\sqrt{2^n n!}} \left( \frac{m\omega}{\pi\hbar} \right)^{1/4} H_n \left( \sqrt{\frac{m\omega}{\hbar}} x \right) \exp\left( -\frac{m\omega x^2}{2\hbar} \right) \\
& E_n = \hbar \omega \left( n + \frac{1}{2} \right), \quad n = 0, 1, 2, \dots
\end{aligned}
$$
{: .notice--info}


### Ladder Operator / 昇降演算子

$$
\begin{aligned}{}
& \hat{a} = \sqrt{\frac{m\omega}{2\hbar}} \hat{x} + \frac{i}{\sqrt{2m\hbar\omega}} \hat{p}, \quad \hat{a}^\dagger = \sqrt{\frac{m\omega}{2\hbar}} \hat{x} - \frac{i}{\sqrt{2m\hbar\omega}} \hat{p} \\
& \hat{a}|n\rangle = \sqrt{n}|n-1\rangle, \quad \hat{a}^\dagger|n\rangle = \sqrt{n+1}|n+1\rangle \\
& \hat{H}|n\rangle = \hbar\omega\left( n + \frac{1}{2} \right)|n\rangle
\end{aligned}
$$
{: .notice--info}


## Symmetry / 対称性

### Spatial Translational Symmetry / 空間並進対称性

$$
\begin{aligned}{}
& \hat{\mathbf{p}} = -i\hbar\nabla \\
& \hat{U}_{\mathbf{a}} = e^{-\frac{i}{\hbar}\mathbf{a}\cdot\hat{\mathbf{p}}} \to \hat{U}_{\mathbf{a}}\psi(\mathbf{r}) = \psi(\mathbf{r}-\mathbf{a}) \\
& \langle \hat{U}_{\mathbf{a}}\psi|\hat{H}|\hat{U}_{\mathbf{a}}\psi\rangle = \langle\psi|\hat{H}|\psi\rangle \to \frac{d}{dt}\langle\hat{\mathbf{p}}\rangle = 0
\end{aligned}
$$
{: .notice--info}


### Rotational Symmetry / 回転対称性

$$
\begin{aligned}{}
& \hat{\mathbf{L}} = -i\hbar\mathbf{r}\times\nabla \\
& \hat{U}_{\boldsymbol{\theta}} = e^{-\frac{i}{\hbar}\boldsymbol{\theta}\cdot\hat{\mathbf{L}}} \to \hat{U}_{\boldsymbol{\theta}}\psi(\mathbf{r}) = \psi(R_{\boldsymbol{\theta}}^{-1}\mathbf{r}) \\
& \langle \hat{U}_{\boldsymbol{\theta}}\psi|\hat{H}|\hat{U}_{\boldsymbol{\theta}}\psi\rangle = \langle\psi|\hat{H}|\psi\rangle \to \frac{d}{dt}\langle\hat{\mathbf{L}}\rangle = 0
\end{aligned}
$$
{: .notice--info}


### Time Translational Symmetry / 時間並進対称性

$$
\begin{aligned}{}
& \hat{E} = i\hbar\frac{\partial}{\partial t} \\
& \hat{U}_{\tau} = e^{-\frac{i}{\hbar}\tau\hat{E}} \to \hat{U}_{\tau}\psi(t) = \psi(t+\tau) \\
& \langle \hat{U}_{\tau}\psi|\hat{H}|\hat{U}_{\tau}\psi\rangle = \langle\psi|\hat{H}|\psi\rangle \to \frac{d}{dt}\langle\hat{E}\rangle = 0
\end{aligned}
$$
{: .notice--info}


### Parity Symmetry / パリティ対称性

$$
\begin{aligned}{}
& \hat{\Pi}\psi(\mathbf{r}) = \psi(-\mathbf{r}), \quad \pi = \pm 1 \\
& \langle \hat{\Pi}\psi|\hat{H}|\hat{\Pi}\psi\rangle = \langle\psi|\hat{H}|\psi\rangle \to \frac{d}{dt}\langle\hat{\Pi}\rangle = 0
\end{aligned}
$$
{: .notice--info}


## Angular Momentum / 角運動量

### Angular Momentum Operator / 角運動量演算子

$$
\begin{aligned}{}
& [\hat{J}_i, \hat{J}_j] = i\hbar \epsilon_{ijk} \hat{J}_k, \quad [\hat{\mathbf{J}}^2, \hat{J}_i] = 0 \\
& \hat{J}_+ = \hat{J}_x + i\hat{J}_y, \quad \hat{J}_- = \hat{J}_x - i\hat{J}_y \\
& \hat{J}_{\pm}|j,m\rangle = \hbar\sqrt{j(j+1) - m(m \pm 1)} |j, m \pm 1\rangle \\
& \hat{\mathbf{J}}^2|j,m\rangle = \hbar^2 j(j+1)|j,m\rangle, \quad j=0, \frac{1}{2}, 1, \dots \\
& \hat{J}_z|j,m\rangle = \hbar m|j,m\rangle, \quad m=-j, -j+1, \dots, j
\end{aligned}
$$
{: .notice--info}


### Orbital Angular Momentum / 軌道角運動量

$$
\begin{aligned}{}
& \hat{\mathbf{L}} = -i\hbar \mathbf{r} \times \nabla \to [\hat{L}_i, \hat{L}_j] = i\hbar \epsilon_{ijk} \hat{L}_k\\
& \hat{\mathbf{L}}^2 = -\hbar^2 \left[\frac{1}{\sin\theta}\frac{\partial}{\partial\theta}\left(\sin\theta\frac{\partial}{\partial\theta}\right) + \frac{1}{\sin^2\theta}\frac{\partial^2}{\partial\phi^2}\right] \\
& \hat{L}_z = -i\hbar\frac{\partial}{\partial\phi} \\
& \hat{\mathbf{L}}^2|l,m\rangle = \hbar^2 l(l+1)|l,m\rangle, \quad l=0, 1, 2, \dots \\
& \hat{L}_z|l,m\rangle = \hbar m|l,m\rangle, \quad m=-l, -l+1, \dots, l \\
& Y_l^m(\theta, \phi) = (-1)^m \sqrt{\frac{(2l+1)}{4\pi}\frac{(l-m)!}{(l+m)!}} P_l^m(\cos\theta) e^{im\phi}
\end{aligned}
$$
{: .notice--info}


### Spin Angular Momentum / スピン角運動量

$$
\begin{aligned}{}
& \hat{\mathbf{S}} = \frac{\hbar}{2} \boldsymbol{\sigma} \to [\hat{S}_i, \hat{S}_j] = i\hbar \epsilon_{ijk} \hat{S}_k\\
& \hat{S}_x = \frac{\hbar}{2} \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad \hat{S}_y = \frac{\hbar}{2} \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \quad \hat{S}_z = \frac{\hbar}{2} \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \\
& \hat{\mathbf{S}}^2|s,m\rangle = \hbar^2 s(s+1)|s,m\rangle, \quad s=\frac{1}{2} \\
& \hat{S}_z|s,m\rangle = \hbar m|s,m\rangle, \quad m=-\frac{1}{2}, \frac{1}{2} \\
& \hat{H} = -\gamma \hat{\mathbf{S}} \cdot \mathbf{B}, \quad \omega_L = \gamma B
\end{aligned}
$$
{: .notice--info}


### Addition of Angular Momentum / 角運動量の合成

$$
\begin{aligned}{}
& \hat{\mathbf{J}} = \hat{\mathbf{J}}_1 + \hat{\mathbf{J}}_2 \to [\hat{J}_i, \hat{J}_j] = i\hbar \epsilon_{ijk} \hat{J}_k \\
& \hat{\mathbf{J}}^2|j,m\rangle = \hbar^2 j(j+1)|j,m\rangle, \quad j=|j_1-j_2|, |j_1-j_2|+1, \dots, j_1+j_2 \\
& \hat{J}_z|j,m\rangle = \hbar m|j,m\rangle, \quad m=-j, -j+1, \dots, j \\
& |j_1,j_2;j,m\rangle = \sum_{m_1,m_2} C_{j_1m_1j_2m_2}^{jm} |j_1,m_1\rangle |j_2,m_2\rangle \\
& C_{j_1m_1j_2m_2}^{jm} \neq 0 \to m = m_1 + m_2 \\
& \sum_{m_1,m_2} C_{j_1m_1j_2m_2}^{jm} C_{j_1m_1j_2m_2}^{j'm'} = \delta_{jj'}\delta_{mm'}
\end{aligned}
$$
{: .notice--info}


## 3D System / 三次元系

### Central Potential / 中心力ポテンシャル

$$
\begin{aligned}{}
& -\frac{\hbar^2}{2m}\nabla^2\psi(\mathbf{r}) + V(\mathbf{r})\psi(\mathbf{r}) = E\psi(\mathbf{r}) \\
& V(\mathbf{r}) = V(r), \quad \psi(\mathbf{r}) = R(r)Y_l^m(\theta,\phi), \quad u(r) = rR(r) \\
& -\frac{\hbar^2}{2m}\frac{d^2u(r)}{dr^2} + \left[V(r) + \frac{\hbar^2 l(l+1)}{2mr^2}\right]u(r) = Eu(r)
\end{aligned}
$$
{: .notice--info}


### Infinite Spherical Well / 無限球形井戸

$$
\begin{aligned}{}
& V(r) = \begin{cases} 0, & r < a \\ \infty, & r \geq a \end{cases} \\
& \psi_{nlm}(r,\theta,\phi) = \frac{\sqrt{2}}{a^{3/2}\left|j_{l+1}(\alpha_{nl})\right|} j_l(k_{nl}r)Y_l^m(\theta,\phi) \\
& j_l(\alpha_{nl})=0, \quad k_{nl} = \frac{\alpha_{nl}}{a} \\
& E_{nl} = \frac{\hbar^2 k_{nl}^2}{2m}, \quad n = 1,2,3,\dots, \quad l = 0,1,2,\dots
\end{aligned}
$$
{: .notice--info}


### Isotropic Harmonic Oscillator / 等方性調和振動子

$$
\begin{aligned}{}
& V(r) = \frac{1}{2}m\omega^2 r^2 \\
& \psi_{n_x n_y n_z}(x,y,z) = \psi_{n_x}(x)\psi_{n_y}(y)\psi_{n_z}(z) \\
& N = n_x+n_y+n_z, \quad g_N = \frac{(N+1)(N+2)}{2} \\
& E_N = \hbar\omega\left(N+\frac{3}{2}\right), \quad N = 0,1,2,\dots
\end{aligned}
$$
{: .notice--info}


### Hydrogen Atom / 水素原子

$$
\begin{aligned}{}
& V(r) = -\frac{e^2}{4\pi\epsilon_0 r} \\
& \psi_{nlm}(r,\theta,\phi) = \sqrt{\left(\frac{2}{na_0}\right)^3 \frac{(n-l-1)!}{2n[(n+l)!]}} e^{-\rho} (2\rho)^l L_{n-l-1}^{2l+1}(2\rho) Y_l^m(\theta,\phi) \\
& a_0 = \frac{4\pi\epsilon_0\hbar^2}{me^2}, \quad \rho = \frac{r}{na_0} \\
& E_n = -\frac{me^4}{2(4\pi\varepsilon_0)^2\hbar^2}\frac{1}{n^2}, \quad n=1,2,3,\dots
\end{aligned}
$$
{: .notice--info}


### Electromagnetic Potential / 電磁ポテンシャル

$$
\begin{aligned}{}
& \hat{H}\psi = \left[\frac{1}{2m}(\hat{\mathbf{p}} - q\mathbf{A})^2 + q\Phi\right]\psi = i\hbar\frac{\partial\psi}{\partial t} \\
& \mathbf{A}' = \mathbf{A} + \nabla\chi, \quad \Phi' = \Phi - \frac{\partial\chi}{\partial t}, \quad \psi' = e^{\frac{i}{\hbar}q\chi}\psi \\
& \hat{H'}\psi' = \left[\frac{1}{2m}(\hat{\mathbf{p}} - q\mathbf{A'})^2 + q\Phi'\right]\psi' = i\hbar\frac{\partial\psi'}{\partial t} \\
\end{aligned}
$$
{: .notice--info}


### Charged Particle / 荷電粒子

$$
\begin{aligned}{}
& E_{n,k_z} = \hbar\omega_c\left(n+\frac{1}{2}\right) + \frac{\hbar^2 k_z^2}{2m}, \quad \omega_c=\frac{|q|B}{m} \\
& \psi = \psi_0 \exp\left(\frac{i}{\hbar}q\int_C \mathbf{A}\cdot d\mathbf{l}\right),\quad \Delta\varphi = \frac{q}{\hbar}\int_S \mathbf{B}\cdot d\mathbf{S}
\end{aligned}
$$
{: .notice--info}


## Approximation Method / 近似法

### Variational Method / 変分法

$$
\begin{aligned}{}
& E_0 \leq \frac{\langle \psi | \hat{H} | \psi \rangle}{\langle \psi | \psi \rangle}
\end{aligned}
$$
{: .notice--info}

### WKB Approximation / WKB近似

$$
\begin{aligned}{}
& \psi(x) \approx \frac{1}{\sqrt{p(x)}} \left(
C_1 e^{\frac{i}{\hbar}\int^x p(x')\,dx'}
+ C_2 e^{-\frac{i}{\hbar}\int^x p(x')\,dx'}
\right) \\
& \psi(x) \approx \frac{1}{\sqrt{\kappa(x)}} \left(
C_1 e^{\frac{1}{\hbar}\int^x \kappa(x')\,dx'}
+ C_2 e^{-\frac{1}{\hbar}\int^x \kappa(x')\,dx'}
\right)
\end{aligned}
$$
{: .notice--info}

### Bound State and Tunneling / 束縛状態とトンネル効果

$$
\begin{aligned}{}
& \int_{x_1}^{x_2} p(x)\,dx = \left(n+\frac{1}{2}\right)\pi\hbar \\
& T = \exp\left(-\frac{2}{\hbar}\int_{x_1}^{x_2} \kappa(x)\,dx\right)
\end{aligned}
$$
{: .notice--info}


## Perturbation Theory / 摂動論

### Non-Degenerate Perturbation Theory / 非縮退定常摂動論

$$
\begin{aligned}{}
& E_n^{(1)} = \langle \psi_n^{(0)} | \hat{V} | \psi_n^{(0)} \rangle \\
& |\psi_n^{(1)}\rangle = \sum_{m \neq n} \frac{|\psi_m^{(0)}\rangle \langle \psi_m^{(0)} | \hat{V} | \psi_n^{(0)} \rangle}{E_n^{(0)} - E_m^{(0)}} \\
& E_n^{(2)} = \sum_{m \neq n} \frac{|\langle \psi_m^{(0)} | \hat{V} | \psi_n^{(0)} \rangle|^2}{E_n^{(0)} - E_m^{(0)}}
\end{aligned}
$$
{: .notice--info}

### Degenerate Perturbation Theory / 縮退定常摂動論

$$
\begin{aligned}{}
& E_{n,\alpha}^{(1)} : \sum_j \langle \psi_{n,i}^{(0)} | \hat{V} | \psi_{n,j}^{(0)} \rangle C_{n,\alpha}^j = E_{n,\alpha}^{(1)} C_{n,\alpha}^i \\
& |\psi_{n,\alpha}^{(1)}\rangle = \sum_{m \neq n, \beta} \frac{|\psi_{m,\beta}^{(0)}\rangle \langle \psi_{m,\beta}^{(0)} | \hat{V} | \psi_{n,\alpha}^{(0)} \rangle}{E_n^{(0)} - E_m^{(0)}} \\
& E_{n,\alpha}^{(2)} = \sum_{m \neq n, \beta} \frac{|\langle \psi_{m,\beta}^{(0)} | \hat{V} | \psi_{n,\alpha}^{(0)} \rangle|^2}{E_n^{(0)} - E_m^{(0)}}
\end{aligned}
$$
{: .notice--info}

### Time-Dependent Perturbation Theory / 時間依存摂動論

$$
\begin{aligned}{}
& i\hbar \frac{\partial C_n(t)}{\partial t} = \sum_m \langle \psi_n^{(0)} | \hat{V}(t) | \psi_m^{(0)} \rangle e^{\frac{i}{\hbar}(E_n - E_m)t} C_m(t) \\
& C_n^{(1)}(t) = -\frac{i}{\hbar} \int_0^t \langle \psi_n^{(0)} | \hat{V}(t') | \psi_i^{(0)} \rangle e^{\frac{i}{\hbar}(E_n - E_i)t'} \, dt' \\
& \hat{V}(t) = \hat{V} e^{\eta t}, \; \eta \to 0 : \quad C_n^{(1)}(0) = \frac{\langle \psi_n^{(0)} | \hat{V} | \psi_i^{(0)} \rangle}{E_i - E_n} \\
& \hat{V}(t) = \hat{V} e^{-i\omega t}, \; t \ge 0 : \quad C_n^{(1)}(t) = \frac{\langle \psi_n^{(0)} | \hat{V} | \psi_i^{(0)} \rangle}{E_n - E_i - \hbar\omega} \left[ 1 - e^{\frac{i}{\hbar}(E_n - E_i - \hbar\omega)t} \right]
\end{aligned}
$$
{: .notice--info}


## Scattering Theory / 散乱理論

### Lippmann-Schwinger Equation / Lippmann-Schwinger方程式

$$
\begin{aligned}{}
& |\psi^{(+)}\rangle
= |\psi^{(0)}\rangle
+ \frac{1}{E-\hat{H}_0+i\epsilon}\hat{V}|\psi^{(+)}\rangle \\
& \psi^{(+)}(\mathbf{r})
= e^{i\mathbf{k}\cdot\mathbf{r}}
-\frac{m}{2\pi\hbar^2}
\int V(\mathbf{r}')
\psi^{(+)}(\mathbf{r}')
\frac{e^{ik|\mathbf{r}-\mathbf{r}'|}}
{|\mathbf{r}-\mathbf{r}'|}
\,d^3r'
\end{aligned}
$$
{: .notice--info}

### Scattering Amplitude / 散乱振幅

$$
\begin{aligned}{}
& r\to\infty,\quad V(\mathbf{r})\to 0 \\
& f(\mathbf{k}_f \leftarrow \mathbf{k}_i)
= -\frac{m}{2\pi\hbar^2}
\int V(\mathbf{r})
\psi_{\mathbf{k}_i}^{(+)}(\mathbf{r})
e^{-i\mathbf{k}_f\cdot\mathbf{r}}
\,d^3r \\
& \psi^{(+)}(\mathbf{r})
= e^{i\mathbf{k}\cdot\mathbf{r}}
+ f(\theta,\phi)\frac{e^{ikr}}{r} \\
& \frac{d\sigma}{d\Omega}
= |f(\theta,\phi)|^2
\end{aligned}
$$
{: .notice--info}

### Born Approximation / Born近似

$$
\begin{aligned}{}
& \psi_{\mathbf{k}_i}^{(+)}(\mathbf{r})
\approx e^{i\mathbf{k}_i\cdot\mathbf{r}},
\quad
\mathbf{q}=\mathbf{k}_f-\mathbf{k}_i \\
& f(\mathbf{q})
= -\frac{m}{2\pi\hbar^2}
\int V(\mathbf{r})
e^{-i\mathbf{q}\cdot\mathbf{r}}
\,d^3r
\end{aligned}
$$
{: .notice--info}

### Partial Wave Expansion / 部分波展開

$$
\begin{aligned}{}
& V(\mathbf{r}) = V(r) \\
& f(\theta)
= \frac{1}{2ik}
\sum_{\ell=0}^{\infty}
(2\ell+1)
\left(e^{2i\delta_\ell}-1\right)
P_\ell(\cos\theta) \\
& \sigma_{\mathrm{tot}}
= \frac{4\pi}{k}\operatorname{Im} f(0)
\end{aligned}
$$
{: .notice--info}


## Path Integral / 経路積分

### Configuration Space / 座標空間

$$
\begin{aligned}{}
& U(x_f, t_f; x_i, t_i) = \int \mathcal{D}[x] e^{\frac{i}{\hbar}S[x]} \\
& \int \mathcal{D}[x] = \lim_{N \to \infty} \left( \frac{m}{2\pi i \hbar \Delta t} \right)^{\frac{N}{2}} \prod_{j=1}^{N-1} dx_j \\
& S[x] = \sum_{j=1}^{N} \left[ \frac{m}{2} \left( \frac{x_j - x_{j-1}}{\Delta t} \right)^2 - V(x_j) \right] \Delta t
\end{aligned}
$$
{: .notice--info}

### Phase Space / 位相空間

$$
\begin{aligned}{}
& U(x_f, t_f; x_i, t_i) = \int \mathcal{D}[x]\mathcal{D}[p] e^{\frac{i}{\hbar}S[x,p]} \\
& \int \mathcal{D}[x]\mathcal{D}[p] = \lim_{N \to \infty} \left( \frac{1}{2\pi \hbar} \right)^N \prod_{j=1}^{N-1} dx_j \prod_{k=1}^N dp_k \\
& S[x,p] = \sum_{j=1}^{N} \left[ p_j \left( \frac{x_j - x_{j-1}}{\Delta t} \right) - H(x_j, p_j) \right] \Delta t
\end{aligned}
$$
{: .notice--info}

### Free Particle / 自由粒子

$$
\begin{aligned}{}
& S_{cl} = \frac{m(x_f - x_i)^2}{2T} \\
& U(x_f, T; x_i, 0) = \sqrt{\frac{m}{2\pi i \hbar T}} \exp\left( \frac{i m (x_f - x_i)^2}{2 \hbar T} \right)
\end{aligned}
$$
{: .notice--info}

### Harmonic Oscillator / 調和振動子

$$
\begin{aligned}{}
& S_{cl} = \frac{m\omega}{2\sin(\omega T)} \left[ (x_i^2 + x_f^2)\cos(\omega T) - 2x_i x_f \right] \\
& U(x_f, T; x_i, 0) = \sqrt{\frac{m\omega}{2\pi i \hbar \sin(\omega T)}} \exp\left( \frac{i m \omega}{2\hbar \sin(\omega T)} \left[ (x_i^2 + x_f^2)\cos(\omega T) - 2x_i x_f \right] \right)
\end{aligned}
$$
{: .notice--info}


## Identical Particle / 同種粒子

### Exchange Operator / 交換演算子

$$
\begin{aligned}{}
& \hat{P}_{ij} (\dots |w_i\rangle \dots |w_j\rangle \dots) = (\dots |w_j\rangle \dots |w_i\rangle \dots) \\
& \begin{aligned}{}
  & \text{Boson:} && \hat{P}_{ij} |\psi\rangle = |\psi\rangle \\
  & \text{Fermion:} && \hat{P}_{ij} |\psi\rangle = -|\psi\rangle \\
  & && w_i = w_j \rightarrow |\psi\rangle = 0
  \end{aligned}
\end{aligned}
$$
{: .notice--info}

### First Quantization / 第一量子化

$$
\begin{aligned}{}
& \text{Boson:}   && |w_1 \le w_2 \le \dots \le w_N\rangle = \frac{1}{\sqrt{N! \prod_\alpha n_\alpha!}} \sum_{\sigma \in S_N} |w_{\sigma(1)}\rangle |w_{\sigma(2)}\rangle \dots |w_{\sigma(N)}\rangle \\
& \text{Fermion:} && |w_1 < w_2 < \dots < w_N\rangle = \frac{1}{\sqrt{N!}} \sum_{\sigma \in S_N} \text{sgn}(\sigma) |w_{\sigma(1)}\rangle |w_{\sigma(2)}\rangle \dots |w_{\sigma(N)}\rangle
\end{aligned}
$$
{: .notice--info}

### Creation & Annihilation Operator / 生成・消滅演算子

$$
\begin{aligned}{}
& \text{Boson:}   && a_\alpha^\dagger |\dots, n_\alpha, \dots\rangle = \sqrt{n_\alpha + 1} |\dots, n_\alpha + 1, \dots\rangle \\
&                 && a_\alpha |\dots, n_\alpha, \dots\rangle = \sqrt{n_\alpha} |\dots, n_\alpha - 1, \dots\rangle \\
&                 && [a_\alpha, a_\beta^\dagger] = \delta_{\alpha\beta} \quad [a_\alpha^\dagger, a_\beta^\dagger] = 0 \\
& \text{Fermion:} && a_\alpha^\dagger |\dots, n_\alpha, \dots\rangle = (-1)^{\sum_{\beta < \alpha} n_\beta} (1 - n_\alpha) |\dots, 1, \dots\rangle \\
&                 && a_\alpha |\dots, n_\alpha, \dots\rangle = (-1)^{\sum_{\beta < \alpha} n_\beta} n_\alpha |\dots, 0, \dots\rangle \\
&                 && \{a_\alpha, a_\beta^\dagger\} = \delta_{\alpha\beta} \quad \{a_\alpha^\dagger, a_\beta^\dagger\} = 0 \\
&                 && (a_\alpha^\dagger)^2 = 0
\end{aligned}
$$
{: .notice--info}

### Second Quantization / 第二量子化

$$
\begin{aligned}{}
& \text{Boson:}   && |n_1, n_2, \dots, n_N\rangle = \prod_\alpha \frac{1}{\sqrt{n_\alpha!}} (a_1^\dagger)^{n_1} (a_2^\dagger)^{n_2} \dots (a_N^\dagger)^{n_N} |0\rangle \\
& \text{Fermion:} && |n_1, n_2, \dots, n_N\rangle = (a_1^\dagger)^{n_1} (a_2^\dagger)^{n_2} \dots (a_N^\dagger)^{n_N} |0\rangle
\end{aligned}
$$
{: .notice--info}


## Dirac Equation / Dirac方程式

### Relativistic Wave Equation / 相対論的波動方程式

$$
\begin{aligned}{}
& \hat{H}^2 = \hat{p}^{\,2}c^2 + m^2c^4 \\
& \left(\frac{1}{c^2}\frac{\partial^2}{\partial t^2} - \nabla^2 + \frac{m^2c^2}{\hbar^2}\right)\psi = 0 \\
& \hat{H} = c\boldsymbol{\alpha}\cdot\hat{\mathbf{p}} + \beta mc^2 \\
& \left(i\hbar\gamma^\mu\partial_\mu - mc\right)\psi = 0
\end{aligned}
$$
{: .notice--info}

### Dirac Representation / Dirac表示

$$
\begin{aligned}{}
& \{\gamma^\mu,\gamma^\nu\} = 2g^{\mu\nu}\mathbb{I}, \quad \gamma^0 =
\begin{pmatrix}
\mathbb{I} & 0 \\
0 & -\mathbb{I}
\end{pmatrix}
,\quad
\gamma^i =
\begin{pmatrix}
0 & \sigma^i \\
-\sigma^i & 0
\end{pmatrix} \\
& \sigma_x =
\begin{pmatrix}
0 & 1 \\
1 & 0
\end{pmatrix}
,\quad
\sigma_y =
\begin{pmatrix}
0 & -i \\
i & 0
\end{pmatrix}
,\quad
\sigma_z =
\begin{pmatrix}
1 & 0 \\
0 & -1
\end{pmatrix}
\end{aligned}
$$
{: .notice--info}

### Plane Wave Solution / 平面波解

$$
\begin{aligned}{}
& \psi(x) = u(p)e^{-\frac{i}{\hbar}p_\mu x^\mu},
&& \psi(x) = v(p)e^{\frac{i}{\hbar}p_\mu x^\mu} \\
& u(p) =
\begin{pmatrix}
\chi^s \\
\frac{c\boldsymbol{\sigma}\cdot\mathbf{p}}{E+mc^2}\chi^s
\end{pmatrix},
&& v(p) =
\begin{pmatrix}
\frac{c\boldsymbol{\sigma}\cdot\mathbf{p}}{E+mc^2}\eta^s \\
\eta^s
\end{pmatrix} \\
& E = \sqrt{p^2c^2 + m^2c^4},
&& -E = -\sqrt{p^2c^2 + m^2c^4}
\end{aligned}
$$
{: .notice--info}

### Non-Relativistic Limit / 非相対論的極限

$$
\begin{aligned}{}
& \psi = e^{-\frac{i}{\hbar}mc^2t}
\begin{pmatrix}
\varphi \\
\chi
\end{pmatrix} \\
& \chi \approx
\frac{\boldsymbol{\sigma}\cdot(\hat{\mathbf{p}}-q\mathbf{A})}{2mc}\varphi \\
& i\hbar\frac{\partial\varphi}{\partial t}
=
\left[
\frac{(\hat{\mathbf{p}}-q\mathbf{A})^2}{2m}
+ q\Phi
-\frac{q\hbar}{2m}\boldsymbol{\sigma}\cdot\mathbf{B}
\right]\varphi
\end{aligned}
$$
{: .notice--info}

### Conserved Current / 保存カレント

$$
\begin{aligned}{}
& j^\mu = c\psi^\dagger\gamma^0\gamma^\mu\psi \\
& \partial_\mu j^\mu = 0
\end{aligned}
$$
{: .notice--info}
