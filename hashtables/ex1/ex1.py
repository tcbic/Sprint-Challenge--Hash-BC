#  Hint:  You may not need all of these. Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)

# limit = weight limit
# weights = list of item weights
# length = length of the list of weights

def get_indices_of_item_weights(weights, length, limit):
    """
    Find the two values in the list of weights whose sum is equal to the limit.
    Return the indices of those two values.
    """
       
    # Create a hash table.
    ht = HashTable(16)

    for i in range(0, length):
        hash_table_insert(ht, weights[i], i)        

    # Traverse through weights...
    for i in range(0, length):
        # Use the complement as the key within the hash table and
        # the index as the value.
        complement = limit - weights[i]
        
        if hash_table_retrieve(ht, complement):
            # Returns the index of the complement in the hash table
            # and the current index.
            
            complement_index = hash_table_retrieve(ht, complement)
            return [complement_index, i]              

    return None

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

# EXAMPLE RUN TEST

# weights = [4, 6, 10, 15, 16]
# length = 5
# limit = 21

# print(get_indices_of_item_weights(weights, length, limit))

# output should be: [3, 1]