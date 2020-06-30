### Link
- [Effective Python Testing With Pytest - RealPython](https://realpython.com/pytest-python-testing/)
- [Pytest - tutorialspoint](https://www.tutorialspoint.com/pytest/index.htm)


```bash
# 파일명에 특정 키워드를 가진 테스트만 실행
pytest -k <substring> -v
pytest -k great -v

# 테스트 그룹화 (mark 사용)
pytest -m <markername> -v
pytest -m great

# 병렬로 테스트 실행
pytest -n <num>

# xml 결과 파일 생성
pytest -v --junitxml="result.xml"
```