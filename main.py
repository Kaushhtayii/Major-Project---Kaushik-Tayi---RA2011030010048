"""This is the main module to run the app"""

# Importing the necessary Python modules.
import streamlit as st

# Import necessary functions from web_functions
from web_functions import load_data # For biomarkers test
from eeg_modulator import load_data_obj # for EEG Test only

# Configure the app
st.set_page_config(
    page_title = 'Alzheimer Stage Detector using EEG',
    page_icon = 'brain',
    layout = 'wide',
    initial_sidebar_state = 'auto'
)
    
# Import pages
from Tabs import home, data, eegdata, predeeg, predict, visualise



# Dictionary for pages
Tabs = {
    "Home": home,
    "Biomarker Data Info": data,
    "EEG Data Info": eegdata,
    "Biomarker AD Test": predict,
    "EEG AD Test":predeeg,
    "Visualisation": visualise
    
}

# Create a sidebar
# Add title to sidear
st.sidebar.title("Navigation")

# Create radio option to select the page
page = st.sidebar.radio("Pages", list(Tabs.keys()))

# Loading the dataset.
df, X, y = load_data() # Alzheimer.csv
df2, X2, y2 = load_data_obj() #EEG_data.csv

# Call the app function of selected page to run
if page in ["Biomarker AD Test", "Visualisation"]:
    Tabs[page].app(df, X, y)
elif (page == "EEG AD Test"):
    Tabs[page].app(df2,X2,y2)
elif (page == "Biomarker Data Info"):
    Tabs[page].app(df)
elif (page == "EEG Data Info"):
    Tabs[page].app(df2)
else:
    Tabs[page].app()