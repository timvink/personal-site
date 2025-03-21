import marimo

__generated_with = "0.11.22"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import micropip
    return (micropip,)


@app.cell(hide_code=True)
async def _(micropip):
    await micropip.install("sudoku-solver-tim")
    import sudoku_solver_tim
    return (sudoku_solver_tim,)


@app.cell
def _():
    from sudoku_solver_tim import Puzzle

    grid = [
        [9, 3, 4, 0, 6, 0, 0, 5, 0],
        [0, 0, 6, 0, 0, 4, 9, 2, 3],
        [0, 0, 8, 9, 0, 0, 0, 4, 6],
        [8, 0, 0, 5, 4, 6, 0, 0, 7],
        [6, 0, 0, 0, 1, 0, 0, 0, 5],
        [5, 0, 0, 3, 9, 0, 0, 6, 2],
        [3, 6, 0, 4, 0, 1, 2, 7, 0],
        [4, 7, 0, 6, 0, 0, 5, 0, 0],
        [0, 8, 0, 0, 0, 0, 6, 3, 4],
    ]
    puzzle = Puzzle(grid)

    # Find the easiest strategy to make progress (remove a pencil mark)
    _ = puzzle.solve_step()
    return Puzzle, grid, puzzle


@app.cell
def _(puzzle):
    # Solve the entire puzzle
    puzzle.solve()
    print(f"\nPuzzle Solved. Strategies used: {puzzle.strategies_used}")
    print(puzzle)
    return


if __name__ == "__main__":
    app.run()
