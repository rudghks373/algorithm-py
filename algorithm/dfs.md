## DFS 알고리즘 구현

![image](https://user-images.githubusercontent.com/32234263/153432717-6e1fc2e0-d1f7-4b43-b1a4-e29551a360a2.png)

> 자료구조 스택과 큐를 활용함
> need_visit 스택과 visited 큐, 두 개의 자료 구조를 생성
> BFS 자료구조는 두 개의 큐를 활용하는데 반해, DFS 는 스택과 큐를 활용한다는 차이가 있음을 인지해야 함

```python
graph = dict()

graph['A'] = ['C', 'B']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

def dfs(graph,start_node):
    visited, need_visit = list(), list()
    need_visit.append(start_node)
    
    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    return visited

dfs(graph, 'A')
```
