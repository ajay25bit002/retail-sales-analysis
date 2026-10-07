# Retail Sales Data Analysis

## Objective

Explore a small retail sales dataset with Python, Pandas, and Matplotlib. The project calculates revenue and highlights useful trends by product, category, region, and month.

## Real-World Problem

Retailers need to know which products and categories generate sales, where customers are buying, and when sales are strongest. This analysis turns order records into a few clear summaries that can support inventory and promotion decisions.

## Dataset Description

`retail_sales.csv` contains 36 sample order records from January through June 2025. Each row represents one order line and includes:

| Column | Description |
| --- | --- |
| `Order_ID` | Unique order number |
| `Date` | Date of the order |
| `Product` | Product sold |
| `Category` | Product category |
| `Quantity` | Number of units sold |
| `Price` | Price per unit in dollars |
| `Region` | Sales region |

The data is realistic sample data created for this project, not actual customer or business records.

## Technologies Used

- Python
- Pandas
- Matplotlib

Install the required packages and run the analysis:

```bash
pip install pandas matplotlib
python retail_analysis.py
```

## Data Cleaning

The script checks each column for missing values, removes incomplete rows, converts dates and numeric values to the appropriate types, and excludes rows with invalid dates, non-positive quantities, or negative prices. It then calculates each order line's sales as `Quantity × Price`.

## Analysis Performed

- Total revenue
- Best-selling product by total quantity
- Best-performing category by revenue
- Revenue by region
- Revenue by month
- Month with the highest revenue

## Visualizations

Running the script saves these charts in the project folder:

- `sales_by_category.png`
- `sales_by_region.png`
- `monthly_sales.png`

## Key Findings

- Total revenue across 36 orders was **$3,717.69**.
- **Notebook** was the best-selling product by quantity, with 83 units sold.
- **Clothing** was the best-performing category by revenue, with $1,415.50 in sales.
- **June 2025** had the highest monthly revenue at $971.72.
- The **South** region had the highest regional revenue at $948.27.

Running `python retail_analysis.py` prints these results and the complete region-wise and monthly sales totals in the terminal.

## Conclusion

This beginner-friendly example shows how a short Pandas workflow can clean order data, calculate sales, compare business dimensions, and create charts. The results can help illustrate product and seasonal trends, while real business decisions should use a larger, verified dataset.# Retail Sales Data Analysis

## Objective

Analyze a small retail sales dataset with Python, Pandas, and Matplotlib to find useful patterns in product, category, region, and monthly sales.

## Real-World Problem

Retail businesses need to know which products and categories customers buy most, which regions generate the most sales, and when sales are strongest. These insights help with inventory, promotions, and planning.

## Dataset Description

`retail_sales.csv` contains 36 sample orders from January through June 2025. Each row represents one order and includes:

| Column | Description |
| --- | --- |
| `Order_ID` | Unique order number |
| `Date` | Date the order was placed |
| `Product` | Product sold |
| `Category` | Product category |
| `Quantity` | Number of units sold |
| `Price` | Price per unit in dollars |
| `Region` | Sales region |

The dataset is realistic sample data for learning and does not represent a real business.

## Technologies Used

- Python
- Pandas
- Matplotlib

Install the dependencies and run the analysis from this folder:

```bash
pip install pandas matplotlib
python retail_analysis.py
```

## Data Cleaning

The script checks each column for missing values, removes rows that are missing required information, and filters out rows with non-positive quantities or negative prices. It converts order dates to dates and calculates each row's sales as `Quantity × Price`.

## Analysis Performed

- Displays the first five dataset rows and missing-value counts.
- Calculates total revenue.
- Finds the best-selling product by units sold.
- Identifies the best-performing category by revenue.
- Calculates total sales by region and by month.
- Identifies the month with the highest sales.

## Visualizations

Running `python retail_analysis.py` saves three charts in this folder:

- `sales_by_category.png` — revenue by product category.
- `sales_by_region.png` — revenue by sales region.
- `monthly_sales.png` — revenue over time.

## Key Findings

The script prints the exact results in the terminal each time it runs. With the included sample dataset:

- **Notebook Set** is the best-selling product by units sold.
- **Electronics** is the best-performing category by revenue.
- **West** is the region with the highest sales.
- **June 2025** is the highest-sales month.

## Conclusion

This beginner-friendly project demonstrates how to load and clean retail data, summarize sales with Pandas, and communicate the results using simple charts. The findings can help a retailer focus inventory and marketing on popular products, categories, regions, and months.
