import igraph as ig
import argparse, os

parser = argparse.ArgumentParser(description='Reads IMGpedia TSV files and prodices igraph lgl')

parser.add_argument('input_graph', type=str, help='the lgl file of the graph')
#parser.add_argument('output_folder', type=str, help='the directory where the results must be stored')
#parser.add_argument('--ext', dest='extension', type=str, default='graph', help='the extension of the CSV files, .graph by default')

args = parser.parse_args()

print("Reading graph")
graph = ig.Graph.Read_Lgl(args.input_graph)
print("Computing connectivity")
components = graph.components()
print("Graph: " + graph.summary())
print("%d connected components" % len(components.subgraphs()))
print("Giant component: " + components.giant().summary())