from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas
import csv
from math import sqrt,exp
def closest(l, R):

    from operator import itemgetter

    tupleList = zip(l,  [ abs(x - R) for x in l ])

    closeToR, delta  = sorted(tupleList, key=itemgetter(1)).pop(0)

    return closeToR  

points1 = pandas.read_csv("./main_results_uav4/_blob_det_v2_points_uav4.csv")
points2 = pandas.read_csv("./main_results_uav8/_blob_det_v2_points_uav8.csv")
points3 = pandas.read_csv("./main_results_uav11/_blob_det_v2_points_uav11.csv")

t3 = points3['time'].values

with open('./points.csv', mode='w') as data_file:
    data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    data_writer.writerow(['time', 'x_uav4','y_uav4','z_uav4','x_uav8','y_uav8','z_uav8','x_uav11','y_uav11','z_uav11'])
    for el in t3:
    # closest time stamp in points 1
        timestamp_1 = closest(points1['time'].values,el)
        timestamp_2 = closest(points2['time'].values,el)
        timestamp_3 = el
        
        x_1 = points1.loc[points1['time'] == timestamp_1]['x'].values[0]
        y_1 = points1.loc[points1['time'] == timestamp_1]['y'].values[0]
        z_1 = points1.loc[points1['time'] == timestamp_1]['z'].values[0]
        
        x_2 = points2.loc[points2['time'] == timestamp_2]['x'].values[0]
        y_2 = points2.loc[points2['time'] == timestamp_2]['y'].values[0]
        z_2 = points2.loc[points2['time'] == timestamp_2]['z'].values[0]


        x_3 = points3.loc[points3['time'] == timestamp_3]['x'].values[0]
        y_3 = points3.loc[points3['time'] == timestamp_3]['y'].values[0]
        z_3 = points3.loc[points3['time'] == timestamp_3]['z'].values[0]

        data_writer.writerow([el, x_1,y_1,z_1,x_2,y_2,z_2,x_3,y_3,z_3])
print("Finished!")