print("Välkommen!")
print("Nu är det dags att svara på frågorna om texten!")

questions = ["Vem räknas som världens första programmerare?",
         "Vad användes för att programmera de första datorerna?",
         "Vilket programmeringsspråk skapade Grace Hopper?",
         "Vem ledde mjukvaruutvecklingen för Apollo-programmet?",
         "Vilka två företag drev PC-revolutionen?"]

anwsers = ["Ada Lovelace",
        "Hålkort",
        "COBOL",
        "Margaret Hamilton",
        "Apple,Microsoft"]

number = -1

for i in questions:
    print(i)
    svar = input("Var snäll och svara på frågan: ")
    number = number+1
    if svar == anwsers[number]:
        print("Rätt svar här kommer nästa fråga!")
    else: 
        print("Tyvärr det var fel!")        