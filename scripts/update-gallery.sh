#!/usr/bin/env bash
# Wrapper que usa o virtualenv local (.venv) se existir.
# Cria o venv + instala Pillow automaticamente na primeira execução.
set -euo pipefail

cd "$(dirname "$0")/.."

VENV_DIR=".venv"

if [ ! -x "${VENV_DIR}/bin/python" ]; then
  echo "Criando virtualenv em ${VENV_DIR}..."
  python3 -m venv "${VENV_DIR}"
  "${VENV_DIR}/bin/pip" install --quiet --upgrade pip
  "${VENV_DIR}/bin/pip" install --quiet Pillow
fi

if ! "${VENV_DIR}/bin/python" -c "import PIL" 2>/dev/null; then
  echo "Instalando Pillow no venv..."
  "${VENV_DIR}/bin/pip" install --quiet Pillow
fi

exec "${VENV_DIR}/bin/python" scripts/update-gallery.py "$@"
