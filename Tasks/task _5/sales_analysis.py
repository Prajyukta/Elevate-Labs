import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")
print("Preview of Data:")
print(df.head())
print("\nDataset Info:")
print(df.info())

print("\nShape of Dataset (rows, columns):")
print(df.shape)

print("\nStatistical Summary:")
print(df.describe())

# ========================
# 4. Group & Aggregate
# ========================
# Total Sales by Product
sales_by_product = df.groupby("Product")["Sales"].sum()
print("\nSales by Product:")
print(sales_by_product)

# Total Sales by Region
sales_by_region = df.groupby("Region")["Sales"].sum()
print("\nSales by Region:")
print(sales_by_region)

# ========================
# 5. Visualizations
# ========================

# Bar Chart - Sales by Product
sales_by_product.plot(kind="bar", title="Sales by Product", figsize=(6,4))
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.show()

# Pie Chart - Sales by Region
sales_by_region.plot(kind="pie", autopct="%1.1f%%", title="Sales by Region", figsize=(5,5))
plt.ylabel("")  # remove y-label
plt.show()

# ========================
# 6. Filtering Rows
# ========================
# Filter rows where Sales > 800
high_sales = df[df["Sales"] > 800]
print("\nHigh Sales Transactions (Sales > 800):")
print(high_sales)

# Example: Filter rows where Region = 'East'
east_region = df[df["Region"] == "East"]
print("\nSales in East Region:")
print(east_region)

# ========================
# 7. Save Results
# ========================
# Save grouped results
sales_by_product.to_csv("sales_by_product.csv")
sales_by_region.to_csv("sales_by_region.csv")

print("\n✅ Analysis Complete. Results saved as CSV files.")
