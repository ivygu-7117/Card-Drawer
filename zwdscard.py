import tkinter as tk
import random

class App:
    def __init__(self):
        self.main_stars = [
            "七杀", "破军", "廉贞", "贪狼", "紫微", "天府", "武曲", "天相", "太阳", "巨门", "天机", "太阴", "天梁", "天同", "空宫"
        ]

        self.aux_stars = [
            "天魁", "天钺", "左辅", "右弼", "文昌", "文曲", "禄存", "天马", "擎羊", "陀螺", "火星", "铃星", "地空", "地劫"   
        ]

        self.longevity_cards = [
            "长生", "沐浴", "冠带", "临官", "帝旺", "衰", "病", "死", "墓", "绝", "胎", "养"
        ]

        self.selected_cards = []

        self.window = tk.Tk()
        self.window.geometry("400x300")

        self.result_label = tk.Label(self.window, text="点击按钮选择一张牌", font=("微软雅黑", 14))
        self.result_label.pack(side=tk.TOP, pady=70)

        button_frame = tk.Frame(self.window)
        button_frame.pack(side=tk.TOP)

        main_star_button = tk.Button(button_frame, text="主星", command=self.select_main_star, font=("微软雅黑", 12))
        main_star_button.pack(side=tk.LEFT, padx=5)

        aux_star_button = tk.Button(button_frame, text="辅星", command=self.select_aux_star, font=("微软雅黑", 12))
        aux_star_button.pack(side=tk.LEFT, padx=5)

        longevity_button = tk.Button(button_frame, text="长生", command=self.select_longevity, font=("微软雅黑", 12))
        longevity_button.pack(side=tk.LEFT, padx=5)

        clear_button = tk.Button(self.window, text="清空结果", command=self.clear_result, font=("微软雅黑", 12))
        clear_button.pack(side=tk.TOP, pady=10)

    def select_card(self, cards):
        return random.choice(cards)

    def show_result(self):
        if self.selected_cards:
            result_text = " ".join(self.selected_cards)
            self.result_label.config(text=result_text)

    def clear_result(self):
        self.selected_cards.clear()
        self.result_label.config(text="点击按钮选择一张牌")

    def select_main_star(self):
        self.selected_cards.clear()  # 清空之前的抽卡结果
        selected_card = self.select_card(self.main_stars)
        self.selected_cards.append(selected_card)
        self.show_result()

    def select_aux_star(self):
        selected_card = self.select_card(self.aux_stars)
        self.selected_cards.append(selected_card)
        self.show_result()

    def select_longevity(self):
        selected_card = self.select_card(self.longevity_cards)
        self.selected_cards.append(selected_card)
        self.show_result()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()
