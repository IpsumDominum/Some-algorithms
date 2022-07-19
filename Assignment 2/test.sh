#g++ tree.cpp -o tree
#./tree < test.script
#./tree < data/trees_in.txt > out.txt
#python tree.py < test.script
#python3 color.py < data/tparse_pw_in.txt > out.txt
#diff out.txt data/tparse_pw_out.txt

python3 color.py < data/tparse_tw_in.txt > out.txt
diff out.txt data/tparse_tw_out.txt