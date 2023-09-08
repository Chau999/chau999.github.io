---
layout: page
title: Publication
permalink: /pubs/
---

*, † denote equal contributions.

{% assign publications = site.publications | sort: "year" | reverse %}
{% for pub in publications%}
  <div class="pubitem">
    <div class="pubtitle">
      {{forloop.rindex}}. {{ pub.title }}
    </div>
    <div class="pubauthors">{{ pub.authors }}</div>
    <div class="pubinfo">
        {{ pub.venue }}, {{ pub.year }}
    </div>
    <div class="publinks">
      {% if pub.pdf %}
            <a href="{{ pub.pdf }}">
              <span class="border">PDF</span> 
            </a>
          {% endif %}
      {% if pub.code %}
        <a href="{{ pub.code }}">
            <span class="border">Code</span>
        </a>
      {% endif %}
      {% if pub.video %}
        <a href="{{ pub.video }}">
            <span class="border">Video</span>
        </a>
      {% endif %}
      {% if pub.poster %}
        <a href="{{ pub.poster }}">
          <i class="fas fa-image"></i>
        </a>
      {% endif %}
    </div>
</div>
<br>
{% endfor %}