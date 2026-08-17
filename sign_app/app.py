
import streamlit as st
import pickle
import numpy as np
from landmarks_extract import extract_landmarks_from_image

st.title("指文字（あ行）認識アプリ")

# 学習済みモデルの読み込み
with open("ai_model.pkl", "rb") as f:
    model = pickle.load(f)

uploaded = st.file_uploader(
    "画像をアップロードしてください（あ・い・う・え・お）",
    type=["jpg", "jpeg", "png", "JPG"]
)

if uploaded is not None:
    temp_path = "temp.jpg"
    with open(temp_path, "wb") as f:
        f.write(uploaded.getvalue())

    feature = extract_landmarks_from_image(temp_path)

    if feature is None:
        st.error("手の検出に失敗しました。画像を変えてみてください。")
    else:
        pred = model.predict(np.array(feature).reshape(1, -1))
        st.success(f"判定結果： {pred[0]}")
        st.image(uploaded)
