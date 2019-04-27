from scripts import*
import numpy as np
import pandas
import matplotlib.pyplot as plt

if __name__ == "__main__":
    testing = True
    if not testing:
        generate_data = input("Would you like to generate data? (Yes or No)")

        if generate_data.lower() in ['yes', 'y']:
            dimensions = input("Enter the dimensions for your data. (eg. 3 3 3 would be a 3 by 3 by 3 matrix)")

    # test = numpy.random.randint(0, 10, size=(2, 5))
    # test1 = numpy.random.randint(0, 10, size=(2, 5))
    # test2 = numpy.random.randint(0, 10, size=(2, 5))
    # test3 = numpy.random.randint(0, 10, size=(2, 3))
    # print(test)
    #
    # plt.scatter(test[0], test[1], c='green')
    # plt.scatter(test1[0], test1[1], c='red')
    # plt.scatter(test2[0], test2[1], c='blue')
    # plt.scatter(test3[0], test3[1], c='orange', s=500)
    # plt.show()
    random_data = np.random.randint(0, 100, size=(2, 50))
    Node_Mapper = np.vectorize(Node)
    Nodes = Node_Mapper(random_data[0], random_data[1])
    print()
    dist_test = np.vectorize(distance)

    k = 3
    k_centroids = np.random.randint(0, 100, size=(2, k))
    centroid1 = Centroid([], Node(k_centroids[0][0], k_centroids[1][0]), k_centroids[0][0], k_centroids[1][0], centroid_color='blue', node_color='blue')
    centroid2 = Centroid([], Node(k_centroids[0][1], k_centroids[1][1]), k_centroids[0][1], k_centroids[1][1], centroid_color='red', node_color='red')
    centroid3 = Centroid([], Node(k_centroids[0][2], k_centroids[1][2]), k_centroids[0][2], k_centroids[1][2], centroid_color='yellow', node_color='yellow')
    Centroids = list([centroid1, centroid2, centroid3])

    tester = [np.argmin(dist_test(i, Centroids)) for i in Nodes]
    print()


    print()

    print()
