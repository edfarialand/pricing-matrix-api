# Pricing Matrix API

This project is a Flask-based API that provides pricing information for new and used iPhones. It scrapes data from external sources and provides endpoints to query this information.

## Project Structure

The project consists of two main Python files:

1. `app.py`: Contains the main Flask application and API routes.
2. `constants.py`: Defines constants and enums used throughout the project.

## Features

- Scrape new phone pricing data from a specified URL
- Retrieve used iPhone pricing data from a Google Sheets document
- API endpoint to query used iPhone prices based on model, storage, carrier lock status, and grade

## Setup and Installation

1. Clone the repository
2. Install the required dependencies:
   ```
   pip install flask pandas requests beautifulsoup4 lxml
   ```

## Usage

To run the application:

```
python app.py
```

This will start the Flask development server.

## API Endpoints

### GET /api/iphone-used/<model>

Returns the price of a used iPhone based on the provided parameters.

Query Parameters:
- `unlocked` (optional): Set to 'true' if the phone is unlocked. Default is false.
- `grade` (optional): The grade of the phone (swap, a, b, c, d, doa). Default is 'b'.
- `storage` (optional): The storage capacity of the phone. Default is '256gb'.

Example Request:
```
GET /api/iphone-used/iphone%2012?unlocked=true&grade=a&storage=128gb
```

## Functions

### new_phone_data()

Scrapes pricing data for new phones from the specified URL. Currently, this function is not fully implemented and only prints the scraped data.

### used_phone_data()

Retrieves and processes used iPhone pricing data from a Google Sheets document. It returns a pandas DataFrame with the processed data.

### iphone_used(model: str)

Handles the API request for used iPhone pricing. It processes the request parameters and returns the appropriate price or error message.

## Constants

The `constants.py` file contains:

- URLs for data sources
- An `AtlasSheets` enum that maps sheet names to Google Docs IDs

## Notes

- The project uses BeautifulSoup for web scraping and pandas for data manipulation.
- Ensure you have the necessary permissions to access the Google Sheets document specified in the `AtlasSheets` enum.

## Future Improvements

- Implement error handling for network requests
- Complete the implementation of the `new_phone_data()` function
- Add more comprehensive input validation for API requests
- Implement caching to reduce the number of requests to external data sources
