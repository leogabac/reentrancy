# Python Scripts
In this directory, you can find regular python scripts for either
1. Simulations.
2. Long-running computations for later visualization.

## Simulations

- **test11.py**\
Simulation at selected $\omega = \pi/2/\tau$ and magnetic $B$. For more information, run
```
python test11.py --help
```
- **test11_field.py** Magnetic field string for LAMMPS.

## Long-Running Jobs

- **make_chir.py**/
Computes the chirality order parameter for all frames in bulk. All $\omega$, $B$ at given size.

- **make_kappa.py**/
Computes the charge order parameter for all frames in bulk. All $\omega$, $B$ at given size.

- **take_distances.py**/
Computes the travelled distance (parallel) at any time $\mathbf{r}(t) = | \mathbf{r}(t) - \mathbf{r}(0) |$ in bulk.

Schema:
| 1 ... N | total_time | field | realization | t | theta

- **trim_distances.py**/
Fils from `take_distances.py` are too big to handle. This script trims a lighter version for 20mT only.
