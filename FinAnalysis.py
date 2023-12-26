def read_file(file_name):
    keynames = ['date', 'activity', 'expense', 'income', 'total']
    expense_list = []
    file = open(file_name, "r")
    expense = file.readline().rstrip().split(",")
    while expense != [""]:
        expense_dict = {}
        for i in range(0, len(expense)):
            expense_dict[keynames[i]] = expense[i]
            expense_dict["classification"] = ""
        expense = file.readline().rstrip().split(',')
        expense_list.append(expense_dict)
    file.close()
    return expense_list


def classify(expense_list, expenseclassification, incomeclassification):
    for expense in expense_list:
        if expense["expense"] != "":
            for key, values in expenseclassification.items():
                for value in values:
                    if value in expense['activity']:
                        expense["classification"] = key
                        break
        elif expense['income'] != "":
            for key, value in incomeclassification.items():
                if value in expense['activity']:
                    expense["classification"] = key
                    break
                else:
                    expense["classification"] = ""
    return expense_list


def makereport(expense_list, report_name):
    expense_list = sorted(expense_list, key=lambda x: x['classification'])
    file = open(report_name, "w")
    for expense in expense_list:
        expense_formatted = f"{expense['date']}, {expense['activity']}, {expense['expense']}, {expense['income']}, {expense['classification']}\n"
        file.write(expense_formatted)


