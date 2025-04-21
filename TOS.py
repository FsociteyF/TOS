import datetime

def تحليل_معرف_TikTok(uid: int):
    # استخراج وقت الإنشاء - Extract creation timestamp
    الطابع_الزمني = uid >> 32
    تاريخ_الإنشاء = datetime.datetime.utcfromtimestamp(الطابع_الزمني)
    الآن = datetime.datetime.utcnow()
    عمر_الحساب = (الآن - تاريخ_الإنشاء).days

    # تصنيف عمر الحساب - Account age classification
    if عمر_الحساب < 30:
        التصنيف = "جديد جداً / Very New"
    elif عمر_الحساب < 180:
        التصنيف = "جديد / New"
    elif عمر_الحساب < 730:
        التصنيف = "متوسط / Medium"
    else:
        التصنيف = "قديم / Old"

    # تخمين المنطقة بناءً على توقيت الإنشاء - Region estimation
    الساعة = تاريخ_الإنشاء.hour
    if 2 <= الساعة <= 8:
        المنطقة = "آسيا / الشرق الأوسط - Asia / Middle East"
    elif 9 <= الساعة <= 14:
        المنطقة = "أوروبا / روسيا - Europe / Russia"
    elif 15 <= الساعة <= 20:
        المنطقة = "أمريكا - Americas"
    else:
        المنطقة = "غير محدد - Unknown"

    # طباعة النتيجة - Print result
    print("معرف المستخدم / User ID:", uid)
    print("تاريخ الإنشاء / Creation Date:", تاريخ_الإنشاء.strftime("%Y-%m-%d %H:%M:%S UTC"))
    print("عمر الحساب بالأيام / Account Age (days):", عمر_الحساب)
    print("تصنيف الحساب / Account Status:", التصنيف)
    print("المنطقة المحتملة / Possible Region:", المنطقة)

# إضافة خيار لإدخال المعرف يدويًا
def main():
    print("أداة تحليل معرف TikTok")
    try:
        معرف = int(input("الرجاء إدخال معرف المستخدم (UID) الخاص بـ TikTok: "))
        تحليل_معرف_TikTok(معرف)
    except ValueError:
        print("يرجى إدخال معرف صحيح (UID) من نوع عدد صحيح.")

if __name__ == "__main__":
    main()
