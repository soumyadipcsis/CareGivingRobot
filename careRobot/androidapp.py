from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from fpdf import FPDF

questions = [
    ("How are you feeling today?", ["Good", "Okay", "Bad"]),
    ("Did you sleep well last night?", ["Yes", "No"]),
    ("Have you taken your morning medication?", ["Yes", "No", "Not Applicable"]),
    ("Did you eat breakfast?", ["Yes", "No"]),
    ("Have you had water in the last hour?", ["Yes", "No"]),
    ("Do you feel any pain right now?", ["No", "Mild", "Moderate", "Severe"]),
    ("Are you experiencing shortness of breath?", ["No", "Yes"]),
    ("Do you feel dizzy or lightheaded?", ["No", "Yes"]),
    ("Do you need help with any tasks today?", ["No", "Yes"]),
    ("Do you have any appointments today?", ["No", "Yes"]),
    ("Do you feel safe at home?", ["Yes", "No"]),
    ("Have you spoken to family or friends today?", ["Yes", "No"]),
    ("Would you like a physical activity suggestion?", ["Yes", "No"]),
    ("Would you like a mental activity suggestion?", ["Yes", "No"]),
    ("Would you like a social activity suggestion?", ["Yes", "No"]),
    ("Are you feeling anxious or depressed?", ["No", "A little", "Yes"]),
    ("Do you need assistance with meals?", ["No", "Yes"]),
    ("Did you enjoy your last activity?", ["Yes", "No"]),
    ("Would you like a wellness check call?", ["Yes", "No"]),
    ("Do you have any concerns to share today?", ["No", "Yes"]),
]

class QandA(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.user_name = TextInput(hint_text="Enter your full name", size_hint_y=None, height=40)
        self.user_age = TextInput(hint_text="Enter your age", input_filter='int', size_hint_y=None, height=40)
        self.add_widget(Label(text="Eldercare Q&A", font_size=24, size_hint_y=None, height=50))
        self.add_widget(self.user_name)
        self.add_widget(self.user_age)
        self.q_widgets = []
        self.answers = {}
        scroll = ScrollView(size_hint=(1, 1))
        self.q_box = BoxLayout(orientation='vertical', size_hint_y=None)
        self.q_box.bind(minimum_height=self.q_box.setter('height'))
        for idx, (q, options) in enumerate(questions):
            l = Label(text=q, size_hint_y=None, height=30)
            s = Spinner(text=options[0], values=options, size_hint_y=None, height=40)
            self.q_box.add_widget(l)
            self.q_box.add_widget(s)
            self.q_widgets.append(s)
        scroll.add_widget(self.q_box)
        self.add_widget(scroll)
        self.report_label = Label(text="", size_hint_y=None, height=180)
        self.add_widget(self.report_label)
        self.btn = Button(text="Generate PDF & Show Exhaustive Report", size_hint_y=None, height=50)
        self.btn.bind(on_press=self.generate_report)
        self.add_widget(self.btn)

    def generate_report(self, instance):
        name = self.user_name.text.strip()
        age = self.user_age.text.strip()
        if not name or not age:
            self.report_label.text = "Please enter your name and age."
            return
        self.answers = {}
        for idx, (q, opts) in enumerate(questions):
            self.answers[q] = self.q_widgets[idx].text
        report_text = self.get_exhaustive_report(name, age, self.answers)
        self.report_label.text = "Exhaustive report below.\nPDF saved as 'eldercare_report.pdf' in app folder.\n\n" + report_text[:800] + ('...' if len(report_text) > 800 else '')
        self.save_pdf(report_text, name, age)

    def get_exhaustive_report(self, user_name, user_age, answers):
        report = f"Eldercare Wellbeing Report\nName: {user_name}\nAge: {user_age}\n\n"
        report += f"Dear {user_name},\n\n"
        report += "Here is a thoughtful overview of your day, reflecting on your wellbeing, routines, and opportunities for joyful living.\n\n"

        # Mood & Wellbeing
        mood = answers.get("How are you feeling today?")
        if mood == "Good":
            report += "You started your day with a positive spirit. Keep nurturing this wonderful energy—it truly sets the tone for your wellbeing.\n"
        elif mood == "Okay":
            report += "Your mood is steady today. Remember, it's perfectly normal to have days that feel 'just okay.' Gentle self-care can help lift your spirits.\n"
        else:
            report += "You felt a bit low today. Please be kind to yourself and consider reaching out to someone you trust. You’re never alone on this journey.\n"

        sleep = answers.get("Did you sleep well last night?")
        if sleep == "Yes":
            report += "You enjoyed restful sleep, which is the foundation of good health.\n"
        else:
            report += "It seems sleep was elusive last night. Try a calming bedtime routine tonight—perhaps some gentle music or a favorite book.\n"

        water = answers.get("Have you had water in the last hour?")
        if water == "Yes":
            report += "Wonderful! Staying hydrated keeps your body and mind refreshed.\n"
        else:
            report += "A gentle reminder to sip some water. Hydration helps every part of your body thrive.\n"

        breakfast = answers.get("Did you eat breakfast?")
        if breakfast == "Yes":
            report += "You had breakfast, giving your day a healthy start!\n"
        else:
            report += "Skipping breakfast can leave you low on energy. Try to enjoy even a light morning meal tomorrow.\n"

        # Medication & Health
        med = answers.get("Have you taken your morning medication?")
        if med == "Yes":
            report += "Medication taken—great attention to your health!\n"
        elif med == "No":
            report += "Please remember your medication; it’s important for your daily wellbeing.\n"
        else:
            report += "No medication needed this morning.\n"

        pain = answers.get("Do you feel any pain right now?")
        if pain == "No":
            report += "No pain reported—may your comfort continue.\n"
        elif pain == "Mild":
            report += "Mild pain noticed. Keep an eye on how you feel, and reach out if it worsens.\n"
        elif pain == "Moderate":
            report += "Some discomfort today. Please consider alerting your caregiver, and take time to rest.\n"
        else:
            report += "Severe pain reported. Please seek support or medical advice as soon as possible.\n"

        breath = answers.get("Are you experiencing shortness of breath?")
        if breath == "Yes":
            report += "Breathing feels difficult. Please take extra care and contact your health provider if this continues.\n"
        else:
            report += "Breathing is easy—wonderful to hear.\n"

        dizzy = answers.get("Do you feel dizzy or lightheaded?")
        if dizzy == "Yes":
            report += "Feeling dizzy can be unsettling. Please move slowly and let someone know if this persists.\n"
        else:
            report += "You feel steady and balanced—excellent!\n"

        # Safety, Social, and Activity
        safe = answers.get("Do you feel safe at home?")
        if safe == "Yes":
            report += "Home feels safe and secure. This is so important for your peace of mind.\n"
        else:
            report += "If you don’t feel safe at home, please talk to someone you trust so steps can be taken to support you.\n"

        help_tasks = answers.get("Do you need help with any tasks today?")
        if help_tasks == "Yes":
            report += "You could use a hand today. Remember, asking for help is a sign of strength, not weakness.\n"
        else:
            report += "You feel able to handle your daily tasks—keep it up!\n"

        appointments = answers.get("Do you have any appointments today?")
        if appointments == "Yes":
            report += "You have appointments—be sure to prepare and ask for assistance if needed.\n"
        else:
            report += "No appointments today—time for relaxation or hobbies!\n"

        social = answers.get("Have you spoken to family or friends today?")
        if social == "Yes":
            report += "You connected with loved ones—these moments are so valuable.\n"
        else:
            report += "Consider reaching out to a friend or family member for a quick chat—it can brighten your day.\n"

        # Activity Preferences
        if answers.get("Would you like a physical activity suggestion?") == "Yes":
            report += "You're open to physical activities—wonderful for your body and mood!\n"
        if answers.get("Would you like a mental activity suggestion?") == "Yes":
            report += "Mental activities can keep your mind sharp. Great choice!\n"
        if answers.get("Would you like a social activity suggestion?") == "Yes":
            report += "Social activities are uplifting. Keep connecting!\n"

        # Meals & Enjoyment
        meal_help = answers.get("Do you need assistance with meals?")
        if meal_help == "Yes":
            report += "It's okay to need help with meals. Let others support you.\n"
        else:
            report += "Meals are managed well—enjoy your food!\n"

        enjoy = answers.get("Did you enjoy your last activity?")
        if enjoy == "Yes":
            report += "You enjoyed your last activity. Let’s keep finding things you love!\n"
        else:
            report += "Didn’t enjoy your last activity? No problem—explore something new tomorrow.\n"

        # Emotional Health
        anxious = answers.get("Are you feeling anxious or depressed?")
        if anxious == "No":
            report += "No anxiety or sadness today—so glad to hear it.\n"
        elif anxious == "A little":
            report += "Feeling a little down is normal. Be gentle with yourself and talk to someone if you’d like.\n"
        else:
            report += "You're feeling anxious or sad. Please reach out for support—there are people who care and want to help.\n"

        wellness = answers.get("Would you like a wellness check call?")
        if wellness == "Yes":
            report += "A wellness call is a great way to feel connected. One will be arranged for you.\n"
        else:
            report += "No wellness call needed right now.\n"

        concerns = answers.get("Do you have any concerns to share today?")
        if concerns == "Yes":
            report += "You have concerns today. Please share them with someone you trust, so they can help.\n"
        else:
            report += "No concerns reported—may your peace continue.\n"

        # Summary Table
        report += "\n---\n"
        report += "Here is a summary of your answers for today:\n\n"
        for q, a in answers.items():
            report += f"• {q}: {a}\n"

        report += (
            "\nThank you for taking time to reflect on your wellbeing today. "
            "Remember: every day is a new opportunity for joy, connection, and self-care. "
            "If you need anything, don’t hesitate to reach out to your loved ones or caregivers.\n"
            "Wishing you peace and happiness always!"
        )

        return report

    def save_pdf(self, report, user_name, user_age):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)
        # Use a common font to avoid Unicode errors
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(0, 10, "Eldercare Wellbeing Report", ln=True, align="C")
        pdf.ln(4)
        pdf.set_font("Arial", '', 12)
        pdf.cell(0, 10, f"User: {user_name}", ln=True)
        pdf.cell(0, 10, f"Age: {user_age}", ln=True)
        pdf.ln(4)
        pdf.set_font("Arial", '', 11)
        for line in report.split('\n'):
            pdf.multi_cell(0, 8, line)
        pdf.output("eldercare_report.pdf")

class CaregivingApp(App):
    def build(self):
        Window.size = (360, 700)
        return QandA()

if __name__ == '__main__':
    CaregivingApp().run()