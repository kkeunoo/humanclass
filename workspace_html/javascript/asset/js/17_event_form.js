function log(message) {
    const div = document.createElement('div')
    div.classList.add('log')
    div.innerHTML = message
    const view = document.querySelector('#view')
    view.prepend(div)
}


// window.onload = 
window.addEventListener('load', function() {

    const query = document.querySelector('#query')
    // focus는 초점이 가있을 때, blue는 초점을 잃었을 때
    // 아래와 같은 부분은 textbox를 클릭했을 때와 밖으로 나왔을 때
    query.addEventListener('focus', function() {
        query.style.backgroundColor = 'yellow'
    })
    query.addEventListener('blur', function() {
        query.style.backgroundColor = ''
    })
    // input은 텍스트 자체가 바뀌는걸 감지하기 때문에, 마우스 우클릭으로
    // 붙여넣기 해도 값이 들어가면 감지하는 이벤트
    query.addEventListener('input', function() {
        log(query.value)

        const r = parseInt(Math.random() * 256)
        const g = parseInt(Math.random() * 256)
        const b = parseInt(Math.random() * 256)
        const a = Math.random()

        query.style.backgroundColor = `rgba(${r}, ${g}, ${b}, ${a})`

    })


    const form = document.querySelector('#form')
    form.addEventListener('submit', function(event){
        
        // prevent는 태그의 기본 고유 기능을 막는다는 함수 (submit 등)
        event.preventDefault()

        if(query.value.trim().length < 2) {
            alert('검색어는 두 글자 이상입니다.')
        } else {
            form.submit()
        }
    })


    // 부모를 클릭해도 적용되지만, 자식을 클릭해도 적용 됨 
    // 클릭해도, 바디부터 자식으로 내려가고(버블링) 다시 자식부터 부모쪽으로 올라가는 단계가 있는데(캡쳐링)
    // addEventListener는 자식에서 부모쪽으로 올라가는 단계가 포함되어있기 때문
    const parent = document.querySelector('#parent')
    // 이벤트는 부모에게 주었지만, 자식을 클릭할 때 마다 target으로 작동(위임)
    parent.addEventListener('click', function(event) {
        log('부모 클릭')

        // target은 실제 이벤트가 발생 한 DOM을 가르키게 됨
        console.log('event.target', event.target)

        // currentTarget은 이벤트가 걸려있는 DOM이 나옴(현재 부모에게 적용되어있음)
        console.log('event.currenttarget', event.currentTarget)

        // this는 currentTarget과 동일하지만, 쉽게 쓸 수 있도록 만들어준 것
        // addEventListener 안에서는 event.currentTarget 를 의미
        // 기본적으로 this객체에는 'window'가 들어가있음
        // 편하지만, 지금 this가 뭔지 알 수 있을때만 사용해야 함 (arrow도 불가)
        console.log('this', this)
        console.log( this === event.currentTarget) // true

    })

    const child1 = document.querySelector('#child1')
    child1.addEventListener('click', function(event) {

        // preventDefault랑 비슷하지만 부모로 올라가는 내 이벤트를 stop
        // 부모에게 전달하는 것(캡쳐링) 방지
        event.stopPropagation()

        log('자식1 클릭')
    })

    // 1. click 된 DOM을 출력
    // 2. 지금 click 요소에 클래스 chk가 있는지 출력
    // 3. 만약, checkbox 일 때 value 출력
    // 4. 제목을 click했을 때 제목 출력
    // 5. 작성자를 click했을 때 속성 writer의 값 출력
    // 6. [같이] table말고 tr에 위임
    const board = document.querySelector('#board')
    board.addEventListener('click', function(event) {
        console.log(event.target)
        // log(event.target)

       if(event.target.classList.contains('chk')) {
            // console.log(event.target.value)
            log(event.target.value)
       }

       if(event.target.classList.contains('title')) {
            log(event.target.innerText)
       }

       // 원래라면 class가 들어가 있어야 하지만, writer로 들어가 있기 때문에
       // hasAttribute로 있는지 확인하고 getAttribute로 값을 가져오기
       if(event.target.hasAttribute('writer')) {
            log(event.target.getAttribute('writer'))
       }
    })

    // 7. [같이] check를 하면 제목이 출력되게 설정
    const trs = document.querySelectorAll('#board tr')
    // all을 쓰게되면 배열로 가져오기에 for문을 쓰는게 좋고, of로 배열의 처음부터 끝까지
    for( let tr of trs ) {
        tr.addEventListener('click', function(event) {
            console.log(event.target)
            // log(event.target)
    
            // tr안에 있는 chk라는 class를 가진 것을 true값 반환하고
            // true일 때 value 출력
            if(event.target.classList.contains('chk')) {
                // console.log(event.target.value)
                log(event.target.value)
            }
            
            // tr안에 있는 title이라는 class를 가진 것을 true값 반환하고
            // true일 때 text 출력
           if(event.target.classList.contains('title')) {
                log(event.target.innerText)
           }
    
           // 원래라면 class가 들어가 있어야 하지만, writer로 들어가 있기 때문에
           // hasAttribute로 있는지 확인하고 getAttribute로 값을 가져오기
           if(event.target.hasAttribute('writer')) {
                log(event.target.getAttribute('writer'))
           }
        })

        // input 태그이고 chk라는 class를 가진 것을 가져온 뒤 click 이벤트 설정
        tr.querySelector('input.chk').addEventListener('click', function(event) {
            // 부모에게 올라가는걸 막았기 때문에 target은 '나' 임
            event.stopPropagation()

            // 이렇게 쓰면 tr상위인 td로 올라갈 수 있음
            // console.log(this.parentNode)

            // parentNode를 사용해서 상위 부모까지 올라갈 수 있음 (형제 등 있을 때)
            console.log(
                this.parentNode.parentNode.querySelector('.title').innerText
            )
        })
    }
})


console.log(this)


window.addEventListener('load', function() {
    /*
        문제1_주문과 배송
        주문 정보 : input으로 이름, 주소를 적을 수 있음
        ㅁ(checkbox) 주문 정보와 배송 정보가 같습니다 
        배송 정보 : input으로 이름, 주소를 적을 수 있음
        * 체크하면 주문 정보 > 배송 정보로 데이터가 복사되도록
        * 체크를 풀면 배송 정보 글씨를 지우기
    */
    const valueChk = document.querySelector('.valueChk')
    valueChk.addEventListener('click', function(event){
        const name1 = document.querySelector('.name1')
        const name2 = document.querySelector('.name2')
        const address1 = document.querySelector('.address1')
        const address2 = document.querySelector('.address2')

        if(valueChk.checked == true) {
            name2.value = name1.value
            address2.value = address1.value
        } else {
            name2.value = ''
            address2.value = ''
        }
    })
    
    /*
        문제2_로그인창
        로그인 버튼을 눌렀을 때 아이디 / 비밀번호가 없으면,
        빨간 글씨가 나오게 (단, 아이디/비밀번호를 쓰고 로그인을 누르면 빨간 글씨 지우기)
    */
    const login = document.querySelector('#login')
    
    login.addEventListener('click', function(){
        const id1 = document.querySelector('.id1')
        const pw1 = document.querySelector('.pw1')
        const errChk = document.querySelector('.errChk')
        // console.log(errChk)
        
        if(id1.value.trim() == '') {
            errChk.innerText = '아이디를 입력하세요'
            // style은 css에 주고나서, Attribute를 줘서 적용시키는게 좋음
            errChk.style.color = 'red'
        } else if(pw1.value.trim() == '') {
            errChk.innerText = '패스워드를 입력하세요'
            errChk.style.color = 'red'
        } else {
            errChk.innerText = ''
        }
        // console.log(id1.value)
        // console.log(pw1.value)
    })

    /*
        문제3_피자주문
        1. 피자 종류 선택(select)
        - 불고기, 페퍼로니, 포테이토, 치즈, 파인애플, 고르곤졸라
        2. 사이즈 선택(radio)
        - small(18,000), medium(20,000), large(22,000)
        3. 도우 선택(radio)
        - 씬, 고구마, 치즈, 소보로
        4. 토핑_topping(checkbox)
        - 감자(2,000), 고구마(2,000), 치즈(2,500), 베이컨(3,000), 옥수수(500), 페퍼론치노(2,500)
        [확인] 
        + 문제3_1 : 선택 내역 모두 출력
        + 문제3_2 : 선택 내역과 총액 출력

        value에 small 18000 이런식으로도 가능하지만,
        속성값에 '가격'이라는것을 따로 줘서 진행해도 됨
    */
   // 최종정리본
   const pay = document.querySelector('#pay')
   pay.addEventListener('click', function(){
       const order = document.querySelector('#order')
       const size = document.querySelector('[name=size]:checked')
       const dough = document.querySelector('[name=dough]:checked')
       const topping = document.querySelectorAll('.topping')
       const orderChk = document.querySelector('#orderChk')
       const orderPrice = document.querySelector('#orderPrice')
       let topResult = ''
       let topPrice = 0
       let priceResult = 0

       for(let i=0; i<topping.length; i++) {
           if(topping[i].checked == true) {
               // console.log('토핑', topping[i].value.split(' ')[0])
               topResult += topping[i].value.split(' ')[0]
               topPrice += Number(topping[i].value.split(' ')[1])
           }
       }
       priceResult += topPrice + Number(size.value.split(' ')[1])

       orderChk.innerText = 
       `종류: ${order.value}, 사이즈: ${size.value.split(' ')[0]}, 도우: ${dough.value}, 토핑:${topResult}`
       orderPrice.innerText = `총액: ${priceResult}원`
    }) 
    
    // 정리본
    //확인버튼(pay)를 누를 때 동작하도록 함수 설정
    // const pay = document.querySelector('#pay')
    // pay.addEventListener('click', function(){
    //     const order = document.querySelector('#order')
    //     const size = document.querySelector('[name=size]:checked')
    //     const dough = document.querySelector('[name=dough]:checked')
    //     const topping = document.querySelectorAll('.topping')
    //     const orderChk = document.querySelector('#orderChk')
    //     const orderPrice = document.querySelector('#orderPrice')
    //     let topResult = ''
    //     let topPrice = 0
    //     let priceResult = 0
        
    //     // console.log(order.value)
    //     // console.log(size.value.split(' ')[0])
    //     // console.log(dough.value)

    //     // 주로 체크박스에서 사용
    //     for(let i=0; i<topping.length; i++) {
    //         if(topping[i].checked == true) {
    //             // console.log('토핑', topping[i].value.split(' ')[0])
    //             topResult += topping[i].value.split(' ')[0]
    //             topPrice += Number(topping[i].value.split(' ')[1])
    //         }
    //     }
    //     priceResult += topPrice + Number(size.value.split(' ')[1])

    //     orderChk.innerText = 
    //     `종류: ${order.value}, 사이즈: ${size.value.split(' ')[0]}, 도우: ${dough.value}, 토핑:${topResult}`
    //     // orderPrice.innerText = `총 금액: ${String(priceResult)}원`
    // }) 
    
    // // const size = document.querySelectorAll('[name=size]')
    
    // // const sizeValue = document.querySelectorAll('[name=size]')
    // // const sizePrice = sizeValue[0].value.split(' ')
    
    // const topping = document.querySelectorAll('.topping')
    // const toppingValue = topping[0].checked
    // const toppingPrice = topping[0].value.split(' ')
    // const orderChk = document.querySelector('#orderChk')
    
    // const pay = document.querySelector('#pay')
    // // console.log(topping[0].checked)
    // // console.log(size.value)
    // // console.log(toppingValue)
    // // console.log(toppingPrice)
    
    

    // pay.addEventListener('click', function(){
    //     const order = document.querySelector('#order')
    //     const size = document.querySelector('[name=size]:checked')
    //     const dough = document.querySelector('[name=dough]:checked')

    //     console.log(order.value)
    //     console.log(dough.value)
    //     // console.log(sizePrice[0])

    //     console.log(size.value)

    //     // for(let i=0; i<size.length; i++) {
    //     //     if(size[i].checked == true){
    //     //         console.log('사이즈', size[i].value.split(' ')[0])
    //     //         break;
    //     //     }
    //     // }

    //     // 주로 체크박스에서 사용
    //     for(let i=0; i<topping.length; i++) {
    //         if(topping[i].checked == true) {
    //             console.log('토핑', topping[i].value.split(' ')[0])
    //         }
    //     }
    // }) 

    
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
    // items.addEventListener('click', function(event){
    //     event.target.classList.add('true')
    //     // console.log(clsValue)

    //     if(event.target.classList.contains('true')) {

    //         event.target.style.fontWeight = 'bold'
    //         event.target.innerText = '✔' + event.target.innerText
    //     } 
 
    //     // event.target.classList.remove('true')
    //     // console.log(itemSet.classList.contains('true'))
    // })
    
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
        for(let j=0; j<chkBox.length; j++) {
            chkBox[j].addEventListener('click', function() {
                if(chkBox[j].checked == false) {
                    allChk.checked = false
                } 
                // for(let i=0; i<chkBox.length; i++) {
                //     if(chkBox[i].checked == false) {
                //         allChk.checked = false
                //     } 
                // }
            })
        }
        // 다 선택이 되었을 때 전체선택이 가능해지게 하려면,
        // 전체 배열을 가져와서 체크개수를 확인해보아야 함

        // const deleteChk = document.querySelector('.deleteChk')
        
        // deleteCol.addEventListener('click', function() {
        //     if(deleteChk.checked == true) {
        //         divAdd.remove()
        //     }
        // })

        // checkDel.addEventListener('click', function() {
        //     for(let i=0; i<10; i++) {
        //         let del = document.querySelector(`.col${divCnt}`)
        //         console.log(del)
        //     }
        // })

        
    })
    
    // const divDel = document.querySelector(`col${divCnt}`)
    // console.log(divDel)
    
})
