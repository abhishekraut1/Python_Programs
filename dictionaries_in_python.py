thisdict = {
            "brand": "Ford",
            "model": "Mustang",
            "year": 1964 }
print(thisdict)
x = thisdict["model"]
x = thisdict.get("model")
thisdict["year"] = 2018
print(thisdict)
for x in thisdict:
    print(x)
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")
print(len(thisdict))
thisdict["color"] = "red"
print(thisdict)
mydict = thisdict.copy()
print(mydict)
cars = {
"AUDI" : {
            "name": "Audi R8",
            "no" : 2007
            },

"BMW" : {
            "name": "BMW 328",
            "year" : 2007
            },
            
"FERRARI" :  {
           "name": "Ferrari 275",
           "year" : 1964
           }
           }
print (cars)