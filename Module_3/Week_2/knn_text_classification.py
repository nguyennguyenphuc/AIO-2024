import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.neighbors import KNeighborsRegressor
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline

from sklearn.metrics import mean_squared_error, r2_score

# Load IMDB dataset from CSV
data = pd.read_csv(r'./data/IMDB-Movie-Data.csv')

# Convert text data (Description) using Bag of Words (BoW)
vectorizer = CountVectorizer(max_features=1000)
X_text_bow = vectorizer.fit_transform(data['Description']).toarray()

# OneHotEncode categorical data (Genre, Director, Actors)
encoder = OneHotEncoder(sparse_output=False)

# Apply OneHotEncoder to each categorical feature individually
X_genre_encoded = encoder.fit_transform(data[['Genre']])
X_director_encoded = encoder.fit_transform(data[['Director']])
X_actors_encoded = encoder.fit_transform(data[['Actors']])

# Combine the encoded categorical features
X_encoded = np.hstack([X_genre_encoded, X_director_encoded, X_actors_encoded])

# Select numerical features and reshape them to 2D
X_year = data['Year'].values.reshape(-1, 1)
X_runtime = data['Runtime (Minutes)'].values.reshape(-1, 1)
X_votes = data['Votes'].values.reshape(-1, 1)
X_revenue = data['Revenue (Millions)'].fillna(
    0).values.reshape(-1, 1)  # Fill missing revenue values with 0
X_rating = data['Rating'].values.reshape(-1, 1)

# Combine all features: text (BoW), categorical, and numerical
X_combined = np.hstack((
    X_text_bow,
    X_encoded,
    X_year,
    X_runtime,
    X_votes,
    X_revenue,
    X_rating
))

# Check final shape of the combined features
print("Shape of X_combined:", X_combined.shape)

# Target variable (Metascore), filling missing values with 0
y = data['Metascore'].fillna(0)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X_combined, y, test_size=0.2, random_state=42)


# Apply PCA to reduce feature dimensions
# Start with 50 principal components
pca = PCA(n_components=50, random_state=42)

# Build a pipeline including StandardScaler, PCA, and KNN Regressor
pipeline = Pipeline([
    ('scaler', StandardScaler()),  # Standardize the data
    ('pca', pca),                  # Apply PCA
    ('knn', KNeighborsRegressor(n_neighbors=10))  # Use KNN with K=10
], memory=None)


# Train the pipeline on the training data
pipeline.fit(X_train, y_train)

# Predict on the test data
y_pred_pca = pipeline.predict(X_test)

# Evaluate the model with PCA
mse_pca = mean_squared_error(y_test, y_pred_pca)
r2_pca = r2_score(y_test, y_pred_pca)
mse = mean_squared_error(y_test, y_pred_pca)
r2 = r2_score(y_test, y_pred_pca)

# Print evaluation results
print("Result with PCA, K=10")
print(f"Mean Squared Error: {mse}")
print(f"R² Score: {r2}")


# Scale the features using StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# Don't use PCA
# Build KNN Regressor with 5 neighbors
knn_regressor = KNeighborsRegressor(n_neighbors=5)
knn_regressor.fit(X_train, y_train)

# Predict the test set
y_pred = knn_regressor.predict(X_test)

# Evaluate using Mean Squared Error (MSE) and R² Score
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print evaluation results
print("Result with non PCA, K=10")
print(f"Mean Squared Error: {mse}")
print(f"R² Score: {r2}")
