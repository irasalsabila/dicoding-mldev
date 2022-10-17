

# Laporan Proyek Machine Learning - Salsabila Zahrah Pranida

## Project Overview
_Recommendation system_ adalah sebuah sistem yang mengacu pada memprediksi sejumlah item atau data untuk pengguna di masa lalu, kemudian dijadikan rekomendasi item paling teratas. Sistem rekomendasi umumnya telah menjadi kelaziman dalam menangani informasi dengan menyarankan pengguna terhadap produk yang paling relevan. Sistem-sistem serupa telah digunakan juga pada produk media, platform film, hingga komersial. 

Beberapa platform yang menyuguhkan film, seperti Vidio, Netflix, WeTV, Viu, dan lainnya menerapkan sistem rekomendasi yang sama. Sistem rekomendasi yang dibuat ini akan memberikan rekomendasi terhadap penguna berdasarkan preferensi genre pengguna, serta _rating_ dari film. Hasil akhir yang diharapkan dari sistem rekomendasi ini adalah dapat memudahkan pengguna untuk mencari film yang diinginkan, baik berdasarkan preferensi film yang serupa, ataupun rekomendasi berdasarkan rating.

## Business Understanding

### Problem Statements
Bagaimana cara memberikan rekomendasi film yang disukai oleh pengguna?

### Goals
Untuk menyelesaikan permasalahan yang telah disampaikan pada bagian _Problem Statement_, maka dibuat sistem rekomendasi yang dapat memberikan rekomendasi film berdasarkan _ratings_ dan aktivitas pengguna pada masa lalu.

### Solution statements
Solusi pembuatan model yang dilakukan adalah dengan menerapkan 1 algoritma machine learning, terbatas pada **Content Based Filtering** dan **Collaborative Filtering**. Diterapkannya 2 algoritma tersebut sama-sama bertujuan untuk memberikan rekomendasi mengenai film kepada pengguna. Algoritma content based filtering akan merekomendasikan film kepada pengguna berdasarkan aktivitas film pengguna di masa lampau. Sedangkan, algoritma collaborative filtering akan merekomendasikan pengguna berdasarkan rating yang paling tinggi.

- **Content Based Filtering**
Algoritma Content Based Filtering adalah algoritma yang menggunakan fitur item untuk merekomendasikan item lain yang serupa dengan apa yang disukai pengguna, berdasarkan tindakan sebelumnya atau umpan balik eksplisit. Algoritma tersebut juga menggunakan kesamaan dalam produk, layanan, atau fitur konten, serta informasi yang dikumpulkan tentang pengguna untuk membuat rekomendasi.

- **Collaborative Filtering**
Algoritma Collaborative Filtering adalah algoritma yang menggunakan kesamaan antara pengguna dan item secara bersamaan untuk memberikan rekomendasi. Algoritma tersebut juga bergantung pada preferensi pengguna serupa untuk menawarkan rekomendasi kepada pengguna tertentu.


## Data Understanding
Dataset yang digunakan pada proyek _machine learning_ merupakan **105.339 data datings** dan **10.329 data movie** yang didapat dari situs [kaggle](https://www.kaggle.com/datasets/ayushimishra2809/movielens-dataset). 

**Variabel-variabel pada Movielens Dataset adalah sebagai berikut:**

1.  movieId = ID movie
2.  title = judul movie
3.  genres = genre dari movie
4.  userId = ID user
5.  rating = rating yang diberikan oleh user terhadap movie
6.  timestamp = waktu ketika user memberikan rating


### Explanatory Data Analysis
Untuk memahami kedua dataset `movies` dan `ratings`, maka dilakukan Univariate Analysis. 

## Data Preparation

_Data preparation_ yang digunakan di antaranya:

1. Seleksi Data: menyeleksi data apakah data tersebut ada yang kosong atau tidak, jika ada data kosong maka akan dihapus. Pada data `ratings` ataupun `movies` tidak didapati data yang kosong. Hal ini dibuktikan dari pengecekan menggunakan `isnull().sum()`.
2. Melakukan Splitting: membagi data menjadi _training_ dan _testing_ untuk _modeling_. Dalam melakukan _splitting_, digunakan rasio 80:20, yang berarti 80% data training, dan 20% data testing.
3. Mengurutkan data: pengurutan data ini dilakukan berdasarkan `movieId` dan dilakukan secara _ascending_.
4. Menghilangkan duplikasi data yang memiliki nilai sama
5. _Cosine Similarity_: menggunakan `cosine_similarity` dari library `sklearn` untuk mendapatkan mengetahui _similarity degree_ 


## Modeling
Tahapan ini membahas mengenai model machine learning yang digunakan untuk menyelesaikan permasalahan. Proses ini dilakukan dengan menggunakan tiga algoritma, yakni **Content Based Filtering** dan **Collaborative Filtering**. Hasil akhir yang diharapkan dari sistem rekomendasi ini adalah dapat memudahkan pengguna untuk mencari film yang diinginkan, baik berdasarkan preferensi film yang serupa, ataupun rekomendasi berdasarkan rating.

1. Dalam membangun **Content Based Filtering**, digunakan module `cosine_similarity` dari _library_ `sklearn`. Digunakan fungsi `movie_recommendation` dengan parameter `movie_name` untuk membangun model. Pada fungsi tersebut juga ditetapkan `k = 5` yang berarti akan mengeluarkan rekomendasi 5 film teratas berdasarkan genre.
- Film yang disukai oleh pengguna dimasa lalu, yang akan dicari rekomendasinya:
- Film yang direkomendasikan melalui fungsi `movie_recommendation`, yang kemudian menghasilkan 5 film teratas sesuai dengan genre yang sama:

1. Dalam membangun **Collaborative Filtering**, dilakukan `training` dan pembuatan model `RecommenderNet`. Training dilakukan dengan optimizer `Adam` dan matriks evaluasi `RMSE`.
- Film genre yang direkomendasikan berdasarkan _rating_ tertinggi:
- Film TOP 10 yang direkomendasikan:


## Evaluation
Evaluasi metrik yang digunakan untuk mengukur kinerja model adalah metrik RMSE (Root Mean Squared Error). RMSE merupakan metode pengukuran dengan mengukur perbedaan nilai dari prediksi sebuah model sebagai estimasi atas nilai yang diobservasi, dan merupakan hasil kuadrat dari MSE. Keakuratan metode estimasi kesalahan pengukuran ditandai dengan adanya nilai RMSE yang kecil. 

Semakin kecil nilai yang diperoleh RMSE, semakin akurat juga modelnya.

Rumus perhitungan matrik MSE: 
![alt](https://www.gstatic.com/education/formulas2/472522532/en/mean_squared_error.svg)

ket:

$\mathrm{RMSE}$	=	mean squared error

${n}$	=	_number of data points_

$Y_{i}$	=	_observed values_ atau _ground truth_ dari nilai sebenarnya.

$\hat{Y}_{i}$	=	_predicted values_ atau _estimated target values_.

Hasil dari evaluasi matriks adalah sebagai berikut:


Dari visualisasi proses training model di atas cukup smooth dan model konvergen pada epochs sekitar 100. Dari proses ini, saya memperoleh nilai error akhir sebesar sekitar 0.19 dan error pada data validasi sebesar 0.20.

Referensi:

[1] [Recommender System for Movielens Datasets using an Item-based Collaborative Filtering in Python](https://www.scipublications.com/journal/index.php/ijmebac/article/view/340)

[2] [Employing opposite ratings users in a new approach to collaborative filtering](https://ijeecs.iaescore.com/index.php/IJEECS/article/viewFile/24894/15925)

[3] [The MovieLens Datasets: History and Context](https://dl.acm.org/doi/10.1145/2827872)

[4] [Movielens Dataset](https://www.kaggle.com/datasets/ayushimishra2809/movielens-dataset)

