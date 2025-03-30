# 🛠️ **Job Scraper Project**
A Python script that scrapes job postings from **Shine.com** based on specified keywords and location, extracts relevant job details, and saves them into a CSV file.

## 🚀 **Features**
- ✅ Scrapes job postings from **multiple pages**.
- ✅ Extracts the following details:
  - **Job Title**
  - **Company Name**
  - **Location**
  - **Job Description**
  - **Key Skills**
- ✅ Saves the scraped data into a `CSV` file.
- ✅ Handles **HTTP exceptions** and missing data gracefully.
- ✅ Displays the job postings in the terminal while scraping.

---

## 🔧 **Technologies Used**
- Python
- `requests` → To send HTTP requests and retrieve the job listing pages.
- `BeautifulSoup` → For HTML parsing and data extraction.
- `pandas` → For organizing and saving the data into a CSV file.

---

## ⚙️ **Installation & Usage**

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/Soumya2705/job-scraper.git
cd job-scraper
```

### 2️⃣ **Install Dependencies**
Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate    # On Linux/Mac
.\venv\Scripts\activate     # On Windows
```

Install the required libraries:
```bash
pip install -r requirements.txt
```

### 3️⃣ **Run the Script**
```bash
python scraper.py
```

✅ **Input values:**
- **Job title** (e.g., `Python Developer`)
- **Location** (e.g., `Bangalore`)
- **Number of pages** (e.g., `3`)

---

## 🗃️ **File Structure**
```
📁 job-scraper
 ├── scraper.py           # Main scraping script
 ├── requirements.txt     # Python dependencies
 ├── shine_job.csv        # Output file with job postings
 ├── README.md            # Project documentation
```

---

## 📊 **Sample Output (CSV)**

The output file `shine_job.csv` will contain the following columns:
```
| Job Title         | Company         | Location      | Description             | Key Skills        |
|-------------------|----------------|---------------|--------------------------|-------------------|
| Python Developer  | ABC Solutions  | Bangalore     | Backend development role | Python, Django    |
| Data Analyst      | XYZ Pvt. Ltd.  | Pune          | Data analysis expert     | SQL, Excel        |
```

---

## ✅ **Error Handling**
- Handles `requests` exceptions, such as:
  - **Timeouts**
  - **Connection errors**
  - **Invalid responses**
- Skips invalid or incomplete job postings gracefully.

