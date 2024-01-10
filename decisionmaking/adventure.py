# Author: Minh Nguyen
# Date: 11/08/2023
# Purpose: Adventure.py loading the story.txt file and parsing it and start game play
# after loading the story data into the graph.

from vertex import Vertex

def parse_line(line):
    section_split = line.split("|")
    vertex_name = section_split[0].strip()

    adjacent_vertices = section_split[1].strip().split(",")

    # add all except empty strings
    adjacent = []
    for a in adjacent_vertices:
        if a:
            adjacent.append(a.strip())

    text = section_split[2].strip()

    return vertex_name, adjacent, text


def load_story(filename):

    vertex_dict = {}

    # Read the lines in the file into a list of lines:
    file = open(filename, "r")

    for l in file:

        # if this is a line in the correct format:
        if len(l.split("|")) == 3:
            vertex_name, adjacent_vertices, text = parse_line(l)

            # print("vertex " + vertex_name)
            # print(" adjacent:  " + str(adjacent_vertices))
            # print(" text:  " + text)

            # create a graph vertex here and add it to the dictionary
            vertex_dict[vertex_name] = Vertex(adjacent_vertices, text)

    file.close()

    return vertex_dict

story_dict = load_story("story.txt")


def play_game():

    # define variables
    # current_vertex - NONE
    # user_input = input()

    # set current vertex to the START vertex - dict["START] = start vertex
    # while loop [adj.list is NOT empty]
        # index = ord(user_input) - ord("a")
        # current_vertex = current_vertex.adj_list[index]

    user_input = input("Press s to start: ")
    # start the game
    if user_input == "s":

        current_vertex = story_dict["START"] # Grab the vertex "START" from the dictionary

        while len(current_vertex.adjacent) != 0: # get the list of choices by a while loop that repeats
            # until you reach a vertex with no outgoing links then the program ends

            user_input = input(current_vertex.data + "\n") # allow the user to input a value
            # like a, b, or c using the Python input function

            index = ord(user_input) - ord("a") # convert a char to a number using ord

            # grab the next vertex from the dictionary
            current_vertex = story_dict[current_vertex.adjacent[index]]

        print(current_vertex.data) # print the results of your choices

play_game() # allows you to play the game