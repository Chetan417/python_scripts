# 1 task
# this task is dict to input the name and show the mark.....

Dict = {
    "kishan" : 95,
    "vijay" : 85,
    "gopal" : 79,
    "rahul" : 63,
    "lalji" : 98,
}
def student_mark_show(Dict):
    student_name = input("Student name: ").lower()

    if student_name in Dict:
        print(f"{student_name}'s marks is : {Dict[student_name]}")

    else:
        print(f"{student_name} is not found...")

student_mark_show(Dict)

# ....................................................................................................................
# 2 task
print("*" * 80)
print("Task 2")
print("*" * 20)
#  print original list
list = [1,2,3,4,5,6,7,8,9,10]
print(f" this is the  original {list}")


#  print first five number
five_element = list[:5]
print(f" this is the first five element :  {five_element}")

# print first five number reversed
Reverse = five_element[::-1]
print(f" This is the reversed element : {Reverse}")
