## 패키지 관리의 필요성

 파이썬 뿐만 아니라 어떤 언어로 개발하느냐에 상관없이 여러 개의 프로젝트를 진행할 때는, 프로젝트에서 사용된 패키지나 라이브러리들의 버전이 명확히 제시되어 있는 것이 좋습니다. 해당 패키지들에 의존하고 있는 패키지들의 버전이 바뀜에 따라 원하지 않는 에러가 발생할 수 있으며, 잘 돌아가던 프로젝트나 프로그램도 문제가 발생할 수 있기 때문입니다.

 이러한 종속성 문제를 해결하기 위해서 Linux 운영체제에서는 apt, yum과 같은 패키지 관리 도구를 제공하고 있으며, 파이썬에서는 일반적으로 pip을 이용해 필요한 패키지를 설치합니다.

 하지만 파이썬은 다양한 버전을 제공하고 있으며(대표적으로 2.x, 3.x) 패키지들은 시간에 따라 변하며, 다른 환경에서도 똑같이 해당 프로젝트가 동작하도록 하기 위해서는 pip 만으로는 부족합니다.



## 파이썬의 사례

 파이썬에서는 이를 해결하기 위해 프로젝트 마다 서로 다른 가상환경(virtual environment)을 구축합니다. 일반적으로 virtualenv 패키지를 설치하여(3.x 버전에서는 이미 설치되어 있음) 파이썬 명령어를 통하여 가상환경을 만들게 됩니다.

-  가상환경 생성

```bash
$ mkdir python-virtual-environments && cd python-virtual-environments

# Python 2:
$ virtualenv env

# Python 3
$ python3 -m venv env

```

 다음과 같이 생성하게 된다면, env 라는 디렉터리가 생길 것이며, 디렉터리 내에는 파이썬 실행에 필요한 바이너리 파일이 생성됩니다.

 가상환경에서 실행하기 위해서는 "activate"라는 과정이 필요한데 명령어는 다음과 같으며, 커서 앞의 (env)를 통해 현재 어떤 가상환경에 있는지 확인할 수 있습니다.

```bash
# Shell
# 활성화(activate)
$ source env/bin/activate
(env) $
# 비활성화(deactivate)
(env) $ deactivate
$
```

 다음과 같이 프로젝트를 진행할 때 가상환경을 구축해서 사용하는 것이 일반적이며, 파이참(pycharm)에서는 프로젝트를 생성하면 자동으로 가상환경을 구축해줍니다.

- virtualenv 패키지 이후에 좀 더 향상된 패키지인 virtualwrapper가 나왔습니다. 이에 대해 알고 싶으시면 참조 링크를 참조하시면 됩니다.



## pipenv 패키지 소개

다음은 다양한 언어들의 패키지 관리 툴입니다.

- Node.js: yarn & npm (lockfile)
- PHP: Composer (lockfile)
- Rust: Cargo (lockfile)
- Ruby: Bundler (lockfile)
- *Python (old way): pip + virtualenv (no lockfile)*
- **Python (new way): pipenv (lockfile)**



 파이썬에서는 `pip freeze > requirements.txt` 으로 필요한 패키지들을 정의하고 가상환경 내에서 pip을 이용해 패키지들을 설치하는 것이 파이썬의 일반적인 절차로 사용되고 있습니다.

 pipenv를 사용하면 기존의 방식에서 좀 더 편하고 간편하면서 효율적으로 패키지 관리를 할 수 있을 것으로 보여집니다.



### 특징

- Pipfile, Pipfile.lock을 통한 패키지 관리
  - Pipfile을 통해 필요한 패키지를 쉽게 확인할 수 있으며, Pipfile.lock에서 의존성이 있는 패키지들을 확인할 수 있습니다.
- virtualenv와 virtualwrapper의 기능을 그대로 활용
  - 기존에는 가상환경이 설정된 디렉터리를 찾아 activate를 실행해야 했지만 Pipfile이 있는 디렉터리에서 pipenv 명령어로 쉽게 activate 할 수 있습니다.
  - 간단한 명령어로 Pipfile을 참조한 가상환경을 쉽게 생성 및 제거 가능
  - 생성된 가상환경 디렉터리의 위치는 $Home/.virtualenvs/[프로젝트]
- 배포 버전과 개발 버전의 구별가능
  - 개발 버전과 배포 버전에 필요한 패키지들을 따로 정의할 수 있습니다.
- Pipfile에 설치된 패키지들의 취약점 분석 가능



## pipenv 사용법

- 설치

```bash
pip install pipenv
```

- 명령어
  - 해당 프로젝트의 루트 경로에서 실행해야 함

```bash
# 파이썬 버전 정의
pipenv --python 3.6

# Pipfile에 정의된 패키지 설치(가상환경 설치)
pipenv install

# 배포 버전만 설치
pipenv install --deploy

# 가상환경 제거
pipenv --rm

# 가상환경 활성화
pipenv shell

# 패키지 설치
pipenv install <패키지>

# 특정 버전 설치
pipenv install django==1.4.2

# 패키지 설치(개발자 버전)
pipenv install <패키지> --dev

# 패키지 제거
pipenv uninstall <패키지>

# 취약점 검사
pipenv check

# 종속성 그래프로 보기
pipenv graph

# 가상환경 활성화 시키지 않고 명령어 실행시키기
pipenv run python -c 'import requests'

# 가상환경 파일 위치 확인
pipenv --venv
```



- 자세한 내용은 <a href="https://pipenv.readthedocs.io/en/latest/">링크</a> 참조



## 참조 링크

- virtualenvironment의 동작 : https://realpython.com/python-virtual-environments-a-primer/
- virtualenv 및 virtialwrapper : https://docs.python-guide.org/dev/virtualenvs/

- pipenv에 대해서 : https://medium.com/homeaway-tech-blog/simplify-your-python-developer-environment-aba90f32dddb
- pipenv 개발자의 공식 문서 : https://pipenv.readthedocs.io/en/latest/
- pipenv 깃 허브 페이지 : https://github.com/pypa/pipenv/