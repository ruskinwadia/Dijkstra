# input
graph = {
    'a': ['b', 'c', 'd'],
    'b': ['a', 'e', 'f'],
    'c': ['a', 'g'],
    'd': ['a', 'h'],
    'e': ['b', 'i'],
    'f': ['b', 'i'],
    'g': ['c', 'j'],
    'h': ['d', 'k'],
    'i': ['e', 'f', 'k', 'h'],
    'j': ['g', 'k'],
    'k': ['i', 'j', 'h']
}

nodelist = []  # List of all nodes (objects)
standby = []  # list of standby nodes
finishedlist = []  # checked all links
path = []  # Final path


class node:
    def __init__(self, data=None):
        self.data = data
        self.links = []
        self.distance = None
        self.distancefrom = None


def distances(start):  # Setting distances for each node as 1 by default
    for each in nodelist:
        # if each.data == 'i':
        #      each.distance = 4
        # elif each.data == 'h':
        #      each.distance = 3
        if each.data != start:
            # print(each.data)
            each.distance = 1
        else:
            each.distance = 0


def redundancyremov():  # Remove redundancies
    for bud in finishedlist:
        if standby.__contains__(bud):
            #print("Standremov: ", bud.data)
            standby.remove(bud)


def prioritycheck(startnode, end):

    # Printing standby and visited nodes

    # print("standby: ", end="")
    # for s in standby:
    #     print(s.data, end=" ")
    # print()

    # print("Finished: ", end="")
    # for bud in finishedlist:
    #     print(bud.data, end=" ")
    # print()

    redundancyremov()

    # Rearranging
    standby.sort(key=lambda x: x.distance)
    # print("Standby sorted: ", end="")
    # for s in standby:
    #     print(s.data, end=" ")
    # print("\n")

    for points in standby:
        # for link in points.links:
        if points not in finishedlist:
            # print(points.data," ",link)
            linkchecks(points, end)


def linkchecks(startnode, end):   # Starting traversal
    #print("Startnode: ", startnode.data, "Distance: ", startnode.distance)
    for link in range(startnode.links.__len__()):  # Each link in the node
        # print(type(startnode.links[link].data))
        for obj in startnode.links[link].data:
            # print("Link->",obj)
            for linknode in nodelist:
                if linknode.data == obj:  # Finding the node in nodelist == link of current node
                    if linknode not in standby:
                        if linknode not in finishedlist:
                            # print("Free link-> ", linknode.data)
                            linknode.distance += startnode.distance      # Calculating distances of nodes

                            linknode.distancefrom = startnode
                            # print(linknode.data, " -> ", linknode.distancefrom," ", linknode.distance, end = "\n\n")
                            # print(linknode.data)
                            standby.append(linknode)
    finishedlist.append(startnode)
    prioritycheck(startnode, end)


def traverse(start, end):
    for a in nodelist:  # Acquire index of start element from list
        if(a.data == start):  # Strings match
            startindex = nodelist.index(a)
            # print(a.data, "-> Index: ", startindex)

    startnode = nodelist[startindex]
    # print("StartNode: ", startnode.data)
    distances(start)
    linkchecks(startnode, end)


def createnodes():      # Creating nodes
    for pt in graph:
        nodelist.append(node(pt))


def createlinks(yes):  # Creating links
    yes = yes

    for a in range(nodelist.__len__()):
        currentnode = nodelist[a]   # Each node
        # print(currentnode.data," -> ",graph[currentnode.data]) #Links of each node
        listoflinks = graph[currentnode.data]

        for b in range(listoflinks.__len__()):
            for nl in nodelist:
                if nl.data == listoflinks[b]:
                    # print(nl.data)
                    nodelist[a].links.append(nl)
                    # print(type(nl))
                # print(nodelist[a].links[b])

    # Printing all nodes with links
    if(yes):
        for a in nodelist:
            for b in range(a.links.__len__()):
                print(a.data, " -> ", a.links[b].data)


def shownodesandlinks():  # Display
    nodelist.sort(key=lambda x: x.distance)
    for a in nodelist:
        if a.distancefrom != None:
            print(a.distancefrom.data, " to ", a.data, " is: ", a.distance)
        else:
            print(a.data, " is the start")


def findfinalpath(start, end):  # Adding nodes to path list
    for nodes in finishedlist:
        if nodes.data == end:
            # print("Node: ", nodes.data)
            endnode = nodes
            break
            # print(endnode)

    # print(endnode.data, " ", endnode.distance)
    while (True):
        # print("Not zero: ", endnode.data)
        path.append(endnode)

        if endnode.data == start:
            break
        endnode = endnode.distancefrom


def printpath():  # Print the path
    path.reverse()
    for a in path:
        print(a.data, end=" ")
    print("\n\n")


def pathfind(start, end):       # Main function
    createnodes()
    createlinks(False)  # True or False for showing all links
    traverse(start, end)
    # shownodesandlinks()
    findfinalpath(start, end)
    print("\n\nThe path from {} to {} is: ".format(start, end), end="")
    printpath()


pathfind('a', 'k')
