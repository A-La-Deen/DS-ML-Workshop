import streamlit as st

st.set_page_config(page_title="MyApp", layout="wide")

st.title("🏠 หน้าหลัก ")
st.write("### Boot Camp: Data Science and Machine Learning")
st.info("7 Day Intensive Hands-on Workshop")
st.write("A LA DEEN")
st.write("##### Day 1: การจัดการข้อมูลพื้นฐานและโครงสร้างข้อมูลด้วย Python")
st.markdown(''':red[A LA DEEN]''')

if st.button("💰 ระบบคำนวณส่วนลดตามยอดซื้อ"):
    st.switch_page("pages/app1_discount_calc.py")
elif st.button("A LA DEEN Clean"):
    st.switch_page("pages/clean_A LA DEEN.py")
elif st.button("App Clean"):
    st.switch_page("pages/clean_app.py")
elif st.button("Chang Info"):
    st.switch_page("pages/transform_app.py")
elif st.button("EDA Info"):
    st.switch_page("pages/EDA_app.py")
