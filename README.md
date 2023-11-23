# Django App  
### Challenge Overview:

Your task is to repair a malfunctioning Django application. Then ensure that application can successfully visualizes data from the provided file 'dataset_world_population_by_country_name.json' 

## How to run application

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt 
python manage.py makemigrations 
python manage.py migrate 
python manage.py collectstatic --noinput 
python manage.py runserver  0.0.0.0:8000

or

docker-compose up   
```

Open http://127.0.0.1:8000/ in browser

## Web Application Task List

1. **Home Page Accessibility:** Ensure that the home page of the application is accessible and functioning properly.

2. **User Registration Functionality:** Test and verify the 'user register' function to ensure it is working correctly for new user registrations.

3. **User Login Functionality:** Fix user login function to confirm it allows users to log in without issues. return JWT access token on a successful login.

4. **User Data Retrieval:** Fetch all user data using the '/api/user/me' API endpoint and ensure the data is correctly retrieved and displayed.

5. **Data Import and Visualization:** Using data form 'dataset_world_population_by_country_name.json' file Visualiz on the home page, (can use SQLite3 database) present this data in various formats:
    - Create a table to display the data in a structured format.
    - Implement a bar graph for a visual representation of the data.
    - Consider other graphical representations like pie charts or line graphs as appropriate.

6. **Advanced Search Functionality:** Develop an advanced search bar on the home page. This feature should allow users to perform detailed searches within the world population data.
7. **Add a Logout button:** Make sure JWT token is invalid after logging out 

## Instructions for Candidates

Understand the Django application, Django ORM and Dataset:  

1. Setup Development Environment:
    Ensure you have Python 3 and Django are installed.
    Optionally, set up SQLite if you plan to use a database.

2. Application Development:
    - Fix broken app and add new features. every feature should fit in home page itself. 
    - Make sure the application runs on 0.0.0.0 at port 8000.
    - Ensure all dashboard features are accessible via http://0.0.0.0:8000/. Do not add new pages

5. Donot change application port number while submiting the code. 

6. Documentation:
    - Create a README file including:
        - An overview of the application and Home page.
        - Details of building components and any external libraries used.
        - Highlight unique features or functionalities of your dashboard.
        - Provide detailed instructions on how to run the application.

7. How to Submit answer:
    - Submit your complete project code along with the README file to a public Github repository
    - Ensure your code is well-commented, follow proper structure and follows good coding practices.
    - Share public Github repository in provided Google forms

### List down your API endpoints
1. http://localhost:8000/api/user/register
2. http://localhost:8000/api/user/login
3. http://localhost:8000/api/user/me
4. http://localhost:8000/api/user/home
5. http://localhost:8000/api/user/logout