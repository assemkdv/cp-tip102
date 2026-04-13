"""
Festival Lineup
Given two lists of strings artists and set_times of length n, 
write a function lineup() that maps each artist to their set time.

An artist artists[i] has set time set_times[i]. Assume i <= 0 < n and len(artists) == len(set_times).

def lineup(artists, set_times):
    pass
Example Usage:

artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

artists2 = []
set_times2 = []

print(lineup(artists1, set_times1))
print(lineup(artists2, set_times2))
Example Output:

{"Kendrick Lamar": "9:30 PM", "Chappell Roan": "5:00 PM", "Mitski": "2:00 PM", "Rosalía": "7:30 PM"}
{}

UNDERSTAND:
>> input: two lists of strings of length n
>> output: dictionary <string, string>

happy case 1: 
input: artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"] and set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]
output: set_times1 = {"Kendrick Lamar": "9:30 PM", "Chappell Roan": "5:00 PM", "Mitski": "2:00 PM", "Rosalía": "7:30 PM"}

happy case 2:
input: artists2 = []
output: {}

edge cases: 
>> empty list --> return empty dictionary

PLAN:
1. create an empty dictionary called match
2. iterate through the indices of the list of artists:
3. for each index:
   3.1 get the artist at that index
   3.2 get the set time at the same index
   3.3 match the artist with their time in the dictionary
4. return the dictionary   
"""

# IMPLEMENT
def lineup(artists, set_times):
    match = {}
    for i in range(len(artists)):
        match[artists[i]] = set_times[i]
    return match

artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

artists2 = []
set_times2 = []

print(lineup(artists1, set_times1))
print(lineup(artists2, set_times2))