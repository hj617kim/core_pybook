#!/usr/bin/env python
# coding: utf-8

# # 최단경로 문제

# 집에서 학교로 가는 최단경로<font size="2">shortest path</font>의 길이를 구하여라. 
# 
# <div align="center"><img src="https://raw.githubusercontent.com/hj617kim/core_pybook/master/images/ch14/sp_01.png" style="width:500px;"></div>
# 

# ## 그래프

# 그래프<font size="2">graph</font>는 정점<font size="2">vertex 또는 마디node</font>과 이음선<font size="2">edge</font>으로 구성된 것을 말한다. 그래프 관련 용어는 아래와 같다.  
# 
# * 정점<font size="2">vertex 또는 마디node</font> 
# * 이음선<font size="2">edge</font>
# * 방향 그래프<font size="2">directed graph</font> : 이음선에 방향이 있는 그래프
# * 가중치<font size="2">weight</font>
# * 가중치 포함 그래프<font size="2">weighted graph</font>
# * 경로<font size="2">path</font> : 이음선으로 연결된 마디들의 나열. 즉, 하나의 마디에서 다른 마디로 가는 이음선의 연결.
# * 단순경로<font size="2">simple path</font> : 같은 마디를 두 번 지나지 않는 경로 
# * 경로의 길이<font size="2">length</font> :  
#    * 가중치  포함 그래프의 경우 : 경로 상에 있는 가중치의 합
#    * 가중치 미포함 그래프의 경우 : 경로 상에 있는 이음선의 수   
#    
# 아래는 방향 그래프와 가중치 포함 그래프이다. 
# <div align="center">
#     <img src="https://raw.githubusercontent.com/hj617kim/core_pybook/master/images/ch14/sp_02.png" style="width:350px;">
#     <img src="https://raw.githubusercontent.com/hj617kim/core_pybook/master/images/ch14/sp_03.png" style="width:300px;">
# </div>
# 

# :::{admonition} 쾨니히스베르크의 다리 문제  
# :class: info    
# 쾨니히스베르크에는 프레겔 강이 흐르고, 두 개의 큰 섬이 있다. 그리고 아래와 같이 두 섬과 나머지를 연결하는 7개의 다리가 있다.  
# <div align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/5/5d/Konigsberg_bridges.png" style="width:300px;"></div>
# 
# 쾨니히스베르크의 다리 문제는 위의 7개의 다리들을 한 번씩만 건너서 처음의 위치로 돌아올 수 있는가이다. 수학자 오일러는 이 문제를 해결하기 위하여 그래프를 도입하였고, 이것이 불가능하다는 것을 증명하였다.  
# :::
# 

# ## 최단경로 문제  
# 
# 위의 문제는 하나의 점<font size="2">마디node</font>에서 다른 점<font size="2">마디node</font>로 가는 최단경로를 구하는 문제이다. 이때 이음선의 가중치와 방향을 함께 고려해야 한다. 이때의 최단경로는 단순경로로 찾으면 된다.   
# 
# **응용 사례**  
# * 도시 간의 최단경로 
# * 다구간 비행기표 여정 
# * 지도앱에서 경유 추가  

# 위의 가중치 포함 방향 그래프에서 v1에서 v3로 가는 단순경로와 길이는 다음 여섯 종류이다.   
# 
# * v1 → v2 → v3            : 경로 길이는 1 + 4 = 5 
# * v1 → v2 → v4 → v3       : 경로 길이는 1 + 1 + 2 = 4
# * v1 → v2 → v5 → v4 → v3  : 경로 길이는 1 + 2 + 7 + 2 = 12
# * v1 → v5 → v2 → v3       : 경로 길이는 3 + 9 + 4 = 16
# * v1 → v5 → v2 → v4 → v3  : 경로 길이는 3 + 9 + 1 + 2 = 15
# * v1 → v5 → v4 → v3       : 경로 길이는 3 + 7 + 2 = 12  
# 
# 이 중에서 v1 → v2 → v4 → v3 가 v1에서 v3로 가는 최단경로이다. 

# ## 다익스트라 알고리즘

# 다익스트라<font size="2">또는 데이크스트라 Dijkstra</font> 알고리즘은 하나의 노드에서 다른 노드로 가는 가장 짧은 경로를 찾는 알고리즘으로, Dijkstra가 고안했다.  
# 
# 다익스트라 알고리즘은 초깃값을 부여하고, 단계를 거듭하며 값을 개선시키는 방법이다. 아래 문제와 함께 다익스트라 알고리즘을 살펴보자. 시작 노드는 1이다.   
# <div align="center">
#     <img src="https://raw.githubusercontent.com/hj617kim/core_pybook/master/images/ch14/sp_03.png" style="width:350px;">
# </div>
# 
# 1. 시작 노드의 경로 길이는 0으로, 다른 노드는 무한대로 초기화한다.  
# 
# |노드|v1|v2|v3|v4|v5|
# |:---:|:---:|:---:|:---:|:---:|:---:|
# |경로의 길이|0|inf|inf|inf|inf|
# 
# 방문하지 않은 노드 중에서 경로의 길이가 가장 짧은 노드를 선택한다. 여기서는 v1이다.  
# 
# 2. v1를 거쳐 다른 노드로 가는 경로를 계산하여, 현재 값보다 작으면 값을 변경한다. 여기서는 v2와 v5가 v1과 연결되어 있다.   
# 
# |노드|v1|v2|v3|v4|v5|
# |:---:|:---:|:---:|:---:|:---:|:---:|
# |경로의 길이|0|1|inf|inf|3|
# 
# 방문하지 않은 노드 중에서 경로의 길이가 가장 짧은 노드를 선택한다. 여기서는 v2이다.  
#   
# 3. v2를 거쳐 다른 노드로 가는 경로를 계산하여, 현재 값보다 작으면 값을 변경한다. 여기서는 v2와 연결된 v3, v4, v5를 살펴보면 된다. v1은 방문한 노드이다. 
# 
# * v1 → v2 → v3 하면 1 + 4이고, 이는 inf 보다 작다.  
# * v1 → v2 → v4 하면 1 + 1이고, 이는 inf 보다 작다. 
# * v1 → v2 → v5 하면 1 + 2이고, 이는 3보다 작지 않다. 
# 
# |노드|v1|v2|v3|v4|v5|
# |:---:|:---:|:---:|:---:|:---:|:---:|
# |경로의 길이|0|1|5|2|3|
# 
# 방문하지 않은 노드 중에서 경로의 길이가 가장 짧은 노드를 선택한다. 여기서는 v4이다. 참고로, v1과 v2는 이미 방문한 노드이다.  
# 
# 4. v4를 거쳐 다른 노드로 가는 경로를 계산하여, 현재 값보다 작으면 값을 변경한다. 여기서는 v4와 연결된 v3를 살펴보면 된다. v2는 방문한 노드다. 
# * v1 → v2 → v4 → v3 하면 1 + 1 + 2이고, 이는 5보다 작다. 
# 
# |노드|v1|v2|v3|v4|v5|
# |:---:|:---:|:---:|:---:|:---:|:---:|
# |경로의 길이|0|1|4|2|3|
# 
# 방문하지 않은 노드 중에서 경로의 길이가 가장 짧은 노드를 선택한다. 여기서는 v5이다. 참고로, v1과 v2, v4는 이미 방문한 노드이다.   
# 
# 5. v5를 거쳐 다른 노드로 가는 경로를 계산하여, 현재 값보다 작으면 값을 변경한다. v5와 연결된 노드는 모두 방문한 노드다.   
# 
# 6. 마지막으로 남은 노드는 v3이다. 따라서, v1에서 v3로 가는 최단경로의 길이는 4이다.   
#   
#   
# 다익스트라 알고리즘을 정리하면 다음과 같다.  
# 
# * 시작 노드의 경로 길이는 0으로, 다른 노드는 무한대로 초기화한다.  
# * 방문하지 않은 노드 중에서 경로의 길이가 가장 짧은 노드를 선택한다. 
# * 위에서 선택한 노드를 거쳐 다른 노드로 가는 비용을 계산한 다음, 현재 값과 비교하여 작은 값을 경로의 길이로 둔다. 
# * 방문하지 않은 노드 중에서 경로의 길이가 가장 짧은 노드를 선택할 때, 그것이 도착 노드가 될 때까지 위의 두 과정을 반복한다.   

# 이제 그래프와 노드의 개수, 시작 노드, 도착 노드를 인자로 받아 최단경로의 길이를 반환하는 `Dijkstra()` 함수를 정의하여라. 이때, 그래프는 아래와 같이 중첩된 리스트로 표현한다. 예를 들어, graph 리스트의 1번 인덱스 값 `[[2, 1], [5, 3]]`은 노드1에서 노드2로 가는 길이(또는 가중치)가 1이고, 노드1에서 노드5로 가는 길이가 3라는 의미다.   
# 
# ```python
# >>> graph = [[],[[2, 1], [5, 3]], [[1, 3], [3, 4], [4, 1], [5, 2]], [[4, 4]], [[2, 2], [3, 2]], [[2, 9], [4, 7]]]
# >>> print(Dijkstra(graph, 5, 1, 3))
# 4
# ```

# In[1]:


from math import inf

def Dijkstra(graph, n_nodes, start, target) :
    #노드의 방문 정보를 담은 리스트 
    nodes = [False] * (n_nodes + 1)
    
    #경로 길이를 담은 리스트
    dst = [inf] * (n_nodes + 1)

    
    #방문하지 않은 노드 중에서 경로의 길이가 가장 짧은 노드를 반환하는 함수-순차탐색
    def get_smallest_node():
        min_value = inf
        for i in range(1, n_nodes + 1) :
            if not nodes[i] and dst[i] < min_value :
                min_value = dst[i]
                idx = i
        return idx
    
    #시작 노드 경로 길이 0, 방문 정보 True
    dst[start] = 0
    nodes[start] = True
    
    
    #시작 노드를 거쳐 경우, 경로의 길이 갱신
    for e in graph[start] :
        dst[e[0]] = e[1]
    
    # 방문하지 않은 노드 중에서 경로의 길이가 가장 짧은 노드를 찾아 위의 과정 반복
    for i in range(n_nodes - 1) :
        sm_node = get_smallest_node()
        nodes[sm_node] = True
        
        # 찾은 노드가 targe이면, 더 이상 반복하지 않아도 됨
        if sm_node == target :
            return dst[target]
        
        for e in graph[sm_node] :
            if dst[sm_node] + e[1] < dst[e[0]] :
                dst[e[0]] = dst[sm_node] + e[1]
                
    return dst[target]


# In[2]:


graph = [[],[[2, 1], [5, 3]], [[1, 3], [3, 4], [4, 1], [5, 2]], [[4, 4]], [[2, 2], [3, 2]], [[2, 9], [4, 7]]]
print(Dijkstra(graph, 5, 1, 3)) 


# :::{admonition} 주의  
# :class: caution  
# 다익스트라 알고리즘은 가중치가 음수가 아닐 때 사용한다. 
# :::
# 

# ## 우선순위 큐

# 우선순위 큐<font size="2">Priority Queue</font>는 우선순위가 높은 항목을 먼저 꺼내는 자료형이다. 파이썬에서는 `queue` 모듈의 `PriorityQueue`클래스를 이용하여 우선순위 큐를 사용할 수 있고, 가장 낮은 항목을 먼저 꺼낸다.  

# :::{admonition} 참고  
# :class: info  
# 스택 : 선입후출<font size="2">Last In First Out, LIFO</font>  
# 큐 : 선입선출<font size="2">First In First Out, FIFO</font>  
# :::
# 

# 우선순위 큐에 항목을 추가할 때는 `put()` 메서드를 이용하며, 항목을 꺼낼 때는 `get()` 메서드를 이용한다. 

# In[3]:


from queue import PriorityQueue

pque1 = PriorityQueue()
pque1.put(3)
pque1.put(5)
pque1.put(1)
pque1.put(4)

print(pque1.get())
print(pque1.get())
print(pque1.get())
print(pque1.get())


# 항목이 추가된 순서와 상관없이 우선순위가 높은 항목, 여기서는 값이 작은 항목부터 반환되는 것을 볼 수 있다.   
#   
# 우선순위 큐에 항목을 추가할 때, 우선순위와 항목을 함께 지정할 수도 있다. 형식은 `(우선순위, 항목)`이다.  

# In[4]:


pque2 = PriorityQueue()
pque2.put((0, 3))
pque2.put((7, 2))
pque2.put((2, 5))
pque2.put((1, 1))

print(pque2.get())
print(pque2.get())
print(pque2.get())
print(pque2.get())


# 그러면, 첫 번째 항목의 값이 작은(또는 우선순위가 높은) 항목부터 반환되는 것을 볼 수 있다. 

# 위의 다익스트라 `Dijkstra()`함수 정의에서 방문하지 않은 노드 중에서 경로의 길이가 가장 짧은 노드를 찾을 때, 순차탐색을 사용하였다. 순차탐색은 원하는 항목을 찾을 수 있다는 장점이 있지만 느리다. 우리는 순차탐색 대신 우선순위 큐를 사용할 수 있다. 

# In[5]:


from math import inf
from queue import PriorityQueue

def Dijkstra1(graph, n_nodes, start, target) :

    #경로 길이를 담은 리스트
    dst = [inf] * (n_nodes + 1)

    pque = PriorityQueue()
    pque.put((0, start))
    dst[start] = 0
    
    while not pque.empty() :
        d, sm_node = pque.get()
        if dst[sm_node] < d :
            continue
        for e in graph[sm_node] :
            if dst[sm_node] + e[1] < dst[e[0]] :
                dst[e[0]] = dst[sm_node] + e[1]
                pque.put((dst[e[0]], e[0]))
                
    return dst[target]


# In[6]:


graph = [[],[[2, 1], [5, 3]], [[1, 3], [3, 4], [4, 1], [5, 2]], [[4, 4]], [[2, 2], [3, 2]], [[2, 9], [4, 7]]]
print(Dijkstra1(graph, 5, 1, 3)) 


# ## 연습 문제

# ### 문제

# A는 이번 여름에 독일 함부르크에서 열리는 학회에 참석하기로 했다. 인천에서 다른 지역을 경유하여 함부르크로 갈 예정이고, 경유하고 싶은 도시와 그 도시까지의 비행 시간을 아래와 같이 정리하였다.   
# 
# 예를 들어, `프랑크푸르트`의 대응하는 값은 ` [['함부르크', 65], ['이스탄불', 195]]`이고, 이는 프랑크푸르트에서 함부르크는 65분, 프랑크푸르트에서 이스탄불은 195분이 소요되는 것을 의미한다.    
# ```python
# travel_time = {'인천' : [['이스탄불', 685], ['뮌헨', 790], ['헬싱키', 825], ['암스테르담', 815], ['프랑크푸르트', 830]], '함부르크': [['인천', 930], ['프랑크푸르트', 70], ['암스테르담', 70]], '이스탄불' : [['함부르크', 210], ['뮌헨', 140], ['헬싱키', 225], ['암스테르담', 200], ['인천', 620]], '뮌헨' : [['함부르크', 65], ['이스탄불', 150], ['프랑크푸르트', 60]], '헬싱키' : [['함부르크', 120], ['암스테르담', 155]], '암스테르담': [['함부르크', 65], ['이스탄불', 210]], '프랑크푸르트': [['함부르크', 65], ['이스탄불', 195], ['인천', 690]]}
# ```

# 인천에서 함부르크로 가는 경로의 최단시간과 그 경로를 보여주는 `Dijkstra_with_path()`함수를 정의하여라. 함수는 다음과 같은 형식으로 실행한다.
# ```
# Dijkstra_with_path(travel_time, 도시의개수, 출발도시, 도착도시)
# ```
# 즉, 이번 문제에서는 다음과 같이 함수를 실행한다.   
# ```
# Dijkstra_with_path(travel_time, 7, '인천', '함부르크')
# ```

# In[7]:


import folium

site = {'인천' : [37.4692, 126.451], '함부르크' : [53.5506, 9.99333], '이스탄불' : [41.0122, 28.976], '뮌헨' : [48.14, 11.58], '헬싱키' : [60.1699, 24.9384], '암스테르담' : [52.3738, 4.89093], '프랑크푸르트' : [50.1167, 8.68333]}
travel_time = {'인천' : [['이스탄불', 685], ['뮌헨', 790], ['헬싱키', 825], ['암스테르담', 815], ['프랑크푸르트', 830]], 
               '함부르크': [['인천', 930], ['프랑크푸르트', 70], ['암스테르담', 70]], 
               '이스탄불' : [['함부르크', 210], ['뮌헨', 140], ['헬싱키', 225], ['암스테르담', 200], ['인천', 620]], 
               '뮌헨' : [['함부르크', 65], ['이스탄불', 150], ['프랑크푸르트', 60]], 
               '헬싱키' : [['함부르크', 120], ['암스테르담', 155]], 
               '암스테르담': [['함부르크', 65], ['이스탄불', 210]], 
               '프랑크푸르트': [['함부르크', 65], ['이스탄불', 195], ['인천', 690]]}

m = folium.Map([46, 70], zoom_start = 3)

for i in site :
    folium.Marker(site[i], tooltip= i).add_to(m)

for i in travel_time :
    for j in travel_time[i] :
        folium.PolyLine(locations = [site[i], site[j[0]]]).add_to(m)
m


# :::{admonition} replit에서 `folium` 모듈의 지도   
# :class: info  
# 
# replit에서 `folium` 모듈의 지도를 보려면 `html` 파일로 저장해야 한다. 예를 들어, 위의 `m`을 `my_map`이라는 이름의 `html` 파일로 저장하려면, 아래와 같이 코드를 작성하면 된다.    
# ```python 
# >>> m.save('my_map.html')
# ```
# :::
# 
