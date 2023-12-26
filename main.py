from FinAnalysis import *


def main():
    expense_classification = {"01 - Order in": ["DD/DOORDASH", "DOMINOS PIZZA"],
                              "02 - Eat Out": ["YALETOWN KEG", "DOWNLOW", "SQ *#5990 STEVE", "THE SPOKE", "TAHINIS",
                                               "BOURBON ST GRIL", "BARAKAT", "AJISEN RAMEN", "OZEN KOREA"],
                              "02- House Items": ["WESTERN DRUG", "SHOPPERS DRUG M"],
                              "03- Groceries": ["COSTCO", "GROCERY CHECKOU"],
                              "04- Cabs": ["UBER CANADA/UBE", "BLACK TOP", "UBER* PENDING"],
                              "05 - Snacks": ["TIM HORTONS", "FRESHSLICE", "TIM'S", "STARBUCKS"],
                              "06- E-transfer out": ["SEND E-TFR"],
                              "07- Wants": ["American Eagle", "RUGDEPO"],
                              "08- University Expense": ["THE BOOK STORE", "WTS PAPERCU", "WESTERNUSE.STOR", "CENGAGE",],
                              "09- Misc": ["LEVEL UP BARBER"]}

    income_classification = {"IN: 01- Pops": "E-TRANSFER",
                             "IN: 02- E-Transfer": "E-TRANSFER",
                             "IN: 03 - Savings": "TFR-FR 6041995"
                             }

    financial_file_import = input("financial data file name: ")
    expense_list = read_file(financial_file_import)
    classified_expense_list = classify(expense_list, expense_classification, income_classification)
    report_input = input("report file name: ")
    makereport(classified_expense_list, report_input)
    print("report updated!")


main()
