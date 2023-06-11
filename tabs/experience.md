---
layout: page
title: Experience
permalink: /exp/
---

{% assign experience = site.experiences | sort: "year" | reverse %}
{% for exp in experience %}
<div class="exp_first_line">
    <p class="exp_position">{{ exp.position }}</p> 
    <p class="exp_duration">{{ exp.duration }}</p>
</div>
<br>
<div class="exp_second_line">
    <p class="exp_company">{{ exp.company }}</p> 
    <p class="exp_location">{{ exp.location }}</p>
</div>
<br>
{% endfor %}