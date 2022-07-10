# -*- encoding: utf-8 -*-
import webbrowser
import sys
import os.path

class Solver:
    data = None
    filepath = "result.html"
    html_str = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>CSVtoHTML</title></head><body><table border="1" width="300"><th>Name</th><th>Korean</th><th>Math</th><th>English</th>'
    html_file = open("result.html","w")

    def __init__(self, path: str) -> None:
        Solver.data = open(path, "r")

    def HTML_maker(self):
        Solver.html_file.write(Solver.html_str) # 표를 그리기 위한 이전까지의 HTML 기본양식 작성
        while True:
            row_str = '<tr>'   # 표의 매 한줄이 끝날 때마다 다음 줄의 HTML을 작성하기 위해 반복문마다 초기화
            line = Solver.data.readline()
            if not line: break
            line_split = line.split(',')   # readline으로 받은 한줄을 ,를 통해 분배
            for i in range(len(line_split)):
                data_str = '<td>'                  # 한 줄 내에서 각 내용을 추가해 줄을 완성
                data_str += str(line_split[i])
                data_str += '</td>'
                row_str += data_str
            row_str += '</tr>'              # 한 줄에 대한 클로징 태그를 닫아서 씀
            Solver.html_file.write(row_str)

        Solver.html_file.write("</table></body></html>") # HTML 양식을 끝내는 코드 추가

    def HTML_opener(self):  # 새 창으로 띄우기 위한 메소드
        webbrowser.open_new_tab(Solver.filepath)

if __name__ == "__main__":
    path = sys.argv[1]

    if os.path.isfile(path):
        maker = Solver(path)
        maker.HTML_maker()
        maker.HTML_opener()

    else:
        print("No such a file!")