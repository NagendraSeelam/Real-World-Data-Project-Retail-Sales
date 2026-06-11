import pandas as pd
import matplotlib.pyplot as plt

# Sample Retail Dataset
data = {
    "Product": ["Laptop", "Phone", "Tablet", "Headphones", "Smartwatch"],
    "Sales": [50000, 35000, 20000, 15000, 18000]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

print("\nStatistical Summary:")
print(df.describe())

# Visualization
plt.figure(figsize=(6,4))
plt.bar(df["Product"], df["Sales"])
plt.title("Retail Product Sales")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.savefig("retail_sales.png")
plt.show()

# Top Product
top_product = df.loc[df["Sales"].idxmax()]

print("\nBest Selling Product:")
print(top_product)
