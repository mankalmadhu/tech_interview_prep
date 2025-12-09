import streamlit as st
import json
import os
from datetime import datetime, timedelta
import pandas as pd

# --- Constants & Config ---
HISTORY_FILE = '.review_history.json'
ROOT_DIR = '.'  # Assumes running from PracticeDSA or repo root
PAGE_TITLE = "Problem Review Tracker"
# SRS Intervals (Level -> Days until next review)
# Matches review_scheduler.py: [1, 3, 7, 14, 28, 60]
SRS_INTERVALS = [1, 3, 7, 14, 28, 60]

st.set_page_config(page_title=PAGE_TITLE, layout="wide")

# --- Helper Functions ---

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r') as f:
            return json.load(f)
    return {"reviews": {}}

def save_history(data):
    with open(HISTORY_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def get_all_python_files(root_dir):
    # Find all .py files, excluding this script and standard exclusions
    files = []
    for root, dirs, filenames in os.walk(root_dir):
        # Filter out directories to avoid recursion into them
        dirs[:] = [d for d in dirs if d not in {'.git', '__pycache__', '.venv', 'env', 'venv', '.idea', '.vscode', 'SystemDesign'}]
        
        for filename in filenames:
            if filename.endswith('.py') and filename not in {'review_app.py', 'review_scheduler.py', 'generate_readmes.py', '__init__.py', 'main.py'}:
                # Store relative path
                full_path = os.path.join(root, filename)
                rel_path = os.path.relpath(full_path, root_dir)
                files.append(rel_path)
    return sorted(files)

def mark_as_reviewed(filepath, history, quality):
    """
    quality: '1' (Hard), '2' (Good), '3' (Easy)
    """
    current_level = 0
    if filepath in history['reviews']:
        current_level = history['reviews'][filepath].get('level', 0)

    # SRS Logic from review_scheduler.py + Custom 'Very Easy'
    days_override = None
    
    if quality == '1': # Hard -> Reset
        new_level = 1
    elif quality == '2': # Good -> +1
        new_level = current_level + 1
    elif quality == '3': # Easy -> +2
        new_level = current_level + 2
    elif quality == '4': # Very Easy -> Custom 10 days
        new_level = current_level + 3
        days_override = 10
    else:
        new_level = current_level + 1 # Fallback

    # Cap level
    if new_level > len(SRS_INTERVALS):
         new_level = len(SRS_INTERVALS)
    
    idx = max(0, min(new_level - 1, len(SRS_INTERVALS) - 1))
    days_to_add = SRS_INTERVALS[idx]
    
    if days_override:
        days_to_add = days_override
            
    next_date = (datetime.now() + timedelta(days=days_to_add)).strftime('%Y-%m-%d')
    today = datetime.now().strftime('%Y-%m-%d')

    history['reviews'][filepath] = {
        'level': new_level,
        'last_reviewed': today,
        'next_review': next_date
    }
    save_history(history)
    st.toast(f"✅ Logged '{filepath}' ({quality_label(quality)})! Next: {next_date} (Lv {new_level})")

def quality_label(q):
    return {'1': 'Hard', '2': 'Good', '3': 'Easy', '4': 'Very Easy'}.get(q, '?')

# --- Main App Logic ---

st.title("🧠 DSA Problem Review Tracker")

history = load_history()
all_files = get_all_python_files(ROOT_DIR)
reviewed_files = history.get('reviews', {})

# -- Data Processing --
today_str = datetime.now().strftime('%Y-%m-%d')
upcoming_reviews = []
untracked_files = []
all_reviewed_data = []

for f in all_files:
    if f in reviewed_files:
        data = reviewed_files[f]
        data['filepath'] = f
        all_reviewed_data.append(data)
        
        # Check if due
        if data.get('next_review', '2000-01-01') <= today_str:
            upcoming_reviews.append(data)
    else:
        untracked_files.append(f)

# -- Dashboard Metrics --
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Solved", len(all_files))
with col2:
    st.metric("Tracked", len(reviewed_files))
with col3:
    st.metric("Due Review", len(upcoming_reviews), delta_color="inverse")
with col4:
    st.metric("Untracked", len(untracked_files))

# -- Tabs --
tab1, tab2, tab3 = st.tabs(["📅 Upcoming Reviews", "🆕 Untracked Problems", "📊 All Tracked"])

with tab1:
    st.header("Due for Review")
    if not upcoming_reviews:
        st.info("No reviews due today! Good job. 🎉")
    else:
        for item in upcoming_reviews:
            with st.container():
                c1, c2 = st.columns([3, 2])
                with c1:
                    st.subheader(item['filepath'])
                    st.caption(f"Current Level: {item.get('level', 0)} | Last: {item.get('last_reviewed', 'Never')}")
                with c2:
                    st.write("How was it?")
                    b1, b2, b3, b4 = st.columns(4)
                    if b1.button("Hard 🥵", key=f"h_{item['filepath']}"):
                        mark_as_reviewed(item['filepath'], history, '1')
                        st.rerun()
                    if b2.button("Good 🙂", key=f"g_{item['filepath']}"):
                        mark_as_reviewed(item['filepath'], history, '2')
                        st.rerun()
                    if b3.button("Easy 🤩", key=f"e_{item['filepath']}"):
                        mark_as_reviewed(item['filepath'], history, '3')
                        st.rerun()
                    if b4.button("V. Easy 🚀", key=f"ve_{item['filepath']}"):
                        mark_as_reviewed(item['filepath'], history, '4')
                        st.rerun()
                st.divider()

with tab2:
    st.header("Untracked Problems")
    st.markdown("These files exist in your folder but aren't in the review history.")
    
    for f in untracked_files:
        c1, c2 = st.columns([3, 2])
        with c1:
            st.text(f)
        with c2:
            st.write("Start Tracking:")
            b1, b2, b3, b4 = st.columns(4)
            # Use same buttons for initial tracking
            if b1.button("Hard", key=f"init_h_{f}"):
                mark_as_reviewed(f, history, '1')
                st.rerun()
            if b2.button("Good", key=f"init_g_{f}"):
                mark_as_reviewed(f, history, '2')
                st.rerun()
            if b3.button("Easy", key=f"init_e_{f}"):
                mark_as_reviewed(f, history, '3')
                st.rerun()
            if b4.button("V. Easy", key=f"init_ve_{f}"):
                mark_as_reviewed(f, history, '4')
                st.rerun()

with tab3:
    st.header("Tracking History")
    if all_reviewed_data:
        df = pd.DataFrame(all_reviewed_data)
        st.dataframe(
            df[['filepath', 'level', 'last_reviewed', 'next_review']].sort_values('next_review'),
            use_container_width=True
        )
    else:
        st.write("No tracked files yet.")

