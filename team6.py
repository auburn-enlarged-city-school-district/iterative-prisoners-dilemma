####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

strategy_name = 'The name the team gives to this strategy'
strategy_description = 'How does this strategy decide?'
strategy_name = 'Follower'
strategy_description = 'If the other team colludes more than betrays, colludes. If the other team betrays more than colludes, betray.'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    
    collude_count = num_colludes(their_history)
    betray_count = num_betray(their_history)
    
    if collude_count >betray_count:
        return 'c'
    else:
        return 'b'


def num_colludes(their_history):
    '''Determines how many times the other team has 
        colluded and returns that number
    '''
    count = 0
    for i in range(len(their_history)):
        if their_history[i] == "c":
            count += 1
    return count
    
    
def num_betray(their_history):
    '''Determines how many times the other team has 
        betrayed and returns that number
    '''
    count = 0
    for i in range(len(their_history)):
        if their_history[i] == "b":
            count += 1
    return count
