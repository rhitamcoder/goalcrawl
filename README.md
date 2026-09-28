# ⚽ Goalcrawl

**A Python web scraper that turns Wikipedia's FIFA World Cup history into a clean, analysis-ready CSV.**

Goalcrawl fetches the FIFA World Cup page on Wikipedia, locates the tournament results table, cleans the messy scraped text, and exports every edition, from Uruguay 1930 through 2026, into a single structured dataset. Each row covers one tournament: host, champion, final score, runner-up, third and fourth place, and the number of teams.

---

## ✨ Features

- 🌐 **Scrapes live data** from Wikipedia using `requests` and `BeautifulSoup`
- 🧹 **Cleans the output**: strips footnote markers like `[a]` and fixes stray spacing around parentheses
- 🛡️ **Defensive error handling**: exits gracefully on network failures, missing tables, or an empty result
- 📄 **Exports to CSV** with clear, consistent column names, ready for pandas, Excel, or Google Sheets
- 🏆 **Covers 23 tournaments**, from the first World Cup in 1930 to the 48-team 2026 edition

---

## 🛠️ Tech Stack

- **Python 3**
- **requests**: fetching the web page
- **BeautifulSoup4**: parsing HTML and extracting table rows
- **re** (standard library): cleaning footnotes and spacing
- **pandas**: structuring the data and writing the CSV

---

## 📁 Project Structure

```
goalcrawl/
├── code.py                  # Scraper script
├── world_cup_results.csv    # Generated output (23 tournaments)
└── README.md
```

---

## 📦 Output Dataset

Running the script produces `world_cup_results.csv` with these columns:

| Column              | Description                                              |
|---------------------|----------------------------------------------------------|
| `edition`           | Tournament number (1 to 23)                              |
| `year`              | Year the tournament was held                             |
| `host`              | Host country or countries                                |
| `champion`          | Winning team                                             |
| `final_score`       | Final result, including extra time and penalties         |
| `runner_up`         | Losing finalist                                          |
| `third_place`       | Third-place team                                         |
| `third_place_score` | Score of the third-place match                           |
| `fourth_place`      | Fourth-place team                                        |
| `teams`             | Number of participating teams                            |

**Sample rows:**

| edition | year | host    | champion  | final_score  | runner_up      | teams |
|---------|------|---------|-----------|--------------|----------------|-------|
| 1       | 1930 | Uruguay | Uruguay   | 4–2          | Argentina      | 13    |
| 2       | 1934 | Italy   | Italy     | 2–1 (a.e.t.) | Czechoslovakia | 16    |
| 3       | 1938 | France  | Italy     | 4–2          | Hungary        | 15    |

---

## ▶️ Getting Started

### Prerequisites

```
pip install requests beautifulsoup4 pandas
```

### Running the Scraper

```
git clone https://github.com/rhitamcoder/goalcrawl.git
```
```
cd goalcrawl
```
```
python code.py
```

If everything works, you'll see `Saved successfully!` and a fresh `world_cup_results.csv` will appear in the project folder.

---

## 🧠 How It Works

1. **Fetch**: sends a request to the Wikipedia FIFA World Cup page with a browser-style `User-Agent` header
2. **Locate**: finds all `wikitable` tables and selects the tournament results table
3. **Extract**: loops through the table rows, keeping only complete 10-column rows that have a champion
4. **Clean**: removes footnote references (e.g. `[a]`) and tidies spacing around parentheses
5. **Export**: loads the records into a pandas DataFrame and saves them as a CSV

---

## ⚠️ Limitations

Goalcrawl depends on the current layout of the Wikipedia page. The script reads the second `wikitable` on the page and expects 10 columns per row, so if Wikipedia restructures that table, the scraper may need updating. It exits with a clear message when it can't find the expected structure.

---

## 📝 License

The code in this repository is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

> **Note:** The MIT License applies to the code only. The scraped data comes from [Wikipedia](https://en.wikipedia.org/wiki/FIFA_World_Cup), whose text is available under the [CC BY-SA license](https://en.wikipedia.org/wiki/Wikipedia:Text_of_the_Creative_Commons_Attribution-ShareAlike_4.0_International_License). Please attribute Wikipedia if you reuse the data.

## 🙌 Acknowledgements

Data sourced from the [FIFA World Cup](https://en.wikipedia.org/wiki/FIFA_World_Cup) article on Wikipedia.
