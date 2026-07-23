console.log('hello js')

// 현재 값이 null인 경우는, html파일을 보았을 때 head를 읽고 body에 btn1이 있으니
// 읽어오지 못 해 로딩이 끝난 뒤에 불러오거나 해야 함
const btn1 = document.querySelector('#btn1')
console.log(1, 'btn1', btn1)

console.log(window)

// 페이지 로딩 이벤트가 발생하면~ 실행해라
// 페이지 로딩이 언제 끝날 지 모르기 때문에 비동기 callback
// window.onload = function() {
//     const btn1 = document.querySelector('#btn1')
//     console.log(2, 'btn1', btn1)
// }

function init() {
    const btn1 = document.querySelector('#btn1')
    console.log(2, 'btn1', btn1)

    const game = document.querySelector('#game')
    game.style.left = '10px'
    game.style.top = '20px'

    bind()
}

// 이렇게 js에 주지 않아도 body에도 쓸 수 있음, 단 변수기때문에 한 번만 적용
window.onload = init

// on을 붙여 바로 적용하거나, 아래와 같이 이벤트를 추가할 수 있음
// onload와 다르게 여러 번 적용할 수 있으나, 현재 예시는 함수가 같아 중복실행 안 됨
// window.addEventListener('load', init)
// window.addEventListener('load', init)
// window.addEventListener('load', init)

// bind는 event들을 묶어 놓기 위해 함수로 실무에서 주로 사용 함
function bind(){
    const btn1 = document.querySelector('#btn1')
    // 아래처럼 동일한 2개의 함수를 주어도, 변수이기 때문에 덮어씌워짐
    btn1.onclick = function() {
        console.log('btn1 클릭')
    }
    btn1.onclick = function() {
        console.log('btn1 click')
    }

    const btn2 = document.querySelector('#btn2')
    // onclick function에 담은 것과 다르게, 동일한 이벤트에 여러 함수 추가 할 수 있음
    btn2.addEventListener('click', function() {
        console.log('btn2 클릭')
    })
    btn2.addEventListener('click', function() {
        console.log('btn2 click')
    })

    const btn4 = document.querySelector('#btn4')
    // btn4click() 으로 하면 실행이 되어버리는데, 실행이 되었을 때
    // 아래 btn4click 지역에 return이 없으므로 btn4click()가 'undefined'가 됨
    // 익명함수는 쓸 수 있지만 함수 자체를 넣으면 실행이 됨
    // remove는 event를 제거해주지만, 익명함수는 쉽게 제거할 수 없음
    btn4.addEventListener('click', btn4click)
    btn4.removeEventListener('click', btn4click)

    // 
    const login = document.querySelector('#login')
    login.addEventListener('click', function() {
        const id = document.querySelector('#id')
        const pw = document.querySelector('#pw')
        const warning = document.querySelector('.warning')

        console.log('ID:',id.value)
        console.log('PW:',pw.value)
        
        // == ''은 스페이스바도 포함되기 때문에, trim으로 공백 제거 후 검사
        // trim으로 연습한 뒤 else if, else로 추가 연습*
        // if(id.value.trim() == '') {
        //     console.log('아이디는 필수입니다.')
        //     warning.innerText = '아이디는 필수입니다.'
        // } else if(pw.value.trim() == '') {
        //     console.log('비밀번호는 필수입니다.')
        //     warning.innerText = '비밀번호는 필수입니다.'
        // } else {
        //     warning.innerText = ''
        // }

        if(id.value.trim() == '') {
            console.log('아이디는 필수입니다.')
            warning.innerText = '아이디는 필수입니다.'

            // <!-- <div class="log">글씨 출력</div> -->
            // const div = document.createElement('div')
            // div.classList.add('log')
            // div.innerHTML = '아이디는 필수입니다.'
            // const view = document.querySelector('#view')
            // view.prepend(div)

            log('아이디는 필수입니다.')
        } else if(pw.value.trim() == '') {
            console.log('아이디는 필수입니다.')
            warning.innerText = '아이디는 필수입니다.'

            log('비밀번호는 필수입니다.')
        } 
    })

    // key를 눌렀을 경우 발생하는 이벤트
    document.querySelector('#id').addEventListener('keydown', function() {
        // log('keydown 발생')
    })
    // pw중복검사 등 할 때 쓴 값이 올라왔을 때 중복이 있는지 등 체크하는 방식에도 쓰임
    document.querySelector('#id').addEventListener('keyup', function(event) {
        // log('keyup 발생')
        // 인자값을 주면 어떤 키를 눌렀는지 받아올 수 있음 (keys 또는 keycode_ASCI코드)
        // keycode는 키패드에 있는 값과 다름, 다만 엔터는 같은 신호가 들어옴
        // console.log(event)
        // log('key:' + event.key)
        log('keyCode:' + event.keyCode)

        // log('shiftKey:' + event.shiftKey)
        // log('ctrlKey:' + event.ctrlKey)
        // log('altKey:' + event.altKey)

        // id에서 enter를 했을 때 pw창으로 focus가 가도록 지정
        if(event.keyCode == 13) { // enter keyCode
            log('엔터 빵')
            const pw = document.querySelector('#pw')
            pw.focus()
        }

        if(event.ctrlKey && event.keyCode == 67) {// ctrl + c 복사방지
            alert('ctrl+c')
        }
    })

    document.querySelector('#pw').addEventListener('keyup', function(event) {
        if(event.keyCode == 13) {
            const login = document.querySelector('#login')
            // pw에서 enter를 칠 경우 login 버튼이 click되도록 설정
            login.click()
        }
    })

    document.querySelector('#top').addEventListener('click', function(event) {
        // 현재 스크롤의 위치를 알 수 있는 document 커맨드
        // 스크롤바의 길이는 전체 길이에서 그만큼만 보고있다는 뜻
        console.log(document.documentElement.scrollTop)
        // document.documentElement.scrollTop = 0

        // window.scrollTo는 smooth 외에도 여러가지가 있음, 나중에 배울 제이슨?이라는 것
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        })
    })

    // window 자체에서 scroll이 움직일 때 마다 Y값을 알 수 있음
    // 스크롤이 더 없다가 내렸을 때 추가적으로 화면을 로딩하는 등 그때 사용해도 좋음
    window.addEventListener('scroll', function() {
        console.log('window.scrollY', window.scrollY)
    })

    document.querySelector('body').addEventListener('keydown', function(event) {
        // log(event.keyCode)
        const game = document.querySelector('#game')
        
        // const left = parseInt(game.style.top)
        // console.log(top)

        // style로 값을 바꿀 땐 항상 설정한 값만 가져올 수 있기 때문에
        // js에서 init에 한 번 더 선언한 뒤에 가져옴
        if(event.keyCode == 39) { // 오른쪽 키를 눌렀을 때 이미지가 10px 이동하도록 변경
            game.style.left = parseInt(game.style.left) + 10 + 'px'
        } else if(event.keyCode == 37) { // 왼쪽방향키
            game.style.left = parseInt(game.style.left) - 10 + 'px'
        } else if(event.keyCode == 40) { // 아랫방향키
            game.style.top = parseInt(game.style.top) + 10 + 'px'
        } else if(event.keyCode == 38) { // 윗방향키
            game.style.top = parseInt(game.style.top) - 10 + 'px'
        } 
    })

}

// 아래처럼 body영역의 attribute에 바로 onclick으로 줄 수도 있다
function btn3click() {
    console.log('btn3 click')
} 

function btn4click() {
    console.log('btn4 click')
} 

function log(message) {
    // <!-- <div class="log">글씨 출력</div> -->
    const div = document.createElement('div')
    div.classList.add('log')
    div.innerHTML = message
    const view = document.querySelector('#view')
    view.prepend(div)
}





