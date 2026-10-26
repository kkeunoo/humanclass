# 07. Date — 같은 시각을 로컬 시간과 UTC로 읽기

[JavaScript 목차](README.md) · [이전: 배열](06_JavaScript_배열과_배열메서드.md) · [다음: 함수](08_JavaScript_함수와_콜백_타이머.md)

기준은 양쪽 `07_date.html`이다. 현재 시각의 숫자를 그대로 외우지 말고 **언제 만든 Date인지, 어느 시간대 기준인지, 원본을 바꾸는지**를 확인한다.

<!-- chapter-toc -->

- [1. 날짜 객체와 값 읽기](#section-1)
- [2. ISO 문자열을 잘랐을 때의 날짜](#section-2)
- [3. 실행 전후 getTime 차이](#section-3)
- [4. setHours는 시간대 표시 변환이 아니라 값 변경](#section-4)
- [5. 짧은 복습](#section-5)
- [추가로 알면 좋은 것](#section-6)

<a id="section-1"></a>

## 1. 날짜 객체와 값 읽기

new Date()는 호출 시점의 시각을 담은 객체를 만든다. now라는 변수 이름 자체에 자동 갱신 기능은 없다. 시간이 지나도 같은 now를 읽으면 저장한 시각을 읽는다. 새 현재 시각이 필요하면 다시 new Date()를 만든다.

### 강사님 코드

출처: `teacher/workspace_html/javascript/07_date.html` 8–21행 · **원본 발췌**

```javascript
    const now = new Date()
    console.log(now)

    // 년
    const y = now.getFullYear()
    console.log("년 :", y)
    
    // 월(0~11) 주의!!
    const M = now.getMonth()
    console.log("월 :", M+1)
    
    // 일
    const d = now.getDate()
    console.log("일 :", d)
```

### 내 코드

출처: `me/workspace_html/javascript/07_date.html` 8–22행 · **원본 발췌**

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

동작은 같다. getMonth()가 0–11을 돌려주므로 사람이 읽는 월에는 1을 더한다. getDate()는 요일이 아니라 **그달의 날짜**다. M과 m은 서로 다른 이름이며 원본은 M을 월, m을 분으로 사용한다.

| 원본 메서드 | 얻는 값 | 범위·단위 |
| --- | --- | --- |
| getFullYear() | 연도 | 예: 2026 |
| getMonth() | 월 인덱스 | 0–11 |
| getDate() | 일 | 1–31 |
| getHours() | 시 | 0–23 |
| getMinutes() | 분 | 0–59 |
| getSeconds() | 초 | 0–59 |
| getTime() | 기준 시각부터 경과 | 밀리초 숫자 |

위 년·월·일·시·분·초 getter는 실행 환경의 로컬 시간대를 따른다. getTime은 1970-01-01T00:00:00Z부터 경과한 밀리초다. 같은 순간의 getTime 값은 시간대 표시를 바꿔도 같다. [MDN Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)

<a id="section-2"></a>

## 2. ISO 문자열을 잘랐을 때의 날짜

### 강사님 코드

출처: `teacher/workspace_html/javascript/07_date.html` 35–40행 · **원본 발췌**

```javascript
    const iso = now.toISOString()
    console.log(iso)
    console.log(iso.split('T')[0])

    const timestamp = now.getTime()
    console.log(timestamp)
```

### 내 코드

출처: `me/workspace_html/javascript/07_date.html` 36–46행 · **원본 발췌**

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

둘 다 같은 변환이다. 내 주석의 ‘영국시간’은 **UTC 기준**으로 바로잡는다. UTC를 영국 현지 시간과 항상 같은 것으로 생각하지 않는다. toISOString() 끝의 Z는 UTC를 뜻하며, split('T')[0]은 **UTC 날짜 부분**이다. [MDN toISOString](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString)

다음은 **출력 차이를 보이기 위해 시각을 고정한 설명 예제**다. 로컬 시간대는 한국으로 가정한다.

```javascript
const sample = new Date('2026-06-29T00:30:00+09:00');
console.log(sample.getDate()); // 한국 시간대: 29
console.log(sample.toISOString()); // 2026-06-28T15:30:00.000Z
console.log(sample.toISOString().split('T')[0]); // 2026-06-28
```

같은 순간이 한국에서는 29일 새벽, UTC에서는 28일 오후다. 따라서 원본의 ISO 날짜 잘라내기를 그대로 ‘오늘의 한국 날짜’ 기능이라고 설명하지 않는다.

<a id="section-3"></a>

## 3. 실행 전후 getTime 차이

강사님 42–47행은 i<1000, 내 50–55행은 i<=1000이다. 강사님은 0–999 총 1,000회, 내 코드는 0–1000 총 1,001회 출력한다. 경과값에는 반복뿐 아니라 console.log 호출 비용과 실행 환경의 영향이 포함된다. 두 파일의 결과를 동일 작업의 정확한 속도 비교로 사용하지 않는다.

내 주석의 ‘20ms 이하면 우연, 이상이면 느림’은 일반적인 판정 기준이 아니다. 수업의 핵심은 **종료 밀리초 - 시작 밀리초**로 경과값을 구하는 구조다. 날짜 시계 변화·측정 정밀도까지 통제하는 성능 측정은 추가 학습이다.

<a id="section-4"></a>

## 4. setHours는 시간대 표시 변환이 아니라 값 변경

### 강사님 코드

출처: `teacher/workspace_html/javascript/07_date.html` 49–54행 · **원본 발췌**

```javascript
    let time = new Date('2026-06-29')
    console.log(time.toISOString())
    
    // time.setHours( 10 )
    time.setHours( now.getHours() + 9 )
    console.log(time.toISOString())
```

### 내 코드

출처: `me/workspace_html/javascript/07_date.html` 58–65행 · **원본 발췌**

```javascript
            let time = new Date('2026-06-29')
            console.log(time.toISOString())

            // 보편적으로 get이 있다면 set도 있는 경우가 많음
            // time.setHours( 10 )
            time.setHours( time.getHours() + 9 )
            time.setHours( now.getHours() + 9 )
            console.log(time.toISOString())
```

new Date('2026-06-29')처럼 날짜만 있는 이 표준 형식은 UTC 자정으로 해석된다. 한국 시간대에서는 같은 순간이 오전 9시다. setHours는 해당 Date의 **로컬 시 값 자체를 변경**하며, 24 이상을 넣으면 날짜도 넘어갈 수 있다. [MDN setHours](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setHours)

강사님은 now의 시+9를 time의 시로 설정한다. 이는 time에 항상 9시간을 더하는 코드가 아니다. 내 코드는 먼저 time의 시+9를 설정하고, 다음 줄에서 다시 now의 시+9로 설정한다. 두 줄이 연달아 실행되므로 별개 예시처럼 해석하면 안 된다. time.getHours()를 쓰는 첫 줄이 ‘그 날짜의 현재 시에서 9 더하기’ 의도에는 맞지만, 이 둘을 시간대 변환 공식으로 사용하지 않는다.

한국 시간대에서 now의 시가 10이라고 가정하면 time은 처음 6월 29일 09시다. 내 첫 setHours 후 18시, 다음 setHours 후 19시가 된다. 강사님은 곧바로 19시다. now의 시가 20이면 29시를 설정하게 되어 다음 날 05시가 된다. 어느 결과도 무조건 현재 날짜를 뜻하지 않는다.

<a id="section-5"></a>

## 5. 짧은 복습

1. getMonth()가 5라면 실제 월은?
2. 한국 새벽 0시 30분에 ISO 날짜만 잘랐을 때 하루 전 날짜가 나올 수 있는가?
3. now를 만든 뒤 1분 기다리면 now.getMinutes()도 자동으로 증가하는가?

<details>
<summary>정답 확인</summary>

1. 6월.
2. 가능하다. ISO는 UTC 기준이기 때문이다.
3. 아니다. now에 저장된 시각을 읽는다.

</details>

<a id="section-6"></a>

## 추가로 알면 좋은 것

Intl 지역화 출력, performance.now 기반 성능 측정, 시간대·일광절약시간 전체 설계, 새로운 날짜 API는 추가 학습이다. 기본 복습에서는 원본 getter·ISO·getTime·setHours의 동작 차이에 집중한다.

