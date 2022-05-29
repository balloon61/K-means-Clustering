# K-means-Clustering
K-means Clustering


Step:
a. First select 4 points as the center, I selected (0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255).
b. Calculate the distance of each data to every center points. Reason: to determine which points belong to which clusters.
c. Assign all the data points to the closest center (cluster). The criterion is based on Euclidean Norm (minimum distance)
d. obtain the new center by calculate the average of all points in the cluster. Reason: to find the better center for this image.
e. Repeat step b to step d, until the distance is not changing anymore.  

![image](https://user-images.githubusercontent.com/55338365/170852841-8149f0d8-ac2e-41ef-900d-85b4612d9818.png)
Fig 1. RGB data distribution
![image](https://user-images.githubusercontent.com/55338365/170852852-d3aca47f-f6ed-47e8-b273-7651d54ada6e.png)
Fig 2. K-means seperation

Result:
cluster center are (r,g,b): 
(2.3345849089378534, 6.993332353452077, 11.283528641483718), 
(125.31497005988024, 55.64690618762475, 32.60738522954092), 
(44.59896640826874, 210.76227390180878, 194.38811369509045), 
(13.698238617480891, 46.88611941951922, 53.432148000443114)

















