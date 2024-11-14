import csv

def read_lower_triangular(file):
    distMat = []
    with open(file, 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            distMat.append([float(value) for value in row])
    n = len(distMat)
    tdistmat =[[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(0,i+1):
            tdistmat[i][j] = distMat[i][j]
            tdistmat[j][i] = tdistmat[i][j]
    return tdistmat

def find_closest_clusters(distMat):

    n = len(distMat)
    min_dist = float('inf')
    closest_pair = (0, 0)
    
    for i in range(1, n):
        for j in range(i):
            if distMat[i][j] < min_dist:
                min_dist = distMat[i][j]
                closest_pair = (i, j)
                
    return closest_pair

def update_distance_matrix(distMat, c1, c2):
  
    n = len(distMat)
    newDistMat = [[distMat[i][j] for j in range(len(distMat))] for i in range(len(distMat))]
    
    for i in range(n):
        if i not in (c1,c2):
            newDistMat[i][c1] = min(newDistMat[i][c1],newDistMat[i][c2])
            newDistMat[c1][i] = newDistMat[i][c1]
    del newDistMat[c2]
    for row in newDistMat:
        del row[c2]

    return newDistMat

def hierarchical_clustering(distMat):

    n = len(distMat)
    clusters = [[i] for i in range(n)]
    
    print("Initial Clusters:", clusters)
    step = 1
    
    while len(clusters) > 1:
       
        c1, c2 = find_closest_clusters(distMat)
        
       
        new_cluster = clusters[c1] + clusters[c2]
        min_ind, max_ind = min(c1, c2), max(c1, c2)
        
       
        clusters[min_ind] = new_cluster
        del clusters[max_ind]
        
        print(f"\nStep {step}: Merged clusters {c1} and {c2} -> New Cluster: {new_cluster}")
        print("Clusters after merge:", clusters)

        distMat = update_distance_matrix(distMat, c1, c2)
        
        print("Updated Distance Matrix:")
        for row in distMat:
            print(row)
        
        step += 1
    
    return clusters

file = 'C:/Users/nalaw/OneDrive/Desktop/dm/hard/single/code.csv'
distMat = read_lower_triangular(file)
print("Initial Distance Matrix:")
for row in distMat:
    print(row)

final_clusters = hierarchical_clustering(distMat)
print("\nFinal Cluster:", final_clusters)
