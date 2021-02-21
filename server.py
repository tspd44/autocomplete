import http.server
import re
import socketserver


class Dictionnary:

  def __init__(self):
    self.next={}
    # Indicator for terminal node (end of word)
    self.leaf=False

  def addWord(self,word):
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

  def browseAndPrint(self, sstr, res):
    if self.leaf and len(res) < 4:
      res.append(sstr)
    if len(res) == 4:
      return
    for i in self.next:
      self.next[i].browseAndPrint(sstr + i, res)

  def autocomplete(self, sstr):
    l = []
    i = 0
    # check if the search string exists
    while i < len(sstr):
      letter = sstr[i]
      if letter in self.next:
        self = self.next[letter]
      else:
        return l
      i += 1
    # if prefix exists, print all the leaves
    self.browseAndPrint(sstr, l)
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
    print(dic.autocomplete(searchToken))

    return


# Open and read the dictionnary
f = open('dic2', 'r')
fileContent = f.readlines()

# Initiate dictionnary class
dic = Dictionnary()
# Fill the dictionnary
for line in fileContent:
  dic.addWord(line.strip())

# Create an object of the http server
handler_object = MyHttpServer

PORT = 8000
my_server = socketserver.TCPServer(("", PORT), handler_object)
print("Listening on port {}".format(PORT))

# Star the server
my_server.serve_forever()
