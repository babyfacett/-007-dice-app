import streamlit as st
import random


def main():
    """Dice rolling application that returns a random number between 1 and 6."""
    st.title("サイコロアプリ")
    st.write("ボタンをクリックすると 1〜6 の数値がランダムに表示されます。")

    if st.button("サイコロを振る"):
        result = random.randint(1, 6)
        st.success(f"出た目は {result} です！")


if __name__ == "__main__":
    main()