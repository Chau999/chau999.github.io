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
Hello! My name is Siu Lun Chau (兆麟 周). I am a postdoctoral researcher at the <a href="https://ri-lab.org/">Rational Intelligence Lab</a> of <a href="https://cispa.de">CISPA Helmholtz Center for Information Security</a> working with
<a href="[http://group.krikamol.org/](https://ri-lab.org/)">Dr. Krikamol Muandet</a> on Trustworthy Machine Learning in Saarbrücken, Germany. Prior to joining CISPA,
I pursued my DPhil within the <a href="https://csml.stats.ox.ac.uk/">Oxford Computational Statisics and Machine Learning Group</a> at the
University of Oxford, under the supervision of <a href="https://sejdino.github.io/">Prof. Dino Sejdinovic</a>,
<a href="http://www.stats.ox.ac.uk/~cucuring/">Prof. Mihai Cucuringu</a> and <a href="https://web.media.mit.edu/~xdong/">Prof. Xiaowen Dong</a>. 
During my DPhil, I interned at <a href="https://www.amazon.jobs/de/business_categories/transport">Amazon Transportation Service group</a>
as an Applied Scientist working on coherent forecasting problems for the EU logistics network.
I have also interned at the <a href="https://ei.is.mpg.de/">Max Planck Institute for Intelligent Systems</a> where I 
worked on improving econometric models with modern machine learning methods. I previously obtained
a masters and bachelor degree with first class honours in mathematics and statistics at the University of Oxford. During my masters,
I worked with <a href="https://www.vanderschaar-lab.com/">Prof. Mihaela Van Der Schaar</a> on disease trajectory modelling with Bayesian nonparametric models.
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



