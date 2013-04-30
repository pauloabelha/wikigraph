from crawler import Crawler
from graph_utils import GraphUtil
import sys
from operator import itemgetter

CRAWLED = True


if __name__ == "__main__":	
	if not CRAWLED:
		c = Crawler('simplewiki-latest-pages-articles.xml', sys.stderr)
		c.crawl()
	gu = GraphUtil()
	'''
	Whole graph might be backwards??
	'''
	#gu.write_adj_list('graph.dat')

	gu.load_graph_adj('graph_official.dat')
#	path = gu.shortest_path('Interpol','Shameless')
#	print path
#	gu.path_subgraph_gexf(path, 'path.gexf')
	gu.subgraph_sorted_nodes(25, 'top.gexf')

	#print gu.shortest_path("Cacica","Maizy")


    




