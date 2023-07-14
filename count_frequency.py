def CountFrequency(my_list):
    freq = {}
    for item in my_list:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
 
    for key, value in freq.items():
        print ("% d : % d"%(key, value))
 
# Driver function
if __name__ == "__main__":
    my_list =[7,4,6,7,3,9,2,1,4,6,9,2,3,5]
    print("The frequency of each element in a list are as follows: ")
    CountFrequency(my_list)

  
    
