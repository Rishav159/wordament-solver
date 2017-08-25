from bottle import route,run,get,post,static_file,request
import json
import datetime
start = datetime.datetime.now()
import dawg
words = open('/usr/share/dict/american-english', 'r').read().splitlines()
d = dawg.DAWG(words)
cd = dawg.CompletionDAWG(words)

matrix = []
visited = []
n = 4
for i in range(n):
    visited.append([False for x in range(n)])
mem = {}

def do_word_exist(word):
    return rand() > 0.5

def is_in_range(i,j):
    if i < 0 or j < 0:
        return False
    if i >= n or j >= n:
        return False
    return True


def traverse(word,position,i,j):
    global mem
    words = []
    positions = []

    if len(word) > 2 and word.lower() in d and word.lower() not in mem:
        words.append(word)
        positions.append(list(position))
        mem[word.lower()] = True
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
    return [words,positions]

def solution():
    global mem
    words = []
    positions = []
    mem = {}
    print(matrix)
    for i in range(n):
        for j in range(n):
            visited[i][j] = True
            x = traverse(matrix[i][j],[i*n+j],i,j)
            words.extend(x[0])
            positions.extend(x[1])
            visited[i][j] = False
    return words,positions
points_array = {
'A':2,
'B':1,
'C':3,
'D':3,
'E':1,
'F':5,
'G':4,
'H':4,
'I':2,
'J':1,
'K':6,
'L':3,
'M':4,
'N':2,
'O':2,
'P':4,
'Q':1,
'R':2,
'S':2,
'T':2,
'U':4,
'V':6,
'W':1,
'X':1,
'Y':5,
'Z':8
}
def points(word):
    score = 0
    for letter in word:
        score += points_array[letter]
    return score
@get('/')
def index():
    return static_file('/index.html',root = './public')

@post('/solve')
def solve():
    global matrix
    r = request.body
    j = json.loads(str(r.getvalue(),'utf-8'))
    matrix = j['matrix']
    final_words,final_positions = solution()
    print(len(final_words))
    print(len(final_positions))
    final_words,final_positions = zip(*sorted(zip(final_words,final_positions), key = lambda x:points(x[0])))
    return json.dumps({'words': final_words, 'positions' : final_positions})
run(host='localhost',port = 3000)
