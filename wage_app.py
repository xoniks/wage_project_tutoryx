import pandas as pd
import streamlit as st 

def calculate_wage(name):
    df = pd.read_csv(name)
    df['rate']=df['currency'].str[1:]
    df.drop('currency',axis=1,inplace=True)
    df.rename(columns={"numberrange": "hours"},inplace=True)
    df['rate'] = df['rate'].astype('float')
    df['wage'] = df['hours']*df['rate']
    return df
    
result = calculate_wage('data_wage - Copy.csv')
print(result)


@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv(index=False).encode('utf-8')