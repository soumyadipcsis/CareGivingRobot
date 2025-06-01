import streamlit as st
import importlib

st.title("CareGivingRobot Logic Test Runner")

st.info("This app will run logic tests on the caregiving_robot_ml module and show results below.")

app = importlib.import_module("caregiving_robot_ml")

def run_get_vitals_video_links_tests():
    results = []
    try:
        assert app.get_vitals_video_links("120/80", "80", "98.6") == [
            app.YOUTUBE_VITALS_MAP["bp"], app.YOUTUBE_VITALS_MAP["pulse"], app.YOUTUBE_VITALS_MAP["temperature"]
        ]
        results.append("✅ get_vitals_video_links with all values: PASSED")
    except AssertionError:
        results.append("❌ get_vitals_video_links with all values: FAILED")
    try:
        assert app.get_vitals_video_links("", "", "") == []
        results.append("✅ get_vitals_video_links with blanks: PASSED")
    except AssertionError:
        results.append("❌ get_vitals_video_links with blanks: FAILED")
    try:
        assert app.get_vitals_video_links("120/80", "", "") == [app.YOUTUBE_VITALS_MAP["bp"]]
        results.append("✅ get_vitals_video_links with BP only: PASSED")
    except AssertionError:
        results.append("❌ get_vitals_video_links with BP only: FAILED")
    try:
        assert app.get_vitals_video_links("", "80", "") == [app.YOUTUBE_VITALS_MAP["pulse"]]
        results.append("✅ get_vitals_video_links with Pulse only: PASSED")
    except AssertionError:
        results.append("❌ get_vitals_video_links with Pulse only: FAILED")
    try:
        assert app.get_vitals_video_links("", "", "98.6") == [app.YOUTUBE_VITALS_MAP["temperature"]]
        results.append("✅ get_vitals_video_links with Temp only: PASSED")
    except AssertionError:
        results.append("❌ get_vitals_video_links with Temp only: FAILED")
    return results

def run_make_vitals_narrative_tests():
    testcases = [
        ("120/80", "80", "98.6", "within the normal range"),
        ("150/100", "80", "98.6", "higher than normal"),
        ("85/55", "80", "98.6", "lower than normal"),
        ("120/80", "50", "98.6", "Pulse is lower than normal"),
        ("120/80", "110", "98.6", "Pulse is higher than normal"),
        ("120/80", "80", "96.0", "Temperature is a bit low"),
        ("120/80", "80", "100.0", "Temperature is slightly elevated"),
        ("bad", "bad", "bad", "Unable to interpret"),
        ("", "", "", "not entered"),
    ]
    results = []
    for bp, pulse, temp, expected in testcases:
        out = app.make_vitals_narrative(bp, pulse, temp)
        if expected in out:
            results.append(f"✅ make_vitals_narrative({bp}, {pulse}, {temp}) contains '{expected}'")
        else:
            results.append(f"❌ make_vitals_narrative({bp}, {pulse}, {temp}) does not contain '{expected}'")
    return results

def run_make_narrative_and_suggestions_tests():
    results = []
    # "bad" scenario
    answers_bad = {
        "How are you feeling today?": "Bad",
        "Did you sleep well last night?": "No",
        "Have you taken your morning medication?": "No",
        "Did you eat breakfast?": "No",
        "Have you had water in the last hour?": "No",
        "Do you feel any pain right now?": "Severe",
        "Are you experiencing shortness of breath?": "Yes",
        "Do you feel dizzy or lightheaded?": "Yes",
        "Do you need help with any tasks today?": "Yes",
        "Do you have any appointments today?": "Yes",
        "Do you feel safe at home?": "No",
        "Have you spoken to family or friends today?": "No",
        "Would you like a physical activity suggestion?": "Yes",
        "Would you like a mental activity suggestion?": "Yes",
        "Would you like a social activity suggestion?": "Yes",
        "Are you feeling anxious or depressed?": "Yes",
        "Do you need assistance with meals?": "Yes",
        "Did you enjoy your last activity?": "No",
        "Would you like a wellness check call?": "Yes",
        "Do you have any concerns to share today?": "Yes",
    }
    narrative = app.make_narrative(answers_bad, "Alex", 70)
    suggestions = app.make_suggestions(answers_bad, "Alex")
    if "not feeling their best" in narrative:
        results.append("✅ make_narrative (bad scenario) contains 'not feeling their best'")
    else:
        results.append("❌ make_narrative (bad scenario) missing 'not feeling their best'")
    if "off days" in suggestions:
        results.append("✅ make_suggestions (bad scenario) contains 'off days'")
    else:
        results.append("❌ make_suggestions (bad scenario) missing 'off days'")
    if "Please remember to take your medication" in suggestions:
        results.append("✅ make_suggestions (bad scenario) contains 'Please remember to take your medication'")
    else:
        results.append("❌ make_suggestions (bad scenario) missing 'Please remember to take your medication'")
    if "Connecting with someone you care about" in suggestions:
        results.append("✅ make_suggestions (bad scenario) contains 'Connecting with someone you care about'")
    else:
        results.append("❌ make_suggestions (bad scenario) missing 'Connecting with someone you care about'")

    # "good" scenario
    answers_good = {
        "How are you feeling today?": "Good",
        "Did you sleep well last night?": "Yes",
        "Have you taken your morning medication?": "Yes",
        "Did you eat breakfast?": "Yes",
        "Have you had water in the last hour?": "Yes",
        "Do you feel any pain right now?": "No",
        "Are you experiencing shortness of breath?": "No",
        "Do you feel dizzy or lightheaded?": "No",
        "Do you need help with any tasks today?": "No",
        "Do you have any appointments today?": "No",
        "Do you feel safe at home?": "Yes",
        "Have you spoken to family or friends today?": "Yes",
        "Would you like a physical activity suggestion?": "No",
        "Would you like a mental activity suggestion?": "No",
        "Would you like a social activity suggestion?": "No",
        "Are you feeling anxious or depressed?": "No",
        "Do you need assistance with meals?": "No",
        "Did you enjoy your last activity?": "Yes",
        "Would you like a wellness check call?": "No",
        "Do you have any concerns to share today?": "No",
    }
    narrative = app.make_narrative(answers_good, "Jamie", 60)
    suggestions = app.make_suggestions(answers_good, "Jamie")
    if "in good spirits" in narrative:
        results.append("✅ make_narrative (good scenario) contains 'in good spirits'")
    else:
        results.append("❌ make_narrative (good scenario) missing 'in good spirits'")
    if "Keep up the positive energy" in suggestions:
        results.append("✅ make_suggestions (good scenario) contains 'Keep up the positive energy'")
    else:
        results.append("❌ make_suggestions (good scenario) missing 'Keep up the positive energy'")
    return results

if st.button("Run All Tests"):
    st.subheader("get_vitals_video_links Tests")
    for line in run_get_vitals_video_links_tests():
        st.write(line)
    st.subheader("make_vitals_narrative Tests")
    for line in run_make_vitals_narrative_tests():
        st.write(line)
    st.subheader("make_narrative and make_suggestions Tests")
    for line in run_make_narrative_and_suggestions_tests():
        st.write(line)
    st.success("All tests executed.")
else:
    st.info("Click the button above to run all logic tests on caregiving_robot_ml.")