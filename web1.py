from urllib.request import urlopen
from bs4 import BeautifulSoup
from flask import render_template
import pandas as pd


html = urlopen("https://en.wikipedia.org/wiki/List_of_oil_refineries#Algeria")  

bsObject = BeautifulSoup(html, "html.parser") 


continent = []
continent=bsObject.select("h2>span.mw-headline")

country_code = []
country_code=bsObject.select("h3>span.mw-headline")


ulli_code=[]
ulli_num=[]
ulli_code=bsObject.select('div.mw-parser-output>ul') #ul전체 개수
li_code=bsObject.select('div.mw-parser-output>ul>li')
# for a in range(0,len(ulli)-1):
#     ulli_num.append(ulli[a].split('</ul>,'))

# print(ulli_code[0])
# for a in range(0,len(ulli_code)-1):
#     if(ulli_code[a])

ulli_total=[]
company_temp=[]
company=[]
num=[]
data=[]
for c in range(0,len(li_code)-1):
    ulli_total.append(li_code[c].get_text())    
# print(ulli_total)
for a in  range(0,len(ulli_total)-1):
    company_temp.append(ulli_total[a].split('), '))
    company.append(company_temp[a][0]+')')
    num.append(company_temp[a][0])
    data.append([company,num])
print(data)

df=pd.DateFrame(data,columns=["company","양"])
df.to_csv('crawling.csv',encoding="utf-8")



# continent =[]
# country=[]

# print(headline_array)
# num_headline=0
# while(1):
#     if headline_array[num_headline].get_text()=='Africa':
#         num_country=0
#         num_country=num_headline+1
#         while(1):
#             if headline_array[num_country].get_text()=='Algeria':
#                 continent.append(headline_array[num_headline].get_text())
#                 country.append(headline_array[num_country].get_text())
                
                
#         continent.append(headline_array[num_headline].get_text())
#     elif len(headline_array)>10:
#         break;      
# print(continent)



