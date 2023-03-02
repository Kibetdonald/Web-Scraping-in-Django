# Web-Scraping-in-Django
This project is a Django web application that scrapes data from a classcentral.com and stores it in a database. The scraped data is displayed on a web page using an endpoint that can be consumed in a front-end application

Installation
To run this project locally, you'll need to follow these steps:

Clone the repository to your local machine:
bash
```
git clone https://github.com/your_username/web-scraping-project.git
```
Install the required dependencies:
```
pip install -r requirements.txt
```
Create a database and run migrations:
```
python manage.py migrate
```
Start the Django development server:
```
python manage.py runserver
```
To use the application, follow these steps:

- Navigate to the homepage of the web application in your web browser.

- Click the "Scrape" button to initiate the web scraping process.

- Once the web scraping process is complete, the scraped data will be displayed on the webpage.

## Web Scraping
This web application uses the BeautifulSoup library to scrape data from a website. The web scraping code is located in the views.py file in the web_scraping app.

## Database
This web application uses a PostgreSQL database to store the scraped data. The database schema is defined in the models.py file in the web_scraping app.
