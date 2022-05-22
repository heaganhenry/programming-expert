# Write a function that accepts two lists of integers and a target. The function should return all pairs of indices where the sum of their values equals the target.

def pairs_sum_to_target(list1, list2, target):
    pairs = []

    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] + list2[j] == target:
                pairs.append([i, j])

    return pairs