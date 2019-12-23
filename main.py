import json
import mysql.connector
from mysql.connector import Error

user=""
score=0

def getStudent():
	name="";
	adr="";
	city="";
	state="";
	email="";
	phno="";
	name=input("Enter Your Name ");
	adr=input("Enter your address ");
	city = input("Enter your City ");
	state=input("Enter State ");
	email=input("Enter your email ");
	phno = input("Enter your Phone Number ");

	try:
		connection = mysql.connector.connect(host='localhost',database='quiz', user='root', password='');
		query="insert into	userprofile values(%s,%s,%s,%s,%s,%s)";
		args=(name,adr,city, state, email, phno);

		cursor = connection.cursor();
		cursor.execute(query,args);
	except Error as error:
		print(error)
	
def updateProfile(user):
	try:
		connection = mysql.connector.connect(host='localhost',database='quiz', user='root', password='');
		query="select * from Profile where "
	except Error as error:
		print(error)

def login():
	try:
		username=input("Enter your Username : ")
		password=input("Enter your Password : ")
		connection = mysql.connector.connect(host='localhost',database='quiz', user='root', password='');
		query="select * from useracc where username='"+username+"' and password='"+password+"'";
		cursor =connection.cursor();
		cursor.execute(query);
		data=cursor.fetchall();
		count=cursor.rowcount;
		
		if(count==1):
			print("Valid User....", query)
			global user
			user=username
			return True
		else:
			print("-------------- Invalid User ------------",query)
			return False
		
	except Error as error:
		print(error)

def showStudent():
	try:
		connection = mysql.connector.connect(host='localhost',database='quiz', user='root', password='');
		query="select * from userprofile";
		cursor =connection.cursor();
		cursor.execute(query);
		data=cursor.fetchall();

		for row in data:
			print("============================================")
			print("            User Data  	")
			print("============================================")
			print("Name is : ",row[0]);
			print("Address is : ",row[1])
			print("City is : ",row[2])
			print("State is : ",row[3])
			print("Email is : ",row[4])
			print("Phone number is : ",row[5])
			print("============================================")
			input("Press any key to cont......")
	except Error as error:
		print(error)


def insertResult(username, marks):
	try:
		connection = mysql.connector.connect(host='localhost',database='quiz', user='root', password='');
		query="insert into	results(username, score) values(%s,%s)";
		args=(username, marks);

		cursor = connection.cursor();
		cursor.execute(query,args);
	except Error as error:
		print(error)


def takeQuiz():
	try:
		connection = mysql.connector.connect(host='localhost',database='quiz', user='root', password='');
		query="select * from questions";
		cursor =connection.cursor();
		cursor.execute(query);
		data=cursor.fetchall();
		for row in data:
			print("============================================")
			print("            Quiz  	")
			print("============================================")
			print("Q. : ",row[1]);
			print("Choice A. : ",row[2])
			print("Choice B. : ",row[3])
			print("Choice C. : ",row[4])
			print("Choice D. : ",row[5])
			ans=input("Enter Your Answer A, B, C, D : ")
			if(ans==row[6]):
				global score
				score=score+1;

			print("============================================")
			input("Press any key to cont......")
		print("Thanks for Taking Quiz. Your Score is : ",score)
		insertResult(user,score);
	except Error as error:
		print(error)

def seeAllResult():
	try:
		connection = mysql.connector.connect(host='localhost',database='quiz', user='root', password='');
		query="select * from results";
		cursor =connection.cursor();
		cursor.execute(query);
		data=cursor.fetchall();
		for row in data:
			print("============================================")
			print("            All Results  	")
			print("============================================")
			print("Name : ",row[0]);
			print("Score : ",row[1])
			print("Test Date : ",row[2])
			print("============================================")
			input("Press any key to cont.......");
			
	except Error as error:
		print(error)


def userResult(user):
	print("============================================")
	print("            User Results  	")
	print("============================================")
	try:
		connection = mysql.connector.connect(host='localhost',database='quiz', user='root', password='');
		query="select * from results where username='"+user+"'";
		cursor =connection.cursor();
		cursor.execute(query);
		data=cursor.fetchall();
		count=cursor.rowcount;
		if(count<1):
			print("Sorry You have not attented any quiz yet ");
			input()
		else:
			for row in data:
				print("============================================")
				print("------------------> Results <------------	")
				print("============================================")
				print("Name : ",row[0]);
				print("Score : ",row[1])
				print("Test Date : ",row[2])
				print("============================================")
				input("Press any key to cont.......");
				
	except Error as error:
		print(error)

def createQuiz():
	print("============================================")
	print("            Create Quiz Section  	")
	print("============================================")
	que=input("Enter Question ")
	ans1=input("A choice : ")
	ans2=input("B choice : ")
	ans3=input("C choice : ")
	ans4=input("D choice : ")
	cans=input("Correct ans A B C or D : ")
	try:
		connection = mysql.connector.connect(host='localhost',database='quiz', user='root', password='');
		query="insert into	questions(que, ans1, ans2, ans3, ans4, cans) values(%s,%s,%s,%s,%s,%s)";
		args=(que,ans1,ans2, ans3,ans4, cans);

		cursor = connection.cursor();
		cursor.execute(query,args);
		print("----------------------> Question added successfully <----------------------")
	except Error as error:
		print(error)
	
		
def header():
	print("=========================================================")
	print("                 Student Quiz System  	")
	print("                 Test Your Knowledge      ");
	print("=========================================================")
	print("Session : 2019                     Mode : Computer Based ")
	print("=========================================================")
	

def quit():
	print("=========================================================")
	print("                 Student Quiz System  	")
	print("                 Test Your Knowledge      ");
	print("=========================================================")
	print("Session : 2019                     Mode : Computer Based ")
	print("=========================================================")
	print("\n\n\nThanks for Using our Quiz.!! Hope you Enjoy It.")
	print("=========================================================")
	input();

def menuStudent():
	stuch=0;
	if(login()):
		while(stuch!=4):
			print("Welcome User : ",user)
			print("\n1. Profile");
			print("\n2. Take Quiz");
			print("\n3. Result");
			print("\n4. Back");
			stuch=int(input("Enter Your Choice "));
			if( stuch==1):
				getStudent();
			if(stuch==2):
				takeQuiz();
			if(stuch==3):
				#global user
				userResult(user);
	else:
		print(" ------------> Invalid User Details <------------------")

def createUser():
	username=input("Enter Username : ")
	password=input("Enter Password : ")
	cpass=input("Confirm Passwowrd : ")
	if(password==cpass):
		try:
			connection = mysql.connector.connect(host='localhost',database='quiz', user='root', password='');
			query="insert into	useracc(username, password) values(%s,%s)";
			args=(username, cpass);

			cursor = connection.cursor();
			cursor.execute(query,args);
		except Error as error:
			print(error)
	else:
		print("Password and Confirm Password should be Same : ")

def allQuestions():
	try:
		connection = mysql.connector.connect(host='localhost',database='quiz', user='root', password='');
		query="select * from questions";
		cursor =connection.cursor();
		cursor.execute(query);
		data=cursor.fetchall();

		for row in data:
			print("============================================")
			print("            All Questions  	")
			print("============================================")
			print("Question Id is : ",row[0]);
			print("Question is : ",row[1])
			print("Choice A is : ",row[2])
			print("Choice B is : ",row[3])
			print("Choice C is  : ",row[4])
			print("Choice D is : ",row[5])
			print("Correct ans is : ",row[6])
			print("============================================")
			input("Press any key to cont......")
	except Error as error:
		print(error)

def deleteQuestion():
	qid=(input("Enter Question id "))
	try:
		connection = mysql.connector.connect(host='localhost',database='quiz', user='root', password='');
		query="delete from questions where qid="+qid;
		cursor =connection.cursor();
		cursor.execute(query);
	except Error as error:
		print(error)

def deleteUser():
	uid=(input("Enter Username "))
	if(uid==user):
		print("You cannot delete Yourself : ")
	else:
		try:
			connection = mysql.connector.connect(host='localhost',database='quiz', user='root', password='');
			query="delete from useracc where username='"+uid+"'";
			print(query)
			cursor =connection.cursor();
			cursor.execute(query);
		except Error as error:
			print(error)

def admin():
	adminch=0
	if(login()):
		while(adminch!=8):
			print("\n1. Add New Questions");
			print("\n2. View Students");
			print("\n3. View Results");
			print("\n4. Create New User ")
			print("\n5. List all Questions ")
			print("\n6. Delete Questions ")
			print("\n7. Delete User ")
			print("\n8. Back");
			adminch=int(input("Enter your choice : "))
			if(adminch==1):
				createQuiz();
			if(adminch==2):
				showStudent();
			if(adminch==3):
				seeAllResult();
			if(adminch==4):
				createUser();
			if(adminch==5):
				allQuestions();
			if(adminch==6):
				deleteQuestion();
			if(adminch==7):
				deleteUser();

def logout():
	user="";

def interface():
	ch=0;
	while(ch!=3):
		header();
		print("\n1. Admin");
		print("\n2. Student");
		print("\n3. Quit");
		ch=int(input("Enter Your Choice : "));
		if(ch==1):
			admin();
		elif(ch==2):
			menuStudent();
		else:
			quit();


interface();