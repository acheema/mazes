Maze problem

Given a file with a maze in the format
##########
X  #     #
#  #  #  #
#     #  O
##########

where the maze begins at X and ends at O
and the only valid spots are spaces,
ouput the shortest valid path filled in
with +s as seen below.

##########
X++# ++++#
# +# +# +#
# ++++# +O
##########

To run this file - put this file in the
directory with the input mazes and run

    python interview.py maze1.txt

To append to the end of an input file
a solved maze, simply put "True" as the
last argument of function "output_path"


Note: distances are not really needed 
for unweighted graphs.

Example input (maze2.txt)
#############################
#                   #       X
#                   #       #
#                   #       #
#   #############   #####   #
#   #       #   #           #
#   #       #   #           #
#   #       #   #           #
#####   #   #   #########   #
#       #           #       #
#       #           #       #
#       #           #       #
#####   #   #########   #####
#       #   #           #   #
#       #   #           #   #
#       #   #           #   #
#   #########   #########   #
#                           #
#                           #
O                           #
#############################
Output:
#############################
#                   #    +++X
#                   #    +  #
#                   #    +  #
#   #############   #####+  #
#   #       #   #        +  #
#   #       #   #        +  #
#   #       #   #        +  #
#####   #   #   #########+  #
#       #           #+++++  #
#       #           #+      #
#       #           #+      #
#####   #   #########+  #####
#       #   #+++++++++  #   #
#       #   #+          #   #
#       #   #+          #   #
#   #########+  #########   #
#+++++++++++++              #
#+                          #
O+                          #
#############################

