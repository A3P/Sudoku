# !/bin/bash

rm timeList.txt
rm basicTaskOut.txt

line=2
for grid in {1..50}
do
    echo "Grid $((grid))" >> basicTaskOut.txt
    sed -n $((line)),$((line + 8))p basicTaskIn.txt > grid.txt
    python3 sud2sat.py grid.txt > sat.txt
    minisat sat.txt solution.txt | grep CPU > time.txt
    python3 sat2sud.py solution.txt >> basicTaskOut.txt
    cat time.txt >> basicTaskOut.txt
    echo $'\n' >> basicTaskOut.txt
    cat time.txt >> timeList.txt
    line=$((line+10))
done
python3 avgtime.py < timeList.txt >> basicTaskOut.txt
