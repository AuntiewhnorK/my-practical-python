"""
Practical Python 1.7 - Calculating Mortgage
Auntiewhnor Kpolie
04/27/2022

Dave has decided to take out a 30-year fixed rate mortgage of $500,000
with Guido's Mortgage, Stock Investment, and Bitcoin trading corporation.
The interest rate is 5% and the monthly payment is $2684.11.

Calculates the total amount that Dave
will have to pay over the life of the mortgage.
"""

# I have added inputs for better user experience.
print(
    """\nWelcome to Total Mortgage Calculator!
    This calculator gives you the total amount Dave (or you) will pay
    over the life of a mortgage.

    You will need:
    Loan Amount, Interest Rate (as decimal), and monthly payment amount.
    All other questions are optional (you can use 0 for them)."""
)

user = input("\nPlease enter (C)alculate Mortgage or (Q)uit: ").lower()

if user == "c":
    # 1.7 Exercise
    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter annual interest rate: "))
    payment = float(input("Enter monthly payment: "))
    total_paid = 0.0

    # 1.8 Exercise - Extra Payments
    month = 0
    extra_payment = float(input("Enter extra payment: "))

    # 1.9 Extra Payment Calculator

    year_start = int(input("How many years have already been paid? "))
    year_end = int(
        input(
            "How many years should extra payments last?"
            " (if nothing has been paid,\n"
            "simulator starts with extra payment) "
        )
    )
    extra_pay_start_month = (year_start * 12) + 1
    extra_pay_end_month = (year_start + year_end) * 12

    while principal > 0:
        month += 1
        # principal decreases
        principal = principal * (1 + rate / 12) - payment
        total_paid = total_paid + payment

        if month >= extra_pay_start_month and month <= extra_pay_end_month:
            principal = principal - extra_payment
            total_paid = total_paid + extra_payment

        # Correct overpayment
        if principal < 0:
            principal = 0
        print(month, round(total_paid, 2), round(principal, 2))

    print(f"Total paid: ${round(total_paid, 2):,}")
    print(f"Months: {month}")

else:
    print("Thank you for using.")
