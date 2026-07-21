---
permalink: /
title: "About"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

Welcome to HikariMusic Site, I am [董宇光]({% link _pages/cv.md %}) from Taiwan.

* As an amateur researcher, I write papers under the name [Uko To](https://www.researchgate.net/profile/Yeu-Guang-Tung)
* As an amateur composer, I create music under the name [HIKARINO](https://eggs.mu/artist/HikariMusic)
* As an amateur engineer, I develop software under the name [HikariMusic](https://github.com/hikarimusic)
* As a medicine enthusiast, 🍊⭐
* As a physics enthusiast, I won a silver medal in [IPHO](https://ipho-unofficial.org/countries/TWN/individual#:~:text=Yeu-Guang%20Tung)
* As an algorithm enthusiast, 🍊⭐

## News

{% include base_path %}
{% assign all_posts = site.paper | concat: site.software | concat: site.music | sort: 'date' %}
{% capture written_year %}'None'{% endcapture %}
{% for post in all_posts reversed %}
  {% capture year %}{{ post.date | date: '%Y' }}{% endcapture %}
  {% if year != written_year %}
    {% capture written_year %}{{ year }}{% endcapture %}
  {% endif %}
  {% include archive-single.html %}
{% endfor %}
