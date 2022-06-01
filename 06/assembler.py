dict1={ 'R0':0 ,'R1':'1','R2':2,'R3':3,'R4':4,'R5':5,'R6':6,'R7':7,'R8':8,'R9':9,'R10':10,'R11':11,
'R12':12,'R13':13,'R14':14,'R15':15,'SCREEN':16384,'KBD':24576,'SP':0,'LCL':1,'ARG':2,'THIS':3,
'THAT':4}
runmem=16
def binary(t):
    t=int(t)
    ad=bin(t)[2:]
    ad=ad.zfill(15)
    return ad

def dest(s):
    dicdest={'M':'001','D':'010','MD':'011','A':'100','AM':'101','AD':'110','AMD':'111'}
    var=''
    '''for i in s:
        if i in 'ADM' and i not in var:
            var.append(i)
    if var!='':
        var.sort()'''
    t=s.find("=")
    if (t==-1):
        var='000'
        return var
    else:
        var=dicdest[s[:t]]
        return var
def jump(s):
    dicj={"JGT":"001",
          "JEQ":"010",
          "JGE":"011",
          "JLT":"100",
          "JNE":"101",
          "JLE":"110",
          "JMP":"111"
    }
    ind=s.find(";")
    if(ind==-1):
        ju="000"
    else:
        s=s.strip()
        ju=dicj[s[ind+1:]]
    return ju

def comp(s):
    global dict1
    diccomp={"0":"101010",
             "1":"111111",
             "-1":"111010",
             "D":"001100",
             "A":"110000",
             "M":"110000",
             "!D":"001101",
             "!A":"110001",
             "!M":"110001",
             "-D":"001111",
             "-A":"110011",
             "-M":"110011",
             "D+1":"011111",
             "A+1":"110111",
             "M+1":"110111",
             "D-1":"001110",
             "A-1":"110010",
             "M-1":"110010",
             "D+A":"000010",
             "D+M":"000010",
             "D-A":"010011",
             "D-M":"010011",
             "A-D":"000111",
             "M-D":"000111",
             "D&A":"000000",
             "D&M":"000000",
             "D|A":"010101",
             "D|M":"010101"
             }
    var=""
    t=s.find("=")
    if (t==-1): 
        t1=s.find(";")
        s=s.strip()
        s=s.strip("(")
        s=s.strip(")")
        if(t1!=-1):
            scomp=diccomp[s[:t1]]
        else:
            scomp=dict1[s]
    else:
        if (s.find(";")==-1):
            s=s.strip()
            scomp=diccomp[s[t+1:]]
        else:
            t1=s.find(";")
            scomp=diccomp[s[t+1:t1]]
    return scomp
    '''for j in s:
        pass'''
def ainst(line):
    global dict1
    global runmem
    t=line[1:]
    if(ord(t[0])-ord('0')<10 and ord(t[0])-ord('0')>-1):
        inst=binary(t)
        inst='0'+inst
        return inst
    else:
        t=t.strip()
        inst=binary(dict1[t])
        inst='0'+inst
        return inst
        '''dict1[t]=runmem
        runmem+=1
        inst=binary(t)
        inst='0'+inst
        return inst'''  
        
def cinst(line):
    global dict1
    inst='111'
    t=line.find("=")
    if (t==-1):
        t=line.find(";")
        if "M" in line[:t]:
            t='1'
        else:
            t='0'
    else:
        s=line.find(";")
        if(s==-1):
            if "M" in line[t:]:
                t="1"
            else:
                t='0'
        else:
            if "M" in line[t:s]:
                t='1'
            else:
                t='0'
    inst+=t
    inst=inst+comp(line)+dest(line)+jump(line)
    return inst
    
      
f=open("Pong.asm",'r')
g=open("abc.txt",'w')
for line in f:
    if not line.isspace():
        if line[0]!='/':
            line=line.strip()
            index=line.find(' ')
            if index==-1:
                g.write(line+'\n')
            else:
                g.write(line[:index]+'\n')
f.close()
g.close()
f=open("abc.txt",'r')
i=0
for line in f:
    if line[0]=="(":
        line=line.strip()
        line=line.strip("(")
        line=line.strip(")")
        dict1[line]=i
        i=i-1   
    i=i+1
f.close()
f=open("abc.txt",'r')
for line in f:
    if line[0]=='@':
        if(line[1] not in '0123456789'):
            t=line[1:]
            t=t.strip()
            t=t.strip(")")
            t=t.strip("(")
            if t not in dict1.keys():
                dict1[t]=runmem
                runmem+=1
f.close()
print(dict1)
f=open("abc.txt",'r')
g=open("abc1.hack","w")
i=0
for line in f:
    #print(i)
    if line[0]=='@':
        inst=ainst(line)
        g.write(inst+'\n')
    elif line[0]=="(" :
        line=line.strip()
        line=line.strip("(")
        line=line.strip(")")
        t=dict1[line]
        inst=binary(t)
        inst='0'+inst
    else:
        inst=cinst(line)
        g.write(inst+'\n')
    i=i+1
f.close()
g.close()
print(dict1['SP'])
'''
print(jump("D;JLT"))
print(ainst("@THAT"))
print(comp("-1;JLE",0))
print(dest("D=D+1;JLT"))
print(dict1["R15"])
print(dict1["ponggame.0"])
'''