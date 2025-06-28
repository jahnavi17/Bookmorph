# 📘 BookMorph: The AI Author Stylist

**BookMorph** is a GenAI-powered application that transforms modern text into the writing style of classic authors like **Jane Austen** and **P.G. Wodehouse** — and even detects whose style your own writing resembles.

> ✍️ Style Transfer + 🕵️ Style Detection + 📊 Embedding-Based Evaluation
> All in one personal NLP project.


---

## 🚀 Features

* ✍️ **Style Transfer**: Rewrite any modern sentence in the voice of Jane Austen or P.G. Wodehouse
* 🧠 **Author Style Profiling**: LLM-generated summaries of each author’s stylistic traits
* 🧪 **Style Similarity Scoring**: Compare generated text to real literary chunks using cosine similarity over embeddings
* 🕵️ **Reverse Style Detection**: Paste any paragraph and detect which author it most resembles

---

## 💡 Motivation

> "As an avid reader, I wanted to build a tool that merges literature and AI — letting users see how different authors might express the same idea, and explore what makes a writing style unique."

This project showcases my skills in **LLM prompt engineering, retrieval-based NLP, semantic embeddings, GenAI evaluation**, and **frontend deployment** using open-source tools.

---

## 🧠 Tech Stack

| Layer             | Tools & Models                                |
| ----------------- | --------------------------------------------- |
| LLM Inference     | Hugging Face Inference API (`zephyr-7b-beta`) |
| Embeddings        | SentenceTransformers (`all-MiniLM-L6-v2`)     |
| Vector Comparison | Cosine similarity (`scikit-learn`)            |
| Interface         | Streamlit                                     |
| Data              | Project Gutenberg novels (Austen, Wodehouse)  |

---


## 🖥️ How to Run Locally

1. **Clone the repo**

```bash
git clone https://github.com/yourusername/bookmorph.git
cd bookmorph
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Set your Hugging Face token**
   Create a `.env` file or set `HF_TOKEN` as an environment variable.

4. **Run the app**

```bash
streamlit run app.py
```

---

## 🔑 Example Usage

> **Input:** “Discipline is choosing between what you want now and what you want most.”
> **Austen-style Output:** “It is not uncommon for desires of the present to contradict those which reason would deem most enduring.”
> **Similarity Score to Austen corpus:** 83.2%

---

## 📚 Authors Included

* **Jane Austen**: Formal, ironic, socially observant
* **P.G. Wodehouse**: Witty, humorous, upper-class slang

(You can easily expand to add more authors via `author_corpus/` and a simple script.)

---

## 📦 To-Do / Future Features

* [ ] Add Shakespeare or Orwell
* [ ] Style evolution chart across authors
* [ ] Export results to PDF or shareable quote images
* [ ] Theme/tag-based quote finder

---

## 📣 Credits

* Project Gutenberg (public domain texts)
* Hugging Face Inference API
* SentenceTransformers by UKPLab
* Inspired by a personal love of books and language ✨

---
