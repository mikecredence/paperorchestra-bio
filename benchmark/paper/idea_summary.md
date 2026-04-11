# Idea Summary: BiomedWritingBench

## Working title
BiomedWritingBench: A Multi-Agent Pipeline and Benchmark for Automated Biomedical Research Paper Writing

## Core question
Can a multi-agent pipeline with domain-specific tool integrations (bioRxiv, PubMed, ClinicalTrials.gov) produce higher-quality biomedical research papers than a single-agent LLM baseline? And how do both compare to human-written published papers?

## Motivation / gap
- PaperOrchestra (Song et al., 2025) demonstrated multi-agent paper writing for AI/ML papers (CVPR/ICLR), but no equivalent exists for biomedical research
- Biomedical papers require domain-specific literature discovery (PubMed, bioRxiv), clinical trial verification, and specialized citation practices — challenges not addressed by ML-focused systems
- No standardized benchmark exists for evaluating automated biomedical paper writing
- Existing automated writing systems are evaluated only on AI conference papers — unclear if they generalize to the diverse subfields of biomedicine (genomics, neuroscience, immunology, drug discovery, etc.)
- The value of multi-agent orchestration vs simple single-pass LLM generation for scientific writing has not been quantified with statistical rigor

## Core contribution (bullet form)
- **BiomedWritingBench**: First benchmark dataset for automated biomedical paper writing — 60 test cases across 10 subfields, reverse-engineered from published bioRxiv preprints with ground truth metadata
- **Bio Paper Orchestra**: A multi-agent paper writing skill with 5-stage pipeline (Outline, Literature, Plot, Writing, Refinement) integrating bioRxiv, PubMed, and ClinicalTrials.gov MCP tools for domain-specific literature discovery
- **Controlled evaluation**: Paired comparison of multi-agent pipeline vs single-agent baseline on 20 papers across 10 biomedical subfields, with structural metrics, LLM-as-judge scoring on 7 axes, and ground truth comparison
- **Key finding**: Multi-agent pipeline produces 86% more citations (p<0.001), significantly higher citation quality (p<0.001) and completeness (p<0.05) scores, while maintaining comparable prose quality — reaching 40% of published paper citation counts vs 20% for baseline
- **Anti-leakage protocol**: Demonstrated prevention of content leakage from pre-training data (abstract similarity to ground truth: 0.10 for both conditions)
- **Open-source release**: Full pipeline, benchmark dataset, evaluation scripts, and all generated papers available at github.com/mikecredence/paperorchestra-bio

## Method in brief
- 5-stage pipeline: (1) Outline Agent generates structured JSON plan, (2) Plot Agent creates figures, (3) Literature Agent discovers and verifies citations via multi-channel search (web + bioRxiv API + Semantic Scholar), (4) Writing Agent produces LaTeX with anti-leakage safeguards, (5) Refinement Agent iterates with 0-100 scoring and rollback
- BiomedWritingBench: 60 test cases constructed by reverse-engineering bioRxiv preprints published in Nature, eLife, Genome Biology, etc. — extracting idea summaries and experimental logs as inputs, with published papers as ground truth
- Evaluation: structural metrics (citation count, word count, compilation rate), LLM-as-judge quality scoring (7 axes: clarity, rigor, completeness, writing, presentation, citations, overall), and distance to ground truth (citation ratio, abstract similarity)
- Statistical testing: paired Wilcoxon signed-rank tests on all metrics (n=20)

## Target venue
NeurIPS 2025 Workshop on Foundation Models for Science (or similar AI+Science workshop)
