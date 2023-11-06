import streamlit as st
import numpy as np
import pandas as pd

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.write(df)

options = st.sidebar.multiselect(
    'What are your favorite colors?',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red']
)

st.balloons()


import time

st.write('Starting a long computation...')

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    # Update the progress bar with each iteration.
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.02)