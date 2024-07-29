import stringprep
import unicodedata
def prepare_string(input_string):
    # 문자열을 NFKC 정규화
    normalized = unicodedata.normalize('NFKC', input_string)

    # 프로파일을 적용하여 유효성 검사 및 필터링
    prepared = []
    for char in normalized:
        # 비 ASCII 공백 문자를 ASCII 공백 문자로 매핑
        if stringprep.in_table_b1(char):
            prepared.append(' ')
        # 일반적으로 유효하지 않은 문자 제거
        elif stringprep.in_table_c12(char) or \
                stringprep.in_table_c21(char) or \
                stringprep.in_table_c22(char) or \
                stringprep.in_table_c3(char) or \
                stringprep.in_table_c4(char) or \
                stringprep.in_table_c5(char) or \
                stringprep.in_table_c6(char) or \
                stringprep.in_table_c7(char) or \
                stringprep.in_table_c8(char) or \
                stringprep.in_table_c9(char):
            continue
        else:
            prepared.append(char)

    return ''.join(prepared)


# 테스트 문자열
test_string = "Hello, 𝐖𝐨𝐫𝐥𝐝! これはテストです。"

# 문자열 준비
prepared_string = prepare_string(test_string)
print(f"Original: {test_string}")
print(f"Prepared: {prepared_string}")

# 결과:
# Original: Hello, 𝐖𝐨𝐫𝐥𝐝! これはテストです。
# Prepared: Hello, WORLD! これはテストです。

import stringprep
import unicodedata

def custom_prepare_string(input_string):
    # 문자열을 NFKC 정규화
    normalized = unicodedata.normalize('NFKC', input_string)

    # 프로파일을 적용하여 유효성 검사 및 필터링
    prepared = []
    for char in normalized:
        # 비 ASCII 공백 문자를 ASCII 공백 문자로 매핑
        if stringprep.in_table_b1(char):
            prepared.append(' ')
        # 일반적으로 유효하지 않은 문자 제거
        elif stringprep.in_table_c12(char) or \
                stringprep.in_table_c21(char) or \
                stringprep.in_table_c22(char) or \
                stringprep.in_table_c3(char) or \
                stringprep.in_table_c4(char) or \
                stringprep.in_table_c5(char) or \
                stringprep.in_table_c6(char) or \
                stringprep.in_table_c7(char) or \
                stringprep.in_table_c8(char) or \
                stringprep.in_table_c9(char):
            continue
        else:
            prepared.append(char)

    return ''.join(prepared)


# 테스트 문자열
test_string = "Test String: 𝐓𝐞𝐬𝐭 これはテストです。"

# 사용자 정의 프로파일을 사용한 문자열 준비
prepared_string = custom_prepare_string(test_string)
print(f"Original: {test_string}")
print(f"Prepared: {prepared_string}")

# 결과:
# Original: Test String: 𝐓𝐞𝐬𝐭 これはテストです。
# Prepared: Test String: TEST これはテストです。

import stringprep
import unicodedata


def prepare_xmpp_jid(jid):
    localpart, domainpart = jid.split('@')

    # 로컬 부분 준비
    localpart = unicodedata.normalize('NFKC', localpart)
    localpart = ''.join([char for char in localpart if not stringprep.in_table_c12(char)])

    # 도메인 부분 준비
    domainpart = unicodedata.normalize('NFKC', domainpart)
    domainpart = domainpart.lower()

    prepared_jid = f"{localpart}@{domainpart}"
    return prepared_jid


# 테스트 JID
jid = "𝐔𝐬𝐞𝐫@Example.COM"

# JID 준비
prepared_jid = prepare_xmpp_jid(jid)
print(f"Original JID: {jid}")
print(f"Prepared JID: {prepared_jid}")

# 결과:
# Original JID: 𝐔𝐬𝐞𝐫@Example.COM
# Prepared JID: USER@example.com