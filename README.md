# Diffusionless Transformation leading to Anistotropic CI GS

Dynamics of Colloidal Ice when the external magnetic field $\mathbf{B}$ is rotated.

- Paper Title (Temptative): Magnetically-Driven Diffusionless Tranformations and Ergodicity Breaking in Square Anisotropic Colloidal Ice

## Installation
To install this project, clone the repository into 
```bash
git clone https://github.com/leogabac/reentrancy.git ~/Documents/reentrancy
```
The codes assume that you have my fork of [icenumerics](https://github.com/leogabac/icenumerics) in the _dev_ branch. This repo must be located in the same parent directory where this repo was cloned.
```
git clone https://github.com/leogabac/icenumerics.git ~/Documents/icenumerics --recurse-submodules
```

## File tree
This is a brief overview and explanation of the file tree of this project.
```
.
├── src
│   ├── auxnumerics/ (Auxiliary functions)
│   ├── notebooks/ (Notebooks for figure making and data vis)
│   ├── py/ (Python scripts for sims and long jobs)
│   ├── static/ (General scripts that will never be modified)
│   ├── parameters.py
│   ├── parameters_thermal.py
│   └── tmp.ipynb
├── LICENSE
├── README.md
├── requirements.txt
```
Each directory has its own _README_ with code documentation.


