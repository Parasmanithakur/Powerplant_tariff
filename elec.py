


maxdemand =float(input("Enter Max Demand "))

    
minLf =float(input("Enter the least lf "))

tarif =float(input("Enter Rs/kwh value "))
LF=[]
CF=[]
temp=minLf

while temp<1:
    temp=temp+0.01
    LF.append(temp)


temp=0.85
while temp<1:
     CF.append(temp)
     temp=temp+0.05


def fun():
    
  
    for lf in LF:
        print("-------------")
        print("For Load Factor "+str("%.2f" %  lf))
        units=maxdemand*lf*8760
        print("Units "+str(units) +"KWH")
        for cf in CF:
           
            print("  power Factor" +str("%.2f" % cf))
            
            print("    -Rs/kva"+ str("%.2f" % (tarif*units/(maxdemand/cf))))
                       
fun()
    