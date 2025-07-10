# RestauRate

RestauRate is a web-based application that enables users to generate reviews for restaurants based on the restaurant's name, suburb, city, cuisine, rating, and any comments. Users are also able to view the details of each previous review and pinpoint the location of the restaurant on an interactive map. Administrators can access a dashboard through login, and be able to view analytics and delete user-generated reviews. 

This personal project was brought to life from my love of trying new places and foods, as well as my passion for developing new technical skills and creating a useful product that people would use. I hope you like it!
https://restaurate-614c59114b94.herokuapp.com/

## Functionalities
Users can:
- Generate reviews
- View previous reviews
- View the details of previous reviews 
- Search for a specific review
- Sort the reviews based on the rating 

Admin users can:
- Log in using a username and password 
- View the total number of reviews
- Calculate the average rating of a restaurant 
- Delete reviews

## Tech stack
**Backend:** Python, Flask
- **Python:** Used to create the main program which defines routes that map URLs to Python functions, and the interface to connect with the database.
- **Flask:** A Python web framework that enables the web application to be deployed to a development server for testing. Uses Jinja2 templating engine for dynamic HTML.

**Frontend:** HTML, CSS, JavaScript
- **HTML:** Basic structure and template of the web pages.
- **CSS:** Style the components on the web pages. 
- **JavaScript:** Include functionalities for components that are present on the web pages. 

**Database:** SQLite 
- **SQLite:** A lightweight relational database that is embedded in the web application. It works directly on VS Code and I found it quite simple to use since the syntax is similar to PostgreSQL.

## Folders and Files
- **static**
  - `style.css` - A CSS file that is used to style the contents of the web application.
  - **Images** - Include the logo for the web application and icons for links.
    
- **templates**
  - `dashboard.html` - An HTML file that serves as the administrator dashboard for the web application.
  - `footer.html` - An HTML file that contains the footer to be added to the web pages.
  - `header.html` - An HTML file that contains the header to be added to the web pages.
  - `home.html` - An HTML file that serves as the home page for the web application. 
  - `login.html` - An HTML file that serves as the login page for the web application. 
  - `restaurant.html` - An HTML file that serves as the template to display the details of different reviews.
  - `review.html` - An HTML file that serves as the review page for the web application.
  - `view.html` - An HTML file that serves as the view page for the web application. 

- `database.py` - A Python file that creates the interface between the web application and the database for CRUD operations.
  - Use print statements in this file to debug the output of CRUD operations.
  
- `initialiseDB.py` - A Python file that initialises the database with the Administrator table and the Restaurants table
  - Default Administrator Username: **admin**
  - Default Administrator Password: **admin**
 
- `main.py` - A Python file that defines functions to redirect and render template HTML pages based on GET and POST methods. 

## How to run
**1.** Ensure that you have installed the required technologies, libraries, and frameworks.

**2.** Replace the `MAPS_AKI_KEY` placeholder with your own Google Maps API key.

**3.** Initialise the database by running the command `python initialiseDB.py` in the terminal.

**4.** Run the main program by running the command `python main.py` in the terminal.

## Learnings
Undertaking this project enabled me to learn the basics of new languages and web development, as well as best practices and templating. Since the web application consists of many different pages, I got to really understand the process of how the frontend interacts with the backend to retrieve data, and then parses that information back through to the frontend. I enjoyed working on the `main.py` file and seeing how to implement Flask to render templates and redirect the user to different web pages.

In regard to adding functionalities to the web pages, I found that distinguishing between which scenarios to retrieve data from the database, or modifying the data already present on the web page to be a particularly important takeaway. I was also able to solidify my understanding of the object-oriented interface to communicate with the database to execute CRUD operations. Overall, this project presented opportunities to learn valuable lessons, which I will keep in mind for future projects.

## Future considerations
While the application works well as an MVP and as a proof of concept, there are a few improvements that I am considering implementing in the future. Notably, the administrator dashboard can benefit from including more statistics and analytics. The inclusion of visual aids such as diagrams and graphs can also help administrators make informed decisions. 

Currently, to view the average rating of a restaurant, the administrator must enter the details of the restaurant exactly how it is stored in the database. However, standardising the input to remove manual errors and improve recognition is important to improve the overall user experience.

I would also love to hear your thoughts, so do not hesitate to give your feedback!
