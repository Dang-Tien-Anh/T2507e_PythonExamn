import pandas as pd

data = {
    "id": [1, 2, 3, 4, 5],
    "name": ["Laptop", "Phone", "Keyboard", "Monitor", "Mouse"],
    "price": [120, 23, 44, 289, 67],
    "quantity": [24, 35, 123, 7848, 50]
}
df = pd.DataFrame(data)

df.to_csv("products.csv", index=False)

df = pd.read_csv("products.csv")
print("\nAll Products:")
print(df)

print("\nProducts with price > 100:")
print(df[df["price"] > 100])

total_value = (df["price"] * df["quantity"]).sum()
print("\nTotal inventory value:", total_value)

df["total"] = df["price"] * df["quantity"]
print("\nProducts with total column:")
print(df)
