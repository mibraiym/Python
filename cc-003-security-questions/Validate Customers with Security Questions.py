from datetime import datetime

first_names = ["Brad", "John", "Sam"]
last_names = ["Pitt", "Snow", "Smith"]

invalid_name = "You are not a customer!"
invalid_date = "You have entered an incorrect value!"
valid_customer = "You are a customer!"

days = [10, 15, 20]
months = [5, 6, 7]
years = [1970, 1980, 1990]

list1 = []
list2 = []

for i in range(0, len(days)):
  list1.append([months[i], days[i], years[i]])
#print(list1)
# list of int lists: [[5, 10, 1970], [6, 15, 1980], [7, 20, 1990]]

for inn_list in list1:
    date_str = "/".join([str(item) for item in inn_list])
    list2.append(datetime.strptime(date_str, "%m/%d/%Y").strftime("%m/%d/%Y"))
#print(list2)
#list of dates: ['05/10/1970', '06/15/1980', '07/20/1990']

if input("Please Enter your first name: ") in first_names :
    if input("Please enter your last name: ") in last_names :  
       if input("Please enter your birthday (MM/DD/YYYY): ") in list2:
         print(valid_customer)
       else:
        print(invalid_date)
    else:
     print(invalid_name)
else:
    print(invalid_name)
    
