---
title: 'Physics 🍊⭐'
date: 2023-01-02
permalink: /note/physics
tags:
  - note
toc: true
---

Equations of Physics

{% include toc %}

# Classical Mechanics / 古典力学

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
\begin{aligned}{}
& \mathbf{P} = m\mathbf{v} && \mathbf{F} \\
& \mathbf{P} = M\mathbf{V} && \mathbf{F} = \sum_{\alpha}\mathbf{F}_\alpha^{(e)}
\end{aligned}
$$
{: .notice--info}

$$
\frac{d\mathbf{P}}{dt} = \mathbf{F} \\
\begin{aligned}{}
\mathbf{P} &= \sum_\alpha m_\alpha\left(\mathbf{V} + \mathbf{v'}_\alpha\right) \\
&= \sum_\alpha m_\alpha\mathbf{V} + \sum_\alpha m_\alpha\mathbf{v'}_\alpha \\
&= M\mathbf{V}
\end{aligned} \\
\begin{aligned}{}
\mathbf{F} &= \sum_\alpha\left(\mathbf{F}_\alpha^{(e)} + \sum_{\beta\neq\alpha}\mathbf{F}_{\alpha\beta}\right) \\
&= \sum_\alpha\mathbf{F}_{\alpha}^{(e)} + \sum_{\beta>\alpha}\left(\mathbf{F}_{\alpha\beta} + \mathbf{F}_{\beta\alpha}\right) \\
&= \sum_\alpha\mathbf{F}_\alpha^{(e)}
\end{aligned}
$$
{: .notice--primary}

### Angular Momentum / 角運動量

$$
\frac{d\mathbf{M}}{dt} = \mathbf{N} \\
\begin{aligned}{}
& \mathbf{M} = m\mathbf{r}\times\mathbf{v} && \mathbf{N} = \mathbf{r}\times\mathbf{F} \\
& \mathbf{M} = M\mathbf{R}\times\mathbf{V} + \sum_\alpha m_\alpha\mathbf{r'}_\alpha\times\mathbf{v'}_\alpha && \mathbf{N} = \sum_\alpha\mathbf{r}_\alpha\times\mathbf{F}_\alpha^{(e)}
\end{aligned}
$$
{: .notice--info}

$$
\frac{d\mathbf{M}}{dt} = m\mathbf{v}\times\mathbf{v} + m\mathbf{r}\times\mathbf{a} = \mathbf{r}\times\mathbf{F} = \mathbf{N} \\
\begin{aligned}{}
\mathbf{M} &= \sum_\alpha m_\alpha\left(\mathbf{R}+\mathbf{r'}_\alpha\right)\times\left(\mathbf{V}+\mathbf{v'}_\alpha\right) \\
&= \sum_\alpha m_\alpha\mathbf{R}\times\mathbf{V} + \mathbf{R}\times\left(\sum_\alpha m_\alpha\mathbf{v}'_\alpha\right) \\
&+ \left(\sum_\alpha m_\alpha\mathbf{r'}_\alpha\right)\times\mathbf{V} + \sum_\alpha m_\alpha\mathbf{r'}_\alpha\times\mathbf{v'}_\alpha \\
&= M\mathbf{R}\times\mathbf{V} + \sum_\alpha m_\alpha\mathbf{r'}_\alpha\times\mathbf{v'}_\alpha
\end{aligned} \\
\begin{aligned}{}
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
\begin{aligned}{}
E &= \frac{1}{2} mv^2 + U \\
E &= \frac{1}{2} MV^2 + \sum_\alpha \frac{1}{2} m_\alpha v_\alpha'^2 + U \\
\end{aligned}
$$
{: .notice--info}

$$
\frac{dE}{dt} = m\mathbf{v} \cdot \mathbf{a} + (\nabla U) \cdot \mathbf{v} + \frac{\partial U}{\partial t} = (\mathbf{F} + \nabla U) \cdot \mathbf{v} = 0 \\
\begin{aligned}{}
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
\begin{aligned}{}
& \frac{d}{dt} \frac{\partial{L}}{\partial{\dot{q}_i}} - \frac{\partial{L}}{\partial{q_i}} = 0 \\
& \frac{d}{dt} \frac{\partial{L}}{\partial{\dot{q}_i}} - \frac{\partial{L}}{\partial{q_i}} + \sum_j \lambda_j \frac{\partial{f_j}}{\partial{q_i}} = 0
\end{aligned}
$$
{: .notice--info}

$$
\begin{aligned}{}
\delta S &= \int_{t_1}^{t_2} \sum_i \left( \frac{\partial{L}}{\partial{q_i}} \delta q_i + \frac{\partial{L}}{\partial{\dot{q}_i}} \delta \dot{q}_i \right) dt \\
&= \int_{t_1}^{t_2} \sum_i \frac{\partial{L}}{\partial{q_i}} \delta q_i dt + \left[ \sum_i \frac{\partial{L}}{\partial{\dot{q}_i}} \delta q_i \right]_{t_1}^{t_2} - \int_{t_1}^{t_2} \sum_i \frac{d}{dt} \left( \frac{\partial{L}}{\partial{\dot{q_i}}} \right) \delta q_i dt \\
&= \int_{t_1}^{t_2} \sum_i \left( \frac{\partial{L}}{\partial{q_i}} - \frac{d}{dt} \frac{\partial{L}}{\partial{\dot{q}_i}} \right) \delta q_i dt \\
&= 0
\end{aligned}
$$
{: .notice--primary}

### Conservation Law / 保存則

$$
\begin{aligned}{}
E &= \sum_i \dot{q}_i \frac{\partial{L}}{\partial{\dot{q}_i}} - L = const. \\
\mathbf{P} &= \sum_\alpha \frac{\partial{L}}{\partial{\mathbf{v}_\alpha}} = const. \\
\mathbf{M} &= \sum_\alpha \mathbf{r}_\alpha \times \frac{\partial{L}}{\partial{\mathbf{v}_\alpha}} = const.
\end{aligned}
$$
{: .notice--info}

$$
\begin{aligned}{}
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
\begin{aligned}{}
\mathbf{r}' &= \mathbf{r} + \mathbf{V}t \\
t' &= t
\end{aligned}
$$
{: .notice--info}

$$
\begin{aligned}{}
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
\begin{aligned}{}
2T &= \sum_\alpha\mathbf{P}_\alpha\cdot\mathbf{v}_\alpha \\
&= \frac{d}{dt}\left(\sum_\alpha\mathbf{P}_\alpha\cdot\mathbf{r}_\alpha\right) - \sum_\alpha\mathbf{F}_\alpha\cdot\mathbf{r}_\alpha
\end{aligned} \\
\begin{aligned}{}
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
\begin{aligned}{}
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
\begin{aligned}{}
\frac{dF}{dt} &= \sum_i \left(\frac{\partial{F}}{\partial{q_i}}\dot{q}_i + \frac{\partial{F}}{\partial{p_i}}\dot{p}_i \right) + \frac{\partial{F}}{\partial{t}} \\
&= \sum_i \left(\frac{\partial{F}}{\partial{q_i}} \frac{\partial{H}}{\partial{p_i}} - \frac{\partial{F}}{\partial{p_i}} \frac{\partial{H}}{\partial{q_i}}\right) + \frac{\partial{F}}{\partial{t}} \\
&= \{F, H\} + \frac{\partial{F}}{\partial{t}}
\end{aligned}
$$
{: .notice--primary}

### Canonical Transformation / 正準変換

$$
\begin{aligned}{}
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
\begin{aligned}{}
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
\begin{aligned}{}
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
\begin{aligned}{}
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
\begin{aligned}{}
L &= \frac{1}{2} \sum_{i,j} m_{ij} \dot{x}_i \dot{x}_j - \frac{1}{2} \sum_{i,j} k_{ij} x_i x_j \\
&= \frac{1}{2} \dot{\mathbf{x}}^T M \dot{\mathbf{x}} - \frac{1}{2} \mathbf{x}^T K \mathbf{x} 
\end{aligned} \\
M \ddot{\mathbf{x}} + K \mathbf{x} = 0 \quad \mathbf{x} = \mathbf{A} e^{i \omega t} \\
|-\omega_n^2 M + K| = 0 \quad (-\omega_n^2 M + K) \mathbf{A}_n = 0 \\
\mathbf{x} = \sum_n \hat{c}_n \mathbf{A}_n e^{i \omega_n t} \\
\mathbf{A}_n^T (K \mathbf{A}_m) - (K \mathbf{A}_n)^T \mathbf{A}_m = (\omega_n^2 - \omega_m^2) \mathbf{A}_n^T M \mathbf{A}_m = 0 \\
\mathbf{A}_n^T M \mathbf{A}_m = \delta_{nm} \quad \mathbf{A}_n^T K \mathbf{A}_m = \delta_{nm} \omega_m^2 \\
\mathbf{x} = \sum_n q_n \mathbf{A}_n \\
\begin{aligned}{}
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
\begin{aligned}{}
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
\begin{aligned}{}
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
\begin{aligned}{}
&\tilde{A}_n e^{i \omega_n t} + \tilde{A}_{-n} e^{i \omega_n t} = 0 && \tilde{A}_{-n} = -\tilde{A}_n \\
&\tilde{A}_n e^{i \omega_n t} \left( e^{-ik_n L} - e^{ik_n L} \right) = 0 && k_n L = n \pi
\end{aligned} \\
\frac{\partial \phi}{\partial x}(0) = \frac{\partial \phi}{\partial x}(L) = 0 \\
\begin{aligned}{}
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

## Central Force Motion / 中心力運動

### Reduced Mass / 換算質量

$$
\begin{aligned}{}
\mu &= \frac{m_1 m_2}{m_1 + m_2} \\
M &= \mu r^2 \dot{\theta} \\
E &= \frac{1}{2} \mu \dot{r}^2 + \frac{1}{2}\frac{M^2}{\mu r^2} + U(r)
\end{aligned}
$$
{: .notice--info}

$$
\begin{aligned}{}
L &= \frac{1}{2} m_1 \left| \frac{m_2}{m_1 + m_2} \dot{\mathbf{r}} \right|^2 + \frac{1}{2} m_2 \left| \frac{m_1}{m_1 + m_2} \dot{\mathbf{r}} \right|^2 - U(r) \\
&= \frac{1}{2} \frac{m_1 m_2}{m_1 + m_2} (\dot{r}^2 + r^2 \dot{\theta}^2) - U(r)
\end{aligned} \\
M = \frac{\partial L}{\partial\dot{\theta}} = \mu r^2 \dot{\theta} \\
\begin{aligned}{}
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
\begin{aligned}{}
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
\begin{aligned}{}
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

### Collision / 衝突

$$
\begin{aligned}{}
\mathbf{v}_1 &= \frac{m_2 \mathbf{v}}{m_1 + m_2} + \frac{m_1 \mathbf{u}_1 + m_2 \mathbf{u}_2}{m_1 + m_2} \\
\mathbf{v}_2 &= \frac{-m_1 \mathbf{v}}{m_1 + m_2} + \frac{m_1 \mathbf{u}_1 + m_2 \mathbf{u}_2}{m_1 + m_2}
\end{aligned} \\
\begin{aligned}{}
\tan{\theta_1} &= \frac{\sin{\theta}}{\cos{\theta} + \frac{m_1}{m_2}} \\
\tan{\theta_2} &= \frac{\sin{\theta}}{\cos{\theta} - 1}
\end{aligned}
$$
{: .notice--info}

$$
m_1 \mathbf{v}_1' + m_2 \mathbf{v}_2' = 0 \\
\mathbf{v}_1' - \mathbf{v}_2' = \mathbf{v} \\
\begin{aligned}{}
\mathbf{v}_1 &= \mathbf{v}_1' + \mathbf{V} = \frac{m_2 \mathbf{v}}{m_1 + m_2} + \frac{m_1 \mathbf{u}_1 + m_2 \mathbf{u}_2}{m_1 + m_2} \\
\mathbf{v}_2 &= \mathbf{v}_2' + \mathbf{V} = \frac{-m_1 \mathbf{v}}{m_1 + m_2} + \frac{m_1 \mathbf{u}_1 + m_2 \mathbf{u}_2}{m_1 + m_2}
\end{aligned} \\
u_2 = 0 \quad u_1 = v \\
\begin{aligned}{}
\tan{\theta_1} &= \frac{m_2 \mathbf{v} \sin{\theta}}{m_2 \mathbf{v} \cos{\theta} + m_1 \mathbf{v}} = \frac{\sin{\theta}}{\cos{\theta} + \frac{m_1}{m_2}} \\
\tan{\theta_2} &= \frac{-m_1 \mathbf{v} \sin{\theta}}{-m_1 \mathbf{v} \cos{\theta} + m_1 \mathbf{v}} = \frac{\sin{\theta}}{\cos{\theta} - 1}
\end{aligned}
$$
{: .notice--primary}

### Scattering / 散乱

$$
\begin{aligned}{}
\frac{d\sigma}{d\Omega} &= \frac{R^2}{4} \\
\frac{d\sigma}{d\Omega} &= \left(\frac{\alpha}{4T}\right)^2 \frac{1}{\sin^4\frac{\theta}{2}}
\end{aligned}
$$
{: .notice--info}

$$
b = R \sin{\varphi} = R \sin{\left(\frac{\pi}{2} - \frac{\theta}{2}\right)} = R \cos{\frac{\theta}{2}} \\
\begin{aligned}{}
\frac{d\sigma}{d\Omega} &= \frac{b}{\sin{\theta}} \left| \frac{db}{d\theta} \right| \\
&= \frac{R \cos{\frac{\theta}{2}}}{2 \sin{\frac{\theta}{2}} \cos{\frac{\theta}{2}}} \cdot \frac{R}{2} \sin{\frac{\theta}{2}} \\
&= \frac{R^2}{4}
\end{aligned} \\
\frac{1}{r_\infty} + \frac{1}{p} = \frac{e}{p} \cos{\varphi} \quad \quad \cos{\varphi} = \frac{1}{e} \\
e = \sqrt{1 + \frac{2EM^2}{m \alpha^2}} = \sqrt{1 + \frac{4T^2 b^2}{\alpha^2}} \\
\tan{\varphi} = \sqrt{e^2 - 1} = \frac{2Tb}{\alpha} \\
b = \frac{\alpha}{2T} \tan{\varphi} = \frac{\alpha}{2T} \tan{\left(\frac{\pi}{2} - \frac{\theta}{2}\right)} = \frac{\alpha}{2T} \cot{\frac{\theta}{2}} \\
\begin{aligned}{}
\frac{d\sigma}{d\Omega} &= \frac{b}{\sin{\theta}} \left| \frac{db}{d\theta} \right| \\
&= \frac{\frac{\alpha}{2T} \cot{\frac{\theta}{2}}}{2 \sin{\frac{\theta}{2}} \cos{\frac{\theta}{2}}} \cdot \frac{\alpha}{4T} \frac{1}{\sin^2{\frac{\theta}{2}}} \\
&= \left(\frac{\alpha}{4T}\right)^2 \frac{1}{\sin^4{\frac{\theta}{2}}}
\end{aligned}
$$
{: .notice--primary}

### Gravity / 重力

$$
\begin{aligned}{}
\Phi &= \frac{U}{m} = -\frac{GM}{r} \\
\mathbf{g} &= -\nabla \Phi = -\frac{GM}{r^2} \hat{\mathbf{e}}_r \\
\mathbf{F} &= m\mathbf{g} = -\frac{GMm}{r^2} \hat{\mathbf{e}}_r
\end{aligned}
$$
{: .notice--info}

## Rigid Body Motion / 剛体運動

### Non-Inertial Frame / 非慣性系

$$
\begin{aligned}{}
\mathbf{r} &= \mathbf{R} + \mathbf{r}' \\
\mathbf{v} &= \mathbf{V} + \mathbf{v}' + \boldsymbol{\Omega} \times \mathbf{r}' \\
\mathbf{a} &= \mathbf{A} + \mathbf{a}' + \dot{\boldsymbol{\Omega}} \times \mathbf{r}' + \boldsymbol{\Omega} \times (\boldsymbol{\Omega} \times \mathbf{r}') + 2 \boldsymbol{\Omega} \times \mathbf{v}'
\end{aligned} 
$$
{: .notice--info}

$$
\frac{d\mathbf{Q}}{dt} = \frac{d'\mathbf{Q}}{dt} + \boldsymbol{\Omega} \times \mathbf{Q} \\
\mathbf{r} = \mathbf{R} + \mathbf{r}' \\
\begin{aligned}{}
\frac{d\mathbf{r}}{dt} &= \frac{d\mathbf{R}}{dt} + \frac{d\mathbf{r}'}{dt}  \\
&= \frac{d\mathbf{R}}{dt} + \frac{d'\mathbf{r}'}{dt} + \boldsymbol{\Omega} \times \mathbf{r}'
\end{aligned} \\
\mathbf{v} = \mathbf{V} + \mathbf{v}' + \boldsymbol{\Omega} \times \mathbf{r}' \\
\begin{aligned}{}
\frac{d\mathbf{v}}{dt} &= \frac{d\mathbf{V}}{dt} + \frac{d\mathbf{v}'}{dt} + \frac{d\boldsymbol{\Omega}}{dt} \times \mathbf{r}' + \boldsymbol{\Omega} \times \frac{d\mathbf{r}'}{dt} \\
&= \frac{d\mathbf{V}}{dt} + \frac{d'\mathbf{v}'}{dt} + \boldsymbol{\Omega}\times\mathbf{v}' + \frac{d\boldsymbol{\Omega}}{dt}  \times \mathbf{r}' + \boldsymbol{\Omega} \times \left( \frac{d'\mathbf{r}'}{dt} + \boldsymbol{\Omega} \times \mathbf{r}' \right)
\end{aligned} \\
\mathbf{a} = \mathbf{A} + \mathbf{a}' + \dot{\boldsymbol{\Omega}} \times \mathbf{r}' + \boldsymbol{\Omega} \times (\boldsymbol{\Omega} \times \mathbf{r}') + 2 \boldsymbol{\Omega} \times \mathbf{v}'
$$
{: .notice--primary}

### Euler Angle / Euler角

$$
\begin{aligned}{}
\Omega_1 &= \dot{\phi} \sin \theta \sin \psi + \dot{\theta} \cos \psi \\
\Omega_2 &= \dot{\phi} \sin \theta \cos \psi - \dot{\theta} \sin \psi \\
\Omega_3 &= \dot{\phi} \cos \theta + \dot{\psi}
\end{aligned} \\
$$
{: .notice--info}

### Inertia Tensor / 慣性テンソル

$$
\begin{aligned}{}
I_{ij} &= \sum_{\alpha} m_{\alpha} (\delta_{ij} r_{\alpha}^2 - r_{\alpha ,i} r_{\alpha ,j}) \\
T &= \sum_{i,j} \frac{1}{2} I_{ij} \Omega_i \Omega_j \\
M_i &= \sum_j I_{ij} \Omega_j
\end{aligned} 
$$
{: .notice--info}

$$
\begin{aligned}{}
T &= \sum_{\alpha} \frac{1}{2} m_{\alpha} (\boldsymbol{\Omega} \times \mathbf{r}_{\alpha}) \cdot (\boldsymbol{\Omega} \times \mathbf{r}_{\alpha}) \\
&= \sum_{\alpha} \frac{1}{2} m_{\alpha} [\Omega^2 r_{\alpha}^2 - (\boldsymbol{\Omega}\cdot\mathbf{r}_{\alpha})^2] \\
&= \sum_{i,j}\sum_{\alpha} \frac{1}{2} m_{\alpha} (\delta_{ij} r_{\alpha}^2 - r_{\alpha ,i} r_{\alpha ,j}) \Omega_i \Omega_j \\
\end{aligned} \\
\begin{aligned}{}
\mathbf{M} &= \sum_{\alpha} m_{\alpha} \mathbf{r}_{\alpha} \times (\mathbf{\Omega} \times \mathbf{r}_{\alpha}) \\
&= \sum_{\alpha} m_{\alpha} [\mathbf{\Omega} (r_{\alpha}^2) - \mathbf{r}_{\alpha} (\mathbf{r}_{\alpha} \cdot \Omega)] \\
M_i &= \sum_j \sum_{\alpha} m_{\alpha} (\delta_{ij} r_{\alpha}^2 - r_{\alpha ,i} r_{\alpha ,j}) \Omega_j
\end{aligned}
$$
{: .notice--primary}

### Euler's Equation / Eulerの運動方程式

$$
\begin{aligned}{}
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
\begin{aligned}{}
\theta &= \text{const.} \\
\dot{\phi} &= \frac{M_z}{I_1} \\
\dot{\psi} &= M_z \cos \theta \left( \frac{1}{I_3} - \frac{1}{I_1} \right)
\end{aligned}
$$
{: .notice--info}

$$
L = \frac{1}{2} I_1 (\dot{\phi}^2 \sin^2 \theta + \dot{\theta}^2) + \frac{1}{2} I_3 (\dot{\phi} \cos \theta + \dot{\psi})^2 \\
\begin{aligned}{}
\frac{\partial L}{\partial \dot{\psi}} &= I_3 (\dot{\phi} \cos \theta + \dot{\psi}) = M_3 = M_z \cos \theta \\
\frac{\partial L}{\partial \dot{\phi}} &= I_1 \dot{\phi} \sin^2 \theta + I_3 (\dot{\phi} \cos \theta + \dot{\psi}) \cos \theta = M_z
\end{aligned} \\
\begin{aligned}{}
\dot{\phi} &= \frac{M_z - M_z \cos^2 \theta}{I_1 \sin^2 \theta} = \frac{M_z}{I_1} \\
\dot{\psi} &= \frac{M_z \cos \theta}{I_3} - \dot{\phi} \cos \theta = M_z \cos \theta \left( \frac{1}{I_3} - \frac{1}{I_1} \right)
\end{aligned} \\
\begin{aligned}{}
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
\begin{aligned}{}
\theta_1 &\leq \theta \leq \theta_2 \\
\dot{\phi}& = \frac{M_z - M_3 \cos \theta}{(I_1 + Ma^2) \sin^2 \theta} \\
\dot{\psi} &= \frac{M_3}{I_3} - \frac{(M_z - M_3 \cos \theta) \cos \theta}{(I_1 + Ma^2) \sin^2 \theta}
\end{aligned}
$$
{: .notice--info}

$$
L = \frac{1}{2} (I_1 + Ma^2) (\dot{\phi}^2 \sin^2 \theta + \dot{\theta}^2) + \frac{1}{2} I_3 (\dot{\phi} \cos \theta + \dot{\psi})^2 - Mga \cos \theta \\
\begin{aligned}{}
\frac{\partial L}{\partial \dot{\psi}} &= I_3 (\dot{\phi} \cos \theta + \dot{\psi}) = M_3 \\
\frac{\partial L}{\partial \dot{\phi}} &= (I_1 + Ma^2) \dot{\phi} \sin^2 \theta + I_3 (\dot{\phi} \cos \theta + \dot{\psi}) \cos \theta = M_z
\end{aligned} \\
\begin{aligned}{}
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
\begin{aligned}{}
\Omega_1 : \quad \lambda^2 &=  \frac{-\Omega_1^2(I_3 - I_1)(I_2 - I_1)}{I_2 I_3} < 0, &&\text{stable} \\
\Omega_2 : \quad \lambda^2 &=  \frac{\Omega_2^2(I_3 - I_2)(I_2 - I_1)}{I_1 I_3} > 0,  &&\text{unstable} \\
\Omega_3 : \quad \lambda^2 &=  \frac{-\Omega_3^2(I_3 - I_2)(I_3 - I_1)}{I_1 I_2} < 0,  &&\text{stable}
\end{aligned}
$$
{: .notice--primary}

## Continuum Mechanics / 連続体力学

### Fundamental Equation / 基礎方程式

$$
\frac{DQ}{Dt} = \frac{\partial Q}{\partial t} + \mathbf{v} \cdot \nabla Q \\
\frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \mathbf{v}) = 0 \\
\rho \frac{D \mathbf{v}}{Dt} = \mathbf{f} + \nabla \cdot \sigma
$$
{: .notice--info}

$$
\frac{d}{dt} \int_V \rho \, dV = \int_V \frac{\partial \rho}{\partial t} \, dV = -\oint_{\partial V} \rho \mathbf{v} \cdot d\mathbf{S} = -\int_V \nabla \cdot (\rho \mathbf{v}) \, dV \\
\frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \mathbf{v}) = 0 \\
\begin{aligned}{}
\frac{d}{dt} \int_V \rho v_i \, dV &= \int_V \frac{\partial (\rho v_i)}{\partial t} \, dV \\
&= - \oint_{\partial V} \rho v_i \mathbf{v} \cdot d\mathbf{S} + \int_V f_i \, dV + \oint_{\partial V} \boldsymbol{\sigma}_i \cdot d\mathbf{S} \\
&= - \int_V \nabla \cdot (\rho v_i \mathbf{v}) \, dV + \int_V f_i \, dV + \int_V \nabla \cdot \boldsymbol{\sigma}_i \, dV
\end{aligned} \\
\begin{aligned}{}
\frac{\partial (\rho v_i)}{\partial t} + \nabla \cdot (\rho v_i \mathbf{v}) &= \frac{\partial \rho}{\partial t} v_i + \rho \frac{\partial v_i}{\partial t} + (\nabla \cdot \rho \mathbf{v}) v_i + \rho (\mathbf{v} \cdot \nabla) v_i \\
&= \rho \left( \frac{\partial v_i}{\partial t} + (\mathbf{v} \cdot \nabla) v_i \right) + \left( \frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \mathbf{v}) \right) v_i \\
&= f_i + \nabla \cdot \boldsymbol{\sigma}_i
\end{aligned} \\
\rho \frac{D \mathbf{v}}{Dt} = \mathbf{f} + \nabla \cdot \sigma
$$
{: .notice--primary}

### Elastic Body / 弾性体

$$
E_{ij} = \frac{1}{2} \left( \frac{\partial r_j}{\partial x_i} + \frac{\partial r_i}{\partial x_k} \right) \\
{\sigma}_{ij} = \lambda \delta_{ij} E_{kk} + 2 \mu E_{ij} \\
\rho \frac{D \mathbf{v}}{Dt} = \mathbf{f} + (\lambda + \mu) \nabla (\nabla \cdot \mathbf{r}) + \mu \nabla^2 \mathbf{r}
$$
{: .notice--info}

$$
\begin{aligned}{}
\rho \frac{Dv_i}{Dt} &= f_i + \frac{\partial {\sigma}_{ij}}{\partial x_j} \\
&= f_i + \lambda \frac{\partial}{\partial x_i} \left( \frac{\partial r_k}{\partial x_k} \right) + \mu \frac{\partial}{\partial x_j} \left( \frac{\partial r_j}{\partial x_i} + \frac{\partial r_i}{\partial x_j} \right) \\
&= f_i + (\lambda + \mu) \frac{\partial}{\partial x_i} (\nabla \cdot \mathbf{r}) + \mu \nabla^2 r_i
\end{aligned}
$$
{: .notice--primary}

### Fluid / 流体

$$
\dot{E}_{ij} = \frac{1}{2} \left( \frac{\partial v_j}{\partial x_i} + \frac{\partial v_i}{\partial x_j} \right) \\
{\sigma}_{ij} = - p \delta_{ij} + \lambda \delta_{ij} \dot{E}_{kk} + 2 \eta \dot{E}_{ij} \\
\rho \frac{D \mathbf{v}}{Dt} = \mathbf{f} - \nabla p + (\lambda + \eta) \nabla (\nabla \cdot \mathbf{v}) + \eta {\nabla}^2 \mathbf{v}
$$
{: .notice--info}

$$
\begin{aligned}{}
\rho \frac{D v_i}{Dt} &= f_i + \frac{\partial {\sigma}_{ij}}{\partial x_j} \\
&= f_i - \frac{\partial p}{\partial x_i} + \lambda \frac{\partial}{\partial x_i} \left( \frac{\partial v_k}{\partial x_k} \right) + \eta \frac{\partial}{\partial x_j} \left( \frac{\partial v_j}{\partial x_i} + \frac{\partial v_i}{\partial x_j} \right) \\
&= f_i - \frac{\partial p}{\partial x_i} + (\lambda + \eta) \frac{\partial}{\partial x_i} (\nabla \cdot \mathbf{v}) + \eta {\nabla}^2 v_i
\end{aligned}
$$
{: .notice--primary}

### Bernoulli's Principle / Bernoulliの定理

$$
\rho \mathbf{v} \cdot \mathbf{s} = \text{const.} \\
p + \frac{1}{2} \rho v^2 + \rho gz = \text{const.}
$$
{: .notice--info}

$$
\lambda = \eta = 0 \quad \frac{\partial \rho}{\partial t} = \frac{\partial \mathbf{v}}{\partial t} = 0 \\
\begin{aligned}{}
\int_{V} \frac{\partial \rho}{\partial t} \, dV &= \int_{V} \nabla \cdot (\rho \mathbf{v}) \, dV \\
&= \oint_{\partial V} \rho \mathbf{v} \cdot d\mathbf{S} \\
&= \int_{S_1} \rho \mathbf{v} \cdot d\mathbf{S} - \int_{S_2} \rho \mathbf{v} \cdot d\mathbf{S} = 0
\end{aligned} \\
\rho \mathbf{v} \cdot \mathbf{s} = \text{const.} \\
\begin{aligned}{}
\rho \frac{D\mathbf{v}}{Dt} &= \rho \left( \mathbf{v} \cdot \nabla \right) \mathbf{v} \\
&= \rho \nabla \left(\frac{v^2}{2}\right) - \rho \nabla \times \left( \nabla \times \mathbf{v} \right) \\
&= -\nabla \left( \rho gz \right) - \nabla p
\end{aligned} \\
\nabla \left( p + \frac{1}{2} \rho v^2 + \rho gz \right) = \rho \mathbf{v} \times \left( \nabla \times \mathbf{v} \right) \\
\mathbf{v} \cdot \nabla \left( p + \frac{1}{2} \rho v^2 + \rho gz \right) = 0 \\
p + \frac{1}{2} \rho v^2 + \rho gz = \text{const.}
$$
{: .notice--primary}

## Special Relativity / 特殊相対性理論

### Lorentz Transformation / Lorentz変換

$$
c^2 dt^2 - dx^2 - dy^2 - dz^2 = \text{const.} \\
X' = LX \\
L = \begin{pmatrix}
\frac{1}{\sqrt{1 - \frac{v^2}{c^2}}} & \frac{-\frac{v}{c}}{\sqrt{1 - \frac{v^2}{c^2}}} & 0 & 0 \\
\frac{-\frac{v}{c}}{\sqrt{1 - \frac{v^2}{c^2}}} & \frac{1}{\sqrt{1 - \frac{v^2}{c^2}}} & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix} \quad
X = \begin{pmatrix}
ct \\
x \\
y \\
z
\end{pmatrix}
$$
{: .notice--info}

$$
g = \begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & -1 & 0 & 0 \\
0 & 0 & -1 & 0 \\
0 & 0 & 0 & -1
\end{pmatrix} \quad 
X = \begin{pmatrix}
ct \\
x \\
y \\
z
\end{pmatrix} \\
(dX)^T g (dX) = const. \\
(dX')^T g (dX') = (L dX)^T g (L dX) = (dX)^T g (dX) \\
L^T g L = g \\
L = \begin{pmatrix}
\cosh \omega & \sinh \omega & 0 & 0 \\
\sinh \omega & \cosh \omega & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix} \\
\begin{pmatrix}
ct' \\
0 \\
0 \\
0
\end{pmatrix}
= \begin{pmatrix}
\cosh \omega & \sinh \omega & 0 & 0 \\
\sinh \omega & \cosh \omega & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}
\begin{pmatrix}
ct \\
vt \\
0 \\
0
\end{pmatrix} \\
\tanh \omega = -\frac{v}{c} \quad \cosh \omega = \frac{1}{\sqrt{1 - \frac{v^2}{c^2}}} \quad \sinh \omega = \frac{-\frac{v}{c}}{\sqrt{1 - \frac{v^2}{c^2}}}
$$
{: .notice--primary}

### Consequence of Transformation / 変換の帰結

$$
\begin{aligned}{}
\tau &= \frac{\tau_0}{\sqrt{1 - \frac{v^2}{c^2}}} \\
\ell &= \ell_0 \sqrt{1 - \frac{v^2}{c^2}} \\
v_x &= \frac{v_x' + v}{1 + \frac{v}{c^2} v_x'} \\
v_y &= \frac{\sqrt{1 - \frac{v^2}{c^2}} v_y'}{1 + \frac{v}{c^2} v_x'}
\end{aligned}
$$
{: .notice--info}

$$
\Delta x' = 0 \quad \Delta t' = \tau_0 \\
\Delta t = \frac{\Delta t' - \frac{v}{c^2} \Delta x'}{\sqrt{1 - \frac{v^2}{c^2}}} = \frac{\Delta t'}{\sqrt{1 - \frac{v^2}{c^2}}} \\
\Delta t = 0 \quad \Delta x' = \ell_0 \\
\Delta x' = \frac{\Delta x - v \Delta t}{\sqrt{1 - \frac{v^2}{c^2}}} = \frac{\Delta x}{\sqrt{1 - \frac{v^2}{c^2}}} \\
v_x = \frac{dx}{dt} = \frac{dx' + v dt'}{dt' + \frac{v}{c^2} dx'} = \frac{v_x' + v}{1 + \frac{v}{c^2} v_x'} \\
v_y = \frac{dy}{dt} = \frac{\sqrt{1 - \frac{v^2}{c^2}} \, dy'}{dt' + \frac{v}{c^2} dx'} = \frac{\sqrt{1 - \frac{v^2}{c^2}} v_y'}{1 + \frac{v}{c^2} v_x'}
$$
{: .notice--primary}

### Relativistic Dynamics / 相対論的力学

$$
\delta S = \delta \int -mc \sqrt{c^2 dt^2 - dx^2 - dy^2 - dz^2} = 0 \\
\begin{aligned}{}
\mathbf{p} &= \frac{m\mathbf{v}}{\sqrt{1 - \frac{v^2}{c^2}}} \\
E &= \frac{mc^2}{\sqrt{1 - \frac{v^2}{c^2}}} = \sqrt{p^2 c^2 + m^2 c^4}
\end{aligned}
$$
{: .notice--info}

$$
\begin{aligned}{}
S &= \int -mc \sqrt{c^2 dt^2 - dx^2 - dy^2 - dz^2} \\
&= \int -mc^2 \sqrt{1 - \frac{v^2}{c^2}} \, dt 
\end{aligned} \\
L = -mc^2 \sqrt{1 - \frac{v^2}{c^2}} \\
\mathbf{p} = \frac{\partial L}{\partial \mathbf{v}} = \frac{m\mathbf{v}}{\sqrt{1 - \frac{v^2}{c^2}}} \\
\begin{aligned}{}
E &= \mathbf{p} \cdot \mathbf{v} - L \\
&= \frac{m v^2}{\sqrt{1 - \frac{v^2}{c^2}}} + mc^2 \sqrt{1 - \frac{v^2}{c^2}} \\
&= \frac{mc^2}{\sqrt{1 - \frac{v^2}{c^2}}}
\end{aligned} \\
p^2 c^2 + m^2 c^4 = \frac{m^2 v^2 c^2}{1 - \frac{v^2}{c^2}} + \frac{m^2 c^4 - m^2 c^2 v^2}{1 - \frac{v^2}{c^2}} = E^2
$$
{: .notice--primary}

### Four-Vector / ４元ベクトル

$$
\mathbf{A'} = L \mathbf{A} \\
\begin{aligned}{}
\mathbf{X} &= (ct, x, y, z) \\
\mathbf{V} &= (\frac{c}{\sqrt{1 - \frac{v^2}{c^2}}}, \frac{v_x}{\sqrt{1 - \frac{v^2}{c^2}}}, \frac{v_y}{\sqrt{1 - \frac{v^2}{c^2}}}, \frac{v_z}{\sqrt{1 - \frac{v^2}{c^2}}}) \\
\mathbf{P} &= (\frac{E}{c}, p_x, p_y, p_z)
\end{aligned} 
$$
{: .notice--info}

$$
\begin{aligned}{}
d\mathbf{X} &= (cdt, dx, dy, dz) \\
d\tau &= \sqrt{dt^2 - \frac{dx^2 + dy^2 + dz^2}{c^2}} = dt \sqrt{1 - \frac{v^2}{c^2}} = \text{const.}
\end{aligned} \\
\begin{aligned}{}
\mathbf{V} &= \frac{d\mathbf{X}}{d\tau} = (\frac{c}{\sqrt{1 - \frac{v^2}{c^2}}}, \frac{v_x}{\sqrt{1 - \frac{v^2}{c^2}}}, \frac{v_y}{\sqrt{1 - \frac{v^2}{c^2}}}, \frac{v_z}{\sqrt{1 - \frac{v^2}{c^2}}}) \\
\mathbf{P} &= m\mathbf{V} = (\frac{E}{c}, p_x, p_y, p_z)
\end{aligned} 
$$
{: .notice--primary}

# Electromagnetism / 電磁気学

## Maxwell's Equation / Maxwell方程式

### Charge and Current / 電荷と電流

$$
\rho = \frac{dq}{d\tau} \quad \mathbf{J} = \rho \mathbf{v} \\
\frac{\partial \rho}{\partial t} = -\nabla \cdot \mathbf{J}
$$
{: .notice--info}

$$
\begin{aligned}{}
\frac{d q}{d t} &= \frac{d}{d t} \int_V \rho \, d\tau = \int_V \left(\frac{\partial \rho}{\partial t}\right) d\tau \\
&= -\oint_S \mathbf{J} \cdot d\mathbf{a} = \int_V (-\nabla \cdot \mathbf{J}) \, d\tau \\
\end{aligned}
$$
{: .notice--primary}

### Electromagnetic Field / 電磁場

$$
\begin{aligned}{}
& \nabla \cdot \mathbf{E} = \frac{1}{\varepsilon_0} \rho \\
& \nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t} \\
& \nabla \cdot \mathbf{B} = 0 \\
& \nabla \times \mathbf{B} = \mu_0 \mathbf{J} + \mu_0 \varepsilon_0 \frac{\partial \mathbf{E}}{\partial t} 
\end{aligned} \\
\mathbf{F} = q\mathbf{E} + q\mathbf{v} \times \mathbf{B}
$$
{: .notice--info}

### Electromagnetic Potential / 電磁ポテンシャル

$$
\begin{aligned}{}
\mathbf{E} &= -\nabla V - \frac{\partial \mathbf{A}}{\partial t} \\
\mathbf{B} &= \nabla \times \mathbf{A}
\end{aligned} \\
\begin{aligned}{}
\nabla^2 V - \mu_0 \varepsilon_0 \frac{\partial V}{\partial t} &= -\frac{1}{\varepsilon_0} \rho \\
\nabla^2 \mathbf{A} - \mu_0 \varepsilon_0 \frac{\partial \mathbf{A}}{\partial t} &= -\mu_0 \mathbf{J}
\end{aligned} \\
\frac{d}{d t}(\mathbf{p} + q \mathbf{A}) = -\nabla (q V - q \mathbf{v} \cdot \mathbf{A})
$$
{: .notice--info}

$$
\nabla \cdot \mathbf{B} = 0 \\
\mathbf{B} = \nabla \times \mathbf{A} \\
\nabla \times \mathbf{E} + \frac{\partial \mathbf{B}}{\partial t} = \nabla \times \left(\mathbf{E} + \frac{\partial \mathbf{A}}{\partial t}\right) = 0 \\
\mathbf{E} + \frac{\partial \mathbf{A}}{\partial t} = -\nabla V \\
\nabla \cdot \mathbf{E} = -\nabla^2 V - \nabla \cdot \left(\frac{\partial \mathbf{A}}{\partial t}\right) = \frac{1}{\varepsilon_0} \rho \\
\nabla^2 V + \frac{\partial}{\partial t}(\nabla \cdot \mathbf{A}) = -\frac{1}{\varepsilon_0} \rho \\
\nabla \times \mathbf{B} - \mu_0 \varepsilon_0 \frac{\partial \mathbf{E}}{\partial t} = \nabla \times (\nabla \times \mathbf{A}) + \mu_0 \varepsilon_0 \frac{\partial}{\partial t} \left(\nabla V\right) + \mu_0 \varepsilon_0 \frac{\partial^2 \mathbf{A}}{\partial t^2} = \mu_0 \mathbf{J} \\
\left(\nabla^2 \mathbf{A} - \mu_0 \varepsilon_0 \frac{\partial^2 \mathbf{A}}{\partial t^2}\right) - \nabla \left(\nabla \cdot \mathbf{A} + \mu_0 \varepsilon_0 \frac{\partial V}{\partial t}\right) = -\mu_0 \mathbf{J} \\
\mathbf{A}' = \mathbf{A} + \nabla \lambda \quad V' = V - \frac{\partial \lambda}{\partial t} \\
\mathbf{B}' = \nabla \times \mathbf{A}' + \nabla \times \nabla \lambda = \nabla \times \mathbf{A} = \mathbf{B} \\
\mathbf{E}' = -\nabla V + \nabla \left(\frac{\partial \lambda}{\partial t}\right) - \frac{\partial \mathbf{A}}{\partial t} - \frac{\partial}{\partial t}(\nabla \lambda) = -\nabla V - \frac{\partial \mathbf{A}}{\partial t} = \mathbf{E} \\
\nabla^2 \lambda - \mu_0 \varepsilon_0 \frac{\partial^2 \lambda}{\partial t^2} = -\nabla \cdot \mathbf{A} - \mu_0 \varepsilon_0 \frac{\partial V}{\partial t} \\
\nabla \cdot (\mathbf{A} + \nabla \lambda) = -\mu_0 \varepsilon_0 \frac{\partial}{\partial t}\left(V - \frac{\partial \lambda}{\partial t}\right) \\
\nabla \cdot \mathbf{A}' = -\mu_0 \varepsilon_0 \frac{\partial V'}{\partial t} \\
\begin{aligned}{}
\nabla^2 V - \mu_0 \varepsilon_0 \frac{\partial V}{\partial t} &= -\frac{1}{\varepsilon_0} \rho \\
\nabla^2 \mathbf{A} - \mu_0 \varepsilon_0 \frac{\partial \mathbf{A}}{\partial t} &= -\mu_0 \mathbf{J}
\end{aligned} \\
\begin{aligned}{}
\mathbf{F} = \frac{d \mathbf{p}}{d t} &= q(\mathbf{E} + \mathbf{v} \times \mathbf{B}) \\
&= q \left[-\nabla V - \frac{\partial \mathbf{A}}{\partial t} + \mathbf{v} \times (\nabla \times \mathbf{A})\right] \\
&= q \left[-\frac{\partial \mathbf{A}}{\partial t} - (\mathbf{v} \cdot \nabla)\mathbf{A} - \nabla V + \nabla(\mathbf{v} \cdot \mathbf{A})\right] \\
&= q \left[-\frac{d \mathbf{A}}{d t} - \nabla(V - \mathbf{v} \cdot \mathbf{A})\right]
\end{aligned} \\
\frac{d}{d t}(\mathbf{p} + q \mathbf{A}) = -\nabla(q V - q \mathbf{v} \cdot \mathbf{A})
$$
{: .notice--primary}

### Energy Conservation / エネルギー保存

$$
E_{\text{em}} = \int_V \left(\frac{\varepsilon_0}{2} E^2 + \frac{1}{2\mu_0} B^2\right) d\tau \\
\mathbf{S} = \frac{1}{\mu_0} \mathbf{E} \times \mathbf{B} \\
\frac{d}{dt}(E_{\text{mech}} + E_{\text{em}}) = -\oint_S \mathbf{S} \cdot d\mathbf{a}
$$
{: .notice--info}

$$
\mathbf{F} \cdot d\mathbf{l} = q(\mathbf{E} + \mathbf{v} \times \mathbf{B}) \cdot \mathbf{v} \,dt = \mathbf{E} \cdot (q\mathbf{v}) \,dt \\
\frac{dE_{\text{mech}}}{dt} = \int_V \mathbf{E} \cdot \mathbf{J} \, d\tau \\
\begin{aligned}{}
\mathbf{E} \cdot \mathbf{J} &= \frac{1}{\mu_0} \mathbf{E} \cdot (\nabla \times \mathbf{B}) - \varepsilon_0 \mathbf{E} \cdot \frac{\partial \mathbf{E}}{\partial t} \\
&= \frac{1}{\mu_0} [\mathbf{B} \cdot (\nabla \times \mathbf{E}) - \nabla \cdot (\mathbf{E} \times \mathbf{B})] - \varepsilon_0 \mathbf{E} \cdot \frac{\partial \mathbf{E}}{\partial t} \\
&= -\varepsilon_0 \mathbf{E} \cdot \frac{\partial \mathbf{E}}{\partial t} - \frac{1}{\mu_0} \mathbf{B} \cdot \frac{\partial \mathbf{B}}{\partial t} - \frac{1}{\mu_0} \nabla \cdot (\mathbf{E} \times \mathbf{B}) \\
&= -\frac{\partial}{\partial t}\left(\frac{\varepsilon_0}{2} E^2 + \frac{1}{2\mu_0} B^2\right) - \frac{1}{\mu_0} \nabla \cdot (\mathbf{E} \times \mathbf{B}) \\
\end{aligned} \\
\begin{aligned}{}
\frac{dE_{\text{mech}}}{dt} &= - \int_V \frac{\partial}{\partial t} \left(\frac{\varepsilon_0}{2} E^2 + \frac{1}{2\mu_0} B^2\right) d\tau - \int_V \frac{1}{\mu_0} \nabla \cdot (\mathbf{E} \times \mathbf{B}) d\tau \\
&= -\frac{d}{d t} \int_V \left(\frac{\varepsilon_0}{2} E^2 + \frac{1}{2\mu_0} B^2\right) d\tau - \oint_S \frac{1}{\mu_0} (\mathbf{E} \times \mathbf{B}) \cdot d\mathbf{a} \\
&= -\frac{dE_{\text{em}}}{dt} - \oint_S \mathbf{S} \cdot d\mathbf{a}
\end{aligned}
$$
{: .notice--primary}

### Momentum Conservation / 運動量保存

$$
\mathbf{P}_{\text{em}} = \int_V \varepsilon_0 \mathbf{E} \times \mathbf{B} \, d\tau \\
T_{ij} = \varepsilon_0\left(E_i E_j - \frac{1}{2} \delta_{ij} E^2\right) + \frac{1}{\mu_0}\left(B_i B_j - \frac{1}{2} \delta_{ij} B^2\right) \\
\frac{d}{dt}(\mathbf{P}_{\text{mech}} + \mathbf{P}_{\text{em}}) = \oint_S \mathbf{T} \cdot d\mathbf{a}
$$
{: .notice--info}

$$
\mathbf{F} = q\mathbf{E} + q\mathbf{v} \times \mathbf{B} \\
\frac{d\mathbf{P}_{\text{mech}}}{dt} = \int_V (\rho\mathbf{E} + \mathbf{J} \times \mathbf{B}) \, d\tau \\
\begin{aligned}{}
& \rho\mathbf{E} + \mathbf{J} \times \mathbf{B} \\
=& \varepsilon_0(\nabla \cdot \mathbf{E})\mathbf{E} + \left(\frac{1}{\mu_0}\nabla \times \mathbf{B} - \varepsilon_0 \frac{\partial \mathbf{E}}{\partial t}\right) \times \mathbf{B} \\
=& \varepsilon_0(\nabla \cdot \mathbf{E})\mathbf{E} - \frac{1}{\mu_0} \mathbf{B} \times (\nabla \times \mathbf{B}) - \varepsilon_0 \mathbf{E} \times (\nabla \times \mathbf{E}) - \varepsilon_0 \frac{\partial}{\partial t} (\mathbf{E} \times \mathbf{B}) \\
=& \varepsilon_0(\nabla \cdot \mathbf{E})\mathbf{E} - \frac{1}{2\mu_0} \nabla(B^2) + \frac{1}{\mu_0} (\mathbf{B} \cdot \nabla)\mathbf{B} \\
&- \frac{\varepsilon_0}{2}\nabla(E^2) + \varepsilon_0(\mathbf{E} \cdot \nabla)\mathbf{E} - \varepsilon_0 \frac{\partial}{\partial t} (\mathbf{E} \times \mathbf{B}) \\
=& \varepsilon_0\left[(\nabla \cdot \mathbf{E})\mathbf{E} + (\mathbf{E} \cdot \nabla)\mathbf{E}\right] + \frac{1}{\mu_0}\left[(\nabla \cdot \mathbf{B})\mathbf{B} + (\mathbf{B} \cdot \nabla)\mathbf{B}\right] \\
&- \nabla\left(\frac{\varepsilon_0}{2} E^2 + \frac{1}{2\mu_0} B^2\right) - \varepsilon_0 \frac{\partial}{\partial t} (\mathbf{E} \times \mathbf{B}) \\
=& \nabla \cdot \overleftrightarrow{T} - \frac{\partial}{\partial t} (\varepsilon_0 \mathbf{E} \times \mathbf{B}) \\
\end{aligned} \\
\begin{aligned}{}
\frac{d\mathbf{P}_{\text{mech}}}{dt} &= - \int_V \frac{\partial}{\partial t} (\varepsilon_0 \mathbf{E} \times \mathbf{B}) d\tau + \int_V \nabla \cdot \overleftrightarrow{T} d\tau \\
&= -\frac{d}{d t} \int_V \varepsilon_0 \mathbf{E} \times \mathbf{B} d\tau + \oint_S \overleftrightarrow{T} \cdot d\mathbf{a} \\
&= -\frac{d\mathbf{P}_{\text{em}}}{dt} + \oint_S \overleftrightarrow{T} \cdot d\mathbf{a}
\end{aligned}
$$
{: .notice--primary}

## Electrostatics / 静電場

### Electric Field / 電場

$$
\begin{aligned}{}
& \nabla \cdot \mathbf{E} = \frac{1}{\varepsilon_0} \rho && \oint_S \mathbf{E} \cdot d\mathbf{a} = \frac{1}{\varepsilon_0} Q \\
& \nabla \times \mathbf{E} = 0 && \oint_C \mathbf{E} \cdot d\mathbf{l} = 0 \\
\end{aligned} \\
\mathbf{E}(\mathbf{r}) = \frac{1}{4\pi\varepsilon_0} \int_V \frac{\rho(\mathbf{r}')\hat{\mathbf{\vec{r}}}}{\vec{r}^2} \, d\tau'
$$
{: .notice--info}

$$
\begin{aligned}{}
\nabla \cdot \mathbf{E}(\mathbf{r}) &= \frac{1}{4\pi\varepsilon_0} \int_V \nabla \cdot \left(\frac{\hat{\mathbf{\vec{r}}}}{\vec{r}^2}\right) \rho(\mathbf{r}') \, d\tau' \\
&= \frac{1}{4\pi\varepsilon_0} \int_V 4\pi\delta^3(\mathbf{r}-\mathbf{r}') \rho(\mathbf{r}') \, d\tau' \\
&= \frac{1}{\varepsilon_0} \rho(\mathbf{r})
\end{aligned} \\
\begin{aligned}{}
\nabla \times \mathbf{E}(\mathbf{r}) &= \frac{1}{4\pi\varepsilon_0} \int_V \nabla \times \left(\frac{\hat{\mathbf{\vec{r}}}}{\vec{r}^2}\right) \rho(\mathbf{r}') \, d\tau' \\
&= 0
\end{aligned}
$$
{: .notice--primary}

### Electric Potential / 電位

$$
\mathbf{E} = -\nabla V \\
\nabla^2 V = -\frac{1}{\varepsilon_0} \rho \\
V(\mathbf{r}) = \frac{1}{4\pi\varepsilon_0} \int_V \frac{\rho(\mathbf{r}')}{\vec{r}} d\tau'
$$
{: .notice--info}

$$
\nabla \times \mathbf{E} = -\nabla \times \nabla V = 0 \\
\nabla \cdot \mathbf{E} = -\nabla^2 V = \frac{1}{\varepsilon_0} \rho \\
\begin{aligned}{}
\nabla^2 V(\mathbf{r}) &= \frac{1}{4\pi\varepsilon_0} \int_V \nabla^2 \left(\frac{1}{\vec{r}}\right) \rho(\mathbf{r}') d\tau' \\
&= \frac{1}{4\pi\varepsilon_0} \int_V -4\pi \delta^3(\mathbf{r}-\mathbf{r}') \rho(\mathbf{r}') d\tau' \\
&= -\frac{1}{\varepsilon_0} \rho(\mathbf{r})
\end{aligned}
$$
{: .notice--primary}

### Electric Energy / 電気エネルギー

$$
\begin{aligned}{}
\Delta W &= q \Delta V \\
W &= \frac{1}{2} \int_V \rho V \, d\tau \\
W &= \frac{\varepsilon_0}{2} \int_V E^2 \, d\tau
\end{aligned}
$$
{: .notice--info}

$$
\Delta W = \int_a^b \mathbf{F} \cdot d\mathbf{l} = \int_a^b q\mathbf{E} \cdot d\mathbf{l} = q \Delta V \\
\begin{aligned}{}
W &= \sum_i \sum_{j<i} q_i V_{ij} \\
&= \frac{1}{2} \sum_i \sum_{j \neq i} q_i V_{ij} \\
&= \frac{1}{2} \sum_i q_i V_i \\
&= \frac{1}{2} \int_V \rho V \, d\tau \\
&= \frac{\varepsilon_0}{2} \int_V (\nabla \cdot \mathbf{E}) V \, d\tau \\
&= \frac{\varepsilon_0}{2} \left[ \oint_S (\mathbf{E}V) \cdot d\mathbf{a} - \int_V \mathbf{E} \cdot (\nabla V) \, d\tau \right] \\
&= \frac{\varepsilon_0}{2} \int_V E^2 \, d\tau
\end{aligned}
$$
{: .notice--primary}

### Electric Dipole / 電気双極子

$$
V(\mathbf{r}) = \frac{1}{4\pi\varepsilon_0} \sum_{n=0}^{\infty} \frac{1}{r^{n+1}} \int_V (r')^n P_n(\cos\alpha) \rho(\mathbf{r}') d\tau' \\
p = qd \\
V_{\text{dip}} = \frac{1}{4\pi\varepsilon_0} \frac{p\cos\theta}{r^2} \\
\mathbf{E}_{\text{dip}} = \frac{1}{4\pi\varepsilon_0} \frac{p(2\cos\theta \,\hat{\mathbf{r}} + \sin\theta \,\hat{\boldsymbol{\theta}})}{r^3}
$$
{: .notice--info}

$$
\frac{1}{\vec{r}} = \frac{1}{\sqrt{r^2 + (r')^2 - 2rr'\cos\alpha}} = \frac{1}{r} \sum_{n=0}^{\infty} \left(\frac{r'}{r}\right)^n P_n(\cos\alpha) \\
\begin{aligned}{}
V(\mathbf{r}) &= \frac{1}{4\pi\varepsilon_0} \int_V \frac{\rho(\mathbf{r}')}{\vec{r}} d\tau' \\
&= \frac{1}{4\pi\varepsilon_0} \int_V \sum_{n=0}^{\infty} \frac{(r')^n}{r^{n+1}} P_n(\cos\alpha) \rho(\mathbf{r}') d\tau' \\
&= \frac{1}{4\pi\varepsilon_0} \sum_{n=0}^{\infty} \frac{1}{r^{n+1}} \int_V (r')^n P_n(\cos\alpha) \rho(\mathbf{r}') d\tau'
\end{aligned} \\
\begin{aligned}{}
V_{\text{dip}} &= \frac{1}{4\pi\varepsilon_0} \frac{1}{r^2} \int_V r' (\cos\alpha) \rho(\mathbf{r}') d\tau' \\
&= \frac{1}{4\pi\varepsilon_0} \frac{1}{r^2} \int_V (\mathbf{r}' \cdot \hat{\mathbf{r}}) \rho(\mathbf{r}') d\tau' \\
&= \frac{1}{4\pi\varepsilon_0} \frac{q \mathbf{d} \cdot \hat{\mathbf{r}}}{r^2} \\
&= \frac{1}{4\pi\varepsilon_0} \frac{qd\cos\theta}{r^2}
\end{aligned} \\
\begin{aligned}{}
\mathbf{E}_{\text{dip}} &= -\nabla V_{\text{dip}} \\
&= \frac{1}{4\pi\varepsilon_0} \frac{qd(2\cos\theta \,\hat{\mathbf{r}} + \sin\theta \,\hat{\boldsymbol{\theta}})}{r^3}
\end{aligned}
$$
{: .notice--primary}

### Uniqueness Theorem / 一意性定理

$$
\begin{aligned}{}
&\rho_1^{\text{volume}} = \rho_2^{\text{volume}}, && V_1^{\text{boundary}} = V_2^{\text{boundary}} \rightarrow &&V_1^{\text{volume}} = V_2^{\text{volume}} \\
& \rho_1^{\text{volume}} = \rho_2^{\text{volume}}, && Q_1^{\text{boundary}} = Q_2^{\text{boundary}} \rightarrow &&\mathbf{E}_1^{\text{volume}} = \mathbf{E}_2^{\text{volume}}
\end{aligned}
$$
{: .notice--info}

$$
\nabla^2 V_3 = \nabla^2 V_1 - \nabla^2 V_2 = -\frac{\rho_1}{\varepsilon_0} + \frac{\rho_2}{\varepsilon_0} = 0 \\
V_3^\Sigma = V_1^\Sigma - V_2^\Sigma = 0 \\
V_3 = 0 \rightarrow V_1 = V_2 \\
\nabla \cdot \mathbf{E}_3 = \nabla \cdot \mathbf{E}_1 - \nabla \cdot \mathbf{E}_2 = \frac{\rho_1}{\varepsilon_0} - \frac{\rho_2}{\varepsilon_0} = 0 \\
\oint_S \mathbf{E}_3 \cdot d\mathbf{a} = \oint_S \mathbf{E}_1 \cdot d\mathbf{a} - \oint_S \mathbf{E}_2 \cdot d\mathbf{a} = \frac{Q_1}{\varepsilon_0} - \frac{Q_2}{\varepsilon_0} = 0 \\
\nabla \cdot (V_3 \mathbf{E}_3) = (\nabla V_3) \cdot \mathbf{E}_3 + V_3 (\nabla \cdot \mathbf{E}_3) = -{E_3}^2 \\
\begin{aligned}{}
\int_V \nabla \cdot (V_3 \mathbf{E}_3) d\tau &= \oint_S (V_3 \mathbf{E}_3) \cdot d\mathbf{a} = \sum V_3 \oint_S \mathbf{E}_3 \cdot d\mathbf{a} \\
&= 0 = -\int_V {E_3}^2 d\tau 
\end{aligned}\\
\mathbf{E}_3 = 0 \rightarrow \mathbf{E}_1 = \mathbf{E}_2
$$
{: .notice--primary}

### Capacitor / コンデンサー

$$
\begin{aligned}{}
Q &= CV \\
I &= C \frac{dV}{dt} \\
W &= \frac{1}{2}CV^2 \\
\end{aligned}
$$
{: .notice--info}

$$
I = \frac{dQ}{dt} = C \frac{dV}{dt} \\
dW = dQ \cdot V = CV \, dV \\
W = \frac{1}{2}CV^2
$$
{: .notice--primary}

## Magnetostatics / 静磁場

### Magnetic Field / 磁場

$$
\begin{aligned}{}
& \nabla \cdot \mathbf{B} = 0 && \oint_S \mathbf{B} \cdot d\mathbf{a} = 0 \\
& \nabla \times \mathbf{B} = \mu_0 \mathbf{J} && \oint_C \mathbf{B} \cdot d\mathbf{l} = \mu_0 I
\end{aligned} \\
\mathbf{B}(\mathbf{r}) = \frac{\mu_0}{4\pi} \int_V \frac{\mathbf{J}(\mathbf{r}') \times \hat{\mathbf{\vec{r}}}}{\vec{r}^2} \, d\tau'
$$
{: .notice--info}

$$
\begin{aligned}{}
\nabla \cdot \mathbf{B}(\mathbf{r}) 
&= \frac{\mu_0}{4\pi} \int_V \nabla \cdot \left[ \mathbf{J}(\mathbf{r}') \times \frac{\hat{\mathbf{\vec{r}}}}{\vec{r}^2} \right] \, d\tau' \\
&= \frac{\mu_0}{4\pi} \int_V -\mathbf{J}(\mathbf{r}') \cdot \left( \nabla \times \frac{\hat{\mathbf{\vec{r}}}}{\vec{r}^2} \right) \, d\tau' \\
&= 0
\end{aligned} \\
\begin{aligned}{}
\nabla \times \mathbf{B}(\mathbf{r}) 
&= \frac{\mu_0}{4\pi} \int_V \nabla \times \left[ \mathbf{J}(\mathbf{r}') \times \frac{\hat{\mathbf{\vec{r}}}}{\vec{r}^2} \right] \, d\tau' \\
&= \frac{\mu_0}{4\pi} \int_V \left[ \mathbf{J}(\mathbf{r}') (\nabla \cdot \frac{\hat{\mathbf{\vec{r}}}}{\vec{r}^2}) - (\mathbf{J}(\mathbf{r}') \cdot \nabla) \frac{\hat{\mathbf{\vec{r}}}}{\vec{r}^2} \right] \, d\tau' \\
&= \frac{\mu_0}{4\pi} \int_V \mathbf{J}(\mathbf{r}') 4\pi \delta^3(\mathbf{r} - \mathbf{r}') \, d\tau' 
+ \frac{\mu_0}{4\pi} \int_V (\mathbf{J}(\mathbf{r}') \cdot \nabla') \frac{\hat{\mathbf{\vec{r}}}}{\vec{r}^2} \, d\tau' \\ &= \mu_0 \mathbf{J}(\mathbf{r}) + \frac{\mu_0}{4\pi} \int_V \left[ \nabla'_2 \cdot \left( \frac{\hat{\mathbf{\vec{r}}}}{\vec{r}^2} \otimes \mathbf{J}(\mathbf{r}') \right) - \frac{\hat{\mathbf{\vec{r}}}}{\vec{r}^2} \left( \nabla' \cdot \mathbf{J}(\mathbf{r}') \right) \right] \, d\tau' \\
&= \mu_0 \mathbf{J}(\mathbf{r}) + \frac{\mu_0}{4\pi} \oint_S \left(\frac{\hat{\mathbf{\vec{r}}}}{\vec{r}^2} \otimes \mathbf{J}(\mathbf{r}')\right) \cdot d\mathbf{a}' + \frac{\mu_0}{4\pi} \int_V \frac{\hat{\mathbf{\vec{r}}}}{\vec{r}^2} \frac{\partial \rho(\mathbf{r}')}{\partial t} \, d\tau' \\
&= \mu_0 \mathbf{J}(\mathbf{r})
\end{aligned}
$$
{: .notice--primary}

### Magnetic Potential / 磁位

$$
\mathbf{B} = \nabla \times \mathbf{A} \\
\nabla^2 \mathbf{A} = -\mu_0 \mathbf{J} \\
\mathbf{A}(\mathbf{r}) = \frac{\mu_0}{4\pi} \int_V \frac{\mathbf{J}(\mathbf{r}')}{\vec{r}} \, d\tau'
$$
{: .notice--info}

$$
\nabla \cdot \mathbf{B} = \nabla \cdot (\nabla \times \mathbf{A}) = 0 \\
\nabla \times \mathbf{B} = \nabla \times (\nabla \times \mathbf{A}) 
= \nabla(\nabla \cdot \mathbf{A}) - \nabla^2 \mathbf{A} \\
\mathbf{A} = \mathbf{A}_0 + \nabla \lambda \\
\mathbf{B} = \nabla \times \mathbf{A}_0 + \nabla \times \nabla \lambda 
= \nabla \times \mathbf{A}_0 = \mathbf{B}_0 \\
\nabla^2 \lambda = -\nabla \cdot \mathbf{A}_0 \\
\nabla \cdot \mathbf{A} = \nabla \cdot \mathbf{A}_0 + \nabla^2 \lambda = 0 \\
\nabla \times \mathbf{B} = -\nabla^2 \mathbf{A} = \mu_0 \mathbf{J} \\
\begin{aligned}{}
\nabla^2 \mathbf{A}(\mathbf{r}) 
&= \frac{\mu_0}{4\pi} \int_V \nabla^2 \left( \frac{1}{\vec{r}} \right) \mathbf{J}(\mathbf{r}') \, d\tau' \\
&= \frac{\mu_0}{4\pi} \int_V -4\pi \delta^3(\mathbf{r} - \mathbf{r}') \mathbf{J}(\mathbf{r}') \, d\tau' \\
&= -\mu_0 \mathbf{J}(\mathbf{r})
\end{aligned}
$$
{: .notice--primary}

### Magnetic Energy / 磁気エネルギー

$$
W = \frac{1}{2} \int_V \mathbf{J} \cdot \mathbf{A} \, d\tau \\
W = \frac{1}{2\mu_0} \int_V B^2 \, d\tau
$$
{: .notice--info}

$$
\begin{aligned}{}
\delta W &= - \delta q \oint_C \mathbf{E} \cdot d\mathbf{l} \\
&= - \delta q \oint_S (\nabla \times \mathbf{E}) \cdot d\mathbf{a} \\
&= I \delta t \oint_S \frac{\partial \mathbf{B}}{\partial t} \cdot d\mathbf{a} \\
&= I \oint_S \delta \mathbf{B} \cdot d\mathbf{a} \\
&= I \oint_S (\nabla \times \delta \mathbf{A}) \cdot d\mathbf{a} \\
&= I \oint_C \delta \mathbf{A} \cdot d\mathbf{l} \\
&= \int_C \mathbf{I} \cdot \delta \mathbf{A} \, dl \\
&= \int_V \mathbf{J} \cdot \delta \mathbf{A} \, d\tau \\
&= \int_V \frac{1}{2} \delta (\mathbf{J} \cdot \mathbf{A}) \, d\tau
\end{aligned} \\
\begin{aligned}{}
W &= \frac{1}{2} \int_V \mathbf{J} \cdot \mathbf{A} \, d\tau \\
&= \frac{1}{2\mu_0} \int_V (\nabla \times \mathbf{B}) \cdot \mathbf{A} \, d\tau \\
&= \frac{1}{2\mu_0} \left[ \int_V \mathbf{B} \cdot (\nabla \times \mathbf{A}) \, d\tau - \int_V \nabla \cdot (\mathbf{A} \times \mathbf{B}) \, d\tau \right] \\
&= \frac{1}{2\mu_0} \int_V B^2 \, d\tau - \frac{1}{2\mu_0} \oint_S (\mathbf{A} \times \mathbf{B}) \cdot d\mathbf{a} \\
&= \frac{1}{2\mu_0} \int_V B^2 \, d\tau
\end{aligned}
$$
{: .notice--primary}

### Magnetic Dipole / 磁気双極子

$$
\mathbf{A}(\mathbf{r}) = \frac{\mu_0}{4\pi} \sum_{n=0}^{\infty} \frac{1}{r^{n+1}} \int_V (r')^n P_n(\cos\alpha) \mathbf{J}(\mathbf{r}') \, d\tau' \\
m = I a \\
\mathbf{A}_{\text{dip}} = \frac{\mu_0}{4\pi} \frac{m \sin\theta \, \hat{\boldsymbol{\phi}}}{r^2} \\
\mathbf{B}_{\text{dip}} = \frac{\mu_0}{4\pi} \frac{m( 2\cos\theta \, \hat{\mathbf{r}} + \sin\theta \, \hat{\boldsymbol{\theta}} )}{r^3}
$$
{: .notice--info}

$$
\frac{1}{\vec{r}} = \frac{1}{\sqrt{r^2 + (r')^2 - 2rr'\cos\alpha}} = \frac{1}{r} \sum_{n=0}^{\infty} \left(\frac{r'}{r}\right)^n P_n(\cos\alpha) \\
\begin{aligned}{}
\mathbf{A}(\mathbf{r}) &= \frac{\mu_0}{4\pi} \int_V \frac{\mathbf{J}(\mathbf{r}')}{\vec{r}} \, d\tau' \\
&= \frac{\mu_0}{4\pi} \int_V \sum_{n=0}^{\infty} \frac{(r')^n}{r^{n+1}} P_n(\cos\alpha) \mathbf{J}(\mathbf{r}') \, d\tau' \\
&= \frac{\mu_0}{4\pi} \sum_{n=0}^{\infty} \frac{1}{r^{n+1}} \int_V (r')^n P_n(\cos\alpha) \mathbf{J}(\mathbf{r}') \, d\tau'
\end{aligned} \\
\begin{aligned}{}
\mathbf{A}_{\text{dip}} &= \frac{\mu_0}{4\pi} \frac{1}{r^2} \oint_C r' (\cos\alpha)  I \,d\mathbf{l}' \\
&= \frac{\mu_0}{4\pi} \frac{I}{r^2} \oint_C \mathbf{r}' \cdot \hat{\mathbf{r}} \,d\mathbf{l}' \\
&= \frac{\mu_0}{4\pi} \frac{I\mathbf{a} \times \hat{\mathbf{r}}}{r^2} \\
&= \frac{\mu_0}{4\pi} \frac{I a \sin\theta \, \hat{\boldsymbol{\phi}}}{r^2}
\end{aligned} \\
\begin{aligned}{}
\mathbf{B}_{\text{dip}} &= \nabla \times \mathbf{A}_{\text{dip}} \\
&= \frac{\mu_0}{4\pi} \frac{I a ( 2\cos\theta \, \hat{\mathbf{r}} + \sin\theta \, \hat{\boldsymbol{\theta}} )}{r^3}
\end{aligned}
$$
{: .notice--primary}

### Electromagnetic Induction / 電磁誘導

$$
\begin{aligned}{}
& \mathcal{E} = \int_C (\mathbf{v} \times \mathbf{B}) \cdot d\mathbf{l} \\
& \mathcal{E} = - \frac{d}{dt} \int_S \mathbf{B} \cdot d\mathbf{a}
\end{aligned}
$$
{: .notice--info}

$$
\begin{aligned}{}
\mathcal{E} &= \frac{1}{q} \int_C q \, (\mathbf{v} \times \mathbf{B}) \cdot d\mathbf{l} \\
&= \int_C (\mathbf{v} \times \mathbf{B}) \cdot d\mathbf{l} \\
\mathcal{E} &= \frac{1}{q} \oint_C q\mathbf{E} \cdot d\mathbf{l} \\
&= \int_S (\nabla \times \mathbf{E}) \cdot d\mathbf{a} \\
&= \int_S -\frac{\partial \mathbf{B}}{\partial t} \cdot d\mathbf{a} \\
&= - \frac{d}{dt} \int_S \mathbf{B} \cdot d\mathbf{a}
\end{aligned}
$$
{: .notice--primary}

### Inductor / インダクタ

$$
\begin{aligned}{}
& \Phi = L I \\
& V = L \frac{dI}{dt} \\
& W = \frac{1}{2} L I^2
\end{aligned}
$$
{: .notice--info}

$$
\begin{aligned}{}
V &= \frac{d\Phi}{dt} = L \frac{dI}{dt} \\
dW &=I\,dt \cdot L \frac{dI}{dt} = L I \, dI \\
W &= \frac{1}{2} L I^2
\end{aligned}
$$
{: .notice--primary}

## Electromagnetism in Matter / 物質中の電磁気学

### Polarization / 分極

$$
\begin{aligned}{}
\mathbf{N} &= \mathbf{p} \times \mathbf{E} \\
\mathbf{F} &= \nabla (\mathbf{p} \cdot \mathbf{E})
\end{aligned}
$$
{: .notice--info}

$$
\begin{aligned}{}
\mathbf{N} &= \int_V \mathbf{r}' \times \left( \rho(\mathbf{r}') \, d\tau' \mathbf{E} \right) \\
&= \left( \int_V \mathbf{r}' \rho(\mathbf{r}') \, d\tau' \right) \times \mathbf{E}
\end{aligned} \\
\begin{aligned}{}
\mathbf{F} &= \int_V \rho(\mathbf{r}') \, d\tau' \, \mathbf{E} \\
&= \int_V \rho(\mathbf{r}') \, d\tau' \left[ \mathbf{E}_0 + \mathbf{r}' \cdot (\nabla \mathbf{E})_0 \right] \\
&= \left( \int_V \rho(\mathbf{r}') \, d\tau' \right) \mathbf{E}_0 
+ \left( \int_V \mathbf{r}' \rho(\mathbf{r}') \, d\tau' \right) \cdot \nabla \mathbf{E} \\
&= \nabla \left[ \left( \int_V \mathbf{r}' \rho(\mathbf{r}') \, d\tau' \right) \cdot \mathbf{E} \right]
\end{aligned}
$$
{: .notice--primary}

### Electric Displacement / 電束密度

$$
\rho_b = -\nabla \cdot \mathbf{P} \quad 
 \sigma_b = \mathbf{P} \cdot \hat{\mathbf{n}} \\
\mathbf{D} = \varepsilon_0 \mathbf{E} + \mathbf{P} = \varepsilon \mathbf{E} \\
 \nabla \cdot \mathbf{D} = \rho_f
$$
{: .notice--info}

$$
\begin{aligned}{}
V &= \frac{1}{4\pi \varepsilon_0} \int_V \frac{\mathbf{P}(\mathbf{r}') \cdot \hat{\mathbf{\vec{r}}}}{\vec{r}^2} \, d\tau' \\
&= \frac{1}{4\pi \varepsilon_0} \int_V \mathbf{P}(\mathbf{r}') \cdot \nabla' \left(\frac{1}{\vec{r}}\right) \, d\tau' \\
&= \frac{1}{4\pi \varepsilon_0} \int_V \left[-\frac{1}{\vec{r}}\nabla' \cdot \mathbf{P}(\mathbf{r}') + \nabla' \cdot \left(\frac{\mathbf{P}(\mathbf{r}')}{\vec{r}}\right)\right] d\tau' \\
&= \frac{1}{4\pi \varepsilon_0} \int_V \frac{-\nabla' \cdot \mathbf{P}(\mathbf{r}')}{\vec{r}} \, d\tau' 
+ \frac{1}{4\pi \varepsilon_0} \oint_S \frac{\mathbf{P}(\mathbf{r}')}{\vec{r}} \cdot d\mathbf{a}' \\
&= \frac{1}{4\pi \varepsilon_0} \int_V \frac{\rho_b(\mathbf{r}')}{\vec{r}} \, d\tau' 
+ \frac{1}{4\pi \varepsilon_0} \oint_S \frac{\sigma_b(\mathbf{r}')}{\vec{r}} \, da'
\end{aligned} \\
\nabla \cdot \mathbf{E} = \frac{1}{\varepsilon_0} \left(\rho_f - \nabla \cdot \mathbf{P}\right) \\
\nabla \cdot \left(\varepsilon_0 \mathbf{E} + \mathbf{P}\right) = \rho_f
$$
{: .notice--primary}

### Magnetization / 磁化

$$
\begin{aligned}{}
\mathbf{N} &= \mathbf{m} \times \mathbf{B} \\
\mathbf{F} &= \nabla (\mathbf{m} \cdot \mathbf{B})
\end{aligned}
$$
{: .notice--info}

$$
\begin{aligned}{}
\mathbf{N} 
&= \oint_C \mathbf{r}' \times \left( I \, d\mathbf{l}' \times \mathbf{B} \right) \\
&= I \oint_C d\mathbf{l}' \left( \mathbf{r}' \cdot \mathbf{B} \right) - I \oint_C \mathbf{B} \left( \mathbf{r}' \cdot d\mathbf{l}' \right) \\
&= (I \, \mathbf{a}) \times \mathbf{B}
\end{aligned} \\
\begin{aligned}{}
\mathbf{F} 
&= \oint_C I \, d\mathbf{l}' \times \mathbf{B} \\
&= I \oint_C d\mathbf{l}' \times \left[ \mathbf{B}_0 + \mathbf{r}' \cdot (\nabla \mathbf{B})_0 \right] \\
&= \left( I \oint_C d\mathbf{l}' \right) \times \mathbf{B}_0 
+ I \oint_C d\mathbf{l}' \times \left[ \mathbf{r}' \cdot (\nabla \mathbf{B})_0 \right] \\
&= \nabla \left[ \left(I \, \mathbf{a} \right) \cdot \mathbf{B} \right]
\end{aligned}
$$
{: .notice--primary}

### Auxiliary Field / 補助磁場

$$
\mathbf{J}_b = \nabla \times \mathbf{M} \quad 
 \mathbf{K}_b = \mathbf{M} \times \hat{\mathbf{n}} \\
\mathbf{H} = \frac{1}{\mu_0} \mathbf{B} - \mathbf{M} = \frac{1}{\mu} \mathbf{B} \\ 
\nabla \times \mathbf{H} = \mathbf{J}_f
$$
{: .notice--info}

$$
\begin{aligned}{}
\mathbf{A}(\mathbf{r}) 
&= \frac{\mu_0}{4\pi} \int_V \frac{\mathbf{M}(\mathbf{r}') \times \hat{\mathbf{\vec{r}}}}{\vec{r}^2} \, d\tau' \\
&= \frac{\mu_0}{4\pi} \int_V \mathbf{M}(\mathbf{r}') \times \nabla' \left(\frac{1}{\vec{r}}\right) d\tau' \\
&= \frac{\mu_0}{4\pi} \int_V \left[ \frac{1}{\vec{r}}\nabla' \times \mathbf{M}(\mathbf{r}') - \nabla' \times \left(\frac{\mathbf{M}(\mathbf{r}')}{\vec{r}}\right) \right] d\tau' \\
&= \frac{\mu_0}{4\pi} \int_V \frac{\nabla' \times \mathbf{M}(\mathbf{r}')}{\vec{r}} \, d\tau' 
+ \frac{\mu_0}{4\pi} \oint_S \frac{\mathbf{M}(\mathbf{r}')}{\vec{r}} \times d\mathbf{a}' \\
&= \frac{\mu_0}{4\pi} \int_V \frac{\mathbf{J}_b(\mathbf{r}')}{\vec{r}} \, d\tau' 
+ \frac{\mu_0}{4\pi} \oint_S \frac{\mathbf{K}_b(\mathbf{r}')}{\vec{r}} \, da
\end{aligned} \\
\nabla \times \mathbf{B} = \mu_0 (\mathbf{J}_f + \nabla \times \mathbf{M}) \\
\nabla \times \left(\frac{1}{\mu_0} \mathbf{B} - \mathbf{M}\right) = \mathbf{J}_f
$$
{: .notice--primary}

### Maxwell's Equations in Matter / 物質中のMaxwell方程式

$$
\begin{aligned}{}
& \nabla \cdot \mathbf{D} = \rho_f \\
& \nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t} \\
& \nabla \cdot \mathbf{B} = 0 \\
& \nabla \times \mathbf{H} = \mathbf{J}_f + \frac{\partial \mathbf{D}}{\partial t}
\end{aligned}
$$
{: .notice--info}

$$
\begin{aligned}{}
\rho &= \rho_f + \rho_b \\
&= \rho_f - \nabla \cdot \mathbf{P}
\end{aligned} \\
\begin{aligned}{}
\mathbf{J} &= \mathbf{J}_f + \mathbf{J}_b + \mathbf{J}_p \\
&= \mathbf{J}_f + \nabla \times \mathbf{M} + \frac{\partial \mathbf{P}}{\partial t}
\end{aligned} \\
\nabla \cdot \mathbf{E} = \frac{1}{\varepsilon_0} \left( \rho_f - \nabla \cdot \mathbf{P} \right) \\
\nabla \cdot \left( \varepsilon_0 \mathbf{E} + \mathbf{P} \right) = \rho_f \\
\nabla \times \mathbf{B} 
= \mu_0 \left( \mathbf{J}_f + \nabla \times \mathbf{M} + \frac{\partial \mathbf{P}}{\partial t} \right) 
+ \mu_0 \varepsilon_0 \frac{\partial \mathbf{E}}{\partial t} \\
\nabla \times \left( \frac{1}{\mu_0} \mathbf{B} - \mathbf{M} \right) 
= \mathbf{J}_f + \frac{\partial}{\partial t} \left( \varepsilon_0 \mathbf{E} + \mathbf{P} \right)
$$
{: .notice--primary}

### Boundary Conditions / 境界条件

$$
\begin{aligned}{}
& \mathbf{D}_{1n} - \mathbf{D}_{2n} = \sigma_f \,\hat{\mathbf{n}} \\
& \mathbf{E}_{1t} - \mathbf{E}_{2t} = 0 \\
& \mathbf{B}_{1n} - \mathbf{B}_{2n} = 0 \\
& \mathbf{H}_{1t} - \mathbf{H}_{2t} = \mathbf{K}_f \times \hat{\mathbf{n}}
\end{aligned}
$$
{: .notice--info}

$$
\begin{aligned}{}
\oint_S \mathbf{D} \cdot d\mathbf{a} 
&= \mathbf{D}_{1n}\cdot \mathbf{a} - \mathbf{D}_{2n}\cdot \mathbf{a} \\
&= \sigma_f \,\hat{\mathbf{n}}\cdot \mathbf{a}
\end{aligned} \\
\begin{aligned}{}
\oint_C \mathbf{E} \cdot d\mathbf{l} 
&= \mathbf{E}_{1t}\cdot \mathbf{l} - \mathbf{E}_{2t}\cdot \mathbf{l} \\
&= 0
\end{aligned} \\
\begin{aligned}{}
\oint_S \mathbf{B} \cdot d\mathbf{a} 
&= \mathbf{B}_{1n}\cdot \mathbf{a} - \mathbf{B}_{2n}\cdot \mathbf{a} \\
&= 0
\end{aligned} \\
\begin{aligned}{}
\oint_C \mathbf{H} \cdot d\mathbf{l} 
&= \mathbf{H}_{1t}\cdot \mathbf{l} - \mathbf{H}_{2t}\cdot \mathbf{l} \\
&= \mathbf{K}_f \cdot (\hat{\mathbf{n}}\times \mathbf{l}) \\
&= (\mathbf{K}_f \times \hat{\mathbf{n}}) \cdot \mathbf{l}
\end{aligned}
$$
{: .notice--primary}

## Electrodynamics / 電気力学

## Electromagnetic Wave / 電磁波

## Radiation / 放射

## Electrical Circuit / 電気回路

## Relativistic Electrodynamics / 相対論的電気力学

### Relativistic Current / 相対論的電流

$$
J^\mu = \left( c\rho, J_x, J_y, J_z \right) \\
\bar{J}^{\mu} = \Lambda^{\mu}_{\nu} J^{\nu} \\
\frac{\partial J^{\mu}}{\partial x^{\mu}} = 0
$$
{: .notice--info}

$$
c\rho = \rho_0 \frac{c}{\sqrt{1 - \frac{u^2}{c^2}}} \\
\mathbf{J} = \rho \mathbf{v} = \rho_0 \frac{\mathbf{v}}{\sqrt{1 - \frac{v^2}{c^2}}} \\
J^{\mu} = \rho_0 v^{\mu} \\
\frac{\partial J^{\mu}}{\partial x^{\mu}} = \frac{\partial \rho}{\partial t} + \nabla \cdot \mathbf{J} = 0
$$
{: .notice--primary}

### Relativistic Field / 相対論的場

$$
F^{\mu \nu} =
\begin{pmatrix}
0 & \frac{E_x}{c} & \frac{E_y}{c} & \frac{E_z}{c} \\
-\frac{E_x}{c} & 0 & B_z & -B_y \\
-\frac{E_y}{c} & -B_z & 0 & B_x \\
-\frac{E_z}{c} & B_y & -B_x & 0
\end{pmatrix} \\
G^{\mu \nu} =
\begin{pmatrix}
0 & B_x & B_y & B_z \\
-B_x & 0 & -\frac{E_z}{c} & \frac{E_y}{c} \\
-B_y & \frac{E_z}{c} & 0 & -\frac{E_x}{c} \\
-B_z & -\frac{E_y}{c} & \frac{E_x}{c} & 0
\end{pmatrix} \\
\bar{F}^{\mu \nu} = \Lambda^\mu_{\lambda} \Lambda^\nu_{\sigma} F^{\lambda \sigma}
\quad
\bar{G}^{\mu \nu} = \Lambda^\mu_{\lambda} \Lambda^\nu_{\sigma} G^{\lambda \sigma} \\
\frac{\partial F^{\mu \nu}}{\partial x^\nu} = \mu_0 J^\mu
\quad
\frac{\partial G^{\mu \nu}}{\partial x^\nu} = 0 \\
\left( \frac{F}{\sqrt{1 - \frac{v^2}{c^2}}} \right)^\mu = q \left( \frac{v}{\sqrt{1 - \frac{v^2}{c^2}}} \right)_\nu F^{\mu \nu}
$$
{: .notice--info}

$$
\begin{aligned}{}
\frac{\partial F^{0\nu}}{\partial x^\nu}
&= \frac{1}{c} \frac{\partial E_x}{\partial x}
+ \frac{1}{c} \frac{\partial E_y}{\partial y}
+ \frac{1}{c} \frac{\partial E_z}{\partial z}
= \frac{1}{c} (\nabla \cdot \mathbf{E})
= \mu_0 c \rho \\
\frac{\partial F^{1\nu}}{\partial x^\nu}
&= -\frac{1}{c^2} \frac{\partial E_x}{\partial t}
+ \frac{\partial B_z}{\partial y}
- \frac{\partial B_y}{\partial z}
= \left( -\frac{1}{c^2} \frac{\partial \mathbf{E}}{\partial t}
+ \nabla \times \mathbf{B} \right)_x
= \mu_0 J_x \\
\frac{\partial G^{0\nu}}{\partial x^\nu}
&= \frac{\partial B_x}{\partial x}
+ \frac{\partial B_y}{\partial y}
+ \frac{\partial B_z}{\partial z}
= \nabla \cdot \mathbf{B} = 0 \\
\frac{\partial G^{1\nu}}{\partial x^\nu}
&= -\frac{1}{c} \frac{\partial B_x}{\partial t}
- \frac{1}{c} \frac{\partial E_z}{\partial y}
+ \frac{1}{c} \frac{\partial E_y}{\partial z}
= -\frac{1}{c} \left( \frac{\partial \mathbf{B}}{\partial t}
+ \nabla \times \mathbf{E} \right)_x
= 0 \\
\end{aligned} \\
\begin{aligned}{}
\frac{F_x}{\sqrt{1 - \frac{v^2}{c^2}}} &= \frac{1}{\sqrt{1 - \frac{v^2}{c^2}}}
\left( q \mathbf{E} + q \mathbf{v} \times \mathbf{B} \right)_x \\
&= q \left[
\frac{-c}{\sqrt{1 - \frac{v^2}{c^2}}}
\left( \frac{-E_x}{c} \right)
+ \frac{v_y}{\sqrt{1 - \frac{v^2}{c^2}}} B_z
- \frac{v_z}{\sqrt{1 - \frac{v^2}{c^2}}} B_y
\right]
\end{aligned}
$$
{: .notice--primary}

### Relativistic Potential / 相対論的ポテンシャル

$$
A^\mu = \left( \frac{V}{c}, A_x, A_y, A_z \right) \\
\bar{A}^\mu = \Lambda^\mu_{\nu} A^\nu \\
F^{\mu \nu} = \frac{\partial A^\nu}{\partial x_\mu} - \frac{\partial A^\mu}{\partial x_\nu} \\
\frac{\partial}{\partial x_\nu} \frac{\partial}{\partial x^\nu} A^\mu = -\mu_0 J^\mu 
$$
{: .notice--info}

$$
\begin{aligned}{}
F^{01} &= \frac{E_x}{c} = -\frac{1}{c} \left( \frac{\partial \mathbf{A}}{\partial t} + \nabla V \right)_x = -\frac{1}{c} \frac{\partial A_x}{\partial t} - \frac{1}{c} \frac{\partial V}{\partial x} \\
F^{12} &= B_z = (\nabla \times \mathbf{A})_z = \frac{\partial A_y}{\partial x} - \frac{\partial A_x}{\partial y}
\end{aligned} \\
\begin{aligned}{}
\left( -\frac{1}{c^2} \frac{\partial^2}{\partial t^2} + \nabla^2 \right) \frac{V}{c}
&= -\mu_0 c \rho \\
\left( -\frac{1}{c^2} \frac{\partial^2}{\partial t^2} + \nabla^2 \right) \mathbf{A}
&= -\mu_0 \mathbf{J} \\
\end{aligned}
$$
{: .notice--primary}

# Thermodynamics / 熱力学

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

$$
\begin{aligned}{}
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
\begin{aligned}{}
& \langle m | n \rangle = \delta_{mn} && \langle a | a' \rangle = \delta(a - a') \\
& \sum_n |n\rangle\langle n| = \mathbb I && \int |a\rangle\langle a| \, da = \mathbb I \\
& |\psi\rangle = \sum_n |n\rangle\langle n|\psi\rangle && |\psi\rangle = \int |a\rangle\langle a|\psi\rangle \, da
\end{aligned}
$$
{: .notice--info}

### Observable / 物理量

$$
\begin{aligned}{}
& \hat{A}|a\rangle = a|a\rangle && \langle a | a \rangle = \mathbb I \\
& a = a^* && \langle a_n | a_m \rangle = \delta_{nm} \\
& \hat{A} = \sum_a a |a\rangle\langle a| && \hat{A} = \int a |a\rangle\langle a| \, da
\end{aligned}
$$
{: .notice--info}

### Measurement / 測定

$$
\begin{aligned}{}
& p(a) = \langle \psi | \hat{P}_a | \psi \rangle \\
& \langle \hat{A} \rangle = \langle \psi | \hat{A} | \psi \rangle \\
& |\psi\rangle \to \frac{\hat{P}_a |\psi\rangle}{\sqrt{\langle \psi | \hat{P}_a | \psi \rangle}}
\end{aligned}
$$
{: .notice--info}

### Evolution / 発展

$$
\begin{aligned}{}
& |\psi(t)\rangle = \hat U(t)\,|\psi(0)\rangle \quad \hat U^\dagger(t)\,\hat U(t) = \mathbb I \\
& \hat U(t) = \exp\left[-\frac{i}{\hbar}\hat H t\right] \\
& \hat U(t) = \mathcal T \exp\left[-\frac{i}{\hbar}\int_{0}^{t}\hat H(t')\,dt'\right]
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

$$
\begin{aligned}{}
& \langle \mathbf{r}|\mathbf{p}\rangle = \frac{1}{(2\pi\hbar)^{3/2}}e^{\frac{i}{\hbar}\mathbf{p}\cdot\mathbf{r}} \\
& \psi(\mathbf{r}) = \int \langle \mathbf{r}|\mathbf{p}\rangle\langle \mathbf{p}|\psi\rangle\,d^{3}p \\
& \hphantom{\psi(\mathbf{r})}
= \int \frac{1}{(2\pi\hbar)^{3/2}}e^{\frac{i}{\hbar}\mathbf{p}\cdot\mathbf{r}}\phi(\mathbf{p})\,d^{3}p \\
& \phi(\mathbf{p}) = \int \langle \mathbf{p}|\mathbf{r}\rangle\langle \mathbf{r}|\psi\rangle\,d^{3}r \\
& \hphantom{\phi(\mathbf{p})}
= \int \frac{1}{(2\pi\hbar)^{3/2}}e^{-\frac{i}{\hbar}\mathbf{p}\cdot\mathbf{r}}\psi(\mathbf{r})\,d^{3}r
\end{aligned}
$$
{: .notice--primary}

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

$$
\begin{aligned}{}
& \langle \mathbf{r}|\mathbf{p}\rangle =
\frac{1}{(2\pi\hbar)^{3/2}}e^{\frac{i}{\hbar}\mathbf{r}\cdot\mathbf{p}}, \quad
-i\hbar\nabla\langle\mathbf{r}|\mathbf{p}\rangle =
\mathbf{p}\langle\mathbf{r}|\mathbf{p}\rangle \\
& \langle \mathbf{p}|\mathbf{r}\rangle =
\frac{1}{(2\pi\hbar)^{3/2}}e^{-\frac{i}{\hbar}\mathbf{r}\cdot\mathbf{p}}, \quad
i\hbar\nabla_{\mathbf{p}}\langle\mathbf{p}|\mathbf{r}\rangle =
\mathbf{r}\langle\mathbf{p}|\mathbf{r}\rangle \\
& \langle \mathbf{r}|\hat{\mathbf{r}}|\psi\rangle =
\mathbf{r}\langle\mathbf{r}|\psi\rangle \\
& \langle \mathbf{r}|\hat{\mathbf{p}}|\psi\rangle
= \int \langle \mathbf{r}|\hat{\mathbf{p}}|\mathbf{p}\rangle
\langle \mathbf{p}|\psi\rangle\,d^{3}p \\
& \hphantom{\langle \mathbf{r}|\hat{\mathbf{p}}|\psi\rangle}
= \int \mathbf{p}\langle \mathbf{r}|\mathbf{p}\rangle
\langle \mathbf{p}|\psi\rangle\,d^{3}p \\
& \hphantom{\langle \mathbf{r}|\hat{\mathbf{p}}|\psi\rangle}
= \int -i\hbar\nabla\langle \mathbf{r}|\mathbf{p}\rangle
\langle \mathbf{p}|\psi\rangle\,d^{3}p \\
& \hphantom{\langle \mathbf{r}|\hat{\mathbf{p}}|\psi\rangle}
= -i\hbar\nabla\langle \mathbf{r}|\psi\rangle \\
& \langle \mathbf{p}|\hat{\mathbf{p}}|\psi\rangle =
\mathbf{p}\langle\mathbf{p}|\psi\rangle \\
& \langle \mathbf{p}|\hat{\mathbf{r}}|\psi\rangle
= \int \langle \mathbf{p}|\hat{\mathbf{r}}|\mathbf{r}\rangle
\langle \mathbf{r}|\psi\rangle\,d^{3}r \\
& \hphantom{\langle \mathbf{p}|\hat{\mathbf{r}}|\psi\rangle}
= \int \mathbf{r}\langle \mathbf{p}|\mathbf{r}\rangle
\langle \mathbf{r}|\psi\rangle\,d^{3}r \\
& \hphantom{\langle \mathbf{p}|\hat{\mathbf{r}}|\psi\rangle}
= \int i\hbar\nabla_{\mathbf{p}}\langle \mathbf{p}|\mathbf{r}\rangle
\langle \mathbf{r}|\psi\rangle\,d^{3}r \\
& \hphantom{\langle \mathbf{p}|\hat{\mathbf{r}}|\psi\rangle}
= i\hbar\nabla_{\mathbf{p}}\langle \mathbf{p}|\psi\rangle \\
& [\hat{x}_i,\hat{p}_j]\psi
= x_i\left(-i\hbar\frac{\partial\psi}{\partial x_j}\right)
-\left[-i\hbar\frac{\partial}{\partial x_j}(x_i\psi)\right] \\
& \hphantom{[\hat{x}_i,\hat{p}_j]\psi}
= -i\hbar x_i\frac{\partial\psi}{\partial x_j}
+i\hbar\frac{\partial x_i}{\partial x_j}\psi
+i\hbar x_i\frac{\partial\psi}{\partial x_j} \\
& \hphantom{[\hat{x}_i,\hat{p}_j]\psi}
= i\hbar\delta_{ij}\psi \\
& [\hat{x}_i,\hat{x}_j]\psi
= x_ix_j\psi - x_jx_i\psi \\
& \hphantom{[\hat{x}_i,\hat{x}_j]\psi}
= 0 \\
& [\hat{p}_i,\hat{p}_j]\psi
= -i\hbar\frac{\partial}{\partial x_i}
\left(-i\hbar\frac{\partial\psi}{\partial x_j}\right)
-\left[-i\hbar\frac{\partial}{\partial x_j}
\left(-i\hbar\frac{\partial\psi}{\partial x_i}\right)\right] \\
& \hphantom{[\hat{p}_i,\hat{p}_j]\psi}
= -\hbar^2\frac{\partial^2\psi}{\partial x_i\partial x_j}
+\hbar^2\frac{\partial^2\psi}{\partial x_j\partial x_i} \\
& \hphantom{[\hat{p}_i,\hat{p}_j]\psi}
= 0
\end{aligned}
$$
{: .notice--primary}

### Expectation Value / 期待値

$$
\begin{aligned}{}
& \langle \hat{A}\rangle = \int \psi^{*}(\mathbf{r})\hat{A}\psi(\mathbf{r})\,d^{3}r \\
& \Delta A\Delta B \geq \frac{1}{2}\left|\langle[\hat{A},\hat{B}]\rangle\right| \\
& \Delta x\Delta p \geq \frac{\hbar}{2}
\end{aligned}
$$
{: .notice--info}

$$
\begin{aligned}{}
& \langle \hat{A}\rangle = \langle\psi|\hat{A}|\psi\rangle \\
& \hphantom{\langle \hat{A}\rangle}
= \int \langle\psi|\mathbf{r}\rangle\langle\mathbf{r}|\hat{A}|\psi\rangle\,d^{3}r \\
& \hphantom{\langle \hat{A}\rangle}
= \int \psi^{*}(\mathbf{r})\hat{A}\psi(\mathbf{r})\,d^{3}r \\
& \Delta A = \sqrt{\langle(\hat{A}-\langle\hat{A}\rangle)^2\rangle}
= \sqrt{\langle(\delta\hat{A})^2\rangle} \\
& \Delta B = \sqrt{\langle(\hat{B}-\langle\hat{B}\rangle)^2\rangle}
= \sqrt{\langle(\delta\hat{B})^2\rangle} \\
& \langle[\hat{A},\hat{B}]\rangle = \langle\hat{A}\hat{B}\rangle - \langle\hat{B}\hat{A}\rangle \\
& \hphantom{\langle[\hat{A},\hat{B}]\rangle}
= \langle(\hat{A}-\langle\hat{A}\rangle)(\hat{B}-\langle\hat{B}\rangle)\rangle
-\langle(\hat{B}-\langle\hat{B}\rangle)(\hat{A}-\langle\hat{A}\rangle)\rangle \\
& \hphantom{\langle[\hat{A},\hat{B}]\rangle}
= \langle\delta\hat{A}\delta\hat{B}\rangle
-\langle\delta\hat{B}\delta\hat{A}\rangle \\
& \hphantom{\langle[\hat{A},\hat{B}]\rangle}
= \langle[\delta\hat{A},\delta\hat{B}]\rangle \\
& (\Delta A)^2(\Delta B)^2
= \langle\delta\hat{A}\psi|\delta\hat{A}\psi\rangle
\langle\delta\hat{B}\psi|\delta\hat{B}\psi\rangle \\
& \hphantom{(\Delta A)^2(\Delta B)^2}
\geq \left|\langle\delta\hat{A}\psi|\delta\hat{B}\psi\rangle\right|^2 \\
& \hphantom{(\Delta A)^2(\Delta B)^2}
\geq \left|\operatorname{Im}\{\langle\delta\hat{A}\psi|\delta\hat{B}\psi\rangle\}\right|^2 \\
& \hphantom{(\Delta A)^2(\Delta B)^2}
= \left|\frac{\langle\delta\hat{A}\psi|\delta\hat{B}\psi\rangle
-\langle\delta\hat{B}\psi|\delta\hat{A}\psi\rangle}{2}\right|^2 \\
& \hphantom{(\Delta A)^2(\Delta B)^2}
= \left|\frac{\langle\delta\hat{A}\delta\hat{B}\rangle
-\langle\delta\hat{B}\delta\hat{A}\rangle}{2}\right|^2 \\
& \hphantom{(\Delta A)^2(\Delta B)^2}
= \left|\frac{\langle[\delta\hat{A},\delta\hat{B}]\rangle}{2}\right|^2 \\
& \hphantom{(\Delta A)^2(\Delta B)^2}
= \left|\frac{\langle[\hat{A},\hat{B}]\rangle}{2}\right|^2 \\
& \Delta x\Delta p \geq \frac{1}{2}\left|\langle[\hat{x},\hat{p}]\rangle\right| \\
& \hphantom{\Delta x\Delta p}
= \frac{1}{2}\left|\langle i\hbar\rangle\right| \\
& \hphantom{\Delta x\Delta p}
= \frac{\hbar}{2}
\end{aligned}
$$
{: .notice--primary}

### Schrödinger Equation / シュレーディンガー方程式

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

$$
\begin{aligned}{}
& \hat{H} = \frac{\hat{\mathbf{p}}^{2}}{2m}+V(\mathbf{r},t) \\
& \hphantom{\hat{H}}
= -\frac{\hbar^{2}}{2m}\nabla^{2}+V(\mathbf{r},t) \\
& \psi(\mathbf{r},t)=u(\mathbf{r})T(t) \\
& \frac{1}{u(\mathbf{r})}\left[-\frac{\hbar^{2}}{2m}\nabla^{2}u(\mathbf{r})+V(\mathbf{r})u(\mathbf{r})\right]
= i\hbar\frac{1}{T(t)}\frac{\partial T(t)}{\partial t}=E \\
& -\frac{\hbar^{2}}{2m}\nabla^{2}u(\mathbf{r})+V(\mathbf{r})u(\mathbf{r})
= Eu(\mathbf{r}) \\
& T(t)=Ce^{-\frac{i}{\hbar}Et} \\
& \psi_{n}(\mathbf{r},t)=u_{n}(\mathbf{r})e^{-\frac{i}{\hbar}E_{n}t} \\
& \psi(\mathbf{r},t)=\sum_{n}c_{n}u_{n}(\mathbf{r})e^{-\frac{i}{\hbar}E_{n}t}
\end{aligned}
$$
{: .notice--primary}

### Probability Current / 確率流

$$
\begin{aligned}{}
& \rho(\mathbf{r},t)=|\psi(\mathbf{r},t)|^{2} \\
& \mathbf{j}(\mathbf{r},t)=\frac{\hbar}{2mi}\left(\psi^{*}\nabla\psi-\psi\nabla\psi^{*}\right) \\
& \frac{\partial\rho}{\partial t}+\nabla\cdot\mathbf{j}=0
\end{aligned}
$$
{: .notice--info}

$$
\begin{aligned}{}
& \frac{\partial\rho}{\partial t}
= \frac{\partial\psi}{\partial t}\psi^{*}
+\psi\frac{\partial\psi^{*}}{\partial t} \\
& \hphantom{\frac{\partial\rho}{\partial t}}
= \left(-\frac{\hbar}{2mi}\nabla^{2}\psi+\frac{V}{i\hbar}\psi\right)\psi^{*}
+\psi\left(\frac{\hbar}{2mi}\nabla^{2}\psi^{*}-\frac{V}{i\hbar}\psi^{*}\right) \\
& \hphantom{\frac{\partial\rho}{\partial t}}
= \frac{\hbar}{2mi}\left(\psi\nabla^{2}\psi^{*}-\psi^{*}\nabla^{2}\psi\right) \\
& \nabla\cdot\mathbf{j}
= \frac{\hbar}{2mi}\left(\nabla\psi^{*}\cdot\nabla\psi+\psi^{*}\nabla^{2}\psi-\nabla\psi\cdot\nabla\psi^{*}-\psi\nabla^{2}\psi^{*}\right) \\
& \hphantom{\nabla\cdot\mathbf{j}}
= \frac{\hbar}{2mi}\left(\psi^{*}\nabla^{2}\psi-\psi\nabla^{2}\psi^{*}\right) \\
& \hphantom{\nabla\cdot\mathbf{j}}
= -\frac{\partial\rho}{\partial t}
\end{aligned}
$$
{: .notice--primary}

### Ehrenfest Theorem / エーレンフェストの定理

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

$$
\begin{aligned}{}
& \frac{d}{dt}\langle\hat{A}\rangle
= \left\langle\frac{\partial\psi}{\partial t}\middle|\hat{A}\middle|\psi\right\rangle
+\left\langle\psi\middle|\frac{\partial\hat{A}}{\partial t}\middle|\psi\right\rangle
+\left\langle\psi\middle|\hat{A}\middle|\frac{\partial\psi}{\partial t}\right\rangle \\
& \hphantom{\frac{d}{dt}\langle\hat{A}\rangle}
= \left\langle\frac{\hat{H}}{i\hbar}\psi\middle|\hat{A}\middle|\psi\right\rangle
+\left\langle\psi\middle|\frac{\partial\hat{A}}{\partial t}\middle|\psi\right\rangle
+\left\langle\psi\middle|\hat{A}\middle|\frac{\hat{H}}{i\hbar}\psi\right\rangle \\
& \hphantom{\frac{d}{dt}\langle\hat{A}\rangle}
= -\frac{1}{i\hbar}\langle\psi|\hat{H}\hat{A}|\psi\rangle
+\left\langle\frac{\partial\hat{A}}{\partial t}\right\rangle
+\frac{1}{i\hbar}\langle\psi|\hat{A}\hat{H}|\psi\rangle \\
& \hphantom{\frac{d}{dt}\langle\hat{A}\rangle}
= \frac{1}{i\hbar}\langle[\hat{A},\hat{H}]\rangle
+\left\langle\frac{\partial\hat{A}}{\partial t}\right\rangle \\
& \frac{d}{dt}\langle\hat{\mathbf{r}}\rangle
= \frac{1}{i\hbar}\langle[\hat{\mathbf{r}},\hat{H}]\rangle \\
& \hphantom{\frac{d}{dt}\langle\hat{\mathbf{r}}\rangle}
= \frac{1}{i\hbar}\left\langle\frac{1}{2m}[\hat{\mathbf{r}},\hat{\mathbf{p}}^{2}]
+[\hat{\mathbf{r}},V(\mathbf{r})]\right\rangle \\
& \hphantom{\frac{d}{dt}\langle\hat{\mathbf{r}}\rangle}
= \frac{1}{2mi\hbar}\left\langle\sum_i
\left([\hat{x}_i,\hat{p}_i]\hat{p}_i+\hat{p}_i[\hat{x}_i,\hat{p}_i]\right)\hat{\mathbf{e}}_i\right\rangle \\
& \hphantom{\frac{d}{dt}\langle\hat{\mathbf{r}}\rangle}
= \frac{1}{2mi\hbar}\left\langle i\hbar\hat{\mathbf{p}}+\hat{\mathbf{p}}i\hbar\right\rangle \\
& \hphantom{\frac{d}{dt}\langle\hat{\mathbf{r}}\rangle}
= \frac{\langle\hat{\mathbf{p}}\rangle}{m} \\
& \frac{d}{dt}\langle\hat{\mathbf{p}}\rangle
= \frac{1}{i\hbar}\langle[\hat{\mathbf{p}},\hat{H}]\rangle \\
& \hphantom{\frac{d}{dt}\langle\hat{\mathbf{p}}\rangle}
= \frac{1}{i\hbar}\left\langle\frac{1}{2m}[\hat{\mathbf{p}},\hat{\mathbf{p}}^{2}]
+[\hat{\mathbf{p}},V(\mathbf{r})]\right\rangle \\
& \hphantom{\frac{d}{dt}\langle\hat{\mathbf{p}}\rangle}
= \frac{1}{i\hbar}\left\langle\sum_i
\left(-i\hbar\frac{\partial V}{\partial x_i}
-i\hbar V\frac{\partial}{\partial x_i}
+i\hbar V\frac{\partial}{\partial x_i}\right)\hat{\mathbf{e}}_i\right\rangle \\
& \hphantom{\frac{d}{dt}\langle\hat{\mathbf{p}}\rangle}
= -\langle\nabla V\rangle
\end{aligned}
$$
{: .notice--primary}


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

$$
\begin{aligned}{}
& \int_{x_0-\varepsilon}^{x_0+\varepsilon}\left[-\frac{\hbar^2}{2m}\psi''(x)+V(x)\psi(x)\right]dx=\int_{x_0-\varepsilon}^{x_0+\varepsilon}E\psi(x)\,dx \\
& \int_{x_0-\varepsilon}^{x_0+\varepsilon}-\frac{\hbar^2}{2m}\psi''(x)\,dx=-\frac{\hbar^2}{2m}\left[\psi'(x_0^+)-\psi'(x_0^-)\right] \\
& \int_{x_0-\varepsilon}^{x_0+\varepsilon}\left[E-V(x)\right]\psi(x)\,dx=0 \quad \left(V(x_0)<\infty\right) \\
& \psi'(x_0^+)=\psi'(x_0^-),\quad \psi(x_0^+)=\psi(x_0^-) \\
& \int_{x_0-\varepsilon}^{x_0+\varepsilon}\left[E-V(x)\right]\psi(x)\,dx\neq 0 \quad \left(V(x_0)=\infty\right) \\
& \psi'(x_0^+)\neq\psi'(x_0^-),\quad \psi(x_0^+)=\psi(x_0^-)
\end{aligned}
$$
{: .notice--primary}

### Free Particle / 自由粒子

$$
\begin{aligned}{}
& V(x) = 0 \\
& \psi(x) = A e^{ikx} + B e^{-ikx} \\
& k = \frac{\sqrt{2mE}}{\hbar}
\end{aligned}
$$
{: .notice--info}

$$
\begin{aligned}{}
& \psi''+\frac{2mE}{\hbar^2}\psi=0 \\
& \psi=e^{\pm ikx},\quad k=\frac{\sqrt{2mE}}{\hbar} \\
\end{aligned}
$$
{: .notice--primary}

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

$$
\begin{aligned}{}
& V=0: && \psi''+\frac{2mE}{\hbar^2}\psi=0 \\
& && \psi=e^{\pm ik_1x},\quad k_1=\frac{\sqrt{2mE}}{\hbar} \\
& V=V_0: && \psi''+\frac{2m(E-V_0)}{\hbar^2}\psi=0 \\
& && \psi=e^{\pm ik_2x},\quad k_2=\frac{\sqrt{2m(E-V_0)}}{\hbar} \\
& x=0: && A+B=C \\
& && ik_1A-ik_1B=ik_2C \\
& && A=\frac{k_1+k_2}{2k_1}C \\
& && B=\frac{k_1-k_2}{2k_1}C \\
& && R=\left|\frac{B}{A}\right|^2=\left(\frac{k_1-k_2}{k_1+k_2}\right)^2 \\
& && T=\frac{k_2|C|^2}{k_1|A|^2}=\frac{4k_1k_2}{(k_1+k_2)^2}
\end{aligned}
$$
{: .notice--primary}

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

$$
\begin{aligned}{}
& V=0: && \psi''+\frac{2mE}{\hbar^2}\psi=0 \\
& && \psi=e^{\pm ikx},\quad k=\frac{\sqrt{2mE}}{\hbar} \\
& V=V_0: && \psi''-\frac{2m(V_0-E)}{\hbar^2}\psi=0 \\
& && \psi=e^{\pm\kappa x},\quad \kappa=\frac{\sqrt{2m(V_0-E)}}{\hbar} \\
& x=a: && Ce^{\kappa a}+De^{-\kappa a}=Fe^{ika} \\
& && \kappa Ce^{\kappa a}-\kappa De^{-\kappa a}=ikFe^{ika} \\
& && C=\frac{\kappa+ik}{2\kappa}Fe^{ika-\kappa a} \\
& && D=\frac{\kappa-ik}{2\kappa}Fe^{ika+\kappa a} \\
& x=0: && A+B=C+D \\
& && ikA-ikB=\kappa C-\kappa D \\
& && A=\frac{ik+\kappa}{2ik}C+\frac{ik-\kappa}{2ik}D \\
& && B=\frac{ik-\kappa}{2ik}C+\frac{ik+\kappa}{2ik}D \\
\end{aligned} \\
\begin{aligned}{}
A &=Fe^{ika}\left[\cosh(\kappa a)+i\frac{\kappa^2-k^2}{2\kappa k}\sinh(\kappa a)\right] \\
T &=\left|\frac{F}{A}\right|^2 \\
& =\left[\cosh^2(\kappa a)+\frac{(\kappa^2-k^2)^2}{4\kappa^2k^2}\sinh^2(\kappa a)\right]^{-1} \\
&=\left[1+\frac{(\kappa^2+k^2)^2}{4\kappa^2k^2}\sinh^2(\kappa a)\right]^{-1} \\
&=\left[1+\frac{V_0^2\sinh^2(\kappa a)}{4E(V_0-E)}\right]^{-1} \\
B&=Fe^{ika}\left[-i\frac{\kappa^2+k^2}{2\kappa k}\sinh(\kappa a)\right] \\
R&=\left|\frac{B}{A}\right|^2 \\
& =\left[\frac{4\kappa^2k^2}{(\kappa^2+k^2)^2}\cosh^2(\kappa a)+\frac{(\kappa^2-k^2)^2}{(\kappa^2+k^2)^2}\sinh^2(\kappa a)\right]^{-1} \\
&=\left[1+\frac{4\kappa^2k^2}{(\kappa^2+k^2)^2\sinh^2(\kappa a)}\right]^{-1} \\
&=\left[1+\frac{4E(V_0-E)}{V_0^2\sinh^2(\kappa a)}\right]^{-1}
\end{aligned}
$$
{: .notice--primary}

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

$$
\begin{aligned}{}
& \psi''+\frac{2mE}{\hbar^2}\psi=0 \\
& \psi=Ae^{ikx}+Be^{-ikx},\quad k=\frac{\sqrt{2mE}}{\hbar}
\end{aligned} \\
\begin{aligned}{}
& x=0: && A+B=0 \\
& && B=-A \\
& x=L: && Ae^{ikL}-Ae^{-ikL}=0 \\
& && A'\sin kL=0,\quad k=\frac{n\pi}{L}
\end{aligned} \\
\begin{aligned}{}
\int_0^L |\psi_n|^2 dx &=|A'|^2\int_0^L \sin^2\left(\frac{n\pi x}{L}\right)dx \\
&=|A'|^2\frac{L}{2}=1, \quad A'=\sqrt{\frac{2}{L}}
\end{aligned} \\
\begin{aligned}{}
& \psi_n(x)=A'\sin\left(\frac{n\pi x}{L}\right)=\sqrt{\frac{2}{L}}\sin\left(\frac{n\pi x}{L}\right) \\
& E_n=\frac{\hbar^2k^2}{2m}=\frac{\hbar^2\pi^2n^2}{2mL^2}
\end{aligned}
$$
{: .notice--primary}

### Harmonic Oscillator / 調和振動子

$$
\begin{aligned}{}
& V(x) = \frac{1}{2} m \omega^2 x^2 \\
& \psi_n(x) = \frac{1}{\sqrt{2^n n!}} \left( \frac{m\omega}{\pi\hbar} \right)^{1/4} H_n \left( \sqrt{\frac{m\omega}{\hbar}} x \right) \exp\left( -\frac{m\omega x^2}{2\hbar} \right) \\
& E_n = \hbar \omega \left( n + \frac{1}{2} \right), \quad n = 0, 1, 2, \dots
\end{aligned}
$$
{: .notice--info}

$$
\begin{aligned}{}
& \frac{d^2\psi}{dx^2}-\frac{m^2\omega^2x^2}{\hbar^2}\psi=-\frac{2mE}{\hbar^2}\psi \\
& \xi=\sqrt{\frac{m\omega}{\hbar}}x, \quad \frac{d^2}{dx^2}=\frac{m\omega}{\hbar}\frac{d^2}{d\xi^2} \\
& \frac{d^2\psi}{d\xi^2}-\xi^2\psi=-\frac{2E}{\hbar\omega}\psi \\
& \xi\to\infty:\quad \frac{d^2\psi}{d\xi^2}-\xi^2\psi\simeq0,\quad \psi\sim e^{-\frac{\xi^2}{2}} \\
& \psi(\xi)=h(\xi)e^{-\frac{\xi^2}{2}}, \quad \psi''=\left[h''-2\xi h'+(\xi^2-1)h\right]e^{-\frac{\xi^2}{2}} \\
& h''-2\xi h'+\left(\frac{2E}{\hbar\omega}-1\right)h=0 \\
& \frac{2E}{\hbar\omega}-1=2n, \quad E=\hbar\omega\left(n+\frac{1}{2}\right) \\
& h_n=A H_n(\xi), \quad \psi_n(\xi)=A H_n(\xi)e^{-\frac{\xi^2}{2}}
\end{aligned}
$$
{: .notice--primary}

### Ladder Operator / 昇降演算子

$$
\begin{aligned}{}
& \hat{a} = \sqrt{\frac{m\omega}{2\hbar}} \hat{x} + \frac{i}{\sqrt{2m\hbar\omega}} \hat{p}, && \hat{a}^\dagger = \sqrt{\frac{m\omega}{2\hbar}} \hat{x} - \frac{i}{\sqrt{2m\hbar\omega}} \hat{p} \\
& \hat{a}|n\rangle = \sqrt{n}|n-1\rangle, && \hat{a}^\dagger|n\rangle = \sqrt{n+1}|n+1\rangle \\
& \hat{H}|n\rangle = \hbar\omega\left( n + \frac{1}{2} \right)|n\rangle
\end{aligned}
$$
{: .notice--info}

$$
\begin{aligned}{}
& \hat{a}\hat{a}^{\dagger} = \frac{m\omega}{2\hbar}\hat{x}^{2} + \frac{1}{2m\hbar\omega}\hat{p}^{2} + \frac{1}{2} \\
& \hat{a}^{\dagger}\hat{a} = \frac{m\omega}{2\hbar}\hat{x}^{2} + \frac{1}{2m\hbar\omega}\hat{p}^{2} - \frac{1}{2} \\
& \hat{H} = \hbar\omega\left(\hat{a}\hat{a}^{\dagger} - \frac{1}{2}\right) = \hbar\omega\left(\hat{a}^{\dagger}\hat{a} + \frac{1}{2}\right)
\end{aligned} \\
\begin{aligned}{}
& [\hat{H},\hat{a}] = -\hbar\omega\hat{a}[\hat{a},\hat{a}^{\dagger}] = -\hbar\omega\hat{a} \\
& \hat{H}\hat{a}|E\rangle = \hat{a}\hat{H}|E\rangle - \hbar\omega\hat{a}|E\rangle = (E-\hbar\omega)\hat{a}|E\rangle \\
& \hat{a}|E\rangle \propto |E-\hbar\omega\rangle \\
& [\hat{H},\hat{a}^{\dagger}] = \hbar\omega[\hat{a},\hat{a}^{\dagger}]\hat{a}^{\dagger} = \hbar\omega\hat{a}^{\dagger} \\
& \hat{H}\hat{a}^{\dagger}|E\rangle = \hat{a}^{\dagger}\hat{H}|E\rangle + \hbar\omega\hat{a}^{\dagger}|E\rangle = (E+\hbar\omega)\hat{a}^{\dagger}|E\rangle \\
& \hat{a}^{\dagger}|E\rangle \propto |E+\hbar\omega\rangle \\
& \langle \hat{H} \rangle = \hbar\omega\left(\langle \hat{a}^{\dagger}\hat{a}\rangle + \frac{1}{2}\right) = \hbar\omega\left(\|\hat{a}|\psi\rangle\|^{2} + \frac{1}{2}\right) \geq 0 \\
& \hat{a}|E_0\rangle = 0,\quad \hat{a}^{\dagger}\hat{a}|E_0\rangle = 0,\quad \hat{H}|E_0\rangle = \frac{\hbar\omega}{2}|E_0\rangle \\
& |E_n\rangle \propto (\hat{a}^{\dagger})^n |E_0\rangle,\quad \hat{H}|E_n\rangle = \hbar\omega\left(n+\frac{1}{2}\right)|E_n\rangle \\
& \hat{a}|n\rangle = C_-|n-1\rangle,\quad \langle n|\hat{a}^{\dagger}\hat{a}|n\rangle = |C_-|^2 \\
& \langle n|\hat{a}^{\dagger}\hat{a}|n\rangle = \frac{\langle n|\hat{H}|n\rangle}{\hbar\omega} - \frac{1}{2} = n,\quad C_- = \sqrt{n} \\
& \hat{a}^{\dagger}|n\rangle = C_+|n+1\rangle,\quad \langle n|\hat{a}\hat{a}^{\dagger}|n\rangle = |C_+|^2 \\
& \langle n|\hat{a}\hat{a}^{\dagger}|n\rangle = \frac{\langle n|\hat{H}|n\rangle}{\hbar\omega} + \frac{1}{2} = n+1,\quad C_+ = \sqrt{n+1}
\end{aligned}
$$
{: .notice--primary}


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

$$
\begin{aligned}{}
& \hat{U}_{\mathbf{a}} = e^{-\frac{i}{\hbar}\mathbf{a}\cdot\hat{\mathbf{p}}} \approx \hat{I} - \frac{i}{\hbar}\mathbf{a}\cdot\hat{\mathbf{p}} \\
& \hat{U}_{\mathbf{a}}\psi(\mathbf{r}) = \psi(\mathbf{r}) - \mathbf{a}\cdot\nabla\psi(\mathbf{r}) = \psi(\mathbf{r}-\mathbf{a}) \\
& \hat{U}_{\mathbf{a}}^{\dagger}\hat{H}\hat{U}_{\mathbf{a}} = \hat{H} \to [\hat{U}_{\mathbf{a}},\hat{H}] = 0 \\
& [\hat{U}_{\mathbf{a}},\hat{H}] = -\frac{i}{\hbar}\mathbf{a}\cdot[\hat{\mathbf{p}},\hat{H}] \to [\hat{\mathbf{p}},\hat{H}] = 0 \\
& \frac{d}{dt}\langle\hat{\mathbf{p}}\rangle = -\frac{i}{\hbar}\langle[\hat{\mathbf{p}},\hat{H}]\rangle \to \frac{d}{dt}\langle\hat{\mathbf{p}}\rangle = 0
\end{aligned}
$$
{: .notice--primary}

### Rotational Symmetry / 回転対称性

$$
\begin{aligned}{}
& \hat{\mathbf{L}} = -i\hbar\mathbf{r}\times\nabla \\
& \hat{U}_{\boldsymbol{\theta}} = e^{-\frac{i}{\hbar}\boldsymbol{\theta}\cdot\hat{\mathbf{L}}} \to \hat{U}_{\boldsymbol{\theta}}\psi(\mathbf{r}) = \psi(R_{\boldsymbol{\theta}}^{-1}\mathbf{r}) \\
& \langle \hat{U}_{\boldsymbol{\theta}}\psi|\hat{H}|\hat{U}_{\boldsymbol{\theta}}\psi\rangle = \langle\psi|\hat{H}|\psi\rangle \to \frac{d}{dt}\langle\hat{\mathbf{L}}\rangle = 0
\end{aligned}
$$
{: .notice--info}

$$
\begin{aligned}{}
& \hat{U}_{\theta} = e^{-\frac{i}{\hbar}\theta\hat{L}_{z}} \approx \hat{I} - \frac{i}{\hbar}\theta\hat{L}_{z} \\
& \hat{U}_{\theta}\psi(\phi) = \psi(\phi) - \theta\frac{\partial\psi(\phi)}{\partial\phi} = \psi(\phi-\theta) \\
& \hat{U}_{\boldsymbol{\theta}}^{\dagger}\hat{H}\hat{U}_{\boldsymbol{\theta}} = \hat{H} \to [\hat{U}_{\boldsymbol{\theta}},\hat{H}] = 0 \\
& [\hat{U}_{\boldsymbol{\theta}},\hat{H}] = -\frac{i}{\hbar}\boldsymbol{\theta}\cdot[\hat{\mathbf{L}},\hat{H}] \to [\hat{\mathbf{L}},\hat{H}] = 0 \\
& \frac{d}{dt}\langle\hat{\mathbf{L}}\rangle = -\frac{i}{\hbar}\langle[\hat{\mathbf{L}},\hat{H}]\rangle \to \frac{d}{dt}\langle\hat{\mathbf{L}}\rangle = 0
\end{aligned}
$$
{: .notice--primary}

### Time Translational Symmetry / 時間並進対称性

$$
\begin{aligned}{}
& \hat{E} = i\hbar\frac{\partial}{\partial t} \\
& \hat{U}_{\tau} = e^{-\frac{i}{\hbar}\tau\hat{E}} \to \hat{U}_{\tau}\psi(t) = \psi(t+\tau) \\
& \langle \hat{U}_{\tau}\psi|\hat{H}|\hat{U}_{\tau}\psi\rangle = \langle\psi|\hat{H}|\psi\rangle \to \frac{d}{dt}\langle\hat{E}\rangle = 0
\end{aligned}
$$
{: .notice--info}

$$
\begin{aligned}{}
& \hat{U}_{\tau} = e^{-\frac{i}{\hbar}\tau\hat{E}} \approx \hat{I} - \frac{i}{\hbar}\tau\hat{E} \\
& \hat{U}_{\tau}\psi(t) = \psi(t) + \tau\frac{\partial\psi(t)}{\partial t} = \psi(t+\tau) \\
& \hat{U}_{\tau}^{\dagger}\hat{H}\hat{U}_{\tau} = \hat{H} \to [\hat{U}_{\tau},\hat{H}] = 0 \\
& [\hat{U}_{\tau},\hat{H}] = -\frac{i}{\hbar}\tau[\hat{E},\hat{H}] \to [\hat{E},\hat{H}] = 0 \\
& \frac{d}{dt}\langle\hat{E}\rangle = -\frac{i}{\hbar}\langle[\hat{E},\hat{H}]\rangle \to \frac{d}{dt}\langle\hat{E}\rangle = 0
\end{aligned}
$$
{: .notice--primary}

### Parity Symmetry / パリティ対称性

$$
\begin{aligned}{}
& \hat{\Pi}\psi(\mathbf{r}) = \psi(-\mathbf{r}), \quad \pi = \pm 1 \\
& \langle \hat{\Pi}\psi|\hat{H}|\hat{\Pi}\psi\rangle = \langle\psi|\hat{H}|\psi\rangle \to \frac{d}{dt}\langle\hat{\Pi}\rangle = 0
\end{aligned}
$$
{: .notice--info}

$$
\begin{aligned}{}
& \hat{\Pi}\psi(\mathbf{r}) = \pi\psi(\mathbf{r}) = \psi(-\mathbf{r}) \\
& \hat{\Pi}^{2}\psi(\mathbf{r}) = \pi^{2}\psi(\mathbf{r}) = \psi(\mathbf{r}) \\
& \pi^{2} = 1, \quad \pi = \pm 1 \\
& \hat{\Pi}^{\dagger}\hat{H}\hat{\Pi} = \hat{H} \to [\hat{\Pi},\hat{H}] = 0 \\
& \frac{d}{dt}\langle\hat{\Pi}\rangle = -\frac{i}{\hbar}\langle[\hat{\Pi},\hat{H}]\rangle = 0
\end{aligned}
$$
{: .notice--primary}


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

$$
\begin{aligned}{}
[\hat{J}^2,\hat{J}_z] &= [\hat{J}_x^2,\hat{J}_z]+[\hat{J}_y^2,\hat{J}_z]+[\hat{J}_z^2,\hat{J}_z] \\
&= \hat{J}_x[\hat{J}_x,\hat{J}_z]+[\hat{J}_x,\hat{J}_z]\hat{J}_x+\hat{J}_y[\hat{J}_y,\hat{J}_z]+[\hat{J}_y,\hat{J}_z]\hat{J}_y \\
&= \hat{J}_x(-i\hbar\hat{J}_y)+(-i\hbar\hat{J}_y)\hat{J}_x+\hat{J}_y(i\hbar\hat{J}_x)+(i\hbar\hat{J}_x)\hat{J}_y \\
&= 0
\end{aligned} \\
\hat{J}^2|j,m\rangle = \hbar^2 j(j+1)|j,m\rangle,\quad \hat{J}_z|j,m\rangle = \hbar m|j,m\rangle \\
\begin{aligned}{}
[\hat{J}^2,\hat{J}_{\pm}] &= [\hat{J}^2,\hat{J}_x]\pm i[\hat{J}^2,\hat{J}_y] = 0
\end{aligned} \\
\begin{aligned}{}
\hat{J}^2\hat{J}_{\pm}|j,m\rangle &= \hat{J}_{\pm}\hat{J}^2|j,m\rangle = \hbar^2 j(j+1)\hat{J}_{\pm}|j,m\rangle
\end{aligned} \\
\begin{aligned}{}
[\hat{J}_z,\hat{J}_{\pm}] &= [\hat{J}_z,\hat{J}_x]\pm i[\hat{J}_z,\hat{J}_y] \\
&= i\hbar\hat{J}_y \pm i(-i\hbar\hat{J}_x) \\
&= \pm \hbar\hat{J}_{\pm}
\end{aligned} \\
\begin{aligned}{}
\hat{J}_z\hat{J}_{\pm}|j,m\rangle &= \hat{J}_{\pm}\hat{J}_z|j,m\rangle \pm \hbar\hat{J}_{\pm}|j,m\rangle \\
&= \hbar(m\pm 1)\hat{J}_{\pm}|j,m\rangle
\end{aligned} \\
\hat{J}_{\pm}|j,m\rangle = C_{\pm}|j,m\pm 1\rangle \\
\begin{aligned}{}
|C_{\pm}|^2 &= \langle j,m|\hat{J}_{\pm}^{\dagger}\hat{J}_{\pm}|j,m\rangle \\
&= \langle j,m|\hat{J}_x^2+\hat{J}_y^2\pm i[\hat{J}_x,\hat{J}_y]|j,m\rangle \\
&= \langle j,m|\hat{J}^2-\hat{J}_z^2\mp\hbar\hat{J}_z|j,m\rangle \\
&= \hbar^2 j(j+1)-\hbar^2 m^2 \mp \hbar^2 m
\end{aligned} \\
C_{\pm} = \hbar\sqrt{j(j+1)-m(m\pm 1)} \\
\langle j,m|\hat{J}^2-\hat{J}_z^2|j,m\rangle = \langle j,m|\hat{J}_x^2+\hat{J}_y^2|j,m\rangle \geq 0 \\
\hbar^2[j(j+1)-m^2]\geq 0,\quad m_{\min}\leq m\leq m_{\max} \\
\hat{J}_+|j,m_{\max}\rangle = 0,\quad j(j+1)-m_{\max}(m_{\max}+1)=0 \\
\hat{J}_-|j,m_{\min}\rangle = 0,\quad j(j+1)-m_{\min}(m_{\min}-1)=0 \\
m_{\max}=j,\quad m_{\min}=-j,\quad m=-j,-j+1,\ldots,j \\
j-(-j)\in\mathbb{Z}_{\geq 0},\quad j=0,\frac{1}{2},1,\ldots
$$
{: .notice--primary}

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

$$
\begin{aligned}{}
[\hat{L}_x,\hat{L}_y] &= -\hbar^2\left(y\frac{\partial}{\partial x}-x\frac{\partial}{\partial y}\right)=i\hbar\hat{L}_z \\
[\hat{L}_y,\hat{L}_z] &= -\hbar^2\left(z\frac{\partial}{\partial y}-y\frac{\partial}{\partial z}\right)=i\hbar\hat{L}_x \\
[\hat{L}_z,\hat{L}_x] &= -\hbar^2\left(x\frac{\partial}{\partial z}-z\frac{\partial}{\partial x}\right)=i\hbar\hat{L}_y 
\end{aligned} \\
\begin{aligned}{}
\hat{L}^2 &= -\hbar^2\left(\mathbf{r}\times\nabla\right)^2 \\
&= -\hbar^2\left[r^2\nabla^2-\left(\mathbf{r}\cdot\nabla\right)^2-\mathbf{r}\cdot\nabla\right] \\
&= -\hbar^2\left[\frac{1}{\sin\theta}\frac{\partial}{\partial\theta}\left(\sin\theta\frac{\partial}{\partial\theta}\right)+\frac{1}{\sin^2\theta}\frac{\partial^2}{\partial\phi^2}\right] 
\end{aligned} \\
\hat{L}_z = -i\hbar\left(x\frac{\partial}{\partial y}-y\frac{\partial}{\partial x}\right)=-i\hbar\frac{\partial}{\partial\phi} \\
\hat{L}_zY_l^m = -i\hbar\frac{\partial Y_l^m}{\partial\phi}=\hbar mY_l^m \rightarrow Y_l^m(\theta,\phi)=\Theta_l^m(\theta)e^{im\phi} \\
Y_l^m(\theta,\phi+2\pi) = Y_l^m(\theta,\phi) \rightarrow 
e^{i2\pi m}=1,\quad m\in\mathbb{Z} \\
\begin{aligned}{}
\hat{L}^2Y_l^m &= -\hbar^2\left[\frac{1}{\sin\theta}\frac{\partial}{\partial\theta}\left(\sin\theta\frac{\partial\Theta_l^m}{\partial\theta}\right)e^{im\phi}-\frac{m^2}{\sin^2\theta}\Theta_l^me^{im\phi}\right] \\
&= \hbar^2l(l+1)\Theta_l^me^{im\phi}
\end{aligned} \\
\frac{1}{\sin\theta}\frac{d}{d\theta}\left(\sin\theta\frac{d\Theta_l^m}{d\theta}\right)+\left[l(l+1)-\frac{m^2}{\sin^2\theta}\right]\Theta_l^m = 0 \\
x = \cos\theta,\quad \frac{d}{d\theta}=-\sin\theta\frac{d}{dx} \\
(1-x^2)\frac{d^2\Theta_l^m}{dx^2}-2x\frac{d\Theta_l^m}{dx}+\left[l(l+1)-\frac{m^2}{1-x^2}\right]\Theta_l^m = 0 \\
\Theta_l^m(x) = AP_l^m(x) \rightarrow Y_l^m(\theta,\phi)=AP_l^m(\cos\theta)e^{im\phi}
$$
{: .notice--primary}

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

$$
\begin{aligned}{}
[\hat{S}_x,\hat{S}_y] &= \frac{\hbar^2}{4}\left[\begin{pmatrix} i & 0 \\ 0 & -i \end{pmatrix}-\begin{pmatrix} -i & 0 \\ 0 & i \end{pmatrix}\right] = i\hbar\hat{S}_z \\
[\hat{S}_y,\hat{S}_z] &= \frac{\hbar^2}{4}\left[\begin{pmatrix} 0 & i \\ i & 0 \end{pmatrix}-\begin{pmatrix} 0 & -i \\ -i & 0 \end{pmatrix}\right] = i\hbar\hat{S}_x \\
[\hat{S}_z,\hat{S}_x] &= \frac{\hbar^2}{4}\left[\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}-\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}\right] = i\hbar\hat{S}_y
\end{aligned} \\
\begin{aligned}{}
\hat{S}_z \begin{pmatrix} 1 \\ 0 \end{pmatrix} &= \frac{\hbar}{2}\begin{pmatrix} 1 \\ 0 \end{pmatrix}, \quad m=\frac{1}{2} \\
\hat{S}_z \begin{pmatrix} 0 \\ 1 \end{pmatrix} &= -\frac{\hbar}{2}\begin{pmatrix} 0 \\ 1 \end{pmatrix}, \quad m=-\frac{1}{2}
\end{aligned} \\
\hat{H}=-\gamma\hat{\mathbf{S}}\cdot\mathbf{B}, \quad
\mathbf{B} = B\hat{\mathbf{z}} \rightarrow \hat{H}=-\gamma\hat{S}_zB \\
\hat{H}|\!\uparrow\rangle=-\frac{\hbar\gamma B}{2}|\!\uparrow\rangle, \quad \hat{H}|\!\downarrow\rangle=\frac{\hbar\gamma B}{2}|\!\downarrow\rangle \\
\begin{aligned}{}
|\psi(t)\rangle &= e^{-\frac{i}{\hbar}\hat{H}t}\left(a|\!\uparrow\rangle+b|\!\downarrow\rangle\right) \\
&= ae^{i\frac{\gamma B}{2}t}|\!\uparrow\rangle+be^{-i\frac{\gamma B}{2}t}|\!\downarrow\rangle \\
&= e^{i\frac{\gamma B}{2}t}\left(a|\!\uparrow\rangle+be^{-i\gamma Bt}|\!\downarrow\rangle\right) \\
\end{aligned} \\
\begin{aligned}{}
\langle S_x\rangle &= \langle\psi(t)|\hat{S}_x|\psi(t)\rangle = \hbar |ab|\cos(\gamma Bt+\phi) \\
\langle S_y\rangle &= \langle\psi(t)|\hat{S}_y|\psi(t)\rangle = -\hbar |ab|\sin(\gamma Bt+\phi) \\
\langle S_z\rangle &= \langle\psi(t)|\hat{S}_z|\psi(t)\rangle = \frac{\hbar}{2}\left(|a|^2-|b|^2\right)
\end{aligned}
$$
{: .notice--primary}

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

$$
\begin{aligned}{}
[\hat{J}_i,\hat{J}_j]
&=[\hat{J}_{1i},\hat{J}_{1j}]+[\hat{J}_{1i},\hat{J}_{2j}]+[\hat{J}_{2i},\hat{J}_{1j}]+[\hat{J}_{2i},\hat{J}_{2j}] \\
&=i\hbar \hat{J}_{1k}+0+0+i\hbar \hat{J}_{2k} =i\hbar \hat{J}_k
\end{aligned} \\
\hat{J}^2|j,m\rangle=\hbar^2j(j+1)|j,m\rangle,\quad \hat{J}_z|j,m\rangle=\hbar m|j,m\rangle \\
\hat{J}_z|j_1,m_1\rangle|j_2,m_2\rangle=\hbar(m_1+m_2)|j_1,m_1\rangle|j_2,m_2\rangle \\
m_{\max}=m_{1\max}+m_{2\max}=j_1+j_2 \\
\sum_{m_{\min}}^{m_{\max}}(2j+1)=(2j_1+1)(2j_2+1) \\
m_{\min}=\sqrt{j_1^2+j_2^2-2j_1j_2}=|j_1-j_2| \\
\begin{aligned}{}
\hat{J}_z|j_1,j_2;j,m\rangle
&=\hbar m|j_1,j_2;j,m\rangle \\
&=\hbar m\sum_{m_1,m_2}C^{jm}_{j_1m_1j_2m_2}|j_1,m_1\rangle|j_2,m_2\rangle \\
\hat{J}_z|j_1,j_2;j,m\rangle&=(\hat{J}_{1z}+\hat{J}_{2z})|j_1,j_2;j,m\rangle \\
&=\sum_{m_1,m_2}C^{jm}_{j_1m_1j_2m_2}(\hbar m_1+\hbar m_2)|j_1,m_1\rangle|j_2,m_2\rangle
\end{aligned} \\
\sum_{m_1,m_2}\hbar(m-m_1-m_2)C^{jm}_{j_1m_1j_2m_2}|j_1,m_1\rangle|j_2,m_2\rangle=0 \\
C^{jm}_{j_1m_1j_2m_2}\neq0\rightarrow m = m_1-m_2 \\
\begin{aligned}{}
\langle j_1,j_2;j,m|j_1,j_2;j',m'\rangle &=\sum_{m_1,m_2}\sum_{m_1',m_2'}C^{jm}_{j_1m_1j_2m_2}C^{j'm'}_{j_1m_1'j_2m_2'}\delta_{m_1,m_1'}\delta_{m_2,m_2'} \\
&=\sum_{m_1,m_2}C^{jm}_{j_1m_1j_2m_2}C^{j'm'}_{j_1m_1j_2m_2}\quad (C\in\mathbb{R}) \\
&=\delta_{jj'}\delta_{mm'}
\end{aligned}
$$
{: .notice--primary}


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

$$
\begin{aligned}{}
\nabla^2 &= \frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial}{\partial r}\right) + \frac{1}{r^2}\left[\frac{1}{\sin\theta}\frac{\partial}{\partial\theta}\left(\sin\theta\frac{\partial}{\partial\theta}\right) + \frac{1}{\sin^2\theta}\frac{\partial^2}{\partial\phi^2}\right] \\
&= \frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial}{\partial r}\right) - \frac{\hat{L}^2}{\hbar^2 r^2}
\end{aligned} \\
V(\mathbf{r})=V(r) \rightarrow [\hat{H}, \hat{L}^2]=0, \; [\hat{H}, \hat{L}_z]=0 \rightarrow \psi=R(r)Y_l^m(\theta, \phi) \\
\begin{aligned}{}
& -\frac{\hbar^2}{2m}\nabla^2\psi + V\psi \\
= &-\frac{\hbar^2}{2m}\left[\frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial\psi}{\partial r}\right) - \frac{\hat{L}^2}{\hbar^2 r^2}\psi\right] + V\psi \\
= &-\frac{\hbar^2}{2m}\left[\frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial R}{\partial r}\right)Y_l^m - \frac{R}{\hbar^2 r^2}\hat{L}^2Y_l^m\right] + VRY_l^m \\
= &-\frac{\hbar^2}{2m}\left[\frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial R}{\partial r}\right)Y_l^m - \frac{R}{\hbar^2 r^2}\hbar^2 l(l+1)Y_l^m\right] + VRY_l^m \\
= &ERY_l^m
\end{aligned} \\
\begin{aligned}{}
& -\frac{\hbar^2}{2m}\frac{1}{r^2}\frac{d}{dr}\left(r^2\frac{dR}{dr}\right) + \frac{\hbar^2 l(l+1)}{2mr^2}R + VR \\
= & -\frac{\hbar^2}{2m}\frac{1}{r^2}\frac{d}{dr}\left[r^2\frac{d}{dr}\left(\frac{u}{r}\right)\right] + \frac{\hbar^2 l(l+1)}{2mr^2}\frac{u}{r} + V\frac{u}{r} \\
= & -\frac{\hbar^2}{2m}\frac{1}{r}\frac{d^2u}{dr^2} + \frac{\hbar^2 l(l+1)}{2mr^2}\frac{u}{r} + V\frac{u}{r} = E\frac{u}{r}
\end{aligned}
$$
{: .notice--primary}

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

$$
-\frac{\hbar^2}{2m}\frac{1}{r^2}\frac{d}{dr}\left(r^2\frac{dR}{dr}\right) + \frac{\hbar^2 l(l+1)}{2mr^2}R = ER \\
\frac{d^2R}{dr^2} + \frac{2}{r}\frac{dR}{dr} + \left[\frac{2mE}{\hbar^2} - \frac{l(l+1)}{r^2}\right]R = 0 \\
k = \frac{\sqrt{2mE}}{\hbar}, \quad E = \frac{\hbar^2 k^2}{2m}, \quad x = kr \\
x^2\frac{d^2R}{dx^2} + 2x\frac{dR}{dx} + \left[x^2 - l(l+1)\right]R = 0 \\
R = A j_l(x) = A j_l(kr), \quad \psi = A j_l(kr)Y_l^m(\theta,\phi) \\
\psi(a,\theta,\phi) = A j_l(ka)Y_l^m(\theta,\phi) = 0, \quad ka = \alpha_{nl}
$$
{: .notice--primary}

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

$$
-\frac{\hbar^2}{2m}\left(\frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} + \frac{\partial^2}{\partial z^2}\right)\psi + \frac{1}{2}m\omega^2(x^2+y^2+z^2)\psi = E\psi \\
(\hat{H}_x+\hat{H}_y+\hat{H}_z)X(x)Y(y)Z(z) = EX(x)Y(y)Z(z) \\
\frac{\hat{H}_xX}{X} + \frac{\hat{H}_yY}{Y} + \frac{\hat{H}_zZ}{Z} = E = E_x+E_y+E_z \\
\hat{H}_x\psi_{n_x} = E_{n_x}\psi_{n_x}, \quad \hat{H}_y\psi_{n_y} = E_{n_y}\psi_{n_y}, \quad \hat{H}_z\psi_{n_z} = E_{n_z}\psi_{n_z} \\
\psi_{n_x n_y n_z}(x, y, z) = \psi_{n_x}(x)\psi_{n_y}(y)\psi_{n_z}(z) \\
\begin{aligned}{}
E &= E_{n_x}+E_{n_y}+E_{n_z} \\
&= \hbar\omega\left(n_x+\frac{1}{2}\right) + \hbar\omega\left(n_y+\frac{1}{2}\right) + \hbar\omega\left(n_z+\frac{1}{2}\right) \\
&= \hbar\omega\left(N+\frac{3}{2}\right)
\end{aligned} \\
N = n_x+n_y+n_z, \quad g_N = \frac{(N+2)!}{N!\,2!} = \frac{(N+1)(N+2)}{2}
$$
{: .notice--primary}

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

$$
-\frac{\hbar^2}{2m}\frac{d^2u}{dr^2} + \left[-\frac{e^2}{4\pi\varepsilon_0 r} + \frac{\hbar^2 l(l+1)}{2mr^2}\right]u = Eu \\
a_0 = \frac{4\pi\varepsilon_0\hbar^2}{me^2}, \quad \kappa^2 = -\frac{2mE}{\hbar^2}, \quad \rho = \kappa r \\
\frac{d^2u}{dr^2} + \left[\frac{2}{a_0r} - \frac{l(l+1)}{r^2} - \kappa^2\right]u = 0 \\
\begin{aligned}{}
& r \to 0: && \frac{d^2u}{dr^2} \simeq \frac{l(l+1)}{r^2}u, && u \sim r^{l+1} \\
& r \to \infty: && \frac{d^2u}{dr^2} \simeq \kappa^2u, && u \sim e^{-\kappa r}
\end{aligned} \\
R(r) = \frac{u(r)}{r} = e^{-\rho}\rho^l v(\rho) \\
-\frac{\hbar^2}{2m}\frac{1}{r^2}\frac{d}{dr}\left(r^2\frac{dR}{dr}\right) + \left[-\frac{e^2}{4\pi\varepsilon_0 r} + \frac{\hbar^2 l(l+1)}{2mr^2}\right]R = ER \\
\frac{d^2R}{dr^2} + \frac{2}{r}\frac{dR}{dr} + \left[\frac{2}{a_0r} - \frac{l(l+1)}{r^2} - \kappa^2\right]R = 0 \\
\rho\frac{d^2v}{d\rho^2} + (2l+2-2\rho)\frac{dv}{d\rho} + \left(\frac{2}{a_0\kappa} -2l-2\right)v = 0 \\
x\frac{d^2v}{dx^2} + (2l+2-x)\frac{dv}{dx} + \left(\frac{1}{a_0\kappa} -l-1\right)v = 0 \\
\frac{1}{a_0\kappa}=n, \quad n=1,2,3,\cdots \\
n-l-1\geq 0, \quad l=0,1,\cdots,n-1 \\
\kappa = \frac{1}{na_0}, \quad \rho=\frac{r}{na_0} \\
v = L_{n-l-1}^{2l+1}(x) = L_{n-l-1}^{2l+1}(2\rho) \\
\psi = Ae^{-\rho}\rho^l L_{n-l-1}^{2l+1}(2\rho) Y_l^m(\theta,\phi) \\
E = -\frac{\hbar^2}{2ma_0^2}\frac{1}{n^2} = -\frac{me^4}{2(4\pi\varepsilon_0)^2\hbar^2}\frac{1}{n^2}
$$
{: .notice--primary}

### Electromagnetic Potential / 電磁ポテンシャル

$$
\begin{aligned}{}
& \hat{H}\psi = \left[\frac{1}{2m}(\hat{\mathbf{p}} - q\mathbf{A})^2 + q\Phi\right]\psi = i\hbar\frac{\partial\psi}{\partial t} \\
& \mathbf{A}' = \mathbf{A} + \nabla\chi, \quad \Phi' = \Phi - \frac{\partial\chi}{\partial t}, \quad \psi' = e^{\frac{i}{\hbar}q\chi}\psi \\
& \hat{H'}\psi' = \left[\frac{1}{2m}(\hat{\mathbf{p}} - q\mathbf{A'})^2 + q\Phi'\right]\psi' = i\hbar\frac{\partial\psi'}{\partial t} \\
\end{aligned}
$$
{: .notice--info}

$$
\begin{aligned}{}
(\hat{\mathbf{p}}-q\mathbf{A}')\psi' &= \left( -i\hbar\nabla -q\mathbf{A} -q\nabla\chi \right) e^{\frac{i}{\hbar}q\chi}\psi \\
&= e^{\frac{i}{\hbar}q\chi} \left( -i\hbar\nabla -q\mathbf{A} \right)\psi \\
(\hat{\mathbf{p}}-q\mathbf{A}')^2\psi' &= e^{\frac{i}{\hbar}q\chi} \left( -i\hbar\nabla -q\mathbf{A} \right)^2\psi \\
\frac{(\hat{\mathbf{p}}-q\mathbf{A}')^2}{2m}\psi' &= e^{\frac{i}{\hbar}q\chi} \frac{(\hat{\mathbf{p}}-q\mathbf{A})^2}{2m}\psi \\
q\Phi'\psi' &= q\left( \Phi-\frac{\partial\chi}{\partial t} \right) e^{\frac{i}{\hbar}q\chi}\psi \\
&= e^{\frac{i}{\hbar}q\chi}q\Phi\psi - q\frac{\partial\chi}{\partial t} e^{\frac{i}{\hbar}q\chi}\psi \\
i\hbar\frac{\partial\psi'}{\partial t} &= i\hbar\frac{\partial}{\partial t} \left( e^{\frac{i}{\hbar}q\chi}\psi \right) \\
&= e^{\frac{i}{\hbar}q\chi} i\hbar\frac{\partial\psi}{\partial t} - q\frac{\partial\chi}{\partial t} e^{\frac{i}{\hbar}q\chi}\psi \\
\hat{H}'\psi' - i\hbar\frac{\partial\psi'}{\partial t} &= e^{\frac{i}{\hbar}q\chi} \left( \hat{H}\psi - i\hbar\frac{\partial\psi}{\partial t} \right) =0
\end{aligned}
$$
{: .notice--primary}

### Charged Particle / 荷電粒子

$$
\begin{aligned}{}
& E_{n,k_z} = \hbar\omega_c\left(n+\frac{1}{2}\right) + \frac{\hbar^2 k_z^2}{2m}, \quad \omega_c=\frac{|q|B}{m} \\
& \psi = \psi_0 \exp\left(\frac{i}{\hbar}q\int_C \mathbf{A}\cdot d\mathbf{l}\right),\quad \Delta\varphi = \frac{q}{\hbar}\int_S \mathbf{B}\cdot d\mathbf{S}
\end{aligned}
$$
{: .notice--info}

$$
\mathbf{B}=B\hat{\mathbf{z}}, \quad \nabla\times\mathbf{A}=\mathbf{B} \to \mathbf{A}=Bx\hat{\mathbf{y}} \\
\hat{H} = \frac{1}{2m} \left[ \hat{p}_x^2 + (\hat{p}_y-qBx)^2 + \hat{p}_z^2 \right] \\
[\hat{H},\hat{p}_y]=0, \quad [\hat{H},\hat{p}_z]=0 \to \psi=e^{ik_y y}e^{ik_z z}X(x) \\
\begin{aligned}{}
\hat{H}\psi &= \frac{1}{2m} \left[ \hat{p}_x^2 + (\hbar k_y-qBx)^2 + (\hbar k_z)^2 \right]\psi \\
&= \left[ \frac{\hat{p}_x^2}{2m} + \frac{q^2B^2}{2m} \left(x-\frac{\hbar k_y}{qB}\right)^2 + \frac{\hbar^2k_z^2}{2m} \right]\psi \\
&= \left[ \frac{\hat{p}_x^2}{2m} + \frac{m\omega_c^2}{2}(x-x_0)^2 + \frac{\hbar^2k_z^2}{2m} \right]\psi
\end{aligned}
\\
\omega_c = \frac{|q|B}{m}, \quad E = \hbar\omega_c\left(n+\frac{1}{2}\right) + \frac{\hbar^2k_z^2}{2m} \\
\mathbf{A}_0 = \mathbf{A}+\nabla\chi=0 \to \mathbf{A}=-\nabla\chi, \quad \chi=-\int_{\mathbf{r}_0}^{\mathbf{r}}\mathbf{A}\cdot d\mathbf{l} \\
\psi_0 = \psi e^{\frac{i}{\hbar}q\chi} \to \psi = \psi_0 e^{-\frac{i}{\hbar}q\chi} = \psi_0 \exp\left( \frac{i}{\hbar}q\int_C\mathbf{A}\cdot d\mathbf{l} \right) \\
\begin{aligned}{}
\Delta\varphi &= \frac{q}{\hbar}\int_{C_1}\mathbf{A}\cdot d\mathbf{l} - \frac{q}{\hbar}\int_{C_2}\mathbf{A}\cdot d\mathbf{l} \\
&= \frac{q}{\hbar}\oint_C\mathbf{A}\cdot d\mathbf{l} = \frac{q}{\hbar}\int_S(\nabla\times\mathbf{A})\cdot d\mathbf{S} \\
&= \frac{q}{\hbar}\int_S\mathbf{B}\cdot d\mathbf{S} = \frac{q\Phi_B}{\hbar}
\end{aligned}
$$
{: .notice--primary}


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

<!-- # Physical Mathematics / 物理数学

## Calculus / 微積分

## Complex Analysis / 複素解析

## Ordinary Differential Equation / 常微分方程式

## Partial Differential Equation / 偏微分方程式

## Special Function / 特殊関数

## Linear Algebra / 線形代数

## Abstract Algebra / 抽象代数

## Vector Analysis / ベクトル解析

## Differential Geometry / 微分幾何 -->

<!-- # Condensed Matter Physics / 物性物理学

# Particle Physics / 素粒子物理学

# Theory of Relativity / 相対性理論

# Quantum Field Theory / 場の量子論 -->
