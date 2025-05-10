# python 最佳实践

## python 基础最佳实践

下面的网址是一个python最佳实践指南

https://pythonguidecn.readthedocs.io/zh/latest/writing/logging.html

https://github.com/mongodb-developer/pymongo-fastapi-crud/tree/main

## FastApi 最佳实践

[https://github.com/zhanymkanov/fastapi-best-practices](https://github.com/zhanymkanov/fastapi-best-practices)

上面最佳实践的模版：https://github.com/fastapi/full-stack-fastapi-template/tree/master?tab=readme-ov-file

全栈最佳实践：https://github.com/fastapi/full-stack-fastapi-template/tree/master?tab=readme-ov-file

https://github.com/mongodb-developer/python/tree/main/fastapi-best-practices

- 目前先尝试一下第一个，循序渐进到全栈 最佳实践（全栈最佳实践包含的东西过多）。

## 技术栈对比

- 包管理器
    - `pipx`
    - `uv`
        - 小众单更轻量级，它类似于 `conda`
    - `poetry` 目前选用，感觉是主流
        - `pip install poetry`
- 代码格式工具
    - `ruff`

## 包管理器

[https://github.com/astral-sh/uv](https://github.com/astral-sh/uv)