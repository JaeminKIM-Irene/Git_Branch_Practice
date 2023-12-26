from datetime import datetime, timedelta

class DateTimeVerifier() :

    def __init__(self, input_date: datetime) -> None :
        self.holidays = ['2023-12-03','2023-12-10','2023-12-17','2023-12-24','2023-12-25','2023-12-31']
        self.date = input_date.date()
        self.time = input_date.time()

    def isHoliday(self) -> None :
        """
        """

        year = self.date.year
        month = self.date.month
        day = self.date.day
        for holiday in self.holidays :
            if holiday == self.date.strftime('%Y-%m-%d') :
                print(f"입력하신 날짜 {year}년 {month}월 {day}일은 휴일입니다")
                return
        print(f"입력하신 날짜 {year}년 {month}월 {day}일은 휴일이 아닙니다")
        return

    def isAfternoon(self) -> None:
        """
        """

        hour = self.time.hour
        minute = self.time.minute
        if hour < 12 :
            print(f"현재 시간은 오전 {hour}시 {minute}분입니다")
        else :
            print(f"현재 시간은 오후 {hour-12}시 {minute}분입니다")

if __name__ == '__main__' :
    now = datetime.now()
    #now = now - timedelta(hours=15) # isAfternoon을 위한 시간 바꾸기
    #now = now - timedelta(days=1) # isHoliday를 위한 날짜 바꾸기

    varifier = DateTimeVerifier(now)
    varifier.isHoliday()
    varifier.isAfternoon()
