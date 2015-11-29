Clothing Recommender  
====================  
  
# サンプル（プロダクト名）  
## 製品概要  
その日の予定に合わせて着ていく服を推薦するアプリ  
  
  
## 使い方  
### クローゼットをつくる  (初回使用時のみ)  
アプリを起動したら、まずはあなた専用のクローゼットを用意します。  
あなたが持っている服の画像をシステムに登録してください。  
あなた専用のクローゼットがアプリ内に作成されます。  
  
### 服を選んでもらおう  
朝起きたら、アプリを開いてその日の予定を入力してください。  
アプリがあなたに最適な服をあなたのクローゼットの中から選んでくれます。  
  
  
### 背景  
#### 開発したきっかけ  
##### 日々の悩みを解決したかった  
お店で売っている商品から選ぶのは楽しくても、いざ着ようとすると...    
天気も予定も考えないといけないし..... 自分の持っている服から選ぶのは大変     
今日はこのシャツが一番いいけど、おとといも着たし....    
  
どの服を着て行こうか迷うこと、ありますよね。  
しかも人によってはほぼ毎日迷ってしまう。  
  
この悩みを解決するために服を推薦するアプリケーションを開発しようと考えた。  
  
##### 研究分野としても面白い  
アルゴリズム部分の開発者(石田)は非常に機械学習が好きで、機械学習アルゴリズムを実装することや機械学習を用いてアプリケーションを作ることを楽しいと感じている。  
  
この課題は入力を予定、出力を服とした推薦モデルを構築することで解決することができるうえ、独自のモデル設計を必要とする。ライブラリやAPIのラッパーを作るだけでは解決できないという意味で非常に興味深い課題であったため取り組もうと思った。  
  
#### 課題  
システム内部に関する課題は下記  
ユーザーに特徴抽出　の領域を選んでもらわなければならない  
  
  
### 製品説明（具体的な製品の説明）  
### 特長  
朝起きたときに「どの服を着ていこうか」と悩むことが多い人に利用してもらいたいアプリケーションである。  
####1. 特長1  
ショッピングに出かけたいときにはおしゃれな服を、博物館などのフォーマルな雰囲気の場所に行くときにはフォーマルな服を提示することができる。  
####2. 特長2  
気温も同時に考慮して服を推薦してくれるため「暖かい部屋で服を着て、いざ出発してみたら意外と寒かった！」といった経験を減らすことができる。  
  
  
### 今後の展望  
服の範囲を自動的に判別する  
  
### 注力したこと  
* 学習モデルの設計と特徴量の設計  
  
  
## 開発技術  
### 推薦アルゴリズム全体の流れ  
本アプリが実装すべき機能は大きく分けて以下の2つである。  
  
1. ユーザーの服をデータベースに登録すること  
2. アプリをした日のユーザーの予定とその日の気温を考慮して服を推薦すること   
  
つまり、ユーザーの予定とその日の気温から、その日ユーザーが着るべき服へのマップを作ることが求められる。  
  
このマップを大きく2つの部分に分ける。  
1. ユーザーの予定から服の特徴量へのマップ  
2. 1で出力された特徴量に最も近い特徴を持った服へのマップ  
  
言い換えると  
1. 予定から「今日は寒いから分厚い服がいいかな」「博物館に行くからフォーマルな感じの服が欲しい」という、着るべき服のだいたいのイメージを作る  
2. 1で作ったイメージに最もよく当てはまる服をユーザーのクローゼットから選び出す  
という2段階に分けられる。  
  
次に、1と2それぞれのマップの内容と、服の特徴量についてより詳細に述べる。  
  
  
  
#### 1. ユーザーの予定から服の特徴量へのマップ  
ここでは「ユーザーの予定と気温」という情報をまとめて「シチュエーション」という単語で扱うこととする。  
  
シチュエーションと服の特徴量を多次元のベクトルで表現すると、シチュエーションから服の特徴量へのマップは多次元ベクトルから多次元ベクトルへのマップとみなすことができる。  
  
シチュエーションとそれに合致する服の特徴量を大量に用意し、RandomForest回帰モデルを学習させることでこのマップを実現した。  
  
  
#### 2. 1で出力された特徴量に最も近い特徴を持った服へのマップ  
上のRandomForestによって出力された特徴量に最も近い特徴量を保持している服を検索する。これはKNN(k-nearest-neighbors)を使えば高速に実行することができる。  
  
  
### 服の特徴量をどうするか  
気温や予定と関連が見られる(有意な)特徴量は、服が長袖かどうか、生地が分厚いかどうかなどによって判定できるが、長袖かどうかを判定するには一般物体認識の技術が必要であり、モデルの学習コストが非常に高くなってしまう。そこで、本アプリでは、生地の分厚さと素材を特徴量としている。  
フォーマルな場ではスーツやコートに近い素材の生地を、そうでない場合はTシャツのような軽い生地の服を選ぶ傾向にある。また、生地の素材は表面の質感に直結することから、特徴量にはテクスチャ特徴量(LBP)を用いた。  
  
### 活用した技術  
モデルにはRandom Forestによる回帰とKNN(k-nearest neighbor search)を用いている。  
[KNN(k-nearest neighbor search)](http://scikit-learn.org/stable/modules/neighbors.html)  
[RandomForest](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html)  
  
### 前処理  
ユーザーが自分の服をデータベースに登録するときの周辺環境はさまざまに変化する。昼間カーテンを開けた部屋、日光の差し込む環境で服を登録することもあれば、夜遅くにアプリの存在を知り、比較的暗い部屋でアプリを起動して服を登録することも考えられる。  
さまざまな環境での利用に対応するため、どんな環境で服の写真を撮っても同じ結果が表示されるようにしなければならない。このため、ユーザーが登録しようとしている画像の輝度を正規化する必要がある。本アプリでは輝度の正規化に[Histogram Equalization](scikit-image.org/docs/dev/auto_examples/plot_equalize.html)を用いた。  
  
### 特徴量  
上記のとおり、服の特徴量には[LBP(Local Binary Pattern)](http://scikit-image.org/docs/dev/auto_examples/plot_local_binary_pattern.html)を用いている。  
  
#### API・データ  
* 学習用のデータセットには[ClothingAttributeDataset](http://web.stanford.edu/~hchen2/datasets.html#clothingattributedataset)を用いた。  
  
#### フレームワーク・ライブラリ・モジュール  
* [scikit-image](http://scikit-image.org/)  
画像の前処理と特徴抽出を行う際に利用した。  
  
* [scikit-learn](http://scikit-learn.org/)  
学習モデルはscikit-learn内に含まれているアルゴリズムの組み合わせで構築されている。  
  
  
  
#### ハッカソンで開発した独自機能・技術  
### 独自技術  
#### 先行研究や既存の製品との比較  
[Magic Closet](http://www.lv-nus.org/papers/2012/magic_closet-MM12.pdf)  
[Style Casters](http://techcrunch.com/2009/10/06/geo-fashion-comes-to-the-iphone-with-stylecasters-clothing-recommendation-app)
  
  
  
#### 製品に取り入れた研究内容（データ・ソフトウェアなど）  
##### 学習モデル  
* RandomForestによる回帰  
* KNN(k-nearest-neighbors)による高速な特徴検索  
  
##### 服の特徴量  
* LBP特徴量  

