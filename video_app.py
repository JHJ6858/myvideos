import os
import glob
import streamlit as st

st.set_page_config(page_title="동영상 모음", page_icon="🎬", layout="centered")
st.title("🎬 내 동영상 모음")
st.image("img/poster.png", caption="설명 (선택)", use_container_width=True)

# ===== 유튜브(미등록) 링크 — 여기에 추가/수정 =====
# ("제목", "링크") 형식. 제목은 원하는 대로 바꾸세요.
YOUTUBE = [
    ("발표 영상", "https://youtu.be/OhOoy5KOrZs"),
]

BASE = os.path.dirname(os.path.abspath(__file__))
EXTS = ("*.mp4", "*.mov", "*.webm", "*.m4v", "*.mkv", "*.avi")

dirs = [BASE, os.path.join(BASE, "videos")]
vids = []
for d in dirs:
    for e in EXTS:
        vids += glob.glob(os.path.join(d, e))
        vids += glob.glob(os.path.join(d, e.upper()))
vids = sorted(set(vids), key=lambda p: os.path.basename(p).lower())

total = len(YOUTUBE) + len(vids)
if total == 0:
    st.info("동영상이 없습니다. videos 폴더에 .mp4 파일을 올리거나 위 YOUTUBE 목록에 링크를 추가하세요.")
else:
    st.caption(f"{total}개 동영상")
    n = 0
    # 1) 유튜브 영상 먼저
    for title, url in YOUTUBE:
        n += 1
        st.subheader(f"{n}. {title}")
        st.video(url)
        st.divider()
    # 2) 폴더(videos/·루트)에 있는 영상 파일
    for v in vids:
        n += 1
        name = os.path.splitext(os.path.basename(v))[0]
        st.subheader(f"{n}. {name}")
        st.video(v)
        st.divider()
