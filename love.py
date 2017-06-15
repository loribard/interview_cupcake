def love(my_rectangle, your_rectangle):
    love = []

    my_coordinates = [my_rectangle['left_x'], my_rectangle['left_x'] + my_rectangle['width'], my_rectangle['bottom_y'], my_rectangle['bottom_y'] + my_rectangle['height']]
    print my_coordinates
    your_coordinates = [your_rectangle['left_x'], your_rectangle['left_x'] + your_rectangle['width'], your_rectangle['bottom_y'], your_rectangle['bottom_y'] + your_rectangle['height']]
    print your_coordinates
    love = [max(my_coordinates[0], your_coordinates[0]), min(my_coordinates[1], your_coordinates[1]), max(my_coordinates[2], your_coordinates[2]), min(my_coordinates[3], your_coordinates[3])]
    print love
    if love[1] < love[0] or love[3] < love[2]:
        print "NO LOVE HERE"
    elif love[1] == love[0] or love[3] == love[2]:
        print "Share an edge only"


my_rectangle = {'left_x': 4, 'bottom_y': 1, 'width': 2, 'height': 2}
your_rectangle = {'left_x': 0, 'bottom_y': 0, 'width': 4, 'height': 4}
love(my_rectangle, your_rectangle)
