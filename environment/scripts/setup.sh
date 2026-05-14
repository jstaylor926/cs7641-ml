#!/usr/bin/env bash
# CS 7641: Machine Learning - environment bootstrap
# Usage:  bash setup.sh
#
# Creates the `cs7641` conda environment from ../conda/environment.yml,
# registers a Jupyter kernel, and runs a quick import smoke-test.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ENV_FILE="$SCRIPT_DIR/../conda/environment.yml"
ENV_NAME="cs7641"

# Prefer mamba if available (much faster solver), else fall back to conda.
if command -v mamba >/dev/null 2>&1; then
  CONDA_CMD="mamba"
elif command -v conda >/dev/null 2>&1; then
  CONDA_CMD="conda"
else
  echo "ERROR: neither mamba nor conda found on PATH."
  echo "Install Miniforge first: https://github.com/conda-forge/miniforge"
  exit 1
fi

echo "==> Using: $CONDA_CMD"
echo "==> Env file: $ENV_FILE"

if conda env list | grep -qE "^\s*${ENV_NAME}\s"; then
  echo "==> Environment '${ENV_NAME}' exists. Updating (with --prune)..."
  $CONDA_CMD env update -f "$ENV_FILE" --prune
else
  echo "==> Creating environment '${ENV_NAME}'..."
  $CONDA_CMD env create -f "$ENV_FILE"
fi

# Register a Jupyter kernel so notebooks can select this env.
echo "==> Registering Jupyter kernel..."
conda run -n "$ENV_NAME" python -m ipykernel install --user \
  --name "$ENV_NAME" --display-name "Python (CS7641)"

# Smoke-test: import the key libraries for each unit.
echo "==> Running import smoke-test..."
conda run -n "$ENV_NAME" python "$SCRIPT_DIR/verify_env.py"

echo ""
echo "==> Done. Activate with:  conda activate ${ENV_NAME}"
