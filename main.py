from website import Website
import os

def clearTerminal():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def main():
    clearTerminal()

    print(u'Welcome to \u001b[31m BBC World News\u001b[0m ')
    print('Press Enter for next title, "R" to read the summry, "Q" to quit and "E" to exit an article')
    print("To enter an article, press 'R' within the summary, or just Enter to go back")
    print('In order to navigate back to previous articles, enter "B"')

    site = Website()

    done = False
    while not done:
        print(u'\u001b[31mBBC World News\u001b[0m ')
        print("Title: ", end='')
        site.printHeadline()
        
        checker = input(u'\u001b[35m>>>\u001b[0m ')

        clearTerminal()
        
        if checker.lower() == 'q':
            break
        elif checker.lower() == 'b':
            site.goBack()
        elif checker.lower() == 'r':
            site.printHeadline()
            site.printSubtitles()
            checker2 = input(u'\u001b[35m>>>\u001b[0m ')
            if checker2.lower() == 'r':
                site.getArticlePage()
                input()

        else:
            site.goForward()
        clearTerminal()
main()