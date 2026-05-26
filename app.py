from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

print("🔥 ITI BOT RUNNING 🔥")

# ================= MAIN MENU =================
main_menu = """🎓 *ITI Admission Assistant*
👨‍💻 Developed by Imran Visar (S.I COPA ITI Jafarabad)

📌 Option select karo:

1️⃣ 📘 ITI એટલે શું?
2️⃣ 📝 Admission Process 
3️⃣ 📂 ITI Admission ક્યાં ડોક્યુમેન્ટ જોઈએ ?
4️⃣ 🎁 ITI માં મળતા સરકારી લાભ
5️⃣ 🚀 ITI પછી Future
6️⃣ 🏫 ITI Jafrabad ma Admission leva mango chho?
"""

# ================= ANSWERS =================
def get_answer(choice):

    if choice == "1":
        return """📘 *ITI એટલે શું?*

ITI (Industrial Training Institute) એ Government training institute છે.

📚 ITI માં 1 વર્ષ અને 2 વર્ષ ના વિવિધ વ્યાવસાયિક કોર્સ ચાલે છે.

🔧 અહીં practical તાલીમ પર ખાસ ધ્યાન આપવામાં આવે છે.

🏭 ITI માં training દરમિયાન:
- On Job Training નો મોકો મળે છે  
- Dual Training System દ્વારા સીધા Industry માં તાલીમ મળી શકે છે  

🎯 ITI નો મુખ્ય ઉદ્દેશ:
- Skill development  
- વિદ્યાર્થી ને job ready બનાવવો  
"""

    elif choice == "2":
        return """📝 *Admission Process*

🌐 Website:
https://itiadmission.gujarat.gov.in/

📌 Steps:

1️⃣ Website open કરો  
2️⃣ Registration કરો (Mobile OTP)  
3️⃣ Login કરી Form Fill કરો  
4️⃣ Government ITI ખાતે જઈ verify કરાવો  
5️⃣ ₹50 registration fee online ભરો  
6️⃣ Trade પસંદ કરો  
"""

    elif choice == "3":
        return """📂 *Documents Required*

- 10th Marksheet  
- LC (School Leaving Certificate)  
- Aadhar Card  
- Photo  
- Caste Certificate (if applicable)  

📌 ITI verify સમયે original documents લઈ જવા જરૂરી છે  
"""

    elif choice == "4":
        return """🎁 *ITI માં મળતા સરકારી લાભ*

🚌 FREE Bus Pass  
➡️ ITI ના દરેક trainee ને ઘરથી ITI સુધી આવવા માટે ST bus માં FREE pass આપવામાં આવે છે  

👩 Mahila (Girls) Scholarship  
➡️ 1 વર્ષ → ₹15,000  
➡️ 2 વર્ષ → ₹24,000  

♿ Divyang Sahay  
➡️ દર મહિને ₹3000 સહાય મળે છે  

🛡️ Accident Insurance  
➡️ ₹4,00,000 cover મળે છે  

🏆 Skill Competition  
➡️ District → ₹7,000  
➡️ State → ₹25,000  
➡️ National → ₹50,000  
"""

    elif choice == "5":
        return """🚀 *ITI પછી Future Opportunities*

💼 Job Opportunities  
➡️ ITI પછી ઇન્ડસ્ટ્રીઝ માં job chance વધી જાય છે  

🏭 Apprenticeship  
➡️ આ સ્કીલ નો લાભ લઈ Industry માં વધુ training મેળવી શકાય અને સાથે સ્ટાઇપેંડ થો ખરું જ.  

🏢 Placement  
➡️ ITI દ્વારા સમાયંતરે રોજગાર ભરતી મેળાનું આયોજન થતું રહે છે જેથી વિદ્યાર્થીને ITI ખાતેથી જ placement મળી જાય છે  

🌍 Foreign Job  
➡️ NCVT certificate થી foreign(વિદેશ) જવા ઈચ્છુક વિધાર્થીઓને વિદેશ નોકરીના CHANCE વધી જાય છે.  

🛠️ Self Employment  
➡️ આ બધાની  સાથે પોતાનો business શરુ કરવા માંગતા વિધાર્થીઓ માટે કૌશલ્ય થી સ્વરોજગાર તો ખરો જ.    

📚 Higher Study  
➡️ ITI ખાતે ૨ વર્ષના કોર્ષ બાદ 
    ધોરણ ૮ પાસ વિધાર્થી ધોરણ ૧૦ સમકક્ષ અને 
    ધોરણ ૧૦ પાસ વિધાર્થી ધોરણ ૧૨ સમકક્ષ સર્ટીફીકેટ મેળવી શકે છે.
      DIPLOMA માં સીધો ત્રીજા સેમેસ્ટર માં પ્રવેશ મેળવી શકે છે.  
"""

    elif choice == "6":
        return """🏫 *ITI Jafrabad Admission*

જો તમે ITI Jafrabad માં admission લેવા માંગો છો તો નીચે આપેલ WhatsApp group માં જોડાઓ 👇

📲 Group Link:
https://chat.whatsapp.com/HeQQHuayjX5EOXapt1ea6t

⚡ Limited seats છે, જલ્દી join કરો!
"""

    else:
        return "❌ 1 થી 6 માંથી યોગ્ય option પસંદ કરો"


# ================= ROUTE =================
# ================= ROUTE =================
@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():

    msg = request.form.get("Body", "").strip()
    print("📩 Message:", msg)

    resp = MessagingResponse()

    # 🔥 TEST RESPONSE
    resp.message("OK WORKING")

    return str(resp)
<Response>
<Message>{reply}</Message>
</Response>"""

# ================= RUN =================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
