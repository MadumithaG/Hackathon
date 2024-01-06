import json

final = {}

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def printSolution(self, dist):
        for node in range(self.V):
            print(node, "\t\t", dist[node])
            final[node] = dist[node]

    def minDistance(self, dist, sptSet):
        min_distance = 1e7
        min_index = -1

        for v in range(self.V):
            if dist[v] < min_distance and not sptSet[v]:
                min_distance = dist[v]
                min_index = v

        return min_index

    def dijkstra(self, src):
        dist = [1e7] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for _ in range(self.V):
            u = self.minDistance(dist, sptSet)
            sptSet[u] = True

            for v in range(self.V):
                if (self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]

        self.printSolution(dist)


with open("Z:\KLA Hackathon\Validators\level0\level0.json", 'r') as file:
    data = json.load(file)

n_neighbourhoods = data["n_neighbourhoods"]
neighbourhoods = data["neighbourhoods"]
total_distances = [neighbourhoods[i]["distances"] for i in neighbourhoods]

g = Graph(n_neighbourhoods)
g.graph = total_distances
g.dijkstra(0)

output_path = {"v0": {"path": ["r0"] + [f"n{i}" for i in range(n_neighbourhoods)] + ["r0"]}}
output_json = json.dumps(output_path, indent=2)
jsonFile = open("Z:\KLA Hackathon\Validators\level0\level0_output.json", "w")
jsonFile.write(output_json)
jsonFile.close()


