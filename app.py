import streamlit as st

st.set_page_config(
    page_title="EduGenie",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 EduGenie")
st.subheader("Your AI Learning Assistant")

st.write(
    "Ask questions, understand concepts, and learn with EduGenie."
)

question = st.text_input("💡 What would you like to learn?")

if st.button("Ask EduGenie"):
    if question:
        st.success("EduGenie received your question!")
        st.write("### Answer")
        st.write(
            "Inheritance allows a Java class to reuse properties "
            "and methods from another class."
        )
    else:
        st.warning("Please enter a question.")

topic = st.text_input("📚 Enter a topic to explain:")

if st.button("Explain Topic"):
    if topic:
        st.success("Topic received!")
        st.write("### Explanation")
        st.write(
            "Demo explanation: This topic will be explained "
            "in simple, student-friendly language."
        )
    else:
        st.warning("Please enter a topic.")

notes = st.text_area("📝 Paste your notes:")

if st.button("Summarize Notes"):
    if notes:
        st.success("Notes received!")
        st.write("### Summary")
        st.write(
            "Demo summary: Your notes will be converted "
            "into short and easy-to-understand points."
        )
    else:
        st.warning("Please paste your notes.")
practice_topic = st.text_input("🧠 Topic for practice questions:")
if st.button("Generate Questions"):
    if practice_topic:
        st.success("Topic received!")
        st.write("### Practice Questions")
        st.write("1. What is the basic concept of this topic?")
        st.write("2. Why is this topic important?")
        st.write("3. Give one example related to this topic.")
    else:
        st.warning("Please enter a topic.")