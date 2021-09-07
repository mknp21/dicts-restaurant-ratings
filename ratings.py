"""Restaurant rating lister."""


# put your code here
the_file = open('scores.txt')
def get_ratings(file):
    ratings= {}
    for line in file:
        line = line.rstrip()
        # restaurant, ratings = line.split(':')
        rest_info = line.split(':')
        restaurant = rest_info[0]
        rate = rest_info[1]
        ratings[restaurant] = int(rate)

    sorted_dict = sorted(ratings)

    return sorted_dict

print(get_ratings(the_file))