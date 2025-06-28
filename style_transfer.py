import json 
import requests

HF_TOKEN = "paste your Huggingface token here"
API_URL = "https://api-inference.huggingface.co/models/meta-llama/Llama-3.1-8B-Instruct"
HEADERS = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

def create_style_transfer_prompt(input_text, author_name, author_profile):
    return f"""
You are an expert in style transfer. Your task is to rewrite the following text in the style of 
{author_name}, based on their writing profile provided below.   
The style profile includes aspects such as tone, vocabulary, sentence structure, and any notable stylistic features.
### Author Profile:
{author_profile}
The style transfer should maintain the original meaning and context of the input text while transforming it 
to reflect the unique style of the author.

Now, rewrite the following text in the style of {author_name}
### Input Text:
{input_text}

### Output Text:
""" 

def query_hugging_face(prompt):
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 300
        }
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)
    if response.status_code == 200:
        return response.json()[0]['generated_text'].split("### Output Text:")[-1].strip()
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None
    
def style_transfer(input_text, author_name) :
    with open("style_profiles.json", "r", encoding="utf-8") as f:
        style_profiles = json.load(f)   
    if author_name not in style_profiles:
        raise ValueError(f"Author {author_name} not found in style profiles.")
    
    author_profile = style_profiles[author_name]
    prompt = create_style_transfer_prompt(input_text, author_name, author_profile)  
    return query_hugging_face(prompt)

if __name__ == "__main__":
    input_text = "The quick brown fox jumps over the lazy dog."
    author_name = "PGWodehouse"
    
    try:
        output_text = style_transfer(input_text, author_name)
        print(f"Output Text:\n{output_text}")
    except Exception as e:
        print(f"An error occurred: {e}")