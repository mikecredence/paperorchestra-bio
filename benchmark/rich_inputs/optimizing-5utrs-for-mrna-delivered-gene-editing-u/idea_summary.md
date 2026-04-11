# Idea Summary: Optimizing 5’UTRs for mRNA-delivered gene editing using deep learning

## Working title
Optimizing 5’UTRs for mRNA-delivered gene editing using deep learning

## Core question
AbstractmRNA therapeutics are revolutionizing the pharmaceutical industry, but methods to optimize the primary sequence for increased expression are still lacking. Here, we design 5’UTRs for efficient mRNA translation using deep learning. We perform polysome profiling of fully or partially randomized 5’UTR libraries in three cell types and find that UTR performance is highly correlated across cell types. We train models on all our datasets and use them to guide the design of high-performing 5’UT

## Motivation / gap
- IntroductionmRNA therapeutics and vaccines provide a safe, effective, and flexible method of delivering transient genetic instructions to living cells and tissues1.
- Compared to plasmid or AAV-based delivery, mRNA offers several advantages, including simple manufacturing that is independent of the encoded therapeutic protein2, lower immunogenicity, and transient g
- As a result, mRNA technology has been crucial for the rapid development of vaccines against the COVID-19 pandemic5,6, and is currently being developed for applications such as protein replacement ther
- An intriguing use of the mRNA platform is delivery of gene editing reagents3,14, because transient expression of gene editors avoids deleterious effects from prolonged exposure such as off-target edit
- Though there are multiple gene editing platforms, single-chain compact enzymes such as megaTALs16 are particularly well-suited to mRNA delivery.

## Core contribution (bullet form)
Extracted from abstract:
AbstractmRNA therapeutics are revolutionizing the pharmaceutical industry, but methods to optimize the primary sequence for increased expression are still lacking. Here, we design 5’UTRs for efficient mRNA translation using deep learning. We perform polysome profiling of fully or partially randomized 5’UTR libraries in three cell types and find that UTR performance is highly correlated across cell types. We train models on all our datasets and use them to guide the design of high-performing 5’UTRs using gradient descent and generative neural networks. We experimentally test designed 5’UTRs with mRNA encoding megaTALTM gene editing enzymes for two different gene targets and in two different cell lines. We find that the designed 5’UTRs support strong gene editing activity. Editing efficiency is correlated between cell types and gene targets, although the best performing UTR was specific to one cargo and cell type. Our results highlight the potential of model-based sequence design for mRNA therapeutics.

## Method in brief
MethodsPolysome profiling in HepG2 cellsHepG2 cells were cultured in EMEM + 10% FBS. The cells were in culture prior to the experiment, passage conditions were 20 mL media and cells at 2e5/mL into a T-75 flask, and cells were allowed to expand for 3 days prior to transfection. Cells used were at passage 6. IVT mRNA corresponding to the 5’UTR 50nt “fixed-end” library was taken from our previous work33. 1 ug IVT mRNA was transfected into one million cells with the Lonza 4D Nucleofector, following the manufacturer’s protocol. Cell lysis was performed 8 hours later, followed by polysome profiling, library preparation, and Illumina sequencing as previously described33.Polysome profiling in T cellsT cells were enriched from peripheral blood mononuclear cells (PBMCs) isolated via Ficoll-Paque gradient centrifugation from healthy donors. Activation was performed with anti CD3/CD28 antibodies in the presence of IL-2. Salt solution and lysis buffer for polysome profiling were prepared as previously described33. IVT mRNA corresponding to the 5’UTR 50nt “fixed-end” library synthesized as part of our previous work33 was used here. 1 ug IVT mRNA was transfected into one million cells with the Lonza 4D Nucleofector, following the manufacturer’s protocol. Transfected cells were plated in T cell growth medium (TCGM) at 1 million cells/mL and incubated at 37C, 5% CO2. 8 hours later, cycloheximide was added dropwise to the media to a final concentration of 100 ug/mL and incubated for 5 addition

## Target venue
Nature Communications
