from datetime import datetime, timedelta

class DateTimeVerifier() :

    def __init__(self, input_date: datetime) -> None :
        self.holidays = ['2023-12-03','2023-12-10','2023-12-17','2023-12-24','2023-12-25','2023-12-31']
        self.date = input_date.date()
        self.time = input_date.time()

    def isHoliday(self) -> None :
        """
        """
        pass

    def isAfternoon(self) -> None:
        """
        """
        pass

if __name__ == '__main__' :
    now = datetime.now()
    #now = now - timedelta(hours=15) # isAfternoon을 위한 시간 바꾸기
    #now = now - timedelta(days=1) # isHoliday를 위한 날짜 바꾸기

    varifier = DateTimeVerifier(now)
    varifier.isHoliday()
    varifier.isAfternoon()
