## Functions in Python

def create_fullname():
    First_name = "Aldair"
    Last_name = "Chan"
    Full_name= First_name+" "+Last_name
    print(Full_name)


create_fullname()


def create_name_ren():
    First_name= "Joel"
    Last_name= "Chan"
    Full_name= First_name+" "+Last_name
    return Full_name

print(create_name_ren())


def create_name_param(First_name,Last_name):
    Full_name= First_name+" "+Last_name
    return Full_name

print(create_name_param("Tefy", "Chac"))