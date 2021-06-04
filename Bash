gpio -g mode 1 out
gpio -g mode 2 out
num=0 

while[ $num -le 19]
do
        /usr/bin/gpio -g toggle 1
	/usr/bin/gpio -g toggle 2
        sleep .5
	let "num += 1"
	echo"$num"
done
gpio -g write 1 0 
gpio -g write 2 0 
