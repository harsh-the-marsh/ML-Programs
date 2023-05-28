# Movie Mood Recommender

This Python code recommends movies based on a user's mood using the IMDb dataset. It leverages TF-IDF vectorization and cosine similarity to find movies with matching genres and similar descriptions.

## Requirements

- Python 3.x
- pandas
- scikit-learn

## Usage

1. Clone the repository:

```
git clone https://github.com/your-username/movie-mood-recommender.git
```

2. Navigate to the project directory:

```
cd movie-mood-recommender
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

4. Place the IMDb dataset (in CSV format) in the project directory.

5. Update the `dataset_path` variable in the `main` function of `movie_recommender.py` with the correct file name.

6. Run the code:

```
python movie_recommender.py
```

7. Enter the mood when prompted (e.g., Action, Comedy, Drama, Horror, Romance).

8. View the suggested movies based on the entered mood.

## Overview

The code performs the following steps:

1. Loads the IMDb dataset, keeping only the relevant columns (title, genre, and description) and removing rows with missing values.
2. Converts the descriptions to lowercase for text processing consistency.
3. Applies TF-IDF vectorization to the movie descriptions using the `TfidfVectorizer` from scikit-learn.
4. Computes cosine similarity scores between the vectorized descriptions using `linear_kernel` from scikit-learn.
5. Takes user input for the mood.
6. Filters movies with matching genres based on the user's mood.
7. Retrieves the similarity scores for the matching movies and sorts them in descending order.
8. Prints the top movie suggestions based on the similarity scores.

Feel free to modify the code to suit your needs and customize the dataset for movie recommendations.

## Dataset

The code assumes the presence of an IMDb dataset in CSV format. The dataset should include the following columns: `title`, `genre`, and `description`. Make sure the dataset is correctly formatted and placed in the project directory before running the code.

## License

This project is licensed under the [MIT License](LICENSE).