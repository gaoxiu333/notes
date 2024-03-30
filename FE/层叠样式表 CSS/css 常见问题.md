
##  高度`0=>auto`如何使用过度动画

1. 固定`height`
2. 借助js实现过渡动画
3. `max-height`
4. `grid`

```css
// max-height
.accordion-body {
  max-height: 0;
  transition: 500ms max-height ease;
}

.accordion:hover .accordion-body {
  max-height: 200px;
}
// grid
.accordion-body {
  display: grid; 
  grid-template-rows: 0fr;
  transition: 250ms grid-template-rows ease;
}

.accordion:hover .accordion-body {
  grid-template-rows: 1fr;
}

.accordion-body > div {
  overflow: hidden;
}
```

