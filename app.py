import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.title('Uber pickups in NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data
  
  # Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')

st.subheader('Raw data')
st.write(data)


df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)
edited_df = st.experimental_data_editor(df)

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")


image = Image.open('https://www.google.com/url?sa=i&url=https%3A%2F%2Fuol.edu.pk%2Fdiscover-uol%2Fhistory%2F&psig=AOvVaw0UPLARJZ7YFeAs8kcewXfk&ust=1685088033935000&source=images&cd=vfe&ved=0CBEQjRxqFwoTCMD_x_iBkP8CFQAAAAAdAAAAABAD')

st.image(image, caption='Sunrise by the mountains')
