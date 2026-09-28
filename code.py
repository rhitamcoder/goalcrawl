import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

try:
    response = requests.get("https://en.wikipedia.org/wiki/FIFA_World_Cup", headers=headers)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Failed to fetch the page: {e}")
    exit()

soup = BeautifulSoup(response.text, "html.parser")

tables = soup.find_all("table", class_="wikitable")

if len(tables) < 2:
    print("Couldn't find enough tables on the page. The page structure may have changed")
    exit()

results_table = tables[1]
rows = results_table.find_all("tr")

tournaments = []

for row in rows[2:]:
    cells = row.find_all(["td", "th"])
    values = [cell.get_text(separator=" ", strip=True) for cell in cells]

    if len(values) == 10 and values[3] != "":
        tournaments.append(values)

def remove_footnotes(text):
    return re.sub(r"\[.*?\]", "", text).strip()

def fix_spacing(text):
    text = re.sub(r"\(\s+", "(", text)
    text = re.sub(r"\s+\)", ")", text)
    return text

column_names = ["edition", "year", "host", "champion", "final_score", "runner_up", "third_place", "third_place_score", "fourth_place", "teams"]

cleaned_tournaments = []
for values in tournaments:
    cleaned_values = [fix_spacing(remove_footnotes(v)) for v in values]
    record = dict(zip(column_names, cleaned_values))
    cleaned_tournaments.append(record)

if len(cleaned_tournaments) == 0:
    print("Warning: no tournaments were collected. Check the scraping logic.")
    exit()

df = pd.DataFrame(cleaned_tournaments)
df.to_csv("world_cup_results.csv", index=False)

print("Saved successfully!")
