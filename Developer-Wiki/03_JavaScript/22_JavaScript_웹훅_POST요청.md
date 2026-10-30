# 22. 웹훅 POST — 보낼 내용을 만들고 전송 단계와 구별하기

[JavaScript 목차](README.md) · [읽기 안내](00_JavaScript_V3_동작_백과_읽기법.md)

웹훅 실습은 메시지 입력을 객체로 묶고 JSON 문자열로 만들어 지정한 주소에 보내는 흐름이다. 객체가 잘 만들어졌다는 것, 요청을 보냈다는 것, 서비스가 처리했다는 것은 각각 다른 확인이다.

<a id="chapter-toc"></a>

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

username·content 객체와 JSON 문자열의 차이를 설명한다. open → 헤더 지정 → send → 응답 처리의 순서를 읽고, 본문 미리 보기와 실제 메시지 전달 성공을 구별한다.

입력·현재 상태·실행 순서·결과를 분리해 설명한다. 실제 수업 원본은 아래에 표시하고, 원본에 없는 선택 학습은 9절 TIP에 둔다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

이 수업에서 사용하는 Discord 웹훅은 정해진 채널로 메시지를 보낼 때 사용하는 주소에 요청하는 방식이다. 사용자 입력을 보낼 본문과 목적지 주소는 다른 정보다. username은 이 예제의 표시 이름, content는 보낼 글이다. username을 적었다고 Discord 계정에 로그인하는 것은 아니다.

| 코드 | 역할 | 자료형·시점 |
| --- | --- | --- |
| prompt.value | 현재 입력 글 | 문자열 |
| param | 이름과 내용을 묶음 | 객체 |
| JSON.stringify(param) | 전송할 JSON 표현 | 문자열 |
| xhr.open('post', url) | 요청 방식·목적지 준비 | 아직 send 전 |
| setRequestHeader | 본문 형식 등 요청 정보 | open 뒤, send 전 |
| xhr.send(body) | 요청 시작 | 성공 처리는 아직 확인 전 |

Content-Type을 application/json으로 지정해 본문 표현 형식을 알린다. 헤더만 지정하고 실제 본문을 다른 형식으로 만들면 일치하지 않는다. 반대로 stringify가 전송까지 대신하는 것은 아니다. 이 함수는 문자열을 만들 뿐이며 요청 시작은 send의 일이다.

> 📚 **출처 · 본문 설명 확인:** [Discord 웹훅 공식 문서](https://docs.discord.com/developers/resources/webhook), [MDN setRequestHeader](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/setRequestHeader). 배운 기능의 뜻을 확인한 근거다. 예제·표·풀이 흐름은 수업 코드를 바탕으로 새로 작성했으며 외부 문장을 직접 인용하지 않았다. 확인일: 2026-10-28.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 스크립트.** [HTML 실행 파일](실습/책형_복습/22_JavaScript_웹훅_POST요청.html)과 같은 폴더의 [JS 파일](실습/책형_복습/22_JavaScript_웹훅_POST요청.js)을 함께 내려받는다. HTML을 브라우저로 열고 Console에서 결과를 확인한다. script는 필요한 HTML 뒤에 연결한다. 콘솔 출력은 페이지 본문에 자동으로 쓰이지 않는다.

**먼저 준비할 HTML · body 안:**

```html
    <label>메시지 연습 <input id="prompt" value="안녕하세요"></label>
    <button id="preview" type="button">본문 미리 보기</button>
    <pre id="result"></pre>
```

```javascript
function makePayload(text) {
    return { username: '연습', content: text };
}
document.getElementById('preview').addEventListener('click', function () {
    const text = document.getElementById('prompt').value;
    const param = makePayload(text);
    const body = JSON.stringify(param);
    document.getElementById('result').textContent = body;
    console.log(typeof param, typeof body);
    console.log(body);
});
```

미리 보기 버튼은 입력을 makePayload에 넘긴다. 함수는 두 속성을 가진 객체를 반환하고, 콜백은 stringify하여 화면과 Console에 표시한다. 미리 보기에는 웹훅 주소와 send 호출이 없으므로 메시지를 전송하지 않는다. 예상 출력은 객체·문자열 변환의 결과이며 전송 성공 메시지가 아니다. 원본의 전송 연결은 아래 실제 코드에서 별도로 읽는다.

**예상 출력 또는 관찰:**

```text
object string
{"username":"연습","content":"안녕하세요"}
```

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 원본의 일부다. 원본에 의존하는 앞 선언·HTML·함수는 다음 절의 연결까지 읽는다. 주석의 잘못된 표현도 원문대로 보존하고 설명에서 교정한다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/22_discord.html` 20–35행

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

**발췌 바로 풀이:** `setRequestHeader('Content-Type', 'application/json')`은 요청 본문 형식을 알린다. `param` 객체의 `username`과 `content`를 `JSON.stringify(param)`으로 문자열로 만들어 `send`에 넘긴다. 내 코드는 username을 내 실습 이름으로 바꿨고, 나머지 흐름은 강사님과 같다. `xhr.onload`는 응답이 돌아온 뒤 `responseText`를 콘솔에 기록한다. 이것만으로 Discord에 실제 메시지가 도착했는지까지 검증하지는 않는다.

양쪽 원본은 버튼 클릭 때 prompt를 읽고 url을 준비한 뒤 XMLHttpRequest를 만든다. open의 post로 목적지를 정하고 Content-Type을 지정한다. 내 param의 username은 내 연습 이름이며 content는 현재 prompt다. stringify한 본문을 send하고 onload에서 responseText를 Console에 기록한다. 웹훅 주소 자체는 재사용 가능한 전송 수단이라 공개 문서에 옮기지 않았으며 이번에도 실제 전송하지 않았다.

<a id="connections"></a>

## 5. 선언·호출·파일이 연결되는 흐름

HTML의 prompt·버튼 → load 때 클릭 등록 → 현재 value 읽기 → param 객체 → JSON 문자열 → open·헤더·send → 나중 onload 순서다. 19장의 객체 변환, 20장의 요청·응답, 21장의 POST 본문 구성을 함께 사용한다. 새 makePayload는 문자열을 받아 객체를 반환하는 설명용 함수이며 원본에 있었던 이름으로 소개하지 않는다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 내 주석은 보낼 두 필드의 양식을 짚고 JSON 문자열을 send에 넘긴다. **공통 한계:** 응답 본문 출력만으로 메시지 도착까지 판정하지 않는다. 서비스가 본문 없는 응답을 보낼 수도 있으므로 빈 문자열을 무조건 실패로 읽지 않는다. **HTML 교정:** type=buttn은 button으로 고친다. **개선 방향:** 입력 검사와 성공·실패 표시를 추가할 수 있지만 원본이 이미 처리한 것과 구별한다.

개선안은 원본을 수정한 결과가 아니다. 실제 오류, 수업용 단순화, 목적에 따른 선택을 구별해 판단한다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



양쪽은 username 문자열을 제외하면 같은 흐름이어서 강사님 코드를 반복하지 않는다. 표시 이름 차이는 개인 선택이며 품질 우열로 평가하지 않는다. 원본 주석의 글자 수 제한처럼 서비스 규칙은 현재 공식 문서를 확인할 항목이지 이 장의 변하지 않는 언어 문법으로 외우지 않는다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 확인 단계 | 코드만으로 확인 가능한 것 | 아직 확인하지 않은 것 |
| --- | --- | --- |
| 객체 생성 | username·content 값 | 요청 전송 |
| stringify | JSON 문자열 결과 | 서버 수신 |
| send 호출 | 요청을 시작하는 코드 | 메시지 생성 성공 |
| onload | 응답을 읽는 처리 | 실제 채널의 표시 결과 |

현재 공식 문서는 웹훅 실행의 요청 필드와 응답 동작을 구분한다. 이 장은 실제 전송을 재현하지 않고 원본 요청 구성과 로컬 본문 미리 보기만 검증했다. 수업 코드의 주소를 다시 쓰거나 메시지를 보내며 확인한 것으로 보고하지 않는다.

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| 입력을 다른 글로 변경 | content 문자열만 변경 | 클릭 때 현재 값 읽기 |
| 표시 이름 변경 | username만 변경 | 객체 속성 값 차이 |
| 입력에 큰따옴표 포함 | JSON 출력에서 필요한 이스케이프 | stringify가 형식 구성 |
| body를 표시만 하기 | 네트워크 요청 없음 | 문자열 생성과 전송은 별개 |

표시는 되는데 전달이 안 된다는 판단 전에 예제가 미리 보기인지 실제 send가 있는지 확인한다. JSON 문자열을 손으로 이어 붙이지 말고 객체를 stringify한 결과를 관찰한다. 응답이 빈 글자여도 본문 유무만으로 성공·실패를 결정하지 않는다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** 웹훅 주소 보관·서버 중계·상태 코드 확인·실패 안내·재시도와 중복 전송 제어는 추가 학습이다. 본문의 필수 범위는 실제 작성한 POST 요청 구성이다.



이 절의 확장은 기본 문제의 필수 조건이 아니다. 📚 출처가 있다는 것과 수업 밖 기능이라는 것은 다른 구분이다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. stringify만 호출하면 전송되는가?
2. 헤더 지정은 open과 send 사이 중 어디인가?
3. 미리 보기 출력이 실제 채널 도착의 증거인가?

<details>
<summary>짧은 풀이 — 먼저 답한 뒤 확인</summary>

문자열만 만들어지며 전송은 별도다. open 뒤 send 전에 지정한다. 미리 보기는 요청 본문의 확인일 뿐 실제 전달의 증거가 아니다.

</details>

| 구별 | 확인 |
| --- | --- |
| 객체 | 필드와 값 |
| 문자열 | JSON 표현 |
| 요청 | 방식·주소·헤더·본문 |
| 결과 | 응답과 실제 처리 |

[장별 연습문제](실습/연습문제/22_JavaScript_웹훅_POST요청_연습문제.md)에서 예상·설명·수정을 이어 간다. 다음은 [실무 코딩 스타일](23_JavaScript_실무_코딩스타일.md)이다.

<!-- 이전 색인 이동 주소 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>

[이 장의 목차](#chapter-toc)에서 현재 설명을 찾는다.
