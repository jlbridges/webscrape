# World Weather Dashboard

## Summary

This project scrapes current weather data for cities around the world from [timeanddate.com](https://www.timeanddate.com/weather/) using Selenium, stores the data in a SQLite database, and displays it through an interactive Streamlit dashboard. The dashboard lets users filter by city and temperature range, and view the data through three visualizations: a bar chart of temperature by city, a histogram showing the distribution of temperatures, and a bar chart of temperature by local time.

## Setup

1. Clone or download this repository.
2. Create and activate a virtual environment:
   - `python -m venv .venv`
   - `.venv\Scripts\activate`
3. Install dependencies:
   - `pip install -r requirements.txt`
4. Run the scraper to populate the database:
   - `python webscrape.py`
5. Launch the dashboard:
   - `streamlit run streamlit_app.py`

## Screenshot
<img width="2249" height="1303" alt="image" src="https://github.com/user-attachments/assets/7ac129c9-8d6d-4c6f-923b-2982723f8165" />
