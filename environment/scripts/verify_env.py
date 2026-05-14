"""CS 7641 environment verification.

Imports the key library for every course unit and prints its version.
Run inside the activated env:  python verify_env.py
"""
import importlib
import sys

# (import name, friendly label, course unit)
CHECKS = [
    ("numpy",            "NumPy",            "core"),
    ("scipy",            "SciPy",            "core"),
    ("pandas",           "pandas",           "core"),
    ("polars",           "polars",           "core"),
    ("sklearn",          "scikit-learn",     "SL / UL"),
    ("imblearn",         "imbalanced-learn", "SL"),
    ("xgboost",          "XGBoost",          "SL"),
    ("lightgbm",         "LightGBM",         "SL"),
    ("catboost",         "CatBoost",         "SL"),
    ("torch",            "PyTorch",          "SL (neural nets)"),
    ("lightning",        "PyTorch Lightning","SL (neural nets)"),
    ("optuna",           "Optuna",           "OL"),
    ("skopt",            "scikit-optimize",  "OL"),
    ("shap",             "SHAP",             "diagnostics"),
    ("eli5",             "ELI5",             "diagnostics"),
    ("lime",             "LIME",             "diagnostics"),
    ("gymnasium",        "Gymnasium",        "RL"),
    ("stable_baselines3","Stable-Baselines3","RL"),
    ("mdptoolbox",       "pymdptoolbox",     "RL"),
    ("matplotlib",       "matplotlib",       "viz"),
    ("seaborn",          "seaborn",          "viz"),
    ("plotly",           "plotly",           "viz"),
    ("altair",           "altair",           "viz"),
    ("jupyterlab",       "JupyterLab",       "notebooks"),
]

def main() -> int:
    print(f"Python {sys.version.split()[0]}\n")
    failures = []
    width = max(len(label) for _, label, _ in CHECKS)
    for mod, label, unit in CHECKS:
        try:
            m = importlib.import_module(mod)
            ver = getattr(m, "__version__", "?")
            print(f"  OK   {label:<{width}}  {ver:<12}  [{unit}]")
        except Exception as exc:  # noqa: BLE001
            print(f"  FAIL {label:<{width}}  {'--':<12}  [{unit}]  -> {exc}")
            failures.append(label)

    print()
    if failures:
        print(f"{len(failures)} package(s) failed to import: {', '.join(failures)}")
        return 1
    print(f"All {len(CHECKS)} packages imported successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
