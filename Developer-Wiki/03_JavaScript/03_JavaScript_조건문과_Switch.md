# 03. 조건문과 switch — 조건의 순서로 실행 경로 결정하기

[JavaScript 목차](README.md) · [이전: 연산자](02_JavaScript_연산자.md)

기준 파일은 양쪽 `03_if.html`과 강사님 `퀴즈/조건문.html`이다. 내 파일의 문제 풀이 상당수는 주석 안에 있다. 아래에 코드만 발췌했더라도 **원본 전체에서는 실행되지 않는 풀이**임을 해당 설명에 표시한다.

<!-- chapter-toc -->

- [1. if와 else if: 먼저 참이 된 갈래 하나](03_JavaScript_조건문과_Switch.md#section-1)
- [2. switch: 값이 같은 case에서 시작하기](03_JavaScript_조건문과_Switch.md#section-2)
- [3. 난수와 가위바위보 — 양쪽 모두 검토하기](03_JavaScript_조건문과_Switch.md#section-3)
- [4. 실제 문제 풀이의 경계값 점검](03_JavaScript_조건문과_Switch.md#section-4)
- [5. 교정 예제와 복습](03_JavaScript_조건문과_Switch.md#section-5)
- [추가로 알면 좋은 것](03_JavaScript_조건문과_Switch.md#section-6)

<a id="section-1"></a>

## 1. if와 else if: 먼저 참이 된 갈래 하나

`if (조건)`의 조건이 참으로 평가되면 연결된 블록을 실행한다. `else`는 앞 조건이 거짓일 때 실행할 갈래다. else if를 이어 쓰면 위에서부터 검사하고 처음 참인 갈래만 실행한다. 반면 독립된 if 여러 개는 각각 검사하므로 여러 블록이 실행될 수 있다.

### 강사님 코드

출처: `teacher/workspace_html/javascript/03_if.html` 48–56행 · **원본 발췌**

```javascript
        if(score >= 90){
            console.log('A')
        } else if(score >= 80){
            console.log('B')
        } else if(score >= 70){
            console.log('C')
        } else {
            console.log('D')
        }
```

### 내 코드

출처: `me/workspace_html/javascript/03_if.html` 54–62행 · **원본 발췌**

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

양쪽 모두 앞에서 score를 85로 지정했으므로 B를 출력한다. 90 이상 검사에 실패한 뒤 80 이상을 검사하므로 여기서 다시 ‘90 미만’을 쓸 필요는 없다. 조건을 70 이상부터 검사하면 95도 C 갈래에 걸린다. 구간 판정은 순서가 중요하다.

내 37행의 ‘컴퓨터가 1번만 일함’은 정확한 기준이 아니다. else if도 앞 조건이 거짓이면 다음 조건을 검사한다. **한 연결문에서 실행되는 갈래가 하나**라는 의미로 이해하자. 또 `!(score >= 60)`과 `score < 60`은 이 수업의 정상 숫자에서는 같지만 NaN까지 포함하면 같지 않다. NaN과의 크기 비교는 거짓이어서 부정 여부에 따라 결과가 달라진다.

양쪽 주석의 거짓 값 목록에는 빈 문자열 `''`가 빠져 있다. 이 수업에서 먼저 기억할 값은 false, 0, '', undefined, null, NaN이다. 문자열 '0'이나 'false'는 빈 문자열이 아니므로 참으로 평가된다. 이 목록을 언어 전체의 완전한 목록이라고 외우지는 말자. [MDN 거짓으로 평가되는 값](https://developer.mozilla.org/en-US/docs/Glossary/Falsy)

<a id="section-2"></a>

## 2. switch: 값이 같은 case에서 시작하기

switch는 case 값과 엄격 동등 비교로 일치 여부를 판단한다. 따라서 숫자 3과 문자열 '3'을 구별한다. 일치한 곳부터 실행하다가 break를 만나면 switch 밖으로 나간다. break가 없으면 다음 case에 적힌 문장도 이어 실행될 수 있다. 여러 case가 같은 일을 할 때는 원본처럼 묶을 수 있다. [MDN switch](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch)

### 강사님 코드

출처: `teacher/workspace_html/javascript/03_if.html` 104–118행 · **원본 발췌**

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

### 내 코드

출처: `me/workspace_html/javascript/03_if.html` 113–127행 · **원본 발췌**

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

phone='s23'인 원본 실행에서는 양쪽 모두 삼성이다. 그러나 i15·i16·i17이면 강사님은 애플, 내 코드는 삼성이라고 출력한다. **내 123행의 출력 문자열을 애플로 고치면 된다.** 실행값 하나만 확인하면 놓칠 수 있는 오류다. ‘==만 switch로 바꿀 수 있다’는 내 주석도 정확하지 않다. 여기서는 동일 값 분기에 적합하다고 이해하고, ==의 자동 변환과 switch의 비교를 섞지 않는다.

<a id="section-3"></a>

## 3. 난수와 가위바위보 — 양쪽 모두 검토하기

Math.random()은 0 이상 1 미만의 값을 돌려준다. 수업 범위의 0·1·2 중 하나를 고르려면 `parseInt(Math.random() * 3)`을 쓴다. 원본의 양의 정수 min·max 범위 공식은 `parseInt(Math.random() * (max - min + 1)) + min`이다. 예를 들어 min=5, max=8이면 5–8을 만든다. 보안용 난수가 필요한 상황은 이 실습의 범위 밖이다. [MDN Math.random](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/random)

### 강사님 퀴즈: 난수 생성

출처: `teacher/workspace_html/javascript/퀴즈/조건문.html` 13–20행 · **원본 발췌**

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

### 내 풀이: 난수 생성

출처: `me/workspace_html/javascript/03_if.html` 223–239행 · **원본 발췌**

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

내 발췌는 원본 222–257행의 블록 주석 안에 있다. 실행하려면 해당 풀이만 따로 꺼내야 한다. 강사님 퀴즈의 3배 방식이 경우를 나누기에 더 적합하다. 내 방식은 0–9를 만든 뒤 나머지를 구하므로 0으로 가는 값은 0·3·6·9 네 개, 1과 2로 가는 값은 각각 세 개다. **결과 범위는 맞지만 분배가 치우친다.** 강사님 기본 파일의 1000배 후 %3도 같은 종류의 작은 치우침이 있다.

강사님 `user || '취소누름'`은 null뿐 아니라 빈 문자열에도 대체 문구를 쓴다. 취소와 빈 입력을 정확히 구분하는 판정은 아니다. 이 원본은 ||가 불리언이 아닌 문자열도 반환한다는 실제 학습 근거다.

### 강사님 퀴즈: 승패 비교

출처: `teacher/workspace_html/javascript/퀴즈/조건문.html` 52–61행 · **원본 발췌**

```javascript
        if(user == rand){
            console.log('비겼다')
        } else if (user=='보' && rand==1
                    || user=='바위' && rand==0
                    || user=='가위' && rand==2
        ) {
            console.log('이겼다')
        } else {
            console.log('졌다')
        }
```

### 내 풀이: 승패 비교

출처: `me/workspace_html/javascript/03_if.html` 241–256행 · **원본 발췌**

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

강사님 발췌의 user는 '가위' 같은 문자열이고 rand는 0·1·2다. `user == rand`로는 정상 선택의 무승부를 판정하지 못한다. 앞의 중첩 if 풀이와 뒤의 이 풀이가 둘 다 실행되어 결과가 여러 번 출력될 수도 있다. 앞의 중첩 풀이도 컴퓨터가 바위·보일 때 잘못된 입력을 마지막 else에서 승패로 처리한다.

내 코드는 컴퓨터 값을 com_rps 문자열로 맞춘 뒤 비교하고, 유효하지 않은 선택을 마지막에 안내한다. **이 승패 비교는 내 방식이 더 명확하다.** 세 가지 승리·패배 조합에서 &&가 ||보다 먼저 묶이지만, 각 조합을 괄호로 감싸면 읽기 편하다. 난수 생성만 교정하고 무승부·승리·패배·잘못된 입력을 모두 확인하면 된다.

<a id="section-4"></a>

## 4. 실제 문제 풀이의 경계값 점검

강사님 기본 파일 121–182행의 12개 문제와 내 풀이를 비교했다. 아직 작성하지 않은 문제를 완성 풀이로 취급하지 않는다.

| 문제 | 내 원본 위치 | 다시 볼 점 |
| --- | --- | --- |
| 양수·0·음수 | 130–144행 | 0을 양수로 처리. 문제는 0을 별도 분류하며 0은 양수가 아님 |
| 홀짝 | 146–160행 | !q2_result % 2 == 0은 !(q2_result % 2 == 0)과 다름. 정수 입력 전제도 필요 |
| 두 수의 큰 값 | 162–183행 | Number로 변환 후 같음도 처리한 점이 좋음. 취소·빈 입력은 별도 확인 필요 |
| 교통비 | 185–201행 | 7000→3000 순서가 적절. 6999·3000·2999 경계도 확인 |
| 가위바위보 | 203–257행 | 위 절의 난수·승패 비교 참고 |
| 두 값 사이 | 259–284행 | x와 y 순서가 뒤집힌 경우도 검사한 점이 좋음. 경계 포함 여부는 문제 조건으로 정함 |
| 월과 계절 | 286–316행 | prompt 문자열을 문자열 case와 비교. '3'과 '03'은 다름 |
| 온도 | 318–336행 | -3 입력이 ‘영하 -3도’가 됨. 원문 조건처럼 영하 3도로 하려면 부호 변환 |
| 35분 뒤 | 338–388행 | 첫 풀이에서 60분을 허용하고 24시로 넘어감. 뒤의 참고형에는 24시간 보정이 있음 |
| 두 자리 같은 숫자 | 390–418행 | 첫 풀이에서 범위보다 %11을 먼저 검사하여 0·110도 같음 처리 |
| 369 | 420–445행 | 십·일의 자리 풀이이므로 임의 자릿수 전체 검사로 일반화하지 않음 |
| 사각형 포함 | 447–450행 | 내 파일에는 문제 주석만 있음. 풀이 완료로 표시하지 않음 |

온도 문제의 -1 곱하기는 ‘정수로 변환’이 아니라 부호를 바꾸는 계산이다. 예를 들어 -3.5에 -1을 곱하면 3.5이며 여전히 소수다. 원본의 임의 온도 경고 문구는 수업 출력 예제이지 건강 판단 기준으로 사용하지 않는다.

### 내 시간 풀이의 참고형

강사님 기본 파일에는 시간 문제 조건만 있고, 다음 코드는 **내 파일에 저장된 참고형**이다. 이름만 보고 강사님 원본이라고 붙이지 않는다.

출처: `me/workspace_html/javascript/03_if.html` 376–387행 · **원본 발췌**

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

이 코드 역시 블록 주석 안에 있다. 35분을 더한 뒤 60분 이상이면 시간을 올리고 분을 줄인다. 시간이 24 이상이면 24를 뺀다. 한 번에 35분만 더하는 이 문제에서는 각 보정 한 번이면 충분하다. 더하는 시간이 매우 큰 경우까지 보장하는 일반 날짜 계산기는 아니다.

<a id="section-5"></a>

## 5. 교정 예제와 복습

아래는 원본 발췌가 아니라 **배운 연산자로 다시 쓴 교정 예제**다. 입력 검증 전체 구현은 생략하고 num이 정상 숫자라고 가정한다.

```javascript
let num = 0;
if (num > 0) {
    console.log('양수');
} else if (num === 0) {
    console.log(0);
} else {
    console.log('음수');
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

1. 위 코드의 출력 두 개는?
2. 3 < a < 20 대신 왜 3 < a && a < 20을 쓰는가?
3. 사각형 x=10–90, y=20–100에 테두리를 포함하여 점이 속하는 조건은?

<details>
<summary>정답 확인</summary>

1. 숫자 0과 '0시 26분'이다.
2. 앞 비교가 true/false가 된 다음 다시 20과 비교되기 때문이다. 두 범위 조건을 &&로 연결해야 한다.
3. `x >= 10 && x <= 90 && y >= 20 && y <= 100`이다. 원본 문제를 바탕으로 작성한 복습 답이며 내 파일의 완성 코드 인용은 아니다.

</details>

<a id="section-6"></a>

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/03_JavaScript_조건문과_Switch_연습문제.md)

## 추가로 알면 좋은 것

객체 매핑으로 모든 분기를 재설계하는 방법, 회원 등급 앱, Number.isInteger 기반 입력 검증 체계는 별도 확장이다. 본문에서는 실제 수업 문제의 조건·경계·출력 교정에 집중한다.

