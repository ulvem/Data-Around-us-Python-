# The following line is an example of how you can add a string (aka text) value to a variable.
exampleVariable = "This is a string added to the variable named exampleVariable"

'''
Explanation:

[variable name] [equal sign] [value]

[variable name]: `exampleVariable`
You can give almost any name to a variable, but be careful with two things:
1. Don't use special characters in it.
2. Use the "snake_case" form where words are separated by underscores, 
   and all letters are in lowercase (e.g., this_is_a_snake_case_text).
   Alternatively, Python also allows "camelCase" like JavaScript, but "snake_case" is more common in Python for variable names.
It is recommended to use the English language throughout your code, especially (but not exclusively) for variable names.

[equal sign]: `=`
Remember, the equal sign between the variable name and the value is crucial.
This serves as the "assignment operator" which assigns the value to the variable.

[value]: `"This is a string added to the variable named exampleVariable"`
The value is the piece of data you want to assign (save) to the variable for later use.

In Python, there's no need for a semicolon at the end of the line.
'''

# The following line is just an example of how you can print text to the console using `print()`.
# You have to write a value or a variable name inside the parentheses.
""" print(exampleVariable) """

# WRITE YOUR CODE HERE
# Import the datetime module to get the current year
import datetime
# Define the details of the first book
book1 = {
    'title': 'To Kill a Mockingbird',
    'author': 'Harper Lee',
    'year': 1960,
    'characters': ['Scout Finch', 'Atticus Finch', 'Jem Finch', 'Tom Robinson']
}

# Define the details of the second book
book2 = {
    'title': '1984',
    'author': 'George Orwell',
    'year': 1949,
    'characters': ['Winston Smith', 'Julia', 'O’Brien', 'Big Brother']
}

# Open the file in write mode
with open('books_info.txt', 'w') as file:
    # Write the details of the first book
    file.write(f"Title: {book1['title']}\n")
    file.write(f"Author: {book1['author']}\n")
    file.write(f"Year of First Publication: {book1['year']}\n")
    file.write(f"Characters: {', '.join(book1['characters'])}\n\n")
    
    # Write the details of the second book
    file.write(f"Title: {book2['title']}\n")
    file.write(f"Author: {book2['author']}\n")
    file.write(f"Year of First Publication: {book2['year']}\n")
    file.write(f"Characters: {', '.join(book2['characters'])}\n")

# Print a confirmation message
print("Book details have been written to books_info.txt")
print("books_info.txt")

# Create a variable named title and assign it the title of your favorite book
title = "To Kill a Mockingbird"

# Print the value of title
print(title)

# Create a variable named author and assign it the author of your favorite book
author = "Harper Lee"

# Print the value of author
print(author)

# Create a variable named year and assign it the publication year of your favorite book
year = 1960

# Print the value of year
print(year)

# Create a variable named year and assign it the publication year of your favorite book
year = 1960

# Create a variable named isNewerThan2000 and set it based on the publication year
isNewerThan2000 = year > 2000

# Print the value of isNewerThan2000
print(isNewerThan2000)

# Create a variable named year and assign it the publication year of your favorite book
year = 1960

# Get the current year
current_year = datetime.datetime.now().year

# Calculate the age of the book
age = current_year - year

# Print the value of age
print(age)

# Create a variable named characters and assign a list of character names from your book
characters = ["Scout Finch", "Atticus Finch", "Jem Finch", "Tom Robinson"]

# Print the value of characters
print(characters)

# Create a variable named characters and assign a list of character names from your book
characters = ["Scout Finch", "Atticus Finch", "Jem Finch", "Tom Robinson"]

# Print the value of the first item from the characters list
print(characters[0])

# Print the value of the second item from the characters list
print(characters[1])

# Define the details of your favorite book
title = "To Kill a Mockingbird"
author = "Harper Lee"
year = 1960
characters = ["Scout Finch", "Atticus Finch", "Jem Finch", "Tom Robinson"]

# Calculate the age of the book
current_year = datetime.datetime.now().year
age = current_year - year

# Determine if the book was published after the year 2000
isNewerThan2000 = year > 2000

# Create a dictionary to store all properties of the book
favoriteBook = {
    'title': title,
    'author': author,
    'year': year,
    'isNewerThan2000': isNewerThan2000,
    'age': age,
    'characters': characters
}

# Print the favoriteBook dictionary
print(favoriteBook)

# Print the value of the author key
print(favoriteBook['author'])

# Print the value of the year key
print(favoriteBook['year'])

# Print the first character from the characters list within the favoriteBook dictionary
print(favoriteBook['characters'][0])

# Calculate the age of each book
current_year = datetime.datetime.now().year
book1['age'] = current_year - book1['year']
book2['age'] = current_year - book2['year']

# Determine if each book was published after the year 2000
book1['isNewerThan2000'] = book1['year'] > 2000
book2['isNewerThan2000'] = book2['year'] > 2000

# Create a list to store the book dictionaries
favoriteBooks = [book1, book2]

# Print the favoriteBooks list
print(favoriteBooks)

# Calculate the age of each book
current_year = datetime.datetime.now().year
book1['age'] = current_year - book1['year']
book2['age'] = current_year - book2['year']

# Determine if each book was published after the year 2000
book1['isNewerThan2000'] = book1['year'] > 2000
book2['isNewerThan2000'] = book2['year'] > 2000

# Create a list to store the book dictionaries
favoriteBooks = [book1, book2]

# Display the title of the second book
print(favoriteBooks[1]['title'])

# Display the first character's name from the characters list of the second book
print(favoriteBooks[1]['characters'][0])

# Calculate the age difference between the two books
age_difference = abs(favoriteBooks[0]['age'] - favoriteBooks[1]['age'])

# Display the age difference
print(f"The age difference between the two books is {age_difference} years.")

