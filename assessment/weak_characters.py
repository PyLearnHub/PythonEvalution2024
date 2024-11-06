def weak_characters(arr):
    weak = 0
    attack = 0
    defense = 0
    for i in range(3):
        for j in range(2):
            if arr[j][1] > attack:
                attack = arr[j][i]
                if arr[j][1] > defense:
                    defense = arr[j][1]
                    weak += 1
    return weak


print(weak_characters([[1, 5], [10, 4], [4, 3]]))


