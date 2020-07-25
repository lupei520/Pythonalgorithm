import random
from fractions import Fraction
import pickle
q=[]
ans=[]
def ContentOne(count,min_number=1,max_number=20):
    while(count):
        symbol=random.choice(["+","-","*","/"])
        if(symbol=="+"):
            n1=random.randint(min_number,max_number)
            n2=random.randint(min_number,max_number)
            user_answer=int(input("%s+%s=" %(n1,n2)))
            if(user_answer==n1+n2):
                print("回答正确!")
            else:
                print("%s+%s=%s" %(n1,n2,n1+n2))
        elif(symbol=="-"):
            n1=random.randint(min_number,max_number)
            n2=random.randint(min_number,max_number)
            n1,n2=max(n1,n1),min(n1,n2)
            user_answer=int(input("%s-%s=" %(n1,n2)))
            if(user_answer==n1-n2):
                print("回答正确!")
            else:
                print("%s-%s=%s" %(n1,n2,n1-n2))
        elif(symbol=="*"):
            n1=random.randint(min_number,max_number)
            n2=random.randint(min_number,max_number)
            user_answer=int(input("%s*%s=" %(n1,n2)))
            if(user_answer==n1*n2):
                print("回答正确!")
            else:
                print("%s*%s=%s" %(n1,n2,n1*n2))
        elif(symbol=="/"):
            n1=Fraction(random.randint(min_number,max_number))
            n2=Fraction(random.randint(min_number,max_number))
            user_answer=Fraction(input("%s/%s=" %(n1,n2)))
            if(user_answer==n1/n2):
                print("回答正确!")
            else:
                print("%s/%s=%s" %(n1,n2,n1/n2))
        count-=1;
def ContentTwo_read(count,min_number=1,max_number=20):  #两个分数的四则运算
    while(count):
        symbol = random.choice(['+', '-', '*', '/'])  # 生成随机符号
        if symbol == '+':
            n1 = random.randint(min_number,max_number)
            n2 = random.randint(min_number,max_number)
            q.append(str(n1) + '+' + str(n2) + '=')
            ans.append(n1 + n2)
        elif symbol == '-':
            n1 = random.randint(min_number,max_number)
            n2 = random.randint(min_number,max_number)
            n1,n2 = max(n1,n1),min(n1,n2)#防止出现负数
            q.append(str(n1) + '-' + str(n2) + '=')
            ans.append(n1 - n2)
        elif symbol == '*':
            n1 = random.randint(min_number,max_number)
            n2 = random.randint(min_number,max_number)
            q.append(str(n1) + '×' + str(n2) + '=')
            ans.append(n1 * n2)
        else:
            n1 = random.randint(min_number,max_number)
            if n1 == 0:
                n2 = random.randint(min_number,max_number)
            else:
                n2 = random.randint(min_number,max_number)
            q.append(str(n1) + '÷' + str(n2) + '=')
            ans.append(Fraction(n1, n2))
        count-=1;
    f1=open("OPASWXXS.data","wb")
    pickle.dump(ans,f1)
    f1.close()
    f=open("小学生快乐文档.txt","w",encoding="utf-8")
    count=1
    count_x=1
    for i in q:
        f.write("%s\t|" %i)
        if(count==4):
            #f.write("\t\t\t%s\n" %str(count*count_x))
            f.write("\t\t\t%s-%s-%s-%s\n" %(str((count*count_x)-3),str((count*count_x)-2),str((count*count_x)-1),str(count*count_x)))
            count_x+=1
            count=0
        count+=1
    f.close()
def ContentTwo_checkup(file="小学生快乐文档.txt"):
    f=open(file,"r",encoding="utf-8")
    count=0
    user_answer=[]
    for line in f:
        while(count<4):
            get=line.split("|")[count]
            get=get.replace("\t","").replace(" ","")
            #print(get)
            get=get.split("=")[-1]
            user_answer.append(get)
            count+=1
        count=0
        #print(get)
    count=0
    f=open("OPASWXXS.data","rb")
    ans=pickle.load(f)
    f.close()
    for i in user_answer:
        try:
            if(Fraction(i)==ans[count]):
                print("第%s题正确!" %str(count+1))
            else:
                print("第%s道题正确答案为：%s" %(str(count+1),ans[count]))
        except ValueError:
            print("未做第%s道题!" %str(count+1))
        finally:
            count+=1
def ContentTwo_AIWrite(file="小学生快乐文档.txt"):
    f=open(file,"r",encoding="utf-8")
    count=0
    question=[]
    for line in f:
        while(count<4):
            get=line.split("|")[count]  #获取题目
            get=get.replace("\t","").replace(" ","")  #处理题目
            question.append(get)
            #print(get)
            count+=1
        count=0
    count=0
    #开始填写答案
    f.close()
    f1=open(file,"w",encoding="utf-8")
    count=1
    count_x=1
    for i in question:
        i=i.replace("=","")
        if("+" in i):
            n1,n2=i.split("+")
            n1=Fraction(n1)
            n2=Fraction(n2)
            answer=n1+n2
            f1.write("%s+%s=%s\t\t|" %(n1,n2,answer))
        elif("-" in i):
            n1,n2=i.split("-")
            n1=Fraction(n1)
            n2=Fraction(n2)
            answer=n1-n2
            f1.write("%s-%s=%s\t\t|" %(n1,n2,answer))
        elif("×" in i):
            n1,n2=i.split("×")
            n1=Fraction(n1)
            n2=Fraction(n2)
            answer=n1*n2
            f1.write("%s×%s=%s\t\t|" %(n1,n2,answer))
        elif("÷" in i):
            n1,n2=i.split("÷")
            n1=Fraction(n1)
            n2=Fraction(n2)
            answer=n1/n2
            f1.write("%s÷%s=%s\t\t|" %(n1,n2,answer))
        if(count==4):
            f1.write("\t\t\t%s-%s-%s-%s\n" %(str((count*count_x)-3),str((count*count_x)-2),str((count*count_x)-1),str(count*count_x)))
            count_x+=1
            count=0
        count+=1
#ContentTwo_read(100)
#ContentTwo_AIWrite()
ContentTwo_checkup()