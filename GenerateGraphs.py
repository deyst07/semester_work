import random
import os


def generate_dag(vertices, edge_probability=0.02):
    """
    Генерирует случайный DAG-граф
    vertices — число вершин
    edge_probability — вероятность появления ребра
    """

    edges = []

    for i in range(vertices):
        for j in range(i + 1, vertices):
            if random.random() < edge_probability:
                edges.append((i, j))

    return edges


def save_graph(filename, vertices, edges):
    """
    Сохраняет граф в файл
    """

    with open(filename, "w") as f:
        f.write(str(vertices) + "\n")
        for u, v in edges:
            f.write(f"{u} {v}\n")


def generate_dataset():

    os.makedirs("graphs", exist_ok=True)

    sizes = list(range(100, 10001, 200))

    print("Generating graphs...")

    for size in sizes:
        edges = generate_dag(size)
        filename = f"graphs/graph_{size}.txt"
        save_graph(filename, size, edges)

        print(f"Saved {filename}")


if __name__ == "__main__":
    generate_dataset()
