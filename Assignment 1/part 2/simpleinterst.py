'''
Write a program to find the simple interest when the value of principle,
rate of interest and time period is provided by the user

'''
def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

# Taking input from the user with basic validation
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (in %): "))
time = float(input("Enter the time period (in years): "))

# Calculate simple interest
simple_interest = calculate_simple_interest(principal, rate, time)

# Display the results
print(f"\nSimple Interest: ${simple_interest:.2f}")
print(f"Principal: ${principal:.2f}, Rate: {rate:.2f}%, Time: {time:.2f} years")