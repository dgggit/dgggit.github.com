---
layout: page
permalink: /publications/
title: Publications
description: 
years: [2021, 2022, 2023, 2024, 2025]
nav: true
headerOrder: 2
---

<div class="publications">

(to be achieved.)

{% for y in page.years %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f papers -q @*[year={{y}}]* %}
{% endfor %}

</div>
