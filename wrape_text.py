string2 = '''The profession of faith is known as the shahada. It is the prerequisite for membership in the \nMuslim community, and an affirmation of the faith. Muslims are required to declare this profession in public \nat least once in their lifetime, but most Muslims recite it daily as part of their prayers. In Arabic, the shahada is \nas follows: “Ashhadu al-la ilaha illa-llah was ashhadu anna Muhammadar rasulu-llah” translated as “ I bear \nwitness that there is no God but Allah and I bear witness that Muhammad is His Messenger” or more simply,\n “There is no god but God and Muhammad is His Messenger. The profession of faith is designed not only for public affirmation, \nbut also to encourage true conviction and sincerity of mind on the part of the worshipper. The phrase is \nabsolutely central to the practice of Islam. Muhammad is reported to have said, “These few words are equal to one \nthird of the Koran. The profession of faith is known as the shahada. It is the prerequisite for membership in the Muslim \ncommunity, and an affirmation of the faith. Muslims are required to declare this profession in public\n at least once in their lifetime, but most Muslims recite it daily as part of their prayers. In Arabic, the \nshahada is as follows: “Ashhadu al-la ilaha illa-llah was ashhadu anna Muhammadar rasulu-llah” translated as “ \nI bear witness that there is no God but Allah and I bear witness that Muhammad is His Messenger” or more simply, \n“There is no god but God and Muhammad is His Messenger. The profession of faith is designed not only for public affirmation,\n but also to encourage true conviction and sincerity of mind on the part of the worshipper. \nThe phrase is absolutely central to the practice of Islam. Muhammad is reported to have said, “These few words are equal to one third of the Koran.'''


def block_of_text(string1):
    lines = string1.splitlines()
    number_of_lines = len(lines)
    for i in range(number_of_lines):
        if i % 2 == 0:
            print("\n\n")
        print(lines[i])

block_of_text(string2)


















