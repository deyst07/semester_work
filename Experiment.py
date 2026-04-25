import os
import time
import csv

from GraphTopologicalSort import Graph


def run_experiment():

    folder = "graphs"
    results = []

    files = sorted(
        os.listdir(folder),
        key=lambda x: int(x.split("_")[1].split(".")[0])
    )

    for filename in files:

        filepath = os.path.join(folder, filename)
        g = Graph(0)
        g.load_from_file(filepath)
        g.topological_sort_kahn()
        
        times = []
        order, iterations = g.topological_sort_kahn()

        for _ in range(5):
            start = time.perf_counter()
            g.topological_sort_kahn()
            end = time.perf_counter()
            times.append(end - start)

        execution_time = sum(times) / len(times)
        
        results.append((g.V, execution_time, iterations))

        print(f"{filename}: done")

    save_results(results)


def save_results(results):

    with open("results.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Vertices", "Time", "Iterations"])
        writer.writerows(results)


if __name__ == "__main__":
    run_experiment()
