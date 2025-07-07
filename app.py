import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from collector.usage_data import fetch_mock_data
from analyzer.patterns import detect_anomalies
from optimizer.optimizer import suggest_optimizations

# ---------------------------
# Dummy credentials
# ---------------------------
USER_CREDENTIALS = {
    "admin": "password123",
    "user1": "secret456"
}

# ---------------------------
# Initialize session state
# ---------------------------
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
if "login_success" not in st.session_state:
    st.session_state["login_success"] = False

# ---------------------------
# Login Page
# ---------------------------
def login():
    st.title("🔐 Login to Cloud Cost Optimizer")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            st.session_state["login_success"] = True
            st.success("✅ Login successful! Click 'Continue' to go to dashboard.")
        else:
            st.error("❌ Invalid username or password.")

    if st.session_state["login_success"]:
        if st.button("Continue"):
            st.session_state["authenticated"] = True

# ---------------------------
# Require Login First
# ---------------------------
if not st.session_state.get("authenticated", False):
    login()
    st.stop()

# ---------------------------
# Dashboard (after login)
# ---------------------------
st.set_page_config(page_title="☁️ Cloud Cost Optimizer", layout="centered")

# Custom CSS
st.markdown("""
    <style>
        .main {
            background-color: #f5f7fa;
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        h1 {
            color: #2c3e50;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            border-radius: 8px;
            padding: 10px 24px;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center;'>☁️ Cloud Cost Optimizer Dashboard</h1>", unsafe_allow_html=True)
st.markdown("---")

# Analyze Button
if st.button("🔍 Analyze My Cloud Usage"):
    data = fetch_mock_data()
    df = pd.DataFrame(data)

    with st.expander("📊 Raw Usage & Cost Data", expanded=True):
        st.dataframe(df, use_container_width=True)

    with st.expander("📈 Usage vs Cost Chart", expanded=True):
        fig, ax = plt.subplots()
        x = df['service']
        ax.bar(x, df['usage'], width=0.4, label='Usage', align='edge', color='#3498db')
        ax.bar(x, df['cost'], width=-0.4, label='Cost', align='edge', color='#e74c3c')
        ax.set_ylabel("Amount")
        ax.set_title("Service-wise Usage vs Cost")
        ax.legend()
        st.pyplot(fig)

    anomalies = detect_anomalies(data)
    suggestions = suggest_optimizations(anomalies)

    st.markdown("---")
    st.subheader("💡 Optimization Suggestions")

    if suggestions:
        for s in suggestions:
            st.warning(s)
    else:
        st.success("No cost inefficiencies found! 🎉")
else:
    st.info("Click the button above to start analyzing your cloud costs.")
