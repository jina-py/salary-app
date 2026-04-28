#シフト記号に応じた日給と勤務時間を設定
shift_master = {
    "H4": {"pay": 5400, "hours": 4.5},
    "H5": {"pay": 6000, "hours": 5},
    "HJ": {"pay": 8750, "hours": 7.25},
    "PB": {"pay": 7600, "hours": 6.25},
    "S4": {"pay": 5450, "hours": 4.5},
    "V8": {"pay": 6725, "hours": 5.5},
    "56": {"pay": 7662, "hours": 6.25},
    "W1": {"pay": 4900, "hours": 4},
    "W4": {"pay": 5525, "hours": 4.5},
    "W5": {"pay": 6150, "hours": 5},
    "X1": {"pay": 4950, "hours": 4},
    "X4": {"pay": 5575, "hours": 4.5},
    "X5": {"pay": 6200, "hours": 5},
    "Y1": {"pay": 5000, "hours": 4},
}

transport = 5 #通勤手当1日5円
total = 0

#入力（例：W1 W1! H4）日祝に ! をつける
input_str = input('（日祝は"!"）シフト：')

#分解＆整形
shifts = input_str.upper().split()

#合計計算
for s in shifts:
    is_holiday = "!" in s
    shift_key = s.replace("!", "")

    if shift_key in shift_master:
        base_pay = shift_master[shift_key]["pay"]
        hours = shift_master[shift_key]["hours"]

        #日祝手当（時給＋50円×時間）
        bonus = 0
        if is_holiday:
            bonus = 50 * hours

        total += base_pay + bonus + transport

    else:
        print(f"{s}は未定義のシフトです") #定義されてないシフト記号を警告

#出力
total = int(total)
print(f"今月の予測給与は {total} 円です")