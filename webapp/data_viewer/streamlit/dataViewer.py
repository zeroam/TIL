import streamlit as st
import pandas as pd
from pydataset import data


df_data = data().sort_values('dataset_id').reset_index(drop=True)
st.dataframe(df_data)   # choices

options = st.selectbox(
    'select a dataset do you like best?', df_data['dataset_id'])

dataset = data(options)

if isinstance(dataset, (pd.core.frame.DataFrame,
        pd.core.series.Series)):
    st.dataframe(dataset)
    st.line_chart(dataset)
