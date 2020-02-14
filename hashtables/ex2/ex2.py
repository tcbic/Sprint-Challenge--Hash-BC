#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)

# Notes from README

# source = starting airport
# destination = the next airport

# ticket of first flight: source = None
# ticket of last flight: source = None

# The route is comprised of just the destinations.

class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
    def __str__(self):
        return f"{self.source}, {self.destination}"   

def reconstruct_trip(tickets, length):

    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    # Place all the tickets into the hash table.
    
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)
    
    # The first destination has a key equal to NONE.
    start = "NONE"
    for i in range(0, length):
        if i == 0:

            route[i] = hash_table_retrieve(hashtable, start)
        else: 
            route[i] = hash_table_retrieve(hashtable, route[i-1])

    # Drop the last NONE.
    # Test won't pass without doing this.
    if route[-1] == "NONE":
        route.remove(route[-1])
    
    return route

# EXAMPLE RUN TEST

# ticket_1 = Ticket("PIT", "ORD")
# ticket_2 = Ticket("XNA", "SAP")
# ticket_3 = Ticket("SFO", "BHM")
# ticket_4 = Ticket("FLG", "XNA")
# ticket_5 = Ticket("NONE", "LAX")
# ticket_6 = Ticket("LAX", "SFO")
# ticket_7 = Ticket("SAP", "SLC")
# ticket_8 = Ticket("ORD", "NONE")
# ticket_9 = Ticket("SLC", "PIT")
# ticket_10 = Ticket("BHM", "FLG")

# tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
#             ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]

# length = len(tickets)


# print(reconstruct_trip(tickets, length))