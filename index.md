---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
title: Personal Website
position: Incoming Assistant Professor
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

[//]: # (## Welcome <i class="em em-wave" aria-role="presentation" aria-label="WAVING HAND SIGN"></i>)

<body>
  <p align="justify" style="color:red;">🚨🚨 PhD Opportunities: Interested in bringing in epistemic intelligence to machine learning systems?
I have several openings for PhD students in 2025 to be based in Singapore and are looking for candidates with a strong statistical, 
mathematical, or machine learning background. More details can be found <a href="https://chau999.github.io/group/">here</a>.</p>
</body>

## Bio 📖
<p align="justify">
Halo, my name is Siu Lun (Alan) Chau. I am an incoming Assistant Professor (commencing May 2025) at the <a href="https://www.ntu.edu.sg/computing">College of Computing 
and Data Science, Nanyang Technological University (NTU), Singapore</a>. I will be leading the <b>Epistemic Intelligence & Computation 
(EPIC)</b> Lab, where our mission is to develop intelligent systems that can recognise the 
limitation of their knowledge (<span style ="color: orangered">uncertainty-awareness</span>), be able to communicate their 
insights (<span style ="color: blue">explainability</span>), and 
effectively 
collaborate with human users (<span style="color: green">preference modelling</span>).
</p>


<p align="justify">
From 2023 to 2025, I was a Postdoctoral Researcher at the <a href="https://ri-lab.org/">Rational Intelligence Lab</a> within the CISPA Helmholtz Center for Information Security, Germany, under the supervision of <a href="https://www.krikamol.org/">Dr. Krikamol Muandet</a>. My research centered on imprecise probabilities, a generalised framework of probability theory, and their application to machine learning challenges, including hypothesis testing and supervised learning under imprecision. Between 2019 and 2023, I pursued my DPhil in Statistics at the <a href="https://csml.stats.ox.ac.uk/">University of Oxford</a>,
where I worked on the intersection of kernel methods and Gaussian processes with applications to trustworthy machine learning, under the 
supervision of <a href="https://sejdino.github.io/">Prof. Dino Sejdinovic</a>. 
During my doctoral studies, I also interned at the <a href="https://ei.is.mpg.de/">
Empirical Inference department of the Max Planck Institute for Intelligent Systems, Tübingen</a>, working on improving econometric 
models using modern machine learning techniques. I hold both a Master’s and a Bachelor’s degree in Mathematics and Statistics, 
graduating with First Class Honours from the University of Oxford, where I received the Departmental Prize for ranking top of the cohort.
</p>


<p align="justify">
In addition to my research, I also enjoy bridging the gap between academia and industry. I interned at <a href="https://relay.amazon.de/?tag=gmar&user=de&ref=gs_c_136100420583xkwd-829792795643_ki">Amazon</a> as an Applied Scientist, addressing coherent forecasting problems for the EU logistics network. I also provided data science and machine learning consulting services for various startups, including <a href="https://ravio.com/">Ravio</a>, <a href="https://catalystlab.ai/">Catalyst AI</a>, <a href="https://www.cambridgespark.com/">Cambridge Spark</a>, <a href="https://www.potatopro.com/companies/crop4sight">Crop4Sight</a>, and <a href="https://www.verifiedmetrics.com/">gini</a>. I also co-founded OSG Digital, Oxford’s first student-led data science consultancy group.
</p>


[//]: # (<p align="justify">)

[//]: # (Hello! My name is Siu Lun Chau &#40;周兆麟&#41;, currently a postdoctoral researcher at the <a href="https://ri-lab.org/">Rational Intelligence Lab</a> within )

[//]: # (<a href="https://cispa.de">CISPA</a> Helmholtz Center for Information Security in Germany. I work under the guidance of )

[//]: # (<a href="https://www.krikamol.org/">Dr. Krikamol Muandet</a>, focusing on advancing the theory and practice of epistemic machine learning, i.e. making models acknolwedge what they don't know, and effecitively communicating)

[//]: # (what they know. To achieve this goal, we need better methods for modelling <b>uncertainty</b>, <b>explanability</b>, and <b>preferences</b>.)

[//]: # ()
[//]: # (</p>)

[//]: # ()
[//]: # (<p align="justify">)

[//]: # (Before joining CISPA, I obtanied my DPhil in Statistical Machine Learning from the University of Oxford, where I worked on problems in the intersection of kernel methods and Gaussian processes under the supervision of <a href="https://sejdino.github.io/">Prof. Dino Sejdinovic</a>. I also interned at Amazon as an Applied Scientist, where I tackled coherent forecasting problems for the EU logistics network. I also interned at the Max Planck Institute for Intelligent Systems, where I worked on improving econometric models with modern machine learning approaches.)

[//]: # (</p>)

[//]: # ()
[//]: # (<p align="justify">)

[//]: # (I hold both a master's and undergraduate degree in Mathematics and Statistics with First Class Honours from the University of Oxford. During my master's, I worked with <a href="https://www.vanderschaar-lab.com/">Prof. Mihaela van der Schaar</a> on modelilng diseases trajectories using Bayesian nonparametric methods.)

[//]: # (</p>)

[//]: # ()
[//]: # (<p align="justify">)

[//]: # (You can read more about my research interests <a href="https://chau999.github.io/research/">here</a>. Please do not hesitate to reach out if you would like to collaborate, I am always excited to hear from you :&#41;)

[//]: # (</p>)

<br>

### Recent Updates 🔔

{% assign news = site.news | sort: "date" | reverse %}
<div class="small-text">
<dl>
{% for new in news limit: 5 %}
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
{% for talk in talks limit: 5 %}
<dt>{{ talk.date |date: "%b-%Y"}}</dt>
<dd><b>{{ talk.talk_title }}</b> 
<br> - <i>{{talk.venue}}</i></dd>
{% endfor %}
</dl>
</div>



