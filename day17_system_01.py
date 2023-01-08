import sys


print(sys.argv)
for i in range(len(sys.argv)):
    if i==0:
        print("function name: {0}".format(sys.argv[0]))
        #print("function name %s" %sys.argv[0])
    else:
        print("{0}.argument: {1}".format(i,sys.argv[i]))
        #print("%d. argument: %s" %(i,sys.argv[i]))
##print(sys.version)
####3.11.0a5 (main, Feb  3 2022, 19:32:53) [MSC v.1929 64 bit (AMD64)]
##print(sys.version_info)
####sys.version_info(major=3, minor=11, micro=0, releaselevel='alpha', serial=5)
