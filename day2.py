i = float(input("plesae enter the profit"))

if i > 100:
	print(((i-100)*0.01+40*0.015+20*0.03+20*0.05+10*0.075+10*0.1)*10000)
elif 60< i <= 100:
	print(((i-60)*0.015+20*0.03+20*0.05+10*0.075+10*0.1)*10000)
elif 40< i <= 60:
	print(((i-40)*0.03+20*0.05+10*0.075+10*0.1)*10000)
elif 20< i <= 40:
	print(((i-20)*0.05+10*0.075+10*0.1)*10000)
elif 10< i <= 20:
	print(((i-10)*0.075+10*0.1)*10000)
elif i <=10:
	print((i*0.1)*10000)
	
# yishang wei wo xie de choulou de daima 

#yixiawei taren xia de jianjie de 
i = int(input('Enter the profit:'))
arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0
for idx in range(0,6):
	if i>arr[idx]:
		r+=(i-arr[idx])*rat[idx]
		print((i-arr[idx])*rat[idx])
		i=arr[idx]
print(r)