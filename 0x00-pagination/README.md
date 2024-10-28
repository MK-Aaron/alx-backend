## 0x00. Pagination
`Back-end`
  

### Resources
###### Read or watch:

- [REST API Design: Pagination](https://www.moesif.com/blog/technical/api-design/REST-API-Design-Filtering-Sorting-and-Pagination/#pagination)
- [HATEOAS](https://en.wikipedia.org/wiki/HATEOAS)

### Learning Objectives
<p>At the end of this project, you are expected to be able to explain to anyone, without the help of Google:</p>

- How to paginate a dataset with simple page and page_size parameters
- How to paginate a dataset with hypermedia metadata
- How to paginate in a deletion-resilient manner


Tasks
###### 0. Simple helper function

Write a function named `index_range` that takes two integer arguments `page` and `page_size`.

<p>The function should return a tuple of size two containing a start index and an end index corresponding to the range of indexes to return in a list for those particular pagination parameters.</p>

<p>Page numbers are 1-indexed, i.e. the first page is page 1.</p>

```
bob@dylan:~$ cat 0-main.py
#!/usr/bin/env python3
"""
Main file
"""

index_range = __import__('0-simple_helper_function').index_range

res = index_range(1, 7)
print(type(res))
print(res)

res = index_range(page=3, page_size=15)
print(type(res))
print(res)

bob@dylan:~$ ./0-main.py
<class 'tuple'>
(0, 7)
<class 'tuple'>
(30, 45)
bob@dylan:~$
```
Repo:

GitHub repository: alx-backend
Directory: 0x00-pagination
File: 0-simple_helper_function.py
 
