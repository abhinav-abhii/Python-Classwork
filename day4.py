web_development =["Afreen","Ashir","Abdu"]
data_science=["Abhinav","Aromal","Anandhu"]
uiux_design=["Afsal","Azar","Nimal"]

all_participants =[web_development, data_science, uiux_design]
print("All Participants:", all_participants)

web_development.append("Maharaja")
print("After adding a participant to Web Development:", web_development)

data_science.insert(1,"Zara")
print("After inserting participant to Data Science:", data_science)

uiux_design.pop()
print("After removing last participant from UI/UX Design:", uiux_design)

new_data_science=data_science.copy()
data_science.clear()
print("New Data Science list:", new_data_science)

print("First two:",web_development[:2])
name_lengths = [len(name) for name in new_data_science]
print("Lengths of Data Science participant names:", name_lengths)

if "Asha" in web_development or "Asha" in data_science or "Asha" in uiux_design:
    print("Asha is enrolled in one of the courses")
else:
    print("Asha is not enrolled in any course")

first_participants=(web_development[0],new_data_science[0],uiux_design[0])
print("First participants from each course:", first_participants)    