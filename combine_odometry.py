from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas
import csv
from math import sqrt
def closest(l, R):

    from operator import itemgetter

    tupleList = zip(l,  [ abs(x - R) for x in l ])

    closeToR, delta  = sorted(tupleList, key=itemgetter(1)).pop(0)

    return closeToR  

def quadratic_distance(x,y,z,x_c,y_c,z_c):
    return sqrt((x-x_c)**2 +(y-y_c)**2 +(z-z_c)**2)

def quadratic_distance2(x,y,x_c,y_c):
    return sqrt((x-x_c)**2 +(y-y_c)**2 )
simulation = True
if simulation:
    simul = '_simulation'
else:
    simul = ''
if simulation:
    points1 = pandas.read_csv("./simulation_results_uav4/main.bag_slow_odom_uav4.csv")
    points2 = pandas.read_csv("./simulation_results_uav8/main.bag_slow_odom_uav8.csv")
    points3 = pandas.read_csv("./simulation_results_uav11/main.bag_slow_odom_uav11.csv")
    centroid = pandas.read_csv("./simulation_centroid_uav4/main.bag_centroid_uav4.csv")
else:
    points1 = pandas.read_csv("./main_results_uav4/main.bag_slow_odom_uav4.csv")
    points2 = pandas.read_csv("./main_results_uav8/main.bag_slow_odom_uav8.csv")
    points3 = pandas.read_csv("./main_results_uav11/main.bag_slow_odom_uav11.csv")
    centroid = pandas.read_csv("./main_centroid_uav4/main.bag_centroid_uav4.csv")
t4 = centroid['time'].values
last_centroid = [0,0,0]
with open('./distances'+simul+'.csv', mode='w') as data_file:
    data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    data_writer.writerow(['time', 'uav4', 'uav8', 'uav11'])

    for el in t4:
    # closest time stamp in points 1
        timestamp_1 = closest(points1['time'].values,el)
        timestamp_2 = closest(points2['time'].values,el)
        timestamp_3 = closest(points3['time'].values,el)
        
        x_1 = points1.loc[points1['time'] == timestamp_1]['x'].values[0]
        y_1 = points1.loc[points1['time'] == timestamp_1]['y'].values[0]
        z_1 = points1.loc[points1['time'] == timestamp_1]['z'].values[0]
        
        x_2 = points2.loc[points2['time'] == timestamp_2]['x'].values[0]
        y_2 = points2.loc[points2['time'] == timestamp_2]['y'].values[0]
        z_2 = points2.loc[points2['time'] == timestamp_2]['z'].values[0]


        x_3 = points3.loc[points3['time'] == timestamp_3]['x'].values[0]
        y_3 = points3.loc[points3['time'] == timestamp_3]['y'].values[0]
        z_3 = points3.loc[points3['time'] == timestamp_3]['z'].values[0]


        x_c = centroid.loc[centroid['time'] == el]['x'].values[0]
        y_c = centroid.loc[centroid['time'] == el]['y'].values[0]
        z_c = centroid.loc[centroid['time'] == el]['z'].values[0]
        # check = points1.loc[points1['time'] == timestamp]['time'].values[0]
        # if timestamp == check:
            # print("alright")
        # current_value_from_sf = centroid.loc[centroid['time'] == el]['x'].values[0]
        if (x_c != -10000000000.0):
            last_centroid = [x_c,y_c,z_c]
            # found centroid
        else:
            [x_c,y_c,z_c] = last_centroid
        
        dist1 = quadratic_distance(x_1,y_1,z_1,x_c,y_c,z_c)
        dist2 = quadratic_distance(x_2,y_2,z_2,x_c,y_c,z_c)
        dist3 = quadratic_distance(x_3,y_3,z_3,x_c,y_c,z_c)
        data_writer.writerow([el, dist1, dist2, dist3])
print("Finished!")