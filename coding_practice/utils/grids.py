import typing as t


__all__ = ["print_grid"]


Grid = t.List[t.List[t.Any]]


def print_grid(grid: Grid, **kwargs) -> None:
    print()
    rows = len(grid)
    for i in range(rows):
        print(" ".join(map(str, grid[i])), **kwargs)
