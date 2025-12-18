import streamlit as st
import pandas as pd

st.title("Justice Gap Analyzer - Deployment Test")
st.write("If you see this, the app is working!")

# Create simple data
data = pd.DataFrame({
    "Case": ["DV", "Property", "Criminal"],
    "Delay %": [72, 45, 38]
})

st.write("Sample analysis:")
st.dataframe(data)
st.bar_chart(data.set_index("Case"))
