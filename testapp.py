import streamlit as st

st.markdown("""
    <style>
    .stApp { background: rgba(0,0,0,0) !important; }
    header { background: rgba(0,0,0,0) !important; }
    section[data-testid="stSidebar"] { background: rgba(0,0,0,0) !important; }
    </style>
""", unsafe_allow_html=True)

st.title("Hello from AR! 👋")
st.write("If you can see this floating in your room, it worked.")
st.slider("Test slider", 0, 100, 50)

