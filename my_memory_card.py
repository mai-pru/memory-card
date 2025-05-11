from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QVBoxLayout,QHBoxLayout,QMessageBox,QRadioButton,QGroupBox,QButtonGroup
from random import *
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
tyrone_list = list()
q1 = Question('when slave end','never','1998','1990','2999')
tyrone_list.append(q1)
q2 = Question('ใครหน้าเหลี่ยม','hundai','prayut','hitler','kim jung un')
tyrone_list.append(q2)
q3 = Question('who is the blackest','hundai','tyrone','jamal','diddy')
tyrone_list.append(q3)
app = QApplication([])
my_win = QWidget()
my_win.setWindowTitle('Memory card')
questionslave = QLabel('Which nationality does not exist?')
RadioGroupBox = QGroupBox("Answer options")
answer = QPushButton('ansler')
anser = QGroupBox('t    es   t   r    es     ul   t')
laby = QLabel('t / f')
slave = QLabel('C   o   rr  e   c   t   a   n   s   wer         .')
main = QVBoxLayout()
mainy = QVBoxLayout()
mainy.addWidget(laby,alignment=(Qt.AlignLeft|Qt.AlignTop))
mainy.addWidget(slave,alignment=(Qt.AlignHCenter))
rbtn_1 = QRadioButton('Enets')
rbtn_2 = QRadioButton('Smurfs')
rbtn_3 = QRadioButton('Chulyms')
rbtn_4 = QRadioButton('Aleuts')
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)  
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)
anser.hide()
anser.setLayout(mainy)
Layout1 = QHBoxLayout()
Layout2 = QHBoxLayout()
Layout3 = QHBoxLayout()
Layout1.addWidget(questionslave,alignment=Qt.AlignHCenter)
Layout2.addWidget(RadioGroupBox)
Layout2.addWidget(anser)
Layout3.addWidget(answer,stretch=3,)
main.addLayout(Layout1)
main.addLayout(Layout2)
main.addLayout(Layout3)
main.setSpacing(5)
def show_result():
    RadioGroupBox.hide()
    anser.show()
    answer.setText('next quston')
def show_qustion():
    anser.hide()
    RadioGroupBox.show()
    answer.setText('ansler')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
def tust():
    if answer.text() == 'ansler':
        show_result()
    else :
        show_qustion()
answers = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]
def ask(q : Question):
    shuffle(answers)
    answers[1].setText(q.wrong2)
    answers[2].setText(q.wrong1)
    answers[3].setText(q.wrong3)
    answers[0].setText(q.right_answer)
    questionslave.setText(q.question)
    slave.setText(q.right_answer)
    show_qustion()
def showcoc(res):
    laby.setText(res)
    show_result()
def checkans():
    if answers[0].isChecked():
        showcoc('cocrect')
        my_win.score += 1
    else :
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            showcoc('incocrect')
def next_question():
    my_win.slave_question += 1
    cur = randint(0,len(tyrone_list) - 1 )
    q = tyrone_list[cur]
    ask(q)
def switch():
    if answer.text() == 'ansler':
        checkans()
    else :
        next_question()
my_win.slave_question = 0
my_win.score = 0
answer.clicked.connect(switch)
next_question()
my_win.setLayout(main)
my_win.show()
app.exec_()