import sys
class Library:
      def __init__(self,listofbooks):
            self.availablebooks=listofbooks

      def displayAvailablebooks(self):
                   print("The books we have available in our NORTH CAMPUS are as follows:")
                   for book in self.availablebooks:
                         print(book)
      def lendBook(self,requestedBook):
            if requestedBook in self.availablebooks:
                  print("The book that you requested is available")
                  self.availablebooks.remove(requestedBook)
            else:
                  print("Sorry, the book that you have requested is currently not in the library")
                  
      def addBook(self,returnedBook):
            self.availablebooks.append(returnedBook)
            print("Thanks for returning the book.")
            
class Student:
      def requestBook(self):
            print("Enter the name of the book you'd like to borrow")
            self.book=input()
            return self.book

      def returnBook(self):
            print("Enter the name of the book you'd like to return")
            self.book=input()
            return self.book
def main():            
      library=Library(["Mock Papers 2020","UI/UX Design","Advanced Computer Networks"])
      student=Student()
      done=False
      while done==False:
            print(""" ##### LIBRARY MENU #####
                  1. Display all available books
                  2. Request a book
                  3. Return a book
                  4. Exit
                  """)
            choice=int(input("Enter Choice:"))
            if choice==1:
                        library.displayAvailablebooks()
            elif choice==2:
                        library.lendBook(student.requestBook())
            elif choice==3:
                        library.addBook(student.returnBook())
            elif choice==4:
                  sys.exit()                 
main()
