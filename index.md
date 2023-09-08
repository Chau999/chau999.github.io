---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
title: Personal Website
position: Postdoctoral Researcher
location: CISPA Helmholtz Center for Information Security
---

## Hello <i class="em em-wave" aria-role="presentation" aria-label="WAVING HAND SIGN"></i>

<p align="justify">
I am currently a postdoctoral researcher at the <a href="https://cispa.de">CISPA Helmholtz Center for Information Security</a> working with
<a href="http://group.krikamol.org/">Dr. Krikamol Muandet</a> in Saarbrücken, Germany. Prior to joining CISPA,
I pursued my DPhil within the <a href="https://csml.stats.ox.ac.uk/">Oxford Computational Statisics and Machine Learning Group</a> at the
University of Oxford, under the supervision of <a href="https://sejdino.github.io/">Prof. Dino Sejdinovic</a>,
<a href="http://www.stats.ox.ac.uk/~cucuring/">Prof. Mihai Cucuringu</a> and <a href="https://web.media.mit.edu/~xdong/">Prof. Xiaowen Dong</a>. 
During my DPhil, I have interned at <a href="https://www.amazon.jobs/de/business_categories/transport">Amazon Transportation Service group</a>
as an Applied Scientist working on coherent forecasting problems for the EU logistics network.
I have also interned at the <a href="https://ei.is.mpg.de/">Max Planck Institute for Intelligent Systems</a> where I 
worked on improving econometric models with modern machine learning methods. I previously obtained
a masters and bachelor degree with first class honours in mathematics and statistics at the University of Oxford. During my masters,
I worked with <a href="https://www.vanderschaar-lab.com/">Prof. Mihaela Van Der Schaar</a> on disease trajectory modelling with Bayesian nonparametric models.
</p>

<p align="justify">
My current research focuses on improving the reliability of machine learning algorithms by integrating principles from game theory and statistical methodologies. 
I have also worked on broader areas of machine learning including model explainability and uncertainty quantification,
kernel methods and Gaussian processes, causal inference and econometrics, ranking and preference learning, and graph machine learning. 
</p>

<p align="justify">
Do not hesitate to reach out if you would like to collaborate, I am always excited to hear from you :)
</p>

<br>


## Updates 🔔
{% assign news = site.news | sort: "date" | reverse %}
<ul>
{% for new in news limit: 5 %}
<li>{{ new.date |date: "%b-%Y" }}: {{ new.blob }}</li>
{% endfor %}
</ul>
