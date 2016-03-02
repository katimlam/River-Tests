#!/usr/bin/python3
import timeit
import time
time_begin = timeit.default_timer()

start = ["Farmer","Goat","Cabbage","Wolf"]
end = []
solution = []

def print_game():
    print("Start:%s" %(start), end="\n")
    print("End:%s" %(end), end="\n") 

def check_if_ok(new_start, new_end):
    if find("Farmer", new_end):
        if find("Goat", new_start) and find("Cabbage", new_start):
            return False
        if find("Wolf", new_start) and find("Goat", new_start):
            return False
    if find("Farmer", new_start):
        if find("Goat", new_end) and find("Cabbage", new_end):
            return False
        if find("Wolf", new_end) and find("Goat", new_end):
            return False
    return True


def if_win(end):
    if len(end)==4:
        return True
    return False

def find(x, lst):
    if x in lst:
        return True
    else:
        return False

def move(new_start, new_end, x, y=None):
    if x!="Farmer" and y!="Farmer":
        return False
    if y!=None:
        if find(x, new_start) and find(y, new_start):     
            new_start.remove(x)
            new_end.append(x)
            new_start.remove(y)
            new_end.append(y)
        elif find(x, new_end) and find(y, new_end):
            new_end.remove(x)
            new_start.append(x)
            new_end.remove(y)
            new_start.append(y)
        else:
            return False
    else:
        if find(x, new_start):
            new_start.remove(x)
            new_end.append(x)
        else:
            new_end.remove(x)
            new_start.append(x)
    return True
'''
while(not if_win()):
    print_game()
    input1 = input("input1: ")
    input2 = input("input2: ")
    if input2=="":
        input2=None
    if input1=="":
        input1=input2
        input2=None
    new_start = [] + start
    new_end = [] + end
    if move(new_start, new_end, input1, input2)== False:
        continue
    if check_if_ok()==True:
        start = [] + new_start
        end = [] + new_end
       
print("Congratulations, you won!")
'''
def steps_over_limit(new_steps,limit):
    if len(new_steps)>limit:
        return True
    return False

def find_solution(start,end,steps,limit):
    start.sort()
    end.sort()
    this_step = "%s" %(start) + "\n"
    this_step = this_step + "%s" %(end) + "\n" + "\n"
    if steps_over_limit(steps, limit):
        return
    if find(this_step, steps):
        return
    if if_win(end):
        solution.insert(0,this_step)
        return True
    new_steps = [] + steps
    new_steps.append(this_step)
    
    for i in range(0, len(start)):
        new_start = [] + start
        new_end = [] + end
        if move(new_start, new_end, start[i]) and check_if_ok(new_start, new_end):
            if find_solution(new_start, new_end, new_steps,limit) == True:
                solution.insert(0,this_step)
                return True

        for k in range(i+1, len(start)):
            loopnew_start = [] + start
            loopnew_end = [] + end
            if move(loopnew_start, loopnew_end, start[i], start[k]) and check_if_ok(loopnew_start, loopnew_end):
                if find_solution(loopnew_start, loopnew_end, new_steps,limit) == True:
                    solution.insert(0,this_step)
                    return True
                

    for i in range(0, len(end)):
        new_start = [] + start
        new_end = [] + end
        if move(new_start, new_end, end[i], None) and check_if_ok(new_start, new_end):
            if find_solution(new_start, new_end, new_steps,limit) == True:
                solution.insert(0,this_step)
                return True

        for k in range(i+1, len(end)):
            loopnew_start = [] + start
            loopnew_end = [] + end
            if move(loopnew_start, loopnew_end, end[i], end[k]) and check_if_ok(loopnew_start, loopnew_end):
                if find_solution(loopnew_start, loopnew_end, new_steps,limit) == True:
                    solution.insert(0,this_step)
                    return True


for i in range(50):
    if find_solution(start,end,[], i):
        print("It takes %s moves."%(i) + "\n")
        break
if len(solution)==0:
    print("No Solution")
else:
    for x in range(0,len(solution)):
        print("%s."%(x+1),end="\n")
        print(solution[x])

    time_stop = timeit.default_timer()
    print("It takes %.3f seconds to solve the puzzle." %(time_stop-time_begin))




            


             



