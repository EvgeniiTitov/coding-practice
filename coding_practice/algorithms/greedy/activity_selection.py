"""
Greedily pick activities coming right after each other
"""


def main():
    activities = [
        ["A1", 0, 6],
        ["A2", 3, 4],
        ["A3", 1, 2],
        ["A4", 5, 8],
        ["A5", 5, 7],
        ["A6", 8, 9],
    ]
    activities.sort(key=lambda item: item[-1])

    picked_activities = [activities.pop(0)]
    for activity in activities:
        _, activity_start, activity_end = activity
        prev_end = picked_activities[-1][-1]
        if activity_start > prev_end:
            picked_activities.append(activity)

    # [['A3', 1, 2], ['A2', 3, 4], ['A5', 5, 7], ['A6', 8, 9]]
    print(picked_activities)


if __name__ == "__main__":
    main()
