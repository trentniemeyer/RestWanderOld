from django.http import HttpResponse
from simserver import SessionServer
from gensim import utils
import Pyro4

from django.http import Http404, HttpResponse
import datetime

def index(request, url):
    server = Pyro4.Proxy(Pyro4.locateNS().lookup('gensim.testserver'))
    results = server.find_similar(url, max_results=5)
    return HttpResponse(results)