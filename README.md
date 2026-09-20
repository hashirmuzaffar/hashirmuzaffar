# Hashir Muzaffar

ML systems engineer in New York. I build speech and language systems that run in
production, and study where they quietly go wrong.

MS Computer Engineering (ML Systems) at NYU Tandon. Co-founder and lead ML
engineer at Zotivo AI, where I work on production voice AI.

---

### Research

**Selective faithfulness in LLM hiring decisions.** When a model is told to
favour a demographic group, does its written justification say so? A four-arm
crossed design over three model families, with blind re-scoring and a two-tier
verbalization detector validated against hand labels. Under revision for FAccT
2027; the collection and analysis pipeline is public.
→ [selective-faithfulness](https://github.com/hashirmuzaffar/selective-faithfulness)

**Cultural bias in vision-language models.** A pilot audit of LLaVA-NeXT on
South Asian representation. Found a 9× domestic-association gap mediated by
clothing, and a 14× exoticisation gap on cultural-event imagery. Proposed MS
thesis direction.
→ [vlm-cultural-bias-pilot](https://github.com/hashirmuzaffar/vlm-cultural-bias-pilot)

Reviewer for AIES.

---

### Systems

**Music recommendation, end to end.** The data and feedback-loop half of a
four-person MLOps build on a self-hosted music server: a Go scrobbler emitting
real listening events, session datasets built for GRU4Rec/SessionKNN, and drift
monitoring on Prometheus + Grafana closing the loop back into retraining.
→ [navidrome-mlops-data-proj05](https://github.com/hashirmuzaffar/navidrome-mlops-data-proj05)

---

### Stack

`Python` `Go` `PyTorch` `ONNX Runtime` `FastAPI` `Kubernetes` `Docker`
`Prometheus` `Grafana` `Redis` `Parquet` `PostgreSQL`

Speech and voice AI · recommender systems · LLM evaluation and auditing ·
model serving and drift monitoring

---

<sub>Most of my day-to-day production work is closed-source. The repos above are
the ones I can show: independent research and coursework, documented so the
design decisions are readable without me in the room.</sub>
