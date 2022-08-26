import cuml
import cudf

df = cudf.DataFrame()
df[1] = [1.0, 2.0, 5.0]
df[2] = [4.0, 2.0, 1.0]
df[3] = [4.0, 2.0, 1.0]
                         
kmeans = cuml.KMeans(n_clusters=2)
kmeans.fit(df)

print(kmeans.labels_)
