# import streamlit as st
# from datetime import datetime

# # Add a beautiful background image using custom CSS
# def set_bg():
#     st.markdown(
#         """
#         <style>
#         .stApp {
#             background-image: url("https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1400&q=80");
#             background-size: cover;
#             background-repeat: no-repeat;
#             background-attachment: fixed;
#         }
#         /* Optional: add a soft overlay for readability */
#         .stApp::before {
#             content: "";
#             background: rgba(255,255,255,0.75);
#             position: fixed;
#             top: 0; left: 0; right: 0; bottom: 0;
#             z-index: 0;
#         }
#         /* Raise the app content above the overlay */
#         .block-container {
#             position: relative;
#             z-index: 1;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# set_bg()

# YOUTUBE_VITALS_MAP = {
#     "bp": "https://www.youtube.com/watch?v=pr29CWlkg8Y",
#     "pulse": "https://www.youtube.com/watch?v=BSlRvD-CZSo",
#     "temperature": "https://www.youtube.com/watch?v=E0CVdXv4RYA",
# }

# def get_vitals_video_links(bp, pulse, temp):
#     links = []
#     if bp:
#         links.append(YOUTUBE_VITALS_MAP["bp"])
#     if pulse:
#         links.append(YOUTUBE_VITALS_MAP["pulse"])
#     if temp:
#         links.append(YOUTUBE_VITALS_MAP["temperature"])
#     return list(dict.fromkeys(links))

# def make_vitals_narrative(bp, pulse, temp):
#     vitals_narr = "**Vitals Narrative:**\n"
#     any_flag = False
#     try:
#         systolic, diastolic = map(int, bp.replace(" ", "").split('/'))
#         if systolic > 140 or diastolic > 90:
#             vitals_narr += "- Blood pressure is higher than normal. Please monitor and consult your doctor if you feel unwell.\n"
#         elif systolic < 90 or diastolic < 60:
#             vitals_narr += "- Blood pressure is lower than normal. Take rest and consult your doctor if you feel faint or dizzy.\n"
#         else:
#             vitals_narr += "- Blood pressure is within the normal range.\n"
#         any_flag = True
#     except Exception:
#         if bp:
#             vitals_narr += "- Unable to interpret blood pressure. Please check the entered value.\n"
#             any_flag = True
#     try:
#         pulse_val = int(pulse.replace(" ", ""))
#         if pulse_val < 60:
#             vitals_narr += "- Pulse is lower than normal. Rest and notify your doctor if you feel tired or dizzy.\n"
#         elif pulse_val > 100:
#             vitals_narr += "- Pulse is higher than normal. Take some rest and monitor your heart rate.\n"
#         else:
#             vitals_narr += "- Pulse is within the normal range.\n"
#         any_flag = True
#     except Exception:
#         if pulse:
#             vitals_narr += "- Unable to interpret pulse. Please check the entered value.\n"
#             any_flag = True
#     try:
#         temp_val = float(temp.replace(" ", ""))
#         if temp_val < 97:
#             vitals_narr += "- Temperature is a bit low. Keep yourself warm and monitor for any symptoms.\n"
#         elif temp_val > 99.5:
#             vitals_narr += "- Temperature is slightly elevated. Consider resting, drinking fluids, and monitoring for fever.\n"
#         else:
#             vitals_narr += "- Temperature is within the normal range.\n"
#         any_flag = True
#     except Exception:
#         if temp:
#             vitals_narr += "- Unable to interpret temperature. Please check the entered value.\n"
#             any_flag = True
#     if not any_flag:
#         vitals_narr += "- Vitals not entered."
#     return vitals_narr

# def make_narrative(answers, user_name, user_age):
#     q = answers
#     narrative = f"**Concise Report for {user_name}, Age {user_age}**\n\n"
#     if q["How are you feeling today?"] == "Good":
#         narrative += f"{user_name} is in good spirits today"
#     elif q["How are you feeling today?"] == "Okay":
#         narrative += f"{user_name} is feeling alright today"
#     else:
#         narrative += f"{user_name} is not feeling their best today"
#     if q["Did you sleep well last night?"] == "Yes":
#         narrative += ", having had a restful night's sleep. "
#     else:
#         narrative += ", though sleep was somewhat restless. "
#     if q["Have you taken your morning medication?"] == "Yes":
#         narrative += "Morning medication was taken as prescribed. "
#     elif q["Have you taken your morning medication?"] == "No":
#         narrative += "Morning medication was not taken. "
#     else:
#         narrative += "No morning medication was needed. "
#     if q["Did you eat breakfast?"] == "Yes":
#         narrative += "Breakfast was eaten. "
#     else:
#         narrative += "Breakfast was skipped. "
#     if q["Have you had water in the last hour?"] == "Yes":
#         narrative += "Hydration is being maintained. "
#     else:
#         narrative += "Hydration could be improved. "
#     pain = q["Do you feel any pain right now?"]
#     if pain == "No":
#         narrative += "There is no pain reported at this time. "
#     elif pain == "Mild":
#         narrative += "A mild level of pain has been experienced. "
#     elif pain == "Moderate":
#         narrative += "Moderate pain has been reported. "
#     else:
#         narrative += "Severe pain is currently present. "
#     if q["Are you experiencing shortness of breath?"] == "Yes":
#         narrative += "Shortness of breath is noted. "
#     if q["Do you feel dizzy or lightheaded?"] == "Yes":
#         narrative += "There is some dizziness or lightheadedness. "
#     narrative += ("The home environment is "
#         f"{'safe' if q['Do you feel safe at home?'] == 'Yes' else 'not entirely safe'}. ")
#     if q["Do you need help with any tasks today?"] == "Yes":
#         narrative += "Additional help is needed with daily tasks. "
#     if q["Do you have any appointments today?"] == "Yes":
#         narrative += "There are appointments scheduled for today. "
#     if q["Have you spoken to family or friends today?"] == "Yes":
#         narrative += "Social interaction with friends or family has occurred. "
#     else:
#         narrative += "There has been little or no social contact so far. "
#     if q["Would you like a physical activity suggestion?"] == "Yes":
#         narrative += "A physical activity suggestion would be welcome. "
#     if q["Would you like a mental activity suggestion?"] == "Yes":
#         narrative += "A mental activity suggestion would be helpful. "
#     if q["Would you like a social activity suggestion?"] == "Yes":
#         narrative += "A social activity suggestion is requested. "
#     feeling = q["Are you feeling anxious or depressed?"]
#     if feeling == "No":
#         narrative += "There are no signs of anxiety or depression. "
#     elif feeling == "A little":
#         narrative += "There is a slight feeling of anxiety or low mood. "
#     else:
#         narrative += "There are significant feelings of anxiety or depression. "
#     if q["Do you need assistance with meals?"] == "Yes":
#         narrative += "Assistance with meals is needed. "
#     if q["Did you enjoy your last activity?"] == "Yes":
#         narrative += "The previous activity was enjoyable. "
#     else:
#         narrative += "The last activity was not particularly enjoyable. "
#     if q["Would you like a wellness check call?"] == "Yes":
#         narrative += "A wellness check call is requested. "
#     if q["Do you have any concerns to share today?"] == "Yes":
#         narrative += "Some additional concerns were raised today. "
#     else:
#         narrative += "No extra concerns have been shared today. "
#     return narrative.strip()

# def make_suggestions(answers, user_name):
#     q = answers
#     suggestions = "#### Suggestions & Encouragement\n"
#     if q["How are you feeling today?"] == "Bad":
#         suggestions += f"- {user_name}, it's okay to have off days. Consider doing something you enjoy, or reaching out to a friend or loved one for support.\n"
#     elif q["How are you feeling today?"] == "Okay":
#         suggestions += "- If you want to boost your mood, a short walk or a favorite activity might help brighten your day.\n"
#     else:
#         suggestions += "- Keep up the positive energy and continue doing what makes you feel good!\n"
#     if q["Did you sleep well last night?"] == "No":
#         suggestions += "- Try to create a relaxing bedtime routine tonight, perhaps by reading or listening to soft music.\n"
#     else:
#         suggestions += "- Good sleep is valuable—keep your evening routine consistent.\n"
#     if q["Have you taken your morning medication?"] == "No":
#         suggestions += "- Please remember to take your medication as prescribed. Setting a daily reminder can be helpful.\n"
#     if q["Did you eat breakfast?"] == "No":
#         suggestions += "- Starting the day with a light breakfast can help maintain your energy.\n"
#     if q["Have you had water in the last hour?"] == "No":
#         suggestions += "- Try to keep a bottle of water nearby and sip regularly throughout the day.\n"
#     pain = q["Do you feel any pain right now?"]
#     if pain == "Mild":
#         suggestions += "- If your pain worsens, take a break and let someone know if you need help.\n"
#     elif pain == "Moderate" or pain == "Severe":
#         suggestions += "- Be sure to mention your pain to a caregiver, and don't hesitate to rest or seek assistance.\n"
#     if q["Are you experiencing shortness of breath?"] == "Yes":
#         suggestions += "- If breathing becomes difficult, sit down, rest, and seek help if it doesn't improve.\n"
#     if q["Do you feel dizzy or lightheaded?"] == "Yes":
#         suggestions += "- Please move slowly and avoid sudden movements. Rest as needed and let someone know.\n"
#     if q["Do you feel safe at home?"] == "No":
#         suggestions += "- Your safety is important. Please discuss any concerns with someone you trust or your care team.\n"
#     if q["Do you need help with any tasks today?"] == "Yes":
#         suggestions += "- Don't hesitate to ask for help with tasks—everyone needs support sometimes.\n"
#     if q["Have you spoken to family or friends today?"] == "No":
#         suggestions += "- Connecting with someone you care about can lift your spirits. Maybe call or message a friend.\n"
#     if q["Would you like a physical activity suggestion?"] == "Yes":
#         suggestions += "- Consider some gentle stretching or a short walk to keep active.\n"
#     if q["Would you like a mental activity suggestion?"] == "Yes":
#         suggestions += "- Try a puzzle, a book, or listening to music for mental stimulation.\n"
#     if q["Would you like a social activity suggestion?"] == "Yes":
#         suggestions += "- Joining a community call or chatting with a neighbor could be enjoyable.\n"
#     feeling = q["Are you feeling anxious or depressed?"]
#     if feeling == "A little":
#         suggestions += "- If you're feeling a bit down, deep breathing and talking to someone you trust can help.\n"
#     elif feeling == "Yes":
#         suggestions += "- You're not alone; reach out to a loved one or professional if you need to talk.\n"
#     if q["Do you need assistance with meals?"] == "Yes":
#         suggestions += "- Let someone know if you need help preparing or enjoying your meals today.\n"
#     if q["Did you enjoy your last activity?"] == "No":
#         suggestions += "- Maybe try a different activity today, or revisit something you enjoyed in the past.\n"
#     if q["Would you like a wellness check call?"] == "Yes":
#         suggestions += "- A wellness check will be arranged soon to make sure you're doing well.\n"
#     if q["Do you have any concerns to share today?"] == "Yes":
#         suggestions += "- Your concerns matter. Talk to your care team or someone you trust about anything on your mind.\n"
#     suggestions += "\nRemember, every small step you take toward your wellbeing is important. You’re doing your best, and that’s enough."
#     return suggestions.strip()

# if "user_name" not in st.session_state: st.session_state["user_name"] = ""
# if "user_age" not in st.session_state: st.session_state["user_age"] = 0
# if "answers" not in st.session_state: st.session_state["answers"] = {}
# if "narrative" not in st.session_state: st.session_state["narrative"] = ""
# if "suggestions" not in st.session_state: st.session_state["suggestions"] = ""
# if "narrative_generated" not in st.session_state: st.session_state["narrative_generated"] = False
# if "saved_reports" not in st.session_state: st.session_state["saved_reports"] = []
# if "vitals" not in st.session_state: st.session_state["vitals"] = {}
# if "vitals_narrative" not in st.session_state: st.session_state["vitals_narrative"] = ""
# if "last_save_success" not in st.session_state: st.session_state["last_save_success"] = False

# qa_list = [
#     ("How are you feeling today?", ["Good", "Okay", "Bad"]),
#     ("Did you sleep well last night?", ["Yes", "No"]),
#     ("Have you taken your morning medication?", ["Yes", "No", "Not Applicable"]),
#     ("Did you eat breakfast?", ["Yes", "No"]),
#     ("Have you had water in the last hour?", ["Yes", "No"]),
#     ("Do you feel any pain right now?", ["No", "Mild", "Moderate", "Severe"]),
#     ("Are you experiencing shortness of breath?", ["No", "Yes"]),
#     ("Do you feel dizzy or lightheaded?", ["No", "Yes"]),
#     ("Do you need help with any tasks today?", ["No", "Yes"]),
#     ("Do you have any appointments today?", ["No", "Yes"]),
#     ("Do you feel safe at home?", ["Yes", "No"]),
#     ("Have you spoken to family or friends today?", ["Yes", "No"]),
#     ("Would you like a physical activity suggestion?", ["Yes", "No"]),
#     ("Would you like a mental activity suggestion?", ["Yes", "No"]),
#     ("Would you like a social activity suggestion?", ["Yes", "No"]),
#     ("Are you feeling anxious or depressed?", ["No", "A little", "Yes"]),
#     ("Do you need assistance with meals?", ["No", "Yes"]),
#     ("Did you enjoy your last activity?", ["Yes", "No"]),
#     ("Would you like a wellness check call?", ["Yes", "No"]),
#     ("Do you have any concerns to share today?", ["No", "Yes"]),
# ]

# tab1, tab2, tab3, tab4 = st.tabs(["Patient Info", "Q & A", "Saved Reports", "Related Videos"])

# with tab1:
#     st.header("Patient Information")
#     st.session_state["user_name"] = st.text_input("Enter patient name", value=st.session_state["user_name"])
#     st.session_state["user_age"] = st.number_input("Enter patient age", min_value=0, max_value=120, step=1, value=st.session_state["user_age"])

# qna_disabled = (not st.session_state["user_name"].strip()) or (not st.session_state["user_age"])
# with tab2:
#     st.header("Q & A")
#     if qna_disabled:
#         st.warning("Please enter the patient's name and age in the 'Patient Info' tab before proceeding.")
#         st.stop()

#     st.subheader("Enter Today's Vitals (Mandatory)")
#     with st.form("vitals_form", clear_on_submit=False):
#         bp = st.text_input("Blood Pressure (e.g., 120/80 mmHg)", value=st.session_state["vitals"].get("BP", ""))
#         pulse = st.text_input("Pulse (bpm)", value=st.session_state["vitals"].get("Pulse", ""))
#         temp = st.text_input("Temperature (°F)", value=st.session_state["vitals"].get("Temperature", ""))
#         vitals_submitted = st.form_submit_button("Save Vitals")
#     if vitals_submitted:
#         st.session_state["vitals"] = {"BP": bp, "Pulse": pulse, "Temperature": temp}
#         st.success("Vitals saved.")

#     if st.session_state["vitals"]:
#         v = st.session_state["vitals"]
#         st.info(f"**Saved Vitals:** BP: {v.get('BP', '')}, Pulse: {v.get('Pulse', '')}, Temp: {v.get('Temperature', '')}")

#     qa_disabled = not (bp and pulse and temp)
#     if not (bp and pulse and temp):
#         st.warning("Please enter and save all vitals before answering the questionnaire.")
#         st.stop()
#     else:
#         for idx, (q, opts) in enumerate(qa_list):
#             prev_answer = st.session_state["answers"].get(q, opts[0])
#             answer = st.radio(q, opts, key=f"qa_{idx}", index=opts.index(prev_answer) if prev_answer in opts else 0)
#             st.session_state["answers"][q] = answer

#         if st.button("Generate Narrative Report"):
#             st.session_state["vitals_narrative"] = make_vitals_narrative(bp, pulse, temp)
#             st.session_state["narrative"] = make_narrative(st.session_state["answers"], st.session_state["user_name"], st.session_state["user_age"])
#             st.session_state["suggestions"] = make_suggestions(st.session_state["answers"], st.session_state["user_name"])
#             st.session_state["narrative_generated"] = True
#             st.session_state["last_save_success"] = False

#         if st.session_state.get("narrative_generated", False) and st.session_state["narrative"]:
#             st.markdown(st.session_state["vitals_narrative"])
#             st.markdown(st.session_state["narrative"])
#             st.markdown(st.session_state["suggestions"])
#             col1, col2 = st.columns(2)
#             with col1:
#                 if st.button("Save Report", key="save_report"):
#                     now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#                     bp = st.session_state["vitals"].get("BP", "")
#                     pulse = st.session_state["vitals"].get("Pulse", "")
#                     temp = st.session_state["vitals"].get("Temperature", "")
#                     video_links = get_vitals_video_links(bp, pulse, temp)
#                     st.session_state["saved_reports"].append({
#                         "datetime": now,
#                         "name": st.session_state["user_name"],
#                         "age": st.session_state["user_age"],
#                         "vitals": st.session_state["vitals"],
#                         "vitals_narrative": st.session_state["vitals_narrative"],
#                         "report": st.session_state["narrative"],
#                         "suggestions": st.session_state["suggestions"],
#                         "video_links": video_links,
#                     })
#                     st.success("Report saved in the 'Saved Reports' tab.")
#                     st.session_state["narrative_generated"] = False
#                     st.session_state["last_save_success"] = True
#             with col2:
#                 if st.button("Not Interested to Save", key="not_save_report"):
#                     st.session_state["narrative"] = ""
#                     st.session_state["suggestions"] = ""
#                     st.session_state["vitals_narrative"] = ""
#                     st.session_state["narrative_generated"] = False
#                     st.session_state["last_save_success"] = False
#                     st.info("Report was not saved. No video suggestion will be available until a report is saved.")

# with tab3:
#     st.header("Saved Narrative Reports")
#     if st.session_state["saved_reports"]:
#         for i, entry in enumerate(reversed(st.session_state["saved_reports"])):
#             st.markdown(f"---\n**Saved on:** {entry['datetime']}  \n**Patient:** {entry['name']}, **Age:** {entry['age']}")
#             v = entry.get("vitals", {})
#             st.markdown(f"**Vitals:** BP: {v.get('BP', '')}, Pulse: {v.get('Pulse', '')}, Temp: {v.get('Temperature', '')}")
#             st.markdown(entry.get("vitals_narrative", ""))
#             st.markdown(entry["report"])
#             st.markdown(entry["suggestions"])
#     else:
#         st.info("No report saved yet. Complete the Q & A and save the report from the previous tab.")

# with tab4:
#     st.header("Related Videos")
#     # Show videos as soon as vitals are available (do not require saving)
#     video_links = []
#     v = st.session_state.get("vitals", {})
#     bp = v.get("BP", "")
#     pulse = v.get("Pulse", "")
#     temp = v.get("Temperature", "")
#     video_links = get_vitals_video_links(bp, pulse, temp) if (bp or pulse or temp) else []
#     if video_links:
#         st.markdown("Videos matched to your entered BP, Pulse, and Temperature:")
#         for link in video_links:
#             st.video(link)
#     else:
#         st.info("Enter and save BP, Pulse, and Temperature in the Q & A tab to view related videos.")


# import streamlit as st
# from datetime import datetime

# # Use a gentle healthcare/wellbeing gradient and a doctor/wellbeing image on the side
# def set_bg():
#     st.markdown(
#         """
#         <style>
#         .stApp {
#             background: linear-gradient(120deg, #f0f6ff 0%, #e6fff5 100%);
#             min-height: 100vh !important;
#             background-attachment: fixed !important;
#         }
#         .doctor-bg-img {
#             position: fixed;
#             top: 0;
#             left: 0;
#             height: 100vh;
#             width: 40vw;
#             min-width: 350px;
#             max-width: 600px;
#             background: url('https://images.unsplash.com/photo-1537368910025-700350fe46c7?auto=format&fit=crop&w=800&q=80') no-repeat left center;
#             background-size: cover;
#             opacity: 0.17;
#             z-index: 0;
#         }
#         @media (max-width: 900px) {
#             .doctor-bg-img { display: none; }
#         }
#         .block-container { position: relative; z-index: 2; }
#         </style>
#         <div class="doctor-bg-img"></div>
#         """,
#         unsafe_allow_html=True
#     )

# set_bg()

# YOUTUBE_VITALS_MAP = {
#     "bp": "https://www.youtube.com/watch?v=pr29CWlkg8Y",
#     "pulse": "https://www.youtube.com/watch?v=BSlRvD-CZSo",
#     "temperature": "https://www.youtube.com/watch?v=E0CVdXv4RYA",
# }
# def get_vitals_video_links(bp, pulse, temp):
#     links = []
#     if bp:
#         links.append(YOUTUBE_VITALS_MAP["bp"])
#     if pulse:
#         links.append(YOUTUBE_VITALS_MAP["pulse"])
#     if temp:
#         links.append(YOUTUBE_VITALS_MAP["temperature"])
#     return list(dict.fromkeys(links))

# def make_vitals_narrative(bp, pulse, temp):
#     vitals_narr = "**Vitals Narrative:**\n"
#     any_flag = False
#     try:
#         systolic, diastolic = map(int, bp.replace(" ", "").split('/'))
#         if systolic > 140 or diastolic > 90:
#             vitals_narr += "- Blood pressure is higher than normal. Please monitor and consult your doctor if you feel unwell.\n"
#         elif systolic < 90 or diastolic < 60:
#             vitals_narr += "- Blood pressure is lower than normal. Take rest and consult your doctor if you feel faint or dizzy.\n"
#         else:
#             vitals_narr += "- Blood pressure is within the normal range.\n"
#         any_flag = True
#     except Exception:
#         if bp:
#             vitals_narr += "- Unable to interpret blood pressure. Please check the entered value.\n"
#             any_flag = True
#     try:
#         pulse_val = int(pulse.replace(" ", ""))
#         if pulse_val < 60:
#             vitals_narr += "- Pulse is lower than normal. Rest and notify your doctor if you feel tired or dizzy.\n"
#         elif pulse_val > 100:
#             vitals_narr += "- Pulse is higher than normal. Take some rest and monitor your heart rate.\n"
#         else:
#             vitals_narr += "- Pulse is within the normal range.\n"
#         any_flag = True
#     except Exception:
#         if pulse:
#             vitals_narr += "- Unable to interpret pulse. Please check the entered value.\n"
#             any_flag = True
#     try:
#         temp_val = float(temp.replace(" ", ""))
#         if temp_val < 97:
#             vitals_narr += "- Temperature is a bit low. Keep yourself warm and monitor for any symptoms.\n"
#         elif temp_val > 99.5:
#             vitals_narr += "- Temperature is slightly elevated. Consider resting, drinking fluids, and monitoring for fever.\n"
#         else:
#             vitals_narr += "- Temperature is within the normal range.\n"
#         any_flag = True
#     except Exception:
#         if temp:
#             vitals_narr += "- Unable to interpret temperature. Please check the entered value.\n"
#             any_flag = True
#     if not any_flag:
#         vitals_narr += "- Vitals not entered."
#     return vitals_narr

# def make_narrative(answers, user_name, user_age):
#     q = answers
#     narrative = f"**Concise Report for {user_name}, Age {user_age}**\n\n"
#     if q["How are you feeling today?"] == "Good":
#         narrative += f"{user_name} is in good spirits today"
#     elif q["How are you feeling today?"] == "Okay":
#         narrative += f"{user_name} is feeling alright today"
#     else:
#         narrative += f"{user_name} is not feeling their best today"
#     if q["Did you sleep well last night?"] == "Yes":
#         narrative += ", having had a restful night's sleep. "
#     else:
#         narrative += ", though sleep was somewhat restless. "
#     if q["Have you taken your morning medication?"] == "Yes":
#         narrative += "Morning medication was taken as prescribed. "
#     elif q["Have you taken your morning medication?"] == "No":
#         narrative += "Morning medication was not taken. "
#     else:
#         narrative += "No morning medication was needed. "
#     if q["Did you eat breakfast?"] == "Yes":
#         narrative += "Breakfast was eaten. "
#     else:
#         narrative += "Breakfast was skipped. "
#     if q["Have you had water in the last hour?"] == "Yes":
#         narrative += "Hydration is being maintained. "
#     else:
#         narrative += "Hydration could be improved. "
#     pain = q["Do you feel any pain right now?"]
#     if pain == "No":
#         narrative += "There is no pain reported at this time. "
#     elif pain == "Mild":
#         narrative += "A mild level of pain has been experienced. "
#     elif pain == "Moderate":
#         narrative += "Moderate pain has been reported. "
#     else:
#         narrative += "Severe pain is currently present. "
#     if q["Are you experiencing shortness of breath?"] == "Yes":
#         narrative += "Shortness of breath is noted. "
#     if q["Do you feel dizzy or lightheaded?"] == "Yes":
#         narrative += "There is some dizziness or lightheadedness. "
#     narrative += ("The home environment is "
#         f"{'safe' if q['Do you feel safe at home?'] == 'Yes' else 'not entirely safe'}. ")
#     if q["Do you need help with any tasks today?"] == "Yes":
#         narrative += "Additional help is needed with daily tasks. "
#     if q["Do you have any appointments today?"] == "Yes":
#         narrative += "There are appointments scheduled for today. "
#     if q["Have you spoken to family or friends today?"] == "Yes":
#         narrative += "Social interaction with friends or family has occurred. "
#     else:
#         narrative += "There has been little or no social contact so far. "
#     if q["Would you like a physical activity suggestion?"] == "Yes":
#         narrative += "A physical activity suggestion would be welcome. "
#     if q["Would you like a mental activity suggestion?"] == "Yes":
#         narrative += "A mental activity suggestion would be helpful. "
#     if q["Would you like a social activity suggestion?"] == "Yes":
#         narrative += "A social activity suggestion is requested. "
#     feeling = q["Are you feeling anxious or depressed?"]
#     if feeling == "No":
#         narrative += "There are no signs of anxiety or depression. "
#     elif feeling == "A little":
#         narrative += "There is a slight feeling of anxiety or low mood. "
#     else:
#         narrative += "There are significant feelings of anxiety or depression. "
#     if q["Do you need assistance with meals?"] == "Yes":
#         narrative += "Assistance with meals is needed. "
#     if q["Did you enjoy your last activity?"] == "Yes":
#         narrative += "The previous activity was enjoyable. "
#     else:
#         narrative += "The last activity was not particularly enjoyable. "
#     if q["Would you like a wellness check call?"] == "Yes":
#         narrative += "A wellness check call is requested. "
#     if q["Do you have any concerns to share today?"] == "Yes":
#         narrative += "Some additional concerns were raised today. "
#     else:
#         narrative += "No extra concerns have been shared today. "
#     return narrative.strip()

# def make_suggestions(answers, user_name):
#     q = answers
#     suggestions = "#### Suggestions & Encouragement\n"
#     if q["How are you feeling today?"] == "Bad":
#         suggestions += f"- {user_name}, it's okay to have off days. Consider doing something you enjoy, or reaching out to a friend or loved one for support.\n"
#     elif q["How are you feeling today?"] == "Okay":
#         suggestions += "- If you want to boost your mood, a short walk or a favorite activity might help brighten your day.\n"
#     else:
#         suggestions += "- Keep up the positive energy and continue doing what makes you feel good!\n"
#     if q["Did you sleep well last night?"] == "No":
#         suggestions += "- Try to create a relaxing bedtime routine tonight, perhaps by reading or listening to soft music.\n"
#     else:
#         suggestions += "- Good sleep is valuable—keep your evening routine consistent.\n"
#     if q["Have you taken your morning medication?"] == "No":
#         suggestions += "- Please remember to take your medication as prescribed. Setting a daily reminder can be helpful.\n"
#     if q["Did you eat breakfast?"] == "No":
#         suggestions += "- Starting the day with a light breakfast can help maintain your energy.\n"
#     if q["Have you had water in the last hour?"] == "No":
#         suggestions += "- Try to keep a bottle of water nearby and sip regularly throughout the day.\n"
#     pain = q["Do you feel any pain right now?"]
#     if pain == "Mild":
#         suggestions += "- If your pain worsens, take a break and let someone know if you need help.\n"
#     elif pain == "Moderate" or pain == "Severe":
#         suggestions += "- Be sure to mention your pain to a caregiver, and don't hesitate to rest or seek assistance.\n"
#     if q["Are you experiencing shortness of breath?"] == "Yes":
#         suggestions += "- If breathing becomes difficult, sit down, rest, and seek help if it doesn't improve.\n"
#     if q["Do you feel dizzy or lightheaded?"] == "Yes":
#         suggestions += "- Please move slowly and avoid sudden movements. Rest as needed and let someone know.\n"
#     if q["Do you feel safe at home?"] == "No":
#         suggestions += "- Your safety is important. Please discuss any concerns with someone you trust or your care team.\n"
#     if q["Do you need help with any tasks today?"] == "Yes":
#         suggestions += "- Don't hesitate to ask for help with tasks—everyone needs support sometimes.\n"
#     if q["Have you spoken to family or friends today?"] == "No":
#         suggestions += "- Connecting with someone you care about can lift your spirits. Maybe call or message a friend.\n"
#     if q["Would you like a physical activity suggestion?"] == "Yes":
#         suggestions += "- Consider some gentle stretching or a short walk to keep active.\n"
#     if q["Would you like a mental activity suggestion?"] == "Yes":
#         suggestions += "- Try a puzzle, a book, or listening to music for mental stimulation.\n"
#     if q["Would you like a social activity suggestion?"] == "Yes":
#         suggestions += "- Joining a community call or chatting with a neighbor could be enjoyable.\n"
#     feeling = q["Are you feeling anxious or depressed?"]
#     if feeling == "A little":
#         suggestions += "- If you're feeling a bit down, deep breathing and talking to someone you trust can help.\n"
#     elif feeling == "Yes":
#         suggestions += "- You're not alone; reach out to a loved one or professional if you need to talk.\n"
#     if q["Do you need assistance with meals?"] == "Yes":
#         suggestions += "- Let someone know if you need help preparing or enjoying your meals today.\n"
#     if q["Did you enjoy your last activity?"] == "No":
#         suggestions += "- Maybe try a different activity today, or revisit something you enjoyed in the past.\n"
#     if q["Would you like a wellness check call?"] == "Yes":
#         suggestions += "- A wellness check will be arranged soon to make sure you're doing well.\n"
#     if q["Do you have any concerns to share today?"] == "Yes":
#         suggestions += "- Your concerns matter. Talk to your care team or someone you trust about anything on your mind.\n"
#     suggestions += "\nRemember, every small step you take toward your wellbeing is important. You’re doing your best, and that’s enough."
#     return suggestions.strip()

# if "user_name" not in st.session_state: st.session_state["user_name"] = ""
# if "user_age" not in st.session_state: st.session_state["user_age"] = 0
# if "answers" not in st.session_state: st.session_state["answers"] = {}
# if "narrative" not in st.session_state: st.session_state["narrative"] = ""
# if "suggestions" not in st.session_state: st.session_state["suggestions"] = ""
# if "narrative_generated" not in st.session_state: st.session_state["narrative_generated"] = False
# if "saved_reports" not in st.session_state: st.session_state["saved_reports"] = []
# if "vitals" not in st.session_state: st.session_state["vitals"] = {}
# if "vitals_narrative" not in st.session_state: st.session_state["vitals_narrative"] = ""
# if "last_save_success" not in st.session_state: st.session_state["last_save_success"] = False

# qa_list = [
#     ("How are you feeling today?", ["Good", "Okay", "Bad"]),
#     ("Did you sleep well last night?", ["Yes", "No"]),
#     ("Have you taken your morning medication?", ["Yes", "No", "Not Applicable"]),
#     ("Did you eat breakfast?", ["Yes", "No"]),
#     ("Have you had water in the last hour?", ["Yes", "No"]),
#     ("Do you feel any pain right now?", ["No", "Mild", "Moderate", "Severe"]),
#     ("Are you experiencing shortness of breath?", ["No", "Yes"]),
#     ("Do you feel dizzy or lightheaded?", ["No", "Yes"]),
#     ("Do you need help with any tasks today?", ["No", "Yes"]),
#     ("Do you have any appointments today?", ["No", "Yes"]),
#     ("Do you feel safe at home?", ["Yes", "No"]),
#     ("Have you spoken to family or friends today?", ["Yes", "No"]),
#     ("Would you like a physical activity suggestion?", ["Yes", "No"]),
#     ("Would you like a mental activity suggestion?", ["Yes", "No"]),
#     ("Would you like a social activity suggestion?", ["Yes", "No"]),
#     ("Are you feeling anxious or depressed?", ["No", "A little", "Yes"]),
#     ("Do you need assistance with meals?", ["No", "Yes"]),
#     ("Did you enjoy your last activity?", ["Yes", "No"]),
#     ("Would you like a wellness check call?", ["Yes", "No"]),
#     ("Do you have any concerns to share today?", ["No", "Yes"]),
# ]

# tab1, tab2, tab3, tab4 = st.tabs(["Patient Info", "Q & A", "Saved Reports", "Related Videos"])

# with tab1:
#     st.header("Patient Information")
#     st.session_state["user_name"] = st.text_input("Enter patient name", value=st.session_state["user_name"])
#     st.session_state["user_age"] = st.number_input("Enter patient age", min_value=0, max_value=120, step=1, value=st.session_state["user_age"])

# qna_disabled = (not st.session_state["user_name"].strip()) or (not st.session_state["user_age"])
# with tab2:
#     st.header("Q & A")
#     if qna_disabled:
#         st.warning("Please enter the patient's name and age in the 'Patient Info' tab before proceeding.")
#         st.stop()

#     st.subheader("Enter Today's Vitals (Mandatory)")
#     with st.form("vitals_form", clear_on_submit=False):
#         bp = st.text_input("Blood Pressure (e.g., 120/80 mmHg)", value=st.session_state["vitals"].get("BP", ""))
#         pulse = st.text_input("Pulse (bpm)", value=st.session_state["vitals"].get("Pulse", ""))
#         temp = st.text_input("Temperature (°F)", value=st.session_state["vitals"].get("Temperature", ""))
#         vitals_submitted = st.form_submit_button("Save Vitals")
#     if vitals_submitted:
#         st.session_state["vitals"] = {"BP": bp, "Pulse": pulse, "Temperature": temp}
#         st.success("Vitals saved.")

#     if st.session_state["vitals"]:
#         v = st.session_state["vitals"]
#         st.info(f"**Saved Vitals:** BP: {v.get('BP', '')}, Pulse: {v.get('Pulse', '')}, Temp: {v.get('Temperature', '')}")

#     qa_disabled = not (bp and pulse and temp)
#     if not (bp and pulse and temp):
#         st.warning("Please enter and save all vitals before answering the questionnaire.")
#         st.stop()
#     else:
#         for idx, (q, opts) in enumerate(qa_list):
#             prev_answer = st.session_state["answers"].get(q, opts[0])
#             answer = st.radio(q, opts, key=f"qa_{idx}", index=opts.index(prev_answer) if prev_answer in opts else 0)
#             st.session_state["answers"][q] = answer

#         if st.button("Generate Narrative Report"):
#             st.session_state["vitals_narrative"] = make_vitals_narrative(bp, pulse, temp)
#             st.session_state["narrative"] = make_narrative(st.session_state["answers"], st.session_state["user_name"], st.session_state["user_age"])
#             st.session_state["suggestions"] = make_suggestions(st.session_state["answers"], st.session_state["user_name"])
#             st.session_state["narrative_generated"] = True
#             st.session_state["last_save_success"] = False

#         if st.session_state.get("narrative_generated", False) and st.session_state["narrative"]:
#             st.markdown(st.session_state["vitals_narrative"])
#             st.markdown(st.session_state["narrative"])
#             st.markdown(st.session_state["suggestions"])
#             col1, col2 = st.columns(2)
#             with col1:
#                 if st.button("Save Report", key="save_report"):
#                     now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#                     bp = st.session_state["vitals"].get("BP", "")
#                     pulse = st.session_state["vitals"].get("Pulse", "")
#                     temp = st.session_state["vitals"].get("Temperature", "")
#                     video_links = get_vitals_video_links(bp, pulse, temp)
#                     st.session_state["saved_reports"].append({
#                         "datetime": now,
#                         "name": st.session_state["user_name"],
#                         "age": st.session_state["user_age"],
#                         "vitals": st.session_state["vitals"],
#                         "vitals_narrative": st.session_state["vitals_narrative"],
#                         "report": st.session_state["narrative"],
#                         "suggestions": st.session_state["suggestions"],
#                         "video_links": video_links,
#                     })
#                     st.success("Report saved in the 'Saved Reports' tab.")
#                     st.session_state["narrative_generated"] = False
#                     st.session_state["last_save_success"] = True
#             with col2:
#                 if st.button("Not Interested to Save", key="not_save_report"):
#                     st.session_state["narrative"] = ""
#                     st.session_state["suggestions"] = ""
#                     st.session_state["vitals_narrative"] = ""
#                     st.session_state["narrative_generated"] = False
#                     st.session_state["last_save_success"] = False
#                     st.info("Report was not saved. No video suggestion will be available until a report is saved.")

# with tab3:
#     st.header("Saved Narrative Reports")
#     if st.session_state["saved_reports"]:
#         for i, entry in enumerate(reversed(st.session_state["saved_reports"])):
#             st.markdown(f"---\n**Saved on:** {entry['datetime']}  \n**Patient:** {entry['name']}, **Age:** {entry['age']}")
#             v = entry.get("vitals", {})
#             st.markdown(f"**Vitals:** BP: {v.get('BP', '')}, Pulse: {v.get('Pulse', '')}, Temp: {v.get('Temperature', '')}")
#             st.markdown(entry.get("vitals_narrative", ""))
#             st.markdown(entry["report"])
#             st.markdown(entry["suggestions"])
#     else:
#         st.info("No report saved yet. Complete the Q & A and save the report from the previous tab.")

# with tab4:
#     st.header("Related Videos")
#     # Show videos as soon as vitals are available (do not require saving)
#     video_links = []
#     v = st.session_state.get("vitals", {})
#     bp = v.get("BP", "")
#     pulse = v.get("Pulse", "")
#     temp = v.get("Temperature", "")
#     video_links = get_vitals_video_links(bp, pulse, temp) if (bp or pulse or temp) else []
#     if video_links:
#         st.markdown("Videos matched to your entered BP, Pulse, and Temperature:")
#         for link in video_links:
#             st.video(link)
#     else:
#         st.info("Enter and save BP, Pulse, and Temperature in the Q & A tab to view related videos.")



# import streamlit as st
# from datetime import datetime

# # Set a sky blue background with a doctor's symbol (icon) on the side
# def set_bg():
#     st.markdown(
#         """
#         <style>
#         .stApp {
#             background: linear-gradient(120deg, #e0f7fa 0%, #b3e5fc 100%);
#             min-height: 100vh !important;
#             background-attachment: fixed !important;
#         }
#         /* Doctor symbol on top right, visible but subtle */
#         .doctor-symbol {
#             position: fixed;
#             top: 40px;
#             right: 50px;
#             width: 120px;
#             height: 120px;
#             opacity: 0.12;
#             z-index: 0;
#             background: url('https://cdn-icons-png.flaticon.com/512/3209/3209265.png') no-repeat center center;
#             background-size: contain;
#         }
#         /* Hide on small screens */
#         @media (max-width: 800px) {
#             .doctor-symbol { display: none; }
#         }
#         .block-container { position: relative; z-index: 2; }
#         </style>
#         <div class="doctor-symbol"></div>
#         """,
#         unsafe_allow_html=True
#     )

# set_bg()

# YOUTUBE_VITALS_MAP = {
#     "bp": "https://www.youtube.com/watch?v=pr29CWlkg8Y",
#     "pulse": "https://www.youtube.com/watch?v=BSlRvD-CZSo",
#     "temperature": "https://www.youtube.com/watch?v=E0CVdXv4RYA",
# }
# def get_vitals_video_links(bp, pulse, temp):
#     links = []
#     if bp:
#         links.append(YOUTUBE_VITALS_MAP["bp"])
#     if pulse:
#         links.append(YOUTUBE_VITALS_MAP["pulse"])
#     if temp:
#         links.append(YOUTUBE_VITALS_MAP["temperature"])
#     return list(dict.fromkeys(links))

# def make_vitals_narrative(bp, pulse, temp):
#     vitals_narr = "**Vitals Narrative:**\n"
#     any_flag = False
#     try:
#         systolic, diastolic = map(int, bp.replace(" ", "").split('/'))
#         if systolic > 140 or diastolic > 90:
#             vitals_narr += "- Blood pressure is higher than normal. Please monitor and consult your doctor if you feel unwell.\n"
#         elif systolic < 90 or diastolic < 60:
#             vitals_narr += "- Blood pressure is lower than normal. Take rest and consult your doctor if you feel faint or dizzy.\n"
#         else:
#             vitals_narr += "- Blood pressure is within the normal range.\n"
#         any_flag = True
#     except Exception:
#         if bp:
#             vitals_narr += "- Unable to interpret blood pressure. Please check the entered value.\n"
#             any_flag = True
#     try:
#         pulse_val = int(pulse.replace(" ", ""))
#         if pulse_val < 60:
#             vitals_narr += "- Pulse is lower than normal. Rest and notify your doctor if you feel tired or dizzy.\n"
#         elif pulse_val > 100:
#             vitals_narr += "- Pulse is higher than normal. Take some rest and monitor your heart rate.\n"
#         else:
#             vitals_narr += "- Pulse is within the normal range.\n"
#         any_flag = True
#     except Exception:
#         if pulse:
#             vitals_narr += "- Unable to interpret pulse. Please check the entered value.\n"
#             any_flag = True
#     try:
#         temp_val = float(temp.replace(" ", ""))
#         if temp_val < 97:
#             vitals_narr += "- Temperature is a bit low. Keep yourself warm and monitor for any symptoms.\n"
#         elif temp_val > 99.5:
#             vitals_narr += "- Temperature is slightly elevated. Consider resting, drinking fluids, and monitoring for fever.\n"
#         else:
#             vitals_narr += "- Temperature is within the normal range.\n"
#         any_flag = True
#     except Exception:
#         if temp:
#             vitals_narr += "- Unable to interpret temperature. Please check the entered value.\n"
#             any_flag = True
#     if not any_flag:
#         vitals_narr += "- Vitals not entered."
#     return vitals_narr

# def make_narrative(answers, user_name, user_age):
#     q = answers
#     narrative = f"**Concise Report for {user_name}, Age {user_age}**\n\n"
#     if q["How are you feeling today?"] == "Good":
#         narrative += f"{user_name} is in good spirits today"
#     elif q["How are you feeling today?"] == "Okay":
#         narrative += f"{user_name} is feeling alright today"
#     else:
#         narrative += f"{user_name} is not feeling their best today"
#     if q["Did you sleep well last night?"] == "Yes":
#         narrative += ", having had a restful night's sleep. "
#     else:
#         narrative += ", though sleep was somewhat restless. "
#     if q["Have you taken your morning medication?"] == "Yes":
#         narrative += "Morning medication was taken as prescribed. "
#     elif q["Have you taken your morning medication?"] == "No":
#         narrative += "Morning medication was not taken. "
#     else:
#         narrative += "No morning medication was needed. "
#     if q["Did you eat breakfast?"] == "Yes":
#         narrative += "Breakfast was eaten. "
#     else:
#         narrative += "Breakfast was skipped. "
#     if q["Have you had water in the last hour?"] == "Yes":
#         narrative += "Hydration is being maintained. "
#     else:
#         narrative += "Hydration could be improved. "
#     pain = q["Do you feel any pain right now?"]
#     if pain == "No":
#         narrative += "There is no pain reported at this time. "
#     elif pain == "Mild":
#         narrative += "A mild level of pain has been experienced. "
#     elif pain == "Moderate":
#         narrative += "Moderate pain has been reported. "
#     else:
#         narrative += "Severe pain is currently present. "
#     if q["Are you experiencing shortness of breath?"] == "Yes":
#         narrative += "Shortness of breath is noted. "
#     if q["Do you feel dizzy or lightheaded?"] == "Yes":
#         narrative += "There is some dizziness or lightheadedness. "
#     narrative += ("The home environment is "
#         f"{'safe' if q['Do you feel safe at home?'] == 'Yes' else 'not entirely safe'}. ")
#     if q["Do you need help with any tasks today?"] == "Yes":
#         narrative += "Additional help is needed with daily tasks. "
#     if q["Do you have any appointments today?"] == "Yes":
#         narrative += "There are appointments scheduled for today. "
#     if q["Have you spoken to family or friends today?"] == "Yes":
#         narrative += "Social interaction with friends or family has occurred. "
#     else:
#         narrative += "There has been little or no social contact so far. "
#     if q["Would you like a physical activity suggestion?"] == "Yes":
#         narrative += "A physical activity suggestion would be welcome. "
#     if q["Would you like a mental activity suggestion?"] == "Yes":
#         narrative += "A mental activity suggestion would be helpful. "
#     if q["Would you like a social activity suggestion?"] == "Yes":
#         narrative += "A social activity suggestion is requested. "
#     feeling = q["Are you feeling anxious or depressed?"]
#     if feeling == "No":
#         narrative += "There are no signs of anxiety or depression. "
#     elif feeling == "A little":
#         narrative += "There is a slight feeling of anxiety or low mood. "
#     else:
#         narrative += "There are significant feelings of anxiety or depression. "
#     if q["Do you need assistance with meals?"] == "Yes":
#         narrative += "Assistance with meals is needed. "
#     if q["Did you enjoy your last activity?"] == "Yes":
#         narrative += "The previous activity was enjoyable. "
#     else:
#         narrative += "The last activity was not particularly enjoyable. "
#     if q["Would you like a wellness check call?"] == "Yes":
#         narrative += "A wellness check call is requested. "
#     if q["Do you have any concerns to share today?"] == "Yes":
#         narrative += "Some additional concerns were raised today. "
#     else:
#         narrative += "No extra concerns have been shared today. "
#     return narrative.strip()

# def make_suggestions(answers, user_name):
#     q = answers
#     suggestions = "#### Suggestions & Encouragement\n"
#     if q["How are you feeling today?"] == "Bad":
#         suggestions += f"- {user_name}, it's okay to have off days. Consider doing something you enjoy, or reaching out to a friend or loved one for support.\n"
#     elif q["How are you feeling today?"] == "Okay":
#         suggestions += "- If you want to boost your mood, a short walk or a favorite activity might help brighten your day.\n"
#     else:
#         suggestions += "- Keep up the positive energy and continue doing what makes you feel good!\n"
#     if q["Did you sleep well last night?"] == "No":
#         suggestions += "- Try to create a relaxing bedtime routine tonight, perhaps by reading or listening to soft music.\n"
#     else:
#         suggestions += "- Good sleep is valuable—keep your evening routine consistent.\n"
#     if q["Have you taken your morning medication?"] == "No":
#         suggestions += "- Please remember to take your medication as prescribed. Setting a daily reminder can be helpful.\n"
#     if q["Did you eat breakfast?"] == "No":
#         suggestions += "- Starting the day with a light breakfast can help maintain your energy.\n"
#     if q["Have you had water in the last hour?"] == "No":
#         suggestions += "- Try to keep a bottle of water nearby and sip regularly throughout the day.\n"
#     pain = q["Do you feel any pain right now?"]
#     if pain == "Mild":
#         suggestions += "- If your pain worsens, take a break and let someone know if you need help.\n"
#     elif pain == "Moderate" or pain == "Severe":
#         suggestions += "- Be sure to mention your pain to a caregiver, and don't hesitate to rest or seek assistance.\n"
#     if q["Are you experiencing shortness of breath?"] == "Yes":
#         suggestions += "- If breathing becomes difficult, sit down, rest, and seek help if it doesn't improve.\n"
#     if q["Do you feel dizzy or lightheaded?"] == "Yes":
#         suggestions += "- Please move slowly and avoid sudden movements. Rest as needed and let someone know.\n"
#     if q["Do you feel safe at home?"] == "No":
#         suggestions += "- Your safety is important. Please discuss any concerns with someone you trust or your care team.\n"
#     if q["Do you need help with any tasks today?"] == "Yes":
#         suggestions += "- Don't hesitate to ask for help with tasks—everyone needs support sometimes.\n"
#     if q["Have you spoken to family or friends today?"] == "No":
#         suggestions += "- Connecting with someone you care about can lift your spirits. Maybe call or message a friend.\n"
#     if q["Would you like a physical activity suggestion?"] == "Yes":
#         suggestions += "- Consider some gentle stretching or a short walk to keep active.\n"
#     if q["Would you like a mental activity suggestion?"] == "Yes":
#         suggestions += "- Try a puzzle, a book, or listening to music for mental stimulation.\n"
#     if q["Would you like a social activity suggestion?"] == "Yes":
#         suggestions += "- Joining a community call or chatting with a neighbor could be enjoyable.\n"
#     feeling = q["Are you feeling anxious or depressed?"]
#     if feeling == "A little":
#         suggestions += "- If you're feeling a bit down, deep breathing and talking to someone you trust can help.\n"
#     elif feeling == "Yes":
#         suggestions += "- You're not alone; reach out to a loved one or professional if you need to talk.\n"
#     if q["Do you need assistance with meals?"] == "Yes":
#         suggestions += "- Let someone know if you need help preparing or enjoying your meals today.\n"
#     if q["Did you enjoy your last activity?"] == "No":
#         suggestions += "- Maybe try a different activity today, or revisit something you enjoyed in the past.\n"
#     if q["Would you like a wellness check call?"] == "Yes":
#         suggestions += "- A wellness check will be arranged soon to make sure you're doing well.\n"
#     if q["Do you have any concerns to share today?"] == "Yes":
#         suggestions += "- Your concerns matter. Talk to your care team or someone you trust about anything on your mind.\n"
#     suggestions += "\nRemember, every small step you take toward your wellbeing is important. You’re doing your best, and that’s enough."
#     return suggestions.strip()

# if "user_name" not in st.session_state: st.session_state["user_name"] = ""
# if "user_age" not in st.session_state: st.session_state["user_age"] = 0
# if "answers" not in st.session_state: st.session_state["answers"] = {}
# if "narrative" not in st.session_state: st.session_state["narrative"] = ""
# if "suggestions" not in st.session_state: st.session_state["suggestions"] = ""
# if "narrative_generated" not in st.session_state: st.session_state["narrative_generated"] = False
# if "saved_reports" not in st.session_state: st.session_state["saved_reports"] = []
# if "vitals" not in st.session_state: st.session_state["vitals"] = {}
# if "vitals_narrative" not in st.session_state: st.session_state["vitals_narrative"] = ""
# if "last_save_success" not in st.session_state: st.session_state["last_save_success"] = False

# qa_list = [
#     ("How are you feeling today?", ["Good", "Okay", "Bad"]),
#     ("Did you sleep well last night?", ["Yes", "No"]),
#     ("Have you taken your morning medication?", ["Yes", "No", "Not Applicable"]),
#     ("Did you eat breakfast?", ["Yes", "No"]),
#     ("Have you had water in the last hour?", ["Yes", "No"]),
#     ("Do you feel any pain right now?", ["No", "Mild", "Moderate", "Severe"]),
#     ("Are you experiencing shortness of breath?", ["No", "Yes"]),
#     ("Do you feel dizzy or lightheaded?", ["No", "Yes"]),
#     ("Do you need help with any tasks today?", ["No", "Yes"]),
#     ("Do you have any appointments today?", ["No", "Yes"]),
#     ("Do you feel safe at home?", ["Yes", "No"]),
#     ("Have you spoken to family or friends today?", ["Yes", "No"]),
#     ("Would you like a physical activity suggestion?", ["Yes", "No"]),
#     ("Would you like a mental activity suggestion?", ["Yes", "No"]),
#     ("Would you like a social activity suggestion?", ["Yes", "No"]),
#     ("Are you feeling anxious or depressed?", ["No", "A little", "Yes"]),
#     ("Do you need assistance with meals?", ["No", "Yes"]),
#     ("Did you enjoy your last activity?", ["Yes", "No"]),
#     ("Would you like a wellness check call?", ["Yes", "No"]),
#     ("Do you have any concerns to share today?", ["No", "Yes"]),
# ]

# tab1, tab2, tab3, tab4 = st.tabs(["Person Info", "Q & A", "Saved Reports", "Related Videos"])

# with tab1:
#     st.header("Person Information")
#     st.session_state["user_name"] = st.text_input("Enter person name", value=st.session_state["user_name"])
#     st.session_state["user_age"] = st.number_input("Enter person age", min_value=0, max_value=120, step=1, value=st.session_state["user_age"])

# qna_disabled = (not st.session_state["user_name"].strip()) or (not st.session_state["user_age"])
# with tab2:
#     st.header("Q & A")
#     if qna_disabled:
#         st.warning("Please enter the person's name and age in the 'Person Info' tab before proceeding.")
#         st.stop()

#     st.subheader("Enter Today's Vitals (Mandatory)")
#     with st.form("vitals_form", clear_on_submit=False):
#         bp = st.text_input("Blood Pressure (e.g., 120/80 mmHg)", value=st.session_state["vitals"].get("BP", ""))
#         pulse = st.text_input("Pulse (bpm)", value=st.session_state["vitals"].get("Pulse", ""))
#         temp = st.text_input("Temperature (°F)", value=st.session_state["vitals"].get("Temperature", ""))
#         vitals_submitted = st.form_submit_button("Save Vitals")
#     if vitals_submitted:
#         st.session_state["vitals"] = {"BP": bp, "Pulse": pulse, "Temperature": temp}
#         st.success("Vitals saved.")

#     if st.session_state["vitals"]:
#         v = st.session_state["vitals"]
#         st.info(f"**Saved Vitals:** BP: {v.get('BP', '')}, Pulse: {v.get('Pulse', '')}, Temp: {v.get('Temperature', '')}")

#     qa_disabled = not (bp and pulse and temp)
#     if not (bp and pulse and temp):
#         st.warning("Please enter and save all vitals before answering the questionnaire.")
#         st.stop()
#     else:
#         for idx, (q, opts) in enumerate(qa_list):
#             prev_answer = st.session_state["answers"].get(q, opts[0])
#             answer = st.radio(q, opts, key=f"qa_{idx}", index=opts.index(prev_answer) if prev_answer in opts else 0)
#             st.session_state["answers"][q] = answer

#         if st.button("Generate Narrative Report"):
#             st.session_state["vitals_narrative"] = make_vitals_narrative(bp, pulse, temp)
#             st.session_state["narrative"] = make_narrative(st.session_state["answers"], st.session_state["user_name"], st.session_state["user_age"])
#             st.session_state["suggestions"] = make_suggestions(st.session_state["answers"], st.session_state["user_name"])
#             st.session_state["narrative_generated"] = True
#             st.session_state["last_save_success"] = False

#         if st.session_state.get("narrative_generated", False) and st.session_state["narrative"]:
#             st.markdown(st.session_state["vitals_narrative"])
#             st.markdown(st.session_state["narrative"])
#             st.markdown(st.session_state["suggestions"])
#             col1, col2 = st.columns(2)
#             with col1:
#                 if st.button("Save Report", key="save_report"):
#                     now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#                     bp = st.session_state["vitals"].get("BP", "")
#                     pulse = st.session_state["vitals"].get("Pulse", "")
#                     temp = st.session_state["vitals"].get("Temperature", "")
#                     video_links = get_vitals_video_links(bp, pulse, temp)
#                     st.session_state["saved_reports"].append({
#                         "datetime": now,
#                         "name": st.session_state["user_name"],
#                         "age": st.session_state["user_age"],
#                         "vitals": st.session_state["vitals"],
#                         "vitals_narrative": st.session_state["vitals_narrative"],
#                         "report": st.session_state["narrative"],
#                         "suggestions": st.session_state["suggestions"],
#                         "video_links": video_links,
#                     })
#                     st.success("Report saved in the 'Saved Reports' tab.")
#                     st.session_state["narrative_generated"] = False
#                     st.session_state["last_save_success"] = True
#             with col2:
#                 if st.button("Not Interested to Save", key="not_save_report"):
#                     st.session_state["narrative"] = ""
#                     st.session_state["suggestions"] = ""
#                     st.session_state["vitals_narrative"] = ""
#                     st.session_state["narrative_generated"] = False
#                     st.session_state["last_save_success"] = False
#                     st.info("Report was not saved. No video suggestion will be available until a report is saved.")

# with tab3:
#     st.header("Saved Narrative Reports")
#     if st.session_state["saved_reports"]:
#         for i, entry in enumerate(reversed(st.session_state["saved_reports"])):
#             st.markdown(f"---\n**Saved on:** {entry['datetime']}  \n**Patient:** {entry['name']}, **Age:** {entry['age']}")
#             v = entry.get("vitals", {})
#             st.markdown(f"**Vitals:** BP: {v.get('BP', '')}, Pulse: {v.get('Pulse', '')}, Temp: {v.get('Temperature', '')}")
#             st.markdown(entry.get("vitals_narrative", ""))
#             st.markdown(entry["report"])
#             st.markdown(entry["suggestions"])
#     else:
#         st.info("No report saved yet. Complete the Q & A and save the report from the previous tab.")

# with tab4:
#     st.header("Related Videos")
#     # Show videos as soon as vitals are available (do not require saving)
#     video_links = []
#     v = st.session_state.get("vitals", {})
#     bp = v.get("BP", "")
#     pulse = v.get("Pulse", "")
#     temp = v.get("Temperature", "")
#     video_links = get_vitals_video_links(bp, pulse, temp) if (bp or pulse or temp) else []
#     if video_links:
#         st.markdown("Videos matched to your entered BP, Pulse, and Temperature:")
#         for link in video_links:
#             st.video(link)
#     else:
#         st.info("Enter and save BP, Pulse, and Temperature in the Q & A tab to view related videos.")


# import streamlit as st
# from datetime import datetime

# # Set a sky blue background with a doctor's symbol (icon) on the side
# def set_bg():
#     st.markdown(
#         """
#         <style>
#         .stApp {
#             background: linear-gradient(120deg, #e0f7fa 0%, #b3e5fc 100%);
#             min-height: 100vh !important;
#             background-attachment: fixed !important;
#         }
#         /* Doctor symbol on top right, visible but subtle */
#         .doctor-symbol {
#             position: fixed;
#             top: 40px;
#             right: 50px;
#             width: 120px;
#             height: 120px;
#             opacity: 0.12;
#             z-index: 0;
#             background: url('https://cdn-icons-png.flaticon.com/512/3209/3209265.png') no-repeat center center;
#             background-size: contain;
#         }
#         /* Hide on small screens */
#         @media (max-width: 800px) {
#             .doctor-symbol { display: none; }
#         }
#         .block-container { position: relative; z-index: 2; }
#         </style>
#         <div class="doctor-symbol"></div>
#         """,
#         unsafe_allow_html=True
#     )

# set_bg()

# YOUTUBE_VITALS_MAP = {
#     "bp": "https://www.youtube.com/watch?v=pr29CWlkg8Y",
#     "pulse": "https://www.youtube.com/watch?v=BSlRvD-CZSo",
#     "temperature": "https://www.youtube.com/watch?v=E0CVdXv4RYA",
# }
# def get_vitals_video_links(bp, pulse, temp):
#     links = []
#     if bp:
#         links.append(YOUTUBE_VITALS_MAP["bp"])
#     if pulse:
#         links.append(YOUTUBE_VITALS_MAP["pulse"])
#     if temp:
#         links.append(YOUTUBE_VITALS_MAP["temperature"])
#     return list(dict.fromkeys(links))

# def make_vitals_narrative(bp, pulse, temp):
#     vitals_narr = "**Vitals Narrative:**\n"
#     any_flag = False
#     try:
#         systolic, diastolic = map(int, bp.replace(" ", "").split('/'))
#         if systolic > 140 or diastolic > 90:
#             vitals_narr += "- Blood pressure is higher than normal. Please monitor and consult your doctor if you feel unwell.\n"
#         elif systolic < 90 or diastolic < 60:
#             vitals_narr += "- Blood pressure is lower than normal. Take rest and consult your doctor if you feel faint or dizzy.\n"
#         else:
#             vitals_narr += "- Blood pressure is within the normal range.\n"
#         any_flag = True
#     except Exception:
#         if bp:
#             vitals_narr += "- Unable to interpret blood pressure. Please check the entered value.\n"
#             any_flag = True
#     try:
#         pulse_val = int(pulse.replace(" ", ""))
#         if pulse_val < 60:
#             vitals_narr += "- Pulse is lower than normal. Rest and notify your doctor if you feel tired or dizzy.\n"
#         elif pulse_val > 100:
#             vitals_narr += "- Pulse is higher than normal. Take some rest and monitor your heart rate.\n"
#         else:
#             vitals_narr += "- Pulse is within the normal range.\n"
#         any_flag = True
#     except Exception:
#         if pulse:
#             vitals_narr += "- Unable to interpret pulse. Please check the entered value.\n"
#             any_flag = True
#     try:
#         temp_val = float(temp.replace(" ", ""))
#         if temp_val < 97:
#             vitals_narr += "- Temperature is a bit low. Keep yourself warm and monitor for any symptoms.\n"
#         elif temp_val > 99.5:
#             vitals_narr += "- Temperature is slightly elevated. Consider resting, drinking fluids, and monitoring for fever.\n"
#         else:
#             vitals_narr += "- Temperature is within the normal range.\n"
#         any_flag = True
#     except Exception:
#         if temp:
#             vitals_narr += "- Unable to interpret temperature. Please check the entered value.\n"
#             any_flag = True
#     if not any_flag:
#         vitals_narr += "- Vitals not entered."
#     return vitals_narr

# def make_narrative(answers, person_name, person_age):
#     q = answers
#     narrative = f"**Concise Report for {person_name}, Age {person_age}**\n\n"
#     if q["How are you feeling today?"] == "Good":
#         narrative += f"{person_name} is in good spirits today"
#     elif q["How are you feeling today?"] == "Okay":
#         narrative += f"{person_name} is feeling alright today"
#     else:
#         narrative += f"{person_name} is not feeling their best today"
#     if q["Did you sleep well last night?"] == "Yes":
#         narrative += ", having had a restful night's sleep. "
#     else:
#         narrative += ", though sleep was somewhat restless. "
#     if q["Have you taken your morning medication?"] == "Yes":
#         narrative += "Morning medication was taken as prescribed. "
#     elif q["Have you taken your morning medication?"] == "No":
#         narrative += "Morning medication was not taken. "
#     else:
#         narrative += "No morning medication was needed. "
#     if q["Did you eat breakfast?"] == "Yes":
#         narrative += "Breakfast was eaten. "
#     else:
#         narrative += "Breakfast was skipped. "
#     if q["Have you had water in the last hour?"] == "Yes":
#         narrative += "Hydration is being maintained. "
#     else:
#         narrative += "Hydration could be improved. "
#     pain = q["Do you feel any pain right now?"]
#     if pain == "No":
#         narrative += "There is no pain reported at this time. "
#     elif pain == "Mild":
#         narrative += "A mild level of pain has been experienced. "
#     elif pain == "Moderate":
#         narrative += "Moderate pain has been reported. "
#     else:
#         narrative += "Severe pain is currently present. "
#     if q["Are you experiencing shortness of breath?"] == "Yes":
#         narrative += "Shortness of breath is noted. "
#     if q["Do you feel dizzy or lightheaded?"] == "Yes":
#         narrative += "There is some dizziness or lightheadedness. "
#     narrative += ("The home environment is "
#         f"{'safe' if q['Do you feel safe at home?'] == 'Yes' else 'not entirely safe'}. ")
#     if q["Do you need help with any tasks today?"] == "Yes":
#         narrative += "Additional help is needed with daily tasks. "
#     if q["Do you have any appointments today?"] == "Yes":
#         narrative += "There are appointments scheduled for today. "
#     if q["Have you spoken to family or friends today?"] == "Yes":
#         narrative += "Social interaction with friends or family has occurred. "
#     else:
#         narrative += "There has been little or no social contact so far. "
#     if q["Would you like a physical activity suggestion?"] == "Yes":
#         narrative += "A physical activity suggestion would be welcome. "
#     if q["Would you like a mental activity suggestion?"] == "Yes":
#         narrative += "A mental activity suggestion would be helpful. "
#     if q["Would you like a social activity suggestion?"] == "Yes":
#         narrative += "A social activity suggestion is requested. "
#     feeling = q["Are you feeling anxious or depressed?"]
#     if feeling == "No":
#         narrative += "There are no signs of anxiety or depression. "
#     elif feeling == "A little":
#         narrative += "There is a slight feeling of anxiety or low mood. "
#     else:
#         narrative += "There are significant feelings of anxiety or depression. "
#     if q["Do you need assistance with meals?"] == "Yes":
#         narrative += "Assistance with meals is needed. "
#     if q["Did you enjoy your last activity?"] == "Yes":
#         narrative += "The previous activity was enjoyable. "
#     else:
#         narrative += "The last activity was not particularly enjoyable. "
#     if q["Would you like a wellness check call?"] == "Yes":
#         narrative += "A wellness check call is requested. "
#     if q["Do you have any concerns to share today?"] == "Yes":
#         narrative += "Some additional concerns were raised today. "
#     else:
#         narrative += "No extra concerns have been shared today. "
#     return narrative.strip()

# def make_suggestions(answers, person_name):
#     q = answers
#     suggestions = "#### Suggestions & Encouragement\n"
#     if q["How are you feeling today?"] == "Bad":
#         suggestions += f"- {person_name}, it's okay to have off days. Consider doing something you enjoy, or reaching out to a friend or loved one for support.\n"
#     elif q["How are you feeling today?"] == "Okay":
#         suggestions += "- If you want to boost your mood, a short walk or a favorite activity might help brighten your day.\n"
#     else:
#         suggestions += "- Keep up the positive energy and continue doing what makes you feel good!\n"
#     if q["Did you sleep well last night?"] == "No":
#         suggestions += "- Try to create a relaxing bedtime routine tonight, perhaps by reading or listening to soft music.\n"
#     else:
#         suggestions += "- Good sleep is valuable—keep your evening routine consistent.\n"
#     if q["Have you taken your morning medication?"] == "No":
#         suggestions += "- Please remember to take your medication as prescribed. Setting a daily reminder can be helpful.\n"
#     if q["Did you eat breakfast?"] == "No":
#         suggestions += "- Starting the day with a light breakfast can help maintain your energy.\n"
#     if q["Have you had water in the last hour?"] == "No":
#         suggestions += "- Try to keep a bottle of water nearby and sip regularly throughout the day.\n"
#     pain = q["Do you feel any pain right now?"]
#     if pain == "Mild":
#         suggestions += "- If your pain worsens, take a break and let someone know if you need help.\n"
#     elif pain == "Moderate" or pain == "Severe":
#         suggestions += "- Be sure to mention your pain to a caregiver, and don't hesitate to rest or seek assistance.\n"
#     if q["Are you experiencing shortness of breath?"] == "Yes":
#         suggestions += "- If breathing becomes difficult, sit down, rest, and seek help if it doesn't improve.\n"
#     if q["Do you feel dizzy or lightheaded?"] == "Yes":
#         suggestions += "- Please move slowly and avoid sudden movements. Rest as needed and let someone know.\n"
#     if q["Do you feel safe at home?"] == "No":
#         suggestions += "- Your safety is important. Please discuss any concerns with someone you trust or your care team.\n"
#     if q["Do you need help with any tasks today?"] == "Yes":
#         suggestions += "- Don't hesitate to ask for help with tasks—everyone needs support sometimes.\n"
#     if q["Have you spoken to family or friends today?"] == "No":
#         suggestions += "- Connecting with someone you care about can lift your spirits. Maybe call or message a friend.\n"
#     if q["Would you like a physical activity suggestion?"] == "Yes":
#         suggestions += "- Consider some gentle stretching or a short walk to keep active.\n"
#     if q["Would you like a mental activity suggestion?"] == "Yes":
#         suggestions += "- Try a puzzle, a book, or listening to music for mental stimulation.\n"
#     if q["Would you like a social activity suggestion?"] == "Yes":
#         suggestions += "- Joining a community call or chatting with a neighbor could be enjoyable.\n"
#     feeling = q["Are you feeling anxious or depressed?"]
#     if feeling == "A little":
#         suggestions += "- If you're feeling a bit down, deep breathing and talking to someone you trust can help.\n"
#     elif feeling == "Yes":
#         suggestions += "- You're not alone; reach out to a loved one or professional if you need to talk.\n"
#     if q["Do you need assistance with meals?"] == "Yes":
#         suggestions += "- Let someone know if you need help preparing or enjoying your meals today.\n"
#     if q["Did you enjoy your last activity?"] == "No":
#         suggestions += "- Maybe try a different activity today, or revisit something you enjoyed in the past.\n"
#     if q["Would you like a wellness check call?"] == "Yes":
#         suggestions += "- A wellness check will be arranged soon to make sure you're doing well.\n"
#     if q["Do you have any concerns to share today?"] == "Yes":
#         suggestions += "- Your concerns matter. Talk to your care team or someone you trust about anything on your mind.\n"
#     suggestions += "\nRemember, every small step you take toward your wellbeing is important. You’re doing your best, and that’s enough."
#     return suggestions.strip()

# if "person_name" not in st.session_state: st.session_state["person_name"] = ""
# if "person_age" not in st.session_state: st.session_state["person_age"] = 0
# if "answers" not in st.session_state: st.session_state["answers"] = {}
# if "narrative" not in st.session_state: st.session_state["narrative"] = ""
# if "suggestions" not in st.session_state: st.session_state["suggestions"] = ""
# if "narrative_generated" not in st.session_state: st.session_state["narrative_generated"] = False
# if "saved_reports" not in st.session_state: st.session_state["saved_reports"] = []
# if "vitals" not in st.session_state: st.session_state["vitals"] = {}
# if "vitals_narrative" not in st.session_state: st.session_state["vitals_narrative"] = ""
# if "last_save_success" not in st.session_state: st.session_state["last_save_success"] = False

# qa_list = [
#     ("How are you feeling today?", ["Good", "Okay", "Bad"]),
#     ("Did you sleep well last night?", ["Yes", "No"]),
#     ("Have you taken your morning medication?", ["Yes", "No", "Not Applicable"]),
#     ("Did you eat breakfast?", ["Yes", "No"]),
#     ("Have you had water in the last hour?", ["Yes", "No"]),
#     ("Do you feel any pain right now?", ["No", "Mild", "Moderate", "Severe"]),
#     ("Are you experiencing shortness of breath?", ["No", "Yes"]),
#     ("Do you feel dizzy or lightheaded?", ["No", "Yes"]),
#     ("Do you need help with any tasks today?", ["No", "Yes"]),
#     ("Do you have any appointments today?", ["No", "Yes"]),
#     ("Do you feel safe at home?", ["Yes", "No"]),
#     ("Have you spoken to family or friends today?", ["Yes", "No"]),
#     ("Would you like a physical activity suggestion?", ["Yes", "No"]),
#     ("Would you like a mental activity suggestion?", ["Yes", "No"]),
#     ("Would you like a social activity suggestion?", ["Yes", "No"]),
#     ("Are you feeling anxious or depressed?", ["No", "A little", "Yes"]),
#     ("Do you need assistance with meals?", ["No", "Yes"]),
#     ("Did you enjoy your last activity?", ["Yes", "No"]),
#     ("Would you like a wellness check call?", ["Yes", "No"]),
#     ("Do you have any concerns to share today?", ["No", "Yes"]),
# ]

# tab1, tab2, tab3, tab4 = st.tabs(["Person Info", "Q & A", "Saved Reports", "Related Videos"])

# with tab1:
#     st.header("Person Information")
#     st.session_state["person_name"] = st.text_input("Enter person name", value=st.session_state["person_name"])
#     st.session_state["person_age"] = st.number_input("Enter person age", min_value=0, max_value=120, step=1, value=st.session_state["person_age"])

# qna_disabled = (not st.session_state["person_name"].strip()) or (not st.session_state["person_age"])
# with tab2:
#     st.header("Q & A")
#     if qna_disabled:
#         st.warning("Please enter the person's name and age in the 'Person Info' tab before proceeding.")
#         st.stop()

#     st.subheader("Enter Today's Vitals (Mandatory)")
#     with st.form("vitals_form", clear_on_submit=False):
#         bp = st.text_input("Blood Pressure (e.g., 120/80 mmHg)", value=st.session_state["vitals"].get("BP", ""))
#         pulse = st.text_input("Pulse (bpm)", value=st.session_state["vitals"].get("Pulse", ""))
#         temp = st.text_input("Temperature (°F)", value=st.session_state["vitals"].get("Temperature", ""))
#         vitals_submitted = st.form_submit_button("Save Vitals")
#     if vitals_submitted:
#         st.session_state["vitals"] = {"BP": bp, "Pulse": pulse, "Temperature": temp}
#         st.success("Vitals saved.")

#     if st.session_state["vitals"]:
#         v = st.session_state["vitals"]
#         st.info(f"**Saved Vitals:** BP: {v.get('BP', '')}, Pulse: {v.get('Pulse', '')}, Temp: {v.get('Temperature', '')}")

#     qa_disabled = not (bp and pulse and temp)
#     if not (bp and pulse and temp):
#         st.warning("Please enter and save all vitals before answering the questionnaire.")
#         st.stop()
#     else:
#         for idx, (q, opts) in enumerate(qa_list):
#             prev_answer = st.session_state["answers"].get(q, opts[0])
#             answer = st.radio(q, opts, key=f"qa_{idx}", index=opts.index(prev_answer) if prev_answer in opts else 0)
#             st.session_state["answers"][q] = answer

#         if st.button("Generate Narrative Report"):
#             st.session_state["vitals_narrative"] = make_vitals_narrative(bp, pulse, temp)
#             st.session_state["narrative"] = make_narrative(st.session_state["answers"], st.session_state["person_name"], st.session_state["person_age"])
#             st.session_state["suggestions"] = make_suggestions(st.session_state["answers"], st.session_state["person_name"])
#             st.session_state["narrative_generated"] = True
#             st.session_state["last_save_success"] = False

#         if st.session_state.get("narrative_generated", False) and st.session_state["narrative"]:
#             st.markdown(st.session_state["vitals_narrative"])
#             st.markdown(st.session_state["narrative"])
#             st.markdown(st.session_state["suggestions"])
#             col1, col2 = st.columns(2)
#             with col1:
#                 if st.button("Save Report", key="save_report"):
#                     now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#                     bp = st.session_state["vitals"].get("BP", "")
#                     pulse = st.session_state["vitals"].get("Pulse", "")
#                     temp = st.session_state["vitals"].get("Temperature", "")
#                     video_links = get_vitals_video_links(bp, pulse, temp)
#                     st.session_state["saved_reports"].append({
#                         "datetime": now,
#                         "name": st.session_state["person_name"],
#                         "age": st.session_state["person_age"],
#                         "vitals": st.session_state["vitals"],
#                         "vitals_narrative": st.session_state["vitals_narrative"],
#                         "report": st.session_state["narrative"],
#                         "suggestions": st.session_state["suggestions"],
#                         "video_links": video_links,
#                     })
#                     st.success("Report saved in the 'Saved Reports' tab.")
#                     st.session_state["narrative_generated"] = False
#                     st.session_state["last_save_success"] = True
#             with col2:
#                 if st.button("Not Interested to Save", key="not_save_report"):
#                     st.session_state["narrative"] = ""
#                     st.session_state["suggestions"] = ""
#                     st.session_state["vitals_narrative"] = ""
#                     st.session_state["narrative_generated"] = False
#                     st.session_state["last_save_success"] = False
#                     st.info("Report was not saved. No video suggestion will be available until a report is saved.")

# with tab3:
#     st.header("Saved Narrative Reports")
#     if st.session_state["saved_reports"]:
#         for i, entry in enumerate(reversed(st.session_state["saved_reports"])):
#             st.markdown(f"---\n**Saved on:** {entry['datetime']}  \n**Person:** {entry['name']}, **Age:** {entry['age']}")
#             v = entry.get("vitals", {})
#             st.markdown(f"**Vitals:** BP: {v.get('BP', '')}, Pulse: {v.get('Pulse', '')}, Temp: {v.get('Temperature', '')}")
#             st.markdown(entry.get("vitals_narrative", ""))
#             st.markdown(entry["report"])
#             st.markdown(entry["suggestions"])
#     else:
#         st.info("No report saved yet. Complete the Q & A and save the report from the previous tab.")

# with tab4:
#     st.header("Related Videos")
#     # Show videos as soon as vitals are available (do not require saving)
#     video_links = []
#     v = st.session_state.get("vitals", {})
#     bp = v.get("BP", "")
#     pulse = v.get("Pulse", "")
#     temp = v.get("Temperature", "")
#     video_links = get_vitals_video_links(bp, pulse, temp) if (bp or pulse or temp) else []
#     if video_links:
#         st.markdown("Videos matched to your entered BP, Pulse, and Temperature:")
#         for link in video_links:
#             st.video(link)
#     else:
#         st.info("Enter and save BP, Pulse, and Temperature in the Q & A tab to view related videos.")

import streamlit as st
from datetime import datetime

# Set a sky blue background with a doctor's symbol (icon) on the side
def set_bg():
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(120deg, #e0f7fa 0%, #b3e5fc 100%);
            min-height: 100vh !important;
            background-attachment: fixed !important;
        }
        /* Doctor symbol on top right, visible but subtle */
        .doctor-symbol {
            position: fixed;
            top: 40px;
            right: 50px;
            width: 120px;
            height: 120px;
            opacity: 0.12;
            z-index: 0;
            background: url('https://cdn-icons-png.flaticon.com/512/3209/3209265.png') no-repeat center center;
            background-size: contain;
        }
        /* Hide on small screens */
        @media (max-width: 800px) {
            .doctor-symbol { display: none; }
        }
        .block-container { position: relative; z-index: 2; }
        </style>
        <div class="doctor-symbol"></div>
        """,
        unsafe_allow_html=True
    )

set_bg()

YOUTUBE_VITALS_MAP = {
    "bp": "https://www.youtube.com/watch?v=pr29CWlkg8Y",
    "pulse": "https://www.youtube.com/watch?v=BSlRvD-CZSo",
    "temperature": "https://www.youtube.com/watch?v=E0CVdXv4RYA",
}

def get_vitals_video_links(bp, pulse, temp):
    links = []
    if bp:
        links.append(YOUTUBE_VITALS_MAP["bp"])
    if pulse:
        links.append(YOUTUBE_VITALS_MAP["pulse"])
    if temp:
        links.append(YOUTUBE_VITALS_MAP["temperature"])
    return list(dict.fromkeys(links))

def make_vitals_narrative(bp, pulse, temp):
    vitals_narr = "**Vitals Narrative:**\n"
    any_flag = False
    try:
        systolic, diastolic = map(int, bp.replace(" ", "").split('/'))
        if systolic > 140 or diastolic > 90:
            vitals_narr += "- Blood pressure is higher than normal. Please monitor and consult your doctor if you feel unwell.\n"
        elif systolic < 90 or diastolic < 60:
            vitals_narr += "- Blood pressure is lower than normal. Take rest and consult your doctor if you feel faint or dizzy.\n"
        else:
            vitals_narr += "- Blood pressure is within the normal range.\n"
        any_flag = True
    except Exception:
        if bp:
            vitals_narr += "- Unable to interpret blood pressure. Please check the entered value.\n"
            any_flag = True
    try:
        pulse_val = int(pulse.replace(" ", ""))
        if pulse_val < 60:
            vitals_narr += "- Pulse is lower than normal. Rest and notify your doctor if you feel tired or dizzy.\n"
        elif pulse_val > 100:
            vitals_narr += "- Pulse is higher than normal. Take some rest and monitor your heart rate.\n"
        else:
            vitals_narr += "- Pulse is within the normal range.\n"
        any_flag = True
    except Exception:
        if pulse:
            vitals_narr += "- Unable to interpret pulse. Please check the entered value.\n"
            any_flag = True
    try:
        temp_val = float(temp.replace(" ", ""))
        if temp_val < 97:
            vitals_narr += "- Temperature is a bit low. Keep yourself warm and monitor for any symptoms.\n"
        elif temp_val > 99.5:
            vitals_narr += "- Temperature is slightly elevated. Consider resting, drinking fluids, and monitoring for fever.\n"
        else:
            vitals_narr += "- Temperature is within the normal range.\n"
        any_flag = True
    except Exception:
        if temp:
            vitals_narr += "- Unable to interpret temperature. Please check the entered value.\n"
            any_flag = True
    if not any_flag:
        vitals_narr += "- Vitals not entered."
    return vitals_narr

def make_narrative(answers, person_name, person_age):
    q = answers
    narrative = f"**Concise Report for {person_name}, Age {person_age}**\n\n"
    if q["How are you feeling today?"] == "Good":
        narrative += f"{person_name} is in good spirits today"
    elif q["How are you feeling today?"] == "Okay":
        narrative += f"{person_name} is feeling alright today"
    else:
        narrative += f"{person_name} is not feeling their best today"
    if q["Did you sleep well last night?"] == "Yes":
        narrative += ", having had a restful night's sleep. "
    else:
        narrative += ", though sleep was somewhat restless. "
    if q["Have you taken your morning medication?"] == "Yes":
        narrative += "Morning medication was taken as prescribed. "
    elif q["Have you taken your morning medication?"] == "No":
        narrative += "Morning medication was not taken. "
    else:
        narrative += "No morning medication was needed. "
    if q["Did you eat breakfast?"] == "Yes":
        narrative += "Breakfast was eaten. "
    else:
        narrative += "Breakfast was skipped. "
    if q["Have you had water in the last hour?"] == "Yes":
        narrative += "Hydration is being maintained. "
    else:
        narrative += "Hydration could be improved. "
    pain = q["Do you feel any pain right now?"]
    if pain == "No":
        narrative += "There is no pain reported at this time. "
    elif pain == "Mild":
        narrative += "A mild level of pain has been experienced. "
    elif pain == "Moderate":
        narrative += "Moderate pain has been reported. "
    else:
        narrative += "Severe pain is currently present. "
    if q["Are you experiencing shortness of breath?"] == "Yes":
        narrative += "Shortness of breath is noted. "
    if q["Do you feel dizzy or lightheaded?"] == "Yes":
        narrative += "There is some dizziness or lightheadedness. "
    narrative += ("The home environment is "
        f"{'safe' if q['Do you feel safe at home?'] == 'Yes' else 'not entirely safe'}. ")
    if q["Do you need help with any tasks today?"] == "Yes":
        narrative += "Additional help is needed with daily tasks. "
    if q["Do you have any appointments today?"] == "Yes":
        narrative += "There are appointments scheduled for today. "
    if q["Have you spoken to family or friends today?"] == "Yes":
        narrative += "Social interaction with friends or family has occurred. "
    else:
        narrative += "There has been little or no social contact so far. "
    if q["Would you like a physical activity suggestion?"] == "Yes":
        narrative += "A physical activity suggestion would be welcome. "
    if q["Would you like a mental activity suggestion?"] == "Yes":
        narrative += "A mental activity suggestion would be helpful. "
    if q["Would you like a social activity suggestion?"] == "Yes":
        narrative += "A social activity suggestion is requested. "
    feeling = q["Are you feeling anxious or depressed?"]
    if feeling == "No":
        narrative += "There are no signs of anxiety or depression. "
    elif feeling == "A little":
        narrative += "There is a slight feeling of anxiety or low mood. "
    else:
        narrative += "There are significant feelings of anxiety or depression. "
    if q["Do you need assistance with meals?"] == "Yes":
        narrative += "Assistance with meals is needed. "
    if q["Did you enjoy your last activity?"] == "Yes":
        narrative += "The previous activity was enjoyable. "
    else:
        narrative += "The last activity was not particularly enjoyable. "
    if q["Would you like a wellness check call?"] == "Yes":
        narrative += "A wellness check call is requested. "
    if q["Do you have any concerns to share today?"] == "Yes":
        narrative += "Some additional concerns were raised today. "
    else:
        narrative += "No extra concerns have been shared today. "
    return narrative.strip()

def make_suggestions(answers, person_name):
    q = answers
    suggestions = "#### Suggestions & Encouragement\n"
    if q["How are you feeling today?"] == "Bad":
        suggestions += f"- {person_name}, it's okay to have off days. Consider doing something you enjoy, or reaching out to a friend or loved one for support.\n"
    elif q["How are you feeling today?"] == "Okay":
        suggestions += "- If you want to boost your mood, a short walk or a favorite activity might help brighten your day.\n"
    else:
        suggestions += "- Keep up the positive energy and continue doing what makes you feel good!\n"
    if q["Did you sleep well last night?"] == "No":
        suggestions += "- Try to create a relaxing bedtime routine tonight, perhaps by reading or listening to soft music.\n"
    else:
        suggestions += "- Good sleep is valuable—keep your evening routine consistent.\n"
    if q["Have you taken your morning medication?"] == "No":
        suggestions += "- Please remember to take your medication as prescribed. Setting a daily reminder can be helpful.\n"
    if q["Did you eat breakfast?"] == "No":
        suggestions += "- Starting the day with a light breakfast can help maintain your energy.\n"
    if q["Have you had water in the last hour?"] == "No":
        suggestions += "- Try to keep a bottle of water nearby and sip regularly throughout the day.\n"
    pain = q["Do you feel any pain right now?"]
    if pain == "Mild":
        suggestions += "- If your pain worsens, take a break and let someone know if you need help.\n"
    elif pain == "Moderate" or pain == "Severe":
        suggestions += "- Be sure to mention your pain to a caregiver, and don't hesitate to rest or seek assistance.\n"
    if q["Are you experiencing shortness of breath?"] == "Yes":
        suggestions += "- If breathing becomes difficult, sit down, rest, and seek help if it doesn't improve.\n"
    if q["Do you feel dizzy or lightheaded?"] == "Yes":
        suggestions += "- Please move slowly and avoid sudden movements. Rest as needed and let someone know.\n"
    if q["Do you feel safe at home?"] == "No":
        suggestions += "- Your safety is important. Please discuss any concerns with someone you trust or your care team.\n"
    if q["Do you need help with any tasks today?"] == "Yes":
        suggestions += "- Don't hesitate to ask for help with tasks—everyone needs support sometimes.\n"
    if q["Have you spoken to family or friends today?"] == "No":
        suggestions += "- Connecting with someone you care about can lift your spirits. Maybe call or message a friend.\n"
    if q["Would you like a physical activity suggestion?"] == "Yes":
        suggestions += "- Consider some gentle stretching or a short walk to keep active.\n"
    if q["Would you like a mental activity suggestion?"] == "Yes":
        suggestions += "- Try a puzzle, a book, or listening to music for mental stimulation.\n"
    if q["Would you like a social activity suggestion?"] == "Yes":
        suggestions += "- Joining a community call or chatting with a neighbor could be enjoyable.\n"
    feeling = q["Are you feeling anxious or depressed?"]
    if feeling == "A little":
        suggestions += "- If you're feeling a bit down, deep breathing and talking to someone you trust can help.\n"
    elif feeling == "Yes":
        suggestions += "- You're not alone; reach out to a loved one or professional if you need to talk.\n"
    if q["Do you need assistance with meals?"] == "Yes":
        suggestions += "- Let someone know if you need help preparing or enjoying your meals today.\n"
    if q["Did you enjoy your last activity?"] == "No":
        suggestions += "- Maybe try a different activity today, or revisit something you enjoyed in the past.\n"
    if q["Would you like a wellness check call?"] == "Yes":
        suggestions += "- A wellness check will be arranged soon to make sure you're doing well.\n"
    if q["Do you have any concerns to share today?"] == "Yes":
        suggestions += "- Your concerns matter. Talk to your care team or someone you trust about anything on your mind.\n"
    suggestions += "\nRemember, every small step you take toward your wellbeing is important. You’re doing your best, and that’s enough."
    return suggestions.strip()

# --- Added CareGivingRobot class for testing ---
class CareGivingRobot:
    """
    A generic care-giving robot logic class for testing.
    """
    def __init__(self, name="CareBot", version="1.0"):
        self.name = name
        self.version = version

    def generate_report(self, answers, person_name, person_age, bp, pulse, temp):
        vitals = make_vitals_narrative(bp, pulse, temp)
        narrative = make_narrative(answers, person_name, person_age)
        suggestions = make_suggestions(answers, person_name)
        return {
            "vitals": vitals,
            "narrative": narrative,
            "suggestions": suggestions
        }

    def video_links_for_vitals(self, bp, pulse, temp):
        return get_vitals_video_links(bp, pulse, temp)

# --- End CareGivingRobot class ---

if "person_name" not in st.session_state: st.session_state["person_name"] = ""
if "person_age" not in st.session_state: st.session_state["person_age"] = 0
if "answers" not in st.session_state: st.session_state["answers"] = {}
if "narrative" not in st.session_state: st.session_state["narrative"] = ""
if "suggestions" not in st.session_state: st.session_state["suggestions"] = ""
if "narrative_generated" not in st.session_state: st.session_state["narrative_generated"] = False
if "saved_reports" not in st.session_state: st.session_state["saved_reports"] = []
if "vitals" not in st.session_state: st.session_state["vitals"] = {}
if "vitals_narrative" not in st.session_state: st.session_state["vitals_narrative"] = ""
if "last_save_success" not in st.session_state: st.session_state["last_save_success"] = False

qa_list = [
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

tab1, tab2, tab3, tab4 = st.tabs(["Person Info", "Q & A", "Saved Reports", "Related Videos"])

with tab1:
    st.header("Person Information")
    st.session_state["person_name"] = st.text_input("Enter person name", value=st.session_state["person_name"])
    st.session_state["person_age"] = st.number_input("Enter person age", min_value=0, max_value=120, step=1, value=st.session_state["person_age"])

qna_disabled = (not st.session_state["person_name"].strip()) or (not st.session_state["person_age"])
with tab2:
    st.header("Q & A")
    if qna_disabled:
        st.warning("Please enter the person's name and age in the 'Person Info' tab before proceeding.")
        st.stop()

    st.subheader("Enter Today's Vitals (Mandatory)")
    with st.form("vitals_form", clear_on_submit=False):
        bp = st.text_input("Blood Pressure (e.g., 120/80 mmHg)", value=st.session_state["vitals"].get("BP", ""))
        pulse = st.text_input("Pulse (bpm)", value=st.session_state["vitals"].get("Pulse", ""))
        temp = st.text_input("Temperature (°F)", value=st.session_state["vitals"].get("Temperature", ""))
        vitals_submitted = st.form_submit_button("Save Vitals")
    if vitals_submitted:
        st.session_state["vitals"] = {"BP": bp, "Pulse": pulse, "Temperature": temp}
        st.success("Vitals saved.")

    if st.session_state["vitals"]:
        v = st.session_state["vitals"]
        st.info(f"**Saved Vitals:** BP: {v.get('BP', '')}, Pulse: {v.get('Pulse', '')}, Temp: {v.get('Temperature', '')}")

    qa_disabled = not (bp and pulse and temp)
    if not (bp and pulse and temp):
        st.warning("Please enter and save all vitals before answering the questionnaire.")
        st.stop()
    else:
        for idx, (q, opts) in enumerate(qa_list):
            prev_answer = st.session_state["answers"].get(q, opts[0])
            answer = st.radio(q, opts, key=f"qa_{idx}", index=opts.index(prev_answer) if prev_answer in opts else 0)
            st.session_state["answers"][q] = answer

        if st.button("Generate Narrative Report"):
            st.session_state["vitals_narrative"] = make_vitals_narrative(bp, pulse, temp)
            st.session_state["narrative"] = make_narrative(st.session_state["answers"], st.session_state["person_name"], st.session_state["person_age"])
            st.session_state["suggestions"] = make_suggestions(st.session_state["answers"], st.session_state["person_name"])
            st.session_state["narrative_generated"] = True
            st.session_state["last_save_success"] = False

        if st.session_state.get("narrative_generated", False) and st.session_state["narrative"]:
            st.markdown(st.session_state["vitals_narrative"])
            st.markdown(st.session_state["narrative"])
            st.markdown(st.session_state["suggestions"])
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Save Report", key="save_report"):
                    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    bp = st.session_state["vitals"].get("BP", "")
                    pulse = st.session_state["vitals"].get("Pulse", "")
                    temp = st.session_state["vitals"].get("Temperature", "")
                    video_links = get_vitals_video_links(bp, pulse, temp)
                    st.session_state["saved_reports"].append({
                        "datetime": now,
                        "name": st.session_state["person_name"],
                        "age": st.session_state["person_age"],
                        "vitals": st.session_state["vitals"],
                        "vitals_narrative": st.session_state["vitals_narrative"],
                        "report": st.session_state["narrative"],
                        "suggestions": st.session_state["suggestions"],
                        "video_links": video_links,
                    })
                    st.success("Report saved in the 'Saved Reports' tab.")
                    st.session_state["narrative_generated"] = False
                    st.session_state["last_save_success"] = True
            with col2:
                if st.button("Not Interested to Save", key="not_save_report"):
                    st.session_state["narrative"] = ""
                    st.session_state["suggestions"] = ""
                    st.session_state["vitals_narrative"] = ""
                    st.session_state["narrative_generated"] = False
                    st.session_state["last_save_success"] = False
                    st.info("Report was not saved. No video suggestion will be available until a report is saved.")

with tab3:
    st.header("Saved Narrative Reports")
    if st.session_state["saved_reports"]:
        for i, entry in enumerate(reversed(st.session_state["saved_reports"])):
            st.markdown(f"---\n**Saved on:** {entry['datetime']}  \n**Person:** {entry['name']}, **Age:** {entry['age']}")
            v = entry.get("vitals", {})
            st.markdown(f"**Vitals:** BP: {v.get('BP', '')}, Pulse: {v.get('Pulse', '')}, Temp: {v.get('Temperature', '')}")
            st.markdown(entry.get("vitals_narrative", ""))
            st.markdown(entry["report"])
            st.markdown(entry["suggestions"])
    else:
        st.info("No report saved yet. Complete the Q & A and save the report from the previous tab.")

with tab4:
    st.header("Related Videos")
    # Show videos as soon as vitals are available (do not require saving)
    video_links = []
    v = st.session_state.get("vitals", {})
    bp = v.get("BP", "")
    pulse = v.get("Pulse", "")
    temp = v.get("Temperature", "")
    video_links = get_vitals_video_links(bp, pulse, temp) if (bp or pulse or temp) else []
    if video_links:
        st.markdown("Videos matched to your entered BP, Pulse, and Temperature:")
        for link in video_links:
            st.video(link)
    else:
        st.info("Enter and save BP, Pulse, and Temperature in the Q & A tab to view related videos.")