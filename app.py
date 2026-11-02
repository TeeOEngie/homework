import streamlit as st

st.set_page_config(page_title="Monitor Recommender", page_icon="🖥️", layout="centered")

# สไตล์หัวเว็บกับเลขงาน
st.markdown("""
<style>
.hero { background: linear-gradient(120deg, #0f766e, #2563eb); border-radius: 16px;
  padding: 40px 32px; margin-bottom: 28px; }
.hero h1 { color: #fff; margin: 0; font-size: 34px; }
.hero p { color: #dbeafe; margin: 8px 0 0; }
.num { font-size: 38px; font-weight: 800; color: #2563eb; line-height: 1; }
</style>
""", unsafe_allow_html=True)

# หัวเว็บ
st.markdown("""
<div class="hero">
  <h1>🖥️ Monitor Recommender</h1>
  <p>นายเกริกยศโกลากุล | 664245017 | 66/43
</div>
""", unsafe_allow_html=True)

# ข้อมูลงาน แก้ชื่อ คำอธิบาย ลิงก์ตรงนี้
works = [
    ("01", "Monitor & User Database",
     "จัดการข้อมูลจอมอนิเตอร์และผู้ใช้งาน",
     "เปิดใน Colab",
     "https://colab.research.google.com/github/TeeOEngie/homework/blob/main/Monitor_Recommender_System_017.ipynb"),
    ("02", "User Relationship Analysis",
     "วิเคราะห์ความสัมพันธ์ระหว่างผู้ใช้งานกับจอที่เลือก",
     "เปิดใน Colab",
     "https://colab.research.google.com/github/TeeOEngie/homework/blob/main/Mornitor017.ipynb"),
    ("03", "Monitor Recommendation System",
     "แนะนำจอมอนิเตอร์ให้ผู้ใช้งาน",
     "เปิดเว็บไซต์",
     "https://e3pwjlm3ekaf6qbrgxljis.streamlit.app/"),
]

# วนทำแถวทีละงาน
for n, title, desc, btn, link in works:
    with st.container(border=True):
        c1, c2, c3 = st.columns([1, 5, 2], vertical_alignment="center")
        c1.markdown(f'<div class="num">{n}</div>', unsafe_allow_html=True)
        c2.markdown(f"**{title}**  \n{desc}")
        c3.link_button(btn, link, use_container_width=True)

# ส่วน pdf (ปุ่มโหลดอย่างเดียว)
st.write("")
st.subheader("📄 เอกสารประกอบ")
try:
    with open("pdf/monitor017pdf.pdf", "rb") as f:
        data = f.read()
    st.download_button("โหลด PDF", data, file_name="monitor017pdf.pdf",
                       mime="application/pdf")
except FileNotFoundError:
    st.warning("ยังไม่มีไฟล์ PDF")