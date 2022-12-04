for x in *_library.py
do
    y=$(echo $x | cut -d '_' -f1)
    echo $y"_library.py"
done