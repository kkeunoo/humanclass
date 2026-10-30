# 18. 브라우저 이동과 지도 — 내 코드와 외부 도구의 연결

[JavaScript 목차](README.md) · [읽기 안내](00_JavaScript_V3_동작_백과_읽기법.md)

location은 주소, history는 방문 기록, window.open은 새 창이나 탭 요청을 다룬다. 지도·우편번호 예제는 여기에 외부 스크립트와 콜백이 더해진다. 내가 작성한 부분과 외부 도구가 제공하는 부분을 나누면 실패한 위치도 찾기 쉽다.

<a id="chapter-toc"></a>

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

현재 주소 읽기·이동·새로고침·방문 기록 이동을 구별한다. 외부 스크립트 → 생성 → 열기 → 완료 콜백의 흐름과 지도 자리·로더·렌더링의 연결을 설명한다.

입력·현재 상태·실행 순서·결과를 분리해 설명한다. 실제 수업 원본은 아래에 표시하고, 원본에 없는 선택 학습은 9절 TIP에 둔다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

브라우저 관련 객체는 페이지의 글자를 바꾸는 DOM과 역할이 다르다. location.href를 읽으면 현재 주소 문자열을 얻고 다른 주소를 대입하면 이동을 요청한다. location.reload()는 현재 페이지를 다시 읽는다. history.go(-2)는 현재 탭의 방문 기록에서 두 단계 이전으로 이동을 요청한다. 기록이 부족하면 기대한 이동이 없을 수 있다.

| 코드 | 요청하는 일 | 확인할 조건 |
| --- | --- | --- |
| location.href = 주소 | 현재 문서의 이동 | 목적지와 현재 실행 페이지 |
| location.reload() | 현재 페이지 다시 읽기 | 입력·화면 상태가 유지된다고 단정하지 않음 |
| history.go(-2) | 기록 두 단계 뒤로 | 그 탭에 해당 기록이 있는지 |
| window.open(url, name, option) | 이름 있는 창·탭 열기 요청 | 브라우저 정책과 기존 이름의 창 |

외부 라이브러리는 script를 읽은 뒤 사용할 수 있는 이름과 기능을 제공한다. new kakao.Postcode의 kakao는 내가 아무 파일에서나 선언한 내장 객체가 아니다. 우편번호 스크립트가 준비되어 있어야 한다. oncomplete 함수는 주소 선택이 완료되었을 때 도구가 호출하며, 매개변수 data에 결과를 전달한다. new를 쓴 순간 이미 주소 결과를 받았다고 생각하지 않는다.

> 📚 **출처 · 본문 설명 확인:** [MDN location.href](https://developer.mozilla.org/en-US/docs/Web/API/Location/href), [history.go](https://developer.mozilla.org/en-US/docs/Web/API/History/go), [window.open](https://developer.mozilla.org/en-US/docs/Web/API/Window/open), [카카오 우편번호 공식 가이드](https://postcode.map.kakao.com/guide). 배운 기능의 뜻을 확인한 근거다. 예제·표·풀이 흐름은 수업 코드를 바탕으로 새로 작성했으며 외부 문장을 직접 인용하지 않았다. 확인일: 2026-10-28.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 스크립트.** [HTML 실행 파일](실습/책형_복습/18_JavaScript_브라우저이동과_지도우편번호.html)과 같은 폴더의 [JS 파일](실습/책형_복습/18_JavaScript_브라우저이동과_지도우편번호.js)을 함께 내려받는다. HTML을 브라우저로 열고 Console에서 결과를 확인한다. script는 필요한 HTML 뒤에 연결한다. 콘솔 출력은 페이지 본문에 자동으로 쓰이지 않는다.

**먼저 준비할 HTML · body 안:**

```html
    <button id="move" type="button">같은 문서의 연습 위치로 이동</button>
    <button id="sample" type="button">가상 주소 결과 풀이</button>
    <p id="address"></p>
    <h2 id="practice">연습 위치</h2>
```

```javascript
document.getElementById('move').addEventListener('click', function () {
    location.href = '#practice';
    console.log('같은 문서 이동');
    console.log(location.href.split('#')[1]);
});
function showAddress(data) {
    const text = data.address + ' / ' + data.zonecode;
    document.getElementById('address').textContent = text;
    console.log(text);
}
document.getElementById('sample').addEventListener('click', function () {
    showAddress({ address: '연습시 학습로 1', zonecode: '00000' });
});
```

이동 버튼은 같은 파일의 #practice로 이동한다. 전체 주소의 앞부분은 저장 위치마다 달라서 고정 출력으로 적지 않고 # 뒤 부분만 확인한다. 두 번째 버튼은 직접 만든 가상 객체를 showAddress에 넘겨 콜백의 매개변수 읽기를 연습한다. 연습시 학습로와 00000은 실재 주소 검색 결과가 아니다. 이 예제에는 카카오 스크립트와 실제 주소 검색이 없으며, 원본의 외부 서비스 동작은 아래 원본 연결에서 별도로 읽는다.

**예상 출력 또는 관찰:**

```text
같은 문서 이동
practice
연습시 학습로 1 / 00000
```

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 원본의 일부다. 원본에 의존하는 앞 선언·HTML·함수는 다음 절의 연결까지 읽는다. 주석의 잘못된 표현도 원문대로 보존하고 설명에서 교정한다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/18_map.html` 9–21행

```javascript
        window.onload = ()=> {
            document.querySelector('#btn1').addEventListener('click', ()=> {
                console.log(location)
                // 현재 주소를 알아낼 수 있는 변수
                console.log(location.href)
                // 아래와 같이 읽어 온 주소의 값을 바꿀수도 있음
                location.href = 'http://naver.com'
            })

            document.querySelector('#btn2').addEventListener('click', ()=> {
                // reload()를 사용해서 새로고침을 할 수 있음
                location.reload()
            })
```

**발췌 바로 풀이:** `location.href`를 읽으면 현재 주소를 알 수 있고, 새 주소를 대입하면 해당 주소로 이동을 시도한다. `location.reload()`는 현재 페이지를 다시 불러온다. 수업 코드의 `http://naver.com`은 이동 예시일 뿐이다. 버튼을 직접 누르면 지금 보고 있는 실습 페이지에서 벗어날 수 있다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/18_map.html` 23–39행

```javascript
            document.querySelector('#btn3').addEventListener('click', ()=> {
                console.log(history)

                // 뒤로 한 칸 가겠다는 함수
                // history.back()
                history.go(-2)
            })

            document.querySelector('#btn4').addEventListener('click', ()=> {
                const url = '17_event_form.html'
                const name = 'open 연습'
                let option = 'width=800,height=600'

                // 새로운 팝업창을 하나 띄울 수 있고 iframe처럼 보안에 좋지 않음
                // 옵션값으로 속성을 줄 수 있고 부모가 뭐 하는지 다 알 수 있음
                window.open(url, name, option)
            })
```

**발췌 바로 풀이:** `history.back()`은 한 단계 뒤로 가는 예시로 주석 처리되어 있다. **실행 중인 코드는 `history.go(-2)`**라서 방문 기록에서 두 단계 뒤로 이동을 시도한다. 이동 가능한 기록이 없으면 기대한 화면 변화가 없을 수 있다. 버튼 이름인 ‘뒤로가기’만 보고 한 단계라고 외우지 말자.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/18_map.html` 41–50행

```javascript
            document.querySelector('#btn5').addEventListener('click', ()=> {
                new kakao.Postcode({
                    oncomplete: function(data) {
                        console.log(data)
                        console.log(data.address)
                        console.log(data.zonecode)
                    }
                }).open();
            })
        }
```

**발췌 바로 풀이:** 양쪽 모두 `new kakao.Postcode(...)`를 만들고 `.open()`으로 검색 창을 요청한다. 주소 선택이 완료되면 `oncomplete`가 호출되고, 예제는 `data.address`와 `data.zonecode`를 콘솔에 출력한다. 아래 외부 스크립트를 읽지 못하면 `kakao.Postcode`도 사용할 수 없다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/18_map.html` 84–85행

```html
    <!-- 카카오 우편번호 찾기 -->
    <script src="//t1.kakaocdn.net/mapjsapi/bundle/postcode/prod/postcode.v2.js"></script>
```

**발췌 바로 풀이:** 여기서는 반환값을 입력 칸에 넣거나 서버에 저장하지 않았다. **콜백으로 받은 값의 확인**까지가 실제 코드다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/18_map.html` 64–82행

```html
    <!-- * 카카오맵 - 지도퍼가기 -->
    <!-- 1. 지도 노드 -->
    <div id="daumRoughmapContainer1784611174105" class="root_daum_roughmap root_daum_roughmap_landing"></div>

    <!--
        2. 설치 스크립트
        * 지도 퍼가기 서비스를 2개 이상 넣을 경우, 설치 스크립트는 하나만 삽입합니다.
    -->
    <script charset="UTF-8" class="daum_roughmap_loader_script" src="https://ssl.daumcdn.net/dmaps/map_js_init/roughmapLoader.js"></script>

    <!-- 3. 실행 스크립트 -->
    <script charset="UTF-8">
        new daum.roughmap.Lander({
            "timestamp" : "1784611174105",
            "key" : "r85qmeux7up",
            "mapWidth" : "640",
            "mapHeight" : "360"
        }).render();
    </script>
```

**발췌 바로 풀이:** 두 코드의 `timestamp`와 `key`는 서로 다르다. 지도 서비스가 준 값이므로 예시끼리 섞어 쓰지 않는다. 외부 서비스 코드가 실행되려면 해당 스크립트를 불러올 수 있어야 한다. 정적 지도 이미지를 누르면 링크로 이동하고, 일반 지도는 로더가 준비된 뒤 `render()`를 호출한다.

내 btn1은 location과 href를 출력한 뒤 네이버 주소로 이동한다. btn2는 새로고침, btn3의 활성 코드는 history.go(-2)다. history.back()은 주석이라 실행하지 않는다. btn4는 17_event_form.html과 창 이름·800×600 옵션을 window.open에 넘긴다. btn5는 Postcode를 만들어 open하고 oncomplete 안에서 data.address·data.zonecode를 Console에 출력한다. 입력 칸에 대입하거나 서버에 저장하는 코드는 없다.

<a id="connections"></a>

## 5. 선언·호출·파일이 연결되는 흐름

우편번호: script 로드 → 버튼 리스너 → new kakao.Postcode에 oncomplete 함수 전달 → open 요청 → 사용자가 주소 선택 → 도구가 data를 인수로 함수 호출 → Console 출력이다. 함수의 몸체는 원본 안에 모두 있고 검색 UI 자체는 외부 도구가 제공한다. 지도: 결과를 넣을 div → roughmapLoader → new daum.roughmap.Lander의 설정 → render 순서다. 지도 이미지에 링크를 건 방식은 이미지를 누르면 이동하는 별도 방식이며, 로더가 지도를 렌더링하는 방식과 구별한다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 내 주석은 주소 읽기와 대입, 새로고침을 가까이 두어 역할을 비교하기 좋다. **교정:** 새 창이 iframe처럼 무조건 보안에 좋지 않다거나 부모의 모든 정보를 알 수 있다는 일반화는 하지 않는다. 이번 원본에서 확인한 것은 주소·이름·크기 옵션 전달이다. **실습 조건:** 실제 창·탭 표시와 팝업 허용은 브라우저 정책에 영향을 받는다. **개선:** 결과를 입력 칸에 넣으려면 콜백 안에서 해당 value에 대입하는 별도 작업이 필요하다. 원본이 이미 했던 것으로 설명하지 않는다.

개선안은 원본을 수정한 결과가 아니다. 실제 오류, 수업용 단순화, 목적에 따른 선택을 구별해 판단한다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



양쪽 버튼의 핵심 동작은 거의 같아 강사님 코드를 반복하지 않는다. 지도 timestamp와 key는 서로 다른 붙여넣기 결과다. 지도 자리의 ID와 생성 설정을 한 묶음으로 읽고 다른 예시의 값을 섞지 않는다. 지도 서비스가 만든 긴 붙여넣기 HTML 전체를 내가 직접 설계한 알고리즘으로 평가하지 않는다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 시점 | 우편번호 결과가 있는가? | 실행하는 부분 |
| --- | --- | --- |
| 외부 script 준비 | 아직 없음 | 라이브러리 이름 사용 가능 |
| 버튼 클릭·open | 아직 선택 전 | 검색 창 요청 |
| 사용자가 항목 선택 | data로 전달 | oncomplete 본문 |
| 원본 콜백 실행 | Console에 관찰 | address·zonecode 읽기 |

현재 공식 가이드에서도 외부 로더와 oncomplete 연결을 확인했다. 이번 검수는 로컬 주소 조각 이동과 가상 객체 풀이만 실행했다. 실제 지도 표시·주소 검색 성공을 확인했다고 보고하지 않는다. 원본의 //로 시작하는 외부 주소는 실행 문서의 프로토콜 조건도 살펴야 하므로 파일을 직접 여는 조건과 웹으로 제공하는 조건을 혼동하지 않는다.

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| 가상 data.address 변경 | 표시 주소만 바뀜 | 함수가 받은 값을 읽음 |
| 콜백 밖에서 결과 출력 시도 | 아직 결과를 받지 못함 | 완료 시점이 다름 |
| 지도 로더 제거 | 도구 이름을 사용할 수 없을 수 있음 | 외부 정의에 의존 |
| go(-2)를 go(-1)로 | 한 단계 이전 요청 | 기록의 이동량 변경 |

kakao 또는 daum을 찾지 못하면 라이브러리 로드와 실행 순서부터 확인한다. 지도 div만 있고 지도는 없으면 로더·생성 설정·render 연결을 확인한다. 뒤로가기 변화가 없으면 현재 탭의 기록 조건을 본다. 콜백을 등록했다고 아직 선택하지 않은 주소가 생기는 것은 아니다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** 새 창과 원래 창의 메시지 교환, 팝업 차단과 외부 로드 실패 UI, 주소 결과를 서버에 저장하는 전체 흐름은 추가 학습이다. 지도 API 전체 설계를 이 붙여넣기 실습에서 배운 내용으로 확대하지 않는다.



이 절의 확장은 기본 문제의 필수 조건이 아니다. 📚 출처가 있다는 것과 수업 밖 기능이라는 것은 다른 구분이다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. 활성 뒤로가기 코드는 몇 단계 이전을 요청하는가?
2. 원본은 주소를 입력 칸에 저장하는가?
3. 가상 객체 예제는 실제 주소 검색인가?

<details>
<summary>짧은 풀이 — 먼저 답한 뒤 확인</summary>

두 단계 이전이다. 원본은 Console 출력까지만 한다. 가상 객체는 매개변수 풀이용이며 실제 검색이 아니다.

</details>

| 기능 | 먼저 볼 것 |
| --- | --- |
| 이동 | 주소·방문 기록 |
| 새 창 | 이름·옵션·브라우저 정책 |
| 외부 도구 | 로더와 실행 순서 |
| 결과 | 완료 콜백의 매개변수 |

[장별 연습문제](실습/연습문제/18_JavaScript_브라우저이동과_지도우편번호_연습문제.md)에서 예상·설명·수정을 이어 간다. 다음은 [객체와 JSON](19_JavaScript_객체와_JSON.md)이다.

<!-- 이전 색인 이동 주소 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>
<a id="section-6"></a>

[이 장의 목차](#chapter-toc)에서 현재 설명을 찾는다.
