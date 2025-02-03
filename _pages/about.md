---
permalink: /
title: "About"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I am 董宇光, a medical student studying at National Taiwan University. As an amateur researcher, I enjoy writing papers. As an amateur engineer, I enjoy developing software. As an amateur composer, I enjoy creating music. As a professional student, I enjoy learning medicine, physics, and algorithms. If you have any hobbies in common, I would be happy to have some discussions with you.

* 2020: National Taiwan University School of Medicine
* 2018: International Physics Olympiad Silver Medal

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
