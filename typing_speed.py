import time 
import random
import lorem
class TypeSpeed:

    def wpm(self,original_s,typed_s,timetaken):
        len_sentence = len(original_s.split())
        time_minute = timetaken/60

        if time_minute == 0:
            return 0
        wpm_ = len_sentence / time_minute
        return round(wpm_)

    
    def cal_accuracy(self,sentence,typed):

        correct = 0
        min_lenthg = min(len(sentence),len(typed))
        for i in range(min_lenthg):
            if sentence[i] == typed[i]:
                correct += 1
        accuracy = (correct/len(sentence)) * 100
        return round(accuracy,2)
    

def test_typing_speed():

    sentence = []

    sentence.append(lorem.sentence()[:500])
    w = TypeSpeed()
    print("\n===== TYPING SPEED TESTER =====")
    print("Instructions:")
    print("1. Jab sentence dikhe, usko exactly type karo.")
    print("2. Enter dabane se timer start hoga, phir type karke Enter dabao.")
    input("Press Enter to start...")
    
    sentence_ = random.choice(sentence)
    print("\n type this sentenc")
    print(sentence_)

    print("\npress enter to start typing")
    start = time.time()
    typing_text = input("\nStart typing here: ")

    end = time.time()

    timetaken = end - start
    wpm_ = w.wpm(sentence_,typing_text,timetaken)
    accuracy_ = w.cal_accuracy(sentence_,typing_text)


    print("\n----- RESULTS -----")
    print(f"Time taken: {timetaken:.2f} seconds")
    print(f"Your speed: {wpm_} words per minute (WPM)")
    print(f"Accuracy: {accuracy_}%")
    
    if accuracy_ < 80:
        print("Tip: Accuracy pe dhyan do, speed baad mein aayegi.")
    elif wpm_ < 30:
        print("Tip: Daily practice karo, speed badhegi.")
    else:

        print("Good job! Keep practicing.")


if __name__ == '__main__':
    test_typing_speed()




