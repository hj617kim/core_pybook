#!/usr/bin/env python
# coding: utf-8

# # 잔돈 지불 문제

# 10원, 50원, 100원, 500원 짜리 동전만을 이용하여 잔돈을 지불하고자 한다. 이때 630원을 지불하기 위해 필요한 최소한의 동전 개수는 얼마인가?

# ## 탐욕 기법  
# 
# 탐욕 기법<font size="2">greedy method</font>은 매 선택 순간에 정해진 기준에 따라 **가장 좋은 것**을 선택하는 기법이다. 잔돈 지불 문제의 경우, 가능한한 가장 큰 단위의 동전을 먼저 사용하는 것을 의미한다. 따라서 630원을 잔돈으로 지불하려면 5개의 동전이 필요하다.   
# 
# * 500원 동전 : 1개
# * 100원 동전 : 1개
# * 10원짜리 동전 : 3개

# In[1]:


def make_change_greedy(coin_list, change) :
    cnt = 0
    coin_list = sorted(coin_list, reverse = True)
    for coin in coin_list :
        cnt += change // coin
        change %= coin
    return cnt


# In[2]:


print(make_change_greedy([10, 50, 100, 500], 630))


# 그런데, 탐욕 알고리즘은 항상 최선의 해답을 제공하지는 않는다. 그 이유는 만약 210원짜리 동전이 추가로 주어진다면, 필요한 동전의 최소 개수는 2개지만, 탐욕 기법은 이전과 동일하게 5개의 동전을 사용하는 해법을 제시하기 때문이다.  

# In[3]:


print(make_change_greedy([10, 50, 100, 210, 500], 630))


# ## 완전 탐색 기법
# 완전 탐색 또는 부르트 포스<font size="2">brute force</font>기법은 가능한 모든 경우를 고려하는 기법을 말한다. 잔돈 지불 문제의 경우, 지불할 수 있는 최소한의 동전 개수를 아래와 같이 재귀로 계산할 수 있다. 즉, 지정된 액수의 잔돈 지불에 필요한 최소한의 동전 개수는 지불액에서 500원, 100원, 50원, 10원을 뺀 각각의 값을 지불하는 데에 필요한 최소한의 동전 개수로 계산한다. 예를 들어, 120원의 경우, 100원, 50원, 10원을 뺀 각각의 값을 지불하는 데에 필요한 최소한의 동전 개수를 계산한다. 그림으로 나타내면, 아래와 같다. 
# 
# <div align="center"><img src="https://raw.githubusercontent.com/hj617kim/core_pybook/master/images/ch11/bruteforce_01.png" style="width:500px;"></div>
# 
# 
# `make_change_brute_force()`함수 선언에 사용된 변수들의 역할은 다음과 같다.  
# 
# * `coin_list` : 사용 가능한 동전들의 리스트
# * `change` : 잔돈 지불액
# * `min_cnt` : 잔돈 지불에 필요한 최소 동전 개수

# In[4]:


def make_change_brute_force(coin_list, change) :
    min_cnt = change // 10
    
    if change in coin_list :
        return 1
    else : 
        for coin in [c for c in coin_list if c <= change] :
            cnt = 1 + make_change_brute_force(coin_list, change - coin)
            if cnt < min_cnt :
                min_cnt = cnt
                
    return min_cnt


# In[5]:


print(make_change_brute_force([10, 50, 100, 500], 630))


# In[6]:


print(make_change_brute_force([10, 50, 100, 210, 500], 630))


# 완전 탐색 알고리즘을 사용하면 해답을 찾을 수 있지만, 보통 실행에 많은 시간이 걸린다. 그래서 좀 더 최적화된 방법을 고민해봐야 한다. 

# ## 메모이제이션 기법 
# 동일 인자에 대한 반복 호출 문제는 메모이제이션 기법으로 간단하게 해결된다. 여기서는 한 번 호출되어 반환된 값을 기억하기 위해 **디폴트딕트**<font size="2">defaultdict</font> 객체를 활용해보자. 디폴트딕트 객체는 사전과 거의 동일한 모음 자료형이지만, 사전 객체와는 달리 특정 키의 포함 여부를 미리 확인할 필요가 없다. 
# 
# ```python 
# >>> aDict = {}
# >>> print(aDict[10])
# KeyError                                  Traceback (most recent call last)
# /tmp/ipykernel_209/1710605932.py in <module>
#       1 aDict = {}
# ----> 2 print(aDict[10])
# 
# KeyError: 10
# ```
# 
# 디폴트딕트 객체를 생성할 때는 값들의 자료형을 명시하며, `int`의 경우 모든 키의 값이 0으로 초기화된다. 

# In[7]:


from collections import defaultdict

aDict = defaultdict(int)
print(aDict[10])


# 아래 `make_change_brute_force2()` 함수는 재귀 호출이 발생할 때마다 그 결과를 디폴트딕트에 기억해두고, 필요한 경우 재활용한다. 

# In[8]:


from collections import defaultdict

def make_change_brute_force2(coin_list, change, known_results=defaultdict(int)) :
    min_cnt = change // 10
    if change in coin_list :
        known_results[change] = 1
        return 1
    elif known_results[change] > 0 :
        return known_results[change]
    else : 
        for coin in [c for c in coin_list if c <= change] :
            cnt = 1 + make_change_brute_force2(coin_list, change - coin, known_results)
            if cnt < min_cnt :
                min_cnt = cnt
            known_results[change] = min_cnt
    return min_cnt


# In[9]:


print(make_change_brute_force2([10, 50, 100, 500], 630, known_results=defaultdict(int)))


# In[10]:


print(make_change_brute_force2([10, 50, 100, 210, 500], 630, known_results=defaultdict(int)))


# :::{admonition} 주의   
# :class: caution  
# `make_change_brute_force2()`함수를 실행할 때, 키워드 인자`known_results=defaultdict(int)`도 지정해야 한다. 그렇지 않으면, 동전의 종류가 달라졌을 때 제대로 동작하지 않는다. 예를 들어, 키워드 인자`known_results=defaultdict(int)`를 지정하지 않고, `make_change_brute_force2([10, 50, 100, 500], 630)`를 실행하면 `known_results`의 기본값인 디폴트딕트에는 키 630에 대응하는 값으로 5가 저장된다. 이 상태에서 동전의 종류가 달라진 `make_change_brute_force2([10, 50, 100, 210, 500], 630)`를 실행하면, `210`원짜리 동전을 고려하지 않고 디폴트딕트에 지정된 키 630에 대응하는 값인 5를 반환한다. 
# 
# ```python
# >>> print(make_change_brute_force2([10, 50, 100, 500], 630))
# 5
# >>> print(make_change_brute_force2([10, 50, 100, 210, 500], 630))
# 5
# ```
# :::
# 

# ## 동적계획법  
# 동적계획법<font size="2">Dynamic Programming, DP</font>은 **최적화 문제**<font size="2">optimization problem</font> 해결에 사용되는 기법 중의 하나로, 큰 문제를 구성하는 작은 문제를 해결한 다음 결과를 저장하고, 그 저장된 결과를 활용하여 큰 문제를 해결하는 방법을 말한다.    

# :::{admonition} 최적화 문제  
# :class: info  
# 최적화 문제는 하나 이상의 해답 중에서 최적의 해답을 찾는 문제이다. 최적의 기준은 문제에 따라 다르며, 보통 특정 기준에 맞는 최댓값 또는 최솟값을 사용한다. 
# :::
# 

# 예를 들어, 잔돈 630원을 지불해야 하는 경우 10원부터 출발해서 630원까지 각각의 경우에 필요한 최소 동전 수를 계산한다. 앞에서 살펴본 메모이제이션 기법을 거꾸로 적용하는 것과 유사하지만, 여기서는 10원, 20원, 30원 등부터 630원까지 **모든 경우**에 대해 차례대로 필요한 최소 동전 수를 저장하고 필요한 경우 재활용한다.   
# 
# 아래 그림은 10원부터 110원까지 잔돈 지불에 필요한 최소 동전 수를 저장하는 과정을 보여준다. 예를 들어, 110원을 지불하고자 하는 경우 아래 세 경우를 확인한 다음에 최솟값을 선택한다.  
# 
# <div align="center"><img src="https://raw.githubusercontent.com/hj617kim/core_pybook/master/images/ch11/df_01.png" style="width:700px;"></div>
# 
# 
# * 10원 동전을 사용하는 경우 : 100원 지불 방식에 1을 더한 값
# * 50원 동전을 사용하는 경우 : 60원 지불 방식에 1을 더한 값
# * 100원 동전을 사용하는 경우 : 10원 지불 방식에 1을 더한 값

# 동적계획법을 이용하여 잔돈 지불 문제를 해결하는 알고리즘은 다음과 같다. 

# In[11]:


from collections import defaultdict

def make_change_dp(coin_list, change) :
    min_cnt = defaultdict(int)
    
    # 10원부터 차례대로 최소 동전 수 계산
    for changeToMake in range(10, change + 10, 10) :
        cnt = changeToMake // 10
        for coin in [c for c in coin_list if c <= changeToMake] :
            if min_cnt[changeToMake - coin] + 1 < cnt :
                cnt = min_cnt[changeToMake - coin] + 1
        min_cnt[changeToMake] = cnt
    
    return min_cnt[change]


# In[12]:


print(make_change_dp([10, 50, 100, 500], 630))


# In[13]:


print(make_change_dp([10, 50, 100, 210, 500], 630))


# 위 알고리즘은 해답을 찾는 데 걸리는 시간이 빠른 편이다. 하지만 지금은 지불에 필요한 최소 동전 수만 계산할 뿐 실제로 어떻게 지불해야 하는가는 알려주지 않는다. 이 문제를 해결하려면 디폴트딕트를 업데이트하면서 동시에 마지막으로 사용된 동전이 무엇이었는지를 기억하면 된다.   

# In[14]:


from collections import defaultdict

def make_change_dp2(coin_list, change) :
    min_cnt = defaultdict(int)
    coins_used = defaultdict(int) 
    
    # 10원부터 차례대로 최소 동전 수 계산
    for changeToMake in range(10, change + 10, 10) :
        cnt = changeToMake // 10
        new_coin = 10
        for coin in [c for c in coin_list if c <= changeToMake] :
            if min_cnt[changeToMake - coin] + 1 < cnt :
                cnt = min_cnt[changeToMake - coin] + 1
                new_coin = coin
        min_cnt[changeToMake] = cnt
        coins_used[changeToMake] = new_coin
    
    return min_cnt[change], coins_used


def print_coins(coins_used, change) :
    coin = change
    while coin > 0 :
        this_coin = coins_used[coin]
        print(this_coin, end = ' ')
        coin = coin - this_coin


# In[15]:


amount = 630
coin_list = [10, 50, 100, 500]

num_coins, coins_used = make_change_dp2(coin_list, amount)
print(f"잔돈 {amount} 원을 지불하기 위해 다음 {num_coins} 개의 동전 필요:", end=" ")
print_coins(coins_used, amount)


# 210원 동전이 추가되면, 210원 동전 3개가 필요함을 확인해준다. 

# In[16]:


amount = 630
coin_list = [10, 50, 100, 210, 500]

num_coins, coins_used = make_change_dp2(coin_list, amount)
print(f"잔돈 {amount} 원을 지불하기 위해 다음 {num_coins} 개의 동전 필요:", end=" ")
print_coins(coins_used, amount)


# ## 연습 문제

# ### 문제

# $w$kg까지 넣을 수 있는 가방을 들고 쥬얼리샵에 침입하였다고 가정한다. 훔칠 수 있는 `n`개의 보석이 주어졌고, 각 보석은 서로 다른 무게를 갖는다고 가정한다. 가방에 넣은 보석의 값어치가 최대가 되도록 할 때, 가방에 넣은 가격을 반환하는 함수`bag1(stuff, w)`를 정의하여라.  
# 
# 예를 들어, 5개의 보석이 있고, 각각의 가격과 무게가 아래 표와 같다면, `stuff = [[2, 3], [3, 4], [4, 8], [5, 8], [9, 10]]`이다.  
# 
# |보석류|무게|가격|
# |:------:|:----:|:----:|
# |1|2|3|
# |2|3|4|
# |3|4|8|
# |4|5|8|
# |5|9|10|
# 
# 참고로, 보석은 쪼갤 수 없다. 

# ```python
# >>> stuff = [[2, 3], [3, 4], [4, 8], [5, 8], [9, 10]]
# >>> bag1(stuff, 20)
# 29
# ```

# ### 문제

# $w$kg까지 넣을 수 있는 가방을 들고 쥬얼리샵에 침입하였다고 가정한다. 훔칠 수 있는 `n`개의 보석가루가 주어졌고, 각 보석 가루는 서로 다른 무게를 갖는다고 가정한다. 가방에 넣은 보석 가루의 값어치가 최대가 되도록 할 때, 가방에 넣은 가격을 반환하는 함수`bag2(stuff, w)`를 정의하여라.  
# 
# 예를 들어, 5개의 보석이 있고, 각각의 가격과 무게가 아래 표와 같다면, `stuff = [[2, 3], [3, 4], [4, 8], [5, 8], [9, 10]]`이다.  
# 
# |보석류|무게|가격|
# |:------:|:----:|:----:|
# |1|2|3|
# |2|3|4|
# |3|4|8|
# |4|5|8|
# |5|9|10|
# 
# 참고로, 보석 가루는 원하는 만큼 담아 갈 수 있다. 

# ```python
# >>> stuff = [[2, 3], [3, 4], [4, 8], [5, 8], [9, 10]]
# >>> bag2(stuff, 20)
# 29.67
# ```

# ### 문제

# **파스칼의 삼각형**<font size="2">Pascal's triangle</font>은 이전 행의 두 원소를 더해 새로운 원소를 추가하는 과정을 반복해서 생성하는 삼각형이다.   
# 
# <div align="center"><img src="https://raw.githubusercontent.com/hj617kim/core_pybook/master/images/ch11/pascal_01.png" style="width:400px;"></div>
# 
# 파스칼 삼각형의 n행, k번째 값은 **이항계수**<font size="2">binomial coefficient</font>와 동일하다.    
# 
# $${}_n C_{k} = \begin{pmatrix} n \\ k  \end{pmatrix} = \frac{n!}{k!(n-k)!}$$    
# 
# 이항계수의 의미는 아래 등식에서 유래한다.  
# 
# $$(a + b)^n = a^n + \begin{pmatrix} n \\ 1  \end{pmatrix}a^{n-1}b + \begin{pmatrix} n \\ 2  \end{pmatrix} a^{n-2}b
# ^2+ \cdots + \begin{pmatrix} n \\ n - 1  \end{pmatrix} ab^{n-1} + b^n  = \sum_{k=0}^n  \begin{pmatrix} n \\ k  \end{pmatrix} a^{n-k}b^k$$

# 또, 이항계수는 다음이 성립한다.   
# 
# $$\begin{pmatrix} n \\ k  \end{pmatrix} = \begin{cases} \begin{pmatrix} n - 1 \\ k -1  \end{pmatrix} + \begin{pmatrix} n - 1 \\ k  \end{pmatrix} & \text{,} 0 < k < n   \\   1 & \text{,} k \in \{0, n\} \end{cases}$$

# 이러한 이항계수는 서로 다른 $n$개의 구슬에서 임의로 서로 다른 $k$개의 구술을 선택하는 방법을 의미하기도 한다. 

# * **재귀를 활용**하여, 파스칼의 삼각형의 $n$행, $k$번째 값, 즉 이항계수 $\begin{pmatrix} n \\ k  \end{pmatrix}$를 반환하는 `bin_recursion(n, k)`함수를 정의하여라. 

# * **동적계획법을 활용**하여, 파스칼의 삼각형의 $n$행, $k$번째 값, 즉 이항계수 $\begin{pmatrix} n \\ k  \end{pmatrix}$를 반환하는 `bin_df(n, k)`함수를 구현해보자.
