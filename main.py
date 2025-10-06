import random

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

edge_positions = { # stores the side order of each edge position, the sequence must match the one given in edge_colors
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

corner_colors = { # stores the color order of each corner in its solved state, the sequence of colors must be in clockwise order from one color to the next
    0: ("W","R","G"),
    1: ("W","B","R"),
    2: ("W","O","B"),
    3: ("W","G","O"),
    4: ("Y","G","R"),
    5: ("Y","R","B"),
    6: ("Y","B","O"),
    7: ("Y","O","G")
}

corner_positions = { # stores the side order of each corner position, the sequence must match the one given in corner_colors
    0: ("U","R","F"),
    1: ("U","B","R"),
    2: ("U","L","B"),
    3: ("U","F","L"),
    4: ("D","F","R"),
    5: ("D","R","B"),
    6: ("D","B","L"),
    7: ("D","L","F"),
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
        mapping of rotations for edges and corners are in edge_rots and corner_rots
        How the function works:
        first, goes through all edges and corners to be looped through, and gets the each piece and its orientation.
        second, it puts each piece in its new position, and adjusts the order of the orientations to match the new positions
        third, it goes through each piece again and adjusts its orientation as needed.
        """
        
        # step 1
        new_edges = []
        edge_ori_pos = []
        for i in edge_rots[side] if CCW else reversed(edge_rots[side]):
            edge_ori_pos.append(edge_positions[i].index(sides[side][0]))
            new_edges.append(i)
        
        new_corners = []
        corner_ori_pos = []
        for i in corner_rots[side] if CCW else reversed(corner_rots[side]):
            corner_ori_pos.append(corner_positions[i].index(sides[side][0]))
            new_corners.append(i)

        # step 2
        edge_ori_pos[0], edge_ori_pos[1], edge_ori_pos[2], edge_ori_pos[3] = edge_ori_pos[1], edge_ori_pos[2], edge_ori_pos[3], edge_ori_pos[0]
        self.edges[new_edges[0]],self.edges[new_edges[1]],self.edges[new_edges[2]],self.edges[new_edges[3]] = self.edges[new_edges[1]],self.edges[new_edges[2]],self.edges[new_edges[3]],self.edges[new_edges[0]]
        
        corner_ori_pos[0], corner_ori_pos[1], corner_ori_pos[2], corner_ori_pos[3] = corner_ori_pos[1], corner_ori_pos[2], corner_ori_pos[3], corner_ori_pos[0]
        self.corners[new_corners[0]],self.corners[new_corners[1]],self.corners[new_corners[2]],self.corners[new_corners[3]] = self.corners[new_corners[1]],self.corners[new_corners[2]],self.corners[new_corners[3]],self.corners[new_corners[0]]

        # step 3
        for i,item in enumerate(edge_rots[side] if CCW else reversed(edge_rots[side])):
            self.edges[item][1] = (edge_ori_pos[i] + edge_positions[item].index(sides[side][0]) + self.edges[item][1] ) % 2
        for i,item in enumerate(corner_rots[side] if CCW else reversed(corner_rots[side])):
            self.corners[item][1] = ( corner_ori_pos[i] - corner_positions[item].index(sides[side][0]) +  self.corners[item][1]) % 3
    
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
    def scramble(self, turns = 30):
        """
        scrambles the cube by making as many random turns as given in the input
        outputs a string sequence with the scramble
        """
        seq = ""
        for i in range(turns):
            turn = random.randint(0,5)
            drtn = bool(random.randint(0,1))
            seq += (sides[turn][0] + ("' " if drtn else " "))
            self.rotate(turn,drtn)
        return '" ' + seq + '"'
    def str_to_list(self,s):
        """
        takes a string with a list of turns, and outputs a list with each turns side and whether it is counter clockwise or clockwise
        """
        l = []
        for i in range(len(s)):
            for j in range(6):
                if s[i] in sides[j]:
                    if s[i + 1] == "'":
                        l.append((j,True))
                        i += 1
                    else:
                        l.append((j,False))
                    break
        return l
    def list_to_str(self,l):
        """
        takes a list with a set of turns and outputs a string with each turn in proper notation
        """
        s = '" '
        for i in range(len(l)):
            s += (sides[l[i][0]][0]) + ( "' " if l[i][1] else " " )
        s += '"'
        return s
    def make_moves(self, moves):
        if type(moves) == str:
            moves = str_to_list(moves)
        for i in range(len(moves)):
            rotate(moves[i][0],moves[i][1])
            
    def solve(self):
        """
        uses the beginners algorithm to solve the cube
        """
        turns = '" '
        # solve the white cross
        for i in range(4):


c = Cube()
c.scramble()
c.solve()
c.visualize()
