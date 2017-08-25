import igraph as ig
import argparse, os

parser = argparse.ArgumentParser(description='Finds communities within the IMGpedia Graph')

parser.add_argument('input_graph', type=str, help='the lgl file of the graph')
parser.add_argument('output_folder', type=str, help='the folder for the output')

args = parser.parse_args()

print("Reading graph")
graph = ig.Graph.Read_Lgl(args.input_graph, directed=True)
print("Computing clusters")
clusters = graph.community_leading_eigenvector()
print("writting result")
counter = 1
for sg in clusters.subgraphs():
	if sg.vcount() < 10: continue
	print(sg.summary())
	sg.write_lgl(os.path.join(args.output_folder, "%d.lgl"%counter))
	counter += 1