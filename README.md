# Invoice Deduplication

Find duplicate invoice references within supplier boundaries.

Supplier identifiers are normalized separately from invoice references. Matching references from different suppliers remain distinct.

## Run

Python 3.11 or newer; no external packages.

```sh
python main.py
python -m unittest discover -s tests -v
```

The module exposes its calculation as an importable function and includes a runnable example.
