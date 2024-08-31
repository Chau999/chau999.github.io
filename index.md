---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
title: Personal Website
position: Postdoctoral Researcher
location: CISPA Helmholtz Center for Information Security
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
            font-weight: bold;
        }
        dd {
            margin-left: 120px; /* Adjust this value for tab distance */
        }
</style>

## Welcome <i class="em em-wave" aria-role="presentation" aria-label="WAVING HAND SIGN"></i>

<p align="justify">

Hello! My name is Siu Lun Chau (周兆麟), currently a postdoctoral researcher at the <a href="https://ri-lab.org/">Rational Intelligence Lab</a> within 
<a href="https://cispa.de">CISPA</a> Helmholtz Center for Information Security in Germany. I work under the guidance of 
<a href="https://www.krikamol.org/">Dr. Krikamol Muandet</a>, focusing on developing machine learning models that acknowledge what they don't know, and effectively communicating what they know. 
To achieve this goal, we need better methods for modelling **uncertainty**, **explanability**, and **preferences**.
</p>

<p align="justify">
Before joining CISPA, I obtanied my DPhil in Statistical Machine Learning from the University of Oxford, where I specialised in kernel methods and Gaussian processes under the supervision of <a href="https://sejdino.github.io/">Prof. Dino Sejdinovic</a>. I also interned at Amazon as an Applied Scientist, where I tackled coherent forecasting problems for the EU logistics network. I also interned at the Max Planck Institute for Intelligent Systems, where I worked on improving econometric models with modern machine learning approaches.
</p>

<p align="justify">
I hold both a master's and undergraduate degree in Mathematics and Statistics with First Class Honours from the University of Oxford. During my master's, I worked with <a href="https://www.vanderschaar-lab.com/">Prof. Mihaela van der Schaar</a> on modelilng diseases trajectories using Bayesian nonparametric methods.
</p>

<p align="justify">
You can read more about my research interests <a href="https://chau999.github.io/research/">here</a>. Please do not hesitate to reach out if you would like to collaborate, I am always excited to hear from you :)
</p>

<br>

### Recent Updates 🔔

{% assign news = site.news | sort: "date" | reverse %}
<div class="small-text">
<dl>
{% for new in news limit: 100 %}
<dt>{{ new.date |date: "%b-%Y"}}</dt>
<dd>{{ new.content }}</dd>
{% endfor %}
</dl>
</div>


<br>

### Upcoming/Recent Talks 🗣️
{% assign talks = site.talks | sort: "date" | reverse %}
<div class="small-text">
<dl>
{% for talk in talks limit: 100 %}
<dt>{{ talk.date |date: "%b-%Y"}}</dt>
<dd><b>{{ talk.talk_title }}</b> 
<br> - <i>{{talk.venue}}</i></dd>
{% endfor %}
</dl>
</div>



