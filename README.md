# ES_Object_Detection

### 초기설정

git init : git의 관리하에 들어감

git config --global user.name "EuiseokJeong"

git config --global user.email "dmltjr4621@gmail.com"


### 현재시점 저장

git status : 아직 저장되지 않은 것 볼 수 있음

git add -A : 모든 것 캡슐에 담음

git commit -m "commit에 대한 설명"


### 과거로 돌아가기

git log : 수정 시점 확인

git reset OOOOOO --hard : git log로 나온 시점의 일련번호 앞 여섯자리 복사하여 돌아감. 이후의 것을 남겨두지 않고 돌아감.

git revert OOOOOO : 이전 단계의 일련번호 입력하여 전 단계로 이동


### 브랜치

git branch (새로 생성할 브랜치 이름) : 새로운 브랜치 생성

git branch : 현재 브랜치 확인

git checkout (이동할 브랜치 이름) : 브랜치로 넘어감

git checkout master : 마스터로 넘어감

git branch -D (삭제할 브랜치 이름)


### merge

git checkout master로 마스터 브랜치로 이동

git merge (마스

Rebase터와 merge할 브랜치 이름)

*마스터와 브랜치가 같은 파일, 같은 라인을 수정하면 충돌 일어남.


### pull

git pull origin master 

### push 
git push origin master
