from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class Student(BaseModel):
    name: str = 'faraz'  # setting here name default value 
    age: Optional[int] = None # optional value example
    email : EmailStr
    # cgpa : float = Field(gt=0, le=10) # We are using contraint here cgpa should be 0 to 10
    # cgpa : float = Field(gt=0, le=10, default=5) # We are using contraint here cgpa should be 0 to 10 and we can also give default value here
    cgpa : float = Field(gt=0, le=10, default=5, description='A decimal value representing CGPA') # we can also add description



# new_student = {'age' : 32} 
new_student = {'age' : '32'}  # here i gave wrong type but in output pydantic did coerce to correct int type and output of age shows 32
new_student = {'age' : '32', 'email' :'abc@gmail.com'} # Pydantic offers email validation if i dont give proper email it throws error
new_student = {'cgpa':1, 'email' :'abc@gmail.com'} # if i use cgpa more than 10 it will throw an error



student = Student(**new_student)

print(student)