import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# App Title
st.title("Individual Supply and Demand Market")

# Input sliders for demand and supply equations
st.sidebar.header("Model Parameters")
a = st.sidebar.slider("Demand Intercept (a)", 0, 1000, 500)
b = st.sidebar.slider("Demand Slope (b)", 1, 100, 50)
c = st.sidebar.slider("Supply Intercept (c)", 0, 1000, 100)
d = st.sidebar.slider("Supply Slope (d)", 1, 100, 20)

# Calculate equilibrium price and quantity
equilibrium_price = (a - c) / (b + d)
equilibrium_quantity = a - b * equilibrium_price

# Generate data points for demand and supply curves
price_range = np.linspace(0, 100, 100)
demand = a - b * price_range
supply = c + d * price_range

# Plot the supply and demand curves
plt.figure(figsize=(8, 6))
plt.plot(price_range, demand, label="Demand Curve", color="blue")
plt.plot(price_range, supply, label="Supply Curve", color="red")
plt.axvline(x=equilibrium_price, color="green", linestyle="--", label="Equilibrium Price")
plt.axhline(y=equilibrium_quantity, color="black", linestyle="--", label="Equilibrium Quantity")
plt.title("Supply and Demand Model")
plt.xlabel("Price")
plt.ylabel("Quantity")
plt.legend()
plt.grid()

# Display plot
st.pyplot(plt)

# Display equilibrium results
st.subheader("Equilibrium Results")
st.write(f"**Equilibrium Price ($):** {equilibrium_price:.2f}")
st.write(f"**Equilibrium Quantity:** {equilibrium_quantity:.2f}")
