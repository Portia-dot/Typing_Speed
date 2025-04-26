import datetime
class Header:
    def __init__(self):
        self.start_timestamp = None
        self.sample_text = ("How fast are your fingers? Do the one-minute typing test to find out! Press the space bar after each word. At the end.How fast are your fingers? Do the one-minute typing test to find out! Press the space bar after each word. At the end"
               "How fast are your fingers? Do the one-minute typing test to find out! Press the space bar after each word. At the end"
               "How fast are your fingers? Do the one-minute typing test to find out! Press the space bar after each word. At the end")
        self.style = ('Arial', 15,)
        self.elapsed_time = 0
        self.remaining_time = 60

    def header_item(self, canvas, text_x, text_y, rect_x1, rect_y1, rect_x2, rect_y2, score_x, score_y,  title_text, score_text ):
        title = canvas.create_text(text_x, text_y, text= title_text, font = self.style)
        rect = canvas.create_rectangle(rect_x1, rect_y1, rect_x2, rect_y2, fill='lightblue', outline='black')
        reading_score = canvas.create_text(score_x, score_y, text=score_text, font = ('Arial', 10))
        return title, rect, reading_score




    def calculate_wps(self, user_typed):
            if self.start_timestamp is None and len(user_typed) > 0:
                self.start_timestamp = datetime.datetime.now()
            if self.start_timestamp is None or len(user_typed) == 0:
                return 0 , 0, None,None, 60
            end_timestamp = datetime.datetime.now()
            elapsed_time = (end_timestamp - self.start_timestamp).total_seconds()
            if elapsed_time < 0.1:
                elapsed_time = 0.1
            remaining_time = 60 - elapsed_time
            if remaining_time < 0:
                remaining_time = 0
            if elapsed_time > 60:
                elapsed_time = 60
            elapsed_minutes = elapsed_time / 60
            if elapsed_minutes > 0:
                total_chars = len(user_typed)
                wps = total_chars / elapsed_minutes / 5
                cpm = total_chars / elapsed_minutes
            else:
                wps = 0
                cpm = 0
            return wps, cpm, elapsed_time, elapsed_minutes, remaining_time

    def reset_timer_variables(self):
        self.start_timestamp = None
        self.elapsed_time = 0
        self. remaining_time = 60