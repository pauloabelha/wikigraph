from database import Redis
import networkx as nx
import matplotlib as mpl
from operator import itemgetter
import sys
import random
from os import path

class GraphUtil:
	def __init__(self):
		self.database = Redis()
		self.G = None
		graph_dir = path.join(path.dirname(__file__), 'graph_gexf.gexf')
		self.load_graph_gexf(graph_dir)
	

	def build_redis_to_adj(self, filename):
		self.G = nx.DiGraph()
		articles = self.database.get_slist_members("articles")
		for article in articles:
			links = self.database.get_slist_members(article)
			for link in links:
				if link in articles:
					self.G.add_edge(link,article)
		nx.write_gml(self.G,filename)
	
	def build_adj_to_gml(self, filename, path):
		self.G = nx.read_adjlist(filename,delimiter=",",create_using=nx.DiGraph(data=True))
		nx.write_gml(self.G,path)
	
	def load_graph_gml(self, filename):
		self.G = nx.read_gml(filename, relabel=True)
		
	def write_graph_gexf(self, filename):
		nx.write_gexf(self.G, filename)

	def load_graph_gexf(self, filename):
		self.G = nx.read_gexf(filename)
		
	def load_graph_adj(self, filename):
		self.G = nx.read_adjlist(filename, delimiter=",",create_using=nx.DiGraph()).reverse(copy=False)
		 
	def degree_histogram(self):
		return nx.degree_histogram(self.G)
	
	def shortest_path(self, start, end):
		return nx.shortest_path(self.G,start,end)

	def path_subgraph(self, path):
		return self.G.subgraph(path)
		
	'''
	DJANGO helper functions
	'''
	def top_nodes(self, n):
		nodes = sorted(self.G.reverse(copy=True).degree_iter(),key=itemgetter(1),reverse=True)[1:n]
		tops = [i[0] for i in nodes]
		return tops

	def neighbor_subgraph(self, node, in_edges=True):
		if in_edges:
			neighbors = self.G.reverse(copy=True).neighbors(node)
		else:
			neighbors = self.G.neighbors(node)
		neighbors.append(node)
		if "" in neighbors:
			neighbors.remove("")
		g = self.G.subgraph(neighbors)
		return g
		
		

	def create_gexf(self, nodes,  filename):
		for n in  nodes.nodes(data=True):
			n[1]["viz"] = {"color":{'r':random.randint(0,256),'g':random.randint(0,256),'b':random.randint(0,256),'a':0}}
		nx.write_gexf(nodes, filename)

	def graph_stats(self, n):
		stats = {}
		stats['Top'] = self.top_nodes(n+1)
		stats['Pagerank'] = nx.pagerank_scipy(self.G)
		stats['Pagerank'] = sorted(stats['Pagerank'].iteritems(), key=itemgetter(1),reverse=True)[0:n+1]
		stats['Articulation Points'] = list(nx.articulation_points(self.G.to_undirected()))
		stats['Histogram'] = self.degree_histogram()[1:26]
		return stats
		
