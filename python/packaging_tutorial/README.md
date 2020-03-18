### Link
- [Packaing Python Projects](https://packaging.python.org/tutorials/packaging-projects/)




## Commands
### Generating distribution archives
```bash
# upgrade buildtools
python3 -m pip install --user --upgrade setuptools wheel

# build package to dist directory
python setup.py sdist bdist_wheel
```



### Uploading the distribution archives

```bash
# install twine package
python3 -m pip install --user --upgrade twine

# dist upload
python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```



### Installing your newly uploaded package

```bash
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps example-pkg-YOUR-USERNAME-HERE
```

