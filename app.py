import joblib
import numpy as np
import streamlit as st

model = joblib.load('house_price_model.pkl')
columns = joblib.load('columns.pkl')

st.title("🏠 House Price Predictor")

area = st.number_input("Total Area (in sqft):")
bhk = st.selectbox("BHK:", [1, 2, 3, 4, 5])
location = st.selectbox("Location:", ['Indira Nagar', 'Whitefield', 'HSR Layout', 'Marathahalli', 'other'])

if st.button("Predict Price"):
    x_input = np.zeros(len(columns))
    x_input[columns.index('total_sqft')] = area
    x_input[columns.index('bhk')] = bhk

    loc_col = f'location_{location}'
    if loc_col in columns:
        x_input[columns.index(loc_col)] = 1

    prediction = model.predict([x_input])[0]
    st.success(f"Estimated Price: ₹ {round(prediction, 2)} Lakhs")
