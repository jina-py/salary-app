import streamlit as st

#シフト記号に応じた日給と勤務時間を設定
shift_master = {
    "H4": {"pay": 5400, "hours": 4.5, "hours1": 4.5, "hours2": 0},
    "H5": {"pay": 6000, "hours": 5, "hours1": 5, "hours2": 0},
    "HJ": {"pay": 8750, "hours": 7.25, "hours1": 6.25, "hours2": 1},
    "PB": {"pay": 7600, "hours": 6.25, "hours1": 4.25, "hours2": 2},
    "S4": {"pay": 5450, "hours": 4.5, "hours1": 3.5, "hours2": 1},
    "V8": {"pay": 6725, "hours": 5.5, "hours1": 3, "hours2": 2.5},
    "56": {"pay": 7662, "hours": 6.25, "hours1": 3, "hours2": 3.25},
    "W1": {"pay": 4900, "hours": 4, "hours1": 2, "hours2": 2},
    "W4": {"pay": 5525, "hours": 4.5, "hours1": 2, "hours2": 2.5},
    "W5": {"pay": 6150, "hours": 5, "hours1": 2, "hours2": 3},
    "X1": {"pay": 4950, "hours": 4, "hours1": 1, "hours2": 3},
    "X4": {"pay": 5575, "hours": 4.5, "hours1": 1, "hours2": 3.5},
    "X5": {"pay": 6200, "hours": 5, "hours1": 1, "hours2": 4},
    "Y1": {"pay": 5000, "hours": 4, "hours1": 0, "hours2": 4},
}

transport = 66 #1日あたり通勤手当
pay1 = 1200 #平日昼時給
pay2 = 1254 #平日夕/日祝昼時給

st.title("給与計算ツール")

#入力（例：W1 W1! H4）日祝に ! をつける
input_str = st.text_input("シフト：",placeholder="X1 W4 H4! Y1")

if st.button("計算"):
    #分解＆整形
    shifts = input_str.upper().split()
    total = 0

    #合計計算
    for s in shifts:
        is_holiday = "!" in s
        key = s.replace("!", "")

        if key in shift_master:
            base = shift_master[key]["hours1"] * pay1 + shift_master[key]["hours2"] * pay2
            hours = shift_master[key]["hours"]
            bonus = 54 * hours if is_holiday else 0 #日祝手当（時給＋50円×時間）
            total += base + bonus + transport
            totalhours += hours
          
        else:
            st.write(f"{s}は未定義のシフトです") #定義されてないシフト記号を警告

    #出力
    st.write(f"合計：{int(total)}円")
    st.write(f"勤務時間：{int(totalhours)}時間")
    
