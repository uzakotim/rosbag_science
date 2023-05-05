from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas
def closest(l, R):

    from operator import itemgetter

    tupleList = zip(l,  [ abs(x - R) for x in l ])

    closeToR, delta  = sorted(tupleList, key=itemgetter(1)).pop(0)

    return closeToR  



points1 = pandas.read_csv("./main_results_uav4/main.bag_slow_odom_uav4.csv")
points2 = pandas.read_csv("./main_results_uav8/main.bag_slow_odom_uav8.csv")
points3 = pandas.read_csv("./main_results_uav11/main.bag_slow_odom_uav11.csv")
centroid = pandas.read_csv("./main_centroid_uav4/main.bag_centroid_uav4.csv")

t4 = centroid['time'].values
 
counter= 0
for el in t4:
# closest time stamp in points 1
    timestamp = closest(points1['time'].values,el)
    check = points1.loc[points1['time'] == timestamp]['time'].values[0]
    if timestamp == check:
        print("alright")
    current_value_from_sf = centroid.loc[centroid['time'] == el]['x'].values[0]
    if (current_value_from_sf != -10000000000.0):
        print(current_value_from_sf)
    counter +=1
    if counter > 9:
        break
#print(len(t1),len(t2),len(t3),len(t4))

