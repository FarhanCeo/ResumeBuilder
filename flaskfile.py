#import email
from flask import *
import chrono
import os
import webbrowser
import func
import combinational

app = Flask(__name__)

#####################
companynames = []
comrole = []
comdate = []
comdesc = []
schoolnames = []
degreenames = []
schoolyears = []
marks = []
skillnames = []
skilldesc = []
skills =[]
#####################


@app.route('/')
def index():
    return render_template('win1.html')  

@app.route('/formTemp1.html')
def formTemp1():
    return render_template('formTemp1.html')

@app.route('/formTemp2.html')
def formTemp2():
    return render_template('formTemp2.html')

@app.route('/formTemp3.html')
def formTemp3():
    return render_template('formTemp3.html')

@app.route('/processing2', methods=['POST'])
def processing2():
    
    if request.method == "POST":
        for key,value in request.form.items():
            print(key,value)
            if key.startswith('cname'):
                companynames.append(value)
            elif key.startswith('crole'):
                comrole.append(value)
            elif key.startswith('cdate'):
                comdate.append(value)
            
            elif key.startswith('schoolname'):
                schoolnames.append(value)
            elif key.startswith('degree'):
                degreenames.append(value)
            elif key.startswith('sdate'):
                schoolyears.append(value)
            elif key.startswith('smarks'):
                marks.append(value)
            elif key.startswith('skillname'):
                skillnames.append(value)
            elif key.startswith('skilldesc'):
                skilldesc.append(value)
            elif key == 'yourname':
                name = value
            elif key == 'email':
                email = value
            elif key == 'phonenumber':
                phone = value
            elif key == 'address':
                address = value
            elif key == 'linkid':
                linkid = value
            elif key == 'summary':
                summary = value
            elif key == 'filename':
                filenamee = value
             
    print("company names",companynames)
    print("company role",comrole)
    print("company date",comdate)
    #print("company desc",comdesc)
    print("school names",schoolnames)
    print("degree names",degreenames)
    print("school years",schoolyears)
    print("marks",marks)
    print("skillnames ",skillnames)
    print("skilldesc",skilldesc)
    
    #s = testcreat.do(a=2,b=3)
    #print("==>",s)
    #createme(name,email,phone,address,linkid,summary,companynames,comrole,comdate,comdesc,schoolnames,degreenames,schoolyears,marks,skills)
    
    func.createme(name = name,address=address, mobno=phone, emailid=email, linkid=linkid,summary = summary,companynames=companynames, comyourrole =comrole, yearrange = comdate, schoolnames = schoolnames, degreenams=degreenames, schoolyears= schoolyears, marks = marks, skillnames = skillnames,skilldesc = skilldesc, filenamee = filenamee)
    #return render_template('showdata.html',companynames=companynames,comrole=comrole,comdate=comdate,comdesc=comdesc,schoolnames=schoolnames,degreenames=degreenames,schoolyears=schoolyears,marks=marks,skills=skills,name=name,email=email,phone=phone,address=address,linkid=linkid,summary=summary)
    webbrowser.open_new("C:\\Users\\lenevo\\Desktop\\Resume with Flask\\frontend\\static\\pdf\\%s.pdf" % filenamee)
    return render_template('success.html')


@app.route('/processing3', methods=['POST'])
def processing3():
    
    if request.method == "POST":
        for key,value in request.form.items():
            print(key,value)
            if key.startswith('cname'):
                companynames.append(value)
            elif key.startswith('crole'):
                comrole.append(value)
            elif key.startswith('cdate'):
                comdate.append(value)
            elif key.startswith('cdesc'):
                comdesc.append(value)
            elif key.startswith('schoolname'):
                schoolnames.append(value)
            elif key.startswith('degree'):
                degreenames.append(value)
            elif key.startswith('sdate'):
                schoolyears.append(value)
            elif key.startswith('smarks'):
                marks.append(value)
            elif key.startswith('skillname'):
                skillnames.append(value)
            elif key.startswith('skilldesc'):
                skilldesc.append(value)
            elif key == 'yourname':
                name = value
            elif key == 'email':
                email = value
            elif key == 'phonenumber':
                phone = value
            elif key == 'address':
                address = value
            elif key == 'linkid':
                linkid = value
            elif key == 'summary':
                summary = value
            elif key == 'filename':
                filenamee = value
             
    print("company names",companynames)
    print("company role",comrole)
    print("company date",comdate)
    print("company desc",comdesc)
    print("school names",schoolnames)
    print("degree names",degreenames)
    print("school years",schoolyears)
    print("marks",marks)
    print("skillnames ",skillnames)
    print("skilldesc",skilldesc)
    
    #s = testcreat.do(a=2,b=3)
    #print("==>",s)
    #createme(name,email,phone,address,linkid,summary,companynames,comrole,comdate,comdesc,schoolnames,degreenames,schoolyears,marks,skills)
    
    combinational.createme(name = name,address=address, mobno=phone, emailid=email, linkid=linkid,summary = summary,companynames=companynames, comyourrole =comrole, yearrange = comdate, descslist = comdesc, schoolnames = schoolnames, degreenams=degreenames, schoolyears= schoolyears, marks = marks, skillnames = skillnames,skilldesc = skilldesc, filenamee = filenamee)
    #return render_template('showdata.html',companynames=companynames,comrole=comrole,comdate=comdate,comdesc=comdesc,schoolnames=schoolnames,degreenames=degreenames,schoolyears=schoolyears,marks=marks,skills=skills,name=name,email=email,phone=phone,address=address,linkid=linkid,summary=summary)
    webbrowser.open_new("C:\\Users\\lenevo\\Desktop\\Resume with Flask\\frontend\\static\\pdf\\%s.pdf" % filenamee)
    return render_template('success.html')

@app.route('/processing1', methods=['POST'])
def processing1():
    if request.method == "POST":
        for key,value in request.form.items():
            print(key,value)
            if key.startswith('cname'):
                companynames.append(value)
            elif key.startswith('crole'):
                comrole.append(value)
            elif key.startswith('cdate'):
                comdate.append(value)
            elif key.startswith('cdesc'):
                comdesc.append(value)
            elif key.startswith('schoolname'):
                schoolnames.append(value)
            elif key.startswith('degree'):
                degreenames.append(value)
            elif key.startswith('sdate'):
                schoolyears.append(value)
            elif key.startswith('smarks'):
                marks.append(value)
            elif key.startswith('skill'):
                skills.append(value)
            elif key == 'yourname':
                name = value
            elif key == 'email':
                email = value
            elif key == 'phonenumber':
                phone = value
            elif key == 'address':
                address = value
            elif key == 'linkid':
                linkid = value
            elif key == 'summary':
                summary = value
            elif key == 'filename':
                filenamee = value
             
    print("company names",companynames)
    print("company role",comrole)
    print("company date",comdate)
    print("company desc",comdesc)
    print("school names",schoolnames)
    print("degree names",degreenames)
    print("school years",schoolyears)
    print("marks",marks)
    print("skills",skills)
    
    #s = testcreat.do(a=2,b=3)
    #print("==>",s)
    #createme(name,email,phone,address,linkid,summary,companynames,comrole,comdate,comdesc,schoolnames,degreenames,schoolyears,marks,skills)
    
    chrono.createme(name = name,address=address, mobno=phone, emailid=email, linkid=linkid,summary = summary,companynames=companynames, comyourrole =comrole, yearrange = comdate, descslist = comdesc, schoolnames = schoolnames, degreenams=degreenames, schoolyears= schoolyears, marks = marks, skills = skills, filenamee = filenamee)
    #return render_template('showdata.html',companynames=companynames,comrole=comrole,comdate=comdate,comdesc=comdesc,schoolnames=schoolnames,degreenames=degreenames,schoolyears=schoolyears,marks=marks,skills=skills,name=name,email=email,phone=phone,address=address,linkid=linkid,summary=summary)
    #webbrowser.open_new("C:\\Users\\lenevo\\Desktop\\Resume with Flask\\frontend\\static\\pdf\\%s.pdf" % filenamee)
    #return render_template('success.html')
    #pass
    webbrowser.open_new("C:\\Users\\lenevo\\Desktop\\Resume with Flask\\frontend\\static\\pdf\\%s.pdf" % filenamee)
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True) 