import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open('crop_yield_diseases.pkl', 'rb') as f:
    pipe= pickle.load(f)

st.title("🌾 Crop Yield Prediction App")

st.write("Enter the crop details to predict expected yield (in quintals/hectare).")


col1, col2 = st.columns(2)

with col1:
  State = st.selectbox("🏞️  State", ["Uttar Pradesh", "Gujarat", "Karnataka", "Punjab", "Maharashtra"])
  District =st.selectbox("🏛️ District",["Lucknow", "Ahmedabad", "Ludhiana", "Nashik", "Bengaluru"])
  Crop = st.selectbox("🌱 Crop", ["Rice", "Wheat", "Maize", "Sugarcane", "Cotton"])
  Season =st.selectbox("📍 Season",["Kharif", "Rabi"])
  Soil_Type = st.selectbox("🧪 Soil Type", ["Loamy", "Sandy", "Clay"])
  Temperature = st.number_input("🌡️ Temperature (°C)", min_value=0, max_value=50, value=28)
  


with col2:
  Fertilizer_Used = st.number_input("🌿 Fertilizer Used",min_value=0, max_value=50, value=28)
  Pesticide_Used =st.number_input("🧴	Pesticide Used ", min_value=0, max_value=10, value=1)
  Disease_Type =st.selectbox("⚠️ Disease Type",["Nan", "Rust","Blight"])
  Rainfall = st.number_input("🌧️ Rainfall (mm)", min_value=0, max_value=1000, value=300, step=10)
  Crop_yield=st.number_input("🧴	 Crop yield ", min_value=0, max_value=10, value=1)

if st.button("Predict Premium"):
    # Build a single‑row DataFrame in the column order expected by your pipeline
    input_df = pd.DataFrame({
    'State': [State],
    'District': [District],
    'Crop': [Crop],
    'Season': [Season],
    'Soil_Type': [Soil_Type],
    'Temperature': [Temperature],
    'Rainfall': [Rainfall],
    'Fertilizer_Used': [Fertilizer_Used],
    'Pesticide_Used': [Pesticide_Used],
    'Crop_yield': [Crop_yield],        
    'Disease_Type': [Disease_Type]       
})
user_input = pd.DataFrame({
     'State': [State],
    'District': [District],
    'Crop': [Crop],
    'Season': [Season],
    'Soil_Type': [Soil_Type],
    'Temperature': [Temperature],
    'Rainfall': [Rainfall],
    'Fertilizer_Used': [Fertilizer_Used],
    'Pesticide_Used': [Pesticide_Used],
    'Crop_yield': [Crop_yield],        
    'Disease_Type': [Disease_Type]
})
prediction = pipe.predict(user_input)[0]
if prediction == 1:
    st.error("🚨 Disease Detected (Yes)")
else:
    st.success("✅ No Disease Detected")


