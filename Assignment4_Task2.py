# Write and Append Data to a File
with open('output.txt', "w") as file:
    text1 = input("Enter text to write to the file: ")
    file.write(text1)
    print("Data successfully written to output.txt.")

# Open the same file in append mode and add more content
with open('output.txt', "a") as file:
    text2 = input("Enter additional text to append: ")
    file.write(text2)
    print("Data successfully appended.")

print("Final content of the file")
with open('output.txt', "r") as file:
    for line in file:
        print(line,end="\n")
