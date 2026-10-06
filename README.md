# CodeAlpha Web Scraping Project


## Project Description

This project demonstrates web scraping using Python. It extracts book information such as title, price, rating, and availability from the Books to Scrape website and stores the collected data in a CSV file.


## Technologies Used

- Python
- Requests
- BeautifulSoup
- Pandas


## Website Scraped

[Books to Scrape](https://books.toscrape.com/)


## Data Collected

The following information was extracted from the website:

- Book Title
- Price
- Rating
- Availability


## Project Structure

```text
CodeAlpha_WebScraping/
├── web_scraping.py
├── books_data.csv
└── README.md


## How It Works

1. Send a request to the website using the Requests library.
2. Parse the HTML using BeautifulSoup.
3. Extract book title, price, rating, and availability.
4. Store the extracted data in a Pandas DataFrame.
5. Clean the price data and convert it into numeric format.
6. Check for missing values and duplicate rows.
7. Save the final dataset as `books_data.csv`.


## Output Dataset

The scraped data is saved in the `books_data.csv` file.

The dataset contains:
- 20 books
- 4 columns
- Title
- Price
- Rating
- Availability


## Requirements

Make sure Python is installed on your system.

Install the required libraries using:

```bash
pip install requests beautifulsoup4 pandas


## How to Run

1. Open the project folder in VS Code.
2. Open the terminal.
3. Run the Python script using:

```bash
python web_scraping.py


## Project Status

Completed as part of the CodeAlpha Data Analytics Internship.


## Author

Fareez Khan