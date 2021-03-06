---
layout: page
title: Projects
permalink: /projects/
description: A collection of my projects.
nav: true
headerOrder: 1
---

<div class="projects grid">

  {% assign sorted_projects = site.projects | sort: "importance" %}
  {% for project in sorted_projects %}
  <div class="grid-item">
    {% if project.redirect %}
    <a href="{{ project.redirect }}" target="_blank">
    {% else %}
    <a href="{{ project.url | relative_url }}">
    {% endif %}
      <div class="card hoverable">
        {% if project.img %}
        <img src="{{ project.img | relative_url }}" alt="project thumbnail">
        {% endif %}
        <div class="card-body">
          <h2 class="card-title">{{ project.title }}</h2>
          <p class="card-text">{{ project.description }}</p>
          {% if project.status == 'initiated' %}
          <span class="badge bg-success">Initiated</span>
          {% endif %}
          {% if project.status == 'launched' %}
          <span class="badge bg-primary">Launched</span>
          {% endif %}
          {% if project.status == 'closed' %}
          <span class="badge bg-dark">Closed</span>
          {% endif %}
          <!-- <div class="row ml-1 mr-1 p-0">
            {% if project.github %}
            <div class="github-icon">
              <div class="icon" data-toggle="tooltip" title="Code Repository">
                <a href="{{ project.github }}" target="_blank"><i class="fab fa-github gh-icon"></i></a>
              </div>
              {% if project.github_stars %}
              <span class="stars" data-toggle="tooltip" title="GitHub Stars">
                <i class="fas fa-star"></i>
                <span id="{{ project.github_stars }}-stars"></span>
              </span>
              {% endif %}
            </div>
            {% endif %}
          </div> -->
        </div>
      </div>
    </a>
  </div>
{% endfor %}

</div>
