

# Convert each item to integer after splitting the string input by a whitespace. Thereafter, create a list of the integers.
arr = list(map(int, input().split(" ")))
N = len(arr)

seen = set(); # Create an unordered set

mex = 0; # Initialise the minimum element 
output = [] # Create an array for the output

# Iterate each item in the given input
for i in range(0, N) :
    # Add that item to the seen items
    seen.add(arr[i])
    while mex in seen:
        mex += 1
    output.append(mex)

# Convert each list item to a string, then join them separated by a whitespace
print(" ".join(map(str, output)))