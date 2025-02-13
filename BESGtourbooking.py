from datetime import datetime

def age_caluculate(dob):
    today = datetime.now()
    return (int(today.strftime("%Y%m%d")) - int(dob)) // 10000

def create_booking(tours, booking):
  print("List of Open Tours:")
  print("^^^^^^^^^^^^^^^^^^^")
  with open("tours.txt", "r") as file:
    file_tours = file.readlines()
    print("{:<20s}{:<36s}{:<22s}{:<18s}{:<20s}{:<20s}{:<20s}{:<20s}".format("Tour Code", "Tour Name", "Departure Date", "Days", "Nights", "Cost per pax", "Capacity", "Status")) #print head of detail
    for tour in file_tours:
      tour_details = tour.split(',') #split the line into a list of strings, where each string is a field in the tours file
      if len(tour_details) == 8:
        print("{:<18s}{:<36s}{:<22s}{:<18s}{:<20s}{:<20s}{:<20s}{:<20s}".format(*tour_details))  #display each tour details
  choice = input("Group booking or Individual booking? (G/I): ")

  if choice.upper() == "G":
    group_travellers = []
    member = int(input("Enter the number of members in the group: "))
    tour_code = input("Enter your Tour Code: ")
    for i in range(member):
      passport_number = input("Enter Passport Number: ")
      name = input("Enter Name: ")
      dob = input("Enter DoB (YYYYMMDD): ")
      contact = input("Enter Contact: ")
      booking_id = len(booking) + 1001
      age = age_caluculate(dob)
      group_travellers.append(booking_id)
      group_travellers.append(tour_code)
      group_travellers.append(passport_number)
      group_travellers.append(name)
      group_travellers.append(age)
      group_travellers.append(contact)

    print("Group Booking Details:")
    print("Booking ID: {}\nTour Code: {}".format(group_travellers[0], group_travellers[1]))
    for key, value in tours[tour_code].items():
      print(f"{key}: {value}")
    print("\nMember Details:")
    print("{:<17}{:<17}{:<17}{:<17}".format("Passport Number", "Name", "Age", "Contact"))
    print("-"*60)
    for i in range(0, len(group_travellers), 6):
      with open("booking.txt", "a") as file:
        file.write("{}, {}, {}, {}, {}, {}\n".format(group_travellers[i+0], group_travellers[i+1], group_travellers[i+2], group_travellers[i+3], group_travellers[i+4], group_travellers[i+5]))
      print("{:<17}{:<17}{:<17}{:<17}".format(group_travellers[i+2], group_travellers[i+3], group_travellers[i+4], group_travellers[i+5]))
    print("Booking confirmed.")

  elif choice.upper() == "I":
    tour_code = input("Enter your Tour Code: ")
    passport_number = input("Enter Passport Number: ")
    name = input("Enter Name: ")
    dob = input("Enter DoB (YYYYMMDD): ")
    contact = input("Enter Contact: ")
    booking_id = len(booking) + 1001
    age = age_caluculate(dob)

    with open("booking.txt", "a") as file2:
      file2.write("{}, {}, {}, {}, {}, {}" "\n".format(booking_id, tour_code, passport_number, name, age, contact))

    print("Individual booking is added. See confirmation below:")
    print(booking_id)
    #available_seat = tours[tour_code]["Capacity"] - counts
    for key, value in tours[tour_code].items():
      print(f"{key}: {value}")
      
    print("{:<17s}{:<17s}{:<17s}{:<17s}".format("Passport Number", "Name", "Age", "Contact"))
    print("-"*60)
    print("{:<17}{:<17}{:<17}{:<17}".format(passport_number, name, age, contact))
  else:
    return


def penalty_calculate(booking_id, tours, tour_code):
  tour_details = tours[tour_code]
  current_date = datetime.now()

  # Extract departure date and time from the tour details
  departure_date_str = tour_details["Departure Date"].strip()
  print("Departure date:", departure_date_str)
  departure_date = datetime.strptime(departure_date_str, '%d-%b-%Y %H:%M')
  days_before_departure = (departure_date - current_date).days
  print("days_before_departure:", days_before_departure, "days")


  if days_before_departure <= 0:
      return "This tour has already departed and cannot be cancelled."
  elif days_before_departure <= 7:
      penalty = 0.9 * int(tour_details["Cost per pax"])
  elif days_before_departure <= 21:
      penalty = 0.6 * int(tour_details["Cost per pax"])
  elif days_before_departure <= 45:
      penalty = 0.3 * int(tour_details["Cost per pax"])
  else:
      return "Cancellation is free more than 45 days before departure."

  return f"The cancellation penalty for booking {booking_id} is {penalty}$."



def cancel_booking(tours, booking):
   booking_id = int(input("Enter Booking ID: "))
   tour_code = input("Enter Tour Code: ")
   if booking is None:
     return "No booking found matching the provided booking ID."
   with open('booking.txt', 'r') as file:
     lines = file.readlines()
   modified_lines = [line for line in lines if not line.startswith(str(booking_id))]
   
   
   penalty = penalty_calculate(booking_id, tours, tour_code)
   confirm = input("Are you sure you want to cancel this booking? (Y/N): ").upper()
   with open("booking.txt", "w") as file:
      if confirm == "Y":
        file.writelines(modified_lines)
        print("Tour cancelled")
        print("Penalty for cancelling:", penalty)
      elif confirm == "N":
        print("Booking not canceled")
        return
 


def search_booking():
  tour_code=input("Enter your tour code: ")
  booking_id=int(input("Enter Booking ID: "))
  print(booking_id)
  with open("tours.txt", "r") as file:
    for line in file:
      components = line.split(',')
      tourcode = components[0]
      if tour_code == tourcode:
        tour_name = components[1]
        departure = components[2]
        capacity = components[6]
        status = components[7]
        print(f"Tour Code: {tour_code}")
        print(f"Name: {tour_name}")
        print(f"Departure: {departure}")
        print(f"Capacity: {capacity}")
        print(f"Status: {status}")

  print("{:<17}{:<18}{:<17}{:<17}".format("passport_number","name","age","contact"))
  print("-"*60)
  with open('booking.txt', 'r') as file:
    for line in file:
      components = line.split(',')
      bookingid = components[0]
      if str(booking_id) == bookingid:
        passport_number = components[2]
        name = components[3]
        age = components[4]
        contact = components[5]
        print("{:<17}{:<17}{:<17}{:<17}".format(passport_number,name,age,contact))


def generate_booking_report(tours, booking):
    tour_codes = input("Enter the tour code (separated by commas)").strip().split(",")
    print("Tour codes entered:", tour_codes)  # Print debug information
    for tour_code in tour_codes:
        tour_code = tour_code.strip()
        print("Checking tour code:", tour_code)  # Print debug information
        if tour_code in tours:
            tour_details = tours[tour_code]
            print("\nTour_Name:", tour_details["Tour Name"])
            print("Tour Code:", tour_code)
            print("Departure Date:", tour_details["Departure Date"])
            print("Capacity:", tour_details["Capacity"])
            print("Status:", tour_details["Status"])
            print("{:<9}{:<15}{:<20}{:<5}{:<12}".format("Booking ID", "Passport", "Name", "Age", "Phone"))
            print("-" * 60)
            for booking_id, booking_details in booking.items():
                if tour_code == booking_details['Tour Code'].strip():
                    print("{:<7}{:<15}{:<20}{:<5}{:<12}".format(
                        booking_id, booking_details['Passport Number'],
                        booking_details['Customer Name'], booking_details['Age'],
                        booking_details['Phone Number']
                    ))
            print("-" * 60)
        else:
            print(f"No tour found with code {tour_code}")

