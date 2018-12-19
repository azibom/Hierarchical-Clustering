# Hierarchical-Clustering
Hierarchical Clustering

#### Hierarchical clustering involves creating clusters that have a predetermined ordering from top to bottom. For example, all files and folders on the hard disk are organized in a hierarchy. There are two types of hierarchical clustering, Divisive and Agglomerative.

## Agglomerative method :fire:
In agglomerative or bottom-up clustering method we assign each observation to its own cluster. Then, compute the similarity (e.g., distance) between each of the clusters and join the two most similar clusters. Finally, repeat steps 2 and 3 until there is only a single cluster left.

```python
# import requirements
from scipy.cluster.hierarchy import linkage,dendrogram,fcluster
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
# load data
iris = load_iris()
# this chart can show you how this algoritm work
plt.subplot(1,2,1)
hierachical = linkage(iris.data,method='complete')
dendrogram(hierachical)
# we "fcluster" you can choose the depth of clustering (in this case we set 3 as depth)
plt.subplot(1,2,2)
labels = fcluster(hierachical, 3, criterion='distance')
plt.scatter(iris.data[:,0], iris.data[:,2], c=labels)

plt.show()
```

#### it is nice to run it yourself and see the result

I hope this article will be useful to you.
