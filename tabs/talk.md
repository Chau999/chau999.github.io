---
layout: page
title: Presentations
permalink: /talk/
---

[//]: # ({% assign talks = site.talks | sort: "date" | reverse %})

[//]: # ({% for talk in talks %})

[//]: # (<div class="talk_info">)

[//]: # (    <p class="talk_title">"{{ talk.talk_title }}"</p> )

[//]: # (    <p class="talk_date">{{ talk.date_ }}</p>)

[//]: # (</div>)

[//]: # (<br>)

[//]: # (<div class="location_info">)

[//]: # (    <p class="talk_venue">{{ talk.venue }}</p> )

[//]: # (    <p class="talk_location">{{ talk.location }}</p>)

[//]: # (</div>)

[//]: # (<br>)

[//]: # ({% endfor %})

<style>
.small-text {
    font-size: 0.9em;
}
        dt {
            float: left;
            clear: left;
            width: 100px;
            text-align: left;
            font-weight: bold;
        }
        dd {
            margin-left: 120px; /* Adjust this value for tab distance */
        }
</style>


# Invited Presentations
{% assign talks = site.talks | sort: "date" | reverse %}
<div class="small-text">
<dl>
{% for talk in talks limit: 100%}
<dt>{{ talk.date |date: "%b-%Y"}}</dt>
<dd><b>{{ talk.talk_title }}</b> 
<br> - <i>{{talk.venue}}</i></dd>
<br>
{% endfor %}
</dl>
</div>