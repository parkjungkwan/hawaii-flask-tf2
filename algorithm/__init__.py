from algorithm.dtree import DTree
if __name__ == '__main__':
    def print_menu():
        print('0. Exit')
        print('1. 결정트리')

        return input('메뉴선택 \n')
    while 1:
        menu = print_menu()
        if menu == '0':
            break
        if menu == '1':
            # DTree().breast_cancer()
            DTree().iris()
        if menu == '2':
           pass
