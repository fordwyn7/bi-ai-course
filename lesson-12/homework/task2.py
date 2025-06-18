import requests
import sqlite3
from bs4 import BeautifulSoup

with sqlite3.connect("jobs.db") as conn:
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            job_title TEXT UNIQUE, 
            company_name TEXT UNIQUE, 
            location TEXT UNIQUE, 
            job_description TEXT,
            application_link TEXT
            )
        """
    )
    conn.commit()
    
res = requests.get("https://realpython.github.io/fake-jobs")
soup = BeautifulSoup(res.content, "html.parser")
jobs = soup.find_all("h2", class_="title is-5")
companies = soup.find_all("h3", class_="subtitle is-6 company")
locations = soup.find_all("p", class_="location")
aplication_links = "https://www.realpython.com"
links = soup.find_all("a", class_ = "card-footer-item")
desc_links = []
for i in links:
    i = i.get("href")
    if i != aplication_links:
        desc_links.append(i)

descriptions = []
for i in desc_links:
    res = requests.get(i)
    soup = BeautifulSoup(res.content, "html.parser")
    description = soup.find_all("p")
    descriptions.append(description[1].text)

for i in range(len(jobs)):
    job_title = jobs[i].text.strip()
    company_name = companies[i].text.strip()
    location = locations[i].text.strip()
    job_description = descriptions[i]
    application_link = desc_links[i]
    
    cursor.execute(
        """INSERT OR IGNORE INTO jobs (job_title, company_name, location, job_description, application_link) 
           VALUES (?, ?, ?, ?, ?)""",
        (job_title, company_name, location, job_description, application_link)
    )
    
def filter_jobs_by_location(location):
    with sqlite3.connect("jobs.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM jobs WHERE location = ?", (location,)
        )
        return cursor.fetchall()

def filter_jobs_by_company(company_name):
    with sqlite3.connect("jobs.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM jobs WHERE company_name = ?", (company_name,)
        )
        return cursor.fetchall()

def export_to_csv(filename):
    import csv
    with sqlite3.connect("jobs.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM jobs")
        rows = cursor.fetchall()
        
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([description[0] for description in cursor.description])  # Write headers
            writer.writerows(rows)  # Write data

