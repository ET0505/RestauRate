# RestauRate

RestauRate is a web-based application that enables users to generate reviews for restaurants. 

This personal project stems from my love of trying new foods and places.

## Functionalities
User can:
- Generate reviews
- View previous reviews
- Search for a specific review
- Sort the reviews based on rating 

Admin users can:
- Log in 
- View the total number of reviews
- Calculate the average rating of a restaurant 
- Delete reviews

## Tech stack
**Backend:** Python, Flask
- Python 

**Frontend:** HTML, CSS, JavaScript
- HTML 
- CSS to style the components 
- JavaScript to include functionalities 

**Database:** SQLite 
- SQLite is a portable SQL database. I found it easy to connect to and work with directly on VS Code.

## Files
main.py - the backend 

**initialiseDB.py** - A Python file to initialise the database with the Administrator table and the Restaurants table
- Default Administrator Username: admin
- Default Administrator Password: admin

## How to run
**1.** Ensure that you have installed the required technologies, libraries, and frameworks.

**2.** Replace the `MAPS_AKI_KEY` placeholder with your own Google Maps API key.

**3.** Initialise the database by running the command `python initialiseDB.py` in the terminal.

**4.** Run the main program by running the command `python main.py` in the terminal.

## Future considerations
While the application works well as an MVP and as proof of concept, there are a few improvements that I am considering to implement in the future. Notably, the administrator dashboard can benefit from including have more statistics and analytics. The inclusion of visual aids such as diagrams and graphs can also help administrators make informed decisions. 

Currently, to view the average rating of a restaurant, the administrator must enter the details of the restaurant exactly how it is stored in the database. However, standardising the input to remove manual errors and improve recognition is important to improve the overall user experience.

I would also love to hear your thoughts, so do not hesitate to give your feedback!
