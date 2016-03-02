#!/usr/bin/python3

def print_game():
    this_step = "Start: %s" %(start) + "\n"
    this_step = this_step + "End: %s" %(end) + "\n" + side + "\n"
    this_step = this_step + "%s"%(times) + "\n"
    print (this_step)
###########################################
def if_win(end, new_times):
    if len(end)==6:
        if new_times["Kid6"]==new_times["Kid7"] and new_times["Kid7"]==new_times["Kid8"] and new_times["Kid8"]==new_times["Kid9"] and new_times["Kid9"]==new_times["Kid10"]:
            return True
    return False

###########################################
def find(x, lst):
    if x in lst:
        return True
    else:
        return False
###########################################
def last_num(str):
    outcome = ""
    for i in range(len(str)):
        if str[i].isnumeric():
            outcome+=str[i]
    return outcome
###########################################
def copy_dict(original, new):
    new["Kid6"] = original["Kid6"]
    new["Kid7"] = original["Kid7"]
    new["Kid8"] = original["Kid8"]
    new["Kid9"] = original["Kid9"]
    new["Kid10"] = original["Kid10"]
    
###########################################
def check_if_ok(new_start, new_end):
    if not find("Father", new_start):
        for kid in new_start:
            if "Kid" in kid == False:
                continue
            for other_kid in new_start:
                if (int(last_num(kid))-int(last_num(other_kid)))**2 ==1:
                   return False 
    else:
        for kid in new_end:
            if "Kid" in kid == False:
                continue
            for other_kid in new_end:
                if (int(last_num(kid))-int(last_num(other_kid)))**2 ==1:
                   return False 
    return True 
                
###########################################                        
def move(new_start, new_end, new_times, side, x=None, y=None):
    if x!="Kid6" and x!="Kid7" and x!="Kid8" and x!="Kid9" and x!="Kid10" and x!=None and y!="Kid6"and y!="Kid7" and y!="Kid8"and y!="Kid9" and y!="Kid10" and y!= None:
        return False
    if x==None and y==None:
        if find("Father", new_start) and side=="s":
            new_start.remove("Father")
            new_end.append("Father")
            return "e"
        elif find("Father", new_end) and side=="e":
            new_end.remove("Father")
            new_start.append("Father")
            return "s"
        else:
            return False

    elif "Kid"in x and y==None:
        if find(x, new_start) and find("Father", new_start) and side=="s":
            new_start.remove("Father")
            new_start.remove(x)
            new_end.append("Father")
            new_end.append(x)
            new_times[x]+=1
            return "e"
        elif find(x,new_end) and find("Father", new_end) and side=="e":
            new_end.remove("Father")
            new_end.remove(x)
            new_start.append("Father")
            new_start.append(x)
            new_times[x]+=1
            return "s"
        else:
            return False

    elif "Kid" in x and "Kid" in y:
        if x!=y:
            if find(x, new_start) and find(y, new_start) and find("Father", new_start) and side=="s":
                new_start.remove("Father")
                new_start.remove(x)
                new_start.remove(y)
                new_end.append("Father")
                new_end.append(x)
                new_end.append(y)
                new_times[x]+=1
                new_times[y]+=1
                return "e"
            elif find(x, new_end) and find(y, new_end) and find("Father",new_end)and side=="e":
                new_end.remove("Father")
                new_end.remove(x)
                new_end.remove(y)
                new_start.append("Father")
                new_start.append(x)
                new_start.append(y)
                new_times[x]+=1
                new_times[y]+=1
                return "s"
            else:
                return False
        else:
            return False

    else:
        return False

###########################################
def find_step(s, steps, repeat_limit=0):
    strip_s = ""
    newlines = 0
    repeat_times = 0
    for i in range(len(s)):
        strip_s += s[i]
        if s[i]=="\n":
            newlines+=1
        if newlines>=3:
            break
    for item in steps:
        strip_item = ""
        strip_item_newlines = 0
        for i in range(len(item)):
            strip_item+=item[i]
            if item[i]=="\n":
                strip_item_newlines+=1
            if strip_item_newlines>=3:
                break
        if strip_item == strip_s:
            repeat_times+=1
    if repeat_times <= repeat_limit:
       return False 
    return True
        
###########################################       
def steps_over_limit(new_steps, limit):
    if len(new_steps)>limit:
        return True
    return False
def times_over_limit(new_times,limit):
    if new_times["Kid6"]>limit or new_times["Kid7"]>limit:
        return True
    if new_times["Kid8"]>limit or new_times["Kid9"]>limit:
        return True
    if new_times["Kid10"]>limit:
        return True
    return False
    
def find_solution(start,end,times,side,steps,limit):
    #print("Solving the puzzle... Please be patient")
    start.sort()
    end.sort()
    this_step = "Start: %s" %(start) + "\n"
    this_step = this_step + "End: %s" %(end) + "\n" + side + "\n"
    this_step = this_step + "%s"%(times) + "\n"
    if times_over_limit(times,limit):
        return
    if find_step(this_step, steps, 0):
        return
    if if_win(end,times):
        solution.insert(0,this_step)
        return True
    new_steps = [] + steps
    new_steps.append(this_step)
    
    for i in range(0, len(start)):
        new_start = [] + start
        new_end = [] + end
        new_times = {}
        copy_dict(times, new_times)
        new_side = move(new_start, new_end, new_times, side, start[i], None)
        if new_side != False and check_if_ok(new_start,new_end):
            if find_solution(new_start, new_end, new_times, new_side, new_steps,limit) == True:
                solution.insert(0,this_step)
                return True

        for k in range(i+1, len(start)):
            loopnew_start = [] + start
            loopnew_end = [] + end
            loopnew_times = {}
            copy_dict(times, loopnew_times)
            loopnew_side = move(loopnew_start, loopnew_end, loopnew_times, side, start[i], start[k])
            if loopnew_side != False and check_if_ok(loopnew_start,loopnew_end):
                if find_solution(loopnew_start, loopnew_end, loopnew_times, loopnew_side, new_steps,limit) == True:
                    solution.insert(0,this_step)
                    return True
                

    for i in range(0, len(end)):
        new_start = [] + start
        new_end = [] + end
        new_times = {}
        copy_dict(times, new_times)
        new_side = move(new_start, new_end, new_times, side, end[i], None)
        if new_side != False and check_if_ok(new_start, new_end):
            if find_solution(new_start, new_end, new_times, new_side, new_steps,limit) == True:
                solution.insert(0,this_step)
                return True

        for k in range(i+1, len(end)):
            loopnew_start = [] + start
            loopnew_end = [] + end
            loopnew_times = {}
            copy_dict(times, loopnew_times)
            loopnew_side = move(loopnew_start, loopnew_end, loopnew_times, side, end[i], end[k])
            if loopnew_side != False and check_if_ok(loopnew_start, loopnew_end):
                if find_solution(loopnew_start, loopnew_end, loopnew_times, loopnew_side, new_steps,limit) == True:
                    solution.insert(0,this_step)
                    return True

    new_start = [] + start
    new_end = [] + end
    new_times = {}
    copy_dict(times, new_times)
    new_side = move(new_start, new_end, new_times, side, None, None)
    if new_side != False and check_if_ok(new_start,new_end):
        if find_solution(new_start, new_end, new_times, new_side, new_steps,limit) == True:
            solution.insert(0,this_step)
            return True

##############################################
import timeit
import time
time_begin = timeit.default_timer()

start = ["Kid6","Kid7","Kid8","Kid9", "Kid10", "Father"]
end = []
times = {"Kid6":0 ,"Kid7":0 ,"Kid8":0 ,"Kid9":0 , "Kid10":0}
side = "s"
solution = []
'''
while(not if_win(end, times)):
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
    new_times = {}
    copy_dict(times, new_times)
    
    new_side = move(new_start, new_end, new_times, side, input1, input2)
    if new_side == False:
        continue
    if check_if_ok(new_start, new_end):
        start = [] + new_start
        end = [] + new_end
        side = "" + new_side
        copy_dict(new_times, times)
print("Congratulations, you won!")
'''
for i in range(50):
    if find_solution(start,end,times,side,[], i):
        print("It takes %s moves."%(len(solution)-1) + "\n")
        break
if len(solution)==0:
    print("No Solution")
else:
    for x in range(0,len(solution)):
        print("%s."%(x+1),end="\n")
        print(solution[x])

    time_stop = timeit.default_timer()
    print("It takes %.3f seconds to solve the puzzle." %(time_stop-time_begin))

    




    
