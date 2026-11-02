import streamlit as st

st.set_page_config(page_title="Monitor Recommender", page_icon="🖥️", layout="wide")

# สไตล์หน้าเว็บ
css = """
<style>
.stApp { background: #0e0e0e; }
h1.t { color: #fff; font-size: 28px; margin-bottom: 4px; }
p.s { color: #aaa; margin-bottom: 28px; }
.grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; }
@media (max-width: 800px) { .grid { grid-template-columns: 1fr; } }
.frame { background: #000; border-radius: 10px; padding: 30px 14px; position: relative; }
.frame::before, .frame::after { content: ""; position: absolute; left: 14px; right: 14px; height: 8px;
  background: repeating-linear-gradient(90deg, #2a2a2a 0 14px, transparent 14px 28px); }
.frame::before { top: 10px; }
.frame::after { bottom: 10px; }
.card { background: #1c1c1c; border-radius: 8px; padding: 24px; min-height: 300px;
  display: flex; flex-direction: column; }
.card .ic { font-size: 36px; }
.card h3 { color: #fff; margin: 14px 0 8px; font-size: 20px; }
.card p { color: #aaa; font-size: 14px; }
.btn { margin-top: auto; display: block; text-align: center; padding: 12px; border-radius: 8px;
  font-weight: 600; text-decoration: none; background: #f1f1f1; color: #111 !important; }
.btn.out { background: transparent; color: #fff !important; border: 1px solid #888; }
</style>
"""

# สร้างการ์ด 1 ใบ
def card(icon, title, desc, link, btn, out=False):
    cls = "btn out" if out else "btn"
    return ('<div class="frame"><div class="card">'
            f'<div class="ic">{icon}</div>'
            f'<h3>{title}</h3><p>{desc}</p>'
            f'<a class="{cls}" href="{link}" target="_blank">{btn} ↗</a>'
            '</div></div>')

# ข้อมูลงาน 3 อัน แก้ชื่อกับคำอธิบายตรงนี้
cards = [
    card("🖥️", "Monitor & User Database",
         "จัดการข้อมูลจอมอนิเตอร์และผู้ใช้งานด้วยฐานข้อมูล",
         "https://colab.research.google.com/github/USER/REPO/blob/main/Monitor_Recommender_System_017.ipynb",
         "เปิดโปรเจกต์"),
    card("👥", "User Relationship Analysis",
         "วิเคราะห์ความสัมพันธ์ระหว่างผู้ใช้งานและจอที่เลือกใช้",
         "https://colab.research.google.com/github/USER/REPO/blob/main/Mornitor017.ipynb",
         "เปิดโปรเจกต์"),
    card("⭐", "Monitor Recommendation System",
         "แนะนำจอมอนิเตอร์จากความต้องการและความสัมพันธ์ของผู้ใช้งาน",
         "https://e3pwjlm3ekaf6qbrgxljis.streamlit.app/",
         "เปิดเว็บไซต์", out=True),
]

# หัวเว็บ + การ์ด
html = (css
        + '<h1 class="t">Monitor Recommender</h1>'
        + '<p class="s">รวมระบบจัดการข้อมูล วิเคราะห์ความสัมพันธ์ และแนะนำจอมอนิเตอร์</p>'
        + '<div class="grid">' + "".join(cards) + '</div>')
st.markdown(html, unsafe_allow_html=True)

# ส่วน pdf ข้างล่าง
st.write("")
st.subheader("เอกสาร PDF")
try:
    with open("pdf/report.pdf", "rb") as f:
        data = f.read()
    st.download_button("โหลด PDF", data, file_name="report.pdf", mime="application/pdf")
except FileNotFoundError:
    st.warning("ยังไม่มีไฟล์ PDF")