# 이 게임의 목적
- https://www.factorio.com +(<-플러스 기호임) https://store.steampowered.com/app/1621690/Core_Keeper 같이 마법 + 공장 자동화 + 모험인 게임 만들기

# 그래서 지금 할거
1. GameObject 만들기-완료 체크(v)
  - 이거는 코드 확인
2. block class 만들기 (<-이상곤이 해야하는거)
  - GameObject를 상속하기-완료 체크(v)
  - images변수 만들어서 거기에 이미지 이름을 넣고 로드해서 사용하기-완료 체크()
  - status = {}<-other property
  - frame 함수 비워두기
  - get_current_image 함수로 혀네 이미지 가져오기
3. cam class 완성하기(줌기능 완성, <-내가 할꺼)
  - zoom구현-완료 체크()
  - 카메라 위치 따라서 이미지 이동-완료 체크(v)
4. entity class 만들기(<-누가 할지 못정함)

# 코딩한때 지키지 않으면 생명을 보장할수 없는것(들)
1. 이미지 로드
```load_function.py
  #load_function.py에 써야하는 코드
  load():
    #이미 있는 코드
    imageManager.imagemanager.preload_general_image("asset/에 있는 이미지 이름", "코딩할때 쓸 이미지 이름")
    #예시
    imageManager.imagemanager.preload_general_image("player.png", "player")
    imageManager.imagemanager.preload_general_image("jio_is_genius.png", "very_good_image")
```
```python
  #이미지를 로드할 코드 파일
  import imageManager
   
  # 다른 코드...
  
  #이미지를 로드할 곳

  image=imageManager.load("이미지 이름")
  #여기서 로드된 이미지를 지역변수(생성되었다가 곧 사라지는 변수) 에 저장 하기!!!!
  #예시
  jiogenius = imageManager.imagemanager.load("very_good_image")
   
```
