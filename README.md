# webpage-email-extractor
This Python script checks if a website is up and extracts email addresses from the specified URL.

## Description
The Webpage Email Extractor is a Python script designed to assist users in checking the availability of a website and extracting email addresses from its content. It utilizes the `requests` library to send HTTP requests to the specified URL and retrieve the webpage's content. The content is then parsed using the `BeautifulSoup` library to extract email addresses using a regular expression pattern.

## Prerequisites

- Python 3.x
- `requests` library (install with `pip install requests`)
- `beautifulsoup4` library (install with `pip install beautifulsoup4`)

## Usage

1. Clone the repository or download the `webpage_email_extractor.py` file.
2. Install the required dependencies using pip:

   ```bash
   pip install requests beautifulsoup4

 # Run the script
urlEmailExtract.py

enter the URL of the website you want to check and extract email addresses from when prompted.

# Features
Checks the availability of a website by sending a HEAD request.
Retrieves the content of the webpage using the requests library.
Parses the HTML content using BeautifulSoup to extract email addresses.
Uses a regular expression pattern to identify and extract email addresses from the webpage's text content.


