#!/usr/bin/env python
# coding: utf-8

# # 기초 추상 자료형

# ## 스택  
# 
# 스택<font size="2">stack</font>은 여러 개의 값을 가지며 값들 사이의 순서가 중요한 선형 자료형이다. 항목의 추가 및 삭제는 보통 **탑**<font size="2">top</font>이라 불리는 한쪽 끝에서만 허용된다. 반면에 다른 한 쪽 끝은 **베이스**<font size="2">base</font>라 한다.  
# 스택은 아래 그림처럼 데이터를 들어온 순으로 쌓아 올린 형상을 생각하면 된다.    
# 
# <div align="center">
#     <img src="https://raw.githubusercontent.com/hj617kim/core_pybook/master/images/ch09/stack01.png" style="width:220px;">
# </div>
# 
# 아래 그림처럼 스택은 들어온 순서의 역순으로 삭제되는 선입후출<font size="2">Last In First Out, LIFO</font>로 처리된다.  
# 
# * 베이스 : 가장 먼저 추가된 항목
# * 탑 : 가장 나중에 추가된 항목이며 가장 먼저 삭제될 대상
# 
# <div align="center">
#     <img src="https://raw.githubusercontent.com/hj617kim/core_pybook/master/images/ch09/stack02.png" style="width:250px;">
# </div>
# 
# **활용 예제** : 인터넷 브라우저의 '뒤로가기(Back)' 버튼  
# 웹페이지가 변경될 때마다 순서를 기억해 둔 다음에 '뒤로가기' 버튼을 누르면 역순으로 이전 웹페이지를 보여준다.  
# 
# **활용 예제** : 응용 프로그램의 되돌리기<font size="2">undo</font> 기능  
# 변경될 때마다 순서를 기억해 둔 다음에 되돌리기 버튼 또는 ctrl + z를 누르면 마지막에 실행된 것부터 실행을 취소한다.  

# ### `Stack` 추상 자료형  
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
# |스택 연산|스택 항목|반환값|
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

# ### 스택 자료구조 구현  
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


# ## 큐

# 큐<font size="2">queue</font>는 스택과 마찬가지로, 선형 자료형이다. 항목의 추가는 보통 **꼬리**<font size="2">rear, tail</font>라 불리는 한 쪽 끝에서만 허용되고, 항목의 삭제는 **머리**<font size="2">front, head</font>라고 불리는 다른 한 쪽 끝에서 이루어진다. 큐는 아래 그림처럼 입력된 순서대로 하나씩 삭제되는 형상을 생각하면 된다. 
# 
# <div align="center">
#     <img src="https://raw.githubusercontent.com/hj617kim/core_pybook/master/images/ch09/queue01.png" style="width:500px;">
# </div>
# 
# 위의 그림처럼 큐는 먼저 들어온 항목이 먼저 나간다는 선입선출<font size="2">First In First Out, FIFO</font>원리를 따르며, 항목들의 추가와 삭제는 입력 순서에 따라 한쪽 방향으로 이동하는 방식이 철저하게 지켜진다.    
# 
# **활용 예제** : 은행 창구 번호표 배분 장치  
# 은행 창구에서 번호표를 배분하는 장치는 방문 순서대로 호출된다.  
# 
# **활용 예제** : 프린터  
# 프린터는 프린팅 과제가 생성된 순서대로 출력된다.  

# ### `Queue` 추상 자료형  
# 큐 추상 자료형을 구체적인 파이썬 자료구조<font size="2">data structure</font>로 구현하려면 갖추어야 하는 기본 기능은 다음과 같다.  
# 
# * `Queue()` : 비어 있는 큐 생성. 생성자의 역할. 
# * `enqueue(item)` : 새로운 항목을 꼬리<font size="2">rear, tail</font>에 추가. 반환값 없음.  
# * `dequeue()` : 머리 항목 삭제. 삭제된 항목 반환. 
# * `is_empty()` : 큐가 비어있는지 여부 판단. 불리언 값 반환.
# * `size()` : 항목 개수 반환.  
# 
# 아래 표는 큐 생성과 함께 다양한 큐 관련 연산의 작동법을 소개한다. 파이썬의 리스트`list`는 큐의 모든 연산을 지원한다. 항목들의 저장을 위해 리스트를 사용하며, 큐의 머리 역할은 리스트의 오른쪽 끝(마지막 항목)이, 꼬리 역할은 왼쪽 끝(첫 번째 항목)이 수행한다.      
# 
# 
# |큐 연산|큐 항목|반환값|
# |:----------|:-------------|:---------:|
# |`q = Queue()`| `[]`||
# |`q.is_empty()`| `[]`|`True`|
# |`q.enqueue(2)`| `[2]`||
# |`q.enqueue('Hello')`| `['Hello', 2]`||
# |`q.enqueue(3.2)`| `[3.2, 'Hello', 2]`||
# |`q.size()`| `[3.2, 'Hello', 2]`|`3`|
# |`q.is_empty()`| `[3.2, 'Hello', 2]`|`False`|
# |`q.enqueue(True)`| `[True, 3.2, 'Hello', 2]`||
# |`q.dequeue()`| `[True, 3.2, 'Hello']`|`2`|
# |`q.dequeue()`| `[True, 3.2]`|`'Hello'`|
# |`q.size()`| `[True, 3.2]`|`2`|

# ### 큐 자료구조 구현  
# 리스트를 활용할 때 중요한 것은 머리와 꼬리를 어디로 설정하는가이다. 앞서 본 것처럼 꼬리는 리스트의 왼쪽편 끝, 머리는 리스트의 오른쪽편 끝으로 정한다. 

# In[9]:


class Queue:
    """리스트를 활용한 큐 구현"""

    def __init__(self):
        """새로운 큐 생성"""
        self._items = []
    
    def __str__(self):
        """큐 표기법: <<[1, 2, 3]>> 등등"""
        return f"<<{self._items}>>"
    
    def is_empty(self):
        """비었는지 여부 확인"""
        return not bool(self._items)

    def enqueue(self, item):
        """꼬리에 항목 추가"""
        self._items.insert(0, item)

    def dequeue(self):
        """머리 항목 삭제"""
        return self._items.pop()

    def size(self):
        """항목 개수 확인"""
        return len(self._items)


# In[10]:


q = Queue()

print(q.is_empty())
q.enqueue(2)
q.enqueue("Hello")
q.enqueue(3.2)
print(q)


# In[11]:


print(q.size())
print(q.is_empty())
q.enqueue(True)


# In[12]:


q.dequeue()
q.dequeue()
print(q)
print(q.size())


# ````{prf:example} 요세푸스 문제<font size="2">Josephus problem</font> 또는 요세푸스 순열<font size="2">Josephus permutation</font>  
# :label: queue-example01  
# n명이 동그랗게 둘러앉아 임의의 한 사람부터 순서를 세어 k번째 사람을 제외하는 게임을 아무도 남지 않을 때까지 계속한다. 자연수 n과 k를 입력받아 제외되는 사람의 순서를 반환하는 `josephus_permutation()` 함수를 정의하여라. 단, k < n라고 가정한다.   
# 
# 예를 들어, 7명의 사람이 있고, 3번째 사람을 제외할 때는 3 -> 6 -> 2 -> 7 -> 5 -> 1 -> 4 순서로 제외한다.     
# ````

# ```python
# >>> print(josephus_permutation(7, 3))
# [3, 6, 2, 7, 5, 1, 4]
# ```

# 큐 활용법은 다음과 같다. 
# 
# 1. 사람들의 번호를 큐에 추가한다. 큐의 머리에는 1이 있고, 꼬리에는 n이 있다. 
# 2. 큐의 머리에 있는 항목을 삭제 후 바로 꼬리에 추가한다. 
# 3. 2의 과정을 k - 1번 반복한다. 그리고 k번째에는 머리에 있는 항목을 삭제한 후 꼬리에 추가하지 않고, 다른 공간에 저장한다.   
# 4. 2와 3의 과정을 큐에 아무 것도 없을 때까지 반복한다. 

# In[13]:


def josephus_permutation(n, k) : 
    
    q = Queue()
    results = []
    
    for i in range(1, n + 1) :
        q.enqueue(i)
        
    while q.size() > 1 :
        for i in range(k - 1) :
            q.enqueue(q.dequeue())
        results.append(q.dequeue())
    
    results.append(q.dequeue())
        
    return results


# In[14]:


print(josephus_permutation(7, 3))


# ## 덱

# 덱<font size="2">double-ended queue, deque</font>은 선형 자료형으로, 큐와는 달리 항목의 추가와 삭제가 머리와 꼬리 양쪽 끝 모두에서 처리된다. 이런 의미에서 덱은 스택과 큐의 기능을 함께 제공하며 어떻게 사용할 것인가는 사용자에 의해 결정된다.  
# 
# <div align="center">
#     <img src="https://raw.githubusercontent.com/hj617kim/core_pybook/master/images/ch09/deque01.png" style="width:500px;">
# </div>
# 
# **활용 예제** : 편집기의 'undo'와 'redo'  
# 문서 작성 중에 'undo' 버튼을 누르면 마지막에 추가된 항목(머리 항목)이 삭제되는 동시에 꼬리 항목으로 추가된다. 이후 'redo' 버튼이 눌리면 꼬리 항목이 삭제되어 다시 머리 항목으로 추가된다. 웹브라우저의 'back'과 'forward' 버튼도 이와 유사하게 작동한다.  

# :::{admonition} 참고    
# :class: info  
# 파이썬에서 덱은 collections 라이브러리의 `deque` 클래스를 이용해 사용할 수 있다. 덱은 스택과 큐를 일반화한 것으로, 이를 이용하여 스택과 큐를 구현할 수 있다.  
# ```python
# >>> from collections import deque
# >>> print(help(deque))
# ```
# :::
# 

# ### `Deque` 추상 자료형  
# 덱 추상 자료형을 구체적인 파이썬 자료구조<font size="2">data structure</font>로 구현하려면 갖추어야 하는 기본 기능은 다음과 같다.  
# 
# * `Deque()` : 비어 있는 덱 생성. 생성자의 역할. 
# * `add_front(item)` : 머리에 새로운 항목 추가. 반환값 없음. 
# * `add_rear(item)` : 꼬리에 새로운 항목 추가. 반환값 없음. 
# * `remove_front()` : 머리 항목 삭제. 삭제된 항목 반환. 
# * `remove_rear()` : 꼬리 항목 삭제. 삭제된 항목 반환.
# * `is_empty()` : 덱이 비었는지 여부 판단. 불리언 값 반환.
# * `size()` : 항목 개수 반환.  
# 
# 아래 표는 덱 생성과 함께 다양한 덱 관련 연산의 작동법을 소개한다. 항목들의 저장을 위해 리스트를 사용하며 머리는 리스트의 오른쪽 끝, 꼬리는 왼쪽 끝을 사용한다.  
# 
# |덱 연산|덱 항목|반환값|
# |:----------|:-------------|:---------:|
# |`d = Deque()`| `[]`||
# |`d.is_empty()`| `[]`|`True`|
# |`d.add_rear(2)`| `[2]`||
# |`d.add_rear('Hello')`| `['Hello', 2]`||
# |`d.add_front(3.2)`| `['Hello', 2, 3.2]`||
# |`d.add_front(True)`| `['Hello', 2, 3.2, True]`||
# |`d.size()`| `['Hello', 2, 3.2, True]`|4|
# |`d.is_empty()`| `['Hello', 2, 3.2, True]`|`False`|
# |`d.add_rear(5)`| `[5, 'Hello', 2, 3.2, True]`||
# |`d.remove_rear()`| `['Hello', 2, 3.2, True]`|`5`|
# |`d.remove_front()`| `['Hello', 2, 3.2]`|`True`|

# ### 덱 자료구조 구현   
# 
# 리스트를 활용할 때 중요한 것은 머리와 꼬리를 어디로 설정하는가이다. 큐의 경우처럼 꼬리는 리스트의 시작, 머리는 리스트의 오른편 끝으로 정하며 이에 따라 항목 추가와 삭제 함수를 적절하게 구현한다.  
# 
# * 머리 
#     * 항목 추가 : 리스트의 `append(item)` 활용
#     * 항목 삭제 : 리스트의 `pop()` 활용
# 
# * 꼬리
#     * 항목 추가 : 리스트의 `insert(0, item)` 활용
#     * 항목 삭제 : 리스트의 `pop(0)` 활용

# In[15]:


class Deque:
    """리스트를 활용한 덱 구현"""

    def __init__(self):
        """새로운 덱 생성"""
        self._items = []
    
    def __str__(self):
        """덱 표기법: <~[1, 2, 3]~> 등등"""
        return f"<~{self._items}~>"
    
    def is_empty(self):
        """비었는지 여부 확인"""
        return not bool(self._items)

    def add_front(self, item):
        """머리에 항목 추가"""
        self._items.append(item)

    def add_rear(self, item):
        """꼬리에 항목 추가"""
        self._items.insert(0, item)

    def remove_front(self):
        """머리 항목 삭제"""
        return self._items.pop()

    def remove_rear(self):
        """꼬리 항목 삭제"""
        return self._items.pop(0)

    def size(self):
        """항목 개수 확인"""
        return len(self._items)


# In[16]:


d = Deque()
print(d.is_empty())
d.add_rear(2)
d.add_rear('Hello')
d.add_front(3.2)
d.add_front(True)
print(d)


# In[17]:


print(d.size())
print(d.is_empty())
d.add_rear(5)
print(d.remove_rear())
print(d.remove_front())
print(d)


# ````{prf:example} 
# :label: deque-example01  
# 'racecar', '토마토', 'stats'와 같이 앞뒤를 뒤집어도 똑같은 문자열을 회문<font size = "2">palindrome</font>이라고 한다. 덱을 활용하여 문자열이 주어질 때, 그 문자열이 회문이면 `Success`를, 아니면 `Fail`를 반환하는 `palindrome_checker()` 함수를 정의하여라.   
# ````

# ```python
# >>> print(palindrome_checker('racecar'))
# True
# >>> print(palindrome_checker('tomato'))
# False
# ```

# 덱 활용법은 다음과 같다.  
# 
# * 주어진 문자열을 덱에 추가한다.  
# * 머리와 꼬리의 항목을 하나씩 꺼내 값을 비교하여, 다른 것이 있으면 `False`를 반환하고, 아니면 `True`를 반환한다. 

# In[18]:


def palindrome_checker(a_string) :
    
    d = Deque()
    
    for ch in a_string :
        d.add_rear(ch)
        
    while d.size() > 1 :
        first = d.remove_front()
        last = d.remove_rear()
        if first != last :
            return False
        
    return True


# In[19]:


print(palindrome_checker('racecar'))


# In[20]:


print(palindrome_checker('tomato'))


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
# $$125_{10} = 1 \times 10^2 + 2 \times 10^1 + 5 \times 10^0 $$
# $$1111101_{2} = 1 \times 2^6 + 1 \times 2^5 + 1 \times 2^4 + 1 \times 2^3 + 1 \times 2^2 + 0 \times 2^1 + 1 \times 2^0$$  

# 십진법으로 표기된 정수를 이진법으로 변환하는 함수`base_converter()` 함수를 정의하여라.   
# 
# ```python
# >>> print(base_converter(125))
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

# ```{admonition} 도움말    
# :class: dropdown  
# 스택에 유용한 항목의 인덱스를 저장하는 방식으로 문제를 해결할 수 있다. 위의 예제의 경우, 아래와 같은 방식으로 해결할 수 있다.    
# 1. 스택을 만든다(s : `[]`).  
# 2. `closing_price()` 함수가 반환할 리스트를 정의한다. 이때, 리스트의 길이는 주식 종가가 기록된 리스트와 같고, 항목은 모두 `0`으로 한다.   
# 3. 반복문을 사용하여, 인자로 들어온 리스트의 각 항목에 접근한다.   
# 4. 현재 스택이 비어 있으므로, `100`의 인덱스 `0`을 스택에 추가한다(s : `[0]`).  
# 5. `101`은 `100`보다 크므로, 스택의 탑에 있는 값 `0`을 꺼낸 다음 `반환할 리스트[0] = 1(101의 인덱스) - 0`을 한다. 그리고 `101`의 인덱스 `1`를 스택에 추가한다(s : `[1]`).    
# 6. `95`는 `101`보다 작으므로, 스택에 추가한다(s : `[1, 2]`).  
# 7. `92`는 `95`보다 작고, 101보다 작으므로, 스택에 추가한다(s : `[1, 2, 3]`).  
# 8. `90`는 `91`와 `95`보다 작고, 101보다도 작으므로, 스택에 추가한다(s : `[1, 2, 3, 4]`).  
# 9. `120`은 `90`보다 크다. 스택의 탑에 있는 값 `4`를 꺼낸 다음 `반환할 리스트[4] = 5(120의 인덱스) - 4`를 한다. 그다음 스택의 탑에 있는 값 `3`을 꺼낸 다음 `반환할 리스트[3] = 5(120의 인덱스) - 3`을 한다. 다시, 그다음 스택의 탑에 있는 값 `2`을 꺼낸 다음 `반환할 리스트[2] = 5(120의 인덱스) - 2`를 한다. 스택에 아무 것도 없을 때까지 위 과정을 반복하고, 마지막에 리스트를 반환하면 된다.  
# ```

# ### 문제

# 문자 없애기 게임을 만들어보자. 게임은 다음과 같이 진행된다.     
# 
# * 컴퓨터는 `abcd` 중 중복을 허용하여 랜덤하게 3개의 문자를 말한다.  
# * 사용자는 `abcd` 중 중복을 허용하여 3개의 문자를 입력한다.  
# * 컴퓨터와 사용자가 입력한 문자열은 순서대로 이어 붙여진다. 그리고 같은 문자가 3번 반복되면 그 문자는 사라진다.  
# 
# 위 과정을 반복하여, 사용자는 모든 문자를 없애야 한다.   
# 
# 예를 들어, 게임 진행 과정은 아래와 같다. `coputer`가 랜덤하게 3개의 문자를 말하면, `user`가 3개의 문자를 입력한다.  
# ```
# computer : bdc
# user : ccd
# ```
# 두 문자열을 이어 붙이면 `bdcccd` 이고 `c`가 3번 반복되어 `bdd`가 남는다. 그 다음은 `computer` 차례다. 
# 
# ```
# computer : cac
# ```
# 문자열을 이어 붙이면 현재 문자열은 `bddcac`이다. 그 다음은 `user` 입력할 차례다. 
# 
# ```
# user : cca
# ```
# 문자열을 이어 붙이면 `bddcaccca` 이고 `c`가 3번 반복되어 `bddcaa`가 남는다. 그 다음 `computer` 차례다. 
# 
# ```
# computer : acc
# ```
# 그러면 `bddcaaacc`가 된다. `a`가 3번 반복되어 `bddccc`가 된다. 그런데 이때도 `c`가 3번 반복되어 사라진다. 그래서 `bdd`가 남는다.  
# 
# 이제 `user`가 `dbb`를 입력하면, 모든 문자가 사라지고 게임이 끝난다.   
# 
# 
# 필요하면, `random` 모듈의 `choices()` 함수를 사용한다. `choices(population, k = 1)`는 `population`에서 중복을 허용하면서 선택한 `k` 크기의 요소를 가진 리스트를 반환한다.  
# 
# 게임을 구현할 때는 사용자에게 문자를 입력 받기 전 현재 남아 있는 문자를 보여줘야 한다.   

# In[21]:


import random

print(random.choices('abc', k = 3))
print(random.choices('abc', k = 3))
print(random.choices('abc', k = 3))


# ### 문제 

# 자연수 n를 입력받아, 1에서 n까지의 정수를 이진법으로 표기한 값들의 리스트를 반환하는 함수`generate_binary_number()`를 정의하여라.  
# 
# ```python
# >>> print(generate_binary_number(2))
# [1, 10]
# >>> print(generate_binary_number(7))
# [1, 10, 11, 100, 101, 110, 111]
# ```

# ```{admonition} 도움말    
# :class: dropdown  
# 큐에 이진수를 추가하는 방식으로 문제를 해결할 수 있다.   
# 1. 큐를 만든다.  
# 2. 큐에 '1'를 추가한다.  
# 3. 큐의 머리에 있는 값(`s1`)을 꺼내 반환할 리스트에 담는다. 그리고 `s1`에 `'0'`과 `'1'`를 더하는 방식으로 다음 이진수를 만들어 큐에 추가한다. 
# 4. 3의 과정을 원하는 만큼 반복한다. 
# ```

# ### 문제     
# n명이 동그랗게 둘러앉아 임의의 한 사람부터 순서를 세어 k번째 사람을 제외하는 게임을 아무도 남지 않을 때까지 계속한다. 단, t명이 제외될 때마다 사람을 세는 방향을 변경한다. 자연수 n, k, t를 입력받아 제외되는 사람의 순서를 반환하는 `josephus_permutation()` 함수를 정의하여라. 단, t, k < n라고 가정한다.   
# 
# 예를 들어, n = 7, k = 3, t = 2라면 3 -> 6 -> 2 -> 5 -> 4 -> 7 -> 1 순서로 제외한다.     
# 
# ```python
# >>> print(josephus_permutation(7, 3, 2))
# [3, 6, 2, 5, 4, 7, 1]
# ```

# ```{admonition} 도움말    
# :class: dropdown  
# 예를 들어, `t`가 2라면, 2사람을 제외하고 사람을 세는 방향을 변경해야 한다. 제외되는 사람을 각각 0, 1, 2, 3, 4, 5, 6이라고 해보자. 그러면 아래와 같은 방식으로 제외한다.  
# * 0, 1 - 시계 방향
# * 2, 3 - 반시계 방향
# * 4, 5 - 시계 방향
# * 6 - 반시계 방향
# 
# 이때, 0, 1, 4, 5는 2로 나눴을 때의 몫이 각각 0, 0, 2, 2이다. 그리고 2, 3, 6은 2로 나눴을 때의 몫이 1, 1, 3이다.   
# 즉, `i`는 0부터 시작하여 사람을 제외할 떄마다 1씩 증가하게 두고, `i // t`의 값이 짝수냐 홀수냐에 따라 방향을 변경하면 된다.  
# 
# ```

# ### 문제 

# 여러 명이 함께 사용하는 실험실 공용 프린터 한 대가 무작위적으로 입력되는 프린팅 작업을 수행할 때 벌어지는 일을 모의실험해보자. 모의실험의 목적은 사용자가 프린팅 명령을 내리고 과제가 출력되기 시작할 때까지 평균적으로 걸리는 시간을 계산하는 일이다.   
# 
# **필요한 객체**  
# 다음 세 개의 객체를 사용한다.  
# * 프린트 객체 : `Printer` 클래스의 인스턴스. 프린터의 기본 기능 제공
#     * 프린팅 과제 내용 : 분당 출력 페이지 수
#     * 프린터 상태 : busy 또는 대기 
#     * 프린팅 과제 수행 
#     * 프린팅 과제별 수행 시간 측정
# * 프린팅 과제 객체 : `Task` 클래스의 인스턴스. 실행할 프린팅 과제 정보 저장
#     * 출력 대상 페이지 수
#     * 과제 생성 시간
#     * 출력 대기 시간 : 생성부터 프린터 출력 시작까지 대기시간
# * 프린팅 큐 객체 : `Queue` 클래스의 인스턴스 
#     * 프린팅 과제 대기 목록 
# 
# **모의실험에 대한 추가 전제 사항**
# * 사람들이 무작위적으로 시간당 20건의 프린팅 과제 출력 실행
# * 하나의 프린팅 과제는 최대 20쪽까지 출력   

# :::{admonition} 180분의 1의 확률 
# :class: info  
# 위 모의실험의 전제조건은 확률적으로 180초에 한 번 프린팅 과제가 생성된다는 것을 의미한다. 매 초마다 1/180 확률로 프린팅 과제가 생성되는 것과 생성된 과제가 1에서 20쪽 사이의 임의의 쪽 수를 출력해야 하는 것을 구현하는 데에는 지정된 구간에서 임의의 정수 하나를 선택하는 `random`모듈의 `randrange()` 함수를 이용한다. 예를 들어, 1에서 180까지의 정수 중에 무작위로 5개의 값을 생성하려면 다음과 같이 실행한다.  
# ```python
# >>> import random
# >>> for _ in range(5):
#         print(random.randrange(1,181))
# ```
# 이 함수를 매초 실행하여 생성된 값이 180인 경우에만 프린팅 과제를 생성하도록 하면 초당 180분의 1로 어떤 사건이 발생하는 것을 모의실험할 수 있다. 초당 180분의 1의 확률로 프린팅 과제를 생성할지 여부를 판단하려면 아래 함수를 초당 한 번 실행하면 된다.
# ```python
# >>> def new_print_task():
#         num = random.randrange(1, 181)
# 
#         return num == 180
# ```
# 위 함수는 1에서 180 사이에서 임의로 선택된 값이 180인 경우 `True`를 반환한다. 
# :::
# 

# **모의실험 단계**  
# 모의실험은 아래 단계들로 이루어진다.
# 
# 1. 프린팅 큐 생성: 비어있는 상태.
# 2. 모든 프린팅 과제의 대기시간을 담아둘 빈 리스트 생성. 과제별 평균 대기시간 측정 용도.
# 3. 매 초당 아래 과제 수행
#     * 초당 180분의 1의 확률로 프린팅 과제 생성
#         * 생성된 시간 저장. 나중에 프린터가 실행될 때의 시간을 확인하여 대기시간을 측정할 수 있도록 함.
#         * 프린팅 과제 생성 후 바로 프린팅 큐에 추가
#     * 프린터가 대기 상태이고 프린팅 큐에 과제가 남아 있으면 아래 과제 수행
#         * 프린팅 큐의 헤드를 삭제하고 수행할 과제로 지정
#         * 해당 과제의 대기 시간 계산(현재 시간과 과제 생성시간의 차이) 후에 모든 과제의 대시기간 리스트에 추가
#         * 과제 출력 페이지 확인 후 출력에 필요한 시간 계산. 해당 시간 동안 프린터 상태가 busy로 표시되어 다음 프린팅 과제가 기다리게 됨.
#         * 해당 프린팅 과제가 완수되면 대기 상태로 전환
# 4. 모든 프린팅 과제 수행 후 과제별 평균 대기시간 계산

# 1단계) `Printer`클래스를 구현하여라. `Printer` 클래스가 가져야 하는 속성과 메서드는 다음과 같다.  
# * 분당 출력 페이지 수  : `self.page_rate`
# * 수행 대상 프린팅 과제 : `self.current_task`
# * 수행 대상 프린팅 과제 수행 시간 : `self.time_remaining`
# * 수행 중인 프린팅 과제 남은 수행 시간동안 busy 상태 유지 : `tick()` 메서드
# * 프린터 상태 : `busy()` 메서드
# * 다음 프린팅 과제 불러오기 : `start_next()` 메서드

# 2단계) `Task` 클래스를 구현하여라. `Task` 클래스가 가져야 하는 속성과 메서드는 다음과 같다.  
# * 프린팅 과제 생성 시간 : `self.timestamp`
# * 프린팅 대상 페이지 수 : 1 ~ 20 사이의 무작위 수 `self.pages`
# * 프린팅 과제 생성 시간 확인 : `get_stamp()` 메서드
# * 프린팅 대상 페이지 수 확인 : `get_pages()` 메서드
# * 과제 생성 후 프린팅 시작까지 대기 시간 : `wait_time()` 메서드

# 3단계) 모의실험 구현  
# 지정된 시간동안 프린팅 작업을 수행할 때 프린팅 과제당 평균 대기 시간을 계산하는 `simulation(num_second, pages_per_minutes)` 함수를 정의하여라.  
# 
# * `num_second` : 프린터 작동 시간
# * `pages_per_minutes` : 분당 출력 페이지 수
# 
# **주의사항** : 여기서는 `for` 반복문이 초당 1회 실행된다고 가정한다. 따라서 아래 함수들은 초당 1회 실행되는 것을 잘 구현한다.  
# * `new_print_task()`
# * `tick()`
# 
# 아래 코드는 분당 5장을 출력하는 프린터를 1시간동안 돌리는 모의실험을 100번 실행할 때의 결과를 보여준다. 
# 
# ```python
# >>> import numpy as np
# >>> average_wait_list = []
# >>> for i in range(100):
#         average_wait_list.append(simulation(3600, 5))
# >>> print(f"평균 대기시간: {np.mean(average_wait_list):6.2f} 초")
# ```

# ### 문제 

# 어느 카페의 바리스타 한명이 무작위적으로 입력되는 주문 작업을 수행할 때 벌어지는 일을 모의실험하여라. 모의실험의 목적은 손님이 주문을 하고 주문한 음료를 받을 때까지 평균적으로 걸리는 시간을 계산하는 일이다.  
