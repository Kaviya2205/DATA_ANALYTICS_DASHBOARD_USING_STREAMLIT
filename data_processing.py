import pandas as pd

def load_data():
    df = pd.read_csv("data/sales_data.csv")  # Replace with your dataset
    df["Date"] = pd.to_datetime(df["Date"])  # Ensure date format
    df["Revenue"] = df["Quantity"] * df["Price"]  # Create a new column
    return df

if __name__ == "__main__":
    data = load_data()
    print(data.head())
