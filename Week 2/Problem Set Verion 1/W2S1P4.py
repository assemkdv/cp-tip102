"""
Task:
Demand for your festival has exceeded expectations, so you're expanding the festival to span two different venues. 
Some artists will perform both venues, while others will perform at just one. 
To ensure that there are no scheduling conflicts, implement a function identify_conflicts() 
that accepts two dictionaries venue1_schedule and venue2_schedule 
each mapping the artists playing at the venue to their set times. 
Return a dictionary containing the key-value pairs that are the same in each schedule.

def identify_conflicts(venue1_schedule, venue2_schedule):
    pass
    
Example Usage:
venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM"
}
venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM"
}

print(identify_conflicts(venue1_schedule, venue2_schedule))

Example Output:
{"Stromae": "9:00 PM", "HARDY": "7:00 PM"}

UNDERSTAND:
input: two dictionaries
output: dictionary

PLAN:
1. create a dictionary called conflict
2. iterate through the key, value pairs of dictionary1:
    2.1. check if the dictionary2 contain the same key as dictionary1:
        2.2. check if the value for that key is the same
            2.3. add to the dictionary conflict
    3. return the dictionary
"""

#IMPLEMENT

def identify_conflicts(venue1_schedule, venue2_schedule):
    conflict = {}
    for artist, time in venue1_schedule.items():
        if artist in venue2_schedule:
            if time == venue2_schedule[artist]:
                conflict[artist] = time
    return conflict            
                
venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM"
}
venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM"
}

print(identify_conflicts(venue1_schedule, venue2_schedule))