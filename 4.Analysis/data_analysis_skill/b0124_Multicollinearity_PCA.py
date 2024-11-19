import pandas as pd
# pip install scikit-learn
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

data = {
    'Feature_1': [1, 2, 3, 4, 5],
    'Feature_2': [2, 4, 6, 8, 10],
    'Feature_3': [5, 3, 4, 2, 1]
}
df = pd.DataFrame(data)

print("Org Data:")
print(df)

# Step 1: Data normalization (scaling required before applying PCA)
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

# Step 2: Apply PCA
pca = PCA(n_components=2)  # Set the number of principal components to 2
pca_result = pca.fit_transform(scaled_data)

# Step 3: Convert the result to a DataFrame
pca_df = pd.DataFrame(pca_result, columns=['PC1', 'PC2'])
print("Data after PCA conversion:")
print(pca_df)

# Step 4: Check the described variance
print("Percentage of variance explained:")
print(pca.explained_variance_ratio_)
