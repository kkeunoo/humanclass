# 07. Date — 저장한 한 순간과 시간대 표시

[JavaScript 목차](README.md) · [읽기 안내](00_JavaScript_V3_동작_백과_읽기법.md)

현재 시각을 읽었다고 그 변수가 자동 시계가 되는 것은 아니다. Date가 담은 순간, 읽는 시간대, 값을 바꾸는 메서드를 나누면 날짜가 하루 다르게 나오는 이유를 설명할 수 있다.

<a id="chapter-toc"></a>

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

로컬 getter·UTC ISO·밀리초를 구분한다. getMonth의0시작과 setHours의 실제 값 변경, 원본 연속 대입을 추적한다.

입력·현재 상태·실행 순서·결과를 분리해 설명한다. 실제 수업 원본은 아래에 표시하고, 원본에 없는 선택 학습은 9절 TIP에 둔다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

new Date()는 호출 시점의 한 순간을 담은 객체를 만든다. now라는 이름에 자동 갱신 기능은 없다. 나중의 현재 시각이 필요하면 다시 만든다. 한 순간을 읽는 로컬 getter와 UTC문자열은 표시 기준이 달라 날짜가 다를 수 있다.

| 메서드 | 얻는 값·단위 |
| --- | --- |
| getFullYear |로컬 연도 |
| getMonth |로컬 월0~11,표시는+1 |
| getDate |로컬 그달 날짜1~31 |
| getHours·getMinutes·getSeconds |로컬 시·분·초 |
| getTime |1970-01-01T00:00:00Z부터 밀리초 |
| toISOString |UTC표시 문자열,끝Z |
| setHours |로컬 시 값 변경 |

한국의6월29일00:30은 UTC의6월28일15:30과 같은 순간이다. ISO를T로 나눠 앞부분만 읽으면 UTC날짜이지 항상 오늘의 한국 날짜가 아니다. UTC를 영국 현지 시간과 항상 같은 것으로 외우지도 않는다.

날짜만 있는 표준 문자열 '2026-06-29'는 UTC자정으로 해석한다. 반면 setHours는 표시 이름만 바꾸는 것이 아니라 객체가 가진 시각을 변경한다.24이상 값을 주면 날짜도 넘어갈 수 있다.

> 📚 **출처 · 본문 설명 확인:** [MDN Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date), [toISOString](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString), [setHours](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setHours). 배운 기능의 뜻을 확인한 근거다. 예제·표·풀이 흐름은 수업 코드를 바탕으로 새로 작성했으며 외부 문장을 직접 인용하지 않았다. 확인일: 2026-10-28.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 스크립트.** [HTML 실행 파일](실습/책형_복습/07_JavaScript_Date와_날짜처리.html)과 같은 폴더의 [JS 파일](실습/책형_복습/07_JavaScript_Date와_날짜처리.js)을 함께 내려받는다. HTML을 브라우저로 열고 Console에서 결과를 확인한다. script는 필요한 HTML 뒤에 연결한다. 콘솔 출력은 페이지 본문에 자동으로 쓰이지 않는다.

```javascript
const sample = new Date('2026-06-29T00:30:00+09:00');
console.log(sample.toISOString());
console.log(sample.toISOString().split('T')[0]);
const dateOnly = new Date('2026-06-29');
console.log(dateOnly.toISOString());
```

실행할 때마다 다른 현재값 대신 순간을 고정했다. +09:00이 있는 첫 문자열은 한국00:30과 같은 순간을 지정하고 ISO는UTC로 표현한다. dateOnly는 날짜 전용 형식의UTC자정이다. 이 예제의ISO출력은 실행기기 시간대에 의존하지 않지만 getDate·getHours를 더하면 로컬 시간대 조건을 별도로 적어야 한다.

**예상 출력 또는 관찰:**

```text
2026-06-28T15:30:00.000Z
2026-06-28
2026-06-29T00:00:00.000Z
```

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 원본의 일부다. 원본에 의존하는 앞 선언·HTML·함수는 다음 절의 연결까지 읽는다. 주석의 잘못된 표현도 원문대로 보존하고 설명에서 교정한다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/07_date.html` 8–22행

```javascript
            const now = new Date();
            console.log(now)

            // now를 썼을 때 표시하기 위한 양식
            // 년
            const y = now.getFullYear()
            console.log("년 : ", y)

            // 월(0~11까지 나옴, 배열과 같이)
            const M = now.getMonth()
            console.log("월 : ", M+1)

            // 일 출력
            const d = now.getDate()
            console.log("일 : ", d)
```

**발췌 바로 풀이:** 동작은 같다. getMonth()가 0–11을 돌려주므로 사람이 읽는 월에는 1을 더한다. getDate()는 요일이 아니라 **그달의 날짜**다. M과 m은 서로 다른 이름이며 원본은 M을 월, m을 분으로 사용한다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/07_date.html` 36–46행

```javascript
            // 년-월-일T시:분:초.밀리세컨드 (iso는 영국시간 UTC세계협정시 기준)
            const iso = now.toISOString()
            console.log(iso)
            console.log(iso.split('T')[0])
            // let date = iso.split('T')
            // console.log(date[0])

            // 1970년도 1월 1일 00시 00분 00초(UTC)부터 현재까지 흐른 밀리초의 총합
            // 1783667295(초) 970(밀리초) = 1783667295970 (epoch사이트에서 변환해줌)
            const timestamp = now.getTime()
            console.log(timestamp)
```

**발췌 바로 풀이:** 둘 다 같은 변환이다. 내 주석의 ‘영국시간’은 **UTC 기준**으로 바로잡는다. UTC를 영국 현지 시간과 항상 같은 것으로 생각하지 않는다. toISOString() 끝의 Z는 UTC를 뜻하며, split('T')[0]은 **UTC 날짜 부분**이다. [MDN toISOString](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString)

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/07_date.html` 58–65행

```javascript
            let time = new Date('2026-06-29')
            console.log(time.toISOString())

            // 보편적으로 get이 있다면 set도 있는 경우가 많음
            // time.setHours( 10 )
            time.setHours( time.getHours() + 9 )
            time.setHours( now.getHours() + 9 )
            console.log(time.toISOString())
```

**발췌 바로 풀이:** new Date('2026-06-29')처럼 날짜만 있는 이 표준 형식은 UTC 자정으로 해석된다. 한국 시간대에서는 같은 순간이 오전 9시다. setHours는 해당 Date의 **로컬 시 값 자체를 변경**하며, 24 이상을 넣으면 날짜도 넘어갈 수 있다. [MDN setHours](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setHours)

내 now는 실행 시각을 저장하고 getMonth()+1로 사람이 읽는 월을 만든다. M과 m은 서로 다른 이름이며 월·분으로 구분했다. ISO 발췌의 split(T)[0]은 UTC 날짜다. getTime은 시작과 끝을 빼 경과 밀리초를 계산한다. 내 setHours는 time.getHours()+9를 설정한 뒤 now.getHours()+9로 또 설정한다. 두 줄을 별도 예시처럼 읽으면 현재 최종값을 틀리게 예상한다.

<a id="connections"></a>

## 5. 선언·호출·파일이 연결되는 흐름

Date 생성 → 객체에 저장된 순간 → getter 또는 ISO 변환 → 문자열 split → 출력 순서다. 원본 now와 time은 다른 객체다. now.getHours()+9를 time에 설정하는 것은 time에 항상 9시간을 더하는 연산이 아니다. getTime 반환은 숫자 밀리초이고 toISOString 반환은 문자열이라 뒤에 붙일 처리가 다르다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 월+1·밀리초·get/set 대응을 주석으로 남겼다. **교정:** UTC를 영국 시간으로 고정하지 않고 setHours를 시간대 변환 공식으로 쓰지 않는다. **비교 조건:** 강사님 i<1000은1000회, 나는 i<=1000이라1001회 출력한다. 로그 비용·환경이 포함된 경과값을 같은 작업의 정밀 성능 비교로 평가하지 않는다.20ms 경계를 일반 속도 법칙으로 삼지도 않는다.

개선안은 원본을 수정한 결과가 아니다. 실제 오류, 수업용 단순화, 목적에 따른 선택을 구별해 판단한다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



getter·ISO 핵심은 같아 중복 인용을 생략한다. 차이는 내 setHours 한 줄이 추가되어 연속 값 변경이 생긴다는 점과 반복 횟수다. 같은 현재 시각을 사용했다고 모든 연산이 같은 날짜·같은 작업량을 가지는 것은 아니다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 한국 시간대·now의 시가10인 별도 조건 | time의 로컬 시각 |
| --- | --- |
| 날짜전용생성 |6월29일09시 |
| 내첫setHours(time시+9) |6월29일18시 |
| 내다음setHours(now시+9) |6월29일19시 |
| 강사님now시+9만설정 |곧바로6월29일19시 |

now의 시가20이면29시를 설정해 다음 날05시로 넘어갈 수 있다. 날짜 객체의 현재값·사용한 인수·실행 순서가 모두 필요하다. 위 조건 없이 현재 날짜를 고정 정답으로 적지 않는다.

| 한 가지 변경 | 예상 | 기준 |
| --- | --- | --- |
| 첫문자열시만09:30으로 |UTC같은날00:30 |9시간차이 |
| 원래UTC날짜부분만확인 |6월28일 |로컬날짜와다름 |
| now생성후기다리기 |저장값자동갱신안됨 |새생성필요 |

날짜가 하루 다르면 시스템 시각이 틀렸다고 단정하지 말고 UTC와 로컬을 먼저 구분한다. 월이 하나 작으면 getMonth의0 시작을 확인한다. 시계가 멈춘 것처럼 보이면 Date를 언제 생성했는지 본다. 타이머로 새 시각을 읽는 것은 다음 함수·타이머 장에서 연결한다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** Intl 지역화·performance.now 측정·시간대와 일광절약시간 전체 설계·새 날짜 API는 추가 학습이다. Date 기본과 원본 getter·ISO·setHours의 차이를 먼저 익힌다.



이 절의 확장은 기본 문제의 필수 조건이 아니다. 📚 출처가 있다는 것과 수업 밖 기능이라는 것은 다른 구분이다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. getMonth가5면 몇 월인가?
2. ISO 날짜가 한국 날짜보다 하루 전일 수 있는가?
3. now를1분 뒤 읽으면 자동으로 시각이 갱신되는가?

<details>
<summary>짧은 풀이 — 먼저 답한 뒤 확인</summary>

6월이다. 한국 새벽에는 UTC가 전날일 수 있다. now는 만든 순간을 유지하므로 새 현재값이 필요하면 다시 Date를 만든다.

</details>

| 구분 | 핵심 |
| --- | --- |
| 로컬값 | get년월일시분초 |
| UTC문자열 | ISO·Z |
| 경과단위 | getTime의밀리초 |
| 실제변경 | setHours |

[장별 연습문제](실습/연습문제/07_JavaScript_Date와_날짜처리_연습문제.md)에서 예상·설명·수정을 이어 간다. 다음은 [함수](08_JavaScript_함수와_콜백_타이머.md)다.

<!-- 이전 색인 이동 주소 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>
<a id="section-6"></a>

[이 장의 목차](#chapter-toc)에서 현재 설명을 찾는다.
