import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from quantum_model import quantum_similarity

df = pd.read_csv("data/movies.csv")

def recommend_movies(user_prefs, top_k=5):
    user_vec = [user_prefs["Action"], user_prefs["Romance"]]
    movie_features = df[["Action", "Romance"]].values

    df["classical_score"] = cosine_similarity([user_vec], movie_features)[0]

    q_scores = []
    for _, row in df.iterrows():
        movie_vec = [row["Action"], row["Romance"]]
        q_scores.append(quantum_similarity(user_vec, movie_vec))
    df["quantum_score"] = q_scores

    df["final_score"] = 0.7*df["classical_score"] + 0.3*df["quantum_score"]
    return df.sort_values("final_score", ascending=False).head(top_k)
