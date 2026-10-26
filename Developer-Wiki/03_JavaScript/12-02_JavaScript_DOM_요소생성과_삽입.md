# 12-02. 요소 생성·삽입 — 표 한 행을 직접 조립하기

[JavaScript 목차](README.md) · [이전: 콘텐츠](12_JavaScript_DOM_콘텐츠생성과_스타일조작.md) · [다음: 스타일·퀴즈](12-03_JavaScript_DOM_스타일과_퀴즈.md)

양쪽 `12_dom_content.html`의 createElement와 삽입 실습이다. **요소 생성 → 내용 설정 → 부모에 연결**을 하나씩 구분한다.

<!-- chapter-toc -->

- [1. createElement만으로 화면에 나타나지는 않는다](#section-1)
- [2. 자식 앞뒤와 형제 앞뒤](#section-2)
- [3. tr 안에 td를 넣기](#section-3)
- [4. rows 배열을 다섯 행으로 만들기](#section-4)
- [5. 문자열을 앞에 붙이면 행 순서가 뒤집힌다](#section-5)
- [6. 복습](#section-6)
- [추가로 알면 좋은 것](#section-7)

<a id="section-1"></a>

## 1. createElement만으로 화면에 나타나지는 않는다

### 강사님 코드

출처: `teacher/workspace_html/javascript/12_dom_content.html` 126–146행 · **원본 발췌**

```javascript
        // DOM 요소 생성
        const div = document.createElement('div') // <div></div>
        console.log(div)
        // <div id="lol"></div>
        div.setAttribute('id', 'lol')
        // <div id="lol">정글차이</div>
        div.innerText = '정글차이'
        console.log(div)

        div.setAttribute('style', 'color:red;')

        const log = document.querySelector('#log')
        // append
        // 마지막 자식 요소로 추가된다
        // 글씨도 넣을 수는 있다
        log.append(div)
        log.append('<h1>abcd</h1>')

        // 같은 객체를 두번 append할 때 조심!!
        // 같은 객체는 이동된다
        log.append(div)
```

### 내 코드

출처: `me/workspace_html/javascript/12_dom_content.html` 142–159행 · **원본 발췌**

```javascript
            const div = document.createElement('div') // <div></div>
            // 주소가 힙 영역에 있는데, 그 사이에 빠르게 값을 찾아오기 때문에 같아보임
            console.log(div)
            // <div id="lol"></div>
            div.setAttribute('id','lol')
            // <div id="lol">정글차이</div>
            div.innerText = '정글차이'
            console.log(div)
        
            div.setAttribute('style','color: red;')

            const log = document.querySelector('#log')
            // append는 마지막 자식 요소로 붙여넣을 수 있음
            // 글씨도 넣을 수는 있지만 자주 쓰이지 않는다
            log.append(div)
            log.append('<h1>abcd</h1>')
            // 같은 객체는 두 번 사용하면 마지막에 사용한 곳으로 이동됨
            log.append(div)
```

둘 다 div 요소를 만들고 id·글자·색상을 지정한 후 #log에 연결한다. createElement는 이미 실제 DOM 요소 객체를 만든다. 내 주석의 ‘가상 DOM을 append해야 실체화’라는 설명은 **문서에 아직 연결되지 않은 요소를 append로 연결한다**로 교정한다. 프레임워크의 가상 DOM과 혼동하지 않는다.

`log.append('<h1>abcd</h1>')`는 문자열을 텍스트로 추가한다. 이때 h1 요소는 생기지 않는다. 같은 div를 다시 append하면 복제하지 않고 맨 뒤로 이동한다. #lol은 두 개가 되지 않는다. [MDN append](https://developer.mozilla.org/en-US/docs/Web/API/Element/append), [MDN appendChild](https://developer.mozilla.org/en-US/docs/Web/API/Node/appendChild)

<a id="section-2"></a>

## 2. 자식 앞뒤와 형제 앞뒤

| 원본 호출 | 붙는 위치 | 원본에 쓴 값 |
| --- | --- | --- |
| log.append(div) | log의 마지막 자식 | 요소 또는 문자열 가능 |
| log.appendChild(p) | log의 마지막 자식 | Node 필요, 문자열 직접 전달 불가 |
| log.prepend(p2) | log의 첫 번째 자식 | p2 요소 |
| log.before(p3) | log 바로 앞 형제 | p3 요소 |
| log.after(p4) | log 바로 뒤 형제 | p4 요소 |

### 강사님 코드

출처: `teacher/workspace_html/javascript/12_dom_content.html` 148–174행 · **원본 발췌**

```javascript
        const p = document.createElement('p')
        p.textContent = 'p태그'

        // appendChild
        // append 처럼 마지막 자식 요소로 추가된다
        // DOM만 넣을 수 있다
        log.appendChild(p)
        // log.appendChild('<h1>글씨일 뿐이다</h1>')

        const p2 = document.createElement('p')
        p2.textContent = 'p2'

        // prepend : 첫번째 자식 요소로 추가
        log.prepend(p2)


        const p3 = document.createElement('p')
        p3.textContent = 'p3'

        // before : 이전 형제로 추가
        log.before(p3)
        
        const p4 = document.createElement('p')
        p4.textContent = 'p4'
        
        // after : 다음 형제로 추가
        log.after(p4)
```

### 내 코드

출처: `me/workspace_html/javascript/12_dom_content.html` 161–186행 · **원본 발췌**

```javascript
            const p = document.createElement('p')
            p.textContent = 'p태그'
            
            //'appendChild' on 'Node': parameter 1 is not of type 'Node'.
            // appendChild에 글씨를 넣으면 DOM이 아니기에 불가능
            // 그 외에는 append와 같이 마지막 자식 요소로 추가된다
            log.appendChild(p)
            // log.appendChild('<h1>글씨일 뿐</h1>')
            
            const p2 = document.createElement('p')
            p2.textContent = 'p2 log 앞에붙이기'
            
            // pre가 들어가면 앞쪽이라는 소리
            // 첫 번째 자식 요소로 추가할 수 있다
            log.prepend(p2)
            
            // before, after는 형제 요소에 대한 이야기로 앞, 뒤에 넣을 수 있음
            // before : 이전 형제로 추가
            // after : 다음 형제로 추가
            const p3 = document.createElement('p')
            p3.textContent = 'p3 형제로 넣기'
            log.before(p3)

            const p4 = document.createElement('p')
            p4.textContent = 'p4 형제로 넣기'
            log.after(p4)
```

내 코드의 p2·p3·p4 글자는 삽입 위치를 함께 적어 화면에서 구분하기 좋다. 동작 자체는 같다. 주석 처리된 appendChild 문자열 호출을 활성화하면 TypeError가 나므로 원본의 정상 실행에 포함한 것으로 읽지 않는다.

```text
p3                         ← log의 이전 형제
#log
  p2                       ← 첫 자식
  원래 글자, '<h1>abcd</h1>' ← 글자 그대로
  #lol                     ← 다시 append하여 뒤로 이동
  p                        ← 마지막 자식
p4                         ← log의 다음 형제
```

<a id="section-3"></a>

## 3. tr 안에 td를 넣기

### 강사님 코드

출처: `teacher/workspace_html/javascript/12_dom_content.html` 181–188행 · **원본 발췌**

```javascript
        let tr = document.createElement('tr')

        let td = document.createElement('td')
        td.innerText = '첫째칸'
        tr.append(td)

        let tbody = document.querySelector('#tbody')
        tbody.prepend(tr)
```

### 내 코드

출처: `me/workspace_html/javascript/12_dom_content.html` 188–199행 · **원본 발췌**

```javascript
            // 문제_tbody안에 tr,td를 넣어라!
            const tbody = document.querySelector('#tbody')
            const tr = document.createElement('tr')
            tbody.append(tr)
            // console.log(tbody)

            const td = document.createElement('td')
            tr.append(td)
            // console.log(tbody)
            
            td.innerText = '첫째칸'
            console.log(tbody)
```

강사님은 td를 채워 tr에 붙인 뒤 tbody 앞에 넣는다. 나는 tr부터 tbody 뒤에 붙이고 td를 이어 붙인다. **비어 있는 tbody에서는 결과가 같다.** 기존 행이 있다면 prepend는 위쪽, append는 아래쪽에 새 행을 넣으므로 결과 위치가 달라진다.

<a id="section-4"></a>

## 4. rows 배열을 다섯 행으로 만들기

rows는 `[['제목1','작성자1'], …, ['제목5','작성자5']]`이다. rows[i]가 한 행의 데이터이고 [0]은 제목, [1]은 작성자다.

### 강사님 코드

출처: `teacher/workspace_html/javascript/12_dom_content.html` 240–265행 · **원본 발췌**

```javascript
        for(let i=0; i<rows.length; i++){

            let tr1 = document.createElement('tr') // <tr></tr>
            console.log(tr1)
            
            let td1 = document.createElement('td') // <td></td>
            console.log(td1)
            // td1.innerText = '제목1'
            td1.innerText = rows[i][0]
            console.log(td1)
    
            let td2 = document.createElement('td')
            td2.innerText = rows[i][1]
            console.log(td2)
    
            // td를 tr에 넣는다
            // tr에 td를 넣는다
            // i love you  // 나는 사랑하는게 있는데 너다 // 내가 사랑하는게 너다
            // tr에 자식으로 붙이느게 td다
            tr1.append(td1)
            tr1.append(td2)
    
            let board = document.querySelector('#board')
            // board에 자식으로 tr을 넣겠다
            board.append(tr1)
        }
```

### 내 코드

출처: `me/workspace_html/javascript/12_dom_content.html` 218–238행 · **원본 발췌**

```javascript
            // 어떤 값들이 들어가야 하는지를 확인해보아야 함
            for(let i=0; i<rows.length; i++) {
                // tr, td를 우선 만들어 놓고 그 다음것을 생각하기
                const tr_board = document.createElement('tr')
                const td1_board = document.createElement('td')
                const td2_board = document.createElement('td')

                // 만들었다면 메인 table tbody에 tr, td를 순차로 넣어야 하기 때문에
                // tbody의 자식으로 tr, tr의 자식으로 td를 넣어 틀을 완성해줌
                board.append(tr_board)
                tr_board.append(td1_board)
                tr_board.append(td2_board)

                // rows에 있는 배열값을 확인했다면 rows0에 0, 1이 각기 td1, td2에 들어가야 함
                // 여기서 0-0,1 1-0,1 뒤에 배열 자리는 0,1 두가지이고 rows에 0번이 0~4이기 때문에
                // tr,td를 만들기 위해 5번 돌린 반복문에서 td값을 넣기 위해 i값을 동일하게 앞에 넣어준다
                // td1_board.append(rows[i][0])
                // td2_board.append(rows[i][1])
                td1_board.innerText = rows[i][0]
                td2_board.innerText = rows[i][1]
            }
```

강사님은 셀을 채운 뒤 행을 연결하고, 나는 행·셀을 연결한 뒤 값을 쓴다. 둘 다 제목1부터 제목5까지 순서대로 만들어진다. 내 코드는 board를 반복문 밖에서 한 번 선택하고, 구성 과정을 단계별 주석으로 설명한 점이 좋다. 변수명을 강사님처럼 바꿔야 정답이 되는 것은 아니다.

<a id="section-5"></a>

## 5. 문자열을 앞에 붙이면 행 순서가 뒤집힌다

### 강사님 코드

출처: `teacher/workspace_html/javascript/12_dom_content.html` 281–292행 · **원본 발췌**

```javascript
        let board2 = document.querySelector('#board2')
        for(let i=0; i<rows.length; i++){
            let html = `
                    <tr>
                        <td>${rows[i][0]}</td>
                        <td>${rows[i][1]}</td>
                    </tr>
            `
            // board2.innerHTML = board2.innerHTML + html
            // board2.innerHTML += html
            board2.innerHTML = html + board2.innerHTML
        }
```

### 내 코드

출처: `me/workspace_html/javascript/12_dom_content.html` 256–270행 · **원본 발췌**

```javascript
            // 위 방법에서는 error가 나면 멈춰서 밖에 html 추가가 안되는데,
            // 아래 방법에서는 3번째줄에 error가 나면 2번째줄까진 나오기 때문에 안전
            // 아래처럼 역순으로(prepend처럼도 사용할 수 있다)
            const board2 = document.querySelector('#board2')
            console.log('board2', board2)

            for(let i=0; i<rows.length; i++) {
                let html = `
                        <tr>
                            <td>${rows[i][0]}</td>
                            <td>${rows[i][1]}</td>
                        </tr>
                    `
                board2.innerHTML = html + board2.innerHTML
            }
```

이번에는 새 행의 HTML을 **기존 내용 앞**에 붙인다. 제목1 → 제목2·제목1 → 제목3·제목2·제목1 순으로 쌓여 최종 순서는 제목5–제목1이다. 같은 원리로 원본의 `str = i + str`을 0–4까지 반복하면 '43210'이다.

내 주석의 ‘중간 오류가 나도 앞부분이 나와서 안전’은 제한적으로만 맞는다. 일부 내용이 남을 수는 있지만 오류 처리나 전체 데이터의 정확성을 보장하지는 않는다. innerHTML 대입은 기존 자식 요소들을 새로 해석해 교체하므로, **문자열을 앞에 붙이는 방법과 기존 요소를 prepend하는 방법은 결과 모양이 비슷해도 같은 작업은 아니다.** 고정된 수업 문자열로 결과를 비교하고, 입력받은 글자 출력은 앞 절의 셀 텍스트 대입으로 연결한다.

<a id="section-6"></a>

## 6. 복습

1. 같은 div를 append 두 번 하면 div가 두 개가 되는가?
2. log.before(p3)에서 p3는 log의 자식인가?
3. tbody가 비어 있지 않을 때 prepend와 append는 어떻게 다른가?
4. 원본 board와 board2의 제목 순서는 각각 무엇인가?

<details>
<summary>정답</summary>

1. 아니다. 같은 요소가 이동한다.
2. 아니다. 바로 앞 형제다.
3. 각각 기존 행의 앞과 뒤에 추가한다.
4. board는 1–5, board2는 5–1이다.

</details>

<a id="section-7"></a>

## 추가로 알면 좋은 것

DocumentFragment, cloneNode, replaceChildren은 원본 밖 확장 API다. 위 문제를 풀기 위해 새로 배우도록 요구하지 않는다.

