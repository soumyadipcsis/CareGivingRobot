import time

class CareGivingRobot:
    def __init__(self, name):
        self.name = name
        self.medication_schedule = {'08:00': 'Blood Pressure Pill', '20:00': 'Cholesterol Pill'}
        self.meal_times = ['07:30', '12:30', '18:30']
        self.hydration_interval = 2  # hours
        self.appointments = []
        self.alert_sent = False

    def remind_medication(self):
        print(f"{self.name}: Would you like to set or hear your medication reminders? (set/hear/skip)")
        choice = input().strip().lower()
        if choice == 'set':
            time_str = input("Enter medication time (HH:MM): ").strip()
            med = input("Enter medication name: ").strip()
            self.medication_schedule[time_str] = med
            print(f"{self.name}: Medication reminder set for {time_str} - {med}.")
        elif choice == 'hear':
            for t, med in self.medication_schedule.items():
                print(f"{self.name}: At {t}, take your {med}.")
        else:
            print(f"{self.name}: No medication reminders this time.")

    def check_fall(self):
        print(f"{self.name}: Would you like to simulate a fall detection now? (yes/no)")
        choice = input().strip().lower()
        if choice == 'yes':
            print(f"{self.name}: Fall detected! Sending alert and contacting caregiver.")
            self.send_alert()
        else:
            print(f"{self.name}: No falls detected. Stay safe!")

    def meal_reminder(self):
        print(f"{self.name}: Would you like to set or hear your meal times? (set/hear/skip)")
        choice = input().strip().lower()
        if choice == 'set':
            times = input("Enter meal times separated by commas (e.g., 07:30,12:30,18:30): ").strip()
            self.meal_times = [t.strip() for t in times.split(',')]
            print(f"{self.name}: Meal times set: {', '.join(self.meal_times)}.")
        elif choice == 'hear':
            print(f"{self.name}: Your meal times are: {', '.join(self.meal_times)}.")
        else:
            print(f"{self.name}: Meal reminders skipped.")

    def hydration_check(self):
        print(f"{self.name}: Would you like regular hydration reminders? (yes/no)")
        choice = input().strip().lower()
        if choice == 'yes':
            interval = input("How often (in hours) should I remind you to drink water? ").strip()
            try:
                self.hydration_interval = int(interval)
                print(f"{self.name}: Hydration reminder set every {self.hydration_interval} hours.")
            except ValueError:
                print(f"{self.name}: Invalid input. Keeping previous interval of {self.hydration_interval} hours.")
        else:
            print(f"{self.name}: Hydration reminders skipped.")

    def appointment_reminder(self):
        print(f"{self.name}: Would you like to add or hear your appointments? (add/hear/skip)")
        choice = input().strip().lower()
        if choice == 'add':
            time_str = input("Enter appointment time (YYYY-MM-DD HH:MM): ").strip()
            desc = input("Enter appointment description: ").strip()
            self.appointments.append((time_str, desc))
            print(f"{self.name}: Appointment added for {time_str} - {desc}.")
        elif choice == 'hear':
            if self.appointments:
                print(f"{self.name}: Your upcoming appointments:")
                for t, desc in self.appointments:
                    print(f" - {t}: {desc}")
            else:
                print(f"{self.name}: No appointments set.")
        else:
            print(f"{self.name}: Appointment reminders skipped.")

    def emergency_call(self):
        print(f"{self.name}: Do you need to make an emergency call? (yes/no)")
        choice = input().strip().lower()
        if choice == 'yes':
            contact = input("Enter emergency contact name: ").strip()
            print(f"{self.name}: Calling {contact} and notifying emergency services!")
        else:
            print(f"{self.name}: Emergency call not initiated.")

    def wellness_check(self):
        print(f"{self.name}: Would you like a wellness check? (yes/no)")
        choice = input().strip().lower()
        if choice == 'yes':
            mood = input("How are you feeling today? (good/okay/bad): ").strip().lower()
            if mood == 'good':
                print(f"{self.name}: That's great! Keep smiling.")
            elif mood == 'okay':
                print(f"{self.name}: If you need anything or feel unwell, let me know.")
            elif mood == 'bad':
                print(f"{self.name}: I'm here for you. Would you like me to notify your caregiver? (yes/no)")
                notify = input().strip().lower()
                if notify == 'yes':
                    self.send_alert()
                else:
                    print(f"{self.name}: If you change your mind, just ask for help.")
            else:
                print(f"{self.name}: Thank you for sharing. Remember, I'm always here to help!")
        else:
            print(f"{self.name}: Skipping wellness check.")

    def daily_activity_suggestion(self):
        print(f"{self.name}: Would you like a suggestion for a daily activity? (yes/no)")
        choice = input().strip().lower()
        if choice == 'yes':
            activity = input("Do you prefer (physical/mental/social) activity today? ").strip().lower()
            suggestion = {
                'physical': "A short walk or gentle stretching.",
                'mental': "A puzzle, book, or memory game.",
                'social': "Calling a friend or joining a video chat group."
            }.get(activity, "Listening to music or meditating.")
            print(f"{self.name}: Suggested activity: {suggestion}")
        else:
            print(f"{self.name}: No activity suggestion for now.")

    def send_alert(self):
        self.alert_sent = True
        print(f"{self.name}: Alert sent to caregiver!")

    def interactive_routine(self):
        print(f"{self.name}: Hello! I am here to assist you.")
        options = [
            ("Medication reminders", self.remind_medication),
            ("Fall detection", self.check_fall),
            ("Meal reminders", self.meal_reminder),
            ("Hydration checks", self.hydration_check),
            ("Appointment reminders", self.appointment_reminder),
            ("Emergency call", self.emergency_call),
            ("Wellness check", self.wellness_check),
            ("Daily activity suggestion", self.daily_activity_suggestion),
            ("Exit", None)
        ]
        while True:
            print("\nWhat would you like to do?")
            for idx, (desc, _) in enumerate(options, 1):
                print(f"{idx}. {desc}")
            choice = input("Enter your choice (number): ").strip()
            try:
                idx = int(choice) - 1
                if idx == len(options) - 1:
                    print(f"{self.name}: Goodbye! Stay healthy.")
                    break
                else:
                    options[idx][1]()
            except (ValueError, IndexError):
                print(f"{self.name}: Invalid choice. Please enter a number between 1 and {len(options)}.")

if __name__ == "__main__":
    robot = CareGivingRobot("ElderCareBot")
    robot.interactive_routine()