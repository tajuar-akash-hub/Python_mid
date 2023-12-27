class Star_cinema:
    hall_list=[]

    @classmethod
    def Entry_hall(cls,hall):
        cls.hall_list.append(hall)
        

class Hall(Star_cinema):

    def __init__(self,rows,cols,hall_no):
        super().__init__()

        self.__seats={}
        self.show_list=[]
        self.__rows=rows
        self.__cols=cols
        self.hall_no=hall_no
        self.emptying_hall()
        Star_cinema.Entry_hall(self)  

    def entry_show(self,id,movie_name,time):
            seats=[]
            show_info=(id,movie_name,time)
            self.show_list.append(show_info)

            for row in range(1,self.__rows+1):
                 seats.append([0]*self.__cols)
          

            self.__seats[id]=seats
    

    def emptying_hall(self):
        for row in range(1,self.__rows+1):
             self.__seats[row]=[0]*self.__cols
    
    def book_seats(self,id,seat_list):
         
         seats=self.__seats[id]
         for row, col in seat_list:
            if 1 <= row <= self.__rows and 1 <= col <= self.__cols and seats[row - 1][col - 1] != 1:
                seats[row - 1][col - 1] = 1
            else:
                print(f"Error: Wrong seat ({row}, {col}) for show {id}")



         self.__seats[id][seat_col-1][seat_row-1]=1
         print("showing available seats now")
         for show_seats in self.__seats[id]:
          print(show_seats)

    def view_available_seats(self,show_ID):
          if show_ID not in self.__seats:
            print(f"Your id {show_ID} is wrong")
            return 
          
          print("showing available seats")
          for i in self.__seats[show_ID]:
              print(i)
     
    def view_show_list(self):
     print(f"Shows in Hall {self.hall_no}:")
     # for show in self.show_list:
     #      print(show)
     return self.show_list
        
Modhumoti_hall=Hall(4,4,100)
Modhumoti_hall.entry_show(500,"My name is Akash","12/12/12")
Modhumoti_hall.entry_show(600,"jibonta bedonar","12/12/12")
Modhumoti_hall.entry_show(700,"Tunnel","12/12/12")

Bashundhara_hall=Hall(4,4,200)
Bashundhara_hall.entry_show(100,"Ki anondo akashe batashe","12/12/12")

Jamuna_hall=Hall(4,4,300)

while True:
     print("welcome to our cinema Hall")
     print("1 : Show all running Show")
     print("2 : View Available Seats")
     print("3 : Book seats")
     print("4.  Exit")

     choice = int(input("Enter your choice "))

     if(choice==1):
          for hall in Star_cinema.hall_list:
            for list in hall.view_show_list():
                print(list)

     elif (choice==2):
          IdInput=int(input('Enter show id '))
          check=False
          measurement=1
          

          for hall in Star_cinema.hall_list:
              for shows in hall.show_list:
                  if IdInput in shows:
                      hall.view_available_seats(IdInput)
                      check=True
                      
                      
                  else :
                      if(check!=True and measurement<2):
                          measurement+=1
                          print("Sorry wrong id of the show")
                          break
                          
                  

     elif (choice==3):
          show_id=int(input("Enter show id : "))

        
          for hall in Star_cinema.hall_list:
              for shows in hall.view_show_list():
                  if(show_id==shows[0]):
                      numberOfTickets=int(input('Enter number of tickets? '))
                      if numberOfTickets <= 0:
                        print("Invalid tickets.")
                        break
                      seat_list=[]
                      for _ in range(numberOfTickets):
                        seat_row = int(input(f"Enter Seat Row: "))
                        seat_col = int(input(f"Enter Seat Col: "))
                        seat_list.append((seat_row, seat_col))

                      hall.book_seats(show_id, seat_list)  
          
     elif(choice==4):
          print("Thanks for visiting us :) ")
          break
          







   










