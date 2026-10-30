# 20-02. 날씨 응답 — 항목을 고르는 일과 같은 시각으로 묶는 일

[JavaScript 목차](README.md) · [읽기 안내](00_JavaScript_V3_동작_백과_읽기법.md)

기온·습도·강수량을 골랐는데 표가 한 줄로 합쳐지지 않는다면 필터가 실패한 것일까? 필요한 항목만 남기는 일과 같은 시각의 항목을 묶는 일은 다른 작업이다. 응답의 구조를 그림처럼 풀어 읽고 두 단계를 차례로 적용한다.

<a id="chapter-toc"></a>

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

중첩 응답에서 item 배열을 찾고 filter 조건을 설명한다. 시각을 객체 키로 묶는 계산을 따라가며, 한 항목당 행과 한 시각당 행의 차이를 비교한다. 표의 tr·td 구조도 확인한다.

입력·현재 상태·실행 순서·결과를 분리해 설명한다. 실제 수업 원본은 아래에 표시하고, 원본에 없는 선택 학습은 9절 TIP에 둔다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

API 응답은 한 개 숫자가 아니라 여러 단계의 객체와 배열일 수 있다. 이 원본은 data → response → body → items → item 순서로 접근하여 배열을 얻는다. 그 배열의 각 항목에는 category·fcstTime·fcstValue가 있다. 같은 시각이라도 기온과 습도는 서로 다른 항목으로 온다.

| 단계 | 입력 | 출력 | 아직 하지 않은 일 |
| --- | --- | --- | --- |
| 경로 접근 | 응답 객체 | item 배열 | 필요한 종류 고르기 |
| filter | 전체 항목 | 세 종류의 새 배열 | 같은 시각끼리 묶기 |
| 그룹 만들기 | 선택 항목 | 시각별 객체 | 화면 행 생성 |
| DOM 생성 | 시각별 값 | 한 시각당 한 행 | 외부 API 성공 검증과는 별개 |

filter의 콜백이 true인 항목만 새 배열에 남는다. 필터는 여러 항목을 합쳐 한 항목으로 만들지 않는다. 0900의 기온·습도·강수량 세 개는 필터 뒤에도 세 개다. groups['0900'] 객체를 만들고 그 안의 T1H·REH·RN1 속성에 각각 값을 넣어야 한 시각의 묶음이 된다.

groups[item.fcstTime][item.category]는 두 번의 속성 접근이다. 먼저 시각의 객체를 찾고 그 안에서 종류 이름으로 값을 넣는다. 변수가 가진 문자열을 키로 쓰므로 대괄호 표기가 필요하다. groups.item.fcstTime처럼 쓰면 이 계산과 다른 이름을 찾는다.

> 📚 **출처 · 본문 설명 확인:** [MDN filter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter), [Object.keys](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/keys). 배운 기능의 뜻을 확인한 근거다. 예제·표·풀이 흐름은 수업 코드를 바탕으로 새로 작성했으며 외부 문장을 직접 인용하지 않았다. 확인일: 2026-10-28.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 스크립트.** [HTML 실행 파일](실습/책형_복습/20-02_JavaScript_날씨응답_필터와_표시.html)과 같은 폴더의 [JS 파일](실습/책형_복습/20-02_JavaScript_날씨응답_필터와_표시.js)을 함께 내려받는다. HTML을 브라우저로 열고 Console에서 결과를 확인한다. script는 필요한 HTML 뒤에 연결한다. 콘솔 출력은 페이지 본문에 자동으로 쓰이지 않는다.

**먼저 준비할 HTML · body 안:**

```html
    <table><thead><tr><th>시각</th><th>T1H</th><th>REH</th><th>RN1</th></tr></thead><tbody id="rows"></tbody></table>
```

**위 파일 head의 style:**

```css
table { border-collapse: collapse; } th, td { border: 1px solid #777; padding: 8px; }
```

```javascript
const data = { response: { body: { items: { item: [
    { category: 'T1H', fcstTime: '0900', fcstValue: '25' },
    { category: 'REH', fcstTime: '0900', fcstValue: '70' },
    { category: 'RN1', fcstTime: '0900', fcstValue: '1' },
    { category: 'LGT', fcstTime: '0900', fcstValue: '0' },
    { category: 'T1H', fcstTime: '1000', fcstValue: '26' },
    { category: 'REH', fcstTime: '1000', fcstValue: '65' },
    { category: 'RN1', fcstTime: '1000', fcstValue: '0' }
] } } } };
const items = data.response.body.items.item;
const selected = items.filter(function (item) {
    return item.category === 'T1H' || item.category === 'REH' || item.category === 'RN1';
});
const groups = {};
for (const item of selected) {
    if (!groups[item.fcstTime]) groups[item.fcstTime] = {};
    groups[item.fcstTime][item.category] = item.fcstValue;
}
const times = Object.keys(groups).sort();
const rows = document.getElementById('rows');
rows.innerHTML = '';
for (const time of times) {
    const values = [time, groups[time].T1H, groups[time].REH, groups[time].RN1];
    const row = document.createElement('tr');
    for (const value of values) {
        const cell = document.createElement('td');
        cell.textContent = value === undefined ? '-' : value;
        row.append(cell);
    }
    rows.append(row);
    console.log(values.join(' | '));
}
console.log('원본 항목', items.length, '선택 항목', selected.length, '표 행', times.length);
```

실제 API 응답이 아닌 가상 객체를 코드 안에 넣어 네트워크 없이 실행한다. 전체 7개에서 LGT 하나를 제외하면 6개다. 같은 시각별로 묶으면 0900·1000의 두 객체가 되고 행도 2개다. 배열의 항목 수와 표 행 수가 달라진 이유를 설명할 수 있어야 한다. times.sort는 앞 장에서 배운 문자열 정렬로 네 자리 시각을 정리한 개선이다. Object.keys의 결과가 언제나 시간순이라고 가정하지 않는다. 빠진 종류는 -로 표시하며 실제 측정값 0과 구분한다.

**예상 출력 또는 관찰:**

```text
0900 | 25 | 70 | 1
1000 | 26 | 65 | 0
원본 항목 7 선택 항목 6 표 행 2
```

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 원본의 일부다. 원본에 의존하는 앞 선언·HTML·함수는 다음 절의 연결까지 읽는다. 주석의 잘못된 표현도 원문대로 보존하고 설명에서 교정한다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/asset/js/20_ajax.js` 91–135행

```javascript
        xhr.onload = function() {
            console.log( xhr.responseText )

            const data = JSON.parse(xhr.responseText)
            console.log(data)

            // response - body - items - item
            // category: LGT - 번개, fcstValue: 0 - 확률, fcstTime: 1600 - 시간(16시)
            // category: T1H(기온), RN1(강수량), REH(습도)
            console.log(data.response.body.items.item[0].category)
            console.log(data.response.body.items.item[0].fcstValue)
            console.log(data.response.body.items.item[0].fcstTime)

            let item = data.response.body.items.item
            // for(let i=0;item.length;i++){
            //     if(item[i].category == 'T1H') {
            //         console.log(item[i])
            //     } else if(item[i].category == 'RN1'){
            //         console.log(item[i])
            //     } else if(item[i].category == 'REH') {
            //         console.log(item[i])
            //     }
            // }

            // for문을 사용해도 되지만, filter를 사용해도 좋음.
            // let filtered = item.filter(function(data) {
            //     if(data.category == 'T1H' 
            //     || data.category == 'RN1'
            //     || data.category == 'REH') {
            //         return true
            //     }
            // })
            // console.log(filtered)

            // 테이블로 표시
            // 1. 예측카테고리 | 예측시간 | 값
            const output = document.querySelector('#output')

            let cateFilter = item.filter(function(data) {
                if(data.category == 'T1H'
                || data.category == 'RN1'
                || data.category == 'REH') {
                    return true
                }
            })
```

**발췌 바로 풀이:** 응답 문자열을 `JSON.parse`한 뒤 `data.response.body.items.item`으로 배열을 얻는다. `filter`는 `category`가 세 코드 중 하나인 항목만 새 배열로 만든다. 데이터 경로가 실제 응답과 다르면 중간 값이 없어서 오류가 날 수 있다. 이번 수업 원본에는 그 경우의 분기 처리가 없다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/asset/js/20_ajax.js` 138–175행

```javascript
            output.innerHTML = ''

            const titleDiv1 = document.createElement('div')
            titleDiv1.innerText = '예측카테고리'
            titleDiv1.classList.add('column')
            output.append(titleDiv1)
            const titleDiv2 = document.createElement('div')
            titleDiv2.innerText = '예측시간'
            titleDiv2.classList.add('column')
            output.append(titleDiv2)
            const titleDiv3 = document.createElement('div')
            titleDiv3.innerText = '값'
            titleDiv3.classList.add('column')
            output.append(titleDiv3)
            
            for(let j=0; j<cateFilter.length; j++) {
                const addDiv = document.createElement('div')
                addDiv.classList.add('filterLine')
                output.append(addDiv)

                const cateDiv = document.createElement('div')
                cateDiv.classList.add('category')
                cateDiv.classList.add('column')
                addDiv.append(cateDiv)
                cateDiv.innerText = cateFilter[j].category

                const timeDiv = document.createElement('div')
                timeDiv.classList.add('time')
                timeDiv.classList.add('column')
                addDiv.append(timeDiv)
                timeDiv.innerText = cateFilter[j].fcstTime

                const valueDiv = document.createElement('div')
                valueDiv.classList.add('value')
                valueDiv.classList.add('column')
                addDiv.append(valueDiv)
                valueDiv.innerText = cateFilter[j].fcstValue
            }
```

**발췌 바로 풀이:** 강사님은 `tr`과 `td`로 HTML 표 행을 만들고, 나는 `div`를 조합해 열을 만든다. **둘 다 세 필드(category, fcstTime, fcstValue)를 보여 주는 같은 학습 목표**다. 내 코드가 길어진 이유는 열마다 요소를 직접 만들고 클래스를 붙였기 때문이다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/asset/js/20_ajax.js` 215–254행

```javascript
            for(let j=0; j<timeFilter.length; j++) {
                const addDiv = document.createElement('div')
                addDiv.classList.add('filterLine')
                output_time.append(addDiv)
                
                const fcstDiv = document.createElement('div')
                fcstDiv.classList.add('fcstTime')
                fcstDiv.classList.add('column')
                addDiv.append(fcstDiv)
                if(timeFilter[j].category == 'T1H') {
                    fcstDiv.innerText = timeFilter[j].fcstTime
                }
         
                const t1hDiv = document.createElement('div')
                t1hDiv.classList.add('T1H')
                t1hDiv.classList.add('column')
                addDiv.append(t1hDiv)
                if(timeFilter[j].category == 'T1H' ||
                    timeFilter[j].category == 'REH') {
                    t1hDiv.innerText = timeFilter[j].fcstValue
                    // jsonT.T1H += timeFilter[j].fcstValue
                }
                
                const rehDiv = document.createElement('div')
                rehDiv.classList.add('REH')
                rehDiv.classList.add('column')
                addDiv.append(rehDiv)
                if(timeFilter[j].category == 'T1H') {
                    rehDiv.innerText = timeFilter[j].fcstValue
                    // jsonT.REH += timeFilter[j].fcstValue
                }
                
                const rn1Div = document.createElement('div')
                rn1Div.classList.add('RN1')
                rn1Div.classList.add('column')
                addDiv.append(rn1Div)
                if(timeFilter[j].category == 'T1H') {
                    rn1Div.innerText = timeFilter[j].fcstValue
                    // jsonT.RN1 += timeFilter[j].fcstValue
                }
```

**발췌 바로 풀이:** 내 코드는 `timeFilter`의 **항목마다** 한 행을 만든다. 그래서 같은 시각의 세 값이 한 행으로 합쳐지지 않는다. 더구나 `T1H` 값을 습도·강수량 칸에도 넣는 조건이 있어 제목과 값이 어긋난다. 원래 문제인 ‘시간별 온도·습도·강수량 한 줄’을 풀려면 강사님처럼 먼저 시각별로 묶어야 한다. 내 첫 번째 표(원본 순서 출력)는 학습 목적대로 작동하는 구조이므로 보존한다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/asset/js/20_ajax.js` 276–308행

```javascript
    const btn4 = document.querySelector('#btn4')
    btn4.addEventListener('click', function() {

        const Q3_xhr = new XMLHttpRequest()

        Q3_xhr.open('GET', 'https://jsonplaceholder.typicode.com/users')
        Q3_xhr.send()
        Q3_xhr.onload = function () {
            console.log(Q3_xhr.responseText)

            const Q3_xhrData = JSON.parse(Q3_xhr.responseText)
            console.log(Q3_xhrData)

            const q3 = document.querySelector('#q3')

            for(let i=0; i<Q3_xhrData.length; i++) {
                // console.log(Q3_xhrData[i].id)
                // console.log(Q3_xhrData[i].name)
                // console.log(Q3_xhrData[i].address.zipcode)
                // console.log(Q3_xhrData[i].company.name)

                let Q3_tr = document.createElement('tr')
                q3.append(Q3_tr)
    
                q3.innerHTML += `
                    <td>${Q3_xhrData[i].id}</td>
                    <td>${Q3_xhrData[i].name}</td>
                    <td>${Q3_xhrData[i].address.zipcode}</td>
                    <td>${Q3_xhrData[i].company.name}</td>
                `
            }
        }
    })
```

**발췌 바로 풀이:** 내 코드는 별도 버튼에서 사용자 목록의 `id`, `name`, `address.zipcode`, `company.name`을 읽으려 했다. 그러나 `tr`을 만들어 붙인 다음 `q3.innerHTML +=`로 **행 바깥에 `td`를 직접 더한다**. 표 구조를 의도대로 만들려면 생성한 `Q3_tr`에 셀을 넣거나 `Q3_tr.innerHTML`을 지정해야 한다. 이 부분은 강사님 파일의 같은 위치에 완성 예제가 없으므로 내 시도와 수정 방향으로 구분한다.

내 cateFilter는 세 종류를 남겨 각 항목의 category·fcstTime·fcstValue를 div 열에 보여 준다. 첫 문제의 목표에는 맞는 구조다. 둘째 timeFilter도 같은 필터이므로 여전히 한 측정 종류당 한 항목이다. 그런데 그 항목마다 행을 만들어 시간별 세 값을 합치지 못한다. T1H 조건에서 습도·강수량 칸에도 같은 fcstValue를 넣는 분기는 열 제목과 값도 어긋난다. 뒤 사용자 목록에서는 tr을 만들고 나서 q3.innerHTML에 td를 더해 생성한 행 바깥을 바꾼다.

<a id="connections"></a>

## 5. 선언·호출·파일이 연결되는 흐름

원본의 요청 준비·send → onload에서 responseText 읽기 → JSON.parse → data.response.body.items.item → filter → 첫 표 생성 또는 시각별 재구성 → DOM 출력 순서다. 새 예제는 통신을 생략하고 응답 이후 처리만 분리했다. 사용자 목록 수정도 tr을 만든 뒤 해당 tr 안에 td를 붙이고 마지막에 tbody에 행을 붙이는 흐름이다. q3와 Q3_tr은 서로 다른 요소이므로 어느 쪽을 수정하는지 확인한다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 내 첫 표는 요소 생성·클래스·입력 필드를 직접 연결하여 DOM 흐름을 잘 드러낸다. **실제 논리 오류:** 둘째 표는 필터만으로 그룹이 만들어졌다고 가정하고 다른 종류의 칸에도 기온 값을 넣는다. **개선:** 먼저 시각별 객체를 만든 뒤 한 묶음을 한 행으로 출력한다. **표 구조 오류:** 새 tr의 내용은 그 tr에 넣어야 한다. tbody의 innerHTML을 다시 쓰면 기존 자식도 재구성할 수 있으므로 행을 만들고 나서 부모 문자열에 셀을 더하는 방식을 혼합하지 않는다.

개선안은 원본을 수정한 결과가 아니다. 실제 오류, 수업용 단순화, 목적에 따른 선택을 구별해 판단한다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교

출처: `D:/workspace_teacher/workspace_html/javascript/asset/js/20_ajax.js` 147–180행

```javascript
            // 문제2
            // 시간 | 온도 | 습도 | 강수량
            let j = {
                '1000':{
                    'T1H': 20,
                    'REH': 80,
                    'RN1': '2.0 mm'
                }
            }

            j = {}
            for(let i=0; i<filtered.length; i++){
                // if( j[filtered[i].fcstTime] == undefined ){
                if( !j[filtered[i].fcstTime] ){
                    j[filtered[i].fcstTime] = {}
                }
                j[filtered[i].fcstTime][filtered[i].category] = filtered[i].fcstValue
            }
            console.log(j)

            const q2 = document.querySelector('#q2')
            let keys = Object.keys(j)
            for(let i=0; i<keys.length; i++){
                const tr = document.createElement('tr')
                tr.innerHTML = `
                    <td>${keys[i]}</td>
                    <td>${j[keys[i]]['T1H']}</td>
                    <td>${j[keys[i]]['REH']}</td>
                    <td>${j[keys[i]]['RN1']}</td>
                `
                q2.append(tr)
            }

        }
```

강사님 발췌의 시각별 객체 구성은 내 둘째 문제를 교정할 때 직접 도움이 되어 인용한다. 처음 j에 적은 예시 객체는 곧 j={}로 덮어쓰므로 실제 결과에 미리 들어 있는 데이터가 아니다. 첫 표는 강사님이 tr·td, 내가 div를 선택한 차이가 있다. 내 코드가 길다는 이유만으로 틀린 것은 아니며 표 구조를 전달하려면 HTML 표가 의미를 더 명확히 표현한다. 강사님도 둘째 출력 앞 q2를 비우지 않아 반복 요청에서 행이 누적될 수 있다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 처리한 항목 | groups의 변화 |
| --- | --- |
| 0900 T1H 25 | 0900 객체 생성, T1H='25' |
| 0900 REH 70 | 같은 0900에 REH='70' 추가 |
| 0900 RN1 1 | 같은 0900에 RN1='1' 추가 |
| LGT 0 | 필터에서 제외되어 그룹 처리 안 함 |
| 1000 세 항목 | 별도 1000 객체에 값 저장 |

이 연습은 같은 예측 날짜의 한 묶음을 가정한다. 여러 날짜를 시간만으로 묶으면 같은 시각이 덮일 수 있다. 누락 종류와 중복 항목도 실제 응답 조건을 따로 확인해야 한다. 원본 키·전체 요청 URL은 싣지 않았고 이번에 외부 날씨 요청도 실행하지 않았다. 여기 숫자는 표 구조를 설명하는 가상 값으로 실제 날씨가 아니다.

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| 1000 RN1 항목 제거 | 둘째 행 강수 칸 - | 누락과 0을 구분 |
| LGT 필터 조건 추가 | 선택 항목 증가 | 표 열 구성은 자동 추가되지 않음 |
| rows 비우기 제거 후 같은 출력 반복 | 행 누적 가능 | 기존 DOM이 남음 |
| 그룹 없이 selected 반복 | 항목당 한 행 | 시간별 묶음이 아님 |

세 값이 한 행에 안 모이면 filter 뒤 자료구조부터 본다. 모든 칸이 기온이면 각 조건과 대입 값을 확인한다. 반복 실행 때 늘어나면 기존 출력 영역을 비웠는지 본다. 응답 경로 오류면 중간 객체가 실제로 있는지 확인하고 임의로 JSON.parse를 반복 호출하지 않는다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** API 키 관리·실패 응답 안내·여러 날짜와 중복값 처리 정책·단위와 결측 상태의 정밀한 표시 등은 추가 학습이다. 본문에서 실습한 filter·객체 키·DOM 생성과 구분한다.



이 절의 확장은 기본 문제의 필수 조건이 아니다. 📚 출처가 있다는 것과 수업 밖 기능이라는 것은 다른 구분이다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. filter는 같은 시각의 세 항목을 한 개로 합치는가?
2. groups[time][category]의 두 대괄호는 무엇을 고르는가?
3. 빠진 강수량과 강수량 0은 같은가?
4. 만든 td를 넣을 대상은 tbody인가, 해당 tr인가?

<details>
<summary>짧은 풀이 — 먼저 답한 뒤 확인</summary>

합치지 않고 조건에 맞는 항목만 남긴다. 첫 대괄호는 시각별 객체, 다음은 그 안의 종류 속성을 고른다. 누락과 0은 다르다. 셀은 해당 tr 안에 넣고 행을 tbody에 붙인다.

</details>

| 작업 | 역할 |
| --- | --- |
| 경로 | 응답에서 배열 찾기 |
| 필터 | 필요한 종류 남기기 |
| 그룹 | 시각별 값 모으기 |
| 출력 | 묶음당 한 행 |

[장별 연습문제](실습/연습문제/20-02_JavaScript_날씨응답_필터와_표시_연습문제.md)에서 예상·설명·수정을 이어 간다. 다음은 [외부 AI 요청](21_JavaScript_외부AI_API요청과_대화기록.md)이다.

<!-- 이전 색인 이동 주소 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>
<a id="section-6"></a>

[이 장의 목차](#chapter-toc)에서 현재 설명을 찾는다.
