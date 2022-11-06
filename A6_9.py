# Write a python script to check 
# whether a given year is a leap year or not.


"""t="ly" if i%400==0 else "ly" if i%4==0 and i%100!=0 else "nly"
print(t
"""
print("Enter a year number:")
year=int (input())
if year % 400==0 or year  % 100!=0 and year % 4==0  :
    print("leap year")
else:
    print("not leap year")    