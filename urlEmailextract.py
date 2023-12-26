import requests
from bs4 import BeautifulSoup
import re

def is_website_up(url):
    try:
        response = requests.head(url, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

def extract_emails_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to fetch URL: {e}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    # Extract email addresses from the text content of the webpage
    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    emails = re.findall(email_pattern, soup.get_text())

    return emails

# Prompt the user to enter a URL
url = input("Enter the URL to check and extract email addresses from: ")

# Check if the website is up
if is_website_up(url):
    print("The website is up.")

    # Call the function with the user-provided URL
    emails = extract_emails_from_url(url)

    # Print the email addresses found
    if emails:
        print("Email addresses found:")
        for email in emails:
            print(email)
    else:
        print("No email addresses found on the webpage.")
else:
    print("The website is not reachable or is down.")
