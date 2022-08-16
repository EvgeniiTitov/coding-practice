import typing as t


ConstraintCheckCallable = t.Callable[[t.List[t.Optional[t.Any]], int], ...]


def solve(
    values: t.Iterable[t.Any],
    constraint_check_callable: ConstraintCheckCallable,
    nb_slots: int
):
    solution = [None] * nb_slots

    def extend_solution(position: int) -> t.Optional[t.List[t.Any]]:
        for value in values:
            solution[position] = value
            if constraint_check_callable(solution, position):
                if position >= nb_slots - 1 or extend_solution(position + 1):
                    return solution
        return None

    return extend_solution(0)
