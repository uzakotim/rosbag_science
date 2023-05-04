import rosbag
bag = rosbag.Bag('../../ctu/uav08/main.bag')
topics = bag.get_type_and_topic_info()[1].keys()
for val in topics:
    print(val)
types = []
for val in bag.get_type_and_topic_info()[1].values():
    types.append(val[0])
