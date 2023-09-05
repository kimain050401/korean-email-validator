# korean-email-validator
이메일 유효성 검증 패키지로, 한국어로 이메일 유효성 검증 결과를 반환합니다.

다양한 측면에서 올바른 이메일인지 검증하고, 일회성 이메일이 아닌 진짜 이메일인지 검증하며, 문제가 있을 경우 유저 친화적인 한국어 문장으로 문제 상황을 반환합니다.

# Get Started
```shell
pip install korean-email-validator
```

# Use Example
```python
import korean_email_validator

print(email_check("user@example.com"))
```

# What is validated
- 문자가 하나 이상 포함되었는가
- @가 포함되었는가
- @가 2개 이상 포함되지 않았는가
- 공백이 포함되지 않았는가
- 마침표(.), 언더바(_), 하이픈(-)을 제외한 특수문자가 포함되지 않았는가
- 마침표(.)가 연속으로 2개 이상 포함되지 않았는가
- [일회성 이메일 도메인](https://github.com/kimain050401/korean-email-validator/blob/main/data/temp_emails.txt)이 포함되지 않았는가
- [올바른 최상위 도메인](https://github.com/kimain050401/korean-email-validator/blob/main/data/tdls.txt)이 아닌 최상위 도메인이 포함되지 않았는가
- 영어가 아닌 다른 언어가 포함되지 않았는가

# License
`korean-email-validator`는 `MIT License`가 적용됩니다.

라이센스에 대한 자세한 내용은 [라이센스](https://github.com/kimain050401/korean-email-validator/blob/main/LICENSE)를 참고해 주세요.
