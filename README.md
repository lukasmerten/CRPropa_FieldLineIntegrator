# CRPropa_FieldLineIntegrator
CRPropa plugin to integrate a magnetic field line.

## Installation 
See the CRPropa plug-in [documentation](https://crpropa.github.io/CRPropa3/pages/example_notebooks/extending-CRPropa/extending-CRPropa.html#Plugins:-Integrate-Custom-C++-Code-to-CRPropa%E2%80%99s-Python-Steering) for installation advice.

## Usage
The FieldLineIntegrator can be used instead of a classical propagation module, e.g., *PropagationBP*. The positions stored in the cadidate correspond to positions along the magnetic field line, which passes through the source position of the Candidate.

The integration direction - parallel or anti-parallel to the magnetic field direction - can be speciefied with the *direction* keyword.

## Citation
When you use the FieldLineIntegrator cite this git repository.
