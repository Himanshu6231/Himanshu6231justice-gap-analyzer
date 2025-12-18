# app_simple.py
import streamlit as st
import pandas as pd

st.title("Justice Gap Analyzer - Basic Version")
st.write("This is a working version with minimal dependencies.")

# Load data
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("legal_aid_dataset.csv")
        return df, True
    except:
        # Create sample data if file doesn't exist
        data = {
            'Case_ID': range(1, 101),
            'Case_Type': ['Domestic_Violence', 'Property_Dispute', 'Criminal'] * 33 + ['Domestic_Violence'],
            'Gender': ['Male', 'Female'] * 50,
            'Delay_Flag': [1, 0] * 50,
            'Income_Bracket': ['Low', 'Medium', 'High'] * 33 + ['Low']
        }
        df = pd.DataFrame(data)
        return df, False

df, file_exists = load_data()

if file_exists:
    st.success("Real data loaded")
else:
    st.info("Using sample data")

# Show data
st.subheader("Data Preview")
st.dataframe(df)

# Analysis
st.subheader("Analysis")
if 'Delay_Flag' in df.columns and 'Case_Type' in df.columns:
    # Calculate delay rates
    delay_analysis = df.groupby('Case_Type')['Delay_Flag'].agg(['mean', 'count'])
    delay_analysis['mean'] = delay_analysis['mean'] * 100
    
    st.write("Delay Rates by Case Type:")
    st.dataframe(delay_analysis)
    
    # Simple chart
    st.bar_chart(delay_analysis['mean'])

st.write("App is working! ✅")
