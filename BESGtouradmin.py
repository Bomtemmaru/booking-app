def display_lists(tours):
  print("Existing list:")
  with open("tours.txt", "r") as file:
    file_tours = file.readlines()
    print("{:<20s}{:<36s}{:<22s}{:<18s}{:<20s}{:<20s}{:<20s}{:<20s}".format("Tour Code", "Tour Name", "Departure Date", "Days", "Nights", "Cost per pax", "Capacity", "Status")) #print head of detail
    for tour in file_tours:
      tour_details = tour.split(',') #split the line into a list of strings, where each string is a field in the tours file
      if len(tour_details) == 8:
        print("{:<18s}{:<36s}{:<22s}{:<18s}{:<20s}{:<20s}{:<20s}{:<20s}".format(*tour_details))  #display each tour details


def set_tour(tours):
    tour_code = input("Enter the Tour Code (XXX-YYMMDD): ")
    tour_name = input("Enter the Tour Name: ")
    departure = input("Enter the Departure Date (DD-MM-YYYY HH:MM): ")
    days = int(input("Enter the number of Days: "))
    nights = int(input("Enter the number of Nights: "))
    cost_per_pax = float(input("Enter the Cost per pax: "))
    capacity = int(input("Enter the Capacity: "))
    status = "Open"

    if abs(days - nights) != 1:
        print("Error: There should be a difference of 1 between days and nights.")
        return


    with open("tours.txt", "a") as file:
        file.write("{}, {}, {}, {}, {}, {}, {}, {}" "\n".format(tour_code, tour_name, departure, days, nights, cost_per_pax, capacity, status))

    print("New tour added successfully!")
    print("Existing list:")
    with open("tours.txt", "r") as file:
      file_tours = file.readlines()
      print("{:<20s}{:<36s}{:<22s}{:<18s}{:<20s}{:<20s}{:<20s}{:<20s}".format("Tour Code", "Tour Name", "Departure Date", "Days", "Nights", "Cost per pax", "Capacity", "Status")) #pr t head of detail
      for tour in file_tours:
        tour_details = tour.split(',') #split the line into a list of strings, where each string is a field in the tours file
        if len(tour_details) == 8:
          print("{:<18s}{:<36s}{:<22s}{:<18s}{:<20s}{:<20s}{:<20s}{:<20s}".format(*tour_details))  #display each tour details

    choice = input("Do you want to add another tour? (Y/N): ")
    if choice.upper() == "Y":
      return set_tour(tours)
    elif choice.upper() == "N":
      return
    else:
      print("Invalid choice. Please enter Y or N.")
      return

def save_tours(tours):
  with open("tours.txt", "w") as file:
      for tour_code, tour_details in tours.items():
          file.write(f"{tour_code},{tour_details['Tour Name']},{tour_details['Departure Date']},{tour_details['Days']},{tour_details['Nights']},{tour_details['Cost per pax']},{tour_details['Capacity']},{tour_details['Status']}\n") #,{tour_details['Seats Booked']}

def count(tours, tour_code):
  count = 0
  for target in tours:
    if target == tour_code:
      count += 1
  return count

def update_tour(tours):
  tour_code = input("Enter your Tour Code: ").upper()
  if tour_code not in tours:
    print("Tour Code not found")
    return
  count(tours, tour_code)

  print("Tour Detail")
  for key, value in tours[tour_code].items():
    print(f"{key}: {value}")

  while True:
    field = input("Enter the section to update (or 'done' to finish): ").strip().title()

    if field == "Done":
      break
    elif field not in tours[tour_code]:
      print("Invalid field. Please enter a valid field.")
      continue

    new_value = input(f"Enter the new value for {field}: ").strip()

    tours[tour_code][field] = new_value
    print(f"{field} updated to {new_value}")

  save_tours(tours)

def delete_tour(tours):
      tour_code = input("Enter your Tour Code: ").upper()

      for key, value in tours[tour_code].items():
        print(f"{key}: {value}")
      with open('tours.txt', 'r') as file:
        lines = file.readlines()
      modified_lines = [line for line in lines if not line.startswith(tour_code)]
      confirm = input("Are you sure you want to delete this tour? (Y/N): ").upper()
      with open("tours.txt", "w") as file:
         if confirm == "Y":
           file.writelines(modified_lines)
           print("Tour deleted successfully!")
         elif confirm == "N":
           print("Tour not deleted")
           return