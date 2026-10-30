# 12-02. 요소 생성과 삽입 — 만들기·채우기·연결하기

[JavaScript 목차](README.md) · [읽기 안내](00_JavaScript_V3_동작_백과_읽기법.md)

JavaScript로 새 태그를 만들 수 있지만 만든 순간 화면에 나타나는 것은 아니다. 요소를 만들고 내용을 넣고 문서의 부모에 연결하는 단계를 나누면 표 한 행도 직접 조립할 수 있다.

<a id="chapter-toc"></a>

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

요소 생성·연결·이동을 구분한다. 자식 앞뒤와 형제 앞뒤를 비교하고 배열의 한 행이 tr·td로 만들어지는 과정을 설명한다.

입력·현재 상태·실행 순서·결과를 분리해 설명한다. 실제 수업 원본은 아래에 표시하고, 원본에 없는 선택 학습은 9절 TIP에 둔다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

document.createElement('p')는 실제 DOM 요소 객체를 만든다. 아직 문서에 연결되지 않았을 뿐이며 프레임워크의 가상 DOM을 만든다는 뜻은 아니다. textContent로 글자를 채운 뒤 부모에 append하면 그 문서에 연결된다.

| 메서드 | 대상 기준 위치 | 전달값 |
| --- | --- | --- |
| append |마지막 자식 |요소·문자열 |
| appendChild |마지막 자식 |Node,문자열 직접 전달 불가 |
| prepend |첫 자식 |요소·문자열 |
| before |바로 앞 형제 |요소·문자열 |
| after |바로 뒤 형제 |요소·문자열 |

같은 요소를 다시 append하면 복제하지 않고 이동한다. 객체 하나가 문서의 두 위치에 동시에 복사되어 붙는 것이 아니다. 반면 append('<b>글자</b>')의 문자열은 텍스트로 붙어 b태그로 해석되지 않는다.

표에서는 tbody 안에 tr, 그 안에 td를 넣어 HTML에서 배운 구조를 만든다. rows[i]가 한 행의 데이터라면 rows[i][0]은 첫 셀, rows[i][1]은 둘째 셀이다. 안쪽 배열의 값과 새 DOM 요소는 다른 자료이므로 값을 읽어 셀의 글자로 써 주는 단계가 필요하다.

> 📚 **출처 · 본문 설명 확인:** [MDN createElement](https://developer.mozilla.org/en-US/docs/Web/API/Document/createElement), [append](https://developer.mozilla.org/en-US/docs/Web/API/Element/append), [appendChild](https://developer.mozilla.org/en-US/docs/Web/API/Node/appendChild). 배운 기능의 뜻을 확인한 근거다. 예제·표·풀이 흐름은 수업 코드를 바탕으로 새로 작성했으며 외부 문장을 직접 인용하지 않았다. 확인일: 2026-10-28.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 스크립트.** [HTML 실행 파일](실습/책형_복습/12-02_JavaScript_DOM_요소생성과_삽입.html)과 같은 폴더의 [JS 파일](실습/책형_복습/12-02_JavaScript_DOM_요소생성과_삽입.js)을 함께 내려받는다. HTML을 브라우저로 열고 Console에서 결과를 확인한다. script는 필요한 HTML 뒤에 연결한다. 콘솔 출력은 페이지 본문에 자동으로 쓰이지 않는다.

**먼저 준비할 HTML · body 안:**

```html
    <div id="log"></div>
    <table>
        <thead><tr><th>제목</th><th>작성자</th></tr></thead>
        <tbody id="board"></tbody>
    </table>
```

```javascript
const log = document.getElementById('log');
const item = document.createElement('p');
item.textContent = '새 문장';
log.append(item);
log.append('<b>글자</b>');
log.append(item);
console.log(log.querySelectorAll('p').length);
console.log(log.textContent);
const rows = [['제목1', '작성자1'], ['제목2', '작성자2']];
const board = document.getElementById('board');
for (let i = 0; i < rows.length; i++) {
    const tr = document.createElement('tr');
    const title = document.createElement('td');
    const writer = document.createElement('td');
    title.textContent = rows[i][0];
    writer.textContent = rows[i][1];
    tr.append(title);
    tr.append(writer);
    board.append(tr);
}
console.log(board.querySelectorAll('tr').length);
console.log(board.querySelectorAll('tr')[0].querySelector('td').textContent);
console.log(board.querySelectorAll('tr')[1].querySelector('td').textContent);
```

item을 두 번 붙여도 p는 하나다. 문자열을 붙인 뒤 같은item을 다시 끝으로 옮겨 글자 순서가 태그 모양 문자열 → 새 문장이 된다. 표는 두 행을 새로 만들어 순서대로 연결한다. 데이터와 부모 요소를 함께 준비한 전체 스크립트이므로 숨은 rows 선언이 없다.

**예상 출력 또는 관찰:**

```text
1
<b>글자</b>새 문장
2
제목1
제목2
```

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 원본의 일부다. 원본에 의존하는 앞 선언·HTML·함수는 다음 절의 연결까지 읽는다. 주석의 잘못된 표현도 원문대로 보존하고 설명에서 교정한다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/12_dom_content.html` 142–159행

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

**발췌 바로 풀이:** 둘 다 div 요소를 만들고 id·글자·색상을 지정한 후 #log에 연결한다. createElement는 이미 실제 DOM 요소 객체를 만든다. 내 주석의 ‘가상 DOM을 append해야 실체화’라는 설명은 **문서에 아직 연결되지 않은 요소를 append로 연결한다**로 교정한다. 프레임워크의 가상 DOM과 혼동하지 않는다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/12_dom_content.html` 161–186행

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

**발췌 바로 풀이:** 내 코드의 p2·p3·p4 글자는 삽입 위치를 함께 적어 화면에서 구분하기 좋다. 동작 자체는 같다. 주석 처리된 appendChild 문자열 호출을 활성화하면 TypeError가 나므로 원본의 정상 실행에 포함한 것으로 읽지 않는다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/12_dom_content.html` 188–199행

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

**발췌 바로 풀이:** 강사님은 td를 채워 tr에 붙인 뒤 tbody 앞에 넣는다. 나는 tr부터 tbody 뒤에 붙이고 td를 이어 붙인다. **비어 있는 tbody에서는 결과가 같다.** 기존 행이 있다면 prepend는 위쪽, append는 아래쪽에 새 행을 넣으므로 결과 위치가 달라진다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/12_dom_content.html` 218–238행

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

**발췌 바로 풀이:** 강사님은 셀을 채운 뒤 행을 연결하고, 나는 행·셀을 연결한 뒤 값을 쓴다. 둘 다 제목1부터 제목5까지 순서대로 만들어진다. 내 코드는 board를 반복문 밖에서 한 번 선택하고, 구성 과정을 단계별 주석으로 설명한 점이 좋다. 변수명을 강사님처럼 바꿔야 정답이 되는 것은 아니다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/12_dom_content.html` 256–270행

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

**발췌 바로 풀이:** 이번에는 새 행의 HTML을 **기존 내용 앞**에 붙인다. 제목1 → 제목2·제목1 → 제목3·제목2·제목1 순으로 쌓여 최종 순서는 제목5–제목1이다. 같은 원리로 원본의 `str = i + str`을 0–4까지 반복하면 '43210'이다.

내 div는 id·글자·빨간색을 지정한 뒤 log에 연결한다. 같은 div를 다시 append하여 복제가 아닌 이동을 관찰했다. p2·p3·p4 글자에 위치 설명을 붙인 점은 자식·형제의 차이를 화면에서 찾기 좋다. 표의 첫 행은 내가 tr부터 tbody에 붙이고 셀을 이어 넣지만 강사님은 셀을 채워 묶은 뒤 행을 넣는다. 빈 tbody에서는 같은 결과이나 앞·뒤 삽입 위치는 다르다.

<a id="connections"></a>

## 5. 선언·호출·파일이 연결되는 흐름

rows의 한 행 → 새 tr → 두 td 생성 → 제목·작성자 대입 → tr의 자식으로 연결 → board의 자식으로 연결 순서다. 원본 rows는 제목1~5·작성자1~5의 다섯 쌍이다. 내 board는 반복 밖에서 한 번 선택하고, 강사님은 반복 안에서 다시 선택한다. DOM을 추가하는 위치와 셀의 글자를 넣는 시점은 구분하되 최종 구조가 같은지 확인한다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 내 주석은 틀을 만든 뒤 데이터를 넣는 과정을 단계별로 설명하고, 반복 밖에서 board를 준비한다. **교정:** append해야 가상 객체가 실체화된다는 설명보다 문서 연결이라고 이해한다. **한계:** 중간 오류 때 일부 행이 남는다는 사실이 코드 전체의 안전성·정확성을 보장하지 않는다. **개선 방향:** 고정 데이터의 HTML 문자열 비교와 입력 글자의 텍스트 대입을 구분한다.

개선안은 원본을 수정한 결과가 아니다. 실제 오류, 수업용 단순화, 목적에 따른 선택을 구별해 판단한다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



같은 생성·삽입을 반복 인용하지 않는다. 강사님의 tbody.prepend와 내 append는 기존 행이 있을 때 위·아래 위치가 달라져 목적에 맞춰 고른다. 변수명을 강사님처럼 바꾸어야 정답이 되는 것은 아니다. 내 단계별 이름과 주석도 구조를 설명할 수 있으면 유익하다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 원본 위치·방식 | 최종 순서 |
| --- | --- |
| board에 행 append |제목1→제목2→…→제목5 |
| board2의 html+기존HTML |제목5→…→제목2→제목1 |
| str=i+str를0~4반복 |43210 |
| 같은요소두번append |한개가끝으로이동 |

문자열을 앞에 붙이는 것은 기존 요소 자체를 prepend하는 것과 다르다. innerHTML 대입은 기존 내용을 다시 해석해 교체한다. 결과 모양이 같아도 기존 자식 객체를 그대로 이동한 작업과 구분한다. appendChild에 문자열을 넣는 원본 줄은 주석이며 켜면 TypeError다.

| 한 가지 변경 | 예상 | 이유 |
| --- | --- | --- |
| board.append만prepend로 |표제목2→제목1 |매회앞에삽입 |
| item의마지막append만제거 |새문장→태그모양글자 |재이동없음 |
| rows에한행추가 |표3행 |length만큼반복 |

만든 요소가 안 보이면 부모에 연결했는지 확인한다. 두 번 붙였는데 개수가 늘지 않으면 같은 객체인지 본다. 위치가 엉뚱하면 자식 앞·뒤인지 형제 앞·뒤인지 나누어 그린다. 표는 tr·td의 부모를 확인한다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** DocumentFragment·template·복제·가상 DOM 라이브러리의 상세는 추가 학습이다. 현재 원본의 생성·연결을 설명하기 위해 필수로 도입하지 않는다.



이 절의 확장은 기본 문제의 필수 조건이 아니다. 📚 출처가 있다는 것과 수업 밖 기능이라는 것은 다른 구분이다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. createElement만 하면 문서 화면에 연결되는가?
2. 같은 요소를 두 번 append하면 몇 개인가?
3. before는 첫 자식에 넣는가?

<details>
<summary>짧은 풀이 — 먼저 답한 뒤 확인</summary>

아직 연결되지 않는다. 같은 객체 하나가 이동한다. before는 이전 형제이며 첫 자식은 prepend다.

</details>

| 단계 | 확인 |
| --- | --- |
| 생성 |createElement |
| 내용 |textContent 등 |
| 연결 |부모와 삽입 위치 |
| 이동 |같은 객체 재사용 |

[장별 연습문제](실습/연습문제/12-02_JavaScript_DOM_요소생성과_삽입_연습문제.md)에서 예상·설명·수정을 이어 간다. 다음은 [스타일과 퀴즈](12-03_JavaScript_DOM_스타일과_퀴즈.md)다.

<!-- 이전 색인 이동 주소 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>
<a id="section-6"></a>
<a id="section-7"></a>

[이 장의 목차](#chapter-toc)에서 현재 설명을 찾는다.
