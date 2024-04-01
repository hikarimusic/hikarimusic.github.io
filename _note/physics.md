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

### Newtonian Mechanics / ニュートン力学

$$
\begin{align*}
& \mathbf{F} = \frac{d\mathbf{P}}{dt} && \mathbf{P} = m\mathbf{v} && \\
& \mathbf{N} = \frac{d\mathbf{L}}{dt} && \mathbf{L} = m\mathbf{r}\times\mathbf{v} && \mathbf{N} = \mathbf{r}\times\mathbf{F} \\
& A = \frac{dE}{dt} && E = \frac{1}{2}m|\mathbf{v}|^2 + U && A = \mathbf{F^{(nc)}}\cdot\mathbf{v}
\end{align*}
$$
{: .notice--info}

$$
\begin{align*}
& \mathbf{F} = \frac{d\mathbf{P}}{dt} && \mathbf{P} = M\mathbf{V} && \mathbf{F} = \sum_{i}\mathbf{F^{(e)}_i} \\
& \mathbf{N} = \frac{d\mathbf{L}}{dt} && \mathbf{L} = M\mathbf{R}\times\mathbf{V} + \sum_{i}m_i\mathbf{r'_i}\times\mathbf{v'_i} && \mathbf{N} = \sum_{i}\mathbf{r_i}\times\mathbf{F^{(e)}_i} \\
& A = \frac{dE}{dt} && E = \frac{1}{2}M|\mathbf{V}|^2 + \sum_{i}\frac{1}{2}m_i|\mathbf{v'_i}|^2 + U && A = \sum_{i}\mathbf{F^{(nc)}_i}\cdot\mathbf{v_i}
\end{align*}
$$
{: .notice--info}

### Lagrangian Mechanics / ラグランジュ力学

$$
\begin{align*}
& \delta\int_{t_1}^{t_2}L(q_i, \dot{q_i}, \dots, t)\,dt = 0 && L = T - U \\
& \frac{\partial{L}}{\partial{q_i}} - \frac{d}{dt}\frac{\partial{L}}{\partial{\dot{q_i}}} = 0 \\
& \frac{\partial{L}}{\partial{q_i}} - \frac{d}{dt}\frac{\partial{L}}{\partial{\dot{q_i}}} + \sum_{j}\lambda_j\frac{\partial{F_j}}{\partial{q_i}} = 0
\end{align*}
$$
{: .notice--info}

$$
\begin{align*}
& H(q_i, p_i, \dots) = \sum_{j}\dot{q_j}\frac{\partial{L}}{\partial{\dot{q_j}}} - L \\
& \dot{q_i} = \quad\frac{\partial{H}}{\partial{p_i}} \\
& \dot{p_i} = -\frac{\partial{H}}{\partial{q_i}}
\end{align*}
$$
{: .notice--info}

### Conservation Law / 保存則

$$
\begin{align*}
& \mathbf{P} = const. && \mathbf{F} = 0 && U = const. \\
& \mathbf{L} = const. && \mathbf{r}\times\mathbf{F} = 0 && U = U(|\mathbf{r}|) \\
& E = const. && \mathbf{F^{(nc)}}\cdot\mathbf{v} = 0 && U = U(\mathbf{r})
\end{align*}
$$
{: .notice--info}

$$
\begin{align*}
& \mathbf{P} = const. && \sum_{i}\mathbf{F^{(e)}_i} = 0 && U = \sum_{i,j}U_{ij}(|\mathbf{r_i}-\mathbf{r_j}|) \\
& \mathbf{L} = const. && \sum_{i}\mathbf{r_i}\times\mathbf{F^{(e)}_i} = 0 && U = \sum_{i}U(|\mathbf{r_i}|)+\sum_{i,j}U_{ij}(|\mathbf{r_i}-\mathbf{r_j}|) \\
& E = const. && \sum_{i}\mathbf{F^{(nc)}_i}\cdot\mathbf{v_i} = 0 && U = U(\mathbf{r_i},\dots)
\end{align*}
$$
{: .notice--info}

## Electrodynamics / 電磁気学

## Thermodynamics / 熱力学

## Quantum Mechanics / 量子力学