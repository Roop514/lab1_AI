"""
Your name(s): Rupinder Kaur
"""


from nodes import WikiPage
from collections import deque

# change the start and destination pages as you like - see if your algorithm can find a route between them
start = WikiPage('https://en.wikipedia.org/wiki/Mount_Royal_University')
goal = WikiPage('https://en.wikipedia.org/wiki/Artificial_intelligence')



# What search algorithm are you using? Why?
# (your response here)



# Does your code work? (Verify the route found by your search algorithm)




# YOUR SEARCH ALGORITHM CODE HERE

def breadth_first_search(problem):
    if problem.is_goal(problem.initial):
        return problem.initial
    
    frontier = deque()
    frontier.append(problem.initial) 
    reached = {problem.initial}

    while frontier():
        state = frontier.popleft()

        for child in expand(state):
            if problem.is_goal(child):
                return child
            if child not in reached:
                reached.add(child)
                frontier.append(child)
    
    return failure
  
# (print the discovered route when you find it)




# Can you think of a search approach that could be faster than your implementation above?
# Describe it.
