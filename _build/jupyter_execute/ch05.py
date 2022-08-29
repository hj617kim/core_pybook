#!/usr/bin/env python
# coding: utf-8

# # 기초 III(제어문, 함수, 이터러블과 이터레이터, 예외처리)

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
# 조건부 표현식은 `if-else` 조건문 형식을 빌려 조건에 따라 다른 값을 나타내는 표현식으로, 형식은 다음과 같다.  
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
# ```
# ```python
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
# >>> gen = squares(5)
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


print(all([1, 3, 0, 2, 15])) # 0 == False를 실행하면 True다. 0이 아닌 수는 True이다. 
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


# ## 예외처리

# 프로그램을 만들다보면 여러 오류가 발생할 수 있다. 파이썬은 오류가 발생하면 오류 메시지를 보여주며 프로그램을 중단한다. 하지만 때로는 오류를 다른 방식으로 처리하고 싶을 때도 있다. 여기서 그에 대한 해결책을 다루고자 한다.  

# ### 오류  
# 오류를 처리하는 방법을 살펴보기 전에, 프로그램을 만들 때 발생할 수 있는 오류 몇 가지를 살펴보자. 오류의 종류를 파악하면 어디서 왜 오류가 발생하였는지를 보다 쉽게 파악하여 코드를 수정할 수 있게 된다. 다음의 코드들은 모두 오류를 발생시킨다. 오류 메시지는 오류의 종류를 명시하고 있으며, 문제가 되는 줄을 다시 보여주고 문제가 되는 부분을 화살표로 가리키고 있다. 
# 

# :::{admonition} 문법 오류<font size="2">SyntaxError</font>  
# :class: caution  
# 아래의 코드에서 문자열 양 끝의 큰 따옴표(또는 작은 따옴표)는 짝이 맞아야 한다.  
# ```python  
# >>> print('Hello, world)
#   File "/tmp/ipykernel_739/1244210618.py", line 1
#     print('Hello, world)
#                         ^
# SyntaxError: EOL while scanning string literal
# ```  
# 아래의 코드에서 괄호는 짝이 맞게 작성해야 한다. 오류 메시지에서는 line2 시작 부분에서 오류가 발생했다고 나왔지만, 실제로는 line1 마지막에 괄호(`)`)가 없어서 발생한 오류이다.   
# ```python
# >>> print(type('3')
# >>> print('Hello, python')
#   File "/tmp/ipykernel_739/2346138518.py", line 2
#     print('Hello, python')
#     ^
# SyntaxError: invalid syntax
# ```
# :::  
# 

# :::{admonition} 0 나누기 오류<font size="2">ZeroDivisionError</font>    
# :class: caution   
# 어떤 값을 0으로 나누려고 하면, 아래와 같이 오류가 발생한다.   
# ```python
# >>> print(3/0)
# ZeroDivisionError                         Traceback (most recent call last)
# /tmp/ipykernel_739/3450647263.py in <module>
# ----> 1 print(3/0)
# 
# ZeroDivisionError: division by zero
# ```
# :::
# 

# :::{admonition} 들여쓰기 오류<font size="2">IndentationError</font>   
# :class: caution  
# 
# 2번 줄과 3번 줄의 들여쓰기 정도가 동일해야 한다. 
# ```python
# >>> for i in range(5) :
#       i -= 2
#         print(i)
#   File "/tmp/ipykernel_739/1686879996.py", line 3
#     print(i)
#     ^
# IndentationError: unexpected indent
# ```
# :::
# 

# :::{admonition} 자료형 오류<font size="2">TypeError</font>   
# :class: caution  
# 
# 정수와 문자열은 `+` 연산을 할 수 없다. 
# ```python
# >>> 3 + 'abc' 
# TypeError                                 Traceback (most recent call last)
# /tmp/ipykernel_739/2042041464.py in <module>
# ----> 1 3 + 'abc'
# 
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# ```
# :::
# 

# :::{admonition} 인덱스 오류<font size="2">IndexError</font>   
# :class: caution  
# 
# 인덱스는 문자열의 길이보다 작거나 같은 수만 사용할 수 있다. 
# ```python
# >>> a_word = 'Hello'
# >>> print(a_word[15])
# IndexError                                Traceback (most recent call last)
# /tmp/ipykernel_739/570418593.py in <module>
#       1 a_word = 'Hello'
# ----> 2 print(a_word[15])
# 
# IndexError: string index out of range
# ```
# :::

# :::{admonition} 값 오류<font size="2">ValueError</font>  
# :class: caution  
# 
# `int()`함수의 인자로 문자열을 사용할 때는 문자열의 모양이 정수 모양이어야 한다.   
# ```python
# >>> int('3.4')  
# ValueError                                Traceback (most recent call last)
# /tmp/ipykernel_739/1056813288.py in <module>
# ----> 1 int('3.4')
# 
# ValueError: invalid literal for int() with base 10: '3.4'
# ```
# :::
# 

# :::{admonition} 속성 오류<font size="2">AttributeError</font>     
# :class: caution  
# 
# 문자열(`str`)에 `split()`메서드를 사용하면, 리스트(`list`)가 된다. `strip()`은 문자열 메서드로 리스트 자료형에 사용할 수 없다.    
# ```python
# >>> 'Hello, python'.split().strip()
# AttributeError                            Traceback (most recent call last)
# /tmp/ipykernel_739/2431863669.py in <module>
# ----> 1 'Hello, python'.split().strip()
# 
# AttributeError: 'list' object has no attribute 'strip'
# ```
# :::

# 지금 살펴본 오류 외에도 다양한 오류가 발생할 수 있다. 그때마다 스스로 오류의 내용과 원인을 확인해 나가는 과정이 필요하다.  

# ### 예외처리

# 프로그램 중간에 오류가 발생할 수 있는 경우를 미리 생각하여 대비하는 과정을 **예외처리<font size="2">exception handling</font>** 라고 부른다. 예를 들어, 오류가 발생하더라도 오류발생 이전까지 생성된 정보들을 저장하거나, 오류 발생 이유를 조금 더 자세히 다루거나, 아니면 오류발생에 대한 보다 자세한 정보를 사용자에게 알려주기 위해 예외처리를 사용한다. 여기서는 `try-except`문을 사용하여 예외처리하는 방법을 살펴보자. 아래의 형식을 따른다.   
# 
# ```
# try : 
#     코드1
# except :
#     코드2
# ```
# 
# * `try`문을 만나면, 먼저 `코드1`(`try`와 `except` 사이의 코드들)부분을 실행한다.   
# * `코드1` 부분이 실행되면서 오류가 발생하지 않으면 `코드2`부분은 무시하고 다음으로 넘어간다. 
# * `코드1` 부분이 실행되면서 오류가 발생하면 더이상 진행하지 않고 바로 `코드2` 부분을 실행한다.   
# 
# 예제와 함께 살펴보자. 아래의 코드는 문법적 오류는 없지만, 정수가 아닌 값을 입력하면 값 오류<font size="2">ValueError</font>가 발생한다.  
# 
# ```python
# >>> int_num = int(input('정수를 입력하세요 : '))
# 정수를 입력하세요 :  3
# ```
# ```python
# >>> int_num = int(input('정수를 입력하세요 : '))
# 정수를 입력하세요 :  3.5
# ValueError                                Traceback (most recent call last)
# /tmp/ipykernel_739/4187675782.py in <module>
# ----> 1 int_num = int(input('정수를 입력하세요 : '))
# 
# ValueError: invalid literal for int() with base 10: '3.5'
# ``` 
# 
# 정수가 아닌 값을 입력하면, `'정수를 입력해야 합니다.'`라는 문구를 출력하고 싶다면 `try-except`문을 이용하여 예외처리할 수 있다.  
# ```python
# >>> num = input("정수를 입력하세요: ")
# >>> try :
#         int_num = int(num)
#         print("입력한 정수", int_num, "의 제곱은", int_num**2, "입니다.")
#     except :
#         print("정수를 입력해야 합니다.")
# 정수를 입력하세요:  3
# 입력한 정수 3 의 제곱은 9 입니다.
# ```
# ```python
# >>> num = input("정수를 입력하세요: ")
# >>> try :
#         int_num = int(num)
#         print("입력한 정수", int_num, "의 제곱은", int_num**2, "입니다.")
#     except :
#         print("정수를 입력해야 합니다.")
# 정수를 입력하세요:  3.5
# 정수를 입력해야 합니다.
# ```
# 
# 위의 코드에서 정수 3을 입력하면 입력한 정수의 제곱을 출력하고, 부동소수점 3.5를 입력하면 정수를 입력해야 한다는 메시지를 보여준다.   
# 
# `while`문을 사용하여 정수를 입력할 때까지 계속 입력을 요구할 수도 있다.   
# ```python
# >>> while True :
#         try :
#             int_num = int(input("정수를 입력하세요: "))
#             print("입력한 정수", int_num, "의 제곱은", int_num**2, "입니다.")
#             break
#         except :
#             print("정수를 입력해야 합니다.")
# 정수를 입력하세요:  3.5
# 정수를 입력해야 합니다.
# 정수를 입력하세요:  1.5
# 정수를 입력해야 합니다.
# 정수를 입력하세요:  5
# 입력한 정수 5 의 제곱은 25 입니다.
# ```

# 오류 종류에 맞추어 다양한 대처를 하기 위해서는 오류의 종류를 명시하여 예외처리를 하면된다. 형식은 아래와 같다. 
# ```
# try : 
#     코드1
# except 오류종류1:
#     코드2
# except 오류종류2:
#     코드3
# ```
# * `try`문을 만나면, 먼저 `코드1`(`try`와 `except` 사이의 코드들)부분을 실행한다.   
# * `코드1` 부분이 실행되면서 오류가 발생하지 않으면 `코드2`, `코드3` 부분은 무시하고 다음으로 넘어간다. 
# * `코드1` 부분이 실행되면서 `오류종류1`의 오류가 발생하면 더이상 진행하지 않고 바로 `코드2` 부분을 실행한다.   
# * `코드1` 부분이 실행되면서 `오류종류2`의 오류가 발생하면 더이상 진행하지 않고 바로 `코드3` 부분을 실행한다.   
# 
# 
# 예제와 함께 살펴보자. 0이 아닌 정수를 입력받은 다음, 10을 입력받은 수로 나눈 값을 출력하는 코드를 작성하려고 한다. 입력 값이 따라 값 오류`VauleError`와 0 나누기 오류`ZeroDivisionError`가 발생할 수 있다. 각각에 상응하는 방식으로 아래와 같이 예외처리를 해보자. `try`문 아래 코드에서 오류가 발생했을 때 `except`문이 여러 개 있다면, 가장 위에 있는 `except`문부터 오류의 종류가 일치하는지를 확인한다. 
# 
# ```python
# >>> num = input('0이 아닌 정수를 입력하세요 : ')
# >>> try :
#         int_num = int(num)
#         ans = 10 / int_num
#         print('결과는', ans, '입니다.')
#     except ValueError :
#         print('정수를 입력하세요.')
#     except ZeroDivisionError :
#         print('0은 입력할 수 없습니다.')
# 0이 아닌 정수를 입력하세요 :  3.5
# 정수를 입력하세요.   
# ```
# ```python
# >>> num = input('0이 아닌 정수를 입력하세요 : ')
# >>> try :
#         int_num = int(num)
#         ans = 10 / int_num
#         print('결과는', ans, '입니다.')
#     except ValueError :
#         print('정수를 입력하세요.')
#     except ZeroDivisionError :
#         print('0은 입력할 수 없습니다.')
# 0이 아닌 정수를 입력하세요 :  0
# 0은 입력할 수 없습니다. 
# ```
# 
# 오류 메시지의 내용까지 알고 싶다면, 오류 종류 옆에 `as 오류메시지변수`를 적어주면 된다. 예를 들어, 아래와 같이 오류 종류 옆에 `as e`라고 적고, 아래에서 오류 메시지를 출력할 수 있다. 
# ```python
# >>> num = input('0이 아닌 정수를 입력하세요 : ')
# >>> try :
#         int_num = int(num)
#         ans = 10 / int_num
#         print('결과는', ans, '입니다.')
#     except ValueError as e :
#         print(e)
#         print('정수를 입력하세요.')
#     except ZeroDivisionError as e :
#         print(e)
#         print('0은 입력할 수 없습니다.')
# 0이 아닌 정수를 입력하세요 :  3.5
# invalid literal for int() with base 10: '3.5'
# 정수를 입력하세요.   
# ```
# ```python
# >>> num = input('0이 아닌 정수를 입력하세요 : ')
# >>> try :
#         int_num = int(num)
#         ans = 10 / int_num
#         print('결과는', ans, '입니다.')
#     except ValueError as e :
#         print(e)
#         print('정수를 입력하세요.')
#     except ZeroDivisionError as e :
#         print(e)
#         print('0은 입력할 수 없습니다.')
# 0이 아닌 정수를 입력하세요 :  0
# division by zero
# 0은 입력할 수 없습니다. 
# ```

# :::{admonition} 주의  
# :class: caution  
# 오류 종류를 잘못 명시하면 예외처리가 제대로 동작하지 않는다.  
# 
# ```python
# >>> try :
#         a = 3 / 0
#     except ValueError :
#         print('This program stops here.')
# ZeroDivisionError                         Traceback (most recent call last)
# /tmp/ipykernel_739/1260866280.py in <module>
#       1 try :
# ----> 2     a = 3 / 0
#       3 except ValueError :
#       4     print('This program stops here.')
# 
# ZeroDivisionError: division by zero
# ```
# 실제로 발생 가능한 오류를 일으킨 다음, 오류 종류를 명시하는 것도 좋다. 
# 
# ```python
# >>> try :
#         a = 3 / 0
#     except ZeroDivisionError :
#         print('This program stops here.')
# This program stops here.
# ```
# :::

# :::{admonition} 참고  
# :class: info  
# 상황에 따라 `try`문은 `else` 또는 `finally`와 함께 사용할 수 있다. `else`는 `try`문 아래에서 오류가 발생하지 않았을 때 실행되고, `finally`은 `try`문 아래에서 오류가 발생했는가와 관계없이 실행된다.   
# 
# 아래와 같은 코드를 살펴보자. `try`문 아래 코드를 실행할 때 어떠한 오류도 발생하지 않는다. 그러면, `except` 아래 코드는 무시하고, `else`와 `finally` 아래 코드가 실행된다. 그리고 `try`문 밖에 있는 `print('E')`가 실행된다.  
# ```python
# >>> try :
#         print('A1')
#         print('A2')
#     except :
#         print('B')
#     else :
#         print('C1')
#         print('C2')
#     finally :
#         print('D')
#     print('E')
# A1
# A2
# C1
# C2
# D
# E
# ```
# 
# `try`문 아래 코드를 실행할 때 오류가 발생하면, 더이상 진행하지 않고 `except`아래 코드를 실행한다. 이후 `else` 아래 코드는 무시하고, `finally`아래 코드와 `print('E')`가 실행된다.
# ```python
# >>> try :
#         print('A1')
#         print(3 / 0)
#         print('A2')
#     except :
#         print('B')
#     else :
#         print('C1')
#         print('C2')
#     finally :
#         print('D')
#     print('E')
# A1
# B
# D
# E
# ```
# 
# 다음와 같이 `else` 아래 있는 코드에서도 오류가 발생할 수 있다. 그런 경우에는 `finally` 아래 코드가 실행된 다음에 오류가 발생한다. 이후 `print('E')`가 실행되지 않는다. 
# ```python
# >>> try :
#         print('A1')
#         print('A2')
#     except :
#         print('B')
#     else :
#         print('C1')
#         print(3 / 0)
#         print('C2')
#     finally :
#         print('D')
#     print('E')
# A1
# A2
# C1
# D
# ZeroDivisionError                         Traceback (most recent call last)
# /tmp/ipykernel_739/1541466067.py in <module>
#       6 else :
#       7     print('C1')
# ----> 8     print(3 / 0)
#       9     print('C2')
#      10 finally :
# 
# ZeroDivisionError: division by zero
# ```
# :::
# 

# :::{admonition} 주의  
# :class: caution  
# `try` 아래 있는 코드에서 `break`, `continue`, `return` 문을 만나도, `finally` 아래 있는 코드를 먼저 실행한 다음 실행한다. 예를 들어, `try`문 아래에서 `break`를 만나 `while`문을 바로 벗어나는 것이 아니라 `finally` 아래 있는 코드를 실행한 다음 `break`문을 실행한다. 
# 
# ```python
# >>> while True :
#         try :
#             break
#         finally :
#             print('A')
# A
# ```
# 
# `finally` 아래 `return`문이 있다면, 리턴값은 `try` 문 아래 리턴값이 아니라 `finally` 아래 리턴값이 된다. 
# ```python
# >>> def bool_return() :
#         try :
#             return True
#         finally :
#             return False
# >>> bool_return()
# False
# ```
# :::

# ### 예외 일으키기  
# 강제로 오류를 발생시키고 싶다면, `raise` 명령어를 사용하면 된다.   
# 
# ```python
# >>> raise
# RuntimeError                              Traceback (most recent call last)
# /tmp/ipykernel_739/2235509928.py in <module>
# ----> 1 raise
# 
# RuntimeError: No active exception to reraise
# ```
# 
# 오류 종류와 어떤 일이 있어났는지도 알려줄 수 있다. 예를 들어, 아래와 같이 `NameError`를 발생시킬 수 있다. 
# ```python
# >>> raise NameError
# NameError                                 Traceback (most recent call last)
# /tmp/ipykernel_739/1567631431.py in <module>
# ----> 1 raise NameError
# 
# NameError: 
# ```
# 그리고 오류 종류 옆에 괄호를 하고 문자열을 넣으면, 오류가 발생했을 때 그 문자열을 보여준다. 
# ```python
# >>> raise NameError('name error 발생')
# NameError                                 Traceback (most recent call last)
# /tmp/ipykernel_739/3044916970.py in <module>
# ----> 1 raise NameError('name error 발생')
# 
# NameError: name error 발생
# ```
# 

# :::{admonition} 코드의 안정성 문제    
# :class: caution  
# 문법 오류 또는 실행 중 오류가 발생하지 않더라도 코드의 안전성이 보장되지는 않는다. 즉, 오류가 발생하지 않더라도 코드를 실행했을 때 기대하는 결과가 나오지 않을 수도 있으니 주의해야 한다. 예를 들어, 아래의 코드는 입력받은 정수의 제곱을 출력해주는 코드를 제대로 구현하지 못하고 있다. 
# 
# ```python
# >>> int_num = int(input("정수를 입력하세요 : "))
# 정수를 입력하세요 : 3
# >>> print("입력한 정수", int_num, "의 제곱은", int_num, "입니다.")
# 입력한 정수 3 의 제곱은 3 입니다.
# ```
# :::
# 

# ## 연습문제

# ### 문제 
# 'racecar', '토마토', 'stats'와 같이 앞뒤를 뒤집어도 똑같은 문자열을 회문<font size = "2">palindrome</font>이라고 한다. 문자열이 주어질 때, 그 문자열이 회문이면 `Success`를, 아니면 `Fail`를 출력하는 코드를 작성하여라.  
#   
# Input : `racecar`  
# Output : `Success`  
#   
# Input : `tomato`  
# Output : `Fail` 

# ### 문제  
# 거꾸로 노래 부르기 좋아하는 청개구리는 아래와 같이 노래를 부른다.  
# 
# `끼토산 야끼토 로디어 냐느가 총깡총깡 서면뛰 를디어 냐느가`  
# 
# 문자열이 주어졌을 때, 공백을 단위로 각 단어를 거꾸로 출력하는 코드를 작성하여라.  
# 단, 특정 노래의 가사는 줄바꿈 없이 주어진다.  
# 
# Input : `lyrics = '산토끼 토끼야 어디로 가느냐 깡총깡총 뛰면서 어디를 가느냐'`  
# Output : `끼토산 야끼토 로디어 냐느가 총깡총깡 서면뛰 를디어 냐느가`  

# ### 문제  
# 카멜<font size = "2">camel</font> 표기법으로 작성된 문자열을 팟홀<font size="2">pothole</font> 표기법(또는 스네이크<font size="2">snake</font> 표기법)으로 변경하는 코드를 작성해보자.    
# 
# * 카멜 표기법 : 소문자로 시작하고, 이어지는 단어의 시작은 대문자로 작성하는 표기법. 예를 들어, `userName`, `printMessage`, `countA` 등. 
# 
# * 팟홀 표기법 또는 스네이크 표기법 : 모두 소문자를 사용하고, 단어 사이에 밑줄기호(`_`)를 사용하는 표기법. 예를 들어, `user_name`, `print_message`, `count_a` 등.   
#   
# 참고) `str.isupper()`메서드는 문자열이 대문자인지를 확인해준다.  
# ```python
# >>> 'A'.isupper()
# True
# >>> 'a'.isupper()
# False
# >>> 'Abc'.isupper()
# False
# ```
# 
# Input : `userName`  
# Output : `user_name`  
#   
# Input : `printMessage`   
# Output : `print_message`    

# ### 문제  
# $n!$<font size="2">팩토리얼factorial</font>은 $1\times2\times3\times ... \times n$ 을 의미한다. 자연수 `n`이 주어졌을 때, `n!`의 끝에 있는 0 <font size="2">terminal zeros</font>의 개수를 출력하는 코드를 작성하여라. `n`은 1보다 크고 100000보다 작은 자연수라고 가정하자.  
# 
# Input : `n = 5`     
# Output : `1`   
# 
# Input : `n = 10`    
# Output : `2`  
# 
# 참고) $5! = 120$, $10! = 3,628,800$   

# ### 문제   
# A대학의 일반차량에 대한 주차요금은 아래와 같다.   
# 
# * 2,000원/최초 30분, 초과 10분마다 500원, 1일(24시간) 최대 요금은 40,000원   
# 
# 일반차량에 대한 입출차 기록이 리스트로 주어졌을 때, 차량별로 주차시간과 주차요금이 정리된 코드를 작성하여라.   
# 
# * 차량번호는 차량 뒷번호 4자리를 기록하고, 동일한 차량번호는 없다고 가정한다.  
# * 시간은 24시간제를 아래와 같이 사용하고, 모든 차량은 00:00부터 23:59분 사이에 한 번씩만 입출차(`IN`/`OUT`) 한다고 가정한다.  
# * 잘못된 입력은 없다고 가정하고, 아직 출차하지 않은 차량에 대해서는 주차시간과 주차요금을 정리할 수 없다.  
# 
# Input : `['07:30 1234 IN', '07:35 2580 IN','08:15 0328 IN', '08:45 2580 OUT', '08:55 9876 IN', '09:20 9876 OUT','11:00 1597 IN', '15:15 1234 OUT', '21:30 0328 OUT']`   
# Output : `{'1234': {'IN': '07:30', 'OUT': '15:15', 'parking_duration': 465, 'parking_fee': 24000}, '2580': {'IN': '07:35', 'OUT': '08:45', 'parking_duration': 70, 'parking_fee': 4000}, '0328': {'IN': '08:15', 'OUT': '21:30', 'parking_duration': 795, 'parking_fee': 40000}, '9876': {'IN': '08:55', 'OUT': '09:20', 'parking_duration': 25, 'parking_fee': 2000}, '1597': {'IN': '11:00'}}`
# 
# 참고) 
# 
# |차량번호|입차시간|출차시간|주차시간(분)|주차요금(원)|
# |:------:|:------:|:------:|:----------:|:---------:|
# |1234|07:30|15:15|465|24000|
# |2580|07:35|08:45|70|4000|
# |0328|08:15|21:30|795|40000|
# |9876|08:55|09:20|25|2000|
# |1597|11:00|-|-|-|

# ### 문제   
# 어느 강좌의 수강생과 시험 점수가 주어졌을 때, 학점을 매기는 프로그램을 만들어보자.    
# * 수강생의 30% 이하가 A학점을 받을 수 있다.  
# * 수강생의 60% 이하가 A학점 또는 B학점을 받을 수 있다.  
# * A학점과 B학점이 아닌 나머지는 C학점이다. 
# * 최대한 좋은 성적을 부여한다. 예를 들어, 10명 중 3등을 했다면, B, C등의 학점도 가능하지만 A학점을 받는다고 가정한다.  
# 
# 입력으로 학생들의 이름과 점수가 두 줄로 들어오는 데, 각 줄의 항목은 공백으로 구분된다. 
# 
# Input :    
# ```  
# 강현 나현 다현 라현 미현 백현 서현 아현 지현 차현 태현 호현   
# 90 62 82 55 75 74 71 68 88 78 85 90  
# ```   
# 
# A, B, C 학점인 학생들의 리스트를 아래와 같은 형식으로 출력하는 데, 이때 각 리스트 항목의 순서는 중요하지 않다.   
# Output :  
# ```  
# A학점 :  ['강현', '지현', '호현']  
# B학점 :  ['다현', '미현', '차현', '태현']  
# C학점 :  ['나현', '라현', '백현', '서현', '아현']  
# ```  

# ### 문제   
# 독일 수학자인 콜라츠<font size="2">Collatz, L.</font>는 1937년에 아래 알고리즘을 얼마나 많이 반복하면 최종적으로 숫자 1에 다다를 것인가를 질문했다.   
# * 주어진 숫자가 짝수라면 2로 나눈다.   
# * 주어진 숫자가 홀수라면 3을 곱한 다음 1을 더한다.   
# 
# 실제로 숫자 7부터 시작해서 위 과정을 16번 반복하면 1에 다다른다.   
# 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1   
#  
# 반면에 숫자 128부터 시작하면 7번만 반복하면 된다.  
# 128, 64, 32, 16, 8, 4, 2, 1   
# 
# 콜라츠는 어떤 자연수로 시작하든지 반복작업이 언젠가는 끝난다고 추측했는데, 아직 언제 끝나는가는 수학적으로 알아내지 못했다. 이를 콜라츠 추측이라고 부른다.   
# 
# 자연수 n을 입력받아 위의 알고리즘을 몇 번 반복하면 1에 다다르는지를 아래와 같은 형식으로 반환하는 `collatz()` 함수를 정의하여라. 단, 100번이상 반복하는 경우 -1를 반환한다.   
# In : `collatz(128)`     
# Out : `(7)128->64->32->16->8->4->2->1`   
# 
# In : `collatz(171)`  
# Out : `(-1)`   

# ### 문제  
# 소수<font size="2">prime number</font>는 1보다 큰 자연수 중 1과 자기자신만을 약수로 가지는 수를 말한다. 예를 들어, 2, 3, 5, 7, 11, 13, 17, 19 등은 소수이다. 자연수 100보다 작은 소수를 생성하는 이터레이터를 만들어라.      

# ### 문제   
# A는 정수를 입력하는 일을 하고 있다. 이때 연속으로 같은 숫자를 입력하면 안되는데, 입력장치의 오류로 연속적으로 같은 숫자가 입력된 것을 발견하였다. A가 입력한 숫자 리스트를 인자로 받아 연속적으로 같은 숫자가 있다면 그 숫자는 하나만 남기고 나머지는 제거한 리스트를 반환하는 함수`disconti_num()`를 만들어라. 단, 입력의 순서는 유지되야 하고, 같은 숫자가 불연속적으로 여러 번 등장할 수 있다.     
# 
# Input : `disconti_num([2, 3, 3, 3, 1, 2, 5])`  
# Output : `[2, 3, 1, 2, 5]`   

# ### 문제  
# 여러 개의 다항식을 곱하는 프로그램을 만들어보자. 다항식은 각 항의 계수로 나타낼 수 있다. 예를 들어, `2`는 $2$를, `1 3 4`는 $1 + 3x + 4x^2$를, `0 4 0 1`은 $4x + x^3$을 의미한다.  
# 
# 입력의 첫 줄에는 다항식의 개수 N(0<N<5)이 주어진다. 그 다음에 들어오는 N개의 줄에는 각 줄마다 다항식의 계수가 공백으로 분리되어 주어진다. 단, 입력으로 주어지는 각 다항식의 계수는 모두 정수이며, 최고차항의 계수는 0이 아니다.   
# 
# 예를 들어, Input이 아래와 같다면, $(1 + 3x)(2 + 4x)3$을 의미하고, 전개하면 $6 + 30x + 36x^2$이므로 `6 30 36`을 출력하면 된다. 다항식의 개수로 0이하, 5이상을 입력하거나 각 다항식의 계수로 정수가 아닌 값을 입력하면, 올바른 값을 입력할 때까지 계속 입력을 받는다.        
# Input :  
# ```
# 3  
# 1 3  
# 2 4  
# 3  
# ```
# Output : `6 30 36`  

# ### 문제   
# 주어진 빙고판에서 빙고의 총 개수를 세는 프로그램을 만들어보자. 빙고판의 행의 개수와 열의 개수는 모두 2이상이고, 행의 개수와 열의 개수는 같다. 빙고판은 `o`와 `x`로만 이루어져 있으며, 빙고 여부는 `o` 기준으로 생각한다. 입력의 첫 줄에는 빙고판 크기 N이 주어진다. 그 다음에 들어오는 N개의 줄에는 `o`와 `x`가 공백으로 분리되어 입력되는데, 각각 N개 넘게 입력하면 N개를 입력할 때까지 계속 입력을 받는다.   
# 
# Input :  
# ```
# 5
# o o o o o 
# o o o o o 
# o o o o o 
# o o o o o 
# o o o o o
# ```
# Output : `Total number of bingo is 12`  
