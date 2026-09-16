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

def breadth_first_search(start,goal):
    if start == goal:
        return start
    
    frontier = deque()
    frontier.append(start) 
    reached = {start}

    while frontier:
        state = frontier.popleft()

        for child in state.children:
            if child == goal:
                return child
            if child not in reached:
                reached.add(child)
                frontier.append(child)
    
    return None

result = breadth_first_search(start, goal)
print(result)

# (print the discovered route when you find it)




# Can you think of a search approach that could be faster than your implementation above?
# Describe it.
