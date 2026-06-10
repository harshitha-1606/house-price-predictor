import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --------------------------
# 📊 Location Data (Realistic Approx)
# --------------------------

TELANGANA = {
    "Hyderabad": {"price": 9000, "growth": 0.10},
    "Rangareddy": {"price": 8500, "growth": 0.09},
    "Medchal": {"price": 8000, "growth": 0.09},
    "Warangal": {"price": 5500, "growth": 0.07},
    "Karimnagar": {"price": 5000, "growth": 0.06},
    "Khammam": {"price": 5200, "growth": 0.06},
    "Nizamabad": {"price": 4800, "growth": 0.05}
}

ANDHRA = {
    "Visakhapatnam": {"price": 8000, "growth": 0.09},
    "Vijayawada": {"price": 7000, "growth": 0.08},
    "Guntur": {"price": 6200, "growth": 0.07},
    "Tirupati": {"price": 6500, "growth": 0.08},
    "Kakinada": {"price": 5200, "growth": 0.06},
    "Rajahmundry": {"price": 5500, "growth": 0.06},
    "Nellore": {"price": 5600, "growth": 0.07},
    "Kurnool": {"price": 4800, "growth": 0.05}
}

# --------------------------
# 🎯 Title
# --------------------------

st.title("🏡 Smart House Investment Predictor")

st.write("Predict house price, future growth & investment potential 📈")

# --------------------------
# 📥 Inputs
# --------------------------

state = st.selectbox("Select State", ["Telangana", "Andhra Pradesh"])

if state == "Telangana":
    district = st.selectbox("Select District", list(TELANGANA.keys()))
    data = TELANGANA[district]
else:
    district = st.selectbox("Select District", list(ANDHRA.keys()))
    data = ANDHRA[district]

house_type = st.selectbox("House Type", ["Apartment", "Villa"])

rooms = st.slider("Number of Rooms", 1, 10, 3)
area = st.number_input("Area (sq ft)", min_value=500, max_value=5000, value=1200)

# --------------------------
# 💰 Price Calculation
# --------------------------

base_price = data["price"]
growth_rate = data["growth"]

# Adjustments
type_factor = 1.2 if house_type == "Villa" else 1.0
room_factor = 1 + (rooms * 0.05)

# Current price
current_price = area * base_price * type_factor * room_factor

# 5-year future price
future_price = current_price * ((1 + growth_rate) ** 5)

# ROI
roi = ((future_price - current_price) / current_price) * 100

# Investment score
if roi > 60:
    score = "🔥 Excellent Investment"
elif roi > 40:
    score = "👍 Good Investment"
else:
    score = "⚠️ Moderate Investment"

# --------------------------
# 📊 Output
# --------------------------

if st.button("Predict Investment"):

    st.subheader("📊 Results")

    st.write(f"📍 Location: {district}, {state}")
    st.write(f"🏠 Type: {house_type}")

    st.success(f"💰 Current Price: ₹ {current_price:,.0f}")
    st.info(f"📈 5-Year Future Price: ₹ {future_price:,.0f}")
    st.warning(f"📊 ROI: {roi:.2f}%")

    st.write(f"🏆 Investment Rating: {score}")

    # --------------------------
    # 📉 Graph
    # --------------------------

    years = [0, 1, 2, 3, 4, 5]
    prices = [current_price * ((1 + growth_rate) ** i) for i in years]

    fig, ax = plt.subplots()
    ax.plot(years, prices, marker='o')
    ax.set_title("📈 Price Growth Over 5 Years")
    ax.set_xlabel("Years")
    ax.set_ylabel("Price (₹)")

    st.pyplot(fig)
