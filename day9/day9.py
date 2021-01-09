# dic = {
#     "a":"aaa",
#     "b":"bbb"
# }
#
# print(dic)
# print(dic["a"])
# print(dic["b"])
#
# empty_dictionary = {}
# print(empty_dictionary)
#
# dic["a"] = "aaaaa"
# print(dic)
#
# #Loop through a dictionary
# for thing in dic:
#     print(thing)

# grading program
student_scores = {
    "Harry" : 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco" : 74,
    "Neville": 62
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

#print(student_grades)
#######################

travel_log = {
    "France" : {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany" : {"cities_visited" : ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5}

}
print(travel_log["France"]["cities_visited"])

starting_dictionary = {
    "a": 9,
    "b": 8,
}


final_dictionary = {
    "a": 9,
    "b": 8,
    "c": 7,
}


