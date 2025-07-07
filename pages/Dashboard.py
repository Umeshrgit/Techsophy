import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from collector.usage_data import fetch_mock_data
from analyzer.patterns import detect_anomalies
from optimizer.optimizer import suggest_optimizations

# Ensure logged in
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("You must log in to view this page.")
    st.stop()

st.title("☁️ Cloud Cost Optimizer Dashboard")
# ... your existing dashboard code ...
