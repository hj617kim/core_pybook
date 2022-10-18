#!/usr/bin/env python
# coding: utf-8

# # 기초 IV(함수, 모듈)

# ## 함수

# ### 함수 정의하기

# 사용자는 함수를 임의로 정의하여 사용할 수 있다. 이번 장에서는 파이썬에서 함수를 정의하는 방법을 조금 더 자세히 살펴보자. 파이썬에서 함수를 정의할 때는 `def`라는 키워드를 사용하며, 아래의 형식을 따른다.   
# 
# ```
# def 함수이름(매개변수1, 매개변수2, ..., 매개변수n) :
#     함수본문
# ```
# 
# 함수의 반환값은 본문에 사용된 명령문을 실행하다가 어느 순간 아래 모양의 기본 명령문을 실행하는 순간 결정된다.  
# ```
# return 반환값  
# ```
# 위 `return` 명령문이 실행되는 순간 지정된 `반환값`이 가리키는 값이 반환되면서 함수의 실행이 멈춘다. 파이썬은 모든 함수가 하나의 반환값을 갖도록 강제한다. 예를 들어, `print()`함수처럼 반환값이 없는 것처럼 보이는 함수도 공식적으로는 아무런 의미가 없는 값을 의미하는 `None`을 반환값으로 사용한다. 즉, 아래 명령문이 항상 마지막에 실행된다.  
# ```
# return None  
# ```

# ### 인자와 매개변수   
# 
# 인자<font size="2">argument</font>는 함수를 호출할 때 실제로 함수에 전달되는 값이고, 매개변수<font size="2">parameter</font>는 인자를 함수본문에 전달하는 역할을 수행한다. 전달방식은 각 매개변수가 지정된 인자를 가리키도록 하는 변수 할당을 통해 이루어진다. 함수호출이 다음과 같이 진행되었다고 가정하자.   
# ```
# 함수이름(인자1, 인자2, ..., 인자n)
# ```
# 
# 그러면 함수본문이 실행되기 전에 다음 할당 명령문이 먼저 실행된다.  
# ```
# 매개변수1 = 인자1
# 매개변수2 = 인자2
# ...
# 매개변수n = 인자n  
# ```  

# #### 인자  
# 인자는 키워드 인자<font size="2">keyword argument</font>와 위치 인자<font size="2">positional argument</font>가 있다.  
# 
# * 키워드 인자 : 함수를 호출할 때, 식별자<font size="2">identifier</font>가 앞에 붙은 인자(예, `start = `) 또는 `**`를 앞에 붙인 딕셔너리로 전달되는 인자를 말한다. 키워드 인자는 굳이 지정하지 않으면 지정된 값을 사용한다. 예를 들어, `help()` 함수로 내장함수`sum()`의 사용 방법을 살펴보자. `sum()`은 숫자를 항목으로 갖는 이터러블을 인자로 받아, `start` 값과 이터러블의 모든 항목을 더한 값을 반환하는 함수다.   
# 
# ```python
# >>> print(help(sum))
# Help on built-in function sum in module builtins:
# 
# sum(iterable, /, start=0)
#     Return the sum of a 'start' value (default: 0) plus an iterable of numbers
#     
#     When the iterable is empty, return the start value.
#     This function is intended specifically for use with numeric values and may
#     reject non-numeric types.
# ```
# 
# `start`의 기본값은 0으로, 다른 값으로 변경하고 싶다면 `start = ` 방식 또는 `**`를 앞에 붙인 딕셔너리를 사용한다.          
# 
# ```python
# >>> sum([1, 1, 1])
# 3
# ```
# 
# 아래 `sum()`함수 호출에서 `10`은 키워드 인자이다. 
# ```python 
# >>> sum([1, 1, 1], start = 10)
# 13
# ```
# ```python
# >>> sum([1, 1, 1], **{'start': 10})
# 13
# ```
# 
#   
# * 위치 인자 : 키워드 인자가 아닌 인자를 말한다. 이터러블 앞에 `*`를 붙여 값을 전달할 수도 있다. 예를 들어, `help()` 함수로 내장함수`divmod()`의 사용 방법을 살펴보자. `divmod()`는 두 수를 인자로 받아, 두 수의 몫과 나머지를 튜플로 묶어 반환하는 함수다.    
# 
# ```python
# >>> help(divmod) 
# Help on built-in function divmod in module builtins:
# 
# divmod(x, y, /)
#     Return the tuple (x//y, x%y).  Invariant: div*y + mod == x.
# ```
# 
# 다음과 같은 `divmod()`함수의 호출에서 `7`과 `2`는 모두 위치 인자이다.   
# ```python
# >>> divmod(7, 2)
# (3, 1)
# ```
# 
# ```python
# >>> divmod(*(7, 2))
# (3, 1)
# ```
# 
# :::{admonition} 주의  
# :class: caution  
# `divmod(x, y, /)`에서 `/`는 그 앞에 있는 매개변수가 위치 전용임을 나타낸다. 따라서 `divmod()`함수를 호출할 때 키워드 인자를 사용하면 오류가 발생한다. 
# 
# ```python
# >>> divmod(x = 7, y = 2) 
# TypeError                                 Traceback (most recent call last)
# /tmp/ipykernel_1321/2561811967.py in <module>
# ----> 1 divmod(x = 7, y = 2)
# 
# TypeError: divmod() takes no keyword arguments
# ```
# :::
# 
# 
# :::{admonition} 참고    
# :class: info    
# `*`을 사용하면, 다음과 같이 이터러블의 각 항목을 편리하게 출력할 수 있다. 
# ```python
# >>> a_list = ['Hello', 'python!']
# >>> print(*a_list)
# Hello python!
# ```
# :::
# 
# 

# #### 매개변수   
# 
# 예제와 함께 살펴보자.   
# 
# ````{prf:example}  
# :label: parameter-example01   
# 
# 두 수를 인자로 받아, 그 합을 반환하는 함수 `my_sum()`을 정의하여라.   
# ```` 

# 다음과 같이 `my_sum()`함수를 정의할 수 있다. 
# ```python
# >>> def my_sum(a, b) :
#         return a + b
# ```
# 
# 위의 함수는 위치 인자를 사용해서 아래와 같이 호출할 수 있다. 
# ```python
# >>> print(my_sum(1, 3))
# 4
# ```
# 
# 매개변수가 위치 전용임을 나타내기 위해 `/`를 사용할 수 있다. 그러면 `/`는 그 앞에 있는 매개변수가 위치 전용임을 나타낸다. 
# ```python
# >>> def my_sum(a, b, /) :
#         return a + b
# ```
# 
# 함수를 호출하는 방법은 이전과 같다. 
# ```python
# >>> print(my_sum(1, 3))
# 4
# ```

# ````{prf:example}
# :label: parameter-example02
# 두 수를 인자로 받아, 그 합을 반환하는 함수 `my_sum_10()`을 정의하여라. 단, 하나의 수를 인자로 사용하면, 그 수에 10을 더한 값을 반환한다.    
# ````

# 다음과 같이 `my_sum_10()` 함수를 정의할 수 있다. 
# 
# ```python
# >>> my_sum_10(a, b = 10) :
#         return a + b
# ```
# 
# 두 수를 인자로 사용하면, 두 수의 합을 반환한다. 
# ```python
# >>> print(my_sum_10(1, 3))
# 4
# >>> print(my_sum_10(1, b = 3))
# 4
# ```
# 
# 하나의 수를 인자로 사용하면, 그 수에 10을 더한 값을 반환한다. 
# ```python
# >>> print(my_sum_10(1))  
# 11
# ```
# 
# 첫 번째 인자는 위치 전용임을 나타내기 위해 `/`를 사용하여 함수를 정의할 수도 있다.  
# ```python
# >>> my_sum_10(a, /, b = 10) :
#         return a + b
# ```
# 함수 호출 방법은 이전과 같다. 
# ```python
# >>> print(my_sum_10(1, 3))
# 4
# >>> print(my_sum_10(1, b = 3))
# 4
# >>> print(my_sum_10(1))
# 11
# ```
# 
# 두 번째 인자는 키워드 전용임을 나타내기 위해 `*`을 사용하여 함수를 정의할 수도 있다. 그러면 `*`는 그 뒤에 있는 매개변수가 키워드 전용임을 나타낸다.   
# ```python
# >>> my_sum_10(a, /, *, b = 10) :
#         return a + b
# ```
# 
# 함수를 호출할 때는 `*` 뒤에는 무조건 키워드 인자를 사용해야 한다.  
# ```python
# >>> print(my_sum_10(1, b = 3))
# 4
# >>> print(my_sum_10(1))
# 11
# ```
# 
# 위치 인자를 사용하면, 오류가 발생한다.  
# ```python
# >>> print(my_sum_10(1, 3))
# TypeError                                 Traceback (most recent call last)
# /tmp/ipykernel_1321/3815314647.py in <module>
# ----> 1 print(my_sum_10(1, 3))
# 
# TypeError: my_sum_10() takes 1 positional argument but 2 were given
# ```
# 
# 

# :::{admonition} 주의   
# :class: caution  
# 함수가 가변 객체를 변경하면 기본값이 변경될 수 있기 때문에, 키워드 매개변수의 기본값으로 가변 객체를 사용하지 않는 것이 좋다. 예를 들어, 빈 리스트를 기본값으로 갖는 `no_func()`함수를 살펴보자. 이 함수는 첫 번째 인자를 두 번째 인자의 항목으로 추가하여 반환하는 함수다.  
# 
# ```python
# >>> def no_func(a, b = []) :
#         b.append(a)
#         return b
# ```
# 
# 함수를 한 번 호출하면 `[1]`를 반환하지만, 두 번째 호출에서는 기본값이 변경되어 `[1]`이 아닌 `[1, 1]`을 반환하는 겂을 볼 수 있다.  
# ```python
# >>> print(no_func(1))
# [1]
# ```
# 
# ```python
# >>> print(no_func(1))
# [1, 1]
# ``` 
# :::
# 

# :::{admonition} 가변 위치<font size ="2">var-positional</font>  
# :class: info  
# 입력 값이 여러 개이지만 몇 개가 입력될지 모를 때는 매개변수 이름 앞에 `*`를 붙이는 방식을 사용하면 된다. 그러면, 입력 값을 전부 모아서 튜플로 만들어 준다. 예를 들어, `zip(*iterables)` 함수는 여러 개의 이터러블을 인자로 받아 각 항목을 튜플로 묶은 형태로 이터레이터를 만들어 반환한다.  
# :::

# ````{prf:example}
# :label: parameter-example03  
# 여러 개의 수를 인자로 받아, 그 합을 구하는 함수 `my_auto_sum()`을 정의하여라.  
# ````

# 다음과 같이 `*args`를 매개변수로 사용하여 `my_auto_sum()` 함수를 정의할 수 있다. `args`는 `arguments`의 약자로, 다른 매개변수 이름으로 변경해도 된다.    
# 
# ```python
# >>> def my_auto_sum(*args) :
#         s = 0
#         for i in args :
#             s += i
#         return s
# ```
# 
# ```python
# >>> print(my_auto_sum(1))
# 1
# >>> print(my_auto_sum(1, 2))
# 3
# >>> print(my_auto_sum(1, 2, 3))
# 6
# >>> print(my_auto_sum(1, 2, 3, 4))
# 10
# >>> print(my_auto_sum(1, 2, 3, 4, 5))
# 15
# >>> print(my_auto_sum(*(1, 3, 5)))
# 9
# ```

# :::{admonition} 가변 키워드<font size ="2">var-keyword</font>    
# :class: info  
# 
# 임의의 개수의 키워드 인자들을 사용해야 할 때는 매개변수 이름 앞에 `**`를 붙이는 방식을 사용하면 된다. 그러면, 입력 값을 전부 모아서 딕셔너리로 만들어 준다. 예를 들어, `dict(**kwargs)` 함수는 여러 개의 키워드 인자들을 입력받아 딕셔너리로 만들어 반환한다. `kwargs`는 `keyword arguments`의 약자이다.   
# 
# 예를 들어, 가변 키워드를 리턴하는 함수 `return_kwargs()`를 정의해보자.  
# ```python
# >>> def return_kwargs(**kwargs) :
#         return kwargs
# ```
# 
# 키워드 인자로 `강현 = 3`을 사용하여 함수를 호출하면, `{'강현': 3}`이 반환된다. 
# ```python
# >>> print(return_kwargs(강현=3))
# {'강현': 3}
# ```
# 
# 키워드 인자로 `강현 = 3`와 `나현=5`을 사용하여 함수를 호출하면, `{'강현': 3, '나현': 5}`이 반환된다. 
# ```python
# >>> print(return_kwargs(강현=3, 나현=5))
# {'강현': 3, '나현': 5}
# ```
# :::

# ### 문서화 문자열  
# 
# 프로그래밍 코드를 저장한 파일에는 코드 외에 코드와 관련된 주석을 적절하게 포함하고 있어야 하는데, 이를 **문서화**라고 한다. 문서화가 제대로 되어있지 않으면 프로그램 개발 및 관리가 어렵기에 문서화는 코드 이상으로 중요하다. 문서화의 기본은 함수에 주석을 추가하는 것이다. 함수 정의에 사용되는 주석을 문서화 문자열<font size="2">docstring</font>이라고 부른다. 큰 따옴표 세 개(`"""..."""`) 또는 작은 따옴표 세 개(`'''...'''`)로 둘러싸인 부분이 문서화를 위해 사용되며 주석으로 처리된다. 예를 들어, 두 수를 인자로 받아, 그 합을 반환하는 함수 `my_sum()`에 문서화 문자열을 추가해보자.      

# In[1]:


def my_sum(a, b) :
    """
        두 개의 숫자를 입력받아, 그 합을 되돌려준다. 
    """
    return a + b


# 함수에 문서화 문자열을 추가하면, `help()`함수를 사용하여 해당 함수의 역할 및 사용법을 확인할 수 있다.  

# In[2]:


help(my_sum)


# ### 제1종 객체  
# 프로그래밍 언어에서 **제1종 객체**<font size="2">first-class object</font>는 변수 할당, 함수의 인자, 함수의 반환값 등으로 사용될 수 있는 객체<font size="2">object</font>를 가리킨다. 반면에 그렇지 않은 객체를  **제2종 객체**<font size="2">second-class object</font>라고 한다.   
# 
# 
# :::{admonition} first-class object 
# :class: info    
# first-class object는 주로 '일급 객체'로 번역되지만, 그보다는 제1종 객체라 하는 것이 개념상 적절하다. first-class와 second-class는 사용법상 구분을 나타내는 반면에 일급과 이급 표현은 질적 차이를 내포하기 때문이다.  
# :::  
# 
# 프로그래밍 언어에 따라 제1종 객체의 기준이 다르다. 예를 들어, C언어에서는 함수가 다른 함수의 인자 또는 반환값으로 사용할 수 없기 때문에 제1종 객체가 아니다. 반면에 파이썬에서는 다룰 수 있는 모든 것이 제1종 객체이다.   
# 
# 

# **함수를 변수에 할당**  
# 함수도 하나의 값이라 변수 할당에 사용될 수 있다. 예를 들어, `print()` 함수를 `a_func` 변수에 할당해보자. 함수를 하나의 값으로 취급할 때는 괄호를 사용하지 않는다.   

# In[3]:


a_func = print


# In[4]:


print(a_func)


# In[5]:


a_func('안녕하세요!')


# 괄호를 사용하면 함수 호출을 의미하기 때문에 아래 코드는 `print()` 함수가 호출된 후에 반환한 `None`이 변수에 할당된다. 

# In[6]:


a_return_value = print()
print(a_return_value)


# **함수를 다른 함수의 인자로 사용**  
# 함수를 다른 함수의 인자로 사용할 수 있다. 예를 들어, `map(function, iterable)` 함수는 `iterable`의 모든 항목에 `function`을 적용한 후 그 결과를 돌려주는 이터레이터를 반환한다. 

# ````{prf:example}
# :label: parameter-example04
# 하나의 인자를 받는 함수와 그 함수의 인자로 사용될 값을 인자로 받아 둘째 인자로 들어온 값에 대해 첫째 인자 함수를 두 번 연속 적용한 값을 반환하는 함수 `do_twice(func, arg)`를 정의하여라. 함수 `f`를 인자 `x`에 두 번 연속 적용한다는 의미는 `f(f(x))`를 의미한다.    
# ````

# `do_twice()`함수는 다음과 같이 정의할 수 있다. 

# In[7]:


def do_twice(func, arg) :
    x = func(arg)
    return func(x)


# 그 다음 `do_twice()`의 인자로 사용할 함수를 하나 정의해보자. 아래 `three_times()`함수는 인자의 세 배를 계산하여 반환한다.  

# In[8]:


def three_times(num) :
    return num * 3


# `three_tiems()` 함수를 정수 `5`에 대해 두 번 연속으로 적용한 값은 45이다. 실제로 5의 세 배는 15, 15의 세 배는 45이다. 다음과 같이 확인할 수 있다.  

# In[9]:


three_times(three_times(5))


# `do_twice()`함수를 사용하여 동일한 결과를 얻을 수 있다. 

# In[10]:


do_twice(three_times, 5)


# **함수가 다른 함수를 반환**  
# 함수를 반환하는 함수를 정의할 수 있다. 예를 들어, 다음의 `adding_n_func(n)` 함수를 생각해보자. `adding_n_func(n)`함수를 호출하면, `n`을 더하는 함수 `my_add_n()`을 반환한다. 

# In[11]:


def adding_n_func(n) :
    
    def my_add_n(m) :
        return n + m
    
    return my_add_n


# `my_add_n()` 함수는 `adding_n_func()` 함수의 본문에서 정의되는 함수이다. 따라서 `adding_n_func()` 함수 밖에서는 절대 사용될 수 없는 일종의 지역 변수이며, 이런 의미로 지역 함수<font size = "2">local function</font>라 불린다.  
# 실제로, `my_add_n()` 함수를 사용하려면 `n`에 해당하는 값이 필요한데 그 값은 `adding_n_func(10)`등이 먼저 실행되어야 정해진다.   
# 이 성질을 이용하여 입력값에 10을 더한 값을 반환하는 함수 `my_add_10()`를 다음과 같이 정의하여 활용할 수 있다.  

# In[12]:


my_add_10 = adding_n_func(10)  # 10을 더하는 함수
my_add_10(3)                   # 10 + 3


# ### 지역 변수와 전역 변수

# 변수들은 어디에서 정의되었는가에 따라 지역 변수<font size="2">local variable</font> 또는 전역 변수<font size="2">global variable</font>라 불린다. 함수를 선언할 때 사용되는 매개변수와 함수 본문에서 선언되는 변수는 함수가 실행되는 동안에만 의미를 갖는 변수들이며, 이런 변수들을 **지역 변수**라 부른다. 반면에 함수 밖에서도 의미를 갖는 변수는 **전역 변수**이다.   
# 
# :::{admonition} 유효범위<font size= "2">scope</font>  
# :class: info    
# 변수의 수명 또는 변수가 유효한 범위를 유효범위라고 부른다. 예를 들어, 전역 변수의 유효범위는 프로그램 전체이고, 지역 변수의 유효범위는 그 변수를 선언한 함수 내부이다.      
# :::
# 
# 
# 예를 들어, 아래의 코드에서 매개변수 `a`, `b`와 함수본문에서 선언된 `local_var`변수는 모두 지역 변수이다. 반면에 `global_var`변수는 전역 변수이다.  

# In[13]:


global_var = 3

def my_add(a, b) :
    local_var = a + b
    return local_var


# 지역변수들은 함수밖에서는 어떤 의미를 갖지 않는다. 예를 들어, `my_add()` 함수를 호출한 다음 `local_var` 변수 값을 출력하려고 하면, 이름이 존재하지 않음을 의미하는 `NameError`오류가 발생한다.   
# 
# ```python
# >>> my_add(1, 2)
# 3
# ```
# 
# ```python
# >>> print(local_var)
# NameError                                 Traceback (most recent call last)
# /tmp/ipykernel_1321/1445025415.py in <module>
# ----> 1 print(local_var)
# 
# NameError: name 'local_var' is not defined
# ```

# :::{admonition} `global` 키워드  
# :class: info  
# 
# 아래의 코드에서 `var` 변수는 전역 변수이고, 함수 `func_a()` 안에서 정의된 `var` 변수는 지역 변수이다. 
# ```python
# >>> var = 'global'  # 전역 변수 var
# ```
# 함수 안에서 `var`변수에 `'local'`을 할당해도 전역 변수의 값이 변경되지 않는다.  
# ```python
# >>> def func_a() :
#         var = 'local'  # 지역 변수 var
#         return var
# ```
# 
# 실제로, `var`의 값을 확인하면 `global`이다.  
# ```python
# >>> print(var)
# global
# ```
# 
# 반면, 함수를 실행하면 지역 변수`var`에 할당된 값인`local`이 반환된다. 
# ```python
# >>> print(func_a())
# local
# ```
# 
# 함수 내부에서 선언된 지역 변수를 전역 변수처럼 사용하려면 `global` 키워드를 사용한다. 
# ```python
# >>> def func_a() :
#         global var
#         var = 'local'  
#         return var
# ```
# 그런 다음에 `var`의 값을 확인하면 `local`이고, `func_a()`의 반환값도 `local`이다. 
# ```python
# >>> print(var)
# local
# ```
# ```python
# >>> print(func_a())
# local
# ```
# 변수의 유효범위를 변경하면 의도하지 않은 일이 발생할 수도 있기 때문에 가능하면 사용하지 않는 것이 좋다. 
# :::

# ### 익명함수(람다함수)

# 파이썬은 익명함수 또는 lambda 함수라고 하는, 값을 반환하는 단순한 한 문장으로 이루어진 함수를 지원한다. 람다 함수를 사용하면 간결하게 코드를 작성할 수 있다. 람다 함수의 형식은 아래와 같다.  
# 
# ```
# lambda arguments : expression
# ```  
# 
# 예제와 함께 살펴보자. 예를 들어, 숫자를 인자로 받아 5를 더한 값을 반환하는 함수는 아래와 같이 정의할 수 있다. 

# In[14]:


def plus_5(n) :
    return n + 5


# In[15]:


print(plus_5(10))
print(plus_5(20))


# 람다 함수를 사용하면, 아래와 같이 코드를 작성할 수 있다. 

# In[16]:


x = lambda a : a + 5


# In[17]:


print(x(10))
print(x(20))


# 두 숫자를 인자로 받아 그 곱을 반환하는 함수는 아래와 같이 정의할 수 있다. 

# In[18]:


y = lambda a, b : a * b


# In[19]:


print(y(2, 3))
print(y(4, 5))


# 람다 함수는 `map(function, iterable)`함수의 인자 등 한 번만 사용할 함수를 정의할 때 사용하면 좋다. 예를 들어, 리스트 `[1, 2, 3, 4, 5]`의 각 항목을 제곱한 다음 5를 더한 값을 항목으로 갖는 리스트 `[6, 9, 14, 21, 30]`을 만들 때, 다음과 같이 코드를 작성할 수 있다. 

# In[20]:


list(map(lambda x : x ** 2 + 5, [1, 2, 3, 4, 5]))


# ````{prf:example}  
# :label: parameter-example05  
# 시퀀스형과 항목을 인자로 받아 시퀀스에 인자로 들어온 항목이 몇 번 등장하는지를 반환하는 `my_count()` 함수를 정의하여라. 이때, 시퀀스형이 문자열이면, 항목으로 들어온 부분 문자열이 문자열에 몇 번 등장하는지를 반환한다.   
# ````

# In[21]:


def my_count(seq, item, is_str = True) :
    cnt = 0
    if is_str :
        for i in range(len(seq) - len(item) + 1) :
            if seq[i : i + len(item)] == item :
                cnt += 1
    else :
        for i in seq :
            if i == item :
                cnt += 1
    return cnt


# In[22]:


my_count('Hello, World! Hello, Python!', 'lo')


# In[23]:


my_count((1, 3, 5, 3, 5, 7), 3, is_str = False)


# ````{prf:example}  
# :label: parameter-example06
# 여러 개의 이터러블을 인자로 받아 각 항목을 튜플로 묶은 형태로 이터레이터를 만들어 반환하는 `my_zip()` 함수를 정의하여라. 
# ````

# In[24]:


def my_zip(*iterables) :
    iterators = [iter(it) for it in iterables]
    while True :
        try : 
            result = []
            for it in iterators :
                result.append(next(it))
            yield tuple(result)
        except StopIteration:
            return


# In[25]:


my_iter = my_zip([1, 2, 3], (1, 2), range(5))


# In[26]:


next(my_iter)


# In[27]:


next(my_iter)


# ## 모듈  
# 
# 모듈은 파이썬 코드를 담고 있는, 확장자가 `py`인 파일이다. 하나의 모듈에는 관련된 일을 처리할 때 사용하는 여러 프로그램 코드들이 포함되어 있다. 예를 들어, `math` 모듈은 `sin()`, `cos()`, `log()` 등 수학에서 매우 중요한 역할을 하는 함수들이 정의되어 있고, `time` 모듈에는 `sleep()` 함수처럼 시간 활용과 관련된 다양한 함수가 포함되어 있다. 그리고 `random` 모듈에는 임의의 정수를 생성하는 것과 관련된 함수 `randint()`등이 정의되어 있다. 모듈은 언제든지 불러와서<font size="2">import</font> 모듈에 포함된 내용을 활용할 수 있다.    

# :::{admonition} 파일 확장자    
# :class: info    
# 파일 확장자는 파일의 형식이나 종류를 표시하기 위해 파일명 뒤에 사용하는 것이다. 예를 들어, 확장자가 `hwp`라면 한글 문서 파일인 것을 알 수 있다.  
# :::
# 

# ### 모듈 만들기 

# 먼저 모듈을 만들어보자. 아래와 같이 앞에서 만든 함수들을 담고 있는 `myfunc.py` 파일을 만든다.  
# 
# ```
# def my_count(seq, item, is_str = True) :
#     count = 0
#     if is_str :
#         for i in range(len(seq) - len(item) + 1) :
#             if seq[i : i + len(item)] == item :
#                 count += 1
#     else :
#         for i in seq :
#             if i == item :
#                 count += 1
#     return count
#     
# 
# def my_zip(*iterables) :
#     iterators = [iter(it) for it in iterables]
#     while True :
#         try : 
#             result = []
#             for it in iterators :
#                 result.append(next(it))
#             yield tuple(result)
#         except StopIteration:
#             return
#         
# 
# print(my_count('helheloh', 'lh'))
# print(my_count((1, 3, 5, 3, 5, 7), 3, is_str = False))
# 
# my_iter = my_zip([1, 2, 3], (1, 2), range(5))
# print(next(my_iter))
# print(next(my_iter))
# ```

# ### 모듈 사용법  
# 
# 특정 모듈에 포함된 코드(예를 들어, 함수 등)를 사용하려면 먼저 해당 모듈을 `import` 해야 한다. 모듈을 임포트하는 방법을 살펴보자.  

# **모듈 임포트 방법1**   
# ```
# import 모듈이름
# ``` 
# 예를 들어, 앞에서 만든 `myfunc.py` 모듈을 임포트하고 싶다면, 아래와 같이 코드를 작성하고 실행하면 된다.   

# In[28]:


import myfunc


# :::{admonition} `__name__` 속성과 `__main__` 함수  
# :class: info  
# 모듈을 임포트하면, 파일 전체가 실행되면서 `print()` 함수로 작성된 코드가 실행되는 것을 볼 수 있다.  
# ```
# 1
# 2
# (1, 1, 0)
# (2, 2, 1)
# ```
# 
# 그런데 이 코드는 파일에 있는 함수가 제대로 작동하는가를 확인하는 용도로 작성된 코드이며, 모듈을 불러올 때 굳이 실행할 필요가 없다. 이런 경우에는 모듈의 `__name__` 속성을 이용하여 아래와 같이 작성하면 모듈을 임포트할 때 굳이 실행할 필요가 없는 코드를 모듈에 포함시킬 수 있다. 
# 
# ```
# if __name__ == '__main__' :
#     print(my_count('helheloh', 'lh'))
#     print(my_count((1, 3, 5, 3, 5, 7), 3, is_str = False))
# 
#     my_iter = my_zip([1, 2, 3], (1, 2), range(5))
#     print(next(my_iter))
#     print(next(my_iter))
# ```
# 
# 위와 같이 하면 `import myfunc`를 실행해도 `if __name__ == '__main__' :` 아래 들여쓰기된 코드는 실행되지 않는다. 반면에 `shell`에서 `python myfunc.py` 형태로 `myfunc.py` 코드를 직접 실행하면 `if __name__ == '__main__' :` 조건문의 본체가 실행된다. 
# 
# 그 이유는 다음과 같다. 파이썬에서 함수, 클래스, 모듈 등은 `__name__`이라는 특별한 속성을 가지고 있는데, 이는 항상 자기 자신을 가리킨다.  
# 
# 예를 들어, 아래 함수를 살펴보자.  
# ```python
# >>>def my_name() :
#        pass
# ```
# 
# 이제 `my_name()` 함수의 `__name__` 속성을 확인해보자. 속성 확인은 자료형의 메서드를 호출하는 방식과 비슷하다. 다만, 속성은 함수가 아니라 괄호를 사용하지 않는다. 
# 
# ```python
# >>> my_name.__name__
# 'my_name'
# ```
# 
# 모듈도 `__name__` 속성을 갖는다. `myfunc.py` 모듈의 `__name__` 속성을 확인해보자. 
# 
# ```python
# >>> myfunc.__name__
# 'myfunc'
# ```
# 
# 이렇게 `import`로 모듈을 가져오면 `__name__` 속성에는 모듈의 이름이 저장되는데, 모듈 파일을 직접 실행했을 때는 모듈의 이름이 아니라 `__main__`이 저장된다.   
# 
# `__main__` 의 이런 기능은 C, Java 등에서 의무적으로 사용되는 `main` 함수와 유사한 기능을 수행한다. `Repl.it` 사이트에서 `main.py` 가 기본적으로 실행되는 이유가 이런 전통에서 유래한다.
# :::
# 

# 모듈에 포함된 코드를 사용할 때는 `모듈이름.코드` 형식을 사용한다. 예를 들어, `myfunc.py` 모듈에 있는 `my_zip()` 함수를 사용하고 싶다면 아래와 같이 코드를 작성하면 된다. 

# In[29]:


range_iter = myfunc.my_zip(range(3), range(5))
for _ in range_iter :
    print(_)


# **모듈 임포트 방법2**  
# 모듈의 이름이 길 경우에는 별칭을 줄 수 있다.  
# ```
# import 모듈이름 as 별칭
# ```  
# 
# 예를 들어, `myfunc.py` 모듈을 별칭`mf`를 사용하여 임포트하고 싶다면, 아래와 같이 코드를 작성하고 실행하면 된다.

# In[30]:


import myfunc as mf


# 모듈에 포함된 코드를 사용할 때는 `별칭.코드` 형식을 사용한다. 예를 들어, `myfunc.py` 모듈에 있는 `my_count()` 함수를 사용하고 싶다면, 이번에는 아래와 같이 코드를 작성하면 된다. 

# In[31]:


count_l = mf.my_count('Hello, world', 'l')
print(f'l의 개수는 {count_l}개이다.')


# **모듈 임포트 방법3**  
# 모듈에서 원하는 코드만 가져올 수 있다. 이 경우 모듈 이름을 추가로 붙일 필요가 없어진다. 이 방식은 특정 코드를 자주 활용해야 할 경우 추천한다.  
# ```
# from 모듈이름 import 특정코드
# ```

# 예를 들어, `myfunc.py` 모듈에 있는 `my_zip()` 함수만 가져오고 싶다면, 아래와 같이 코드를 작성하면 된다. 

# In[32]:


from myfunc import my_zip


# 그러면 모듈 이름을 추가로 붙이지 않고 `my_zip()` 함수를 사용할 수 있다. 

# In[33]:


my_zip_iter = my_zip(range(10), 'abcde')
for i in my_zip_iter :
    print(i)


# :::{admonition} 주의    
# :class: caution  
# 이 경우에는 모듈에 포함된 다른 코드는 사용할 수 없다.  
# ```python
# >>> count_l = my_count('Hello, world', 'l')
# NameError                                 Traceback (most recent call last)
# /tmp/ipykernel_1412/1744407135.py in <module>
# ----> 1 count_l = my_count('Hello, world', 'l')
# 
# NameError: name 'my_count' is not defined
# ```
# :::
# 

# **모듈 임포트 방법4**  
# 특정 모듈에 포함된 코드 전체를 한꺼번에 임포트할 수도 있다. 다만, 일반적으로 추천되는 방식은 아니다.  
# ```
# from 모듈이름 import * 
# ```

# 예를 들어, `myfunc.py` 모듈 전체를 한꺼번에 임포트해보자.  

# In[34]:


from myfunc import *


# 그러면 모듈 이름을 추가로 붙이지 않고, `myfunc.py` 모듈에 있는 코드를 사용할 수 있다. 

# In[35]:


count_l = my_count('Hello, world', 'l')
print(f'l의 개수는 {count_l}개이다.')


# **모듈 내용 확인하기**  
# 특정 모듈에 포함된 함수 등을 확인하기 위해 `help()`함수를 사용할 수 있다. 

# In[36]:


help(myfunc)


# ## 연습문제

# ### 문제  
# 진약수를 구하여 합한 값이 상대 수가 되는 두 수를 **친화수**라고 부른다. 예를 들어, 220와 284는 친화수이다.   
# * 220의 진약수 : 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110 & 1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110 = 284  
# * 284의 진약수 : 1, 2, 4, 71, 142 & 1 + 2 + 4 + 71 + 142 = 220   
# 두 수를 입력받아 그 수가 친화수인지 여부를 반환하는 함수`amicable_nums()`를 정의하여라.   
# 
# Input :  `amicable_nums(220, 284)`      
# Output : `220과 284는 친화수입니다.`   
# 
# Input :  `amicable_nums(1184, 1210)`    
# Output : `1184과 1210는 친화수입니다.`  
# 
# Input :  `amicable_nums(6230, 6368)`   
# Output : `6230과 6368는 친화수가 아닙니다.`  

# ### 문제  
# `iterable`의 모든 항목에 `function`을 적용한 후 그 결과를 돌려주는 이터레이터를 반환하는 `my_map(function, iterable)` 함수를 정의하여라.  

# ### 문제  
# 단어우월효과<font size="2">word superiority effect</font>란 문장 속에 단어가 비정상적인 순서로 배열되더라도 이를 정하확게 인지할 수 있는 현상을 말한다. 문자열을 인자로 받아 각 단어의 순서를 임의로 배열한 다음 반환하는 `word_superiority_effect()`함수를 정의하여라. 단, 각 단어의 첫 문자는 그 위치 그대로 둔다. 
# 
# Input : 
# ```
# words = '문장 속에 단어가 비정상적인 순서로 배열되더라도 이를 정확하게 인지할 수 있다'
# word_superiority_effect(words) 
# ```
# 
# 아래는 하나의 예시로, 임의로 배열했을 때 아래와 같지 않을 수 있다.   
# Output : `문장 속에 단가어 비상정적인 순로서 배되열더라도 이를 정하확게 인할지 수 있다` 
# 
# 필요하다면, `random` 모듈의 `sample()` 함수를 사용한다. `sample(x, k)` 은 시퀀스`x`의 항목에서 `k`개를 중복없이 임의로 뽑아 리스트로 반환해주는 함수다. 예를 들어, 아래와 같이 코드를 작성하면, 문자열에서 각 문자를 중복없이 임의로 선택해 리스트로 만들어준다.      

# In[37]:


import random


# In[38]:


a_word = 'abc'
print(random.sample(a_word, len(a_word)))
print(random.sample(a_word, len(a_word)))


# ### 문제  
# 타겟들을 인자로 받아 주어진 문장에서 가장 많이 등장하는 타켓단어가 무엇이고, 몇 번 등장하는지를 반환하는 함수 `target_words()`를 정의하여라. 문제에서 말하는 타겟단어란 타겟(예, 단어 맨 뒤에 붙는 `은`, `는`, `이`, `가`, `을`, `를` 등의 조사) 중 하나가 붙어 있는 단어를 말한다. 주어진 문장은 `파이썬은 범용 프로그래밍 언어로 간결하고 쉬운 문법을 가지고 있다`로, 변경하고 싶다면 키워드 인자(예, `words =`)를 사용한다.    
# 
# Input : `target_words('은')`    
# Output : `파이썬(1)`   
# 
# Output의 순서는 중요하지 않다.  
# 
# Input : `target_words('은', '로')`  
# Output : `파이썬(1) 언어(1)`  
# 
# Input : 
# ```
# words = '눈 눈이 와요 눈 눈이 와요 눈이 와요 눈이 와요 창밖에도 눈이 와요'  
# target_words('이', words = words)  
# ```
# Output : `눈(5)`  
#   
# Input :  
# ```
# words = '고양이는 밥을 먹고 있고, 강아지는 잠을 자고 있다'
# target_words('는', words = words)   
# ```  
# Output : `고양이(1) 강아지(1)`

# ### 문제  
# 모듈 만들기
