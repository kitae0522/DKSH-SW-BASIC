import datetime


class Logger:
    def log(self, msg):
        print(msg)


class TimeStampLogger(Logger):
    def log(self, whoami):
        msg = f"{whoami} >> {datetime.datetime.now()}"
        super().log(msg)


class DateLogger(Logger):
    def log(self, whoami):
        msg = f"{whoami} >> {datetime.datetime.now().strftime('%Y-%m-%d')}"
        super().log(msg)


if __name__ == '__main__':
    def main():
        l = Logger()
        t = TimeStampLogger()
        d = DateLogger()
        l.log("Logger")  # 출력 결과: Logger
        t.log("TimeStampLogger")  # 출력 결과: TimeStampLogger >> 2023-09-20 02:07:58.936596
        d.log("DateLogger")  # 출력 결과: DateLogger >> 2023-09-20


    main()
