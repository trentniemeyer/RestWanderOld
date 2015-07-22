import Pyro4

from django.http import Http404, HttpResponse

def index(request, url):
    server = Pyro4.Proxy(Pyro4.locateNS().lookup('gensim.testserver'))
    results = server.find_similar(url, max_results=5)
    return HttpResponse(results)