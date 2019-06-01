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

如果程序各个功能之间的联系较为紧密则采用功能式架构<br>
反之则适合使用分区式架构