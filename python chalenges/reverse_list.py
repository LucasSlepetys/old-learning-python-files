
#! Challenge:
#* A giving list was given. It's lenght is undefined. It could be a list of 5 items or a list of 100 items...
#* With the given list:

#* 1) Reverse the list E.X: [0,1,2,3,4,5] -> [5,4,3,2,1,0]
#* 2) Convert all letters to capital letter
#* 3) Convert all words with lenght of < 6 to small letters

#! Sample Input:

list = ["Lucas", "hi", 10, 11, "computer", "hello", "Germany", "Brazil"]

#! Expected Output:

#list = ["BRAZIL", "GERMANY", "hello", "COMPUTER", 11, 10, "hi", "lucas"]

#! Code goes here:

def reverse_list(list):
    output_list = []
    for i in list[::-1]:
        try:
            i = i.upper()
        except Exception:
            print("It's a number!")

        try:
            if len(i) < 6:
                i = i.lower()
        except Exception:
            print("Number...")
        
        output_list.append(i)
        
    return output_list
    
print(reverse_list(list))