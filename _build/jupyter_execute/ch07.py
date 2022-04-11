#!/usr/bin/env python
# coding: utf-8

# # 파이썬 프로그래밍의 기초 V

# ## 클래스

# ### 클래스와 인스턴스

# **클래스**<font size = "2">class</font>는 서로 관련된 데이터와 해당 데이터를 다루는 함수들을 하나로 묶어 추상화하는 방법으로, 클래스를 이용하여 필요한 자료형<font size="2">data type</font>을 직접 정의할 수 있다. 예를 들어, 지금까지 사용했던 정수, 문자열, 리스트와 같은 자료형들도 모두 `int`, `str`, `list` 클래스로 정의되어 있다. 한편, 우리가 `2`, `'Hello'`, `[1, 2, 3]`을 각각 정수, 문자열, 리스트 자료형의 값이라고 부르듯이 특정 클래스의 값에 해당하는 대상을 정의할 수 있는데, 이를 해당 클래스의 **인스턴스**<font size="2">instance</font>라고 부른다. 그리고 특정 클래스의 인스턴스를 일반적으로 **객체**<font size="2">object</font>라고 부른다. 예를 들어, `2`, `'Hello'`, `[1, 2, 3]`은 객체이며, 각각 `int`, `str`, `list` 클래스의 인스턴스이다.  

# :::{admonition} 객체와 인스턴스    
# :class: info    
# 보통 대상에 집중할 때는 객체라는 표현을 사용하며, 특정 클래스와의 관계에 집중할 때는 인스턴스라는 표현을 주로 사용한다. 예를 들어, '`2`는 객체'이고, '`2`는 `int` 클래스의 인스턴스'라고 표현한다.   
# :::

# :::{admonition} 참고    
# :class: info    
# 파이썬에서 사용되는 모든 대상은 특정 클래스의 인스턴스, 즉 객체이다. 파이썬의 자료형들은 모두 클래스로 정의되어 있으며, 심지어 이러한 클래스도 `type`이라는 클래스의 인스턴스이다. 특정 객체의 클래스, 즉 자료형을 확인하려면 `type()` 함수를 사용한다.   
# 
# ```python
# >>> print(type(int))
# <class 'type'>
# ```
# 
# ```python
# >>> print(type(str))
# <class 'type'>
# ```
# 
# ```python
# >>> print(type(list))
# <class 'type'>
# ```
# :::
# 

# :::{admonition} 객체지향프로그래밍<font size = "2">Object-Oriented Programming, OOP</font>  
# :class: info    
# OOP는 프로그래밍 기법 중 하나로, 프로그램을 구성하는 객체<font size="2">object</font>들을 중심으로 구현해야 할 프로그램을 완성시키는 방식을 말한다.    
# :::
# 

# ### 속성과 메서드   
# 클래스에는 변수와 함수들이 선언되어 있는데, 여기에 특별한 성질의 객체를 묘사하고 다루기 위해 필요한 속성과 도구를 저장한다. 보통 클래스에서 선언된 변수를 **속성 변수** 또는 **속성**<font size="2">attribute</font>, 함수를 **메서드**<font size="2">method</font>라고 부르고, 이는 해당 클래스를 통하여 또는 해당 클래스의 인스턴스를 통하여 호출될 수 있다.  
# 
# * **속성**<font size="2">attribute</font>
#     * 클래스에서 선언된 변수
#     * 생성되는 객체들이 사용하는 값 또는 특성값 저장
# * **메서드**<font size="2">attribute</font>
#     * 클래스에서 선언된 함수
#     * 속성 정보를 이용하고 다룰 수 있는 도구
# 
# 예를 들어, 문자열 `'Hello'`은 어떤 형식으로든 Hello라는 단어를 속성으로 가지고 있어야 하며, `split`, `strip`, `find` 등의 문자열 메서드로 속성 정보를 이용할 수 있다. 또한, 리스트 `[1, 2, 3]`도 어떤 형식으로든 1, 2, 3을 속성으로 갖고 있어야 하며, `append`, `pop`, `sort` 등의 리스트 메서드로 속성 정보를 이용할 수 있다.   
# 
#     

# ## `Fraction` 클래스  
# 분수들의 클래스인 `Fraction` 클래스를 정의하면서 클래스에 대해서 살펴보자.  

# ### 클래스 정의하기 

# 파이썬에서는 클래스를 정의하기 위해 `class`라는 키워드를 사용하며, 아래의 형식을 따른다.  
# 
# ```
# class 클래스이름 :
#     # 속성 및 메서드 선언 
# ```

# 예를 들어, `Fraction` 클래스는 아래와 같이 정의할 수 있다.  

# In[1]:


class Fraction :
    pass


# **문서화 문자열**<font size="2">docstring</font>  
# 큰 따옴표 세 개(`"""..."""`) 또는 작은 따옴표 세 개(`'''...'''`)를 사용하여 클래스에 주석을 추가할 수 있다. 예를 들어, `Fraction` 클래스에 `Fraction 클래스`라는 문서화 문자열을 추가해보자.  

# In[2]:


class Fraction :
    """
      Fraction 클래스
    """
    pass


# 클래스에 문서화 문자열을 추가하면, `help()` 함수를 사용하여 해당 함수의 역할 및 사용법을 확인할 수 있다. 

# In[3]:


help(Fraction)


# ### 특수 메서드

# 생성된 객체와 관련된 속성과 메서드를 확인하려면 `dir()`함수를 사용한다. 예를 들어, `Fraction`의 속성과 메서드를 확인해보자. 

# In[4]:


print(dir(Fraction))


# 그러면 `Fraction`의 속성과 메서드를 확인할 수 있다. 여기에는 `Fraction` 클래스를 선언할 때 명시하지 않았던 여러 속성과 메서드가 보이는데, 그 이유는 다음과 같다.  
# 
# * 파이썬의 모든 클래스는 `object`라는 최상위 클래스를 상속한다.  
# * 하나의 클래스를 상속하면 해당 클래스의 속성과 메서드도 모두 함께 상속받는다.  
# * `object` 클래스에는 위에서 언급된, 이중 밑줄로 감싼 속성과 메서드가 선언되어 있다.   
# 
# `object` 클래스에 포함된 속성과 메서드는 모두 양끝이 이중 밑줄로 감싸여 있는데, 양끝이 이중 밑줄로 감싸인 메서드를 특별히 **특수 메서드**<font size="2">special method</font> 또는 **매직 메서드**<font size="2">magic method</font>라고 부른다. 임의의 클래스는 `object` 클래스에서 선언된 특수 메서드와 속성을 모두 상속 받는다. 상속받은 속성과 메서드는 상속한 클래스에서 선언한 그대로 사용할 수 있다. 예를 들어, `__class__` 속성은 객체의 자료형 정보를 저장하고 있다. `Fraction`의 `__class__` 속성을 확인해보자. 속성 확인은 메서드를 호출하는 방식과 비슷하다.  

# In[5]:


Fraction.__class__


# `type()` 함수는 해당 객체의 `__class__` 속성을 확인하여 전달하는 일을 한다. 

# In[6]:


type(Fraction)


# 한편, 상속받은 메서드는 재정의하여 사용할 수도 있는데, 이를 **메서드 재정의** 또는 **메서드 오버라이딩**<font size="2">method overriding</font>이라 부른다. 위의 매직 메서드는 고유의 역할을 수행하기 위해 준비되었지만, 대부분 제대로 정의되지 않은 채로 상속된다. 이제 메서드 재정의를 하면서 중요한 특수 메서드 몇 개를 살펴보자.    

# ### `__init__()` 메서드

# `__init__()` 메서드는 클래스의 인스턴스의 속성 정보에 필요한 값들을 인자로 받는 함수로 활용된다. 예를 들어, `Fraction` 클래스의 경우, 분자와 분모에 해당하는 값을 받아 지정된 값으로 분수를 하나의 객체로 생성하는 데에 사용할 수 있다. 다음과 같이 `Fraction` 클래스를 선언할 때, `__init__()` 메서드를 재정의해보자.  

# In[7]:


class Fraction :
    """
      Fraction 클래스
    """
    def __init__(self, num, den) :
        """
          num : 분자numerator
          den : 분모denominator 
        """
        self.num = num
        self.den = den


# `Fraction` 클래스의 `__init__()` 메서드에 사용된 매개변수와 인스턴스 변수는 다음과 같다.  
# 
# * `self` : 생성되는 인스턴스 자신을 가리킴. 파이썬에서 클래스의 모든 (인스턴스) 메서드의 첫째 인자로 사용됨. 메서드를 호출할 때 `self`에 대한 인자는 사용하지 않음. 
# * `num` : 생성되는 분수의 분자로 사용될 값을 받는 매개변수.  
# * `den` : 생성되는 분수의 분모로 사용될 값을 받는 매개변수. 
# * `self.num` : 생성되는 분수의 분자로 사용되는 값을 가리키는 인스턴스 변수(속성 변수)
# * `self.den` : 생성되는 분수의 분모로 사용되는 값을 가리키는 인스턴스 변수(속성 변수)   
# 
# 인스턴스 변수 `self.num`과 `self.den`은 생성되는 분수의 상태<font size="2">state</font>를 저장하는 역할을 수행한다.  

# :::{admonition} 참고    
# :class: info  
# 매개변수의 이름을 `self`가 아닌 다른 변수를 사용해도 되지만, 관례적으로 `self`를 사용한다. 
# :::
# 

# ### 인스턴스 생성

# `Fraction` 클래스의 인스턴스, 즉 하나의 분수에 해당하는 객체를 선언하려면 `__init__()`메서드를 분자, 분모에 해당하는 인자와 함께 호출해야 한다. `__init__()` 메서드의 호출은 다음과 같이 클래스 이름을 마치 함수처럼 활용하면 된다.  

# In[8]:


a_fraction = Fraction(2, 7)


# 그러면 `a_fraction` 변수는 $\frac{2}{7}$에 해당하는 객체를 가리킨다. 

# <div align="center"><img src="https://raw.githubusercontent.com/hj617kim/core_pybook/master/images/ch07/class01.png" style="width:700px;"></div>

# 이제 `print()`함수를 사용하여 `a_fraction`을 확인해보자. 

# In[9]:


print(a_fraction)


# 그러면 `a_function`이 가리키는 값이 아닌 자신이 어떤 클래스의 인스턴스인지와 자신이 저장된 메모리 주소를 알려준다. 이는 `Fraction` 클래스가 자신의 인스턴스를 소개하는 기능을 제공하지 않았기 때문이다.  

# ### `__str__()` 메서드

# `__str__()` 메서드는 해당 클래스의 인스턴스를 `print()`함수를 통해 어떻게 보여줄 것인가를 문자열로 지정하는 함수로 활용된다. `Fraction` 클래스의 `__str__()` 메서드를 재정의해보자. 

# In[10]:


class Fraction :
    """
      Fraction 클래스
    """
    def __init__(self, num, den) :
        """
          num : 분자numerator
          den : 분모denominator 
        """
        self.num = num
        self.den = den
        
    def __str__(self) :
        return f"{self.num}/{self.den}"


# 그러면 이제 `print()`함수를 사용하면 원하는 대로 작동한다. 

# In[11]:


a_fraction = Fraction(2, 7)
print(a_fraction)


# `__str__()` 메서드를 직접 호출해도 동일한 결과를 얻는다. 

# In[12]:


a_fraction.__str__()


# `str()` 함수는 인자로 사용된 객체가 제공하는 `__str__()` 메서드를 내부에서 호출한다. 

# In[13]:


str(a_fraction)


# ### `__add__()` 메서드

# 이제 분수의 기본 연산이 가능하도록 코드를 작성해보자. 지금은 분수의 덧셈을 시도하면 오류가 발생한다.  
# 
# ```python 
# >>> f1 = Fraction(1, 4)
# >>> f2 = Fraction(1, 2)
# >>> f1 + f2 
# TypeError                                 Traceback (most recent call last)
# /tmp/ipykernel_82/2739786759.py in <module>
# ----> 1 f1 + f2
# 
# TypeError: unsupported operand type(s) for +: 'Fraction' and 'Fraction'
# ```
# 
# 이는 덧셈 연산자 `+`가 `Fraction` 클래스의 인스턴스에 대해 지원되지 않기 때문이다. 분수의 덧셈을 위해 `+` 연산자를 사용하려면 `Fraction` 클래스에 `__add__()` 메서드가 적절하게 정의되어 있어야 한다. 아래 표현식은 `f1 + f2`에 해당하는 값을 가리키게 된다.  
# ```
# f1.__add__(f2)
# ```
# 
# 분수의 덧셈은 아래와 같이 정의된다. 

# $$ 
# \frac{a}{b} + \frac{c}{d} = \frac{ad}{bd} + \frac{bc}{bd} = \frac{ad + bc}{bd} 
# $$

# 이를 구현하는 `__add__()` 메서드를 `Fraction` 클래스에 추가하자. 

# In[14]:


class Fraction :
    """
      Fraction 클래스
    """
    def __init__(self, num, den) :
        """
          num : 분자numerator
          den : 분모denominator 
        """
        self.num = num
        self.den = den
        
    def __str__(self) :
        return f"{self.num}/{self.den}"
    
    def __add__(self, other_fraction) :
        new_num = self.num * other_fraction.den + self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)


# In[15]:


f1 = Fraction(1, 4)
f2 = Fraction(1, 2)


# 그러면 이제 `Fraction`클래스의 인스턴스는 `__add__()` 메서드를 갖는다. 
# <div align="center"><img src="https://raw.githubusercontent.com/hj617kim/core_pybook/master/images/ch07/class02.png" style="width:700px;"></div>

# In[16]:


f3 = f1.__add__(f2)
print(f3)


# 덧셈 연산자 `+`를 사용해도 잘 작동한다. 

# In[17]:


f3 = f1 + f2
print(f3)


# 지금 덧셈은 잘 작동하지만 결과값이 기약분수의 형태가 아니다. 기약분수를 계산하려면 최대공약수를 계산하는 알고리즘이 필요하다.   
# 
# **유클리드 호제법**<font size="2">Euclidean-algorithm</font>  
# 유클리드 호제법은 두 정수 m과 n의 최대공약수를 구하는 가장 빠르고 효과적인 기법이다.  
# * m을 n으로 나눌 수 있으면 n이 최대공약수이다. 
# * 그렇지 않으면 n과 m % n의 최대공약수가 원하는 최대공약수이다.   
#   
# 예를 들어, 20과 30을 생각해보자. 
# * 20을 30으로 나눌 수 없다.  
# * 30과 20 % 30(= 20)의 최대공약수를 구한다. 
# * 30을 20으로 나눌 수 없다. 
# * 20과 30 % 20(= 10)의 최대공약수를 구한다. 
# * 20을 10으로 나눌 수 있으므로, 10이 최대공약수이다.   

# :::{admonition} 유클리드 호제법  
# :class: info  
# 두 정수 $m$과 $n$의 최대공약수를 $gcd(m, n)$라고 하자. 그러면 정수 $m$, $n$, $q$, $r$($n != 0$, $0 \leq  r < |n|$)에 대하여 $m = nq + r$ 이면 $gcd(m, n) = gcd(n, r)$이 성립한다.  
# 
# [증명]  
# 두 정수 $m$과 $n$의 최대공약수를 $gcd(m, n) = g$라고 하자.  
# 최대공약수 성질에 의해, $m = m'g$, $n = n'g$, $gcd(m', n') = 1$($m'$과 $n'$은 서로소)이다.   
# 그런데 $m = nq + r$ 이므로 $r = m - nq = g(m' - n'q)$이다. 즉, $r$은 $g$의 배수이다.  
# 따라서 $n = n'g$, $r = g(m' - n'q)$이므로, $gcd(n, r) = g$ 을 보이기 위해서는 $gcd(n', m' - n'q) = 1$임을 보이면 된다.  
# 
# 귀류법을 사용해보자. $1$이 아닌 어떤 정수 $d$가 존재하여 $gcd(n', m' - n'q) = d$라고 하자.   
# 그러면, 적당한 정수 $a$, $b$에 대하여 $n' = da$, $m' - n'q = db$가 된다.  
# 정리하면, $m' = n'q + db = (da)q + db = d(aq + b)$가 되는데, 이는 $m'$과 $n'$이 서로소라는 가정에 모순이 된다.   
# 따라서 $gcd(n', m' - n'q) = 1$이고, $gcd(m, n) = gcd(n, r)$이 성립한다.   
# :::
# 

# 유클리드 호제법을 구현하면 다음과 같다. 

# In[18]:


def gcd(m, n):
    while m % n != 0:
        m, n = n, m % n
    return n


# In[19]:


gcd(20, 30)


# 이제 `gcd()` 함수를 `__add__()` 메서드 정의에 활용하자. 

# In[20]:


class Fraction :
    """
      Fraction 클래스
    """
    def __init__(self, num, den) :
        """
          num : 분자numerator
          den : 분모denominator 
        """
        self.num = num
        self.den = den
        
    def __str__(self) :
        return f"{self.num}/{self.den}"
    
    def __add__(self, other_fraction) :
        new_num = self.num * other_fraction.den + self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)


# 그러면 이제 `6/8`이 아니라 `3/4`를 반환한다. 

# In[21]:


f1 = Fraction(1, 4)
f2 = Fraction(1, 2)
f3 = f1 + f2
print(f3)


# ### `__eq__()` 메서드

# 이제 두 분수가 동등한지 여부를 확인하는 코드를 작성해보자. 예를 들어, 아래 `x`와 `y`는 모두 분수 `1/2`를 가리킨다.  

# In[22]:


x = Fraction(1, 2)
y = Fraction(1, 2)


# 하지만 서로 독립적으로 생성되었기 때문에 서로 다른 객체를 가리키고 있다. 
# <div align="center"><img src="https://raw.githubusercontent.com/hj617kim/core_pybook/master/images/ch07/class03.png" style="width:700px;"></div>
# 
# 따라서 두 변수가 가리키는 값은 동등하지 않다고 판정된다. 

# In[23]:


print(x == y)


# 이런 경우에 의도적으로 동등하다고 판정되게 하고 싶다면, `__eq__()` 메서드가 적절하게 정의되어 있어야 한다. 일반적으로 두 분수의 동등성은 아래와 같이 정의된다.  

# $$
# \frac{a}{b}= \frac{c}{d} \Longleftrightarrow ad = bc
# $$

# 이를 구현하는 `__eq__()` 메서드를 `Fraction` 클래스에 추가하자. 

# In[24]:


class Fraction :
    """
      Fraction 클래스
    """
    def __init__(self, num, den) :
        """
          num : 분자numerator
          den : 분모denominator 
        """
        self.num = num
        self.den = den
        
    def __str__(self) :
        return f"{self.num}/{self.den}"
    
    def __add__(self, other_fraction) :
        new_num = self.num * other_fraction.den + self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)
    
    def __eq__(self, other_fraction) :
        first_num = self.num * other_fraction.den
        second_num = other_fraction.num * self.den
        return first_num == second_num


# In[25]:


x = Fraction(1, 2)
y = Fraction(1, 2)
print(x == y)


# ### 게터와 세터 메서드

# 아래 `a_fraction`의 분자와 분모의 값을 알고 싶다면, 아래와 같이 `num`과 `den` 속성을 확인하면 된다. 

# In[26]:


a_fraction = Fraction(1, 2)
print(a_fraction)
print(a_fraction.num)
print(a_fraction.den)


# 그리고 `num` 속성에 접근하여 값을 임의로 변경할 수도 있다.   

# In[27]:


a_fraction.num = 3
print(a_fraction.num)
print(a_fraction)


# :::{admonition} 참고     
# :class: info    
# 파이썬 클래스의 모든 것은 원칙적으로 공개<font size="2">public</font>되며, 접근 및 수정될 수 있다. 외부 노출을 최대한 줄이고 싶다면, 특별한 방식으로 변수와 메서드의 이름을 지을 수 있다.  
# * 한 개의 밑줄(`_`)로 시작 : 굳이 사용자가 알 필요 없는 속성 변수와 메서드 이름.  
# * 두 개의 밑줄(`__`)로 시작 : 숨기고자 하는 속성 변수와 메서드 이름.   
# 
# 예제와 함께 살펴보자. 
# ```
# class Fraction :
#     """
#       Fraction 클래스
#     """
#     def __init__(self, num, den) :
#         """
#           num : 분자numerator
#           den : 분모denominator 
#         """
#         self.num = num
#         self.den = den
#         self._hidden1 = 1
#         self.__hidden2 = -1
# ```
# ```python
# >>> a_fraction = Fraction(1, 2)
# ```
# 
# 하나의 밑줄로 시작하면 외부에서 사용하지 말라는 권유이다. 실제로 하나의 밑줄로 시작하는 `_hidden1` 속성은 직접 접근하여 값을 확인할 수 있다. 
# ```python
# >>> print(a_fraction._hidden1)
# 1
# ```
# 
# 반면, 두 밑줄로 시작하는 `__hidden2` 속성은 직접 접근하여 값을 확인할 수 없다. 
# ```python
# >>> print(a_fraction.__hidden2)
# AttributeError                            Traceback (most recent call last)
# /tmp/ipykernel_82/2133196738.py in <module>
# ----> 1 print(a_fraction.__hidden2)
# 
# AttributeError: 'Fraction' object has no attribute '__hidden2'
# ```
# :::

# :::{admonition} `__dict__` 속성    
# :class: info  
# `__dict__` 속성을 확인하면 객체의 속성 변수와 해당 속성 값으로 이루어진 사전을 얻는다. 그런데 `a_fraction`의 `__dict__`속성을 확인하면, `__hidden2` 대신에 `_Fraction__hidden2`가 있다. 이렇게 두 개의 밑줄로 시작하는 변수의 이름은 내부적으로 클래스 이름이 붙는 방식으로 변경된다. 이를 **네임 맹글링**<font size="2">name mangling</font>이라 한다.  
# ```python
# >>> a_fraction.__dict__
# {'num': 1, 'den': 2, '_hidden1': 1, '_Fraction__hidden2': -1}
# ```
# 
# 변경된 이름을 이용하면 속성을 확인할 수 있다. 
# ```python
# >>> a_fraction._Fraction__hidden2
# -1
# ```
# :::
# 

# 하지만 속성에 직접 접근하여 값을 변경하면서 데이터가 부적절한 값으로 변경될 가능성이 있어 사용자가 객체 외부에서 데이터에 직접 접근하는 것을 막는 것이 좋다. 보통 메서드를 만들어 객체의 속성값을 확인하거나 지정하는데, 이를 각각 **게터<font>getter</font>** 메서드와 **세터<font size="2">setter</font>** 메서드라 부르고, 관용적으로 게터 메서드 이름은 `get`으로, 세터 메서드의 이름은 `set`으로 시작한다.   
# 
# `a_fraction`의 분자와 분모의 값을 확인하는 `get_num()`와 `get_den()` 메서드를 `Fraction` 클래스에 추가하자. 

# In[28]:


class Fraction :
    """
      Fraction 클래스
    """
    def __init__(self, num, den) :
        """
          num : 분자numerator
          den : 분모denominator 
        """
        self.num = num
        self.den = den
        
    def __str__(self) :
        return f"{self.num}/{self.den}"
    
    def __add__(self, other_fraction) :
        new_num = self.num * other_fraction.den + self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)
    
    def __eq__(self, other_fraction) :
        first_num = self.num * other_fraction.den
        second_num = other_fraction.num * self.den
        return first_num == second_num
    
    def get_num(self) :
        return f"{self.num}"
    
    def get_den(self) :
        return f"{self.den}"


# In[29]:


a_fraction = Fraction(1, 2)
print(a_fraction)
print(a_fraction.get_num())
print(a_fraction.get_den())


# ## 연습 문제

# ### 문제  
# `Fraction` 클래스의 인스턴스가 사칙연산을 모두 지원하도록 아래 메서드를 구현하여라. 그러면 `-`, `*`, `/` 연산 기호를 사용할 수 있다.   
# 
# * `__sub__()` : 뺄셈(`-`)
# * `__mul__()` : 곱셈(`*`)
# * `__truediv__()` : 나눗셈(`/`) 

# ### 문제  
# `Fraction` 클래스의 인스턴스가 정수와의 사칙연산도 가능하도록 아래 메서드를 수정하여라.  
# 
# * `__add__()` : 덧셈(`+`)
# * `__sub__()` : 뺄셈(`-`)
# * `__mul__()` : 곱셈(`*`)
# * `__truediv__()` : 나눗셈(`/`) 

# ### 문제  
# `Fraction` 클래스의 인스턴스가 크기 비교가 가능하도록 아래 메서드를 구현하여라. 그러면 `<`, `>`, `<=`, `>=` 연산 기호를 사용할 수 있다.     
# 
# * `__lt__()` : 작다<font size="2">less than</font>(`<`)
# * `__gt__()` : 크다<font size="2">greater than</font>(`>`)
# * `__le__()` : 작거나 같다<font size="2">less than or equals</font>(`<=`)
# * `__ge__()` : 크거나 같다<font size="2">greater than or equals</font>(`>=`)

# ### 문제    
# (1) 은행 계좌를 관리하는 `BankAccount` 클래스를 정의하여라. `BankAccount` 클래스의 인스턴스는 `은행명`, `계좌번호`, `잔액`, `비밀번호`를 인자로 받아 다음과 같이 생성한다.   
# 
# ```python
# >>> seoul = BankAccount('서울은행', '1234-4567', 50000, 'a1234')
# ```
# 
# (2) 위의 `seoul`를 출력하면, 다음과 같이 은행명(계좌번호) 잔액을 출력하도록 `BankAccount` 클래스를 수정하여라.   
# ```python  
# >>> print(seoul)  
# '서울은행(1234-4567) 잔액 : 50000원'  
# ```
#   
# (3) 비밀번호는 외부에서 직접 접근할 수 없도록 하고, 비밀번호를 변경하는 일을 하는 `set_pw()`메서드를 `BankAccount` 클래스에 구현하여라.   
# ```python
# >>> seoul.set_pw('5678')
# 비밀번호가 변경되었습니다.
# ```
# 
# (4) 잔액을 변경하는 일을 하는 `set_money()`메서드를 `BankAccount` 클래스에 구현하여라. 단, `set_money()` 메서드는 외부에서 직접 접근할 수 없도록 한다. 
# 
# 
# (5) 입금하는 일을 하는 `deposit()`메서드를 `BankAccount` 클래스에 구현하여라. 이때 (4)에서 정의한 `set_money()` 메서드를 이용한다.   
# ```python
# >>> seoul.deposit(30000)
# 30000원이 입금되었습니다.  
# ```
# ```python
# >>> print(seoul)
# '서울은행(1234-4567) 잔액 : 80000원'  
# ```
# 
# (6) 송금하는 일을 하는 `send_money()`메서드를 `BankAccount` 클래스에 구현하여라.  
# ```python
# >>> suwon = BankAccount('수원은행', '8912-2345', 20000, 'abcabc')
# >>> seoul.send_money('5678', suwon, 10000)  #순서대로 비번, 은행명, 금액
# 수원은행에 10000원 송금했습니다.  
# >>> print(seoul)
# '서울은행(1234-4567) 잔액 : 70000원'
# >>> print(suwon)
# '수원은행(8912-2345) 잔액 : 30000원'
# ```
# 
# 이때 비밀번호가 틀리면 송금하지 않는다. 
# ```python
# >>> seoul.send_money('a2580', suwon, 10000)  #순서대로 비밀번호, 은행명, 금액
# 비밀번호를 잘 못 입력했습니다.   
# ```
# 
# 잔액보다 많은 금액을 송금할 수 없다. 
# ```python
# >>> seoul.send_money('5678', suwon, 100_000)  #순서대로 비밀번호, 은행명, 금액
# 잔액을 초과하는 금액은 송금할 수 없습니다. 
# ```
