---
permalink: /
title: "About"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I am 董宇光, a medical student studying at the School of Medicine, National Taiwan University. I had been learning physics in high school and am currently studying medicine and algorithms. I am interested in cancer genomics and structural biology.

* International Physics Olympiad: Silver Medal
* 東京大学一般選抜：理一プラス４３点理三落ち

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
