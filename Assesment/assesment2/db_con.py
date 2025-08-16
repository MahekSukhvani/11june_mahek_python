
import pymysql

#database connection 

def con():
    try:
        db = pymysql.connect(
            host="localhost",
            user="root",
            password="mahek5507",
            database="hotel"
        )
        return db
    except Exception as e:
        print("Connection Error:", e)
        return None


db=con()
cr=db.cursor()

#table creation 

table_creation = "create table check_in(id int primary key auto_increment , name text , address text , num text ,day text,room text , pay_method text)"

try:
      cr.execute(table_creation)
      print("Table Created SuccessFully")
except Exception as e:
      print(e)


#insert guest

def insert_guest(name, address, number, days, room, payment):
    db = con()
    if db is None:
        return False
    try:
        cursor = db.cursor()
        query = "INSERT INTO check_in (name, address, num, day, room, pay_method) VALUES (%s, %s, %s, %s, %s, %s)"  
        #%s is here placeholder that hold a place that here value exist as as variable 
        cursor.execute(query, (name, address, number, days, room, payment))
        db.commit()
        return True
    except Exception as e:
        print("Insert Error:", e)
        return False
    finally:
        db.close()

#show guest list

def fetch_all_guests():
    db = con()
    if db is None:
        return []
    cursor = db.cursor()
    cursor.execute("SELECT * FROM check_in")
    data = cursor.fetchall()
    db.close()
    return data

#serch guest 

def search_guest_id(guest_id):
    db = con()
    
    try:
        cr.execute("SELECT * FROM check_in WHERE id = %s", (guest_id,))
        return cr.fetchone()    
    
    except Exception as e:
        print("Search Error:", e)
    finally:
        db.close()




#delete guest (check out)

def delete_guest(guest_id):
    db = con()
 
    try:
        cr = db.cursor()  
        cr.execute("DELETE FROM check_in WHERE id = %s", (guest_id,))
        db.commit()
        return True
    except Exception as e:
        print("Delete Error:", e)
        return False
    finally:
        db.close()