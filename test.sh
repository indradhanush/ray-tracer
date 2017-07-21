rm image100.jpg
rm image200.jpg
rm image500.jpg
rm image750.jpg
rm image1000.jpg

python run.py 100 && open image100.jpg &
python run.py 200 && open image200.jpg &
python run.py 500 && open image500.jpg &
python run.py 750 && open image750.jpg &
python run.py 1000 && open image1000.jpg
