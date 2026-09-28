import mysql.connector

class BookListCreateRetrieveUpdateDelete:
    def __init__(self):
        self.connection=mysql.connector.connect(user="root",password="tiger",host="localhost",database="library_db")
        self.cursor=self.connection.cursor()
        print("successfully connected")
    def list(self):
        query = "select * from book"
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        if records:
            # for row in records:
            #     print(row)
            return records
        else:
            print("no records")
    def create(self,title,author,price,pages,language):
        query="insert into book(title,author,price,pages,language) values(%s,%s,%s,%s,%s)"
        data=(title,author,price,pages,language)
        self.cursor.execute(query,data)
        self.connection.commit()
        print("Data inserted successfully")

    def retrieve(self,id):
        query = "select * from book where id=%s"
        data =(id,)
        self.cursor.execute(query,data)
        record = self.cursor.fetchone()
        if record:
            print(record)
        else:
            print("no records")
    def update(self,id,title,author,price,pages,language):
        query="update book set title=%s,author=%s,price=%s,pages=%s,language=%s where id=%s"
        data=(title,author,price,pages,language,id)
        self.cursor.execute(query,data)
        self.connection.commit()
        if self.cursor.rowcount>0:
            print("Data updated")
        else:
            print("no record found")
    def delete(self,id):
        query="delete from book where id=%s"
        data=(id,)
        self.cursor.execute(query,data)
        self.connection.commit()
        if self.cursor.rowcount>0: # if no updation rowcount return 0
            print("Data is deleted")
        else:
            print("No record found")

book_instance=BookListCreateRetrieveUpdateDelete()