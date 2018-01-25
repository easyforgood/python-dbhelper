Python qiyue_db  —— 用来简化数据库操作的库
================

> **Only** Work on python3


## What's this

抽象了常用了db操作.

- 读取配置文件, 连接数据库 并获取数据库操作对象。

- 根据MySQL查询和执行命令

- 同时获取 MySQL 和 MongoDB的操作对象

MongoDB 数据库操作对象 请参考 Pymongo
MySQL 数据库操作 基于 MySQLDB进行了简单封装，提供 queryall 和 execsql 和 execmany 的方法。使用方法和MySQLDB类似。


## Install

- pip install -r requirements.txt

- python setup.py install


## How to

1. 创建 db.json. 参考 `./example/db.json `

2.  ` import dbhelper`. 获取 **dbhelper**.

  dbhelper 常见用法见 `./examples/db.py`


## Changelog


### V1.0.0 

- 通过配置文件的方式， 简化了dbhelper 的创建过程

- 简化了 查询数据 或者 导出文件的过程

