## 滚动条

- 锚点
- css 锚点动画

```
    scroll-padding-top: 5rem/* 80px */;
  scroll-behavior: smooth;

```

- Js 实现

```js
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        const target = document.querySelector(this.getAttribute('href'));
        const targetOffset = target.getBoundingClientRect().top + window.pageYOffset;
        const currentOffset = window.pageYOffset;
        const scrollOffset = targetOffset - currentOffset;

        window.scrollBy({
            top: scrollOffset,
            behavior: 'smooth'
        });
    });
});
```

