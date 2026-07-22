# -*- coding: utf-8 -*-
"""
동영상을 앱에 '심어두고' 보여주는 Streamlit 앱 (업로드 X, 외부 접속자 모두 재생 가능)
사용법:
  1) 이 파일 옆의 'videos' 폴더에 동영상(.mp4 권장)을 넣는다
  2) streamlit run video_app.py
"""
import os
import glob
import streamlit as st

st.set_page_config(page_title="동영상 모음", page_icon="🎬", layout="centered")

# 스크립트 위치 기준 videos 폴더 (실행 위치와 무관하게 동작)
BASE = os.path.dirname(os.path.abspath(__file__))
VID_DIR = os.path.join(BASE, "videos")
os.makedirs(VID_DIR, exist_ok=True)

EXTS = ("*.mp4", "*.mov", "*.webm", "*.m4v", "*.mkv", "*.avi")

st.title("🎬 내 동영상 모음")

# videos 폴더의 모든 동영상 (이름순)
vids = []
for e in EXTS:
    vids += glob.glob(os.path.join(VID_DIR, e))
    vids += glob.glob(os.path.join(VID_DIR, e.upper()))
vids = sorted(set(vids), key=lambda p: os.path.basename(p).lower())

if not vids:
    st.info(f"동영상이 없습니다.\n\n**{VID_DIR}** 폴더에 동영상(.mp4)을 넣고 새로고침하세요.")
else:
    st.caption(f"{len(vids)}개 동영상 · 접속하는 모두에게 표시됩니다")
    for i, v in enumerate(vids, 1):
        name = os.path.splitext(os.path.basename(v))[0]
        size = os.path.getsize(v) / 1e6
        st.subheader(f"{i}. {name}")
        st.caption(f"{size:.1f} MB")
        st.video(v)
        st.divider()
