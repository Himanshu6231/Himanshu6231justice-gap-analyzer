# app.py - SIMPLE VERSION
import streamlit as st
import pandas as pd
import numpy as np

# Page config
st.set_page_config(
    page_title="Justice Gap Analyzer",
    page_icon="⚖️",
    layout="wide"
)

# Title
st.title("⚖️ Systemic Justice Gap Analyzer")
st.markdown("**Using FP-Growth Association Rule Mining**")

# Check if we can load data
try:
    df = pd.read_csv("legal_aid_dataset.csv")
    st.success(f"✅ Successfully loaded {len(df)} records")
    
    # Show basic info
    st.subheader("Dataset Preview")
    st.dataframe(df.head())
    
    # Basic stats
    st.subheader("Statistics")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Cases", len(df))
    
    with col2:
        if 'Case_Type' in df.columns:
            st.metric("Case Types", df['Case_Type'].nunique())
    
    with col3:
        if 'Delay_Flag' in df.columns:
            delay_rate = df['Delay_Flag'].mean() * 100
            st.metric("Delay Rate", f"{delay_rate:.1f}%")
    
    # Simple analysis
    if 'Case_Type' in df.columns and 'Delay_Flag' in df.columns:
        st.subheader("Delay Analysis by Case Type")
        delay_by_type = df.groupby('Case_Type')['Delay_Flag'].mean().sort_values(ascending=False)
        st.bar_chart(delay_by_type)
    
except Exception as e:
    st.error(f"❌ Error loading data: {str(e)}")
    st.info("Please make sure 'legal_aid_dataset.csv' is in the same directory.")

# Test if modules can be imported
st.subheader("Module Test")
try:
    import sklearn
    st.success("✅ scikit-learn imported successfully")
except:
    st.warning("⚠️ scikit-learn not available")

try:
    import mlxtend
    st.success("✅ mlxtend imported successfully")
except:
    st.warning("⚠️ mlxtend not available")

try:
    import plotly
    st.success("✅ plotly imported successfully")
except:
    st.warning("⚠️ plotly not available")

# Footer
st.markdown("---")
st.markdown("**App Status: Testing Dependencies**")
