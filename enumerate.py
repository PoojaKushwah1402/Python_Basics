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