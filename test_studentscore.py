'''
학생성적 관리 예제 구현
1. 필수 기능 : 새로운 성적 입력, 입력 성적 수정, 입력 성적 삭제, 입력된 성적 검색
'''

# 1. 사전 변수 선언 : 키, 값 설정
student_dict={1:40, 2:70, 3:90}

# 2. while 반복문 사용해 무한 반복문 구조 만들기
# while 조건식에서 사용할 변수 선언 + 초기화 : condition = True
condition = True
while(condition == True):
    print("1. 성적 입력 2. 성적 수정 3. 성적 삭제 4. 성적 검색 5. 종료")
    menu_no = int(input("번호 입력(1~5):"))
    if (menu_no == 1):
          print("1. 성적 입력을 선택")
          input_kor=int(input("국어점수입력"))
          max_student_no=max(student_dict.keys())
          max_student_no += 1
          print("새 학생 번호", max_student_no)
          student_dict[max_student_no]=input_kor
          print("새 학생 번호와 국어 점수 저장")

    elif(menu_no ==2):
          print("2. 성적 수정을 선택")
          print("입력된 학생 성적 수정")
          input_int=int(input("수정할 학생 번호 입력:"))
          if(input_int in student_dict):
              print("수정할 학생 번호 찾음")
              input_kor=int(input("수정할 국어 점수 입력:"))
              student_dict[input_kor]=input_kor
              print("수정끝")
          else:
              print("수정할 학생 번호 찾지 못함")

    elif(menu_no ==3):
          print("3. 성적 삭제를 선택")
          print("입력된 학생 성적 삭제")
          input_no=int(input("학생번호 입력"))
          if(input_no in student_dict):
              student_dict.pop(input_no)
              print("학생 성적 삭제")
          else:
              print("학생 번호 찾지 못함")

    elif(menu_no ==4):
          print("4. 성적 검색을 선택")
          print("입력된 학생 성적 검색")
          input_no=int(input("학생 번호 입력:"))
          if(input_no in student_dict):
              print("학생성적 찾음. 국어점수:", student_dict[input_no])
          else:
             print("학생 번호 찾지 못함")

    elif(menu_no ==5):
          print("5.종료를 선택")
          break

    else:
          print("메뉴에 없는 번호 입력")
          continue
