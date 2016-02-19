## fbWordCounter 
is an utility to count particular words in facebook messages. It operates on a file __messages.htm__, which you can get from [facebook.com/settings](http://facebook.com/settings). 

![fbWordCounter interface](https://github.com/czeslavo/fbWordCounter/blob/master/fbWordCounter/fbwc.png?raw=true) 

### usage
You need to have PyQt4 installed. 
In root directory:
```
sudo python setup.py install
```
In directory which includes messages.htm
```
fbwc
```

If your files is huge, you will have to wait until it's parsed. Later, you can enter your and your friend's name, the words you would like to count in your conversations (separated with semicolon) and click __count__ button. The output (occurences per particular month) will appear in the text box.


  
