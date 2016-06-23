##Program to generate MineCraft Commannd sequences
##Audra Brown
##6/23/2016 v0.1

#build a single-walled, square keep
#clears interior, opens roof and floor
#@param ir interior radius (distance from center to wall)
#@param ht height of the keep relative to sp
#@param block the substance to build out of
#@param block_sub number of the block variation
def keep(ir, ht, block, block_sub):
    cmds = []
    final = '/summon FallingSand ~ ~1 ~ {Block:redstone_block,'
    i = 1
    s = '/fill '
    br = ir+1
    cmds.append(s+'~'+str(br)+' ~'+' ~'+str(br)+' ~'+str(br/-1)+' ~'+str(ht)+' ~'+str(br/-1)+' '+block+' '+str(block_sub)+' hollow')
    cmds.append(s+'~'+str(ir)+' ~-1'+' ~'+str(ir)+' ~'+str(ir/-1)+' ~'+str(ht+1)+' ~'+str(ir/-1)+' '+'air')

    for c in cmds:
        final += crCommand(c,i)
        i += 1
    return final[:-1]+getCurlys(len(cmds))


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
    for x in range(0,i):
        result += '}'
    return result



def test():
    cmd = "/fill ~ ~ ~"
    print(keep(5,10, 'stone', 0))


test()
    
    
    
    
    
