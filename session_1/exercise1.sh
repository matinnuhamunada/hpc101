MY_DIR="/scratch/he61/$USER/mydir"
mkdir -p $MY_DIR
touch $MY_DIR/myfile.txt
echo $MY_DIR/"your text" > myfile.txt
ls $MY_DIR