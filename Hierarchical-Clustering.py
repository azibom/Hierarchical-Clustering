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
