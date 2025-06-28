import json
import random 
import requests 

CHUNKS_FILE = "chunked_texts.json"
OUTPUT_FILE = "style_profiles.json"

API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
HF_TOKEN = "paste your Huggingface token here"  # Replace with your Hugging Face token

headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def generate_prompt(chunks):
    return f"""
You are an expert in analyzing writing styles. Given the following text chunks, 
please analyze the style and provide a detailed profile of the author's writing style, 
including aspects such as tone, vocabulary, sentence structure, and any notable stylistic features.
The profile should be comprehensive and insightful, suitable for a literary analysis context.
Write this as if you are describing the author's style to a literary student.

###Text chunks:
{chunks[0]}
{chunks[1]}
{chunks[2]}

Please provide a comprehensive style profile.
### Style Profile:
"""

def query_hugging_face(prompt):
    payload = {
        "inputs": prompt,
         "parameters": {
            "max_new_tokens": 300
            }
    } 

    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()[0]['generated_text'].split("### Style Profile:")[-1].strip()
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None
    
def main():
    with open(CHUNKS_FILE, "r" , encoding="utf-8") as f:
        chunks = json.load(f)

    style_profiles = {}
    
    for author, chunks in chunks.items():
        print(f"Generating style profile for {author}...")
        sample_chunks = random.sample(chunks, 3) if len(chunks) > 3 else chunks
        prompt = generate_prompt(sample_chunks)

        try:
            style_profile = query_hugging_face(prompt)
            if style_profile:
                style_profiles[author] = style_profile
                print(f"Style profile for {author} generated successfully.")
        except Exception as e:
            print(f"An error occurred while processing {author}: {e}")
            continue

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(style_profiles, f, ensure_ascii=False, indent=4)
    print(f"Style profiles saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()