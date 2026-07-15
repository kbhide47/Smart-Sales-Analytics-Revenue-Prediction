import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/cleaned/cleaned_superstore.csv")

print("File Loaded")

# Convert date columns
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

print(df["Order Date"].dtype) 
sales_by_category = df.groupby("Category")["Sales"].sum()

print("Grouping Done")

plt.figure(figsize=(8,5))
sales_by_category.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

print("Before Show")
plt.savefig("images/sales_by_category.png") #save this img
plt.show()

print("After Show")
# ============================================
# Sales by Sub-Category
# ============================================

sales_by_subcategory = df.groupby("Sub-Category")["Sales"].sum().sort_values()

print("\n========== SALES BY SUB-CATEGORY ==========")
print(sales_by_subcategory)

plt.figure(figsize=(12,6))

sales_by_subcategory.plot(kind="barh")

plt.title("Total Sales by Sub-Category")
plt.xlabel("Sales")
plt.ylabel("Sub-Category")

plt.tight_layout()
plt.savefig("images/sales_by_subcategory.png")


plt.show()
# ============================================
# Profit by Category
# ============================================

profit_by_category = df.groupby("Category")["Profit"].sum()

print("\n========== PROFIT BY CATEGORY ==========")
print(profit_by_category)
# ==========================================
# Profit by Category
# ==========================================

profit_by_category = df.groupby("Category")["Profit"].sum()

print("\n========== PROFIT BY CATEGORY ==========")
print(profit_by_category)

plt.figure(figsize=(8,5))

profit_by_category.plot(kind="bar")

plt.title("Total Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")

plt.tight_layout()

plt.savefig("images/profit_by_category.png")

plt.show()
# ==========================================
# Profit by Sub-Category
# ==========================================

profit_by_subcategory = df.groupby("Sub-Category")["Profit"].sum().sort_values()

print("\n========== PROFIT BY SUB-CATEGORY ==========")
print(profit_by_subcategory)

plt.figure(figsize=(12,6))

profit_by_subcategory.plot(kind="barh")

plt.title("Total Profit by Sub-Category")
plt.xlabel("Profit")
plt.ylabel("Sub-Category")

plt.tight_layout()

plt.savefig("images/profit_by_subcategory.png")

plt.show()
# ==========================================
# Sales by Region
# ==========================================

sales_by_region = df.groupby("Region")["Sales"].sum().sort_values()

print("\n========== SALES BY REGION ==========")
print(sales_by_region)
plt.figure(figsize=(8,5))

sales_by_region.plot(kind="bar")

plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")

plt.tight_layout()

plt.savefig("images/sales_by_region.png")

plt.show()
sales_by_region = df.groupby("Region")["Sales"].sum().sort_values()
print("\n========== SALES BY REGION ==========")
print(sales_by_region)

# ==========================================
# Profit by Region
# ==========================================

profit_by_region = df.groupby("Region")["Profit"].sum().sort_values()

print("\n========== PROFIT BY REGION ==========")
print(profit_by_region)
plt.figure(figsize=(8,5))

profit_by_region.plot(kind="bar", color="green")

plt.title("Total Profit by Region")
plt.xlabel("Region")
plt.ylabel("Profit")

plt.tight_layout()

plt.savefig("images/profit_by_region.png")

plt.show()
# =====================================
# Monthly Sales Trend
# =====================================

monthly_sales = df.groupby(df["Order Date"].dt.to_period("M"))["Sales"].sum()

print("\n========== MONTHLY SALES ==========")
print(monthly_sales)

plt.figure(figsize=(12,5))

monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("images/monthly_sales_trend.png")

plt.show()
# =====================================
# Monthly Profit Trend
# =====================================

monthly_profit = df.groupby(df["Order Date"].dt.to_period("M"))["Profit"].sum()

print("\n========== MONTHLY PROFIT ==========")
print(monthly_profit)

plt.figure(figsize=(12,5))

monthly_profit.plot(kind="line", marker="o", color="green")

plt.title("Monthly Profit Trend")
plt.xlabel("Month")
plt.ylabel("Profit")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("images/monthly_profit_trend.png")

plt.show()
# ==========================================
# Monthly Sales Trend
# ==========================================

# Create Month-Year column
df["Month"] = df["Order Date"].dt.to_period("M")

monthly_sales = df.groupby("Month")["Sales"].sum()

print("\n========== MONTHLY SALES ==========")
print(monthly_sales)

plt.figure(figsize=(12,5))

monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("images/monthly_sales_trend.png")

plt.show()
# ==========================================
# Sales by Segment
# ==========================================

sales_by_segment = df.groupby("Segment")["Sales"].sum().sort_values()

print("\n========== SALES BY SEGMENT ==========")
print(sales_by_segment)

plt.figure(figsize=(8,5))

sales_by_segment.plot(kind="bar", color="skyblue")

plt.title("Sales by Segment")
plt.xlabel("Segment")
plt.ylabel("Sales")

plt.tight_layout()

plt.savefig("images/sales_by_segment.png")

plt.show()
# ==========================================
# Profit by Segment
# ==========================================

profit_by_segment = df.groupby("Segment")["Profit"].sum().sort_values()

print("\n========== PROFIT BY SEGMENT ==========")
print(profit_by_segment)

plt.figure(figsize=(8,5))

profit_by_segment.plot(kind="bar", color="green")

plt.title("Profit by Segment")
plt.xlabel("Segment")
plt.ylabel("Profit")

plt.tight_layout()

plt.savefig("images/profit_by_segment.png")

plt.show()
# ==========================================
# Sales by Ship Mode
# ==========================================

sales_by_shipmode = df.groupby("Ship Mode")["Sales"].sum().sort_values()

print("\n========== SALES BY SHIP MODE ==========")
print(sales_by_shipmode)

plt.figure(figsize=(8,5))

sales_by_shipmode.plot(kind="bar")

plt.title("Sales by Ship Mode")
plt.xlabel("Ship Mode")
plt.ylabel("Sales")

plt.tight_layout() # Adjusts spacing automatically

plt.savefig("images/sales_by_shipmode.png")

plt.show()
# ==========================================
# Profit by Ship Mode
# ==========================================

profit_by_shipmode = df.groupby("Ship Mode")["Profit"].sum().sort_values()

print("\n========== PROFIT BY SHIP MODE ==========")
print(profit_by_shipmode)

plt.figure(figsize=(8,5))

profit_by_shipmode.plot(kind="bar")

plt.title("Profit by Ship Mode")
plt.xlabel("Ship Mode")
plt.ylabel("Profit")

plt.tight_layout()

plt.savefig("images/profit_by_shipmode.png")

plt.show()
# ==========================================
# Top 10 Products by Sales
# ==========================================

top10_sales_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n========== TOP 10 PRODUCTS BY SALES ==========")
print(top10_sales_products)

plt.figure(figsize=(12,6))

top10_sales_products.plot(kind="barh")

plt.title("Top 10 Products by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Product Name")

plt.tight_layout()

plt.savefig("images/top10_products_sales.png")

plt.show()
# ==========================================
# Top 10 Loss-Making Products
# ==========================================

top10_loss_products = (
    df.groupby("Product Name")["Profit"]
    .sum()
    .sort_values(ascending=True)
    .head(10)
)

print("\n========== TOP 10 LOSS-MAKING PRODUCTS ==========")
print(top10_loss_products)

plt.figure(figsize=(12,6))

top10_loss_products.plot(kind="barh", color="red")

plt.title("Top 10 Loss-Making Products")
plt.xlabel("Total Profit")
plt.ylabel("Product Name")

plt.tight_layout()

plt.savefig("images/top10_loss_products.png")

plt.show()
import seaborn as sns
# ==========================================
# Correlation Heatmap
# ==========================================

correlation = df[["Sales", "Profit", "Quantity", "Discount", "Delivery Days"]].corr()

print("\n========== CORRELATION MATRIX ==========")
print(correlation)

plt.figure(figsize=(8,6))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig("images/correlation_heatmap.png")

plt.show()
# ==========================================
# Boxplot - Sales
# ==========================================

plt.figure(figsize=(8,5))

plt.boxplot(df["Sales"])

plt.title("Boxplot of Sales")
plt.ylabel("Sales")

plt.tight_layout()

plt.savefig("images/boxplot_sales.png")

plt.show()
# ==========================================
# Boxplot - Profit
# ==========================================

plt.figure(figsize=(8,5))

plt.boxplot(df["Profit"])

plt.title("Boxplot of Profit")
plt.ylabel("Profit")

plt.tight_layout()

plt.savefig("images/boxplot_profit.png")

plt.show()
# ==========================================
# Boxplot - Discount
# ==========================================

plt.figure(figsize=(8,5))

plt.boxplot(df["Discount"])

plt.title("Boxplot of Discount")
plt.ylabel("Discount")

plt.tight_layout()

plt.savefig("images/boxplot_discount.png")

plt.show()