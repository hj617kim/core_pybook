#!/usr/bin/env python
# coding: utf-8

# # 파이썬 프로그래밍의 기초 I

# ## 기본 자료형

# 자료형<font size = "2">Data Type</font>은 컴파일러나 인터프리터에게 데이터를 어떻게 사용할 것인지 알려주는 데이터 속성 중 하나다.   
# 파이썬에서 지원하는 몇 가지 주요 자료형을 간단히 살펴보자. 

# * 숫자형 <font size = "2">Numeric Types</font>
#     * 정수형 <font size = "2">Integral</font>
#         * 정수 <font size = "2">`int`</font>
#         * 불리언 <font size = "2">`bool`</font>
#     * 부동소수점 <font size = "2">`float`</font>
# 
# * 문자열 <font size = "2">`str`</font>
# * `None`

# ### 정수 

# 일반적으로 알고 있는 정수<font size = "2">int</font>(자연수, 0, 음의 정수)들의 자료형이다. 정수형으로 나타내면 덧셈, 뺄셈, 곱셈, 나눗셈 등의 기본 연산이 가능하다.  
# 예를 들어, ..., -3, -2, -1, 0, 1, 2, 3, ...은 모두 정수형(`int`)이다.  

# In[1]:


2 + 3 - 4


# In[2]:


4 * 2


# ### 부동소수점  

# 부동소수점<font size = "2">float</font>은 원래 실수를 컴퓨터에서 다루기 위해 개발되었으나 실제로는 유리수 일부만을 다룬다. 무리수인 원주율 $\pi$의 경우에도 컴퓨터의 한계로 인해 소수점 이하 적당한 자리에서 끊어서 사용한다. 예를 들어, 1.2, 0.333, -1.2, -3.7680, 4.0, .7 등은 모두 부동소수점형(`float`)이다.  

# In[3]:


1.2 + 3.5


# :::{admonition} 참고  
# :class: info  
# 정수부나 소수부가 0이라면 생략하고 작성할 수 있다. 예를 들어, `0.7`은 `.7`로, `1.0`은 `1.`이라고 작성할 수 있다.  
# ```python 
# >>> 0.7 == .7
# True
# >>> 1.0 == 1.
# True
# ```
# :::

# :::{admonition} 지수 표현 방식  
# :class: info  
# `e`나 `E` 다음에 오는 수는 10의 지수가 된다. 예를 들어, `30000.0`은 `3e4` 또는 `3E4`라고 작성할 수 있다.
# ```python 
# >>> 30000.0 == 3e4
# True
# >>> 30000.0 == 3E4
# True
# ```
# 이렇게 표현된 수는 부동소수점이다. 
# :::

# :::{admonition} 부동소수점의 한계  
# :class: caution  
# 부동소수점은 십진 소수를 정확하게 표현하지 못한다. 예를 들어, `0.1 + 0.1 + 0.1`을 계산하면 0.30000000000000004으로 `0.3`이 같은지를 확인하면 `False`가 나온다. 
# 
# ```python
# >>> 0.1 + 0.1 + 0.1
# 0.30000000000000004
# >>> 0.1 + 0.1 + 0.1 == 0.3
# False
# ```
# :::

# #### 기본 연산

# 파이썬의 기본 연산을 표로 정리하면 아래와 같다. 

# |연산 기호|의미|예시|실행 결과|
# |:----------:|:----------:|:----------:|:--------:|
# |`+`|덧셈| `3 + 4` |`7`|
# |`-`|뺄셈| `7 - 2` | `5`|
# |`*`|곱셈| `2 * 6` | `12`|
# |`/`|나눗셈|`14 / 4`|`3.5`|
# |`**`|지수|`2 ** 3`|`8`|
# |`//`|몫|`9 // 2`|`4`|
# |`%`|나머지|`3 % 2`|`1`|

# In[4]:


7 ** 3


# In[5]:


9 ** 0.5


# In[6]:


7 / 3


# In[7]:


7 // 3 


# In[8]:


7 % 3


# :::{admonition} 참고  
# :class: info
# 
# (a // b) * b + a % b 를 구하면 a이다. 
# :::

# In[9]:


7 == (7 // 3) * 3 + 7 % 3


# In[10]:


-7 == (-7 // 3) * 3 + (-7 % 3)


# ### 문자열 

# 문자열<font size = "2">str</font>은 문자들을 나열한 값들을 일컫는 자료형으로 작은 따옴표(`'`) 또는 큰 따옴표(`"`)를 사용한다. 

# In[11]:


'Hello, World'


# In[12]:


"Hello, World"


# ````{prf:example}
# :label: str-example
# 
# `Hello, "World"`를 보이는 그대로 출력하는 코드를 작성하여라. 
# ````

# 문자열 내부에서 큰 따옴표를 사용하고 싶을 때는 작은 따옴표로 문자열을 감싸면 된다. 

# In[13]:


print('Hello, "World"')


# 반대로 문자열 내부에서 작은 따옴표를 사용하고 싶을 때는 큰 따옴표로 문자열을 감싸면 된다.

# In[14]:


print("I'm a student")


# 백슬래시(`\`, 한글 키보드에서는 원화기호￦를 사용)를 사용하여 문자열 내부에서 사용되는 따옴표의 특수 역할을 해제<font size = "2">escape</font>할 수 있다. 

# In[15]:


print("Hello, \"World\"")


# 여러 줄로 이루어진 문자열은 삼중 따옴표(`''' '''` 또는 `""" """`)를 사용할 수 있다. 

# In[16]:


print('''
Hello,
 World
''')


# In[17]:


print("""
Hello,
 World
""")


# #### 문자열에 특수 문자 활용하기

# 백슬래시(￦), 줄바꾸기(￦n), 탭(￦t) 등은 문자열에 사용될 경우 특수한 기능을 갖는다.

# In[18]:


print("Hello\n World")


# In[19]:


print("Hello\t World")


# 백슬래시(`\`)기호를 붙여서 특수 기능을 해제<font size= "2">escape</font>할 수 있다.

# In[20]:


print("Hello\\n World")


# In[21]:


print("Hello\\t World")


# In[22]:


print("Good\\night")


# 연속된 백슬래시 두 개를 출력하려면 아래와 같이 해야 한다.

# In[23]:


print("\\\\")


# :::{admonition} 주의  
# :class: caution  
# 
# 아래와 같이 코드를 작성하면 오류가 발생하므로 주의해야 한다.
# 
# ```python
# >>> print("\\\")
#   File "/tmp/ipykernel_76/2337434698.py", line 1
#     print("\\\")
#                 ^
# SyntaxError: EOL while scanning string literal
# ```
# :::

# :::{admonition} 순수 문자열  
# :class: info  
# '가공되지 않은'의 의미를 갖는 'raw' 단어의 첫 글자인 'r'을 문자열 앞에 두면 특수 기능이 사라진다.
# :::

# In[24]:


print(r"Hello\n World")


# In[25]:


print(r"Hello\t World")


# In[26]:


print(r"Hello\ World")


# #### 기본 연산

# |연산 기호|의미|예시|실행 결과|
# |:----------:|:----------:|:----------:|:--------:|
# |`+`|덧셈| `'Hello ' + 'python'` |`'Hello python'`|
# |`*`|곱셈| `3*'Hello '` | `Hello Hello Hello `|

# #### f-string

# 문자열 앞에 `f`를 붙이면, 문자열 포매팅 <font size = "2" >string formatting</font>을 사용할 수 있다. 

# :::{admonition} 문자열 포매팅 <font size = "2" >string formatting</font>  
# :class: info  
# 문자열 포매팅이란 문자열 안에 값을 삽입하는 방법이다. 
# :::
# 

# 예제와 함께 살펴보자. 

# In[27]:


name = '강현'
f'{name}님, 안녕하세요.'


# In[28]:


age = 3
f'강현이는 {age}살이다.'


# In[29]:


name = '강현'
age = 3
f'{name}이는 {age}살이다.'


# `{}`안에 변수와 수식(`+`, `-`, `*`, `/` 등)을 함께 사용하는 것도 가능하다. 

# In[30]:


name = '강현'
age = 3
f'{name}이의 동생은 {age - 2}살이다'


# **소수점 표현**  
# 
# 콜론(`:`) 뒤에 소수점아래 몇 번째 자리까지 출력할지를 적어주면, 그 만큼을 보여준다.  
# 예제와 함께 살펴보자. 
# * `.`은 소수점을 의미하고, 소수점 뒤의 숫자는 소수점 뒤에 나올 숫자의 개수다.  

# In[31]:


num = 0.123456789
print(f'{num:.1f}')
print(f'{num:.2f}')
print(f'{num:.3f}')
print(f'{num:.5f}')  # 소수점 아래 여섯 번째 자리에서 반올림


# **문자열 정렬**

# In[32]:


num1 = 0.12
num2 = 0.12345
num3 = 0.12345678


# In[33]:


print(f"He paid {num1} dollars.")
print(f"He paid {num2} dollars.")
print(f"He paid {num3} dollars.")


# * 콜론`:` 뒤에 `<`은 왼쪽 정렬, `>`은 오른쪽 정렬, `^`은 가운데 정렬을 의미한다. 
# * 정렬 문자(`<`, `>`, `^`) 뒤에 숫자만큼의 공간을 사용한다.
# * 정렬 문자(`<`, `>`, `^`) 앞에 문자를 적으면 그 문자로 공백을 채운다. 

# In[34]:


print(f"He paid {num1:>10} dollars.")
print(f"He paid {num2:>10} dollars.")
print(f"He paid {num3:>10} dollars.")


# In[35]:


print(f"He paid {num1:<10} dollars.")
print(f"He paid {num2:<10} dollars.")
print(f"He paid {num3:<10} dollars.")


# In[36]:


print(f"He paid {num1:^10} dollars.")
print(f"He paid {num2:^10} dollars.")
print(f"He paid {num3:^10} dollars.")


# In[37]:


print(f"He paid {num1:.^20} dollars.")
print(f"He paid {num2:.^20} dollars.")
print(f"He paid {num3:.^20} dollars.")


# 소수점 표현과 정렬을 동시에 사용할 수도 있다.

# In[38]:


print(f"He paid {num:*>10.2f} dollars.")
print(f"He paid {num:*>10.3f} dollars.")
print(f"He paid {num:*>10.4f} dollars.")


# ### 불리언 

# 불리언<font size = "2">bool</font>자료형은 참(`True`)과 거짓(`False`)를 나타내는 자료형이다. 파이썬에서 불리언 자료형은 `int` 형의 자식형<font size = "2"> subtype</font>이고, 대부분의 상황에서 `True`와 `False`는 각각 `1`과 `0`처럼 동작한다. 

# #### 논리 연산자

# |연산 기호|의미|예시|실행 결과|
# |:----------:|:----------:|:----------:|:--------:|
# |`and`|그리고|`True and False`|`False`|
# |`or`|또는|`True or False`|`True`|
# |`not`|부정|`not False`|`True`|

# :::{admonition} 참고  
# :class: info
# 
# `x and y`는 `x`가 참일 때만 `y`를 확인한다.  
# `x or y`는 `x`가 거짓일 때만 `y`를 확인한다.
# 
# 예를 들어, 아래와 같이  `False and 3/0`를 실행하면 `False`가 나온다. 
# ```python
# >>> False and 3/0
# ```
# 
# 하지만 반대로 `3/0 and False`를 실행하면 오류가 발생한다. 
# ```python
# >>> False and 3/0
# ZeroDivisionError                         Traceback (most recent call last)
# /tmp/ipykernel_422/2156724109.py in <module>
# ----> 1 True and 3/0
# 
# ZeroDivisionError: division by zero
# ```
# :::

# #### 비교 연산자

# |연산 기호|의미|예시|실행 결과|
# |:----------:|:----------:|:----------:|:--------:|
# |`<`|작다|`2 < 1`|`False`|
# |`<=`|작거나 같다|`1 <= 2`|`True`|
# |`>`|크다|`2 > 1`|`True`|
# |`>=`|크거나 같다|`1 >= 2`|`False`|
# |`==`|같다|`1 == '1'`|`False`|
# |`!=`|같지 않다|`1 != '1'`|`True`|
# |`is`|객체 아이덴티티|`1 is 1.0`|`False`|
# |`is not`|부정된 객체 아이덴티티|`3 is not 3`|`False`|

# 서로 다른 숫자형을 제외하고는 서로 다른 형은 같다고 비교되지 않는다. 

# 예를 들어, 정수 `1`와 부동소수점 `1.0`이 같은지 여부를 확인해보자.

# In[39]:


1 == 1.0


# 반면, 정수 `1`과 문자열 `'1'`은 형<font size = "2">type</font>이 달라서 같은지 여부를 확인해보면, `False`가 나온다.

# In[40]:


1 == '1'


# :::{admonition} 참고   
# :class: info
# 
# 객체의 아이덴티티<font size="2">identity</font>는 메모리상에서의 객체의 주소라 생각해도 된다.   
# `id()` 함수는 아이덴티티를 정수로 표현한 값을 돌려준다.
# :::

# In[41]:


print(id(1))
print(id(2))


# In[42]:


1 is 2


# In[43]:


id(1) == id(2)


# :::{admonition} 참고   
# :class: info
# 
# `x is y`가 `True`면 `x == y`도 `True`다.  
# 반면, `x == y`는 `True`이지만 `x is y`는 `False`일 수 있다.
# :::

# In[44]:


1 == 1.0


# In[45]:


1 is 1.0


# 문자열도 비교연산자를 사용할 수 있다.   
# 크기 비교 연산자들은 영어 사전식의 알파벳 순서를 사용한다. 

# In[46]:


'apple' == 'pineapple'


# In[47]:


'apple' < 'banana'


# :::{admonition} 참고   
# :class: info
# 영어 알파벳의 경우 대문자가 소문자보다 작다고 판단한다.
# :::

# ### `None`

# `None`은 `NoneType` 자료형에 속하는 하나의 값으로 어떤 의미도 없는 값을 말한다.

# :::{admonition} 주의   
# :class: caution
# 변수 할당에 사용되어 저장될 수 있지만 연산 등에 사용하면 오류가 발생한다.  
# :::

# ## 변수

# ### 변수와 변수할당

# **변수**<font size = "2">variable</font>는 (컴퓨터 메모리에) 저장된 하나의 값을 가리키는 이름을 말한다. 

# #### 변수명

# 변수명은 임의로 정할 수 있지만 할당되는 값과 연관된 이름을 사용할 것을 권장한다.  
# 또한 아래 제한 사항을 지켜야 한다.   
# 
# * 반드시 영어 알파벳 문자(a-z, A-Z) 또는 밑줄기호(`_`)로 시작해야 하며, 이후에는 알파벳, 숫자(0-9), 밑줄기호가 임의로 사용될 수 있다.
# * 파이썬 키워드<font size = "2">keyword</font>를 변수 이름으로 사용하면 안된다.
# * 대소문자를 구분해야 한다: `YOU`, `you`, `You`, `yOu`는 모두 다른 이름으로 처리된다.
# * `-`, `+`, `*`, `/` 등의 연산자 기호는 이름에 사용할 수 없다.
# * `@`, `$`, `?` 등의 기호도 사용되지 않는다.
# * 변수명에 공백을 사용할 수 없다.

# **파이썬 키워드**  
# 파이썬 프로그래밍 언어의 키워드는 3.10버전 기준으로 총 35개이다. 

# ```
# False      await      else       import     pass
# None       break      except     in         raise
# True       class      finally    is         return
# and        continue   for        lambda     try
# as         def        from       nonlocal   while
# assert     del        global     not        with
# async      elif       if         or         yield
# ```

# ````{prf:example}
# :label: var_name-example
# 다음 중 변수명으로 사용 가능한 것은?
# 
# * `123k`    
# * `a123!`   
# * `_K1212`  
# * `name`  
#   
# 변수명은 알파벳 문자나 밑줄기호로 시작해야 하므로 `123k`는 변수명으로 사용할 수 없고, `!` 기호도 변수명에 사용될 수 없다. 위에서 가능한 변수명은 `_K1212`와 `name`이다.  
# 
# ````

# #### 변수 할당 <font size = "2">variable assignment </font>

# 변수를 선언하려면 해당 변수가 하나의 값을 가리키도록 하는 **변수 할당**을 명령해야 한다.  

# :::{admonition} 주의   
# :class: caution
# 변수가 정의되지 않고(값을 할당하지 않고) 사용하려고 하면 오류가 발생한다.   
# :::

# 변수 선언과 할당은 동시에 이루어지며, 변수명이 등호기호(`=`) 왼편에, 변수와 연관된 값<font size = "2">value</font>을 표현하는 **표현식**<font size = "2">expression</font>은 등호 기호 오른편에 위치한다.

# `변수 = 값`

# In[48]:


num = 5
pi = 3.1415926535897932
name = '강현'


# * `num` 변수가 가리키는 값은 정수 `5`이다. 
# * `pi` 변수가 가리키는 값은 부동소수점 `3.1415926535897932`이다.
# * `name` 변수가 가리키는 값은 문자열 `'강현'`이다.

# 선언된 변수는 할당된 값과 동일하게 취급된다. 

# In[49]:


'안녕, ' + name


# In[50]:


2 * num


# 변수가 가리키는 값은 변경될 수 있다. 예를 들어, 변수 `num`에 `17`을 새롭게 할당하면, `num` 변수가 가리키는 값은 정수 `5`가 아니라 정수 `17`이다. 

# In[51]:


print(num)
num = 17
print(num)


# **세미콜론**

# 모든 명령문은 한 줄에 완성하는 것이 기본이며, 연속된 명령문은 줄바꿈을 해서 작성한다. 하지만 매우 간단한 명령문은 한 줄에 연속으로 작성할 수 있는데, 이때 세미콜론(`;`)을 사용한다. 

# In[52]:


a = 1; b = 2; c = 3


# In[53]:


print(a)
print(b)
print(c)


# 세미콜론을 사용하기보다는 각각의 명령문을 줄바꿈하여 명확하게 작성하는 것을 추천한다. 

# **다중 할당** <font size = "2">multiple assignment</font>

# **다중할당**은 동시에 2개 이상의 값을 2개 이상의 변수에 할당하는 것을 말한다. 

# In[54]:


a, b, c = 2, 4, 6


# In[55]:


print(a)
print(b)
print(c)


# **변수 스왑** <font size= "2">variable swap</font>

# 일반적으로 두 변수를 스왑할 때 임시변수 <font size = "2">temporarily variable</font>를 사용한다.  

# In[56]:


a = 1
b = 2
print('a :', a, ', b :', b)

temp = a
a = b
b = temp

print('a :', a, ', b :', b)


# 하지만 파이썬은 임시변수를 사용하지 않고 아래와 같이 스왑할 수 있다. 

# In[57]:


a = 1
b = 2
print('a :', a, ', b :', b)

a, b = b, a
print('a :', a, ', b :', b)


# #### Augmented assignment statements

# Augmented assignment statements은 이항 연산과 할당을 합한 것이다. 

# |연산 기호|예시|의미|
# |:----------:|:----------:|:----------:|
# |`+=`|`x += 1` |`x = x + 1`|
# |`-=`| `x -= 1` | `x = x - 1`|
# |`*=`| `x *= 2` | `x = 2*x`|
# |`/=`|`x /= 2`|`x = x / 2`|
# |`**=`|`x **= 2`|`x = x**2`|
# |`//=`|`x //= 2`|`x = x //2`|
# |`%=`|`x %= 2`|`x = x % 2`|

# In[58]:


x = 5
print(x)
x /= 2
print(x)


# ### 동적 타이핑과 정적 타이핑

# #### 동적 타이핑과 정적 타이핑

# 파이썬은 **동적 타이핑** <font size = "2">Dynamic typing</font>을 지원한다. 동적 타이핑은 변수를 미리 선언하지 않고, 변수를 생성하고자 할 때 값을 초기화하여 사용하는 것을 말한다. 변수의 자료형은 파이썬이 알아서 판단하기 때문에 동적 타이핑은 프로그래밍을 처음 접하는 사람들에게 편리하다.   
# 
# 동적 타이핑과는 달리 변수를 사용하기 전 미리 선언해야 하는 **정적 타이핑** <font size = "2">Static Typing</font>도 있다. C나 자바처럼 주로 컴파일 방식의 언어가 정적 타이핑을 지원한다. 이처럼 사용할 변수와 변수에 할당될 값의 자료형을 미리 선언하는 것은 불편해 보일 수도 있다. 하지만 정적 타이핑은 컴파일하는 과정에서 선언한 자료형에 맞는 값을 할당하였는지, 선언 후 사용하지 않는 변수가 있는지를 확인하여 버그 발생 확률을 낮출 수 있다는 장점이 있다. 이에 동적 타이핑을 지원하는 파이썬에서도 타입 힌트 <font size = "2">Type Hints</font>를 명시하기도 한다.

# #### 타입 힌트

# 파이썬 3.5이후 버전에서는 타입 힌트 또는 타입 어노테이션 <font size = "2">Type Annotation</font>을 사용할 수 있다. 

# 다음과 같이 변수명 뒤에 콜론(`:`)을 붙이고 타입을 적어주는 방식으로 타입 힌트를 추가한다.  
# 예를 들어, `a : int`, `b : float`, `c : bool`, `s : str`등과 같이 사용한다.

# In[59]:


num : int = 5
pi : float = 3.1415926535897932
name : str = '강현'


# In[60]:


print(num)
print(pi)
print(name)


# :::{admonition} 주의   
# :class: caution   
# 타입 힌트의 사용은 실제 코드 실행에 아무런 영향을 미치지 않는다.  
# :::
# 
# 
# 예를 들어, 변수 `a`에 타입 힌트와는 다른 형<font size= "2">type</font>의 값을 할당하여도 오류가 발생하지 않는다. 

# In[61]:


a : int = 3.4
print(a)
print(type(a))


# :::{admonition} mypy  
# :class: info   
# 타입 검사기를 사용하면 코드가 실행될 때 타입 힌트에 오류가 있는지를 확인할 수 있다. 현재 많이 사용되고 있는 파이썬 타입 검사기 중 하나는 mypy<font size= "2">마이파이</font>이다.   
# 
# 주피터 노트북 <font size = "2">jupyter notebook </font>에서는 아래의 코드를 사용하여 mypy를 설치하여 사용할 수 있다. 
# ```python
# >>> pip install mypy-ipython  
# >>> %load_ext mypy_ipython
# ```
# 
# 그런 다음 아래와 코드를 작성하고 타입 검사기를 사용해보자. 
# ```python
# >>> a : int = 3.4
# >>> print(a)
# 3.4
# >>> print(type(a))
# <class 'float'>
# ```
# mypy를 사용하면 타입 힌트가 작성된 파이썬 파일의 코드 전체에 타입 힌트 오류가 있는지를 확인할 수 있다.  
# ```python
# >>> %mypy
#     a : int = 3.4
# error: Incompatible types in assignment (expression has type "float", variable has type "int")
# Found 1 error in 1 file (checked 1 source file)
# Type checking failed
# ```
# 여기서는 타입 힌트와 일치하지 않는 값이 할당되었다는 메시지와 함께 오류가 발생하였다.
# 
# :::

# ## 함수

# 프로그램은 명령문의 합성으로 구현된다. 그런데 특정 기능을 수행하는 명령문의 일부가 너무 길거나, 반복적으로 사용되어 보다 편하게 사용하고 싶거나 프로그램을 보다 체계적으로 구현하도록 하고 싶을 때가 있다. 그럴 때는 특정 기능을 수행하는 명령문에 이름을 주고 필요에 따라 해당 이름을 대신 활용할 수 있다. 
# 
# 함수는 함수의 이름에 가려진 명령문을 대행하며 해당 명령문을 실행하려면 지정된 함수를 **호출** <font size = "2">call </font> 하면 된다.
# **함수 호출** <font size = "2"> function call </font>은 함수 이름과 연관된 명령문을 실행하도록 하는 일종의 명령문이다. 함수 호출의 일반적인 형식은 다음과 같다. 

# `함수이름(인자1, 인자2, ..., 인자n)`

# ### `type()` 함수

# `type()` 함수는 인자의 자료형을 확인해준다.

# In[62]:


type(-3)


# In[63]:


type(3.141592)


# In[64]:


type(True)


# In[65]:


type('Hello, World!')


# In[66]:


type(None)


# 변수의 자료형은 변수가 현재 가리키는 값의 자료형으로 지정된다. 따라서 변수에 할당된 값의 자료형이 달라지면 변수의 자료형도 함께 달라진다. 

# In[67]:


num = 3
type(num)


# In[68]:


num = 3.14
type(num)


# In[69]:


num = '3.14'
type(num)


# ### 형변환 함수

# 형변환<font size = "2">type casting</font>은 자료형을 변환하는 것으로, 파이썬은 다양한 형변환 함수를 제공한다. 

# #### `int()` 함수

# `int()` : 정수형으로 변환. 부동소수점을 정수로 변환할 때, 소수점 이하는 버려진다.

# In[70]:


int(3.2)


# In[71]:


int(2.9)


# In[72]:


int('6')


# In[73]:


int(True)


# In[74]:


int(False)


# :::{admonition} 주의   
# :class: caution  
# `int()` 함수의 인자로 문자열을 사용할 때는 그 모양이 정수모양이어야 한다. 
# 
# ```python 
# >>> int('9.2')
# ValueError                                Traceback (most recent call last)
# /tmp/ipykernel_422/3306962362.py in <module>
# ----> 1 int('9.2')
# 
# ValueError: invalid literal for int() with base 10: '9.2'
# ```
# :::

# :::{admonition} 주의  
# :class: caution
# 변수를 형변환한다고 해서 변수에 할당된 값이 변하는 것은 아니다. 다만, 형변환한 값을 다른 변수에 저장해서 활용할 수는 있다. 
# :::

# In[75]:


float_num = 2.3
print(int(float_num))
print(type(float_num))


# In[76]:


int_num = int(float_num)
print(type(int_num))


# #### `float()` 함수

# `float()` 부동소수점형으로 변환

# In[77]:


float(2)


# In[78]:


float(True)


# In[79]:


float(False)


# In[80]:


float('7')


# :::{admonition} 주의  
# :class: caution
# `float()` 함수의 인자로 문자열을 사용할 때는 그 모양이 정수 또는 부동소수점 모양이어야 한다.  
# 
# ```python
# >>> float('3GB')
# ValueError                                Traceback (most recent call last)
# /tmp/ipykernel_422/1346430820.py in <module>
# ----> 1 float('3GB')
# 
# ValueError: could not convert string to float: '3GB'
# ```
# :::

# #### `str()` 함수

# `str()` : 문자열형으로 변환

# In[81]:


str(1)


# In[82]:


str(3.4)


# In[83]:


str(True)


# In[84]:


str(None)


# #### `bool()` 함수

# `bool()` : 불리언형으로 변환  

# :::{admonition} 참고   
# :class: info
# `bool()` 함수는 `0`, `0.0`, `''`(빈 문자열)처럼 0이거나 비어 있는 값을 인자로 사용하면 `False`를 반환한다.  
# :::

# In[85]:


bool(None)


# In[86]:


bool(0)


# In[87]:


bool(1)


# In[88]:


bool(3)


# In[89]:


bool(0.0)


# In[90]:


bool(2.3)


# In[91]:


bool('')


# In[92]:


bool('abc')


# ### `input()` 함수

# 사용자의 입력은 `input()` 함수를 사용하여 받을 수 있다. 아래와 같이 `input()`을 입력하고 코드를 실행하면, 그 아래에 값을 입력하라는 창이 나온다. 그곳에 `Hello, python!`을 입력하고 엔터<font size ="2">enter</font>를 누르면 입력한 문자열이 그대로 출력된다.  
# ```python
# >>> input()
# Hello, python!
# 'Hello, python!'
# ```

# `input()` 함수로 입력받은 값은 변수에 할당하여 사용할 수도 있다.  
# 
# ```python
# >>> name = input()
#  python!
# >>> print("Hello, " + name)
# Hello, python!
# ```

# 이때 `input()` 함수로 입력받은 값은 문자열`str`이다.  
# 
# ```python
# >>> type(name)
# str
# ```

# 사용자가 숫자를 입력하더라도 입력받은 값은 문자열`str`이다.  
# 
# ```python
# >>> num = input()
#  123
# >>> type(num)
# str
# ```

# 사용자에게 무엇을 입력할지 알려주고 싶다면, 그 내용의 문자열을 `input()`의 인자로 사용하면 된다.  
# 
# ```python
# >>> input_num = input("정수를 입력하세요 : ")
# 정수를 입력하세요 :  135
# >>> print("입력하신 정수는 " + input_num + "입니다.")
# 입력하신 정수는 135입니다.
# ```

# ### `print()` 함수

# 그 동안 출력을 위해 `print()` 함수를 사용하였다. 예를 들어, `Hello, python`을 출력하고 싶다면, 아래와 같이 코드를 작성하면 된다. 

# In[93]:


print('Hello, python')


# 이제 `print()` 함수에 대해서 조금 더 살펴보자. 

# * 큰 따옴표(또는 작은 따옴표)로 둘러싸인 문자열을 연속해서 사용하면 문자열에서 +연산을 한 것과 동일한 결과를 출력해준다.

# In[94]:


print("Hello ""World")
print('Hello ''World')
print('Hello '"World")
print("Hello " + "World")


# * 콤마(`,`)로 구분하여 여러 개의 인자를 사용할 수 있다.

# In[95]:


print("Hello", "World")


# In[96]:


print("강아지", 3, "마리")


# * 인자들 사이에 구분자를 넣고 싶다면, `sep`을 변경하면 된다. `sep`의 기본값은 공백이다.

# In[97]:


print("010", "1234", "5678", sep = "-")
print("Hello", "World", sep = ", ")


# * 마지막에 출력할 문자를 변경하고 싶다면, `end`를 변경하면 된다. `end`의 기본값은 줄변경(`\n`)이다.

# In[98]:


print("a")
print("b", end = "")
print("c", end = "\t")
print("d")


# :::{admonition} 참고  
# :class: info  
# `print()` 함수에 의해 화면에 출력되는 문자열은 반환값이 아니고 화면에 지정된 값을 출력하는 명령문의 실행 결과에 불과하다. 함수의 반환값은 변수에 할당해서 사용할 수 있지만 화면에 출력된 문자열은 그럴 수 없다는 데서 `print()` 함수는 특정한 반환값을 생성하지 않고, 대신에 `None`이 반환값으로 사용된다는 것을 확인할 수 있다. 
# :::

# In[99]:


x = print(123) # 아래 123은 변수 x가 가리키는 값이 아니다. 


# In[100]:


print(x) #변수 x는 None을 가리킨다.


# ## 연습문제

# ### 문제
# 다음을 연산기호를 이용하여 수식으로 표현하고, 그 결과를 확인하여라.    
# 
# * 3 + 9 - 8  
# * (27 + 3) × 2 - 42 ÷ 3  
# * [{(9 ÷ 2) × 12} - 7] × 3 - 1

# ### 문제  
# 문자열 `Good morning!` 을 출력하는 코드를 작성하여라.  
# 

# ### 문제  
# `Hello!`를 3번 연속(`Hello!Hello!Hello!`)으로 출력하는 코드를 작성하여라. 

# ### 문제  
# 사용자에게 문자열을 입력받고, 그 문자열을 5번 연속으로 출력하는 코드를 작성하여라.   
# 예를 들어, 사용자가 `Hello!`를 입력했다면, `Hello!Hello!Hello!Hello!Hello!`를 출력한다. 

# ### 문제  
# 두 정수 a와 b를 입력받아 `a + b`, `a - b`, `a * b`, `a / b`, `a // b`, `a % b`를 출력하는 코드를 작성하여라.   
# 
# 
# Input : a = 3, b = 2  
# Output : 
# ```
# 3 + 2 = 5  
# 3 - 2 = 1
# 3 * 2 = 6 
# 3 / 2 = 1.5
# 3 // 2 = 1
# 3 % 2 = 1
# ```

# ### 문제
# 
# 두 자연수 x와 y를 입력받아 두 수의 산술평균<font size = "2">arithmetic mean</font>, 기하평균<font size = "2">geometric mean</font>, 조화평균<font size = "2">harmonic mean</font>을 출력하는 코드를 작성하여라.   
# 두 자연수 x와 y의 산술평균($M_a$), 기하평균($M_g$), 조화평균($M_h$)을 구하는 식은 아래와 같다.  
# * $M_a =$ <font size = "4">$\frac{x + y}{2}$ </font>  
# 
# * $M_g =\sqrt{xy}$ 
# 
# * $M_h =$ <font size = "4">$\frac{2}{\frac{1}{x} + \frac{1}{y}}$</font>  

# ### 문제   
# 오늘이 무슨 요일인지 주어질 때, 100일 후는 무슨 요일인지를 출력하는 코드를 작성하여라.  
# 단, 1234560은 각각 월화수목금토일을 의미한다. 즉, 2는 화요일이다.   
# Input : 2   
# Output : 4   

# ### 문제  
# 다음은 BTS의 butter 가사 일부분이다. 아래와 같이 문자열을 출력하는 코드를 작성하여라(따옴표 포함).  
# ```
# Smooth like "butter"
# Like a criminal undercover
# Gon' pop like trouble
# Breakin' into your heart like that
# ```

# ### 문제  
# `input()`로 정수를 입력받아, 아래의 형식으로 그 값을 출력하는 코드를 작성하여라.  
# 단, 정수는 10000이하의 수를 입력한다고 가정한다. 
# 
# Input : 3  
# Output : `입력하신 숫자는 000003입니다.`  
# 
# Input : 123  
# Output : `입력하신 숫자는 000123입니다.`

# ### 문제  
# 30cm × 30cm 크기의 타일이 있다. 타일은 온장을 그대로 사용할 수도 있고, 잘라서 일부분만 사용할 수도 있다. **단, 잘라서 사용한 타일의 나머지는 사용하지 않는다.** 주어진 크기의 바닥에 타일을 깔기 위해 사용되는 온장 타일과 잘라서 사용한 타일의 개수를 공백으로 구분하여 출력하는 코드를 작성하여라.  
# 
# Input : width = 400, height = 300  (width와 height는 모두 정수)  
# Output : 130 10

# ### 문제  
# 
# 어느 대기실에는 N개의 의자가 일렬로 놓여 있다. 어느 두 사람도 이웃하여 앉지 않을 때, 앉을 수 있는 최대 인원수와 최소 인원수를 출력하는 코드를 작성하여라. 단, 대기실에는 충분히 많은 사람이 있고, 띄어 앉기가 가능하다면 모두 앉고 싶어한다. 
# 예를 들어, 5개의 의자가 일렬로 놓여 있을 때, 한 칸씩 띄어 앉으면(ex, ■□■□■) 3명이 앉을 수 있다. 반면, 누군가 두 번째(ex, □■□□□ )나 네 번째(ex, □□□■□) 의자에 앉으면, 띄어 앉기하여 5개의 의자에 2명이 앉을 수 있다(ex, □■□■□, □■□□■, ■□□■□, □■□■□). 따라서 5개의 의자가 일렬로 놓여 있을 때, 띄어 앉기를 하여 최대 3명, 최소 2명 앉을 수 있다.
# 
# Input : N = 5  
# Output : 3 2

# ### 문제   
# d m 길이의 철로 양끝에 서로 마주보고 있는 두 대의 기차 A, B가 있고, 기차 A위에는 파리 한 마리가 있다. 두 기차 A와 B가 서로를 향해 달릴 때, 파리는 기차 A에서 기차 B까지 날아가다가 기차 B와 부딪히기 직전 방향을 바꿔 기차 A에게 날아가고 다시 기차 A와 부딪히기 직전 기차 B를 향해 날아가기를 반복한다. 그러다가 기차 A, B는 부딪힌다. 이때, 기차 A의 속력은 a m/s, 기차 B의 속력은 b m/s, 파리의 속력은 c m/s 이다. d, a, b, c가 주어졌을 때, 파리가 부딪히기 직전까지 날아다닌 거리(m)를 구하는 코드를 작성하여라. 단, d, a, b, c는 모두 10000이하의 자연수이고, a, b < c < d를 만족하도록 임의로 입력한다.  
# 
# Input : d = 16, a = 3, b = 5, c = 8   
# Output : 16

# ### 문제  
# 
# 다음과 같은 방법으로 (세 자리 수) × (세 자리 수) 를 계산할 수 있다.   
# 
# <div align="left">
#     <img src="https://raw.githubusercontent.com/hj617kim/core_pybook/master/images/ch04/pro01.png" style="width:250px;">
# </div>  
# 
# 두 세 자리 수가 주어질 때, ①, ②, ③, ④에 들어갈 값을 각각 줄변경하여 출력하는 구하는 코드를 작성하여라.  
# 
# Input : a = 265, b = 112  
# Output :  
# ```
# 530   
# 265  
# 265 
# 29680
# ```

# ### 문제  
# A편의점은 500원, 100원, 50원, 10원을 보유하고 있고, 동전의 개수를 최소화하여 거스름 돈을 주려고 한다.  
# 거슬러 줘야 하는 금액이 n원일 때, 최소 동전의 개수를 출력하는 코드를 작성하여라.     
# 단, n은 10의 배수이며 5000보다 작은 정수고, 모든 화폐는 무한하게 있다고 가정한다. 
# 
# Input : n = 1730  
# Output : 8
