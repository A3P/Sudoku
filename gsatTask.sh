# !/bin/bash

rm timeList.txt
rm basicTaskOut.txt
rm task1Output.txt

line=2
for grid in {1..50}
do
echo "Grid $((grid))" >> basicTaskOut.txt
sed -n $((line)),$((line + 8))p basicTaskIn.txt > grid.txt
python3 sud2sat.py grid.txt -gsat > sat.txt

#Gsat/gsat sat.txt solution.txt | grep CPU > time.txt
Gsat/make
Gsat/gsat <<eof
sat.txt
solution2.txt
report.txt



eof

    python3 sat2sud.py solution2.txt >> basicTaskOut.txt
    cat time.txt >> basicTaskOut.txt
    echo $'\n' >> basicTaskOut.txt
    cat time.txt >> timeList.txt
    line=$((line+10))
done
python3 avgtime.py < timeList.txt >> basicTaskOut.txt

rm timeList.txt
for grid in {1..95}
do
    echo "Grid $((grid))" >> task1Output.txt
    sed -n $((grid))p task1Input.txt > grid.txt
    python3 sud2sat.py grid.txt -gsat > sat.txt
    Gsat/gsat sat.txt solution2.txt | grep CPU > time.txt
    python3 sat2sud.py solution2.txt >> task1Output.txt
    cat time.txt >> task1Output.txt
    echo $'\n' >> task1Output.txt
    cat time.txt >> timeList.txt
done
python3 avgtime.py < timeList.txt >> task1Output.txt
