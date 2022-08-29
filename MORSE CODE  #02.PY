from ast import Break
from tkinter.ttk import Separator
ch1=input("Enter 1 for translating phrase to morse code\nEnter 2 for translating morse code to phrase")
from playsound import playsound
L3=[]
if ch1=='1':
    FIT=input("Enter the phrase-->")
    FI=FIT.upper()
    L2=[]
    L3=[]
    L1=list(FI)
    for i in L1:
        if i=='A':
            L2.append('.- ')
            playsound('morsea.wav')
        elif i=='B':
            L2.append('-... ')
            playsound('morseab.wav')
        elif i=='C':
            L2.append('-.-. ')
            playsound('morsec.wav')
        elif i=='D':
            L2.append('-.. ')
            playsound('morsead.wav')
        elif i=='E':
            L2.append('. ')
            playsound('morseae.wav')
        elif i=='F':
            L2.append('..-. ')
            playsound('morseaf.wav')
        elif i=='G':
            L2.append('--. ')
            playsound('morseg.wav')
        elif i=='H':
            L2.append('.... ')
            playsound('morseah.wav')
        elif i=='I':
            L2.append('.. ')
            playsound('morsei.wav')
        elif i=='J':
            L2.append('.--- ')
            playsound('morsej.wav')
        elif i=='K':
            L2.append('-.- ')
            playsound('morsek.wav')
        elif i=='L':
            L2.append('.-.. ')
            playsound('morsel.wav')
        elif i=='M':
            L2.append('-- ')
            playsound('morsem.wav')
        elif i=='N':
            L2.append('-. ')
            playsound('morsen.wav')
        elif i=='O':
            L2.append('--- ')
            playsound('morseo.wav')
        elif i=='P':
            L2.append('.--. ')
            playsound('morsep.wav')
        elif i=='Q':
            L2.append('--.- ')
            playsound('morseq.wav')
        elif i=='R':
            L2.append('.-. ')
            playsound('morser.wav')
        elif i=='S':
            L2.append('... ')
            playsound('morses.wav')
        elif i=='T':
            L2.append('- ')
            playsound('morset.wav')
        elif i=='U':
            L2.append('..- ')
            playsound('morseu.wav')
        elif i=='V':
            L2.append('...- ')
            playsound('morsev.wav')
        elif i=='W':
            L2.append('.-- ')
            playsound('morsew.wav')
        elif i=='X':
            L2.append('-..- ')
            playsound('morsex.wav')
        elif i=='Y':
            L2.append('-.-- ')
            playsound('morsey.wav')
        elif i=='Z':
            L2.append('--.. ')
            playsound('morsez.wav')
        elif i=='0':
            L2.append('----- ')
            playsound('morse0.wav')
        elif i=='1':
            L2.append('.---- ')
            playsound('morse1.wav')
        elif i=='2':
            L2.append('..--- ')
            playsound('morse2.wav')
        elif i=='3':
            L2.append('...-- ')
            playsound('morse3.wav')
        elif i=='4':
            L2.append('....- ')
            playsound('morse4.wav')
        elif i=='5':
            L2.append('..... ')
            playsound('morse5.wav')
        elif i=='6':
            L2.append('-.... ')
            playsound('morse6.wav')
        elif i=='7':
            L2.append('--... ')
            playsound('morse7.wav')
        elif i=='8':
            L2.append('---.. ')
            playsound('morse8.wav')
        elif i=='9':
            L2.append('----. ')
            playsound('morse9.wav')
        elif i==' ':
            L2.append('/ ')
            playsound('morsea.wav')
    sep=''
    print(sep.join(L2))
elif ch1=='2':
    SIT=input("Enter the morse code")
    SI=SIT.split()
    for i in SI:
        if i=='.-':
            L3.append('A')
        elif i=='-...':
            L3.append('B')
        elif i=='-.-.':
            L3.append('C')
        elif i=='-..':
            L3.append('D')
        elif i=='.':
            L3.append('E')
        elif i=='..-.':
            L3.append('F')
        elif i=='--.':
            L3.append('G')
        elif i=='....':
            L3.append('H')
        elif i=='..':
            L3.append('I')
        elif i=='.---':
            L3.append('J')
        elif i=='-.-':
            L3.append('K')
        elif i=='.-..':
            L3.append('L')
        elif i=='--':
            L3.append('M')
        elif i=='-.':
            L3.append('N')
        elif i=='---':
            L3.append('O')
        elif i=='.--.':
            L3.append('P')
        elif i=='--.-':
            L3.append('Q')
        elif i=='.-.':
            L3.append('R')
        elif i=='...':
            L3.append('S')
        elif i=='-':
            L3.append('T')
        elif i=='..-':
            L3.append('U')
        elif i=='...-':
            L3.append('V')
        elif i=='.--':
            L3.append('W')
        elif i=='-..-':
            L3.append('X')
        elif i=='-.--':
            L3.append('Y')
        elif i=='--..':
            L3.append('Z')
        elif i=='-----':
            L3.append('0')
        elif i=='.----':
            L3.append('1')
        elif i=='..---':
            L3.append('2')
        elif i=='...--':
            L3.append('3')
        elif i=='....-':
            L3.append('4')
        elif i=='.....':
            L3.append('5')
        elif i=='-....':
            L3.append('6')
        elif i=='--...':
            L3.append('7')
        elif i=='---..':
            L3.append('8')
        elif i=='----.':
            L3.append('9')
        elif i=='/':
            L3.append(' ')
    sep=''
    print(sep.join(L3))