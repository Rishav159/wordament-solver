
import datetime
start = datetime.datetime.now()
import dawg
words = open('/usr/share/dict/american-english', 'r').read().splitlines()
d = dawg.DAWG(words)
cd = dawg.CompletionDAWG(words)

matrix = []
visited = []
n = int(input())
for i in range(n):
    matrix.append(list(input().split(' ')))
    visited.append([False for x in range(n)])

def do_word_exist(word):
    return rand() > 0.5

def is_in_range(i,j):
    if i < 0 or j < 0:
        return False
    if i >= n or j >= n:
        return False
    return True


def traverse(word,position,i,j):
    words = []
    positions = []
    # print('word is ')
    # print(word)
    # print('position is ')
    # print(position)
    if len(word) > 2 and word.lower() in d:
        words.append(word)
        positions.append(list(position))
    #Top-Left
    if is_in_range(i-1,j-1) and not visited[i-1][j-1]:
        new_word = word
        new_word += matrix[i-1][j-1]
        new_position = position
        new_position.append((i-1)*n + j-1)
        if cd.has_keys_with_prefix(new_word.lower()):
            visited[i-1][j-1] = True
            received_words,received_positions = traverse(new_word,new_position,i-1,j-1)
            words.extend(received_words)
            positions.extend(received_positions)
            visited[i-1][j-1] = False
        position.pop()
        # print("Back to "+word)
    #Top
    if is_in_range(i-1,j) and not visited[i-1][j]:
        new_word = word
        new_word += matrix[i-1][j]
        new_position = position
        new_position.append((i-1)*n + j)
        if cd.has_keys_with_prefix(new_word.lower()):
            visited[i-1][j] = True
            received_words,received_positions = traverse(new_word,new_position,i-1,j)
            words.extend(received_words)
            positions.extend(received_positions)
            visited[i-1][j] = False
        position.pop()
        # print("Back to "+word)
    #Top-Right
    if is_in_range(i-1,j+1) and not visited[i-1][j+1]:
        new_word = word
        new_word += matrix[i-1][j+1]
        new_position = position
        new_position.append((i-1)*n + j+1)
        if cd.has_keys_with_prefix(new_word.lower()):
            visited[i-1][j+1] = True
            received_words,received_positions = traverse(new_word,new_position,i-1,j+1)
            words.extend(received_words)
            positions.extend(received_positions)
            visited[i-1][j+1] = False
        position.pop()
        # print("Back to "+word)
    #Right
    if is_in_range(i,j+1) and not visited[i][j+1]:
        new_word = word
        new_word += matrix[i][j+1]
        new_position = position
        new_position.append((i)*n + j+1)
        if cd.has_keys_with_prefix(new_word.lower()):
            visited[i][j+1] = True
            received_words,received_positions = traverse(new_word,new_position,i,j+1)
            words.extend(received_words)
            positions.extend(received_positions)
            visited[i][j+1] = False
        position.pop()
        # print("Back to "+word)
    #Bottom-Right
    if is_in_range(i+1,j+1) and not visited[i+1][j+1]:
        new_word = word
        new_word += matrix[i+1][j+1]
        new_position = position
        new_position.append((i+1)*n + j+1)
        if cd.has_keys_with_prefix(new_word.lower()):
            visited[i+1][j+1] = True
            received_words,received_positions = traverse(new_word,new_position,i+1,j+1)
            words.extend(received_words)
            positions.extend(received_positions)
            visited[i+1][j+1] = False
        position.pop()
        # print("Back to "+word)
    #Bottom
    if is_in_range(i+1,j) and not visited[i+1][j]:
        new_word = word
        new_word += matrix[i+1][j]
        new_position = position
        new_position.append((i+1)*n + j)
        if cd.has_keys_with_prefix(new_word.lower()):
            visited[i+1][j] = True
            received_words,received_positions = traverse(new_word,new_position,i+1,j)
            words.extend(received_words)
            positions.extend(received_positions)
            visited[i+1][j] = False
        position.pop()
        # print("Back to "+word)
    #Bottom-Left
    if is_in_range(i+1,j-1) and not visited[i+1][j-1]:
        new_word = word
        new_word += matrix[i+1][j-1]
        new_position = position
        new_position.append((i+1)*n + j-1)
        if cd.has_keys_with_prefix(new_word.lower()):
            visited[i+1][j-1] = True
            received_words,received_positions = traverse(new_word,new_position,i+1,j-1)
            words.extend(received_words)
            positions.extend(received_positions)
            visited[i+1][j-1] = False
        position.pop()
        # print("Back to "+word)
    #Left
    if is_in_range(i,j-1) and not visited[i][j-1]:
        new_word = word
        new_word += matrix[i][j-1]
        new_position = position
        new_position.append((i)*n + j-1)
        if cd.has_keys_with_prefix(new_word.lower()):
            visited[i][j-1] = True
            received_words,received_positions = traverse(new_word,new_position,i,j-1)
            words.extend(received_words)
            positions.extend(received_positions)
            visited[i][j-1] = False
        position.pop()
        # print("Back to "+word)
    # print("Returning "+word)
    # print(arr)
    # print("Returning ")
    # print(words)
    # print(positions)
    return [words,positions]

def solution():
    words = []
    positions = []
    for i in range(n):
        for j in range(n):
            visited[i][j] = True
            x = traverse(matrix[i][j],[i*n+j],i,j)
            words.extend(x[0])
            positions.extend(x[1])
            visited[i][j] = False
    return words,positions
final_words,final_positions = solution()

final_words,final_positions = zip(*sorted(zip(final_words,final_positions), key = lambda x:len(x[0])))
for word,position in zip(final_words,final_positions):
    print(word)
    print(position)
# final_words = list(set(final_words))
# # print(final_words)
# final_words.sort(key = lambda x:len(x))
# for word in final_words:
#     print(word)
end = datetime.datetime.now()
diff = end-start
print("Calculated in : " + str(diff.total_seconds()) +" seconds.")
