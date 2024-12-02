import json
x={"fruit":"apple",
   "car":"ferrari",
   "truck":"samsung"
}
y=json.dumps(x)
print(y)
print(type(y))

z=json.loads(y)
print(z)
print(type(z))