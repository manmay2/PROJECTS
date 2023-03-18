# WELCOME TO THE HTML CREATOR WHICH WILL HELP US TO GENERATE CODE FOR HTML AND CSS

lorem=''

def insert(bas,add,ini):
	add=add[::-1]
	for i in add:

		bas.insert(bas.index(ini)+1,i)

def p_(bas,ini,f2,css_bas):	
	add=['<p>\n','Sample Text Starts here............','</p>\n']
	insert(bas,add,ini)
	ini='</p>\n'
	css_bas.insert(0,'.p\n')		
	f2.writelines(css_bas)
	css_bas.remove('.p\n')
def img_(bas,ini,f2,css_bas):
	# src=input("ENTER THE IMAGE'S FILENAME : ")
	# height=int(input("ENTER THE HEIGHT OF THE IMAGE : "))
	# width=int(input("ENTER THE WIDTH OF THE IMAGE : "))
	# alt=input("ENTER THE ALTERNATING MESSAGE INCASE IF IMAGE ISN'T DISPLAYED")
	add=["<img src=xyz.jpg,height=123,width=123,alt='SAMPLE GOES HERE.....'>\n"]
	insert(bas,add,ini)
	ini=add[0]
	css_bas.insert(0,'.img\n') 
	f2.writelines(css_bas)
	css_bas.remove('.img\n')
def hx_(bas,ini,f2,css_bas):
	# x=input("ENTER THE HEADING TAG FROM 1-6 : ")

	add=['<h1>\n',lorem,'</h1>\n']
	insert(bas,add,ini)
	ini='</h1>\n'

	css_bas.insert(0,'.h1\n')
	f2.writelines(css_bas)
	css_bas.remove('.h1\n')
def sup_(bas,ini,sup,f2,css_bas):
	if(sup=='<sub>'):
		add=['<sub>\n','Sample Text Starts here............\n','</sub>\n']
		insert(bas,add,ini)
		ini='</sub>\n'
		css_bas.insert(0,'.sub\n')
		f2.writelines(css_bas)
		css_bas.remove('.sub\n')
	elif(sup=='<sup>'):
		add=['<sup>\n','Sample Text Starts here............\n','</sup>\n']
		insert(bas,add,ini)
		ini='</sup>\n'
		css_bas.insert(0,'.sup\n')
		f2.writelines(css_bas)
		css_bas.remove('.sup\n')
			

def ol_(bas,ini,f2,css_bas):
	add=['<ol type=' '>\n','</ol>\n']
	insert(bas,add,ini)
	ini='<ol type=' '>\n'
	css_bas.insert(0,'.ol\n')
	f2.writelines(css_bas)
	css_bas.remove('.ol\n')
def li_(bas,ini,f2,css_bas):
	add=['<li>\n',lorem,'\n','</li>\n']
	insert(bas,add,ini)
	css_bas.insert(0,'.li\n')
	f2.writelines(css_bas)
	css_bas.remove('.li\n')																								
def ul_(bas,ini,f2,css_bas):
	add=['<ul style=' '>\n','</ul>\n']
	insert(bas,add,ini)
	ini='<ul style=' '>\n'
	css_bas.insert(0,'.ul\n')
	f2.writelines(css_bas)
	css_bas.remove('.ul\n')
def main():
	title_=input("[*] ENTER THE TITLE OF THE DOCUMENT : ")
	file_html=input("[*] ENTER THE FILENAME FOR THE HTML TEMPLATE : ")
	file_css=input("[*] ENTER THE FILENAME FOR THE CSS TEMPLATE : ")
	file_js=input("[*] ENTER THE FILENAME FOR THE JAVASCRIPT FILE :  ")
	global lorem
	with open(file_html,'w') as f1:
		with open(file_css,'w') as f2: 
			with open(file_js,'w') as f3:
				p=input("[*] DO YOU WANT TO ADD PARAGRAPH TAG : Y/N : ").upper()
				img=input("[*] DO YOU WANT TO ADD IMAGE TAG : Y/N : ").upper()
				H=input("[*] DO YOU WANT TO ADD HEADER  TAG : Y/N : ").upper()
				sup=input("[*] DO YOU WANT TO ADD SUPERSCRIPT/SUBSCRIPT TAG , enter the tag name in the tag format : ")
				ol=input("[*] DO YOU WANT TO ADD ORDER LISTS : Y/N : ").upper()
				ul=input("[*] DO YOU WANT TO ADD UNORDER LISTS : Y/N : ").upper()
				ini='<body>\n' 
				lorem='Lorem ipsum dolor sit amet consectetur adipisicing elit. Perspiciatis nobis doloremque exercitationem eveniet nesciunt at. Voluptates provident vero amet vel omnis excepturi delectus autem accusamus voluptatibus perferendis quasi, debitis quaerat inventore blanditiis eum quis. In quisquam accusantium iusto natus illo possimus ducimus voluptates fugiat, adipisci enim est ullam ut perspiciatis quod officia aliquid praesentium repellat omnis dolor perferendis quia ipsam veritatis commodi reiciendis. Ex, voluptate libero. Non quod recusandae, dicta aliquam reprehenderit saepe cumque minus mollitia eveniet ipsa vitae nesciunt quos fugit! Nisi debitis velit inventore quas obcaecati fugiat doloribus mollitia. Saepe, ratione nostrum aspernatur amet maxime, iusto eius natus aliquid adipisci maiores itaque doloremque quam vero nulla labore cum ipsam non omnis repellat error illo quibusdam nam necessitatibus ipsum. Repellendus eligendi non eum. Quia optio vitae perspiciatis architecto nulla fugit recusandae assumenda illum adipisci eum quasi id, autem dolore quisquam pariatur culpa temporibus maiores ratione nihil. Tempora, quos laborum. Reprehenderit libero exercitationem id! Quidem pariatur nisi blanditiis ipsum ex illum maxime voluptatibus voluptas corrupti dolor maiores placeat, explicabo soluta doloribus itaque exercitationem. Omnis a minus expedita aliquam voluptate odit. A sit vel nisi laudantium enim inventore, maxime commodi adipisci illum natus, voluptate eos dolore atque similique deleniti quia explicabo?'
				bas=['<!DOCTYPE html>\n','<html lang="en">\n','<head>\n','    <meta charset="UTF-8">\n',
				'    <meta http-equiv="X-UA-Compatible" content="IE=edge">\n',
				'    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n',f'    <title>{title_}</title>\n',f'<link rel="stylesheet" href={file_css}></head>\n',
				'<body>\n','</body>\n','</html>']
				css_bas=["{\n","color : 'Blue';\n","font-size : 50px';\n","font-family : 'Times New Roman',Times,Serif;\n","background_color : 'Green';\n","background-image : 'src.jpg';\n","background : url(src.jpg);\n","background-size : 300px 100px;\n","background-repeat : no-repeat;\n","}\n"]
				if(p=='Y'):
					p_(bas,ini,f2,css_bas)
					
					
				if(img=='Y'):
					img_(bas,ini,f2,css_bas)
					
				if(H=='Y'):
					hx_(bas,ini,f2,css_bas)

				if(sup=='<sup>' or sup=='<sub>'):
					sup_(bas,ini,sup,f2,css_bas)
				if(ol=='Y'):
					ol_(bas,ini,f2,css_bas)
					li_(bas,ini,f2,css_bas)
					ini='</ol>\n'
				if(ul=='Y'):
					ul_(bas,ini,f2,css_bas)
					li_(bas,ini,f2,css_bas)
					ini='</ul>\n'
				
				f1.writelines(bas)
main()

