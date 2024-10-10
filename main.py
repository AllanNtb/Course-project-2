# Name: Anne Allard Noteboom
# Course Code: BIT502
# Student Number: 4308756
# Assenssment: 2
#

# ------------------------------
# Imports
# ------------------------------

import tkinter
from tkinter import messagebox
import os


# ------------------------------
# Tkinter setup
# ------------------------------

window = tkinter.Tk()
window.title("City Gym Membership")
window.config(bg= '#34495e')


# ------------------------------
# Variables
# ------------------------------

# Store text in the variables so we can change it later if we need to

basic = "Basic"
regular = "Regular"
premium = "Premium"
three_months = "3 months"
six_months = "6 months"
twelve_months = "12 months"
weekly = "Weekly"
monthly = "Monthly"
optional_1 = "24/7 Access"
optional_2 = "Personal training"
optional_3 = "Diet consultation"
optional_4 = "Online video access"

# Variables that store the results of the elements

member_type = tkinter.StringVar(window, basic)                 # Selected membership type
member_duration = tkinter.StringVar(window, three_months)      # Duration of membership
direct_debit = tkinter.BooleanVar(window, False)            # Direct debit
extra1 = tkinter.BooleanVar(window, False)                  # Optional extra 1
extra2 = tkinter.BooleanVar(window, False)                  # Optional extra 2
extra3 = tkinter.BooleanVar(window, False)                  # Optional extra 3
extra4 = tkinter.BooleanVar(window, False)                  # Optional extra 4
payment_frequency = tkinter.StringVar(window, weekly)     # Payment frequency weekly/monthly

basic_price = 10
regular_price = 15
premium_price = 20

three_month_discount = 0
six_month_discount = 2
twelve_month_discount = 5

# ------------------------------
# Functions
# -------------------------

# Defining various functions
def clear_all():
    entry_first_name.delete(0, tkinter.END)
    entry_last_name.delete(0, tkinter.END)
    entry_address.delete(0, tkinter.END)
    entry_mobile.delete(0, tkinter.END)
    member_type.set(basic)
    member_duration.set(three_months)
    payment_frequency.set(weekly)
    direct_debit.set(False)
    extra1.set(False)
    extra2.set(False)
    extra3.set(False)
    extra4.set(False)
    label_total_cost_base.config(text="--")
    label_total_cost_extras.config(text="--")
    label_total_cost_discount.config(text="--")
    label_total_cost_total.config(text="--")
    label_total_cost_payment.config(text="--")


def calculate():
    # Takes care of collecting information on user's options chosen
    global membership_price
    global duration_discount
    global extra_total
    global direct_debit_discount_formula
    global frequency
    global total_discount
    global grand_total

    membership_price = 0.00
    duration_discount = 0.00
    extra_total = 0.00
    direct_debit_discount_formula = 0.00
    frequency = 0.00

    if member_type.get() == basic:
        membership_price += basic_price

    if member_type.get() == regular:
        membership_price += regular_price

    if member_type.get() == premium:
        membership_price += premium_price

    if member_duration.get() == three_months:
        duration_discount += three_month_discount

    if member_duration.get() == six_months:
        duration_discount += six_month_discount

    if member_duration.get() == twelve_months:
        duration_discount += twelve_month_discount

    if direct_debit.get() == True:
        direct_debit_discount_formula = (membership_price / 100) * 1
        
    if extra1.get() == True:
        extra_total += 1

    if extra2.get() == True:
        extra_total += 20

    if extra3.get() == True:
        extra_total += 20

    if extra4.get() == True:
        extra_total += 2

    # Calculate discounts and total price
    total_discount = direct_debit_discount_formula + duration_discount
    grand_total = membership_price + extra_total - total_discount

    if payment_frequency.get() == weekly:
        frequency = grand_total

    if payment_frequency.get() == monthly:
        frequency = grand_total * 4

    # Updates the window
    #label_total_cost_base.config(text=round(membership_price, 2))
    label_total_cost_base.config(text = f'${round(membership_price, 2)}')
    label_total_cost_extras.config(text = f'${round(extra_total, 2)}')
    label_total_cost_discount.config(text= f'${round(total_discount, 2)}')
    label_total_cost_total.config(text= f'${round(grand_total, 2)}')
    label_total_cost_payment.config(text= f'${round(frequency, 2)}')


def submit():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    address = entry_address.get()
    mobile = entry_mobile.get()
    type_member = member_type.get()
    duration = member_duration.get()
    payment = payment_frequency.get()
    regular_payment = 0.00
    method = ''

    #callinng calculate so we can use the data from the function in this function
    calculate()

    if first_name == '' or not first_name.isalpha():
        messagebox.showinfo("Error", "Please enter a valid first name.")
        return

    if last_name == '' or not last_name.isalpha():
        messagebox.showinfo("Error", "Please enter a valid last name.")
        return

    if address == '':
        messagebox.showinfo("Error", "Please enter your address.")
        return

    if mobile == '' or not mobile.isdigit():
        messagebox.showinfo("Error", "Please enter a valid mobile number.")
        return

    if type_member == '':
        messagebox.showinfo("Error", "Please select a membership type.")
        return

    if duration == '':
        messagebox.showinfo("Error", "Please select a membership duration.")
        return

    if payment == '':
        messagebox.showinfo("Error", "Please select a payment frequency.")
        return



    if direct_debit.get() == True:
        method = 'Direct Debit'

    else:
        method = 'Automatic Payment'

    # Write user details to text file
    with open('members_data.txt', 'a') as file:
        file.write(f'First Name: {first_name}\n')
        file.write(f'Last Name: {last_name}\n')
        file.write(f'Address: {address}\n')
        file.write(f'Mobile: {mobile}\n')
        file.write(f'Member Type: {type_member}\n')
        file.write(f'Membership Duration: {duration}\n')
        file.write(f'Membership Base Price: {membership_price}\n')
        file.write(f'Extras Price: {extra_total}\n')
        file.write(f'Total Discount: {total_discount}\n')
        file.write(f'Net Membership Price: {grand_total}\n')
        file.write(f'Regular Payments: {regular_payment}\n')
        file.write(f'Payment Frequency: {frequency}\n')
        file.write(f'Method of Payment: {method}\n')

    # Clear input fields and display success message
    clear_all()
    messagebox.showinfo('Completed', 'Your details have been submitted.')

    # ------------------------------
# Widget definitions
# ------------------------------
# The widget definitions are found in this section, no positioning has been done here, just declaration


#### Labels ####

label_first_name = tkinter.Label(window, text = "First Name:", bg= '#34495e', font= ('Helvetica', 10, 'bold'))
label_last_name = tkinter.Label(window, text = "Last Name:", bg= '#34495e', font= ('Helvetica', 10, 'bold'))
label_address = tkinter.Label(window, text = "Address:", bg= '#34495e', font= ('Helvetica', 10, 'bold'))
label_mobile = tkinter.Label(window, text = "Mobile:", bg= '#34495e', font= ('Helvetica', 10, 'bold'))

label_membership_type = tkinter.Label(window, text = "Membership Plan", bg= '#34495e', font= ('Helvetica', 10, 'bold'))
label_membership_duration = tkinter.Label(window, text = "Membership Duration", bg= '#34495e', font= ('Helvetica', 10, 'bold'))
label_direct_debit = tkinter.Label(window, text = "Direct Debit", bg= '#34495e', font= ('Helvetica', 10, 'bold'))
label_payment_frequency = tkinter.Label(window, text = "Payment Frequency", bg= '#34495e', font= ('Helvetica', 10, 'bold'))

label_optional_extras = tkinter.Label(window, text = "Optional Extras:", bg= '#34495e', font= ('Helvetica', 10, 'bold'))

label_total_header = tkinter.Label(window, text = "Totals", bg= '#34495e', font= ('Helvetica', 10, 'bold'))
label_total_base = tkinter.Label(window, text = "Membership:", bg= '#34495e', font= ('Helvetica', 10, 'bold'))
label_total_extras = tkinter.Label(window, text = "Extras:", bg= '#34495e', font= ('Helvetica', 10, 'bold'))
label_total_discount = tkinter.Label(window, text = "Discount:", bg= '#34495e', font= ('Helvetica', 10, 'bold'))
label_total_total = tkinter.Label(window, text = "Total:", bg= '#34495e', font= ('Helvetica', 10, 'bold'))
label_total_payment = tkinter.Label(window, text = "Regular payment:", bg= '#34495e', font= ('Helvetica', 10, 'bold'))


label_total_cost_base = tkinter.Label(window, text = "--", bg= '#34495e', font= ('Helvetica', 10, 'bold'))
label_total_cost_extras = tkinter.Label(window, text = "--", bg= '#34495e', font= ('Helvetica', 10, 'bold'))
label_total_cost_discount = tkinter.Label(window, text = "--", bg= '#34495e', font= ('Helvetica', 10, 'bold'))
label_total_cost_total = tkinter.Label(window, text = "--", bg= '#34495e', font= ('Helvetica', 10, 'bold'))
label_total_cost_payment = tkinter.Label(window, text = "--", bg= '#34495e', font= ('Helvetica', 10, 'bold'))


#### Entry text boxes ####

entry_first_name = tkinter.Entry(window)
entry_last_name = tkinter.Entry(window)
entry_address = tkinter.Entry(window)
entry_mobile = tkinter.Entry(window)

#### Radio buttons ####

radio_member_1 = tkinter.Radiobutton(window, text = basic, variable = member_type, value = basic, bg= '#34495e', font= ('Helvetica', 10, 'bold'))
radio_member_2 = tkinter.Radiobutton(window, text = regular, variable = member_type, value = regular, bg= '#34495e', font= ('Helvetica', 10, 'bold'))
radio_member_3 = tkinter.Radiobutton(window, text = premium, variable = member_type, value = premium, bg= '#34495e', font= ('Helvetica', 10, 'bold'))

radio_duration_1 = tkinter.Radiobutton(window, text = three_months, variable = member_duration, value = three_months, bg= '#34495e', font= ('Helvetica', 10, 'bold'))
radio_duration_2 = tkinter.Radiobutton(window, text = six_months, variable = member_duration, value = six_months, bg= '#34495e', font= ('Helvetica', 10, 'bold'))
radio_duration_3 = tkinter.Radiobutton(window, text = twelve_months, variable = member_duration, value = twelve_months, bg= '#34495e', font= ('Helvetica', 10, 'bold'))

radio_payment_1 = tkinter.Radiobutton(window, text = weekly, variable = payment_frequency, value = weekly, bg= '#34495e', font= ('Helvetica', 10, 'bold'))
radio_payment_2 = tkinter.Radiobutton(window, text = monthly, variable = payment_frequency, value = monthly, bg= '#34495e', font= ('Helvetica', 10, 'bold'))

#### Checkbuttons ####

checkbutton_direct_debit = tkinter.Checkbutton(window, text = "", variable = direct_debit, onvalue = True, offvalue = False, bg= '#34495e')

checkbutton_extra1 = tkinter.Checkbutton(window, text = optional_1, variable = extra1, onvalue = True, offvalue = False, bg= '#34495e', font= ('Helvetica', 10, 'bold'))
checkbutton_extra2 = tkinter.Checkbutton(window, text = optional_2, variable = extra2, onvalue = True, offvalue = False, bg= '#34495e', font= ('Helvetica', 10, 'bold'))
checkbutton_extra3 = tkinter.Checkbutton(window, text = optional_3, variable = extra3, onvalue = True, offvalue = False, bg= '#34495e', font= ('Helvetica', 10, 'bold'))
checkbutton_extra4 = tkinter.Checkbutton(window, text = optional_4, variable = extra4, onvalue = True, offvalue = False, bg= '#34495e', font= ('Helvetica', 10, 'bold'))


#### Buttons ####

button_calculate = tkinter.Button(window, text = "Calculate", command = calculate, bg= '#1abc9c', font= ('Helvetica', 10, 'bold'))
button_submit = tkinter.Button(window, text = "Submit", command = submit, bg= '#1abc9c', font= ('Helvetica', 10, 'bold'))


# ------------------------------
# Widget positioning
# ------------------------------
# All of the widget positioning is found here
# Another method of positioning widgets can be used if you comment this code out and use your own design

label_first_name.grid(row = 0, column = 0, sticky = "w")
label_last_name.grid(row = 1, column = 0, sticky = "w")
label_address.grid(row = 2, column = 0, sticky = "w")
label_mobile.grid(row = 3, column = 0, sticky = "w")

label_membership_type.grid(row = 4, column = 0, sticky = "w")
label_membership_duration.grid(row = 7, column = 0, sticky = "w")
label_direct_debit.grid(row = 10, column = 0, sticky = "w")
label_payment_frequency.grid(row = 16, column = 0, sticky = "w")

entry_first_name.grid(row = 0, column = 1, sticky = "w")
entry_last_name.grid(row = 1, column = 1, sticky = "w")
entry_address.grid(row = 2, column = 1, sticky = "w")
entry_mobile.grid(row = 3, column = 1, sticky = "w")

radio_member_1.grid(row = 4, column = 1, sticky = "w")
radio_member_2.grid(row = 5, column = 1, sticky = "w")
radio_member_3.grid(row = 6, column = 1, sticky = "w")

radio_duration_1.grid(row = 7, column = 1, sticky = "w")
radio_duration_2.grid(row = 8, column = 1, sticky = "w")
radio_duration_3.grid(row = 9, column = 1, sticky = "w")

checkbutton_direct_debit.grid(row = 10, column = 1, sticky = "w")

label_optional_extras.grid(row = 11, column = 0, sticky = "w")
checkbutton_extra1.grid(row = 11, column = 1, sticky = "w")
checkbutton_extra2.grid(row = 12, column = 1, sticky = "w")
checkbutton_extra3.grid(row = 13, column = 1, sticky = "w")
checkbutton_extra4.grid(row = 14, column = 1, sticky = "w")

radio_payment_1.grid(row = 16, column = 1, sticky = "w")
radio_payment_2.grid(row = 17, column = 1, sticky = "w")

label_total_header.grid(row = 18, column = 0, sticky = "w")
label_total_base.grid(row = 19, column = 0, sticky = "w")
label_total_extras.grid(row = 20, column = 0, sticky = "w")
label_total_discount.grid(row = 21, column = 0, sticky = "w")
label_total_total.grid(row = 22, column = 0, sticky = "w")
label_total_payment.grid(row = 23, column = 0, sticky = "w")

label_total_cost_base.grid(row = 19, column = 1, sticky = "w")
label_total_cost_extras.grid(row = 20, column = 1, sticky = "w")
label_total_cost_discount.grid(row = 21, column = 1, sticky = "w")
label_total_cost_total.grid(row = 22, column = 1, sticky = "w")
label_total_cost_payment.grid(row = 23, column = 1, sticky = "w")

button_calculate.grid(row = 24, column = 0)
button_submit.grid(row = 24, column = 1)

# ----------------------------------
# Tkinter mainloop
window.mainloop()