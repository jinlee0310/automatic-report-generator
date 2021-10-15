# automatic-report-generator

보고서 작성과 쿼리 생성을 위한 자동화 스크립트입니다.

## Prerequisites

- python3.6 이상 사용
- git 설치가 필요합니다.

- 깃과 파이썬이 뭔지 안다-><a href="https://github.com/hyojinLee-git/automatic-report-generator#how-to-use">여기</a>
- 깃과 파이썬이 뭔지 모른다-><a href="https://github.com/hyojinLee-git/automatic-report-generator#setting">여기</a>

## Setting

### Install python

이미지

### Install git

이미지

### Setting git

1. git bash를 열어줍니다.
2. 바탕화면에 폴더를 생성하고 아래와 같이 입력합니다. foldername은 사용자가 설정한 폴더 이름입니다.

```shell
cd/Desktop/foldername
```

3. git bash에 아래와 같이 입력합니다.(어려운 과정을 거치는 이유는 추후 파일 수정이 있을 수 있기 때문)

```shell
git init #.git 폴더 생성
git remote add origin https://github.com/hyojinLee-git/automatic-report-generator.git #원격 저장소 연결
git pull origin main #파일 다운로드
```

4. 정상적으로 완료되었다면 폴더에 automatic-report-generator가 설치되어 있습니다.

## How To Use?

### 쿼리 생성기

1. Querybox를 실행해 데이터를 확인합니다.
2. 명령프롬프트를 켭니다.(검색-cmd-enter)
3. automatic-report-generator폴더로 이동합니다.
   이미지
4. 쿼리 생성기를 실행해 값을 입력합니다.

   ```shell
   python query_generator.py #쿼리 생성기 실행
   ```

   파일 이름은 다운받은 데이터파일 제목입니다.<br>
   입력 형식은 <strong>컬럼 데이터타입</strong>입니다.(컬럼과 데이터타입 사이에 공백이 있어야 합니다.)<br>
   ex). C1 전화번호<br>

5. 입력이 끝났다면 ctrl+c를 누릅니다.
6. 폴더에 파일이름 SQL 쿼리.txt 파일이 생성됩니다.
7. 복사해서 Querybox에 붙여넣기 하시면 됩니다.

### 보고서 생성기

1. 보고서 생성기가 있는 폴더에 '파일이름\_SQL진단결과보고서.xlsx' 파일을 생성합니다.
2. 보고서 샘플에 있는 것처럼 컬럼목록을 만들어줍니다.
3. 파일을 닫습니다.
4. 명령프롬프트를 켭니다.(검색-cmd-enter)
5. automatic-report-generator폴더로 이동합니다.
   이미지
6. 보고서 생성기를 실행합니다.

```shell
pip install -r requirements
python report_generator.py #보고서 생성기 실행
```

7. 쿼리생성기와 마찬가지로 파일 이름과 <strong>컬럼 데이터타입</strong>을 입력합니다.

- 보고서 생성기를 실행하면 쿼리 생성기의 txt파일이 자동 생성됩니다.

8. 보고서 샘플 중 업무 규칙을 입력합니다.

## Run

```shell
pip install -r requirements
python query_generator.py #쿼리 생성기 실행
python report_generator.py #보고서 생성기 실행
```

## Error
