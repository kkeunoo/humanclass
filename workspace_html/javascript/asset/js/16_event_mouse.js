// 전역변수는 언더바처럼 따로 지정해주어도 좋음
let _isDrag = false
let _offsetX = 0
let _offsetY = 0

function log(message) {
    const div = document.createElement('div')
    div.classList.add('log')
    div.innerHTML = message
    const view = document.querySelector('#view')
    view.prepend(div)
}

// onload 구역을 만들어서 안에 실행 할 함수를 넣어두면 용이함
window.onload = function() {
    bind()
}

function bind() {

    // 우클릭 하는 메뉴를 컨텍스트 메뉴라고 함
    const area = document.querySelector('#area')
    // contextmenu를 false로 주게되면 해당 영역은 우클릭 메뉴를 사용할 수 없음
    area.oncontextmenu = () => {
        alert('오른쪽 버튼 금지입니다')
        return false;
    }

    // selectstart로 해당 영역 드래그를 막을 수 있음
    area.onselectstart = function() {
        return false;
    }

    const area2 = document.querySelector('#area2')
    // oncopy는 ctrl+c 등 복사할 때 발생하는 이벤트 (클립보드에 저장되는 것)
    area2.addEventListener('copy', function(event) {
        // preventDefault는 ctrl+c 등이 하는 기본을 막아주는 것
        event.preventDefault()
        
        // selection은 드래그를 했을 때 영역을 알려줌
        const selection = window.getSelection().toString()
        console.log(selection)
        if(selection.length == 0) {
            return
        }

        // 아래처럼 clipboard 영역에 str로 추가해주면, 출처가 붙어서 나옴
        const str = '[출처] www.naver.com'
        const result = selection + str

        // plain은 텍스트에 순수한 글씨, 거기에 result를 추가
        event.clipboardData.setData('text/plain', result)
    })

    // 아래 실행함수들의 경우 해당 영역 내에서 눌렀을때만 작동함
    area2.addEventListener('dblclick', function() {
        // 0.3초 이내에 클릭이 두 번 발생했을 때 dblclick으로 알 수 있음
        log('더블클릭발생')
    })

    area2.addEventListener('mousedown', function() {
        // mouse가 눌렸을 때 확인 할 수 있음
        log('mousedown')
    })

    area2.addEventListener('mouseup', function() {
        // mouse가 올라왔을 때 확인 할 수 있음
        log('mouseup')
    })

    area2.addEventListener('click', function(evt) {
        // mouse가 클릭되었을 때 때 확인 할 수 있음
        log('click')

        // evt전달인자가 하나기 때문에 , 대신 + 를 사용함
        // offsetY는 돔 0,0(좌상단) 기준으로 마우스가 어디서 클릭이 되었는지 나옴 (상대값)
        // 만약, 돔 위치가 이동하더라도 돔 안에서의 0,0이 적용
        log('offsetY : '+ evt.offsetY)
        // pageY의 경우 스크롤 관계 없이 문서 에서 0,0(좌상단) 기준 (절대값)
        log('pageY : '+ evt.pageY)
        // 서버에 접속할 수 있는 도구(client)의 0,0 기준
        // client는 page와 다르게 지금 보고있는 브라우저의 좌상단 기준
        log('clientY : '+ evt.clientY)
        // screen은 내가 보고 있는 화면(실제 모니터 참고) 좌상단 기준
        log('screenY : '+ evt.screenY)
    })

    // mouseenter와 mouseover 동일한 기능, 마우스가 올라오면
    // area2.addEventListener('mouseenter', function(evt) {
    area2.addEventListener('mouseover', function(evt) {
        log('moseover')
        area2.style.backgroundColor = 'yellow'
    })

    // area2.addEventListener('mouseleave', function(evt) {
    area2.addEventListener('mouseout', function(evt) {
        log('mouseout')
        area2.style.backgroundColor = 'white'
    })

    area2.addEventListener('mousemove', function(evt) {
        log('mousemove')
        log(`offsetX : ${evt.offsetX}, offsetY : ${evt.offsetY}`)
    })

    document.querySelector('body').addEventListener('mousemove', function(evt) {
        const game = document.querySelector('#game')

        // 마우스 좌상단에 붙여놓았기 때문에, 1px정도 떨어뜨려놓아야 클릭이 됨
        // 그렇지 않고 붙여놓았을 때는 그림이 클릭하게 되는 효과이기 때문
        game.style.top = evt.pageY + 10 + 'px'
        game.style.left = evt.pageX + 10 + 'px'

        // log(`offsetX : ${evt.offsetX}, offsetY : ${evt.offsetY}`)
    })

    // drag and drop 만들기
    document.querySelector('#img').addEventListener('mousedown', function(evt) {
        _isDrag = true
        // 눌렀을 때 X, Y값을 저장해두어야 하기 때문에 전역변수를 선언해서 저장
        _offsetX = evt.offsetX
        _offsetY = evt.offsetY
    })
    document.querySelector('#img').addEventListener('mouseup', function(evt) {
        // 마우스를 뗀다면 drag 하고있는것을 중단하기 위해 false로 변환
        _isDrag = false
    })

    document.querySelector('body').addEventListener('mousemove', function(evt) {
        const img = document.querySelector('#img')

        if(_isDrag) {
            img.style.top = (evt.pageY - _offsetY) + 'px'
            img.style.left = (evt.pageX - _offsetX) + 'px'
        }
    })

    window.addEventListener('resize', function(evt) {
        // 아래와 같이 입력하면, w와 h에 브라우저 안쪽 width, height를 알 수 있음
        // 단, 스크롤 영역을 제외한 부분이기 때문에 그 부분까지면 아우터를 써야 함
        const w = window.innerWidth
        const h = window.innerHeight

        log(`화면w:${w}, 높이h:${h}`)
    })

}