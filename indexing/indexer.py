# -- extracting the first words 
def extract_and_match(words_list, matching_words_list):
    # Dictionary to hold the matches
    matches_dict = {}

    for index, sentence in enumerate(words_list):
        # Split sentence into words
        words = sentence.split()

        # Extract word groups
        first_word = ' '.join(words[:1])
        first_two_words = ' '.join(words[:2])
        first_three_words = ' '.join(words[:3])

        # Check for matches and update the dictionary
        for match in matching_words_list:
            if match in [first_word, first_two_words, first_three_words]:
                # If the match is found, append the index to the list of indices for that match
                if match not in matches_dict:
                    matches_dict[match] = [index]
                else:
                    matches_dict[match].append(index)

    return matches_dict

# -- After mapping the first few, I wrap the rest. 
def fill_indices_to_n_correctly(matching_dict, n):
    updated_dict = {}
    keys = list(matching_dict.keys())  # List of keys for ordered access

    for i, key in enumerate(keys):
        # Start index is the original index for this key
        start_index = matching_dict[key][0]

        # Determine the end index for this sequence
        if i + 1 < len(keys):  # If there's a next key, end before its start index
            next_key_start = matching_dict[keys[i+1]][0]
            end_index = min(next_key_start, n + 1)
        else:  # For the last key, go up to n
            end_index = n + 1

        # Assign the sequence of indices to the current key
        updated_dict[key] = list(range(start_index, end_index))

    return updated_dict
