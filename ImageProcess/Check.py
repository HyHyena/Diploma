import ProcessImage


class Check():

    def check(self, dir, answers):
        elements = ProcessImage.gettxts(dir)
        with open(dir+"all.txt", "w") as all:
            for elem in elements:
                right, wrong = self.checkone(self, elem, answers)
                all.write("Имя: " + elem.split("/")[-2])
                all.write("\nПравильные: " + ", ".join(str(r) for r in right))
                all.write("\nНеправильные: " + ", ".join(str(w) for w in wrong) + "\n")
                all.write("Итого: " + str(len(right)) + "/" + str(len(right)+len(wrong)) + "\tПроцент выполнения: " + str(round(len(right)/(len(right)+len(wrong)), 2))
                          +"\n")

    def checkone(self, end, answers):
        file = end
        with open(file, "r") as f:
            dada = f.readlines()
        with open(answers, "r") as f:
            ans = f.readlines()
        i = 0
        right = list()
        wrong = list()
        for i in range(len(dada)):
            if dada[i] == ans[i]:
                right.append(i + 1)
            else:
                wrong.append(i + 1)
        return right, wrong
