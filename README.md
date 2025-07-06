# 이 게임의 목적
- https://www.factorio.com +(<-플러스 기호임) https://store.steampowered.com/app/1621690/Core_Keeper 같이 마법 + 공장 자동화 + 모험인 게임 만들기

# 그래서 지금 할거
1. block class 만들기 (<-이상곤이 해야하는거)
2. cam class 완성하기(줌기능 완성, <-내가 할꺼)
3. entity class 만들기(<-누가 할지 못정함)

# 코딩한때 지키지 않으면 생명을 보장할수 없는것(들)
1. 이미지 로드
```load_function.py
  #load_function.py에 써야하는 코드
  load():
    #이미 있는 코드
    
```
```python
  #이미지를 로드할 코드 파일
  import imageManager
   
  # 다른 코드...
  
  #이미지를 로드할 곳

  image=imageManager.load("이미지 이름")
  #여기서 로드된 이미지를 지역변수(생성되었다가 곧 사라지는 변수) 에 저장 하기!!!!
   
```
