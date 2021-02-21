import http.server
import re
import socketserver


class Dictionnary:
  """
  The Dictionnary object contains all the words stored in a TRIE
  """
  def __init__(self):
    """
    The data structure
    self.next : a dict containing at most 26 nodes (26 letters)
    self.leaf : a boolean value to check if current node is a leaf
    """
    self.next={}
    # Indicator for terminal node (end of word)
    self.leaf=False

  def addWord(self,word):
    """
    Used to insert a word in the datastructure
    self.next : a dict containing at most 26 nodes (26 letters)
    self.leaf : a boolean value to check if current node is a leaf
    """
    i=0
    # Browse the datastructure and create new nodes if necessary
    while i < len(word):
      letter = word[i]
      if not letter in self.next:
        node = Dictionnary()
        self.next[letter] = node
      self = self.next[letter]
      # A final node (leaf) is tagged when last letter is reached
      if i == len(word) - 1:
        self.leaf = True
      else:
        self.leaf = False
      i += 1

  def browse(self, sstr, res):
    """
    Browse the data structure and store the leaf in res
    sstr : the search prefix string
    res : list used to store the result
    """
    if self.leaf and len(res) < 4:
      res.append(sstr)
    # Limit the result to 4 strings
    if len(res) == 4:
      return
    for i in self.next:
      self.next[i].browse(sstr + i, res)

  def autocomplete(self, pstr):
    """
      Used to browse the data structure and store the leaf in res
      pstr : the search prefix string
      res : list used to store the result
    """
    l = []
    i = 0
    # check if the search string exists
    while i < len(pstr):
      letter = pstr[i]
      if letter in self.next:
        self = self.next[letter]
      else:
        return l
      i += 1
    # if prefix exists, find all the leaves
    self.browse(pstr, l)
    return l 

class MyHttpServer(http.server.SimpleHTTPRequestHandler):

  def do_GET(self):

    self.send_response(200)
    self.send_header("Content-type", "text/html")
    self.end_headers()

    # Extract query value
    match = re.search('/autocomplete\?query=(.*)', self.path, re.IGNORECASE)

    if not match:
      print("Query : not found")
      return

    searchToken = match.group(1)

    print("Searching for {}".format(searchToken))

    global dic
    res = dic.autocomplete(searchToken)

    print(res)
    self.wfile.write(bytes(', '.join(res), "utf8"))

    return


# Open and read the dictionnary
f = open('dic', 'r')
fileContent = f.readlines()

# Initiate dictionnary class
dic = Dictionnary()

# Fill the dictionnary with non case sensitive data
for line in fileContent:
  dic.addWord(line.lower().strip())

# Create an object of the http server
handler_object = MyHttpServer

PORT = 8000
my_server = socketserver.TCPServer(("", PORT), handler_object)
print("Listening on port {}".format(PORT))

# Star the server
my_server.serve_forever()
