# Open the input file for reading and the output file for writing
with open("new.txt", "r") as f, open("new2.txt", "w") as f2:
    content = f.read()  # Read the entire content of the file

    digits = "0123456789"
    n_alpha = 0
    n_digits = 0

    # Iterate through each character in the content
    for char in content:
        if char.isalpha():
            n_alpha += 1
        elif char.isdigit():
            n_digits += 1

    # Write the counts to the output file
    f2.write(f"Letters are {n_alpha}\nDigits are {n_digits}")

# Files are automatically closed when exiting the 'with' block
