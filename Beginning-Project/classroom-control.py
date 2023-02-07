a_class=["Luna", "Lina"]
b_class=["Jake", "Chris"]
name=input("Enter game")
if name in a_class:
    print("The person is in class A")
elif name in b_class:
    print("The person is in class B")
else:
    print("The person is not in the classrooms")