Wikigraph
=========

Basic Crawling and Data Visualization of Simple Wikipedia. Could eventually be scaled to Wikipedia, although crawling/link extraction should be done using Hadoop or similar distributed methods. 

##Dependencies
- [NetworkX Graph Library]("www.networkx.lanl.gov")
- SciPy (Depends on NumPy)
- [Redis]("www.redis.io")
- redis (Python lib)
- lxml (Python lib)
- elementtree (Python lib)
- Django (Python lib)

```shell
apt-get install python-scipy
apt-get install python-numpy python-scipy
apt-get install redis-server
pip install redis
apt-get install libxml2-dev
apt-get install libxslt1-dev
pip install elementtree
pip install django
```

###Visualization
Visualization is done using a combination of [Django]("www.djangoproject.com") and [sigma.js]("www.sigmajs.org"). After crawling, one should output the graph in GEXF format using functions in the GraphUtils.py class. Django will load the graph at each request (need to change) into memory as a NetworkX object. Depending on the page, it will then output it another subgraph in GEXF form. This subgraph GEXF will be loaded by sigma.js and displayed. Django development server must be running to serve the request.
```shell
python manage.py runserver
```



