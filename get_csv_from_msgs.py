import sys
import os
import csv
import rosbag
import rospy

##################
# DESCRIPTION:
# Creates CSV files of the robot joint states from a rosbag (for visualization with e.g. pybullet)
# 
# USAGE EXAMPLE:
# rosrun your_package get_jstate_csvs.py /root/catkin_ws/bagfiles your_bagfile.bag
# ##################

filename = "main.bag"
directory = "./uav04"
print("Reading the rosbag file")
if not directory.endswith("/"):
  directory += "/"
extension = ""
if not filename.endswith(".bag"):
  extension = ".bag"
bag = rosbag.Bag(directory + filename + extension)

# Create directory with name filename (without extension)
results_dir = directory + filename[:-4] + "_results"
if not os.path.exists(results_dir):
  os.makedirs(results_dir)

print("Writing robot joint state data to CSV")

with open(results_dir +"/"+filename+'_slow_odom_uav8.csv', mode='w') as data_file:
  data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
  #data_writer.writerow(['time', 'robot_elbow_joint', 'robot_shoulder_lift_joint', 
  #'robot_shoulder_pan_joint', 'robot_wrist_1_joint', 'robot_wrist_2_joint', 'robot_wrist_3_joint'])
  # Get all message on the /joint states topic
  for topic, msg, t in bag.read_messages(topics=['/uav8/odometry/slow_odom']):
    # Only write to CSV if the message is for our robot
      pose_x = msg.pose.pose.position.x
      pose_y = msg.pose.pose.position.y
      pose_z = msg.pose.pose.position.z
      data_writer.writerow([t, pose_x, pose_y, pose_z])

print("Finished creating csv file!")
bag.close()

