import matplotlib.pyplot as plt
import seaborn as sns

def plot_sales_trend(df):
    plt.figure(figsize=(10, 5))
    df.groupby(df["Date"].dt.to_period("M"))["Revenue"].sum().plot(kind="line", marker="o", color="b")
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Revenue ($)")
    plt.grid()
    return plt

def plot_top_products(df):
    plt.figure(figsize=(10, 5))
    top_products = df.groupby("Product")["Revenue"].sum().nlargest(5)
    sns.barplot(x=top_products.index, y=top_products.values, palette="viridis")
    plt.title("Top 5 Best-Selling Products")
    plt.ylabel("Total Revenue ($)")
    return plt
