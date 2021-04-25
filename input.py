#! /usr/bin/env python3

from tkinter import *

class input:
	### Window_1 ###
	def input():
		### Variable ###
		color = '#ADDEEE'

		### Function ###
		def read():
			print("In construction...")
		def quit():
			input.destroy()

		### Fenètre ###
		input = Tk()
		input.title("Gpio Input")
		input.geometry("600x350")
		input.maxsize(600, 350)
		input.minsize(600, 350)
		input.config(background=color)
		input.iconphoto(False, PhotoImage(file='python.png'))

		### Header ###
		header = Frame(input, bg=color)
		header.pack(fill=X)
		boutton = Button(header, text="Back", font=("Courrier, 10"), bg='white', fg=color, command=quit)
		boutton.pack(side=LEFT, padx=10, pady=10)
		titre = Label(header, text="input Contrôler", bg=color, font=("Courrier", 30), fg='white')
		titre.pack(side=LEFT, padx=65)
		sublable = Label(input, text="Bienvenus, ce programme vous autorise\n à lire l'entrée gpio  de ce \nraspberry pi", bg=color, font=("Courrier, 10"), fg='white')
		sublable.pack()

		### input of the input ###
		question = Frame(input, bg=color)
		question.pack(pady=20)
		num = Label(question, fg='white', font=("Courrier, 15"), text="Le nombre du gpio : ", bg=color)
		num.pack(side=LEFT)
		gpio_pin = Entry(question, bg='white', font="Courrier")
		gpio_pin.pack()

		lec = Label(question, fg='white', font=("Courrier, 15"), text="La méthode de lecture : ", bg=color)
		lec.pack(side=LEFT, pady=15)
		edge_l = Entry(question, bg='white', font="Courrier")
		edge_l.pack(pady=15)

		### Let open ###
		input.mainloop()
input.input()