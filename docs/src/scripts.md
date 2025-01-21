# Script documentation/overview

In this page, you will find a brief overview on what all scripts are supposed to make. To see the detailed implementation, check each script individually.

## Python Scripts

In this directory, you can find regular python scripts for either

1. Simulations.
2. Long-running computations for later visualization.

| Name              | Type | Description                                                                      |
| ----------------- | ---- | -------------------------------------------------------------------------------- |
| test11.py         | SIM  | Sim. at selected $\omega=\pi/2/\tau$ and $B$. <br> Run `python test11.py --help` |
| test11_field.py   | AUX  | Magnetic field string for LAMMPS                                                 |
| make_chir.py      | LR   | Comp. chirality OP for all frames in bulk.                                       |
| make_kappe.py     | LR   | Comp. charge OP for all frames in bulk.                                          |
| take_distances.py | LR   | Comp. displacement (parallel) at any time (in bulk) $\mathbf{r}(t)$              |
| trim_distances.py | LR   | Trims a lighter version from `take_distances.py` data for 20mT only.             |
