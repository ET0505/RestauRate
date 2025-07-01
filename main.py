import requests 
from flask import *
import os
import database 

app = Flask(__name__)
app.secret_key = 'YOUR_SECRET_KEY'
MAPS_API_KEY = "YOUR_GOOGLE_MAPS_API_KEY"


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login.html', methods = ['GET', 'POST'])
def login():
    # If submitting the username and data, redirect to dashboard if successful, redirect back to login if unsuccessful
    if (request.method == "POST"):
        login_return_data = database.checkLogin(request.form['username'], request.form['password'])

        if login_return_data is None:
            flash("Incorrect information. Please try again.")
            return redirect(url_for('login'))
        
        welcome_str = f"Welcome back {login_return_data[0]} {login_return_data[1]}"
        flash(welcome_str)

        return redirect(url_for('adminView'))
    
    # If just viewing the page, render the template 
    elif (request.method == "GET"):
        return render_template('login.html')


@app.route('/logout', methods = ['GET', 'POST'])
def logout():
    flash('You have logged out.')
    return redirect(url_for('login'))


@app.route('/view.html', methods = ['GET', 'POST'])
def view():
    if (request.method == "POST"):
        return redirect(url_for('home'))

    # If just viewing the page, retrieve all reviews from database 
    elif (request.method == "GET"):
        reviews_return_data = database.findReviews()

        if len(reviews_return_data) == 0:
            flash('No reviews present')

        return render_template('view.html', reviews_list = reviews_return_data)


@app.route('/dashboard.html', methods = ['GET', 'POST'])
def adminView():
    if (request.method == "POST"):
        # If submitting the delete form, delete the matching reivew from the database
        if "delete-review" in request.form:
            delete_id_data = database.deleteReview(request.form['delete-id'])

            if delete_id_data == '' or int(delete_id_data) > get_review_amount() or int(delete_id_data) <= 0:
                flash("Invalid id. Please try again.")
            else:
                flash('Deletion successful')

            return redirect(url_for('adminView'))

        # If submitting the find average form, calculate the average rating of the provided restaurant
        elif "find-average" in request.form:
            restaurant_name = request.form['restaurant-name']
            restaurant_suburb = request.form['restaurant-suburb']
            restaurant_city = request.form['restaurant-city']

            average_rating_data = database.getAverage(restaurant_name, restaurant_suburb, restaurant_city)

            if average_rating_data is None:
                flash('No reviews found. Please try again.')
            else:
                average_rating = average_rating_data[0]
                flash(f'Average rating of {restaurant_name} is {average_rating:.2f}/10')
            
            return redirect(url_for('adminView'))
        
    # If just viewing the page, retrieve all reviews from the database 
    elif (request.method == "GET"):
        admin_reviews_return_data = database.findReviewsAdmin()

        if len(admin_reviews_return_data) == 0:
            flash('No reviews present')

        return render_template('dashboard.html', admin_reviews_list = admin_reviews_return_data, total_number = get_review_amount())


@app.route('/review.html', methods = ['GET', 'POST'])
def review():
    # If submitting a review, add the review into the database 
    if (request.method == 'POST'):
        review_return_data = database.addReview(request.form['name'], request.form['suburb'], request.form['city'], 
                                                request.form['cuisine'], request.form['rating'], request.form['comment'])

        if review_return_data is False:
            flash('Error')
            return redirect(url_for('review'))
    
        flash("Review received")
        return redirect(url_for('view'))

    # If just viewing the page, render the template 
    elif (request.method == "GET"):
        return render_template('review.html')


# Render the template to display restaurant details 
@app.route('/restaurant/<name>/<suburb>/<city>.html')
def display(name, suburb, city):    
    restaurant_details = database.getRestaurant(name, suburb, city)

    return render_template('restaurant.html', restaurant = restaurant_details)


# Parse the MAPS_API_KEY to the frontend 
@app.route('/config', methods = ['GET'])
def get_config():
    return jsonify({"api_key": MAPS_API_KEY})


# Retrieve the total number of entries in the Restaurants table
@app.route('/numbers', methods = ['GET'])
def get_review_amount():
    return database.getNumbers()


if __name__ == "__main__":
    app.run(debug = True)
