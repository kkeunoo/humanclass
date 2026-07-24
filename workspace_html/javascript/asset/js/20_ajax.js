window.addEventListener('load',bind)

// browser는 서버에 가서 Text를 받아와 해석, AJAX는 Text를 받아오는것 까지만
// 브라우저는 직접 사이트를 이동해야 하지만 AJAX는 값을 가져올 수 있음
function bind() {

    const btn1 = document.querySelector('#btn1')
    btn1.addEventListener('click', function() {

        // AJAX는 4단계로 구성되어 있음(url도 가능하고, 파일도 가능함)
        // 1_ajax 객체 생성 
        const xhr = new XMLHttpRequest()

        // 2_보낼 준비 방식(method), 주소(url)
        xhr.open('GET', 'https://jsonplaceholder.typicode.com/users')

        // 3_보내기
        xhr.send()

        // 4_결과 받기 및 활용, 갔다 오면~이기 때문에 콜백함수 이용
        xhr.onload = function() {
            console.log('다녀왔어')
            console.log( xhr.responseText )

            // 깜짝퀴즈, 두번째 사람의 이름을 출력하기 (Ervin)
            // 세번째 사람의 lat(좌표)를 출력하기
            const xhrData = JSON.parse(xhr.responseText)
            console.log(xhrData)
            // 첫번째 방법
            console.log(xhrData[1]['name'])
            console.log(xhrData[2]['address']['geo']['lat'])
            // 두번째 방법
            console.log(xhrData[1].name)
            console.log(xhrData[2].address.geo.lat)
        
        }

    })

    const btn2 = document.querySelector('#btn2')
    btn2.addEventListener('click', function() {

        const xhr = new XMLHttpRequest()
    
        // 상대주소로 하지 않아도 갔다 오는 이유는, html에서 자바스크립트를
        // 연결했기 때문에 head영역 자바스크립트 안에 들어갔기 때문에
        // 20_ajax.html의 폴더 경로와 동일함 (주소경로를 참고한다는 말이 더 정확)
        xhr.open('GET', '19_json.html')
        xhr.send()
        
        xhr.onload = function() {
            console.log( xhr.responseText )
        }

        // 아래에 들어가있어도, 비동기기 때문에 값을 받지 않고 로그상 위에 먼저 나오게 됨
        console.log( '['+ xhr.responseText +']' )
        
    })

    const btn3 = document.querySelector('#btn3')
    btn3.addEventListener('click', function() {

        const now = new Date()
        // const today = new Date().toISOString().split('T')[0].split('-').join('')
        const today = now.toISOString().split('T')[0].replace(/-/g,'')
        let hour = now.getHours() - 1
        if(hour < 10) {
            hour = '0' + hour + '00'
        } else {
            hour = hour + '00'
        }

        // 기상청 날씨예보 받아오기
        const key = ''
        
        let url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtFcst'
        url += '?'
        url += 'serviceKey='+key
        url += '&numOfRows=1000'
        url += '&pageNo=1'
        url += '&dataType=JSON'
        url += '&base_date='+today
        url += '&base_time='+hour
        url += '&nx=63'
        url += '&ny=110'
        
        const xhr = new XMLHttpRequest()
    
        xhr.open('GET', url)
        xhr.send()
        xhr.onload = function() {
            console.log( xhr.responseText )

            const data = JSON.parse(xhr.responseText)
            console.log(data)

            // response - body - items - item
            // category: LGT - 번개, fcstValue: 0 - 확률, fcstTime: 1600 - 시간(16시)
            // category: T1H(기온), RN1(강수량), REH(습도)
            console.log(data.response.body.items.item[0].category)
            console.log(data.response.body.items.item[0].fcstValue)
            console.log(data.response.body.items.item[0].fcstTime)

            let item = data.response.body.items.item
            // for(let i=0;item.length;i++){
            //     if(item[i].category == 'T1H') {
            //         console.log(item[i])
            //     } else if(item[i].category == 'RN1'){
            //         console.log(item[i])
            //     } else if(item[i].category == 'REH') {
            //         console.log(item[i])
            //     }
            // }

            // for문을 사용해도 되지만, filter를 사용해도 좋음.
            // let filtered = item.filter(function(data) {
            //     if(data.category == 'T1H' 
            //     || data.category == 'RN1'
            //     || data.category == 'REH') {
            //         return true
            //     }
            // })
            // console.log(filtered)

            // 테이블로 표시
            // 1. 예측카테고리 | 예측시간 | 값
            const output = document.querySelector('#output')

            let cateFilter = item.filter(function(data) {
                if(data.category == 'T1H'
                || data.category == 'RN1'
                || data.category == 'REH') {
                    return true
                }
            })
            // console.log(cateFilter[9].fcstTime)

            output.innerHTML = ''

            const titleDiv1 = document.createElement('div')
            titleDiv1.innerText = '예측카테고리'
            titleDiv1.classList.add('column')
            output.append(titleDiv1)
            const titleDiv2 = document.createElement('div')
            titleDiv2.innerText = '예측시간'
            titleDiv2.classList.add('column')
            output.append(titleDiv2)
            const titleDiv3 = document.createElement('div')
            titleDiv3.innerText = '값'
            titleDiv3.classList.add('column')
            output.append(titleDiv3)
            
            for(let j=0; j<cateFilter.length; j++) {
                const addDiv = document.createElement('div')
                addDiv.classList.add('filterLine')
                output.append(addDiv)

                const cateDiv = document.createElement('div')
                cateDiv.classList.add('category')
                cateDiv.classList.add('column')
                addDiv.append(cateDiv)
                cateDiv.innerText = cateFilter[j].category

                const timeDiv = document.createElement('div')
                timeDiv.classList.add('time')
                timeDiv.classList.add('column')
                addDiv.append(timeDiv)
                timeDiv.innerText = cateFilter[j].fcstTime

                const valueDiv = document.createElement('div')
                valueDiv.classList.add('value')
                valueDiv.classList.add('column')
                addDiv.append(valueDiv)
                valueDiv.innerText = cateFilter[j].fcstValue
            }


            // 2. 시간(fcstTime) | 온도(T1H) | 습도(REH) | 강수량(RN1) (시간에 맞게 출력)
            const output_time = document.querySelector('#output_time')

            let timeFilter = item.filter(function(data) {
                if(data.category == 'T1H'
                || data.category == 'RN1'
                || data.category == 'REH') {
                    return true
                }
            })
            console.log(timeFilter)

            output_time.innerHTML = ''

            const timeDiv1 = document.createElement('div')
            timeDiv1.innerText = '시간\n(fcstTime)'
            timeDiv1.classList.add('column2')
            output_time.append(timeDiv1)
            const timeDiv2 = document.createElement('div')
            timeDiv2.innerText = '온도\n(T1H)'
            timeDiv2.classList.add('column2')
            output_time.append(timeDiv2)
            const timeDiv3 = document.createElement('div')
            timeDiv3.innerText = '습도\n(REH)'
            timeDiv3.classList.add('column2')
            output_time.append(timeDiv3)
            const timeDiv4 = document.createElement('div')
            timeDiv4.innerText = '강수량\n(RN1)'
            timeDiv4.classList.add('column2')
            output_time.append(timeDiv4)

            // let jsonT = {
            //     "T1H" : "",
            //     "REH" : "",
            //     "RN1" : ""
            // }
            
            for(let j=0; j<timeFilter.length; j++) {
                const addDiv = document.createElement('div')
                addDiv.classList.add('filterLine')
                output_time.append(addDiv)
                
                const fcstDiv = document.createElement('div')
                fcstDiv.classList.add('fcstTime')
                fcstDiv.classList.add('column')
                addDiv.append(fcstDiv)
                if(timeFilter[j].category == 'T1H') {
                    fcstDiv.innerText = timeFilter[j].fcstTime
                }
         
                const t1hDiv = document.createElement('div')
                t1hDiv.classList.add('T1H')
                t1hDiv.classList.add('column')
                addDiv.append(t1hDiv)
                if(timeFilter[j].category == 'T1H' ||
                    timeFilter[j].category == 'REH') {
                    t1hDiv.innerText = timeFilter[j].fcstValue
                    // jsonT.T1H += timeFilter[j].fcstValue
                }
                
                const rehDiv = document.createElement('div')
                rehDiv.classList.add('REH')
                rehDiv.classList.add('column')
                addDiv.append(rehDiv)
                if(timeFilter[j].category == 'T1H') {
                    rehDiv.innerText = timeFilter[j].fcstValue
                    // jsonT.REH += timeFilter[j].fcstValue
                }
                
                const rn1Div = document.createElement('div')
                rn1Div.classList.add('RN1')
                rn1Div.classList.add('column')
                addDiv.append(rn1Div)
                if(timeFilter[j].category == 'T1H') {
                    rn1Div.innerText = timeFilter[j].fcstValue
                    // jsonT.RN1 += timeFilter[j].fcstValue
                }
                
                // if(timeFilter[j].fcstTime) {
                //     if(timeFilter[j].category == 'T1H'
                //     || timeFilter[j].category == 'REH'
                //     || timeFilter[j].category == 'RN1') {
                //         t1hDiv.innerText = timeFilter[j].fcstValue
                //         rehDiv.innerText = timeFilter[j].fcstValue
                //         rn1Div.innerText = timeFilter[j].fcstValue
                //     } 
                // }

                // 값 받아올 땐 string!
            }
            // console.log(jsonT)

        }
    })
    
    // btn4 클릭하면 제이슨 연습용주소에서 받은 정보 중
    // id, name, zipcode, 회사이름(company)

    const btn4 = document.querySelector('#btn4')
    btn4.addEventListener('click', function() {

        const Q3_xhr = new XMLHttpRequest()

        Q3_xhr.open('GET', 'https://jsonplaceholder.typicode.com/users')
        Q3_xhr.send()
        Q3_xhr.onload = function () {
            console.log(Q3_xhr.responseText)

            const Q3_xhrData = JSON.parse(Q3_xhr.responseText)
            console.log(Q3_xhrData)

            const q3 = document.querySelector('#q3')

            for(let i=0; i<Q3_xhrData.length; i++) {
                // console.log(Q3_xhrData[i].id)
                // console.log(Q3_xhrData[i].name)
                // console.log(Q3_xhrData[i].address.zipcode)
                // console.log(Q3_xhrData[i].company.name)

                let Q3_tr = document.createElement('tr')
                q3.append(Q3_tr)
    
                q3.innerHTML += `
                    <td>${Q3_xhrData[i].id}</td>
                    <td>${Q3_xhrData[i].name}</td>
                    <td>${Q3_xhrData[i].address.zipcode}</td>
                    <td>${Q3_xhrData[i].company.name}</td>
                `
            }
        }
    })

    const btn5 = document.querySelector('#btn5')
    btn5.addEventListener('click', function() {

        let a = undefined
        // try를 실행하고 오류가 나면 catch로 넘어감
        // catch는 전달인자가 있음
        // javascipt는 하나 오류나면 안 넘어가기 때문에, try catch로 잡음
        // 잡게되면 오류 다음에 있는 것은 실행이 됨
        try {
            a.push(1)
        }catch( e ){
            // console.log로 확인해봐야 err메세지를 확인할 수 있음
            console.log(e)
        }

        const url = 'https://jsonplaceholder.typicode.com/users'
        
        // 원래 방식
        // // 1_ajax 객체 생성 
        // const xhr = new XMLHttpRequest()
        // // 2_보낼 준비 방식(method), 주소(url)
        // xhr.open('GET', 'https://jsonplaceholder.typicode.com/users')
        // // 3_보내기
        // xhr.send()
        // // 4_결과 받기 및 활용, 갔다 오면~이기 때문에 콜백함수 이용
        // xhr.onload = function() {
        //     console.log('다녀왔어')
        //     console.log( xhr.responseText )
        // }

        // fetch(주소, 옵션json), 3번까지가 한 번에 끝남
        // ~하면(then), fetch의 get이 다 끝나면
        fetch(url, {
            method: 'GET'
            // then은 앞에 있는것이 동작 끝나면 진행 됨
        }).then(function(response) {
            console.log(response)
            // 아래는 JSON.parse(a.responseText) 역할 
            return response.json()
        }).then(function (data) {
            console.log(data)
        }).catch(function (error) {
            console.error( error )
        })
    })


    const btn6 = document.querySelector('#btn6')
    btn6.addEventListener('click', function() {
        debugger

        console.log('btn6 클릭')
        debug()
        console.log('끝')
    })
}

function debug() {
    let a = 1

    console.log(a)
}