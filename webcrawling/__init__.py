from webcrawling.controller import Controller
if __name__ == '__main__':
    def print_menu():
        print('0. Exit')
        print('1. Bugs Music')
        print('2. Naver Movie')
        print('3. Wiki')
        print('4. hanbit')
        print('5. weather')
        return input('메뉴 선택 \n')


    app = Controller()
    while 1:
        menu = print_menu()
        if menu == '1':
            app.bugs_music('https://music.bugs.co.kr/chart/track/realtime/total?chartdate=20200201&charthour=16')
        if menu == '2':
            app.naver_movie('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
        if menu == '3':
            app.wiki('http://dh.aks.ac.kr/Encyves/wiki/index.php/조선_세종')
        if menu == '4':
            app.hanbit('http://www.hanbit.co.kr/member/login_proc.php')
        if menu == '5':
            app.hanbit('')
        elif menu == '0':
            break