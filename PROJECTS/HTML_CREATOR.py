# WELCOME TO THE HTML CREATOR WHICH WILL HELP US TO GENERATE CODE FOR HTML AND CSS
# file_name=input("ENTER THE HTML FILE NAME : ")

# p_=input("DO YOU WANT TO ADD PARAGRAPH TAG : Y/N : ")
# img_=input("DO YOU WANT TO ADD IMAGE TAG : Y/N : ")
# H_=input("DO YOU WANT TO ADD HEADER  TAG : Y/N : ")
# sup_=input("DO YOU WANT TO ADD SUPERSCRIPT TAG : Y/N : ")
# sub_=input("DO YOU WANT TO ADD SUBSCRIPT TAG : Y/N : ")
# ol_=input("DO YOU WANT TO ADD ORDER LISTS : Y/N : ")
# ul_=input("DO YOU WANT TO ADD UNORDER LISTS : Y/N : ")

def p_(bas,ini):
	add=['<p>','Sample Text Starts here............','</p>']
	bas.insert(bas.index(ini)+1,add)
	ini='<p>'
def img_(bas,ini):
	# src=input("ENTER THE IMAGE'S FILENAME : ")
	# height=int(input("ENTER THE HEIGHT OF THE IMAGE : "))
	# width=int(input("ENTER THE WIDTH OF THE IMAGE : "))
	# alt=input("ENTER THE ALTERNATING MESSAGE INCASE IF IMAGE ISN'T DISPLAYED")
	add=["<img src=xyz.jpg,height=123,width=123,alt='SAMPLE GOES HERE.....'"]
	bas.insert(bas.index(ini)+1,add)
	ini=add
def h1_(bas,ini):
	add=['<h1>','Sample Text Starts here............','</h1>']
	bas.insert(bas.index(ini)+1,add)
	ini='<h1>'
def h2_(bas,ini):
	add=['<h2>','Sample Text Starts here............','</h2>']
	bas.insert(bas.index(ini)+1,add)
	ini='<h2>'
def h3_(bas,ini):
	add=['<h3>','Sample Text Starts here............','</h3>']
	bas.insert(bas.index(ini)+1,add)
	ini='<h3>'
def h4_(bas,ini):
	add=['<h4>','Sample Text Starts here............','</h4>']
	bas.insert(bas.index(ini)+1,add)
	ini='<h4>'
def h5_(bas,ini):
	add=['<h5>','Sample Text Starts here............','</h5>']
	bas.insert(bas.index(ini)+1,add)
	ini='<h5>'
def h6_(bas,ini):
	add=['<h6>','Sample Text Starts here............','</h6>']
	bas.insert(bas.index(ini)+1,add)
	ini='<h6>'
def sup_(bas,ini):
	add=['<sup>','Sample Text Starts here............','</sup>']
	bas.insert(bas.index(ini)+1,add)
	ini='<sup>'
def sub_(bas,ini):
	add=['<sub>','Sample Text Starts here............','</sub>']
	bas.insert(bas.index(ini)+1,add)
	ini='<sub>'
def ol_(bas,ini):
	add=['<ol type=' '>','</ol>']
	bas.insert(bas.index(ini)+1,add)
	ini='<ol type=' '>'
def li_(bas,ini):
	add=['<li>     ','<li>      ']
	bas.insert(bas.index(ini)+1,add)
	ini='' 																										# DOUBT
def ul_(bas,ini):
	add=['<ul style=' '>','</ul>']
	bas.insert(bas.index(ini)+1,add)
	ini='<ul style=' '>'
def main(bas,file_name,ini):
	with open('INDEX.HTML','w') as f1:
		#basic doctype
		bas=['<!DOCTYPE html>','<html lang="en">','<head>','    <meta charset="UTF-8">',
		'    <meta http-equiv="X-UA-Compatible" content="IE=edge">',
		'    <meta name="viewport" content="width=device-width, initial-scale=1.0">','    <title>Document</title>','</head>',
		'<body>','</body>','</html>']
		for i in bas:
			f1.writelines(i+'\n')
		
	
