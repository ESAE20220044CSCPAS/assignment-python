#question 1

import re
Information = {
    "Name" : "ADEKOYA ADESESAN R",
    "Course" : "Computer Science",
    "Level" : "200",
    "Gender" : "Male"
}
pattern= r"1"
matching_value= [value for value in Information.keys() if re.search(pattern,value)]
replaced_dict = {}
for key, value in Information.items():
    replaced_value = re.sub(pattern, "g", value)
    replaced_dict[key] = replaced_value
    print (replaced_dict)

#question 2
Set = "Male501"
print (set[:-3])
print (Set[0:5])