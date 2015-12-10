import networkx as nx


class Activity:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, activity_index, predecessor_array, activity_name, activity_duration):
        self.activity_index = activity_index
        self.predecessor_array = predecessor_array
        self.activity_name = activity_name
        self.activity_duration = activity_duration

    def __str__(self):
        return self.activity_name + " (node # " + str(self.activity_index) + ")"

    def __repr__(self):
        return self.activity_name + " (node # " + str(self.activity_index) + ")"

    def __lt__(self, other):
        return self.activity_duration < other.activity_duration


def make_activities():
    activities = [Activity] * 16
    activities[0] = None

    write_screenplay = Activity(1, [], "Writing a screenplay", 30)
    activities[1] = write_screenplay

    making_costumes = Activity(2, [7], "Making costumes", 5)
    activities[2] = making_costumes

    rehearsals = Activity(3, [7], "Rehearsals", 12)
    activities[3] = rehearsals

    promo_mats = Activity(4, [8], "Making promotional material", 5)
    activities[4] = promo_mats

    show_programs = Activity(5, [8], "Making programs", 3)
    activities[5] = show_programs

    sets_and_props = Activity(6, [11], "Making sets and props", 10)
    activities[6] = sets_and_props

    casting = Activity(7, [8], "Casting", 3)
    activities[7] = casting

    venue_contracting = Activity(8, [12], "Obtaining a venue", 3)
    activities[8] = venue_contracting

    organizing_lights = Activity(9, [10], "Organizing lights and stage effects", 3)
    activities[9] = organizing_lights

    dress_rehearsal = Activity(10, [3, 6], "Dress rehearsal", 1)
    activities[10] = dress_rehearsal

    hire_stage_hands = Activity(11, [8], "Hiring stage hands", 1)
    activities[11] = hire_stage_hands

    choosing_performance_dates = Activity(12, [1], "Choosing performance dates and show times", 1)
    activities[12] = choosing_performance_dates

    selling_tickets = Activity(13, [8], "Selling the tickets", 7)
    activities[13] = selling_tickets

    arranging_seating = Activity(14, [13], "Arranging seating", 2)
    activities[14] = arranging_seating

    end_node = Activity(15, [2, 9, 4, 5, 14], "End", 0)
    activities[15] = end_node

    activity_network = nx.DiGraph()
    activity_network.add_nodes_from(activities[1:len(activities)])

    runsum = 1
    for task in activity_network:
            j = 0
            while j < len(task.predecessor_array):
                '''print("adding edge # " + str(runsum) + " from " + " (activity index #" + str(
                    activities[task.predecessor_array[
                        j]].activity_index) + ") " + " to " + " (activity #" + str(
                    task.activity_index) + ") " + " (iteration # " + str(runsum) + ")") '''
                activity_network.add_edge(activities[task.predecessor_array[j]], task,
                                          label=activities[task.predecessor_array[j]].activity_duration,
                                          weight=activities[task.predecessor_array[j]].activity_duration)
                j = j + 1
                runsum += 1

    '''#Debuggery
    i = 1
    for edge in activity_network.edges():
        print(str(i) + " " + str(edge[0]) + " -> " + str(edge[1]) + " " + str(
            activity_network.get_edge_data(edge[0], edge[1])['weight']))
        i += 1  #end_Debuggery '''
    print("-------------------------")

    last_s = None
    for s in nx.dag_longest_path(activity_network):
        print(str(s))

        if not (last_s == None):
            activity_network.get_edge_data(last_s, s)['color'] = "red"

        last_s = s
    print("-------------------------")

    happy_write_dot(activity_network, "critical_path_in_activity_network.gv")

    ''' #Debuggery
     i = 1
     for node in activity_network.nodes():
        print(str(i) + " " + str(node.activity_name) + str(node.predecessor_array) + str(node.in_graph))
        print(activity_network.number_of_edges(node))
        i += 1 #end_Debuggery'''


def happy_write_dot(G, path):
    """
    Write NetworkX graph G to Graphviz dot format on path.
    Parameters
    ----------
    G : graph
       A networkx graph
    path : filename
       Filename or file handle to write
    """
    try:
        import pygraphviz
    except ImportError:
        raise ImportError('requires pygraphviz ',
                          'http://pygraphviz.github.io/')
    A = nx.to_agraph(G)
    A.write(path)
    A.clear()
    return


make_activities()
