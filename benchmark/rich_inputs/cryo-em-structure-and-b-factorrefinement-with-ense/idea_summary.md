# Idea Summary: Cryo-EM structure and B-factor refinement with ensemble representation

## Working title
Cryo-EM structure and B-factor refinement with ensemble representation

## Core question
AbstractCryo-EM experiments produce images of macromolecular assemblies that are combined to produce three-dimensional density maps. It is common to fit atomic models of the contained molecules to interpret those maps, followed by a density-guided refinement. Here, we propose TEMPy-REFF, a novel method for atomic structure refinement in cryo-EM density maps. By representing the atomic positions as components of a mixture model, their variances as B-factors, and a model ensemble description, we s

## Motivation / gap
- IntroductionCryo-electron microscopy (cryo-EM) can resolve the structure of biomolecules at an ever-improving resolution.
- Larger complexes can now be visualised as 3-dimensional density maps at near-atomic resolutions, and in various conformations.
- The interpretation of those maps often hinges on fitting atomic models of the different macromolecules present in the complex1–3.
- This procedure is often difficult and requires the user to provide accurate models, and a well-estimated resolution (which can vary at different parts of the map).
- Pre-existing experimental or predicted atomic models may be in a different conformation and converging to a well-fitted one may require significant sampling.Several methods are in common use for this 

## Core contribution (bullet form)
Extracted from abstract:
AbstractCryo-EM experiments produce images of macromolecular assemblies that are combined to produce three-dimensional density maps. It is common to fit atomic models of the contained molecules to interpret those maps, followed by a density-guided refinement. Here, we propose TEMPy-REFF, a novel method for atomic structure refinement in cryo-EM density maps. By representing the atomic positions as components of a mixture model, their variances as B-factors, and a model ensemble description, we significantly improve the fit to the map compared to what is currently achievable with state-of-the-art methods. We validate our method on a large benchmark of 366 cryo-EM maps from EMDB at 1.8-7.1Å resolution and their corresponding PDB assembly models. We also show that our approach can provide newly-modelled regions in EMDB deposited maps by combining it with AlphaFold-Multimer. Finally, our method provides a natural interpretation of maps into components, allowing us to accurately create composite maps.

## Method in brief
MethodsDefinitionsGiven a reference experimental 3D map ME, with an estimated resolution R, we will attempt to improve the fit of a model comprised of N atoms, that has estimated coordinates , B-factors , and occupancies  (which we will set to 1 and ignore thereafter).AlgorithmThe full algorithm can be summarised below with detailed explanation following:
Initialise coordinates , B-factors , and resolution r.Loop over:
Compute conformational energy and forces  and , for a given forcefield.Compute a simulated density map  Compute map-derived forces .Change coordinates X using .Change B-factors and occupancies based on the experimental cryo-EM map, ME.Simulated cryo-EM mapFrom the position X and the B-factors B, we can compute a simulated map, MS, by adding up the expected intensity due to each atom in a given group of atoms, modelled with a Gaussian distribution:



with each Gaussian taking the form:



with Nithe atomic number of the corresponding atom with index i, xithe cartesian coordinates, and Bithe B-factor. Although it is possible to define a 3-dimensional B-factor, we restrict ourselves to a scalar for our refinement.Finally, we consider the error (which comprises background noise, reconstruction errors, and additional components) as a uniform distribution across the whole map, determined by a single scalar parameter:



with kbg the uniform distribution parameter, corresponding to the average background noise level. We thus obtain the final expression for the simula

## Target venue
Nature Communications
