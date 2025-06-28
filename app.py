import streamlit as st
from scripts.style_transfer import style_transfer
from scripts.style_evaluation import get_similarity_score, detect_author

st.set_page_config(page_title="BookMorph – AI Author Stylist", layout="centered")

st.title("📘 BookMorph – AI Author Stylist")
st.markdown(
    "Transform modern text into the literary style of classic authors.\n\n"
    "_Powered by open LLMs + embeddings + your reading passion!_"
)

# Author selection
author = st.selectbox("Choose an author style", ["JaneAusten", "PGWodehouse"])

# Input text
input_text = st.text_area("Enter text to rewrite", height=150, placeholder="e.g. 'Discipline is choosing between what you want now and what you want most.'")

if st.button("Rewrite in Style"):
    if not input_text.strip():
        st.warning("Please enter some text.")
    else:
        with st.spinner("Generating..."):
            try:
                styled_text = style_transfer(input_text, author)
                result = get_similarity_score(styled_text, author)

                # Output
                st.markdown("### ✍️ Rewritten in Style")
                st.success(styled_text)

                st.markdown("### 📊 Similarity Score")
                st.write(f"**{result * 100:.2f}% match** with real {author.capitalize()} writing")

            except Exception as e:
                st.error(f"Something went wrong: {e}")

st.markdown("---")
st.header("🕵️ Reverse Style Detection")
st.markdown("Paste any paragraph, and we’ll detect which author’s style it most resembles.")

detection_input = st.text_area("Enter a paragraph to analyze", height=150, key="detect_input")

if st.button("Detect Author Style"):
    if not detection_input.strip():
        st.warning("Please enter some text to analyze.")
    else:
        with st.spinner("Analyzing..."):
            result = detect_author(detection_input, top_k=1)

            st.markdown("### 🧠 Closest Match")
            st.success(f"**{result['best_author'].title()}** – Similarity Score: **{result['score'] * 100:.2f}%**")

            st.markdown("### 📊 All Scores")
            for author, score in result["all_scores"]:
                st.write(f"- {author.title()}: {score * 100:.2f}%")

