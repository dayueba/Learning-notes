# 用flask开发应用

## 项目结构


- 功能式架构
    ```
    app/
        blueprints/
            - __init__.py
            - auth.py
            - main.py
        forms/
            - __init__.py
            - auth.py
            - main.py
        static/
        templates/
            - auth/
            - main/
            - base.html
        ___init__.py
    ```
- 分区式架构
    ```
    app/
        main/
            - __init__.py
            - views.py
            - forms.py
            - templates/
            - static/
        auth/
            - __init__.py
            - views.py
            - forms.py
            - templates/
            - static/
        __init__.py
    ```
- 混合式架构
    ```
    app/ 
        main/
            - __init__.py
            - views.py
            - forms.py
        auth/
            - __init__.py
            - views.py
            - forms.py
        templates/
            - auth/
            - main/
        static/
        __init__.py
    ```

如果程序各个功能之间的联系较为紧密则采用功能式架构

反之则适合使用分区式架构


自定义命令
    @app.cli.command()

客户端 http请求 -> web服务器 -> wsgi 将请求数据转换为flask能使用的Python数据
flask 生成响应 -> wsgi 转为为http响应 -> web服务器发送 -> 客户端