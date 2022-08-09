def main():
    states_needed = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}

    stations = dict()
    stations["kone"] = {"id", "nv", "ut"}
    stations["ktwo"] = {"wa", "id", "mt"}
    stations["kthree"] = {"or", "nv", "ca"}
    stations["kfour"] = {"nv", "ut"}
    stations["kfive"] = {"ca", "az"}

    stations_selected = set()
    while len(states_needed):
        states_covered = set()
        best_station = None
        for station, states_station_covers in stations.items():
            covered = states_station_covers.intersection(states_needed)
            if len(covered) > len(states_covered):
                states_covered = covered
                best_station = station

        stations_selected.add(best_station)
        states_needed -= states_covered

    print("Stations selected:", stations_selected)


if __name__ == "__main__":
    main()
