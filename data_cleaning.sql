create database ecommerce_db;
USE ecommerce_db;
create table sales_data (
InvoiceNo varchar(50),
StockCode varchar(50),
Description TEXT,
Quantity INT,
InvoiceDate DATETIME,
UnitPrice DECIMAL(10,2),
CustomerId varchar(50),
Country varchar(100),
TotalSpend DECIMAL(12,2),
YearMonth varchar(10),
Hour int
);

use ecommerce_db;
-- Total row count check table
select count(*) as total_records from ecommerce_db.sales_data;
-- sample preview
select * from sales_data limit 5;

-- Top 10 Countries by total Revenue
select
Country,
count(distinct InvoiceNo) as totalOrders,
count(distinct CustomerId) as TotalCustomers,
round(sum(TotalSpend), 2) as TotalRevenue
from sales_data
group by country
order by TotalRevenue desc
limit 10;