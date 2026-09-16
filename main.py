"""
Your name(s): Rupinder Kaur , Loren Mena
"""


from nodes import WikiPage
from collections import deque

# change the start and destination pages as you like - see if your algorithm can find a route between them
start = WikiPage('https://en.wikipedia.org/wiki/Mount_Royal_University')
goal = WikiPage('https://en.wikipedia.org/wiki/Artificial_intelligence')


# What search algorithm are you using? Why?
# We are using the breadth first search algorithm because it explores
# pages level by level and finds the shortest path from the starting
# page to goal page



# Does your code work? (Verify the route found by your search algorithm)
# Yes, running the search from Mount_Royal_University to
# Artificial_intelligence found the shortest route, which has 2 links:
# Mount_Royal_University -> University_of_Alberta -> Artificial_intelligence
# We manually verified this route by checking both pages on Wikipedia and
# confirming each contains a real hyperlink to the next page in the route.



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

if result is not None:
    route = result.get_ancestors()
    print(f"Route found ({len(route) -1} links):")
    for page in route:
        print(" ", page)
else:
    print("No route found.")

# (print the discovered route when you find it)




# Can you think of a search approach that could be faster than your implementation above?
# Describe it.
#
# Bidirectional BFS.
# Instead of only searching forward from the start page, we could search
# from both ends at the same time. So while we're expanding pages
# forward from Mount_Royal_University like we already do, we'd also run
# a second search backward from Artificial_intelligence, using pages
# that link TO it instead of pages it links to. We'd go back and forth
# expanding a bit from each side until the two searches bump into each
# other on some page. Once that happens we know we found a connection,
# and we can stitch the two halves together to get the full path.
