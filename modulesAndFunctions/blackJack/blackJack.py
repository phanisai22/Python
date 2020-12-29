import tkinter
import random
# import time


def load_images(card_images):
    suits = ['heart', 'club', 'diamond', 'spade']
    face_cards = ['king', 'queen', 'jack']

    # if tkinter.TkVersion >= 8.6:
    #     extension = 'png'
    # else:
    extension = 'ppm'

    #     for each suit , retrieve the image for the card .
    for suit in suits:
        #       first the number cards 1 to 10
        # /mnt/NV/DocumentsNV/Github/Python/modulesAndFunctions/blackJack/cards
        # cards/{}_{}.{}
        for card in range(1, 11):
            name = '/mnt/NV/DocumentsNV/Github/Python/modulesAndFunctions/blackJack/cards/{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image,))

        # for face cards
        for card in face_cards:
            name = '/mnt/NV/DocumentsNV/Github/Python/modulesAndFunctions/blackJack/cards/{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image,))


def deal_card(frame):
    # pop the next card of the top of the deck .
    next_card = deck.pop(0)
    deck.append(next_card)
    # add the image to the label and display the label .
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')
    # now return the cards face value .
    return next_card


def score_hand(hand):
    score = 0
    ace = False
    for next_card in hand:
        value = next_card[0]
        if value == 1 and not ace:
            value = 11
            ace = True
        score += value
        if score > 21 and ace:
            score -= 10
            ace = False

    return score


def deal_dealer():
    dealer_hand.append(deal_card(dealer_card_frame))
    dealer_score = score_hand(dealer_hand)
    # player_score = score_hand(player_hand)

    dealer_score_label.set(dealer_score)

    if dealer_score > 21:
        result_text.set("Player win's... Match ended !")
    else:
        result_text.set('Draw Player')


def deal_player():
    player_hand.append(deal_card(player_card_frame))
    player_score = score_hand(player_hand)

    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("Dealer win's... Match ended !")
        # main_window.quit()
        # time.sleep(5)
        # main_window.destroy()
    else:
        result_text.set('Draw Dealer')
    # global player_score
    # global player_ace
    # card_value = deal_card(player_card_frame)[0]
    # if card_value == 1 and not player_ace:
    #     card_value = 11
    #     player_ace = True
    # player_score += card_value
    #
    # # If we would bust , check is there is an ace and do -10 .
    # if player_score > 21 and player_ace:
    #     player_score -= 10
    #     player_ace = False
    #
    # player_score_label.set(player_score)
    #
    # if player_score > 21:
    #     result_text.set('Dealer wins')


def restart_game():
    global dealer_card_frame
    global player_card_frame
    global dealer_hand
    global player_hand
    global deck

    dealer_card_frame.destroy()
    player_card_frame.destroy()

    # Embedded frame to hold the card images .
    dealer_card_frame = tkinter.Frame(card_frame, background='green')
    dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)

    player_card_frame = tkinter.Frame(card_frame, background='green')
    player_card_frame.grid(row=2, column=1, rowspan=2, sticky='ew')

    result_text.set('')
    player_score_label.set(0)
    dealer_score_label.set(0)

    # create the list to store the dealer's and player's hand .
    dealer_hand = []
    player_hand = []

    # deal_player()
    # dealer_hand.append(deal_card(dealer_card_frame))
    # dealer_score_label.set(score_hand(dealer_hand))
    # deal_player()


def shuffle_cards():
    random.shuffle(deck)


if __name__ == '__main__':

    main_window = tkinter.Tk()

    main_window.title('Black Jack')
    main_window.geometry('640x480')
    main_window.configure(background='green')

    result_text = tkinter.StringVar()
    result = tkinter.Label(main_window, textvariable=result_text)
    result.grid(row=0, column=0, columnspan=3)

    card_frame = tkinter.Frame(main_window, relief='sunken', borderwidth=1, background='green')
    card_frame.grid(row=1, column=0, sticky='ew', rowspan=2, columnspan=3)

    dealer_score_label = tkinter.IntVar()
    tkinter.Label(card_frame, text='Dealer', background='green', fg='white').grid(row=0, column=0)
    tkinter.Label(card_frame, textvariable=dealer_score_label, background='green', fg='white').grid(row=1, column=0)

    # Embedded frame to hold the card images .
    dealer_card_frame = tkinter.Frame(card_frame, background='green')
    dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)

    player_score_label = tkinter.IntVar()
    # player_score = 0
    # player_ace = False

    tkinter.Label(card_frame, text='Player', background='green', fg='white').grid(row=2, column=0)
    tkinter.Label(card_frame, textvariable=player_score_label, background='green', fg='white').grid(row=3, column=0)

    # Embedded frame to hold the card images .
    player_card_frame = tkinter.Frame(card_frame, background='green')
    player_card_frame.grid(row=2, column=1, rowspan=2, sticky='ew')

    # Buttons frame
    button_frame = tkinter.Frame(main_window)
    button_frame.grid(row=3, column=0, columnspan=3, sticky='w')

    dealer_button = tkinter.Button(button_frame, text='Dealer', command=deal_dealer)
    dealer_button.grid(row=0, column=0, sticky='w')
    player_button = tkinter.Button(button_frame, text='Player', command=deal_player)
    player_button.grid(row=0, column=1, sticky='e')

    # load cards
    cards = []
    load_images(cards)
    # print(cards)

    # create a new deck of cards .
    deck = list(cards)

    # create the list to store the dealer's and player's hand .
    dealer_hand = []
    player_hand = []

    # deal_player()
    # dealer_hand.append(deal_card(dealer_card_frame))
    # dealer_score_label.set(score_hand(dealer_hand))
    # deal_player()

    # starting a new game .
    restart_button = tkinter.Button(button_frame, text='Play again', command=restart_game)
    restart_button.grid(row=0, column=2, sticky='e')

    # additional buttons .
    exit_button = tkinter.Button(button_frame, text='Exit match', command=main_window.destroy)
    exit_button.grid(row=0, column=4, sticky='e')
    shuffle_button = tkinter.Button(button_frame, text='Shuffle Deck', command=shuffle_cards)
    shuffle_button.grid(row=0, column=3, sticky='e')

    main_window.mainloop()
