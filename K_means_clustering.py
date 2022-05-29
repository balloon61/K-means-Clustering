import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import cv2


# my data structure to save data
class cluster:

    def __init__(self):
        self.point = []
        self.cluster_number = 0
        self.r = []
        self.g = []
        self.b = []

    # change its cluster
    def change_cluster(self, c):
        self.cluster_number = c

    # get the point and also save the rbg values
    def get_point(self, point):
        self.point.append(point)
        self.r.append(point[0])
        self.g.append(point[1])
        self.b.append(point[2])


# Compute the distance
def distance(dx, dy, dz):
    return np.sqrt(dx * dx + dy * dy + dz * dz)


if __name__ == '__main__':
    # input image
    img = cv2.imread("image.png")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # split the iamge rgb
    r, g, b = cv2.split(img)
    # let r, g, b be (xxx, 1) matrix
    r = r.flatten()
    g = g.flatten()
    b = b.flatten()  # plotting

    data = []
    # put it rgb data in a list data
    for i in range(len(r)):
        temp = []
        temp.append(r[i])
        temp.append(g[i])
        temp.append(b[i])
        data.append(temp)
    # initial parameters
    times = 1
    center = []
    final_cluster1 = cluster()
    final_cluster2 = cluster()
    final_cluster3 = cluster()
    final_cluster4 = cluster()

    # run the algorithm
    while True:
        # initial center set up
        if times == 1:
            center.append([0, 0, 0])
            center.append([100, 0, 0])
            center.append([0, 100, 0])
            center.append([0, 0, 100])
            times = 2
        # class initialize
        previous_center = center
        c1 = cluster()
        c2 = cluster()
        c3 = cluster()
        c4 = cluster()
        # go through every points
        for l in range(len(data)):
            minimum = np.sqrt(255 * 255 * 3)  # maximum distance * distance
            which_cluster = 0
            # find which center is cloest to the point
            for j in range(len(center)):

                d = distance(center[j][0] - data[l][0], center[j][1] - data[l][1], center[j][2] - data[l][2])
                if d < minimum:
                    minimum = d
                    which_cluster = j
                # print(d)
            # Assign to the cluster
            if which_cluster == 0:
                c1.get_point(data[l])
                c1.change_cluster(which_cluster)
            elif which_cluster == 1:
                c2.get_point(data[l])
                c2.change_cluster(which_cluster)
            elif which_cluster == 2:
                c3.get_point(data[l])
                c3.change_cluster(which_cluster)
            elif which_cluster == 3:
                c4.get_point(data[l])
                c4.change_cluster(which_cluster)
            # New center

        # calculate new center
        center = []
        x_total = 0
        y_total = 0
        z_total = 0
        if len(c1.point) > 0:

            for k in range(len(c1.point)):
                x_total = c1.point[k][0] + x_total
                y_total = c1.point[k][1] + y_total
                z_total = c1.point[k][2] + z_total
            center.append([x_total / len(c1.point), y_total / len(c1.point), z_total / len(c1.point)])

        x_total = 0
        y_total = 0
        z_total = 0

        if len(c2.point) > 0:
            for k in range(len(c2.point)):
                x_total = c2.point[k][0] + x_total
                y_total = c2.point[k][1] + y_total
                z_total = c2.point[k][2] + z_total
            center.append([x_total / len(c2.point), y_total / len(c2.point), z_total / len(c2.point)])

        x_total = 0
        y_total = 0
        z_total = 0

        if len(c3.point) > 0:

            for k in range(len(c3.point)):
                x_total = c3.point[k][0] + x_total
                y_total = c3.point[k][1] + y_total
                z_total = c3.point[k][2] + z_total
            center.append([x_total / len(c3.point), y_total / len(c3.point), z_total / len(c3.point)])

        x_total = 0
        y_total = 0
        z_total = 0

        if len(c4.point) > 0:
            for k in range(len(c4.point)):
                x_total = c4.point[k][0] + x_total
                y_total = c4.point[k][1] + y_total
                z_total = c4.point[k][2] + z_total
            center.append([x_total / len(c4.point), y_total / len(c4.point), z_total / len(c4.point)])
        print("current center is :", center)
        if previous_center == center:
            final_cluster1 = c1
            final_cluster2 = c2
            final_cluster3 = c3
            final_cluster4 = c4
            break
    print("cluster center is :", center)
    # set up color
    colors = ["#0000FF", "#00FF00", "#FF0066", "#000066"]
    fig = plt.figure()
    # plot the K-means figure
    ax = Axes3D(fig)
    ax.scatter(final_cluster1.r, final_cluster1.g, final_cluster1.b, color=colors[0])
    ax.scatter(final_cluster2.r, final_cluster2.g, final_cluster2.b, color=colors[1])
    ax.scatter(final_cluster3.r, final_cluster3.g, final_cluster3.b, color=colors[2])
    ax.scatter(final_cluster4.r, final_cluster4.g, final_cluster4.b, color=colors[3])

    plt.show()
