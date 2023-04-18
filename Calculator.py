def add_time(start, duration, day=""):
    #print(start, duration, day)
    daylist=['Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday']
    starterlist=start.split(":")
    durationlist=duration.split(":")
    minstart=starterlist[1].split(" ") #['06', 'PM']
    #print(starterlist, durationlist,minstart)#['11', '40 AM'] ['0', '25'] ['40', 'AM']
    #print(int(minstart[0])+int(durationlist[1]))
    heure=int(starterlist[0])
    if starterlist[0]==12 and minstart[1]=="AM":
        heure=0
    if int(starterlist[0]) < 12 and minstart[1]=="PM":
        heure=int(starterlist[0])+12
    #print(heure)
    minutes = int(minstart[0])+int(durationlist[1])
    heure =heure+ int(durationlist[0])
    n=0
    #print(minutes)
    #print(heure)
    while minutes >=60:
        heure=heure+1
        minutes= minutes-60
    #print(heure, minutes)

    while heure>=24:
        n=n+1
        heure=heure-24
    #On traduit l heure en AM et Pm
    #print(heure)
    #print(n)
    heurev=heure
    if heure<1:
        heurev=heure+12
        minstart[1]="AM"
    if heure <12 and heure >=1:
        minstart[1]="AM"
    if heure >= 12:
        minstart[1]="PM"
        if heure>=13:
            heurev=heure-12
    if minutes <10:
        minutes= "0"+str(minutes)
    time= str(heurev)+":"+ str(minutes)+" "+minstart[1]
    
    index=0
    if day.capitalize() in daylist:
        #print(day.capitalize())
        index = daylist.index(day.capitalize())
        a=index+n
        while a >= len(daylist):
            a=a-len(daylist)
        time= time+", " + daylist[a]
    if n>=1:
        if n==1:
            time= time+" (next day)"
        else:
            time= time +" ("+str(n)+" days later)"
    return time
