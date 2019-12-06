a=input('请输入一个距离：')
f=open('xyz.dat','r')
lines=f.readlines() # 此行代码是把文件xyz.dat数据读成数组
print("xyz.dat文件里有%s行数据"%len(lines))
for line in lines:
    name=line.split(',')[0]
    x=line.split(',')[1]
    y=line.split(',')[2]
    xy=((float(x)-116.404269)**2+(float(y)-39.914714)**2)**0.5
    print('点名是:%s,x是:%s,y是%s,距离是:%s'%(name,x,y,xy))
    if xy>float(a):
        print('点%s在距离之外'%name)
    elif xy==float(a):
        print('点%s等于距离'%name)
    else:
        print('点%s在距离之内'%name)