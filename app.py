import streamlit as st

# Conversion Factors
conversion_factors = {
    "Length": {
        "meter": {"kilometer": 0.001, "mile": 0.000621371, "yard": 1.09361, "foot": 3.28084, "inch": 39.3701},
        "kilometer": {"meter": 1000, "mile": 0.621371, "yard": 1093.61, "foot": 3280.84, "inch": 39370.1},
    },
    "Weight": {
        "gram": {"kilogram": 0.001, "pound": 0.00220462, "ounce": 0.035274},
        "kilogram": {"gram": 1000, "pound": 2.20462, "ounce": 35.274},
    },
    "Temperature": {
        "celsius": {"fahrenheit": lambda c: (c * 9/5) + 32, "kelvin": lambda c: c + 273.15},
        "fahrenheit": {"celsius": lambda f: (f - 32) * 5/9, "kelvin": lambda f: (f - 32) * 5/9 + 273.15},
        "kelvin": {"celsius": lambda k: k - 273.15, "fahrenheit": lambda k: (k - 273.15) * 9/5 + 32},
    }
}

# Streamlit UI
st.title("🔄 Simple Unit Converter")

# Select category
category = st.selectbox("Select Category", list(conversion_factors.keys()))

# Select units
units = list(conversion_factors[category].keys())
from_unit = st.selectbox("From", units)
to_unit = st.selectbox("To", units)

# Input value
value = st.number_input("Enter Value", value=1.0)

# Convert
if st.button("Convert"):
    if category == "Temperature":
        conversion_func = conversion_factors[category][from_unit].get(to_unit)
        result = conversion_func(value) if conversion_func else "Invalid Conversion"
    else:
        result = value * conversion_factors[category][from_unit].get(to_unit, 1)
    
    st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")