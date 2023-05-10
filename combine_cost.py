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

def quadratic_distance(x,y,z,x_c,y_c,z_c):
    return sqrt((x-x_c)**2 +(y-y_c)**2 +(z-z_c)**2)

def quadratic_distance2(x,y,x_c,y_c):
    return sqrt((x-x_c)**2 +(y-y_c)**2 )
def cost(x,y,x_prev,y_prev,goal_y,goal_x,obs_x,obs_y,obs_2_x,obs_2_y):
	height       = 5
	width_goal   = 25
	width_obst   = 4
	goal_depth   = 5
	obst_weight  = 25
	return 8*(x-x_prev)**2 + 8*(y-y_prev)**2 + (y-goal_y)**2 + (x-goal_x)**2 + height + obst_weight*exp(-((y-obs_y)**2)/width_obst)*exp(-((x-obs_x)**2)/width_obst)+ exp(-((y-obs_2_y)**2)/width_obst)*exp(-((x-obs_2_x)**2)/width_obst) - goal_depth*exp(-((x-goal_x)**2)/width_goal)*exp(-((y-goal_y)**2)/width_goal)
simulation = True

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
if simulation:
    simul = '_simulation'
else:
    simul = ''
with open('./costs'+ simul +'.csv', mode='w') as data_file:
    data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    data_writer.writerow(['time', 'uav4', 'uav8', 'uav11'])
    first = True
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
        if not first:
            cuav4 = cost(x_1,y_1,x_1_prev,y_1_prev,y_c,x_c,x_2,y_2,x_3,y_3)
            cuav8 = cost(x_2,y_2,x_2_prev,y_2_prev,y_c,x_c,x_1,y_1,x_3,y_3)
            cuav11 = cost(x_3,y_3,x_3_prev,y_3_prev,y_c,x_c,x_1,y_1,x_2,y_2)
            data_writer.writerow([el, cuav4,cuav8,cuav11])
        else:
            first = False
        x_1_prev = x_1
        y_1_prev = y_1
        z_1_prev = z_1
        
        x_2_prev = x_2
        y_2_prev = y_2
        z_2_prev = z_2
        
        x_3_prev = x_3
        y_3_prev = y_3
        z_3_prev = z_3
print("Finished!")