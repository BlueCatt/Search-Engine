import cawler
from cawler import Crawler
cw = Crawler()
url = 'https://www.nytimes.com/?mcubz=0'
cw.BFS(url,'NewYork Times Home',0)