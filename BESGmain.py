import BESGtouradmin
import BESGtourbooking
import BESGdiscount
import BESGcancellation_penalty


def load_tours(): #defined each tour data for every section in BESGtouradmin
  tours = {}
  try:
      with open("tours.txt", "r") as file:
          for line in file:
              tour_data = line.strip().split(",")
              tour_code = tour_data[0]
              tour_details = {
                  "Tour Name": tour_data[1],
                  "Departure Date": tour_data[2],
                  "Days": int(tour_data[3]),
                  "Nights": int(tour_data[4]),
                  "Cost per pax": float(tour_data[5]),
                  "Capacity": int(tour_data[6]),
                  "Status": tour_data[7]
              }
              tours[tour_code] = tour_details
  except FileNotFoundError:
      print("Tours file not found. Creating new file...")
  return tours

def load_bookings(): #defined each booking data for every section in BESGtourbooking
  booking = {}
  try:
      with open("booking.txt", "r") as file:
          for line in file:
              booking_data = line.strip().split(",")
              booking_id = int(booking_data[0])
              booking_details = {
                  "Tour Code": booking_data[1],
                  "Passport Number": booking_data[2],
                  "Customer Name": booking_data[3],
                  "Age": int(booking_data[4]),
                  "Phone Number": int(booking_data[5])
              }
              booking[booking_id] = booking_details
  except FileNotFoundError:
      print("Bookings file not found. Creating new file...")
  return booking

def load_discount_scheme(): #defined each discount scheme data in BESGdiscount
    discount_scheme = {}
    with open("discount_scheme.txt", "r") as file:
        for line in file:
            group_size, discount_percentage = line.strip().split(",")
            discount_scheme[int(group_size)] = float(discount_percentage)
    return discount_scheme

def load_cancellation_penalties(): #defined each cancellation penalty data in BESGcancellation_penalty
    cancellation_penalties = {}
    with open("cancellation_penalties.txt", "r") as file:
        for line in file:
            penalty_type, penalty_amount = line.strip().split(",")
            cancellation_penalties[penalty_type] = float(penalty_amount)
    return cancellation_penalties

def main():
  while True:
     tours = load_tours()
     booking = load_bookings()
     discount_scheme = load_discount_scheme()
     cancellation_penalties = load_cancellation_penalties()
     print("\n^^^^ BESG ^^^^")
     print("1. Tour Admin")
     print("2. Tour Booking")
     print("3. Discount Schemes Setup")
     print("4. Cancellation Penalties Setup")
     print("0. Exit")

     option = input("Enter option: ")
     if option == "1":
       tour_admin(tours)
     elif option == "2":
       tour_booking(tours, booking)
     elif option == "3":
        discount_sub_menu(discount_scheme)
     elif option == "4":
            cancellation_sub_menu(cancellation_penalties)
     elif option == "0":
            print("Exiting...")
            break
     else:
            print("Invalid option, please try again.")

def tour_admin(tours):
   while True:
     print("<<<< Tour Admin >>>>")
     print("a. List Tours")
     print("b. Setup Tour")
     print("c. Update Tour")
     print("d. Delete Tour")
     print("m. Back to main menu")
     option2 = input("Enter option: ")
     if option2 == "a":
       BESGtouradmin.display_lists(tours)
     elif option2 == "b":
       BESGtouradmin.set_tour(tours)
     elif option2 == "c":
       BESGtouradmin.update_tour(tours)
     elif option2 == "d":
       BESGtouradmin.delete_tour(tours)
     elif option2 == "m":
       break
     else:
       print("Invalid option, please try again.")

def tour_booking(tours, booking):
   while True:
      print(">>>> Tour Booking <<<<")
      print("a. Create Booking")
      print("b. Cancel Booking")
      print("c. Search Booking")
      print("d. Booking Report")
      print("m. Back to main menu")
      option3 = input("Enter option: ")
      if option3 == "a":
        BESGtourbooking.create_booking(tours, booking)
      elif option3 == "b":
        BESGtourbooking.cancel_booking(tours, booking)
      elif option3 == "c":
        BESGtourbooking.search_booking()
      elif option3 == "d":
        BESGtourbooking.generate_booking_report(tours, booking)
      elif option3 == "m":
        break
      else:
         print("Invalid option, please try again.")

def discount_sub_menu(discount_scheme):
    while True:
        print("\n---- Discount Schemes ----")
        print("a. Add new line")
        print("b. Update line")
        print("c. Remove line")
        print("m. Back to main menu")
        option = input("Enter option: ")

        if option == "a":
            BESGdiscount.add_discount_scheme(discount_scheme)
        elif option == "b":
            BESGdiscount.update_discount_scheme(discount_scheme)
        elif option == "c":
            BESGdiscount.remove_discount_scheme(discount_scheme)
        elif option == "m":
            break
        else:
            print("Invalid option, please try again.")


def cancellation_sub_menu(cancellation_penalties):
    while True:
        print("\n---- Cancellation Penalties ----")
        print("a. Add new line")
        print("b. Update line")
        print("c. Remove line")
        print("m. Back to main menu")
        option = input("Enter option: ")

        if option == "a":
            BESGcancellation_penalty.add_cancellation_penalty(cancellation_penalties)
        elif option == "b":
            BESGcancellation_penalty.update_cancellation_penalty(cancellation_penalties)
        elif option == "c":
            BESGcancellation_penalty.remove_cancellation_penalty(cancellation_penalties)
        elif option == "m":
            break
        else:
            print("Invalid option, please try again.")

main()
