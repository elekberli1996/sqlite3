import sqlite3

connection=sqlite3.connect("cars.db")
cursor=connection.cursor()


#table yaratmak funksyasi
def create_Table():
    cursor.execute("CREATE TABLE IF NOT EXISTS CAR (model TEXT,marka TEXT, yil INT,fiyat INT)")
    connection.commit()

#insert funksyasi
def insert_Data(model,marka,yil,fiyat):
    cursor.execute("INSERT INTO CAR VALUES(?,?,?,?)",(model,marka,yil,fiyat))
    connection.commit()
# create_Table()

#Butun dalatlari goster
def all_data():
    cursor.execute("SELECT * FROM CAR")
    data=cursor.fetchall()
    for i in data:
        print(i)

#qiymete gore filter
def filter_price():
    cursor.execute("SELECT MODEL FROM CAR WHERE fiyat>100000")
    data=cursor.fetchall()
    print(data)


#update 

def update(oldname,newname):
    cursor.execute("UPDATE CAR SET MODEL=? WHERE MODEL=?",(newname,oldname))
    connection.commit()

# update("BMV","BMW")


#Delete 
def delete_Date(model):
    cursor.execute("DELETE FROM CAR WHERE MODEL=?",(model,))
    connection.commit()

delete_Date("LADA")

# filter_price()
# all_data()

#ISTENLILEN SAYDA DATA ELAVE ET    
# while True:
#     islem=input("cikmak inin Q basin devam etmek icin enter girin")
#     if islem=="Q":
#         break
#     else:
#         model=input("Araba modeli")
#         marka=input("Araba markasi")
#         yil=int(input("hangi yil"))
#         fiyat=int(input("fiyati kac"))
#         insert_Data(model,marka,yil,fiyat)


connection.close()