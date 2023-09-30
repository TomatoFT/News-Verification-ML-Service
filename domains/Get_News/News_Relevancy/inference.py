import numpy as np
from sentence_transformers import SentenceTransformer


# Load the Vietnamese SBERT model
def preload_relenvancy_model():
    return SentenceTransformer("keepitreal/vietnamese-sbert")


model = preload_relenvancy_model()


def calculate_the_similarity_score(embedding1, embedding2):
    return np.dot(embedding1, embedding2) / (
        np.linalg.norm(embedding1) * np.linalg.norm(embedding2)
    )


def get_the_similarity_score(sentence1, sentence2):
    # Encode the sentences
    embedding1 = model.encode([sentence1])[0]
    embedding2 = model.encode([sentence2])[0]

    # Calculate the cosine similarity
    similarity_score = calculate_the_similarity_score(embedding1, embedding2)

    return round(float(similarity_score), 3)
