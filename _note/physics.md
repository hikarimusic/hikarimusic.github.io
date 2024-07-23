---
title: 'Physics 🍊⭐'
date: 2023-01-02
permalink: /note/physics
tags:
  - note
toc: true
---

Equations of fundamental physics.

{% include toc %}

# Analytical Mechanics / 解析力学

## Newtonian Mechanics / Newton力学

### Equation of Motion / 運動方程式

$$
\mathbf{F} = \frac{d}{dt}\left(m\mathbf{v}\right) \\
\mathbf{F}_{\alpha\beta} = -\mathbf{F}_{\beta\alpha}
$$
{: .notice--info}

### Momentum / 運動量

$$
\frac{d\mathbf{P}}{dt} = \mathbf{F} \\
\begin{aligned}
& \mathbf{P} = m\mathbf{v} && \mathbf{F} \\
& \mathbf{P} = M\mathbf{V} && \mathbf{F} = \sum_{\alpha}\mathbf{F}_\alpha^{(e)}
\end{aligned}
$$
{: .notice--info}

$$
\frac{d\mathbf{P}}{dt} = \mathbf{F} \\
\begin{aligned}
\mathbf{P} &= \sum_\alpha m_\alpha\left(\mathbf{V} + \mathbf{v'}_\alpha\right) \\
&= \sum_\alpha m_\alpha\mathbf{V} + \sum_\alpha m_\alpha\mathbf{v'}_\alpha \\
&= M\mathbf{V}
\end{aligned} \\
\begin{aligned}
\mathbf{F} &= \sum_\alpha\left(\mathbf{F}_\alpha^{(e)} + \sum_{\beta\neq\alpha}\mathbf{F}_{\alpha\beta}\right) \\
&= \sum_\alpha\mathbf{F}_{\alpha}^{(e)} + \sum_{\beta>\alpha}\left(\mathbf{F}_{\alpha\beta} + \mathbf{F}_{\beta\alpha}\right) \\
&= \sum_\alpha\mathbf{F}_\alpha^{(e)}
\end{aligned}
$$
{: .notice--primary}

### Angular Momentum / 角運動量

$$
\frac{d\mathbf{M}}{dt} = \mathbf{N} \\
\begin{aligned}
& \mathbf{M} = m\mathbf{r}\times\mathbf{v} && \mathbf{N} = \mathbf{r}\times\mathbf{F} \\
& \mathbf{M} = M\mathbf{R}\times\mathbf{V} + \sum_\alpha m_\alpha\mathbf{r'}_\alpha\times\mathbf{v'}_\alpha && \mathbf{N} = \sum_\alpha\mathbf{r}_\alpha\times\mathbf{F}_\alpha^{(e)}
\end{aligned}
$$
{: .notice--info}

$$
\frac{d\mathbf{M}}{dt} = m\mathbf{v}\times\mathbf{v} + m\mathbf{r}\times\mathbf{a} = \mathbf{r}\times\mathbf{F} = \mathbf{N} \\
\begin{aligned}
\mathbf{M} &= \sum_\alpha m_\alpha\left(\mathbf{R}+\mathbf{r'}_\alpha\right)\times\left(\mathbf{V}+\mathbf{v'}_\alpha\right) \\
&= \sum_\alpha m_\alpha\mathbf{R}\times\mathbf{V} + \mathbf{R}\times\left(\sum_\alpha m_\alpha\mathbf{v}'_\alpha\right) \\
&+ \left(\sum_\alpha m_\alpha\mathbf{r'}_\alpha\right)\times\mathbf{V} + \sum_\alpha m_\alpha\mathbf{r'}_\alpha\times\mathbf{v'}_\alpha \\
&= M\mathbf{R}\times\mathbf{V} + \sum_\alpha m_\alpha\mathbf{r'}_\alpha\times\mathbf{v'}_\alpha
\end{aligned} \\
\begin{aligned}
\mathbf{N} &= \sum_\alpha \mathbf{r}_\alpha\times\left(\mathbf{F}_\alpha^{(e)} + \sum_{\beta\neq\alpha}\mathbf{F_{\alpha\beta}}\right) \\
&= \sum_\alpha\mathbf{r}_\alpha\times\mathbf{F}_\alpha^{(e)} + \sum_{\beta>\alpha}\left(\mathbf{r}_\alpha\times\mathbf{F}_{\alpha\beta} + \mathbf{r}_\beta\times\mathbf{F}_{\beta\alpha}\right) \\
&= \sum_\alpha\mathbf{r}_\alpha\times\mathbf{F}_\alpha^{(e)} + \sum_{\beta>\alpha}\left(\mathbf{r}_\alpha-\mathbf{r}_\beta\right)\times\mathbf{F}_{\alpha\beta} \\
&= \sum_\alpha\mathbf{r}_\alpha\times\mathbf{F}_\alpha^{(e)}
\end{aligned}
$$
{: .notice--primary}

### Energy / エネルギー

$$
\frac{dE}{dt} = 0 \\
\begin{aligned}
E &= \frac{1}{2} mv^2 + U \\
E &= \frac{1}{2} MV^2 + \sum_\alpha \frac{1}{2} m_\alpha v_\alpha'^2 + U \\
\end{aligned}
$$
{: .notice--info}

$$
\frac{dE}{dt} = m\mathbf{v} \cdot \mathbf{a} + (\mathbf{\nabla} U) \cdot \mathbf{v} + \frac{\partial U}{\partial t} = (\mathbf{F} + \mathbf{\nabla} U) \cdot \mathbf{v} = 0 \\
\begin{aligned}
E &= \sum_\alpha \frac{1}{2} m_\alpha (\mathbf{V} + \mathbf{v}_\alpha') \cdot (\mathbf{V} + \mathbf{v}_\alpha') \\
&= \sum_\alpha \frac{1}{2} m_\alpha V^2 + \left(\sum_\alpha m_\alpha \mathbf{v}_\alpha'\right) \cdot \mathbf{V} + \sum_\alpha \frac{1}{2} m_\alpha v_\alpha'^2 \\
&= \frac{1}{2} MV^2 + \sum_\alpha \frac{1}{2} m_\alpha v_\alpha'^2
\end{aligned}
$$
{: .notice--primary}

## Lagrangian Mechanics / Lagrange力学

### Lagrange's Equation / Langrange方程式

$$
\delta S = \delta\int_{t_1}^{t_2} L dt = 0 \quad L = T - U\\
\begin{aligned}
& \frac{d}{dt} \frac{\partial{L}}{\partial{\dot{q}_i}} - \frac{\partial{L}}{\partial{q_i}} = 0 \\
& \frac{d}{dt} \frac{\partial{L}}{\partial{\dot{q}_i}} - \frac{\partial{L}}{\partial{q_i}} + \sum_j \lambda_j \frac{\partial{f_j}}{\partial{q_i}} = 0
\end{aligned}
$$
{: .notice--info}

$$
\begin{aligned}
\delta S &= \int_{t_1}^{t_2} \sum_i \left( \frac{\partial{L}}{\partial{q_i}} \delta q_i + \frac{\partial{L}}{\partial{\dot{q}_i}} \delta \dot{q}_i \right) dt \\
&= \int_{t_1}^{t_2} \sum_i \frac{\partial{L}}{\partial{q_i}} \delta q_i dt + \left[ \sum_i \frac{\partial{L}}{\partial{\dot{q}_i}} \delta q_i \right]_{t_1}^{t_2} - \int_{t_1}^{t_2} \sum_i \frac{d}{dt} \left( \frac{\partial{L}}{\partial{\dot{q_i}}} \right) \delta q_i dt \\
&= \int_{t_1}^{t_2} \sum_i \left( \frac{\partial{L}}{\partial{q_i}} - \frac{d}{dt} \frac{\partial{L}}{\partial{\dot{q}_i}} \right) \delta q_i dt \\
&= 0
\end{aligned}
$$
{: .notice--primary}

### Conservation Law / 保存則

$$
\begin{aligned}
E &= \sum_i \dot{q}_i \frac{\partial{L}}{\partial{\dot{q}_i}} - L = const. \\
\mathbf{P} &= \sum_\alpha \frac{\partial{L}}{\partial{\mathbf{v}_\alpha}} = const. \\
\mathbf{M} &= \sum_\alpha \mathbf{r}_\alpha \times \frac{\partial{L}}{\partial{\mathbf{v}_\alpha}} = const.
\end{aligned}
$$
{: .notice--info}

$$
\begin{aligned}
& \quad\; \frac{d}{dt} \left( \sum_i \dot{q}_i \frac{\partial{L}}{\partial{\dot{q}_i}} - L \right) \\
&= \sum_i \left[ \ddot{q}_i \frac{\partial{L}}{\partial{\dot{q}_i}} + \dot{q}_i \frac{d}{dt} \frac{\partial{L}}{\partial{\dot{q}_i}} - \frac{\partial{L}}{\partial{q_i}} \dot{q}_i - \frac{\partial{L}}{\partial{\dot{q}_i}} \ddot{q}_i \right] \\
&= 0 \\
\delta L &= \sum_\alpha \frac{\partial{L}}{\partial{\mathbf{r}_\alpha}} \cdot \mathbf{\epsilon} \\
&= \mathbf{\epsilon} \cdot \sum_\alpha \frac{d}{dt} \frac{\partial{L}}{\partial{\mathbf{v}_\alpha}} \\
&= 0 \\
\delta L &= \sum_\alpha \left( \frac{\partial{L}}{\partial{\mathbf{r}_\alpha}} \cdot \mathbf{\theta} \times \mathbf{r}_\alpha + \frac{\partial{L}}{\partial{\mathbf{v}_\alpha}} \cdot \mathbf{\theta} \times \mathbf{v}_\alpha \right) \\
&= \sum_\alpha \left[ \mathbf{\theta} \cdot \mathbf{r}_\alpha \times \frac{d}{dt}\frac{\partial{L}}{\partial{\mathbf{v}_\alpha}} + \mathbf{\theta} \cdot \mathbf{v}_\alpha \times \frac{\partial{L}}{\partial{\mathbf{v}_\alpha}} \right] \\
&= \mathbf{\theta} \cdot \sum_\alpha \frac{d}{dt} \left( \mathbf{r}_\alpha \times \frac{\partial{L}}{\partial{\mathbf{v}_\alpha}} \right) \\
&= 0
\end{aligned}
$$
{: .notice--primary}

### Galilean Transformation / ガリレイ変換

$$
\begin{aligned}
\mathbf{r}' &= \mathbf{r} + \mathbf{V}t \\
t' &= t
\end{aligned}
$$
{: .notice--info}

$$
\begin{aligned}
L' &= \frac{1}{2} m \left( \mathbf{v}' \right)^2 - U'(\mathbf{r}') \\
&= \frac{1}{2} m \mathbf{v}^2 + m \mathbf{v} \cdot \mathbf{V} + \frac{1}{2} m \mathbf{V}^2 - U(\mathbf{r}) \\
&= L + \frac{d}{dt} \left( m \mathbf{r} \cdot \mathbf{V} + \frac{1}{2} m \mathbf{V}^2 t \right) \\
\delta S' &= \delta \int_{t_1}^{t_2} L' dt' \\
&= \delta \int_{t_1}^{t_2} L dt + \delta \left[ m \mathbf{r} \cdot \mathbf{V} + \frac{1}{2} m \mathbf{V}^2 t \right]_{t_1}^{t_2} \\
&= \delta S
\end{aligned}
$$
{: .notice--primary}

### Virial Theorem / Virial定理

$$
U(\alpha \mathbf{r}) = \alpha ^k U(\mathbf{r}) \\
\frac{t'}{t} = \left( \frac{l'}{l} \right)^{1-\frac{k}{2}} \\
\langle T \rangle = \frac{k}{2}\langle U \rangle
$$
{: .notice--info}

$$
l' = \alpha l \quad t' = \beta t \\
\frac{T'}{T} = \alpha^2 \beta^{-2} = \frac{U'}{U} = \alpha^k \\
\beta = \alpha^{1-\frac{k}{2}} \\
\begin{aligned}
2T &= \sum_\alpha\mathbf{P}_\alpha\cdot\mathbf{v}_\alpha \\
&= \frac{d}{dt}\left(\sum_\alpha\mathbf{P}_\alpha\cdot\mathbf{r}_\alpha\right) - \sum_\alpha\mathbf{F}_\alpha\cdot\mathbf{r}_\alpha
\end{aligned} \\
\begin{aligned}
\langle 2T \rangle &= \lim_{\tau\to\infty}\frac{1}{\tau}\int_o^\infty\frac{d}{dt}\left(\sum_\alpha\mathbf{P}_\alpha\cdot\mathbf{r}_\alpha\right)dt - \langle\sum_\alpha\mathbf{F}_\alpha\cdot\mathbf{r}_\alpha\rangle \\
&= \lim_{\tau\to\infty}\frac{1}{\tau}\left[\sum_\alpha\mathbf{P}_\alpha\cdot\mathbf{r}_\alpha\right]_0^\infty + \langle\sum_\alpha\frac{\partial U}{\partial\mathbf{r}_\alpha}\cdot\mathbf{r}_\alpha\rangle \\
&= k\langle U \rangle
\end{aligned}
$$
{: .notice--primary}

## Hamiltonian Mechanics / Hamilton力学

### Hamilton's Equation / Hamilton方程式

$$
H = \sum_i p_i \dot{q}_i - L \quad p_i = \frac{\partial{L}}{\partial{\dot{q}_i}} \\
\dot{q}_i = \frac{\partial{H}}{\partial{p}_i} \quad \dot{p}_i = -\frac{\partial{H}}{\partial{q}_i} 
$$
{: .notice--info}

$$
\begin{aligned}
dH &= \sum_i \left(\dot{q}_i dp_i + p_i d\dot{q}_i \right) - \sum_i \left(\frac{\partial{L}}{\partial{q_i}} dq_i + \frac{\partial{L}}{\partial{\dot{q}_i}}d\dot{q_i}\right) - \frac{\partial{L}}{\partial{t}}dt \\
&= \sum_i \left(\dot{q}_i dp_i - \dot{p}_i dq_i\right) - \frac{\partial{L}}{\partial{t}} dt
\end{aligned} \\
\dot{q}_i = \frac{\partial{H}}{\partial{p_i}} \quad \dot{p}_i = -\frac{\partial{H}}{\partial{q_i}} \quad \frac{\partial{L}}{\partial{t}} = -\frac{\partial{H}}{\partial{t}}
$$
{: .notice--primary}

### Poisson Bracket / Poisson括弧

$$
\{F, G\} = \sum_i \left(\frac{\partial{F}}{\partial{q_i}} \frac{\partial{G}}{\partial{p_i}} - \frac{\partial{F}}{\partial{p_i}} \frac{\partial{G}}{\partial{q_i}}\right) \\
\frac{dF}{dt} = \{F, H\} + \frac{\partial{F}}{\partial{t}}
$$
{: .notice--info}

$$
\begin{aligned}
\frac{dF}{dt} &= \sum_i \left(\frac{\partial{F}}{\partial{q_i}}\dot{q}_i + \frac{\partial{F}}{\partial{p_i}}\dot{p}_i \right) + \frac{\partial{F}}{\partial{t}} \\
&= \sum_i \left(\frac{\partial{F}}{\partial{q_i}} \frac{\partial{H}}{\partial{p_i}} - \frac{\partial{F}}{\partial{p_i}} \frac{\partial{H}}{\partial{q_i}}\right) + \frac{\partial{F}}{\partial{t}} \\
&= \{F, H\} + \frac{\partial{F}}{\partial{t}}
\end{aligned}
$$
{: .notice--primary}

### Canonical Transformation / 正準変換

$$
\begin{aligned}
& W(q,Q,t): && p = \frac{\partial{W}}{\partial{q}} && P = -\frac{\partial{W}}{\partial{Q}} && H' = H + \frac{\partial{W}}{\partial{t}} \\
& W(q,P,t): && p = \frac{\partial{W}}{\partial{q}} && Q=\frac{\partial{W}}{\partial{P}} && H' = H + \frac{\partial{W}}{\partial{t}} \\
& W(p,Q,t): && q = -\frac{\partial{W}}{\partial{p}} && P = -\frac{\partial{W}}{\partial{Q}} && H' = H + \frac{\partial{W}}{\partial{t}} \\
& W(p,P,t): && q = -\frac{\partial{W}}{\partial{p}} && Q = \frac{\partial{W}}{\partial{P}} && H' = H + \frac{\partial{W}}{\partial{t}}
\end{aligned}
$$
{: .notice--info}

$$
\delta \int_{t_1}^{t_2} \left(\sum_i p_i \dot{q}_i - H\right) dt = 0 \quad \delta \int_{t_1}^{t_2} \left(\sum_i P_i \dot{Q}_i - H'\right) dt = 0 \\
\sum_i p_i dq_i - H dt = \sum_i P_i dQ_i - H' dt + dW_1(q,Q,t) \\
dW_1 = \sum_i p_i dq_i - \sum_i P_i dQ_i + (H' - H) dt \\
p_i = \frac{\partial{W_1}}{\partial{q_i}} \quad P_i = -\frac{\partial{W_1}}{\partial{Q_i}} \quad H' = H + \frac{\partial{W_1}}{\partial{t}} \\
W_2 = W_1 + \sum_i P_i Q_i \\
dW_2 = \sum_i p_i dq_i + \sum_i Q_i dP_i + (H' - H) dt \\
p_i = \frac{\partial{W_2}}{\partial{q_i}} \quad Q_i = \frac{\partial{W_2}}{\partial{P_i}} \quad H' = H + \frac{\partial{W_2}}{\partial{t}} \\
W_3 = W_1 - \sum_i p_i q_i \\
dW_3 = -\sum_i q_i dp_i - \sum_i P_i dQ_i + (H' - H) dt \\
q_i = -\frac{\partial{W_3}}{\partial{p_i}} \quad P_i = -\frac{\partial{W_3}}{\partial{Q_i}} \quad H' = H + \frac{\partial{W_3}}{\partial{t}} \\
W_4 = W_1 - \sum_i p_i q_i + \sum_i P_i Q_i \\
dW_4 = - \sum_i q_i dp_i + \sum_i Q_i dP_i + (H' - H) dt \\
q_i = -\frac{\partial{W_4}}{\partial{p_i}} \quad Q_i = \frac{\partial{W_4}}{\partial{P_i}} \quad H' = H + \frac{\partial{W_4}}{\partial{t}}
$$
{: .notice--primary}

### Hamilton–Jacobi Equation / Hamilton–Jacobi方程式

$$
\frac{\partial{S}}{\partial{t}} + H\left(q,\frac{\partial{S}}{\partial{q}},t\right) = 0
$$
{: .notice--info}

$$
H' = H + \frac{\partial{W}}{\partial{t}} = 0 \\
\dot{P}_i = -\frac{\partial{H'}}{\partial{Q_i}} = 0 \quad P_i = \alpha_i \\
\begin{aligned}
\frac{dW}{dt} &= \sum_i \frac{\partial{W}}{\partial{q_i}} \dot{q}_i + \frac{\partial{W}}{\partial{t}} \\
&= \sum_i p_i \dot{q}_i - H \\
&= L
\end{aligned} \\
W = \int L dt = S
$$
{: .notice--primary}

### Liouville's Theorem / Liouvilleの定理

$$
\int_R \prod_i dq_i dp_i = \int_{R'} \prod_i dQ_i dP_i
$$
{: .notice--info}

$$
\prod_i dQ_i dP_i = \frac{\partial{(Q,P)}}{\partial{(q,p)}} \prod_i dq_i dp_i \\
\begin{aligned}
\frac{\partial{(Q,P)}}{\partial{(q,p)}} &= \frac{\partial{(Q,P)}}{\partial{(q,P)}} \frac{\partial{(q,P)}}{\partial{(q,p)}} = \frac{\partial{(Q)}}{\partial{(q)}} \frac{\partial{(P)}}{\partial{(p)}} \\
&= \frac{\frac{\partial{(Q)}}{\partial{(q)}}}{\frac{\partial{(p)}}{\partial{(P)}}} = \frac{\det\left(\frac{\partial^2 W}{\partial q_j \partial P_i}\right)}{\det\left(\frac{\partial^2 W}{\partial P_j \partial q_i}\right)} \\
&= 1
\end{aligned}
$$
{: .notice--primary}

## Oscillation / 振動

## Wave / 波動

## Collision / 衝突

## Central Force Motion / 中心力運動

## Rigid Body Motion / 剛体運動

## Gravity / 重力

# Electromagnetism / 電磁気学

## Maxwell's Equation / Maxwell方程式

## Electromagnetic Potential / 電磁ポテンシャル

## Electrostatics / 静電場

## Magnetostatics / 静磁場

## Electromagnetic Induction / 電磁誘導

## Electromagnetic Wave / 電磁波

## Radiation / 放射

## Waveguide / 導波管

## Electrical Circuit / 電気回路

# Statistical Mechanics / 統計力学

## First Law of Thermodynamics / 熱力学第一法則

## Second Law of Thermodynamics / 熱力学第二法則

## Thermodynamic Potential / 熱力学ポテンシャル

## Microstate and Probability / 微視状態と確率

## Ensemble Theory / アンサンブル理論

## Classicial Ideal Gas / 古典理想気体

## Quantum Ideal Gas / 量子理想気体

## Lattice Vibration / 格子振動

## Phase Transition / 相転移

# Quantum Mechanics / 量子力学

## State and Measurement / 状態と測定

## Schrödinger Equation / Schrödinger方程式

## Angular Momentum / 角運動量

## One-Dimensional System / １次元系

## Three-Dimensional System / ３次元系

## Electromagnetic Field System / 電磁場系

## Perturbation Theory / 摂動論

## Scattering Theory / 散乱理論

## Identical Particles / 同種粒子

<!-- # Condensed Matter Physics / 物性物理学

# Particle Physics / 素粒子物理学

# Theory of Relativity / 相対性理論

# Quantum Field Theory / 場の量子論 -->