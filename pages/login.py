# login.py

import streamlit as st

# Fake database: email → password
USER_CREDENTIALS = {
    "user1@example.com": "password123",
    "admin@cloud.com": "adminpass"
}

def login_page():
    st.set_page_config(page_title="Login | Cloud Optimizer", layout="centered")
    st.markdown("<h2 style='text-align: center;'>🔐 Cloud Cost Optimizer Login</h2>", unsafe_allow_html=True)
    st.markdown("---")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if email in USER_CREDENTIALS and USER_CREDENTIALS[email] == password:
            st.session_state["authenticated"] = True
            st.session_state["user_email"] = email
            st.success("✅ Login successful! Redirecting to dashboard...")
            st.experimental_rerun()
        else:
            st.error("❌ Invalid email or password")

# Run login logic
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    login_page()
else:
    st.switch_page("app.py")
