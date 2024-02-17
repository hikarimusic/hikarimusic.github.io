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