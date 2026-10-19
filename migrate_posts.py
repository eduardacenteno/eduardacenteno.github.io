"""Migra os Highlights do WordPress (eduardacenteno.com) para posts Jekyll.

Uso: python migrate_posts.py   (rodar na raiz do repositório)
"""
import json
import urllib.request
from pathlib import Path

WP = "https://eduardacenteno.com/wp-content/uploads/"
ROOT = Path(__file__).parent
POSTS_DIR = ROOT / "_posts"
IMG_DIR = ROOT / "assets" / "img"

AVATAR = WP + "2023/08/cropped-oks9dxdv.png"

# Em cada body, "IMG/" vira o caminho local das imagens daquele post.
POSTS = [
    dict(date="2026-04-09", slug="agora-integro-o-conselho-consultivo-academico-do-grios",
         title="Agora integro o Conselho Consultivo Acadêmico do GRIOS!", lang="pt-BR", tags=[],
         images={"grios.png": "2026/04/image-1.png"},
         body="""Nesse ano, fui selecionada para integrar o Conselho Consultivo Acadêmico do GRIOS (Global Research Initiative on Open Science), composto por especialistas de nove países, selecionados por meio de processo aberto para garantir diversidade geográfica e disciplinar. Mais informações [aqui](https://www.reprodutibilidade.org/post/a-nossa-co-diretora-eduarda-centeno-agora-integra-o-conselho-consultivo-acad%C3%AAmico-do-grios).

This year, I was selected to join the Academic Advisory Board of GRIOS (Global Research Initiative on Open Science), composed of experts from nine countries, chosen through an open process to ensure geographic and disciplinary diversity. More information [here](https://www.reprodutibilidade.org/post/a-nossa-co-diretora-eduarda-centeno-agora-integra-o-conselho-consultivo-acad%C3%AAmico-do-grios).

![](IMG/grios.png)"""),

    dict(date="2026-04-02", slug="premio-de-teses-de-ciencia-aberta-na-franca",
         title="Prêmio de Teses de Ciência Aberta na França", lang="pt-BR", tags=[],
         images={"premio.png": "2026/04/image.png"},
         body="""Em dezembro de 2025, tive o prazer de viajar até Paris para receber o Prêmio de Teses de Ciência Aberta na França! Foi um reconhecimento incrível da minha tese de doutorado! Mais informações [aqui](https://www.reprodutibilidade.org/post/nossa-diretora-eduarda-centeno-recebe-o-pr%C3%AAmio-franc%C3%AAs-prix-science-ouverte-de-la-th%C3%A8se).

In December 2025, I had the pleasure of traveling to Paris to receive the Open Science Thesis Award in France! It was an incredible recognition of my doctoral dissertation! More information [here](https://www.reprodutibilidade.org/post/nossa-diretora-eduarda-centeno-recebe-o-pr%C3%AAmio-franc%C3%AAs-prix-science-ouverte-de-la-th%C3%A8se).

![](IMG/premio.png)"""),

    dict(date="2025-10-21", slug="global-federation-of-reproducibility-networks-meet-the-networks-brazil",
         title="Global Federation of Reproducibility Networks: Meet the networks – Brazil!", tags=[],
         images={},
         body="""I recently had the opportunity to share my work as Executive Director of the [Brazilian Reproducibility Network](https://www.reprodutibilidade.org/) (BrRN) in a series of webinars about the Global Federation of RNs, hosted by the French RN. It was great to see old acquaintances and share our efforts here in Brazil!

[Watch the webinar here](https://www.canal-u.tv/chaines/rfrr/meet-the-networks-brazil)."""),

    dict(date="2025-08-05", slug="primeira-atuacao-na-sbpc-como-diretora-executiva-da-rbr",
         title="Primeira atuação na SBPC como diretora executiva da RBR", lang="pt-BR",
         tags=["events", "personal journey"],
         images={"sbpc.jpg": "2025/08/whatsapp-image-2025-08-05-at-14.30.51_f58d4513.jpg"},
         body="""Mês passado, fui ao Recife (PE, Brasil) representar a Rede Brasileira de Reprodutibilidade na 77ª Reunião Anual da Sociedade Brasileira para o Progresso da Ciência. [Aqui](https://www.reprodutibilidade.org/post/rede-brasileira-de-reprodutibilidade-na-77a-reuni%C3%A3o-anual-da-sbpc-presen%C3%A7a-ativa-nos-debates-sobre) um post no blog da RBR sobre minha atuação no evento.

![](IMG/sbpc.jpg)"""),

    dict(date="2025-06-27", slug="coming-back-home", title="Coming back home!", tags=["personal journey"],
         images={"home.jpg": "2025/06/img-20241204-wa0040-1.jpg"},
         body="""After nearly 10 years abroad —living in England, France, and the Netherlands— I've recently returned to Brazil and stepped into a new role as co-Executive Director of the [Brazilian Reproducibility Network](https://www.reprodutibilidade.org/). It wasn't an easy decision to leave behind my life and loved ones in Europe (for now, at least), but it felt right for this chapter of my life.

I'm very proud to bring back everything I've learned across the Atlantic and use that knowledge to contribute to the country that first believed in me —giving me the chance to grow into the professional and person I am today. A huge thank you to the Science Without Borders program by CAPES that, back in 2015, funded my studies in the UK during my bachelor's. It genuinely launched my international journey.

To everyone I met during my time in Europe: **thank you**. Every experience, conversation, and collaboration helped shape me, both professionally and personally. While I'm now geographically distant, the connections we built remain strong, and I hope to keep nurturing them from across the ocean.

Now that I'm back, I find myself in that funny in-between space: feeling a bit too European for Brazil, and too Brazilian for Europe. I think that's something many expats relate to. But I'm embracing it. I'm excited to (re)discover how things work here —who to talk to, what we can learn, and what we can share with the world. There's a lot ahead, and although most of my scientific path has unfolded abroad, I'm looking forward to diving in and growing, right here.

To my new team and (reproducibility) community: thank you for welcoming me back home!

![](IMG/home.jpg)"""),

    dict(date="2025-06-27", slug="dr-centeno", title="Dr. Centeno!", tags=["events"],
         images={f"defense-{i}.webp": f"2025/06/img_20241110_202749_{n}.webp"
                 for i, n in enumerate(["170", "254", "351", "355", "367"], 1)},
         body="""Late last year, I completed my Ph.D. and successfully defended my dissertation, titled *"[The investigation of songbirds' cortical-basal ganglia neural sleep dynamics through an Open Science-inspired computational framework](https://theses.fr/2024BORD0237)."* In this project, I developed and integrated an Open Science-inspired infrastructure for data collection, management, analysis, and sharing to support research on how zebra finches learn and consolidate their songs. The four years I devoted to this work were both challenging —true to the nature of most Ph.D. journeys— and rewarding. I gained invaluable knowledge, met great people, and grew personally and professionally. Most importantly, I gained clarity about the paths I want to pursue —and those I don't— after my defense. While the thesis itself tells one story, I always recommend reading the acknowledgements section and the appendix. It's there you'll find the real heart of the project: the incredible people who walked alongside me and helped me reach the finish line, and the side projects that kept me motivated throughout the years.

If I can recommend something to anyone who decides to pursue a Ph.D.: build communities, take care of yourself, and dedicate time to side projects that bring you joy.

![](IMG/defense-1.webp)
![](IMG/defense-2.webp)
![](IMG/defense-3.webp)
![](IMG/defense-4.webp)
![](IMG/defense-5.webp)"""),

    dict(date="2024-10-25", slug="interview-for-womens-voices", title="Interview for \u201cWomen's Voices\u201d",
         tags=["article"], images={},
         body="""I was recently interviewed by Sara Carracedo about my perspectives on academia and leadership as a woman in science. Check out this great project below:

> [Women's Voices: Eduarda Gervini Zampieri Centeno](https://www.bordeaux-neurocampus.fr/en/womens-voices-eduarda-gervini-zampieri-centeno/)"""),

    dict(date="2024-10-15", slug="phd-defense-coming-up-soon", title="PhD Defense coming up soon!",
         tags=["events"], images={},
         body="""On November 7th, I'll be defending my PhD thesis in Bordeaux! A zoom link is also available upon request to watch it online 🙂

More information here:

> [Thesis defense – Eduarda Gervini Zampieri Centeno](https://www.bordeaux-neurocampus.fr/en/event/soutenance-de-these-eduarda-gervini-zampieri-centeno/)"""),

    dict(date="2024-09-26", slug="bordeauxtea-plos", title="BordeauxTea @ PLOS", tags=["article", "events"],
         images={"plos.png": "2024/09/image.png"},
         body="""Fjola and I recently wrote a post to PLOS 'Your Say' blog, and it was also featured in their ECR Community blog! Super cool! Check it out below: <https://ecrcommunity.plos.org/2024/09/20/two-phd-students-journey-in-organizing-the-1st-open-science-workshop-in-bordeaux/>

![](IMG/plos.png)"""),

    dict(date="2024-08-02", slug="goodbye-to-the-multinet-team",
         title="Goodbye to the Multinet team and the ANW department!", tags=["personal journey"],
         images={"1.jpg": "2024/08/20230929_133117.jpg", "2.png": "2024/08/labphoto.png",
                 "3.jpg": "2024/08/dsc02879.jpg", "4.jpeg": "2024/08/2022.jpeg",
                 "5.jpg": "2024/08/heidag.jpg", "6.jpg": "2024/08/osfest.jpg",
                 "7.jpg": "2024/08/osteam.jpg", "8.png": "2024/08/image.png"},
         body="""After five years in the Multinet team, it's now time to [say goodbye](https://multinetlab.com/2024/07/11/our-bbq-and-goodbye-eduarda/). What a pleasure it was to be part of this group where I learned so much, and got to grow immensely professionally and personally. I'll always be grateful to my mentors and colleagues for this beautiful ride. I also want to thank my peers from the ANW [Open Science working group](https://anatomy-neurosciences.com/initiatives/openscience/), who joined me in creating and expanding this project to bring the OS principles to our department. I am very proud of the work we did together, and I'm looking forward to seeing the new projects the OSWG will come up with!

![](IMG/1.jpg)
![](IMG/2.png)
![](IMG/3.jpg)
![](IMG/4.jpeg)
![](IMG/5.jpg)
![](IMG/6.jpg)
![](IMG/7.jpg)
![](IMG/8.png)"""),

    dict(date="2024-07-15", slug="neurasmus-annual-meeting-in-amsterdam",
         title="Neurasmus Annual meeting in Amsterdam!", tags=["events"],
         images={"neurasmus.jpeg": "2024/07/1720602696874.jpeg"},
         body="""Last week, I had the pleasure to participate as a Neurasmus Alumnus and talk to the current students about balancing PhD projects with extracurricular activities! It's always amazing to meet new neurasmates and exchange experiences about the program and beyond.

More [here](https://www.linkedin.com/feed/update/urn:li:share:7216730780536868864).

![](IMG/neurasmus.jpeg)"""),

    dict(date="2024-06-25", slug="imn-day-my-first-phd-award",
         title="IMN day & my first PhD Best Talk award!", tags=["award", "events"],
         images={"imn.png": "2024/06/image-3.png"},
         body="""On June 19th, I presented my PhD work at the 2024 edition of the IMN day and received the Best Presentation award!

![](IMG/imn.png)

> Adrien Boissenin and Carmen Guerrero-Marquez received best poster prizes, and @ElbaMolpeceres and @eduardagzc received the best talk prizes 🙌
>
> — Institute of Neurodegenerative Diseases (IMN) (@IMNresearch), [June 21, 2024](https://twitter.com/IMNresearch/status/1804141899424346431)"""),

    dict(date="2024-06-13", slug="neurocampus-doctoral-research-day",
         title="Neurocampus Doctoral Research Day", tags=["events"],
         images={"drd.png": "2024/06/image-2.png"},
         body="""On June 7th, I had the opportunity to present my PhD work to the Neurocampus community. It was a great experience to expose and discuss my thesis with my peers, and of course, start practising for my defence coming up later this year!

![](IMG/drd.png)

> At the Doctoral Research Day, Sara Carracedo and @eduardagzc had the opportunity to present their PhD work to the whole community of Bordeaux Neurocampus 😁 Sara got a grant from @Neuro_Bordeaux the @Casden_BP 👏 Congrats to both of them!
>
> — Institute of Neurodegenerative Diseases (IMN) (@IMNresearch), [June 12, 2024](https://twitter.com/IMNresearch/status/1800874715600589307)"""),

    dict(date="2024-06-13", slug="anw-oswg-wins-oscaward", title="ANW OSWG wins OSCAward!",
         tags=["award", "events"], images={"oscaward.png": "2024/06/image-1.png"},
         body="""The ANW OSWG's '[Open Science Guidebook for Neuroscience](https://marbarrantescepas.github.io/OS-neuroscience/)' project has been honoured with an award in the 'Open Educational Resources' category at the 2nd edition of the OSCAwards. Congratulations to the entire team, and a special shoutout to Mar Barrantes for spearheading this initiative! 🎉

![](IMG/oscaward.png)

> Thanks @OSCAmsterdam for awarding the Open (Neuro)Science Guidelines 🌟🧠! Grateful to be part of such amazing OS team @AnatNeu_Ams
>
> — Mar Barrantes Cepas (@marbarrace), [June 12, 2024](https://twitter.com/marbarrace/status/1800942192296439892)"""),

    dict(date="2024-02-12", slug="multinet-ohbm-blog", title="MULTINET @ OHBM blog!",
         tags=["article", "award"], images={"ohbm.png": "2024/02/image.png"},
         body="""My master thesis was recently awarded the [Brain Structure and Function](https://www.springer.com/journal/429) Best Paper Award and here is a blogpost about it! The OHBM team also wrote [this](https://www.ohbm-com.com/brain-bites/network-neuroscience) SciComm piece about it!

[![](IMG/ohbm.png)](https://www.ohbmbrainmappingblog.com/blog/interview-with-eduarda-gervini-zampieri-centeno-2023-winner-of-the-brain-structure-and-function-award)"""),

    dict(date="2024-02-12", slug="passing-the-baton-to-carmen-and-jakob-the-new-bordeauxtea-hosts",
         title="Passing the baton to Carmen and Jakob: the new BordeauxTea hosts!", tags=["article"],
         images={},
         body="""I'm very happy to know that my baby project will be taken care of by two good friends and colleagues! Read more about our journey in the link below!

> [ReproducibiliTea in Bordeaux: celebrating three years of success](https://www.bordeaux-neurocampus.fr/reproducibilitea-in-bordeaux-celebrating-three-years-of-success/)"""),

    dict(date="2023-12-01", slug="the-neuro-irv-and-helga-cooper-foundation-open-science-prize",
         title="The Neuro – Irv and Helga Cooper Foundation Open Science Prize!", tags=["award"],
         images={"neuro.png": "2023/12/image.png"},
         body="""Last night, I received one of the runner-up Trainee prizes from [The Neuro – Irv and Helga Cooper Foundation](https://www.mcgill.ca/neuro/open-science/open-science-awards-and-prizes/neuro-irv-and-helga-cooper-foundation-open-science-prizes)! My application highlighted my Open Science work in France and the Netherlands. I'm super happy to have my efforts recognized internationally, and truly thankful to everyone who has supported me in this journey. A special shout to [Fernando Santos](https://www.linkedin.com/in/fernando-a-nobrega-santos-282594238/), [Linda Douw](https://www.linkedin.com/in/drlindadouw/), and [Cristina Lemos](https://www.linkedin.com/in/cristinalemos-89b9b44/)! 🎉

![](IMG/neuro.png)"""),

    dict(date="2023-10-24", slug="the-anw-oswg-snagged-a-spot-at-ols-cohort-8-pocketed-the-vu-challenge-award",
         title="The ANW OSWG snagged a spot at OLS cohort 8 & pocketed the VU challenge award!",
         tags=["award"], images={"ols.png": "2023/10/image-1.png"},
         body="""The [Open Science Working Group](https://anatomy-neurosciences.com/initiatives/openscience/) from the Anatomy and Neurosciences department hit the jackpot! We applied and were selected for the 8th cohort of the [OLS training program](https://openlifesci.org/openseeds/ols-8/projects-participants.html). *Drum roll, please!* And what's more exciting? We won a whopping 3K from the [VU Challenge Award](https://vu.nl/en/news/2023/vu-open-science-challenge-award-2023-eight-projects-funded) to work on our super-duper project: **Crafting a Handbook for Open Science in Neuroscience** 🎉🎉🎉

[![](IMG/ols.png)](https://docs.google.com/presentation/d/e/2PACX-1vTfp4FBmrsu0Hb5H-w2Howm2QNVbEaTQGVo9h-dQcgFNT-TN30Pm_S3kv6JARcdhPp1JkN0go_ulIGP/pub?slide=id.g21d0ef90081_0_0)

*Source: The OLS Team*"""),

    dict(date="2023-10-24", slug="the-1st-open-science-workshop-bordeaux-neurocampus-was-a-big-success",
         title="The 1st Open Science Workshop @ Bordeaux Neurocampus was a big success!!!",
         tags=["events"], images={"group.jpg": "2023/10/openscience-workshop-group-231019-dsc_3569-copie.jpg"},
         body="""![](IMG/group.jpg)

After months of preparation, the [1st Bordeaux Neurocampus Open Science Workshop](https://bordeaux-neurocampus.github.io/OS-Workshop-2023/) is now over and leaves behind a great success and an eager-to-continue community of Open Science enthusiasts!

Highlights can be seen [here](https://www.linkedin.com/posts/eduardagzc_openscience-activity-7121456390115586048-zf-X)."""),

    dict(date="2023-09-17", slug="clean-readable-code-epfl", title="Clean & Readable Code @ EPFL",
         tags=["events"], images={"orper.jpg": "2023/09/orper.jpg"},
         body="""Last week, I had the great opportunity to give a workshop on how to write clean and readable code at the [ORPER summer school](https://orperschool.github.io/) at the Swiss Federal Institute of Technology in Lausanne (EPFL). Furthermore, I participated in a panel discussion with [Russ Poldrack](https://profiles.stanford.edu/russell-poldrack), [Zoltan Dienes](https://profiles.sussex.ac.uk/p718-zoltan-dienes), and [Juliette Boscheron](https://people.epfl.ch/juliette.boscheron) (event organizer & a good friend) about changing the research incentives toward Open Science values.

![](IMG/orper.jpg)"""),

    dict(date="2023-08-11", slug="open-science-talk-ulaval", title="Open Science talk @ ULaval",
         tags=["events"], images={"laval.jpeg": "2023/08/laval.jpeg"},
         body="""Last month, I had a great time at the [Institut Intelligence et données](https://twitter.com/IID_ULaval) (Université Laval) in Canada, where I gave a talk entitled "The 'why, what, and how' of Open Science and its impact on my professional (and personal) journey." The audience was super responsive and asked several great questions – what a pleasure it was to be there!

![](IMG/laval.jpeg)"""),

    dict(date="2023-08-10", slug="bordeauxtea-institut-pasteur", title="BordeauxTea @ Institut Pasteur!",
         tags=["events"], images={"pasteur.jpg": "2023/08/1678869164912.jpg"},
         body="""![](IMG/pasteur.jpg)

Earlier this year, [Fjola Hyseni](https://www.linkedin.com/in/ACoAACbZ_xUBAGWWrgNP0vJeBO8EAcTRpcUNhD4) and I were at Institut Pasteur for the Recherche Reproductible days to present our BordeauxTea (ReproducibiliTea journal club from the Bordeaux Neurocampus) and share our experience so far with Open Science in our Ph.D. The event focused on reproducibility in science and started assembling a French network for reproducible research. It was a great learning experience – thanks to the organizers for inviting us to participate and contribute to this discussion!

A summary of the event can be found here (in French): <https://lnkd.in/eQJp6gXk>"""),

    dict(date="2023-08-09", slug="oswgbordeaux", title="1st Bordeaux Neurocampus Open Science Workshop",
         tags=["events"], images={"flyer.jpg": "2023/08/flyer_page-0001.jpg"},
         body="""Hey! I'm organizing the 1st Open Science Workshop happening at the Bordeaux Neurocampus (France) this October. Registration & food are free, and we have travel grants! More info at: <https://bordeaux-neurocampus.github.io/OS-Workshop-2023/>

![](IMG/flyer.jpg)"""),

    dict(date="2023-08-09", slug="best-paper-award-ohbm-2023", title="Best Paper Award @ OHBM 2023",
         tags=["award"], images={"ohbm.jpg": "2023/08/whatsapp-image-2023-07-23-at-14.24.06-edited-1.jpg"},
         body="""A month back, my master's thesis received the [Best Paper Award from the Brain Structure and Function](https://www.springer.com/journal/429/updates/25948058) editors. This prize is given to the best paper of the year and was handed to me at the Organization for Human Brain Mapping opening ceremony in Montreal, Canada!

Here is the link to the project: <https://github.com/multinetlab-amsterdam/network_TDA_tutorial/tree/main>

Check out the video [here](https://www.linkedin.com/feed/update/urn:li:activity:7089257465199869952/)!

![](IMG/ohbm.jpg)"""),

    dict(date="2023-06-10", slug="promoting-the-dutch-open-science-festival",
         title="Promoting the Dutch Open Science Festival!", tags=["events"], images={},
         body="""Don't miss the National Open Science Festival in Rotterdam on August 31st! I was personally involved in promoting this amazing event. Check it out here: [opensciencefestival.nl](http://opensciencefestival.nl/registration-for-sessions-and-workshops/)

> On why you can't miss the Open Science Festival 2023! An interview with Eduarda Centeno MSc, researcher at Vrije Universiteit Medical Center. #osf2023nl #OpenScience
>
> — National Open Science Festival NL (@osf2023nl), [June 9, 2023](https://twitter.com/osf2023nl/status/1667111802239426560)"""),

    dict(date="2023-06-02", slug="open-science-retreat-in-kochel-am-see",
         title="Open Science Retreat in Kochel am See!", tags=["events"],
         images={"1.jpg": "2023/08/whatsapp-image-2023-08-10-at-01.46.48.jpg",
                 "2.jpg": "2023/08/whatsapp-image-2023-08-10-at-01.46.49.jpg",
                 "3.jpg": "2023/08/whatsapp-image-2023-08-10-at-01.46.482.jpg"},
         body="""In April, I had the opportunity to experience my first Open Science Retreat. It was a full week in a beautiful village by the lake, with many wonderful people and engaging conversations that broadened my horizons about my career and the Open Science movement. By the end of the week, we even developed a comprehensive syllabus to promote the implementation of Open Science in formal education. Feel free to explore it here: [Open Science Education](https://openscienceeducation.org/).

![](IMG/1.jpg)
![](IMG/2.jpg)
![](IMG/3.jpg)"""),

    dict(date="2023-05-10", slug="got-to-represent-the-osc-nl-the-dutch-eosc-meeting",
         title="Got to represent the OSC-NL @ the Dutch EOSC meeting", tags=["events"],
         images={"eosc.jpg": "2023/08/1681420117675.jpg"},
         body="""I was invited to represent the Open Science Communities in the Netherlands at the Dutch EOSC Tripartite meeting at SURF (Utrecht) earlier this year. Alongside other panelists, I advocated for the sustained funding of these communities to facilitate the implementation of Open Science practices in research. You can find more information about the event [here](https://osc-international.com/inosc/osc-nl-at-the-dutch-eosc-tripartite-event/).

![](IMG/eosc.jpg)"""),

    dict(date="2023-02-09", slug="oscawards-hosted-the-event-got-a-prize",
         title="OSCAwards! Hosted the event & got a prize!", tags=["award"],
         images={"1.jpg": "2023/08/dsc02879.jpg", "2.jpg": "2023/08/2dsc02874.jpg",
                 "3.jpg": "2023/08/dsc02759-1.jpg", "4.jpg": "2023/08/dsc02762-1.jpg"},
         body="""![](IMG/1.jpg)

In January, I had the fantastic opportunity to host part of the OSCAwards ceremony [at SPUI25](https://spui25.nl/programma/science-for-all-the-2023-oscawards) and mediate a round table with great Open Science enthusiasts! At the event, I also received an award for my master's thesis work under the 'Open Educational Resources' category. The project is available online [on GitHub](https://github.com/multinetlab-amsterdam/network_TDA_tutorial/tree/main). Go [MULTINET](https://multinetlab.com/) team!

![](IMG/2.jpg)
![](IMG/3.jpg)
![](IMG/4.jpg)"""),

    dict(date="2022-11-11", slug="bordeauxtea-in-brainstorm", title="BordeauxTea in BrainStorm!",
         tags=["article"], images={"brainstorm_1st-issue.pdf": "2023/08/brainstorm_1st-issue_finished.pdf"},
         body="""My partner in crime, Fjola Hyseni, and I wrote a short letter about Open Science and our journey with it for the first edition of [BrainStorm](https://twitter.com/Sci_BrainStorm) – the Neurocampus student journal! Check it out below:

[Download BrainStorm – 1st issue (PDF)](IMG/brainstorm_1st-issue.pdf)"""),

    dict(date="2022-10-10", slug="the-open-science-workgroup-presents-its-first-poster",
         title="The Open Science Workgroup presents its first poster!", tags=["events"],
         images={"poster.jpg": "2023/08/fb4fnzdwyaaf4oq.jpg"},
         body="""Our [Open Science Workgroup](https://anatomy-neurosciences.com/initiatives/openscience/) showcased its first poster at the National Open Science Festival, hosted at Vrije Universiteit Amsterdam in the Netherlands. This great event allowed us to connect with like-minded individuals and expand our network. Our poster even caught the attention of the VU Rector Magnificus!! Explore the festival highlights [here](https://twitter.com/eduardagzc/status/1566695461804802049/photo/1) & stay tuned for more updates as we continue promoting Open Science practices.

![](IMG/poster.jpg)"""),

    dict(date="2022-08-10", slug="tbt-of-my-wet-lab-times", title="#TBT of my wet lab times!",
         tags=["events"], images={"oxford.jpg": "2023/08/1601594481123.jpg"},
         body="""Back in 2016, I used to work with induced pluripotent stem cells with Dr. Bithell and (now Dr.) Pati, investigating models for neurodegenerative diseases. Our work was selected to be presented at the Oxford Dementia Research Day at the University of Oxford. I'm far from the wet lab nowadays, but I'm still very proud of that day! Here is some work that followed from this research: [2D versus 3D human induced pluripotent stem cell-derived cultures for neurodegenerative disease modelling](https://link.springer.com/article/10.1186/s13024-018-0258-4).

![](IMG/oxford.jpg)"""),

    dict(date="2022-07-13", slug="fens-2022", title="FENS 2022!", tags=["events"],
         images={"fens.jpg": "2023/08/1657700503443.jpg"},
         body="""Presented my work at FENS 2022 in Paris, France.

![](IMG/fens.jpg)"""),

    dict(date="2021-10-10", slug="fernando-i-gsi21", title="Fernando & I @ GSI'21!", tags=["events"],
         images={"gsi.png": "2023/08/e6-pophx0ag90rw.png"},
         body="""My great mentor, Fernando Santos, and I got to present our work at the [Conference on Geometric Science of Information](https://web2.see.asso.fr/en/GSI2021) at the Sorbonne University in Paris, France. This occasion also led to a [book chapter](https://link.springer.com/chapter/10.1007/978-3-030-80209-7_71)! (Sorry for the photo's low quality, but that's what we had available in COVID/Zoom times!)

![](IMG/gsi.png)"""),
]


def download(url: str, dest: Path) -> None:
    if dest.exists():
        return
    dest.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            dest.write_bytes(r.read())
        print(f"  ✓ {dest.relative_to(ROOT)}")
    except Exception as e:
        print(f"  ✗ falhou: {url} ({e})")


def main() -> None:
    POSTS_DIR.mkdir(exist_ok=True)
    download(AVATAR, IMG_DIR / "avatar.png")

    for p in POSTS:
        img_url_path = f"/assets/img/posts/{p['slug']}/"
        for name, wp_path in p["images"].items():
            download(WP + wp_path, IMG_DIR / "posts" / p["slug"] / name)

        front = ["---", f"title: {json.dumps(p['title'], ensure_ascii=False)}"]
        if p.get("tags"):
            front.append(f"tags: {json.dumps(p['tags'], ensure_ascii=False)}")
        if p.get("lang"):
            front.append(f"lang: {p['lang']}")
        front.append("---")

        body = p["body"].replace("IMG/", img_url_path)
        out = POSTS_DIR / f"{p['date']}-{p['slug']}.md"
        out.write_text("\n".join(front) + "\n\n" + body + "\n", encoding="utf-8")
        print(f"📝 {out.relative_to(ROOT)}")

    print(f"\nPronto! {len(POSTS)} posts gerados.")


if __name__ == "__main__":
    main()