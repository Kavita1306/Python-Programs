class Sumofnumbers:
   def negSum(self, list):

       neg_sum = 0

       for num in list:

           num = int(num)

           if(num < 0):

               neg_sum += num     
       print("Sum of negative numbers: ",neg_sum)              

   def posSum(self, list):

       pos_even_sum = 0

       pos_odd_sum = 0
       for num in list:

           num = int(num)

           if(num >= 0):

               if(num % 2 == 0):

                   pos_even_sum += num
               else:

                   pos_odd_sum += num

       print("Sum of even positive numbers is: ",
             pos_even_sum)

       print("Sum of odd positive numbers is: ",
             pos_odd_sum)


list_num = [-13, 50, 48, -97, 61]


obj = Sumofnumbers()

obj.negSum(list_num)

obj.posSum(list_num)
