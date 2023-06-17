import streamlit as st 
import pandas as pd
from wage_app import calculate_wage,convert_df


st.title('Wage App Tutoryx')


file_in = st.file_uploader('Please upload employee file')

if file_in is not None:
    dataframe = calculate_wage(file_in)
    st.write(dataframe)
    
    csv = convert_df(dataframe)
    file_name_in = st.text_input('Please enter a name for file','None')

    if file_name_in is not 'None':
        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name=file_name_in+'.csv',
            mime='text/csv',
        )