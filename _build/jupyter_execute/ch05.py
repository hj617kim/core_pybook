#!/usr/bin/env python
# coding: utf-8

# # 파이썬 프로그래밍의 기초 III

# ## 제어문

# 프로그램 실행의 흐름을 제어하는 명령문을 살펴보자. 
# 
# * `if` 조건문
# * `for` 반복문
# * `while` 반복문

# ### `if` 조건문

# `if` 조건문을 사용하면, 특정 조건 하에서만 어떤 코드가 실행되게 할 수 있다. 예를 들어, "이런저런 경우(조건)에만 무엇무엇을 해라"는 `if`문으로 나타낼 수 있으며, 아래의 형식을 따른다.  
# 
# ```
# if 이런저런 :
#     무엇무엇
# ```

# :::{admonition} 주의    
# :class: caution   
# `if` 조건문 뒤에 반드시 콜론(`:`)을 사용해야 하며, `무엇무엇`은 반드시 들여쓰기<font size = "2">indentation</font> 해야 한다. 들여쓰기를 하지 않으면 오류가 발생한다.     
# :::

# :::{admonition} 블록<font size = "2">block</font>  
# :class: info  
# 프로그래밍에서 블록은 특정한 일을 수행하는 한 단위의 코드 묶음을 말한다. 보통 중괄호(`{}`)로 묶여 있는 경우가 많으나 파이썬에서는 들여쓰기<font size = "2">indent</font>로 블록을 지정한다. 이때 들여쓰기는 공백<font size = "2">space</font> 4칸을 권장한다.     
# :::

# 예를 들어, x가 0보다 작을 때만, `x is negative`를 출력하는 코드를 작성해보자.  

# In[1]:


x = -10

if x < 0 :
    print('x is negative')
    
print('Here!')


# `if` 다음에 위치한 조건이 참이면 해당 블록의 코드를 실행하고, 거짓이면 해당 본문 블록을 건너뛴다.   

# In[2]:


x = 10

if x < 0 :
    print('x is negative')
    
print('Here!')


# :::{admonition} `pass` 명령문   
# :class: info  
# `pass` 명령문은 아무 것도 하지 않고 다음으로 넘어 가도록 하는 명령문이다.   
#   
# `if` 조건문이 참일 때 실행할 코드를 작성하지 않으면 오류가 발생한다. 
# 
# ```python
# >>> if x < 0 :
#   File "/tmp/ipykernel_981/2079685468.py", line 3
#     if x < 0 :
#               ^
# SyntaxError: unexpected EOF while parsing
# ```
# 
# x가 0보다 작을 때 할 일을 다음에 지정하고자 할 때는 `pass` 명령문을 사용할 수 있다. 
# ```python
# >>> if x < 0 :
#         pass
# ```
# :::
# 

# 조건문이 참(`True`)이면 `무엇무엇1`과 `무엇무엇2`를 실행하고, 조건문이 거짓(`False`)이면 `무엇무엇3`과 `무엇무엇4`를 실행하라고 할 때는 `if-else`문을 사용할 수 있다. `if-else`문은 아래의 형식을 따른다.  
# 
# ```
# if 조건문 : 
#     무엇무엇1
#     무엇무엇2
# else :
#     무엇무엇3
#     무엇무엇4
# ```

# :::{admonition} 들여쓰기 깊이  
# :class: caution  
# 파이썬은 들여쓰기에 민감한 언어이다. 위의 `if-else`문의 경우, `if`와 `else`의 들여쓰기 깊이가 같아야 하고, `if`와 `else` 아래 실행할 코드들(`무엇무엇2`, `무엇무엇1`, `무엇무엇3`, `무엇무엇4`)도 들여쓰기 깊이가 같아야 한다. 
# :::
# 
# 

# 예를 들어, x가 0보다 작으면 `x is negative`를 출력하고, 아니면 `x is non-negative`를 출력하는 코드를 작성해보자. 

# In[3]:


x = 10

if x < 0 :
    print('x is negative')
else :
    print('x is non-negative')


# :::{admonition} 조건부 표현식<font size="2">conditional expression</font>  
# :class: info  
# 조건부 표현식을 사용하면, `if-else`문을 다음과 같이 한 줄에 간단히 표현할 수 있다.  
# 
# ```
# 'x is negative' if x < 0 else 'x is non-negative'
# ```  
# :::
# 

# 여러 조건을 사용해야 하는 경우에는 `if-else`문을 중첩해서 사용하거나 `if-elif-else`처럼 다중 조건문을 사용할 수 있다.  
# 예를 들어, x가 0보다 작으면 `x is negative`를, x가 0보다 크면 `x is positive`를, 둘 다 아니면 `x is zero`를 출력하는 코드를 작성해보자.  

# In[4]:


x = 10

if x < 0 :
    print('x is negative')
elif x > 0 :
    print('x is positive')
else :
    print('x is zero')


# 위에 위치한 조건문의 참거짓 여부부터 조사하며, 한 곳에서 만족되면 나머지 부분은 무시된다. `elif`문은 원하는 만큼 사용할 수 있고, `else`문은 마지막에 한 번 사용하거나 생략할 수 있다.  

# ### `for` 반복문

# 반복문(루프)는 동일한 코드를 반복해서 실행시킬 때 사용한다. 반복문을 만들기 위해 `for`문과 `while`문을 사용할 수 있다. 여기서는 `for` 반복문을 먼저 살펴보고, 이후에 `while` 반복문을 살펴본다. 

# `for`반복문은 리스트, 튜플, 문자열과 같은 이터러블 자료형의 값에 포함된 항목을 순회하는 데 사용할 수 있으며, 아래의 형식을 따른다.  
# 
# ```
# for 항목변수 in 리스트(또는 튜플, 문자열 등) :
#     코드1
#     코드2
# ```

# 예를 들어, 리스트`[1, 3, 5]`에 포함된 항목들의 제곱을 출력하는 코드를 작성해보자. 

# In[5]:


for i in [1, 3, 5] :
    print(i, '의 제곱은', i**2, '이다.')


# :::{admonition} 참고  
# :class: info  
# 
# 항목변수는 임의로 만들어 사용할 수 있다. 단, `for` 반복문을 사용한 다음, 항목변수`item`의 값을 확인하면 `5`가 출력된다.   
# ```python
# >>> for item in [1, 3, 5] :
#         print(item, '의 제곱은', item**2, '이다.')
# 1 의 제곱은 1 이다.
# 3 의 제곱은 9 이다.
# 5 의 제곱은 25 이다.
# 
# >>> print(item)
# 5
# ```
# 
# 반복을 위해 사용하는 변수의 값을 무시하고 싶다면 밑줄기호(`_`)를 사용할 수 있다. 
# ```python
# >>> for _ in [1, 3, 5] :
#         print(_, '의 제곱은', _**2, '이다.')
# 1 의 제곱은 1 이다.
# 3 의 제곱은 9 이다.
# 5 의 제곱은 25 이다.
# ```
# :::
# 

# `for`문을 튜플, `range`, 문자열과 함께 사용해보자. 

# In[6]:


for tup in (1, 3, 5, 7) :
    print(tup)


# In[7]:


for i in range(5) :
    print(i)


# 아래 코드는 문자열에 포함된 문자 각각을 출력한다. 

# In[8]:


for s in 'Hello' :
    print(s)


# In[9]:


a_word = 'Hello'
for i in range(len(a_word)) :
    print(a_word[i])


# :::{admonition} `continue` 명령문   
# :class: info  
# 
# 반복문이 실행되는 도중에 `continue` 명령문을 만나면, 순간 실행되는 코드의 실행을 멈추고 다음 순번 항목을 대상으로 반복문을 이어간다. 예를 들어, `range(5)`에 포함된 항목 중에서 `3`을 제외한 값들을 출력하고 싶다면 아래와 같이 코드를 작성할 수 있다. 
# 
# ```python
# >>> for i in range(5) :
#         if i == 3 :
#             continue
#         print(i)
# 0
# 1
# 2
# 4
# ```
# :::
# 

# :::{admonition} `break` 명령문   
# :class: info  
# 반복문이 실행되는 도중에 `break` 명령문을 만나면, 순간 실행되는 반복문 자체의 실행을 멈추고, 가장 가까이서 둘러싸는 하나의 루프(`for` 반복문 또는 `while` 반복문)로부터 빠져나간다. 예를 들어, `range(5)`에 포함된 항목 중에서 `3`을 만나는 순간 출력을 멈추게 하려면 다음과 같이 코드를 작성할 수 있다.  
# 
# ```python
# >>> for i in range(5) :
#         if i == 3 :
#             break
#         print(i)
# 0
# 1
# 2
# ```
# 
# `break` 명령문은 가장 가까이 있는 루프를 빠져나가며, 또 다른 반복문에 의해 감싸져 있다면 해당 반복문을 이어서 실행한다. 
# ```python
# >>> for i in range(4) :
#         for j in range(4) :
#             if j == 2 :
#                 break
#             print(i, j)
#         print('='*5)
# 0 0
# 0 1
# =====
# 1 0
# 1 1
# =====
# 2 0
# 2 1
# =====
# 3 0
# 3 1
# =====
# ```
# :::

# ### `while` 반복문

# `while`반복문은 주어진 조건이 참(`True`)이 만족되는 동안이나 `break` 명령문을 만날 때까지 동일한 코드를 반복시킬 때 사용할 수 있으며, 아래의 형식을 따른다.   
# 
# ```
# while 조건 : 
#     코드1
#     코드2
# ```

# 예를 들어, `안녕하세요`를 5번 출력하는 코드를 작성해보자. 

# In[10]:


n = 0
while n < 5 :
    print('안녕하세요.')
    n += 1


# ````{prf:example}
# :label: loop-example1
# 
# 1에서 7까지의 정수를 출력하는데, 3의 배수는 정수 대신 `짝`을 출력하는 코드를 작성하여라. 
# ````

# In[11]:


n = 0
while n < 7 :
    n += 1
    if n % 3 == 0 :
        print('짝')
        continue
    print(n)


# :::{admonition} 주의  
# :class: caution  
# `while`반복문을 사용할 때는 조건문이 언젠가는 만족되지 않아서 더 이상 루프가 돌지 않도록 코드를 작성하는 것이 중요하다. 예를 들어, 아래의 코드는 종료 조건을 만족할 수 없어 무한으로 코드를 반복하는 무한 루프<font size = "2">infinite loop</font>가 발생한다. n이 3이되면 `continue` 명령문을 만나고, 그 다음 반복을 실행하지만 여전히 n에는 3이 있기 때문이다.  
# 
# ```python
# >>> n = 1
# >>> while n < 8 :
#         if n % 3 == 0 :
#             continue
#         print(n)
#         n += 1
# KeyboardInterrupt                         Traceback (most recent call last)
# /tmp/ipykernel_1504/1015293582.py in <module>
#       1 n = 1
# ----> 2 while n < 8 :
#       3     if n % 3 == 0 :
#       4         continue
#       5     print(n)
# 
# KeyboardInterrupt: 
# ```
# :::
# 

# 위의 코드는 아래와 같이 `for`문을 사용하여 작성할 수도 있다. 

# In[12]:


for n in range(1, 8) :
    if n % 3 == 0 :
        print('짝')
        continue
    print(n)


# ````{prf:example}
# :label: loop-example2
# 
# 리스트 `[1, 5, 10, 2, 4, 6, 3, 6, 9]`에 포함된 항목들의 합을 계산하는 과정 중에 3을 만나면 계산을 멈추고, 그때까지의 합을 출력하는 코드를 작성하여라. 
# ````

# In[13]:


sequence = [1, 5, 10, 2, 4, 6, 3, 6, 9]
total_until_3 = 0

for item in sequence :
    if item == 3 :
        break
    total_until_3 += item
    
print(total_until_3)


# In[14]:


sequence = [1, 5, 10, 2, 4, 6, 3, 6, 9]
total_until_3 = 0

n = 0
while n < len(sequence) :
    if sequence[n] == 3 :
        break
    total_until_3 += sequence[n]
    n += 1

print(total_until_3)


# ## 함수

# ### 함수 정의하기 
# 
# 그 동안 파이썬에서 이미 누군가에 의해 정의된 함수들(`type()`, `int()`, `float()`, `print()` 등등)을 살펴봤다. 이러한 함수들을 파이썬 **내장함수**라고 부른다. 한편, 사용자가 필요에 따라 함수를 임의로 정의할 수도 있다. 파이썬에서는 함수를 정의하기 위해 `def`라는 키워드를 사용하며, 아래의 형식을 따른다.  
# 
# ```
# def 함수이름(매개변수1, 매개변수2, ..., 매개변수n) :
#     함수본문
#     return 리턴값
# ```
# 
# **매개변수**는 함수에 입력으로 전달되는 값을 받는 변수이다.
# 함수본문에서 **`return`** 이라는 키워드에 도달하면 함수의 실행은 그 지점에서 중단되고, 리턴<font size = "2">return</font>값이 있는 경우에는 함수를 실행한 곳에 그 값을 반환한다. 이때, 리턴값은 `return` 바로 뒤에 오는 값이며, 함수가 특정 인자와 함께 실행되면 함수본문의 코드에 맞게 값을 조작한 후 최종적으로 돌려주는 값을 가리킨다.

# :::{admonition} 주의  
# :class: caution  
# 함수를 정의할 때, 괄호(`()`) 뒤에 콜론(`:`)을 반드시 사용해야 하며, 함수본문은 들여쓰기를 해야 한다. 들여쓰기는 선택이 아닌 의무사항이다.  
# :::
# 

# 예를 들어, 인자 두 개를 입력받아 그 합을 리턴하는 함수인 `my_sum()` 함수는 다음과 같이 정의한다. 함수의 이름은 임의로 정할 수 있지만 함수의 기능에 맞게 정하는 것이 좋다. 

# In[15]:


def my_sum(a, b) :
    return a + b


# 리턴값이 명시되지 않은 함수를 정의할 수 있으며, 그때 함수의 리턴값은 항상 `None`이다. 그리고 입력값이 없다면 아래와 같이 함수 이름 뒤의 괄호를 비워두면 된다. 
# 
# ```
# def 함수이름() :
#     함수본문
# ```

# 예를 들어, 입력값도 리턴값도 명시되지 않는 `say()` 함수를 아래와 같이 정의할 수도 있다. 

# In[16]:


def say() :
    print('Hello python!')


# 함수에는 다음과 같은 방식으로 타입 힌트를 추가한다. 
# 
# * 각각의 매개변수 옆에 콜론(`:`)을 적고 타입 힌트를 추가한다.  
# * 함수의 리턴값 타입은 함수명 괄호 뒤에 화살표 기호(`->`)를 적고 타입 힌트를 추가한다.   
# 
# 예를 들어, `my_sum()` 함수의 매개 변수는 모두 `float`이고, 리턴값도 `float`라면 다음과 같이 타입 힌트를 추가할 수 있다. 

# In[17]:


def my_sum(a : float, b : float) -> float :
    return a + b


# ### 함수 호출하기 

# 함수를 정의한 후에 사용하려면 **함수를 호출**해야 한다. **함수를 호출한다**는 말은 필요한 만큼의 값을 인자로 사용하여 함수를 실행한다는 의미이다. 즉, 함수 호출은 아래 모양의 코드를 실행하는 것이다.  
# 
# 함수를 호출할 때 전달하는 입력값들은 **인자**라고 부른다.  
# ```
# 함수이름(인자1, 인자2,..., 인자n)
# ```

# 예를 들어, 2와 3을 더한 값을 출력하려면 `my_sum()`함수를 아래와 같은 방식으로 호출하면 된다.

# In[18]:


print(my_sum(2, 3))


# 변수를 인자로 사용할 수도 있으며, 리턴값을 다른 변수에 저장할 수도 있다.

# In[19]:


x = 2
y = 3
z = my_sum(2, 3)
print(z)


# :::{admonition} 주의 
# :class: caution  
# 매개변수의 개수와 인자의 개수가 맞지 않으면 오류가 발생한다.  
# ```python
# >>> print(my_sum(3))
# TypeError                                 Traceback (most recent call last)
# /tmp/ipykernel_1887/3553718912.py in <module>
# ----> 1 print(my_sum(3))
# 
# TypeError: my_sum() missing 1 required positional argument: 'b'
# >>> print(my_sum(1, 2, 3))
# TypeError                                 Traceback (most recent call last)
# /tmp/ipykernel_1887/828772552.py in <module>
# ----> 1 print(my_sum(1, 2, 3))
# 
# TypeError: my_sum() takes 2 positional arguments but 3 were given
# ```
# :::
# 

# ## 이터러블과 이터레이터

# ### 이터러블

# 이터러블<font size = "2">iterable</font> 또는 이터러블 객체는 값을 한 번에 하나씩 돌려줄 수 있는 반복 가능한 객체로, `for` 반복문과 함께 사용될 수 있다.   
# 예를 들어, 모든 시퀀스 자료형(예, 리스트, 튜플, 문자열 등)은 이터러블하고, 시퀀스 자료형은 아니지만 사전 자료형도 이터러블하다.  

# In[20]:


for i in [1, 2, 3] :
    print(i)


# In[21]:


for k in {'a' : '에이', 'b' : '비'} :
    print(k)


# 이터러블 객체는 `__iter__()` 메서드를 가지고 있다.

# In[22]:


a_list = [1, 2, 3]
print(dir(a_list)) #dir() 함수를 사용하여 a_list가 어떤 메서드를 가지고 있는지 확인할 수 있다. 


# ### 이터레이터

# 이터레이터<font size = "2">iterator</font>는 값을 하나씩 꺼낼 수 있는 객체로, 이터러블의 `__iter__()` 메서드나 내장함수 `iter()`를 사용하여 이터레이터를 만들 수 있다. 

# In[23]:


a_list = [1, 2, 3]
a_iter = iter(a_list)
type(a_iter)


# 이터레이터의 `__next__()` 메서드나 내장함수 `next()`를 반복적으로 호출하면 값을 차례대로 돌려준다.    

# In[24]:


a_iter.__next__() 


# In[25]:


a_iter.__next__()


# In[26]:


a_iter.__next__()


# :::{admonition} 주의  
# :class: caution  
# 차례대로 이터레이터의 항목을 모두 꺼낸 다음에 `__next__()` 메서드를 실행하면 `StopIteration` 오류가 발생한다. 
# 
# ```python
# >>> a_iter.__next__()
# StopIteration                             Traceback (most recent call last)
# /tmp/ipykernel_79/31460938.py in <module>
# ----> 1 a_iter.__next__()
# 
# StopIteration: 
# ```
# :::
# 

# 이터레이터는 값을 바로 보여주지 않는다. 이터레이터의 항목은 리스트로 형변환하면 쉽게 확인할 수 있다. 

# In[27]:


a_list = [1, 2, 3]
a_iter = iter(a_list)
print(a_iter)
print(list(a_iter))


# :::{admonition} 참고  
# :class: info  
# `for`반복문을 사용할때마다 이터러블의 `__iter__()`메서드는 새로운 이터레이터 객체를 자동으로 만들어주기 때문에 사용자가 직접 이터레이터를 만들 필요는 없다.  
# 예를 들어, 아래와 같이 리스트를 이용하여 `for` 반복문을 실행하면 리스트의 `__iter__()` 메서드가 호출된다. 
# ```python
# >>> a_list = [1, 2, 3]
# >>> for item in a_list :
#         print(item)
# 1
# 2
# 3
# ```
# :::
# 

# ### 제너레이터 

# 제너레이터<font size = "2">generator</font>는 특별한 이터레이터로, `__iter__()`와 `__next__()` 메서드를 구체적으로 구현할 필요없이 간단하게 이터레이터를 정의할 수 있다. 제너레이터는 함수와 비슷한 방식으로 정의하지만 함수 안에 `return`키워드 대신 `yield` 키워드를 사용하여 생성해야 하는 값들을 지정한다는 점이 다르다.     

# 예를 들어, 1부터 n의 제곱을 생성하는 제너레이터는 아래와 같이 정의한다. 

# In[28]:


def squares(n) :
    for i in range(1, n + 1) :
        yield i ** 2


# In[29]:


gen = squares(5)
type(gen)


# 제너레이터는 지정된 값들을 바로 생성하지 않으며, 생성할 준비만 해두고 필요할 때 값을 생성하여 메모리를 보다 효율적으로 사용할 수 있다.   
# `__next__()` 메서드나 `next()` 함수를 사용하여 항목을 차례대로 가져올 수 있다.  

# In[30]:


gen.__next__()


# In[31]:


gen.__next__()


# In[32]:


next(gen)


# `for` 반복문에 사용하면 그때 필요한 항목을 하나씩 생성한다.  
# 앞에서 `1, 4, 9` 항목을 가져왔기 때문에 `16`과 `25`만 출력된 것을 볼 수 있다. 

# In[33]:


for x in gen :
    print(x, end = ' ')


# :::{admonition} 주의   
# :class: caution  
# 제너레이터도 `__next__()` 메서드가 모든 항목을 순회하면 더 이상 가리키는 값이 없다. 따라서 한 번 더 `for` 반복문을 사용했을 때, 아무 것도 출력하지 않는다. 
# 
# ```python
# >>> for x in gen :
#         print(x, end = ' ')
# ```
# 
# 동일한 제너레이터를 다시 사용하려면 제너레이터를 다시 생성해야 한다. 
# ```python
# >>> gen = squares()
# >>> for x in gen :
#         print(x, end = ' ')
# 1 4 9 16 25 
# ```
# :::
# 

# **제너레이터 표현식**  
# 제너레이터는 제너레이터 표현식을 사용하여 만들 수도 있다. 조건제시법과 유사하지만 소괄호(`( )`)로 감싸서 만든다. 

# In[34]:


squares = (i ** 2 for i in range(1, 6))
type(squares)


# :::{admonition} 주의  
# :class: caution  
# 소괄호로 감싸서 만들지만 튜플 자료형이 아니라 제너레이터이다. 
# :::
# 

# In[35]:


print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))


# ### 이터러블에 유용한 내장함수

# #### `enumerate()` 함수  
# `enumerate(iterable, start = 0)` : 카운트와 `iterable`의 항목을 튜플로 묶은 형태로 이터레이터를 만들어 반환한다. 카운트는 기본적으로 0부터 시작하고 다른 값부터 시작하고 싶다면 `start` 값을 변경해주면 된다. 

# In[36]:


seasons = ['봄', '여름', '가을', '겨울']
print(list(enumerate(seasons)))
print(list(enumerate(seasons, start = 10)))


# In[37]:


class_name = ['강현', '나현', '다현']
class_name_enum = enumerate(class_name, 1)

for num, name in class_name_enum :
    print(f'{num}번 학생은 {name}입니다.')


# #### `zip()` 함수

# 여러 개의 이터러블을 인자로 받아 각 항목을 튜플로 묶은 형태로 이터레이터를 만들어 반환한다. 

# In[38]:


data_zip = zip(['3월', '2월', '9월'], ['강현', '나현', '다현'])

for month, name in data_zip :
    print(f'{name}은 {month}달에 태어났다.')


# #### `all()` 함수    
# 
# 이터러블의 모든 항목이 참이거나 비어있으면 `True`, 아니면 `False`를 반환한다. 

# In[39]:


print(all([1, 3, 0, 2, 15])) # 0 == False은 True다.
print(all([1, 3, 2, 15]))


# #### `any()` 함수  
# 
# 이터러블의 항목 중 어느 하나라도 참이면 `True`, 아니면 `False`를 반환한다. 

# In[40]:


print(any((False, 1, False, False)))
print(any((False, 1 == 3, False, False)))


# #### `filter()` 함수  
# `filter(function, iterable)`은 `function`이 참을 반환하는 `iterable`의 요소들로 이터레이터를 만들어 반환한다.   

# In[41]:


def is_even(n) :
    if not n % 2 :
        return True
    else :
        return False

print(is_even(5))
print(is_even(10))


# In[42]:


num = [2, 8, 9, 3, 10, 12]
num_iter = filter(is_even, num)


# In[43]:


for item in num_iter :
    print(item, end = ' ')


# In[44]:


num_iter = filter(is_even, num)
list(num_iter)


# #### `map()` 함수  
# `map(function, iterable)` : `iterable`의 모든 항목에 `function`을 적용한 후 그 결과를 돌려주는 이터레이터를 반환한다.  

# In[45]:


def is_even(n) :
    if not n % 2 :
        return True
    else :
        return False


# In[46]:


num = [2, 8, 9, 3, 10, 12]
num_map = map(is_even, num)


# In[47]:


for item in num_map :
    print(item, end = ' ')

