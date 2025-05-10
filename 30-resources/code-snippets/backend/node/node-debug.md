---
title: node-debug
created: 2025-02-16 14:54
updated: 2025-02-16 14:56
type: resource
status: active
schema: v1
tags: [source/notion, topic/backend/nodejs, lang/javascript, topic/debug]
---

# Node Debug

最近使用nodejs运行项目，莫名其妙开启自动调试，也不知道在哪里关闭

最后终于找到了

原因是之前配置 vs code 调试 React 源码时，让 vs vode 在系统中设置了一个环境变量，如下：

```bash
echo $NODE_OPTIONS
## 删除
unset NODE_OPTIONS
```

`$NODE_OPTIONS` 是 **VS Code** 调试器为了能够调试 Node.js 进程而自动设置的，它会加载 bootloader.js，并且可能会附加 --inspect 或其他调试相关选项，导致调试器自动启动 