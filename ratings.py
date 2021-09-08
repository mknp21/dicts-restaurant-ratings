"""Restaurant rating lister."""


# put your code here
the_file = open('scores.txt')
def get_ratings(file):
    """ Return an alphabetized list of restaurants and their ratings"""


    ratings= {}

    for line in file:
        line = line.rstrip()
        rest_info = line.split(':')

        restaurant, rate = rest_info
        ratings[restaurant] = rate


    sorted_ratings = sorted(ratings.items())
    
    for item in sorted_ratings:
        print(f" {item[0]} is rated at {item[1]}")

    # return ratings

get_ratings(the_file)