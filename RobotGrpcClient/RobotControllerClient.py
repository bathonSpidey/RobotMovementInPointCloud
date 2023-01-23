import grpc
import robot_pb2_grpc as pb2_grpc
import robot_pb2 as pb2

class RobotControllerClient(object):
    def __init__(self):
        self.host = "localhost"
        self.server_port = 5230
        self.channel = grpc.insecure_channel(f'{self.host}:{self.server_port}')
        self.stub = pb2_grpc.RobotControllerServerStub(self.channel)

    def get_angles(self, message=""):
        message = pb2.CurrentAnglesRequest(angles=message)
        result = self.stub.GetAngles(message)
        return [float(value) for value in result.angles.split(', ')]

    def move_to(self, message):
        message = pb2.MotorAnglesRequest(angles=message)
        return self.stub.Move(message)

"""
if __name__ == "__main__":
    client = RobotControllerClient()
    result = client.get_angles("")
    print(result)
    client.move_to([45.0])"""
