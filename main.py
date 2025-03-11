import pandas as pd
import streamlit as st

# Streamlit app title
st.title("CSV Filter App")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Load the CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)
    
    # Normalize column names (lowercase & strip spaces)
    df.columns = df.columns.str.lower().str.strip()
    
    # Check if 'website' column exists
    if 'website' in df.columns:
        # Filter rows where 'website' column is empty or null
        filtered_df = df[df['website'].isna() | (df['website'].astype(str).str.strip() == '')]
        
        # Convert DataFrame to Excel
        output_path = 'filtered_data.xlsx'
        filtered_df.to_excel(output_path, index=False)
        
        # Provide download link
        st.download_button(label="Download Filtered Data", data=open(output_path, "rb"), file_name="filtered_data.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    else:
        st.error("The uploaded CSV file does not contain a 'website' column.")