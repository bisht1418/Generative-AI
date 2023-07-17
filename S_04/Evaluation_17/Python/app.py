# Palindrome or not

def CheckPalindrome(num):
    strNum = str(num)
    ansStr = ""
    for i in range(0, len(strNum)):
        ansStr = strNum[i] + ansStr
    return strNum == ansStr


num = 101

if (CheckPalindrome(num)):
    print("Yes Number is Palindrome")
else:
    print("Number is not palindrome")

# ================================================================
company = {
    'employees': {
        'John': {'age': 35, 'job_title': 'Manager'},
        'Emma': {'age': 28, 'job_title': 'Software Engineer'},
        'Kelly': {'age': 41, 'job_title': 'Senior Developer'},
        'Sam': {'age': 30, 'job_title': 'Software Engineer'},
        'Mark': {'age': 37, 'job_title': 'Senior Manager'},
        'Sara': {'age': 32, 'job_title': 'Software Engineer'},
    }
}


# Find the average age. also conside the employee whose job tiitle start from the S

sum = 0
count = 0
for key in company["employees"]:
    jobTitle = company["employees"][key]["job_title"]
    if (jobTitle[0] == "S"):
        sum += company["employees"][key]["age"]
        count += 1

if (count):
    print(sum/count)
else:
    print(0)
