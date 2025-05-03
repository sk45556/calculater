import streamlit as st

# Page configuration
st.set_page_config(page_title="Stylish Calculator", page_icon="🧮", layout="centered")

# Title and description
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🧮 Stylish Calculator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Enter two numbers to see the results of basic arithmetic operations.</p>", unsafe_allow_html=True)
st.markdown("---")

# Input section with columns
col1, col2 = st.columns(2)
with col1:
    number1 = st.number_input("🔢 Enter your first number", value=0.0, format="%.2f")
with col2:
    number2 = st.number_input("🔢 Enter your second number", value=1.0, format="%.2f")

# Divider
st.markdown("---")

# Results section
st.markdown("### ➗ Results")

st.success(f"✅ **Addition**: {number1} + {number2} = {number1 + number2}")
st.info(f"✅ **Subtraction**: {number1} - {number2} = {number1 - number2}")
st.warning(f"✅ **Multiplication**: {number1} × {number2} = {number1 * number2}")

if number2 != 0:
    st.error(f"✅ **Division**: {number1} ÷ {number2} = {number1 / number2:.2f}")
else:
    st.error("❌ **Division**: Cannot divide by zero")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 0.9em;'>Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)
