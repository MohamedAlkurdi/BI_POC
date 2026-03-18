import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Shop Financial Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

#  Embedded sample data (from actual client files) 

ORDERS_DATA = [
    {"order_no": "#2791", "product": "Amazing Yamaguchi Ted 2 - 10cm", "supplier": "AliExpress", "fulfillment": "DSers", "revenue": 51.29, "cogs": 23.04, "shipping": 0.00, "tax": 3.84, "status": "Fulfilled", "date": "2025-01-01", "track_service": "CAINIAO_STANDARD", "freight_days": 7},
    {"order_no": "#2793", "product": "Anime Figure – Attack on Titan", "supplier": "AliExpress", "fulfillment": "DSers", "revenue": 16.97, "cogs": 9.76, "shipping": 1.99, "tax": 0.56, "status": "Fulfilled", "date": "2025-01-03", "track_service": "CAINIAO_STANDARD", "freight_days": 9},
    {"order_no": "#2795", "product": "One Piece Luffy Figure 15cm", "supplier": "AliExpress", "fulfillment": "DSers", "revenue": 35.46, "cogs": 20.90, "shipping": 6.95, "tax": 0.00, "status": "Fulfilled", "date": "2025-01-05", "track_service": "YANWEN", "freight_days": 14},
    {"order_no": "#2801", "product": "Demon Slayer Tanjiro Figure", "supplier": "AliExpress", "fulfillment": "EPROLO", "revenue": 42.00, "cogs": 18.50, "shipping": 3.20, "tax": 1.20, "status": "Fulfilled", "date": "2025-01-08", "track_service": "YANWEN", "freight_days": 12},
    {"order_no": "#2804", "product": "Naruto Sage Mode Figure", "supplier": "AliExpress", "fulfillment": "EPROLO", "revenue": 38.99, "cogs": 17.30, "shipping": 4.10, "tax": 1.10, "status": "Fulfilled", "date": "2025-01-10", "track_service": "CAINIAO_STANDARD", "freight_days": 8},
    {"order_no": "#2810", "product": "My Hero Academia – Deku Figure", "supplier": "AliExpress", "fulfillment": "EPROLO", "revenue": 29.99, "cogs": 13.40, "shipping": 2.80, "tax": 0.90, "status": "Fulfilled", "date": "2025-01-14", "track_service": "YANWEN", "freight_days": 11},
    {"order_no": "#2815", "product": "Dragon Ball Z – Goku SSJ4", "supplier": "AliExpress", "fulfillment": "Buckydrop", "revenue": 55.00, "cogs": 24.00, "shipping": 5.50, "tax": 1.65, "status": "Fulfilled", "date": "2025-01-18", "track_service": "4PX", "freight_days": 10},
    {"order_no": "#2820", "product": "Spy x Family – Anya Plush", "supplier": "AliExpress", "fulfillment": "Buckydrop", "revenue": 22.50, "cogs": 9.80, "shipping": 2.10, "tax": 0.68, "status": "Fulfilled", "date": "2025-01-22", "track_service": "4PX", "freight_days": 9},
    {"order_no": "#2828", "product": "Jujutsu Kaisen – Gojo Figure", "supplier": "AliExpress", "fulfillment": "Buckydrop", "revenue": 48.00, "cogs": 21.50, "shipping": 4.80, "tax": 1.44, "status": "Fulfilled", "date": "2025-01-26", "track_service": "4PX", "freight_days": 8},
    {"order_no": "#2835", "product": "Chainsaw Man – Denji Figure", "supplier": "AliExpress", "fulfillment": "Buckydrop", "revenue": 44.00, "cogs": 19.20, "shipping": 3.90, "tax": 1.32, "status": "Fulfilled", "date": "2025-02-01", "track_service": "4PX", "freight_days": 7},
    {"order_no": "#2840", "product": "One Piece Zoro Three Swords", "supplier": "AliExpress", "fulfillment": "DSers", "revenue": 39.00, "cogs": 17.00, "shipping": 3.50, "tax": 1.17, "status": "Fulfilled", "date": "2025-02-05", "track_service": "CAINIAO_STANDARD", "freight_days": 10},
    {"order_no": "#2847", "product": "Bleach – Ichigo Hollow Mask", "supplier": "AliExpress", "fulfillment": "Buckydrop", "revenue": 50.00, "cogs": 22.00, "shipping": 5.00, "tax": 1.50, "status": "Fulfilled", "date": "2025-02-10", "track_service": "4PX", "freight_days": 8},
    {"order_no": "#2853", "product": "Evangelion – Rei Ayanami Figure", "supplier": "AliExpress", "fulfillment": "Buckydrop", "revenue": 46.00, "cogs": 20.50, "shipping": 4.60, "tax": 1.38, "status": "Fulfilled", "date": "2025-02-15", "track_service": "4PX", "freight_days": 7},
    {"order_no": "#2858", "product": "Haikyuu – Hinata Figure", "supplier": "AliExpress", "fulfillment": "Buckydrop", "revenue": 33.00, "cogs": 14.80, "shipping": 3.30, "tax": 0.99, "status": "Fulfilled", "date": "2025-02-20", "track_service": "4PX", "freight_days": 9},
    {"order_no": "#2864", "product": "Vinland Saga – Thorfinn", "supplier": "AliExpress", "fulfillment": "Buckydrop", "revenue": 41.00, "cogs": 18.40, "shipping": 4.10, "tax": 1.23, "status": "Fulfilled", "date": "2025-02-25", "track_service": "4PX", "freight_days": 8},
    {"order_no": "#2870", "product": "Blue Lock – Isagi Figure", "supplier": "AliExpress", "fulfillment": "Buckydrop", "revenue": 36.00, "cogs": 16.20, "shipping": 3.60, "tax": 1.08, "status": "Fulfilled", "date": "2025-03-01", "track_service": "4PX", "freight_days": 7},
    {"order_no": "#2876", "product": "Frieren – Frieren Figure", "supplier": "AliExpress", "fulfillment": "Buckydrop", "revenue": 52.00, "cogs": 23.40, "shipping": 5.20, "tax": 1.56, "status": "Fulfilled", "date": "2025-03-05", "track_service": "4PX", "freight_days": 8},
    {"order_no": "#2882", "product": "Sword Art Online – Asuna", "supplier": "AliExpress", "fulfillment": "EPROLO", "revenue": 37.00, "cogs": 16.60, "shipping": 3.70, "tax": 1.11, "status": "Cancelled", "date": "2025-03-08", "track_service": "-", "freight_days": 0},
    {"order_no": "#2888", "product": "Made in Abyss – Nanachi", "supplier": "AliExpress", "fulfillment": "Buckydrop", "revenue": 30.00, "cogs": 13.50, "shipping": 3.00, "tax": 0.90, "status": "Fulfilled", "date": "2025-03-10", "track_service": "4PX", "freight_days": 7},
    {"order_no": "#2894", "product": "Re:Zero – Rem Figure", "supplier": "AliExpress", "fulfillment": "Buckydrop", "revenue": 59.99, "cogs": 27.00, "shipping": 6.00, "tax": 1.80, "status": "Fulfilled", "date": "2025-03-14", "track_service": "4PX", "freight_days": 8},
]

TRANSACTIONS_DATA = [
    {"type": "Balance Recharge", "amount_usd": 160.53, "method": "PayPal", "date": "2026-03-12", "description": "Balance Recharge"},
    {"type": "Order Payment", "amount_usd": -25.20, "method": "Balance", "date": "2026-03-13", "description": "Payment for Procured Goods #8052"},
    {"type": "Service Fee", "amount_usd": -0.34, "method": "Balance", "date": "2026-03-13", "description": "Procurement Service Fee #8052"},
    {"type": "Order Payment", "amount_usd": -18.90, "method": "Balance", "date": "2026-03-14", "description": "Payment for Procured Goods #8053"},
    {"type": "Balance Recharge", "amount_usd": 80.00, "method": "PayPal", "date": "2026-03-15", "description": "Balance Recharge"},
    {"type": "Order Payment", "amount_usd": -33.50, "method": "Balance", "date": "2026-03-15", "description": "Payment for Procured Goods #8054"},
    {"type": "Refund", "amount_usd": 12.00, "method": "Balance", "date": "2026-03-16", "description": "Refund – Cancelled Order #8049"},
]

df = pd.DataFrame(ORDERS_DATA)
df["date"] = pd.to_datetime(df["date"])
df["profit"] = df["revenue"] - df["cogs"] - df["shipping"] - df["tax"]
df["margin_pct"] = (df["profit"] / df["revenue"] * 100).round(1)
df["month"] = df["date"].dt.to_period("M").astype(str)

df_tx = pd.DataFrame(TRANSACTIONS_DATA)
df_tx["date"] = pd.to_datetime(df_tx["date"])

#  Sidebar 
with st.sidebar:
    st.image("https://img.icons8.com/fluency/48/combo-chart.png", width=40)
    st.title("Dashboard Controls")
    st.markdown("---")

    fulfillment_options = ["All"] + sorted(df["fulfillment"].unique().tolist())
    selected_fulfillment = st.selectbox("📦 Fulfillment Service", fulfillment_options)

    status_options = ["All", "Fulfilled", "Cancelled"]
    selected_status = st.selectbox("🔖 Order Status", status_options)

    min_date = df["date"].min().date()
    max_date = df["date"].max().date()
    date_range = st.date_input("📅 Date Range", value=(min_date, max_date), min_value=min_date, max_value=max_date)

    st.markdown("---")
    st.caption("📌 Sample Data — POC Demo")
    st.caption("Real data integration coming in MVP phase.")

#  Filter data 
filtered = df.copy()
if selected_fulfillment != "All":
    filtered = filtered[filtered["fulfillment"] == selected_fulfillment]
if selected_status != "All":
    filtered = filtered[filtered["status"] == selected_status]
if len(date_range) == 2:
    filtered = filtered[(filtered["date"].dt.date >= date_range[0]) & (filtered["date"].dt.date <= date_range[1])]

fulfilled = filtered[filtered["status"] == "Fulfilled"]

#  Header 
st.title("📊 Shop Financial Dashboard")
st.caption("Proof of Concept · Sample Data Only · Built with Streamlit")
st.markdown("---")

#  KPI Cards 
col1, col2, col3, col4, col5 = st.columns(5)

total_revenue   = fulfilled["revenue"].sum()
total_cogs      = fulfilled["cogs"].sum()
total_shipping  = fulfilled["shipping"].sum()
total_tax       = fulfilled["tax"].sum()
total_profit    = fulfilled["profit"].sum()
avg_margin      = fulfilled["margin_pct"].mean() if len(fulfilled) > 0 else 0
num_orders      = len(fulfilled)
avg_freight     = fulfilled[fulfilled["freight_days"] > 0]["freight_days"].mean()

col1.metric("💰 Revenue", f"${total_revenue:,.2f}")
col2.metric("📦 COGS", f"${total_cogs:,.2f}")
col3.metric("🚚 Shipping Costs", f"${total_shipping:,.2f}")
col4.metric("✅ Net Profit", f"${total_profit:,.2f}", delta=f"{avg_margin:.1f}% margin")
col5.metric("🛒 Orders", f"{num_orders}", delta=f"Avg {avg_freight:.1f}d delivery" if avg_freight > 0 else None)

st.markdown("---")

#  Row 1: Profit Over Time + Cost Breakdown 
col_left, col_right = st.columns([2, 1])

with col_left:
    st.subheader("📈 Revenue & Profit by Month")
    monthly = fulfilled.groupby("month").agg(
        Revenue=("revenue", "sum"),
        COGS=("cogs", "sum"),
        Shipping=("shipping", "sum"),
        Tax=("tax", "sum"),
        Profit=("profit", "sum"),
    ).reset_index()

    fig = go.Figure()
    fig.add_bar(name="COGS", x=monthly["month"], y=monthly["COGS"], marker_color="#EF5350")
    fig.add_bar(name="Shipping", x=monthly["month"], y=monthly["Shipping"], marker_color="#FF7043")
    fig.add_bar(name="Tax", x=monthly["month"], y=monthly["Tax"], marker_color="#FFA726")
    fig.add_bar(name="Profit", x=monthly["month"], y=monthly["Profit"], marker_color="#66BB6A")
    fig.update_layout(barmode="stack", height=320, margin=dict(t=10, b=10), legend=dict(orientation="h"))
    st.plotly_chart(fig, use_container_width=True)

with col_right:
    st.subheader("🥧 Cost Breakdown")
    labels = ["COGS", "Shipping", "Tax", "Profit"]
    values = [total_cogs, total_shipping, total_tax, total_profit]
    colors = ["#EF5350", "#FF7043", "#FFA726", "#66BB6A"]
    fig2 = go.Figure(go.Pie(labels=labels, values=values, hole=0.45,
                             marker=dict(colors=colors)))
    fig2.update_layout(height=320, margin=dict(t=10, b=10), showlegend=True,
                       legend=dict(orientation="h"))
    st.plotly_chart(fig2, use_container_width=True)

#  Row 2: Fulfillment breakdown + Margin per product 
col_a, col_b = st.columns(2)

with col_a:
    st.subheader("🏭 Profit by Fulfillment Service")
    by_ff = fulfilled.groupby("fulfillment").agg(
        Profit=("profit", "sum"),
        Orders=("order_no", "count"),
        Avg_Margin=("margin_pct", "mean")
    ).reset_index().sort_values("Profit", ascending=True)

    fig3 = px.bar(by_ff, x="Profit", y="fulfillment", orientation="h",
                  color="Avg_Margin", color_continuous_scale="RdYlGn",
                  labels={"fulfillment": "Service", "Avg_Margin": "Avg Margin %"},
                  height=300)
    fig3.update_layout(margin=dict(t=10, b=10), coloraxis_colorbar=dict(title="Margin %"))
    st.plotly_chart(fig3, use_container_width=True)

with col_b:
    st.subheader("📦 Top Products by Profit")
    top_products = fulfilled.groupby("product").agg(
        Profit=("profit", "sum"),
        Orders=("order_no", "count"),
    ).reset_index().sort_values("Profit", ascending=False).head(8)

    fig4 = px.bar(top_products, x="Profit", y="product", orientation="h",
                  color="Profit", color_continuous_scale="Blues",
                  height=300)
    fig4.update_layout(margin=dict(t=10, b=10), showlegend=False,
                       coloraxis_showscale=False,
                       yaxis=dict(tickfont=dict(size=10)))
    st.plotly_chart(fig4, use_container_width=True)

#  Row 3: Order Table (drilldown) 
st.markdown("---")
st.subheader("🔍 Order-Level Drilldown")

sort_col = st.selectbox("Sort by", ["date", "revenue", "profit", "margin_pct", "freight_days"], index=1)
show_df = fulfilled[["order_no", "date", "product", "fulfillment", "revenue",
                      "cogs", "shipping", "tax", "profit", "margin_pct", "freight_days",
                      "track_service", "status"]].sort_values(sort_col, ascending=False)

show_df.columns = ["Order", "Date", "Product", "Fulfillment", "Revenue ($)",
                   "COGS ($)", "Shipping ($)", "Tax ($)", "Profit ($)", "Margin (%)",
                   "Freight Days", "Carrier", "Status"]

st.dataframe(
    show_df.style
        .format({"Revenue ($)": "${:.2f}", "COGS ($)": "${:.2f}",
                 "Shipping ($)": "${:.2f}", "Tax ($)": "${:.2f}",
                 "Profit ($)": "${:.2f}", "Margin (%)": "{:.1f}%"}),
    use_container_width=True,
    height=320
)

#  Row 4: Transactions 
st.markdown("---")
st.subheader("💳 Buckydrop Transaction Statement (Sample)")

col_t1, col_t2 = st.columns([2, 1])
with col_t1:
    st.dataframe(df_tx[["date", "type", "description", "amount_usd", "method"]].rename(columns={
        "date": "Date", "type": "Type", "description": "Description",
        "amount_usd": "Amount (USD)", "method": "Payment Method"
    }).style.format({"Amount (USD)": "${:+.2f}"}), use_container_width=True, height=280)

with col_t2:
    balance = df_tx["amount_usd"].sum()
    total_recharge = df_tx[df_tx["amount_usd"] > 0]["amount_usd"].sum()
    total_spent = abs(df_tx[df_tx["amount_usd"] < 0]["amount_usd"].sum())

    st.metric("💳 Current Balance", f"${balance:,.2f}")
    st.metric("⬆️ Total Recharged", f"${total_recharge:,.2f}")
    st.metric("⬇️ Total Spent", f"${total_spent:,.2f}")

#  Footer 
st.markdown("---")
st.caption("🔒 This is a proof-of-concept demo using embedded sample data. The full MVP will support live data upload from DSers, EPROLO, and Buckydrop exports.")