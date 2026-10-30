# 03. 조건문과 switch — 실행 경로와 경계값

[JavaScript 목차](README.md) · [읽기 안내](00_JavaScript_V3_동작_백과_읽기법.md)

입력한 점수에 따라 등급을 정하거나 선택한 메뉴마다 다른 일을 해야 한다. 조건문은 조건의 참거짓으로 실행 경로를 나누고, switch는 값이 맞는 갈래를 찾는다. 경로 하나가 맞았다고 모든 경우가 맞는 것은 아니다.

<a id="chapter-toc"></a>

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

if·else if·독립 if의 차이를 설명한다. switch의 비교와 break, 원본 난수·승패·시간·범위 문제의 경계값을 확인한다.

입력·현재 상태·실행 순서·결과를 분리해 설명한다. 실제 수업 원본은 아래에 표시하고, 원본에 없는 선택 학습은 9절 TIP에 둔다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

if는 조건이 참으로 평가될 때 블록을 실행한다. else if를 연결하면 위에서 검사하여 처음 참인 갈래 하나를 실행한다. 앞 조건이 거짓이어야 아래로 내려오므로 점수 90 이상 다음의 80 이상은 이미 90 미만인 범위를 대상으로 한다. 독립 if 여러 개는 각각 검사하므로 여러 블록이 실행될 수 있다.

조건에 꼭 불리언 변수만 들어가는 것은 아니다. 수업에서 먼저 구별할 거짓 취급 값은 false·0·빈 문자열·undefined·null·NaN이다. 문자열 '0'·'false'는 비어 있지 않아 참으로 평가된다. 이것을 언어 전체의 완전한 목록으로 외우지는 않는다.

switch는 case와 엄격 동등 비교로 맞는 지점을 찾아 실행을 시작한다. break가 없으면 다음 case 문장도 이어 실행할 수 있다. 여러 case를 묶어 같은 작업을 하거나 default로 나머지를 처리한다. 숫자 3과 문자열 '3'은 다르다.

| 상황 | 알맞은 판단 |
| --- | --- |
| 점수 구간 | 높은 구간부터 else if 순서 확인 |
| 같은 선택값 묶기 | switch의 case·break |
| 범위 두 조건 | `3 < a && a < 20`처럼 결합 |
| 경계 | 바로 아래·경계·바로 위 입력 |

`3<a<20`은 수학처럼 동시에 검사하지 않는다. 첫 비교가 참거짓 값이 된 뒤 다음 비교가 된다. 정상 숫자에서의 부등식 변형도 NaN까지 같은 결과라고 일반화하지 않는다.

> 📚 **출처 · 본문 설명 확인:** [MDN if...else](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else), [switch](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch), [Falsy](https://developer.mozilla.org/en-US/docs/Glossary/Falsy). 배운 기능의 뜻을 확인한 근거다. 예제·표·풀이 흐름은 수업 코드를 바탕으로 새로 작성했으며 외부 문장을 직접 인용하지 않았다. 확인일: 2026-10-28.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 스크립트.** [HTML 실행 파일](실습/책형_복습/03_JavaScript_조건문과_Switch.html)과 같은 폴더의 [JS 파일](실습/책형_복습/03_JavaScript_조건문과_Switch.js)을 함께 내려받는다. HTML을 브라우저로 열고 Console에서 결과를 확인한다. script는 필요한 HTML 뒤에 연결한다. 콘솔 출력은 페이지 본문에 자동으로 쓰이지 않는다.

```javascript
let score = 85;
if (score >= 90) {
    console.log('A');
} else if (score >= 80) {
    console.log('B');
} else {
    console.log('C');
}
let hour = 23;
let minute = 51;
minute += 35;
if (minute >= 60) {
    hour++;
    minute -= 60;
}
if (hour >= 24) {
    hour -= 24;
}
console.log(`${hour}시 ${minute}분`);
```

85는 90 이상에서 거짓, 80 이상에서 참이므로 B만 출력한다. 시간은 51+35=86분을 먼저 만들고, 60분을 빼고 시간을 하나 올려 24시26분으로 만든 뒤, 24시를0시로 보정한다. 한 번에35분을 더하는 조건에서는 각 보정 한 번이면 충분하다. 매우 큰 임의 시간까지 처리하는 일반 날짜 계산기라는 뜻은 아니다.

**예상 출력 또는 관찰:**

```text
B
0시 26분
```

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 원본의 일부다. 원본에 의존하는 앞 선언·HTML·함수는 다음 절의 연결까지 읽는다. 주석의 잘못된 표현도 원문대로 보존하고 설명에서 교정한다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/03_if.html` 54–62행

```javascript
		if (score >= 90) {
			console.log('A')
		} else if (score >= 80) {
			console.log('B')
		} else if (score >= 70) {
			console.log('C')
		} else {
			console.log('D')
		}
```

**발췌 바로 풀이:** 양쪽 모두 앞에서 score를 85로 지정했으므로 B를 출력한다. 90 이상 검사에 실패한 뒤 80 이상을 검사하므로 여기서 다시 ‘90 미만’을 쓸 필요는 없다. 조건을 70 이상부터 검사하면 95도 C 갈래에 걸린다. 구간 판정은 순서가 중요하다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/03_if.html` 113–127행

```javascript
		switch (phone) {
			case 's23':
			case 's24':
			case 's25':
			case 's26':
				console.log('삼성')
				break;
			case 'i15':
			case 'i16':
			case 'i17':
				console.log('삼성')
				break;
			default:
				console.log('삼성, 애플 아님')
		}
```

**발췌 바로 풀이:** phone='s23'인 원본 실행에서는 양쪽 모두 삼성이다. 그러나 i15·i16·i17이면 강사님은 애플, 내 코드는 삼성이라고 출력한다. **내 123행의 출력 문자열을 애플로 고치면 된다.** 실행값 하나만 확인하면 놓칠 수 있는 오류다. ‘==만 switch로 바꿀 수 있다’는 내 주석도 정확하지 않다. 여기서는 동일 값 분기에 적합하다고 이해하고, ==의 자동 변환과 switch의 비교를 섞지 않는다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/03_if.html` 223–239행

```javascript
		let q5_rps = prompt('5. 가위/바위/보 중에 입력해주세요.')
		// 사용자의 값은 prompt로 입력받으며, 랜드로 0,1,2만 출력하게 하여 해당 값이 출력 될 때
		// com_rps라는 변수에 가위/바위/보 중에서 값을 받아올 수 있도록 if문 구성
		let rand = parseInt(Math.random() * 10) % 3
		let com_rps;

		// console.log로 정확한 값을 받아오는지 출력해본 뒤 com_rps 변수에 값 입력
		if(rand === 0){
			com_rps = '가위'
			// console.log(com_rps)
		} else if(rand === 1){
			com_rps = '바위'
			// console.log(com_rps)
		} else {
			com_rps = '보'
			// console.log(com_rps)
		}
```

**발췌 바로 풀이:** 내 발췌는 원본 222–257행의 블록 주석 안에 있다. 실행하려면 해당 풀이만 따로 꺼내야 한다. 강사님 퀴즈의 3배 방식이 경우를 나누기에 더 적합하다. 내 방식은 0–9를 만든 뒤 나머지를 구하므로 0으로 가는 값은 0·3·6·9 네 개, 1과 2로 가는 값은 각각 세 개다. **결과 범위는 맞지만 분배가 치우친다.** 강사님 기본 파일의 1000배 후 %3도 같은 종류의 작은 치우침이 있다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/03_if.html` 241–256행

```javascript
		// 가위/바위/보 에서 승리/패배/비기는 경우의 수는 3가지씩으로 or(||)로 구성
		if(q5_rps == com_rps){
			console.log(`비겼습니다. (나: ${q5_rps} , 컴퓨터: ${com_rps})`)
		} else if (q5_rps == '가위' && com_rps == '바위'
			|| q5_rps == '바위' && com_rps == '보'
			|| q5_rps == '보' && com_rps == '가위'
		) {
			console.log(`졌습니다. (나: ${q5_rps} , 컴퓨터: ${com_rps})`)
		} else if (q5_rps == '가위' && com_rps == '보'
			|| q5_rps == '바위' && com_rps == '가위'
			|| q5_rps == '보' && com_rps == '바위'
		) {
			console.log(`이겼습니다. (나: ${q5_rps} , 컴퓨터: ${com_rps})`)
		} else {
			alert('가위/바위/보 중에서 입력해주세요.')
		}
```

**발췌 바로 풀이:** 강사님 퀴즈의 user는 '가위' 같은 문자열이고 rand는 0·1·2다. `user == rand`로는 정상 선택의 무승부를 판정하지 못한다. 앞의 중첩 if 풀이와 뒤의 이 풀이가 둘 다 실행되어 결과가 여러 번 출력될 수도 있다. 앞의 중첩 풀이도 컴퓨터가 바위·보일 때 잘못된 입력을 마지막 else에서 승패로 처리한다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/03_if.html` 376–387행

```javascript
		let hour = parseInt(Math.random() * 24)
		let minute = parseInt(Math.random() * 60)
		console.log(`${hour}시 ${minute}분`)
		minute += 35
		if(minute >= 60){
		hour ++
		minute -= 60
		}
		if(hour >= 24){
		hour -= 24
		}
		console.log(`${hour}시 ${minute}분`)
```

**발췌 바로 풀이:** 이 코드 역시 블록 주석 안에 있다. 35분을 더한 뒤 60분 이상이면 시간을 올리고 분을 줄인다. 시간이 24 이상이면 24를 뺀다. 한 번에 35분만 더하는 이 문제에서는 각 보정 한 번이면 충분하다. 더하는 시간이 매우 큰 경우까지 보장하는 일반 날짜 계산기는 아니다.

점수 원본은85에서B다. 내 ‘컴퓨터가1번만 일함’ 메모는 조건 검사 자체가 한 번이라는 뜻이 아니라 연결된 갈래 하나가 실행된다는 뜻으로 고쳐 읽는다. switch는 현재s23이라 양쪽삼성이지만, 내i15·i16·i17도삼성으로 적혀 있어 애플로 교정해야 한다.

가위바위보 내 발췌는 원본222–257행의 블록 주석 안에 있어 파일을 열어도 실행되지 않는다. 컴퓨터 값을 문자열 com_rps로 바꿔 같은 종류끼리 비교한 점은 명확하다. 그러나 `parseInt(Math.random()*10)%3`은0·1·2 범위는 맞아도0에4가지,나머지에3가지씩 배분되어 치우친다. 강사님 퀴즈의3배 방식과 비교한다.

승패는 같은 선택·패배 세 조합·승리 세 조합·잘못된 입력으로 나눴다. &&가||보다 먼저 묶이지만 각 조합에 괄호를 붙이면 읽기 쉽다. 내 시간 참고형도 주석 안의 학습 기록이다. 조건만 있는 강사님 문제를 내 파일의 참고형 출처로 바꾸어 쓰지 않는다.

<a id="connections"></a>

## 5. 선언·호출·파일이 연결되는 흐름

입력·초기값 → 위쪽 조건부터 평가 → 선택된 블록 → 값 변경 → 출력 순서다. Math.random은0이상1미만의 값을 반환하고 수업의 `parseInt(Math.random()*3)`은0·1·2를 만든다. 양의정수 min·max의 원본식은 `parseInt(Math.random()*(max-min+1))+min`이다. user prompt는문자열·취소null이므로, 숫자rand와문자열user를 바로 무승부 비교하면 맞지 않는다. 강사님 `user||"취소누름"`은빈 문자열도 대체하므로 취소만 정확히 구분하는 판정은 아니다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 내 승패 비교는 컴퓨터 선택을 문자열로 맞추고 유효하지 않은 입력도 안내한다. 두 수 비교의 같음, 뒤집힌 범위도 고려한 기록이 있다. **실제 오류:** switch의 애플 출력, 0의 양수 처리, 두 자리 범위 검사보다 %11을 먼저 검사한 부분은 고쳐야 한다. **개선 방향:** 대표 입력 하나 대신 경계와 반례를 먼저 적는다. 주석 안 풀이·아직 문제만 있는 사각형을 완성된 실행 기능으로 표시하지 않는다.

개선안은 원본을 수정한 결과가 아니다. 실제 오류, 수업용 단순화, 목적에 따른 선택을 구별해 판단한다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교

출처: `D:/workspace_teacher/workspace_html/javascript/03_if.html` 104–118행

```javascript
        switch(phone){
            case 's23':
            case 's24':
            case 's25':
            case 's26':
                console.log('삼성')
                break
            case 'i15':
            case 'i16':
            case 'i17':
                console.log('애플')
                break
            default :
                console.log('삼성, 애플 아님')
        }
```

출처: `D:/workspace_teacher/workspace_html/javascript/퀴즈/조건문.html` 13–20행

```javascript
        let rand = Math.random() // 0 <= rand < 1
        rand = parseInt(rand * (2+1)) // 0~2까지 랜덤
        // 0:가위 1:바위 2:보
        // let user = '가위'
        let user = prompt('가위바위보 중에 하나 적으시오')
        // console.log('user : ', user)
        let a = user || '취소누름'
        console.log('user : ', typeof user, a)
```

첫 강사님 발췌는 애플 갈래의 올바른 출력과 비교하는 데 필요하다. 두 번째는0·1·2를 만들 때 직접3배하는 방식이라 내10배후나머지보다 적합하다. 다만 강사님 기본 파일의1000배후%3도 같은 종류의 치우침이 있으며, 퀴즈의 문자열user와숫자rand 무승부 비교도 검토해야 한다. 강사님이라는 이유로 양쪽 오류를 건너뛰지 않는다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 원본 문제 | 다시 확인할 조건 |
| --- | --- |
| 양수·0·음수 | 0은 별도 분류, 양수가 아님 |
| 홀짝 | `!값 % 2 == 0`과 전체 조건 부정은 다름 |
| 큰 값 | 같음 처리와 취소·빈 입력 구분 |
| 교통비 |7000·6999·3000·2999 경계 |
| 두 값 사이 |끝점 포함 여부·x/y 뒤집힘 |
| 월·계절 |prompt의 '3'과'03'은 다른 문자열 |
| 온도 | -3→‘영하3도’라면 부호 변경, 정수 변환은 아님 |
|35분 뒤 |60분 미만·24시 미만으로 보정 |
| 두 자리 같은 숫자 |10~99 범위를 먼저 확인,0·110 반례 |
|369 |십·일의 자리 풀이를 임의 자릿수로 일반화하지 않음 |
| 사각형 포함 |내 원본은 문제만 있음 |

온도의 -1곱하기는 부호 변경이라 -3.5→3.5이며 정수 변환이 아니다. 원본 경고 문구를 건강 판단 기준으로 삼지 않는다. 학습 예제의 출력 의미와 실제 판단 용도는 다르다.

| 한 가지 변경 | 예상 | 이유 |
| --- | --- | --- |
| score만95 |A |첫 갈래 참 |
| 원래 minute만25 |0시0분 |정확히60분 경계 |
| 원래 hour만22 |23시26분 |24시 보정 불필요 |
| 별도 switch시험의 phone만i15 |내오류 드러남 |현재s23만 보면 놓침 |

잘못된 결과가 나오면 어느 조건에서 처음 참이 되었는지 적는다. 난수를 계속 돌려 우연히 확인하기보다 입력값을 잠시 고정해 무승부·승리·패배·잘못된 입력을 각각 확인한다. 난수 생성과 승패 판정은 다른 검토 대상이다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** 객체 매핑으로 분기 재설계, 별도 검증 API·보안 난수는 추가 학습이다. Math.random을 보안용으로 써도 된다는 뜻으로 범위를 넓히지 않는다.



이 절의 확장은 기본 문제의 필수 조건이 아니다. 📚 출처가 있다는 것과 수업 밖 기능이라는 것은 다른 구분이다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. 95점인데70이상부터검사하면어떤갈래에먼저걸리는가?
2. 숫자3과문자열3은switch에서같은가?
3. 사각형x10~90·y20~100의테두리포함조건은?

<details>
<summary>짧은 풀이 — 먼저 답한 뒤 확인</summary>

먼저 적은70이상 갈래에 걸린다. switch는 엄격 비교여서 다르다. `x>=10&&x<=90&&y>=20&&y<=100`이다. 마지막은 새 복습 답이며 내 미완성 원본의 완성 풀이 인용이 아니다.

</details>

| 확인 | 핵심 |
| --- | --- |
| else if | 처음참인갈래 |
| switch | 엄격비교·break |
| 범위 | 두비교와&& |
| 검증 | 경계·반례·주석상태 |

[장별 연습문제](실습/연습문제/03_JavaScript_조건문과_Switch_연습문제.md)에서 예상·설명·수정을 이어 간다. 다음은 [반복문](04_JavaScript_반복문과_배열순회.md)이다.

<!-- 이전 색인 이동 주소 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>
<a id="section-6"></a>

[이 장의 목차](#chapter-toc)에서 현재 설명을 찾는다.
