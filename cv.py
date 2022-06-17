import os.path
import re
import docx2txt
import PyPDF2
from pdf2docx import Converter

def file_input():
 resume=input("enter the resume path: ")
 name,extension=os.path.splitext(resume)
 if extension=="":
    print("please mention the type of file along with the resume path: ",file_input())
 else:
    path_list=name.split( "\\" )
    file_name=path_list[len(path_list)-1]
    print("File name: ",file_name)
    print("extention of the file:",extension)
    file_type(extension,name,resume,file_name)

def resume_scorer_txt(text,resume_txt,file_name):
    email=re.findall(r"[a-zA-Z0-9\.\-+_]+@[a-zA-Z0-9\.\-+_]+\.[a-z]+",text)
    if len(email) == 0:
        print("email address is not found, resume FAILED(rejected)")
    else:
        print("Email: ", email[0])
        skilss = []
        for i in resume_txt:
            temp = re.sub("[^a-zA-Z0-9]", "", i)
            if temp.lower() in ["xml", "html", "javascript", "css3", "css", "python"]:
                skilss.append(temp.lower())

        print("Resume score: ", len(set(skilss)))
        print("Skills found: ", sorted(set(skilss)))
        store = open("cv_data_file.txt", "a")
        if len(skilss)==0:
            store.write("File_name: "+file_name+ ", " + "email: " + email[0] + ", " + "skills: " + "[No skills]" + "\n")
            store.close()
        else:
            store.write("File_name: "+file_name+ ", " + "email: " + email[0] + ", " + "skills: " + str(sorted(set(skilss))) + "\n")
            store.close()

        if len(set(skilss)) > 5:
            print("resume status: PASS")
            passed_cv = open("passed_cv_datafile.txt", "a")
            passed_cv.write("File_name: "+file_name+ ", " + "email :" + email[0] + ", " + "skills: " + str(sorted(set(skilss))) + "\n")
            passed_cv.close()
        else:
            print("resume status: FAIL")

def resume_scorer_doc(text,resume_txt,file_name):
 email = re.findall(r"[a-zA-Z0-9\.\-+_]+@[a-zA-Z0-9\.\-+_]+\.[a-z]+", text)
 # pattern=re.compile(r"^\d{3}-\d{3}-\d{4}$")
 # phone_no=re.findall(pattern,text)
 # print(phone_no)
 if len(email)==0:
     print("email address is not found,resume FAILED(rejected)")
 else:
  print("Email: ", email[0])

  skilss=[]
  for i in resume_txt.split():
     temp=re.sub("[^a-zA-Z0-9]","",i)
     required_skils=["xml","html","javascript","css3","css","python","java","angular","bootstrap","jquery"]
     if temp.lower() in required_skils:
         skilss.append(temp.lower())
  print("Resume score: ",len(set(skilss)))
  print("Skills found: ",sorted(set(skilss)))
  store=open("cv_data_file.txt","a")
  if len(skilss) == 0:
      store.write("File_name: "+file_name+ ", " + "email: " + email[0] + ", " + "skills: " + "[No skills]" + "\n")
      store.close()
  else:
      store.write("File_name: "+file_name+ ", " + "email: " + email[0] + ", " + "skills: " + str(sorted(set(skilss))) + "\n")
      store.close()

  if len(set(skilss))>5:
     print("resume status: PASS")
     passed_cv = open("passed_cv_datafile.txt", "a")
     passed_cv.write("File_name: "+file_name+ ", " + "email: " + email[0] + ", " + "skills: " + str(sorted(set(skilss))) + "\n")
     passed_cv.close()
  else:
     print("resume status: FAIL")

def file_type(extension,name,resume,file_name):
 resume_txt=[]
 if extension==".txt":
    file=open(resume,"r")
    for j in file:
        strip=j.strip()
        list=strip.split()
        for k in list:
            resume_txt.append(k)
    text=" ".join(resume_txt)
    resume_scorer_txt(text,resume_txt,file_name)

 if extension==".docx":
  resume_txt=docx2txt.process(resume)
  text=" ".join((resume_txt.split()))
  resume_scorer_doc(text,resume_txt,file_name)

 if extension==".pdf":
    file_name_docx=name+".docx"
    cv=Converter(resume)
    cv.convert(file_name_docx)
    cv.close()
    name, extension = os.path.splitext(file_name_docx)
    if extension==".docx":
        resume_txt = docx2txt.process(file_name_docx)
        text = " ".join((resume_txt.split()))
        resume_scorer_doc(text,resume_txt,file_name)

#calling the function
file_input()