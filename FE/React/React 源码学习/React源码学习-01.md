## 起步

从 Github 下载 React 源码，先了解源码的目录结构：

- [React源码目录文件构成](https://github.com/puxiao/notes/blob/master/React%E6%BA%90%E7%A0%81%E7%9B%AE%E5%BD%95%E6%96%87%E4%BB%B6%E6%9E%84%E6%88%90.md)
- [官方 如何贡献](https://legacy.reactjs.org/docs/how-to-contribute.html)

注意：

`ReactDOM.render` 已经被在最新版本中被弃用，请使用` ReactDOM.createRoot` 

![img](https://jser.dev/static/react-internals-overview-light.png)

### Debug

##### HTML 元素断点

Chrome支持在特定HTML元素上设置断点， 当该元素属性发生变化时，断点回发生变化；对调试网页中特定元素的样式或者属于发生变化非常有用；支持以下三种断点

- Element break on
  - Subtree modifications
  - Attribute modifications
  - node removel

**用法：**打开控制台->Element->右键要断点的元素->break on ->勾选你要调试的选项（支持多选）





