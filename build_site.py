"""Cria a estrutura completa do site Jekyll e gera eduardacenteno-site.zip.

Uso: coloque este arquivo e migrate_posts.py numa pasta vazia e rode:
    python build_site.py
"""
import zipfile
from pathlib import Path

ROOT = Path(__file__).parent

FILES = {}

FILES["_config.yml"] = r'''title: Eduarda Centeno
description: Neuroscientist, Open Science advocate and co-Executive Director of the Brazilian Reproducibility Network.
url: "https://eduardacenteno.com"
baseurl: ""
lang: en
permalink: /:year/:month/:day/:title/

contact: egzcenteno(at)gmail.com
social:
  linkedin: https://linkedin.com/in/eduardagzc/
  github: https://github.com/eduardacenteno
  orcid: https://orcid.org/0000-0002-1490-4903

exclude:
  - build_site.py
  - migrate_posts.py

plugins:
  - jekyll-seo-tag
  - jekyll-feed
'''

FILES["Gemfile"] = r'''source "https://rubygems.org"
gem "github-pages", group: :jekyll_plugins
'''

FILES["CNAME"] = "eduardacenteno.com\n"

FILES["_layouts/default.html"] = r'''<!DOCTYPE html>
<html lang="{{ page.lang | default: site.lang }}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  {% seo %}
  {% feed_meta %}
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{{ '/assets/css/style.css' | relative_url }}">
</head>
<body>
  <a class="skip" href="#content">Skip to content</a>

  <header class="site-header">
    <div class="wrap header-inner">
      <a class="brand" href="{{ '/' | relative_url }}">
        <img src="{{ '/assets/img/avatar.png' | relative_url }}" alt="" width="44" height="44">
        <span>{{ site.title }}</span>
      </a>
      <button class="menu-toggle" aria-expanded="false" aria-controls="nav">☰ Menu</button>
      <nav id="nav" class="nav">
        <ul>
          <li><a href="{{ '/' | relative_url }}" {% if page.url == '/' %}aria-current="page"{% endif %}>About Me</a></li>
          <li><a href="{{ '/curriculum-vitae/' | relative_url }}" {% if page.url == '/curriculum-vitae/' %}aria-current="page"{% endif %}>Professional Experience</a></li>
          <li><a href="{{ '/highlights/' | relative_url }}" {% if page.url == '/highlights/' or page.layout == 'post' %}aria-current="page"{% endif %}>Highlights</a></li>
        </ul>
        <ul class="social">
          <li><a href="{{ site.social.linkedin }}">LinkedIn</a></li>
          <li><a href="{{ site.social.github }}">GitHub</a></li>
          <li><a href="{{ site.social.orcid }}">ORCID</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <main id="content" class="wrap">
    {{ content }}
  </main>

  <footer class="site-footer">
    <div class="wrap">Contact: {{ site.contact }}</div>
  </footer>

  <script>
    const btn = document.querySelector('.menu-toggle');
    const nav = document.getElementById('nav');
    btn.addEventListener('click', () => {
      const open = nav.classList.toggle('open');
      btn.setAttribute('aria-expanded', open);
    });
  </script>
</body>
</html>
'''

FILES["_layouts/post.html"] = r'''---
layout: default
---
<article class="post">
  <h1>{{ page.title }}</h1>
  <p class="meta">
    <time datetime="{{ page.date | date_to_xmlschema }}">{{ page.date | date: "%B %-d, %Y" }}</time>
    {% if page.tags.size > 0 %} · {{ page.tags | join: ", " }}{% endif %}
  </p>
  {{ content }}
</article>
<p class="back"><a href="{{ '/highlights/' | relative_url }}">← All highlights</a></p>
'''

FILES["index.md"] = r'''---
layout: default
title: About Me
---

# About Me

Hey there!

Welcome to my webpage!

Some key information about me: I'm a Brazilian and have lived abroad for several years; I have a master's degree and a Ph.D. in (Open Computational) Neuroscience; I'm a huge Open Science enthusiast and have been advocating for this framework in Europe for the past 7 years, where I participated in different Open Science boards and initiatives, specially in France and in the Netherlands. I am currently co-Executive Director of the [Brazilian Reproducibility Network](https://www.reprodutibilidade.org/), thereby expanding my Open Science expertise back to my home country.

In my free time, I love reading [check out my [Goodreads page](COLE_AQUI_O_LINK)!], travelling, eating good food, dancing, and spending time with my friends & family (pets included, of course).
'''

FILES["highlights.html"] = r'''---
layout: default
title: Highlights
permalink: /highlights/
---
<h1>Highlights</h1>

{% for post in site.posts %}
<article class="post-card">
  <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
  <p class="meta">
    <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %-d, %Y" }}</time>
    {% if post.tags.size > 0 %} · {{ post.tags | join: ", " }}{% endif %}
  </p>
  {{ post.content }}
</article>
{% endfor %}
'''

FILES["curriculum-vitae.md"] = r'''---
layout: default
title: Professional Experience
permalink: /curriculum-vitae/
---

<div class="cv" markdown="1">

# Professional Experience

I'm currently based in Florianópolis, Brazil.

## Main Skills

- Open Science
- Python Programming
- Version Control
- Computational Neuroscience
- Leadership

## Formal Education

- **2020 – 2024: Ph.D. in Neuroscience** at Bordeaux Neurocampus Graduate Program, France
- **2018 – 2020: M.Sc. in Neuroscience** at [Neurasmus European Master Program in Neuroscience](https://www.neurasmus.u-bordeaux.fr/student-life/alumni-success-stories/), Université de Bordeaux, France & Vrije Universiteit Amsterdam, Netherlands
- **2015 – 2016: Academic Mobility – Visiting Undergraduate Student in Biological Sciences** at the University of Reading, United Kingdom
- **2013 – 2018: B.Sc. in Biotechnology** at Universidade Federal de Pelotas, Brazil

## Work Experience

- **2025 – Present: Executive Director** of the [Brazilian Reproducibility Network](http://www.reprodutibilidade.org)
- **2020 – 2024: Research Assistant** at the [MULTINETlab](https://multinetlab.com/open-science/), Amsterdam UMC location VUmc, Netherlands
- **2016 – 2018: Portuguese-English Academic-Text Editor and Translator** at [Mayer Scientific Editing](http://www.mayerscientificediting.com/)

## Open Science Activities

### Community Positions

- **2026 – Present: Board Member** of the [Global Research Initiative on Open Science](https://www.grios.org/)
- **2025 – Present: Board Member** of the [International Network of Open Science & Scholarship Communities](https://osc-international.com/)
- **2023 – 2025: Open Science Expert** representing the Netherlands at [Knowledge Exchange](https://www.knowledge-exchange.info/projects/project/open-science)
- **2021 – 2024: Member** of the [INCF Working Group on Standardized Data](https://www.incf.org/sig/incf-working-group-standardized-data) & BIDS BEP032 Extension Proposal
- **2021 – 2024: Board Member** of the [Open Science Community Amsterdam](https://osc-international.com/osc-amsterdam/), Netherlands
- **2021 – 2024: Founder & Coordinator** of the [Open Science Working Group](https://anatomy-neurosciences.com/initiatives/openscience/) from the Anatomy and Neurosciences department, Amsterdam UMC location VUmc, Netherlands
- **2020 – 2023: Founder & Co-Host** of the ReproducibiliTea at the Bordeaux Neurocampus ([BordeauxTea](https://twitter.com/BordeauxTea)), France
- **2019 – 2020: Founder & Co-Host** of the ReproducibiliTea Amsterdam Vrije Universiteit, Netherlands

### Event Organization

- **2023: Founder & Organizer** of the [1st Open Science Workshop at the Bordeaux Neurocampus](https://www.bordeaux-neurocampus.fr/en/1st-open-science-workshop-2023/), France
- **2025: Organizer** of the Brazilian Reproducibility Network's [Ambassadors Annual Event](https://www.reprodutibilidade.org/post/abertura-da-segunda-coorte-do-programa-de-embaixadores)

### Published Material

- **2025: Co-author & Project Manager of** Brazilian Reproducibility Network's [Primers](https://zenodo.org/communities/redereprodutibilidade/records?q=&l=list&p=1&s=10&sort=newest)
- **2025: Co-author of** Open Science in Brazil: Trajectory, Challenges, and Future Perspectives. DOI: [10.5281/zenodo.17806546](https://doi.org/10.5281/zenodo.17806546)
- **2025: Co-author of** Brazilian Reproducibility Network. DOI: [10.1590/SciELOPreprints.12671](https://doi.org/10.1590/SciELOPreprints.12671)
- **2024: My PhD thesis manuscript** – "[The investigation of songbirds' cortical-basal ganglia neural sleep dynamics through an Open Science-inspired computational framework](https://theses.fr/2024BORD0237)"
- **2023: Co-author of [Open Science: Principles and Practices](https://openscienceeducation.org/)** – a course outline in the form of a syllabus to facilitate Open Science teaching integration in higher education
- **2022: Co-author in BrainStorm** – more on this letter can be found [here](/2022/11/11/bordeauxtea-in-brainstorm/)
- **2022: Co-author of** the Human Connectome Project resting-state fMRI Connectivity Matrices (Young Adult + Aging). DOI: [10.5281/zenodo.6770119](https://doi.org/10.5281/zenodo.6770119)
- **2022: First author of** the [Notebook for Network and Topological Analysis in Neuroscience](https://github.com/multinetlab-amsterdam/network_TDA_tutorial). DOI: [10.5281/zenodo.4483650](https://doi.org/10.5281/zenodo.4483650)

### Talks, Panels & Roundtables

- **2026: Invited Speaker** at the International Course ["Building a responsible research environment: research integrity in the formation of early-career researchers"](https://cursosqualificacao2.campusvirtual.fiocruz.br/hotsite/condutaresponsavelfar2025/12357), hosted by Fiocruz, Brazil
- **2025: Invited Speaker** at the [Global Federation of Reproducibility Networks: Meet the networks](https://www.canal-u.tv/chaines/rfrr/meet-the-networks-brazil)
- **2025: Invited Speaker** at the [FeSBE Regional Event in Salvador](https://2025.fesbe.org.br/2025reg/), Brazil, hosted by Prof. Eduardo Colombari
- **2025: Invited Speaker** at the Neuroscience Seminar Series of the Federal University of Santa Catarina, Brazil, hosted by Prof. Maurício Peña and Prof. Patrícia Brocardo
- **2025: Invited Speaker** at the [Open Science Community Launch Event](https://mailchi.mp/36b2ffa20fb7/newsletter-para-assinantes-n-14-agosto2025-12872605) at the Federal University of Pelotas, Brazil, hosted by Prof. Anelise Montagner
- **2024: Presenter** at the [Institute of Neurodegenerative Diseases (IMN) day](/2024/06/25/imn-day-my-first-phd-award/)
- **2023: Invited Speaker** at the [Reproducible Research Day](/2023/08/10/bordeauxtea-institut-pasteur/) at Institut Pasteur, France
- **2023: Invited Speaker at [Institut Intelligence et données](/2023/08/11/open-science-talk-ulaval/)** – "The 'Why, What, and How' of Open Science and its impact on my professional (and personal) journey." Université Laval, Canada
- **2023: Panelist representing the Open Science Communities in the Netherlands** at the [European Open Science Cloud Tripartite meeting hosted by SURF](/2023/05/10/got-to-represent-the-osc-nl-the-dutch-eosc-meeting/), Utrecht, Netherlands
- **2021, 2022, 2023: Open Science Roundtable Host** at the [Introduction to Experimental Neuroscience Workshop](https://www.bordeaux-neurocampus.fr/en/workshop-introduction-to-experimental-neuroscience-2023/) at the Bordeaux Neurocampus, France

## Teaching & Supervision Experience

- **2023: Invited lecturer** – I was invited by Linda Douw to give a lecture on Open Science & Preregistration in the Neuroscience Master program at the Vrije Universiteit Amsterdam
- **2023: Coding Documentation Instructor** at the [EPFL Open Science Summer School](https://orperschool.github.io/), Switzerland
- **2023: Helper** at the Software Carpentry Workshop at the Vrije Universiteit Amsterdam, Netherlands
- **2023: Master's Thesis Daily Supervisor** of C. Guerrero (M2 student), France
- **2022: Master's Thesis Daily Supervisor** of V. Puyo (M2 student), France
- **2021: Instructor** at the [Computational Neuroscience Crash Course](https://github.com/bordeaux-neurocampus/CNCC-2021-beginner) hosted at the Bordeaux Neurocampus, France
- **2021: Instructor** at the [Introduction to Experimental Neuroscience Workshop](https://github.com/bordeaux-neurocampus/WIEN2021) at the Bordeaux Neurocampus, France

## Grants and Awards

- **2025: Prix Science Ouverte de la Thèse** by the [French Ministry of Higher Education, Research, and Space](https://www.reprodutibilidade.org/en/post/our-director-eduarda-centeno-receives-the-french-prix-science-ouverte-de-la-th%C3%A8se)
- **2024: Best Talk Award** at the [Institute of Neurodegenerative Diseases (IMN) day](/2024/06/25/imn-day-my-first-phd-award/)
- **2023: Open Science Runner-up Trainee Prize** by [the Neuro & Irv and Helga Cooper Foundation](/2023/12/01/the-neuro-irv-and-helga-cooper-foundation-open-science-prize/)
- **2023: Best Paper Award** by the [Brain Structure and Function Editorial Board](https://link.springer.com/journal/429/updates/25948058)
- **2023: [Open Educational Resource Award (OSCAwards)](/2023/02/09/oscawards-hosted-the-event-got-a-prize/)** by the Open Science Community Amsterdam, Netherlands
- **2023: [GPR Ph.D. Extension Fellowship](https://www.bordeaux-neurocampus.fr/en/laureats-des-bourses-de-soudure-2023-du-gpr-brain_2030/)** by the Bordeaux Neurocampus, France
- **2023: Jülich Forschungszentrum Travel Grant** to attend the [Open Science Retreat](https://open.science-retreat.org/) in Kochel am See, Germany
- **2020 – 2023: Ph.D. Fellowship** by the Bordeaux Neurocampus Graduate Program, France
- **2018 – 2020: Neurasmus Scholarship: A European Master's in Neuroscience**, France & Netherlands
- **2019: Munich Brain Course Award** by the Graduate School of Systemic Neurosciences from Ludwig Maximilians Universität, Germany
- **2015 – 2016: Science Without Borders Scholarship** by CNPq, Brazil
- **2013 – 2014: Young Talents for Science Scholarship** by CAPES, Brazil
- **2009, 2010, 2011: Highest Grades Prize** at São Luiz Gonzaga High School, Brazil

## Languages

- **Portuguese:** Native Speaker
- **English:** C1
- **French:** B1-2
- **Spanish:** A2
- **German:** A2

Download my full CV [here](https://mega.nz/file/NiJTkQYR#IKbGR494P_wz6cF6rosnU0D7eg5Hvrz2tbmF4dpvl6w).

</div>
'''

FILES["assets/css/style.css"] = r''':root {
  --bg: #faf8f5;
  --surface: #ffffff;
  --text: #1f2328;
  --muted: #5b6370;
  --accent: #0f6e6e;
  --border: #e6e1d9;
  --max: 46rem;
}

* { box-sizing: border-box; }

body {
  margin: 0;
  background: var(--bg);
  color: var(--text);
  font: 400 1.0625rem/1.7 Inter, system-ui, sans-serif;
}

.wrap { max-width: var(--max); margin: 0 auto; padding: 0 1.25rem; }

h1, h2, h3 { font-family: Fraunces, Georgia, serif; line-height: 1.2; }
h1 { font-size: 2.4rem; margin: 2.5rem 0 1rem; }
h2 { font-size: 1.5rem; margin: 2.5rem 0 .75rem; }
h3 { font-size: 1.15rem; margin: 1.75rem 0 .5rem; color: var(--muted); font-style: italic; }

a { color: var(--accent); text-underline-offset: 3px; }
a:hover { text-decoration-thickness: 2px; }

img { max-width: 100%; height: auto; border-radius: 8px; display: block; margin: 1.5rem 0; }

blockquote { margin: 1.5rem 0; padding: .25rem 1.25rem; border-left: 3px solid var(--accent); color: var(--muted); }

.skip { position: absolute; left: -999px; }
.skip:focus { left: 1rem; top: 1rem; background: var(--surface); padding: .5rem 1rem; z-index: 10; }

.site-header { background: var(--surface); border-bottom: 1px solid var(--border); }
.header-inner {
  display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between;
  gap: 1rem; padding-top: 1rem; padding-bottom: 1rem;
}
.brand {
  display: flex; align-items: center; gap: .75rem;
  color: var(--text); text-decoration: none;
  font-family: Fraunces, Georgia, serif; font-size: 1.35rem; font-weight: 700;
}
.brand img { margin: 0; border-radius: 50%; }

.nav { display: flex; flex-wrap: wrap; gap: 1.5rem; }
.nav ul { list-style: none; margin: 0; padding: 0; display: flex; gap: 1.1rem; }
.nav a { color: var(--muted); text-decoration: none; font-weight: 500; font-size: .95rem; }
.nav a:hover, .nav a[aria-current] { color: var(--accent); }
.social { padding-left: 1.5rem !important; border-left: 1px solid var(--border); }
.social a { font-size: .85rem; }

.menu-toggle {
  display: none; background: none; border: 1px solid var(--border);
  border-radius: 6px; padding: .4rem .8rem; font: inherit; cursor: pointer;
}

@media (max-width: 720px) {
  .menu-toggle { display: block; }
  .nav { display: none; width: 100%; flex-direction: column; gap: 1rem; }
  .nav.open { display: flex; }
  .nav ul { flex-direction: column; gap: .5rem; }
  .social { padding-left: 0 !important; border-left: none; flex-direction: row !important; }
  h1 { font-size: 2rem; }
}

.meta { color: var(--muted); font-size: .9rem; margin-top: -.25rem; }
.post-card { padding: 2rem 0; border-bottom: 1px solid var(--border); }
.post-card h2 { margin-top: 0; }
.post-card h2 a { color: var(--text); text-decoration: none; }
.post-card h2 a:hover { color: var(--accent); }
.back { margin-top: 3rem; }

.cv li { margin-bottom: .45rem; }

.site-footer {
  margin-top: 4rem; padding: 2rem 0;
  border-top: 1px solid var(--border);
  color: var(--muted); font-size: .9rem;
}
'''

SKIP_IN_ZIP = {"build_site.py", "migrate_posts.py"}


def main() -> None:
    # 1. Arquivos do site
    for rel, content in FILES.items():
        path = ROOT / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        print(f"📄 {rel}")

    # 2. Posts + imagens
    if (ROOT / "migrate_posts.py").exists():
        import migrate_posts
        migrate_posts.main()
    else:
        print("⚠️  migrate_posts.py não encontrado: os posts não foram gerados.")

    # 3. Zip
    zip_path = ROOT.parent / f"{ROOT.name}.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(ROOT.rglob("*")):
            if f.is_file() and f.name not in SKIP_IN_ZIP and "__pycache__" not in f.parts:
                z.write(f, f.relative_to(ROOT))
    print(f"\n📦 Zip criado: {zip_path}")


if __name__ == "__main__":
    main()