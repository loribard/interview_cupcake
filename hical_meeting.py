def hical_meeting(lsta):
    list_of_lists = []
    lsta.sort()
    for item in lsta:
        list_of_lists.append(list(item))
    print list_of_lists
    list_timeslots = [list_of_lists[0]]
    for i in range(1,len(list_of_lists)):
        if list_of_lists[i][0] <= list_timeslots[-1][1]:
            list_timeslots[-1] = [list_timeslots[-1][0],max((list_of_lists[i][1]),list_timeslots[-1][1])]
        else:
            list_timeslots.append(list_of_lists[i])
    booked = []
    for item in list_timeslots:
        booked.append(tuple(item))
    print booked



















hical_meeting(  [(0, 1), (3, 5), (4, 8), (10, 12), (9, 13)])
hical_meeting([(1,2),(2,3)])
hical_meeting([(1,5),(2,3)])
hical_meeting(  [(1, 10), (2, 6), (3, 5), (7, 9)])