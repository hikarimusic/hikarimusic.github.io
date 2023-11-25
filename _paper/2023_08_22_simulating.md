---
title: 'Simulating Evolution of Multi-Particle System with GPU Acceleration in PyTorch'
date: 2023-08-22
permalink: /paper/2023_08_22_simulating
tags:
  - paper
---

Simulating the evolution of a system of particles based on physical laws can be computational costly. We propose a simple way to perform GPU acceleration using PyTorch. Taking advantage of the efficient matrix operations and gradient calculations in PyTorch, we can readily accelerate the simulation using GPU. We showed that this method produces correct simulation results and runs significantly faster then when using CPU.

**Tung, Yeu-Guang (2023). Simulating Evolution of Multi-Particle System with GPU Acceleration in PyTorch. figshare. Preprint. [https://doi.org/10.6084/m9.figshare.24002613.v2](https://doi.org/10.6084/m9.figshare.24002613.v2)**

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Responsive A4 Aspect Ratio</title>
</head>
<body>

<iframe id="myIframe" src="https://widgets.figshare.com/articles/24002613/embed?show_title=1" width="100%" height="100%" allowfullscreen frameborder="0"></iframe>

<script>
    // Function to set the height based on the A4 aspect ratio
    function setA4AspectRatio() {
        var iframe = document.getElementById('myIframe');
        var width = iframe.offsetWidth;
        var height = width * 1.41; // A4 aspect ratio

        // Set the calculated height
        iframe.style.height = height + 'px';
    }

    // Call the function on page load
    window.addEventListener('load', setA4AspectRatio);

    // Update the height whenever the window is resized
    window.addEventListener('resize', setA4AspectRatio);
</script>

</body>
</html>
