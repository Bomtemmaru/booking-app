def save_cancellation_penalties(cancellation_penalties):
    with open("cancellation_penalties.txt", "w") as file:
        for penalty_type, penalty_amount in cancellation_penalties.items():
            file.write(f"{penalty_type},{penalty_amount}\n")

def add_cancellation_penalty(cancellation_penalties):
    penalty_type = input("Enter the penalty type: ")
    penalty_amount = float(input("Enter the penalty amount: "))
    cancellation_penalties[penalty_type] = penalty_amount
    save_cancellation_penalties(cancellation_penalties)
    print("Cancellation Penalty Added Successfully")

def update_cancellation_penalty(cancellation_penalties):
    penalty_type = input("Enter the penalty type to update: ")
    if penalty_type in cancellation_penalties:
        penalty_amount = float(input("Enter the new penalty amount: "))
        cancellation_penalties[penalty_type] = penalty_amount
        save_cancellation_penalties(cancellation_penalties)
        print("Cancellation Penalty Updated Successfully")
    else:
        print("Cancellation Penalty not found")

def remove_cancellation_penalty(cancellation_penalties):
    penalty_type = input("Enter the penalty type to remove: ")
    if penalty_type in cancellation_penalties:
        del cancellation_penalties[penalty_type]
        save_cancellation_penalties(cancellation_penalties)
        print("Cancellation Penalty Removed Successfully")
    else:
        print("Cancellation Penalty not found")

def display_cancellation_penalties(cancellation_penalties):
    print("Current Cancellation Penalties:")
    for penalty_type, penalty_amount in cancellation_penalties.items():
        print(f"Penalty Type: {penalty_type}, Penalty Amount: {penalty_amount}")