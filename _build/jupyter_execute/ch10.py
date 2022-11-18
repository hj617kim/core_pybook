#!/usr/bin/env python
# coding: utf-8

# # 재귀

# ## 재귀와 재귀함수

# 재귀<font size="2">recursion</font>는 "본래 있던 곳으로 다시 돌아온다"는 의미로, 주어진 문제를 해결하기 위해 자기자신을 이용하는 기법을 말하며, 함수 본문에 자기자신을 호출하는 함수를 **재귀 함수**<font size="2">recursive function</font>라고 부른다.   
# 
# 예를 들어, 자연수 `n`을 인자로 받아 `n`, `n-1`,... , `1`을 출력한 다음에 `발사!`를 출력하는 함수 `countdown()`을 재귀를 활용하여 정의해보자. 
#   * `n`이 0 이하인 경우 : `발사!` 출력 
#   * `n`이 양의 정수인 경우 : `n`을 출력한 다음 바로 `countdown(n - 1)` 호출

# In[1]:


def countdown(n) :
    if n <= 0 :
        print('발사!')
    else :
        print(n)
        countdown(n - 1)


# In[2]:


countdown(3)


# 위 코드를 보면, `n`이 양수인 경우 동일한 함수가 호출되지만 인자가 1씩 적어진다. 그리고 결국에는 인자가 `0`이 되어 실행이 멈춘다. 

# ## 재귀함수의 콜 스택

# 함수가 실행되는 동안 발생하는 모든 정보는 컴퓨터 메모리 상에서 **프레임**<font size="2">frame</font>형식으로 관리된다. 이때 프레임은 하나의 함수가 실행되는 동안 발생하는 지역 변수의 생성 및 값 할당, 할당된 값 업데이트 등을 관리한다. 함수의 실행과 함께 생성된 프레임은 함수의 실행이 종료되면 스택에서 사라진다.   

# 재귀 함수의 실행과정 동안에도 많은 프레임의 생성과 소멸이 발생하여, 경우에 따라 콜 스택의 변화가 매우 복잡해지기도 한다. 아래 그림은 `countdown(3)`을 호출했을 때의 콜 스택의 상태를 **스택 다이어그램**<font size="2">stack diagram</font>으로, `countdown(0)`이 호출되어 콜 스택이 가장 높게 쌓였을 때이다.  
# <div align="center">
#     <img src="https://raw.githubusercontent.com/hj617kim/core_pybook/master/images/ch10/call_stack01.png" style="width:800px;">
# </div> 
# 
# 스택 다이어그램의 변화는 다음과 같다. 
# * 프레임 생성 순서
# ```
# Global frame => countdown 프레임(인자 3) => countdown 프레임(인자 2) => countdown 프레임(인자 1) => countdown 프레임(인자 0)
# ```
# * 프레임 사멸 순서  
# ```
# countdown 프레임(인자 0) => countdown 프레임(인자 1) => countdown 프레임(인자 2) => countdown 프레임(인자 3) => Global frame
# ```
# 
# 실제로 위 코드의 전체 실행 과정을 <a width="800" height="500" frameborder="0" href="https://pythontutor.com/iframe-embed.html#code=def%20countdown%28n%29%20%3A%0A%20%20%20%20if%20n%20%3C%3D%200%20%3A%0A%20%20%20%20%20%20%20%20print%28'%EB%B0%9C%EC%82%AC!'%29%0A%20%20%20%20else%20%3A%0A%20%20%20%20%20%20%20%20print%28n%29%0A%20%20%20%20%20%20%20%20countdown%28n%20-%201%29%0A%20%20%20%20%20%20%20%20%0Acountdown%283%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false" style ='color : blue'>Python Tutor : 프레임의 생성과 사멸</a>에서 확인해보면 함수 호출이 발생할 때마다 프레임이 생성되고 또 함수의 실행이 완료될 때마다 해당 함수의 프레임이 사멸하는 것을 확인할 수 있다. 

# :::{admonition} 스택<font size="2">stack</font>, 콜 스택<font size="2">call stack</font>, 스택 다이어그램<font size="2">stack diagram</font>   
# :class: info  
# 프레임은 생성된 순서 역순으로 사멸한다. 즉, 가장 나중에 생성된 프레임이 가장 먼저, 가장 먼저 생성된 프레임이 가장 나중에 사멸한다. 이렇게 작동하는 구조가 **스택**<font size="2">stack</font>이기에 함수의 프레임으로 구성된 스택을 **콜 스택**<font size="2">call stack</font>이라 부른다. **스택 다이어그램**<font size="2">stack diagram</font>은 콜 스택의 변화를 다이어그램으로 표현한다.  
# :::

# ## 기저 조건와 무한 재귀

# 재귀 함수의 실행이 멈추려면 재귀 호출 과정에서 언젠가는 더 이상 자신을 호출하지 않아야 한다. `countdown()` 함수는 `0`과 함께 호출될 때 더 이상 재귀 호출을 하지 않는다. 이렇게 더 이상 재귀 호출이 발생하지 않도록 하는 경우를 **종료 조건** 또는 **기저 조건**<font size="2">base case</font>이라 한다. 즉, `countdown()` 함수의 기저 조건은 `n = 0`이다.  
# 반면에 아래 함수는 기저 조건을 갖지 않는다.   
# 
# ```
# def count_infinitely(n):
#     print(n)
#     count_infinitely(n+1)
# ```
# 
# `count_infinitely()` 함수를 호출하면 재귀 호출이 무한정 반복됨을 쉽게 알 수 있다. 이러한 상황을 **무한 재귀**<font size="2">infinite recursion</font>라 한다. 그런데 파이썬을 포함해서 대부분의 프로그래밍 언어는 재귀 호출의 무한 반복을 허용하지 않고 언젠가 아래와 같은 오류를 발생시키면서 실행을 중지시킨다.  
# ```
# RecursionError: maximum recursion depth exceeded while calling a Python object
# ```

# :::{admonition} 최대 재귀 한도   
# :class: info  
# 파이썬은 **최대 재귀 한도**<font size="2">Maximum recursion depth</font>를 정해 허용되는 재귀 호출의 최대 반복 횟수를 지정한다. 한도는 파이썬 버전과 운영체제에 등에 따라 다를 수 있으며 필요에 따라 조정하는 것도 가능하다.  
# 
# 사용하는 파이썬의 최대 재귀 한도는 다음 명령문으로 확인할 수 있다.   
# ```python
# >>> import sys
# >>> print(sys.getrecursionlimit())
# ```
# :::
# 

# 재귀 함수를 실행해서 무한 반복에 빠지거나 최대 재귀 한도를 벗어났다는 오류 메시지가 발생하면 다음 두 가지 사항을 확인해야 한다.   
# 
# * 기저 조건이 주어졌는가?  
# * 어떠한 경우에 기저 조건에 도달하는가?  
# 
# 하나라도 충족되지 않거나 확인할 수 없다면 해당 재귀 함수의 활용에 매우 주의를 기울여야 한다. 

# ## 재귀 시각화  
# 재귀를 이해하기 위해 재귀 알고리즘의 작동과정을 시각화해보자. 시각화를 위해 `turtle` 모듈을 이용한다. 예를 들어, `draw_spiral()`함수는 아래 그림과 같은 소용돌이를 그린다. 

# ```
# import turtle
# 
# def draw_spiral(my_turtle, line_len):
#     if line_len > 0:
#         my_turtle.forward(line_len)
#         my_turtle.right(90)
#         draw_spiral(my_turtle, line_len - 5)
# 
# 
# my_turtle = turtle.Turtle()
# my_screen = turtle.Screen()
# draw_spiral(my_turtle, 100)
# my_screen.exitonclick()  #스크린을 클릭할 때, 창이 닫아준다. 
# ```
# 
# 
# <div align="center"><img src="https://raw.githubusercontent.com/hj617kim/core_pybook/master/images/ch10/fractal_spiral.png" style="width:200px;"></div>
# 

# ## 재귀 활용 예제

# ### 계승함수

# 자연수 n이 주어졌을 때, n의 계승 또는 n 팩토리얼<font size="2">factorial</font>은 1부터 n까지의 곱으로, 기호로는 n!를 사용한다. n! = n × (n - 1)!이므로, n!을 계산하는 함수를 재귀를 이용하여 구현하면 다음과 같다.  
# 
# * 종료 조건 : `n == 0`  

# In[3]:


def factorial(n) :
    if n == 0 :
        return 1
    else :
        return n * factorial(n - 1)


# In[4]:


print(factorial(1))
print(factorial(3))
print(factorial(5))


# ### 피보나치 수열

# 피보나치 수열<font size="2">fibonacci sequence</font>은 첫째와 둘째 항이 1이고, 그 뒤의 항은 바로 앞에 있는 두 항의 합인 수열을 말한다.  
#   
# $1$, $1$, $2$, $3$, $5$, $8$, $13$, $21$, $34$, $55$, ...
# 
# 또는 
# 
# fibo($1$) = $1$, fibo($2$) = $1$, fibo($n + 2$) = fibo($n$) + fibo($n + 1$) $\forall n \in \mathbb{N}$

# * 종료 조건 : `n == 1 or n == 2`

# In[5]:


def fibo(n) :
    if n == 1 or n == 2:
        return 1
    else :
        return fibo(n - 1) + fibo(n - 2)


# In[6]:


print(fibo(1))
print(fibo(2))
print(fibo(4))
print(fibo(8))


# ## 재귀 문제점

# 재귀를 사용하면 간결하게 코드를 작성할 수 있으며, 때로는 어려운 문제가 간단하게 해결되기도 한다. 반면, 재귀 알고리즘은 실행에 많은 시간이 걸린다는 문제가 있다. 예를 들어, 재귀를 활용하여 정의한 피보나치 함수는 `fibo(7)`를 계산하기 위해 `fibo()`함수를 24번이나 호출하고 있다(아래 그림과 <a style = "color:blue;" href="https://pythontutor.com/iframe-embed.html#code=def%20fibo%28n%29%20%3A%0A%20%20%20%20if%20n%20%3D%3D%201%20or%20n%20%3D%3D%202%3A%0A%20%20%20%20%20%20%20%20return%201%0A%20%20%20%20else%20%3A%0A%20%20%20%20%20%20%20%20return%20fibo%28n%20-%201%29%20%2B%20fibo%28n%20-%202%29%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0Aprint%28fibo%287%29%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false">파이썬 튜터</a> 참고).  
# 
# <div align="center"><img src="https://raw.githubusercontent.com/hj617kim/core_pybook/master/images/ch10/fibo_01.png" style="width:800px;"></div>
# 
# 그렇다면 `fibo(8)`을 계산하기 위해 `fibo()` 함수를 몇 번이나 호출할까? 38번 정도를 호출한다. 이렇게 `fibo()` 함수는 인자가 커질수록 호출 횟수가 기하급수적으로 늘어난다. 사실 너무 커서 실질적으로 사용할 수 없다. 예를 들어, `fibo(100)`도 제대로 구하지 못한다.  

# ### 반복문 사용

# 보통 재귀적으로 해결할 수 있는 문제는 반복문을 사용하여 해결할 수 있다. `for` 반복문을 사용하여 피보나치 함수를 정의해보자.  

# In[7]:


def fibo2(n) :
    first = 1
    second = 1
    for _ in range(2, n) :
        first, second = second, first + second
    return second 


# In[8]:


print(fibo2(100))


# ### 메모이제이션   
# 메모이제이션<font size="2">memoization</font>은 한 번 호출되어 실행된 값을 저장해두고, 필요한 경우 다시 계산하지 않고 저장된 값을 사용하는 기법이다. 메모이제이션을 사용하여 피보나치 함수를 정의해보자.   
# * `memo_dict` : 기저 조건이 저장되어 있고, 이후 계산되는 피보나치 수를 저장한다. 

# In[9]:


memo_dict = {1:1, 2:1}

def fibo3(n) : 
    if n not in memo_dict :
        memo_dict[n] = fibo3(n - 2) + fibo3(n - 1)
    return memo_dict[n]


# In[10]:


print(fibo3(100))


# ## 연습 문제

# ### 문제 

# 독일 수학자인 콜라츠<font size="2">Collatz, L.</font>는 1937년에 아래 알고리즘을 얼마나 많이 반복하면 최종적으로 숫자 1에 다다를 것인가를 질문했다.   
# * 주어진 숫자가 짝수라면 2로 나눈다.   
# * 주어진 숫자가 홀수라면 3을 곱한 다음 1을 더한다.   
# ​
# 실제로 숫자 7부터 시작해서 위 과정을 16번 반복하면 1에 다다른다.   
# 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1   
#  
# 반면에 숫자 128부터 시작하면 7번만 반복하면 된다.  
# 128, 64, 32, 16, 8, 4, 2, 1   
# ​
# 콜라츠는 어떤 자연수로 시작하든지 반복작업이 언젠가는 끝난다고 추측했는데, 아직 언제 끝나는가는 수학적으로 알아내지 못했다. 이를 콜라츠 추측이라고 부른다.   
# ​
# 자연수 n을 입력받아 위의 알고리즘을 몇 번 반복하면 1에 다다르는지를 아래와 같은 형식으로 반환하는 `collatz()` 함수를 **재귀를 사용**하여 정의하여라.   
# In : `collatz(128)`     
# Out : `128->64->32->16->8->4->2->1`   

# ### 문제   
# 카탈란 수<font size="2">또는 카탈랑 수 Catalan number</font>는 아래와 같이 정의된 자연수의 수열로, 개수 세기 문제<font size="2">counting problem</font>들을 해결하는 과정에서 많이 나타난다. 
# 
# $1$, $1$, $2$, $5$, $14$, $42$, $132$, $429$, $1430$, $4862$, ... 
# 
# 음이 아닌 정수 $n$에 대해서, $n$번째 카탈란 수$C_n$는 다음과 같이 정의할 수 있다.  
# $$
# C_n = \frac{(2n)!}{n!(n + 1)!}
# $$
# 
# 

# 또, 카탈란 수는 다음과 같이 점화식으로 나타낼 수도 있다. 
# $$
# C_0 = 1,\quad C_{n+1} = \frac{2(2n + 1)}{n + 2} C_n
# $$
# 
# 

# n을 인자로 받아, n번째 카탈란 수를 반환하는 `catalan_number()` 함수를 정의하여라. 

# :::{admonition} 카탈란 수    
# :class: info  
# 
# 1. $n$쌍의 괄호로 만들 수 있는 올바른 괄호의 개수는 카탈란 수 $C_n$이다. 예를 들어, 3쌍의 괄호로 만들 수 있는 올바른 괄호 구조는 5개로, 아래와 같다.   
# `((()))`, `()(())`, `(())()`, `(()())`, `()()()`  
# 
# 2. $n + 2$각형을 $n$개의 삼각형으로 나누는 방법의 수는 카탈란 수 $C_n$이다. 예를 들어, 6각형을 4개의 삼각형으로 나누는 방법의 수는 14개로, 아래와 같다.   
# <div align="center"><img src="https://raw.githubusercontent.com/hj617kim/core_pybook/master/images/ch10/catalan_01.png" style="width:600px;"></div>
# :::
# 

# ### 문제  
# 
# 코흐 곡선<font size="2">Koch curve</font>는 프랙탈<font size="2">fractal</font> 중 하나로 다음과 같이 만든다.  
# 
# 1. 선분을 하나 그린다. 
# 2. 각 변을 3등분해서, 한 변의 길이가 그 3등분한 길이와 같은 정삼각형을 만든다. 이때 밑변은 없앤다. 
# 3. 2의 과정을 계속 반복한다.   
# 
# <div align="center"><img src="https://raw.githubusercontent.com/hj617kim/core_pybook/master/images/ch10/koch_curve_01.png" style="width:700px;"></div>
# 
# 코흐 눈송이는 시작하는 도형이 정삼각형이고, 각 변에 대해 코흐 곡선과 같은 과정을 반복한다.   
# 
# `turtle` 모듈을 이용하여 코흐 곡선과 코흐 눈송이를 그려라. 

# ### 문제   
# 하노이 탑<font size="2">Tower of Hanoi</font> 문제는 세 개의 탑 중에 하나의 탑에 쌓여 있는 다양한 크기의 원판들을 다른 탑으로 옮기는 게임이다. 단, 원판 이동 중에 아래 제한조건들은 반드시 지켜야 한다.  
# 
# * 한 번에 한 개의 원판만 옮긴다.  
# * 큰 원판이 그보다 작은 원판 위에 위치할 수 없다.   
# 
# 예를 들어, 탑A에 있는 3개의 원판을 탑C로 옮기는 방법은 아래와 같다.  
# 
# <div align="center"><img src="https://raw.githubusercontent.com/hj617kim/core_pybook/master/images/ch10/hanoi_01.png" style="width:500px;"></div>
# 1. 작은 원판을 탑A에서 탑C로 옮긴다. 
# <div align="center"><img src="https://raw.githubusercontent.com/hj617kim/core_pybook/master/images/ch10/hanoi_02.png" style="width:500px;"></div>
# 2. 중간 원판을 탑A에서 탑B로 옮긴다. 
# <div align="center"><img src="https://raw.githubusercontent.com/hj617kim/core_pybook/master/images/ch10/hanoi_03.png" style="width:500px;"></div>
# 3. 작은 원판을 탑C에서 탑B로 옮긴다. 
# <div align="center"><img src="https://raw.githubusercontent.com/hj617kim/core_pybook/master/images/ch10/hanoi_04.png" style="width:500px;"></div>
# 4. 큰 원판을 탑A에서 탑C로 옮긴다. 
# <div align="center"><img src="https://raw.githubusercontent.com/hj617kim/core_pybook/master/images/ch10/hanoi_05.png" style="width:500px;"></div>
# 5. 작은 원판을 탑B에서 탑A로 옮긴다. 
# <div align="center"><img src="https://raw.githubusercontent.com/hj617kim/core_pybook/master/images/ch10/hanoi_06.png" style="width:500px;"></div>
# 6. 중간 원판을 탑B에서 탑C로 옮긴다. 
# <div align="center"><img src="https://raw.githubusercontent.com/hj617kim/core_pybook/master/images/ch10/hanoi_07.png" style="width:500px;"></div>
# 7. 작은 원판을 탑A에서 탑C로 옮긴다.  
# <div align="center"><img src="https://raw.githubusercontent.com/hj617kim/core_pybook/master/images/ch10/hanoi_08.png" style="width:500px;"></div>
# 

# 위 설명을 n개의 원판을 옮길 때로 일반화하면 다음과 같다.  
# 
# 1. `n-1`개의 원판을 중간 지점의 위치에 옮긴다.  
# 2. 가장 큰 원판을 목적지로 옮긴다. 
# 3. 중간 지점에 위치한 `n-1`개의 원판을 목적지로 옮긴다.   
# 
# 아래의 코드에 위와 같은 일을 하는 `move_tower(n, from_tower, with_tower, to_tower)` 함수를 정의하여라.   
# 
# * `n` : 원판 개수
# * `from_tower` : 출발 탑
# * `with_tower` : 중간 지점 탑
# * `to_tower` : 목적지 탑   
# 

# :::{admonition} 하노이 탑  
# :class: info  
# 하노이 탑 문제에서 탑에 원판을 추가, 삭제하는 것은 스택에서 항목을 추가, 삭제할 때와 같다. 이에 하노이 탑 문제에서의 탑은 스택으로 정의할 수 있다.  
# :::
# 

# ```
# # 시각화를 위해 turtle 모듈 임포트
# from turtle import *
# 
# # 원판 클래스
# class Disc(Turtle):                                              
#     def __init__(self, n):
#         Turtle.__init__(self, shape="square") #사각형 모양의 거북이 생성
#         self.penup()           #원판이 움직일 때 자취를 남기지 않음
#         self.shapesize(1.2, n*2)  #원판 두께는 모두 같고, 길이는 달라지게 설정.                                                         
# # 탑tower 클래스
# class Tower(list):
#     def __init__(self, name, x):
#         self.name = name
#         self.x = x
# 
#     def message(self):
#         penup()             #거북이가 움직일 때 자취를 남기지 않음
#         goto(self.x, -220)  #아래 텍스트가 입력될 장소로 이동
#         write(self.name, align="center", font=("Courier", 17))        
#         
#     def push(self, d):   
#         d.setx(self.x)               #원판의 x좌표 설정             
#         d.sety(-150+30*len(self))    #원판의 y좌표 설정
#         self.append(d)               #원판을 타워에 추가
# 
#     def pop(self):
#         d = list.pop(self)           #원판을 타워에서 제거         
#         d.sety(150)                        
#         return d                                        
# 
# # 원판을 옮기는 일을 하는 함수
# def move_tower(n, from_tower, with_tower, to_tower):
#     pass                              
# 
# # Enter를 눌렀을 때 실행할 함수
# def play():
#     clear()      #거북이는 그대로 두고 화면을 지움
#     A.message()  #탑A 아래 A라고 표시
#     B.message()
#     C.message()
#     move_tower(5, A, B, C)  #5개의 원탑을 이동시킴                                 
# 
# # 처음 실행할 함수
# def main():
#     global A, B, C
# 
#     A = Tower('A', -300)  #탑 객체 생성   
#     B = Tower('B', 0)
#     C = Tower('C', 300)
#     
#     for i in range(5,0,-1):  #탑A에 5개의 원판 넣기
#         A.push(Disc(i))   
#         
#     penup()         #이동할 때, 자취를 남기지 않게 함
#     ht()            #텍스트를 그릴 거북이는 안 보이게 함
#     goto(0, -220)   #아래 텍스트가 입력될 장소로 이동. 0, -220로 이동.
# 
#     write("Press the Enter key", align="center", font=("Courier", 17))    #텍스트를 화면에 나타냄
# 
#     onkey(play, "Return")  #Enter키를 누르면 play() 함수 실행
#     listen() #사용자의 입력을 기다림  
#     return 
# 
# 
# main()      #main() 함수 실행           
# mainloop()  #turtle graphic 창을 종료할 때까지 프로그램을 실행
# ```

# :::{admonition} 클래스 상속    
# :class: info  
# 클래스를 선언할 때, 다른 클래스의 상태<font size="2">state</font>와 메서드<font size="2">method</font>를 상속<font size="2">inheritance</font> 받아 활용할 수 있다. 보통 상속을 받는 클래스를 **자식 클래스** 또는 **하위 클래스**, 상속을 해주는 클래스를 **부모 클래스** 또는 **상위 클래스**라고 부른다. 예를 들어, `list`, `tuple`, `str` 클래스는 `Sequence` 클래스를 상속하기 때문에 객체를 다루는 공통된 방식을 갖는다. 상속을 정의하는 방식은 다음과 같다.  
# 
# ```
# class 자식클래스(부모클래스) :
#     클래스 본문
# ```
# 
# 클래스 상속을 활용할 때의 주요 장점은 다음과 같다.  
# * 기존에 작성된 코드를 필요에 따라 수정, 재활용할 수 있다. 
# * 데이터(객체) 사이의 관계를 보다 잘 이해할 수 있다.  
# 
# 모든 클래스에는 초기 설정 메서드인 `init()` 메서드가 포함되어야 한다. 만약 자식 클래스에 `init()` 메서드가 정의되어 있지 않다면, 부모 클래스의 `init()`메서드를 그대로 사용한다.  
# 
# 부모 클래스에서 선언된 메서드는 모두 자식 클래스에서 **재정의**할 수 있다.   
# 
# 아래 `Tower` 클래스는 리스트`list` 클래스를 상속받는다. 따라서 `Tower`클래스의 인스턴스는 `list`의 `pop()`, `append()` 등의 메서드를 사용할 수 있다.  
# ```
# # 탑tower 클래스
# class Tower(list):
#     def __init__(self, name, x):
#         self.name = name
#         self.x = x
# ```
# 
# 아래 `Disc` 클래스는 `Turtle` 클래스를 상속받는다. 따라서 `Disc`클래스의 인스턴스는 `Turtle`의 `__init__()`, `penup()`, `shapesize()` 등의 메서드를 사용할 수 있다.  
# ```
# # 원판 클래스
# class Disc(Turtle):                                              
#     def __init__(self, n):
#         Turtle.__init__(self, shape="square") 
#         self.penup()           #원판이 움직일 때 자취를 남기지 않음
#         self.shapesize(1.2, n*2)  #원판 두께는 모두 같고, 길이는 달라지게 설정.
# ```
# 
# :::
# 

# :::{admonition} `Tower` 클래스의 `pop()` 메서드  
# :class: info  
# 
# 하노이 탑에서 탑은 스택으로 정의하고 있으며, 이를 위해 `list` 자료형을 활용하고 있다. 만약, 탑에 또는 스택에 항목을 추가하는 `pop()` 메서드를 정의하기 위해 아래와 같이 코드를 작성하면 어떻게 될까? 
# 
# ```
# def pop(self) :
#     d = self.pop()
#     d.sety(150)
#     return d
# ```
# `self.pop()`의 내부에서 리스트의 `pop()` 메서드가 실행되기를 원하겠지만, 실제로는 `pop()` 메서드 안에서 다시 `pop()` 메서드를 호출하는 재귀 호출이 된다. 이러한 현상을 방지하기 위해 두 가지 선택을 해볼 수 있다.  
# 
# * 스택에 항목을 추가하는 메서드 명을 다른 것으로 사용한다. 예를 들어, `pop1()`으로 사용할 수 있다. 
# ```
# def pop1(self) :
#     d = self.pop()
#     d.sety(150)
#     return d
# ```
# 그러면, 문제 없이 동작한다. 하지만, 메서드 명이 변경되어 혼동스럽다. 
# 
# * `list`의 `pop()`메서드와 구별해주기 위해 아래와 같이 코드를 작성할 수도 있다. 
# ```
# def pop(self):
#     d = list.pop(self)                   
#     d.sety(150)                        
#     return d     
# ```
# 
# :::
# 

# ### 문제
# 
# **재귀**를 사용해 주어진 수열의 첫 원소를 포함하는 부분수열 중 부분수열 원소들의 최대합을 반환하는 `subseq_max()` 함수를 정의하라.   
# 
# 예를 들어, `subseq_max([5, 3, -2, -1])`은 아래와 같으므로 `8`이다. 
# 
# * 5 + 3 - 2 - 1 = 5
# * 5 + 3 - 2 = 6
# * 5 + 3 = 8
# * 5 = 5
# 
# 또, `subseq_max([2, -5, -3, 15, 17, -11])`은 아래와 같으므로 `26`이다. 
# 
# * 2 -5 -3 + 15 + 17 - 11 = 15
# * 2 -5 -3 + 15 + 17 = 26
# * 2 -5 -3 + 15 = 9
# * 2 -5 -3 = -6
# * 2 -5 = -3
# * 2 = 2
# 

# ### 문제
# 앞 문제에서 정의한 `subseq_max()`와 재귀를 사용해 주어진 수열 안에 있는 모든 연속된 부분수열들에 대해 부분수열 원소들의 최대합을 반환하는 `all_subseq_max()` 함수를 정의하라.
#   
# 예를 들어, `all_subseq_max([5, 3, -2, -1])`은 아래와 같으므로 이다.
# 
# * 5 + 3 - 2 - 1 = 5
# * 5 + 3 - 2 = 6
# * 5 + 3 = 8
# * 5 = 5
# * 3 - 2 - 1 = 0
# * 3 - 2 = 1
# * 3 = 3
# * -2 - 1 = -3
# * -2 = -2
# 

# ### 문제 
# 임의로 중첩된 리스트를 풀어 중첩이 없는 리스트로 반환하는 `flatten()` 함수를 재귀를 이용하여 구현하라.   
# 
# ```python
# >>> flatten([1, [2, 3, 4], [5, 6, [7, 8]]])
# [1, 2, 3, 4, 5, 6, 7, 8]
# >>> flatten([[4.8, 1.2], 3.3, [5.6, 7.2, 9.8]])
# [4.8, 1.2, 3.3, 5.6, 7.2, 9.8]
# ```
