x={
    "fruit":"apple",
    "car":"ford",
    "cycle":"bi"
}
print(x)
x["student"]="boy"
print(x)

print(x.items())

if "ccle" in x:
    print("Yes")
else:
    print("No")


x.update({"cycle":"di"})
print(x)