#Install MatPlotLib library. Draw basic graphs for sales dataset using MatPlotLib

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# STEP 1: Load Dataset
# -----------------------------
# Replace with your file path
df = pd.read_csv('sales_data.csv')

# Display first few rows
print(df.head())

# -----------------------------
# STEP 2: Data Preprocessing
# -----------------------------
# Convert Order Date to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Create new columns
df['Month'] = df['Order Date'].dt.month
df['Sales'] = df['Quantity Ordered'] * df['Price Each']

# -----------------------------
# STEP 3: GRAPH 1 - Monthly Sales (Line Chart)
# -----------------------------
monthly_sales = df.groupby('Month')['Sales'].sum()

plt.figure()
plt.plot(monthly_sales.index, monthly_sales.values, marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid()
plt.show()

# -----------------------------
# STEP 4: GRAPH 2 - Sales by Product (Bar Chart)
# -----------------------------
product_sales = df.groupby('Product')['Sales'].sum()

plt.figure()
product_sales.plot(kind='bar')
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.show()

# -----------------------------
# STEP 5: GRAPH 3 - Quantity Distribution (Histogram)
# -----------------------------
plt.figure()
plt.hist(df['Quantity Ordered'], bins=10)
plt.title("Quantity Distribution")
plt.xlabel("Quantity Ordered")
plt.ylabel("Frequency")
plt.show()

# -----------------------------
# STEP 6: GRAPH 4 - Sales Share (Pie Chart)
# -----------------------------
plt.figure()
product_sales.head(5).plot(kind='pie', autopct='%1.1f%%')
plt.title("Top 5 Products Sales Share")
plt.ylabel("")
plt.show()

# -----------------------------
# STEP 7: GRAPH 5 - Price vs Quantity (Scatter Plot)
# -----------------------------
plt.figure()
plt.scatter(df['Price Each'], df['Quantity Ordered'])
plt.title("Price vs Quantity")
plt.xlabel("Price")
plt.ylabel("Quantity")
plt.show()

print("\n===== GRAPHS GENERATED SUCCESSFULLY =====")

