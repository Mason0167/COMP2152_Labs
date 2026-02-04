monday_class = {"Alice", "Bob", "Charlie", "Diana"}
wednesday_class = {"Bob", "Diana", "Eve", "Frank"}

monday_class.add("Grace")
print("Monday class: ", monday_class)
print("Wednesday class: ", wednesday_class)

both_class = monday_class & wednesday_class
print("Attend both classes: ", both_class)

allStudents = monday_class or wednesday_class
print("Attend either class: ", allStudents)

onlyMondayClass = monday_class - wednesday_class
print("Only attend Monday class: ", onlyMondayClass)

onlyOne = monday_class ^ wednesday_class
print("Only one class", onlyOne)

print("Is Monday subset of all students?", monday_class <= wednesday_class)

