# Diffusionless Transformation leading to Anistotropic CI GS

Dynamics of Colloidal Ice when the external magnetic field $\mathbf{B}$ is rotated.

- Paper Title (Temptative): Magnetically-Driven Diffusionless Tranformations and Ergodicity Breaking in Square Anisotropic Colloidal Ice
- Authors: [leogabac](https://github.com/leogabac/), and [aortiza](https://github.com/aortiza).

For detailed information, go to the [DOCUMENTATION](./docs/index.md).

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
> Each directory has its own _README_ with code documentation.
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
 The main idea behind this file structure is to 
1. Generate data using a script from the `py` directory. (Long-running jobs)
2. Import the generated data into a notebook from the `notebook` directory for analysis, visualization and figure making.

This intended workflow comes from an opinionated programmer (myself) who finds Jupyter Notebooks rather unstable for long-running jobs, but still uses them for interactive visualization.




