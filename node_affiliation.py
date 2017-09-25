import argparse, os

parser = argparse.ArgumentParser(description='Reads the clustering result and returns an afiliation list of the nodes')

parser.add_argument('input_hog', type=str, help='the directory where the HOG clusters are')
parser.add_argument('input_ghd', type=str, help='the directory where the GHD clusters are')
parser.add_argument('output_folder', type=str, help='the directory where the results must be stored')

args = parser.parse_args()

nodes = {}

hog_files = []
ghd_files = []

for p,d,f in os.walk(args.input_hog):
	hog_files.extend([x for x in f if x.endswith('lgl')])
	break
for p,d,f in os.walk(args.input_ghd):
	ghd_files.extend([x for x in f if x.endswith('lgl')])
	break
	
print("parsing HOG")	
for hog in hog_files:
	cluster = hog.split('.')[0]+"H"
	for line in open(os.path.join(args.input_hog,hog), 'r'):
		if line.startswith('#'):
			node = line.split()[-1].strip()
		else:
			node = line.strip()
		if node not in nodes:
			nodes[node] = [cluster]
		elif cluster not in nodes[node]:
			nodes[node].append(cluster)

print("parsing GHD")			
for ghd in ghd_files:
	cluster = ghd.split('.')[0]+"G"
	for line in open(os.path.join(args.input_ghd,ghd), 'r'):
		if line.startswith('#'):
			node = line.split()[-1].strip()
		else:
			node = line.strip()
		if node not in nodes:
			nodes[node] = [cluster]
		elif cluster not in nodes[node]:
			nodes[node].append(cluster)

out_file = open(os.path.join(args.output_folder, "node_affiliation"), 'w')
for node in nodes:
	out_file.write("%s;%s\n" %(node, ';'.join(nodes[node])))
out_file.close()