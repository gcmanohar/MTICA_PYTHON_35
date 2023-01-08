import sys
print("commimg through std_out")
#std_out is saved
save_stdout=sys.stdout
fpath=open(r"C:\Windows\System32\day17\day17.txt",'w')
sys.stdout=fpath
print("this line goes to day17.txt")
print(input())
#return to normal
sys.stdout= save_stdout
fpath.close()
