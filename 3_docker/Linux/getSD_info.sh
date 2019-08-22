
#!/bin/bash
VAR=$(df /media/sd/ 2>/dev/null)
COUNT=$(df /media/sd/ 2>/dev/null | wc -c)
#COUNT=$($VAR | wc -c)
#echo $COUNT
#if [ "$VAR" != " " ];
if [ $COUNT -le 100 ];
then echo "SD ist nicht da"
else echo "SD ist da"
fi

#echo
#echo $VAR | wc -c
#echo $VAR


#SD Karten Größe abfragen
df /media/sd/ | cut -c 41-50 | cut -dA -f1