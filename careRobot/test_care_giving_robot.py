import unittest
from caregiving_robot_ml import CareGivingRobot

class TestCareGivingRobot(unittest.TestCase):
    def setUp(self):
        self.robot = CareGivingRobot("TestBot")

    def test_remind_medication(self):
        self.robot.remind_medication('08:00')
        self.robot.remind_medication('20:00')
        # Output should indicate medication reminders

    def test_fall_detection_and_alert(self):
        # Force fall detection to True for test
        self.robot.send_alert()
        self.assertTrue(self.robot.alert_sent)

if __name__ == '__main__':
    unittest.main()