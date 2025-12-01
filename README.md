# 指文字（あ行）認識AIアプリ  
MediaPipe Handsで抽出した手のランドマーク座標を用いて、  
「あ・い・う・え・お」の指文字を認識する機械学習モデルとWebアプリです。

---

## 📌 概要
このプロジェクトは、手話の指文字（あ行）を静止画から判定するアプリケーションです。  
MediaPipeによる特徴点抽出 → RandomForestによる学習 → StreamlitでWebアプリ化  
という **機械学習の一連の流れ** をまとめています。

学習と推論の両方を理解できる実践的なプロジェクトです。

---

## 🧠 使用技術
- Python 3.x  
- MediaPipe Hands  
- OpenCV  
- RandomForestClassifier（scikit-learn）  
- NumPy / Pandas  
- Streamlit（Webアプリ化）

---

## 🏗 プロジェクト構成
```
sign-fingerspell-ai/
├── sign_app/
│   ├── app.py                 # Streamlit アプリ本体
│   ├── ai_model.pkl           # 学習済みモデル
│   └── landmarks_extract.py   # MediaPipe でランドマーク抽出
│
├── notebooks/
│   ├── 01_landmark_extraction.ipynb   # 特徴点抽出処理
│   └── 02_training_model.ipynb        # モデル学習
│
├── data/ （必要に応じて公開しない）
├── requirements.txt
└── README.md
```

---

## 📸 アプリ画面（スクリーンショット）

### 📌 トップ画面
![アプリ画面](images/アプリ画面.png)

### 📌 画像アップロード画面
![画像](images/画像.png)

### 📌 判定結果
![判定結果](images/成果の画像.png)


## 🚀 使い方（ローカル実行）
### 1. 必要なライブラリをインストール
```
pip install -r requirements.txt
```

### 2. アプリを起動
```
streamlit run app/app.py
```

### 3. ブラウザで確認
```
http://localhost:8501
```

---

## 🎯 学習モデルについて

### ● 特徴量（63次元）  
MediaPipe Hands の 21点 × (x, y, z) の座標を使用。

### ● モデル  
- RandomForestClassifier  
- 5クラス分類（あ・い・う・え・お）

---

## 📊 モデル精度
（例、後で差し替え可能）

- Accuracy：92.3% 
- Confusion Matrix：あり  
- 指文字のランドマークにばらつきがある場合は misclassification あり

---

## 🔮 今後の改善案
- 学習データの増加で精度向上（特に「え」「お」）  
- スマホカメラ対応（リアルタイム認識）  
- CNN などのDeep Learningモデルへ発展  
- 手話認識（複数動き）の拡張

---

## 👤 制作者
**山田真一郎（やま）**  
Python / データサイエンス / 画像認識を学習中  
Webアプリや機械学習モデルの開発経験あり

---

## 📄 ライセンス
This project is licensed under the MIT License.
