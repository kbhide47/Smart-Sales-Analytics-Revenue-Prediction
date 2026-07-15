import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.express as px
import joblib
from database import get_connection

model = joblib.load("models/best_model.pkl")
encoder = joblib.load("models/onehot_encoder.pkl")
st.set_page_config(
    page_title="Smart Sales Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Smart Sales Analytics & Revenue Prediction System")
st.markdown(
    """
    Analyze sales performance, monitor KPIs, explore trends, and predict future sales using Machine Learning.
    """
)

st.markdown("---")
st.sidebar.markdown("---")

st.sidebar.info(
    """
    ## 📌 Dashboard Summary

    📊 Dataset : Superstore Sales

    🤖 Model : Linear Regression

    📈 Dashboard : Streamlit

    📉 Charts : Plotly

    💾 Features:
    - KPI Cards
    - Interactive Filters
    - Sales Analysis
    - Profit Analysis
    - Sales Prediction
    - Download CSV
    """
)


# Dataset path
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "best_model.pkl"
model = joblib.load(MODEL_PATH)
DATA_PATH = BASE_DIR / "data" / "cleaned" / "cleaned_superstore.csv"
conn = get_connection()

df = pd.read_sql(
    "SELECT * FROM superstore",
    conn
)

conn.close()
# ==========================
# Dashboard Filters
# ==========================
   
st.sidebar.title("📊 Dashboard Filters")

st.sidebar.markdown("---")

selected_region = st.sidebar.multiselect(
    "🌍 Select Region",
    options=sorted(df["Region"].unique()),
    default=sorted(df["Region"].unique())
)
selected_category = st.sidebar.multiselect(
    "🛍️ Select Category",
    options=sorted(df["Category"].unique()),
    default=sorted(df["Category"].unique())
)
filtered_df = df[
    (df["Region"].isin(selected_region)) &
    (df["Category"].isin(selected_category))
]
query = f"""
SELECT *
FROM superstore
WHERE Region IN ({','.join(['?'] * len(selected_region))})
AND Category IN ({','.join(['?'] * len(selected_category))})
"""

conn = get_connection()

filtered_df = pd.read_sql(
    query,
    conn,
    params=selected_region + selected_category
)

conn.close()
st.download_button(
    label="📥 Download Filtered Data",
    data=filtered_df.to_csv(index=False),
    file_name="filtered_sales_data.csv",
    mime="text/csv"
)

col1, col2, col3 = st.columns(3)

st.write(filtered_df.head())
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="💰 Total Sales",
    value=f"${filtered_df['Sales'].sum():,.2f}"
    )
    st.markdown("---")
with col2:
    st.metric(
        label="📈 Total Profit",
        value=f"${filtered_df['Profit'].sum():,.2f}"
    )
    st.markdown("---")
with col3:
    st.metric(
        label="📦 Total Orders",
        value=filtered_df["Order ID"].nunique()
    )
    st.markdown("---")

    st.info(
    f"""
    📊 Showing **{filtered_df.shape[0]}** records

    🌍 Regions Selected: **{len(selected_region)}**

    🛍️ Categories Selected: **{len(selected_category)}**
    """
)
    
with st.expander("📋 View Dataset Summary"):

    st.write("Rows:", filtered_df.shape[0])
    st.write("Columns:", filtered_df.shape[1])

    st.dataframe(filtered_df.head())

    from datetime import datetime

st.caption(
    f"🕒 Last Updated: {datetime.now().strftime('%d-%m-%Y %I:%M %p')}"
)

col1, col2 = st.columns(2)

with col1:

    st.subheader("Sales by Category")

    sales_by_category = (
        filtered_df.groupby("Category")["Sales"]
        .sum()
        .reset_index()
    )

    fig1 = px.bar(
        sales_by_category,
        x="Category",
        y="Sales",
        color="Category",
        title="💰 Sales by Category",
        template="plotly_white",
        text_auto=".2s"
    )

    fig1.update_layout(
        title_x=0.5,
        xaxis_title="Category",
        yaxis_title="Sales ($)"
    )

    st.plotly_chart(fig1, use_container_width=True)
    st.markdown("---")
# ================= Profit =================

with col2:

    st.subheader("Profit by Category")

    profit_by_category = (
        filtered_df.groupby("Category")["Profit"]
          .sum()
          .reset_index()
    )

    fig2 = px.bar(
    profit_by_category,
    x="Category",
    y="Profit",
    color="Category",
    title="📈 Profit by Category",
    template="plotly_white",
    text_auto=".2s"
)

    fig2.update_layout(
    title_x=0.5,
    xaxis_title="Category",
    yaxis_title="Profit ($)"
)

    st.plotly_chart(fig2, use_container_width=True)
    st.markdown("---")

st.subheader("Monthly Sales Trend")

# Convert Order Date to datetime
filtered_df["Order Date"] = pd.to_datetime(filtered_df["Order Date"])

# Create Month-Year column
filtered_df["Month"] = filtered_df["Order Date"].dt.to_period("M").astype(str)

monthly_sales = (
   filtered_df.groupby("Month")["Sales"]
      .sum()
      .reset_index()
)

fig3 = px.line(
    monthly_sales,
    x="Month",
    y="Sales",
    markers=True,
    title="Monthly Sales Trend"
)

st.plotly_chart(fig3, use_container_width=True)
st.markdown("---")

st.subheader("Region-wise Sales")

sales_by_region = (
    filtered_df.groupby("Region")["Sales"]
    .sum()
    .reset_index()
)

fig4 = px.bar(
    sales_by_region,
    x="Region",
    y="Sales",
    color="Region",
    title="Sales by Region"
)

st.plotly_chart(fig4, use_container_width=True)
st.markdown("---")

st.subheader("🗄️ SQL Analytics")

conn = get_connection()

top_regions = pd.read_sql(
    """
    SELECT Region,
           ROUND(SUM(Sales),2) AS Total_Sales
    FROM superstore
    GROUP BY Region
    ORDER BY Total_Sales DESC
    """,
    conn
)

conn.close()

st.dataframe(top_regions, use_container_width=True)
st.markdown("### 🏆 Top 5 Categories by Sales")

conn = get_connection()

top_categories = pd.read_sql(
    """
    SELECT Category,
           ROUND(SUM(Sales),2) AS Total_Sales
    FROM superstore
    GROUP BY Category
    ORDER BY Total_Sales DESC
    LIMIT 5
    """,
    conn
)

conn.close()

st.dataframe(top_categories, use_container_width=True)
st.markdown("### 💡 Business Insight")

conn = get_connection()

best_region = pd.read_sql(
    """
    SELECT Region,
           ROUND(SUM(Profit),2) AS Total_Profit
    FROM superstore
    GROUP BY Region
    ORDER BY Total_Profit DESC
    LIMIT 1
    """,
    conn
)

conn.close()

st.success(
    f"🏆 Most Profitable Region: {best_region.iloc[0]['Region']} "
    f"(Profit: ₹{best_region.iloc[0]['Total_Profit']:,.2f})"
)

# ==========================
# Sales & Profit by Sub-Category
# ==========================

st.markdown("---")

col3, col4 = st.columns(2)

# ---------- Sales by Sub-Category ----------

with col3:

    st.subheader("Sales by Sub-Category")

    sales_subcategory = (
        filtered_df.groupby("Sub-Category")["Sales"]
        .sum()
        .reset_index()
        .sort_values(by="Sales", ascending=False)
    )

    fig5 = px.bar(
        sales_subcategory,
        x="Sub-Category",
        y="Sales",
        color="Sales",
        title="Sales by Sub-Category"
    )

    st.plotly_chart(fig5, use_container_width=True)
    st.markdown("---")

# ---------- Profit by Sub-Category ----------

with col4:

    st.subheader("Profit by Sub-Category")

    profit_subcategory = (
        filtered_df.groupby("Sub-Category")["Profit"]
        .sum()
        .reset_index()
        .sort_values(by="Profit", ascending=False)
    )

    fig6 = px.bar(
        profit_subcategory,
        x="Sub-Category",
        y="Profit",
        color="Profit",
        title="Profit by Sub-Category"
    )

    st.plotly_chart(fig6, use_container_width=True)
    st.markdown("---")

st.subheader("Sales Distribution by Category")

category_sales = (
    filtered_df.groupby("Category")["Sales"]
    .sum()
    .reset_index()
)

fig7 = px.pie(
    category_sales,
    names="Category",
    values="Sales",
    title="Sales Distribution",
    hole=0.4
)

st.plotly_chart(fig7, use_container_width=True)
st.markdown("---")

st.subheader("Top 10 Products by Sales")

top_products = (
    filtered_df.groupby("Product Name")["Sales"]
    .sum()
    .reset_index()
    .sort_values(by="Sales", ascending=False)
    .head(10)
)

fig8 = px.bar(
    top_products,
    x="Sales",
    y="Product Name",
    orientation="h",
    color="Sales",
    title="Top 10 Products"
)

st.plotly_chart(fig8, use_container_width=True)
st.markdown("---")

st.subheader("Top 10 Loss-Making Products")

loss_products = (
    filtered_df.groupby("Product Name")["Profit"]
    .sum()
    .reset_index()
    .sort_values(by="Profit", ascending=True)
    .head(10)
)

fig9 = px.bar(
    loss_products,
    x="Profit",
    y="Product Name",
    orientation="h",
    color="Profit",
    title="Top 10 Loss-Making Products"
)

st.plotly_chart(fig9, use_container_width=True)

st.markdown("---")

st.header("📈 Model Performance")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("R² Score", "0.91")

with col2:
    st.metric("MAE", "₹245.38")

with col3:
    st.metric("RMSE", "₹412.56")
st.header("🔮 Sales Prediction")
category = st.selectbox(
    "Category",
    df["Category"].unique()
)

sub_category = st.selectbox(
    "Sub-Category",
    df["Sub-Category"].unique()
)

region = st.selectbox(
    "Region",
    df["Region"].unique()
)

quantity = st.number_input(
    "Quantity",
    min_value=1,
    value=1
)

discount = st.slider(
    "Discount",
    min_value=0.0,
    max_value=1.0,
    value=0.0,
    step=0.05
)
segment = st.selectbox(
    "Segment",
    df["Segment"].unique()
)

ship_mode = st.selectbox(
    "Ship Mode",
    df["Ship Mode"].unique()
)

delivery_days = st.number_input(
    "Delivery Days",
    min_value=1,
    value=4
)
if st.button("Predict Sales"):

    input_data = pd.DataFrame(
        {
            "Category": [category],
            "Sub-Category": [sub_category],
            "Region": [region],
            "Segment": [segment],
            "Ship Mode": [ship_mode],
            "Quantity": [quantity],
            "Discount": [discount],
            "Delivery Days": [delivery_days]
        }
    )

    # Separate categorical and numerical columns
    categorical_cols = [
        "Category",
        "Sub-Category",
        "Region",
        "Segment",
        "Ship Mode"
    ]

    numerical_cols = [
        "Quantity",
        "Discount",
        "Delivery Days"
    ]


    # One hot encode categorical data
    encoded_data = encoder.transform(
        input_data[categorical_cols]
    )


    # Convert encoded array into dataframe
    encoded_df = pd.DataFrame(
        encoded_data,
        columns=encoder.get_feature_names_out(categorical_cols)
    )


    # Combine numerical + encoded features
    final_input = pd.concat(
        [
            input_data[numerical_cols].reset_index(drop=True),
            encoded_df.reset_index(drop=True)
        ],
        axis=1
    )


    prediction = model.predict(final_input)


    st.success(
        f"Predicted Sales: ₹ {prediction[0]:,.2f}"
    )
st.markdown("---")

st.markdown(
    """
    <div style='text-align:center; color:gray;'>
        📊 Smart Sales Analytics & Revenue Prediction System <br>
        Developed by <b>Kasturi Bhide</b> using Python, Streamlit, Plotly & Machine Learning
    </div>
    """,
    unsafe_allow_html=True
)