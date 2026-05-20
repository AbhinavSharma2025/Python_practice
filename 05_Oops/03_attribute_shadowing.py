class chai:
    temprature ="hot"
    strength="strong"

cutting=chai()
print(cutting.temprature)
cutting.temprature="mild" 
cutting.cup="small"
print("After changing ",cutting.temprature)
print("Cup size is ",cutting.cup)
print("direct look into class ", chai.temprature)

#if we delete the object's value then it will fallback or shadow the class attribute
del cutting.temprature
#it will give error as there is no cup object in class chai so delteing it removes it and printing it gives error
del cutting.cup
print(cutting.temprature)
print(cutting.cup )