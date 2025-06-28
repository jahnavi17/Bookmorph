import json 
from sentence_transformers import SentenceTransformer
import numpy as np
import random 
from sklearn.metrics.pairwise import cosine_similarity

MODEL = SentenceTransformer('all-distilroberta-v1') 
AUTHORS_DATA = "chunked_texts.json"

with open(AUTHORS_DATA, 'r', encoding="utf-8") as f:
    author_chunks = json.load(f)

def get_similarity_score(generated_text, author_name, n=5):
    if author_name not in author_chunks:
        raise ValueError("Author not found in chunk data")

    # Get N real author samples
    samples = random.sample(author_chunks[author_name], min(n, len(author_chunks[author_name])))

    # Generate embeddings
    gen_emb = MODEL.encode([generated_text])
    real_embs = MODEL.encode(samples)

    if gen_emb.ndim == 1:
        gen_emb = np.expand_dims(gen_emb, axis=0)
    if real_embs.ndim == 1:
        real_embs = np.expand_dims(real_embs, axis=0)

    # Compute cosine similarity
    scores = cosine_similarity(gen_emb, real_embs)[0]
    average_score = float(np.mean(scores))
    return round(average_score, 4)

def detect_author(input_text, top_k=1, num_of_samples=10):
    scores = {}
    embeddings = MODEL.encode([input_text]) 
    for author, chunks in author_chunks.items():
        samples = random.sample(chunks,min(num_of_samples, len(chunks)))
        real_embs = MODEL.encode(samples)

        similarity = cosine_similarity(embeddings, real_embs)
        scores[author] = float(np.mean(similarity))
    
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    if top_k == 1:
        best_author , score = sorted_scores[0]
        return {
            "best_author": best_author,
            "score": score,
            "all_scores": sorted_scores
        }
    else:
        return {
            "top_authors": sorted_scores[:top_k],
            "all_scores": sorted_scores
        }
    
if __name__ == "__main__":
    # Example usage
    # generated_text = "This is a sample text that mimics the style of a specific author."
    # author_name = "PGWodehouse"
    # score = get_similarity_score(generated_text, author_name)
    # print(f"Similarity score for {author_name}: {score}")

    input_text = "This is a sample text to detect the author."
    result = detect_author(input_text)
    print(result)