# 10. 문자열 — 찾고, 자르고, 바꾼 결과를 저장하기

[JavaScript 목차](README.md) · [이전: TV 실습](09-02_JavaScript_TV상태관리.md)

기준은 양쪽 `10_string.html`이다. 문자열 메서드는 원본 문자열 자체를 수정하지 않는다. 결과를 돌려받아 사용할 뿐이므로 `str.replace(...)`를 호출했다는 이유만으로 str이 바뀌었다고 읽지 않는다.

<!-- chapter-toc -->

- [1. 원본 문장으로 결과 읽기](#section-1)
- [2. replace는 새 문자열을 반환한다](#section-2)
- [3. trim과 입력 검사](#section-3)
- [4. 이메일 가리기 비교](#section-4)
- [5. 내 추가 풀이의 범위](#section-5)
- [6. 배운 메서드로 교정한 짧은 함수](#section-6)
- [7. 짧은 복습](#section-7)
- [추가로 알면 좋은 것](#section-8)

<a id="section-1"></a>

## 1. 원본 문장으로 결과 읽기

양쪽 문장은 `기사도가 죽었을 리가`다. 공백도 인덱스와 길이에 포함된다. 인덱스는 0부터 시작한다.

| 표현 | 이 문장의 결과 | 의미 |
| --- | --- | --- |
| str.length | 11 | 원본 문장의 길이 |
| str.indexOf('죽었') | 5 | 시작 인덱스 |
| str.indexOf('가') | 3 | 처음 일치한 위치 |
| str.indexOf('나') | -1 | 없음 |
| str.slice(3,6) | '가 죽' | 시작 포함·끝 제외 |
| str.substring(3,6) | '가 죽' | 이 양수 범위에서는 slice와 같음 |
| str.substr(3,7) | '가 죽었을 리' | 3부터 7개 |
| str.split(' ') | ['기사도가','죽었을','리가'] | 공백으로 분리한 배열 |

substring의 두 번째 인수는 끝 인덱스, substr의 두 번째 인수는 길이다. substr은 원본에 있으므로 해석은 본문에서 다루되 새 코드에는 slice·substring을 우선 사용한다. 현재 문서에서 substr은 권장되지 않는 레거시 기능으로 안내된다. [MDN substr](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/substr)

<a id="section-2"></a>

## 2. replace는 새 문자열을 반환한다

### 강사님 코드

출처: `teacher/workspace_html/javascript/10_string.html` 25–34행 · **원본 발췌**

```javascript
    let s1 = str.replace('죽었', '살았')
    console.log(str)
    console.log(s1)

    let s2 = str.replace('가', '나')
    console.log(s2)

    // 정규 표현식
    s2 = str.replace(/가/g, '나')
    console.log(s2)
```

### 내 코드

출처: `me/workspace_html/javascript/10_string.html` 23–35행 · **원본 발췌**

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

같은 실험이다. s1은 '기사도가 살았을 리가'지만 str은 그대로다. 문자열 '가'를 사용한 replace는 첫 번째 일치만 바꿔 '기사도나 죽었을 리가'가 된다. 원본 `/가/g`는 정규표현식으로 가를 찾아 모두 바꾸는 간단한 사용이라 본문에 남긴다. 결과는 '기사도나 죽었을 리나'다. 정규표현식의 상세 작성법을 여기의 필수 전제로 확대하지 않는다.

<a id="section-3"></a>

## 3. trim과 입력 검사

양쪽 str2의 처음 값 `'    1 2  3   '`에 trim을 쓰면 `'1 2  3'`이다. 양 끝 공백만 제거하고 중간 공백은 그대로 남는다. 강사님은 그 뒤 str2를 공백만 있는 문자열로 바꾸므로 length 검사와 trim().length 검사가 다르다. 내 코드는 'abc'로 바꾸어 두 조건이 모두 참이다. 공백 제거의 필요성을 관찰하기에는 강사님 입력이 더 적합하다.

05장의 prompt 입력에 적용할 때도 **null인지 먼저 검사**해야 한다. 취소 결과 null에는 trim 메서드를 호출할 수 없다. 이는 새로운 검증 체계가 아니라 배운 메서드를 올바른 자료형에 호출하는 교정이다.

<a id="section-4"></a>

## 4. 이메일 가리기 비교

마스킹은 일부 문자를 별표로 보이게 만드는 출력 가공이다. 원본 문자열을 암호화하거나 서버에서 지우는 기능이 아니다. 수업 문제4의 ‘별표 네 개 고정’과 문제5의 ‘가린 글자 수만큼 별표’를 구분한다.

### 강사님 코드

출처: `teacher/workspace_html/javascript/10_string.html` 85–100행 · **원본 발췌**

```javascript
    let email = 'study.todair@gmail.com'
    
    // let id = email.split('@')[0]

    let pos = email.indexOf('@')
    let id = ''
    if (pos != -1){
        id = email.slice(0, pos)
    }
    let mask_id_1 = id.slice(0, 2)
    let len = id.length - 2
    let mask_id_2 = ''
    for(let i=0; i<len; i++){
        mask_id_2 += "*"
    }
    console.log(mask_id_1 + mask_id_2 + email.substring(pos))
```

### 내 코드

출처: `me/workspace_html/javascript/10_string.html` 155–171행 · **원본 발췌**

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

같은 유효한 이메일 입력에서 id는 study.todair, 길이 12다. 앞 두 글자 st를 남기고 **별표 10개**와 @gmail.com을 붙인다. 강사님 문제 주석의 예시와 실제 계산값이 일치한다. 내 코드는 id와 길이를 중간 출력하여 확인하기 좋다. 원본 길이에 맞추어 반복하므로 repeat 같은 새 메서드로 바꾸지 않아도 된다.

### 내 다른 시도에서 별표가 누적되지 않는 이유

출처: `me/workspace_html/javascript/10_string.html` 139–149행 · **원본 발췌**

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

매번 원본 email에서 글자 하나만 교체해 securityEmail에 저장한다. 이전 결과를 다음 교체의 입력으로 쓰지 않으므로 별표가 누적되지 않는다. 같은 글자가 앞에도 있으면 replace는 의도한 인덱스보다 앞의 글자를 바꿀 수도 있다. 강사님처럼 ‘앞부분 + 별표 누적 + 뒷부분’으로 나누는 방식이 이 문제에서는 더 명확하다. 내 마지막 풀이도 그 구조를 적용했다.

### @가 없는 입력에서는?

양쪽은 pos=-1이면 id를 비워 두지만 마지막 출력은 실행한다. 강사님의 substring(-1)은 0부터 읽어 원문 전체를 붙이고, 내 slice(-1)은 마지막 글자만 붙인다. 둘 다 올바른 이메일 마스킹 성공으로 취급해서는 안 된다. **수정 예제에서는 @가 없으면 안내하고 반환**하도록 만들면 된다. 이메일 전체 형식 검증까지 완료했다는 뜻은 아니다.

<a id="section-5"></a>

## 5. 내 추가 풀이의 범위

| 내 원본 위치 | 배운 메서드 사용 | 확인할 한계 |
| --- | --- | --- |
| 69–75행 emailValue | indexOf 후 slice로 ID 출력 | @가 없으면 slice(0,-1)로 마지막 글자를 빼버림 |
| 82–93행 genderValue | - 다음 한 글자 추출 | 예제 코드 1/2만 비교. else가 모든 다른 입력까지 한 분류로 처리하므로 일반적인 식별·검증 함수로 소개하지 않음 |
| 103–110행 resultCheck | 공백·-·:로 차례로 split | 고정 형식에서 07월·43분 출력. Date 파싱이나 임의 형식 처리 기능은 아님 |
| 117–132행 마스킹 | 실제 ID 길이만큼 별표 생성 | ‘문제4’ 제목이지만 고정 네 개가 아닌 문제5 조건의 방식 |

단순 비교용 예제 입력을 실제 개인정보 판단 기준으로 확대하지 않는다. 또한 보조 변수를 함수 바깥에 둔 내 풀이들은 호출 때마다 같은 변수 값을 덮는다. 해당 호출 안에서만 필요하면 함수 안의 let으로 옮겨 읽을 범위를 줄일 수 있다. 이는 08장의 지역변수 원리를 적용한 제안이다.

<a id="section-6"></a>

## 6. 배운 메서드로 교정한 짧은 함수

아래는 **두 원본을 바탕으로 만든 교정 예제**다. 문자열 입력에서 @의 존재만 확인하며 완전한 이메일 검증 함수는 아니다.

```javascript
function maskEmail(email) {
    let pos = email.indexOf('@');
    if (pos < 1) return '이메일을 확인하세요';
    let id = email.slice(0,pos);
    let stars = '';
    for (let i=2; i<id.length; i++) stars += '*';
    return id.slice(0,2) + stars + email.slice(pos);
}
console.log(maskEmail('abcd@example.com')); // ab**@example.com
console.log(maskEmail('abcd')); // 이메일을 확인하세요
```

ID가 두 글자 이하면 이 조건에서는 가려질 글자가 없다. 더 짧은 ID도 가려야 한다면 별도 정책을 정해야 한다. 원본 요구인 ‘앞 두 글자 표시’와 새로운 요구를 섞지 않는다.

<a id="section-7"></a>

## 7. 짧은 복습

1. replace 결과를 저장하지 않으면 원본 문자열이 바뀌는가?
2. substring(3,7)과 substr(3,7)의 두 번째 인수 의미는?
3. 공백만 입력한 문자열을 비어 있다고 판단하려면?

<details>
<summary>정답 확인</summary>

1. 바뀌지 않는다.
2. 각각 끝 인덱스와 개수다.
3. trim 후 length를 확인한다. prompt 취소는 null 검사를 먼저 한다.

</details>

<a id="section-8"></a>

## 추가로 알면 좋은 것

정규표현식 상세 검증, repeat·padStart, 유니코드의 글자 수 세기, 일반 이메일 파서·마스킹 정책은 확장이다. length를 모든 언어·이모지의 눈에 보이는 글자 수와 같다고 일반화하지 않는다.

