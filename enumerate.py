# # Python enumerate() Function

# # enumerate(iterable, start=0)
# # Parameters:
# # Iterable: any object that supports iteration
# # Start: the index value from which the counter is 
# #               to be started, by default it is 0

# l1 = [1,2,3,4,5]
# s1 = "geek"
# obj1 = enumerate(l1)
# obj2 = enumerate(s1)
# k= list(obj1)
 
# print ("Return type:",type(obj1))
# print (k[0][1])  #eat
 
# # changing start index to 2 from 0
# print (list(obj2))


class Solution(object):
    def twoSum(self, nums, target):
        obj ={}
        
        for index,number in enumerate(nums) :
            remainder = target-number
            if (remainder in obj) :
                return [obj[remainder],index]
            
            obj[number] = index

# How enumerate() Works
# The enumerate() function returns an enumerate object, which is an iterator. As each element is accessed 
# from this enumerate object, a tuple is returned, containing the index and element at that index: (index, element).
# Thus, in the above for loop, with each iteration, it is assigning the elements of this returned tuple to the 
# index and element variables. In other words, the returned tuple is being unpacked inside the for-statement:

# for index, element in enumerate(num_list):
# # similar to:
# index, element = (index, element)

name_list = ['Jane', 'John', 'Mike']
print(list(enumerate(name_list,2))) #[(2, 'Jane'), (3, 'John'), (4, 'Mike')]
