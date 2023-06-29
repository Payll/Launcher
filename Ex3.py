def calculate_transmission_cost(movie_title, cost_cap):
    # Get the length of the movie title
    title_length = len(movie_title)

    # Return the minimum of the length of the title and the cost cap
    return min(title_length, cost_cap)


tile, cost = input().split()
print(calculate_transmission_cost(tile, float(cost)))
