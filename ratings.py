"""Restaurant rating lister."""


# put your code here
the_file = open('scores.txt')
def get_ratings(file):
    ratings= {}
    for line in file:
        line = line.rstrip()
        restaurant, ratings = line.split(':')
        ratings[restaurant] = ratings

