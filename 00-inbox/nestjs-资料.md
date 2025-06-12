```bash
src/
├── core/                        # 📌 项目基础设施，和业务无关
│   ├── constants/               # 全局常量（如APP_NAME、TOKEN_HEADER）
│   ├── decorators/              # 通用装饰器
│   ├── exceptions/              # 全局异常封装
│   ├── filters/                 # 全局异常过滤器
│   ├── guards/                  # 全局/通用守卫
│   ├── interceptors/            # 全局拦截器（日志、耗时等）
│   ├── logger/                  # 全局 Logger 服务和模块
│   ├── middleware/              # 全局中间件
│   ├── pipes/                   # 全局管道
│   ├── utils/                   # 全局工具方法
│   ├── events/                  # 事件总线封装
│   └── jwt/                     # 基础 JWT 封装（encode/decode 工具）
│
├── shared/                      # 📌 跨 feature 复用的业务相关模块
│   ├── modules/                 
│   │   ├── auth/                # 认证模块
│   │   │   ├── dto/
│   │   │   ├── strategies/
│   │   │   ├── guards/
│   │   │   ├── services/
│   │   │   ├── controllers/
│   │   │   └── auth.module.ts
│   │   │
│   │   ├── scheduler/           # 定时任务模块
│   │   ├── event-bus/           # 事件发布订阅模块
│   │   └── ...
│   │
│   ├── services/                # 跨模块业务服务（如短信、邮件）
│   ├── constants/               # 业务相关常量、枚举
│   ├── interfaces/              # 通用业务接口定义
│   ├── utils/                   # 业务辅助工具（如订单时间处理）
│   ├── dto/                     # 通用 DTO（分页、查询）
│   └── validators/              # 通用验证器（手机号、邮箱）
│
├── features/                    # 📌 具体业务模块（按功能划分）
│   ├── user/
│   │   ├── dto/
│   │   ├── entities/
│   │   ├── services/
│   │   ├── controllers/
│   │   ├── repositories/
│   │   ├── use-cases/
│   │   └── user.module.ts
│   │
│   └── product/
│       └── ...
│
├── config/                      # 📌 配置相关
│   ├── app.config.ts
│   ├── database.config.ts
│   ├── jwt.config.ts
│   └── ...
│
├── database/                    # 📌 数据库相关
│   ├── migrations/
│   ├── seeds/
│   └── index.ts
│
├── main.ts                       # 应用启动入口
└── app.module.ts                 # 根模块
```

## 目录职责

|**📦 目录**|**📌 职责**|
|---|---|
|core/|项目底座基础设施，通用不依赖业务|
|shared/|跨 feature 复用业务相关功能模块|
|features/|独立业务功能模块，按功能域拆分|
|config/|所有项目配置|
|database/|数据迁移、初始种子数据|
|main.ts / app.module.ts|应用启动、全局模块注册|


## 常用命令

|**命令**|**简写形式**|**作用**|**示例**|
|---|---|---|---|
|nest generate module|nest g mo|生成模块|nest g mo users|
|nest generate controller|nest g co|生成控制器|nest g co users|
|nest generate service|nest g s|生成服务|nest g s users|
|nest generate gateway|nest g ga|生成 WebSocket 网关|nest g ga chat|
|nest generate middleware|nest g mi|生成中间件|nest g mi logger|
|nest generate interceptor|nest g in|生成拦截器|nest g in logging|
|nest generate guard|nest g gu|生成守卫|nest g gu roles|
|nest generate pipe|nest g pi|生成管道|nest g pi validation|
|nest generate filter|nest g f|生成异常过滤器|nest g f http-exception|
|nest generate resource|nest g res|生成带 CRUD 的资源模块|nest g res users|
|nest generate class|nest g cl|生成普通类|nest g cl utils/math-helper|
|nest generate interface|nest g interface|生成接口|nest g interface user|
|nest generate enum|nest g enum|生成枚举|nest g enum role|
|nest generate decorator|nest g d|生成自定义装饰器|nest g d roles|

## 常用参数

|**参数**|**作用**|**示例**|
|---|---|---|
|--no-spec|不生成测试文件|nest g s users --no-spec|
|--flat|不创建单独目录，直接放在当前目录|nest g s auth --flat|
|--type|指定资源类型（在 resource 中用）|nest g res product --type graphql|





## 数据库

1. 使用本地docker
2. 使用线上免费：https://dev.to/prisma/how-to-setup-a-free-postgresql-database-on-heroku-1dc1