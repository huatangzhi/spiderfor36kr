#import some module used in spider
import urllib
import re
from operator import itemgetter
from bs4 import BeautifulSoup




filename = '36kr.html'

def getHtml(url):
    '''get the html and save as 36kr.html'''
    page = urllib.urlopen(url)
    html = page.read()
    if  html:
        file36kr = open(filename,'w')
        file36kr.write(html)
        file36kr.close()


def parseHtml(filename):
    '''parse html return the sorted list contains product, vote'''
    file36kr = open(filename,'r')
    soup =BeautifulSoup(file36kr, "html.parser")

    #products , list, contains all product
    products = list()
    for p in soup.find_all("a", class_="post-url"):
        products.append(p.string)

    #votes , list, contains all votes
    votes = list()
    for v in soup.find_all("span", class_="vote-count"):
        votes.append(int(v.string))

    #product2vote, dict, contains (product:vote)
    #product2votesorted, list, sort the product by vote
    product2vote = dict()
    if len(products) == len(votes):
        for i in range(len(products)):
            product2vote.setdefault(products[i],votes[i])
        product2votesorted = sorted(product2vote.items(), key=itemgetter(1), reverse=False)
        return  product2votesorted
    else:
        print 'Error'
    file36kr.close()

if __name__ == '__main__':
    url =  'http://next.36kr.com/posts'
    getHtml(url)
    sortedlist = parseHtml(filename)
    for i in  sortedlist:
        print i[0], i[1]