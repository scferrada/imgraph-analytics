import igraph as ig
import argparse, os

parser = argparse.ArgumentParser(description='Reads IMGpedia TSV files and prodices igraph lgl')

parser.add_argument('input_folder', type=str, help='the directory where the graph files are')
parser.add_argument('output_folder', type=str, help='the directory where the results must be stored')
parser.add_argument('--ext', dest='extension', type=str, default='', help='the extension of the CSV files, none by default')

args = parser.parse_args()

files = []
for p, d, f in os.walk(args.input_folder):
	files.extend([os.path.join(p,x) for x in f if x.endswith(args.extension)])
	break
print("Loading %d TSVs" % len(files))
edges = []	
for filename in files:
	for line in open(filename, 'r').readlines():
		if "\t2\t" in line:
			parts = line.split("\t")
			edges.append((int(parts[0]), int(parts[1])))
print("Making Graph")
graph = ig.Graph(edges, directed=True)
print("Saving graph")
graph.write_lgl(os.path.join(args.output_folder,"hog.lgl"))