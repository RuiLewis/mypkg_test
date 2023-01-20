import rclpy
from rclpy.node import Node
from std_msgs.srv import Query

def cb(request, response):
    if request.name == "Rui":
        response.age = 22
    else:
        response.age = 0
    
    return response

rclpy.init()
node = Node("talker")
srv = node.create_service(Query, "query", cb)
rclpy.spin(node)


