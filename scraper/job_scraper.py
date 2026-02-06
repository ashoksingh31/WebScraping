import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://remoteok.com/remote-python-jobs"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

jobs = []

for job in soup.find_all("tr", class_="job"):
    title = job.find("h2")
    company = job.find("h3")

    if title and company:
        jobs.append({
            "title": title.text.strip(),
            "company": company.text.strip()
        })

df = pd.DataFrame(jobs)
df.to_csv("python_jobs.csv", index=False)

print("Saved python_jobs.csv")
