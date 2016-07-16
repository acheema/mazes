Maze problem
--------------------------------------
Problem statement

Given a file with a maze in the format

##########
X  #     #
#  #  #  #
#     #  O
##########

where the maze begins at X and ends at O
and the only valid spots are spaces,
output the shortest valid path filled in
with +s as seen below.

##########
X++# ++++#
# +# +# +#
# ++++# +O
##########

--------------------------------------

To run this file - put this file in the
directory with the input mazes and run

    python interview.py maze1.txt

To append the solved maze to the end of
an input file, simply put "True" as the
last argument of the call to "output_path"
on line 82.

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

