


def fun(a):
    # Define the available currency notes
   l = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

    # Create a dictionary to store the count of each note
   d = {}

    # Initialize the note count dictionary with 0 for each note denomination
   for i in l:
        d[i] = 0

    # Calculate the number of each currency note required
    for i in l:
        if a >= i:
            count = a// i
            a -= count * i
            d[i] = count

    # Print the result
    for note, count in note_count.items():
            print(f"{note} {count}")

# Example usage
a=int(input("Enter amount "))
fun(a)






