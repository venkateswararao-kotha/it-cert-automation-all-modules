'''
Let's look at one last code block. The Guess() function below takes a list of participants,
assigns each a random number from 1 to 9, and stores this information in a dictionary with
the participant name as the key. It then returns True if Larry was assigned the number 9
and False if this was not the case. Run it to see what it does.



import random

participants = ['Jack', 'Jill', 'Larry', 'Tom']


def Guess(participants):
    my_participant_dict = {}
    for participant in participants:
        my_participant_dict[participant] = random.randint(1, 9)
    if my_participant_dict['Larry'] == 9:
        return True
    else:
        return False


print(Guess(participants))


The code seems to be working fine. However, there are some things that could go wrong, 
so find the part that might throw an exception and wrap it in a try-except block to ensure 
that you get sensible behavior. Do this in the cell below. Code your function to return 
None if an exception occurs.

'''

# Revised Guess() function
def Guess(participants):
    my_participant_dict = {}
    try:
        for participant in participants:
            my_participant_dict[participant] = random.randint(1, 9)
        if my_participant_dict['Larry'] == 9:
            return True
    except:
        return None
    else:
        return False

participants = ['Cathy','Fred','Jack','Tom']
print(Guess(participants))


'''
Was the above output None? If not, go back to the code block containing your revised Guess() function and 
make edits so that the output is None for the previous code block. If the above output was indeed None, 
congratulations! You've mastered the basics of handling errors and exceptions in Python and you are all 
done with this notebook!
'''