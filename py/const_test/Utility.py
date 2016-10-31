def GenerateInFile(class_num, const_num):
    f = open('ConstInFile.py', 'wb')
    for i in range(class_num):
        for j in range(const_num):
            #print 'CLASS_%d_CONST_%d' % (i, j)
            f.write('CLASS_%d_CONST_%d = %d\n' % (i, j, i*5 + j))
        f.write('\n')
    f.close()

def GenerateInClass(class_num, const_num):
    f = open('ConstInClass.py', 'wb')
    for i in range(class_num):
        f.write('class CLASS_%d():\n' % i)
        for j in range(const_num):
            f.write('\tCONST_%d = %d\n' % (j, (i*5+j)))
        f.write('\n')
    f.close()