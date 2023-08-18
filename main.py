import re
import long_responses as long

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True


    for word in user_message:
        if word in recognised_words:
            message_certainty += 1
    

    # calculate recognise words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))



def get_response(user_input):
    split_message = re.split(r'\s + |[,;!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


#testing the response system
while True:
    print('Bot: ' + get_response(input('you')))