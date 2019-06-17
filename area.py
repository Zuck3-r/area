print("面積を求めます。以下の１～から選んでください")
print("１：四角形")
print("２：三角形")
print("３：円")
print("４：台形")
print("５：ひし形")
print("６：平行四辺形")

n= int(input())

if n==1:
	x=int(input("縦："))
	y=int(input("横："))
	print("面積:"+str(x*y))
elif n==2:
	x=int(input("底辺："))
	y=int(input("高さ："))
	print("面積："+str(x*y/2))
elif n==3:
	r=int(input("半径："))
	print("πは3.14で計算します")
	pi=3.14	
	print("面積："+str(r*r*pi))
elif n==4:
	x=int(input("上底："))
	y=int(input("下底："))
	z=int(input("高さ："))
	print("面積："+str((x+y)*z/2))
elif n==5:
        x=int(input("対角線："))
        print("面積："+str(x*x/2))
elif n==6:
	x=int(input("底辺："))
	y=int(input("高さ："))
	print("面積："+str(x*y))
