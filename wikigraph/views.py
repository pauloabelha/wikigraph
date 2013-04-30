# Create your views here.
from django.shortcuts import render_to_response
from wikiproj.graph_utils import *
from os import path

def home(request):
    gu = GraphUtil()
    nodes = gu.top_nodes(400)
    gexf_dir = path.join(path.dirname(__file__), 'static/path.gexf')
    gu.create_gexf(gu.path_subgraph(nodes),gexf_dir)
    return render_to_response('graph/home_graph.html',{'path':nodes})

def home_adv(request, n):
    gu = GraphUtil()
    nodes = gu.top_nodes(int(n))
    gexf_dir = path.join(path.dirname(__file__), 'static/path.gexf')
    gu.create_gexf(gu.path_subgraph(nodes),gexf_dir)
    return render_to_response('graph/home_graph.html',{'path':nodes})    

def node_detail(request, node="United States"):
    gu = GraphUtil()
    context = {}
    context['in_edges'] = gu.neighbor_subgraph(node, True).nodes()
    context['in_edges_num'] = len(context['in_edges'])
    context['out_edges'] = gu.neighbor_subgraph(node, False).nodes()
    context['out_edges_num'] = len(context['out_edges'])
    context['node'] = node
    gexf_dir = path.join(path.dirname(__file__), 'static/path.gexf')
    gu.create_gexf(gu.path_subgraph(context['in_edges']),gexf_dir)
    return render_to_response('graph/detail.html',context)


def shortest_path(request, node1, node2):
    gu = GraphUtil()
    gexf_dir = path.join(path.dirname(__file__), 'static/path.gexf')
    p = gu.shortest_path(node1,node2)
    gu.create_gexf(gu.path_subgraph(p),gexf_dir)
    return render_to_response('graph/shortest_path.html',{'path':p,'node1':node1,'node2':node2})

def stats(request):
    gu = GraphUtil()
    stats = gu.graph_stats(25)
    context = {}
    context['histogram'] = stats['Histogram']
    context['top_degree'] = stats['Top']
    context['top_pagerank'] = stats['Pagerank']
    context['art_points'] = stats['Articulation Points']
    return render_to_response('graph/stats.html',context)
