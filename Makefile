.PHONY: all docs

build_assets:
	echo "y" | uv run marimo export html-wasm --mode edit notebooks/sudoku_solver_example.py -o docs/assets/sudoku_solver_notebook

serve:
	uv run mkdocs serve --watch docs/blog