from urllib.request import urlopen
from bs4 import BeautifulSoup
from flask import render_template
import pandas as pd


html = urlopen("https://en.wikipedia.org/wiki/List_of_oil_refineries#Algeria")  

bsObject = BeautifulSoup(html, "html.parser") 


continent = []
continent=bsObject.select("h2>span.mw-headline")

ulli_code=[]
ulli_num=[]
ulli_code=bsObject.select('div.mw-parser-output>ul') #ul전체 개수
li_code=bsObject.select('div.mw-parser-output>ul>li')

# li_tag_num=[]
# for i in range(0,len(ulli_code)-1):
#     temp_li_tag_num=ulli_code[i] 
#     temp_li_tag_num=str(temp_li_tag_num)  
#     li_tag_num.append(temp_li_tag_num.count('<li>'))
# print(li_tag_num)  


# country_code = []
# country_code=bsObject.select("h3>span.mw-headline")
# country=[]
# print(len(li_tag_num))
# print(len(country_code))
# for coun in range(0,len(country_code)-1):
#     # if c>10:
#     #     break
#     for i in range(li_tag_num[coun]):
#         country.append(country_code[coun].get_text())  
# print(len(country))

# print(li_tag_num[50])
# print(country_code[50])
# print(country_code)
# print(country) 

  


ulli_total=[]
company_temp=[]
company=[]
num=[]
data=[]
for c in range(0,len(li_code)-1):
    ulli_total.append(li_code[c].get_text())    
print(ulli_total)  


for a in  range(0,len(ulli_total)-1):
    if '), ' in ulli_total[a]: 
        print('냐')
        ulli_total[a]=ulli_total[a].split('), ')
        company_temp.append(ulli_total[a])
        company.append(company_temp[a][0]+')')
        if len(company_temp[a])>=2:
            if('bbl/d' in company_temp[a][1]):
                temp_com=company_temp[a][1].split('bbl/d')
                print(temp_com[0])
                num.append(temp_com[0].strip())
            else:
                num.append("0")    
        else:
            num. append('값 없음')  
    elif ', ' in ulli_total[a]:
        print(',,,,,,,,,@@')
        company_temp.append(ulli_total[a].split(', '))
        company.append(company_temp[a][0])
        if len(company_temp[a])>=2:
            if('bbl/d' in company_temp[a][1]):
                temp_com=company_temp[a][1].split('bbl/d')
                print(temp_com[0])
                num.append(temp_com[0].strip())
            elif('bbl/day' in company_temp[a][1]):
                temp_com=company_temp[a][1].split('bbl/day')
                print(temp_com[0])
                num.append(temp_com[0].strip())    

            else:
                num.append("0")    
        else:
            num. append('값 없음')           
    elif ') ' in ulli_total[a]:
        print('@@')
        company_temp.append(ulli_total[a].split(') '))
        company.append(company_temp[a][0]+')')
        if len(company_temp[a])>=2:
            if('bbl/d' in company_temp[a][1]):
                temp_com=company_temp[a][1].split('bbl/d')
                print(temp_com[0])
                num.append(temp_com[0].strip())

            else:
                num.append("0")    
        else:
            num. append('값 없음')
           
    else:
         company_temp.append(ulli_total[a])
         company.append(ulli_total[a])
         num. append('값 따로 넣어주기')  

    data.append([company[a],num[a]])
print(data)

df=pd.DataFrame(data,columns=["회사","bbl/day"])
df.to_csv('crawling4.csv',index=False,encoding="utf-8")
