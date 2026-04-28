import streamlit as st

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

st.title("給与計算ツール")

#入力（例：W1 W1! H4）日祝に ! をつける
input_str = st.text_input('（日祝は"!"）シフト：')

if st.button("計算"):
    #分解＆整形
    shifts = input_str.upper().split()
    total = 0

    #合計計算
    for s in shifts:
        is_holiday = "!" in s
        key = s.replace("!", "")

        if key in shift_master:
            base = shift_master[key]["pay"]
            hours = shift_master[key]["hours"]
            bonus = 50 * hours if is_holiday else 0 #日祝手当（時給＋50円×時間）
            total += base_pay + bonus + transport
          
        else:
            st.write(f"{s}は未定義のシフトです") #定義されてないシフト記号を警告

    #出力
    st.write(f"合計：{int(total)}円")
    
