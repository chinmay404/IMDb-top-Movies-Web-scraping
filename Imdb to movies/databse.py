from logging import exception
import mysql.connector
def connect_db() :
    localhost = "localhost"  #input("LocalHost : ")
    user = "root"            #input("User : ")
    passwd = "chinmay1718"   #input("Password : ")
    dbname = "web_scrapping_imdb"     #db_name       input("DataBase : ")
    # try:
    mydb = mysql.connector.connect(
        host = localhost,
        user = user, 
        passwd =passwd,
        database = dbname)
    return mydb
    


