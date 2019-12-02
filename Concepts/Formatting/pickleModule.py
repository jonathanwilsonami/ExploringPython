# Serialization - is the process of converting an object into a stream of bytes to store the object or transmit it to memory, 
#a database, or a file. Its main purpose - is to save the state of an object in order to be able to recreate it when needed. 
#The reverse process is called deserialization.

#Pickle module - is used for implementing binary protocols for serializing and de-serializing a Python object structure. 
#Also called: flattening, Marshalling. Stores Python objects. Can be anything such a var or list, etc. Makes reading in lots of 
#data a lot faster. 

#Use cases: Transfering large objects from one server to another or one storage to another. 

#Caveats: One is security risk. Need to make sure you know exactly what that objects is i.e. you could run code that you do not want to. 

import pickle as p

#Serialize
#my_dict = {1:"Frank", 2:"Wilson", 3:4, 4:"Sam"} 
#p_out = open("my_dict", "wb")#wb for reading bytes
#pickle.dump(my_dict, p_out)#Dumps my_dict as computer readable
#p_out.close()

#Deserialize
p_in = open("dict.pickle", "rb")
my_dict_returned = p.load(p_in)
print(my_dict_returned)
print(my_dict_returned[2])
