import cudf
import cugraph

# Input data as edge pairs defined by source and destination vertices
data = {'src': [1,2,3,4,5,6,7,8,10,11,12,13,17,19,21,31,2,3,7,13,17,19,21,30,3,7,8,9,13,27],
        'dst': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,2,2,2,2,2,2]}
gdf = cudf.DataFrame(data)

# Build the Graph
G = cugraph.Graph()
G.from_cudf_edgelist(gdf, source='src', destination='dst')

# Calculate the PageRank score of each vertex
df_page = cugraph.pagerank(G)

# Print the top 10 PageRank scores
print(df_page.sort_values('pagerank', ascending=False).head(10))

