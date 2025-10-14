
header = """\n\t***** BOOKSTORE RECEIPT *****
\t------------------------------"""


item1 = "\nBook Title: {}\tPrice: ₹{}".format("Python Basics", 450)
item2 = "\nBook Title: {}\tPrice: ₹{}".format("Data Science Intro", 600)


total_price = 450 + 600
total = "\n\nTotal Price:₹{}".format(total_price)


thank_you="\n\tthank"+"-"+"you"

receipt = header + item1 + item2 + total + thank_you

print(receipt.upper())
