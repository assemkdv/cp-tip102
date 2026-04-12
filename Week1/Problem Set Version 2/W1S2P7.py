"""
NaNaNa Batman!
Write a function nanana_batman() that accepts an integer x and 
prints the string "nanana batman!" where "na" is repeated x times. 
Do not use the * operator.

def nanana_batman(x):
	pass
Example Usage

x = 6
nanana_batman(x)

x = 0
nanana_batman(x)
Example Output:

"nananananana batman!"
"batman!"
"""

def nanana_batman(x):
    result = ""
    i = 0
    while i < x:
        result += "na"
        i += 1

    if result:
        print(f"{result} batman!")
    else:
        print("batman!")    


x = 6
nanana_batman(x)

x = 0
nanana_batman(x)