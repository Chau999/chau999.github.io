---
layout: page
title: Invited Talk
permalink: /talk/
---

{% assign talks = site.talks | sort: "date" | reverse %}
{% for talk in talks %}
<div class="talk_info">
    <p class="talk_title">"{{ talk.talk_title }}"</p> 
    <p class="talk_date">{{ talk.date_ }}</p>
</div>
<br>
<div class="location_info">
    <p class="talk_venue">{{ talk.venue }}</p> 
    <p class="talk_location">{{ talk.location }}</p>
</div>
<br>
{% endfor %}