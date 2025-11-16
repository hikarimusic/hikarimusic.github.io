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
* 2019: International Physics Olympiad Silver Medal

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
