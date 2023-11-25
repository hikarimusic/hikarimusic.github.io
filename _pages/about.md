---
permalink: /
title: "About"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I am 董宇光 (Yeu-Guang Tung), a medical student at school of medicine, National Taiwan University. I had been learning physics in high school, and am learning medicine and algorithm currently. I am intesrested in the application of computational physics in drug discovery.

* 東京大学一般選抜：理科一類 +32 点合格ライン超え（理三落ちAランク）
* 台湾大学医学部医学科：進学
* 国際物理オリンピック：銀メダル

脳の細胞は増えないが、パラメーターは多分変えらます。

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

## Note

{% include base_path %}
{% capture written_year %}'None'{% endcapture %}
{% for post in site.note reversed %}
  {% capture year %}{{ post.date | date: '%Y' }}{% endcapture %}
  {% if year != written_year %}
    {% capture written_year %}{{ year }}{% endcapture %}
  {% endif %}
  {% include archive-single.html %}
{% endfor %}
