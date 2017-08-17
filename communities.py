import igraph as ig
import argparse, os

parser.add_argument('input_graph', type=str, help='the lgl file of the graph')

args = parser.parse_args()

print("Reading graph")
graph = ig.Graph.Read_Lgl(args.input_graph)
print("Computing connectivity")
clusters = graph.community_leading_eigenvector()
print("writting result")
counter = 1
for sg in clusters.subgraphs():
	print(sg.summary())
	sg.write_lgl("%d.lgl"%counter)
	counter += 1