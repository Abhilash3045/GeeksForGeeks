# Function to check if string
# starts and ends with 'gfg'
def gfg(S):
    b = S.lower()
    if (b[:3]=="gfg" and b[-3:]=="gfg"):
        print("Yes")
    else:
        print("No")