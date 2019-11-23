#######Notes########
#Everything is an object in Python
#Python is a dynamically typed language
#Stack Mem - methods excuted here. Starts with main. Where references are created. Stack frames (usually within a function). Variables in different stack frames 
#do not overide vars in other stack frames. 
#Heap Mem - where objects and instances are created
#Dead Objects - objects with no refernces. Garbage Collector comes and removes object from memory. Alg used = Reference Counting (counts num of references). Java uses a mark-and-sweep alg. 

x = 10 
print(type(x))

#Both y and x point to the same object in memory
y = x
print(id(x))
print(id(y))

#x now points to a different object 11
x = x + 1
print(x, id(x))
print(y, id(y))

#x and y point to the same object now because Python optimizes memory utilization 
#by locating the same object reference to a new vvariable if object already exsists
#with the same value. 
y = y + 1
print(y, id(y))

z = 200 

#Return the hex mem location
print(hex(id(z)))
  
#Make reference counter go to zero
z = None