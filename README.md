# IMDb-Top-250-Scraper-Analysis-SQL-Pipeline
End-to-end ETL pipeline scraping IMDb's Top 250. Features robust HTML parsing with BeautifulSoup, advanced data cleaning with Pandas, trend analysis using Seaborn, and automated SQL database integration via SQLAlchemy.
# 🎬 IMDb Top 250: Scraper, Analysis & SQL Pipeline

## 📌 Project Overview
This project is a comprehensive **Data Analysis & Engineering Pipeline**. It scrapes the top 250 movies from IMDb, cleans the raw data, performs Exploratory Data Analysis (EDA) to find historical trends, and stores the final dataset in a SQL database.

## 🚀 Key Features
1.  **Web Scraping:** Extracts Title, Year, Rating, Duration, and MPAA Content Rating.
2.  **Advanced Data Cleaning:**
    * **Type Casting:** Converts string years/ratings to Int/Float.
    * **Logic Conversion:** Parses strings like `"2h 45m"` into calculated integer minutes (e.g., `165`).
    * **Standardization:** Renames columns to snake_case (`user_rating`) for SQL compatibility.
3.  **Exploratory Data Analysis (EDA):**
    * Visualized **"Ratings Over Time"** to identify golden eras of cinema.
    * Analyzed **"Runtime Trends"** to see if movies are getting longer.
    * Correlation Heatmaps to find relationships between Duration and Rating.
4.  **SQL Integration:** Automated the database creation using `SQLAlchemy` to prevent file-lock errors.

## 🛠️ Tech Stack
| Category | Libraries Used |
| :--- | :--- |
| **Data Processing** | `Pandas`, `NumPy` |
| **Visualization** | `Matplotlib`, `Seaborn` |
| **Database** | `SQLAlchemy`, `SQLite3`, `JupySQL` |
| **Scraping** | `BeautifulSoup4` |

## 📊 Visual Insights
The project includes several visualizations to understand the data:
* **Correlation Heatmap:** Shows the relationship between a movie's length and its user rating.
* **Runtime Evolution:** A line chart tracking the average movie duration from the 1920s to 2024.
* **Category Analysis:** Bar charts analyzing the Content Rating (PG-13, R, etc.) of the top movies.

## 📂 Database Schema
The final SQL table `Top_Movies` is structured as follows:

| Column | Type | Description |
| :--- | :--- | :--- |
| `title` | TEXT | Movie Name |
| `year` | INTEGER | Release Year |
| `content_rating` | TEXT | MPAA Rating (e.g., PG-13) |
| `user_rating` | FLOAT | IMDb Score |
| `duration(minutes)`| INTEGER | Calculated Runtime |

## 💡 How to Run
1.  **Install Requirements:**
    ```bash
    pip install pandas seaborn sqlalchemy beautifulsoup4 ipython-sql
    ```
2.  **Execute Notebook:**
    Run `IMDB_Analysis.ipynb`. The script will:
    * Scrape/Parse the data.
    * Generate the Seaborn plots.
    * Create `Movies_Project.db` and save the data.

---
*Created as a Portfolio Project.*
