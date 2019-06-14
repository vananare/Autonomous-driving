#!/bin/bash
# My first script

#export PYTHONPATH="$PYTHONPATH:/home/xr-10/Carla-9.5/PythonAPI:/home/xr-10/Carla-9.5/PythonAPI:/home/xr-10/Carla-9.5/PythonAPI/Training:/home/xr-10/anaconda3/envs/carla_driver/lib/python27.zip:/home/xr-10/anaconda3/envs/carla_driver/lib/python2.7:/home/xr-10/anaconda3/envs/carla_driver/lib/python2.7/plat-linux2:/home/xr-10/anaconda3/envs/carla_driver/lib/python2.7/lib-tk:/home/xr-10/anaconda3/envs/carla_driver/lib/python2.7/lib-old:/home/xr-10/anaconda3/envs/carla_driver/lib/python2.7/lib-dynload:/home/xr-10/.local/lib/python2.7/site-packages:/home/xr-10/anaconda3/envs/carla_driver/lib/python2.7/site-packages:carla/dist/carla-0.9.5-py2.7-linux-x86_64.egg:carla"
sudo echo "Fetching root priveliged"
for i in {1..401} 
do
	echo "Starting Carla"
	DISPLAY= ../CarlaUE4.sh /Game/Carla/Maps/Town01 & -benchmark -fps=60 & 
	pid=$!	
	sleep 10

	echo "Carla PID: $pid"
	echo "#############################################################################################"
	echo "#############################################################################################"
	echo "#############################################################################################"
	echo "#############################################################################################"
	echo ""
	echo "------------------------     Iteration $i out of 400     ------------------------------------"
	echo ""
	echo "#############################################################################################"
	echo "#############################################################################################"
	echo "#############################################################################################"
	echo "#############################################################################################"
	echo "starting recorder"
	python2 recorder_trimmed.py --path Training_data_temp #> output_log/stdoutrecorder$i.txt 2> output_log/stderrecorder$i.txt & 
	echo "killing Carla"
	kill -SIGINT $pid
	sudo fuser -k -n tcp 2000
done

