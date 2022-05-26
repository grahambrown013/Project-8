""" Graham Brown
    CSC 110 SP22 001-2
    Project -8

    This program implements concepts around 'Ranked Choice Voting'.
    Each function will take a list of scores essentially and return a winner based off of  the guidelines of the Ranked Choice Votings we use.
    The functions:
        1. get_file_contents(filename):
            This function takes this file, 'filename', reads the contents into a string, and returns that string.split
            If the file does not exist, the function should return None.

        2. get_votes(string):
            This function will take the parameter 'string' and return a split up string as a list of list of strings.

        3. borda_scores(votes):
            This function will return a dictionary which has candidates as keys and for each key, the associated value is the total "Borda count"
            Borda Count: Assigns points to given rankings. The candidate with the most points wins.

        4. plurality(votes):
            This function should return a dictionary that has candidates as keys and for each key,
            the associated value is the total number of first-place rankings for that candidate.

        5. pairwise(votes):
            This function should return a dictionary. The keys will be 2-value tuples of the form (candidateX, candidateY), where candidate here means the name of a candidate.
            The value associated with (candidateX, candidateY) will be the count of the number of times that candidateX was ranked above candidateY.
            There are no keys of the form (Z,Z). E.g., there is no key ("Alice", "Alice") because it doesn’t make sense to think of Alice being ranked above or below herself.

        6. condorcet_winner(votes):
            This function should return a string which is the Condorcet winner. If no candidate qualifies as a Condorcet winner, the function will return None.
            A Condorcet winner is the candidate that beat every other candidate in head-to-head matches.

        7. winners(scores):
            This function should return a list of the candidate(s) with the highest score.


"""

def get_file_contents(filename):
    """
    Args:
        A file (presumably .csv because that's what we been working with)

    Returns:
        This function takes this file, 'filename', reads the contents into a string, and returns that string.split
        If the file does not exist, the function should return None.

    """
    open_file = open(filename,'r')
    result=''
    for line in open_file:
        result += line

    if result == '':
        return None
    else:
        return result

def get_votes(string):
    """
    Args:
        string: A string containing letters, commas and '\n'
    Returns:
        This function will take the parameter 'string' and return a split up string as a list of list of strings.

    """
    split_list = string.split('\n')
    result = []
    temp = []
    for string in split_list:
        for index in string:
            if index != ',':
                temp.append(str(index))
        if len(temp) > 0:
            result.append(temp)
        temp = []
    return result

def borda_scores(votes):
    """
    Args:
        votes (list): A list of rankings

    Returns:
        This function will return a dictionary which has candidates as keys and for each key, the associated value is the total "Borda count"
        Borda Count: Assigns points to given rankings. The candidate with the most points wins.
    """
    result = {}

    for L in votes:
        for strings in range(len(L)):
            num_voters = len(L)
            index = 0
            if L[strings] not in result:
                result[L[strings]] = 0
            while num_voters > 0:
                if strings == index:
                    result[L[strings]] += len(L)-index
                index+=1
                num_voters-=1
    return result

def plurality(votes):
    """
    Args:
        votes (dictionary): A list of rankings.

    Returns:
        This function should return a dictionary that has candidates as keys and for each key,
        the associated value is the total number of first-place rankings for that candidate.

    """
    result = {}
    for L in votes:
        for strings in range(len(L)):
            if strings == 0 and L[strings] not in result:
                result[L[strings]] = 1
            elif strings == 0:
                result[L[strings]] += 1
    return result

def pairwise(votes):
    """
    Args:
        votes (dictionary): A list of rankings.

    Returns:
        This function should return a dictionary. The keys will be 2-value tuples of the form (candidateX, candidateY), where candidate here means the name of a candidate.
        The value associated with (candidateX, candidateY) will be the count of the number of times that candidateX was ranked above candidateY.
        There are no keys of the form (Z,Z). E.g., there is no key ("Alice", "Alice") because it doesn’t make sense to think of Alice being ranked above or below herself.
    """
    result = {}
    pairs = []
    #gather pairs into a list
    for List in votes:
        for letter in range(len(List)):
            for l in range(letter+1, len(List)):
                pair = (List[letter], List[l])
                if pair not in pairs and pair[0]!=pair[1]:
                    pairs.append(pair)
    #loop through pairs
    for pair in pairs:
        #loop through the original lists and check what index comes before the other.
        for List in votes:
            letter_check = False
            for letter in List:
                if letter == pair[1]:
                    letter_check = True
                elif letter == pair[0] and letter_check == False:
                    if pair not in result:
                        result[pair] = 0
                    result[pair] += 1

    return result

def condorcet_winner(votes):
    """
    Arg:
        votes (dictionary): A list of rankings.

    Returns:
        This function should return a string which is the Condorcet winner. If no candidate qualifies as a Condorcet winner, the function will return None.
        A Condorcet winner is the candidate that beat every other candidate in head-to-head matches.
    """
    #if index 0 is ranked above index 1 more often and
    #index 0 was ranked above index 2 more often
    #index 0 beat all candidates
    #else if 1 is ranked above 0 and 2 more often, 1 wins
    temp = pairwise(votes)
    #print(temp)
    largest = 0
    immediate_loser = ''
    for pair in temp:
        value = temp[pair]
        if value > largest:
            largest = value
            immediate_loser = pair[1]
    new = {}
    for pair in temp:
        value = temp[pair]
        if pair[0] != immediate_loser and pair[1] != immediate_loser:
            new[pair] = value

    #print(new)
    largest = 0
    winner = ''
    Tie = False
    for pair in new:
        value = new[pair]
        if value > largest:
            largest = value
            winner = pair[0]
            Tie = False
        elif value == largest:
            Tie = True

    if len(votes) == 1:
        for k in votes:
            return k[0]
    if Tie == True:
        return None
    elif Tie == False:
        return winner
def winners(scores):
    """
    Args:
        scores (dictionary): A dictionary mapping candidates to their scores.

    Returns:
        This function should return a list of the candidate(s) with the highest score.
    """
    largest = 0
    for key in scores:
        value = scores[key]
        if value > largest:
            largest = value
    winners = []
    for key in scores:
        value = scores[key]
        if value == largest:
            winners.append(key)

    return winners

def main():
    #get_votes("a,b,c\nc,b,a\na,c,b")
    votes1 = [["a", "b", "c"], ["c", "b", "a"], ["a", "c", "b"]]
    votes2 = [["a", "b"], ["b", "a"], ["a", "b"]]
    votes3 = [["a", "b", "c"], ["b", "c", "a"], ["c", "a", "b"]]
    #winners({"a": 1, "b": 2, "c": 3})
    #winners({"a": 1, "b": 1, "c": 1})
    condorcet_winner([('Carol', 'Bob', 'Alice'), ('Bob', 'Alice', 'Carol')])
    #condorcet_winner([('Bob', 'Alice'), ('Alice', 'Bob'), ('Bob', 'Alice')])
    #condorcet_winner([('Bob', 'Carol', 'Alice'), ('Carol', 'Alice', 'Bob')])
    #condorcet_winner([('Alice','Bob'), ('Bob','Alice')])
    #condorcet_winner([('Alice', 'Bob', 'Carol'), ('Bob', 'Carol', 'Alice')])
    #condorcet_winner(votes1) == {"a": 7, "b": 5, "c": 6}
    #condorcet_winner(votes2) == {"a": 5, "b": 4}
    #condorcet_winner(votes3) == {"a": 6, "b": 6, "c": 6}
main()
