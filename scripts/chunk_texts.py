import os
import json 

INPUT_DIR = "author_corpus"
OUTPUT_FILE = "chunked_texts.json"
MAX_CHARS = 500

def clean_text(text):
    """Clean the text by removing unnecessary passages from the texts."""
    start_marker = "*** START OF THIS PROJECT GUTENBERG"
    end_marker = "*** END OF THIS PROJECT GUTENBERG"
    start_index = text.find(start_marker)
    end_index = text.find(end_marker)

    if start_index != -1 and end_index != -1:
        return text[start:end]
    return text

def chunk_text(text, max_chars=MAX_CHARS):
    """Chunk the text into smaller parts."""
    chunks = []
    current_chunk = ""

    for line in text.splitlines():
        if len(current_chunk) + len(line) <= max_chars:
            current_chunk += line + "\n"
        else:
            chunks.append(current_chunk.strip())
            current_chunk = line + "\n"

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks

def process_files():
    """Process all text files in the input directory and save chunked texts to a JSON file."""
    author_chunks = {}

    for filename in os.listdir(INPUT_DIR):
        author = filename.split('_')[0]

        if author not in author_chunks:
            author_chunks[author] = []

        if filename.endswith(".txt"):
            file_path = os.path.join(INPUT_DIR, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
                cleaned_text = clean_text(text)
                chunks = chunk_text(cleaned_text)
                author_chunks[author].extend(chunks)

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as output_file:
        json.dump(author_chunks, output_file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    process_files()
    print(f"Chunked texts saved to {OUTPUT_FILE}")