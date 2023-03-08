#if the citizen's income was not higher than 85,528 thalers, the tax was equal to 18% of the income minus 556 thalers and 2 cents (this was what they called tax relief)
#if the income was higher than this amount, the tax was equal to 14,839 thalers and 2 cents, plus 32% of the surplus over 85,528 thalers.
#It should accept one floating-point value: the income.
#Next, it should print the calculated tax, rounded to full thalers. There's a function named round() which will do the rounding for you – you'll find it in the skeleton code in the editor.

income = float(input("Enter the annual income: "))

if int(income) < 85528:
	tax = income * 0.18 - 556.02
else:
    tax = 14839.02 + 0.32(income - 85528)
# Write the rest of your code here.

tax = round(tax, 0)
print("The tax is:", tax, "thalers")
