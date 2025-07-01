import sqlite3

# Connect to the database 
def openConnection():
    try:
        conn = sqlite3.connect("restaurants.db")
        curs = conn.cursor()

    except sqlite3.Error as sqle:
        print(f"sqlite3.Error: {sqle}")
        return

    return conn


# Initialise the database with the Administrator table and Restaurants table
def initialiseDatabase():

    conn = openConnection()

    if conn is None:
        print('fail')
        return
    
    try:
        curs = conn.cursor()
        curs.execute('''CREATE TABLE IF NOT EXISTS Administrator (
                        firstName TEXT,
                        lastName TEXT,
                        userName TEXT PRIMARY KEY,
                        password TEXT)
                        ''')
        
        curs.execute('''INSERT INTO Administrator (firstName, lastName, userName, password)
                        VALUES ('Administrator', '', 'admin', 'admin')
                        ''')

        # Reset the reviews by deleting the Restaurants table
        # curs.execute('''DROP TABLE Restaurants''')

        curs.execute('''CREATE TABLE IF NOT EXISTS Restaurants (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        suburb TEXT NOT NULL, 
                        city TEXT NOT NULL,
                        cuisine TEXT NOT NULL,
                        rating DECIMAL,
                        comment TEXT NOT NULL)
                        ''')

        conn.commit()

    except sqlite3.Error as sqle:
        print(f"sqlite3.Error: {sqle}")
        return 
    
    finally:
        conn.close()


# Initialise the database 
initialiseDatabase()
