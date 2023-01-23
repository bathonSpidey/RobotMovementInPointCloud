import unittest
from RobotControllerClient import RobotControllerClient


class ClientTests(unittest.TestCase):
    def setUp(self):
        self.client = RobotControllerClient()

    def test_get_angles(self):
        result = self.client.get_angles()
        self.assertGreaterEqual(len(result), 5)

    def test_move_to(self):
        currentAngles = self.client.get_angles()
        self.client.move_to([90])
        self.assertNotEqual(currentAngles, self.client.get_angles())



if __name__ == '__main__':
    unittest.main()
