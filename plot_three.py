from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas

points1 = pandas.read_csv("./main_results_uav4/main.bag_slow_odom_uav4.csv")
points2 = pandas.read_csv("./main_results_uav8/main.bag_slow_odom_uav8.csv")
points3 = pandas.read_csv("./main_results_uav11/main.bag_slow_odom_uav11.csv")

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
# first points


x = points1['x'].values[:10]
y = points1['y'].values[:10]
z = points1['z'].values[:10]

ax.scatter(x,y,z,c='orange',marker ='o')
x = points2['x'].values[:10]
y = points2['y'].values[:10]
z = points2['z'].values[:10]

ax.scatter(x,y,z,c='orange',marker ='o')
x = points3['x'].values[:10]
y = points3['y'].values[:10]
z = points3['z'].values[:10]

ax.scatter(x,y,z,c='orange',marker ='o',label="Start")

#all other points

x = points1['x'].values[10:-10]
y = points1['y'].values[10:-10]
z = points1['z'].values[10:-10]

ax.scatter(x,y,z,c='r',marker ='o',label="uav4")
x = points2['x'].values[10:-10]
y = points2['y'].values[10:-10]
z = points2['z'].values[10:-10]

ax.scatter(x,y,z,c='b',marker ='o',label="uav8")
x = points3['x'].values[10:-10]
y = points3['y'].values[10:-10]
z = points3['z'].values[10:-10]

ax.scatter(x,y,z,c='g',marker ='o',label="uav11")

#last point

x = points1['x'].values[-10:-1]
y = points1['y'].values[-10:-1]
z = points1['z'].values[-10:-1]

ax.scatter(x,y,z,c='black',marker ='o')
x = points2['x'].values[-10:-1]
y = points2['y'].values[-10:-1]
z = points2['z'].values[-10:-1]

ax.scatter(x,y,z,c='black',marker ='o')
x = points3['x'].values[-10:-1]
y = points3['y'].values[-10:-1]
z = points3['z'].values[-10:-1]

ax.scatter(x,y,z,c='black',marker ='o',label="Finish")

plt.legend(loc="upper left")
plt.title("3D pathes during the experiment")
plt.show()
