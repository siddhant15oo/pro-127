from bs4 import BeautifulSoup as bs    
import requests
import pandas as pd 
#import
#give websit link
#get data from request 
#html.parsaar
#find table

startURL='https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
page=requests.get(startURL)
print(page)

soup=bs(page.text,'html.parser')
stars_table=soup.find('table')

temlist=[]
table_rows=stars_table.find_all('tr')
for i in table_rows:
    td=i.find_all('td')
    row=[j.text.rstrip()for j in td]
    temlist.append(row)


star_name=[]
star_mass=[]
star_distance=[]
star_radius=[]
star_lo=[]

for i in range(0,len(temlist)):
    star_name.append(temlist[i][1])
    star_distance.append(temlist[i][3])
    star_lo.append(temlist[i][5])
    star_mass.append(temlist[i][7])
    star_lo.append(temlist[i][9])

df=pd.DataFrame(list(star_name,star_mass,star_radius,star_distance,star_lo),columns=['Name','Mass','Radius','Distance','Luminosity'])
df.to_csv('stars.csv')