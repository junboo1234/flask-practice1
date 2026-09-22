# Flask 실행 정리

## 1. venv 실행

### PowerShell

.\venv\Scripts\Activate.ps1

### venv 종료

deactivate

## 2. Flask 디버그 모드 실행

### 코드로 실행

`app.py`

```python
if __name__ == "__main__":
    app.run(debug=True)
```

실행:

python app.py

### CMD / PowerShell 명령어로 실행

flask run --debug

또는 앱 파일을 직접 지정:

flask --app app run --debug
