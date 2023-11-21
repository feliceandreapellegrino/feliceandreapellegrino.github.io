---
layout: page
title: projects
permalink: /projects/
description: Some projects and opportunities
nav: true
nav_order: 6
display_categories: [work]
horizontal: true
---

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
         {%- for project in sorted_projects -%}
            {% include projects_horizontal.html %}
          {%- endfor %}
    </div>
</div>


<!-- pages/projects.md -->
<div class="projects">
{%- if site.enable_project_categories and page.display_categories %}
  <!-- Display categorized projects -->
  {%- for category in page.display_categories %}
  <h2 class="category">{{ category }}</h2>
  {%- assign categorized_projects = site.projects | where: "category", category -%}
  {%- assign sorted_projects = categorized_projects | sort: "importance" %}
  <!-- Generate cards for each project -->
  {% if page.horizontal -%}
 <!-- <div class="container"> -->
    <div class="row">
      <div class="col">
          {%- for project in sorted_projects -%}
            {% include projects_horizontal.html %}
          {%- endfor %}
      </div>
    </div>
<!-- </div> -->
  {%- else -%}
  <div class="grid">
    {%- for project in sorted_projects -%}
      {% include projects.html %}
    {%- endfor %}
  </div>
  {%- endif -%}
  {% endfor %}

{%- else -%}
<!-- Display projects without categories -->
  {%- assign sorted_projects = site.projects | sort: "importance" -%}
  <!-- Generate cards for each project -->
  {% if page.horizontal -%}
  <!-- <div class="container"> -->
    <div class="row">
      <div class="col">
          {%- for project in sorted_projects -%}
            {% include projects_horizontal.html %}
          {%- endfor %}
      </div>
    </div>
  <!-- </div> -->
  {%- else -%}
  <div class="grid">
    {%- for project in sorted_projects -%}
      {% include projects.html %}
    {%- endfor %}
  </div>
  {%- endif -%}
{%- endif -%}
</div>
