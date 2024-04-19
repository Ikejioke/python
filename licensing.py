def check_license_eligibility(age):
    if age >= 18:
        print("\nYou are eligible for a learner's permit.\n")
    elif age >= 16:
        print("\nYou are eligible for a learner's permit.\n")
    else:
        print("\nSorry, you are not eligible for a driver's license yet.\n")


age = int(input("\nPlease enter your age:"))

check_license_eligibility(age)