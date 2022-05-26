# Project-8
Goal:
This project is designed to reinforce the techniques around Python lists, dictionaries, and files.

Description:
This program will implement a few concepts around Ranked Choice Voting.

It will be comprised of a bunch of different functions.

Extra-Credit Opportunities
Check Gradescope for opportunities to earn extra credit for getting things working early.

Forbidden:
Your program may not use any techniques or Python features forbidden below. Do not use the following list-related functionality:

Do not use any string methods other than split.

Do not “import” any functionality into your code.

Do not use list slicing.

Do not use any techniques not covered in class.

You may use list’s append method

Violating these rules will sacrifice correctness credit.

Functional Requirements:
This program requires implementation of many user-defined functions outlined below.

**def get_file_contents(filename):**
  This function opens a file for reading, reads the contents into a string, and returns that string.

  If the file does not exist, the function should return None.

**def get_votes(string):**
  This function takes a string as its parameter and returns a list of list of strings as the return value:

  Lines are separated by the newline character. Your program can use the split method to separate the string into a list of lines.
  Empty lines should be ignored.
  Non-empty lines are comma-separated. Your program can use the split method to separate a line into a list of strings.
  Each list of strings represents the rankings of the candidates for one voter. The list of those lists represents all of the rankings by the voters.

  assert get_votes("a,b,c\nc,b,a\na,c,b") == [
      ["a", "b", "c"],
      ["c", "b", "a"],
      ["a", "c", "b"],
  ]
  assert get_votes("a,b\nb,a\na,b") == [["a", "b"], ["b", "a"], ["a", "b"]]
  In the first assert above, there were three voters who each ranked the candidates (a, b, and c).

  The first voter ranked a above b above c.
  The second voter ranked c above b above a.
  The third voter ranked a above c above b.

**def borda_scores(votes):**
  One way to elect a candidate using Ranked Choice Voting is called the “Borda Count” method. It assigns points to given rankings. The candidate with the   most points wins.

  If there are N candidates, being ranked first is worth N points, being ranked second is worth N-1 points, etc.

  This function should take a list of rankings as its input parameter, and it should return a dictionary. The returned dictionary has candidates as keys,    and for each key, the associated value is the total “Borda count” (i.e., points) for that candidate.

  Your code may assume that every voter ranked all of the candidates.
  votes1 = [["a", "b", "c"], ["c", "b", "a"], ["a", "c", "b"]]
  votes2 = [["a", "b"], ["b", "a"], ["a", "b"]]
  votes3 = [["a", "b", "c"], ["b", "c", "a"], ["c", "a", "b"]]

  assert borda_scores(votes1) == {"a": 7, "b": 5, "c": 6}
  assert borda_scores(votes2) == {"a": 5, "b": 4}
  assert borda_scores(votes3) == {"a": 6, "b": 6, "c": 6}
  
**def plurality(votes):**
  Another way to elect a candidate using Ranked Choice Voting is called the “Plurality” method. It assigns one point for being ranked first by a voter.     The candidate with the most points wins.

  This function should take a list of rankings as its input parameter, and it should return a dictionary. The returned dictionary has candidates as keys,   and for each key, the associated value is the total number of first-place rankings for that candidate.

  assert plurality(votes1) == {"a": 2, "c": 1}
  assert plurality(votes2) == {"a": 2, "b": 1}
  assert plurality(votes3) == {"a": 1, "b": 1, "c": 1}
  def pairwise(votes):
  Some very sophisticated ways of choosing a winner in Ranked Choice Voting depend on viewing the rankings as a bunch one-to-one contests. So, if Alice,     Bob, and Carol are all candidates, then we can view this as three different races: Alice vs. Bob, Alice vs Carol, and Bob vs. Carol.

  This function should take a list of rankings as its input parameter, and it should return a dictionary:

  The keys will be 2-value tuples of the form (candidateX, candidateY), where candidate here means the name of a candidate.
  The value associated with (candidateX, candidateY) will be the count of the number of times that candidateX was ranked above candidateY.
  There are no keys of the form (Z,Z). E.g., there is no key ("Alice", "Alice") because it doesn’t make sense to think of Alice being ranked above or       below herself.
  assert pairwise(votes1) == {
      ("a", "b"): 2,
      ("a", "c"): 2,
      ("b", "c"): 1,
      ("c", "b"): 2,
      ("c", "a"): 1,
      ("b", "a"): 1,
  }

  assert pairwise(votes2) == {("a", "b"): 2, ("b", "a"): 1}

  assert pairwise(votes3) == {
      ("a", "b"): 2,
      ("a", "c"): 1,
      ("b", "c"): 2,
      ("b", "a"): 1,
      ("c", "a"): 2,
      ("c", "b"): 1,
  }
  
**def condorcet_winner(votes):**
  Another way to elect a candidate using Ranked Choice Voting is called the “Condorcet” method. It looks to see if there is a candidate that “beat” every   other candidate in head-to-head matches.

  For instance, in a race between Alice, Bob, and Carol, if Alice was ranked above Bob more often than Bob was ranked above Alice, and Alice was ranked     above Carol more often than Carol was ranked above Alice, then Alice beat all the other candidates head-to-head, and would be the Condorcet winner.

  This function should take a list of rankings as its input parameter, and it should return the Condorcet winner, if there is one. If no candidate           qualifies as a Condorcet winner, then the function should return None.

  assert condorcet_winner(votes1) == "a"
  assert condorcet_winner(votes2) == "a"
  assert condorcet_winner(votes3) == None
  def winners(scores):
  This function takes a single dictionary as its parameter. The dictionary maps candidates to their scores. It should return a list of the candidate(s)     with the highest score.

  The return value should be sorted in ascending order using the sort method on lists.

  assert winners({"a": 1, "b": 2, "c": 3}) == ["c"]
  assert winners({"a": 1, "b": 1, "c": 1}) == ["a", "b", "c"]
  
  
Testing file-based programs
Developing and testing file-based programs is more complicated than simple assert-based development we’ve done previously.

Advice:
Start early.
Read the requirements carefully, including the forbidden/required elements. Note that there are per-function requirements and some program-wide requirements.
Do one function at a time, get it working, and then move on the the next function.
Start early.
Code Style Requirements:
Please see the Style Guide posted to D2L for docstring formatting requirements. It is located under Content > Table of Contents > Project Information > Project Style Guide

This link may work: Project Style Guide

Grading:
The project will be graded on passing all the test cases (77%) and adherence to expectations (23%) (e.g., docstring format, avoiding forbidden things).

Turn-In Process:
What to turn in: A single file called, “rcv.py”, that includes the functions described above. (The grading system is case-sensitive, so make sure your filename is in all lower-case letters.)

Where to turn it in: https://gradescope.com/

Note that the test cases are automatically run when you submit your program. If you wish to resubmit your program (prior to the deadline), you may do so as many times as you like. I.e., you can fix bugs and resubmit.

NOTE: This assignment is NOT turned in via D2L. It must be turned in via Gradescope.
Late Policy
Projects are not accepted late.

Due Date
Apr 28, 2022 8:00 PM
Completion Date: Apr 28, 2022 8:00 PM
