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
I have several openings for PhD students to start in Jan/Aug 2026 to be based in Singapore and are looking for candidates with a strong 
mathematical, statistical, or machine learning background. More details can be found <a href="https://chau999.github.
io/group/">here</a>.</p>

<p align="justify" style="color:red;">
Due to the high volume of applications, I may not be able to respond to every email. Thank you for your understanding.
</p>

<h2> Welcome </h2>
<p align="justify">
Hi, my name is Siu Lun (Alan) Chau. I am an Assistant Professor in Statistical Machine Learning at the <a href="https://www.ntu.edu.
sg/computing">College of Computing and Data Science, Nanyang Technological University (NTU), Singapore</a>. I lead the 
<b>Epistemic Intelligence & Computation 
(EPIC) Lab</b>, where the mission is to develop intelligent systems that can recognise their own limitations and communicate
what they know--and how well they know it--with clarity and confidence. To achieve this, we focus on the 
theoretical foundations and methodological development of epistemic uncertainty-aware machine learning. In particular, we 
leverage tools from imprecise probabilities, cooperative game theory, and kernel methods to represent, quantify, and resolve
uncertainty, as well as to support learning and decision-making under uncertainty. 

<p align="justify">
<b> Background. </b> From 2023 to 2025, I was a Postdoctoral Researcher at the <a href="https://ri-lab.org/">Rational
Intelligence Lab</a> within CISPA Helmholtz Center for Information Security, Germany,
under the supervision of <a href="https://www.krikamol.org/">Dr. Krikamol Muandet</a>. My research centered on 
imprecise probabilistic machine learning, a generalised probability theory framework, and their integration to machine learning 
challenges, including hypothesis testing, supervised learning, and forecast elicitation under imprecision. Between 2019 and 2023, I 
pursued my DPhil in 
Statistics at the <a href="https://csml.stats.ox.ac.uk/">University of Oxford</a>,
where I worked at the intersection of kernel methods and Gaussian processes, under the 
supervision of <a href="https://sejdino.github.io/">Prof. Dino Sejdinovic</a>. 
During my doctoral studies, I also interned at the <a href="https://ei.is.mpg.de/">
Empirical Inference department of the Max Planck Institute for Intelligent Systems, Tübingen</a>, working on improving econometric 
models using modern machine learning techniques. I hold both a Master’s and a Bachelor’s degree in Mathematics and Statistics, 
graduating with First Class Honours from the University of Oxford, where I received the Departmental Prize for ranking top of the cohort.
</p>


<p align="justify">
I also enjoy bridging the gap between academia and industry. I interned at <a href="https://relay.amazon.de/?
tag=gmar&user=de&ref=gs_c_136100420583xkwd-829792795643_ki">Amazon</a> as an Applied Scientist, addressing coherent forecasting problems 
for the EU logistics network. I also provided data science and machine learning consulting services for various startups, including <a 
href="https://ravio.com/">Ravio</a>, <a href="https://catalystlab.ai/">Catalyst AI</a>, <a href="https://www.cambridgespark.
com/">Cambridge Spark</a>, <a href="https://www.potatopro.com/companies/crop4sight">Crop4Sight</a>, and <a href="https://www.
verifiedmetrics.com/">gini</a>. I also co-founded Oxford Strategy Group Digital, Oxford’s first student-led data science consultancy group.
</p>


<br>

<h2> News</h2>

{% assign news = site.news | sort: "date" | reverse %}
<div class="small-text">
<dl>
{% for new in news limit: 8 %}
<dt>{{ new.date |date: "%b-%Y"}}</dt>
<dd>{{ new.content }}</dd>
{% endfor %}
</dl>
</div>




