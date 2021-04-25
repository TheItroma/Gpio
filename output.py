#! /usr/bin/env python3

from tkinter import *

class output:
	### Window_1 ###
	def output():
		### Variable ###
		texte = "Le nombre du gpio : "
		color = '#41B77F'

		### Function ###
		def ctrl(gpin, valeur):
			try:
				value = open("/sys/class/gpio/gpio" + gpin + "/value", "r")
				value.readlines()
				value.close()
			except:
				export = open("/sys/class/gpio/export", "w")
				export.write(str(gpin))
				export.close()
			finally:
				direction = open("/sys/class/gpio/gpio" + gpin + "/direction", "r")
				oi = direction.readlines()
				if oi[0] == 'in\n':
					direction_w = open("/sys/class/gpio/gpio" + gpin + "/direction", "w")
					direction_w.write("out")
					direction_w.close()
				value = open("/sys/class/gpio/gpio" + gpin + "/value", "w")
				value.write(str(valeur))
				value.close()
		def one():
			gpinn = str(gpio_pin.get())
			if gpinn.isdigit():
				ctrl(gpinn, 1)
				la.pack_forget()
			else:
				la.pack(side=LEFT)		
		def zero():
			gpinn = str(gpio_pin.get())
			if gpinn.isdigit():
				ctrl(gpinn, 0)
				la.pack_forget()
			else:
				la.pack(side=LEFT)
		def quit():
			global back
			output.destroy()

		### Fenètre ###
		output = Tk()
		output.title("Gpio Output")
		output.geometry("600x350")
		output.maxsize(600, 350)
		output.minsize(600, 350)
		output.config(background=color)
		output.iconphoto(False, PhotoImage(file='python.png'))

		### Header ###
		frame_1 = Frame(output, bg=color)
		frame_1.pack(fill=X)
		button = Button(frame_1, text="Back", font=("Courrier, 10"), bg='white', fg=color, command=quit)
		button.pack(side=LEFT, padx=10, pady=10)
		title = Label(frame_1, text="Output  Contrôler", bg=color, font=("Courrier", 30), fg='white')
		title.pack(side=LEFT, padx=40)
		subtitle = Label(output, text="Bienvenus, ce programme vous autorise\n à contrôler la sortie gpio  de ce \nraspberry pi", bg=color, font=("Courrier, 10"), fg='white')
		subtitle.pack()

		### Button ###	
		question = Frame(output, bg=color)
		question.pack(pady=50)
		num = Label(question, fg='white', font=("Courrier, 15"), text=texte, bg=color)
		num.pack(side=LEFT)
		gpio_pin = Entry(question, bg='white', font="Courrier")
		gpio_pin.pack()
		la = Label(question, text="Oupsss, vous devez entrez un nombre...", font=("Courrier, 12"), bg=color, fg="white")
		la.pack(side=RIGHT)
		la.pack_forget()
		activer = Button(output, text="   Activer   ", font=("Courrier, 15"), fg=color, bg='white', command=one)
		activer.pack(side=LEFT, padx=25)
		désactiver = Button(output, text="Désactiver", font=("Courrier, 15"), fg=color, bg='white', command=zero)
		désactiver.pack(side=RIGHT, padx=25)
		### Let open ###
		output.mainloop()
output.output()
