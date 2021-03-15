

from matplotlib import pyplot as plt
maxdemand =float(input("Enter Max Demand "))

    
minLf =float(input("Enter the least lf "))

tarif =float(input("Enter Rs/kwh value "))
LF=[]
CF=[]
temp=minLf

while temp<1:
    
    LF.append(temp)
    temp=temp+0.01


temp=0.85
while temp<1:
     CF.append(temp)
     temp=temp+0.05

cf1=[]
cf2=[]
cf3=[]
def fun():
    
  
    for lf in LF:
        print("-------------")
        print("For Load Factor "+str("%.2f" %  lf))
        units=maxdemand*lf*8760
        print("Units "+str(units) +"KWH")
        for cf in CF:

            if cf==0.85:
               cf1.append(tarif*units/(maxdemand/cf))
            if cf==0.90:
               cf2.append(tarif*units/(maxdemand/cf))   
            if ("%.2f" % cf)=='0.95':
               cf3.append(tarif*units/(maxdemand/cf))             
            print("  power Factor" +str("%.2f" % cf))
            
            print("    -Rs/kva"+ str("%.2f" % (tarif*units/(maxdemand/cf))))
                       
fun()

plt.plot(LF,cf1,label='pf-0.85')
plt.plot(LF,cf2,label='pf-0.90')
plt.plot(LF,cf3,label='pf-0.95')
plt.ylabel('Tarif (Rs/kva)')
plt.xlabel('Load factor')
plt.title('Tarif by LF')
plt.legend()
plt.show()

    