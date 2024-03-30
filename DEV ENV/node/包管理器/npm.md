# NPM Cheat Sheet

npm 备忘单

### 查看版本

```bash
npm -v
npm --version
```

### 获取帮助

```bash
npm
npm help
```

### npm配置

```bash
npm config set <key>=<value>  # 设置某个配置
npm config get <key>          # 查看某个配置
npm config list               # 查看配置列表
npm config ls -l              # 查看npm所有默认配置
npm config delete <key>       # 删除配置
npm config edit               # 编辑配置
npm config fix                # 自动修复错误或者无效的配置
```

### 创建`package.json`

```bash
npm init
npm init -y 	# 创建package.json，并且使用默认配置
npm init --yes
```

### 安装包

```bash
# 中括号内为别名
npm i                               # npm@5之后，默认和 --save 一样
npm i --save package-name           # [-S,-P] 安装在 dependencies，这是默认设置     
npm i --save-dev package-name       # [-D] 安装在 devDependencies
npm i --save-optional package-name  # [-O] 安装在 optionalDependencies
npm i --no-save package-name        # 防止保存到dependencies
npm i --save-exact package-name     # [-E]安装一个确切版本的包
npm i --save-bundle package-name    # [-B] 安装在 bundleDependencies
npm i -g package-name               # 全局安装
npm i --production                  # 安装除了 devDependecies 之外的所有内容
```

> npm i
>
> TODO 版本 ^ ~

### 安装包名称（版本）

```json
// -
1.2.3 - 2.3.4 // 代表 >=1.2.3 <=2.3.4 之间的版本，包含左右版本。
// 如果结尾版本（右侧的版本）有空缺，将以 0 补位，并且递增非 0 版本号作为最大版本号：
1.2.3 - 2.3 // >=1.2.3 <2.4.0
1.2.3 - 2 // >=1.2.3 < 3.0.0
// * 
1.x // 代表 >=1.0.0 <2.0.0 (主版本限定为 1 的版本号)
1.2.x // 代表 >=1.2.0 <1.3.0 (主版本+次版本限定为 1.2 的版本号)
// ~ 以倒数第二个版本号+1为递增版本，可更新 [起始，结束) 范围内的所有版本号
~1.2.3 // 代表 >=1.2.3 <1.(2+1).0 即 >=1.2.3 <1.3.0
// ^
// 更新主版本号，如果版本号为 0，则往下取非 0 版本号递增，作为最大版本号。
^1.2.3 // 代表 >=1.2.3 <2.0.0
^0.2.3 // 代表 >=0.2.3 <0.3.0
```

> 参考：
>
> - [semver](https://github.com/npm/node-semver)
> - [运行npm install命令的时候会发生什么？](https://bbs.huaweicloud.com/blogs/348904?utm_source=luntan&utm_medium=bbs-ex&utm_campaign=other&utm_content=content)

### 更新包

```bash
npm update -g package-name
npm update --save package-name
npm update --save-dev package-name
```

### 删除包

```bash
npm uninstall -g package-name
npm uninstall -save package-name
npm uninstall --save-dev package-name
```

### 查看包

```bash
# 查看全局
npm list -g # 别名 npm ls
npm list -g --depth 0
npm list -g --depth 1
# 查看本地
npm list 
npm list --depth 0
npm list --depth 1
# 检查过时的依赖包
npm outdated
npm view packageName versions # 查看包的所有版本
```

### 常见问题处理

- 如果安装包存在版本冲突导致npm i 的时候报错怎么办？

```bash
rm -rf node_modules #删除 node_modules
npm cache clean --force #强制清楚npm缓存
npm i	# 重新安装一遍
```

其他参考：

- [npm audit](http://eux.baidu.com/blog/fe/npm%20aduit%E4%BA%8C%E4%B8%89%E4%BA%8B)

## npm 发布包

TODO
- 登陆/发包
- npmrc 文件配置
- 设置源
- 设置代理
- package.json 文件说明


---
## npm 仓库

- [verdaccio](https://github.com/verdaccio/verdaccio) 基于 nodejs 的轻量级私有仓库
- Nexus - 基于JAVA



## registry

- 官方 - https://registry.npmjs.org/
- 淘宝 - https://registry.npm.taobao.org/

```bash
npm i package --registry=URL # 单个包
npm config set registry URL # 设置
```