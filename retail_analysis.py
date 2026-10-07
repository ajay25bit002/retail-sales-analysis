"""Summarize retail sales and save a few simple charts."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


DATA_FILE = Path(__file__).with_name("retail_sales.csv")


def main():
    sales_data = pd.read_csv(DATA_FILE)

    print("First 5 rows:")
    print(sales_data.head())

    print("\nMissing values before cleaning:")
    print(sales_data.isnull().sum())

    # Remove incomplete rows and convert columns to the types used below.
    sales_data = sales_data.dropna().copy()
    sales_data["Date"] = pd.to_datetime(sales_data["Date"], errors="coerce")
    sales_data["Quantity"] = pd.to_numeric(sales_data["Quantity"], errors="coerce")
    sales_data["Price"] = pd.to_numeric(sales_data["Price"], errors="coerce")
    sales_data = sales_data.dropna(subset=["Date", "Quantity", "Price"])
    sales_data = sales_data[sales_data["Quantity"] > 0]
    sales_data = sales_data[sales_data["Price"] >= 0].copy()

    sales_data["Sales"] = sales_data["Quantity"] * sales_data["Price"]
    total_revenue = sales_data["Sales"].sum()

    product_quantities = sales_data.groupby("Product")["Quantity"].sum()
    best_selling_product = product_quantities.idxmax()
    best_selling_quantity = product_quantities.max()

    category_sales = sales_data.groupby("Category")["Sales"].sum().sort_values(ascending=False)
    best_category = category_sales.idxmax()
    best_category_revenue = category_sales.max()

    region_sales = sales_data.groupby("Region")["Sales"].sum().sort_values(ascending=False)
    monthly_sales = sales_data.groupby(sales_data["Date"].dt.to_period("M"))["Sales"].sum()
    monthly_sales.index = monthly_sales.index.astype(str)
    highest_sales_month = monthly_sales.idxmax()
    highest_month_sales = monthly_sales.max()

    print("\nAnalysis results:")
    print(f"Records analyzed: {len(sales_data)}")
    print(f"Total revenue: ${total_revenue:,.2f}")
    print(f"Best-selling product (by quantity): {best_selling_product} ({best_selling_quantity:g} units)")
    print(f"Best-performing category (by revenue): {best_category} (${best_category_revenue:,.2f})")
    print("\nRegion-wise sales:")
    print(region_sales.to_string(float_format=lambda amount: f"${amount:,.2f}"))
    print("\nMonthly sales:")
    print(monthly_sales.to_string(float_format=lambda amount: f"${amount:,.2f}"))
    print(f"\nHighest-sales month: {highest_sales_month} (${highest_month_sales:,.2f})")

    category_sales.plot(kind="bar", color="#2f7f78", title="Sales by Category")
    plt.xlabel("Category")
    plt.ylabel("Sales ($)")
    plt.xticks(rotation=25, ha="right")
    plt.tight_layout()
    plt.savefig(Path(__file__).with_name("sales_by_category.png"))
    plt.close()

    region_sales.plot(kind="bar", color="#d18b47", title="Sales by Region")
    plt.xlabel("Region")
    plt.ylabel("Sales ($)")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(Path(__file__).with_name("sales_by_region.png"))
    plt.close()

    monthly_sales.plot(kind="line", marker="o", color="#496b9a", title="Monthly Sales")
    plt.xlabel("Month")
    plt.ylabel("Sales ($)")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(Path(__file__).with_name("monthly_sales.png"))
    plt.close()

    print("\nKey Findings")
    print(f"- Total revenue across {len(sales_data)} orders was ${total_revenue:,.2f}.")
    print(f"- {best_selling_product} sold the most units ({best_selling_quantity:g}).")
    print(f"- {best_category} generated the highest category revenue (${best_category_revenue:,.2f}).")
    print(f"- {highest_sales_month} was the strongest month (${highest_month_sales:,.2f}).")
    print(f"- {region_sales.idxmax()} was the highest-revenue region (${region_sales.max():,.2f}).")
    print("\nCharts saved: sales_by_category.png, sales_by_region.png, monthly_sales.png")


if __name__ == "__main__":
    main()
