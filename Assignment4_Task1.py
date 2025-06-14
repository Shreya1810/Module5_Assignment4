i = 1
try:
    with open('sample.txt','r') as file:
        for line in file:
            print(f"line {i}: {line.strip()}")
            i += 1

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")