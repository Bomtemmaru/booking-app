def save_discount_scheme(discount_scheme):
    with open("discount_scheme.txt", "w") as file:
        for group_size, discount_percentage in discount_scheme.items():
            file.write(f"{group_size},{discount_percentage}\n")

def add_discount_scheme(discount_scheme):
    group_size = int(input("Enter the group size: "))
    discount_percentage = float(input("Enter the discount percentage: "))
    discount_scheme[group_size] = discount_percentage
    save_discount_scheme(discount_scheme)
    print("Discount Scheme Added Successfully")

def update_discount_scheme(discount_scheme):
    group_size = int(input("Enter the group size to update: "))
    if group_size in discount_scheme:
        discount_percentage = float(input("Enter the new discount percentage: "))
        discount_scheme[group_size] = discount_percentage
        save_discount_scheme(discount_scheme)
        print("Discount Scheme Updated Successfully")
    else:
        print("Discount Scheme not found")

def remove_discount_scheme(discount_scheme):
    group_size = int(input("Enter the group size to remove: "))
    if group_size in discount_scheme:
        del discount_scheme[group_size]
        save_discount_scheme(discount_scheme)
        print("Discount Scheme Removed Successfully")
    else:
        print("Discount Scheme not found")

def display_discount_scheme(discount_scheme):
    print("Current Discount Schemes:")
    for group_size, discount_percentage in discount_scheme.items():
        print(f"Group Size: {group_size}, Discount Percentage: {discount_percentage}")