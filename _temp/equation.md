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
& \hat{H}|\psi(t)\rangle = i\hbar \frac{\partial}{\partial t} |\psi(t)\rangle 
\end{aligned}
$$
{: .notice--info}


## Formalism / 形式論

### State / 状態

$$
\begin{aligned}
& \langle m | n \rangle = \delta_{mn} && \langle a | a' \rangle = \delta(a - a') \\
& \sum_n |n\rangle\langle n| = \mathbb I && \int |a\rangle\langle a| \, da = \mathbb I \\
& |\psi\rangle = \sum_n |n\rangle\langle n|\psi\rangle && |\psi\rangle = \int |a\rangle\langle a|\psi\rangle \, da
\end{aligned}
$$
{: .notice--info}

### Observable / 物理量

$$
\begin{aligned}
& \hat{A}|a\rangle = a|a\rangle && \langle a | a \rangle = \mathbb I \\
& a = a^* && \langle a_n | a_m \rangle = \delta_{nm} \\
& \hat{A} = \sum_a a |a\rangle\langle a| && \hat{A} = \int a |a\rangle\langle a| \, da
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
& |\psi(t)\rangle = \hat U(t)\,|\psi(0)\rangle \quad \hat U^\dagger(t)\,\hat U(t) = \mathbb I \\
& \hat U(t) = \exp\left[-\frac{i}{\hbar}\hat H t\right] \\
& \hat U(t) = \mathcal T \exp\left[-\frac{i}{\hbar}\int_{0}^{t}\hat H(t')\,dt'\right]
\end{aligned}
$$
{: .notice--info}


## Wave Mechanics / 波動力学

### Wave Function / 波動関数

$$
\begin{aligned}
& \langle x | \psi \rangle = \psi(x) \\
& \langle \phi | \psi \rangle = \int_{-\infty}^{\infty} \phi^*(x) \psi(x) dx \\
& \langle x | \hat{x} | \psi \rangle = x \psi(x) \\
& \langle x | \hat{p} | \psi \rangle = -i\hbar \frac{\partial}{\partial x} \psi(x)
\end{aligned}
$$
{: .notice--info}

### Change of Basis / 基底変換

$$
\begin{aligned}
& \langle x | x' \rangle = \delta(x - x') && \langle p | p' \rangle = \delta(p - p') \\
& \langle x | p \rangle = \frac{1}{\sqrt{2\pi\hbar}} e^{\frac{i}{\hbar}px} && \langle p | x \rangle = \frac{1}{\sqrt{2\pi\hbar}} e^{-\frac{i}{\hbar}px} \\
& \phi(p) = \frac{1}{\sqrt{2\pi\hbar}} \int_{-\infty}^{\infty} \psi(x) e^{-\frac{i}{\hbar}px} dx && \psi(x) = \frac{1}{\sqrt{2\pi\hbar}} \int_{-\infty}^{\infty} \phi(p) e^{\frac{i}{\hbar}px} dp
\end{aligned}
$$
{: .notice--info}

### Schrödinger Equation / Schrödinger方程式

$$
\begin{aligned}
& -\frac{\hbar^2}{2m} \frac{\partial^2\Psi(x,t)}{\partial x^2} + V(x)\Psi(x,t) = i\hbar \frac{\partial\Psi(x,t)}{\partial t} \\
& -\frac{\hbar^2}{2m} \frac{d^2\psi(x)}{dx^2} + V(x)\psi(x) = E\psi(x)
\end{aligned}
$$
{: .notice--info}

### Probability Current / 確率流

$$
\begin{aligned}
& \frac{\partial |\Psi|^2}{\partial t} = -\nabla \cdot \mathbf{j} \\
& \mathbf{j} = \frac{i\hbar}{2m} (\Psi \nabla \Psi^* - \Psi^* \nabla \Psi)
\end{aligned}
$$
{: .notice--info}

### Ehrenfest's Theorem / Ehrenfestの定理

$$
\begin{aligned}
& \frac{d}{dt} \langle \hat{A} \rangle = -\frac{i}{\hbar} \langle [\hat{A}, \hat{H}] \rangle \\
& \frac{d}{dt} \langle \hat{x} \rangle = \left\langle \frac{\partial \hat{H}}{\partial \hat{p}} \right\rangle \\
& \frac{d}{dt} \langle \hat{p} \rangle = \left\langle -\frac{\partial \hat{H}}{\partial \hat{x}} \right\rangle
\end{aligned}
$$
{: .notice--info}

### Uncertainty Principle / 不確定性原理

$$
\begin{aligned}
& \Delta A \Delta B \geq \frac{1}{2} |\langle [A, B] \rangle| \\
& [\hat{x}, \hat{p}] = i\hbar \quad \Delta x \Delta p \geq \frac{\hbar}{2}
\end{aligned}
$$
{: .notice--info}


## 1D System / １次元系

### Free Particle / 自由粒子

$$
\begin{aligned}
& V(x) = 0 \\
& \psi(x) = A e^{ikx} + B e^{-ikx} \\
& k = \frac{\sqrt{2mE}}{\hbar}
\end{aligned}
$$
{: .notice--info}

### Step Potential / 段差ポテンシャル

$$
\begin{aligned}
& V(x) = \begin{cases} 0, & x < 0 \\ V_0, & x \geq 0 \end{cases} \\
& \psi(x) = \begin{cases} A e^{ik_1 x} + B e^{-ik_1 x}, & x < 0 \\ C e^{ik_2 x}, & x \geq 0 \end{cases} \\
& k_1 = \frac{\sqrt{2mE}}{\hbar}, \quad k_2 = \frac{\sqrt{2m(E-V_0)}}{\hbar} \\
& R = \left| \frac{B}{A} \right|^2 = \left( \frac{k_1 - k_2}{k_1 + k_2} \right)^2 \\
& T = \frac{k_2}{k_1} \left| \frac{C}{A} \right|^2 = \frac{4k_1 k_2}{(k_1 + k_2)^2}
\end{aligned}
$$
{: .notice--info}

### Potential Barrier / ポテンシャル障壁

$$
\begin{aligned}
& V(x) = \begin{cases} V_0, & |x| \leq \frac{a}{2} \\ 0, & |x| > \frac{a}{2} \end{cases} \\
& \psi(x) = \begin{cases} A e^{ikx} + B e^{-ikx}, & x < -\frac{a}{2} \\ C e^{\kappa x} + D e^{-\kappa x}, & -\frac{a}{2} \leq x \leq \frac{a}{2} \\ F e^{ikx}, & x > \frac{a}{2} \end{cases} \\
& k = \frac{\sqrt{2mE}}{\hbar}, \quad \kappa = \frac{\sqrt{2m(V_0-E)}}{\hbar} \\
& R = \left| \frac{B}{A} \right|^2 = \left[ 1 + \frac{4E(V_0-E)}{V_0^2 \sinh^2(\kappa a)} \right]^{-1} \\
& T = \left| \frac{F}{A} \right|^2 = \left[ 1 + \frac{V_0^2 \sinh^2(\kappa a)}{4E(V_0-E)} \right]^{-1}
\end{aligned}
$$
{: .notice--info}

### Square Well / 井戸型ポテンシャル

$$
\begin{aligned}
& V(x) = \begin{cases} 0, & |x| < \frac{L}{2} \\ \infty, & |x| \geq \frac{L}{2} \end{cases} \\
& \psi_n(x) = \begin{cases} \sqrt{\frac{2}{L}} \cos\left(\frac{n\pi x}{L}\right), & n=1,3,5,\dots \\ \sqrt{\frac{2}{L}} \sin\left(\frac{n\pi x}{L}\right), & n=2,4,6,\dots \end{cases} \\
& E_n = \frac{\hbar^2 \pi^2 n^2}{2mL^2}
\end{aligned}
$$
{: .notice--info}

### Harmonic Oscillator / 調和振動子

$$
\begin{aligned}
& V(x) = \frac{1}{2} m \omega^2 x^2 \\
& \psi_n(x) = \frac{1}{\sqrt{2^n n!}} \left( \frac{m\omega}{\pi\hbar} \right)^{1/4} H_n \left( \sqrt{\frac{m\omega}{\hbar}} x \right) \exp\left( -\frac{m\omega x^2}{2\hbar} \right) \\
& E_n = \hbar \omega \left( n + \frac{1}{2} \right), \quad n = 0, 1, 2, \dots
\end{aligned}
$$
{: .notice--info}

### Ladder Operator / 昇降演算子

$$
\begin{aligned}
& \hat{a} = \sqrt{\frac{m\omega}{2\hbar}} \hat{x} + \frac{i}{\sqrt{2m\hbar\omega}} \hat{p} && \hat{a}^\dagger = \sqrt{\frac{m\omega}{2\hbar}} \hat{x} - \frac{i}{\sqrt{2m\hbar\omega}} \hat{p} \\
& \hat{a}|n\rangle = \sqrt{n}|n-1\rangle && \hat{a}^\dagger|n\rangle = \sqrt{n+1}|n+1\rangle \\
& \hat{H}|n\rangle = \hbar\omega\left( n + \frac{1}{2} \right)|n\rangle
\end{aligned}
$$
{: .notice--info}


## Symmetry / 対称性

### Spatial Translational Invariance / 空間並進不変性

$$
\begin{aligned}
& \hat{\mathbf{p}} = -i\hbar\nabla \\
& \hat{U}_\mathbf{a}|\mathbf{r}\rangle = |\mathbf{r}+\mathbf{a}\rangle \to \hat{U}_\mathbf{a} = e^{-\frac{i}{\hbar}\hat{\mathbf{p}}\cdot\mathbf{a}} \\
& \langle\psi_\mathbf{a}|\hat{H}|\psi_\mathbf{a}\rangle = \langle\psi|\hat{H}|\psi\rangle \to \frac{d}{dt}\langle\hat{\mathbf{p}}\rangle = 0
\end{aligned}
$$
{: .notice--info}

### Rotational Invariance / 回転不変性

$$
\begin{aligned}
& \hat{\mathbf{L}} = -i\hbar \mathbf{r} \times \nabla \\
& \hat{U}_\theta|\mathbf{r}\rangle = |R_\theta\mathbf{r}\rangle \to \hat{U}_\theta = e^{-\frac{i}{\hbar}\hat{\mathbf{L}}\cdot\boldsymbol{\theta}} \\
& \langle\psi_{\boldsymbol{\theta}}|\hat{H}|\psi_{\boldsymbol{\theta}}\rangle = \langle\psi|\hat{H}|\psi\rangle \to \frac{d}{dt}\langle\hat{\mathbf{L}}\rangle = 0
\end{aligned}
$$
{: .notice--info}

### Time Translational Invariance / 時間並進不変性

$$
\begin{aligned}
& \hat{H} = -\frac{\hbar^2}{2m}\nabla^2 + V(\mathbf{r}, t) \\
& \hat{U}_\tau|\psi(t)\rangle = |\psi(t+\tau)\rangle \rightarrow \hat{U}_\tau = e^{-\frac{i}{\hbar}\hat{H}\tau} \\
& \langle\psi_{\tau}|\hat{H}|\psi_{\tau}\rangle = \langle\psi|\hat{H}|\psi\rangle \to \frac{d}{dt}\langle\hat{H}\rangle = 0
\end{aligned}
$$
{: .notice--info}


## Angular Momentum / 角運動量

### Angular Momentum Operator / 角運動量演算子

$$
\begin{aligned}
& [\hat{J}_i, \hat{J}_j] = i\hbar \epsilon_{ijk} \hat{J}_k \quad [\hat{\mathbf{J}}^2, \hat{J}_i] = 0 \\
& \hat{J}_+ = \hat{J}_x + i\hat{J}_y \quad \hat{J}_- = \hat{J}_x - i\hat{J}_y \\
& \hat{J}_{\pm}|j,m\rangle = \hbar\sqrt{(j \mp m)(j \pm m + 1)} |j, m \pm 1\rangle \\
& \hat{\mathbf{J}}^2|j,m\rangle = \hbar^2 j(j+1)|j,m\rangle, \quad j=0, \frac{1}{2}, 1, \dots \\
& \hat{J}_z|j,m\rangle = \hbar m|j,m\rangle, \quad m=-j, -j+1, \dots, j
\end{aligned}
$$
{: .notice--info}

### Orbital Angular Momentum / 軌道角運動量

$$
\begin{aligned}
& \hat{\mathbf{L}}^2 = -\hbar^2 \left[\frac{1}{\sin\theta}\frac{\partial}{\partial\theta}\left(\sin\theta\frac{\partial}{\partial\theta}\right) + \frac{1}{\sin^2\theta}\frac{\partial^2}{\partial\phi^2}\right] \\
& \hat{L}_z = -i\hbar\frac{\partial}{\partial\phi} \\
& \hat{\mathbf{L}}^2|l,m\rangle = \hbar^2 l(l+1)|l,m\rangle, \quad l=0, 1, 2, \dots \\
& \hat{L}_z|l,m\rangle = \hbar m|l,m\rangle, \quad m=-l, -l+1, \dots, l \\
& Y_l^m = (-1)^m \sqrt{\frac{(2l+1)}{4\pi}\frac{(l-m)!}{(l+m)!}} P_l^m(\cos\theta) e^{im\phi}
\end{aligned}
$$
{: .notice--info}

### Spin Angular Momentum / スピン角運動量

$$
\begin{aligned}
& \hat{S}_x = \frac{\hbar}{2} \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \quad \hat{S}_y = \frac{\hbar}{2} \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} \quad \hat{S}_z = \frac{\hbar}{2} \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \\
& \hat{\mathbf{S}}^2|s,m\rangle = \hbar^2 s(s+1)|s,m\rangle, \quad s=\frac{1}{2} \\
& \hat{S}_z|s,m\rangle = \hbar m|s,m\rangle, \quad m=-\frac{1}{2}, \frac{1}{2} \\
& \hat{H} = -\gamma \hat{\mathbf{S}} \cdot \mathbf{B} \quad \omega_L = \gamma B
\end{aligned}
$$
{: .notice--info}

### Addition of Angular Momentum / 角運動量の合成

$$
\begin{aligned}
& \hat{\mathbf{J}} = \hat{\mathbf{J}}_1 + \hat{\mathbf{J}}_2 \\
& \hat{\mathbf{J}}^2|j,m\rangle = \hbar^2 j(j+1)|j,m\rangle, \quad j=|j_1-j_2|, |j_1-j_2|+1, \dots, j_1+j_2 \\
& \hat{J}_z|j,m\rangle = \hbar m|j,m\rangle, \quad m=-j, -j+1, \dots, j \\
& C_{j_1m_1j_2m_2}^{jm} \neq 0 \to m = m_1 + m_2 \\
& \sum_{m_1,m_2} C_{j_1m_1j_2m_2}^{jm} C_{j_1m_1j_2m_2}^{j'm'} = \delta_{jj'}\delta_{mm'}
\end{aligned}
$$
{: .notice--info}


## 3D System / 3次元系

### Radial Equation / 動径方程式

$$
\begin{aligned}
& \psi(r,\theta,\phi) = R(r)Y_l^m(\theta,\phi) \\
& u(r) = rR(r) \\
& -\frac{\hbar^2}{2m}\frac{d^2u}{dr^2} + \left[V(r) + \frac{\hbar^2 l(l+1)}{2mr^2}\right]u = Eu
\end{aligned}
$$
{: .notice--info}

### Free Particle / 自由粒子

$$
\begin{aligned}
& V(r) = 0 \\
& \psi_{klm}(r, \theta, \phi) = \sqrt{\frac{2k^2}{\pi}} j_l(kr) Y_{l}^{m}(\theta, \phi) \\
& E = \frac{\hbar^2 k^2}{2m}
\end{aligned}
$$
{: .notice--info}

### Isotropic Harmonic Oscillator / 等方性調和振動子

$$
\begin{aligned}
& V(r) = \frac{1}{2} m \omega^2 r^2 \\
& E_n = \hbar \omega \left( n + \frac{3}{2} \right), \quad n = 0, 1, 2, \dots \\
& d(n) = \frac{1}{2}(n+1)(n+2)
\end{aligned}
$$
{: .notice--info}

### Hydrogen Atom / 水素原子

$$
\begin{aligned}
& V(r) = -\frac{e^2}{4\pi\epsilon_0 r} \\
& a_0 = \frac{4\pi\epsilon_0\hbar^2}{me^2} \quad \rho = \frac{r}{na_0} \\
& \psi_{nlm}(r,\theta,\phi) = \sqrt{\left(\frac{2}{na_0}\right)^3 \frac{(n-l-1)!}{2n(n+l)!}} e^{-\rho} (2\rho)^l L_{n-l-1}^{2l+1}(2\rho) Y_l^m(\theta,\phi) \\
& E_n = -\frac{me^4}{32\pi^2\epsilon_0^2\hbar^2}\frac{1}{n^2}, \quad n=1,2,3,\dots \\
& L^2 = \hbar^2 l(l+1), \quad l=0,1,\dots,n-1 \\
& L_z = \hbar m, \quad m=-l,-l+1,\dots,l
\end{aligned}
$$
{: .notice--info}

### Electromagnetic Field / 電磁場

$$
\begin{aligned}
& \hat{H} = \frac{1}{2m}(\hat{\mathbf{p}} - q\mathbf{A})^2 + q\phi \\
& \mathbf{A}' = \mathbf{A} + \nabla\chi, \quad \phi' = \phi - \frac{\partial\chi}{\partial t}, \quad \psi' = e^{\frac{i}{\hbar}q\chi}\psi \\
& \hat{H}\psi = i\hbar\frac{\partial\psi}{\partial t} \to \hat{H}'\psi' = i\hbar\frac{\partial\psi'}{\partial t}
\end{aligned}
$$
{: .notice--info}

### Charged Particle / 荷電粒子

$$
\begin{aligned}
& E_{n,k_z} = \hbar\omega_c\left(n+\frac{1}{2}\right) + \frac{\hbar^2 k_z^2}{2m}, \quad n=0,1,2,\dots \\
& \omega_c = \frac{|q|B}{m} \\
& \psi = \psi_0 \exp\left(\frac{i}{\hbar}q\int_C \mathbf{A}\cdot d\mathbf{l}\right) \\
& \Delta\varphi = \frac{q}{\hbar}\oint_S \mathbf{B}\cdot d\mathbf{S}
\end{aligned}
$$
{: .notice--info}


## Approximation Method / 近似法


## Perturbation Theory / 摂動論

### Non-Degenerate Perturbation Theory / 非縮退定常摂動論

$$
\begin{aligned}
& E_n^{(1)} = \langle \psi_n^{(0)} | \hat{V} | \psi_n^{(0)} \rangle \\
& |\psi_n^{(1)}\rangle = \sum_{m \neq n} \frac{|\psi_m^{(0)}\rangle \langle \psi_m^{(0)} | \hat{V} | \psi_n^{(0)} \rangle}{E_n^{(0)} - E_m^{(0)}} \\
& E_n^{(2)} = \sum_{m \neq n} \frac{|\langle \psi_m^{(0)} | \hat{V} | \psi_n^{(0)} \rangle|^2}{E_n^{(0)} - E_m^{(0)}}
\end{aligned}
$$
{: .notice--info}

### Degenerate Perturbation Theory / 縮退定常摂動論

$$
\begin{aligned}
& E_{n,\alpha}^{(1)} : \sum_j \langle \psi_{n,i}^{(0)} | \hat{V} | \psi_{n,j}^{(0)} \rangle C_{n,\alpha}^j = E_{n,\alpha}^{(1)} C_{n,\alpha}^i \\
& |\psi_{n,\alpha}^{(1)}\rangle = \sum_{m \neq n, \beta} \frac{|\psi_{m,\beta}^{(0)}\rangle \langle \psi_{m,\beta}^{(0)} | \hat{V} | \psi_{n,\alpha}^{(0)} \rangle}{E_n^{(0)} - E_m^{(0)}} \\
& E_{n,\alpha}^{(2)} = \sum_{m \neq n, \beta} \frac{|\langle \psi_{m,\beta}^{(0)} | \hat{V} | \psi_{n,\alpha}^{(0)} \rangle|^2}{E_n^{(0)} - E_m^{(0)}}
\end{aligned}
$$
{: .notice--info}

### Time-Dependent Perturbation Theory / 時間依存摂動論

$$
\begin{aligned}
& i\hbar \frac{\partial C_n(t)}{\partial t} = \sum_m \langle \psi_n^{(0)} | \hat{V}(t) | \psi_m^{(0)} \rangle e^{\frac{i}{\hbar}(E_n - E_m)t} C_m(t) \\
& C_n^{(1)}(t) = -\frac{i}{\hbar} \int_0^t \langle \psi_n^{(0)} | \hat{V}(t') | \psi_i^{(0)} \rangle e^{\frac{i}{\hbar}(E_n - E_i)t'} \, dt' \\
& \hat{V}(t) = \hat{V} e^{\eta t}, \; \eta \to 0 : \quad C_n^{(1)}(0) = \frac{\langle \psi_n^{(0)} | \hat{V} | \psi_i^{(0)} \rangle}{E_i - E_n} \\
& \hat{V}(t) = \hat{V} e^{-i\omega t}, \; t \ge 0 : \quad C_n^{(1)}(t) = \frac{\langle \psi_n^{(0)} | \hat{V} | \psi_i^{(0)} \rangle}{E_n - E_i - \hbar\omega} \left[ 1 - e^{\frac{i}{\hbar}(E_n - E_i - \hbar\omega)t} \right]
\end{aligned}
$$
{: .notice--info}


## Scattering Theory / 散乱理論


## Path Integral / 経路積分

### Configuration Space / 座標空間

$$
\begin{aligned}
& U(x_f, t_f; x_i, t_i) = \int \mathcal{D}[x] e^{\frac{i}{\hbar}S[x]} \\
& \int \mathcal{D}[x] = \lim_{N \to \infty} \left( \frac{m}{2\pi i \hbar \Delta t} \right)^{\frac{N}{2}} \prod_{j=1}^{N-1} dx_j \\
& S[x] = \sum_{j=1}^{N} \left[ \frac{m}{2} \left( \frac{x_j - x_{j-1}}{\Delta t} \right)^2 - V(x_j) \right] \Delta t
\end{aligned}
$$
{: .notice--info}

### Phase Space / 位相空間

$$
\begin{aligned}
& U(x_f, t_f; x_i, t_i) = \int \mathcal{D}[x]\mathcal{D}[p] e^{\frac{i}{\hbar}S[x,p]} \\
& \int \mathcal{D}[x]\mathcal{D}[p] = \lim_{N \to \infty} \left( \frac{1}{2\pi \hbar} \right)^N \prod_{j=1}^{N-1} dx_j \prod_{k=1}^N dp_k \\
& S[x,p] = \sum_{j=1}^{N} \left[ p_j \left( \frac{x_j - x_{j-1}}{\Delta t} \right) - H(x_j, p_j) \right] \Delta t
\end{aligned}
$$
{: .notice--info}

### Free Particle / 自由粒子

$$
\begin{aligned}
& S_{cl} = \frac{m(x_f - x_i)^2}{2T} \\
& U(x_f, T; x_i, 0) = \sqrt{\frac{m}{2\pi i \hbar T}} \exp\left( \frac{i m (x_f - x_i)^2}{2 \hbar T} \right)
\end{aligned}
$$
{: .notice--info}

### Harmonic Oscillator / 調和振動子

$$
\begin{aligned}
& S_{cl} = \frac{m\omega}{2\sin(\omega T)} \left[ (x_i^2 + x_f^2)\cos(\omega T) - 2x_i x_f \right] \\
& U(x_f, T; x_i, 0) = \sqrt{\frac{m\omega}{2\pi i \hbar \sin(\omega T)}} \exp\left( \frac{i m \omega}{2\hbar \sin(\omega T)} \left[ (x_i^2 + x_f^2)\cos(\omega T) - 2x_i x_f \right] \right)
\end{aligned}
$$
{: .notice--info}


## Identical Particle / 同種粒子

### Exchange Operator / 交換演算子

$$
\begin{aligned}
& \hat{P}_{ij} (\dots |w_i\rangle \dots |w_j\rangle \dots) = (\dots |w_j\rangle \dots |w_i\rangle \dots) \\
& \begin{aligned}
  & \text{Boson:} && \hat{P}_{ij} |\psi\rangle = |\psi\rangle \\
  & \text{Fermion:} && \hat{P}_{ij} |\psi\rangle = -|\psi\rangle \\
  & && w_i = w_j \rightarrow |\psi\rangle = 0
  \end{aligned}
\end{aligned}
$$
{: .notice--info}

### First Quantization / 第一量子化

$$
\begin{aligned}
& \text{Boson:}   && |w_1 \le w_2 \le \dots \le w_N\rangle = \frac{1}{\sqrt{N! \prod_\alpha n_\alpha!}} \sum_{\sigma \in S_N} |w_{\sigma(1)}\rangle |w_{\sigma(2)}\rangle \dots |w_{\sigma(N)}\rangle \\
& \text{Fermion:} && |w_1 < w_2 < \dots < w_N\rangle = \frac{1}{\sqrt{N!}} \sum_{\sigma \in S_N} \text{sgn}(\sigma) |w_{\sigma(1)}\rangle |w_{\sigma(2)}\rangle \dots |w_{\sigma(N)}\rangle
\end{aligned}
$$
{: .notice--info}

### Creation & Annihilation Operator / 生成・消滅演算子

$$
\begin{aligned}
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
\begin{aligned}
& \text{Boson:}   && |n_1, n_2, \dots, n_N\rangle = \prod_\alpha \frac{1}{\sqrt{n_\alpha!}} (a_1^\dagger)^{n_1} (a_2^\dagger)^{n_2} \dots (a_N^\dagger)^{n_N} |0\rangle \\
& \text{Fermion:} && |n_1, n_2, \dots, n_N\rangle = (a_1^\dagger)^{n_1} (a_2^\dagger)^{n_2} \dots (a_N^\dagger)^{n_N} |0\rangle
\end{aligned}
$$
{: .notice--info}


## Dirac Equation / Dirac方程式
