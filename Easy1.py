s = input().rstrip()

#including the length and english characters with space  
if 1 <= len(s) <= 104 and (st.isalpha() and st.isspace() for st in s):
    string = s.split(" ")
    
    # atleast one word to be present
    if any(word.isalpha() for word in string):
        #if the if condition is satisfied it prints the last word
        print(string[-1])
    else:
        print("At least one word to be present in the input.")
else:
    print("Invalid input.")