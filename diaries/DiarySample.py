from diaries.AbstractDiary import AbstractDiary


class DiarySample(AbstractDiary):
    def get_date(self):
        return "2022-12-08"

    def get_summary(self):
        return "なにもない⼀⽇だった"

    def get_author(self):
        return "Sample"
