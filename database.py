import sqlite3

# Connect to the database 
def openConnection():
    try:
        conn = sqlite3.connect("restaurants.db")
        cursor = conn.cursor()

    except sqlite3.Error as sqle:
        print(f"sqlite3.Error: {sqle}")

    return conn


# Check that the provided username and password exists in the database 
def checkLogin(username, password):
    try:
        conn = openConnection()
        curs = conn.cursor()

        curs.execute("SELECT * FROM Administrator WHERE userName = ? AND password = ?", (username, password))

        result = curs.fetchone()    

        if result is None:
            return 

    except sqlite3.Error as sqle:
        print(f"sqlite3.Error: {sqle}")
    
    conn.close()
    return [result[0], result[1]]


# Fetch all reviews within the database 
def findReviews():
    try:
        conn = openConnection()
        curs = conn.cursor()

        curs.execute('''SELECT name, suburb, city, cuisine, rating, comment FROM Restaurants''')
    
        result = curs.fetchall()

        if result is None:
            return
        
        res = []

        col = ['name', 'suburb', 'city', 'cuisine', 'rating', 'comment']

        for row in result:
            res.append(dict(zip(col, row)))

        conn.close()
        return res
        

    except sqlite3.Error as sqle:
        print(f"sqlite3.Error: {sqle}")

    return result


# Fetch all reviews within the database for admin view 
def findReviewsAdmin():
    try:
        conn = openConnection()
        curs = conn.cursor()

        curs.execute('''SELECT * FROM Restaurants''')
    
        result = curs.fetchall()

        if result is None:
            return
        
        res = []

        col = ['id', 'name', 'suburb', 'city', 'cuisine', 'rating', 'comment']

        for row in result:
            res.append(dict(zip(col, row)))

        conn.close()
        return res
        
    except sqlite3.Error as sqle:
        print(f"sqlite3.Error: {sqle}")

    return result


# Delete the review that matches the id provided 
def deleteReview(id):
    try:
        conn = openConnection()
        curs = conn.cursor()

        curs.execute('''DELETE FROM Restaurants WHERE id = ?''', (id,))
        
        curs.close()
        conn.commit()

        return id
    
    except sqlite3.Error as sqle:
        print(f"sqlite3.Error: {sqle}")

    conn.close()
    return id


# Add a review into the database 
def addReview(name, suburb, city, cuisine, rating, comment):
    try:
        conn = openConnection()
        curs = conn.cursor()

        curs.execute('''INSERT INTO Restaurants (name, suburb, city, cuisine, rating, comment)
                        VALUES (?, ?, ?, ?, ?, ?)''', (name, suburb, city, cuisine, rating, comment))
    
        curs.close()
        conn.commit()
    
        return True 
    
    except sqlite3.Error as sqle:
        print(f"sqlite3.Error: {sqle}")
    
    conn.close()
    return False 


# Fetch the details of the restaurant provided
def getRestaurant(name, suburb, city):
    try:
        conn = openConnection()
        curs = conn.cursor()

        curs.execute('''SELECT * FROM Restaurants 
                        WHERE name = ? AND suburb = ? AND city = ?''', (name, suburb, city))
        
        result = curs.fetchone()
        
        if result is None:
            return
        
        return result
    
    except sqlite3.Error as sqle:
        print(f"sqlite3.Error: {sqle}")


# Fetch the total number of reviews in the database 
def getNumbers():
    try:
        conn = openConnection()
        curs = conn.cursor()

        curs.execute('SELECT * FROM Restaurants')

        result = curs.fetchall()

        if result is None:
            return 0
        
        conn.close()
        return len(result)

    except sqlite3.Error as sqle:
        print(f"sqlite3.Error: {sqle}")


# Fetch the average rating of the restaurant provided 
def getAverage(name, suburb, city):
    try:
        conn = openConnection()
        curs = conn.cursor()

        curs.execute('''SELECT AVG(rating) FROM Restaurants 
                        WHERE name = ? AND suburb = ? AND city = ?''', (name, suburb, city))

        result = curs.fetchone()

        if result is None:
            return 0
        
        conn.close()
        return result

    except sqlite3.Error as sqle:
        print(f"sqlite3.Error: {sqle}")
