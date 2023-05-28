import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

def load_dataset(file_path):
    df = pd.read_csv(file_path) # Select relevant columns
    df = df[['title', 'genre', 'description']] # Remove rows with missing values
    df = df.dropna()
    df['description'] = df['description'].str.lower()
    return df

def vectorize_text(descriptions):
    # Initialize TF-IDF vectorizer
    tfidf = TfidfVectorizer(stop_words='english')
    # Apply TF-IDF vectorization to descriptions
    tfidf_matrix = tfidf.fit_transform(descriptions)
    return tfidf_matrix

def compute_similarity_scores(tfidf_matrix):
    cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)
    return cosine_similarities

def get_movie_suggestions(mood, df, cosine_similarities, num_suggestions=5):
    # Find index of movies with matching genre
    indices = df[df['genre'].str.contains(mood, case=False)].index
    # Compute similarity scores for the matching movies
    similarity_scores = list(enumerate(cosine_similarities[indices]))
    # Sort movies based on similarity scores
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    # Get top movie suggestions
    top_movies = [df['title'][i] for i, _ in similarity_scores[:num_suggestions]]
    return top_movies

def main():
    dataset_path = 'imdb_dataset.csv'
    df = load_dataset(dataset_path)
    tfidf_matrix = vectorize_text(df['description'])
    # Compute similarity scores
    cosine_similarities = compute_similarity_scores(tfidf_matrix)
    # Test movie suggestions
    mood = 'action'
    suggestions = get_movie_suggestions(mood, df, cosine_similarities)
    print(f"Movie Suggestions for {mood}:\n")
    for movie in suggestions:
        print(movie)

if __name__ == '__main__':
    main()