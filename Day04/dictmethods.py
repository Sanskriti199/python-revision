info={
    "name":"apnacollege",
    "subjects":["python","C","java"],
    "topics":("dict","set"),
    "age":35,
    "is_adult":True,
    12.99:94.4
}

print(info.keys())
#type casting

print(list(info.keys()))

print(info.values())

print(info.items())

print(info.get("age"))

info.update({
    "city":"delhi"
})
print(info)