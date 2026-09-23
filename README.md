# 🛒 E-Commerce Sales Data Cleaning & Exploratory Data Analysis (EDA)

An end-to-end data analytics project focused on cleaning, transforming, and analyzing transnational sales data for a UK-based online retail company.

---

## 📌 Project Overview
* **Dataset:** E-Commerce Transaction Data (UK Retailer)
* **Tools Used:** Python, Pandas, NumPy, Matplotlib, Seaborn, Kaggle Notebook
* **Key Challenge:** Raw data contained missing customer identifiers, transaction cancellations (negative quantities/prices), duplicate logs, and unstructured date strings.

---

## 🛠️ Data Cleaning Pipeline
1. **Missing Data Handling:** Filtered out ~135k rows missing `CustomerID` to ensure accurate customer-level analytics.
2. **Returns & Anomaly Removal:** Stripped negative and zero values across `Quantity` and `UnitPrice` (cancellations/inventory adjustments).
3. **De-duplication:** Removed duplicate records to preserve data integrity.
4. **Feature Engineering:**
   * Converted raw date strings into standard datetime objects.
   * Derived `TotalSpend` (`Quantity * UnitPrice`).
   * Created temporal features (`YearMonth`, `Hour`) for time-series aggregation.

---

## 📊 Key Insights & Visualizations
* **Top Products:** High-volume items are dominated by novelty homeware and party goods.
* **International Markets:** Beyond the UK domestic market, countries like the Netherlands, Germany, and France represent the largest revenue drivers.
* **Peak Purchasing Hours:** Order volume consistently peaks between **11:00 AM and 2:00 PM**.

---

## 🚀 How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/Adil-sde/ecommerce-sales-data-cleaning.git
   
