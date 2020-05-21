# Create node for RouteTrie
class RouteTrieNode:
    def __init__(self,default_handler):
        self.children = {}
        self.handler = default_handler

    def insert(self,word,default_handler):
        if word not in self.children:
            self.children[word] = RouteTrieNode(default_handler)


# Create RouteTrie to store our routes and their associated handlers
class RouteTrie:
    def __init__(self,root_handler,default_handler):
        self.root = RouteTrieNode(root_handler)
        self.default_handler = default_handler # place holder for default handler string

    def insert(self, path_list, handler):
        current_node = self.root
        for word in path_list:
            current_node.insert(word, self.default_handler)
            current_node = current_node.children[word]
        current_node.handler = handler
        return

    def find(self,path_list):
        current_node = self.root
        for word in path_list:
            if word in current_node.children:
                current_node = current_node.children[word]
            else:
                return self.default_handler
        return current_node.handler


# The Router class to wrap the Trie tree and handle 
class Router:
    def __init__(self,root_handler,default_handler):
        self.route_trie = RouteTrie(root_handler,default_handler)

    def add_handler(self, path, handler):
        path_list = self.split_path(path)
        self.route_trie.insert(path_list,handler)
        

    def lookup(self,path):
        path_list = self.split_path(path)
        return self.route_trie.find(path_list)

    def split_path(self,path):
        output_list = list()
        string = ''
        for char in path:
            if char == '/' and string == '':
                continue
            if char == '/':
                output_list.append(string)
                string = ''
                continue
            string += char
        if char != '/':
            output_list.append(string)
        return output_list

# Testing
router = Router("Root Handler", "404 page not found!")
root = "/"
path1 = "/home/Dan/Udacity/project"
path2 = "/home/Dan/school"
path3 = "/etc/proc"
handler1 = "Dan project handler"
handler2 = "Dan school handler"
handler3 = "Proc handler"
router.add_handler(path1,handler1)
router.add_handler(path2,handler2)
router.add_handler(path3,handler3)

print("Test 1: lookup for the root handler")
print(router.lookup("/"))
# Expected Output: Root Handler
print("--------------------------------------\n")

print("Test 2: lookup for a handler")
print(router.lookup("/home/Dan/Udacity/project"))
# Expected Output: Dan project handler
print("--------------------------------------\n")

print("Test 3: Handle sailing slashes")
print(router.lookup("/home/Dan/Udacity/project/"))
# Expected Output: Dan project handler
print("--------------------------------------\n")

print("Test 4: lookup for another handler")
print(router.lookup("/home/Dan/school"))
# Expected Output: Dan school handler
print("--------------------------------------\n")

print("Test 5: lookup for another handler")
print(router.lookup("/etc/proc"))
# Expected Output: Proc handler
print("--------------------------------------\n")

print("Test 6: lookup for not found handler")
print(router.lookup("/etc"))
# Expected Output: 404 page not found!
print("--------------------------------------\n")

print("Test 7: lookup for not found handler")
print(router.lookup("/home/Tom"))
# Expected Output: 404 page not found!
print("--------------------------------------\n")