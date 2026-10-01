import os
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="E-Commerce Sales & RFM Analytics",
    page_icon="🛒",
    layout="wide",
)

st.title("🛒 E-Commerce Sales & Customer Analytics Dashboard")
st.markdown(
    "Interactive business dashboard built on cleaned transnational retail"
    " transaction data."
)


@st.cache_data
def load_data():
  file_candidates = [
      "ecommerce_cleaned_data.csv",
      os.path.join("sql_sheet", "ecommerce_cleaned_data.csv"),
      os.path.join(
          os.path.expanduser("~"), "Desktop", "ecommerce_cleaned_data.csv"
      ),
      os.path.join(
          os.path.expanduser("~"),
          "OneDrive",
          "Desktop",
          "ecommerce_cleaned_data.csv",
      ),
  ]

  for path in file_candidates:
    if os.path.exists(path):
      data = pd.read_csv(path)

      # Auto-calculate TotalSpend if not present
      if "TotalSpend" not in data.columns:
        if "Quantity" in data.columns and "UnitPrice" in data.columns:
          data["TotalSpend"] = data["Quantity"] * data["UnitPrice"]

      # Auto-extract Hour safely
      if "Hour" not in data.columns and "InvoiceDate" in data.columns:
        data["InvoiceDate"] = pd.to_datetime(data["InvoiceDate"])
        data["Hour"] = data["InvoiceDate"].dt.hour

      return data
  return None


df = load_data()

if df is None:
  st.error("❌ 'ecommerce_cleaned_data.csv' file load nahi ho saki.")
else:
  # Sidebar Filters
  st.sidebar.header("Filter Options")
  all_countries = ["All"] + sorted(df["Country"].dropna().unique().tolist())
  selected_country = st.sidebar.selectbox("Select Country:", all_countries)

  filtered_df = (
      df if selected_country == "All" else df[df["Country"] == selected_country]
  )

  # Top Metric Cards (KPIs)
  spend_col = "TotalSpend" if "TotalSpend" in filtered_df.columns else "Quantity"
  total_revenue = filtered_df[spend_col].sum()
  total_orders = filtered_df["InvoiceNo"].nunique()
  total_customers = (
      filtered_df["CustomerID"].nunique()
      if "CustomerID" in filtered_df.columns
      else 0
  )
  avg_order_value = total_revenue / total_orders if total_orders > 0 else 0

  kpi1, kpi2, kpi3, kpi4 = st.columns(4)
  kpi1.metric("Total Revenue", f"${total_revenue:,.2f}")
  kpi2.metric("Total Invoices", f"{total_orders:,}")
  kpi3.metric("Unique Buyers", f"{total_customers:,}")
  kpi4.metric("Avg Order Value", f"${avg_order_value:,.2f}")

  st.markdown("---")

  # Visualizations Row 1
  col1, col2 = st.columns(2)

  with col1:
    st.subheader("Top 10 Countries by Total Revenue")
    country_rev = (
        df.groupby("Country")[spend_col]
        .sum()
        .reset_index()
        .sort_values(by=spend_col, ascending=False)
        .head(10)
    )
    fig_bar = px.bar(
        country_rev,
        x=spend_col,
        y="Country",
        orientation="h",
        color=spend_col,
        color_continuous_scale="Blues",
        labels={spend_col: "Revenue ($)", "Country": "Country"},
    )
    fig_bar.update_layout(yaxis={"categoryorder": "total ascending"})
    st.plotly_chart(fig_bar, use_container_width=True)

  with col2:
    st.subheader("Peak Purchasing Hours")
    if "Hour" in filtered_df.columns:
      hourly_trend = (
          filtered_df.groupby("Hour")["InvoiceNo"].nunique().reset_index()
      )
      fig_line = px.line(
          hourly_trend,
          x="Hour",
          y="InvoiceNo",
          markers=True,
          labels={"Hour": "Hour of Day (24-hr)", "InvoiceNo": "Orders Placed"},
      )
      fig_line.update_traces(line_color="#004B91")
      st.plotly_chart(fig_line, use_container_width=True)
    else:
      st.info("Hour data unavailable for time trends.")

  # Visualizations Row 2
  if "Description" in filtered_df.columns:
    st.subheader("Top 10 Best-Selling Products by Revenue")
    top_products = (
        filtered_df.groupby("Description")[spend_col]
        .sum()
        .reset_index()
        .sort_values(by=spend_col, ascending=False)
        .head(10)
    )
    fig_prod = px.bar(
        top_products,
        x=spend_col,
        y="Description",
        orientation="h",
        color=spend_col,
        color_continuous_scale="Viridis",
        labels={spend_col: "Sales ($)", "Description": "Product"},
    )
    fig_prod.update_layout(yaxis={"categoryorder": "total ascending"})
    st.plotly_chart(fig_prod, use_container_width=True)
      
