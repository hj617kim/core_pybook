#!/usr/bin/env python
# coding: utf-8

# # 탐색

# 탐색<font size="2">searching</font>이란 모음 객체에서 특정 값의 포함여부 및 위치를 확인하는 과정을 말한다. 파이썬 리스트의 경우 `in` 연산자가 항목의 포함 여부를 $O(n)$의 시간복잡도로 확인해준다. 여기서는 항목의 포함여부를 확인하는 탐색 알고리즘을 소개하고 각 알고리즘의 차이점을 살펴본다.  

# ## 순차탐색

# 순차탐색<font size="2">sequential search</font>은 탐색 방법 중 가장 간단하고 자연스러운 방법으로, 순서를 따라 차례대로 특정 값인지를 확인하는 방법을 말한다. 파이썬의 리스트, 튜플 등은 위치에 따라 적절한 인덱스를 가지고 있어서 인덱스 순서대로 항목을 확인할 수 있다. 예를 들어, 다음은 순차탐색으로 `17`을 찾는 과정이다.     
# 
# 1. 첫 번째 항목을 확인한다. 첫 번째 항목은 `5`로 `17`이 아니다. 따라서 그 다음 항목을 확인한다.   
# 
# <div align="center"><img src="https://raw.githubusercontent.com/hj617kim/core_pybook/master/images/ch12/ss_01.png" style="width:500px;"></div>
# 
# 2. 두 번째 항목을 확인한다. 두 번째 항목은 `13`으로 `17`이 아니다. 따라서 그 다음 항목을 확인한다.  
# 
# <div align="center"><img src="https://raw.githubusercontent.com/hj617kim/core_pybook/master/images/ch12/ss_02.png" style="width:500px;"></div>
# 
# 3. 세 번째 항목을 확인한다. 세 번째 항목은 찾고자 하는 `17`이다. 따라서 탐색을 멈춘다.  
# 
# <div align="center"><img src="https://raw.githubusercontent.com/hj617kim/core_pybook/master/images/ch12/ss_03.png" style="width:500px;"></div>

# 하나의 리스트와 하나의 값을 입력 받아 순차탐색을 통해 주어진 값의 포함 여부를 판단하는 `sequential_search()` 함수를 정의해보자.   

# In[1]:


def sequential_search(a_list, item) :
    for i in a_list :
        if i == item :
            return True
    return False


# In[2]:


a_list = [5, 13, 17, 2, 48, 22]
print(sequential_search(a_list, 17))
print(sequential_search(a_list, 7))


# 탐색 알고리즘의 시간복잡도 분석은 일반적으로 항목과 값의 비교를 기본 계산단위로 사용한다. 순차검색은 항상 원하는 항목을 찾을 수 있다는 장점이 있지만, 최악의 경우 모든 항목을 살펴봐야 하므로 시간복잡도는 $O(n)$이다. 예를 들어, 아래에는 `17`이 없어서, 처음부터 모든 항목을 살펴봐야 한다.     
# 
# <div align="center"><img src="https://raw.githubusercontent.com/hj617kim/core_pybook/master/images/ch12/ss_04.png" style="width:500px;"></div>

# **정렬된 리스트 순차탐색**  
# 
# 아래 그림의 리스트는 항목들이 오름차순으로 정렬되어 있다. 이런 경우에 순차탐색 알고리즘은 일반적인 경우와는 조금 다르게 작동시킬 수 있다. 예를 들어, 아래 정렬된 리스트에서 `17`을 찾을 때, 항목을 확인하다가 찾아야 하는 `17`보다 큰 값을 항목으로 만나면 더 이상 탐색을 진행하지 않도록 할 수 있다. 
# 
# <div align="center"><img src="https://raw.githubusercontent.com/hj617kim/core_pybook/master/images/ch12/ss_05.png" style="width:500px;"></div>

# In[3]:


def ordered_sequential_search(a_list, item) :
    for i in a_list :
        if i == item :
            return True
        elif i > item :
            return False
    return False


# In[4]:


ordered_list = [2, 5, 22, 27, 48, 50]
print(ordered_sequential_search(ordered_list, 17))
print(ordered_sequential_search(ordered_list, 5))


# 위 알고리즘은 찾고자 하는 항목이 리스트의 항목으로 포함되지 않은 경우에만 약간의 개선이 발생한다. 

# ## 이진탐색

# 이진탐색<font size="2">binary search</font>은 정렬된 리스트를 탐색할 때 사용할 수 있는 알고리즘으로, 순차탐색보다 훨씬 빠르게 대상을 탐색할 수 있다. 이진 탐색은 리스트의 중앙에 위치한 항목부터 비교를 시작하여 참이면 탐색을 멈추고, 아니면 중앙 위치 왼편 또는 오른편 한 쪽에 대해서만 동일한 탐색 과정을 반복 실행한다. 예를 들어, 다음은 이진탐색으로 `51`을 찾는 과정이다.    
# 
# 1. 정렬된 항목들의 중앙 항목을 확인하여, 찾고자 하는 항목과 비교한다. 만약 항목의 개수가 짝수라면, 중앙에 있는 두 개의 항목 중 작은 쪽을 확인한다. 5번째 있는 항목의 값은 `27`로, 찾고자 하는 `51`보다 작다. 따라서 오른편에 대해서 동일한 탐색 과정을 반복한다.   
# <div align="center"><img src="https://raw.githubusercontent.com/hj617kim/core_pybook/master/images/ch12/bs_01.png" style="width:500px;"></div>
# 
# 2. 오른편의 중앙에 있는 항목은 찾고자 하는 `51`이다. 따라서 탐색을 멈춘다. 
# <div align="center"><img src="https://raw.githubusercontent.com/hj617kim/core_pybook/master/images/ch12/bs_02.png" style="width:500px;"></div>

# 하나의 리스트와 하나의 값을 입력 받아 이진탐색을 통해 주어진 값의 포함 여부를 판단하는 `binary_search()` 함수를 정의해보자.   

# In[5]:


def binary_search(a_list, item) :
    first = 0
    last = len(a_list) - 1
    
    while first <= last :
        mid = (first + last) // 2
        if a_list[mid] == item :
            return True
        elif item < a_list[mid] :
            last = mid - 1
        else :
            first = mid + 1
    return False


# In[6]:


sorted_list_bs = [2, 5, 17, 22, 27, 35, 42, 51, 62, 70]
print(binary_search(sorted_list_bs, 51))
print(binary_search(sorted_list_bs, 17))
print(binary_search(sorted_list_bs, 47))


# 이진탐색 알고리즘에 사용된 반복문이 실행될 때마다 비교 횟수는 1이 늘고, 그 다음 탐색 구간의 크기는 절반으로 줄어든다. 따라서 최악의 경우, $\frac{n}{2^k} = 1$을 만족할 때까지 반복문이 실행된다.    
# 
# |비교 횟수 | 탐색구간 크기|
# |:-----:|:-----:|
# |1|$\frac{n}{2}$|
# |2|$\frac{n}{2^2}$|
# |3|$\frac{n}{2^3}$|
# |$\cdots$|$\cdots$|
# |k|$\frac{n}{2^k}$|
# 
# 즉, 최악의 경우 $k = \log_2 n$번 항목과 값의 비교가 발생하며, 이진탐색 알고리즘의 시간복잡도는 $O(\log n)$이 된다. 

# 순차탐색과는 달리 이진탐색은 모든 항목을 탐색하지 않는다. 이러한 이진탐색은 속도가 빠르다는 장점이 있지만, 정렬된 리스트에만 사용할 수 있다는 단점도 있다. 한 번 정렬해 둔 다음에 탐색을 많이 활용한다면 이진탐색이 속도가 빠르므로, 정렬 비용이 든다 하더라도 정렬을 할 가치가 있다. 하지만 리스트가 매우 긴 경우, 정렬 시간이 매우 오래 걸리기 때문에 그냥 순차탐색을 하는 것이 더 나을 수 있다.  

# ## 분할정복

# 분할정복<font size="2">divide-and-conquer</font>은 직접 해결할 수 있을 정도로 단순해질 때까지 작은 문제로 분할하여 문제를 해결하는 방법을 말한다. 예를 들어, 이진탐색이 대표적인 분할정복 기법의 활용예제이다. 이진탐색의 경우 리스트를 절반으로 줄이는 과정을 반복하면서 항목의 포함여부를 판단하며, 작은 크기와 구간에 대한 포함여부가 판단되는 순간 그것을 원래 문제의 결론으로 사용하고 동시에 실행을 멈춘다.  
# 
# 분할정복 기법으로 해결되는 문제는 보통 재귀로 매우 효율적으로 해결된다. 이는 비록 재귀호출이 반복적으로 발생하기는 하지만 재귀호출 도중 결론이 나면 바로 실행이 완료되기 때문이다. 이러한 분할정복 기법은 다양한 알고리즘 문제 해결에 활용된다. 예를 들어, 다음 장에서 살펴볼 합병정렬과 퀵정렬도 분할정복 기법을 사용한다.   

# 하나의 리스트와 하나의 값을 입력 받아 이진탐색을 재귀함수로 구현하는 `binary_search_recursive()` 함수를 정의해보자.   

# In[7]:


def binary_search_recursive(a_list, item) :
    if len(a_list) == 0 :
        return False
    else :
        mid = len(a_list) // 2
        if a_list[mid] == item :
            return True
        elif item < a_list[mid] :
            return binary_search_recursive(a_list[:mid], item)
        else :
            return binary_search_recursive(a_list[mid + 1 :], item) 


# In[8]:


sorted_list_bs = [2, 5, 17, 22, 27, 35, 42, 51, 62, 70]
print(binary_search_recursive(sorted_list_bs, 51))
print(binary_search_recursive(sorted_list_bs, 17))
print(binary_search_recursive(sorted_list_bs, 47))


# :::{admonition} 디렉터리<font size="2">directory, 폴더</font>와 파일<font size="2">file</font> 다루기     
# :class: info  
# 
# **`os` 모듈**  
# `os` 모듈은 운영체제에서 제공하는 여러 기능을 파이썬으로 조작 가능하게 한다. 여기서 `os`는 operating system<font size="2">운영체제</font>의 약자이다.   
# 
# * `os.getcwd()` : 현재 작업하고 있는 위치의 디렉터리<font size="2">current working directory</font>를 문자열로 반환.  
# * `os.chdir(path)` : 작업 디렉터리를 변경.
# * `os.mkdir(path)` : `path`라는 디렉터리를 만든다. 디렉터리가 이미 존재하면, `FileExistsError`가 발생.  
# * `os.rmdir(path)` : 디렉터리 `path`를 삭제한다. 디렉터리가 존재하지 않으면 `FileNotFoundError`, 디렉터리가 비어있지 않으면 `OSError`가 발생.  
# * `os.unlink(path)` or `os.remove(path)`: 파일 `path`를 삭제한다. 
# * `os.listdir(path)` : `path`에 의해 주어진 디렉터리에 있는 항목들의 이름을 담고 있는 리스트를 반환. 
# 
# 
# **`zipfile` 모듈**   
#   
# `zipfile` 모듈은 zip 파일을 만들고, 읽고, 쓰고, 추가하는 일 등을 한다. 여기서는 파일을 압축하고, 해제하는 방법을 알아보자.  
# * `zipfile.ZipFile(path, mode = 'r')` : zip 파일을 읽고 쓰는 클래스.
#    * `mode = 'r'` : 읽기 모드
#    * `mode = 'w'` : 쓰기 모드 
# * `ZipFile.write(filename)` : 압축할 filename 지정  
# * `ZipFile.extractall()` : 모든 파일 압축 해제
# * `ZipFile.namelist()` : 압축 파일 내에 존재하는 파일명을 리스트로 반환.
# * `zipfile.close()` : zip 파일 닫기 
# 
# 예를 들어, 디렉터리 `my_dir`아래에 있는 `my_file01.txt`와 `my_file02.txt`를 압축하는 코드는 아래와 같다. 
# ```
# import zipfile
# 
# my_zip = zipfile.ZipFile('./zipName.zip', 'w')
# my_zip.write('./my_dir/my_file01.txt')
# my_zip.write('./my_dir/my_file02.txt')
# my_zip.close()
# ```
# 
# 그리고 `zipName.zip`을 해제하는 방법은 아래와 같다. 
# ```
# import zipfile 
# 
# my_zip = zipfile.ZipFile('./zipName.zip')
# my_zip.extractall() # 경로를 인자로 줄 수도 있음.
# 
# ```
# 
# 이제 파일에 저장된 데이터를 불러오거나 파일에 데이터를 저장하는 방법을 살펴보자. 이를 위해 파이썬 내장함수 `open(filename, mode='r')`을 사용한다. 
# 
# * `filename` : 파일 이름을 담은 문자열
# * `mode` : 파일이 사용될 방식
#   * `r` : 읽기 모드.
#   * `w` : 쓰기 모드. 같은 이름의 파일이 이미 존재하면, 그 파일의 내용은 모두 사라지고, 존재하지 않으면 새로운 파일이 생성됨.
#   * `a` : 추가 모드. 파일의 마지막에 새로운 내용을 추가시킬 때 사용. 
# 
# **새 파일에 쓰기**  
# * 새 파일을 생성한 후에 내용을 적어 넣으려면, `open()` 함수를 쓰기 모드(`w`-모드)를 이용하여, 아래 형식으로 호출. 
# > `open('파일경로를 포함한 파일이름', 'w')`    
# * 생성된 파일에 내용을 추가하려면, `write()` 메서드를 활용한다.
# > `파일객체.write(추가내용)`  
# * 생성된 파일에 내용추가하기가 종료되었으면 해당 파일객체를 닫아야 함. 파일 객체를 닫는 것이 예상치 못한 오류를 방지.
# > `파일객체.close()`
# 
# 
# **파일 읽기**
# * 파일을 읽으려면, open 함수를 읽기 모드(r-모드)를 이용하여, 아래 형식으로 호출하면 된다.
# > `open('파일경로를 포함한 파일이름', 'r')`
# * `for ... in 파일객체` 형식으로 파일 내용 확인 가능. 
# * `파일객체.readline()` 메서드 : 파일에 저장된 내용을 한 줄씩 읽어 들여 문자열로 반환. 
# * `파일객체.readlines()` 메서드 : 파일에 저장된 내용의 각 줄을 항목으로 갖는 리스트 반환. 
# * `파일객체.read()` 메서드 : 파일에 저장된 내용 전체를 하나의 문자열로 반환. 
# 
# **`with`문**  
# `with`문을 사용하면 `close()`를 사용하지 않아도 열린 파일을 자동으로 닫아 준다. 다음의 형식은 
# ```
# with open('파일경로를 포함한 파일이름') as f :
#     코드
# ```
# 아래 코드에 대응한다. 
# ```
# f = open('파일경로를 포함한 파일이름')
# 코드 
# f.close()
# ```
# :::
# 

# ## 연습 문제

# ### 문제
