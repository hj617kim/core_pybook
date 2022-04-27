#!/usr/bin/env python
# coding: utf-8

# # 기초 추상 자료형

# ## 스택  
# 
# 스택<font size="2">stack</font>은 여러 개의 값을 가지며 값들 사이의 순서가 중요한 선형 자료형이다. 항목의 추가 및 삭제는 보통 **탑**<font size="2">top</font>이라 불리는 한쪽 끝에서만 허용된다. 반면에 다른 한 쪽 끝은 **베이스**<font size="2">base</font>라 한다.  
# 스택은 아래 그림처럼 데이터를 들어온 순으로 쌓아 올린 형상을 생각하면 된다.    
# 
# <div align="center">
#     <img src="https://raw.githubusercontent.com/hj617kim/core_pybook/master/images/ch09/stack01.png" style="width:400px;">
# </div>
# 
# 아래 그림처럼 스택은 들어온 순서의 역순으로 삭제되는 선입후출<font size="2">Last In First Out</font>로 처리된다.  
# 
# * 베이스 : 가장 먼저 추가된 항목
# * 탑 : 가장 나중에 추가된 항목이며 가장 먼저 삭제될 대상
# 
# <div align="center">
#     <img src="https://raw.githubusercontent.com/hj617kim/core_pybook/master/images/ch09/stack02.png" style="width:400px;">
# </div>
# 
# **활용 예제** : 인터넷 브라우저의 '뒤로가기(Back)' 버튼  
# 웹페이지가 변경될 때마다 순서를 기억해 둔 다음에 '뒤로가기' 버튼을 누르면 역순으로 이전 웹페이지를 보여준다.  
# 
# **활용 예제** : 응용 프로그램의 되돌리기<font size="2">undo</font> 기능  
# 변경될 때마다 순서를 기억해 둔 다음에 되돌리기 버튼 또는 ctrl + z를 누르면 마지막에 실행된 것부터 실행을 취소한다.  

# ## `Stack` 추상 자료형  
# 스택 추상 자료형을 구체적인 파이썬 자료구조<font size="2">data structure</font>로 구현하려면 갖추어야 하는 기본 기능은 다음과 같다.  
# * `Stack()` : 비어 있는 스택 생성. 생성자의 역할.  
# * `push(item)` : 새로운 항목을 탑<font size="2">top</font>으로 추가. 
# * `pop()` : 탑 항목 삭제. 삭제된 항목 반환.
# * `peek()` : 탑 항목 반환. 하지만 삭제하지는 않음. 
# * `is_empty()` : 스택이 비었는지 여부 판단. 불리언 값 반환.
# * `size()` : 항목 개수 반환.   
# 
# 아래 표는 스택 생성과 함께 다양한 스택 관련 연산의 작동법을 소개한다. 파이썬은 스택 추상 자료형을 별도로 제공하지는 않지만, 리스트`list`가 스택의 모든 연산을 지원한다.   
# 
# |스택연산|스택항목|반환값|
# |:----------|:-------------|:---------:|
# |`s = Stack()`| `[]`||
# |`s.is_empty()`|`[]`|`True`|
# |`s.push(2)`|`[2]`||
# |`s.push('Hello')`|`[2, 'Hello']`||
# |`s.peek()`|`[2, 'Hello']`|`'Hello'`|
# |`s.push(3.2)`|`[2, 'Hello', 3.2]`||
# |`s.size()`|`[2, 'Hello', 3.2]`|`3`|
# |`s.is_empty()`|`[2, 'Hello', 3.2]`|`False`|
# |`s.push(True)`|`[2, 'Hello', 3.2, True]`||
# |`s.pop()`|`[2, 'Hello', 3.2]`|`True`|
# |`s.pop()`|`[2, 'Hello']`|`3.2`|
# |`s.size()`|`[2, 'Hello']`|`2`|
# 
# 

# ## 스택 자료구조 구현  
# 스택 자료구조를 `Stack` 클래스로 구현하기 위해 리스트를 항목들의 저장 장치로 활용하며, 앞서 소개한 기능들은 모두 메서드로 정의한다. 스택의 탑 역할은 리스트의 오른쪽 끝(마지막 항목)이 수행하도록 한다. 그러면 리스트의 `pop()`과 `append()`를 잘 활용할 수 있다.  

# In[1]:


class Stack:
    """리스트를 활용한 스택 구현"""

    def __init__(self):
        """새로운 스택 생성"""
        self._items = []

    def __str__(self):
        """스택 표기법: <[1, 2, 3]> 등등"""
        return f"<{self._items}>"
        
    def is_empty(self):
        """비었는지 여부 확인"""
        return not bool(self._items)

    def push(self, item):
        """새 항목 추가"""
        self._items.append(item)

    def pop(self):
        """항목 제거"""
        return self._items.pop()

    def peek(self):
        """탑 항목 반환"""
        return self._items[-1]

    def size(self):
        """항목 개수 반환"""
        return len(self._items)


# :::{admonition} 참고    
# :class: info  
# 리스트의 첫 번째 항목을 스택의 탑으로 하려면 `pop(0)`와 `insert(0, item)`을 사용하면 된다.  
# :::
# 

# 위 표를 코드로 구현하면 다음과 같다. 

# In[2]:


s = Stack()
print(s)
print(s.is_empty())


# In[3]:


s.push(2)
s.push('Hello')

print(s)
print(s.peek())


# In[4]:


s.push(3.2)
print(s)
print(s.size())
print(s.is_empty())


# In[5]:


s.push(True)
print(s)
print(s.pop())


# In[6]:


print(s)
print(s.pop())
print(s.size())


# ````{prf:example}
# :label: stack-example01  
# 함수나 연산 실행에 사용되는 괄호는 짝이 맞아야 한다. 즉, 여는 괄호와 닫는 괄호의 짝이 맞아야 한다. 파이썬의 경우 괄호가 맞지 않으면 구문 오류`SyntaxError`가 발생한다.   
# 
# 스택을 이용하여 괄호로 이루어진 문자열이 짝이 맞는 괄호들로 이루어졌는지 여부를 판단하는 함수`par_checker()` 를 구현하여라.   
# ````

# ```python
# >>> print(par_checker("((()))"))
# True
# >>> print(par_checker("()()()"))
# True
# >>> print(par_checker("((())"))
# False
# >>> print(par_checker(")("))
# False
# ```

# 스택 활용법은 다음과 같다. 괄호로 이루어진 문자열이 주어졌을 때, 왼편부터 시작하여 여는 괄호와 닫는 괄호를 만날 때마다 아래 작업을 반복한다.  
# * 여는 괄호(`(`) : 스택에 추가  
# * 닫는 괄호(`)`) : 스택의 탑 항목 삭제   
# 
# 위 작업을 반복하다 보면 아래 세 가지 경우가 발생한다.  
# * 문자열을 다 확인하기 전에 스택이 비워지는 경우 - 닫는 괄호가 더 많기 때문.    
# * 끝까지 다 확인했을 때 스택이 비워지지 않은 경우 - 여는 괄호가 더 많기 때문.  
# * 위 두 경우가 아니면 모든 괄호의 짝은 맞음.

# In[7]:


def par_checker(par_string) :
    
    s = Stack()
    
    for p in par_string :
        if p == "(" :
            s.push(p)
        elif s.is_empty() :
            return False
        else :
            s.pop()
            
    return s.is_empty()


# In[8]:


print(par_checker("((()))"))
print(par_checker("()()()"))
print(par_checker("((())"))
print(par_checker(")("))


# ## 연습문제

# ### 문제  
# 함수나 연산 실행에 사용되는 괄호는 짝이 맞아야 한다. 즉, 여는 괄호와 닫는 괄호의 짝이 맞아야 한다. 파이썬의 경우 괄호가 맞지 않으면 구문 오류`SyntaxError`가 발생한다. 아래 괄호로 이루어진 문자열이 짝이 맞는 괄호들로 이루어졌는지 여부를 판단하는 함수`balance_checker()`를 구현하여라.  
# * `(`, `)` : 소괄호
# * `{`, `}` : 중괄호
# * `[`, `]` : 대괄호
# 
# ```python
# >>> print(balance_checker('{{([][])}()}'))
# True
# ```
# 
# ```python
# >>> print(balance_checker('[[{{(())}}]]'))
# True
# ```
# 
# ```python
# >>> print(balance_checker('[][][](){}'))
# True
# ```
# 
# ```python
# >>> print(balance_checker('([))'))
# False
# ```
# 
# ```python
# >>> print(balance_checker('[{()]'))
# False
# ```

# ### 문제  
# 

# 십진법은 우리가 일반적으로 사용하는 기수법<font size="2">numeral system</font>으로, 0,1,2,3,4,5,6,7,8,9라는 10개의 숫자를 가지고 수를 표현하며, 수의 자리가 하나씩 올라감에 따라 자릿값이 10배씩 커진다. 반면에 이진법은 0과 1, 두 개의 숫자를 가지고 수를 표현하며, 수의 자리가 하나씩 올라감에 따라 자릿값이 2배씩 커진다. 예를 들어, 십진법 정수 $125_{10}$를 이진법으로 표기하면 $1111101_{2}$이 된다. 
# 
# $$123_{10} = 1 \times 10^2 + 2 \times 10^1 + 3 \times 10^0 $$
# $$1111101_{2} = 1 \times 2^6 + 1 \times 2^5 + 1 \times 2^4 + 1 \times 2^3 + 1 \times 2^2 + 0 \times 2^1 + 1 \times 2^0$$  

# 십진법으로 표기된 정수를 이진법으로 변환하는 함수`base_converter()` 함수를 정의하여라.   
# 
# ```python
# >>> print(base_converter(123))
# 1111101
# ```
# 
# ```python
# >>> print(base_converter(7))
# 111
# ```
# 
# ```python
# >>> print(base_converter(11))
# 1011
# ```

# ```{admonition} 도움말    
# :class: dropdown
# 십진법으로 표기된 정수의 이진법 표기를 찾는 알고리즘은 아래와 같다.  
# * 2로 나눈 후 나머지를 스택에 추가한다.  
# * 2로 나눈 몫을 대상으로 위 과정을 반복한다. 
# * 스택에 쌓인 값들을 거꾸로 읽는다. 즉, `pop()`을 연속적으로 활용한다.  
# ```

# ### 문제  
# 회의 시간을 정하기 위해 팀원들에게 회의하기 어려운 시간을 구간으로 조사하였다. 그리고 겹치는 구간을 합해 회의 불가능한 시간을 정리하려고 한다. 이때, 13시부터 15시까지 회의가 어렵다면, 이를 `[13, 15]`로 표현한다.  
# 
# 예를 들어, 아래와 같다면, 회의 불가능한 시간은 9시부터 10시(`[9, 10]`), 12시부터 15시(`[12, 15]`)이다.   
# * A는 13시부터 15시까지 회의 불가능 - `[13, 15]`  
# * B는 9시부터 10시, 12시부터 14시 회의 불가능 - `[9, 10]`, `[12, 14]`  
# 
# 시간은 0~24사이(끝 값 포함)의 정수로 입력된다고 가정한다.  
# 
# 여러 개의 길이가 2인 리스트를 인자로 받아, 각 구간을 합하여 겹치지 않는 구간을 만든 다음 반환하는 `merge_intervals()` 함수를 정의하여라.     
# 
# ```python
# >>> print(merge_intervals([13, 15], [9, 10], [12, 14]))
# [[9, 10], [12, 15]]
# ```
# 
# ```python
# >>> print(merge_intervals([10, 16], [9, 12]))
# [[9, 16]]
# ```

# ```{admonition} 도움말    
# :class: dropdown
# * 시작 시간을 기준으로 오름차순으로 정렬한다.   
# * 스택을 만든다.    
# * 각 구간에 대해 스택이 비어있거나 스택의 탑에 있는 구간의 끝 시간이 그 구간의 시작 시간보다 작으면(즉, 두 구간이 겹치지 않는 경우), 그 구간을 스택에 넣는다.  
# * 위에서 구간이 겹친다면, 스택의 탑에 있는 구간의 끝 시간을 업데이트하여 두 구간을 병합한다.  
# * 스택에 있는 겹치지 않는 모든 구간을 반환한다.   
# ```

# ### 문제

# 매일의 주식 종가가 기록된 리스트를 입력받아서, 주식가격이 오르기 위해서는 며칠을 기다려야 하는지를 반환하는 함수 `closing_price()`를 정의하여라.   
# 
# 예를 들어, 첫째 날의 종가는 100원이고 1일만 지나면 종가가 오른다. 둘째 날의 종가는 101원이고 4일이 지나야 종가가 오른다.   
# ```python 
# >>>print(closing_price([100, 101, 95, 92, 90, 120]))
# [1, 4, 3, 2, 1, 0]
# ```
