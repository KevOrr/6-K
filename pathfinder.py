import collections

def getmovies(person):
    pass #TODO implement

def getpeople(movie):
    pass #TODO implement

def get_related_people(person):
    related_people = []
    for movie in getmovies(person):
        for related_person in getpeople(movie):
            related_people.append((person.id, movie.id, related_person.id)) #TODO change to correct id attribute
    return related_people

def findpath(start, goal, heuristic=None, verbosity=1):
    """findpath(start, goal, heuristic=None, verbosity=1): --> path list

    The brains of 6°K, findpath utilizes a bidirectional tree search to find the optimal path
    between two people nodes (but who cares about any other goal node besides Bacon?).
    
    start and goal must be two TODO ids or TODO people objects.
    
    heuristic isn't currently implemented, but when it is, it must be a callable that
    can take a TODO object and return a float from 0 to 1, representing the relative probability
    that the goal node can be found using a path from the current node.
    
    verbosity
        0. No printed output
        1. Only print success/failure messages
        2. Also print additional info, such as the current node that is being expanded"""

    start_paths = collections.deque([[related] for related in get_related_people(start)])
    goal_paths = collections.deque([[related] for related in get_related_people(goal)])
    start_seen, goal_seen = set([link[2] for link in start_paths]), set([link[2] for link in goal_paths])
    start_seen.add(start)
    goal_seen.add(goal)
    
    while True:
        current_start_depth = len(start_paths[0])
        while current_start_depth == len(start_paths[0]):
            current_start_path = start_paths.popleft()
            if max_depth and len(current_start_path) >= max_depth:
                if verbosity >= 1:
                    print('Failed to find a path from {} (id {}) to {} (id {}) within {} links') # TODO format this
            if verbosity >= 2:
                print('Currently expanding {} (id {}) from the start side') #TODO
            for link in get_related_people(current_start_path[-1][2]):
                if link[2] in goal_seen:
                    if verbosity >= 1:
                        print('Found a path of length {} from {} (id {}) to {} (id {})') #TODO
                    return joinpaths(current_start_path, goal_paths)
                if link[2] in start_seen:
                    continue
                else:
                    start_paths.append(current_start_path + link)
                    start_seen.add(link[0])
                # if get_related_people is exhausted, the current node won't be appended back to the queue

        # This next block should basically be a mirror of the above block
        current_goal_path = goal_paths.popleft()
        if verbosity >= 2:
            print('Currently expanding {} (id {}) from the goal side') #TODO
        for link in get_related_people(current_goal_path[-1][0]):
            if link[0] in start_seen:
                current_link = []
                total_path = [i for i in link for link in joinpaths(current_goal_path, start_path)]
                final_path = [(total_path.pop(0),)]
                if verbosity >= 1:
                    print('Found a path of length {} from {} (id {}) to {} (id {})') #TODO
                return reversepath(joinpaths(current_goal_path, start_paths)))
            if link[0] in goal_seen:
                continue
            else:
                goal_paths.append(current_goal_path + link)
                goal_seen.add(link[0])
            # if get_related_people is exhausted, the current node won't be appended back to the queue

def joinpaths(start_path, goal_paths):
    pass
        
