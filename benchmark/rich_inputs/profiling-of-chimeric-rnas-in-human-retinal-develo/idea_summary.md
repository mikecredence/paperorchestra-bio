# Idea Summary: Profiling of chimeric RNAs in human retinal development with retinal organoids

## Working title
Profiling of chimeric RNAs in human retinal development with retinal organoids

## Core question
AbstractChimeric RNAs have been found in both cancer and healthy human cells. They have regulatory effects on human stem/progenitor cell differentiation, stemness maintenance and central nervous system (CNS) development. However, their physiological functions in the retinal development remain unknown. Based on the human embryonic stem cells (hESC)-derived retinal organoids (ROs) spanning from day 0 to day 120, we present the expression atlas of chimeric RNAs throughout the developing ROs. We con

## Motivation / gap
- IntroductionThe human retina is a laminal structure with a large number of different constituent cells that form morphologically and functionally distinct circuits.
- They work in parallel and in combination to produce complex visual output (Hoon et al., 2014).
- During retinogenesis, different subtypes of neurons are generated from the same group of retinal progenitor cells and self-assembled accurately into a functionally mature retina (Masland, 2012).Dissec
- A few groups systematically expounded the transcriptomics, chromatin accessibility and proteomic dynamics during human and mouse retinogenesis (Huang et al., 2022), and comprehensively described the s
- They identified an unexpected role for ATOH7 expression in regulation of photoreceptor specification during late retinogenesis (Lu et al., 2020), as well as the enriched bivalent modification of H3K4m

## Core contribution (bullet form)
Extracted from abstract:
AbstractChimeric RNAs have been found in both cancer and healthy human cells. They have regulatory effects on human stem/progenitor cell differentiation, stemness maintenance and central nervous system (CNS) development. However, their physiological functions in the retinal development remain unknown. Based on the human embryonic stem cells (hESC)-derived retinal organoids (ROs) spanning from day 0 to day 120, we present the expression atlas of chimeric RNAs throughout the developing ROs. We confirmed the existence of some common chimeric RNAs and also discovered many novel chimeric RNAs during retinal development. We focused on CTNNBIP1-CLSTN1 (CTCL) whose downregulation causes precocious neuronal differentiation and a marked reduction of neural progenitors in human cerebral organoids. Our study found that CTCL also plays a key role in human retinogenesis, CTCL loss-of-function obstructed RO differentiation but prompted the retinal pigment epithelial (RPE) differentiation. Together, this work provides a landscape of chimeric RNAs and reveals evidence for their crucial roles in human retina development.

## Method in brief
Materials and methodsRNA sequencing and data analysisA total amount of 1-3μg RNA per sample was used as input material for the RNA sample preparations. Sequencing libraries were generated using VAHTS Universal V6 RNA-seq Library Prep Kit for Illumina ® (NR604-01/02) following the manufacturer’s recommendations and index codes were added to attribute sequences to each sample. Briefly, mRNA was purified from total RNA using poly-T oligo-attached magnetic beads. Then we added fragmentation buffer to break the mRNA into short fragments. First strand cDNA was synthesized using random hexamer primer and RNase H. Second strand cDNA synthesis was subsequently performed using buffer, dNTPs, DNA polymerase I and RNase H. And then, the double stranded cDNA was purified by AMPure P beads or QiaQuick PCR kit. The purified double stranded cDNA was repaired at the end, added a tail and connected to the sequencing connector, then the fragment size was selected, and finally the final cDNA library was obtained by PCR enrichment.We used FusionCatcher software (https://github.com/ndaniel/fusioncatcher) to identify chimeric RNAs in human ROs. Positive chimeric RNAs identified using FusionCatcher were selected with alignment of spanning unique reads. The expression level of chimeric RNAs was reflected from log (Spanning_unique_reads/Total_number_of_reads*10000000) value. To analyze the expression of parental genes in human ROs, raw reads were first mapped to the hg38 human genome reference sequenc

## Target venue
eLife
