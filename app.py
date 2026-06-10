import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Title
st.title("🏠 Smart House Price Predictor")

st.write("Enter details below:")

# Inputs
rooms = st.slider("Number of Rooms", 1, 10, 3)
house_type = st.selectbox("House Type", ["Apartment", "Villa"])

# Load dataset
url = "https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv"
df = pd.read_csv(url)

X = df.drop("medv", axis=1)
y = df["medv"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Backend logic
crim = 0.1
zn = 0
indus = 10
chas = 1 if house_type == "Villa" else 0
nox = 0.5
age = 60
dis = 4
rad = 4
tax = 300
ptratio = 15
b = 390
lstat = 10

if st.button("Predict Price"):

    user_data = pd.DataFrame([[crim, zn, indus, chas, nox, rooms, age, dis, rad, tax, ptratio, b, lstat]],
                             columns=X.columns)

    prediction = model.predict(user_data)[0]

    # Broker price
    broker_price = prediction * 1.15

    # Adjusted price
    adjusted_price = prediction * (1.1 if house_type == "Villa" else 0.95)

    st.subheader("Results")
    st.write(f"💰 Actual Price: {prediction:.2f}")
    st.write(f"🏢 Broker Price: {broker_price:.2f}")
    st.write(f"🌍 Adjusted Price: {adjusted_price:.2f}")

    # Graph
    labels = ["Actual", "Broker", "Adjusted"]
    values = [prediction, broker_price, adjusted_price]

    fig, ax = plt.subplots()
    ax.bar(labels, values)
    ax.set_title("Price Comparison")

    st.pyplot(fig) 
