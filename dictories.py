from operator import truediv

person={"name":"sumit","age":21}
print(person)
print(type(person))
print(person.get("name"))
print(person.get("value"))
print(person.get("value","not fount"))
person["value"] = "satna"
print(person)
customers = {
    "coo1":{
        "name":"sumit","email":"gupta@gmail.com"
    }
}
print(person["age"])
name = "aman jiya ashish archana"
family_name ={}
count=1
age = count
for word in name.split():
            if word in family_name:
                family_name[word] += 1
            else:
                family_name[word] = age
print(family_name)
print(family_name.get(word))
from collections import Counter
family_name = Counter(name.split())
print(family_name)

def fib(n,memo={}):
    if n in memo:
        return memo[n]
    if n<= 1 :
        return n
    memo[n] = fib(n-1,memo) + fib(n-2,memo)
    return memo[n]
print(fib(4))
app_setting={
    "difference":True,
   "database":{
       "host":"127.0.0.1"
   }
}
if app_setting["difference"]:
    print(app_setting["database"]["host"])
del person["name"]
print(person)
for data in person.keys():
    print(data)
for datas in person.values():
    print(datas)
if (age is person.keys()):
     print(True)
else:
    print(False)
person1 ={"age":21,"value":"satna"}
if(person1 is person.keys()):
    print(True)
else:
    print(False)
print(person is person1)
a =[1 ,3 ,2]
b = a
c =a
print(a is b )
print(b is c)
print(a is c)
#switch work in python
def switch_work(w):
    match w:
        case 1:
            print("monday")
        case 2:
            print("tuesday")
        case 3:
            print("wednesday")
        case 4:
            print("thursday")
        case 5:
            print("friday")
        case 6:
            print("Stareday")
        case 7:
            print("Sunday")

switch_work(3)