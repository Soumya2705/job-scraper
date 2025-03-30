# Assignment 11: Scraping Job Postings
# 1.	Objective: Write a Python script to scrape job postings from a job website (e.g., Indeed, Glassdoor) for a specific keyword.
# 2.	Instructions:
# ○	Use requests to access the job listing page with the specified keyword (e.g., "Python Developer").
# ○	Use BeautifulSoup to parse the page and extract job titles, company names, locations, and brief descriptions.
# ○	Display the extracted information in a structured format (e.g., table).
# ○	Save the scraped job postings to a CSV file.


# Project made by:
# 1. Divyansh Sharma (2446010)
# 2. Nandini Bansal (2446057)
# 3. Soumyajit saha (2446024)


import pandas as pd
import requests
from bs4 import BeautifulSoup

# Base URL for the Shine job search site
base_url = "https://www.shine.com"

def find_job_postings(job_title, loc, pages):

    # Format the job title and location for URL compatibility
    job_title = job_title.lower().replace(" ", "-")
    loc = loc.lower().replace(" ", "-")

    job_postings = []

    for page in range(1, pages + 1):
        url = f"{base_url}/job-search/{job_title}-jobs-in-{loc}-{page}"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error if the request failed
            soup = BeautifulSoup(response.text, "html.parser")
            print(f"Processing page {page}...")

            # Find all job cards on the page
            job_cards = soup.find_all("div", class_="jobCard")
            for job_card in job_cards:
                try:
                    job_url = base_url + job_card.find("a")["href"]
                    job_response = requests.get(job_url)
                    job_response.raise_for_status()

                    job_soup = BeautifulSoup(job_response.text, "html.parser")

                    # Extract job details
                    title = job_soup.find("h1", class_="font-size-24").text.strip()
                    company = job_soup.find("div", class_="JobDetailWidget_jobCard_cName__qvsdW").text.strip()
                    location = job_soup.find("div", class_="JobDetailWidget_jobCard_lists_item__w6Yow JobDetailWidget_locationIcon__u85a7").find("a").text.strip()
                    description = job_soup.find("div", class_="jobDetail_jsrpRightDetail_text__jqs8a").find("span").text.strip()
                    key_skills = job_soup.find("li",class_="btn btn-white-border").find_all("li").text.strip()

                    # Append job details to the list
                    job_postings.append({
                        "Job Title": title,
                        "Company": company,
                        "Location": location,
                        "Description": description,
                        "Key Skills":key_skills,
                    })
                    print(f"Added job: {title} at {company}")

                except (requests.RequestException, AttributeError) as e:
                    print(f"Failed to retrieve job details from {job_url}: {e}")

        except requests.RequestException as e:
            print(f"Failed to retrieve page {page}: {e}")

    return job_postings


job_title = input("Enter job title you want to search: ")
location = input("Enter location you want to search: ")
try:
    pages = int(input("Enter number of pages you want to search: "))
    print("Fetching data...")

    # Fetch job postings and save them to a CSV-comma seperated value file
    job_postings = find_job_postings(job_title, location, pages)
    if job_postings:
        df = pd.DataFrame(job_postings)

        df.to_csv("shine_job.csv", index=False)
        print("Job data saved to shine_job.csv")
    else:
        print("No job postings found.")

except ValueError:
    print("Invalid input for the number of pages. Please enter an integer.")

