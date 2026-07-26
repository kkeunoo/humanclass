---
title: CSS Position과 Overflow
category: CSS
last_updated: 2026-07-27
status: Active
---

# CSS Position과 Overflow


## position

```css
.card { position: relative; }
.badge { position: absolute; top: 10px; right: 10px; }
```

- static: 기본 흐름
- relative: 원래 위치를 기준으로 이동하며 absolute 자식의 기준이 될 수 있다.
- absolute: 가장 가까운 position 지정 조상을 기준으로 배치된다.
- fixed: 브라우저 화면 기준으로 고정된다.
- sticky: 스크롤 조건에서 지정 위치에 붙는다.

## overflow

```css
.description {
  width: 260px;
  height: 100px;
  overflow: auto;
}
```

- visible: 넘친 내용이 보인다.
- hidden: 넘친 부분을 자른다.
- scroll: 항상 스크롤 영역을 만든다.
- auto: 필요할 때만 스크롤을 만든다.

## 주의사항

absolute 요소는 일반 문서 흐름에서 빠지므로 부모 높이가 자동으로 늘지 않을 수 있다.
