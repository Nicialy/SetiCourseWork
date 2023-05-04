# Backend сервис


## Стэк:
    FastAPI
    python3.10+

1. Клонируем
```bash
foo@bar:~$ git clone gihub-link
```
2. Заходим в папку
```bash
foo@bar:~$ cd Backend
```
3. Создаем вертуальное пространство
```bash
foo@bar:~$ python  -m venv .venv
```
3.1 Активируем venv - для Linux и MacOS.
```bash
foo@bar:~$ source venv/bin/activate
```
4. Устанавливаем библиотеки
```bash
foo@bar:~$ pip install -r requirements.txt
```
5. Запускаем бэк
```bash
foo@bar:~$ python main.py
```

## Cмена порта и хоста

### Откройте main.py и измените 

```python
import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8080)
```

