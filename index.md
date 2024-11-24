---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
title: Personal Website
position: Incoming Assistant Professor
location: College of Computing and Data Science, Nanyang Technological University
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

### Bio 📖
<p align="justify">
Dr. Siu Lun Chau is an incoming Assistant Professor (commencing May 2025) at the College of <a href="https://www.ntu.edu.sg/computing">Computing and Data Science, Nanyang Technological University (NTU), Singapore</a>. He will lead the <b>Epistemic Intelligence & Computation (EPIC)</b> Lab, focused on developing intelligent systems that recognise and acknowledge what they don’t know while effectively communicating what they already know.
</p>

<p align="justify">
From 2023 to 2025, Dr. Chau was a Postdoctoral Researcher at the <a href="https://ri-lab.org/">Rational Intelligence Lab</a> within the CISPA Helmholtz Center for Information Security, Germany, under the supervision of <a href="https://www.krikamol.org/">Dr. Krikamol Muandet</a>. His research centered on imprecise probabilities, a generalised framework of probability theory, and their application to machine learning challenges, including hypothesis testing and supervised learning under imprecision. Between 2019 and 2023, Dr. Chau pursued his DPhil in Statistics at the <a href="https://csml.stats.ox.ac.uk/">University of Oxford</a>, where he worked on the intersection of kernel methods and Gaussian processes with applications to trustworthy machine learning, under the supervision of <a href="https://sejdino.github.io/">Prof. Dino Sejdinovic</a>. During his doctoral studies, he also interned at the <a href="https://ei.is.mpg.de/">Empirical Inference devision of the Max Planck Institute for Intelligent Systems, Tübingen</a>, working on enhancing econometric models using modern machine learning techniques. Dr. Chau holds both a Master’s and a Bachelor’s degree in Mathematics and Statistics, graduating with First Class Honours from the University of Oxford, where he received the Departmental Prize for ranking top of his cohort.
</p>


<p align="justify">
In addition to his academic achievements, Dr. Chau enjoys bridging the gap between academia and industry. He interned at <a href="https://relay.amazon.de/?tag=gmar&user=de&ref=gs_c_136100420583xkwd-829792795643_ki">Amazon</a> as an Applied Scientist, addressing coherent forecasting problems for the EU logistics network. He has also provided data science and machine learning consulting services for various startups, including <a href="https://ravio.com/">Ravio</a>, <a href="https://catalystlab.ai/">Catalyst AI</a>, <a href="https://www.cambridgespark.com/">Cambridge Spark</a>, <a href="https://www.potatopro.com/companies/crop4sight">Crop4Sight</a>, and <a href="https://www.verifiedmetrics.com/">gini</a>. Dr. Chau also co-founded OSG Digital, Oxford’s first student-led data science consultancy group.
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



