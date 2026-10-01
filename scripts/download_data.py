from __future__ import annotations

import csv
import sys
from io import StringIO

import pandas as pd
import requests

from inf8239_u02.config import ROOT, settings
from inf8239_u02.data import sha256


def main() -> int:
    if settings.data_source == "local":
        print(f"Modo local. Archivo configurado: {settings.dataset_path}")
        return 0

    if settings.data_source != "url" or not settings.dataset_url:
        print("Configure DATA_SOURCE=url y DATASET_URL en .env", file=sys.stderr)
        return 2

    output = ROOT / "data/raw/dataset.csv"
    output.parent.mkdir(parents=True, exist_ok=True)

    response = requests.get(settings.dataset_url, timeout=60)
    response.raise_for_status()

    content = response.content.decode("utf-8")

    csv.field_size_limit(10_000_000)

    rows = list(csv.reader(StringIO(content), delimiter="\t"))

    header = rows[0]
    data = rows[1:]

    valid_rows = [row for row in data if len(row) == len(header)]

    df = pd.DataFrame(valid_rows, columns=header)
    df.to_csv(output, index=False, encoding="utf-8")

    print(f"Guardado: {output}")
    print(f"Filas: {len(df)}")
    print(f"Columnas: {list(df.columns)}")
    print(f"SHA-256: {sha256(output)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())