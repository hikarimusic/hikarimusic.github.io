---
permalink: /
title: "About"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I am 董宇光 (Yeu-Guang Tung), a medical student studying at the School of Medicine, National Taiwan University. I had been learning physics in high school and am currently studying medicine and algorithms. I am interested in the application of computational physics in drug discovery.

* National Taiwan University School of Medicine
* International Physics Olympiad Silver Medal
* 東京大学一般選抜：理科一類 +32 点合格点超え

## Paper

{% include base_path %}
{% capture written_year %}'None'{% endcapture %}
{% for post in site.paper reversed %}
  {% capture year %}{{ post.date | date: '%Y' }}{% endcapture %}
  {% if year != written_year %}
    {% capture written_year %}{{ year }}{% endcapture %}
  {% endif %}
  {% include archive-single.html %}
{% endfor %}

## Software

{% include base_path %}
{% capture written_year %}'None'{% endcapture %}
{% for post in site.software reversed %}
  {% capture year %}{{ post.date | date: '%Y' }}{% endcapture %}
  {% if year != written_year %}
    {% capture written_year %}{{ year }}{% endcapture %}
  {% endif %}
  {% include archive-single.html %}
{% endfor %}

## Music

{% include base_path %}
{% capture written_year %}'None'{% endcapture %}
{% for post in site.music reversed %}
  {% capture year %}{{ post.date | date: '%Y' }}{% endcapture %}
  {% if year != written_year %}
    {% capture written_year %}{{ year }}{% endcapture %}
  {% endif %}
  {% include archive-single.html %}
{% endfor %}