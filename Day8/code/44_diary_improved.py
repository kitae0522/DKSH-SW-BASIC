import uuid
import time


class ReturnClass:
    def __init__(self, _is_error, _message):
        self.is_error = _is_error
        self.message = _message

    def __iter__(self):
        yield self.is_error
        yield self.message


class ReturnClassWithResult(ReturnClass):
    def __init__(self, _is_error, _message, _result):
        super().__init__(_is_error, _message)
        self.result = _result

    def __iter__(self):
        yield self.is_error
        yield self.message
        yield self.result


class Diary:
    def __init__(self, diary_info):
        self.id = diary_info["id"]
        self.title = diary_info["title"]
        self.content = diary_info["content"]
        self.weather = diary_info["weather"]
        self.datetime = diary_info["datetime"]


class DiaryService:
    def __init__(self):
        self.diary_list = []

    def find_diary(self, diary_id):
        for idx, diary in enumerate(self.diary_list):
            if diary.id != diary_id:
                continue
            return ReturnClassWithResult(False, "* 성공적으로 일기를 찾았습니다.", idx)
        return ReturnClassWithResult(True, "* 일기를 찾지 못했습니다.", None)

    def create_diary(self, diary_title, diary_content, diary_weather):
        diary_id = str(uuid.uuid4())
        new_diary = Diary({"id": diary_id,
                           "title": diary_title,
                           "content": diary_content,
                           "weather": diary_weather,
                           "datetime": time.time()})
        self.diary_list.append(new_diary)

    def read_diary(self, diary_id):
        is_error, message, result = self.find_diary(diary_id)
        if is_error or result is None:
            return ReturnClassWithResult(True, message, None)
        return ReturnClassWithResult(False,
                                     "* 성공적으로 일기를 읽어왔습니다.",
                                     f"제목: {self.diary_list[result].title}\n"
                                     f"내용: {self.diary_list[result].content}\n"
                                     f"날씨: {self.diary_list[result].weather}\n")

    def update_diary(self, diary_id, diary_content):
        is_error, message, result = self.find_diary(diary_id)
        if is_error or result is None:
            return ReturnClass(True, message)
        get_diary = self.diary_list[result]
        self.diary_list[result] = Diary({
            "id": get_diary.id,
            "title": get_diary.title,
            "content": diary_content,
            "weather": get_diary.weather,
            "datetime": get_diary.datetime
        })
        return ReturnClass(False, "* 성공적으로 일기를 수정했습니다.")

    def delete_diary(self, diary_id):
        is_error, message, result = self.find_diary(diary_id)
        if is_error or result is None:
            return ReturnClass(True, message)
        del self.diary_list[result]
        return ReturnClass(False, "* 성공적으로 일기를 삭제했습니다.")


if __name__ == '__main__':
    app = DiaryService()
    app.create_diary("test1", "dhsmfdms skfTLrk gmflrnsk", "흐림")
    while True:
        print("=" * 30 + "\n",
              "일기 프로그램\n",
              "=" * 30 + "\n",
              "0. 일기 목록보기\n",
              "1. 일기 작성하기\n",
              "2. 일기 불러오기\n",
              "3. 일기 수정하기\n",
              "4. 일기 삭제하기\n",
              "5. 프로그램 종료",
              sep=""
              )
        cmd = int(input("메뉴를 선택하세요: "))
        if cmd == 0:
            print("|> 일기 목록")
            for diary in app.diary_list:
                print(f'ID: {diary.id} | 제목: {diary.title}')
        elif cmd == 1:
            title = input("|> 일기 제목을 입력하세요: ")
            weather = input("|> 날씨를 입력하세요: ")
            content = input("|> 일기 내용을 입력하세요: ")
            app.create_diary(title, content, weather)
        elif cmd == 2:
            d_id = input("|> 불러올 일기 ID를 입력하세요: ")
            is_error, message, result = app.read_diary(d_id)
            print(message)
            if not is_error:
                print(result)
        elif cmd == 3:
            d_id = input("|> 수정할 일기 ID를 입력하세요: ")
            is_error, message, _ = app.find_diary(d_id)
            if is_error:
                print(message)
            else:
                content = input("|> 일기 내용을 입력하세요: ")
                is_error, message = app.update_diary(d_id, content)
                print(message)
        elif cmd == 4:
            d_id = input("|> 삭제할 일기 ID를 입력하세요: ")
            is_error, message, _ = app.find_diary(d_id)
            if is_error:
                print(message)
            else:
                is_error, message = app.delete_diary(d_id)
                print(message)
        elif cmd == 5:
            break
        print()
