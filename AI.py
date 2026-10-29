import tkinter as go
import requests

print("requst is working")


caf=go.Tk()
caf.title("ROONIE")

caf.geometry("900x600")


welcome=go.Label(caf,text="WELCOME AM YOUR NEW AI",font=("Arial",20))
welcome.pack(pady=40)



chat_box=go.Text(caf,height=20,width=80)
chat_box.pack(pady=20)

message_entry=go.Entry(caf,width=60)
message_entry.pack(pady=10)




def solve_math(message):
    try:
        answer = eval(message)
        return f"The answer is {answer}."
    except:
        return None


def solve_percentage(message):
    message = message.lower()

    if "percent" in message or "%" in message:
        try:
            numbers = [float(word) for word in message.replace("%", " ").split()
                       if word.replace(".", "", 1).isdigit()]

            if len(numbers) >= 2:
                percent = numbers[0]
                number = numbers[1]

                answer = (percent / 100) * number

                return f"{percent}% of {number} is {answer}."

        except:
            pass

    return None


def solve_average(message):
    message = message.lower()

    if "average" in message:
        try:
            numbers = [float(word) for word in message.replace(",", " ").split()
                       if word.replace(".", "", 1).isdigit()]

            if numbers:
                answer = sum(numbers) / len(numbers)

                return f"The average is {answer}."

        except:
            pass

    return None


def solve_rectangle(message):
    message = message.lower()

    if "area" in message and "rectangle" in message:
        try:
            numbers = [float(word) for word in message.replace(",", " ").split()
                       if word.replace(".", "", 1).isdigit()]

            if len(numbers) >= 2:
                length = numbers[0]
                width = numbers[1]

                answer = length * width

                return f"The area of the rectangle is {answer}."

        except:
            pass

    return None


def solve_square(message):
    message = message.lower()

    if "area" in message and "square" in message:
        try:
            numbers = [float(word) for word in message.replace(",", " ").split()
                       if word.replace(".", "", 1).isdigit()]

            if numbers:
                side = numbers[0]

                answer = side * side

                return f"The area of the square is {answer}."

        except:
            pass

    return None






def solve_triangle(message):
    message = message.lower()

    if "area" in message and "triangle" in message:
        try:
            numbers = [float(word) for word in message.replace(",", " ").split()
                       if word.replace(".", "", 1).isdigit()]

            if len(numbers) >= 2:
                base = numbers[0]
                height = numbers[1]

                answer = (base * height) / 2

                return f"The area of the triangle is {answer}."

        except:
            pass

    return None




def solve_equation(message):
    message = message.lower().replace(" ", "")

    if "=" not in message or "x" not in message:
        return None

    try:
        left, right = message.split("=")

        number = float(right)

        if "x+" in left:
            value = float(left.split("x+")[1])
            answer = number - value

        elif "x-" in left:
            value = float(left.split("x-")[1])
            answer = number + value

        elif "x*" in left:
            value = float(left.split("x*")[1])
            answer = number / value

        elif "x/" in left:
            value = float(left.split("x/")[1])
            answer = number * value

        else:
            return None

        return f"x = {answer}"

    except:
        return None


def python_helper(message):
    if "what is python" in message.lower():
        return "Python is a programming language that is easy to learn and very powerful."

    elif " variable" in message.lower():
        return "A variable is a name used to store a value."

    elif "function" in message.lower():
        return "A function is a reusable block of code that performs a task."

    else:
        return None







def chat_helper(message):
    if "hello" in message.lower():
        return "Hello master 😎 How are you?"

    elif "how are you" in message.lower():
        return "I'm doing great! let ue get down to it master 🔥"

    elif "who are you" in message.lower():
        return "I'm Roonie , your Python-built AI."

    else:
        return None


def send_message():
    message = message_entry.get()

    if message == "":
        return

    chat_box.insert(go.END, "Perfect: " + message + "\n")

    
    response = solve_math(message)

    
    if response is None:
        response = solve_percentage(message)

    
    if response is None:
        response = solve_average(message)

    
    if response is None:
        response = solve_rectangle(message)

    
    if response is None:
        response = solve_square(message)

    
    if response is None:
        response = solve_triangle(message)

    
    if response is None:
        response = python_helper(message)

    
    if response is None:
        response = chat_helper(message)


    if response is None:
            response = solve_equation(message)

    
    if response is None:
        response = "I don't understand that yet, but we can teach me!"



 

    chat_box.insert(go.END, "AI: " + response + "\n\n")

    message_entry.delete(0, go.END)
    message_entry.focus()













send_button = go.Button(caf, text="Send", width=10,
                        command=send_message)

send_button.pack()    


















caf.mainloop()