import sqlite3

connection = sqlite3.connect("Shatanov_TD.db")
cursor = connection.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS Customers
               (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
               Name CHAR(50), 
               Surname CHAR(50), 
               Tel INTEGER NOT NULL, 
               Order_ID INTEGER NOT NULL,
               FOREIGN KEY (Order_ID) REFERENCES Orders(ID))''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Orders
               (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
               Order_title CHAR(120) NOT NULL, 
               Description TEXT,
               Delivery_ID INTEGER NOT NULL,
               Receipt_ID INTEGER NOT NULL,
               FOREIGN KEY (Delivery_ID) REFERENCES Deliveries(ID)
               FOREIGN KEY (Receipt_ID) REFERENCES Receipts(ID))''')


cursor.execute('''CREATE TABLE IF NOT EXISTS Deliveries
               (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
               Title CHAR(120) NOT NULL, 
               Delivery_Date DATE NOT NULL)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Receipts
               (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
               Title CHAR(120) NOT NULL,
               Payment_Date DATE, 
               Price REAL NOT NULL)''')

cursor.execute("INSERT INTO Customers VALUES(0, 'Jack0', 'London', 88005553530, 0)")
cursor.execute("INSERT INTO Customers VALUES(1, 'Jack1', 'London', 88005553531, 1)")
cursor.execute("INSERT INTO Customers VALUES(2, 'Jack2', 'London', 88005553532, 2)")
cursor.execute("INSERT INTO Customers VALUES(3, 'Jack3', 'London', 88005553533, 3)")
cursor.execute("INSERT INTO Customers VALUES(4, 'Jack4', 'London', 88005553534, 4)")
cursor.execute("INSERT INTO Customers VALUES(5, 'Jack5', 'London', 88005553535, 5)")
cursor.execute("INSERT INTO Customers VALUES(6, 'Jack6', 'London', 88005553536, 6)")
cursor.execute("INSERT INTO Customers VALUES(7, 'Jack7', 'London', 88005553537, 7)")
cursor.execute("INSERT INTO Customers VALUES(8, 'Jack8', 'London', 88005553538, 8)")
cursor.execute("INSERT INTO Customers VALUES(9, 'Jack9', 'London', 88005553539, 9)")

cursor.execute("INSERT INTO Orders VALUES(0, 'Chair0', 'Ltetfjesgfgejhfgjesgzfjgsjfgjfgehj', 0, 0)")
cursor.execute("INSERT INTO Orders VALUES(1, 'Chair1', 'Ltetfjesgfgejhfgjesgzfjgsjfgjfgehj', 1, 1)")
cursor.execute("INSERT INTO Orders VALUES(2, 'Chair2', 'Ltetfjesgfgejhfgjesgzfjgsjfgjfgehj', 2, 2)")
cursor.execute("INSERT INTO Orders VALUES(3, 'Chair3', 'Ltetfjesgfgejhfgjesgzfjgsjfgjfgehj', 3, 3)")
cursor.execute("INSERT INTO Orders VALUES(4, 'Chair4', 'Ltetfjesgfgejhfgjesgzfjgsjfgjfgehj', 4, 4)")
cursor.execute("INSERT INTO Orders VALUES(5, 'Chair5', 'Ltetfjesgfgejhfgjesgzfjgsjfgjfgehj', 5, 5)")
cursor.execute("INSERT INTO Orders VALUES(6, 'Chair6', 'Ltetfjesgfgejhfgjesgzfjgsjfgjfgehj', 6, 6)")
cursor.execute("INSERT INTO Orders VALUES(7, 'Chair7', 'Ltetfjesgfgejhfgjesgzfjgsjfgjfgehj', 7, 7)")
cursor.execute("INSERT INTO Orders VALUES(8, 'Chair8', 'Ltetfjesgfgejhfgjesgzfjgsjfgjfgehj', 8, 8)")
cursor.execute("INSERT INTO Orders VALUES(9, 'Chair9', 'Ltetfjesgfgejhfgjesgzfjgsjfgjfgehj', 9, 9)")

cursor.execute("INSERT INTO Deliveries VALUES(0, 'Chair', '2022-02-25')")
cursor.execute("INSERT INTO Deliveries VALUES(1, 'Chair', '2022-02-25')")
cursor.execute("INSERT INTO Deliveries VALUES(2, 'Chair', '2022-02-25')")
cursor.execute("INSERT INTO Deliveries VALUES(3, 'Chair', '2022-02-25')")
cursor.execute("INSERT INTO Deliveries VALUES(4, 'Chair', '2022-02-25')")
cursor.execute("INSERT INTO Deliveries VALUES(5, 'Chair', '2022-02-25')")

cursor.execute("INSERT INTO Receipts VALUES(0, 'Chair', '2022-02-25', 564.25)")
cursor.execute("INSERT INTO Receipts VALUES(1, 'Chair', '2022-02-25', 564.25)")
cursor.execute("INSERT INTO Receipts VALUES(2, 'Chair', '2022-02-25', 564.25)")
cursor.execute("INSERT INTO Receipts VALUES(3, 'Chair', '2022-02-25', 564.25)")
cursor.execute("INSERT INTO Receipts VALUES(4, 'Chair', '2022-02-25', 564.25)")
cursor.execute("INSERT INTO Receipts VALUES(5, 'Chair', '2022-02-25', 564.25)")

cursor.execute("DELETE FROM Customers WHERE ID = 6")
cursor.execute("DELETE FROM Customers WHERE Order_ID > 8")
cursor.execute("DELETE FROM Deliveries")

cursor.execute("UPDATE Customers SET Tel = 88005553567 WHERE ID = 5")
cursor.execute("UPDATE Customers SET Tel = 88005553567, Surname = 'jACK' WHERE ID = 7")
cursor.execute("UPDATE Orders SET Order_title = 'Стул' WHERE Order_title = 'Chair1'")
cursor.execute("UPDATE Orders SET Order_title = 'Стул', Description = 'авыавыаыв' WHERE Order_title = 'Chair1'")

connection.commit()


connection.close()
