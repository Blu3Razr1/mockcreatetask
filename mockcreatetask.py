'''
Evan Watson, Elliot Esposito
1-30-19
v1.1
Calculates variables within Specific Heat Equation (q = mCΔT)
'''

#makes lists for units of measurement
unit_dic = {'mass': ['kilograms', 'grams', 'kg', 'g'], 'heat': ['joules', 'j', 'kj', 'kilojoules'], 'sC': ['j/gc', 'j/molc']}

#creates separate vars for each list
heats = list(unit_dic.get('heat'))
masses = list(unit_dic.get('mass'))
sC = list(unit_dic.get('sC'))

#main function
def main():
  while True: #while loop
    var_solveQ = '''
    What do you want to find?
    q = The heat
    m = The mass
    sC = The Specific Heat Capacity
    ΔT (dT) = The change in temperature
    '''
    var_solve = input(var_solveQ).lower() #multi-line input
    if var_solve == 'q':
        q_solve()
        break
    elif var_solve == 'm':
        m_solve()
        break
    elif var_solve == 'sc':
        sC_solve()
        break
    elif var_solve == 'dt':
        ΔT_solve()
        break
    else:
        continue

##################           ##################
                #SOLVING FOR Q#
##################           ##################
def q_solve():
    while True: #loop to repeat question
            unit_heat =  input("What units would you like to use, Joules, or Kilojoules?>> ").lower()
            if unit_heat in heats: #checks for value in the list 'heats'
                if unit_heat == 'j' or unit_heat == 'joules':
                  mass_v = float(input("Ok, what is the mass of your object? "))
                  sC_v = float(input("What is the specific heat capicity of your material? "))
                  changeTemp_v = float(input("What is the change in temperature? "))
                  heat_v = (mass_v*sC_v*changeTemp_v)
                  print('The heat released/abosrbed is %.2f Joules, remember to use sig figs!' % heat_v)
                elif unit_heat == 'kj' or unit_heat == 'kilojoules':
                  mass_vK = float(input("Ok, what is the mass of your object? "))
                  sC_vK = float(input("What is the specific heat capicity of your material?(in J/gC)>> "))
                  changeTemp_vK = float(input("What is the change in temperature? "))
                  heat_vK = ((mass_vK*sC_vK*changeTemp_vK)/1000)
                  print('The heat released/abosrbed is %.3f Kilojoules, remember to use sig figs!' % heat_vK)
                break
            else:
                print("Please enter a unit of heat (J, KJ, Joules, or Kilojoules) >>")
                continue #repeats question

##################           ##################
                #SOLVING FOR M#
##################           ##################
def m_solve():
     while True: #loop to repeat question
            unit_mass =  input("What units would you like to use, Grams, or Kilograms?>> ").lower()
            if unit_mass in masses: #checks for value in the list 'masses'
                if unit_mass == 'g' or unit_mass == 'grams':
                  q_v = float(input("Ok, how much heat was released/absorbed? "))
                  sC_v = float(input("What is the specific heat capicity of your material? "))
                  changeTemp_v = float(input("What is the change in temperature? "))
                  mass_v = (q_v/(sC_v*changeTemp_v))
                  print('The mass of your object is %.2f grams, remember to use sig figs!' % mass_v)
                elif unit_mass == 'kg' or unit_mass == 'kilograms':
                  q_vK = float(input("Ok, how much heat was released/absorbed? "))
                  sC_vK = float(input("What is the specific heat capicity of your material?(in J/gC)>> "))
                  changeTemp_vK = float(input("What is the change in temperature? "))
                  mass_vK = ((q_vK/(sC_vK*changeTemp_vK))/1000)
                  print('The mass of your object is %.3f Kilograms, remember to use sig figs!' % mass_vK)
                break
            else:
                print("Please enter a unit of mass (g, kg, grams, or kilograms)>>")
                continue #repeats question

#################           #################
              #SOLVING FOR sC#
#################           #################
def sC_solve():
    while True: #loop to repeat question
            unit_sC =  input("What units would you like to use, J/gC, or J/molC?>> ").lower()
            if unit_sC in sC: #checks for value in the list 'sC'
                if unit_sC == 'j/gc':
                  mass_v = float(input("Ok, what is the mass of your object? "))
                  q_v = float(input("How much heat was released/absorbed? "))
                  changeTemp_v = float(input("What is the change in temperature? "))
                  sC_v = (q_v/(mass_v*changeTemp_v))
                  print('The specific heat capacity of your material is %.2f J/gC, remember to use sig figs!' % sC_v)
                elif unit_sC == 'j/molc':
                  mass_vM = float(input("Ok, what is the mass of your object>> " ))
                  Mmass_v = float(input("What is the molar mass of your material?(Multiply by coefficient if necessary)>> "))
                  q_vM = float(input("How much heat was released/absorbed ?(in J)>> "))
                  changeTemp_vM = float(input("What is the change in temperature? "))
                  sC_vM = (q_vM/(mass_vM*changeTemp_vM))*Mmass_v
                  print('The molar heat capacity of your material is %.3f J/molC, remember to use sig figs!' % sC_vM)
                break
            else:
                print("Please enter j/gc OR j/molc >>")
                continue #repeats question

#################           #################
              #SOLVING FOR ΔT#
#################           #################
def ΔT_solve():
    while True:
        print("Ok, you are solveing for delta T, please enter the following information:")
        q_v = float(input("Heat released/abosrbed (J)>> "))
        mass_v = float(input("Mass of object (g)>> "))
        sC_v = float(input("Specific heat capacity of material (J/gC)>> "))
        ΔT_v = (q_v/(mass_v*sC_v))
        print("The change in temperature during this reaction was %.2f degrees centigrade" % ΔT_v)
        break

main() #calling the main function to start the program
