#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello World !!!")


# In[3]:


money = True

if money == True:
    print("택시를 타자")
else:
    print("걸어 가자")
    


# In[8]:


money = 500

if money >= 5000:
    print("택시를 타자")
elif money >=1000:
    print("버스를 타자")
else:
    print("걸어가자")


# In[ ]:


#학생의 성적을 입력 받아서 
#점수가 90이상이면 "A학점입니다."
#점수가 80이상이면 "B학점입니다."
#점수가 70이상이면 "C학점입니다."
#점수가 60이상이면 "D학점입니다."
#나머지가 모두 "F학점입니다."


# In[11]:


score = int(input("학생의 점수는 몇 점입니까? "))

if score >=90:
    print("A 학점입니다")
    
elif score >=80:
    print("B 학점입니다")
    
elif score >=70:
    print("C 학점입니다")
    
elif score >=60:
    print("D 학점입니다")
else:
    print("F 학점입니다")


# In[12]:


#while


no = 10 

while no >= 0:
    print(no)
    no = no - 1


# In[17]:


prompt = "1. 덧셈 / 2. 뺄셈 / 3. 곱셈 / 4. 나눗셈 / 5. 종료"
no = 0


while no <= 4:
    print(prompt)
    no = int(input())
    
    


# In[19]:


#while문의 경우에는 반복 횟수가 정확하지 않을 경우가 많기 때문에 조건에서 뿐만이 아니라 중간에 반복을 종료 시키는 방법도 필요하다.

no = 0

while no <= 10:
    print(no)
    no = no + 1
    
no = 0

while True:
    print(no)
    no = no + 1
    
    if no > 10:
        break
        
    #무한반복이니 중간에 정지시킬 필요가 있다. 조건에다가 or break


# In[ ]:


no = 0


# In[29]:


no = 0 #살짝틀림
sum = 0

while True: 
    no % 3 == 0 
    sum = sum + no
    no = no + 3
    
    if no > 100:
          break
    
print(sum) 


# In[30]:


no = 1
sum = 0

while no <= 100: 
    if no % 3 == 0:
        sum = sum + no
    
    no = no + 1 #no += 1  java no++
    
print(sum)


# In[ ]:


# for 구문


# In[32]:


for i in [1,2,3,4,5,6,7,8,9,10]:
    print(i)


# In[40]:


math = [80, 90, 70, 70, 100]


j = 1
for i in math: 
    if i >= 90:
        print(j, "번째 학생은 합격입니다.")
    else:
        print(j, "번째 학생은 불합격입니다.")
        j += 1


# In[41]:


for i in [1,2,3,4,5,6,7,8,9,10]:
    print(i)


# In[44]:


for i in [1,2,3,4,5,6,7,8,9,10]:
    if i % 2 == 0:
           print(i)


# In[48]:


for i in [1,2,3,4,5,6,7,8,9,10]:
    if i % 2 != 0:
        continue
    print(i)


# In[49]:


#range함수

# 숫자를 자동으로 생성해준다. for문과 함께 사용되는 경우가 아주 많다. 


# In[51]:


print(range(1,11))


# In[55]:


for i in range(1,11): #두번째 수는 미만     
    print(i)


# In[62]:


# for 문으로 구구단 출력하기

for i in range(2,10): #i는 단을 표현
    for j in range(1,10):
           print(i*j, end ="\t")
    print()


# In[88]:


# range를 사용하여 100이하의 수중 짝수들만의 합계를 구하세요

sum = 0

for i in range(1, 101):
    i += 1
    if i % 2 ==0:
        sum += i
print(sum)


# In[91]:


#range는 (start, stop, step)  으로 사용한다.

#for i in range(11): #start를 생략 하면 0에서 시작
    # print(i)
    
for i in range(0,11,2): #stop을 생략하면 1씩 증가
     print(i)


# In[99]:


#리스트 축약/내포 list comprehension
#리스트를 좀 더 편리하고 직관적으로 만드는 방법이다. 

list1 = [1,2,3,4]

print(list1)

list2 = [num           for num in list1] 

print(list2)

list3 = [num*2           for num in list1]

print(list3)

list4 = [num           for num in list1    if num % 2 == 0]       # 3 2 1 

print(list4)


# In[111]:


no = 70

if no >= 70:
    print("합격입니다")
else:
    print("불합격입니다")   
    
    
print("합격입니다" if no>=80  else "불합격입니다. ")

