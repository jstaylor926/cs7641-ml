# CS 7641 — Machine Learning: Python Environment

Reproducible Python environment covering all four units of CS 7641: Supervised
Learning (SL), Optimization & Uncertainty in Learning (OL), Unsupervised
Learning (UL), and Reinforcement Learning (RL). Package selection follows the
**Software** section of the course syllabus.

## Quick start (conda / mamba — recommended)

```bash
cd environment/scripts
bash setup.sh
conda activate cs7641
```

`setup.sh` creates the `cs7641` environment, registers a Jupyter kernel
("Python (CS7641)"), and runs an import smoke-test. If you don't have conda,
install [Miniforge](https://github.com/conda-forge/miniforge) first.

Manual alternative:

```bash
mamba env create -f environment/conda/environment.yml   # or: conda env create -f ...
conda activate cs7641
python environment/scripts/verify_env.py
```

## pip / venv alternative

```bash
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r environment/requirements/requirements.txt
python environment/scripts/verify_env.py
```

## What's included, mapped to the course

| Area | Packages | Used in |
|------|----------|---------|
| Numerical / data | numpy, scipy, pandas, polars | all units |
| Core ML | scikit-learn, imbalanced-learn | SL, UL |
| Boosted trees | xgboost, lightgbm, catboost | SL |
| Neural networks | pytorch, torchvision, lightning | SL3 |
| Optimization / tuning | optuna, scikit-optimize | OL |
| Interpretability / calibration | shap, eli5, lime | reports, diagnostics |
| Reinforcement learning | gymnasium, stable-baselines3, pymdptoolbox | RL |
| Visualization | matplotlib, seaborn, plotly, altair | reports |
| Notebooks | jupyterlab, ipykernel, ipywidgets | all units |

Python is pinned to **3.11** for broad compatibility across PyTorch, the
gradient-boosting libraries, and the RL stack. The full set (183 resolved
packages) was dependency-checked and resolves with no conflicts.

## Notes / deliberate omissions

- **PyTorch only.** TensorFlow/Keras and JAX/Flax are listed as alternatives in
  the syllabus, not requirements — omitted to keep the environment lean. The
  syllabus recommends PyTorch for MLPs on tabular data.
- **`scikit-learn-extra`** (k-medoids, etc.) is intentionally left out. Its last
  release pins `scikit-learn < 1.4`, which would hold the whole environment back
  several major versions. If you specifically need it for a UL experiment,
  install it into a separate throwaway env rather than this one.
- **Optional extras** not included (add to `environment.yml` if you go there):
  time-series tooling (statsmodels, darts, prophet), experiment trackers
  (MLflow, W&B), distributed RL (RLlib), and fairlearn/netcal.

## Reproducibility

To capture an exact lock of what you actually installed:

```bash
conda activate cs7641
pip freeze > environment/requirements/requirements.lock.txt
```
