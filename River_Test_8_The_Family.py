#!/usr/bin/python3
import timeit
import time
time_begin = timeit.default_timer()

start = ["Father","Mother","Girl1","Girl2", "Boy1","Boy2","Police","Thief"]
end = []
side = "s"
solution = []

def print_game():
    this_step = "Start: %s" %(start) + "\n"
    this_step = this_step + "End: %s" %(end) + "\n" + side + "\n"
    print (this_step)

def if_win(end):
    if len(end)==8:
        return True
    return False

def find(x, lst):
    if x in lst:
        return True
    else:
        return False
############################## 
def check_if_ok(new_start, new_end):
    for person in new_start:
        if "Boy" in person and not find("Father",new_start):
            for second_person in new_start:
                if second_person=="Mother":
                    return False
        elif "Girl" in person and not find("Mother",new_start):
            for second_person in new_start:
                if second_person=="Father":
                    return False            
        elif person=="Thief" and len(new_start)>1 and not find("Police",new_start):
            return False

    for person in new_end:
        if "Boy" in person and not find("Father",new_end):
            for second_person in new_end:
                if second_person=="Mother":
                    
                    return False
        elif "Girl" in person and not find("Mother",new_end):
            for second_person in new_end:
                if second_person=="Father":
                    return False            
        elif person=="Thief" and len(new_end)>1 and not find("Police",new_end):
            return False

    return True
##############################            
    
def move(new_start, new_end, side, x, y=None):
    if x==None:
        return False
    if x!="Father" and x!="Mother" and x!="Girl1" and x!="Girl2" and x!="Boy1" and x!="Boy2"and x!="Police" and x!="Thief":
        return False
    if y!="Father" and y!="Mother" and y!="Girl1" and y!="Girl2" and y!="Boy1" and y!="Boy2"and y!="Police" and y!="Thief" and y!= None:
        return False
    if y==None:
        if x=="Father" or x=="Mother" or x=="Police":
            if find(x, new_start) and side=="s":
                new_start.remove(x)
                new_end.append(x)
                return "e"
            elif find(x, new_end) and side=="e":
                new_end.remove(x)
                new_start.append(x)
                return "s"
            else:
                return False
        else:
            return False
    elif x!=y and (x=="Father" or x=="Mother" or x=="Police" or y=="Father" or y=="Mother" or y=="Police"):
        if find(x, new_start) and find(y, new_start) and side=="s":
            new_start.remove(x)
            new_start.remove(y)
            new_end.append(x)
            new_end.append(y)
            return "e"
        elif find(x, new_end) and find(y, new_end) and side=="e":
            new_start.append(x)
            new_start.append(y)
            new_end.remove(x)
            new_end.remove(y)
            return "s"
        else:
            return False
    else:
        return False
########################################################################      
'''while(not if_win(end)):
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
print("Congratulations, you won!")'''
############################################################################ 
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
        if "Girl"in s[i]:
            s[i] = "Girl"
        elif "Boy" in s[i]:
            s[i] = "Boy"
    for i in range(0, len(e)):
        if "Girl" in e[i]:
            e[i] = "Girl"
        elif "Boy" in e[i]:
            e[i] = "Boy"
          
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

    if side=="s":
        for i in range(0, len(start)):
            new_start = [] + start
            new_end = [] + end
            new_side = move(new_start, new_end, side, start[i])
            if new_side != False and check_if_ok(new_start,new_end):
                if find_solution(new_start, new_end, new_side, new_steps,limit):
                    solution.insert(0,this_step)
                    return True
            for k in range(i+1, len(start)):
                new_start = [] + start
                new_end = [] + end
                new_side = move(new_start, new_end, side, start[i], start[k])
                if new_side != False and check_if_ok(new_start,new_end):
                    if find_solution(new_start, new_end, new_side, new_steps,limit) == True:
                        solution.insert(0,this_step)
                        return True
                
    if side=="e":
        for i in range(0, len(end)):
            new_start = [] + start
            new_end = [] + end
            new_side = move(new_start, new_end, side, end[i])
            if new_side != False and check_if_ok(new_start,new_end):
                if find_solution(new_start, new_end, new_side, new_steps,limit) == True:
                    solution.insert(0,this_step)
                    return True
            for k in range(i+1, len(end)):
                new_start = [] + start
                new_end = [] + end
                new_side = move(new_start, new_end, side, end[i], end[k])
                if new_side != False and check_if_ok(new_start,new_end):
                    if find_solution(new_start, new_end, new_side, new_steps,limit) == True:
                        solution.insert(0,this_step)
                        return True
#################################################################################
                


for i in range(50):
    print("Solving for move less than or equal to %s..."%(i))
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


    




    
