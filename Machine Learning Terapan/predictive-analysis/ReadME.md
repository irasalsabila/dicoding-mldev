
# Laporan Proyek Machine Learning - Salsabila Zahrah Pranida

## Domain Proyek
Domain yang dipilih untuk dilakukan prediksi adalah domain kesehatan, yang berfokus pada penyakit kardiovaskular. 

Penyakit kardiovaskular (CVD) adalah penyebab utama kematian di seluruh dunia, merenggut sekitar 17,9 juta jiwa setiap tahun dan menyumbang 31% dari semua kematian di seluruh dunia. Empat dari setiap lima kematian akibat penyakit kardiovaskular disebabkan oleh serangan jantung dan stroke, dan sepertiga dari kematian ini terjadi lebih awal pada orang di bawah usia 70 tahun. Gagal jantung adalah kejadian umum yang disebabkan oleh CVD dan dataset ini berisi 11 fitur yang dapat digunakan untuk memprediksi kemungkinan penyakit jantung. 
 
Orang dengan penyakit kardiovaskular atau risiko kardiovaskular tinggi (karena adanya satu atau lebih faktor risiko seperti hipertensi, diabetes, hiperlipidemia, kondisi medis yang sudah ada sebelumnya) adalah pengguna awal yang memerlukan deteksi dan manajemen dini, di mana model _machine learning_ yang dibuat dapat sangat membantu. 

## Business Understanding

### Problem Statements
Bagaimana mengetahui pasien memiliki penyakit jantung (_heart disease_) berdasarkan riwayat dari variabel-variabel kesehatan yang ada?

### Goals
Untuk menyelesaikan permasalahan yang telah disampaikan pada bagian _Problem Statement_, maka dibuat model yang digunakan untuk memprediksi apakah seseorang memiliki penyakit jantung (_heart disease_) berdasarkan riwayat kesehatannya.

### Solution statements
Solusi pembuatan model yang dilakukan adalah dengan menerapkan 3 algoritma machine learning, terbatas pada **_K-NN_**, **_Random Forest_**, dan **_AdaBoost_**. Diterapkannya 3 algoritma tersebut bertujuan untuk mengkomparasi dan mendapatkan model atau algoritma yang memiliki tingkat _error_ yang paling kecil, sehingga prediksi penyakit jantung memiliki akurasi yang tinggi.

- **_K-NN_**
Algoritma _K-Nearest Neighbor_ (K-NN) adalah algoritma _machine learning_ yang sederhana dan mudah diterapkan, yang mana umumnya digunakan untuk menyelesaikan masalah klasifikasi dan regresi. Algoritma ini termasuk dalam _supervised learning_. Tujuan dari algortima K-NN adalah untuk mengidentifikasi _nearest neighbor_ dari titik yang diberikan, sehingga dapat menetapkan label prediksi ke titik tersebut.

- **_Random Forest_**
_Random forest_ adalah kombinasi dari masing – masing _tree_ atau pohon, yang kemudian dikombinasikan ke dalam satu model. _Random Forest_ bergantung pada sebuah nilai vector acak dengan distribusi yang sama pada semua pohon yang masing masing _tree_ memiliki kedalaman yang maksimal.

- **_AdaBoost_**
_AdaBoost_ atau _Adaptive Boost_ merupakan algoritma yang memanfaatkan _bagging_ dan _boosting_ untuk meningkatkan akurasi. Sama seperti algoritma _random forest_, algoritma _AdaBoost_ juga menggunakan beberapa _decision tree_ untuk melakukan prediksi.

## Data Understanding
Dataset yang digunakan pada proyek _machine learning_ merupakan **918 data observasi** yang didapat dari situs [kaggle](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction) dan [UCI Machine Learning Repository](http://archive.ics.uci.edu/ml/datasets/Heart+Disease). Terdapat 11 fitur yang dapat digunakan untuk memprediksi kemungkinan penyakit jantung. 

**Variabel-variabel pada Heart Failure UCI Dataset adalah sebagai berikut:**

1.  Age: usia pasien, dalam tahun (_years_)
2.  Sex: jenis kelamin pasien 
	- M: Pria (_Male_), 
	- F: Wanita (_Female_)
3.  ChestPainType: tipe sakit pada dada
    - TA: Typical Angina, 
    - ATA: Atypical Angina, 
    - NAP: Non-Anginal Pain, 
    - ASY: Asymptomatic
4.  RestingBP: tekanan darah (_mm Hg_)
5.  Cholesterol: serum cholesterol (_mm/dl_)
6.  FastingBS: gula darah 
    - if FastingBS > 120 mg/dl 
    - 0: sebaliknya (_otherwise_)
7.  RestingECG: hasil ECG 
    - Normal: Normal, 
    - ST: memiliki kelainan gelombang ST-T (inversi gelombang T dan/atau elevasi atau depresi ST > 0,05 mV), 
    - LVH: menunjukkan kemungkinan atau pasti hipertrofi ventrikel kiri menurut kriteria Estes
8.  MaxHR: detak jantung maksimum tercapai (Nilai numerik antara 60 dan 202)
9.  ExerciseAngina: angina yang diinduksi oleh olahraga [
    - Y: Ya, 
    - N: Tidak (_No_)
10.  Oldpeak: oldpeak = ST (Nilai numerik diukur dalam depresi)
11.  ST_Slope: kemiringan puncak latihan segmen ST 
     - Up: upsloping, 
     - Flat: flat, 
     - Down: downsloping]
12.  HeartDisease: kelas keluaran
     - 1: Penyakit Jantung (_heart disease_), 
     - 0: Normal


**Explanatory Data Analysis**
Untuk memahami data _heart disease_ dilakukan visualisasi menggunakan _bar chart_ dan _pie chart_. Dalam memvisualisasikannya, dilakukan dengan _Univariate Analysis_ dan _Multivariate Analysis_. Untuk keseluruhannya, dataset dibagi menjadi dua fitur, yakni fitur _categorical_ dan fitur _numerical_.


## Data Preparation
Pada bagian ini Anda menerapkan dan menyebutkan teknik data preparation yang dilakukan. Teknik yang digunakan pada notebook dan laporan harus berurutan.

_Data preparation_ yang digunakan di antaranya:

1. Seleksi Data: Menyeleksi data apakah data tersebut ada yang kosong atau tidak, jika ada data kosong maka akan dihapus.
2. Menangani Outlier: Melakukan pengecekan apakah data _heart disease_ memiliki data outlier. Apabila terdapat data outlier, maka akan dihapus. Dalam menangani _outlier_, digunakan metode IQR.
3. Melakukan Label Encoder: Melakukan proses encoding terhadap `categorical_feature`. Hal ini dilakukan karena fitur-fitur kategorikal perlu dirubah agar dapat digunakan pada tahap _modeling_.
4. Melakukan Splitting: membagi data menjadi _training_ dan _testing_ untuk _modeling_. Dalam melakukan _splitting_, digunakan rasio 80:20, yang berarti 80% data training, dan 20% data testing.
5. Standarisasi: membantu membuat fitur data menjadi bentuk yang lebih mudah diolah oleh algoritma.


## Modeling
Tahapan ini membahas mengenai model machine learning yang digunakan untuk menyelesaikan permasalahan. Proses ini dilakukan dengan menggunakan tiga algoritma, yakni KNN, RandomForest, dan AdaBoost. Hasil akhirnya adalah untuk mencari algoritma yang memiliki performa paling baik dari ketiga algoritma yang digunakan. Dapat dilihat dari _bar chart_ yang menunjukkan tiga model algoritma yang digunakan. Diketahui bahwa algoritma KNN merupakan algoritma yang memiliki error yang paling kecil dibanding model lainnya.

![model](https://github.com/irasalsabila/dicoding-mldev/blob/main/Machine%20Learning%20Terapan/output/eval.png?raw=true)

Gambar di atas dapat dilihat juga pada tabel di bawah ini. Tabel memberikan informasi detail terkait hasil _training_ dan _testing_

|		| train	    |	test      |
|---------------|-----------|-------------|
|KNN		| 0.000128  |	0.000141  |
|AdaBoost	| 0.000183  |	0.000201  |
|RandomForest	| 0.00012   |	0.000158  |

Pada tabel di bawah disajikan informasi hasil prediksi dari model yang digunakan. Dari tabel yang disajikan dapat dilihat bahwa prediksi menggunakan KNN pada baris 199, memiliki hasil paling sesuai dengan data aslinya, dibandingkan kedua model lainnya.

|     | y_true | prediksi_KNN | prediksi_AdaBoost | prediksi_RandomForest |
|-----|--------|--------------|-------------------|-----------------------|
| 199 | 0      | 0            | 1                 | 1                     |
| 44  | 1      | 1            | 1                 | 1                     |
| 103 | 1      | 1            | 1                 | 1                     |
| 852 | 1      | 1            | 1                 | 1                     |

## Evaluation
Evaluasi metrik yang digunakan untuk mengukur kinerja model adalah metrik mse (Mean Squared Error). Pemilihan matrik ini disebabkan karena kasus atau domain proyek yang dipilih adalah klasifikasi. Matrik MSE, pada dasarnya akan mengukur kuadrat rerata error dari prediksi yang dilakukan. MSE juga akan menghitung selisih kuadrat antara prediksi dan target, yang kemudian melakukan perhitungan rata-rata terhadap nilai-nilai tersebut.

Semakin tinggi nilai yang diperoleh MSE, semakin buruk juga modelnya. Nilai MSE tidak pernah negatif, tetapi akan menjadi NOL untuk model yang sempurna.

Rumus perhitungan matrik MSE: 
![alt](https://www.gstatic.com/education/formulas2/472522532/en/mean_squared_error.svg)

ket:

$\mathrm{MSE}$	=	mean squared error

${n}$	=	_number of data points_

$Y_{i}$	=	_observed values_ atau _ground truth_ dari nilai sebenarnya, dalam kasus ini nilai yang digunakan adalah nilai dari variabel `HeartDisease`

$\hat{Y}_{i}$	=	_predicted values_ atau _estimated target values_, dalam kasus ini nilai yang digunakan adalah nilai prediksi model terhadap variabel `HeartDisease`


Untuk melakukan evaluasi matrik, dapat menerapkan _code_ yang berada pada Evaluation Model yang tercantum pada _notebook_. Dalam melakukan evaluasi, nilai $\hat{Y}_{i}$ merupakan nilai prediksi yang keluar dari variabel-variabel yang ada dalam `Xtrain`, seperti `Age`, `Sex`, `ChestPainType`, `RestingBP`, `Cholesterol`, `FastingBS`, `RestingECG`, `MaxHR`, `ExerciseAngina`, `Oldpeak`, dan `ST_Slope`. Variabel-variabel pada tabel di bawah kemudian digunakan untuk melakukan prediksi, yang mana akan mengeluarkan nilai 0 atau 1, dan akan tersimpan pada variabel _predicted value_ .

|   |       Age |       Sex | ChestPainType | RestingBP | Cholesterol | FastingBS | RestingECG |     MaxHR | ExerciseAngina |   Oldpeak |  ST_Slope |
|--:|----------:|----------:|--------------:|----------:|------------:|----------:|-----------:|----------:|---------------:|----------:|----------:|
| 0 |  0.052026 |  0.516309 |      1.276887 |  0.970493 |   -0.036784 | -0.551733 |   0.017264 | -0.581047 |      -0.824310 | -0.831502 |  1.051095 |
| 1 |  0.052026 | -1.936826 |      0.230501 |  0.414627 |    1.007298 | -0.551733 |   1.600366 |  0.126132 |      -0.824310 | -0.831502 |  1.051095 |
| 2 |  0.158042 |  0.516309 |     -0.815884 | -0.030066 |    1.410278 | -0.551733 |   0.017264 | -0.188170 |       1.213136 |  0.293802 | -0.596519 |
| 3 | -1.114157 | -1.936826 |      1.276887 |  0.970493 |    0.503574 | -0.551733 |   0.017264 |  1.501203 |      -0.824310 | -0.831502 |  1.051095 |
| 4 | -0.372041 |  0.516309 |     -0.815884 |  0.414627 |    0.292926 | -0.551733 |   1.600366 |  0.126132 |       1.213136 |  3.857266 | -0.596519 |

Sedangkan, nilai $Y_{i}$ merupakan nilai sebenarnya dari variabel `HeartDisease`, yakni 0 dan 1. Kemudian, MSE akan melakukan perhitungan yang melibatkan hasil dari _predicted value_ dan _ground truth_, yang keduanya sama-sama memiliki nilai 0 dan 1.

Referensi:

[1] [Heart Failure: Diagnosis, Severity Estimation and Prediction of Adverse Events Through Machine Learning Techniques](https://www.sciencedirect.com/science/article/pii/S2001037016300460)

[2] [Heart Failure UCI Dataset](http://archive.ics.uci.edu/ml/datasets/Heart+Disease)
