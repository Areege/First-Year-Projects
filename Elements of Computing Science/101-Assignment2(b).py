#Code developed by Areege Chaudhary (10197607): October 26, 2015

#prompt the user to input the values for the principal, the length of the term and the annual interest rate
principal=int(input('What is the total amount of money borrowed? (enter numerical digits only)'))
term_year=int(input('How many years will it take to repay? (enter numerical digits only)'))
rate_year=int(input('What is the annual interest rate? (enter an integer percentage value)'))
#calculate the value of the term entered in years to months by multiplying it by 12
term_month=term_year*12
#calculate the decimal value of the percentage entered by the user by dividing the value by 100
rate_month_decimal=rate_year/100
#calculate the monthly interest rate by dividing the annual interest rate by 12
rate_month=rate_month_decimal/12
#calculate the monthly payment using the monthly mortgage payment formula
payment=((principal*rate_month)/(1-(1+rate_month)**-term_month))
#calculate the total amount of interest paid
interest_paid=(payment*term_month)-principal
#output the results to the user
print('The monthly payment is','$'+format(payment, '.2f'), 'and the total interest paid over the term is', '$'+format(interest_paid, '.2f')+'.')

              
