# 18. 브라우저 이동과 지도·우편번호 예제

[JavaScript 목차](README.md) · [이전: 메뉴·Todo 실습](17-04_JavaScript_메뉴와_Todo실습.md)

파일 이름은 `18_map.html`이지만 실제 수업 내용은 **주소 이동·새로고침·방문 기록·새 창**, 그리고 **외부 지도·우편번호 스크립트 사용**이다. 강사님과 내 원본의 버튼 동작은 거의 같다. 외부 서비스는 네트워크와 서비스 상태에 따라 달라질 수 있으므로 코드에서 확인되는 범위까지만 설명한다.

<!-- chapter-toc -->

- [1. 현재 페이지 이동과 다시 불러오기](#section-1)
- [2. 방문 기록과 새 창](#section-2)
- [3. 우편번호 검색 결과 읽기](#section-3)
- [4. 지도를 붙이는 두 방식](#section-4)
- [직접 확인할 질문](#section-5)
- [추가로 알면 좋은 것](#section-6)

<a id="section-1"></a>

## 1. 현재 페이지 이동과 다시 불러오기

### 강사님 코드

출처: `teacher/workspace_html/javascript/18_map.html` 8~17행 · **원본 발췌**

```javascript
    window.onload = ()=>{
        document.querySelector('#btn1').addEventListener('click', ()=>{
            console.log(location)
            console.log(location.href)
            location.href = 'http://naver.com'
        })

        document.querySelector('#btn2').addEventListener('click', ()=>{
            location.reload()
        })
```

### 내 코드

출처: `me/workspace_html/javascript/18_map.html` 9~21행 · **원본 발췌**

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

`location.href`를 읽으면 현재 주소를 알 수 있고, 새 주소를 대입하면 해당 주소로 이동을 시도한다. `location.reload()`는 현재 페이지를 다시 불러온다. 수업 코드의 `http://naver.com`은 이동 예시일 뿐이다. 버튼을 직접 누르면 지금 보고 있는 실습 페이지에서 벗어날 수 있다.

<a id="section-2"></a>

## 2. 방문 기록과 새 창

### 강사님 코드

출처: `teacher/workspace_html/javascript/18_map.html` 18~31행 · **원본 발췌**

```javascript
        document.querySelector('#btn3').addEventListener('click', ()=>{
            console.log(history)
            
            // history.back()
            history.go(-2)
        })

        document.querySelector('#btn4').addEventListener('click', ()=>{
            const url = '17_event_form.html'
            const name = 'open 연습'
            let option = 'width=800,height=600'

            window.open(url, name, option)
        })
```

### 내 코드

출처: `me/workspace_html/javascript/18_map.html` 23~39행 · **원본 발췌**

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

`history.back()`은 한 단계 뒤로 가는 예시로 주석 처리되어 있다. **실행 중인 코드는 `history.go(-2)`**라서 방문 기록에서 두 단계 뒤로 이동을 시도한다. 이동 가능한 기록이 없으면 기대한 화면 변화가 없을 수 있다. 버튼 이름인 ‘뒤로가기’만 보고 한 단계라고 외우지 말자.

`window.open(url, name, option)`은 `17_event_form.html`을 새 브라우저 창이나 탭으로 열도록 요청한다. `name`은 창 이름, `option`은 너비·높이 설정이다. 실제 표시 방식은 브라우저의 팝업 정책에 달려 있다. 내 주석의 “iframe처럼 보안에 좋지 않음”은 이 코드만으로 증명되는 일반 규칙이 아니다. 이번 학습에서는 **새 창을 열고 주소·이름·크기 옵션을 넘긴다**는 데 집중한다.

<a id="section-3"></a>

## 3. 우편번호 검색 결과 읽기

### 강사님 코드

출처: `teacher/workspace_html/javascript/18_map.html` 32~41행 · **원본 발췌**

```javascript
        document.querySelector('#btn5').addEventListener('click', ()=>{
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

### 내 코드

출처: `me/workspace_html/javascript/18_map.html` 41~50행 · **원본 발췌**

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

양쪽 모두 `new kakao.Postcode(...)`를 만들고 `.open()`으로 검색 창을 요청한다. 주소 선택이 완료되면 `oncomplete`가 호출되고, 예제는 `data.address`와 `data.zonecode`를 콘솔에 출력한다. 아래 외부 스크립트를 읽지 못하면 `kakao.Postcode`도 사용할 수 없다.

### 원본의 외부 스크립트

출처: `me/workspace_html/javascript/18_map.html` 84~85행 · **원본 발췌**

```javascript
    <!-- 카카오 우편번호 찾기 -->
    <script src="//t1.kakaocdn.net/mapjsapi/bundle/postcode/prod/postcode.v2.js"></script>
```

여기서는 반환값을 입력 칸에 넣거나 서버에 저장하지 않았다. **콜백으로 받은 값의 확인**까지가 실제 코드다.

<a id="section-4"></a>

## 4. 지도를 붙이는 두 방식

양쪽 HTML에는 지도 이미지에 링크를 건 부분과, 지도용 빈 `div`를 준비한 뒤 외부 스크립트로 렌더링하는 부분이 있다. 긴 이미지 지도 HTML은 지도 서비스가 만들어 준 붙여넣기 코드다. 실제 수업에서 직접 다룬 핵심은 아래처럼 **지도 자리·로더·렌더링 코드가 연결된다**는 점이다.

### 강사님 코드

출처: `teacher/workspace_html/javascript/18_map.html` 54~73행 · **원본 발췌**

```javascript
    <!-- 일반 지도 -->
<!-- * 카카오맵 - 지도퍼가기 -->
<!-- 1. 지도 노드 -->
<div id="daumRoughmapContainer1784611170515" class="root_daum_roughmap root_daum_roughmap_landing"></div>

<!--
	2. 설치 스크립트
	* 지도 퍼가기 서비스를 2개 이상 넣을 경우, 설치 스크립트는 하나만 삽입합니다.
-->
<script charset="UTF-8" class="daum_roughmap_loader_script" src="https://ssl.daumcdn.net/dmaps/map_js_init/roughmapLoader.js"></script>

<!-- 3. 실행 스크립트 -->
<script charset="UTF-8">
	new daum.roughmap.Lander({
		"timestamp" : "1784611170515",
		"key" : "rkqpeyht8az",
		"mapWidth" : "640",
		"mapHeight" : "360"
	}).render();
</script>
```

### 내 코드

출처: `me/workspace_html/javascript/18_map.html` 64~82행 · **원본 발췌**

```javascript
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

두 코드의 `timestamp`와 `key`는 서로 다르다. 지도 서비스가 준 값이므로 예시끼리 섞어 쓰지 않는다. 외부 서비스 코드가 실행되려면 해당 스크립트를 불러올 수 있어야 한다. 정적 지도 이미지를 누르면 링크로 이동하고, 일반 지도는 로더가 준비된 뒤 `render()`를 호출한다.

<a id="section-5"></a>

## 직접 확인할 질문

1. ‘뒤로가기’ 버튼은 실제로 방문 기록 몇 단계 뒤를 요청할까?
2. 우편번호 창에서 선택한 주소는 원본 코드의 어디에 표시될까?
3. 지도 `div`만 복사하고 로더·렌더링 코드를 빼면 지도가 나타날까?

<a id="section-6"></a>

## 추가로 알면 좋은 것

새 창과 원래 창 사이에 데이터를 주고받거나 외부 서비스의 실패 상태를 처리하는 방법은 이 수업 원본에서 다루지 않았다. 실제 서비스에서는 팝업 차단, 외부 스크립트 불러오기 실패 등도 고려한다.

