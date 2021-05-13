// class="bar" 인 요소 모두 탐색
var bars = document.querySelectorAll('.bar')
// console.log(bars)
// console.log(bars[0].getAttribute('value'))

// 전체 수 구하기 : 확진환자 = 완치 + 치료중 + 사망, 따라서 확진환자를 전체로 보고 나머지는 비율로
var total = parseInt(bars[0].getAttribute('value'))
// console.log(total)

// width 지정하기
for (let index = 0; index < bars.length; index++){
    console.log(100*parseInt(bars[index].getAttribute('value'))/total);
    bars[index].style.width = String(100*parseInt(bars[index].getAttribute('value'))/total)+'%';
}