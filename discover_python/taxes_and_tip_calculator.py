print "Welcome to the taxes and tip calculator!" #Welcoming the user

price_b_tax = float(raw_input("What is the price before tax?")) #Base price of meal
tax = float(raw_input("What are the taxes? (in %)")) #Getting the percentage of tax from user 
tip = float(raw_input("What do you want to tip? (in %)")) #Getting tip percentage from the user

price = price_b_tax * (100+tax) * (100 + tip) / 10000 #Math's to get the final price

print "The price you pay is: $%s" % price #Displaying final price
