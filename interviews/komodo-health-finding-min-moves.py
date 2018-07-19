"""
input = [1, 2, 3]
output = 2

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]

input = [1,3,5,6]
Could be a number btwn start < any numb (may not exist in the list) < end
elements can repeat
sorted increm

"""

# accept sorted source
def calc_moves(source, trigger):
    moves = 0
    for item in source:
        if item != trigger:
            moves += 1
    return moves

def calc_moves1(source):

    moves_calculated = {}
    trigger = -1

    for i in range(len(source)):
        moves = 0
        trigger = source[i]
        for j in range(len(source)):

            if i != j and source[j] != trigger:
                moves += abs(trigger - source[j])
                #moves += 1
        moves_calculated[source[i]] = moves


    print  moves_calculated
    return min(moves_calculated.values())


def calc_moves2(source, trigger=-1):
    moves_calculated = {}
    total_elements = len(source)

    for i in range(total_elements):
        trigger = source[i]
        print "trigger=",trigger

        right = i+1
        left = i-1
        print "left=",left," right=",right

        if (right < total_elements) and (left >= 0):
            best_move = min(helper(trigger,source[right]), helper(trigger,source[left]))
        if left < 0:
            best_move = helper(trigger,source[right])
        if right >= total_elements:
            best_move = helper(trigger,source[left])
        print "\nbest_move=",best_move
        moves_calculated[trigger] = best_move
    print moves_calculated
    return min(moves_calculated.values())

def helper(trigger,current):
    print "trigger=",trigger," current=",current
    if current != None and trigger != current:
        return abs(trigger-current)
    else: return 0

"""
trigger => moves
1 => m1
3 => m2
5 => m3
6 => m4

[1,3,5,6] => [1, 2, 5, 6] => [1, 1, 5, 6]


min(m1,m2,m3,m4)


"""

input = [3,1,5,6]
input = sorted(input)
trigger = 3

print "moves ...", calc_moves(input, trigger)

print "moves1 ...", calc_moves1(input)

print "moves2 ...", calc_moves2(input)
