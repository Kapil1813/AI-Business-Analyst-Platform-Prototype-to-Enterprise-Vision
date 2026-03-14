from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

stored_requests = [
    "portfolio risk dashboard",
    "trading data integration platform",
    "multi asset performance analytics",
    "market exposure monitoring tool"
]

def find_similar(new_request):

    embeddings = model.encode(stored_requests + [new_request])

    similarity = cosine_similarity(
        [embeddings[-1]],
        embeddings[:-1]
    )

    return similarity[0]