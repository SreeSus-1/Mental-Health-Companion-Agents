import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from agents.tracker_agent import WellnessTrackerAgent

from agents.reflection_agent import ReflectionAgent
from agents.reframe_agent import CognitiveReframeAgent
from memory.journal_db import save_entry, get_entries

st.title("Mental Health Companion Agents")

tracker = WellnessTrackerAgent()

reflection_agent = ReflectionAgent()
reframe_agent = CognitiveReframeAgent()

menu = st.sidebar.selectbox(
    "Menu",
    ["Daily Journal", "Wellness Trends"]
)

if menu == "Daily Journal":

    mood = st.slider("How are you feeling today?", 1, 10)

    journal = st.text_area("Write your journal entry")

    if st.button("Analyze Entry"):

        tracker.save_journal(mood, journal)

        with st.spinner("Reflecting on emotions..."):
            reflection = reflection_agent.analyze(journal)

        with st.spinner("Generating supportive perspective..."):
            reframe = reframe_agent.reframe(journal)

        st.subheader("Emotional Reflection")
        st.write(reflection)

        st.subheader("Supportive Perspective")
        st.write(reframe)

elif menu == "Wellness Trends":

    entries = tracker.get_history()

    if entries:

        df = pd.DataFrame(entries)

        st.subheader("Mood Trend Over Time")

        fig, ax = plt.subplots()

        ax.plot(df["date"], df["mood"], marker="o")

        ax.set_xlabel("Date")
        ax.set_ylabel("Mood Score")

        st.pyplot(fig)

        st.dataframe(df)

    else:

        st.write("No entries yet.")