edge_rots = { # rotation mapping of edges. the key is the side, and each edge whose positon is in the tuple moves to the next position in the tuple (last one goes to first one)
    0: (0,3,2,1),
    1: (0,4,8,7),
    2: (1,5,9,4),
    3: (2,6,10,5),
    4: (3,7,11,6),
    5: (8,9,10,11)
}

corner_rots = { # rotation mapping of corners. the key is the side, and each corner whose positon is in the tuple moves to the next position in the tuple (last one goes to first one)
    0: (0,3,2,1),
    1: (0,4,7,3),
    2: (0,1,5,4),
    3: (1,2,6,5),
    4: (2,3,7,6),
    5: (4,5,6,7)
}

edge_colors = { # stores the color order of each edge in its solved state
    0: ("W","G"),
    1: ("W","R"),
    2: ("W","B"),
    3: ("W","O"),
    4: ("G","R"),
    5: ("R","B"),
    6: ("B","O"),
    7: ("O","G"),
    8: ("Y","G"),
    9: ("Y","R"),
    10: ("Y","B"),
    11: ("Y","O")
}

edge_positions = { # stores the side order of each edge position
    0: ("U","F"),
    1: ("U","R"),
    2: ("U","B"),
    3: ("U","L"),
    4: ("F","R"),
    5: ("R","B"),
    6: ("B","L"),
    7: ("L","F"),
    8: ("D","F"),
    9: ("D","R"),
    10: ("D","B"),
    11: ("D","L")
}

corner_colors = { # stores the color order of each corner in its solved state
    0: ("W","G","R"),
    1: ("W","R","B"),
    2: ("W","B","O"),
    3: ("W","O","G"),
    4: ("Y","R","G"),
    5: ("Y","B","R"),
    6: ("Y","B","O"),
    7: ("Y","G","O")
}

corner_positions = { # stores the side order of each corner position
    0: ("U","F","R"),
    1: ("U","R","B"),
    2: ("U","B","L"),
    3: ("U","L","F"),
    4: ("D","F","R"),
    5: ("D","B","R"),
    6: ("D","B","L"),
    7: ("D","F","L")  
}

sides = { # each side id and its orientation and color
    0: ("U","W"),
    1: ("F","G"),
    2: ("R","R"),
    3: ("B","B"),
    4: ("L","O"),
    5: ("D","Y")
}

piece_order = { # the order each piece should be printed out for each side in the visualize function (True/False is for if its an edge or not; int is the id in its respective list)
    0: ((False,2),(True,2),(False,1),(True,3),(True,1),(False,3),(True,0),(False,0)),
    1: ((False,3),(True,0),(False,0),(True,7),(True,4),(False,7),(True,8),(False,4)),
    2: ((False,0),(True,1),(False,1),(True,4),(True,5),(False,4),(True,9),(False,5)),
    3: ((False,6),(True,10),(False,5),(True,6),(True,5),(False,2),(True,2),(False,1)),
    4: ((False,2),(True,3),(False,3),(True,6),(True,7),(False,6),(True,11),(False,7)),
    5: ((False,7),(True,8),(False,4),(True,11),(True,9),(False,6),(True,10),(False,5))
}

class Cube:
    def __init__(self,edges=None,corners=None):
        """
        this class represents the rubiks cube. the two lists represent the position and orientation of the rubiks cube.
        each item in each list represents one piece. the sublists show the id and rotation of each piece.
        A piece is in its correct location if its 0th value is equal to its index (so piece 0 in edges is in the correct spot if edges[0][0] = 0).
        A piece is in the correct orientation if its 1st value is 0. Edges can have 2 possible orientations, so this number could be 0 or 1. Corners can be 0, 1, or 2.
        """
        if edges == None: # if edges is not passed, put all edges in order and oriented correctly
            edges = [[0,0],[1,0],[2,0],[3,0],
            [4,0],[5,0],[6,0],[7,0],
            [8,0],[9,0],[10,0],[11,0]]
        if corners == None: # if corners is not passed, put all corners in order and oriented correctly
            corners = [[0,0],[1,0],[2,0],[3,0],
            [4,0],[5,0],[6,0],[7,0]]
        self.edges = edges
        self.corners = corners
    def rotate(self,side,CCW):
        """
        rotates a side of the cube.
        side chooses which side is rotated. see sides for mapping
        CCW chooses whether it should be a clockwise or counterclockwise rotation. True = CCW, False = CW
        Each rotation does 4 basic things. first, reorient all edges. every affected edge wil be toggled between 0 and 1.
        second, reorient all corners. CCW increases orientation from 0 to 1, 1 to 2, and 2 to 0. CW does the opposite.
        third, reorganize the edges array. 4 edges should be moved into each others positon in a loop (edge 1 -> edge 2 -> edge 3 -> edge 4 -> edge 1; it would go in opposite order for counter clockwise)
        fourth, reorganize the corners array, it follows a similar pattern to the edges array
        mapping of rotations for edges and corners are in edge_rots and corner_rots
        """
        #step 1:
        new_edges = []
        for i in edge_rots[side] if CCW else reversed(edge_rots[side]):
            self.edges[i][1] = (self.edges[i][1] + (1 if CCW else -1)) % 2
            new_edges.append(i) # save this so we dont have to do a second loop
        #step 2:
        new_corners = []
        for i in corner_rots[side] if CCW else reversed(corner_rots[side]):
            self.corners[i][1] = (self.corners[i][1] + (1 if CCW else -1)) % 3
            new_corners.append(i) # save this so we dont have to do a second loop
        #step 3:
        self.edges[new_edges[0]],self.edges[new_edges[1]],self.edges[new_edges[2]],self.edges[new_edges[3]] = self.edges[new_edges[1]],self.edges[new_edges[2]],self.edges[new_edges[3]],self.edges[new_edges[0]]
        #step 4:
        self.corners[new_corners[0]],self.corners[new_corners[1]],self.corners[new_corners[2]],self.corners[new_corners[3]] = self.corners[new_corners[1]],self.corners[new_corners[2]],self.corners[new_corners[3]],self.corners[new_corners[0]]

    def visualize(self):
        """
        prints out a text visualization of the state of the cube.
        It is a flattened cube in th shape if a cross, and each piece face is given its color as W,G,R,B,O, or Y
        """
        def get_color(edge,piece,pos,ori,side):
            """
            get the color of a specific side of a piece
            edge is a boolean, True if the piece is an edge, false if corner
            piece is the piece of the piece (0th item in its list)
            pos is the position of the piece (its position in the list)
            ori is the orientation of the piece
            side is the side to check the color for

            steps to get the color of a side of a piece:
            first, look at the pieces position in its position dict. find the value in the tuple matching the side, and add its index to the orientation mod possible orientations (2 for edges, 3 for corners)
            second, in the colors dict, go to the key of the piece, and return the color with the same index as the result of the first step
            """
            
            # step 1
            i = (( edge_positions[pos] if edge else corner_positions[pos] ).index(sides[side][0]) + ori ) % ( 2 if edge else 3 )
            # step 2
            return ( edge_colors[piece] if edge else corner_colors[piece] )[i]
        def get_lines(side):
            """ 
            takes in side, which cooresponds to the sides dict. outputs a list of 3 strings, each of which have 3 characters, and coorespond to a side of the cube
            """
            lines = []
            for i in range(3):
                line = ""
                for j in range(3):
                    edge = piece_order[side][i*3+j - ( 0 if i*3+j < 4 else 1 )][0]
                    pos = piece_order[side][i*3+j - ( 0 if i*3+j < 4 else 1 )][1]
                    piece = self.edges[pos][0] if edge else self.corners[pos][0]
                    ori = self.edges[pos][1] if edge else self.corners[pos][1]
                    line += get_color(edge,piece,pos,ori,side) if i*3 + j != 4 else sides[side][1]
                lines.append(line)
            return lines
        white = get_lines(0)
        green = get_lines(1)
        red = get_lines(2)
        blue = get_lines(3)
        orange = get_lines(4)
        yellow = get_lines(5)
        for i in range(3):
            print("    " + white[i])
        for i in range(3):
            print(orange[i] + " " + green[i] + " " + red[i])
        for i in range(3):
            print("    " + yellow[i])
        for i in range(3):
            print("    " + blue[i])
        print()

            
x = Cube()
x.visualize()
x.rotate(1,True)
x.rotate(1,True)
x.rotate(1,True)
x.rotate(1,True)
x.visualize()