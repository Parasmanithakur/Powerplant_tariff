

from matplotlib import pyplot as plt 
#for ploting graph matplotlib lib is used
maxdemand =float(input("Enter Max Demand "))
#user is expected to give max demand value in kw
    
minLf =float(input("Enter the least lf "))
#least lf is asked from user rg0.75,0.68etc
tarif =float(input("Enter Rs/kwh value "))
#tarif is asked from user rg 1,2.02,1.07 etc
LF=[]
CF=[]
temp=minLf
#making a list of load factor from least lf
while temp<1:
    
    LF.append(temp)
    temp=temp+0.01


temp=0.85
#assuming power factor of 0.85 and making a list of powerfactor from this
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
            if ("%.2f" % cf)=='1.00':
               cf4.append(tarif*units/(maxdemand/cf))             
            print("  power Factor" +str("%.2f" % cf))
            
            print("    -Rs/kva"+ str("%.2f" % (tarif*units/(maxdemand/cf))))
                       
fun()
#now we just use lib to plot graph for visualization of data
plt.plot(LF,cf1,'b--.',label='pf-0.85')
plt.plot(LF,cf2,label='pf-0.90')
plt.plot(LF,cf3,label='pf-0.95')
plt.plot(LF,cf4,label='pf-1')

plt.ylabel('Tarif (Rs/kva)')
plt.xlabel('Load factor')
plt.title('Tarif by LF')
plt.legend()
plt.show()

    
