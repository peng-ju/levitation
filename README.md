### This repository contains useful codes for the levitation experiment.

---
## Instructions

1. Make sure you have installed `python3.10.13` or do `sudo apt install Python3.10.13`.
2. Clone the repo.
3. (Recommended) Create and activate a [virtualenv](https://virtualenv.pypa.io/) under the `env/` directory. Git is already configured to ignore it.
4. Install the very minimal requirements using `pip3 install -r requirements.txt`
5. Run [Jupyter](https://jupyter.org/) in whatever way works for you. The simplest would be to run `pip3 install jupyter && jupyter notebook`.
6. Activate your virtual environment with `source venv/bin/activate`,
7. Run Python script within your virtual environment.

---
- `physics_constant.py` contains all physics constant used in the simulations.
- `helpers.py` contains helper functions for the simulations.
- `Free_fall.ipynb` simulates how a nanoparticle rotates in the free fall experiment.