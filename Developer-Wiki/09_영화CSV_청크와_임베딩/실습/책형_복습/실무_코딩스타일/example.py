from request_tools import validate_request

print('정상:', validate_request(10, 2, [10, 20, 30]))
for user_id, top_k in [(99, 2), (10, 0)]:
    try:
        validate_request(user_id, top_k, [10, 20, 30])
    except ValueError as error:
        print(error)
print('원본 사용자 목록:', [10, 20, 30])
