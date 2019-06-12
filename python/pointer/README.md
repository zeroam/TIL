## Pointers in Python

### 참조링크

- [Pointers in Python: What's the Point?](https://realpython.com/pointers-in-python/)



### Objects in Python

- 파이썬에서는 모든 것이 객체임
  - isinstance() 메소드를 사용해 확인해 볼 수 있음
  - 숫자, 리스트형, 함수 모두 객체

```python
>>> isinstance(1, object)
True
>>> isinstance(list(), object)
True
>>> def foo():
...     pass
...
>>> isinstance(foo, object)
True
```

- 객체가 가지고 있는 최소한의 데이터
  - [Reference count](<https://docs.python.org/3/library/sys.html#sys.getrefcount>)
    - [파이썬에서의 메모리 관리](<https://realpython.com/python-memory-management/>)
  - Type
    - 객체 타입
  - Value
    - 실제 값



### Immutable vs Mutable Objects

1. Immutable objects : 바뀔 수 없음
2. Mutable objects : 바뀔 수 있음

| Type        | Immutable? |
| ----------- | ---------- |
| `int`       | Yes        |
| `float`     | Yes        |
| `bool`      | Yes        |
| `complex`   | Yes        |
| `tuple`     | Yes        |
| `frozenset` | Yes        |
| `str`       | Yes        |
| `list`      | No         |
| `set`       | No         |
| `dict`      | No         |

- 원시타입(primitive type)은 일반적으로 바뀌지 않음(immutable)
- id()는 객체의 주소를 반환함
- is 는 객체의 메모리 주소가 같으면 True를 반환함

```python
# 값을 수정하는 것으로 보이지만 실제로는 새로운 객체를 대입하는 것(메모리 주소가 바뀜)
>>> x = 5
>>> id(x)
1672242336
>>> x += 1
>>> x
6
>>> id(x)
1672242352

# str 타입 또한 바뀌지 않음(immutable)
>>> s = "real_python"
>>> id(s)
55892112
>>> s += "_rocks"
>>> s
'real_python_rocks'
>>> id(s)
60589840

# 바뀌지 않는(immutable) 타입을 바꾸려 하면 에러 발생
>>> s[0] = 'R'
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    s[0] = 'R'
TypeError: 'str' object does not support item assignment
    
# list 자료형의 경우 값을 바꿀 수 있음(mutable)
# 주소 값도 바뀌지 않음
>>> my_list = [1, 2, 3]
>>> id(my_list)
55395072
>>> my_list.append(4)
>>> my_list
[1, 2, 3, 4]
>>> id(my_list)
55395072
>>> my_list[0] = 0
>>> my_list
[0, 2, 3, 4]
>>> id(my_list)
55395072
```



### Understanding Variables

- 파이썬 변수는 C 또는 C++ 변수와 근본적으로 다름
  - 실질적으로, 파이썬은 변수를 가지고 있지 않음
  - 파이썬은 이름(names)을 가지고 있지, 변수(variable)을 가지고 있지 않음



#### Variables in C

```c
int x = 2337;
```

1. integer 를 위한 메모리를 할당함
2. 2337 값을 메모리 공간에 대입함
3. x 가 그 값을 가리킴

![In-Memory representation of X (2337)](https://files.realpython.com/media/c_memory1.334fe7c13e82.png)

```c
x = 2338;
```

- x 변수에 새로운 값을 대입함
  - 이전 값을 덮어 씀(overwrite)
  - 변수는 변경 가능(mutable)하다는 의미
  - x 의 메모리 주소는 바뀌지 않고 값만 바뀜

![New In-Memory representation of X (2338)](https://files.realpython.com/media/c_memory2.14d638daf718.png)

```c
int y = x;
```

- 변수 y 에 x 를 대입
  - y 를 위한 메모리 공간 생성
  - x 의 값을 y의 메모리 공간에 복사
  - x 와 y 는 다른 메모리 주소를 가지고 있음 -> y 의 값을 변경하더라도 x에는 영향을 주지 않음

![In-Memory representation of X (2338) and Y (2338)](https://files.realpython.com/media/c_memory3.5afe110faf4d.png)

```c
y = 2339;
```

- x와 y는 가리키는 메모리 주소가 다르기 떄문에 서로 영향을 받지 않음

![Updated representation of Y (2339)](https://files.realpython.com/media/c_memory4.45a45dbbfaab.png)



#### Names in Python

- 파이썬은 변수(variables)가 아닌 이름(names)을 가지고 있음

```python
>>> x = 2337
```

1. PyObject 생성
2. PyObject의 typecode를 integer로 설정
3. PyObject의 값(value)를 2337로 설정
4. x 라는 이름 생성
5. x를 새로운 PyObject로 향하게 함
6. PyObject의 refcount를 1 증가

- PyObject는 파이썬의 object와 다름
  - CPython에만 해당되며 Python 객체의 기본 구조를 나타냄

![Python In-Memory representation of X (2337)](https://files.realpython.com/media/py_memory1.2b6e5f8e5bc9.png)

- x에 새로운 값 대입
  - C 와는 다르게 동작
  - 아래 명령어는 대입이라기 보다는 이름 x를 참조에 바인딩 하는 것
  - reference count가 0이 된 객체는 garbage collector에 의해 나중에 정리됨

```python
>>> x = 2338
```

1. 새로운 PyObject 생성
2. PyObject의 typecode를 integer로 설정
3. PyObject의 값(value)를 2338로 설정
4. x가 새로운 PyObect를 향하게 함
5. 새로운 PyObject의 refcount를 1 증가
6. 기존의 PyObject의 refcount를 1 감소

![Python Name Pointing to new object (2338)](https://files.realpython.com/media/py_memory2.99bb432c3432.png)

```python
>>> y = x
```

- 새로운 이름을 가지지만 새로운 객체를 생성하지는 않음

![X and Y Names pointing to 2338](https://files.realpython.com/media/py_memory3_1.ea43471d3bf6.png)

```python
>>> y is x
True
```

- y와 x는 같은 주소를 갖는 같은 객체
  - 위 객체는 immutable이기 때문에 값을 변경할 수 없음
  - 값을 변경하면 새로운 객체를 참조하게 됨

```python
>>> y += 1
>>> y is x
False
```

![x name and y name different objects](https://files.realpython.com/media/py_memory4.0a15e8415a15.png)

- ##### 요약

  - 파이썬은 변수를 할당하는 것이 아니라 이름을 참조에 바인딩 하는 것
  - in Python, you don’t assign variables. Instead, you bind names to references.



#### A note on Intern Objects in Python

```python
>>> x = 1000
>>> y = 1000
>>> x is y
False
# .py 파일로 실행할 때는 True

>>> x = 1000
>>> y = 499 + 501
>>> x is y
False
# .py 파일로 실행할 때는 True
```

1. 파이썬 객체 생성(1000)
2. x 에 객체 대입
3. 파이썬 객체 생성(499)
4. 파이썬 객체 생성(501)
5. 객체 2개 더하기
6. 새로운 객체 생성(1000)
7. y에 객체 대입

- 파일로 실행하면 True가 되는 이유
  - 파이썬은 객체의 특정 하위 집합을 미리 만들고, 일상적으로 사용하기 위해 전역 네임 스페이스에 유지하기 때문
    - interned object
    - 정수 -5~256
    - ASCII 문자, 숫자, underscore(_)
    - 20 자 이내의 문자열(string)

```python
# 20자 이내의 문자열(interned object) - 같은 주소
>>> s1 = "realpython"
>>> id(s1)
51567656
>>> s2 = "realpython"
>>> id(s2)
51567656
>>> s1 is s2
True

# ASCII 문자, 숫자, _ 가 아닌 경우(ex. !) - 다른 주소
>>> s1 = "Real Python!"
>>> s2 = "Real Python!"
>>> s1 is s2
False
```



### Simulating Pointers in Python

- 파이썬에서 포인터 기능의 이점을 활용하는 방법

1. mutable 타입을 포인터로 사용
2. custom 파이썬 객체를 사용



#### Using Mutable Types as Pointer

- C

```c
// 함수
void add_one(int *x)
{
    *x += 1;
}

// 메인 함수
#include <stdio.h>

int main(void)
{
    int y = 2337;
    printf("y = %d\n", y);
    add_one(&y);
    printf("y = %d\n", y);
    return 0;
}

// 결과
y = 2337
y = 2338
```

- Python
  - 실제로 파이썬에서 포인터는 존재하지 않음
  - list 형 같은 mutable 객체를 사용하여 값 변경 가능

```python
>>> def add_one(x):
...     x[0] += 1
...
>>> y = [2337]
>>> add_one(y)
>>> y[0]
2338

# 튜플은 immutable 타입이기 때문에 에러 발생
>>> z = (2337,)
>>> add_one(z)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    add_one(z)
  File "<pyshell#55>", line 2, in add_one
    x[0] += 1
TypeError: 'tuple' object does not support item assignment
    
# 사전형 사용하기
>>> counters = {"func_calls": 0}
>>> def bar():
...     counters["func_calls"] += 1
...
>>> def foo():
...     counters["func_calls"] += 1
...     bar()
...
>>> foo()
>>> counters["func_calls"]
2
```



#### Using Python Objects

- 함수 호출 횟수 카운팅 예제
  - 사전형을 이용하는 것은 포인터와 같이 동작시킬 수 있는 좋은 방법
  - _metrics는 멤버 변수
    - @property를 통해 해당 변수에 접근하는 것이 좋은 방법
  - inc_func_calls(), inc_cat_pics() 함수
    - metrics 값을 변경하는 메서드
    - 포인터를 수정하는 것처럼 수정하는 클래스가 생성됨

```python
class Metrics(object):
    def __init__(self):
        self._metrics = {
            "func_calls": 0,
            "cat_pictures_served": 0
        }

    @property
    def func_calls(self):
        return self._metrics["func_calls"]

    @property
    def cat_pictures_served(self):
        return self._metrics["cat_pictures_served"]

    def inc_func_calls(self):
        self._metrics["func_calls"] += 1

    def inc_cat_pics(self):
        self._metrics["cat_pictures_served"] += 1

    
# @property는 해당 메서드를 속성으로서 접근할 수 있도록 해줌
>>> metrics = Metrics()
>>> metrics.func_calls
0
>>> metrics.cat_pictures_served
0

# metric 값 변경
>>> metrics = Metrics()
>>> metrics.inc_func_calls()
>>> metrics.inc_func_calls()
>>> metrics.func_calls
2
```





























-----

### 참조

- [@property란?](<https://www.machinelearningplus.com/python/python-property/>)
  - 메소드 호출할 때 ( )를 붙이지 않고 값을 불러올 수 있는 기능 - getter 기능
  - @(property를 붙인 메서드).setter
    - 위의 데코레이터를 통해 setter 를 설정할 수 있음
  - @(property를 붙인 메서드).deleter
    - 위의 데코레이터를 통해 deleter를 설정할 수 있음
  - 언제 사용하나?
    - 속성 하나가 변경될 때 다른 속성이 변경되어야 할 때

```python
class Person():
    def __init__(self, firstname, lastname):
        self.first = firstname
        self.last = lastname

    @property
    def fullname(self):
        return self.first + ' ' + self.last

    @fullname.setter
    def fullname(self, name):
        firstname, lastname = name.split()
        self.first = firstname
        self.last = lastname

    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None

    def email(self):
        return f'{self.first}.{self.last}@email.com'


if __name__ == "__main__":
    person = Person('selva', 'prabhakaran')
    print(person.fullname)  #> selva prabhakaran
    print(person.first)  #> selva
    print(person.last)  #> prabhakaran

    # Setting fullname calls the setter method and updates person.first and person.last
    person.fullname = 'velu pillai'

    # Print the changed values of `first` and `last`
    print(person.fullname) #> velu pillai
    print(person.first)  #> pillai
    print(person.last)  #> pillai

    # fullname deleter 호출 self.first, self.last를 지움
    del person.fullname
    print(person.first) #> None
    print(person.last)  #> None
```

























