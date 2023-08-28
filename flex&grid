# **Flex&Grid**

웹 레이아웃의 종류

## Flex

단일 방향 레이아웃으로 수평(행)과 수직(열) 중 하나의 방향으로만 다룰 수 있음

1. disply 속성
- flex: 컨테이너의 속성을 수직으로 설정
- inline-block: 컨테이너의 속성을 수평으로 설정

<aside>
<img src="/icons/playback-play_brown.svg" alt="/icons/playback-play_brown.svg" width="40px" /> .container{
 display: flex;
}

</aside>

1. flex-direction(방향)
- row: 기본 설정, 플렉스 요소는 왼쪽에서 오른쪽으로, 위에서 아래로 배치
- row-reverse: 플렉스 요소를 반대방향으로 배치
- column: 수평의 쓰기 방식을 수직 방향으로 배치(위에서 아래)
- column-reverse: 수평의 쓰기 방식을 수직 방향으로 배치(아래에서 위)

<aside>
<img src="/icons/playback-play_brown.svg" alt="/icons/playback-play_brown.svg" width="40px" /> .container{
 display: flex;
 flex-direction: row;
}

</aside>

1. flex-wrap(줄바꿈)
- nowrap: 기본 설정, 플렉스 요소가 다음 줄로 넘어가지 않음(요소의 너비를 줄여 한 줄에 모두 배치)
- wrap: 플렉스의 요소가 여유공간이 없으면 다음 줄로 배치
- wrap-reverse: 위에서 아래방향으로 다음 줄로 배치

<aside>
<img src="/icons/playback-play_brown.svg" alt="/icons/playback-play_brown.svg" width="40px" /> .container{
 display: flex;
 flex-wrap: wrap;
}

</aside>

1. align-items(수직 방향 정렬)
- stretch: 기본 설정, 요소의 높이가 컨테이너의 높이와 같게 변경된 뒤에 연이어 배치
- flex-start : 컨테이너의 위쪽에 배치
- flex-end : 컨테이너의 아래쪽에 배치
- center :컨테이너의 가운데에 배치
- baseline : 컨테이너의 기준선(baseline)에 배치

<aside>
<img src="/icons/playback-play_brown.svg" alt="/icons/playback-play_brown.svg" width="40px" /> .container{
 display: flex;
 align-items: end;
}

</aside>

1. align-content(요소가 2줄 이상이며 flex-wrap 속성이 있을 경우에 설정 가능)
- stretch: 기본 설정, 플렉스 라인의 높이가 남는 공간을 전부 차지
- flex-start: 플렉스 라인이 왼쪽으로 뭉침
- flex-end: 플렉스 라인이 오른쪽으로 뭉침
- center: 플렉스 라인이 가운데로 뭉침
- space-between: 플렉스 라인이 일정한 간격을 두고 컨테이너에 고르게 분포
- space-around: 플렉스 라인이 일정한 간격을 갖고 양끝의 공간을 남기며 고르게 분포

<aside>
<img src="/icons/playback-play_brown.svg" alt="/icons/playback-play_brown.svg" width="40px" /> .container{
 display: flex;
 flex-wrap: wrap;
 align-content: center;
}

</aside>

1. justify-content(수평 방향 정렬)
- flex-start: 기본 설정, 요소는 앞쪽부터 배치
- flex-end: 뒤쪽부터 배치
- center: 가운데에서부터 배치
- space-between: 시작 요소는 시작점에 마지막 요소는 끝점에 정렬되고 나머지는 사이에 고르게 분포
- space around: 시작과 끝, 사이의 요소들 모두 여유공간을 두고 배치

<aside>
<img src="/icons/playback-play_brown.svg" alt="/icons/playback-play_brown.svg" width="40px" /> .container{
 display: flex;
 flex-wrap: wrap;
 justify-content: space-between;
}

</aside>

1. align-self(수직방향 정렬)
- align-items 보다 우선 적용되고 요소마다 서로 다른 align 속성 값을 설정할 수 있음

<aside>
<img src="/icons/playback-play_brown.svg" alt="/icons/playback-play_brown.svg" width="40px" /> .container{
  display: flex;
  flex-wrap:wrap;
 }
.red{
 align-self: flex-start;
}
.yellow{
 align-self: flex-end;
}

</aside>

## Grid

수평과 수직 동시에 축을 가지고 있는 레이아웃으로 영역을 2차원으로 다룰 수 있음

1. grid-template-columns/rows(열/행 크기 정의)

<aside>
<img src="/icons/playback-play_green.svg" alt="/icons/playback-play_green.svg" width="40px" /> .container {

 display: grid;

 grid-template-columns: 1fr;

 grid-template-rows: 2fr;

}

</aside>

fr(fractical unit)= 사용 가능한 공간에 대한 비율

1. justify-items(그리드 요소 수평 방향 정렬)
- normal: 기본 설정, stretch와 동일
- start: 시작점 기준 왼쪽에 배치
- center: 수평 가운데 배치
- end: 끝점 기준 오른쪽에 배치
- stretch: 컨테이너의 높이와 같게 변경 후 연이어 배치

<aside>
<img src="/icons/playback-play_green.svg" alt="/icons/playback-play_green.svg" width="40px" /> .container {

 display: grid;

 grid-template-columns: 1fr;

 grid-template-rows: 2fr;

 justify-items: center;

}

</aside>

1. align-items(수직 방향 정렬)

<aside>
<img src="/icons/playback-play_green.svg" alt="/icons/playback-play_green.svg" width="40px" /> .container {

 display: grid;

 grid-template-columns: 1fr;

 grid-template-rows: 2fr;

 justify-items: center;

 align-items: center;

}

</aside>

→ 가로 및 세로(2차원) 가운데 배치 됨

1. align-self(그리드 요소마다 서로 다른 align 속성값 설정 가능)

<aside>
<img src="/icons/playback-play_green.svg" alt="/icons/playback-play_green.svg" width="40px" /> .container {

 display: grid;

 grid-template-columns: 1fr;

 grid-template-rows: 2fr;

 justify-items:center;
}
.blue{

 align-self: start;

}

</aside>

1. justify-self(수평 방향 정렬)

<aside>
<img src="/icons/playback-play_green.svg" alt="/icons/playback-play_green.svg" width="40px" /> .container {

 display: grid;

 grid-template-columns: 1fr;

 grid-template-rows: 2fr;

 justify-items:center;
}
.blue{

 align-self: start;

 justify-self: end;

}

</aside>

1. justify-content(콘텐츠 열 사이 수평 방향 정렬)
- normal: 기본 설정, stretch와 동일
- start: 시작점 기준 왼쪽에 배치
- center: 수평 가운데 배치
- end: 끝점 기준 오른쪽에 배치
- space-around: 위, 아래, 요소들 사이 모두 여유 공간을 두고 배치
- space-between: 시작 요소는 시작점에, 마지막 요소는 끝점에 정렬되고 나머지는 사이에 고르게 배치
- space-evenly: 모든 여백이 고르게 배치
- stretch: 컨테이너의 높이와 같게 변경 후 연이어 배치

<aside>
<img src="/icons/playback-play_green.svg" alt="/icons/playback-play_green.svg" width="40px" /> .container {

  display: grid;

  grid-template-columns: 1fr 1fr;

  grid-template-rows: 150px 150px;

 align-content: space-between;

}

</aside>
