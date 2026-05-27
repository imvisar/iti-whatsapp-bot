from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

print("🔥 ITI BOT RUNNING 🔥")

# ================= HOME =================
@app.route("/")
def home():
    return "BOT RUNNING"

# ================= MAIN MENU =================
main_menu = """🎓 *ITI JAFRABAD ADMISSION BOT*

👨‍💻 Developed by Imran Visar (S.I COPA)

━━━━━━━━━━━━━━━━━━

📌 Option પસંદ કરો:

1️⃣ 📘 ITI એટલે શું?
2️⃣ 📝 Admission Process 
3️⃣ 📂 Documents Required  
4️⃣ 🎁 ITI માટે સરકાર યોજનાઓ   
5️⃣ 🚀 ITI પછી future  
6️⃣ 🏫 ITI Jafrabad માં Admission  

━━━━━━━━━━━━━━━━━━

👉 નંબર મોકલો (1-6)
"""

# ================= ANSWERS =================
def get_answer(choice):

    if choice == "1":
        return """📘 *ITI એટલે શું?*

ITI (Industrial Training Institute) એ Government training institute છે.

📚 ITI માં 1 વર્ષ અને 2 વર્ષ ના વિવિધ વ્યવસાયલક્ષી  કોર્સ ચાલે છે.

🔧 અહીં practical તાલીમ પર ખાસ ધ્યાન આપવામાં આવે છે.

🏭 Training દરમિયાન:
- On Job Training  
- Dual Training System દ્વારા Industry માં training  

🎯 ITI નો મુખ્ય ઉદ્દેશ:
Skill development અને job ready બનાવવું  
"""

    elif choice == "2":
        return """📝 *Admission Process*

🌐 Website:
https://itiadmission.gujarat.gov.in/

📌 Steps:

1️⃣ Website open કરો  
2️⃣ Registration કરો  
3️⃣ Login કરી Form Fill કરો  
4️⃣ સરકારી ITI ખાતે ફોર્મ verify કરાવો  
5️⃣ ₹50 fee ભરો  
6️⃣ Trade પસંદ કરો  
"""

    elif choice == "3":
        return """📂 *Documents Required*

- 10th Marksheet(૧૦ નાપાસ માટે ૮/૯ Marksheet)  
- LC  
- Aadhar Card  
- Photo
- જાતિનો દાખલો (લાગુ પડતા માટે) 

📌 Original documents verify માટે જરૂરી છે  
"""

    elif choice == "4":
        return """🎁 *ITI ના લાભ*

🚌 તમામ તાલીમાર્થીઓને FREE Bus Pass  

👩 Girls Scholarship:
➡️ 1 વર્ષ → ₹15,000  
➡️ 2 વર્ષ → ₹24,000  

♿ Divyang:
➡️ ₹3000/month સહાય  

🛡️ Accident Insurance:
➡️ ₹4,00,000 cover  

🏆 Skill Competition prizes  
"""

    elif choice == "5":
        return """🚀 *ITI પછી Future*

💼industries માં Job Opportunities વધે છે  

🏭 Apprenticeship કરી શકો  

🏢 Placement મેળા દ્વારા સરળતાથી job  

🌍 NCVT પ્રમાણપત્રથી foreign job chance  

🛠️ Self business પણ કરી શકો  
"""

    elif choice == "6":
        return """🏫 *ITI JAFRABAD ADMISSION*

Admission લેવા માંગો છો? 👇

📲 WhatsApp Group:
https://chat.whatsapp.com/HeQQHuayjX5EOXapt1ea6t

📌 અહીં મળશે:
✔️ Guidance  
✔️ Form help  
✔️ Trade selection  

👉 આજે જ join કરો 🚀
"""

    else:
        return "❌ કૃપા કરીને 1 થી 6 માંથી option પસંદ કરો"

# ================= WHATSAPP ROUTE =================
@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():

    msg = request.form.get("Body", "").strip().lower()
    print("📩 Message:", msg)

    resp = MessagingResponse()

    if msg in ["hi", "hello", "menu"]:
        resp.message(main_menu)
    else:
        resp.message(get_answer(msg))

    return str(resp)

# ================= RUN =================
if __name__ == "__main__":
    app.run()
