# 17-04. 메뉴와 Todo — 한 번의 조작 뒤 화면 상태를 맞추기

[JavaScript 목차](README.md) · [읽기 안내](00_JavaScript_V3_동작_백과_읽기법.md)

메뉴를 여러 번 누르고 Todo를 추가·삭제하면 처음에는 보이지 않던 문제가 나타난다. 한 번 잘 보이는 것과 여러 조작 뒤에도 상태가 맞는 것은 다르다. 작은 화면을 직접 바꾸면서 등록 시점·선택 범위·검사 순서를 읽어 보자.

<a id="chapter-toc"></a>

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

한 메뉴만 강조하고 표시가 중복되지 않게 한다. Todo의 생성·개별 삭제·전체 선택·선택 삭제를 연결하며, 공통 버튼은 한 번 등록하고 현재 항목 상태를 다시 계산하는 이유를 설명한다.

입력·현재 상태·실행 순서·결과를 분리해 설명한다. 실제 수업 원본은 아래에 표시하고, 원본에 없는 선택 학습은 9절 TIP에 둔다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

화면 상태는 “어느 메뉴가 선택됐는가, 어떤 할 일이 체크됐는가” 같은 현재 정보다. 메뉴가 한 개만 선택되어야 한다면 모든 항목의 이전 강조를 지운 뒤 현재 항목만 강조한다. 선택 표시를 글자 앞에 계속 더하면 원래 글자와 상태가 섞여 ✔가 누적될 수 있다. 아래 개선 예제는 CSS 클래스로 표시하여 문구 자체를 바꾸지 않는다.

Todo 한 줄은 체크박스·내용·삭제 버튼을 묶은 요소다. 줄을 만들 때는 입력 검사 → 요소 생성 → 자식 구성 → 이벤트 연결 → 목록에 추가 순서로 읽는다. 검사 실패 때는 그 전에 종료해야 빈 줄이나 없는 버튼에 연결하는 오류를 피할 수 있다.

| 처리 | 등록·조회 시점 | 이유 |
| --- | --- | --- |
| 새 줄의 삭제·체크 | 줄을 만들 때 그 줄에 등록 | 자신이 속한 항목 처리 |
| 전체 선택·선택 삭제 | 처음 한 번 등록 | 항목마다 공통 버튼 등록이 누적되지 않음 |
| 현재 체크 목록 | 조작할 때 다시 조회 | 추가·삭제된 항목까지 현재 상태 반영 |
| 전체 선택 표시 | 상태 변경 뒤 재계산 | 일부 해제·삭제·빈 목록까지 일치 |

현재 목록이 비면 전체 선택은 false로 정한다. 체크 수와 전체 수가 모두 0이라고 “전부 체크”로 표시하면 빈 화면에서 혼동하기 쉽기 때문이다. 이것은 아래 개선 예제에서 명시한 화면 규칙이다.

> 📚 **출처 · 본문 설명 확인:** [MDN Element.querySelector](https://developer.mozilla.org/en-US/docs/Web/API/Element/querySelector). 배운 기능의 뜻을 확인한 근거다. 예제·표·풀이 흐름은 수업 코드를 바탕으로 새로 작성했으며 외부 문장을 직접 인용하지 않았다. 확인일: 2026-10-28.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 스크립트.** [HTML 실행 파일](실습/책형_복습/17-04_JavaScript_메뉴와_Todo실습.html)과 같은 폴더의 [JS 파일](실습/책형_복습/17-04_JavaScript_메뉴와_Todo실습.js)을 함께 내려받는다. HTML을 브라우저로 열고 Console에서 결과를 확인한다. script는 필요한 HTML 뒤에 연결한다. 콘솔 출력은 페이지 본문에 자동으로 쓰이지 않는다.

**먼저 준비할 HTML · body 안:**

```html
    <ul id="menu"><li><button type="button">인기순</button></li><li><button type="button">최신순</button></li></ul>
    <label>할 일 <input id="todo"></label><button id="add" type="button">추가</button>
    <p id="warning"></p>
    <label><input id="all" type="checkbox">전체 선택</label>
    <button id="deleteSelected" type="button">선택 삭제</button>
    <div id="list"></div>
```

**위 파일 head의 style:**

```css
.selected { font-weight: bold; } .selected::before { content: "✔ "; } .row { display: flex; gap: 8px; margin: 8px 0; } .done { text-decoration: line-through; }
```

```javascript
const menuButtons = document.querySelectorAll('#menu button');
for (const button of menuButtons) {
    button.addEventListener('click', function () {
        for (const item of menuButtons) item.classList.remove('selected');
        this.classList.add('selected');
    });
}
const list = document.getElementById('list');
const all = document.getElementById('all');
function syncAll() {
    const checks = list.querySelectorAll('.chk');
    const checked = list.querySelectorAll('.chk:checked');
    all.checked = checks.length > 0 && checks.length === checked.length;
}
function paintRow(check) {
    const text = check.parentNode.querySelector('span');
    if (check.checked) text.classList.add('done');
    else text.classList.remove('done');
}
document.getElementById('add').addEventListener('click', function () {
    const input = document.getElementById('todo');
    const warning = document.getElementById('warning');
    if (input.value.trim() === '') {
        warning.textContent = '한 글자 이상 입력';
        return;
    }
    warning.textContent = '';
    const row = document.createElement('div');
    row.classList.add('row');
    const check = document.createElement('input');
    check.type = 'checkbox';
    check.classList.add('chk');
    check.setAttribute('aria-label', '할 일 선택');
    const text = document.createElement('span');
    text.textContent = input.value.trim();
    const del = document.createElement('button');
    del.type = 'button';
    del.textContent = '삭제';
    del.addEventListener('click', function () {
        row.remove();
        syncAll();
    });
    check.addEventListener('click', function () {
        paintRow(check);
        syncAll();
    });
    row.append(check, text, del);
    list.prepend(row);
    input.value = '';
    syncAll();
});
all.addEventListener('click', function () {
    const checks = list.querySelectorAll('.chk');
    for (const check of checks) {
        check.checked = this.checked;
        paintRow(check);
    }
    syncAll();
});
document.getElementById('deleteSelected').addEventListener('click', function () {
    const checks = list.querySelectorAll('.chk:checked');
    for (const check of checks) check.parentNode.remove();
    syncAll();
});
```

메뉴의 인기순을 두 번, 최신순을 한 번 눌러도 ✔가 문구에 누적되지 않고 최신순만 강조된다. 빈 입력으로 추가하면 경고만 보이고 줄은 없다. 첫째·둘째를 순서대로 추가하면 prepend 때문에 둘째가 위다. 전체 선택한 뒤 둘째만 해제하면 전체 선택도 풀린다. 선택 삭제는 체크가 남아 있는 첫째만 지운다. 남은 둘째를 개별 삭제하면 빈 목록과 전체 선택 해제가 유지된다. 이 예제는 Console 대신 화면 상태를 확인한다. 새 개선 예제이며 원본 오류를 숨겨 원래 완성 코드였던 것으로 소개하지 않는다.

**예상 출력 또는 관찰:**

```text
빈 입력: 경고, 줄 0개
첫째·둘째 추가: 둘째가 위, 줄 2개
전체 선택 후 둘째 해제: 전체 선택 해제
선택 삭제: 둘째만 남음
남은 줄 삭제: 줄 0개, 전체 선택 해제
```

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 원본의 일부다. 원본에 의존하는 앞 선언·HTML·함수는 다음 절의 연결까지 읽는다. 주석의 잘못된 표현도 원문대로 보존하고 설명에서 교정한다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/asset/js/17_event_form.js` 333–378행

```javascript
    /*
        문제4_메뉴 선택
        인기상품순, 낮은가격순, 높은가격순, 신상품순, 상품평 많은순 눌렀을 때
        색이 진해지면서 V표시정도 되게끔 (클래스를 줬다뺐다)
    */
    const items = document.querySelector('#items')
    const itemSet = document.querySelectorAll('[class^=item]')
    console.log(items.classList.contains('true'))
    console.log(itemSet)
    let textKeep = ''

    // click했을 때 'true'라는것을 주기 전에 다 제거해서
    // 없애준 뒤에 click한 값만 'true;'라는걸 다시 줌

    // itemSet.setAttribute('click', 'false')
    for(let i=0; i<itemSet.length; i++) {
    // textKeep = items[0].innerText
        itemSet[i].addEventListener('click', function(event){
            // console.log(itemSet[i].classList.contains('true'))
            // itemSet[i].classList.remove('true')
            event.target.classList.add('true')
            // console.log(clsValue)
            textKeep = event.target.innerText
            
            if(event.target.classList.contains('true')) {
                
                event.target.style.fontWeight = 'bold'
                event.target.innerText = '✔' + event.target.innerText
            } 
            // event.target.classList.remove('true')
            // console.log(itemSet.classList.contains('true'))
            // itemSet[i].addEventListener('mouseout', function(event) {
            //     event.target.classList.remove('true')
            //     event.target.style.fontWeight = ''
            //     event.target.innerText = textKeep
            // })
        })
        // if(itemSet[i].classList.contains('true')) {
        //     console.log('있어용')
        // }
        // itemSet[i].addEventListener('mouseout', function(event) {
        //     event.target.style.fontWeight = ''
        //     event.target.classList.remove('true')
        //     event.target.innerText = textKeep
        // })
    }
```

**발췌 바로 풀이:** 나는 메뉴마다 리스너를 붙였다. 클릭한 항목에 `true` 클래스를 추가하지만 다른 메뉴의 `true`는 제거하지 않는다. 다시 누를 때마다 `✔`도 중복해서 붙는다. 로컬 화면에서 같은 항목을 두 번 눌러 **`✔✔인기상품순`**이 되는 것을 확인했다. `textKeep`에 직전 글자를 저장하지만 되돌리는 데 사용하지 않는다. 즉, 주석의 **하나만 선택되게 하기**와 실제 실행은 다르다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/asset/js/17_event_form.js` 393–451행

```javascript
    /*
        문제5_Todo List
        [할 일] [추가버튼] 
        + 문제5-1 : 추가버튼을 눌렀을 때 리스트 안에 추가되도록
        단, 앞에 체크박스가 같이 생기면서 체크하면 취소선 가도록
        위에 쌓이도록 진행

        + 문제 5-2 : 개별 삭제 버튼을 추가로 넣어서 삭제 버튼 눌렀을 때
        줄 전체가 지워져야 함 (체크누르면 제목나왔던애랑 비슷함) dom.remove() 사용

        + 문제 5-3 : 좌상단에 전체선택 버튼이 있고 누르면 체크박스 전체 선택되도록
        + 문제 5-4 : 전체 선택 후에 하나라도 개별 해제가 되면, 전체 선택도 해제(고른것만 남아있고)
        일일히 나머지 대상을 선택했을 때 전체선택칸도 선택되게끔
        + 문제 5-5 : 선택삭제 라는 버튼이 추가되어 선택한 것만 삭제할 수 있도록
    */

    const inputDiv = document.querySelector('#inputDiv')
    let divCnt = 0
    inputDiv.addEventListener('click', function() {
        const column = document.querySelector('#column')
        const inputText = document.querySelector('#inputText')
        const divAdd = document.createElement('div')
        // const checkDel = document.querySelector('#checkDel')
        divCnt++
        
        for(let i=1; i<2; i++) {
            divAdd.classList.add(`col${divCnt}`)
        }
        column.prepend(divAdd)

        // console.log(inputText.innerText)
        if(inputText.value.trim() == '') {
            alert('할일은 한 글자 이상 입력하세요.')
        } else {
            divAdd.innerHTML = `
            <input type="checkbox" class=deleteChk>
            ${inputText.value}
            <button type="button" class="deleteCol">삭제</button>
            `

            inputText.value = ''
        }

        const deleteCol = document.querySelector('.deleteCol')
        // console.log(divAdd)
        // console.log(deleteCol)
        deleteCol.addEventListener('click', function() {
            divAdd.remove()
        })

        const deleteChk = document.querySelector('.deleteChk')
        deleteChk.addEventListener('click', function(){
            if(deleteChk.checked == true) {
                console.log('체크됨')
                deleteChk.parentNode.style.textDecoration = 'line-through'
            } else {
                deleteChk.parentNode.style.textDecoration = ''
            }
        }) 
```

**발췌 바로 풀이:** 빈 입력을 검사하기 전에 새 div를 붙인다. 처음부터 빈 값이면 삭제 버튼이 없어 null 오류가 난다. 정상 항목을 추가한 경우에는 prepend 직후 첫 버튼이 새 줄의 버튼과 일치한다. 반면 기존 정상 항목 뒤 빈 줄을 추가하면 그 기존 버튼에 빈 줄을 삭제하는 함수도 붙을 수 있다. 따라서 문서 전체 선택이 정상 입력에서도 언제나 잘못된 대상을 고른다고 단정하지 않는다. 개선에서는 검사 후 생성하고 각 줄 안에서 조회하여 범위를 분명히 한다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/asset/js/17_event_form.js` 453–500행

```javascript
        const allChk = document.querySelector('#allChk')
        allChk.addEventListener('click', function() {
            if(allChk.checked == true) { 
                console.log(1)
                deleteChk.checked = true
                deleteChk.parentNode.style.textDecoration = 'line-through'
            } else {
                deleteChk.checked = false
                deleteChk.parentNode.style.textDecoration = ''
            }
        })

        const checkDel = document.querySelector('#checkDel')
        checkDel.addEventListener('click', function(){
            if(deleteChk.checked == true) {
                divAdd.remove()
            }
        })

        const chkBox = document.querySelectorAll('.deleteChk')
        console.log('chkBox', chkBox)
        // let cnt = 0
        // for(let j=0; j<chkBox.length; j++) {
        //     if(chkBox[j].checked) {
        //         cnt++
        //     } else if(!chkBox[j].checked){
        //         cnt--
        //     }

        //     if(cnt == chkBox.length) {
        //         allChk.checked = true
        //     } else {
        //         allChk.checked = false
        //     }

        chkBox[j].addEventListener('click', function() {
            if(chkBox[j].checked) {
                allChk.checked = false
            } 
            for(let i=0; i<chkBox.length; i++) {
                if(chkBox[i].checked == false) {
                    allChk.checked = false
                } 
            }
        })
        // chkBox[i].checked = allChk.checked

        
```

**발췌 바로 풀이:** 내 코드는 항목을 추가할 때마다 전체 선택·선택 삭제 리스너를 다시 등록한다. 각각 새로 만든 `deleteChk`, `divAdd`만 가리키므로 항목이 늘면 리스너도 누적된다. 더 결정적인 문제는 `chkBox[j]`의 **`j`가 선언되지 않았다는 점**이다. 로컬 화면에서 항목 추가 후 `ReferenceError: j is not defined`가 기록됐다. 이 줄을 `i`로 바꾸는 것만으로는 누적 리스너와 전체 선택 상태 계산 문제가 해결되지 않는다.

내 메뉴는 현재 항목에 true 클래스를 붙이고 글자 앞에 ✔를 더한다. 다른 항목의 상태를 지우는 활성 코드는 없으므로 여러 항목이 굵어지고 같은 항목은 ✔가 누적된다. Todo는 빈 입력을 검사하기 전에 div를 prepend한다. 첫 항목부터 빈 값이면 삭제 버튼이 없어 null에 addEventListener를 호출한다. 정상 입력에서는 새 줄이 맨 앞에 있으므로 문서 전체 querySelector가 우연히 그 줄의 버튼을 찾는다. 다만 정상 항목이 있는 뒤 빈 줄을 추가하면 기존 버튼을 잡아 그 버튼에 빈 줄을 지우는 함수까지 붙일 수 있다. 이어지는 chkBox[j]는 j가 선언되지 않아 ReferenceError가 난다.

<a id="connections"></a>

## 5. 선언·호출·파일이 연결되는 흐름

add 클릭 → 입력 검사 → 새 row와 check·text·del 준비 → 각 자식 이벤트 등록 → row에 자식 추가 → list.prepend → syncAll 호출이다. paintRow는 체크 상태를 취소선 클래스로 반영하고 syncAll은 현재 목록을 다시 찾아 전체 선택을 계산한다. 전체 선택에서 check.checked를 직접 대입해도 개별 click 함수가 저절로 실행되지는 않으므로 paintRow를 명시적으로 호출한다. 삭제 후에도 syncAll을 호출하여 같은 상태 규칙을 유지한다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 빈 입력을 막으려는 검사와 체크 취소선은 살릴 가치가 있다. **실제 오류:** 빈 값 검사보다 요소 부착이 먼저이며 j가 선언되지 않았다. **구조상 한계:** 추가할 때마다 전체 선택·선택 삭제 리스너를 새로 등록하므로 공통 버튼의 처리 수가 누적된다. **개선:** 검사를 맨 앞으로 옮기고 항목 내부 참조는 자신이 만든 요소로 한정한다. 공통 등록은 밖에서 한 번만 한다. j를 i로 바꾸는 것만으로 나머지 문제가 해결되지는 않는다.

개선안은 원본을 수정한 결과가 아니다. 실제 오류, 수업용 단순화, 목적에 따른 선택을 구별해 판단한다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교

출처: `D:/workspace_teacher/workspace_html/javascript/퀴즈/이벤트.html` 163–173행

```javascript
function q4(){
    document.querySelector('#q4 ul').addEventListener('click', function(event){
        
        event.currentTarget.querySelectorAll('li').forEach(function(li){
            // if(li.classList.contains('bold')){
                li.classList.remove('bold')
            // }
        })
        event.target.classList.add('bold')
    })
}
```

출처: `D:/workspace_teacher/workspace_html/javascript/퀴즈/이벤트.html` 224–259행

```javascript
    const list = document.querySelector('#q5 #list')
    list.addEventListener('click', function(event){
        if( event.target.classList.contains('del') ){
            event.target.parentNode.remove()
        }
        if( event.target.classList.contains('chk') ){
            console.log('해당 줄의 checkbox 클릭')
        }
    })

    document.querySelector('#q5 .chk_all').addEventListener('click', function(event){
        const chks = document.querySelectorAll('#q5 .chk')
        // if(this.checked){
        //     for(let i=0; i<chks.length; i++){
        //         chks[i].checked = true
        //     }
        // } else {
        //     for(let i=0; i<chks.length; i++){
        //         chks[i].checked = false
        //     }
        // }

        for(let i=0; i<chks.length; i++){
            chks[i].checked = this.checked
        }

    })

    document.querySelector('#q5 .del_selected').addEventListener('click', function(event){
        const chks_c = document.querySelectorAll('#q5 .chk:checked')
        let i=0
        while(i<chks_c.length){
            chks_c[i].parentElement.remove()
            i++
        }
    })
```

강사님 메뉴는 모든 li의 강조를 제거한 뒤 현재 항목을 강조하여 한 개 선택 규칙이 명확하다. 다만 ul 빈 곳을 누르면 ul에 강조를 붙일 가능성은 남는다. 강사님의 전체 선택·선택 삭제는 새 항목 추가 밖에서 등록하여 참고할 만하다. 강사님 코드도 빈 Todo를 막지 않고 입력을 innerHTML에 넣으며 삭제 후 전체 선택 재계산이 완전하지 않다. 잘된 구조를 가져오되 강사님 원본 전체를 완성된 서비스 코드로 평가하지 않는다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 상황 | 원본에서 확인한 결과 | 개선 예제의 규칙 |
| --- | --- | --- |
| 메뉴 같은 항목 두 번 | ✔✔ 누적 | 클래스 표시 한 번 |
| 처음부터 빈 Todo | 빈 div 뒤 null 오류 | 생성 전에 종료 |
| 정상 Todo 두 개 | 각각 추가되나 j 오류 발생 | 선언된 반복 변수 사용 |
| 정상 항목 뒤 빈 Todo | 기존 삭제 버튼에 빈 줄 삭제도 연결 가능 | 빈 값은 DOM 변화 없음 |
| 항목 추가 반복 | 공통 버튼 리스너 누적 | 공통 등록 한 번 |

이번 별도 headless 브라우저 검수에서 원본의 네 상황을 확인했다. 정상 항목 두 개 뒤 예전 항목 삭제는 해당 항목을 지웠다. 따라서 “문서 전체 querySelector이므로 정상 입력에서도 언제나 틀린 버튼”이라는 기존 설명은 교정했다. 범위를 좁히는 개선의 근거와 실제 발생한 오류를 나누어 기록한다. D 드라이브 원본은 수정하지 않았다.

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| prepend를 append로 | 첫째가 위에 남음 | 추가 위치 차이 |
| syncAll의 길이 > 0 조건 제거 | 빈 목록을 전부 체크로 계산 가능 | 0과 0도 같음 |
| 삭제 후 syncAll 제거 | 전체 선택 표시가 오래 남을 수 있음 | 화면 상태 재계산 누락 |
| paintRow 호출 제거 | 직접 checked 대입 때 취소선이 안 맞음 | 속성 변경은 click 실행이 아님 |

빈 줄이 생기면 검사보다 먼저 DOM을 바꿨는지 본다. j 오류는 실행 줄과 변수 선언 범위를 확인한다. 공통 버튼이 여러 번 반응하면 등록이 추가 콜백 안에 있는지 살핀다. 체크와 취소선이 다르면 checked 값 대입 뒤 표시 갱신까지 했는지 확인한다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** 새로고침 뒤 유지하는 저장 기능, 서버와의 동기화, 복잡한 상태 관리 도구와 접근성 전체 설계는 추가 학습이다. 기본 예제는 수업에서 배운 DOM·함수·배열/반복·클래스 조작으로 구성한다.



이 절의 확장은 기본 문제의 필수 조건이 아니다. 📚 출처가 있다는 것과 수업 밖 기능이라는 것은 다른 구분이다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. 빈 값 검사는 어느 단계보다 먼저 해야 하는가?
2. 전체 선택 리스너를 추가 함수 안에서 등록하면 무엇이 누적되는가?
3. checked를 대입하면 개별 click 리스너가 자동 실행되는가?
4. 전체 0개·선택 0개일 때 왜 별도 조건을 두었는가?

<details>
<summary>짧은 풀이 — 먼저 답한 뒤 확인</summary>

요소를 만들거나 붙이기 전에 검사한다. 추가할 때마다 공통 버튼의 새 리스너가 쌓인다. checked 대입은 click을 자동 발생시키지 않는다. 빈 목록을 선택 완료로 보이지 않게 하려는 명시적인 화면 규칙 때문이다.

</details>

| 단계 | 확인할 것 |
| --- | --- |
| 검사 | 실패 시 DOM을 바꾸기 전 종료 |
| 등록 | 항목별과 공통 버튼 분리 |
| 조회 | 현재 목록과 해당 줄의 범위 |
| 갱신 | 체크·취소선·전체 선택 일치 |

[장별 연습문제](실습/연습문제/17-04_JavaScript_메뉴와_Todo실습_연습문제.md)에서 예상·설명·수정을 이어 간다. 다음은 [브라우저 이동](18_JavaScript_브라우저이동과_지도우편번호.md)이다.

<!-- 이전 색인 이동 주소 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>

[이 장의 목차](#chapter-toc)에서 현재 설명을 찾는다.
