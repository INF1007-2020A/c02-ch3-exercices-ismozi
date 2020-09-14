#!/usr/bin/env python


def dissipated_power(voltage, resistance):
	puissance = (voltage**2)/resistance
	return puissance

def orthogonal(v1, v2):
	# TODO: Retourner vrai si les vecteurs sont orthogonaux, faux sinon.
	prod_scal=(v1[0]*v2[0])+(v1[1]*v2[1]) 
	
	if prod_scal == 0:
		ortho=True
	else:
		ortho=False

	return ortho

def average(values):
	# TODO: Calculer la moyenne des valeurs positives (on ignore les valeurs strictement négatives).
	somme=0
	moyenne=0
	counter_positifs=0
	for v in values:
		if v>=0:
			counter_positifs+=1
			somme+=v
	
	moyenne=somme/counter_positifs
	return moyenne

def bills(value):
	# TODO: Calculez le nombre de billets de 20$, 10$ et 5$ et pièces de 1$ à remettre pour représenter la valeur.
	
	twenties=tens=fives=ones=0
	
	while value != 0:
		if value >= 20:
			twenties+=1
			value-=20			
		elif value >= 10:
			tens+=1
			value-=10			
		elif value >= 5:
			fives+=1
			value-=5			
		elif value >= 1:
			ones+=1
			value-=1
			

	return (twenties, tens, fives, ones)

if __name__ == "__main__":
	#print(dissipated_power(69, 420))
	#print(orthogonal((1, 1), (-1, 1)))
	#print(average([1, 4, -2, 10]))
	print(bills(137))
