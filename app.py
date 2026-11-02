import base64
import streamlit as st

st.set_page_config(page_title="รวมงานส่งอาจารย์", page_icon="📚")

st.title("รวมงานส่งอาจารย์")
st.write("ชื่อ: ตอง | รหัส: xxxxxxxx | วิชา: xxxxx")

# แท็บ 3 งาน + 1 แท็บ pdf
tab1, tab2, tab3, tab4 = st.tabs(["งานที่ 1", "งานที่ 2", "งานที่ 3", "เอกสาร PDF"])

with tab1:
    st.header("งานที่ 1")
    st.link_button("เปิดใน Colab",
        "https://colab.research.google.com/github/USER/REPO/blob/main/Monitor_Recommender_System_017.ipynb")

with tab2:
    st.header("งานที่ 2")
    st.link_button("เปิดใน Colab",
        "https://colab.research.google.com/github/USER/REPO/blob/main/Mornitor017.ipynb")

with tab3:
    st.header("งานที่ 3")
    st.link_button("เปิดเว็บงาน", "https://e3pwjlm3ekaf6qbrgxljis.streamlit.app/")

with tab4:
    st.header("เอกสาร PDF")
    try:
        # อ่านไฟล์ pdf
        with open("pdf/report.pdf", "rb") as f:
            data = f.read()
        # ปุ่มโหลด
        st.download_button("โหลด PDF", data, file_name="report.pdf",
                           mime="application/pdf")
        # โชว์ในหน้าเว็บ
        b64 = base64.b64encode(data).decode()
        st.markdown(
            f'<iframe src="data:application/pdf;base64,{b64}" width="100%" height="700"></iframe>',
            unsafe_allow_html=True,
        )
    except FileNotFoundError:
        st.warning("ยังไม่มีไฟล์ PDF")