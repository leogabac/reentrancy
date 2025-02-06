# Python Scripts

In this page, you will find a brief overview on what all scripts are supposed to make.\
To see the detailed implementation, check each script individually.

1. Simulations.

| Name            | Type | Description                                                                      |
| --------------- | ---- | -------------------------------------------------------------------------------- |
| test11.py       | SIM  | Sim. at selected $\omega=\pi/2/\tau$ and $B$. <br> Run `python test11.py --help` |
| test11_field.py | AUX  | Magnetic field string for LAMMPS                                                 |

2. Long-running computations for later visualization.

| Name              | Type | Scope            | Description                                                          |
| ----------------- | ---- | ---------------- | -------------------------------------------------------------------- |
| make_chir.py      | LR   | FRAMES <br> BULK | Comp. chirality OP.                                                  |
| make_kappe.py     | LR   | FRAMES <br> BULK | Comp. charge OP.                                                     |
| take_distances.py | LR   | FRAMES <br> BULK | Comp. displacement (parallel) $\mathbf{r}(t)$                        |
| trim_distances.py | LR   | FRAMES <br> BULK | Trims a lighter version from `take_distances.py` data for 20mT only. |
