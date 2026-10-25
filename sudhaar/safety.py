"""Basic phrase-triggered demo routing. Not a clinical or reliable risk classifier."""
from .i18n import t

URGENT_TERMS = [
    "overdose", "can't breathe", "cannot breathe", "difficulty breathing", "not breathing",
    "unconscious", "seizure", "poisoning", "passed out", "won't wake up", "life threatening",
    "ओवरडोज", "सांस नहीं", "बेहोश", "दौरा", "ज़हर", "जहर", "होश नहीं", "सांस नहीं आ रही", "శ్వాస తీసుకోలేను", "மூச்சு விட முடியவில்லை", "ಉಸಿರಾಡಲು ಆಗುತ್ತಿಲ್ಲ", "ശ്വസിക്കാൻ കഴിയുന്നില്ല", "ਸਾਹ ਨਹੀਂ ਆ ਰਿਹਾ", "શ્વાસ નથી", "ଶ୍ୱାସ ନେଇପାରୁନି",
    "শ্বাস নিতে পারছি না", "অজ্ঞান", "খিঁচুনি", "বিষক্রিয়া",
    "மூச்சு விட முடியவில்லை", "மயக்கம்", "வலிப்பு",
    "శ్వాస తీసుకోలేక", "స్పృహ లేకుండా", "श्वास घेता येत नाही", "बेशुद्ध", "झटके"
]
SELF_HARM_TERMS = [
    "suicid", "kill myself", "end my life", "self-harm", "hurt myself",
    "आत्महत्या", "खुद को मार", "खुद को नुकसान", "जीना नहीं चाहता", "जीना नहीं चाहती", "خودکشی", "ਆਤਮਹੱਤਿਆ", "ಆತ್ಮಹತ್ಯೆ", "ആത്മഹത്യ", "આપઘાત", "ଆତ୍ମହତ୍ୟା", "আত্মহত্যা",
    "আত্মহত্যা", "নিজেকে আঘাত", "বাঁচতে চাই না",
    "தற்கொலை", "என்னை காயப்படுத்த", "வாழ விரும்பவில்லை",
    "ఆత్మహత్య", "నన్ను నేను హాని", "బతకాలని లేదు",
    "स्वतःला इजा", "जगायचे नाही"
]

def detect_risk(message: str):
    """Return urgent/self_harm for selected phrases; this can miss risks or over-trigger."""
    text = (message or "").casefold()
    if any(term in text for term in URGENT_TERMS):
        return "urgent"
    if any(term in text for term in SELF_HARM_TERMS):
        return "self_harm"
    return None

def safety_copy(kind: str, lang: str = "en"):
    if kind == "urgent":
        return {
            "title": t("urgent_title", lang),
            "body": t("urgent_body", lang),
            "main": t("safety_banner", lang),
            "contacts": [
                {"name": "112 — Emergency response", "url": "https://112.gov.in/"},
                {"name": "14416 — Tele-MANAS mental-health support", "url": "https://telemanas.mohfw.gov.in/"},
                {"name": "14446 — National De-addiction Helpline", "url": "https://socialjustice.gov.in/schemes/42"},
            ],
        }
    return {
        "title": t("mental_title", lang),
        "body": t("mental_body", lang),
        "main": t("mental_body", lang),
        "contacts": [
            {"name": "112 — Emergency response if danger is immediate", "url": "https://112.gov.in/"},
            {"name": "14416 — Tele-MANAS", "url": "https://telemanas.mohfw.gov.in/"},
            {"name": "14446 — National De-addiction Helpline", "url": "https://socialjustice.gov.in/schemes/42"},
        ],
    }
