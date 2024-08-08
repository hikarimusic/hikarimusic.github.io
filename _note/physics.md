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

### Small Oscillation / 微小振動

$$
\ddot{x} + \omega_0^2 x = 0 \\
x = \tilde{A} e^{i \omega_0 t}
$$
{: .notice--info}

$$
U'(x_0) = 0 \quad U''(x_0) = k \\
L = \frac{1}{2} m \dot{x}^2 - \frac{1}{2} k x^2 \\
m \ddot{x} + k x = 0 \\
\ddot{x} + \omega_0^2 x = 0 \\
x = \tilde{A} e^{i \omega_0 t}
$$
{: .notice--primary}

### Damped Oscillation / 減衰振動

$$
\ddot{x} + 2 \beta \dot{x} + \omega_0^2 x = 0 \\
\begin{aligned}
x &= e^{-\beta t} \cdot \tilde{A} e^{i \sqrt{\omega_0^2 - \beta^2} t} \\
x &= e^{-\beta t} (A + B t) \\
x &= e^{-\beta t} \left( A_1 e^{\sqrt{\beta^2 - \omega_0^2} t} + A_2 e^{-\sqrt{\beta^2 - \omega_0^2} t} \right)
\end{aligned}
$$
{: .notice--info}

$$
m \ddot{x} + b \dot{x} + k x = 0 \\
\ddot{x} + 2 \beta \dot{x} + \omega_0^2 x = 0 \\
x = e^{\gamma t} \\
\gamma^2 + 2 \beta \gamma + \omega_0^2 = 0 \\
\gamma = -\beta \pm \sqrt{\beta^2 - \omega_0^2} \\
x = e^{-\beta t} \left( A_1 e^{\sqrt{\beta^2 - \omega_0^2} t} + A_2 e^{-\sqrt{\beta^2 - \omega_0^2} t} \right)
$$
{: .notice--primary}

### Forced Oscillation / 強制振動

$$
\ddot{x} + 2 \beta \dot{x} + \omega_0^2 x = \alpha e^{i \omega t} \\
x_p = \tilde{A} e^{i \omega t} \\
|\tilde{A}| = \frac{\alpha}{\sqrt{(\omega^2 - \omega_0^2)^2 + 4 \beta^2 \omega^2}} \\
\text{arg}(\tilde{A}) = \tan^{-1} \left( \frac{2 \beta \omega}{\omega^2 - \omega_0^2} \right)
$$
{: .notice--info}

$$
m \ddot{x} + b \dot{x} + k x = f\cos(\omega t) \\
\ddot{x} + 2 \beta \dot{x} + \omega_0^2 x = \alpha e^{i \omega t} \\
x_p = \tilde{A} e^{i \omega t} \\
(-\omega^2 + 2 \beta \omega i + \omega_0^2) \tilde{A} = \alpha \\
\tilde{A} = \frac{\alpha}{(\omega_0^2 - \omega^2) + 2 \beta \omega i}
$$
{: .notice--primary}

### Coupled Oscillation / 連成振動

$$
M \ddot{\mathbf{x}} + K \mathbf{x} = 0 \\
\left( -\omega_n^2 M + K \right) \mathbf{A_n} = 0 \\
\mathbf{x} = \sum_n \tilde{c}_n \mathbf{A_n} e^{i \omega_n t} \\
\mathbf{x} = \sum_n q_n \mathbf{A_n} \quad \ddot{q}_n + \omega_n^2 q_n = 0
$$
{: .notice--info}

$$
\begin{aligned}
L &= \frac{1}{2} \sum_{i,j} m_{ij} \dot{x}_i \dot{x}_j - \frac{1}{2} \sum_{i,j} k_{ij} x_i x_j \\
&= \frac{1}{2} \dot{\mathbf{x}}^T M \dot{\mathbf{x}} - \frac{1}{2} \mathbf{x}^T K \mathbf{x} 
\end{aligned} \\
M \ddot{\mathbf{x}} + K \mathbf{x} = 0 \quad \mathbf{x} = \mathbf{A} e^{i \omega t} \\
|-\omega_n^2 M + K| = 0 \quad (-\omega_n^2 M + K) \mathbf{A}_n = 0 \\
\mathbf{x} = \sum_n \hat{c}_n \mathbf{A}_n e^{i \omega_n t} \\
\mathbf{A}_n^T (K \mathbf{A}_m) - (K \mathbf{A}_n)^T \mathbf{A}_m = (\omega_n^2 - \omega_m^2) \mathbf{A}_n^T M \mathbf{A}_m = 0 \\
\mathbf{A}_n^T M \mathbf{A}_m = \delta_{nm} \quad \mathbf{A}_n^T K \mathbf{A}_m = \delta_{nm} \omega_m^2 \\
\mathbf{x} = \sum_n q_n \mathbf{A}_n \\
\begin{aligned}
L &= \frac{1}{2} \sum_{n,m} \dot{q}_n (\mathbf{A}_n^T M \mathbf{A}_m) \dot{q}_m - \frac{1}{2} \sum_{n,m} q_n (\mathbf{A}_n^T K \mathbf{A}_m) q_m \\
&= \frac{1}{2} \sum_n \dot{q}_n^2 - \frac{1}{2} \sum_n \omega_n^2 q_n^2
\end{aligned} \\
\ddot{q}_n + \omega_n^2 q_n = 0
$$
{: .notice--primary}

## Wave / 波動

### Wave Equation / 波動方程式

$$
\frac{\partial}{\partial t} \left( \frac{\delta L}{\delta (\partial_t \phi)} \right) + \frac{\partial}{\partial x} \left( \frac{\delta L}{\delta (\partial_x \phi)} \right) - \frac{\delta L}{\delta \phi} = 0 \\
\rho \frac{\partial^2 \phi}{\partial t^2} - k \frac{\partial^2 \phi}{\partial x^2} = 0
$$
{: .notice--info}

$$
L = \int \mathcal{L} \left( \phi, \frac{\partial \phi}{\partial t}, \frac{\partial \phi}{\partial x}, t \right) dx \\
\begin{aligned}
\delta S &= \int dt \int dx \left[ \frac{\delta L}{\delta \phi} \delta \phi + \frac{\delta L}{\delta (\partial_t \phi)} \delta (\partial_t \phi) + \frac{\delta L}{\delta (\partial_x \phi)} \delta (\partial_x \phi) \right] \\
&= \int dt \int dx \left[ \frac{\delta L}{\delta \phi} - \frac{\partial}{\partial t} \left( \frac{\delta L}{\delta (\partial_t \phi)} \right) - \frac{\partial}{\partial x} \left( \frac{\delta L}{\delta (\partial_x \phi)} \right) \right] \delta \phi 
\end{aligned} \\
\frac{\partial}{\partial t} \left( \frac{\delta L}{\delta (\partial_t \phi)} \right) + \frac{\partial}{\partial x} \left( \frac{\delta L}{\delta (\partial_x \phi)} \right) - \frac{\delta L}{\delta \phi} = 0 \\
L = \int \left[ \frac{1}{2} \rho (\partial_t \phi)^2 - \frac{1}{2} k (\partial_x \phi)^2 \right] dx \\
\delta L = \int \left[ \rho (\partial_t \phi) \delta (\partial_t \phi) - k (\partial_x \phi) \delta (\partial_x \phi) \right] dx \\
\frac{\delta L}{\delta (\partial_t \phi)} = \rho \frac{\partial \phi}{\partial t} \quad \frac{\delta L}{\delta (\partial_x \phi)} = -k \frac{\partial \phi}{\partial x} \\
\rho \frac{\partial^2 \phi}{\partial t^2} - k \frac{\partial^2 \phi}{\partial x^2} = 0
$$
{: .notice--primary}

### Bounded Wave / 有界波

$$
\frac{\partial^2 \phi}{\partial t^2} - v^2 \frac{\partial^2 \phi}{\partial x^2} = 0 \\
\phi = \sum_n \tilde{A}_n e^{i (\omega_n t - k_n x)} \\
\begin{aligned}
&\phi(0) = \phi(L) = 0: && k_n = \frac{n \pi}{L} \quad \tilde{A}_{-n} = -\tilde{A}_n \\
&\frac{\partial \phi}{\partial x}(0) = \frac{\partial \phi}{\partial x}(L) = 0: && k_n = \frac{n \pi}{L} \quad \tilde{A}_{-n} = \tilde{A}_n \\
&\phi(0) = \phi(L),\; \frac{\partial \phi}{\partial x}(0) = \frac{\partial \phi}{\partial x}(L): && k_n = \frac{2n \pi}{L}
\end{aligned}
$$
{: .notice--info}

$$
\phi(x,t) = \psi(x) e^{i \omega t} \\
\psi(x) = \tilde{A} e^{-ikx} \\
\phi = \sum_n \tilde{A}_n e^{i(\omega_n t - k_n x)} \quad k_n = \pm \frac{\omega_n}{v} \\
\phi(0) = \phi(L) = 0 \\
\begin{aligned}
&\tilde{A}_n e^{i \omega_n t} + \tilde{A}_{-n} e^{i \omega_n t} = 0 && \tilde{A}_{-n} = -\tilde{A}_n \\
&\tilde{A}_n e^{i \omega_n t} \left( e^{-ik_n L} - e^{ik_n L} \right) = 0 && k_n L = n \pi
\end{aligned} \\
\frac{\partial \phi}{\partial x}(0) = \frac{\partial \phi}{\partial x}(L) = 0 \\
\begin{aligned}
& -\tilde{A}_n k_n e^{i \omega_n t} - \tilde{A}_{-n} (-k_n) e^{i \omega_n t} = 0 && \tilde{A}_{-n} = \tilde{A}_n \\
& -\tilde{A}_n k_n e^{i \omega_n t} \left( e^{-ik_n L} - e^{ik_n L} \right) = 0 && k_n L = n \pi
\end{aligned} \\
\phi(0) = \phi(L) \quad \frac{\partial \phi}{\partial x}(0) = \frac{\partial \phi}{\partial x}(L) \\
\begin{align*}
\left( \tilde{A}_n + \tilde{A}_{-n} \right) e^{i\omega_n t} &= \left(\tilde{A}_n e^{-i k_n L} + \tilde{A}_{-n} e^{i k_n L} \right) e^{i\omega_n t} \\
\left( -\tilde{A}_n k_n + \tilde{A}_{-n} k_n \right) e^{i\omega_n t} &= \left( -\tilde{A}_n k_n e^{-i k_n L} + \tilde{A}_{-n} k_n e^{i k_n L} \right) e^{i\omega_n t}
\end{align*} \\
e^{ik_n L} = e^{-ik_n L} = 1 \quad k_n L = 2n \pi
$$
{: .notice--primary}

### Free Wave / 自由波

$$
\frac{\partial^2 \phi}{\partial t^2} - v^2 \frac{\partial^2 \phi}{\partial x^2} = 0 \\
\phi = \int \tilde{A}(k) e^{i (\omega t - k x)} \, dk \\
v_p = \frac{\omega}{k} \quad v_g = \frac{d\omega}{dk}
$$
{: .notice--info}

$$
\phi(x, t) = \psi(x) e^{i \omega t} \\
\psi(x) = \tilde{A} e^{-i k x} \\
\phi = \int \tilde{A}(k) e^{i (\omega t - k x)} \, dk \quad k = \frac{\omega}{v} \\
\omega = \omega_0 + \left( \frac{d\omega}{dk} \right)_0 (k - k_0) \\
\omega t - k x = (\omega_0 t - k_0 x) + (k - k_0)(\omega_0' t - x) \\
\phi = \int \tilde{A}(k) e^{i(\omega_0 t - k_0 x)} e^{i (k - k_0) (\omega_0' t - x)} \, dk \\
v_p = \frac{\omega}{k} \quad v_g = \frac{d\omega}{dk}
$$
{: .notice--primary}

## Collision / 衝突

## Central Force Motion / 中心力運動

### Reduced Mass / 換算質量

$$
\begin{aligned}
\mu &= \frac{m_1 m_2}{m_1 + m_2} \\
M &= \mu r^2 \dot{\theta} \\
E &= \frac{1}{2} \mu \dot{r}^2 + \frac{1}{2}\frac{M^2}{\mu r^2} + U(r)
\end{aligned}
$$
{: .notice--info}

$$
\begin{aligned}
L &= \frac{1}{2} m_1 \left| \frac{m_2}{m_1 + m_2} \dot{\mathbf{r}} \right|^2 + \frac{1}{2} m_2 \left| \frac{m_1}{m_1 + m_2} \dot{\mathbf{r}} \right|^2 - U(r) \\
&= \frac{1}{2} \frac{m_1 m_2}{m_1 + m_2} (\dot{r}^2 + r^2 \dot{\theta}^2) - U(r)
\end{aligned} \\
M = \frac{\partial L}{\partial\dot{\theta}} = \mu r^2 \dot{\theta} \\
\begin{aligned}
E &= \frac{1}{2} \mu \dot{r}^2 + \frac{1}{2} \mu r^2 \dot{\theta}^2 + U(r) \\
&= \frac{1}{2} \mu \dot{r}^2 + \frac{1}{2}\frac{M^2}{\mu r^2} + U(r)
\end{aligned}
$$
{: .notice--primary}

### Orbit / 軌道

$$
U_{\text{eff}}(r) = U(r) + \frac{M^2}{2\mu r^2} \\
t = \int \frac{dr}{\sqrt{\frac{2}{\mu} (E - U_{\text{eff}}(r))}} \\
\theta = \int \frac{M dr}{r^2 \sqrt{2\mu (E - U_{\text{eff}}(r))}}
$$
{: .notice--info}

$$
E = \frac{1}{2} \mu \dot{r}^2 + U_{\text{eff}}(r) \\
\frac{dr}{dt} = \sqrt{\frac{2}{\mu} (E - U_{\text{eff}}(r))} \\
t = \int \frac{dr}{\sqrt{\frac{2}{\mu} (E - U_{\text{eff}}(r))}} \\
\begin{aligned}
\frac{d\theta}{dr} &= \frac{d\theta}{dt} \frac{dt}{dr} \\
&= \frac{M}{\mu r^2} \frac{1}{\sqrt{\frac{2}{\mu} (E - U_{\text{eff}}(r))}} 
\end{aligned} \\
\theta = \int \frac{M dr}{r^2 \sqrt{2\mu (E - U_{\text{eff}}(r))}}
$$
{: .notice--primary}

### Kepler Problem / Kepler問題

$$
U = -\frac{\alpha}{r} \quad p = \frac{M^2}{\mu\alpha} \quad e = \sqrt{1 + \frac{2EM^2}{\mu \alpha^2}} \\
r = \frac{p}{1 + e \cos \theta} \\
\tau = 2\pi \sqrt{\frac{\mu}{\alpha}}a^{3/2}
$$
{: .notice--info}

$$
\begin{aligned}
\theta &= \int \frac{\frac{M}{r^2} \, dr}{\sqrt{2\mu \left( E + \frac{\alpha}{r} - \frac{M^2}{2\mu r^2} \right)}} \\
&= \int \frac{\frac{1}{r^2} \,dr}{\sqrt{ -\left( \frac{1}{r} - \frac{\mu \alpha}{M^2}\right)^2 + \frac{\mu^2 \alpha^2}{M^4}\left(1 + \frac{2EM^2}{\mu \alpha^2}\right)}} \\
&= \int \frac{\frac{1}{r^2} \,dr}{\sqrt{ -\left( \frac{1}{r} - \frac{1}{p}\right)^2 + \frac{e^2}{p^2}}} \\
&= \int \frac{\frac{e}{p}\sin\phi\,d\phi}{\frac{e}{p}\sin \phi} \\
&= \phi + C \quad \left( \frac{1}{r} - \frac{1}{p} = \frac{e}{p} \cos \phi \right)
\end{aligned} \\
r = \frac{p}{1 + e \cos \theta} \quad a = \frac{p}{1 - e^2} \quad b = \frac{p}{\sqrt{1 - e^2}} \\
\tau = \frac{\pi ab}{\dot{S}} = \frac{\pi a \sqrt{ap}}{\frac{M}{2\mu}}= 2\pi \sqrt{\frac{\mu}{\alpha}}a^{3/2}
$$
{: .notice--primary}

### Gravity / 重力

$$
\begin{aligned}
\Phi &= \frac{U}{m} = -\frac{GM}{r} \\
\mathbf{g} &= -\mathbf{\nabla} \Phi = -\frac{GM}{r^2} \hat{\mathbf{e}}_r \\
\mathbf{F} &= m\mathbf{g} = -\frac{GMm}{r^2} \hat{\mathbf{e}}_r
\end{aligned}
$$
{: .notice--info}

## Rigid Body Motion / 剛体運動

### Non-Inertial Frame / 非慣性系

$$
\begin{aligned}
\mathbf{r} &= \mathbf{R} + \mathbf{r}' \\
\mathbf{v} &= \mathbf{V} + \mathbf{v}' + \boldsymbol{\Omega} \times \mathbf{r}' \\
\mathbf{a} &= \mathbf{A} + \mathbf{a}' + \dot{\boldsymbol{\Omega}} \times \mathbf{r}' + \boldsymbol{\Omega} \times (\boldsymbol{\Omega} \times \mathbf{r}') + 2 \boldsymbol{\Omega} \times \mathbf{v}'
\end{aligned} 
$$
{: .notice--info}

$$
\frac{d\mathbf{Q}}{dt} = \frac{d'\mathbf{Q}}{dt} + \boldsymbol{\Omega} \times \mathbf{Q} \\
\mathbf{r} = \mathbf{R} + \mathbf{r}' \\
\begin{aligned}
\frac{d\mathbf{r}}{dt} &= \frac{d\mathbf{R}}{dt} + \frac{d\mathbf{r}'}{dt}  \\
&= \frac{d\mathbf{R}}{dt} + \frac{d'\mathbf{r}'}{dt} + \boldsymbol{\Omega} \times \mathbf{r}'
\end{aligned} \\
\mathbf{v} = \mathbf{V} + \mathbf{v}' + \boldsymbol{\Omega} \times \mathbf{r}' \\
\begin{aligned}
\frac{d\mathbf{v}}{dt} &= \frac{d\mathbf{V}}{dt} + \frac{d\mathbf{v}'}{dt} + \frac{d\boldsymbol{\Omega}}{dt} \times \mathbf{r}' + \boldsymbol{\Omega} \times \frac{d\mathbf{r}'}{dt} \\
&= \frac{d\mathbf{V}}{dt} + \frac{d'\mathbf{v}'}{dt} + \boldsymbol{\Omega}\times\mathbf{v}' + \frac{d\boldsymbol{\Omega}}{dt}  \times \mathbf{r}' + \boldsymbol{\Omega} \times \left( \frac{d'\mathbf{r}'}{dt} + \boldsymbol{\Omega} \times \mathbf{r}' \right)
\end{aligned} \\
\mathbf{a} = \mathbf{A} + \mathbf{a}' + \dot{\boldsymbol{\Omega}} \times \mathbf{r}' + \boldsymbol{\Omega} \times (\boldsymbol{\Omega} \times \mathbf{r}') + 2 \boldsymbol{\Omega} \times \mathbf{v}'
$$
{: .notice--primary}

### Euler Angle / Euler角

$$
\begin{aligned}
\Omega_1 &= \dot{\phi} \sin \theta \sin \psi + \dot{\theta} \cos \psi \\
\Omega_2 &= \dot{\phi} \sin \theta \cos \psi - \dot{\theta} \sin \psi \\
\Omega_3 &= \dot{\phi} \cos \theta + \dot{\psi}
\end{aligned} \\
$$
{: .notice--info}

### Inertia Tensor / 慣性テンソル

$$
\begin{aligned}
I_{ij} &= \sum_{\alpha} m_{\alpha} (\delta_{ij} r_{\alpha}^2 - r_{\alpha ,i} r_{\alpha ,j}) \\
T &= \sum_{i,j} \frac{1}{2} I_{ij} \Omega_i \Omega_j \\
M_i &= \sum_j I_{ij} \Omega_j
\end{aligned} 
$$
{: .notice--info}

$$
\begin{aligned}
T &= \sum_{\alpha} \frac{1}{2} m_{\alpha} (\boldsymbol{\Omega} \times \mathbf{r}_{\alpha}) \cdot (\boldsymbol{\Omega} \times \mathbf{r}_{\alpha}) \\
&= \sum_{\alpha} \frac{1}{2} m_{\alpha} [\Omega^2 r_{\alpha}^2 - (\boldsymbol{\Omega}\cdot\mathbf{r}_{\alpha})^2] \\
&= \sum_{i,j}\sum_{\alpha} \frac{1}{2} m_{\alpha} (\delta_{ij} r_{\alpha}^2 - r_{\alpha ,i} r_{\alpha ,j}) \Omega_i \Omega_j \\
\end{aligned} \\
\begin{aligned}
\mathbf{M} &= \sum_{\alpha} m_{\alpha} \mathbf{r}_{\alpha} \times (\mathbf{\Omega} \times \mathbf{r}_{\alpha}) \\
&= \sum_{\alpha} m_{\alpha} [\mathbf{\Omega} (r_{\alpha}^2) - \mathbf{r}_{\alpha} (\mathbf{r}_{\alpha} \cdot \Omega)] \\
M_i &= \sum_j \sum_{\alpha} m_{\alpha} (\delta_{ij} r_{\alpha}^2 - r_{\alpha ,i} r_{\alpha ,j}) \Omega_j
\end{aligned}
$$
{: .notice--primary}

### Euler's Equation / Eulerの運動方程式

$$
\begin{aligned}
I_1 \dot{\Omega}_1 + (I_3 - I_2) \Omega_2 \Omega_3 &= N_1 \\
I_2 \dot{\Omega}_2 + (I_1 - I_3) \Omega_3 \Omega_1 &= N_2 \\
I_3 \dot{\Omega}_3 + (I_2 - I_1) \Omega_1 \Omega_2 &= N_3
\end{aligned}
$$
{: .notice--info}

$$
\frac{d\mathbf{M}}{dt} = \frac{d'\mathbf{M}}{dt} + \boldsymbol{\Omega} \times \mathbf{M} = \mathbf{N} \\
\begin{bmatrix}
I_1 \dot{\Omega}_1 \\
I_2 \dot{\Omega}_2 \\
I_3 \dot{\Omega}_3
\end{bmatrix}
+
\begin{bmatrix}
\Omega_1 \\
\Omega_2 \\
\Omega_3
\end{bmatrix}
\times
\begin{bmatrix}
I_1 \Omega_1 \\
I_2 \Omega_2 \\
I_3 \Omega_3
\end{bmatrix}
=
\begin{bmatrix}
N_1 \\
N_2 \\
N_3
\end{bmatrix}
$$
{: .notice--primary}

### Symmetrical Top (Free) / 対称コマ（自由）

$$
\begin{aligned}
\theta &= \text{const.} \\
\dot{\phi} &= \frac{M_z}{I_1} \\
\dot{\psi} &= M_z \cos \theta \left( \frac{1}{I_3} - \frac{1}{I_1} \right)
\end{aligned}
$$
{: .notice--info}

$$
L = \frac{1}{2} I_1 (\dot{\phi}^2 \sin^2 \theta + \dot{\theta}^2) + \frac{1}{2} I_3 (\dot{\phi} \cos \theta + \dot{\psi})^2 \\
\begin{aligned}
\frac{\partial L}{\partial \dot{\psi}} &= I_3 (\dot{\phi} \cos \theta + \dot{\psi}) = M_3 = M_z \cos \theta \\
\frac{\partial L}{\partial \dot{\phi}} &= I_1 \dot{\phi} \sin^2 \theta + I_3 (\dot{\phi} \cos \theta + \dot{\psi}) \cos \theta = M_z
\end{aligned} \\
\begin{aligned}
\dot{\phi} &= \frac{M_z - M_z \cos^2 \theta}{I_1 \sin^2 \theta} = \frac{M_z}{I_1} \\
\dot{\psi} &= \frac{M_z \cos \theta}{I_3} - \dot{\phi} \cos \theta = M_z \cos \theta \left( \frac{1}{I_3} - \frac{1}{I_1} \right)
\end{aligned} \\
\begin{aligned}
\frac{\partial L}{\partial \theta} &= I_1 \dot{\phi}^2 \sin \theta \cos \theta - I_3 (\dot{\phi} \cos \theta + \dot{\psi}) \dot{\phi} \sin \theta \\
&= \frac{M_z^2}{I_1} \sin \theta \cos \theta - \frac{M_z^2}{I_1} \sin \theta \cos \theta = 0 \\
&= \frac{d}{dt} \left( \frac{\partial L}{\partial \dot{\theta}} \right) = \frac{d}{dt} (I_1 \dot{\theta}) \quad (\dot{\theta} = \text{const.})
\end{aligned} \\
E = \frac{1}{2} I_1 \left( \frac{M_z^2}{I_1^2} \sin^2 \theta + \dot{\theta}^2 \right) + \frac{1}{2} I_3 \frac{M_z^2}{I_3^2} \cos^2 \theta \\
\quad \theta = \text{const.}
$$
{: .notice--primary}

### Symmetrical Top (Gravity) / 対称コマ（重力）

$$
\begin{aligned}
\theta_1 &\leq \theta \leq \theta_2 \\
\dot{\phi}& = \frac{M_z - M_3 \cos \theta}{(I_1 + Ma^2) \sin^2 \theta} \\
\dot{\psi} &= \frac{M_3}{I_3} - \frac{(M_z - M_3 \cos \theta) \cos \theta}{(I_1 + Ma^2) \sin^2 \theta}
\end{aligned}
$$
{: .notice--info}

$$
L = \frac{1}{2} (I_1 + Ma^2) (\dot{\phi}^2 \sin^2 \theta + \dot{\theta}^2) + \frac{1}{2} I_3 (\dot{\phi} \cos \theta + \dot{\psi})^2 - Mga \cos \theta \\
\begin{aligned}
\frac{\partial L}{\partial \dot{\psi}} &= I_3 (\dot{\phi} \cos \theta + \dot{\psi}) = M_3 \\
\frac{\partial L}{\partial \dot{\phi}} &= (I_1 + Ma^2) \dot{\phi} \sin^2 \theta + I_3 (\dot{\phi} \cos \theta + \dot{\psi}) \cos \theta = M_z
\end{aligned} \\
\begin{aligned}
\dot{\phi} &= \frac{M_z - M_3 \cos \theta}{(I_1 + Ma^2) \sin^2 \theta} \\
\dot{\psi} &= \frac{M_3}{I_3} - \frac{(M_z - M_3 \cos \theta) \cos \theta}{(I_1 + Ma^2) \sin^2 \theta}
\end{aligned} \\
E = \frac{1}{2} (I_1 + Ma^2) \dot{\theta}^2 + \frac{1}{2} \frac{(M_z - M_3 \cos \theta)^2}{(I_1 + Ma^2) \sin^2 \theta} + \frac{1}{2} \frac{M_3^2}{I_3} + Mga \cos \theta \\
u = \cos \theta \quad \dot{\theta}^2 = \frac{\dot{u}^2}{1 - u^2} \\
E = \frac{1}{2} (I_1 + Ma^2) \frac{\dot{u}^2}{1 - u^2} + \frac{1}{2} \frac{(M_z - M_3 u)^2}{(I_1 + Ma^2)(1 - u^2)} + \frac{1}{2} \frac{M_3^2}{I_3} + Mga u \\
\dot{u}^2 = (1 - u^2) \left( A - B u \right) - \frac{(M_z - M_3 u)^2}{(I_1 + Ma^2)^2} \geq 0 \\
f(\cos \theta_1) = f(\cos \theta_2) = 0 \\
\theta_1 \leq \theta \leq \theta_2
$$
{: .notice--primary}

### Asymmetrical Top (Free) / 非対称コマ（自由）

$$
\sqrt{2EI_1} \leq M \leq \sqrt{2EI_3} \\
\Omega_1: \text{stable} \quad \Omega_2: \text{unstable} \quad \Omega_3: \text{stable}
$$
{: .notice--info}

$$
M^2 = M_1^2 + M_2^2 + M_3^2 \\
E = \frac{M_1^2}{2I_1} + \frac{M_2^2}{2I_2} + \frac{M_3^2}{2I_3} \\
\sqrt{2EI_1} \leq M \leq \sqrt{2EI_3} \\
\delta \Omega_1 = a e^{\lambda t} \quad \delta \Omega_2 = b e^{\lambda t} \quad \delta \Omega_3 = c e^{\lambda t} \\
\begin{aligned}
\Omega_1 : \quad \lambda^2 &=  \frac{-\Omega_1^2(I_3 - I_1)(I_2 - I_1)}{I_2 I_3} < 0, &&\text{stable} \\
\Omega_2 : \quad \lambda^2 &=  \frac{\Omega_2^2(I_3 - I_2)(I_2 - I_1)}{I_1 I_3} > 0,  &&\text{unstable} \\
\Omega_3 : \quad \lambda^2 &=  \frac{-\Omega_3^2(I_3 - I_2)(I_3 - I_1)}{I_1 I_2} < 0,  &&\text{stable}
\end{aligned}
$$
{: .notice--primary}

## Continuum Mechanics / 連続体力学

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

# Physical Mathematics / 物理数学

## Calculus / 微積分

## Complex Analysis / 複素解析

## Ordinary Differential Equation / 常微分方程式

## Partial Differential Equation / 偏微分方程式

## Special Function / 特殊関数

## Linear Algebra / 線形代数

## Abstract Algebra / 抽象代数

## Vector Calculus / ベクトル解析

## Differential Geometry / 微分幾何

<!-- # Condensed Matter Physics / 物性物理学

# Particle Physics / 素粒子物理学

# Theory of Relativity / 相対性理論

# Quantum Field Theory / 場の量子論 -->