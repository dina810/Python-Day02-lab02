my_dict={
    "name":"dina",
    "age":27,
    "address":{
        "street":1,
        "city"  :"mans"
  }
} 
my_dict["name"]
my_dict["address"]["city"]="sss"
my_dict["track"]="python"
print(my_dict) 

for key in my_dict.keys():
#for key in my_dict.items():
    #print(f"{key} => {value}")
    print(my_dict[key])
#if "name" in my_dict.values():
#print(my_dict.get("myname"))