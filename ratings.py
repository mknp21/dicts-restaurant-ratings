"""Restaurant rating lister."""


# put your code here
the_file = open('scores.txt')
def get_ratings(file):
    """ Return an alphabetized list of restaurants and their ratings"""
    
    ratings = {}

    new_restaurant = input("Add a new restaurant to rate:")
    new_restaurant_score = input(f"Add a rating for {new_restaurant}:")

    ratings[new_restaurant] = new_restaurant_score

    for line in file:
        line = line.rstrip()
        rest_info = line.split(':')

        restaurant, rate = rest_info
        ratings[restaurant] = rate


    sorted_ratings = sorted(ratings.items())
    
    for item in sorted_ratings:
        print(f" {item[0]} is rated at {item[1]}")

get_ratings(the_file)






