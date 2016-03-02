#!/usr/python3
import timeit
import time
time_begin = timeit.default_timer()

start = ["Soldier1","Soldier2","Soldier3","Kid1", "Kid2"]
end = []
side = "s"
solution = []

def print_game():
    this_step = "Start: %s" %(start) + "\n"
    this_step = this_step + "End: %s" %(end) + "\n" + side + "\n"
    print (this_step)

def if_win(end):
    if len(end)==5:
        return True
    return False

def find(x, lst):
    if x in lst:
        return True
    else:
        return False

def check_if_ok(new_start, new_end):
    return True
    
def move(new_start, new_end, side, x, y=None):
    if x==None:
        return False
    if x!="Soldier1" and x!="Soldier2" and x!="Soldier3" and x!="Kid1" and x!="Kid2" and y!="Soldier1"and y!="Soldier2" and y!="Soldier3"and y!="Kid1" and y!="Kid2" and y!= None:
        return False
    if y!=None:
        if "Kid" in x and "Kid" in y and x!=y:
            if find(x, new_start) and find(y, new_start) and side=="s":
                new_start.remove(x)
                new_start.remove(y)
                new_end.append(x)
                new_end.append(y)
                return "e"
            elif find(x, new_end) and find(y, new_end) and side=="e":
                new_end.remove(x)
                new_end.remove(y)
                new_start.append(x)
                new_start.append(y)
                return "s"
            else:
                return False
        else:
            return False
    elif ("Soldier"in x or "Kid"in x) and y==None:
        if find(x, new_start) and side=="s":
            new_start.remove(x)
            new_end.append(x)
            return "e"
        elif find(x,new_end) and side=="e":
            new_end.remove(x)
            new_start.append(x)
            return "s"
        else:
            return False
    else:
        return False
'''       
while(not if_win(end)):
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
    new_side = move(new_start, new_end, side, input1, input2)
    if new_side == False:
        continue
    if check_if_ok(new_start, new_end):
        start = [] + new_start
        end = [] + new_end
        side = "" + new_side
print("Congratulations, you won!")
'''
def steps_over_limit(new_steps,limit):
    if len(new_steps)>limit:
        return True
    return False

def find_solution(start,end,side,steps,limit):
    start.sort()
    end.sort()
    
    s = [] + start
    e = [] + end
    for i in range(0, len(s)):
        if "Kid"in s[i]:
            s[i] = "Kid"
        elif "Soldier" in s[i]:
            s[i] = "Soldier"
    for i in range(0, len(e)):
        if "Kid" in e[i]:
            e[i] = "Kid"
        elif "Soldier" in e[i]:
            e[i] = "Soldier"
          
    this_step = "Start: %s" %(s) + "\n"
    this_step = this_step + "End: %s" %(e) + "\n" + side + "\n"
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
        new_side = move(new_start, new_end, side, start[i], None)
        if new_side != False:
            if find_solution(new_start, new_end, new_side, new_steps,limit) == True:
                solution.insert(0,this_step)
                return True

        for k in range(i+1, len(start)):
            loopnew_start = [] + start
            loopnew_end = [] + end
            loopnew_side = move(loopnew_start, loopnew_end, side, start[i], start[k])
            if loopnew_side != False:
                if find_solution(loopnew_start, loopnew_end, loopnew_side, new_steps,limit) == True:
                    solution.insert(0,this_step)
                    return True
                

    for i in range(0, len(end)):
        new_start = [] + start
        new_end = [] + end
        new_side = move(new_start, new_end, side, end[i], None)
        if new_side != False:
            if find_solution(new_start, new_end, new_side, new_steps,limit) == True:
                solution.insert(0,this_step)
                return True

        for k in range(i+1, len(end)):
            loopnew_start = [] + start
            loopnew_end = [] + end
            loopnew_side = move(loopnew_start, loopnew_end, side, end[i], end[k])
            if loopnew_side != False:
                if find_solution(loopnew_start, loopnew_end, loopnew_side, new_steps,limit) == True:
                    solution.insert(0,this_step)
                    return True


for i in range(50):
    if find_solution(start,end,side,[], i):
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



    




    
