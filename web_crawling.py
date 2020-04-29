from urllib.request import urlopen
from bs4 import BeautifulSoup
from flask import render_template
import pandas as pd

html = urlopen("https://en.wikipedia.org/wiki/List_of_oil_refineries#Algeria")  

bsObject = BeautifulSoup(html, "html.parser") 

ulli_code=bsObject.select('div.mw-parser-output>ul') #ul전체 개수

print(ulli_code[0])

# for a in range(0,len(ulli_code)-1):
#     ulli_code[0]