import os
import glob
import streamlit as st

st.set_page_config(page_title="동영상 모음", page_icon="🎬", layout="centered")
st.title("🎬 내 동영상 모음")

BASE = os.path.dirname(os.path.abspath(__file__))
EXTS = ("*.mp4", "*.mov", "*.webm", "*.m4v", "*.mkv", "*.avi")

dirs = [BASE, os.path.join(BASE, "videos")]
vids = []
for d in dirs:
    for e in EXTS:
        vids += glob.glob(os.path.join(d, e))
        vids += glob.glob(os.path.join(d, e.upper()))
vids = sorted(set(vids), key=lambda p: os.path.basename(p).lower())

if not vids:
    st.info("동영상이 없습니다. 저장소에 .mp4 파일을 올리고 새로고침하세요.")
else:
    st.caption(f"{len(vids)}개 동영상")
    for i, v in enumerate(vids, 1):
        name = os.path.splitext(os.path.basename(v))[0]
        st.subheader(f"{i}. {name}")
        st.video(v)
        st.divider()
