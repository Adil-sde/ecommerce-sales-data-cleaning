# 🛒 E-Commerce Sales Analytics & RFM Segmentation Pipeline

An end-to-end data analytics project focused on data cleaning, automated database pipelines, business intelligence analysis, and customer tier segmentation for transnational retail records.

---

## 📌 Project Overview
* **Dataset:** 500K+ Transnational E-Commerce Sales Records
* **Tech Stack:** Python (Pandas, NumPy, Matplotlib, Seaborn, SQLAlchemy), MySQL Workbench, VS Code
* **Core Objectives:** Handle anomalous data (returns, missing IDs), automate database ingestion, calculate MoM sales growth, and perform RFM customer segmentation.

---

## 🛠️ Data Pipeline Architecture
1. **Data Cleaning (Pandas):** 
   * Filtered 135K+ records with missing `CustomerID`.
   * Removed cancellations/returns (negative `Quantity`) and zero unit prices.
   * Engineered temporal features (`YearMonth`, `Hour`, `TotalSpend`).
2. **Database Ingestion (SQLAlchemy):**
   * Designed optimal schema with primary keys, indexes, and precise decimal types.
   * Executed chunked automated data upload into MySQL database.
3. **Business Intelligence & SQL Analytics:**
   * **MoM Growth:** Calculated monthly revenue changes using CTEs and `LAG()` window functions.
   * **RFM Segmentation:** Segmented buyers into VIP, Loyal, and At-Risk tiers using `NTILE(4)`.
   * **Sales Trends:** Analyzed peak transaction hours and top international revenue streams.

---

## 📊 Key SQL Queries
* `data_cleaning.sql`: Contains schema definitions, aggregation metrics, MoM growth calculations, and the RFM segmentation model.

---

## 👤 Author & Connect
* **Adil Ansari**
* **GitHub:** [github.com/Adil-sde](https://github.com/Adil-sde)
* **LinkedIn:** [linkedin.com/in/adilansarisde](https://www.linkedin.com/in/adilansarisde/)
