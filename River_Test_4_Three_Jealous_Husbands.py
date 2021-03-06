#!/usr/bin/python3
import timeit
import time
time_begin = timeit.default_timer()

start = ["Husband1","Husband2","Husband3","Wife1", "Wife2", "Wife3"]
end = []
side = "s"
solution = []

def print_game():
    this_step = "Start: %s" %(start) + "\n"
    this_step = this_step + "End: %s" %(end) + "\n" + side + "\n"
    print (this_step)

def if_win(end):
    if len(end)==6:
        return True
    return False

def find(x, lst):
    if x in lst:
        return True
    else:
        return False

def last_num(str):
    return str[-1] 

def check_if_ok(new_start, new_end):
    for wife in new_start:
        if "Wife" in wife:
            for husband in new_start:
                if "Husband" in husband and last_num(husband)==last_num(wife):
                    break
            else:
                for other_husband in new_start:
                    if "Husband" in other_husband:
                        return False
    for wife in new_end:
        if "Wife" in wife:
            for husband in new_end:
                if "Husband" in husband and last_num(husband)==last_num(wife):
                    break
            else:
                for other_husband in new_end:
                    if "Husband" in other_husband:
                        return False
    return True
                
                        
def move(new_start, new_end, side, x, y=None):
    if x==None:
        return False
    if x!="Husband1" and x!="Husband2" and x!="Husband3" and x!="Wife1" and x!="Wife2" and x!="Wife3" and y!="Husband1"and y!="Husband2" and y!="Husband3"and y!="Wife1" and y!="Wife2" and y != "Wife3" and y!= None:
        return False
    if y!=None:
        if x!=y:
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
    elif ("Husband"in x or "Wife"in x) and y==None:
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
##############################################        
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
############################################## 
'''def find_similar(start,end,side,steps):
    s = [] + start
    e = [] + end
    st = [] + steps
    for i in range(0, len(s)):
        if "Husband"in s[i]:
            s[i] = "Husband"
        elif "Wife" in s[i]:
            s[i] = "Wife"
    for i in range(0, len(e)):
        if "Husband" in e[i]:
            e[i] = "Husband"
        elif "Wife" in e[i]:
            e[i] = "Wife"
    text = "Start: %s" %(s) + "\n" + "End: %s" %(e) + "\n" + side + "\n"
    for i in range(len(st)):
        step = ""
        for k in range(len(st[i])):
            if char.isdigit()==False:
                step+=st[i][k]
        if step==text:
            return False
    return True
'''       
    
def steps_over_limit(new_steps, limit):
    if len(new_steps)>limit:
        return True
    return False        
    
def find_solution(start,end,side,steps,limit):
    start.sort()
    end.sort()
    this_step = "Start: %s" %(start) + "\n"
    this_step = this_step + "End: %s" %(end) + "\n" + side + "\n"
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
        if new_side != False and check_if_ok(new_start,new_end):
            if find_solution(new_start, new_end, new_side, new_steps,limit) == True:
                solution.insert(0,this_step)
                return True

        for k in range(i+1, len(start)):
            loopnew_start = [] + start
            loopnew_end = [] + end
            loopnew_side = move(loopnew_start, loopnew_end, side, start[i], start[k])
            if loopnew_side != False and check_if_ok(loopnew_start,loopnew_end):
                if find_solution(loopnew_start, loopnew_end, loopnew_side, new_steps,limit) == True:
                    solution.insert(0,this_step)
                    return True
                

    for i in range(0, len(end)):
        new_start = [] + start
        new_end = [] + end
        new_side = move(new_start, new_end, side, end[i], None)
        if new_side != False and check_if_ok(new_start, new_end):
            if find_solution(new_start, new_end, new_side, new_steps,limit) == True:
                solution.insert(0,this_step)
                return True

        for k in range(i+1, len(end)):
            loopnew_start = [] + start
            loopnew_end = [] + end
            loopnew_side = move(loopnew_start, loopnew_end, side, end[i], end[k])
            if loopnew_side != False and check_if_ok(loopnew_start, loopnew_end):
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
    



    




    
