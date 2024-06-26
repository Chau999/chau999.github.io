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
        .thumbnail {
            float: right;
            margin-left: 10px;
            width: auto; /* Adjust the size as needed */
            height: 100px; /* Adjust the size as needed */
        }
        .pubitem {
            overflow: hidden;
        }
</style>


<div>
<h2> Publications </h2>
My research mainly spans across the topics of <span style ="color: orangered">Uncertainty-aware ML</span>
(<span class="paper_type_UAI">UAI</span>), <span style ="color: blue">Explanation in ML</span>(<span class="paper_type_XAI">XAI</span>), and <span style="color: green"> Preference Modelling</span>(<span class="paper_type_pl">PM</span>).
</div>
<br>

{% assign publications = site.publications | where: "preprint", "false" | sort: "year" | reverse %}
{% for pub in publications%}
  <div class="pubitem">
    <div class="pubtitle">
{% if pub.thumbnail %}
        <img class="thumbnail" src="{{ pub.thumbnail }}" alt="Thumbnail">
      {% endif %}
      {{forloop.rindex}}. {{ pub.title }} 
        {% if pub.UAI %}
            <span class="paper_type_UAI">UAI</span>
        {% endif %}
        {% if pub.XAI %}
            <span class="paper_type_XAI">XAI</span>
        {% endif %}
        {% if pub.PM %}
            <span class="paper_type_pl">PM</span>
        {% endif %}
    </div>
    <div class="pubauthors">{{ pub.authors }}</div>
    <div class="pubinfo">
        <span style="color: red">{{ pub.award }}</span> {{ pub.venue }}, {{ pub.year }}
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
