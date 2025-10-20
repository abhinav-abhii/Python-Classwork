Python={"Abhinav","Afsal","Azar"}
Data_science={"Abhinav","Aromal","Abdu","Anandhu"}
print("Students enrolled in Python:", Python)
print("Students enrolled in Data Science:", Data_science)

Python.add("Nimal")
print("After adding:", Python)

Data_science.remove("Abdu")
print("After removing:", Data_science)

intersection=Python.intersection(Data_science)
print("Students enrolled in both Python and Data Science:", intersection)

print("Students enrolled in Python not in Data Science:",Python.difference(Data_science))

print("Students enrolled in Both courses:",Data_science.union(Python))

dict={
    "Python":len(Python),
    "Data Science":len(Data_science)
}

for course, count in dict.items():
    print(f"Course: {course}, Students: {count}")

    growth_forecast = {course: count * 2 for course, count in dict.items()}
print("Expected growth:", growth_forecast)