from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

print("🔥 ITI BOT RUNNING 🔥")

# ================= HOME =================
@app.route("/")
def home():
    return "BOT RUNNING"

# ================= MAIN MENU =================
main_menu = """🎓 ITI Admission Assistant

1️⃣ ITI એટલે શું?
2️⃣ Admission Process
3️⃣ Documents Required
4️⃣ ITI લાભ
5️⃣ ITI પછી Future
"""

# ================= ANSWERS =================
def get_answer(choice):

    if choice == "1":
        return "ITI એ Government training institute છે."

    elif choice == "2":
        return "Website: https://itiadmission.gujarat.gov.in/"

    elif choice == "3":
        return "10th marksheet, LC, Aadhar, Photo"

    elif choice == "4":
        return "FREE Bus Pass, Scholarship, Divyang sahay"

    elif choice == "5":
        return "Job, Apprenticeship, Placement"

    else:
        return "Please select valid option"

# ================= WHATSAPP ROUTE =================
@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():

    msg = request.form.get("Body", "").strip().lower()
    print("📩 Message:", msg)

    if msg in ["hi", "hello"]:
        reply = main_menu
    else:
        reply = get_answer(msg)

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>
<Message>{reply}</Message>
</Response>""", 200, {'Content-Type': 'application/xml'}

# ================= RUN =================
if __name__ == "__main__":
    app.run()
