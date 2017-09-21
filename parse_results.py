import argparse, shelve, os

parser = argparse.ArgumentParser(description='Translates clustering results to image links')

parser.add_argument('input_shelve', type=str, help='The shelve file of the dictionary')
parser.add_argument('input_folder', type=str, help='The directory where the results must be readed')
parser.add_argument('--reverse', dest='rev', type=bool, default=False, help='Provide if the given graph is name -> oid. Default False.')

args = parser.parse_args()

graph = shelve.open(args.input_shelve)
wc_url = 'http://commons.wikimedia.org/wiki/File:%s\n'

if args.rev:
	graph_rev = shelve.open('graph_rev.db')
	for key in graph:
		graph_rev[str(graph[str(key)])] = key
	graph_rev.close()
	graph = graph_rev	

cluster_files = []
for p,d,f in os.walk(args.input_folder):
	cluster_files.extend(f)
	break 
	
for file in cluster_files:
	with open(os.path.join(args.input_folder, file[:-4]+'.txt'), 'w') as cluster:
		for line in open(os.path.join(args.input_folder,file), 'r'):
			if line.startswith('#'):
				img = graph[line[1:].strip()]
			else:
				img = graph[line.strip()]
			cluster.write(wc_url % line)