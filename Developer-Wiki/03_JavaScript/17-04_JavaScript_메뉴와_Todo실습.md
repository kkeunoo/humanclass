# 17-04. 메뉴 선택과 Todo — 여러 요소의 상태 관리

[JavaScript 목차](README.md) · [이전: 주문·로그인·피자](17-03_JavaScript_주문_로그인_피자실습.md)

강사님의 `퀴즈/이벤트.html`과 내 `17_event_form.html`·`asset/js/17_event_form.js`를 비교한다. 메뉴는 한 항목만 강조하고, Todo는 생성·개별 삭제·전체 선택·선택 삭제가 목표다. **실습 의도와 현재 실행 결과를 구분해 읽자.**

<!-- chapter-toc -->

- [1. 메뉴 한 개 강조하기](#section-1)
- [2. Todo 추가·삭제](#section-2)
- [3. 전체 선택과 선택 삭제](#section-3)
- [직접 확인할 질문](#section-4)
- [추가로 알면 좋은 것](#section-5)

<a id="section-1"></a>

## 1. 메뉴 한 개 강조하기

### 강사님 코드

출처: `teacher/workspace_html/javascript/퀴즈/이벤트.html` 163~173행 · **원본 발췌**

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

`ul`에 클릭 리스너 하나를 두고 모든 `li`의 `bold`를 지운 다음 클릭한 요소에 붙인다. HTML에서 클릭 대상이 `li`이므로 작동한다. `ul`의 빈 곳을 누르면 `ul`에 붙을 수 있다는 점은 현재 코드의 한계다.

### 내 코드

출처: `me/workspace_html/javascript/asset/js/17_event_form.js` 333~378행 · **원본 발췌**

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

나는 메뉴마다 리스너를 붙였다. 클릭한 항목에 `true` 클래스를 추가하지만 다른 메뉴의 `true`는 제거하지 않는다. 다시 누를 때마다 `✔`도 중복해서 붙는다. 로컬 화면에서 같은 항목을 두 번 눌러 **`✔✔인기상품순`**이 되는 것을 확인했다. `textKeep`에 직전 글자를 저장하지만 되돌리는 데 사용하지 않는다. 즉, 주석의 **하나만 선택되게 하기**와 실제 실행은 다르다.

수업에서 배운 방식으로 고치려면 클릭할 때 모든 메뉴의 `true`와 굵은 글씨를 먼저 지우고, 기존 `✔`를 정리한 뒤 현재 메뉴만 강조한다. 이 경우 강사님의 한 부모 리스너 방식은 새 메뉴를 추가해도 같은 리스너가 처리할 수 있어 더 간결하다.

<a id="section-2"></a>

## 2. Todo 추가·삭제

### 강사님 코드

출처: `teacher/workspace_html/javascript/퀴즈/이벤트.html` 174~222행 · **원본 발췌**

```javascript
function q5(){
    document.querySelector('#q5 #add').addEventListener('click', function(event){
        const todo = document.querySelector('#q5 #todo')
        const list = document.querySelector('#q5 #list')

/*
            <div style="display:flex; justify-content: space-between;">
                <input type="checkbox" class="chk">
                <span>할 일1</span>
                <button type="button" class="del">삭제</button>
            </div>
*/

        const div = document.createElement('div')
        div.style.justifyContent = 'space-between'
        div.setAttribute('style', 'display:flex; justify-content: space-between;')
        div.innerHTML = `
                <input type="checkbox" class="chk">
                <span>${todo.value}</span>
                <button type="button" class="del">삭제</button>
        `
        div.querySelector('.del').addEventListener('click', function(event){
            this.parentNode.remove()
        })
        div.querySelector('.chk').addEventListener('click', function(event){
            // if(event.currentTarget.checked == false)
            if(!event.currentTarget.checked){
                document.querySelector('#q5 .chk_all').checked = false
            } else {
                const chks = document.querySelectorAll('#q5 .chk')
                let count = 0
                for(let i=0; i<chks.length; i++){
                    if(chks[i].checked){
                        count++
                    }
                }
                const chks_c = document.querySelectorAll('#q5 .chk:checked')
                // if(count == chks.length){
                console.log(chks_c.length , chks.length)
                if(chks_c.length == chks.length){
                    document.querySelector('#q5 .chk_all').checked = true
                }
            }
        })

        list.prepend(div)
        document.querySelector('#q5 .chk_all').checked = false
        todo.value = ''
    })
```

강사님은 입력값으로 새 `div`를 만들고 체크박스·삭제 버튼을 연결한 뒤 `prepend`로 맨 위에 놓는다. 새 항목을 추가하면 전체 선택을 해제한다. 코드에는 빈 문자열 검사가 없어 빈 Todo도 추가된다. `innerHTML`에 입력값을 직접 넣는 점도 수업 코드의 한계다.

### 내 코드

출처: `me/workspace_html/javascript/asset/js/17_event_form.js` 393~451행 · **원본 발췌**

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

내 코드는 `trim()`으로 빈 입력을 검사하고 체크하면 취소선을 보여 준다. 다만 **빈 입력을 검사하기 전에 `prepend(divAdd)`를 실행**해 빈 줄이 먼저 생긴다. 빈 입력 시 `divAdd.innerHTML`은 비어 있으므로 이어지는 `deleteCol.addEventListener(...)`에서 `deleteCol`이 `null`인 오류도 난다. 로컬 화면 검수에서 빈 항목을 시도한 뒤 입력값이 있는 항목을 추가했을 때 빈 `div`가 남고 `null` 오류가 기록됐다. 새 항목을 두 개 이상 만든 뒤에는 `document.querySelector('.deleteCol')`가 항상 맨 위 항목을 찾는다. 각 항목의 리스너가 자신이 만든 버튼에 붙도록 `divAdd.querySelector(...)`를 써야 한다.

<a id="section-3"></a>

## 3. 전체 선택과 선택 삭제

### 강사님 코드

출처: `teacher/workspace_html/javascript/퀴즈/이벤트.html` 224~259행 · **원본 발췌**

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

전체 선택 클릭 때 그 시점의 체크박스를 모두 찾아 `this.checked`와 맞춘다. 선택 삭제는 `:checked`인 항목만 찾아 부모 줄을 지운다. 개별 체크박스 리스너는 하나가 해제되면 전체 선택을 풀고, 전부 체크되면 다시 켠다. 삭제 뒤 전체 선택 표시를 즉시 재계산하지 않는 경우는 남아 있다.

### 내 코드

출처: `me/workspace_html/javascript/asset/js/17_event_form.js` 453~500행 · **원본 발췌**

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

내 코드는 항목을 추가할 때마다 전체 선택·선택 삭제 리스너를 다시 등록한다. 각각 새로 만든 `deleteChk`, `divAdd`만 가리키므로 항목이 늘면 리스너도 누적된다. 더 결정적인 문제는 `chkBox[j]`의 **`j`가 선언되지 않았다는 점**이다. 로컬 화면에서 항목 추가 후 `ReferenceError: j is not defined`가 기록됐다. 이 줄을 `i`로 바꾸는 것만으로는 누적 리스너와 전체 선택 상태 계산 문제가 해결되지 않는다.

### 수업 범위 안에서 고치는 순서

1. 입력이 비었으면 **요소를 만들거나 붙이기 전에** 바로 종료한다.
2. 새 `div`의 삭제·체크 버튼은 `divAdd.querySelector(...)`로 잡는다.
3. 전체 선택·선택 삭제 리스너는 항목 추가 리스너 **밖에서 한 번씩만** 등록한다.
4. 체크 상태가 바뀔 때 현재 `.deleteChk`를 다시 조회해 전체 선택 표시를 계산한다.

강사님 코드는 3·4번의 참고가 된다. 내 코드의 빈 값 검사와 취소선은 살릴 수 있다. 추가한 항목의 HTML을 한 번에 문자열로 넣는 방식은 양쪽 코드에 있지만, 사용자 입력을 그대로 `innerHTML`에 넣는 것은 실제 서비스용 방식으로 옮기기 어렵다.

<a id="section-4"></a>

## 직접 확인할 질문

1. Todo에 공백만 입력하고 추가하면 내 코드에서는 어느 줄까지 실행될까?
2. Todo가 세 개일 때 전체 선택 버튼의 리스너는 내 코드에서 몇 번 등록됐을까?
3. 메뉴를 같은 항목에서 두 번 누르면 글씨 앞의 `✔`는 어떻게 될까?

<a id="section-5"></a>

## 추가로 알면 좋은 것

Todo 문장을 화면에 넣을 때 `textContent`로 글자를 넣으면 입력값을 HTML로 해석하지 않는다. 이 차이는 실제 서비스를 만들 때 중요하지만, 여기서는 먼저 수업에서 다룬 이벤트·요소 생성·상태 갱신의 흐름을 이해한다.

