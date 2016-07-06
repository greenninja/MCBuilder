##Program to generate MineCraft Commannd sequences
##Audra Brown
##6/23/2016 v0.1

#build a single-walled, square keep
#clears interior, opens roof and floor
#@param ir interior radius (distance from center to wall)
#@param ht height of the keep relative to sp
#@param block the substance to build out of
#@param block_sub number of the block variation
#@param floors boolean if true, there will be a top and bottom to the keep
def keep1(ir, ht, gl, block, block_sub, floor, ceiling, filename):
    cmds = []
    final = '/summon FallingSand ~ ~1 ~ {Block:redstone_block,'
    i = 1
    s = '/fill '
    br = ir+1
    f= open(filename+".txt", 'a')
    f.write(s+'~'+str(br)+' '+str(gl)+' ~'+str(br)+' ~'+str(br/-1)+' '+str(ht+gl)+' ~'+str(br/-1)+' '+block+' '+str(block_sub)+' hollow'+'\n')
    if floor and ceiling:
        f.write(s+'~'+str(ir)+' '+str(gl+1)+' ~'+str(ir)+' ~'+str(ir/-1)+' '+str(ht+gl-1)+' ~'+str(ir/-1)+' '+'air'+'\n')
    elif floor:
        f.write(s+'~'+str(ir)+' '+str(gl+1)+' ~'+str(ir)+' ~'+str(ir/-1)+' '+str(ht+gl)+' ~'+str(ir/-1)+' '+'air'+'\n')
    else:
        f.write(s+'~'+str(ir)+' '+str(gl)+' ~'+str(ir)+' ~'+str(ir/-1)+' '+str(ht+gl-1)+' ~'+str(ir/-1)+' '+'air'+'\n')    

    return True

#build a single-walled, square keep (absolute coordinates)
#clears interior, opens roof and floor
#@param ir interior radius (distance from center to wall)
#@param ht height of the keep relative to sp
#@param block the substance to build out of
#@param block_sub number of the block variation
#@param floors boolean if true, there will be a top and bottom to the keep
def keep2(ir, ht, gl, block, block_sub, floor, ceiling, filename, xcoor, zcoor):
    cmds = []
    i = 1
    s = '/fill '
    br = ir+1
    f= open(filename+".txt", 'a')
    f.write(s+str(br+xcoor)+' '+str(gl)+' '+str(br+zcoor)+' '+str(xcoor-br)+' '+str(ht+gl)+' '+str(zcoor-br)+' '+block+' '+str(block_sub)+' hollow'+'\n')
    if floor and ceiling:
        f.write(s+str(ir+xcoor)+' '+str(gl+1)+' '+str(ir+zcoor)+' '+str(xcoor-ir)+' '+str(ht+gl-1)+' '+str(zcoor-ir)+' '+'air'+'\n')
    elif floor:
        f.write(s+str(ir+xcoor)+' '+str(gl+1)+' '+str(ir+zcoor)+' '+str(xcoor-ir)+' '+str(ht+gl)+' '+str(zcoor-ir)+' '+'air'+'\n')
    else:
        f.write(s+str(ir+xcoor)+' '+str(gl)+' '+str(ir+zcoor)+' '+str(xcoor-ir)+' '+str(ht+gl-1)+' '+str(zcoor-ir)+' '+'air'+'\n')    

    return True


#builds keep with no sub_block
def keep(ir, ht,gl, block, floor, ceiling, filename):
    keep1(ir, ht,gl, block, 0, floor, ceiling, filename)
    return

def keepAbs(ir, ht,gl, block, floor, ceiling, filename, x, z):
    keep2(ir, ht,gl, block, 0, floor, ceiling, filename,x,z)
    return

#build a cascading tower that follow phi
#@param ht total height
#@param ir inner radius of uppermost section
def phiTower(ht, ir,block,gl):
    philist =getPhi2(ht)
    irr = ir
    for p in philist:
        keep(irr, p,gl,block,False,True,"phiTower"+str(ht)+'_'+str(ir)+'_'+str(gl))
        irr +=1
        
    #END

#build a cascading tower that follow phi
#@param ht total height
#@param ir inner radius of uppermost section
def phiTowerAbs(ht, ir,block,gl,x,y):
    philist =getPhi2(ht)
    irr = ir
    for p in philist:
        keepAbs(irr, p,gl,block,False,True,"phiTower"+str(ht)+'_'+str(ir)+'_'+str(gl),x,y)
        irr +=1
        
    #END

#get phi sequence (starting at top)
#@param the number to base sequence (big number)
def getPhi1(n):
    ls = [n]
    i = n
    while i > 0:
        i = i/1.61
        i = int(float(str(i)[:3]))
        ls.append(i)
    return ls

#get phi sequence (starting at bottom)
#@param the number to base sequence (big number)
def getPhi2(n):
    ls = []
    i = 1
    while i < n+1:
        i = i*1.61
        i = int(float(str(i)[:3])+.5)
        ls.append(i)
    
    ls.reverse()
    print(ls)

    return ls
        
    

#puts the command into a form that can be sequenced
#@param command the command
#@param order the execution time of the command (sequence position)
def crCommand(command, order):
    wrap_start = "Time:"
    wrap_center = ',Riding:{id:"FallingSand",Block:command_block,TileEntityData:{Command:'
    wrap_end = '},'
    return wrap_start+str(order)+wrap_center+'"'+command+'"'+wrap_end;



#generate a string with the appropriate number of end curly braces
def getCurlys(i):
    result = ''
    for x in range(1,i):
        result += '}'
    return result+'}'



def test():
    getPhi1(100)
    getPhi2(100)
    phiTowerAbs(100,1,"ice",100, 1152,-8)


test()
    
    
    
    
    
