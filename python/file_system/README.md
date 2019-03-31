## FileSystem

### 참조링크

- [10 Python File System Methods You Should Know](<https://towardsdatascience.com/10-python-file-system-methods-you-should-know-799f90ef13c2>)



#### os, shutil 모듈

- os 모듈은 OS와 상호작용하는 주된 파이썬 모듈
- os 모듈으로 디렉토리를 만들고, shutil 모듈으로 복사하거나 이동



#### pathlib 모듈이 새로 추가됨

- 파일을 파싱하거나 파일 경로를 활용하는데 장점이 있음



#### 10 File System Methods

- **Get Info**

  - `os.getcwd()`
    - shell 커맨드 : pwd
    - 현재 작업 디렉토리 경로를 string으로 돌려줌
  - `os.listdir()`
    - shell 커맨드 : ls
    - 현재 작업경로의 파일들을 string의 리스트 형태로 돌려줌
  - `os.walk("starting_directory_path")`
    - 현재 디렉터리, 서브 디렉터리, 파일 경로를 반환하는 제너레이터(generator)를 반환함

  ```python
  import os
  
  cwd = os.getcwd()
  
  for dir_path, dir_names, file_names in os.walk(cwd):
      for f in file_names:
          print(f)
  ```

  

- **Change Things**
  - 파일 시스템을 이용한 코드를 짤 때에는 try-except(에러처리)를 포함한 코드를 짜는 것이 좋음
  - `os.chdir("/absolute/or/relative/path")`
    - shell 커맨드 : cd
    - 현재 작업 경로를 이동함
  - `os.path.join()`
    - path를 생성함
    - 일반적인 string 연결 되신 이 메소드를 사용하는 것이 좋음
  - `os.makedirs("dir1/dir2")`
    - shell 커맨드 : mkdir -p
    - 디렉터리를 생성함
  - `shutil.copy2("source_file_path", "destination_directory_path")`
    - shell 커맨드 : cp
    - 파일이나 디렉터리를 복사함
  - `shutil.move("source_file_path", "destination_directory_path")`
    - shell 커맨드 : mv
    - 파일이나 디렉터리를 옮김
  - `os.remove("my_file_path")`
    - shell 커맨드 : rm
    - 파일을 삭제함
  - shutil.rmtree("my_directory_path")
    - shell 커맨드 : rm - rf
    - 디렉터리와 디렉터리에 있는 모든 파일을 삭제함