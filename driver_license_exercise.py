# You have to get a new driver's license and you show up at the office at the same time as other 4 people.
# The office says that they will see everyone in alphabetical order and it takes 20 minutes for them to process each
# new license. All of the agents are available now and they can each see one customer at a time. How long will it take
# for you to walk out of the office with your new license?

# Task: Given everyone's name that showed up at the same time, determine how long it will take to get your new license.
# Input: a string of your name, an integer of the number of agents available and a string of the other four names
# separated by spaces.
# Output: an integer of the number of minutes that it will take to get your license.

def calculate_time_spent(name, people, agents):
    """Method to calculate the time spent based on available agents and people in front of you"""

    time_per_customer = 20
    people = people.split()
    people.append(your_name)
    people.sort()
    queue_position = people.index(name)

    # calculating the time based on your position in queue and available agents
    if queue_position < agents:
        time_spent = time_per_customer
    elif queue_position == agents:
        time_spent = 2 * time_per_customer
    else:
        time_spent = (queue_position // agents + 1) * time_per_customer

    message = f'The time you will spend is {time_spent} minutes.'
    return message


available_agents = int(input('How many agents are available? -> '))
your_name = input('Please type your name here -> ')
other_people = input('Please type the other 4 names separated by space -> ')

print(calculate_time_spent(your_name, other_people, available_agents))
