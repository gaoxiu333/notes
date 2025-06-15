---
title: React技术栈项目指引
jd_id: J10-20250520-1600
created: 2025-05-20 16:00
updated: 2025-06-16 00:00
type: moc
status: active
tags: [topic/react, topic/frontend, topic/engineering, topic/boilerplate]
---

# ⚛️ React 技术栈项目指引

## 📝 项目概述

构建现代化 React boilerplate，采用 Monorepo 架构和 Turborepo 管理，集成最佳实践和完整开发工具链。

## 📂 核心文件索引

### 📋 项目规划

- [[01-项目大纲|📊 项目大纲]] - 完整的项目规划和技术架构

### 🛠️ 技术配置

- [[04-TypeScript配置指南|⚙️ TypeScript配置]] - TS 配置详解和最佳实践
- [[05-TypeScript类型系统|🧩 类型系统]] - TypeScript 类型系统设计
- [[06-状态管理方案|🔗 状态管理]] - Zustand/React Query 等
- [[07-错误边界与异常处理|🛡️ 错误边界与异常处理]]
- [[08-路由与导航配置|🗺️ 路由与导航]]
- [[09-依赖管理与包管理指南|📦 依赖管理]]
- [[10-Mock数据与接口模拟|🔄 Mock 数据与接口模拟]]
- [[11-性能监控与埋点配置|📊 性能监控与埋点]]
- [[12-性能优化实践|⚡ 性能优化实践]]
- [[13-架构设计与目录结构|🏗️ 架构设计与目录结构]]
- [[14-设计系统与协作规范|🎨 设计系统与协作规范]]

### 📚 学习资源

- [[15-参考资源与学习材料|📚 参考资源]] - 系统化的学习材料和工具文档

## 🎯 中期目标 (2-4 周)

- [ ] 搭建实际的 boilerplate 代码
- [ ] 建立样式系统和组件库
- [ ] 配置完整的开发工具链
- [ ] 编写自动化脚本

## 🔗 相关链接

### 📚 技术资源

- [[../../30-resources/30-01-前端技术/00-MOC-前端技术|前端技术资源]] - React 技术栈资源库

### 💻 开发中心

- [[../../20-areas/20-03-前端开发/00-MOC-前端开发|前端开发]] - 前端技术学习中心

### 🏠 导航

- [[../../99-system/MOCs/00-快速导航|返回导航]] - 回到主导航页面

## 🌐 外部参考资源

### 🎯 优秀案例

- [bulletproof-react](https://github.com/alan2207/bulletproof-react) - React 架构最佳实践
- [Nextjs-Frontend-Boilerplate](https://github.com/shaadcode/Nextjs-Frontend-Boilerplate) - Next.js 项目模板
- [codeguide-starter-lite](https://github.com/CodeGuide-dev/codeguide-starter-lite) - AI 辅助开发配置参考

### 🛠️ 核心工具

- [Turborepo](https://turbo.build/repo) - Monorepo 构建工具
- [Next.js](https://nextjs.org/) - React 全栈框架
- [Shadcn UI](https://ui.shadcn.com/) - 现代 UI 组件库
- [Tailwind CSS](https://tailwindcss.com/) - 原子化 CSS 框架
- [pnpm](https://pnpm.io/) - 高效包管理器

### 📖 设计规范

- [Feature-Sliced Design](https://feature-sliced.github.io/documentation/) - 前端架构方法论

## 🔍 快速访问

### 按类型访问

- **配置相关**: [[04-TypeScript配置指南|TS配置]] | [[09-依赖管理与包管理指南|依赖管理]] | [[10-Mock数据与接口模拟|Mock配置]]
- **开发相关**: [[06-状态管理方案|状态管理]] | [[07-错误边界与异常处理|错误边界]] | [[08-路由与导航配置|路由导航]]
- **架构相关**: [[12-性能优化实践|性能优化]] | [[13-架构设计与目录结构|架构设计]] | [[14-设计系统与协作规范|设计系统]]
- **资源**: [[15-参考资源与学习材料|参考资料]]

## ⚙️ 维护指南

### 文件管理规则

1. 新增文件时必须在此 MOC 中添加对应索引
2. 保持文件命名规范：`XX-文件名.md`
3. 确保每个文件都有完整的 YAML 元数据
4. 定期检查和更新链接有效性

---

> [!info] 📈 项目进展
> **最近更新**: 2025-06-16 - 完成文档整理和重复文件清理，项目文档结构已优化  
> **下次检查**: 开始实际 boilerplate 代码开发
