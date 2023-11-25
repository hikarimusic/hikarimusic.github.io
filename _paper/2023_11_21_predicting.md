---
title: 'Predicting Electron Distributions in Drug Molecules Using Density Functional Theory in Real Space'
date: 2023-11-21
permalink: /paper/2023_11_21_predicting
tags:
  - paper
---

Electron distributions in drug molecules are crucial in drug design and can be predicted using density functional theory (DFT). We propose a comprehensive scheme to perform DFT calculations in real space instead of using the conventional orbital basis set. We detail the implementation of spherical space and basis, Pulay's density mixing, Hamiltonian matrix construction, Kohn-Sham equation solution, and Bader's charge analysis in discretized coordinate basis. We demonstrate that the demanding computation can be carried out in a highly parallel manner with simple codes by exploiting efficient algorithms in the PyTorch and NumPy packages. We perform calculations on the drug acyclovir and predict the electron distribution, partial charges, and energy levels in the molecule. The study may facilitate research in computational molecular science and structure-based drug design.

**Tung, Yeu-Guang (2023). Predicting Electron Distributions in Drug Molecules Using Density Functional Theory in Real Space. figshare. Preprint. [https://doi.org/10.6084/m9.figshare.24598284.v1](https://doi.org/10.6084/m9.figshare.24598284.v1)**

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Responsive A4 Aspect Ratio</title>
</head>
<body>

<iframe id="myIframe" src="https://widgets.figshare.com/articles/24598284/embed?show_title=1" width="100%" height="100%" allowfullscreen frameborder="0"></iframe>

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
