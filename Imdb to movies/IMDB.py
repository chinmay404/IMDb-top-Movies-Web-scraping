from tkinter import INSERT
import requests
from bs4 import BeautifulSoup
import databse as DB
import execute as ex

# web_scrapping_imdb
try:
    url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
    source = requests.get(url)
    source.raise_for_status()  #For Url Error
except Exception as e:
    print (e)
soup = BeautifulSoup(source.text,'html.parser')
movies = soup.find("tbody",class_= 'lister-list').find_all('tr')    
    
#DataBase
mydb = DB.connect_db()   #input("DataBase : ")
ex.insert("USE web_scrapping_imdb")
# ex.insert("CREATE TABLE top (ind int,name VARCHAR(255), Year int , Rating int)")


for mov in movies:
    name = mov.find('td', class_='titleColumn').a.text
    rank = mov.find('td',class_='titleColumn').get_text(strip=True).split('.')[0]
    year = mov.find('td', class_='titleColumn').span.text.strip('()')
    rating = mov.find('td', class_='ratingColumn imdbRating').get_text(strip=True)
    data = (rank,name,rating,year)
    stmt = ("INSERT INTO top(ind,name,Year,Rating)""VALUES(%s,%s,%s,%s)")
    ex.double_insert(stmt,data)

print(len(movies)+"Insert Sucessfull !!")
mydb.commit()


    

   
    



