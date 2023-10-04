import time


def create_diary(_id, _title, _weather, _date, _content, _diary_list):
    _diary_list.append(dict(
        diary_id=_id,
        diary_title=_title,
        diary_weather=_weather,
        diary_date=_date,
        diary_content=_content
    ))
    return _diary_list


def read_diary(_id, _diary_list):
    for diary in _diary_list:
        if diary["diary_id"] != _id:
            continue
        return True, (
                f'제목: {diary["diary_title"]}\n' +
                f'게시일: {diary["diary_date"]}\n' +
                f'날씨: {diary["diary_weather"]}\n' +
                f'내용: {diary["diary_content"]}'
        )
    return False, None


def update_diary(_id, _content, _diary_list):
    is_update = False
    for idx, diary in enumerate(_diary_list):
        if diary["diary_id"] == _id:
            diary["diary_content"] = _content
            is_update = True
            break
    if is_update:
        return True, _diary_list
    return False, None


def delete_diary(_id, _diary_list):
    for idx, diary in enumerate(_diary_list):
        if diary["diary_id"] != _id:
            continue
        del _diary_list[idx]
        return True, _diary_list
    return False, None


if __name__ in '__main__':
    def main():
        diary_list = [
            {
                "diary_id": 0,
                "diary_title": "test1",
                "diary_weather": "맑음",
                "diary_date": time.time(),
                "diary_content": "오늘은 날씨가 맑구나"
            },
            {
                "diary_id": 1,
                "diary_title": "test2",
                "diary_weather": "흐림",
                "diary_date": time.time() + 1,
                "diary_content": "오늘은 날씨가 흐리구나"
            }
        ]
        idx = len(diary_list)
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
                for diary in diary_list:
                    print(f'ID: {diary["diary_id"]} | 제목: {diary["diary_title"]}')
            elif cmd == 1:
                title = input("|> 일기 제목을 입력하세요: ")
                weather = input("|> 날씨를 입력하세요: ")
                content = input("|> 일기 내용을 입력하세요: ")
                diary_list = create_diary(idx, title, weather, time.time(), content, diary_list)
                idx += 1
            elif cmd == 2:
                d_id = int(input("|> 불러올 일기 ID를 입력하세요: "))
                res, diary = read_diary(d_id, diary_list)
                if res:
                    print("|> 일기를 성공적으로 불러왔습니다.")
                    print(diary)
                else:
                    print("|> 일기를 불러오지 못했습니다.")
            elif cmd == 3:
                d_id = int(input("|> 수정할 일기 ID를 입력하세요: "))
                content = input("|> 일기 내용을 입력하세요: ")
                res, _diary_list = update_diary(d_id, content, diary_list)
                if res:
                    print("|> 수정에 성공했습니다.")
                    diary_list = _diary_list
                else:
                    print("|> 수정에 실패했습니다.")
            elif cmd == 4:
                d_id = int(input("|> 삭제할 일기 ID를 입력하세요: "))
                res, _diary_list = delete_diary(d_id, diary_list)
                if res:
                    print("|> 삭제에 성공했습니다.")
                    diary_list = _diary_list
                else:
                    print("|> 삭제에 실패했습니다.")
            elif cmd == 5:
                break
            print()


    main()
