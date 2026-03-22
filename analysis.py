import pandas as pd

data = {
    "Product": ["Laptop", "Mobile", "Headphones"],
    "Quantity": [2, 5, 10],
    "Price": [50000, 20000, 2000]
}

df = pd.DataFrame(data)

df["Revenue"] = df["Quantity"] * df["Price"]

print(df)
print("Total Revenue:", df["Revenue"].sum())
