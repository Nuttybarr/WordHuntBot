
import serial
from platform import python_branch
import pyautogui
import time
from more_itertools import sort_together

#arduino = serial.Serial(port='/dev/cu.usbmodem11301', baudrate=115200, timeout=.1)



class Point:
    x = 0
    y = 0
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

POINTS = [
          [Point(504, 320), Point(604, 320), Point(704, 320), Point(804, 320)],
          [Point(504, 420), Point(604, 420), Point(704, 420), Point(804, 420)],
          [Point(504, 520), Point(604, 520), Point(704, 520), Point(804, 520)],
          [Point(504, 620), Point(604, 620), Point(704, 620), Point(804, 620)]
         ]

# def determineSwipe(point1, point2):
#     #x is row, y
#     #0 up
#     #1 upright
#     #2 right
#     #3 downright   
#     #4 down
#     #5 downleft
#     #6 left
#     #7 upleft
#     i is colf(point2.x > point1.x): 
#         if(point2.y > point1.y): 
#             return 3
#         if(point1.y == point2.y): 
#             return 2
#         else:
#             return 1
#     elif(point1.x == point2.x): 
#         if(point2.y > point1.y):
#             return 4
#         else:
#             return 0
#     else:
#         if(point2.y > point1.y): 
#             return 5
#         if(point1.y == point2.y):
#             return 6
#         else:
#             return 7

# def write_read(x):
#     arduino.write(bytes(str(x), 'utf-8'))
#     time.sleep(0.05)
#     data = arduino.readline()
#     return data

def swipeRel(point1, point2, wait):
    #print(write_read(determineSwipe(point1, point2)))
    #pyautogui.moveRel(point2.x - point1.x, point2.y - point1.y, wait)
    pyautogui.dragRel(point2.x - point1.x, point2.y - point1.y, wait, button="left")

def swipeWord(swipes, wait= 0):
    #print(POINTS[swipes[0][0]][swipes[0][1]])
    point1 = POINTS[swipes[0][0]][swipes[0][1]]
    pyautogui.moveTo(point1.x, point1.y, wait)
    #pyautogui.click()
    #pyautogui.mouseDown()
    for i in range(len(swipes)-1):
        point1 = POINTS[swipes[i][0]][swipes[i][1]]
        point2 = POINTS[swipes[i+1][0]][swipes[i+1][1]]
        swipeRel(point1, point2, wait)
        #print(point1.x, point1.y, " --> ", point2.x, point2.y)
    #pyautogui.mouseUp()



class TrieNode:
 
    # Trie node class
    def __init__(self):
        self.children = [None] * 26
 
        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False
 
M = 4
N = 4
ans = []
totalSwipes = []

class Boogle:
 
    # Trie data structure class
    def __init__(self):
        self.root = self.getNode()
 
    def getNode(self):
 
        # Returns new trie node (initialized to NULLs)
        return TrieNode()
 
    def _charToIndex(self, ch):
 
        # private helper function
        # Converts key current character into index
        # use only 'A' through 'Z' and upper case
        return ord(ch) - ord('A')
 
    def insert(self, key):
 
        # If not present, inserts key into trie
        # If the key is prefix of trie node,
        # just marks leaf node
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
 
            # if current character is not present
            if not pCrawl.children[index]:
 
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]
            # print('h', self.root.children)
 
        # mark last node as leaf
        pCrawl.isEndOfWord = True
 
 
def is_Safe(i, j, vis):
    return 0 <= i < M and 0 <= j < N and not vis[i][j]
 

def search_word(root, boggle, i, j, vis, string, swipes):

    if root.isEndOfWord and string not in ans:
        ans.append(string)
        totalSwipes.append(swipes)
 
    if is_Safe(i, j, vis):
        vis[i][j] = True
        for K in range(26):
            if root.children[K] is not None:
                ch = chr(K+ord('A'))
                # print(i, j, " : ", ch)
                # Recursively search reaming character of word
                # in trie for all 8 adjacent cells of boggle[i][j]
                if is_Safe(i + 1, j + 1, vis) and boggle[i + 1][j + 1] == ch:
                    search_word(root.children[K], boggle,
                                i + 1, j + 1, vis, string + ch, swipes +[(i+1,j+1)])
                if is_Safe(i, j + 1, vis) and boggle[i][j + 1] == ch:
                    search_word(root.children[K], boggle,
                                i, j + 1, vis, string + ch, swipes + [(i,j+1)])
                if is_Safe(i - 1, j + 1, vis) and boggle[i - 1][j + 1] == ch:
                    search_word(root.children[K], boggle,
                                i - 1, j + 1, vis, string + ch, swipes + [(i-1,j+1)])
                if is_Safe(i + 1, j, vis) and boggle[i + 1][j] == ch:
                    search_word(root.children[K], boggle,
                                i + 1, j, vis, string + ch, swipes + [(i+1,j)])
                if is_Safe(i + 1, j - 1, vis) and boggle[i + 1][j - 1] == ch:
                    search_word(root.children[K], boggle,
                                i + 1, j - 1, vis, string + ch, swipes + [(i+1,j-1)])
                if is_Safe(i, j - 1, vis) and boggle[i][j - 1] == ch:
                    search_word(root.children[K], boggle,
                                i, j - 1, vis, string + ch, swipes + [(i,j-1)])
                if is_Safe(i - 1, j - 1, vis) and boggle[i - 1][j - 1] == ch:
                    search_word(root.children[K], boggle,
                                i - 1, j - 1, vis, string + ch, swipes + [(i-1,j-1)])
                if is_Safe(i - 1, j, vis) and boggle[i - 1][j] == ch:
                    search_word(root.children[K], boggle,
                                i - 1, j, vis, string + ch, swipes + [(i-1,j)])
        vis[i][j] = False
 
 
def char_int(ch):
   
    # private helper function
    # Converts key current character into index
    # use only 'A' through 'Z' and upper case
    return ord(ch) - ord('A')
 
 
def findWords(boggle, root):
   
    # Mark all characters as not visited
    visited = [[False for i in range(N)] for i in range(M)]
 
    pChild = root
 
    string = ""
 
    # traverse all matrix elements
    for i in range(M):
        for j in range(N):
            # we start searching for word in dictionary
            # if we found a character which is child
            # of Trie root
            if pChild.children[char_int(boggle[i][j])]:
                # print('h')
                string = string + boggle[i][j]
                swipes = [(i,j)]
                # print(i, j, " : ", string)
                search_word(pChild.children[char_int(boggle[i][j])],
                            boggle, i, j, visited, string, swipes)
                string = ""
    #ans2 = sorted(ans, key=len, reverse= True)

    
    



dictionary = []

with open("WordHuntWords.txt") as words:
    dictionary = words.read().splitlines()

# root Node of trie
t = Boogle()
 
# insert all words of dictionary into trie
n = len(dictionary)
for i in range(n):
    t.insert(dictionary[i])

root = t.root
seq = input("What is the board?")
while(len(seq) != 16):
    seq = input("What is the board?")

board = []
index = 0
for i in range(4):
    row = []
    for j in range(4):
        row.append(seq[index])
        index+=1
    board.append(row)

    
# board = [['T', 'K', 'A', 'T'],
#           ['O', 'C', 'E', 'F'],
#           ['A', 'G', 'S', 'W'],
#           ['R', 'O', 'U', 'R']]
 
# print(root.children)
findWords(board, root)



time.sleep(3)
print("go")

ans2, totalSwipes2 = sort_together([ans, totalSwipes], key=len, reverse= True)

for j in range(len(ans2)):
        print(ans2[j], " : ", totalSwipes2[j])

for i in range(len(ans2)):
    print("#", i, " Getting ", ans2[i], " : ", totalSwipes2[i])
    swipeWord(totalSwipes2[i], 0)
    




 
