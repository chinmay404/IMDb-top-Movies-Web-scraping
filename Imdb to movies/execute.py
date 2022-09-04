import databse as DB

mydb = DB.connect_db()
mc = mydb.cursor()

def insert(query):
    mc.execute(query)
    
def double_insert(q1 , q2):
    mc.execute(q1,q2)
    