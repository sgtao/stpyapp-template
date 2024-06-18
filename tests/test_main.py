# tests/test_main.py
from streamlit.testing.v1 import AppTest

def test_show_title():
    """show title"""
    at = AppTest.from_file("src/main.py")
    at.run(timeout=10)  # タイムアウトを10秒に設定
    assert at.title[0].value == "Hello World"
