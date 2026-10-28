# 22. 웹훅으로 POST 요청 보내기

[JavaScript 목차](README.md) · [이전: 외부 AI API 요청](21_JavaScript_외부AI_API요청과_대화기록.md)

양쪽 `22_discord.html`은 텍스트 입력을 읽고 Discord 웹훅 형식의 JSON 요청 본문을 만드는 연습이다. **원본의 웹훅 주소는 다시 사용할 수 있는 전송 주소일 수 있어 이 문서에 옮기지 않는다.** 실제 메시지 전송도 실행하지 않았다. 수업에서 확인되는 요청 구성만 살핀다.

**POST 요청 본문이란?** 서버로 보낼 내용을 객체로 준비하고, 실제 전송할 문자열로 바꾼 값이다. 아래는 전송하지 않는 **설명용 작은 예제**다.

```javascript
const param = { username: '연습', content: '안녕하세요' };
const body = JSON.stringify(param);
console.log(body); // {"username":"연습","content":"안녕하세요"}
```

`param`은 객체, `body`는 문자열이다. 수업 원본은 이 문자열을 `XMLHttpRequest.send(...)`에 전달한다. 주소를 다루는 단계와 응답을 확인하는 단계는 아래의 강사님·내 원본 발췌로 구분한다.

<!-- chapter-toc -->

- [1. 클릭에서 요청 본문까지](22_JavaScript_웹훅_POST요청.md#section-1)
- [2. 앞 장과 연결하기](22_JavaScript_웹훅_POST요청.md#section-2)
- [직접 확인할 질문](22_JavaScript_웹훅_POST요청.md#section-3)
- [추가로 알면 좋은 것](22_JavaScript_웹훅_POST요청.md#section-4)

<a id="section-1"></a>

## 1. 클릭에서 요청 본문까지

양쪽 코드 모두 버튼 클릭 때 `#prompt.value`를 읽고, `XMLHttpRequest`를 만든 뒤 `open('post', url)`로 전송 주소를 지정한다. 원본의 18행에 `url` 선언이 있으나 주소 자체는 여기서 생략한다.

### 강사님 코드 — 주소 다음 부분의 원본 발췌

출처: `teacher/workspace_html/javascript/22_discord.html` 20~35행 · **원본 발췌**

```javascript
                const xhr = new XMLHttpRequest()
                xhr.open('post', url)

                xhr.setRequestHeader('Content-Type', 'application/json')
                const param = {
                    username: '쵬니수', // 80자 제한
                    content: prompt
                }

                xhr.send( JSON.stringify(param) )

                xhr.onload = function(){
                    console.log(xhr.responseText)
                }

            })
```

### 내 코드 — 주소 다음 부분의 원본 발췌

출처: `me/workspace_html/javascript/22_discord.html` 20~35행 · **원본 발췌**

```javascript
                const xhr = new XMLHttpRequest()
                xhr.open('post', url)

                xhr.setRequestHeader('Content-Type','application/json')
                // discord에 보내기 위한 파라미터 양식
                const param = {
                    username: 'zl존법사v',
                    content: prompt
                }

                xhr.send( JSON.stringify(param) )

                xhr.onload = function() {
                    console.log(xhr.responseText)
                }
            })
```

`setRequestHeader('Content-Type', 'application/json')`은 요청 본문 형식을 알린다. `param` 객체의 `username`과 `content`를 `JSON.stringify(param)`으로 문자열로 만들어 `send`에 넘긴다. 내 코드는 username을 내 실습 이름으로 바꿨고, 나머지 흐름은 강사님과 같다. `xhr.onload`는 응답이 돌아온 뒤 `responseText`를 콘솔에 기록한다. 이것만으로 Discord에 실제 메시지가 도착했는지까지 검증하지는 않는다.

<a id="section-2"></a>

## 2. 앞 장과 연결하기

19장은 객체를 JSON 문자열로 바꾸는 `JSON.stringify`, 20장은 `XMLHttpRequest`의 `open`·`send`·`onload`, 21장은 `fetch`로 POST 요청을 만드는 예제를 다뤘다. 이번 실습은 **객체 → JSON 문자열 → POST 요청** 순서를 함께 사용한다.

내 HTML의 버튼은 `type="buttn"`이라고 적혀 있다. `type="button"`으로 고치는 것이 맞다. 버튼 클릭 리스너를 붙이는 코드 자체는 원본에 있다.

<a id="section-3"></a>

## 직접 확인할 질문

1. `param` 객체와 `JSON.stringify(param)`의 결과는 자료형이 어떻게 다를까?
2. `Content-Type` 헤더는 무엇을 알릴까?
3. 응답 본문을 콘솔에 찍는 것과 메시지 전송 성공을 확인하는 것은 같은 일일까?

<a id="section-4"></a>

## 추가로 알면 좋은 것

웹훅 주소는 알게 된 사람이 메시지를 보낼 수 있는 주소이므로 공개 Wiki에 직접 넣지 않는다. 실제 서비스에서는 전송 성공 여부와 실패 응답도 검사한다. 이 수업 원본에는 그런 검사가 없다.

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/22_JavaScript_웹훅_POST요청_연습문제.md) → [다음: 실무 코딩 스타일](23_JavaScript_실무_코딩스타일.md)

