# 20-02. 날씨 응답 — 필요한 항목만 골라 표로 바꾸기

[JavaScript 목차](README.md) · [이전: AJAX와 fetch](20_JavaScript_AJAX와_fetch.md)

양쪽 `20_ajax.js`는 날씨 서비스 요청을 만들고, 응답의 `item` 배열에서 기온 `T1H`, 강수량 `RN1`, 습도 `REH`를 골라 화면에 표시한다. 원본에는 요청용 서비스 키가 들어 있어 **이 문서에 키와 전체 URL을 옮기지 않는다**. 키를 지운 코드 일부만 인용한다. 외부 요청을 실제로 재실행해 응답을 확인한 기록은 없다.

<!-- chapter-toc -->

- [1. 응답 배열에서 세 종류 고르기](20-02_JavaScript_날씨응답_필터와_표시.md#section-1)
- [2. 원본 순서대로 행 만들기](20-02_JavaScript_날씨응답_필터와_표시.md#section-2)
- [3. 같은 시각의 값 묶기](20-02_JavaScript_날씨응답_필터와_표시.md#section-3)
- [4. 사용자 목록 표시 실습](20-02_JavaScript_날씨응답_필터와_표시.md#section-4)
- [직접 확인할 질문](20-02_JavaScript_날씨응답_필터와_표시.md#section-5)
- [추가로 알면 좋은 것](20-02_JavaScript_날씨응답_필터와_표시.md#section-6)

<a id="section-1"></a>

## 1. 응답 배열에서 세 종류 고르기

### 강사님 코드

출처: `teacher/workspace_html/javascript/asset/js/20_ajax.js` 95~123행 · **원본 발췌**

```javascript
        // 4. 결과 활용
        xhr.onload = function(){
            // console.log( xhr.responseText )
            const data = JSON.parse( xhr.responseText )
            console.log( data )

            console.log( data.response.body.items.item[0].category )
            console.log( data.response.body.items.item[0].fcstValue )
            console.log( data.response.body.items.item[0].fcstTime )

            // category가 T1H(기온), RN1(강수량), REH(습도)
            let item = data.response.body.items.item
            // for(let i=0; i<item.length; i++){
            //     if(item[i].category == 'T1H'){
            //         console.log(item[i])
            //     } else if(item[i].category == 'RN1'){
            //         console.log(item[i])
            //     } else if(item[i].category == 'REH'){
            //         console.log(item[i])
            //     }
            // }
            let filtered = item.filter(function(data){
                if(data.category == 'T1H' 
                    || data.category == 'RN1' 
                    || data.category == 'REH'){
                    return true
                }
            })
            console.log(filtered)
```

### 내 코드

출처: `me/workspace_html/javascript/asset/js/20_ajax.js` 91~135행 · **원본 발췌**

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

응답 문자열을 `JSON.parse`한 뒤 `data.response.body.items.item`으로 배열을 얻는다. `filter`는 `category`가 세 코드 중 하나인 항목만 새 배열로 만든다. 데이터 경로가 실제 응답과 다르면 중간 값이 없어서 오류가 날 수 있다. 이번 수업 원본에는 그 경우의 분기 처리가 없다.

<a id="section-2"></a>

## 2. 원본 순서대로 행 만들기

### 강사님 코드

출처: `teacher/workspace_html/javascript/asset/js/20_ajax.js` 125~145행 · **원본 발췌**

```javascript
            // 문제1
            // 예측카테고리 | 예측시간 | 값

/*
            <tr>
                <td>T1H</td>
                <td>0900</td>
                <td>28</td>
            </tr>
*/
            const q1 = document.querySelector('#q1')
            q1.innerHTML = ''
            for(let i=0; i<filtered.length; i++){
                const tr = document.createElement('tr')
                tr.innerHTML = `
                    <td>${filtered[i].category}</td>
                    <td>${filtered[i].fcstTime}</td>
                    <td>${filtered[i].fcstValue}</td>
                `
                q1.append(tr)
            }
```

### 내 코드

출처: `me/workspace_html/javascript/asset/js/20_ajax.js` 138~175행 · **원본 발췌**

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

강사님은 `tr`과 `td`로 HTML 표 행을 만들고, 나는 `div`를 조합해 열을 만든다. **둘 다 세 필드(category, fcstTime, fcstValue)를 보여 주는 같은 학습 목표**다. 내 코드가 길어진 이유는 열마다 요소를 직접 만들고 클래스를 붙였기 때문이다.

<a id="section-3"></a>

## 3. 같은 시각의 값 묶기

### 강사님 코드

출처: `teacher/workspace_html/javascript/asset/js/20_ajax.js` 147~180행 · **원본 발췌**

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

강사님은 예측 시각을 객체 키로 삼고 그 안에 `T1H`·`REH`·`RN1` 값을 넣는다. `Object.keys(j)`로 시각 목록을 얻어 한 시각당 한 행을 그린다. 이는 앞 장의 객체·키와 이번 장의 배열 필터를 연결하는 실습이다.

### 내 코드

출처: `me/workspace_html/javascript/asset/js/20_ajax.js` 215~254행 · **원본 발췌**

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

내 코드는 `timeFilter`의 **항목마다** 한 행을 만든다. 그래서 같은 시각의 세 값이 한 행으로 합쳐지지 않는다. 더구나 `T1H` 값을 습도·강수량 칸에도 넣는 조건이 있어 제목과 값이 어긋난다. 원래 문제인 ‘시간별 온도·습도·강수량 한 줄’을 풀려면 강사님처럼 먼저 시각별로 묶어야 한다. 내 첫 번째 표(원본 순서 출력)는 학습 목적대로 작동하는 구조이므로 보존한다.

<a id="section-4"></a>

## 4. 사용자 목록 표시 실습

### 내 코드

출처: `me/workspace_html/javascript/asset/js/20_ajax.js` 276~308행 · **원본 발췌**

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

내 코드는 별도 버튼에서 사용자 목록의 `id`, `name`, `address.zipcode`, `company.name`을 읽으려 했다. 그러나 `tr`을 만들어 붙인 다음 `q3.innerHTML +=`로 **행 바깥에 `td`를 직접 더한다**. 표 구조를 의도대로 만들려면 생성한 `Q3_tr`에 셀을 넣거나 `Q3_tr.innerHTML`을 지정해야 한다. 이 부분은 강사님 파일의 같은 위치에 완성 예제가 없으므로 내 시도와 수정 방향으로 구분한다.

<a id="section-5"></a>

## 직접 확인할 질문

1. 필터 후에도 `fcstTime`이 같은 항목이 여러 개 남는 이유는 무엇일까?
2. 한 시각의 세 측정값을 같은 행에 표시하려면 어떤 키로 먼저 묶어야 할까?
3. `tr`을 만든 뒤 `td`는 어느 요소의 안에 넣어야 할까?

<a id="section-6"></a>

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/20-02_JavaScript_날씨응답_필터와_표시_연습문제.md)

## 추가로 알면 좋은 것

실제 외부 API 사용 시 요청 실패, 응답 형식 변화, 키 관리가 필요하다. 이번 수업의 본문은 원본에서 다룬 `XMLHttpRequest`·JSON·`filter`·DOM 출력 흐름에 한정한다.

