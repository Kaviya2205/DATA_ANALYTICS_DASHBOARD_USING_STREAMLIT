import streamlit as st
import pandas as pd
import visualizations as vz
from data_processing import load_data

# Load Data
df = load_data()

# Sidebar Filters
st.sidebar.header("Filters")
date_range = st.sidebar.date_input("Select Date Range", [df["Date"].min(), df["Date"].max()])
filtered_df = df[(df["Date"] >= pd.to_datetime(date_range[0])) & (df["Date"] <= pd.to_datetime(date_range[1]))]

# Dashboard Title
st.title("📊 Data Analytics Dashboard")
st.subheader("Explore Sales & Financial Data Trends")

# Display Data Summary
st.write("### Dataset Preview", filtered_df.head())

# Revenue Trend
st.write("### Sales Trend Over Time")
st.pyplot(vz.plot_sales_trend(filtered_df))

# Top-Selling Products
st.write("### Top 5 Best-Selling Products")
st.pyplot(vz.plot_top_products(filtered_df))

# Summary Metrics
st.write("### Key Metrics")
total_revenue = filtered_df["Revenue"].sum()
total_orders = filtered_df.shape[0]
st.metric(label="Total Revenue", value=f"${total_revenue:,.2f}")
st.metric(label="Total Orders", value=total_orders)
