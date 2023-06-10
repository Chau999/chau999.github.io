---
layout: page
title: Publication
permalink: /pubs/
---

<style>
.pubitem {
  margin: 0em 0;
  line-height: 1em;
}
.pubtitle {
  margin-bottom: 0.5em;
  line-height: 1.2em;
  font-weight: bold;
}
.pubauthors,
.pubinfo {
  font-size: 75%;
  margin-bottom: 0.75em;
}
</style>

{% assign publications = site.publications | sort: "year" | reverse %}
{% for pub in publications %}
  <div class="pubitem">
    <div class="pubtitle">
      {{forloop.rindex}}. {{ pub.title }}
    </div>
    <div class="pubauthors">{{ pub.authors }}</div>
    <div class="pubinfo">{{ pub.venue }}, {{ pub.year }}</div>
  <br>
</div>
{% endfor %}