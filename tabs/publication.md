---
layout: page
title: Publications
permalink: /pubs/
---

<style>
.small-text {
    font-size: 0.9em;
}
        dt {
            float: left;
            clear: left;
            width: 100px;
            text-align: left;
            color: royalblue;
        }
        dd {
            margin-left: 120px; /* Adjust this value for tab distance */
        }
</style>

#### <ins>Preprints</ins>

{% assign publications = site.publications | where: "preprint", "true" | sort: "year" | reverse %}
{% for pub in publications%}
  <div class="pubitem">
    <dl>
    <dt>{{pub.venue_short}}</dt>
    <dd>
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
    </dd>
    </dl>
</div>

<br>
{% endfor %}

#### <ins>Published</ins>
{% assign publications = site.publications | where: "preprint", "false" | sort: "year" | reverse %}
{% for pub in publications%}
  <div class="pubitem">
    <dl>
    <dt>{{pub.venue_short}}</dt>
    <dd>
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
    </dd>
    </dl>
</div>
<br>
{% endfor %}
