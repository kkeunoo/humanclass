# 10. 문자열 — 찾고 자르고 바꾼 결과를 사용하기

[JavaScript 목차](README.md) · [읽기 안내](00_JavaScript_V3_동작_백과_읽기법.md)

문자열은 글자 데이터다. 위치를 찾고 일부를 자르고 다른 글자로 바꿀 수 있지만 메서드를 호출한 것만으로 원본 문자열 자체가 바뀌지는 않는다. 반환한 결과를 어디에 저장하고 다음에 쓰는지 따라간다.

<a id="chapter-toc"></a>

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

인덱스·길이·부분 문자열·변환 결과를 구분한다. trim과 취소 확인, 이메일 가리기의 누적·입력 한계를 설명한다.

입력·현재 상태·실행 순서·결과를 분리해 설명한다. 실제 수업 원본은 아래에 표시하고, 원본에 없는 선택 학습은 9절 TIP에 둔다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

문자열 인덱스도0부터 시작하고 공백도 위치에 포함된다. 원본 ‘기사도가 죽었을 리가’의 길이는11, '죽었'의 시작은5, 첫'가'는3이며 없는'나'의indexOf는-1이다. 수업의 이 문자열은 글자와 위치를 세어 이해할 수 있지만 모든 이모지·복합문자가 항상 길이1인 것은 아니라는 상세는 TIP으로 둔다.

| 메서드 | 역할 | 원본 예 |
| --- | --- | --- |
| slice(시작,끝) |시작 포함·끝 제외 |slice(3,6)='가 죽' |
| substring(시작,끝) |양수범위에선위와같은결과 |음수처리는다름 |
| substr(시작,개수) |지정개수추출 |substr(3,7)='가 죽었을 리' |
| split(' ') |공백으로나눈배열 |기사도가/죽었을/리가 |
| replace(문자열,새문자) |처음일치교체한새문자열 |원본은유지 |
| trim() |양끝공백제거한새문자열 |중간공백은유지 |

substr은 원본에 있어 해석하되 새 코드에는slice·substring을 우선 사용한다. 원본 `/가/g`로 모두 바꾸는 간단한 정규표현식 사용은 본문 범위다. 패턴 전체 작성법까지 필수로 넓히지는 않는다. replace를 여러 번 할 때 매번 원본에서 시작하면 앞의 수정이 누적되지 않는다.

> 📚 **출처 · 본문 설명 확인:** [MDN String](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String), [replace](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace), [substr](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/substr). 배운 기능의 뜻을 확인한 근거다. 예제·표·풀이 흐름은 수업 코드를 바탕으로 새로 작성했으며 외부 문장을 직접 인용하지 않았다. 확인일: 2026-10-28.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 스크립트.** [HTML 실행 파일](실습/책형_복습/10_JavaScript_문자열과_문자열메서드.html)과 같은 폴더의 [JS 파일](실습/책형_복습/10_JavaScript_문자열과_문자열메서드.js)을 함께 내려받는다. HTML을 브라우저로 열고 Console에서 결과를 확인한다. script는 필요한 HTML 뒤에 연결한다. 콘솔 출력은 페이지 본문에 자동으로 쓰이지 않는다.

```javascript
function maskEmail(email) {
    const pos = email.indexOf('@');
    if (pos < 1) {
        return '이메일을 확인하세요';
    }
    const id = email.slice(0, pos);
    let stars = '';
    for (let i = 2; i < id.length; i++) {
        stars += '*';
    }
    return id.slice(0, 2) + stars + email.slice(pos);
}
console.log(maskEmail('abcd@example.com'));
console.log(maskEmail('abcd'));
const word = '사과 주스';
console.log(word.replace('사과', '포도'));
console.log(word);
```

maskEmail은@앞 위치가1이상인지 보고 ID앞두글자를 남긴 뒤 나머지 길이만큼 별표를 쌓는다. 원본을 바탕으로 한 새 개선 함수다. @없는 입력은 즉시 안내를 반환한다. 완전한 이메일 형식 검증이나 암호화가 아니라 출력 가공이다. 마지막 두 줄은 replace가 새문자열을 돌려주고 word는 그대로임을 보여 준다.

**예상 출력 또는 관찰:**

```text
ab**@example.com
이메일을 확인하세요
포도 주스
사과 주스
```

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 원본의 일부다. 원본에 의존하는 앞 선언·HTML·함수는 다음 절의 연결까지 읽는다. 주석의 잘못된 표현도 원문대로 보존하고 설명에서 교정한다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/10_string.html` 23–35행

```javascript
            let s1 = str.replace('죽었','살았')
            console.log(str)
            console.log(s1)

            // '가'가 2개 있어도 처음 만나는것만 바꿈 
            // (반복하려면 while indexof로 -1 받을 때 까지)
            let s2 = str.replace('가','나')
            console.log(s2)

            // 정규표현식으로 원본에 있는 해당하는 전체를 바꿀 수 있음
            // Regular Expression /VALUE/i , 패턴구분자+찾을 문자열 패턴+패턴구분자+패턴변경자(g는 global)
            s2 = str.replace(/가/g,'나')
            console.log(s2)
```

**발췌 바로 풀이:** 같은 실험이다. s1은 '기사도가 살았을 리가'지만 str은 그대로다. 문자열 '가'를 사용한 replace는 첫 번째 일치만 바꿔 '기사도나 죽었을 리가'가 된다. 원본 `/가/g`는 정규표현식으로 가를 찾아 모두 바꾸는 간단한 사용이라 본문에 남긴다. 결과는 '기사도나 죽었을 리나'다. 정규표현식의 상세 작성법을 여기의 필수 전제로 확대하지 않는다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/10_string.html` 155–171행

```javascript
            let email = 'study.todair@gmail.com'
            // let id = email.split('@')[0]
            let pos = email.indexOf('@')
            let id = ''
            // @가 없으면 -1이 반환되기때문에 -1이 아닐 경우에 슬라이스 진행
            if(pos != -1) {
                id = email.slice(0,pos)
            }
            console.log(id)
            let mask_id_1 = id.slice(0, 2)
            let len = id.length - 2
            console.log(len)
            let mask_id_2 = ''
            for(let i=0; i<len; i++) {
                mask_id_2 += '*'
            }
            console.log(mask_id_1 + mask_id_2 + email.slice(pos))
```

**발췌 바로 풀이:** 같은 유효한 이메일 입력에서 id는 study.todair, 길이 12다. 앞 두 글자 st를 남기고 **별표 10개**와 @gmail.com을 붙인다. 강사님 문제 주석의 예시와 실제 계산값이 일치한다. 내 코드는 id와 길이를 중간 출력하여 확인하기 좋다. 원본 길이에 맞추어 반복하므로 repeat 같은 새 메서드로 바꾸지 않아도 된다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/10_string.html` 139–149행

```javascript
            function secCheck(email) {
                sumCheck = email.indexOf('@')
                console.log(sumCheck)

                for(let j=2; j<sumCheck; j++) {
                    securityEmail = email.replace(email[j],'*')
                    console.log(securityEmail)
                }
            }
            secCheck('todair@naver.com')
            secCheck('study.todair@gmail.com')
```

**발췌 바로 풀이:** 매번 원본 email에서 글자 하나만 교체해 securityEmail에 저장한다. 이전 결과를 다음 교체의 입력으로 쓰지 않으므로 별표가 누적되지 않는다. 같은 글자가 앞에도 있으면 replace는 의도한 인덱스보다 앞의 글자를 바꿀 수도 있다. 강사님처럼 ‘앞부분 + 별표 누적 + 뒷부분’으로 나누는 방식이 이 문제에서는 더 명확하다. 내 마지막 풀이도 그 구조를 적용했다.

내 str.replace(죽었,살았)는 새 s1을 만들고 str은 유지한다. 문자열가 교체는 첫가만, /가/g는 두가를 모두바꿔‘기사도나 죽었을 리나’다. 마지막 이메일 풀이의 ID는12글자라 앞st와별표10개가 된다. 중간id·len을 출력한 점은 확인에 좋다. secCheck는 매번 원본email에서 한글자만 교체해 이전별표가 누적되지 않는 다른 시도다.

<a id="connections"></a>

## 5. 선언·호출·파일이 연결되는 흐름

문자열 입력 → indexOf 반환 위치 → slice로 앞뒤 구간 → 반복으로 별표 문자열 → 합친 결과 return → 호출 쪽 출력 순서다. 이메일 가리기 함수의 정의와 호출을 같이 실었다. 원본 보조 변수들이 함수 밖에 있으면 호출 때마다 덮어쓰므로 그 호출에만 필요한 값은 함수 안 let·const로 범위를 줄일 수 있다.05장의 prompt에는 null 검사를 먼저 해야 취소값에 trim을 호출하는 오류를 피한다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 마지막 풀이는 앞부분·별표·뒷부분을 나누어 길이에 맞게 누적했다. **오류 경로:** @가 없어 pos=-1인데도 출력을 계속하면 강사님 substring(-1)은 원문 전체, 내 slice(-1)은 끝 글자를 붙인다. **개선 방향:** 앞의 새 함수처럼 필요 조건이 없을 때 안내하고 return한다. 짧은 ID를 몇 글자 가릴지와 빈 도메인을 어떻게 검사할지는 별도 정책이다. 부분 가리기를 개인정보 전체 검증이나 원문 삭제로 설명하지 않는다.

개선안은 원본을 수정한 결과가 아니다. 실제 오류, 수업용 단순화, 목적에 따른 선택을 구별해 판단한다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



강사님은 공백만 있는 값으로 trim 전후 길이를 비교해 양끝 정리의 필요성을 보기 좋다. 내 abc는 둘 다 길이가 있어 조건 차이를 드러내지 않는다. 이메일 누적 방식은 강사님 구조가 초기 secCheck보다 명확했고 내 마지막 풀이도 이를 적용했다. 같은 완성 코드를 다시 인용하기보다 변경 이유와 원본 입력의 한계를 설명한다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 내 추가 기록 | 의미·한계 |
| --- | --- |
| emailValue |@없으면slice(0,-1)로끝글자빠짐 |
| genderValue |일부예제코드만비교,일반식별검증아님 |
| resultCheck |고정형식의월·분split,일반Date파싱아님 |
| 마스킹문제4표시 |실제는고정별표4개아닌길이만큼방식 |

문제4의 ‘별표 네 개 고정’과 문제5의 ‘가린 개수만큼’을 구분한다. trim은 양끝만 제거하므로 '    1 2  3   '→'1 2  3'이며 중간 공백 두 개도 남는다. substring의 끝 인덱스와 substr의 개수도 구분한다.

| 한 가지 변경 | 예상 | 이유 |
| --- | --- | --- |
| 첫이메일ID만abcdef로 |ab****@example.com |길이6에서두글자남김 |
| 원래ID만a로 |a@example.com |이정책에가릴글자없음 |
| 원래word.replace결과를word에저장 |const재대입오류 |반환과선언구분 |

원본이 안 바뀌면 메서드 실패라고 단정하지 말고 반환값 저장을 본다. 문자를 위치로 교체하려고 replace(email[j],"*")를 쓰면 앞에 같은 글자가 있어 다른 위치를 바꿀 수 있다. 입력 형식이 틀린 경우와 코드 계산 오류를 나눈다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** 정규표현식 상세·Unicode 문자 단위·범용 이메일 검증·repeat 등 새 메서드는 추가 학습이다. 간단한 /가/g 사용이 있다는 이유로 전체 패턴 문법을 배운 것으로 간주하지 않는다.



이 절의 확장은 기본 문제의 필수 조건이 아니다. 📚 출처가 있다는 것과 수업 밖 기능이라는 것은 다른 구분이다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. replace는 원본을 바꾸는가?
2. trim은 중간 공백도 모두 제거하는가?
3. @없는 이메일에서 바로 마스킹 출력해도 되는가?

<details>
<summary>짧은 풀이 — 먼저 답한 뒤 확인</summary>

새 문자열을 반환한다. 양끝 공백만 제거한다. 필요 조건이 없으면 안내하고 돌아가는 등 처리 정책을 정해야 한다.

</details>

| 확인 | 핵심 |
| --- | --- |
| 위치 |0시작·없으면-1 |
| 자르기 |끝인덱스/개수 |
| 변경 |새결과반환 |
| 입력 |null·형식·정책구분 |

[장별 연습문제](실습/연습문제/10_JavaScript_문자열과_문자열메서드_연습문제.md)에서 예상·설명·수정을 이어 간다. 다음은 [DOM 선택](11_JavaScript_DOM_선택과_속성_클래스조작.md)이다.

<!-- 이전 색인 이동 주소 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>
<a id="section-6"></a>
<a id="section-7"></a>
<a id="section-8"></a>

[이 장의 목차](#chapter-toc)에서 현재 설명을 찾는다.
