array1 = ["pakistan", 29, "islamabad", 34, "USA", "Software house", 23]

arr1 = len(array1)

print(arr1)

num = []
str1 = []

# Print the array of value 
for x in array1:
    if isinstance(x , int):
        num.append(x)
        
    elif isinstance(x , str):
            str1.append(x)
                       
print("These are integer values ", num)
print("These are string values ",str1)
    
          
# Print the index of value         
# for i in range(arr1):
#     print(i)
#     if isinstance(i, int):
#         print(i)