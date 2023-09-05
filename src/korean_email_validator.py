import re

def email_check(email):
    if not email or email == " ":
        return "이메일이 입력되지 않았어요."
    
    if email.find("@") == -1:
        return "이메일에 @가 포함되어 있지 않아요."
    
    if email.count("@") > 1:
        return "이메일에 @는 2개 이상 있을 수 없어요."
    
    if email.find(" ") != -1:
        return "이메일에는 공백을 사용할 수 없어요."

    pattern = re.compile(r'[^\w\s\-_.@]')
    matches = pattern.findall(email)
    if matches:
        for char in matches:
            return "이메일에는 마침표(.), 언더바(_), 하이픈(-)을 제외한 특수문자(" + char + ")를 사용할 수 없어요."
    
    if email.split("@")[1].find("..") != -1:
        return "이메일의 도메인 부분에는 .이 연속으로 2개 이상 있을 수 없어요."
    
    f = open("../data/temp_emails.txt", "r")
    temp_emails = f.read().split("\n")
    f.close()
    if email.split("@")[1] in temp_emails:
        return "일회성 이메일은 사용할 수 없어요."
    
    f = open("../data/tdls.txt", "r")
    tdls = f.read().split("\n")
    f.close()
    pattern = r'\.([^.]+)$'
    match = re.search(pattern, email)
    if match:
        result = match.group(1)
        if "." + result not in tdls:
            return "최상위 도메인(." + result + ")이 올바르지 않아요."

    pattern = re.compile(r'[^\x00-\x7F]+')
    non_english_chars = pattern.findall(email)
    if non_english_chars:
        for char in non_english_chars:
            return "이메일에 영어가 아닌 다른 문자(" + char + ")를 사용할 수 없어요."
    
    return "Valid email"

print(email_check("test@test.com"))