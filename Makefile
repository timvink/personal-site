# A bare `make` serves the site; it must never rebuild the committed notebook bundle.
.DEFAULT_GOAL := serve

.PHONY: build_assets serve

build_assets:
	echo "y" | uv run marimo export html-wasm --mode edit notebooks/sudoku_solver_example.py -o docs/assets/sudoku_solver_notebook

serve:
	uv run mkdocs serve
