w = 'Hello Python World!'
print w
print '\n'

hw = 'Hello World'
C_hw = hw.upper()
fid = open('test.dat','w')
for i in range(len(C_hw)):
    print C_hw[i]
    fid.write(C_hw[i])
    fid.write('\n')
fid.close()

print 'Finished writing Hellow World to a file!'
