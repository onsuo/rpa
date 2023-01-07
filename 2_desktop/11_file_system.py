import datetime
import fnmatch
import os
import shutil

# 파일 기본
print(os.getcwd())  # current working directory 현재 작업 공간
os.chdir("02_desktop")  # 02_desktop 으로 작업 공간 이동
print(os.getcwd())
os.chdir("..")  # 부모 폴더로 이동
print(os.getcwd())
os.chdir("../..")  # 조부모 폴더로 이동
print(os.getcwd())
os.chdir("C:/")  # 주어진 절대 경로로 이동
print(os.getcwd())


# 파일 경로 만들기
file_path = os.path.join(os.getcwd(), "my_file.txt")  # 절대 경로 생성
# print(file_path)


# 파일 경로에서 폴더 정보 가져오기
print(os.path.dirname(r"C:\Dev\rpa\02_desktop\my_file.txt"))


# 파일 정보 가져오기

# 파일의 생성 날짜
file_path = "02_desktop/10_log.py"
ctime = os.path.getctime(file_path)
print(ctime)
# 날짜 정보를 strftime 을 통해서 연월일 시분초 형태로 출력
print(datetime.datetime.fromtimestamp(ctime).strftime("%Y/%m/%d %H:%M:%S"))

# # 파일의 수정 날짜
mtime = os.path.getmtime(file_path)
print(datetime.datetime.fromtimestamp(mtime).strftime("%Y/%m/%d %H:%M:%S"))

# # 파일의 마지막 접근 날짜
atime = os.path.getatime(file_path)
print(datetime.datetime.fromtimestamp(mtime).strftime("%Y/%m/%d %H:%M:%S"))

# # 파일 크기
size = os.path.getsize(file_path)
print(size)  # 바이트 단위로 파일 크기 가져오기


# 파일 목록 가져오기
print(os.listdir())  # 모든 폴더, 파일 목록 가져오기
print(os.listdir("02_desktop"))  # 주어진 폴더 밑에서 모든 폴더, 파일 목록 가져오기

# 파일 목록 가져오기 (하위 폴더 모두 포함)
result = os.walk(".")  # 주어진 폴더 밑에 있는 모든 폴더, 파일 목록 가져오기
print(result)

for root, dirs, files in result:
    print(root, dirs, files)

# 만약 폴더 내에서 특정 파일들을 찾으려면?
name = "11_file_system.py"
result = []
for root, dirs, files in os.walk("."):
    # [a.txt, b.txt, c.txt, 11_file_system.py, ...]
    if name in files:
        result.append(os.path.join(root, name))
print(result)

# 만약 폴더 내에서 특정 패턴을 가진 파일들을 찾으려면?
# *.xlsx, *.txt, 자동화*.png
pattern = "*.py"  # .py 로 끝나는 모든 파일
result = []
for root, dirs, files in os.walk("."):
    # [a.txt, b.txt, c.txt, 11_file_system.py, ...]
    for name in files:
        if fnmatch.fnmatch(name, pattern):  # 이름과 패턴이 일치하면
            result.append(name)
print(result)


# 주어진 경로가 파일인지 폴더인지
print(os.path.isdir("02_desktop"))  # 02_desktop 은 폴더인가? True
print(os.path.isfile("02_desktop"))  # 02_desktop 은 파일인가? False

print(os.path.isdir("img.png"))  # img.png 은 폴더인가? False
print(os.path.isfile("img.png"))  # img.png 은 파일인가? True

# 만약에 지정된 경로에 해당하는 파일 / 폴더가 없다면?
print(os.path.isfile("imggg.png"))

# 주어진 경로가 존재하는지?
if os.path.exists("02_desktop"):
    print("파일 또는 폴더가 존재합니다.")
else:
    print("존재하지 않습니다.")


# 파일 만들기
open("new_file.txt", "a", encoding="utf8").close()  # 빈 파일 생성


# 폴더 만들기
os.mkdir("new_folder")
os.mkdir("new_folders/a/b/c")  # 실패: 하위 폴더를 가지는 폴더 생성 시도
os.makedirs("new_folders/a/b/c")  # 성공: 하위 폴더를 가지는 폴더 생성


# 파일명 / 폴더명 변경하기
os.rename("new_file.txt", "new_file_rename.txt")  # new_file.txt -> new_file_rename.txt 로 이름 변경
os.rename("new_folder", "new_folder_rename")


# 파일 삭제하기
os.remove("new_file_rename.txt")


# 폴더 지우기
os.rmdir("new_folder_rename")  # 폴더 안이 비었을 때만 삭제 가능
shutil.rmtree("new_folders")  # 폴더 안이 비어있지 않아도 완전 삭제 가능
# 모든 파일이 삭제될 수 있으므로 주의!!!


# 파일 복사하기
# 어떤 파일을 폴더 안으로 복사하기
shutil.copy("run_btn.png", "test_folder")  # 원본 파일 경로, 대상 폴더 경로
# 어떤 파일을 폴더 안에 새로운 파일 이름으로 복사하기
shutil.copy("run_btn.png", "test_folder/copied_run_btn.png")  # 원본 파일 경로, 대상 경로 (변경된 파일명까지)
shutil.copyfile("run_btn.png", "test_folder/copied_run_btn_2.png")  # 원본 파일 경로, 대상 파일 경로

# copy, copyfile: 메타정보 복사 X
# copy2: 메타정보 복사 O
shutil.copy("run_btn.png", "test_folder/copy.png")  # 원본 파일 경로, 대상 경로 (변경된 파일명까지)
shutil.copy2("run_btn.png", "test_folder/copy2.png")  # 원본 파일 경로, 대상 폴더/파일 경로


# 폴더 복사하기
shutil.copytree("test_folder", "test_folder2")  # 원본 폴더 경로, 대상 폴더 경로
shutil.copytree("test_folder", "test_folder3")


# 폴더 이동
shutil.move("test_folder", "test_folder3")  # test_folder 를 test_folder3 밑으로 이동
shutil.move("test_folder2", "test_folder3")
shutil.move("test_folder3", "test_folder_rename")  # 폴더명 변경되는 효과
