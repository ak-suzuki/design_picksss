# DesignPicksssとは
Webサイトデザインの参考サイト集です。
以前WordPressを使用してWebサイトデザイン参考サイト集（ https://fooodesign.com/ ）を作成したが、これをPython化する。

## 目的
- 管理画面を作って機能を追加する🍔
    - サムネイル画像を今まで、Photoshopで手動でサイズ変更していたがそれをPythonにやってもらいたい
- AWSのお勉強🍕

## 開発環境構築手順

※ settingsファイル、envファイルが必要なので事前に渡す

1. docker-compose.yml がある階層で

    ```
    $ docker-compose -f docker-compose.yml build
    ```

2. docker-compose up する

    ```
    $ docker-compose -f docker-compose.yml up
    ```

3. 初回のmigrate
   - アプリケーションの中に入って
        ```
        $ docker exec -it django_app /bin/bash
        ```
    - migrate
        ```
        # python manage.py migrate
        ```


4. createsperuser 管理者ユーザ作成
  - アプリケーションの中に入ってる状態で
    ```
    $ python manage.py createsuperuser
    Username (leave blank to use 'xxx'): admin
    Email address: xxx@xxx
    Password:
    Password (again):
    Superuser created successfully.
    ```

5. Django admin画面から、5.の `Username` と `Password` でログインできればOK🎉
    - http://127.0.0.1:8000/admin/login/?next=/admin/

6. さぁ開発！！！

# マークダウンの書き方メモ

# タイトル1
## タイトル2
## タイトル3

- 箇条書き
  - 箇条書き
    - 箇条書き

```python
import os
```

```mermaid
flowchart TD
A(start)
A --> B[処理1]
B --> C(continue)
D(conotinue)
D --> E[続き]
E --> F(end)
