---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
title: Personal Website
position: Assistant Professor in Statistical Machine Learning
location: College of Computing and Data Science, Nanyang Technological University, Singapore
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

<p align="justify" style="color:darkblue;">🚨🚨 PhD Opportunities: Interested in bringing in epistemic intelligence to machine learning systems?
I have several openings for PhD students to start in Aug 2026 to be based in Singapore and are looking for candidates with a strong 
mathematical, statistical, or machine learning background. More details can be found <a href="https://chau999.github.
io/group/">here</a>.</p>


<h2> Welcome </h2>

<p align="justify">

Hi, my name is Siu Lun (Alan) Chau. I am an Assistant Professor in Statistical Machine Learning at the <a href="https://www.ntu.edu.

sg/computing">College of Computing and Data Science, Nanyang Technological University (NTU), Singapore</a>. I lead the 

<a href="https://chau999.github.io/group">Epistemic Intelligence & Computation 

(EPIC) Lab</a>, understanding and addressing epistemic uncertainty in machine learning—how to represent, quantify, propagate, compare, and explain knowledge-level uncertainty in intelligent systems.

<p align="justify">

<b> Background. </b> From 2023 to 2025, I was a Postdoctoral Researcher at the <a href="https://ri-lab.org/">Rational

Intelligence Lab</a> within CISPA Helmholtz Center for Information Security, Germany,

under the supervision of <a href="https://www.krikamol.org/">Dr. Krikamol Muandet</a>. Between 2019 and 2023, I 

pursued my DPhil in Statistics at the <a href="https://csml.stats.ox.ac.uk/">University of Oxford</a> under the 

supervision of <a href="https://sejdino.github.io/">Prof. Dino Sejdinovic</a>. 

During my doctoral studies, I also interned at the <a href="https://ei.is.mpg.de/">

Empirical Inference department of the Max Planck Institute for Intelligent Systems, Tübingen</a> and Amazon UK. 

I hold both a Master’s and a Bachelor’s degree in Mathematics and Statistics, graduating with First Class Honours from the University of Oxford, 
where I received the Departmental Prize for ranking top of the cohort.

</p>





<br>

<h2> News</h2>

{% assign news = site.news | sort: "date" | reverse %}
<div class="small-text">
<dl>
{% for new in news limit: 5 %}
<dt>{{ new.date |date: "%b-%Y"}}</dt>
<dd>{{ new.content }}</dd>
{% endfor %}
</dl>
</div>




