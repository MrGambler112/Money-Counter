#Tkinter Library
import tkinter

#Name and description
print ("This program is called The Change Maker")

print ("\nThis program calculates the minimum number of coins and bills in order to\n"
       "efficiently and effectively sort the amount of physical currency required\n"
       "to fulfill the user defined amount of pennies (up to 10,000)")

#Application inquiring about the amount of pennies
amount_of_pennies = int(input("\nWhat is the amount of pennies? (up to 10,000 pennies): "))

#Coins/Bills and their values in pennies
nickel = 5
quarter = 25
loonie = 100
five_dollar_bill = 500
twenty_dollar_bill = 2000

#Calculations
twenties = amount_of_pennies // twenty_dollar_bill
remaining_pennies = amount_of_pennies % twenty_dollar_bill

fives = remaining_pennies // five_dollar_bill
remaining_pennies %= five_dollar_bill

loonies = remaining_pennies // loonie
remaining_pennies %= loonie

quarters = remaining_pennies // quarter
remaining_pennies %= quarter

nickels = remaining_pennies // nickel
remaining_pennies %= nickel

remainder = remaining_pennies / 100


#Monetary Denominations
twenty_value = twenties * 20
five_value = fives * 5
loonie_value = loonies * 1
quarter_value = round(quarters * 0.25, 2)
nickels_value = round(nickels * 0.05, 2)


total = (twenty_value + five_value + loonie_value + quarter_value + nickels_value)

#Final execution
print("\nNumber of pennies initially entered:", amount_of_pennies)

print ("\ntwenty dollar bills:", twenties, "Value:" " $", twenty_value)

print ("\nfive dollar bills:", fives, "Value:" " $", five_value)

print ("\nloonies:", loonies, "Value:" " $", loonie_value)

print ("\nquarters", quarters, "Value:" " $", quarter_value)

print ("\nnickels:", nickels, "Value:" " $", nickels_value)

print ("\nOverall value of the currency is:" " $", total)

print ("\nThe amount of remaining pennies are:" " $", remainder)

#Window dimensions
window = tkinter.Tk()
window.title("Money Counter")
window.geometry("800x800")

#Canvas dimensions (Canvas Create)
canvas = tkinter.Canvas(window, width = 800, height = 800, background = "black")
canvas.pack()

#Graphic Title Text
canvas.create_text(400, 16, text = "The Change Maker", fill = "white", font = ('Arial 15 bold'))

#Box Around Title
canvas.create_rectangle(240, 0, 560, 32, outline = "white", width = "3")

                            #First Row
#fifth box
canvas.create_rectangle(560, 640, 680, 520, outline = "white", width = "3")
#fourth box
canvas.create_rectangle(560, 520, 680, 400, outline = "white", width = "3")
#third box
canvas.create_rectangle(560, 400, 680, 280, outline = "white", width = "3")
#second box
canvas.create_rectangle(560, 280, 680, 160, outline = "white", width = "3")
#first box
canvas.create_rectangle(560, 160, 680, 40, outline = "white", width = "3")

                            #Second Row
#fifth box
canvas.create_rectangle(440, 640, 560, 520, outline = "white", width = "3")
#fourth box
canvas.create_rectangle(440, 520, 560, 400, outline = "white", width = "3")
#third box
canvas.create_rectangle(440, 400, 560, 280, outline = "white", width = "3")
#second box
canvas.create_rectangle(440, 280, 560, 160, outline = "white", width = "3")
#first box
canvas.create_rectangle(440, 160, 560, 40, outline = "white", width = "3")

                            #Third Row
#fifth box
canvas.create_rectangle(320, 640, 440, 520, outline = "white", width = "3")
#fourth box
canvas.create_rectangle(320, 520, 440, 400, outline = "white", width = "3")
#third box
canvas.create_rectangle(320, 400, 440, 280, outline = "white", width = "3")
#second box
canvas.create_rectangle(320, 280, 440, 160, outline = "white", width = "3")
#first box
canvas.create_rectangle(320, 160, 440, 40, outline = "white", width = "3")

                            #Fourth Row
#fifth box
canvas.create_rectangle(200, 640, 320, 520, outline = "white", width = "3")
#fourth box
canvas.create_rectangle(200, 520, 320, 400, outline = "white", width = "3")
#third box
canvas.create_rectangle(200, 400, 320, 280, outline = "white", width = "3")
#second box
canvas.create_rectangle(200, 280, 320, 160, outline = "white", width = "3")
#first box
canvas.create_rectangle(200, 160, 320, 40, outline = "white", width = "3")

                            #Fifth Row
#fifth box
canvas.create_rectangle(80, 640, 200, 520, outline = "white", width = "3")
#fourth box
canvas.create_rectangle(80, 520, 200, 400, outline = "white", width = "3")
#third box
canvas.create_rectangle(80, 400, 200, 280, outline = "white", width = "3")
#second box
canvas.create_rectangle(80, 280, 200, 160, outline = "white", width = "3")
#first box
canvas.create_rectangle(80, 160, 200, 40, outline = "white", width = "3")

#Coins/Bills Column Labels
canvas.create_text(620, 680, text = "Twenties\nValue: $ " + str(twenty_value), fill = "white", font = ('Arial 12 bold'))
canvas.create_text(500, 680, text = "Fives\nValue: $ " + str(five_value), fill = "white", font = ('Arial 12 bold'))
canvas.create_text(380, 680, text = "Loonies\nValue: $ " + str(loonie_value), fill = "white", font = ('Arial 12 bold'))
canvas.create_text(260, 680, text = "Quarters\nValue: $ " + str(quarter_value), fill = "white", font = ('Arial 12 bold'))
canvas.create_text(140, 680, text = "Nickels\nValue: $ " + str(nickels_value), fill = "white", font = ('Arial 12 bold'))

#Label for inital pennies
canvas.create_text(400, 736, text = "Initial Pennies Entered: " + str(amount_of_pennies) + " (¢)", fill = "white", font = ('Arial 12 bold'))

#Label for total amount and total change
canvas.create_text(250, 760, text = "Total Amount: $", fill = "white", font = ('Arial 12 bold'))
canvas.create_text(450, 760, text = "Total Change: $", fill = "white", font = ('Arial 12 bold'))

#Amount for total amount and total change
canvas.create_text(340, 760, text = str(total), fill = "white", font = ('Arial 12 bold'))
canvas.create_text(540, 760, text = str(remainder), fill = "white", font = ('Arial 12 bold'))

#Proportioanlly filled boxes for correct amount of currency 
canvas.create_rectangle(680, 640 - min(twenties, 5) * 120, 560, 640, fill = "#607C3C", outline = "white", width = "2")
canvas.create_rectangle(560, 640 - min(fives, 5) * 120, 440, 640, fill = "#809C13", outline = "white", width = "2")
canvas.create_rectangle(440, 640 - min(loonies, 5) * 120, 320, 640, fill = "#ABC32F", outline = "white", width = "2")
canvas.create_rectangle(320, 640 - min(quarters, 5) * 120, 200, 640, fill = "#B5E550", outline = "white", width = "2")
canvas.create_rectangle(200, 640 - min(nickels, 5) * 120, 80, 640, fill = "#ECECA3", outline = "white", width = "2")

#Amount of currency above the boxes
canvas.create_text(620, 640 - min(twenties, 5) * 120 - 8, text = twenties, fill = "white")
canvas.create_text(500, 640 - min(fives, 5) * 120 - 8, text = fives, fill = "white")
canvas.create_text(380, 640 - min(loonies, 5) * 120 - 8, text = loonies, fill = "white")
canvas.create_text(260, 640 - min(quarters, 5) * 120 - 8, text = quarters, fill = "white")
canvas.create_text(140, 640 - min(nickels, 5) * 120 - 8, text = nickels, fill = "white")

window.mainloop()




