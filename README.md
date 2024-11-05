# stGUI (under developing)
This is for controlling the power supplys of the steering magnets@R3.<br>
The model of the power supplys are ZX-S800 LAN (Takasago).<br>
<br>
Used libraries;<br>
&ensp;tkinter >> GUI<br>
&ensp;paramiko >> ssh<br>
&ensp;time >> sleep<br>
&ensp;threading >> threading<br>
<br>
Code structure;<br>
&ensp;main.py >> main, run this code<br>
&ensp;variables.py >> prepare variables<br>
&ensp;knobs.py >> make window and set labels, text boxes, and buttons<br>
&ensp;connect_ssh.py >> function to connect the power supplys with SSH<br>
&ensp;activate.py >> connect and activate the power supplys<br>
&ensp;output.py >> make the power supplys on<br>
&ensp;read.py >> read and show current, voltage, and output status<br>
&ensp;set.py >> set current and reflect the value to text boxes<br>
&ensp;OneSec.py >> run read.py in every 1 seconds<br>
&ensp;beforeClose.py >> prevent to close the window when current is NOT zero<br>