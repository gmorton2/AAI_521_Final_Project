import numpy as np
import pandas as pd
import tensorflow as tf
import os
import random
import cv2
import math

target_dict={'10C': 0,
 '10D': 1,
 '10H': 2,
 '10S': 3,
 '2C': 4,
 '2D': 5,
 '2H': 6,
 '2S': 7,
 '3C': 8,
 '3D': 9,
 '3H': 10,
 '3S': 11,
 '4C': 12,
 '4D': 13,
 '4H': 14,
 '4S': 15,
 '5C': 16,
 '5D': 17,
 '5H': 18,
 '5S': 19,
 '6C': 20,
 '6D': 21,
 '6H': 22,
 '6S': 23,
 '7C': 24,
 '7D': 25,
 '7H': 26,
 '7S': 27,
 '8C': 28,
 '8D': 29,
 '8H': 30,
 '8S': 31,
 '9C': 32,
 '9D': 33,
 '9H': 34,
 '9S': 35,
 'AC': 36,
 'AD': 37,
 'AH': 38,
 'AS': 39,
 'JC': 40,
 'JD': 41,
 'JH': 42,
 'JS': 43,
 'KC': 44,
 'KD': 45,
 'KH': 46,
 'KS': 47,
 'QC': 48,
 'QD': 49,
 'QH': 50,
 'QS': 51}

model_path = "Black_Jack/card_trained_model/card_trained_model"
#new_model = tf.saved_model.load(model_path)
new_model = tf.keras.models.load_model(model_path)

def keep_count(predicted_value):
    count=0
    if (predicted_value.startswith('2') or predicted_value.startswith('3') or 
    predicted_value.startswith('4') or predicted_value.startswith('5') or predicted_value.startswith('6')):
        count+=1
    elif (predicted_value.startswith('7') or predicted_value.startswith('8') or 
    predicted_value.startswith('9')):
        pass
    else:
        count-=1
    return count

def hand_value(predicted_value, user_hand_value):
    hand_value=0
    if(predicted_value.startswith('2')):
        hand_value+=2
    elif(predicted_value.startswith('3')):
        hand_value+=3
    elif(predicted_value.startswith('4')):
        hand_value+=4
    elif(predicted_value.startswith('5')):
        hand_value+=5
    elif(predicted_value.startswith('6')):
        hand_value+=6
    elif(predicted_value.startswith('7')):
        hand_value+=7
    elif(predicted_value.startswith('8')):
        hand_value+=8
    elif(predicted_value.startswith('9')):
        hand_value+=9
    elif(predicted_value.startswith('A')):
        if user_hand_value >= 11:
            hand_value+=1
        else:
            hand_value+=11
    else:
        hand_value+=10
    return hand_value

def basic_strategy(hand_value, dealer_card, player_cards):
    choice=''
    if not player_cards[0].startswith('A') or not player_cards[1].startswith('A'):
        if 4 <= hand_value <= 7:
            choice='hit'
        elif hand_value == 8:
            choice='hit'
        elif hand_value == 9:
            if dealer_card.startswith('2') or dealer_card.startswith('3') or dealer_card.startswith('4') or dealer_card.startswith('5') or dealer_card.startswith('6'):
                choice='double'
            else:
                choice='hit'
        elif hand_value == 10:
            if dealer_card.startswith('10') or dealer_card.startswith('J') or dealer_card.startswith('K') or dealer_card.startswith('Q') or dealer_card.startswith('A'):
                choice='hit'
            else:
                choice='double'
        elif hand_value == 11:
            choice='double'
        elif hand_value == 12:
            if dealer_card.startswith('4') or dealer_card.startswith('5') or dealer_card.startswith('6'):
                choice='stand'
            else:
                choice='hit'
        elif hand_value == 13:
            if dealer_card.startswith('2') or dealer_card.startswith('3') or dealer_card.startswith('4') or dealer_card.startswith('5') or dealer_card.startswith('6'):
                choice='stand'
            else:
                choice='hit'
        elif hand_value == 14:
            if dealer_card.startswith('2') or dealer_card.startswith('3') or dealer_card.startswith('4') or dealer_card.startswith('5') or dealer_card.startswith('6'):
                choice='stand'
            else:
                choice='hit'
        elif hand_value == 15:
            if dealer_card.startswith('2') or dealer_card.startswith('3') or dealer_card.startswith('4') or dealer_card.startswith('5') or dealer_card.startswith('6'):
                choice='stand'
            else:
                choice='hit'
        elif hand_value == 16:
            if dealer_card.startswith('2') or dealer_card.startswith('3') or dealer_card.startswith('4') or dealer_card.startswith('5') or dealer_card.startswith('6'):
                choice='stand'
            else:
                choice='hit'
        else:
            choice='stand'
    else:
        if player_cards[0].startswith('2') or player_cards[1].startswith('2'):
            if dealer_card.startswith('4') or dealer_card.startswith('5') or dealer_card.startswith('6'):
                choice='double'
            else:
                choice='hit'
        elif player_cards[0].startswith('3') or player_cards[1].startswith('3'):
            if dealer_card.startswith('4') or dealer_card.startswith('5') or dealer_card.startswith('6'):
                choice='double'
            else:
                choice='hit'
        elif player_cards[0].startswith('4') or player_cards[1].startswith('4'):
            if dealer_card.startswith('4') or dealer_card.startswith('5') or dealer_card.startswith('6'):
                choice='double'
            else:
                choice='hit'
        elif player_cards[0].startswith('5') or player_cards[1].startswith('5'):
            if dealer_card.startswith('4') or dealer_card.startswith('5') or dealer_card.startswith('6'):
                choice='double'
            else:
                choice='hit'
        elif player_cards[0].startswith('6') or player_cards[1].startswith('6'):
            if dealer_card.startswith('2') or dealer_card.startswith('3') or dealer_card.startswith('4') or dealer_card.startswith('5') or dealer_card.startswith('6'):
                choice='double'
            else:
                choice='hit'
        elif player_cards[0].startswith('7') or player_cards[1].startswith('7'):
            if dealer_card.startswith('2') or dealer_card.startswith('7') or dealer_card.startswith('8'):
                choice='stand'
            elif dealer_card.startswith('3') or dealer_card.startswith('4') or dealer_card.startswith('5') or dealer_card.startswith('6'):
                choice='double'
            else:
                choice='hit'
        elif player_cards[0].startswith('8') or player_cards[1].startswith('8'):
            if dealer_card.startswith('6'):
                choice='double'
            else:
                choice='stand'
        else:
            choice='stand'
        
    return choice

def image_transformation(deck_folder, file):
    image = cv2.imread(deck_folder+"/"+file, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(image, (180, 180))
    img_transformed = img.reshape((1, img.shape[0], img.shape[1], 1))
    return img_transformed

def predict_image(img_transformed, target_dict):
    prediction = new_model.predict(img_transformed)
    highest_prob_idx=prediction.argmax()
    # retrun the key based on the value
    value=list(target_dict.keys()) [list(target_dict.values()).index(highest_prob_idx)]
    return value

def reset_values(player_hand_value, dealer_hand_value, player_hand, dealer_hand, num_of_cards):
    player_hand_value=0
    dealer_hand_value=0
    num_of_cards=0
    player_hand.clear()
    dealer_hand.clear()
    return player_hand_value, dealer_hand_value, player_hand, dealer_hand, num_of_cards

def get_card(deck_folder,cards_in_use):
    card_file = random.choice(os.listdir(deck_folder))
                    
    if card_file not in cards_in_use:
        cards_in_use.append(card_file)
        img_transformed = image_transformation(deck_folder, card_file)
        value = predict_image(img_transformed,target_dict)
    else:
        value = None 
        
    return value

def bet_amount(count,bet_unit):
    if count <= 1:
        return bet_unit
    else:
        return bet_unit*count

def black_jack(target_dict):
    # pick random point in deck between 60%-95% that 
    # when reached then the deck is shuffled again (simulates a casino).
    shuffle_limit = math.floor(52*random.uniform(.6, .95))
    cards_in_play=0
    player_hand=[]
    dealer_hand=[]
    cards_in_use = []
    count=0
    player_hand_value = 0
    dealer_hand_value = 0
    bank_roll = 5000.0
    bet_unit = 50.0
    num_of_units = bank_roll/bet_unit
    
    while cards_in_play < shuffle_limit or bank_roll <= 0:
        deck_folder='Black_Jack/deck/deck'
        num_of_cards=0
        bank_roll_float = "{:.2f}".format(bank_roll)
        print('\n------------------------------------------------------------------')
        print(f"You currently have ${bank_roll_float}")
        amount = bet_amount(count,bet_unit)
        bet_amount_float = "{:.2f}".format(amount)
        print(f"Based on the current count of {count} you will bet ${bet_amount_float}")
        print("\n|||||||||||||||||||||\nNew Hand\n|||||||||||||||||||||\n")
        while num_of_cards<4:
            card_file = random.choice(os.listdir(deck_folder))
            
            if card_file not in cards_in_use:
                cards_in_use.append(card_file)
                img_transformed = image_transformation(deck_folder, card_file)
                value = predict_image(img_transformed,target_dict)
                
                if num_of_cards % 2 == 0:
                    dealer_hand.append(value)
                    count+=keep_count(value)
                else:
                    player_hand.append(value)
                    count+=keep_count(value)
                    player_hand_value+=hand_value(value,player_hand_value)
                cards_in_play+=1
                num_of_cards+=1
                
            else:
                continue
        dealer_hand_value+=(hand_value(dealer_hand[0],dealer_hand_value)+hand_value(dealer_hand[1],dealer_hand_value))
        print("Hand 1:")
        print(str(dealer_hand)+" = "+str(dealer_hand_value))  
        print(str(player_hand)+" = "+str(player_hand_value))
        print("Current Count: ",count)
        print("===============================")
        
        
        if dealer_hand_value == 21 and player_hand_value != 21:
            print("Dealer wins!")
            bank_roll-=amount
            player_hand_value,dealer_hand_value,player_hand,dealer_hand,num_of_cards = reset_values(player_hand_value,dealer_hand_value,player_hand,dealer_hand,num_of_cards)
            continue
        elif dealer_hand_value == 21 and player_hand_value == 21:
            print("Push")
            player_hand_value,dealer_hand_value,player_hand,dealer_hand,num_of_cards = reset_values(player_hand_value,dealer_hand_value,player_hand,dealer_hand,num_of_cards)
            continue
        else:
            choice = basic_strategy(player_hand_value, dealer_hand[1], player_hand)  
            #player
            hand_num=1
            while choice != 'stand':
                if choice == 'hit':
                    print("Player will hit.")
                    
                    while player_hand_value < 17:
                        value = get_card(deck_folder,cards_in_use)
                        if value is None:
                            continue
                        else:
                            count += keep_count(value)
                            cards_in_play += 1
                            player_hand.append(value)
                            hand_num += 1
                            player_hand_value += hand_value(value, player_hand_value)
                            print(f"Hand {hand_num}:")
                            print(str(dealer_hand) + " = " + str(dealer_hand_value), flush=True)  
                            print(str(player_hand) + " = " + str(player_hand_value), flush=True)
                            print("Current Count: ",count)
                            print("===============================")
                            
                            choice = basic_strategy(player_hand_value, dealer_hand[1], player_hand) 
                            if choice == 'stand':
                                break
                            else:
                                continue
                #double down
                else:
                    print("Player will double down.")
                    while True:
                        value = get_card(deck_folder,cards_in_use)
                        if value is None:
                            continue
                        else:
                            count+=keep_count(value)
                            cards_in_play+=1
                            player_hand.append(value)
                            hand_num+=1
                            player_hand_value += hand_value(value,player_hand_value)
                            print(f"Hand {hand_num}:",flush=True)
                            print(str(dealer_hand)+" = "+str(dealer_hand_value),flush=True)  
                            print(str(player_hand)+" = "+str(player_hand_value),flush=True)
                            print("Current Count: ",count)
                            print("===============================")
                            
                            choice='stand'
                            break

            print("Player will Stand")
            if player_hand_value > 21:
                print("Dealer Wins")
                bank_roll-=amount
                player_hand_value,dealer_hand_value,player_hand,dealer_hand,num_of_cards = reset_values(player_hand_value,dealer_hand_value,player_hand,dealer_hand,num_of_cards)
                continue
            else:
                while dealer_hand_value < 17:
                    value = get_card(deck_folder,cards_in_use)
                    if value is None:
                        continue
                    else:
                        count+=keep_count(value)
                        cards_in_play+=1
                        dealer_hand.append(value)
                        dealer_hand_value += hand_value(value,dealer_hand_value)
                        hand_num+=1
                        print(f"Hand {hand_num}:")
                        print(str(dealer_hand)+" = "+str(dealer_hand_value))  
                        print(str(player_hand)+" = "+str(player_hand_value))
                        print("Current Count: ",count)
                        print("===============================")

                if player_hand_value > 21 or dealer_hand_value > player_hand_value:
                    if dealer_hand_value > 21 and player_hand_value <= 21:
                        print("Player Wins")
                        bank_roll+=amount
                    else:
                        print("Dealer wins")
                        bank_roll-=amount
                    player_hand_value,dealer_hand_value,player_hand,dealer_hand,num_of_cards = reset_values(player_hand_value,dealer_hand_value,player_hand,dealer_hand,num_of_cards)
                    continue
                elif dealer_hand_value > 21 or dealer_hand_value < player_hand_value:
                    print("Player wins")
                    bank_roll+=amount
                    player_hand_value,dealer_hand_value,player_hand,dealer_hand,num_of_cards = reset_values(player_hand_value,dealer_hand_value,player_hand,dealer_hand,num_of_cards)
                    continue
                else:
                    print("Push")
                    player_hand_value,dealer_hand_value,player_hand,dealer_hand,num_of_cards = reset_values(player_hand_value,dealer_hand_value,player_hand,dealer_hand,num_of_cards)
                    continue
                    
    profit = bank_roll - 5000.0
    if profit > 0:
        profit_float = "{:.2f}".format(profit)
        print(f'\nYou have made ${profit}')
    else:
        profit*=-1
        profit_float = "{:.2f}".format(profit)
        print(f'\nYou have lost ${profit}')