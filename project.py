lines = None
with open("data.txt") as file:
    lines = file.readlines()

if not lines :
    print("Something Went Wrong!")
    exit()

def getTopStudent(subject:str , dataset:dict):
    maxMarks = 0
    maxStudent = ""
    for name,marks in dataset.items():
        if maxMarks < marks:
            maxMarks = marks
            maxStudent = name
    return maxStudent,maxMarks

def getMarks(recode:tuple):
    return recode[1]  


mark_lines = lines[1:]
subject_marks = {}
studentMarks = {}
messages = []

for line in mark_lines:
    rows = line.split(',')
    name = rows[0].strip()
    subject = rows[1].strip()
    marks = int(rows[2].strip())
    
    if subject not in subject_marks:
        subject_marks[subject] = {}
    
    subject_marks[subject][name] = marks

    earlyMarks = studentMarks.get(name,0)
    studentMarks[name] = earlyMarks + marks 
    
for subject,dataset in subject_marks.items():
    name, marks = getTopStudent(subject,dataset)
    msg = f"Top Student for {subject} is {name} {marks} marks."
    print(msg)
    messages.append(msg)

markList = [(name ,marks) for name,marks in studentMarks.items()]
markList.sort(key = getMarks,reverse=True)
top = markList[0]
msg = f"Top Student Is {top[0]} .Toatal Mark Is {top[1]}."
print(msg)

messages.append(msg)

with open("messages.txt",'w') as OutPutMessage:
    for msg in messages:
        OutPutMessage.write(msg)
        OutPutMessage.write('\n')

