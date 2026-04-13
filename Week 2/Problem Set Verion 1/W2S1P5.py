"""
Best Set
As part of the festival, attendees cast votes for their favorite set. 
Given a dictionary votes that maps attendees id numbers to the artist they voted for, 
return the artist that had the highest number of votes. 
If there is a tie, return any artist with the top number of votes.

def best_set(votes):
    pass
Example Usage:

votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

print(best_set(votes1))
print(best_set(votes2))
Example Output:

SZA
Ethel Cain
Note: SZA and Ethel Cain would both be acceptable answers for the second example

UNDERSTAND:
input: dictionary <int, string>
output: string (artist with the highest number of votes)

PLAN:
1. create an empty dictionary called freq
2. loop through the values in votes:
   2.1 count how many times each artist appears
   2.2 store the count in freq
3. return the key in freq with the highest value

IMPLEMENT:
"""

def best_set(votes):
    if len(votes) == 0:
        return None
    freq = {}
    for artist in votes.values():
        freq[artist] = freq.get(artist, 0) + 1
    return max(freq, key=freq.get)            

votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}
print(best_set(votes1))

votes2 = {}
print(best_set(votes2))