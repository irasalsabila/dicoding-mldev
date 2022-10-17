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

| userId | movieId | rating | timestamp |  |
|---:|---:|---:|---:|---|
| count | 105339.000000 | 105339.000000 | 105339.000000 | 1.053390e+05 |
| mean | 364.924539 | 13381.312477 | 3.516850 | 1.130424e+09 |
| std | 197.486905 | 26170.456869 | 1.044872 | 1.802660e+08 |
| min | 1.000000 | 1.000000 | 0.500000 | 8.285650e+08 |
| 25% | 192.000000 | 1073.000000 | 3.000000 | 9.711008e+08 |
| 50% | 383.000000 | 2497.000000 | 3.500000 | 1.115154e+09 |
| 75% | 557.000000 | 5991.000000 | 4.000000 | 1.275496e+09 |
| max | 668.000000 | 149532.000000 | 5.000000 | 1.452405e+09 |

Dari tabel di atas dapat diketahui dengan detail bahwa data `rating` memiliki minimum rating sebesar 0.5, dan maksimal rating sebesar 5, serta rata-rata rating sebesar 3.5

## Data Preparation

_Data preparation_ yang digunakan di antaranya:

1. Seleksi Data: menyeleksi data apakah data tersebut ada yang kosong atau tidak, jika ada data kosong maka akan dihapus. Pada data `ratings` ataupun `movies` tidak didapati data yang kosong. Hal ini dibuktikan dari pengecekan menggunakan `isnull().sum()`.
2. Melakukan Splitting: membagi data menjadi _training_ dan _testing_ untuk _modeling_. Dalam melakukan _splitting_, digunakan rasio 80:20, yang berarti 80% data training, dan 20% data testing.
3. Mengurutkan data: pengurutan data ini dilakukan berdasarkan `movieId` dan dilakukan secara _ascending_.
4. Menghilangkan duplikasi data yang memiliki nilai sama
5. Melakukan pembobotan dengan TF-IDF.
6. _Cosine Similarity_: menggunakan `cosine_similarity` dari library `sklearn` untuk mendapatkan mengetahui _similarity degree_ 


## Modeling
Tahapan ini membahas mengenai model machine learning yang digunakan untuk menyelesaikan permasalahan. Proses ini dilakukan dengan menggunakan tiga algoritma, yakni **Content Based Filtering** dan **Collaborative Filtering**. Hasil akhir yang diharapkan dari sistem rekomendasi ini adalah dapat memudahkan pengguna untuk mencari film yang diinginkan, baik berdasarkan preferensi film yang serupa, ataupun rekomendasi berdasarkan rating.

1. Dalam membangun **Content Based Filtering**, hal pertama yang akan dilakukan adalah melakukan pembobotan terhadap fitur `genre` menggunakan module `TfidfVectorizer` dari _library_ `sklearn` untuk mendapatkan genre apa saja yang ada. Selanjutnya, digunakan module `cosine_similarity` dari _library_ `sklearn`. Digunakan fungsi `movie_recommendation` dengan parameter `movie_name` untuk membangun model. Pada fungsi tersebut juga ditetapkan `k = 5` yang berarti akan mengeluarkan rekomendasi 5 film teratas berdasarkan genre.

- Film yang disukai oleh pengguna dimasa lalu, yang akan dicari rekomendasinya:

| id | title | genre | timestamp |  |
|---:|---:|---:|---:|---|
| 113 | 1 | Toy Story (1995) | Adventure\|Animation\|Children\|Comedy\|Fantasy | 1.053390e+05 |

- Film yang direkomendasikan melalui fungsi `movie_recommendation`, yang kemudian menghasilkan 5 film teratas sesuai dengan genre yang sama:

|  | title | genre |  |  |
|---:|---:|---:|---:|---|
| 0 | Shrek the Third (2007) | Adventure\|Animation\|Children\|Comedy\|Fantasy |
| 1 | Adventures of Rocky and Bullwinkle, The (2000) | Adventure\|Animation\|Children\|Comedy\|Fantasy |
| 2 | Wild, The (2006) | Adventure\|Animation\|Children\|Comedy\|Fantasy |
| 3 | Antz (1998) | Adventure\|Animation\|Children\|Comedy\|Fantasy | 
| 4 | Tale of Despereaux, The (2008) | Adventure\|Animation\|Children\|Comedy\|Fantasy |

1. Dalam membangun **Collaborative Filtering**, dilakukan `training` dan pembuatan model `RecommenderNet`. Training dilakukan dengan optimizer `Adam` dan matriks evaluasi `RMSE`. Model `RecommenderNet` akan menghitung skor _match_ di antara dua _embedding layers_ milik _user_ dan _movie_ melalui `dot_product`, dan menambahkan bias ke keduanya. _Match_ skor kemudian akan berada pada skala interval 0 hingga 1 melalui `sigmoid`.

- Film genre yang direkomendasikan berdasarkan _rating_ tertinggi:

| movie with high ratings from user |
|---|
| Multiplicity (1996) : Comedy |
| Maverick (1994) : Adventure\|Comedy\|Western |
| Age of Innocence, The (1993) : Drama |
| Legends of the Fall (1994) : Drama\|Romance\|War\|Western |
| Primal Fear (1996) : Crime\|Drama\|Mystery\|Thriller |


- Film TOP 10 yang direkomendasikan:

| Top 10 movie recommendation |
|---|
| Memories (Memorîzu) (1995) : Animation\|Fantasy\|Sci-Fi\|Thriller |
| King of Masks, The (Bian Lian) (1996) : Drama |
| Memories of Murder (Salinui chueok) (2003) : Crime\|Drama\|Mystery\|Thriller |
| Until the End of the World (Bis ans Ende der Welt) (1991) : Adventure\|Drama\|Sci-Fi |
| Interstate 60 (2002) : Adventure\|Comedy\|Drama\|Fantasy\|Mystery\|Sci-Fi\|Thriller |
| Resident Evil: Retribution (2012) : Action\|Horror\|Sci-Fi\|IMAX |
| Fireworks (Hana-bi) (1997) : Crime\|Drama |
| Pier, The (Jetée, La) (1962) : Romance\|Sci-Fi |
| Star Wreck: In the Pirkinning (2005) : Action\|Comedy\|Sci-Fi |
| Animal Farm (1954) : Animation\|Drama |


## Evaluation
### Content Based Filtering
Evaluasi yang dapat digunakan adalah matriks presisi. Presisi merupakan sebuah kemampuan dari alat ukur untuk menunjukkan angka yang sama bila dipakai secara berulang-ulang dalam kondisi pengukuran dan obyek ukur yang sama. Pada kasus ini, presisi akan memprediksi label yang benar terhadap keseluruhan prediksi. 

Rumus perhitungan matrik presisi:
![pres](https://user-images.githubusercontent.com/57740421/196231953-e943707a-8221-4f64-80f7-d6826a514c58.png)

Dari hasil rekomendasi yang ditampilkan pada bagian modeling, diketahui bahwa pengguna akan mencari rekomendasi film terkait `Toy Story (1995)`. Kemudian, sistem rekomendasi memberikan 5 film terkait yang memiliki genre serupa, yakni `Adventure\|Animation\|Children\|Comedy\|Fantasy`. Berdasarkan rumus presisi di atas, diketahui bahwa keseluruhan rekomendasi yang diberikan memiliki genre serupa dengan film yang dicari rekomendasinya. Artinya, presisi sistem yang dibangun sebesar 5/5 atau 100%.

### Collaborative Filtering
Evaluasi metrik yang digunakan untuk mengukur kinerja model adalah metrik RMSE (Root Mean Squared Error). RMSE merupakan metode pengukuran dengan mengukur perbedaan nilai dari prediksi sebuah model sebagai estimasi atas nilai yang diobservasi, dan merupakan hasil kuadrat dari MSE. Keakuratan metode estimasi kesalahan pengukuran ditandai dengan adanya nilai RMSE yang kecil. 

Semakin kecil nilai yang diperoleh RMSE, semakin akurat juga modelnya.

Rumus perhitungan matrik MSE: 
![image](https://user-images.githubusercontent.com/57740421/196224758-6f05beb8-a8bd-4abb-ab5c-72801d9c3b9f.png)

ket:

$\mathrm{RMSE}$	=	mean squared error

${n}$	=	_number of data points_

$Y_{i}$	=	_observed values_ atau _ground truth_ dari nilai sebenarnya.

$\hat{Y}_{i}$	=	_predicted values_ atau _estimated target values_.

Hasil dari evaluasi matriks adalah sebagai berikut:
![ev-rmse](https://user-images.githubusercontent.com/57740421/196224789-a7403170-7bdd-4266-aa98-c493a06df202.png)


Dari visualisasi proses training model di atas cukup smooth dan model konvergen pada epochs sekitar 100. Dari proses ini, saya memperoleh nilai error akhir sebesar sekitar 0.19 dan error pada data validasi sebesar 0.20.

Referensi:

[1] [Recommender System for Movielens Datasets using an Item-based Collaborative Filtering in Python](https://www.scipublications.com/journal/index.php/ijmebac/article/view/340)

[2] [Employing opposite ratings users in a new approach to collaborative filtering](https://ijeecs.iaescore.com/index.php/IJEECS/article/viewFile/24894/15925)

[3] [The MovieLens Datasets: History and Context](https://dl.acm.org/doi/10.1145/2827872)

[4] [Movielens Dataset](https://www.kaggle.com/datasets/ayushimishra2809/movielens-dataset)

