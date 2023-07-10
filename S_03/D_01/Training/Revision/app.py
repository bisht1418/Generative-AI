# Monday Evaluation

# Answer a
def reverseStr(str):
    revStr = ""
    for x in str:
        revStr = x + revStr

    return revStr


ans = reverseStr("Python is fun")
print(ans)


# =================================================

employees = [
    {"name": "Neeraj", "salary": 400, "designation": "ceo"},
    {"name": "Anmol", "salary": 800, "designation": "ssd"},
    {"name": "Dheeraj", "salary": 10, "designation": "worker"},
]


salary = 0
myEmp = ""
for employee in employees:
    if employee["salary"] > salary:
        salary = employee["salary"]
        myEmp = employee
print(myEmp)
