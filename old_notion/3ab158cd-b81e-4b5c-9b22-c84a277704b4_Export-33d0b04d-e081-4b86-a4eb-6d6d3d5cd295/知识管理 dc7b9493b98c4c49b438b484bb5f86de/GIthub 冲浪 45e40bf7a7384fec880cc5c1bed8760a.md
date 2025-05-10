# GIthub 冲浪

## **搜索关键词**

- awesome
- learn XXX in the hard way
- learn by doing
- boilerplate - 入门套件/样板
- starter - 启动机
- roadmap
- Useful NVM commands

## **Github 个人预览页面**

- [参考1](https://github.com/maurodesouza/profile-readme-generator)
- [参考2](https://gprm.itsvg.in/)

> 生成预览关键字： GitHub Profile README Generator
> 

## **发现项目**

- 当前热门主题：[https://github.com/topics](https://github.com/topics)
- 当你对某个主题感兴趣时：`github.com/topics/<topic>`
- [在 GitHub 上寻找为开源做出贡献的方法](https://docs.github.com/en/get-started/exploring-projects-on-github/finding-ways-to-contribute-to-open-source-on-github)

## **fork**

如何同步？

1. github的WebUI版本，点击同步
2. 通过git同步：先关联上游仓库，然后fetch更新，最后合并到目标分之上。

```
git remote add upstream https://github.com/ORIGINAL-OWNER/Spoon-Knife.git
git rempte -v
git fetch upstream
git checkout main
git merge upstream/main

```

## **pull request**