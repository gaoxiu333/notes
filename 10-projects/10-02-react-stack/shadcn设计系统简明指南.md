# Shadcn Token 使用指南

## 页面层次结构

**background/foreground** - 页面最基础的背景和文字色

**card/card-foreground** - 内容卡片的背景和文字色，比页面背景稍有层次感

**popover/popover-foreground** - 弹出层（下拉菜单、提示框）的背景和文字色

> background = 背景色
> foreground = 这个背景上应该用什么颜色的文字

## 交互元素

**primary/primary-foreground** - 主要操作按钮，最重要的交互元素

**secondary/secondary-foreground** - 次要操作按钮，重要性低于 primary

**accent/accent-foreground** - 强调元素，用于突出显示某些内容

**destructive/destructive-foreground** - 危险操作，如删除、警告等

## 辅助信息

**muted/muted-foreground** - 弱化信息，用于说明文字、次要内容

**border** - 分割线、边框颜色

**input** - 表单输入框的边框颜色

**ring** - 键盘焦点时的外围光环颜色

## 专门用途

**chart-1 到 chart-5** - 数据可视化专用的 5 种颜色，用于图表中的不同数据系列

**sidebar 系列** - 侧边栏组件专用颜色，包括 sidebar、sidebar-primary、sidebar-accent 等

## 使用原则

**配对使用** - 每个背景色都有对应的前景色，确保文字可读性

**语义化** - 根据元素的功能选择对应的 token，而不是根据颜色外观

**层次感** - background → card → popover 体现了 UI 的层次关系

**一致性** - 相同功能的元素使用相同的 token，保持视觉统一

## 明暗模式

所有 token 都有明暗两套值，切换主题时自动生效，无需额外处理

## 什么时候用什么

- 页面背景用 background
- 内容容器用 card
- 弹出元素用 popover
- 主要按钮用 primary
- 次要按钮用 secondary
- 说明文字用 muted-foreground
- 危险操作用 destructive
- 图表数据用 chart 系列
