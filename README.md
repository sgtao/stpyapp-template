# stpyapp-template
[streamlit](https://streamlit.io/)のアプリ開発するためのテンプレートを作ってみる

## コンテンツ
- サンプルコード（[streamlit-example](https://github.com/streamlit/streamlit-example)）を追加

## Usage
- [poetry cli](https://cocoatomo.github.io/poetry-ja/cli/)を利用する

### Setup
```sh
poetry install
poetry shell
```

### コマンド一覧
```sh
$ task --list
start        streamlit run src/main.py
test         pytest tests
test-cov     pytest tests --cov --cov-branch -svx
test-repo    pytest tests --cov --cov-report=html
format       black --line-length 79 src
lint         flake8 src
check-format black整形とflake8チェックを実行
```

### Start as local service
```sh
# on poetry shell
# streamlit hello
# streamlit run src/main.py
task start
# Local URL: http://localhost:8501
```


### format and lint check
```sh
# task format
# task lint
task check-format
```


### Test with `pytest`
- [streamlitのテスト手法](https://docs.streamlit.io/develop/concepts/app-testing/get-started)を参考にテストを実施
```sh
# on poetry shell
# pytest tests/test_main.py
task test
```

### Test coverage

#### show c1 coverage
```sh
# on poetry shell
task test-cov
```

#### output HTML coverage report
```sh
# on poetry shell
task test-repo
```


## License
Apache-2.0 license

