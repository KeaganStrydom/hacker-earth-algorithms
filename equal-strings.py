
t = int(input()); # Number of test cases

# Switch any two 
def flipAny(i, j, S):
    interim = S[i]
    S[i] = S[j];
    S[j] = interim;

for case in range(0, t):
    # Get length and cost
    N, X = map(int, input().split(" "))

    S = input()
    T = input()
    cost = 0;

    for i in range(0, N):
        for j in range(i, N):
            if (T[i] == S[j]):
                if (i == j): 
                    break; # Do nothing
                
                if (j-i == 1): # Neighbours
                    cost += 1;
                else:
                    cost += X;
                
                flipAny(i, j, S)
                break; # Currently not equal
                





