# Ex 1
assert "price_usd" in paid_to_growers.columns, "Ex. 1 - You need to create the price_usd column in the paid_to_growers DataFrame!"
assert paid_to_growers["price_usd"].dtype == pd.Series([0.1,0.2,0.3]), "Ex. 1 - The price_usd column is not of type float! You can convert it with the .astype() method"
assert abs(paid_to_growers["price_usd"].mean()-0.8660280468749999) < 0.01, "Ex. 1 - Are you sure you divided by the right factor? Remember that one cent is 0.01 dollars. Note: Don't round your results."
print("Exercise 1 looks correct!")

# Ex 2
assert "price_ratio" in paid_to_growers.columns, "Ex. 2 - You need to create the price_ratio column in the paid_to_growers DataFrame!"
assert paid_to_growers["price_ratio"].dtype == pd.Series([0.1,0.2,0.3]), "Ex. 2 - The price_ratio column is not of type float! If you divide two columns of type float, the result is a float."
assert abs(paid_to_growers["price_ratio"].mean()-4.875194287709183) < 0.01, "Ex. 2 - Are you sure you divided the right columns? Note: Don't round your results."
print("Exercise 2 looks correct!")

# Ex 3
assert "answer" in globals(), "Ex. 3 - You need to create the answer variable! You do that by uncommenting the appropriate line in exercise 3."
assert type(answer) == type("hey"), "Ex. 3 - The answer variable is not a string. Something really weird must have happened. Don't change or redefine the variable, simply uncomment the line!"
print("Exercise 3 passed the preliminary sanity checks.")
print("Exercise 3 looks correct!")